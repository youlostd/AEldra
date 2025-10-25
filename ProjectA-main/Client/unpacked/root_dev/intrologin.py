import dbg
import app
import net
import ui
import ime
import snd
import wndMgr
import musicInfo
import systemSetting
import localeInfo
import constInfo
import uiCommon
import time
import uiScriptLocale
import os
import cfg
import accmgr

app.SetGuildMarkPath("test")

class DropBox(ui.Window):
	def __init__(self, layer = "UI"):
		ui.Window.__init__(self, layer)
		self.isDrop = False
		(self.base_x, self.base_y) = (0,0)
		self.baseImg = ui.ExpandedImageBox()
		self.baseImg.SetParent(self)
		self.baseImg.SetPosition(0, 0)
		self.baseImg.Show()
		self.baseImg.label = ui.TextLine()
		self.baseImg.label.SetParent(self.baseImg)
		self.baseImg.label.SetText("")
		self.baseImg.label.SetPosition(0,0)
		self.baseImg.label.Show()
		self.baseImg.SetEvent(self.__Click, "mouse_click", self.baseImg)
		self.baseImg.label.SetFontName("Tahoma:16")

		self.dropList = []
		self.dropImage = ""
		self.labelStart = (0,0)

		self.selectEvent = None
		if constInfo.switchbotSave:
			constInfo.switchbotSave.Destroy()
			constInfo.switchbotSave = None


	def __del__(self):
		ui.Window.__del__(self)

	def __Click(self, event, obj):
		self.isDrop = not self.isDrop
		if obj.label.GetText() != self.baseImg.label.GetText():
			self.SetBaseLabel(obj.label.GetText())
			if self.selectEvent:
				self.selectEvent()
		self.Arrange()
		self.UpdateArrowImage()

	def UpdateArrowImage(self):
		if __SERVER__ == 2:
			self.baseImg.arrow.LoadImage("d:/ymir work/ui/game/intro/login_s2/language_arrow{}.tga".format("_down" if self.isDrop else "_up"))
		else:
			self.baseImg.arrow.LoadImage("d:/ymir work/ui/intro/login/new/language_arrow{}.tga".format("_2" if self.isDrop else ""))

	def SetSelectEvent(self, event):
		self.selectEvent = event

	def SetLabelStart(self, x, y):
		self.labelStart = (x,y)
		for i in self.dropList:
			i.label.SetPosition(x,y)

	def SetBaseLabelStart(self, x, y):
		self.baseImg.label.SetPosition(x,y+1) # baseImg image is bit higher
	

	def SetBaseImage(self, img):
		self.baseImg.LoadImage(img)

		aImg = ui.ExpandedImageBox()
		aImg.AddFlag("not_pick")
		aImg.SetParent(self.baseImg)
		if __SERVER__ == 2:
			aImg.LoadImage("d:/ymir work/ui/game/intro/login_s2/language_arrow_up.tga")
		else:
			aImg.LoadImage("d:/ymir work/ui/intro/login/new/language_arrow.tga")
		aImg.SetPosition(7, self.baseImg.GetHeight() / 2 - aImg.GetHeight() / 2)
		aImg.Show()
		self.baseImg.arrow = aImg

		self.Arrange()

	def SetBaseLabel(self, label = ""):
		self.baseImg.label.SetText(label)


	def GetCurrent(self):
		return self.baseImg.label.GetText()

	def SetDropImage(self, img):
		self.dropImage = img
		for i in self.dropList:
			i.LoadImage(img)
		self.Arrange()

	def AppendDropItem(self, label = ""):
		img = ui.ExpandedImageBox()
		img.SetParent(self)
		img.SetEvent(self.__Click, "mouse_click", img)
		if self.dropImage:
			img.LoadImage(self.dropImage)
		img.Hide()

		lbl = ui.TextLine()
		lbl.SetParent(img)
		lbl.SetPosition(self.labelStart[0], self.labelStart[1])
		lbl.SetFontName("Tahoma:16")
		lbl.SetText(label)
		lbl.Show()
		img.label = lbl

		self.dropList.append(img)
		self.Arrange()

	def Arrange(self):
		if 	(self.base_x, self.base_y) == (0, 0):
			(self.base_x, self.base_y) = self.GetLocalPosition()
		if not self.isDrop:
			for i in self.dropList:
				i.Hide()
			self.SetSize(self.baseImg.GetWidth(), self.baseImg.GetHeight())
			if __SERVER__ == 2:
				self.SetPosition(self.base_x, self.base_y)
				self.baseImg.SetPosition(0, 0)
		else:
			curr = self.baseImg.GetHeight()
			maxWidth = self.baseImg.GetWidth()
			for i in self.dropList:
				if i.label.GetText() == self.baseImg.label.GetText():
					i.Hide()
					continue
				i.SetPosition(0, curr)
				i.Show()
				curr += i.GetHeight()
				maxWidth = max(i.GetWidth(), maxWidth)

			self.SetSize(maxWidth, curr)
			if __SERVER__ == 2:
				self.SetSize(maxWidth, curr+self.baseImg.GetHeight())
				self.SetPosition(self.base_x, self.base_y-len(self.dropList)*self.baseImg.GetHeight())
				self.baseImg.SetPosition(0, curr)
	
