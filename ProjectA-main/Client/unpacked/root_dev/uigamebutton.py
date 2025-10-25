import app
import ui
import player
import net
import constInfo
import uiToolTip
import localeInfo
import uiCommon
import cfg

"""
class ChatColorMenu(ui.ImageBox):

	PREMIUM_CHAT_COLORS = [
		ui.GenerateColor(121, 219, 133), # GREEN
		ui.GenerateColor(101, 144, 198), # BLUE
		ui.GenerateColor(173, 198, 101), # YELLOW
		ui.GenerateColor(141, 79, 185),  # PURPLE
		ui.GenerateColor(0, 0, 0),		 # BLACK
	]

	def __init__(self):
		ui.ImageBox.__init__(self)
		self.is_loaded = False

	def __del__(self):
		ui.ImageBox.__del__(self)

	def Destroy(self):
		pass

	def __LoadWindow(self):
		self.LoadImage("d:/ymir work/ui/chat/color_bg.tga")

		self.bars = []
		y_start = 8
		for i in xrange(len(self.PREMIUM_CHAT_COLORS)):
			bar = ui.Bar()
			bar.SetParent(self)
			bar.SetSize(30, 16)
			bar.SetColor(self.PREMIUM_CHAT_COLORS[i])
			bar.SetPosition(6, y_start)
			bar.Hide()
			bar.OnMouseLeftButtonDown = lambda arg=i: self.OnMouseLeftButtonDown(arg)

			self.bars.append(bar)
			y_start += 21
		
		self.is_loaded = True

	def Open(self):
		if not self.is_loaded:
			self.__LoadWindow()

		self.Show()
		for bar in self.bars:
			bar.Show()

	def Close(self):
		self.Hide()

	def OnMouseLeftButtonDown(self, key=-1):
		if key not in range(len(self.PREMIUM_CHAT_COLORS)):
			return

		net.SendChatPacket("/premium_color {}".format(key))
		tchat("SendChatPacket: /premium_color {}".format(key))

		self.Close()
"""

