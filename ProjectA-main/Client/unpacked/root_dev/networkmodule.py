###################################################################################################
# Network

import app
import chr
import dbg
import net
import snd

import chr
import chrmgr
import background
import player
import playerSettingModule

import ui
import uiPhaseCurtain

import localeInfo
import uiCommon
import constInfo

class PopupDialog(uiCommon.PopupDialog):

	def __init__(self, isLock = True):
		uiCommon.PopupDialog.__init__(self)

		self.CloseEvent = None
		self.CloseOnIMEReturnEvent = None
		self.isLock = isLock

	def __del__(self):
		ui.ScriptWindow.__del__(self)

	def Open(self, msg, event = 0, buttonName = localeInfo.UI_CANCEL, eventOnIMEReturn = 0):
		uiCommon.PopupDialog.Open(self)

		if self.isLock:
			self.Lock()

		self.CloseEvent = event
		self.CloseOnIMEReturnEvent = eventOnIMEReturn

		self.SetButtonName(buttonName)
		self.SetAcceptEvent(ui.__mem_func__(self.Close))

		self.SetText(msg)

	def Close(self):
		if not self.IsShow():
			self.CloseEvent = None
			return

		if self.isLock:
			self.Unlock()

		if self.CloseEvent:
			self.CloseEvent()
			self.CloseEvent = None
		
		uiCommon.PopupDialog.Close(self)

	def OnIMEReturn(self):
		self.Close()

		if self.CloseOnIMEReturnEvent:
			self.CloseOnIMEReturnEvent()
			self.CloseOnIMEReturnEvent = None

		return True