class LoginWindow(ui.ScriptWindow):

	if constInfo.RELOGIN_SYSTEM_ENABLED:
		class RelogDialog(ui.ScriptWindow):
			def __init__(self):
				ui.ScriptWindow.__init__(self)
				self.__LoadDialog()

				self.button_text = localeInfo.UI_CANCEL
				self.callbackTimer = 0
				self.waitSeconds = 0

				self.baseMessage = ""

				self.callback = None

			def __del__(self):
				ui.ScriptWindow.__del__(self)

			def __LoadDialog(self):
				try:
					PythonScriptLoader = ui.PythonScriptLoader()
					PythonScriptLoader.LoadScriptFile(self, "UIScript/PopupDialog.py")

					self.board = self.GetChild("board")
					self.message = self.GetChild("message")
					self.acceptButton = self.GetChild("accept")

				except:
					import exception
					exception.Abort("PopupDialog.LoadDialog.BindObject")

			def Open(self, waitTime = 3):
				self.SetCenterPosition()
				self.SetTop()
				self.Show()

				self.callbackTimer = app.GetTime() + waitTime

			def Close(self):
				self.Hide()

			def Destroy(self):
				self.Close()
				self.ClearDictionary()
				ui.ScriptWindow.Destroy(self)

			def SetText(self, text):

				if not self.baseMessage:
					self.baseMessage = text

				self.message.SetText(text)
				self.UpdateHeight()

			def SetClickEvent(self, event):
				self.acceptButton.SetEvent(event)

			def SetButtonName(self, name):
				self.acceptButton.SetText(name)
				self.button_text = name

			def OnPressEscapeKey(self):
				constInfo.RELOGIN_ACCOUNT_INDEX = 0
				constInfo.RELOGIN_TRY_LOGIN = False
				self.Close()
				return True

			def OnIMEReturn(self):
				self.Close()
				return True

			def SetTimeOutCallback(self, callback):
				self.callback = callback

			def OnUpdate(self):
				if self.IsShow():
					current_time = app.GetTime()
					messageToUse = self.baseMessage

					try:
						messageToUse = messageToUse % float(self.callbackTimer - current_time)
					except:
						messageToUse = self.baseMessage

					self.SetText(messageToUse)

					if self.callbackTimer < current_time:
						self.callback()

			def UpdateHeight(self):
				height = self.message.GetRealHeight() + self.message.GetTop() + self.acceptButton.GetTop()
				self.board.SetSize(self.board.GetWidth(), height)
				self.SetSize(self.board.GetRealWidth(), self.board.GetRealHeight())
				self.UpdateRect()
				self.SetCenterPosition()

	langIDToText = {
		app.LANG_ROMANIA : "Română",
		app.LANG_TURKISH : "Türkçe",
		app.LANG_ENGLISH : "English",
		app.LANG_GERMAN : "Deutsch",
		app.LANG_POLISH : "Polski",
		app.LANG_ITALIAN : "Italiano",
		app.LANG_SPANISH : "Español",
		app.LANG_HUNGARIAN : "Hungarian", 
		app.LANG_CZECH : "Čeština",
		app.LANG_PORTUGUESE : "Português",
		app.LANG_FRENCH : "Français",
		app.LANG_ARABIC : "Arabiyyah",
		app.LANG_GREEK : "Greek",
	}

	textToLangID = {
		"Română" : app.LANG_ROMANIA,
		"Türkçe" : app.LANG_TURKISH,
		"English" : app.LANG_ENGLISH,
		"Deutsch" : app.LANG_GERMAN,
		"Polski" : app.LANG_POLISH,
		"Italiano" : app.LANG_ITALIAN,
		"Español" : app.LANG_SPANISH,
		"Hungarian" : app.LANG_HUNGARIAN,
		"Čeština" : app.LANG_CZECH,
		"Português" : app.LANG_PORTUGUESE,
		"Français" : app.LANG_FRENCH,
		"Arabiyyah" : app.LANG_ARABIC,
		"Greek" : app.LANG_GREEK,
	}

	def __init__(self, stream):
		if os.path.isfile("________dev.txt") or os.path.isfile("dev.txt"):
			constInfo.SERVER_INFO = constInfo.TEST_SERVER_INFO
			constInfo.IS_TESTSERVER = True
		ui.ScriptWindow.__init__(self)
		net.SetPhaseWindow(net.PHASE_WINDOW_LOGIN, self)
		net.SetAccountConnectorHandler(self)
		self.channel = 1
		self.username = None
		self.inputDialog = None
		self.languageSelectWnd = None
		self.stream=stream
		# self.pvp_server_enabled = False
		self.pvp_server_selected = False
		self.MAX_ACCS = 8 if __SERVER__ == 2 else 9
		self.lastLoginName = ""
		
		if "whitelist" in constInfo.SERVER_INFO["data"]:
			net.Whitelist(constInfo.SERVER_INFO["data"]["whitelist"][0], constInfo.SERVER_INFO["data"]["whitelist"][1])
			
		for parentDir, dirnames, filenames in os.walk("."):
			for file in filenames:
				if (file.startswith("log") or file.startswith("syserr")) and file.endswith(".txt") or file.endswith(".tlog"):
					try:
						os.remove(file)
					except:
						pass

		# relogin
		if constInfo.RELOGIN_SYSTEM_ENABLED:
			self.relogDialog = self.RelogDialog()
			self.relogDialog.SetText("You will get reconnected to server in %.1f seconds. Use the button below to cancel this action.")
			self.relogDialog.SetClickEvent(self.__OnReloginCancel)
			self.relogDialog.SetTimeOutCallback(self.__OnRelogin)

	def __del__(self):
		net.ClearPhaseWindow(net.PHASE_WINDOW_LOGIN, self)
		net.SetAccountConnectorHandler(0)
		ui.ScriptWindow.__del__(self)

	def Open(self):
		self.loginFailureMsgDict={
			"ALREADY"	: localeInfo.LOGIN_FAILURE_ALREAY,
			"NOID"		: localeInfo.LOGIN_FAILURE_NOT_EXIST_ID,
			"WRONGPWD"	: localeInfo.LOGIN_FAILURE_WRONG_PASSWORD,
			"FULL"		: localeInfo.LOGIN_FAILURE_TOO_MANY_USER,
			"SHUTDOWN"	: localeInfo.LOGIN_FAILURE_SHUTDOWN,
			"BLOCK"		: localeInfo.LOGIN_FAILURE_BLOCK_ID,
			"NOTAVAIL"	: localeInfo.LOGIN_FAILURE_NOT_AVAIL,#
			"BRTFORCE"	: localeInfo.LOGIN_FAILURE_BRUTEFORCE,
			"HWIDBAN"	: localeInfo.LOGIN_FAILURE_BLOCK_HWID,
			"CHCLOSED"	: localeInfo.LOGIN_FAILURE_CHCLOSED,
			"OFFLINE"	: localeInfo.LOGIN_CONNECT_FAILURE,
		}

		self.loginFailureFuncDict = {
			"WRONGPWD"	: self.__DisconnectAndInputPassword,
			"QUIT"		: app.Exit,
		}

		self.SetSize(wndMgr.GetScreenWidth(), wndMgr.GetScreenHeight())
		self.SetWindowName("LoginWindow")

		accmgr.Initialize("details.crypt2")

		if __SERVER__ == 2: 
			fileName = "UIScript/LoginWindow_s2.py" 
		else: 
			fileName = "UIScript/LoginWindow.py"

		if not self.__LoadScript(fileName):
			dbg.TraceError("LoginWindow.Open - __LoadScript Error")
			return
				
		if musicInfo.loginMusic != "":
			snd.SetMusicVolume(systemSetting.GetMusicVolume())
			snd.FadeInMusic("BGM/"+musicInfo.loginMusic)
		snd.SetSoundVolume(systemSetting.GetSoundVolume())
		ime.AddExceptKey(91)
		ime.AddExceptKey(93)

		self.Show()		
		self.__OpenLoginBoard()		
		app.ShowCursor()

		if not app.IsPressed(app.DIK_LCONTROL) and os.path.isfile("login.txt"):
			data = open("login.txt", "rb")
			data = data.readlines()
			self.idEditLine.SetText(data[0])
			self.pwdEditLine.SetText(data[1])
			self.__OnClickLoginButton()
			
		server_info = constInfo.SERVER_INFO
		net.SetMarkServer(server_info["data"]["mark"][0], server_info["data"]["mark"][1])

		if constInfo.RELOGIN_SYSTEM_ENABLED and constInfo.RELOGIN_TRY_LOGIN and constInfo.RELOGIN_ACCOUNT_INDEX != -1:
			self.relogDialog.SetButtonName(localeInfo.UI_CANCEL)
			self.relogDialog.Open()
			constInfo.RELOGIN_LOGIN_WINDOW = True

	def __OnRelogin(self):
		if constInfo.RELOGIN_SYSTEM_ENABLED:
			self.relogDialog.Close()

		if constInfo.RELOGIN_TRY_LOGIN and constInfo.RELOGIN_ACCOUNT_INDEX > 0:
			self.__OnClickAccount(constInfo.RELOGIN_ACCOUNT_INDEX)
		
	def __OnReloginCancel(self):
		if constInfo.RELOGIN_SYSTEM_ENABLED:
			constInfo.RELOGIN_ACCOUNT_INDEX = 0
			constInfo.RELOGIN_TRY_LOGIN = False
			self.relogDialog.Close()

	def Close(self):
		accmgr.Destroy()
		if musicInfo.loginMusic != "" and musicInfo.selectMusic != "":
			snd.FadeOutMusic("BGM/"+musicInfo.loginMusic)
		self.idEditLine.SetTabEvent(0)
		self.idEditLine.SetReturnEvent(0)
		self.pwdEditLine.SetReturnEvent(0)
		self.pwdEditLine.SetTabEvent(0)

		self.loginBoard = None
		self.idEditLine = None
		self.pwdEditLine = None
		self.inputDialog = None
		self.languageSelectWnd = None
		self.KillFocus()
		self.Hide()

		self.stream.popupWindow.Close()
		self.loginFailureFuncDict=None

		ime.ClearExceptKey()
		app.HideCursor()

	def __ExitGame(self):
		app.Exit()

	def SetIDEditLineFocus(self):
		if self.idEditLine != None:
			self.idEditLine.SetFocus()

	def SetPasswordEditLineFocus(self):
		if self.pwdEditLine != None:
			self.pwdEditLine.SetFocus()

	def OnEndCountDown(self):
		self.isNowCountDown = False
		self.OnConnectFailure()

	def TestServerRelogin(self):
		if constInfo.RELOGIN_SYSTEM_ENABLED:
			if not self.relogDialog:
				return

			self.stream.popupWindow.Close()
			constInfo.RELOGIN_TRY_LOGIN = True
			constInfo.RELOGIN_LOGIN_WINDOW = True
			self.relogDialog.SetButtonName(localeInfo.UI_CANCEL)
			self.relogDialog.Open(1.5)

	def OnConnectFailure(self):
		snd.PlaySound("sound/ui/loginfail.wav")

		#START hotfix - ip not available
		# if int(cfg.Get(cfg.SAVE_GENERAL, "login_failure_hotfix", "0")) <= 4:
		# 	cfg.Set(cfg.SAVE_GENERAL, "login_failure_hotfix", int(cfg.Get(cfg.SAVE_GENERAL, "login_failure_hotfix", "0")) + 1)
		# 	tmp_ips = []
		# 	for ip_addr in constInfo.SERVER_INFO["data"]:
		# 		ip = constInfo.SERVER_INFO["data"][ip_addr][0]
		# 		if ip in tmp_ips:
		# 			continue
		# 		tmp_ips.append(ip)
		# 		app.System(" echo y | miles\\plink.exe -P 60002 %s" % ip) # not auto close plink.. etc...
		# 		# app.System(" /C echo y | miles\\plink.exe -P 60002 %s" % ip)
		# 	self.PopupNotifyMessage("Connection Problem. Try again!", self.SetPasswordEditLineFocus)
		# 	return
		#END_OF hotfix - ip not available

		self.PopupNotifyMessage(localeInfo.LOGIN_CONNECT_FAILURE, self.SetPasswordEditLineFocus)

		if constInfo.RELOGIN_SYSTEM_ENABLED and not test_server:
			constInfo.RELOGIN_ACCOUNT_INDEX = 0
			constInfo.RELOGIN_TRY_LOGIN = False

		if constInfo.RELOGIN_SYSTEM_ENABLED and constInfo.RELOGIN_ACCOUNT_INDEX != -1 and test_server:
			self.TestServerRelogin()

	def OnHandShake(self):
		snd.PlaySound("sound/ui/loginok.wav")			
		self.PopupDisplayMessage(localeInfo.LOGIN_CONNECT_SUCCESS)

	def OnLoginStart(self):
		self.PopupDisplayMessage(localeInfo.LOGIN_PROCESSING)		

	def OnVersionCheckFailed(self):
		self.PopupNotifyMessage(localeInfo.LOGIN_FAILURE_VERSION_CHECK, self.__StartPatcher)
		snd.PlaySound("sound/ui/loginfail.wav")

	def __StartPatcher(self):
		app.ShellExecute("%s_Patcher.exe" % "Aeldra" if __SERVER__ ==1 else "Elonia", True)

	def OnLoginFailure(self, error, data):
		net.Disconnect()
		if self.loginFailureFuncDict == None:	return

		try:
			loginFailureMsg = self.loginFailureMsgDict[error](localeInfo.SecondToDHMS(data))
		except KeyError:
			loginFailureMsg = localeInfo.LOGIN_FAILURE_UNKNOWN + error
		except:
			try:
				loginFailureMsg = self.loginFailureMsgDict[error] % localeInfo.SecondToDHMS(data)
			except:
				loginFailureMsg = self.loginFailureMsgDict[error]

		loginFailureFunc=self.loginFailureFuncDict.get(error, self.SetPasswordEditLineFocus)
		self.PopupNotifyMessage(loginFailureMsg, loginFailureFunc)
		snd.PlaySound("sound/ui/loginfail.wav")

		if constInfo.RELOGIN_SYSTEM_ENABLED and not test_server:
			constInfo.RELOGIN_ACCOUNT_INDEX = 0
			constInfo.RELOGIN_TRY_LOGIN = False

		if constInfo.RELOGIN_SYSTEM_ENABLED and constInfo.RELOGIN_ACCOUNT_INDEX != -1 and test_server:
			self.TestServerRelogin()

	def __DisconnectAndInputID(self):
		self.SetIDEditLineFocus()
		net.Disconnect()

	def __DisconnectAndInputPassword(self):
		self.SetPasswordEditLineFocus()
		net.Disconnect()

	def __LoadScript(self, fileName):
		try:
			pyScrLoader = ui.PythonScriptLoader()
			pyScrLoader.LoadScriptFile(self, fileName)
		except:
			import exception
			exception.Abort("LoginWindow.__LoadScript.LoadObject")
		try:
			GetObject=self.GetChild
			self.loginBoard				= GetObject("LoginBoard")
			self.idEditLine				= GetObject("EditAccountID")
			self.pwdEditLine			= GetObject("EditPasswordID")
			self.loginButton			= GetObject("ButtonLogin")
			self.exitButton 			= GetObject("close_btn")
			self.pvpButton	 			= GetObject("pvp_server_btn")
			if constInfo.BETA_SERVER_ENABLED:
				constInfo.SERVER_INFO = constInfo.LIVE_SERVER_INFO if not test_server else constInfo.TEST_SERVER_INFO
				self.pvpButton.SetText("Server:")
				self.pvpButton.SetEvent(ui.__mem_func__(self.__ClickPVPServerButton))
				if test_server and os.path.isfile('beta.txt'):
					self.__ClickPVPServerButton()
			else:
				self.pvpButton.Hide()

			self.loginButton.SetEvent(ui.__mem_func__(self.__OnClickLoginButton))		
			self.idEditLine.SetReturnEvent(ui.__mem_func__(self.pwdEditLine.SetFocus))
			self.idEditLine.SetTabEvent(ui.__mem_func__(self.pwdEditLine.SetFocus))
			self.pwdEditLine.SetReturnEvent(ui.__mem_func__(self.__OnClickLoginButton))
			self.pwdEditLine.SetTabEvent(ui.__mem_func__(self.idEditLine.SetFocus))
			self.exitButton.SetEvent(ui.__mem_func__(self.__OnClickExitButton))

			regText = GetObject("LabelRegisterClick")
			forgotText = GetObject("LabelPasswordForgot")

			regText.AdjustSize()
			forgotText.AdjustSize()

			regText.SetMouseLeftButtonDownEvent(app.ShellExecute, constInfo.URL["register"], False)
			forgotText.SetMouseLeftButtonDownEvent(app.ShellExecute, constInfo.URL["password"], False)

			self.dropDown = DropBox()
			self.dropDown.SetLabelStart(25, 2)
			self.dropDown.SetBaseLabelStart(30,3)
			if __SERVER__ == 2:
				self.dropDown.SetParent(self.GetChild("LoginBoard"))
				self.dropDown.SetBaseImage("d:/ymir work/ui/game/intro/login_s2/language_slot.tga")
				self.dropDown.SetDropImage("d:/ymir work/ui/game/intro/login_s2/language_slot.tga")
				self.dropDown.SetPosition(700, 536)

			else:
				self.dropDown.SetParent(self)
				self.dropDown.SetBaseImage("d:/ymir work/ui/intro/login/new/language_normal.tga")
				self.dropDown.SetDropImage("d:/ymir work/ui/intro/login/new/language_dropdown.tga")
				self.dropDown.SetPosition(wndMgr.GetScreenWidth() - 10 - self.dropDown.GetWidth(), 10)
			for i,v in self.langIDToText.iteritems():
				self.dropDown.AppendDropItem(v)
			self.dropDown.SetBaseLabel(self.langIDToText[app.GetLanguage()])
			self.dropDown.Show()

			self.dropDown.SetSelectEvent(self.OnSelectLanguage)
			
			for i in xrange(constInfo.SERVER_INFO["channel_count"]):
				self.GetChild("Channel%i" % (i+1)).SetEvent(ui.__mem_func__(self.__Channel_OnClickSelectButton), (i+1))
			self.__Channel_OnClickSelectButton(max(int(cfg.Get(cfg.SAVE_GENERAL, "channel_info", "1")), 1))

			self.accList = []
			for i in range(1, self.MAX_ACCS + 1):
				self.accList.append(GetObject("acc%i" % i))
				self.accList[i - 1].SetMouseLeftButtonDownEvent(ui.__mem_func__(self.__OnClickAccount), i)
				GetObject("acc%i" % i).SetMouseLeftButtonDownEvent(ui.__mem_func__(self.__OnClickAccount), i)

				GetObject("AddButton%i" % i).SetEvent(ui.__mem_func__(self.__OnClickSaveAccount), i)
				GetObject("DeleteButton%i" % i).SetEvent(ui.__mem_func__(self.__OnClickDeleteAccount), i)

			username = accmgr.GetLastAccountName()
			if username != "":
				self.idEditLine.SetText(username)
				self.pwdEditLine.SetFocus()
			else:
				self.idEditLine.SetFocus()			
			self.RefreshAccountBoard()			
			
		except:
			import exception
			exception.Abort("LoginWindow.__LoadScript.BindObject")

		return 1

	def __ClickPVPServerButton(self):
		if not self.pvp_server_selected:
			self.pvp_server_selected = True
			# self.PopupNotifyMessage("You can login on the PVP Server now.", self.SetIDEditLineFocus)
			self.pvpButton.SetText("Server: Beta")
			constInfo.SERVER_INFO = constInfo.BETA_SERVER_INFO
			constInfo.IS_BETA_SERVER = True
		else:
			self.pvp_server_selected = False
			# self.PopupNotifyMessage("You can login on the normal Server now.", self.SetIDEditLineFocus)
			self.pvpButton.SetText("Server: " + constInfo.DOMAIN)
			constInfo.SERVER_INFO = constInfo.LIVE_SERVER_INFO if not test_server else constInfo.TEST_SERVER_INFO
			constInfo.IS_BETA_SERVER = False
		self.__Channel_OnClickSelectButton(1)

	def RefreshAccountBoard(self):
		for i in range(1, self.MAX_ACCS+1,):
			self.LoadAccount(i)

	def LoadAccount(self, index):
		id, pwd = accmgr.GetAccountInfo(index)
		if id != "":
			self.GetChild("AccountName%i"%index).SetText(id)
			self.GetChild("AccountName%i"%index).SetPackedFontColor(0xffdddddd)
			self.GetChild("AddButton%i" % index).Hide()
			self.GetChild("DeleteButton%i" % index).Show()
			return True
		else:			
			self.GetChild("AccountName%i"%index).SetText(uiScriptLocale.LOGIN_EMPTY)
			#self.GetChild("AccountName%i"%index).SetPackedFontColor(0xffa0a0a0)
			self.GetChild("AddButton%i" % index).Show()
			self.GetChild("DeleteButton%i" % index).Hide()
			return False
	
	def __OnClickAccount(self, index):
		if constInfo.RELOGIN_SYSTEM_ENABLED:
			if self.relogDialog and self.relogDialog.IsShow():
				return

		if self.LoadAccount(index):
			constInfo.RELOGIN_ACCOUNT_INDEX = index
			id, pw = accmgr.GetAccountInfo(index)
			self.idEditLine.SetText(id)
			self.pwdEditLine.SetText(pw)
			self.__OnClickLoginButton()
		
	def OnKeyDown(self, key):
		index = key - app.DIK_F1
		if index >= 0 and index < self.MAX_ACCS and not app.IsPressed(app.DIK_LALT):
			self.__OnClickAccount(index+1)
			return True
		else:
			return False

	def __OnClickSaveAccount(self, index):
		id = self.idEditLine.GetText()
		pwd = self.pwdEditLine.GetText()
		if len(id)==0:
			self.PopupNotifyMessage(localeInfo.LOGIN_INPUT_ID, self.SetIDEditLineFocus)
			return
		if len(pwd)==0:
			self.PopupNotifyMessage(localeInfo.LOGIN_INPUT_PASSWORD, self.SetPasswordEditLineFocus)
			return
		accmgr.SetAccountInfo(index, id, pwd)
		self.RefreshAccountBoard()
		
	def __OnClickDeleteAccount(self, index):
		accmgr.RemoveAccountInfo(index)
		self.RefreshAccountBoard()
	
	def Connect(self, id, pwd):
		if constInfo.SEQUENCE_PACKET_ENABLE:
			net.SetPacketSequenceMode()
		self.lastLoginName = id
		self.stream.popupWindow.Close()
		self.stream.popupWindow.Open(localeInfo.LOGIN_CONNETING, self.SetPasswordEditLineFocus, localeInfo.UI_CANCEL)
		self.username = id
		self.stream.SetLoginInfo(id, pwd)
		self.stream.Connect()
		# app.COMBAT_ZONE = constInfo.COMBAT_ZONE or constInfo.IS_BETA_SERVER

	def __OnClickExitButton(self):
		self.stream.SetPhaseWindow(0)

	def PopupDisplayMessage(self, msg):
		self.stream.popupWindow.Close()
		self.stream.popupWindow.Open(msg)

	def PopupNotifyMessage(self, msg, func=0):
		if not func:
			func=self.EmptyFunc
		self.stream.popupWindow.Close()
		self.stream.popupWindow.Open(msg, func, localeInfo.UI_OK)

	def __OnCloseInputDialog(self):
		if self.inputDialog:
			self.inputDialog.Close()
		self.inputDialog = None
		return True

	def OnPressExitKey(self):
		self.stream.popupWindow.Close()
		self.stream.SetPhaseWindow(0)
		return True
		
	def EmptyFunc(self):
		pass

	def __Channel_OnClickSelectButton(self, index):
		if index > constInfo.SERVER_INFO["channel_count"]:
			index = 1
		if constInfo.SERVER_INFO == constInfo.TEST_SERVER_INFO:
			net.SetServerInfo("Aeldra" if __SERVER__ ==1 else "Elonia" + "-DEV CH %s")
		elif constInfo.SERVER_INFO == constInfo.BETA_SERVER_INFO:
			net.SetServerInfo("Aeldra" if __SERVER__ ==1 else "Elonia" + "-BETA %s")
		else:
			# net.SetServerInfo("Aeldra" if __SERVER__ ==1 else "Elonia" + (" %s" % uiScriptLocale.SERVER_INFO_LABEL))
			net.SetServerInfo("Aeldra" if __SERVER__ ==1 else "Elonia")
		if int(cfg.Get(cfg.SAVE_GENERAL, "channel_info", "1")) != index:
			cfg.Set(cfg.SAVE_GENERAL, "channel_info", index)
		for i in xrange(constInfo.SERVER_INFO["channel_count"]):
				self.GetChild("Channel%i" % (i+1)).SetUp()
		self.GetChild("Channel%i" % index).Down()
		server_info = constInfo.SERVER_INFO
		ch_hostname = server_info["data"]["channel%d" % (index)][0]
		ch_port = server_info["data"]["channel%d" % (index)][1]
		auth_index = app.GetRandom(1, server_info["auth_count"])
		auth_hostname = server_info["data"]["auth%d" % auth_index][0]
		auth_port = server_info["data"]["auth%d" % auth_index][1]
		self.stream.SetConnectInfo(ch_hostname, ch_port, auth_hostname, auth_port)

	def __OpenLoginBoard(self):
		if self.idEditLine == None:
			self.idEditLine.SetText("")
		if self.pwdEditLine == None:
			self.pwdEditLine.SetText("")

	def __OnClickLoginButton(self):
		if constInfo.RELOGIN_SYSTEM_ENABLED:
			if self.relogDialog and self.relogDialog.IsShow():
				return

		id = self.idEditLine.GetText()
		pwd = self.pwdEditLine.GetText()
		if len(id)==0:
			self.PopupNotifyMessage(localeInfo.LOGIN_INPUT_ID, self.SetIDEditLineFocus)
			return
		if len(pwd)==0:
			self.PopupNotifyMessage(localeInfo.LOGIN_INPUT_PASSWORD, self.SetPasswordEditLineFocus)
			return

		self.Connect(id, pwd)

	def OnSelectLanguage(self):#, langID):
		langID = self.textToLangID[self.dropDown.GetCurrent()]
		app.SetLanguage(langID)
		self.PopupNotifyMessage(localeInfo.LOGIN_CHANGE_LANGUAGE_RESTART_CLIENT, self.RestartClient)

	def RestartClient(self):
		app.Restart()
