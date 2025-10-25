import net
import app
import ui
import uiOption
import uiSystemOption
import uiGameOption
import uiScriptLocale
import networkModule
import constInfo
import localeInfo
import cfg
import grp
import uiNewGameOption

###################################################################################################
## System
class SystemDialog(ui.ScriptWindow):

	CHANNEL_BUTTON_TIME_NEED = 0.1

	def __init__(self, interfaceHandle):
		ui.ScriptWindow.__init__(self)
		self.__Initialize()
		self.interfaceHandle = interfaceHandle
	
	def __Initialize(self):
		self.systemOptionDlg = None
		self.gameOptionDlg = None
		self.changeButton = None
		self.channelButton = None
		self.moveChannelDialog = None
		self.interfaceHandle = None
		if constInfo.NEW_PICKUP_FILTER:
			self.pickupOptionWnd = None

		if constInfo.ENABLE_INGAME_WIKI:
			self.wikiWnd = None

	def CheckChannelButton(self):
		if constInfo.CURRENT_CHANNEL_IDX == 99:
			self.channelButton.Disable()
		else:
			self.channelButton.Enable()
		
	def LoadDialog(self):	
		pyScrLoader = ui.PythonScriptLoader()
		pyScrLoader.LoadScriptFile(self, "uiscript/systemdialog.py")

		self.GetChild("system_option_button").SAFE_SetEvent(self.__ClickSystemOptionButton)
		self.GetChild("game_option_button").SAFE_SetEvent(self.__ClickGameOptionButton)
		self.GetChild("change_button").SAFE_SetEvent(self.__ClickChangeCharacterButton)
		self.GetChild("channel_button").SAFE_SetEvent(self.__ClickChannelSwitchButton)
		self.GetChild("logout_button").SAFE_SetEvent(self.__ClickLogOutButton)
		self.GetChild("exit_button").SAFE_SetEvent(self.__ClickExitButton)
		self.GetChild("cancel_button").SAFE_SetEvent(self.Close)

		self.GetChild("mall_button").SAFE_SetEvent(self.__ClickInGameShopButton)

		self.changeButton = self.GetChild("change_button")
		self.channelButton = self.GetChild("channel_button")
		self.CheckChannelButton()		

		if constInfo.NEW_PICKUP_FILTER:
			self.GetChild("pickup_option_button").SAFE_SetEvent(self.__ClickPickupOption)

		if constInfo.ENABLE_INGAME_WIKI:
			self.GetChild("wiki_button").SAFE_SetEvent(self.__ToggleWikiWindow)

	if constInfo.ENABLE_INGAME_WIKI:
		def __ToggleWikiWindow(self):
			if self.wikiWnd:
				if self.wikiWnd.IsShow():
					self.wikiWnd.Hide()
				else:
					self.wikiWnd.Show()
					self.wikiWnd.SetTop()
					
			self.Close()

	def Destroy(self):
		self.ClearDictionary()
		
		if self.gameOptionDlg:
			self.gameOptionDlg.Destroy()
			
		if self.systemOptionDlg:
			self.systemOptionDlg.Destroy()
			
		if self.moveChannelDialog:
			self.moveChannelDialog.Destroy()

		if constInfo.NEW_PICKUP_FILTER:
			if self.pickupOptionWnd:
				self.pickupOptionWnd.Destroy()

		self.__Initialize()

	def OpenDialog(self):
		self.Show()

	def __ClickChannelSwitchButton(self):
		self.Close()
		
		if not self.moveChannelDialog:
			self.moveChannelDialog = MoveChannelDialog()

		self.moveChannelDialog.Show()

	def __ClickChangeCharacterButton(self):
		self.Close()
		net.ExitGame()

	def __OnClosePopupDialog(self):
		self.popup = None		

	def __ClickLogOutButton(self):
		constInfo.RELOGIN_TRY_LOGIN = False
		self.Close()
		net.LogOutGame()

	def __ClickExitButton(self):
		self.Close()
		net.ExitApplication()
		
	def __ClickSystemOptionButton(self):
		self.Close()

		if not self.systemOptionDlg:
			self.systemOptionDlg = uiSystemOption.OptionDialog()

		self.systemOptionDlg.Show()

	def __ClickGameOptionButton(self):
		self.Close()

		if not self.gameOptionDlg:
			if constInfo.NEW_UI_GAMEOPTION:
				self.gameOptionDlg = uiNewGameOption.OptionDialog(self.interfaceHandle)
			else:
				self.gameOptionDlg = uiGameOption.OptionDialog(self.interfaceHandle)

		self.gameOptionDlg.Show()

	def __ClickInGameShopButton(self):
		self.Close()

		net.SendChatPacket("/in_game_mall")

	if constInfo.NEW_PICKUP_FILTER:
		def __ClickPickupOption(self):
			self.Close()

			if not self.pickupOptionWnd:
				self.pickupOptionWnd = PickupOptionWindow()

			self.pickupOptionWnd.Open()

	def Close(self):
		self.Hide()
		return True

	def RefreshMobile(self):
		if self.gameOptionDlg:
			self.gameOptionDlg.RefreshMobile()
		#self.optionDialog.RefreshMobile()

	def OnMobileAuthority(self):
		if self.gameOptionDlg:
			self.gameOptionDlg.OnMobileAuthority()
		#self.optionDialog.OnMobileAuthority()

	def OnBlockMode(self, mode):
		if constInfo.NEW_UI_GAMEOPTION:
			uiNewGameOption.blockMode = mode
		else:
			uiGameOption.blockMode = mode
		if self.gameOptionDlg:
			self.gameOptionDlg.OnBlockMode(mode)
		#self.optionDialog.OnBlockMode(mode)

	def OnChangePKMode(self):
		if self.gameOptionDlg:
			self.gameOptionDlg.OnChangePKMode()
		#self.optionDialog.OnChangePKMode()
	
	def OnPressExitKey(self):
		self.Close()
		return True

	def OnPressEscapeKey(self):
		self.Close()
		return True