##
## Main Stream
##
class MainStream(object):
	isChrData=0	

	def __init__(self):
		print "NEWMAIN STREAM ----------------------------------------------------------------------------"
		net.SetHandler(self)
		net.SetTCPRecvBufferSize(1024*1024)
		net.SetTCPSendBufferSize(1024*1024)
		net.SetUDPRecvBufferSize(4096)

		self.id=""
		self.pwd=""
		self.addr=""
		self.port=0
		self.account_addr=0
		self.account_port=0
		self.slot=0
		self.isAutoSelect=0
		self.isAutoLogin=0

		self.curtain = 0
		self.curPhaseWindow = 0
		self.newPhaseWindow = 0

	def __del__(self):
		print "---------------------------------------------------------------------------- DELETE MAIN STREAM "

	def Destroy(self):
		if self.curPhaseWindow:
			self.curPhaseWindow.Close()
			self.curPhaseWindow = 0

		if self.newPhaseWindow:
			self.newPhaseWindow.Close()
			self.newPhaseWindow = 0

		self.popupWindow.Destroy()
		self.popupWindow = 0

		self.curtain = 0

	def Create(self):
		self.CreatePopupDialog()

		self.curtain = uiPhaseCurtain.PhaseCurtain()

	def SetPhaseWindow(self, newPhaseWindow):
		if self.newPhaseWindow:
			#print "�̹� ���ο� ������� �ٲۻ��¿��� �� �ٲ�", newPhaseWindow
			self.__ChangePhaseWindow()

		self.newPhaseWindow=newPhaseWindow

		if self.curPhaseWindow:
			#print "���̵� �ƿ�Ǹ� �ٲ�"
			self.curtain.FadeOut(self.__ChangePhaseWindow)
		else:
			#print "���� �����찡 ���� ���¶� �ٷ� �ٲ�"
			self.__ChangePhaseWindow()

	def __ChangePhaseWindow(self):
		oldPhaseWindow=self.curPhaseWindow
		newPhaseWindow=self.newPhaseWindow
		self.curPhaseWindow=0
		self.newPhaseWindow=0

		if test_server:
			#dbg.LogBox("total window obj count: "+ str(constInfo.WINDOW_TOTAL_OBJ_COUNT))
			import game, gc, os
			if isinstance(newPhaseWindow, game.GameWindow):
				constInfo.WINDOW_COUNT_OBJ = False
				# if oldPhaseWindow:
					# oldPhaseWindow.Close()
				# del oldPhaseWindow
				gc.collect()
				constInfo.WINDOW_COUNT_OBJ = True

			elif isinstance(oldPhaseWindow, game.GameWindow):
				constInfo.WINDOW_COUNT_OBJ = True
				# if oldPhaseWindow:
					# oldPhaseWindow.Close()
				# del oldPhaseWindow
				gc.collect()
				constInfo.WINDOW_COUNT_OBJ = False
				if constInfo.WINDOW_OBJ_COUNT > 3:
					dbg.LogBox("!ATTENTION! WINDOW_MEMORY_LEAK DETECTED\n LEAKING WINDOW COUNT: "+ str(constInfo.WINDOW_OBJ_COUNT))
					if not os.path.isdir("memory_leak"):
						os.mkdir("memory_leak")
					leakReport = 0
					while os.path.isfile("memory_leak/window_memory_leak%i.txt" % leakReport):
						leakReport += 1
					opFile = open("memory_leak\\\\window_memory_leak%i.txt"%leakReport, "w+")
					opRootFile = open("memory_leak\\\\window_memory_leak_root%i.txt"%leakReport, "w+")
					for i, v in constInfo.WINDOW_OBJ_LIST.iteritems():
						opFile.write(v.typeStr + " parent type: " + v.strParent + "\n")
						for j in v.traceBack:
							opFile.write("\t" + j + "\n")
						"""for j in gc.garbage:
							if id(j) == i:
								for k in gc.get_referrers(j)[1:]:
									opFile.write("\t\treferences in " + str(k) + "\n")
						if v.strParent.find("ui.") < 0:
							opRootFile.write("\t" + v.strParent + "\n")"""
						if v.strParent == "":
							opRootFile.write(v.typeStr + "\n")
					opRootFile.flush()
					opRootFile.close()
					opFile.flush()
					opFile.close()

		if oldPhaseWindow:
			oldPhaseWindow.Close()

		if newPhaseWindow:
			newPhaseWindow.Open()

		self.curPhaseWindow=newPhaseWindow
	
		if self.curPhaseWindow:
			self.curtain.FadeIn()
		else:
			app.Exit()

	def CreatePopupDialog(self):
		self.popupWindow = PopupDialog()
		self.popupWindow.Hide()


	## SelectPhase
	##########################################################################################	
	def SetLoginPhase(self):
		net.Disconnect()

		import introLogin
		if test_server:
			constInfo.WINDOW_COUNT_OBJ = False
		self.SetPhaseWindow(introLogin.LoginWindow(self))

	def SetSelectEmpirePhase(self):
		try:
			import introEmpire	
			self.SetPhaseWindow(introEmpire.SelectEmpireWindow(self))
		except:
			import exception
			exception.Abort("networkModule.SetSelectEmpirePhase")


	def SetReselectEmpirePhase(self):
		try:
			import introEmpire
			# self.SetPhaseWindow(introEmpire.SelectEmpireWindow(self))
			self.SetPhaseWindow(introEmpire.ReselectEmpireWindow(self))
		except:
			import exception
			exception.Abort("networkModule.SetReselectEmpirePhase")

	def SetSelectCharacterPhase(self):
		try:
			localeInfo.LoadLocaleData()
			import new_introSelect
			self.popupWindow.Close()
			self.SetPhaseWindow(new_introSelect.SelectCharacterWindow(self))
		except:
			import exception
			exception.Abort("networkModule.SetSelectCharacterPhase")

	def SetCreateCharacterPhase(self):
		try:
			import new_introCreate
			self.SetPhaseWindow(new_introCreate.CreateCharacterWindow(self))
		except:
			import exception
			exception.Abort("networkModule.SetCreateCharacterPhase")

	def SetTestGamePhase(self, x, y):
		try:
			import introLoading
			loadingPhaseWindow=introLoading.LoadingWindow(self)
			loadingPhaseWindow.LoadData(x, y)
			self.SetPhaseWindow(loadingPhaseWindow)
		except:
			import exception
			exception.Abort("networkModule.SetLoadingPhase")



	def SetLoadingPhase(self):
		try:
			import introLoading
			self.SetPhaseWindow(introLoading.LoadingWindow(self))
		except:
			import exception
			exception.Abort("networkModule.SetLoadingPhase")

	def SetGamePhase(self):
		try:
			import game
			self.popupWindow.Close()
			if test_server:
				constInfo.WINDOW_COUNT_OBJ = True
				constInfo.WINDOW_OBJ_COUNT = 0
				constInfo.WINDOW_OBJ_LIST = {}
			self.SetPhaseWindow(game.GameWindow(self))
		except:
			import dbg
			dbg.TraceError("networkModule.SetGamePhase")
			raise
			import exception
			exception.Abort("networkModule.SetGamePhase")

	################################
	# Functions used in python

	## Login
	def Connect(self):		
		import constInfo
		if constInfo.KEEP_ACCOUNT_CONNETION_ENABLE:
			net.ConnectToAccountServer(self.addr, self.port, self.account_addr, self.account_port)
		else:
			net.ConnectTCP(self.addr, self.port)

		#net.ConnectUDP(IP, Port)

	def SetConnectInfo(self, addr, port, account_addr=0, account_port=0):
		self.addr = addr
		self.port = port
		self.account_addr = account_addr
		self.account_port = account_port

	def GetConnectAddr(self):
		return self.addr

	def SetLoginInfo(self, id, pwd):
		self.id = id
		self.pwd = pwd
		net.SetLoginInfo(id, pwd)

	def CancelEnterGame(self):
		pass

	## Select
	def SetCharacterSlot(self, slot):
		self.slot=slot

	def GetCharacterSlot(self):
		return self.slot

	## Empty
	def EmptyFunction(self):
		pass