class GameButtonWindow(ui.ScriptWindow):
	def __init__(self):
		ui.ScriptWindow.__init__(self)
		self.__LoadWindow("UIScript/gamewindow.py")
		self.wndShopSellNotification = None
		self.PopupNotification = None

	def __del__(self):
		ui.ScriptWindow.__del__(self)

	def __LoadWindow(self, filename):
		try:
			pyScrLoader = ui.PythonScriptLoader()
			pyScrLoader.LoadScriptFile(self, filename)
		except Exception, msg:
			import dbg
			dbg.TraceError("GameButtonWindow.LoadScript - %s" % (msg))
			app.Abort()
			return False

		try:
			self.gameButtonDict={
				"STATUS" : self.GetChild("StatusPlusButton"),
				"SKILL" : self.GetChild("SkillPlusButton"),
				"QUEST" : self.GetChild("QuestButton"),
				"HELP" : self.GetChild("HelpButton"),
				"BUILD" : self.GetChild("BuildGuildBuilding"),
				"EXIT_OBSERVER" : self.GetChild("ExitObserver"),
				#"CHATCOLOR" : self.GetChild("ChatColorButton"),
				"SOLD_ITEM" : self.GetChild("SoldItemButton"),
			}

			self.gameButtonDict["EXIT_OBSERVER"].SetEvent(ui.__mem_func__(self.__OnClickExitObserver))
			#self.gameButtonDict["CHATCOLOR"].SetEvent(ui.__mem_func__(self.__OnClickChatColor))
			self.gameButtonDict["SOLD_ITEM"].SetEvent(ui.__mem_func__(self.__OnSoldItemClick))

		except Exception, msg:
			import dbg
			dbg.TraceError("GameButtonWindow.LoadScript - %s" % (msg))
			app.Abort()
			return False

		self.__HideAllGameButton()
		self.SetObserverMode(player.IsObserverMode())

		#chatColorMenu = ChatColorMenu()
		#chatColorMenu.SetParent(self)
		#chatColorMenu.Close()
		#self.chatColorMenu = chatColorMenu

		#if not self.__IsPremium():
		#	premiumToolTip = uiToolTip.ToolTip()
		#	premiumToolTip.HideToolTip()
		#	premiumToolTip.AppendDescription(localeInfo.CHAT_COLOR_PREMIUM_INFO, 26)
		#	self.gameButtonDict["CHATCOLOR"].SetToolTipWindow(premiumToolTip)

		return True

	def Destroy(self):
		for key in self.gameButtonDict:
			self.gameButtonDict[key].SetEvent(0)

		self.gameButtonDict={}

	def SetButtonEvent(self, name, event):
		try:
			self.gameButtonDict[name].SetEvent(event)
		except Exception, msg:
			print "GameButtonWindow.LoadScript - %s" % (msg)
			app.Abort()
			return

	def ShowBuildButton(self):
		self.gameButtonDict["BUILD"].Show()

	def HideBuildButton(self):
		self.gameButtonDict["BUILD"].Hide()

	#def ShowChatColorButton(self):
	#	ccbutton = self.gameButtonDict["CHATCOLOR"]
	#	ccbutton.Show()

	#	if self.__IsPremium():
	#		ccbutton.Enable()
	#	else:
	#		ccbutton.Disable()

	#def __IsPremium(self):
	#	return constInfo.CHATCOLOR_PREMIUM

	#def HideChatColorButton(self):
	#	self.gameButtonDict["CHATCOLOR"].Hide()

	#	if self.chatColorMenu.IsShow():
	#		self.chatColorMenu.Close()

	def CheckGameButton(self):

		if not self.IsShow():
			return

		statusPlusButton=self.gameButtonDict["STATUS"]
		skillPlusButton=self.gameButtonDict["SKILL"]
		helpButton=self.gameButtonDict["HELP"]

		if player.GetStatus(player.STAT) > 0:
			statusPlusButton.Show()
		else:
			statusPlusButton.Hide()

		if self.__IsSkillStat() and player.GetStatus(player.LEVEL) < 103:
			skillPlusButton.Show()
		else:
			skillPlusButton.Hide()

		# if 0 == player.GetPlayTime():
		# 	helpButton.Show()
		# else:
		helpButton.Hide()

	def __IsSkillStat(self):
		if player.GetStatus(player.LEVEL) > 105:
			return False

		if player.GetStatus(player.SKILL_ACTIVE) > 0:
			return True

		return False

	def __OnClickExitObserver(self):
		net.SendChatPacket("/observer_exit")

	#def __OnClickChatColor(self):
	#	if self.chatColorMenu.IsShow():
	#		self.chatColorMenu.Close()
	#	else:
	#		ccbutton = self.gameButtonDict["CHATCOLOR"]
	#		x, y = ccbutton.GetGlobalPosition()
	#
	#		self.chatColorMenu.SetPosition(x - 21 + ccbutton.GetWidth()/2 , y - 116 - 5)
	#		self.chatColorMenu.Open()
	#		self.chatColorMenu.SetTop()

	def ShowSoldItemButton(self, vnum, count, price):
		self.gameButtonDict["SOLD_ITEM"].Show()
		
		if int(cfg.Get(cfg.SAVE_OPTION, "SHOW_SELL_NOTIFICATION", "1")) == 1:
			popup = uiCommon.ShopSellPopup()
			popup.SetStep(0)
			popup.SetItemVnum(vnum, count, price)
			popup.SlideIn()
			self.PopupNotification = popup

	def __OnSoldItemClickAccept(self):
		if self.wndShopSellNotification:
			self.wndShopSellNotification.Close()
		self.__OnSoldItemClick()

	def __OnSoldItemClick(self):
		if len(constInfo.SOLD_ITEMS_QUEUE) == 0:
			self.gameButtonDict["SOLD_ITEM"].Hide()
			return

		sold_item = constInfo.SOLD_ITEMS_QUEUE.pop(0)
		vnum = sold_item[0]
		count = sold_item[1]
		price = sold_item[2]
		wndShopSellNotification = uiCommon.ShopSellNotification()
		wndShopSellNotification.SetData(vnum, count, price)
		wndShopSellNotification.Open()
		wndShopSellNotification.SetAcceptEvent(self.__OnSoldItemClickAccept)
		self.wndShopSellNotification = wndShopSellNotification

	def __HideAllGameButton(self):
		for btn in self.gameButtonDict.values():
			btn.Hide()

	def SetObserverMode(self, isEnable):
		if isEnable:
			self.gameButtonDict["EXIT_OBSERVER"].Show()
		else:
			self.gameButtonDict["EXIT_OBSERVER"].Hide()

	#def OnUpdate(self):
	#	ccbutton = self.gameButtonDict["CHATCOLOR"]
	#	if ccbutton.IsIn():
	#		ccbutton.ShowToolTip()
	#	else:
	#		ccbutton.HideToolTip()