class MoveChannelDialog(ui.ScriptWindow):
	def __init__(self):
		ui.ScriptWindow.__init__(self)
		self.__LoadWindow()
		self.btns = []
		self.Open()		
		
	def __del__(self):
		del self.btns
		ui.ScriptWindow.__del__(self)
		
	def Destroy(self):
		self.Close()
		
	def __LoadWindow(self):
		pyScrLoader = ui.PythonScriptLoader()
		try:
			pyScrLoader.LoadScriptFile(self, "uiscript/MoveChannelDialog.py")
		except:
			import exception
			exception.Abort("MoveChannelDialog.__LoadDialog.LoadObject")

	def Open(self):
		try:
			GetObject=self.GetChild
			self.moveChannelBoard = GetObject("MoveChannelBoard")
			self.blackBoard = GetObject("BlackBoard")
			self.GetChild("MoveChannelTitle").SetCloseEvent(ui.__mem_func__(self.Close))
		
			for i in xrange(constInfo.SERVER_INFO['channel_count']):
				btn = ui.Button()
				btn.SetUpVisual("d:/ymir work/ui/public/select_btn_01.sub")
				btn.SetOverVisual("d:/ymir work/ui/public/select_btn_02.sub")
				btn.SetDownVisual("d:/ymir work/ui/public/select_btn_03.sub")
				btn.SetText("%s %d" % (localeInfo.CHANNEL, (int(i)+1)))
				btn.SetParent(self.blackBoard) 
				btn.SetPosition(6, 6 + 28 * i)
				btn.SetEvent(ui.__mem_func__(self.__SelectChannel), i)
				self.btns.append(btn)
				self.btns[i].Show()
				
			self.SetSize(190, constInfo.SERVER_INFO['channel_count'] * 28 + 12 + 52)
			self.moveChannelBoard.SetSize(190, constInfo.SERVER_INFO['channel_count'] * 28 + 52	)
			self.blackBoard.SetSize(161, constInfo.SERVER_INFO['channel_count'] * 28 + 8)
		except:
			import exception
			exception.Abort("MoveChannelDialog.Open.BindObject")

		ui.ScriptWindow.Show(self)
			
	def __SelectChannel(self, index):
		net.SendChatPacket("/fast_change_channel %d %s" % (index + 1, constInfo.SERVER_INFO["data"]["channel%i" % (index + 1)][0]))
		cfg.Set(cfg.SAVE_GENERAL, "channel_info", index + 1)
		self.Close()
			
	def Close(self):
		self.Hide()
		return True
		
	def Show(self):
		ui.ScriptWindow.Show(self)
		self.SetCenterPosition()
		
	def OnPressEscapeKey(self):
		self.Close()
		return True


if constInfo.NEW_PICKUP_FILTER:
	class PickupOptionWindow(ui.ScriptWindow):
		def __init__(self):
			ui.ScriptWindow.__init__(self)
			self.pickupFilterButtonList = []
			self.pickupAllButtonList = []
			self.__LoadWindow()
			self.RefreshPickUpFilter()
			self.RefreshPickUpAll()

		def __del__(self):
			ui.ScriptWindow.__del__(self)

		def __LoadWindow(self):
			try:
				pyScrLoader = ui.PythonScriptLoader()
				pyScrLoader.LoadScriptFile(self, "uiscript/pickupoption.py")
			except:
				import exception
				exception.Abort("PickupOptionWindow.__LoadWindow.LoadObject")

			try:
				GetObject = self.GetChild
				self.pickupFilterButtonList.append((GetObject("disable_pickup_weapon"), cfg.DISABLE_PICKUP_WEAPON,))
				self.pickupFilterButtonList.append((GetObject("disable_pickup_armor"), cfg.DISABLE_PICKUP_ARMOR,))
				self.pickupFilterButtonList.append((GetObject("disable_pickup_etc"), cfg.DISABLE_PICKUP_ETC))
				self.pickupFilterButtonList.append((GetObject("disable_pickup_potion"), cfg.DISABLE_PICKUP_POTION))
				self.pickupFilterButtonList.append((GetObject("disable_pickup_book"), cfg.DISABLE_PICKUP_BOOK))
				self.pickupFilterButtonList.append((GetObject("pickup_size_1"), cfg.DISABLE_PICKUP_SIZE_1))
				self.pickupFilterButtonList.append((GetObject("pickup_size_2"), cfg.DISABLE_PICKUP_SIZE_2))
				self.pickupFilterButtonList.append((GetObject("pickup_size_3"), cfg.DISABLE_PICKUP_SIZE_3))
				self.pickupAllButtonList.append(GetObject("pickup_all_fast"))
				self.pickupAllButtonList.append(GetObject("pickup_all_slow"))
				GetObject("TitleBar").SetCloseEvent(ui.__mem_func__(self.Close))
			except:
				import exception
				exception.Abort("PickupOptionWindow.__LoadWindow.BindObject")

			for i in self.pickupFilterButtonList:
				i[0].SetToggleUpEvent(lambda arg = i[1] : ui.__mem_func__(self.__OnChangePickUpFilter)(arg))
				i[0].SetToggleDownEvent(lambda arg = i[1] : ui.__mem_func__(self.__OnChangePickUpFilter)(arg))

			self.pickupAllButtonList[0].SetToggleUpEvent(self.__OnClickPickupAllOnButton)
			self.pickupAllButtonList[1].SetToggleUpEvent(self.__OnClickPickupAllOffButton)
			self.pickupAllButtonList[0].SetToggleDownEvent(self.__OnClickPickupAllOnButton)
			self.pickupAllButtonList[1].SetToggleDownEvent(self.__OnClickPickupAllOffButton)

		def __OnChangePickUpFilter(self, flag):
			cur = int(cfg.Get(cfg.SAVE_OPTION, "disabled_pickup_types", "0"))
			cfg.Set(cfg.SAVE_OPTION, "disabled_pickup_types", str(cur ^ flag))
			self.RefreshPickUpFilter()

		def RefreshPickUpFilter(self):
			cur = int(cfg.Get(cfg.SAVE_OPTION, "disabled_pickup_types", "0"))
			for i in self.pickupFilterButtonList:
				if cur & i[1]:
					i[0].Down()
				else:
					i[0].SetUp()

		def RefreshPickUpAll(self):
			if cfg.Get(cfg.SAVE_OPTION, "pickup_all_fast", "1") == "1":
				self.pickupAllButtonList[0].Down()
				self.pickupAllButtonList[1].SetUp()
			else:
				self.pickupAllButtonList[0].SetUp()
				self.pickupAllButtonList[1].Down()

		def __OnClickPickupAllOnButton(self):
			cfg.Set(cfg.SAVE_OPTION, "pickup_all_fast", "1")
			self.RefreshPickUpAll()

		def __OnClickPickupAllOffButton(self):
			cfg.Set(cfg.SAVE_OPTION, "pickup_all_fast", "0")
			self.RefreshPickUpAll()

		def Open(self):
			self.SetCenterPosition()
			self.Show()

		def Close(self):
			self.Hide()

		def OnPressEscapeKey(self):
			self.Close()
			return True

		def Destroy(self):
			self.ClearDictionary()
			self.pickupFilterButtonList = []
			self.pickupAllButtonList = []
