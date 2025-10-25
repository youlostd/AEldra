import ui
import snd
import systemSetting
import net
import chat
import app
import localeInfo
import constInfo
import chrmgr
import player
import cfg
import background

blockMode = 0
viewChatMode = 0

MOBILE = False

if constInfo.ITEM_TEXTAIL_OPTION:
	ONLY_ITEM_TEXTAIL = int(cfg.Get(cfg.SAVE_GENERAL, "only_item_textail", "0"))

if localeInfo.IsYMIR():
	MOBILE = True


class OptionDialog(ui.ScriptWindow):

	def __init__(self, interfaceHandle):
		ui.ScriptWindow.__init__(self)
		self.__Initialize()
		self.interfaceHandle = interfaceHandle
		self.__Load()

		self.RefreshViewChat()
		self.RefreshAlwaysShowName()
		self.RefreshShowDamage()
		self.RefreshGoldPickupChat()
		self.RefreshItemHighlight()
		if not constInfo.NEW_PICKUP_FILTER:
			self.RefreshPickUpFilter()
			self.RefreshPickUpAll()
		self.RefreshQuestLetter()
		self.RefreshUseNight()
		self.RefreshHideShopAds()
		self.RefreshHideCostumes()
		self.RefreshRenderOpt()
		self.RefreshFPS()
		if constInfo.HIDE_NPC_OPTION:
			self.RefreshHideNPC()

	def __del__(self):
		ui.ScriptWindow.__del__(self)
		print " -------------------------------------- DELETE GAME OPTION DIALOG"

	def __Initialize(self):
		self.titleBar = 0
		self.titleBar2 = 0
		self.nameColorModeButtonList = []
		self.viewTargetBoardButtonList = []
		self.pvpModeButtonDict = {}
		self.blockButtonList = []
		self.viewChatButtonList = []
		self.alwaysShowNameButtonList = []
		self.showDamageButtonList = []
		self.itemHighlightButtonList = []
		self.goldPickupChatButtonList = []
		if not constInfo.NEW_PICKUP_FILTER:
			self.pickupFilterButtonList = []
			self.pickupAllButtonList = []
		self.questLetterButtonList = []
		self.useNightButtonList = []
		self.hideShopAdsButtonList = []
		self.hideCostumesButtonList = []
		self.renderOptButtonList = []
		self.refreshInventoryBagSlot = None
		self.interfaceHandle = None

		self.renderDistances = [15000.0, 5000.0, 1500.0]

		if constInfo.ENABLE_CHANGE_TEXTURE_SNOW:
			self.snowmode = []

		self.showFPSButtonList = []
		if constInfo.HIDE_NPC_OPTION:
			self.hideNPCButtonList = []
		if constInfo.SAVE_WINDOW_POSITION:
			self.wndSavePosButtons = []

	def Destroy(self):
		self.ClearDictionary()

		self.__Initialize()
		print " -------------------------------------- DESTROY GAME OPTION DIALOG"
	
	def __Load_LoadScript(self, fileName):
		try:
			pyScriptLoader = ui.PythonScriptLoader()
			pyScriptLoader.LoadScriptFile(self, fileName)
		except:
			import exception
			exception.Abort("OptionDialog.__Load_LoadScript")

	def __Load_BindObject(self):
		try:
			GetObject = self.GetChild
			self.titleBar = GetObject("titlebar")
			self.titleBar2 = GetObject("titlebar2")
			self.nameColorModeButtonList.append(GetObject("name_color_normal"))
			self.nameColorModeButtonList.append(GetObject("name_color_empire"))
			
			self.viewTargetBoardButtonList.append(GetObject("target_board_no_view"))
			self.viewTargetBoardButtonList.append(GetObject("target_board_view"))
			
			self.pvpModeButtonDict[player.PK_MODE_PEACE] = GetObject("pvp_peace")
			self.pvpModeButtonDict[player.PK_MODE_REVENGE] = GetObject("pvp_revenge")
			self.pvpModeButtonDict[player.PK_MODE_GUILD] = GetObject("pvp_guild")
			self.pvpModeButtonDict[player.PK_MODE_FREE] = GetObject("pvp_free")
			self.blockButtonList.append(GetObject("block_exchange_button"))
			self.blockButtonList.append(GetObject("block_party_button"))
			self.blockButtonList.append(GetObject("block_guild_button"))
			self.blockButtonList.append(GetObject("block_whisper_button"))
			self.blockButtonList.append(GetObject("block_friend_button"))
			self.blockButtonList.append(GetObject("block_party_request_button"))
			self.viewChatButtonList.append(GetObject("view_chat_on_button"))
			self.viewChatButtonList.append(GetObject("view_chat_off_button"))
			self.alwaysShowNameButtonList.append(GetObject("always_show_name_on_button"))
			self.alwaysShowNameButtonList.append(GetObject("always_show_name_off_button"))
			if constInfo.ITEM_TEXTAIL_OPTION:
				self.alwaysShowNameButtonList.append(GetObject("show_only_items_names_button"))
			else:
				GetObject("show_only_items_names_button").Hide()
			self.showDamageButtonList.append(GetObject("show_damage_on_button"))
			self.showDamageButtonList.append(GetObject("show_damage_off_button"))
			self.itemHighlightButtonList.append(GetObject("item_highlight_option_on"))
			self.itemHighlightButtonList.append(GetObject("item_highlight_option_off"))
			self.goldPickupChatButtonList.append(GetObject("gold_pickup_chat_option_on"))
			self.goldPickupChatButtonList.append(GetObject("gold_pickup_chat_option_off"))
			self.questLetterButtonList.append(GetObject("quest_letter_show"))
			self.questLetterButtonList.append(GetObject("quest_letter_hide"))

			if not constInfo.NEW_PICKUP_FILTER:
				self.pickupFilterButtonList.append((GetObject("disable_pickup_weapon"), cfg.DISABLE_PICKUP_WEAPON,))
				self.pickupFilterButtonList.append((GetObject("disable_pickup_armor"), cfg.DISABLE_PICKUP_ARMOR,))
				self.pickupFilterButtonList.append((GetObject("disable_pickup_etc"), cfg.DISABLE_PICKUP_ETC))

				self.pickupAllButtonList.append(GetObject("pickup_all_fast"))
				self.pickupAllButtonList.append(GetObject("pickup_all_slow"))

			self.useNightButtonList.append(GetObject("usenight_on_button"))
			self.useNightButtonList.append(GetObject("usenight_off_button"))

			self.hideShopAdsButtonList.append(GetObject("hide_shop_ad_on_button"))
			self.hideShopAdsButtonList.append(GetObject("hide_shop_ad_off_button"))

			self.hideCostumesButtonList.append(GetObject("hide_costume_weapon"))
			self.hideCostumesButtonList.append(GetObject("hide_costume_armor"))
			self.hideCostumesButtonList.append(GetObject("hide_costume_hair"))
			self.hideCostumesButtonList.append(GetObject("hide_costume_acce"))

			self.renderOptButtonList.append(GetObject("render_low"))
			self.renderOptButtonList.append(GetObject("render_medium"))
			self.renderOptButtonList.append(GetObject("render_high"))

			if constInfo.ENABLE_CHANGE_TEXTURE_SNOW:
				self.snowmode.append(GetObject("snow_on"))
				self.snowmode.append(GetObject("snow_off"))

			self.showFPSButtonList.append(GetObject("hide_fps"))
			self.showFPSButtonList.append(GetObject("show_fps"))

			if constInfo.HIDE_NPC_OPTION:
				self.hideNPCButtonList.append(GetObject("HideBuffi"))
				self.hideNPCButtonList.append(GetObject("HideMount"))
				self.hideNPCButtonList.append(GetObject("HidePet"))

			if constInfo.SAVE_WINDOW_POSITION:
				self.wndSavePosButtons.append(GetObject("wnd_pos_btn0"))
				self.wndSavePosButtons.append(GetObject("wnd_pos_btn1"))

		except:
			import exception
			exception.Abort("OptionDialog.__Load_BindObject")

	def __Load(self):
		if constInfo.NEW_PICKUP_FILTER:
			self.__Load_LoadScript("uiscript/gameoptiondialognew.py")
		else:
			self.__Load_LoadScript("uiscript/gameoptiondialog.py")

		self.__Load_BindObject()

		self.SetCenterPosition()

		self.titleBar.SetCloseEvent(ui.__mem_func__(self.Close))
		self.titleBar2.SetCloseEvent(ui.__mem_func__(self.Close))

		self.nameColorModeButtonList[0].SAFE_SetEvent(self.__OnClickNameColorModeNormalButton)
		self.nameColorModeButtonList[1].SAFE_SetEvent(self.__OnClickNameColorModeEmpireButton)

		self.viewTargetBoardButtonList[0].SAFE_SetEvent(self.__OnClickTargetBoardViewButton)
		self.viewTargetBoardButtonList[1].SAFE_SetEvent(self.__OnClickTargetBoardNoViewButton)

		self.pvpModeButtonDict[player.PK_MODE_PEACE].SAFE_SetEvent(self.__OnClickPvPModePeaceButton)
		self.pvpModeButtonDict[player.PK_MODE_REVENGE].SAFE_SetEvent(self.__OnClickPvPModeRevengeButton)
		self.pvpModeButtonDict[player.PK_MODE_GUILD].SAFE_SetEvent(self.__OnClickPvPModeGuildButton)
		self.pvpModeButtonDict[player.PK_MODE_FREE].SAFE_SetEvent(self.__OnClickPvPModeFreeButton)

		self.blockButtonList[0].SetToggleUpEvent(self.__OnClickBlockExchangeButton)
		self.blockButtonList[1].SetToggleUpEvent(self.__OnClickBlockPartyButton)
		self.blockButtonList[2].SetToggleUpEvent(self.__OnClickBlockGuildButton)
		self.blockButtonList[3].SetToggleUpEvent(self.__OnClickBlockWhisperButton)
		self.blockButtonList[4].SetToggleUpEvent(self.__OnClickBlockFriendButton)
		self.blockButtonList[5].SetToggleUpEvent(self.__OnClickBlockPartyRequest)

		self.blockButtonList[0].SetToggleDownEvent(self.__OnClickBlockExchangeButton)
		self.blockButtonList[1].SetToggleDownEvent(self.__OnClickBlockPartyButton)
		self.blockButtonList[2].SetToggleDownEvent(self.__OnClickBlockGuildButton)
		self.blockButtonList[3].SetToggleDownEvent(self.__OnClickBlockWhisperButton)
		self.blockButtonList[4].SetToggleDownEvent(self.__OnClickBlockFriendButton)
		self.blockButtonList[5].SetToggleDownEvent(self.__OnClickBlockPartyRequest)

		self.viewChatButtonList[0].SAFE_SetEvent(self.__OnClickViewChatOnButton)
		self.viewChatButtonList[1].SAFE_SetEvent(self.__OnClickViewChatOffButton)

		self.alwaysShowNameButtonList[0].SAFE_SetEvent(self.__OnClickAlwaysShowNameOnButton)
		self.alwaysShowNameButtonList[1].SAFE_SetEvent(self.__OnClickAlwaysShowNameOffButton)
		if constInfo.ITEM_TEXTAIL_OPTION:
			self.alwaysShowNameButtonList[2].SAFE_SetEvent(self.__OnClickOnlyShowItemOnButton)

		self.showDamageButtonList[0].SAFE_SetEvent(self.__OnClickShowDamageOnButton)
		self.showDamageButtonList[1].SAFE_SetEvent(self.__OnClickShowDamageOffButton)

		self.itemHighlightButtonList[0].SetToggleUpEvent(self.__OnClickItemHighlightOnButton)
		self.itemHighlightButtonList[1].SetToggleUpEvent(self.__OnClickItemHighlightOffButton)
		self.itemHighlightButtonList[0].SetToggleDownEvent(self.__OnClickItemHighlightOnButton)
		self.itemHighlightButtonList[1].SetToggleDownEvent(self.__OnClickItemHighlightOffButton)

		self.goldPickupChatButtonList[0].SetToggleUpEvent(self.__OnClickGoldPickupChatOnButton)
		self.goldPickupChatButtonList[1].SetToggleUpEvent(self.__OnClickGoldPickupChatOffButton)
		self.goldPickupChatButtonList[0].SetToggleDownEvent(self.__OnClickGoldPickupChatOnButton)
		self.goldPickupChatButtonList[1].SetToggleDownEvent(self.__OnClickGoldPickupChatOffButton)

		self.questLetterButtonList[0].SetToggleUpEvent(self.__OnClickQuestLetterOnButton)
		self.questLetterButtonList[1].SetToggleUpEvent(self.__OnClickQuestLetterOffButton)
		self.questLetterButtonList[0].SetToggleDownEvent(self.__OnClickQuestLetterOnButton)
		self.questLetterButtonList[1].SetToggleDownEvent(self.__OnClickQuestLetterOffButton)

		if not constInfo.NEW_PICKUP_FILTER:
			for i in self.pickupFilterButtonList:
				i[0].SetToggleUpEvent(lambda arg = i[1] : ui.__mem_func__(self.__OnChangePickUpFilter)(arg))
				i[0].SetToggleDownEvent(lambda arg = i[1] : ui.__mem_func__(self.__OnChangePickUpFilter)(arg))

			self.pickupAllButtonList[0].SetToggleUpEvent(self.__OnClickPickupAllOnButton)
			self.pickupAllButtonList[1].SetToggleUpEvent(self.__OnClickPickupAllOffButton)
			self.pickupAllButtonList[0].SetToggleDownEvent(self.__OnClickPickupAllOnButton)
			self.pickupAllButtonList[1].SetToggleDownEvent(self.__OnClickPickupAllOffButton)

		self.useNightButtonList[0].SetToggleUpEvent(self.__OnClickUseNightOnButton)
		self.useNightButtonList[1].SetToggleUpEvent(self.__OnClickUseNightOffButton)
		self.useNightButtonList[0].SetToggleDownEvent(self.__OnClickUseNightOnButton)
		self.useNightButtonList[1].SetToggleDownEvent(self.__OnClickUseNightOffButton)

		self.hideShopAdsButtonList[0].SetToggleUpEvent(self.__OnClickHideShopAdsOnButton)
		self.hideShopAdsButtonList[1].SetToggleUpEvent(self.__OnClickHideShopAdsOffButton)
		self.hideShopAdsButtonList[0].SetToggleDownEvent(self.__OnClickHideShopAdsOffButton)
		self.hideShopAdsButtonList[1].SetToggleDownEvent(self.__OnClickHideShopAdsOnButton)

		self.__ClickRadioButton(self.nameColorModeButtonList, constInfo.GET_CHRNAME_COLOR_INDEX())
		self.__ClickRadioButton(self.viewTargetBoardButtonList, constInfo.GET_VIEW_OTHER_EMPIRE_PLAYER_TARGET_BOARD())
		self.__SetPeacePKMode()

		self.hideCostumesButtonList[0].SetToggleDownEvent(self.__OnChangeHideCostumesOn, 0)
		self.hideCostumesButtonList[1].SetToggleDownEvent(self.__OnChangeHideCostumesOn, 1)
		self.hideCostumesButtonList[2].SetToggleDownEvent(self.__OnChangeHideCostumesOn, 2)
		self.hideCostumesButtonList[3].SetToggleDownEvent(self.__OnChangeHideCostumesOn, 3)

		self.hideCostumesButtonList[0].SetToggleUpEvent(self.__OnChangeHideCostumesOff, 0)
		self.hideCostumesButtonList[1].SetToggleUpEvent(self.__OnChangeHideCostumesOff, 1)
		self.hideCostumesButtonList[2].SetToggleUpEvent(self.__OnChangeHideCostumesOff, 2)
		self.hideCostumesButtonList[3].SetToggleUpEvent(self.__OnChangeHideCostumesOff, 3)

		for i in xrange(len(self.renderOptButtonList)):
			self.renderOptButtonList[i].SetToggleUpEvent(lambda arg = i : ui.__mem_func__(self.__OnClickChangeRenderOpt)(arg))
			self.renderOptButtonList[i].SetToggleDownEvent(lambda arg = i : ui.__mem_func__(self.__OnClickChangeRenderOpt)(arg))

		if constInfo.ENABLE_CHANGE_TEXTURE_SNOW:
			self.snowmode[0].SAFE_SetEvent(self.__SnowOn)
			self.snowmode[1].SAFE_SetEvent(self.__SnowOff)
			self.UpdateSnow()

		self.showFPSButtonList[0].SetToggleDownEvent(self.__ShowFPS, 0)
		self.showFPSButtonList[1].SetToggleDownEvent(self.__ShowFPS, 1)

		if constInfo.HIDE_NPC_OPTION:
			self.hideNPCButtonList[0].SetToggleDownEvent(self.__HideNPC, 0)
			self.hideNPCButtonList[1].SetToggleDownEvent(self.__HideNPC, 1)
			self.hideNPCButtonList[2].SetToggleDownEvent(self.__HideNPC, 2)

			self.hideNPCButtonList[0].SetToggleUpEvent(self.__ShowNPC, 0)
			self.hideNPCButtonList[1].SetToggleUpEvent(self.__ShowNPC, 1)
			self.hideNPCButtonList[2].SetToggleUpEvent(self.__ShowNPC, 2)

		if constInfo.SAVE_WINDOW_POSITION:
			self.wndSavePosButtons[0].SAFE_SetEvent(self.__OnClickSaveWndPosBtn, 0)
			self.wndSavePosButtons[1].SAFE_SetEvent(self.__OnClickSaveWndPosBtn, 1)

			saved = int(cfg.Get(cfg.SAVE_GENERAL, "save_wnd_pos", "0"))
			self.wndSavePosButtons[saved].Down()

	def __OnClickChangeRenderOpt(self, flag):
		cfg.Set(cfg.SAVE_OPTION, "perf_tree_range", self.renderDistances[flag])
		cfg.Set(cfg.SAVE_OPTION, "perf_gravel_range", self.renderDistances[flag])
		cfg.Set(cfg.SAVE_OPTION, "perf_effect_range", self.renderDistances[flag])
		cfg.Set(cfg.SAVE_OPTION, "perf_shop_range", self.renderDistances[flag])
		background.SetForceRefreshTree()
		background.SetForceRefreshGravel()
		background.RefreshShopRange();
		self.RefreshRenderOpt()

	def RefreshRenderOpt(self):
		cur = float(cfg.Get(cfg.SAVE_OPTION, "perf_tree_range", self.renderDistances[2]))
		for i in xrange(len(self.renderDistances)):
			self.renderOptButtonList[i].SetUp()
			if cur >= self.renderDistances[i]:
				if i == 0 or i > 0 and cur < self.renderDistances[i-1]:
					self.renderOptButtonList[i].Down()
				

	def __ClickRadioButton(self, buttonList, buttonIndex):
		try:
			selButton=buttonList[buttonIndex]
		except IndexError:
			return

		for eachButton in buttonList:
			eachButton.SetUp()

		selButton.Down()

	def __SetNameColorMode(self, index):
		constInfo.SET_CHRNAME_COLOR_INDEX(index)
		self.__ClickRadioButton(self.nameColorModeButtonList, index)

	def __SetTargetBoardViewMode(self, flag):
		constInfo.SET_VIEW_OTHER_EMPIRE_PLAYER_TARGET_BOARD(flag)
		self.__ClickRadioButton(self.viewTargetBoardButtonList, flag)

	def __OnClickNameColorModeNormalButton(self):
		self.__SetNameColorMode(0)

	def __OnClickNameColorModeEmpireButton(self):
		self.__SetNameColorMode(1)

	def __OnClickTargetBoardViewButton(self):
		self.__SetTargetBoardViewMode(0)

	def __OnClickTargetBoardNoViewButton(self):
		self.__SetTargetBoardViewMode(1)

	def __OnClickCameraModeShortButton(self):
		self.__SetCameraMode(0)

	def __OnClickCameraModeLongButton(self):
		self.__SetCameraMode(1)

	def __OnClickFogModeLevel0Button(self):
		self.__SetFogLevel(0)

	def __OnClickFogModeLevel1Button(self):
		self.__SetFogLevel(1)

	def __OnClickFogModeLevel2Button(self):
		self.__SetFogLevel(2)

	def __OnClickBlockExchangeButton(self):
		self.RefreshBlock()
		global blockMode
		net.SendChatPacket("/setblockmode " + str(blockMode ^ player.BLOCK_EXCHANGE))
	def __OnClickBlockPartyButton(self):
		self.RefreshBlock()
		global blockMode
		net.SendChatPacket("/setblockmode " + str(blockMode ^ player.BLOCK_PARTY))
	def __OnClickBlockGuildButton(self):
		self.RefreshBlock()
		global blockMode
		net.SendChatPacket("/setblockmode " + str(blockMode ^ player.BLOCK_GUILD))
	def __OnClickBlockWhisperButton(self):
		self.RefreshBlock()
		global blockMode
		net.SendChatPacket("/setblockmode " + str(blockMode ^ player.BLOCK_WHISPER))
	def __OnClickBlockFriendButton(self):
		self.RefreshBlock()
		global blockMode
		net.SendChatPacket("/setblockmode " + str(blockMode ^ player.BLOCK_FRIEND))
	def __OnClickBlockPartyRequest(self):
		self.RefreshBlock()
		global blockMode
		net.SendChatPacket("/setblockmode " + str(blockMode ^ player.BLOCK_PARTY_REQUEST))

	def __OnClickViewChatOnButton(self):
		global viewChatMode
		viewChatMode = 1
		systemSetting.SetViewChatFlag(viewChatMode)
		self.RefreshViewChat()
	def __OnClickViewChatOffButton(self):
		global viewChatMode
		viewChatMode = 0
		systemSetting.SetViewChatFlag(viewChatMode)
		self.RefreshViewChat()

	if constInfo.ITEM_TEXTAIL_OPTION:
		def __OnClickOnlyShowItemOnButton(self):
			global ONLY_ITEM_TEXTAIL
			ONLY_ITEM_TEXTAIL = 1
			systemSetting.SetAlwaysShowNameFlag(False)
			self.RefreshAlwaysShowName()
			cfg.Set(cfg.SAVE_GENERAL, "only_item_textail", "1")


	def __OnClickAlwaysShowNameOnButton(self):
		if constInfo.ITEM_TEXTAIL_OPTION:
			global ONLY_ITEM_TEXTAIL
			ONLY_ITEM_TEXTAIL = 0
			cfg.Set(cfg.SAVE_GENERAL, "only_item_textail", "0")
		systemSetting.SetAlwaysShowNameFlag(True)
		self.RefreshAlwaysShowName()

	def __OnClickAlwaysShowNameOffButton(self):
		if constInfo.ITEM_TEXTAIL_OPTION:
			global ONLY_ITEM_TEXTAIL
			ONLY_ITEM_TEXTAIL = 0
			cfg.Set(cfg.SAVE_GENERAL, "only_item_textail", "0")
		systemSetting.SetAlwaysShowNameFlag(False)
		self.RefreshAlwaysShowName()

	def __OnClickShowDamageOnButton(self):
		systemSetting.SetShowDamageFlag(True)
		self.RefreshShowDamage()

	def __OnClickShowDamageOffButton(self):
		systemSetting.SetShowDamageFlag(False)
		self.RefreshShowDamage()

	def __CheckPvPProtectedLevelPlayer(self):	
		if player.GetStatus(player.LEVEL)<constInfo.PVPMODE_PROTECTED_LEVEL:
			self.__SetPeacePKMode()
			chat.AppendChat(chat.CHAT_TYPE_INFO, localeInfo.OPTION_PVPMODE_PROTECT % (constInfo.PVPMODE_PROTECTED_LEVEL))
			return 1

		return 0

	def __SetPKMode(self, mode):
		for btn in self.pvpModeButtonDict.values():
			btn.SetUp()
		if self.pvpModeButtonDict.has_key(mode):
			self.pvpModeButtonDict[mode].Down()

	def __SetPeacePKMode(self):
		self.__SetPKMode(player.PK_MODE_PEACE)

	def __RefreshPVPButtonList(self):
		self.__SetPKMode(player.GetPKMode())

	if app.ENABLE_MELEY_LAIR_DUNGEON:
		def setMeleyMap(self):
			mapName = background.GetCurrentMapName()
			if mapName == "metin2_map_n_flame_dragon":
				if player.GetGuildID() != 0 and player.GetPKMode() != player.PK_MODE_GUILD:
					for btn in self.pvpModeButtonDict.values():
						btn.SetUp()
					
					net.SendChatPacket("/pkmode 4", chat.CHAT_TYPE_TALKING)
					self.pvpModeButtonDict[player.PK_MODE_GUILD].Down()

		def isMeleyMap(self, button):
			mapName = background.GetCurrentMapName()
			if mapName == "metin2_map_n_flame_dragon":
				if self.pvpModeButtonDict[button]:
					self.pvpModeButtonDict[button].SetUp()
				
				chat.AppendChat(chat.CHAT_TYPE_INFO, localeInfo.CANNOT_CHANGE_FIGHT_MODE)
				return 1
			
			return 0

	def __OnClickPvPModePeaceButton(self):
		if app.ENABLE_MELEY_LAIR_DUNGEON:
			if self.isMeleyMap(player.PK_MODE_PEACE):
				return
		if self.__CheckPvPProtectedLevelPlayer():
			return

		self.__RefreshPVPButtonList()

		if constInfo.PVPMODE_ENABLE:
			net.SendChatPacket("/pkmode 0", chat.CHAT_TYPE_TALKING)
		else:
			chat.AppendChat(chat.CHAT_TYPE_INFO, localeInfo.OPTION_PVPMODE_NOT_SUPPORT)

	def __OnClickPvPModeRevengeButton(self):
		if app.ENABLE_MELEY_LAIR_DUNGEON:
			if self.isMeleyMap(player.PK_MODE_REVENGE):
				return
		if self.__CheckPvPProtectedLevelPlayer():
			return

		self.__RefreshPVPButtonList()

		if constInfo.PVPMODE_ENABLE:
			net.SendChatPacket("/pkmode 1", chat.CHAT_TYPE_TALKING)
		else:
			chat.AppendChat(chat.CHAT_TYPE_INFO, localeInfo.OPTION_PVPMODE_NOT_SUPPORT)

	def __OnClickPvPModeFreeButton(self):
		if app.ENABLE_MELEY_LAIR_DUNGEON:
			if self.isMeleyMap(player.PK_MODE_FREE):
				return
		if self.__CheckPvPProtectedLevelPlayer():
			return

		self.__RefreshPVPButtonList()

		if constInfo.PVPMODE_ENABLE:
			net.SendChatPacket("/pkmode 2", chat.CHAT_TYPE_TALKING)
		else:
			chat.AppendChat(chat.CHAT_TYPE_INFO, localeInfo.OPTION_PVPMODE_NOT_SUPPORT)

	def __OnClickPvPModeGuildButton(self):
		if app.ENABLE_MELEY_LAIR_DUNGEON:
			if self.isMeleyMap(player.PK_MODE_GUILD):
				return
		if self.__CheckPvPProtectedLevelPlayer():
			return

		self.__RefreshPVPButtonList()

		if 0 == player.GetGuildID():
			chat.AppendChat(chat.CHAT_TYPE_INFO, localeInfo.OPTION_PVPMODE_CANNOT_SET_GUILD_MODE)
			return

		if constInfo.PVPMODE_ENABLE:
			net.SendChatPacket("/pkmode 4", chat.CHAT_TYPE_TALKING)
		else:
			chat.AppendChat(chat.CHAT_TYPE_INFO, localeInfo.OPTION_PVPMODE_NOT_SUPPORT)

	def OnChangePKMode(self):
		self.__RefreshPVPButtonList()

	def __OnChangeMobilePhoneNumber(self):
		global MOBILE
		if not MOBILE:
			return

		import uiCommon
		inputDialog = uiCommon.InputDialog()
		inputDialog.SetTitle(localeInfo.MESSENGER_INPUT_MOBILE_PHONE_NUMBER_TITLE)
		inputDialog.SetMaxLength(13)
		inputDialog.SetAcceptEvent(ui.__mem_func__(self.OnInputMobilePhoneNumber))
		inputDialog.SetCancelEvent(ui.__mem_func__(self.OnCloseInputDialog))
		inputDialog.Open()
		self.inputDialog = inputDialog

	def __OnDeleteMobilePhoneNumber(self):
		global MOBILE
		if not MOBILE:
			return

		import uiCommon
		questionDialog = uiCommon.QuestionDialog()
		questionDialog.SetText(localeInfo.MESSENGER_DO_YOU_DELETE_PHONE_NUMBER)
		questionDialog.SetAcceptEvent(ui.__mem_func__(self.OnDeleteMobile))
		questionDialog.SetCancelEvent(ui.__mem_func__(self.OnCloseQuestionDialog))
		questionDialog.Open()
		self.questionDialog = questionDialog

	def OnInputMobilePhoneNumber(self):
		global MOBILE
		if not MOBILE:
			return

		text = self.inputDialog.GetText()

		if not text:
			return

		text.replace('-', '')
		net.SendChatPacket("/mobile " + text)
		self.OnCloseInputDialog()
		return True

	def OnInputMobileAuthorityCode(self):
		global MOBILE
		if not MOBILE:
			return

		text = self.inputDialog.GetText()
		net.SendChatPacket("/mobile_auth " + text)
		self.OnCloseInputDialog()
		return True

	def OnDeleteMobile(self):
		global MOBILE
		if not MOBILE:
			return

		net.SendChatPacket("/mobile")
		self.OnCloseQuestionDialog()
		return True

	def OnCloseInputDialog(self):
		self.inputDialog.Close()
		self.inputDialog = None
		return True

	def OnCloseQuestionDialog(self):
		self.questionDialog.Close()
		self.questionDialog = None
		return True

	def OnPressEscapeKey(self):
		self.Close()
		return True

	def RefreshMobile(self):
		global MOBILE
		if not MOBILE:
			return

		if player.HasMobilePhoneNumber():
			self.inputMobileButton.Hide()
			self.deleteMobileButton.Show()
		else:
			self.inputMobileButton.Show()
			self.deleteMobileButton.Hide()

	def OnMobileAuthority(self):
		global MOBILE
		if not MOBILE:
			return

		import uiCommon
		inputDialog = uiCommon.InputDialogWithDescription()
		inputDialog.SetTitle(localeInfo.MESSENGER_INPUT_MOBILE_AUTHORITY_TITLE)
		inputDialog.SetDescription(localeInfo.MESSENGER_INPUT_MOBILE_AUTHORITY_DESCRIPTION)
		inputDialog.SetAcceptEvent(ui.__mem_func__(self.OnInputMobileAuthorityCode))
		inputDialog.SetCancelEvent(ui.__mem_func__(self.OnCloseInputDialog))
		inputDialog.SetMaxLength(4)
		inputDialog.SetBoardWidth(310)
		inputDialog.Open()
		self.inputDialog = inputDialog

	def RefreshBlock(self):
		global blockMode
		for i in xrange(len(self.blockButtonList)):
			if 0 != (blockMode & (1 << i)):
				self.blockButtonList[i].Down()
			else:
				self.blockButtonList[i].SetUp()

	def RefreshViewChat(self):
		if systemSetting.IsViewChat():
			self.viewChatButtonList[0].Down()
			self.viewChatButtonList[1].SetUp()
		else:
			self.viewChatButtonList[0].SetUp()
			self.viewChatButtonList[1].Down()

	def RefreshAlwaysShowName(self):
		if systemSetting.IsAlwaysShowName():
			self.alwaysShowNameButtonList[0].Down()
			self.alwaysShowNameButtonList[1].SetUp()
			if constInfo.ITEM_TEXTAIL_OPTION:
				self.alwaysShowNameButtonList[2].SetUp()
		elif constInfo.ITEM_TEXTAIL_OPTION and ONLY_ITEM_TEXTAIL:
			self.alwaysShowNameButtonList[0].SetUp()
			self.alwaysShowNameButtonList[1].SetUp()
			self.alwaysShowNameButtonList[2].Down()
		else:
			self.alwaysShowNameButtonList[0].SetUp()
			self.alwaysShowNameButtonList[1].Down()
			if constInfo.ITEM_TEXTAIL_OPTION:
				self.alwaysShowNameButtonList[2].SetUp()

	def RefreshShowDamage(self):
		if systemSetting.IsShowDamage():
			self.showDamageButtonList[0].Down()
			self.showDamageButtonList[1].SetUp()
		else:
			self.showDamageButtonList[0].SetUp()
			self.showDamageButtonList[1].Down()

	def OnBlockMode(self, mode):
		global blockMode
		blockMode = mode
		self.RefreshBlock()

	def Show(self):
		self.RefreshMobile()
		self.RefreshBlock()
		ui.ScriptWindow.Show(self)
		if app.ENABLE_MELEY_LAIR_DUNGEON:
			self.setMeleyMap()

	def Close(self):
		self.Hide()

	if not constInfo.NEW_PICKUP_FILTER:
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

	def __OnClickItemHighlightOnButton(self):
		cfg.Set(cfg.SAVE_OPTION, "item_highlight", "1")
		self.RefreshItemHighlight()

	def __OnClickItemHighlightOffButton(self):
		cfg.Set(cfg.SAVE_OPTION, "item_highlight", "0")
		self.RefreshItemHighlight()

	def RefreshItemHighlight(self):
		if cfg.Get(cfg.SAVE_OPTION, "item_highlight", "1") == "1":
			self.itemHighlightButtonList[0].Down()
			self.itemHighlightButtonList[1].SetUp()
		else:
			self.itemHighlightButtonList[0].SetUp()
			self.itemHighlightButtonList[1].Down()
		if self.refreshInventoryBagSlot:
			self.refreshInventoryBagSlot()

	def __OnClickGoldPickupChatOnButton(self):
		cfg.Set(cfg.SAVE_OPTION, "gold_pickup_chat", "1")
		self.RefreshGoldPickupChat()

	def __OnClickGoldPickupChatOffButton(self):
		cfg.Set(cfg.SAVE_OPTION, "gold_pickup_chat", "0")
		self.RefreshGoldPickupChat()

	def RefreshGoldPickupChat(self):
		if cfg.Get(cfg.SAVE_OPTION, "gold_pickup_chat", "1") == "1":
			self.goldPickupChatButtonList[0].Down()
			self.goldPickupChatButtonList[1].SetUp()
		else:
			self.goldPickupChatButtonList[0].SetUp()
			self.goldPickupChatButtonList[1].Down()

	if not constInfo.NEW_PICKUP_FILTER:
		def __OnClickPickupAllOnButton(self):
			cfg.Set(cfg.SAVE_OPTION, "pickup_all_fast", "1")
			self.RefreshPickUpAll()

		def __OnClickPickupAllOffButton(self):
			cfg.Set(cfg.SAVE_OPTION, "pickup_all_fast", "0")
			self.RefreshPickUpAll()

		def RefreshPickUpAll(self):
			if cfg.Get(cfg.SAVE_OPTION, "pickup_all_fast", "1") == "1":
				self.pickupAllButtonList[0].Down()
				self.pickupAllButtonList[1].SetUp()
			else:
				self.pickupAllButtonList[0].SetUp()
				self.pickupAllButtonList[1].Down()

	def __OnClickQuestLetterOnButton(self):
		cfg.Set(cfg.SAVE_OPTION, "quest_letter_show", "1")
		self.RefreshQuestLetter()

	def __OnClickQuestLetterOffButton(self):
		cfg.Set(cfg.SAVE_OPTION, "quest_letter_show", "0")
		self.RefreshQuestLetter()

	def RefreshQuestLetter(self):
		if cfg.Get(cfg.SAVE_OPTION, "quest_letter_show", "1") == "1":
			self.questLetterButtonList[0].Down()
			self.questLetterButtonList[1].SetUp()
		else:
			self.questLetterButtonList[0].SetUp()
			self.questLetterButtonList[1].Down()
		self.interfaceHandle.RefreshQuestLetterVisibility()

	def SetRefreshInventoryBagSlotFunc(self, func):
		self.refreshInventoryBagSlot = func

	def RefreshUseNight(self):
		if cfg.Get(cfg.SAVE_OPTION, "use_night", "0") == "1":
			self.useNightButtonList[0].Down()
			self.useNightButtonList[1].SetUp()
			background.SetEnvironmentData(1)
		else:
			self.useNightButtonList[0].SetUp()
			self.useNightButtonList[1].Down()
			background.SetEnvironmentData(0)
			
	def __OnClickUseNightOnButton(self):
		cfg.Set(cfg.SAVE_OPTION, "use_night", "1")
		self.RefreshUseNight()

	def __OnClickUseNightOffButton(self):
		cfg.Set(cfg.SAVE_OPTION, "use_night", "0")
		self.RefreshUseNight()

	def RefreshHideShopAds(self):
		if cfg.Get(cfg.SAVE_OPTION, "hide_auctionshop_title", "1") == "0":
			self.hideShopAdsButtonList[0].Down()
			self.hideShopAdsButtonList[1].SetUp()
		else:
			self.hideShopAdsButtonList[0].SetUp()
			self.hideShopAdsButtonList[1].Down()
			
	def __OnClickHideShopAdsOnButton(self):
		tchat("a")
		cfg.Set(cfg.SAVE_OPTION, "hide_auctionshop_title", "1")
		self.RefreshHideShopAds()
		net.SendChatPacket("/reload_environment")
		chat.AppendChat(1, "Change apply after restart")
		tchat("b")

	def __OnClickHideShopAdsOffButton(self):
		tchat("a")
		cfg.Set(cfg.SAVE_OPTION, "hide_auctionshop_title", "0")
		self.RefreshHideShopAds()
		net.SendChatPacket("/reload_environment")
		chat.AppendChat(1, "Change apply after restart")
		tchat("b")
		
	def __OnChangeHideCostumesOn(self, flag):
		if not constInfo.AUCTION_PREMIUM:
			chat.AppendChat(1, "You need premium for this feature.")
			return

		arr = ["hide_costume_weapon", "hide_costume_armor", "hide_costume_hair", "hide_costume_acce"]
		cfg.Set(cfg.SAVE_PLAYER, arr[flag], "1")
		self.RefreshHideCostumes(True)

	def __OnChangeHideCostumesOff(self, flag):
		arr = ["hide_costume_weapon", "hide_costume_armor", "hide_costume_hair", "hide_costume_acce"]
		cfg.Set(cfg.SAVE_PLAYER, arr[flag], "0")
		self.RefreshHideCostumes(True)

	def RefreshHideCostumes(self, SendCmd = False):
		tchat("RefreshHideCostumes")
		if not constInfo.AUCTION_PREMIUM:
			return
			
		arr = {0:"hide_costume_weapon", 1:"hide_costume_armor", 2:"hide_costume_hair", 3:"hide_costume_acce"}
		cmd = '/set_hide_costumes'
		for i, val in arr.iteritems():
			cur = int(cfg.Get(cfg.SAVE_PLAYER, val, "0"))
			if cur:
				self.hideCostumesButtonList[i].Down()
			else:
				self.hideCostumesButtonList[i].SetUp()
			cmd = cmd + ' %d' % cur
			
		if SendCmd:
			tchat('cmd %s' % cmd)
			net.SendChatPacket(cmd)

		# hideCostumeAcce = int( cfg.Get( cfg.SAVE_PLAYER, "hide_costume_acce", "0" ) == "1" )
	
		# if hideCostumeAcce:
		# 	self.hideCostumesButtonList[3].Down()
		# else:
		# 	self.hideCostumesButtonList[3].SetUp()

		# player.SetHideSashes(hideCostumeAcce)

	if constInfo.ENABLE_CHANGE_TEXTURE_SNOW:
		def __SnowOn(self):
			systemSetting.SetSnowTexturesMode(True)
			self.UpdateSnow()
			if background.GetCurrentMapName():
				snow_maps = [
					"outdoor/a1",
					"outdoor/b1",
					"outdoor/c1"
				]
				snow_maps_textures = {
					"outdoor/a1" : "textureset\metin2_a1_snow.txt",
					"outdoor/b1" : "textureset\metin2_b1_snow.txt",
					"outdoor/c1" : "textureset\metin2_c1_snow.txt", }
				if str(background.GetCurrentMapName()) in snow_maps:
					background.TextureChange(snow_maps_textures[str(background.GetCurrentMapName())])
			background.EnableSnow(1)

		def __SnowOff(self):
			systemSetting.SetSnowTexturesMode(False)
			self.UpdateSnow()
			if background.GetCurrentMapName():
				snow_maps = [
					"outdoor/a1",
					"outdoor/b1",
					"outdoor/c1"
				]
				snow_maps_textures = {
					"outdoor/a1" : "textureset\metin2_a1.txt",
					"outdoor/b1" : "textureset\metin2_b1.txt",
					"outdoor/c1" : "textureset\metin2_c1.txt", }
				if str(background.GetCurrentMapName()) in snow_maps:
					background.TextureChange(snow_maps_textures[str(background.GetCurrentMapName())])
			background.EnableSnow(0)

		def UpdateSnow(self):
			if systemSetting.IsSnowTexturesMode():
				self.snowmode[0].Down()
				self.snowmode[1].SetUp()
			else:
				self.snowmode[0].SetUp()
				self.snowmode[1].Down()

	def RefreshFPS(self):
		for x in xrange(1):
			showFPS = constInfo.SHOW_FPS
			if showFPS:
				self.showFPSButtonList[x].Down()

	def __ShowFPS(self, arg):
		cfg.Set(cfg.SAVE_OPTION, "SHOW_FPS", arg)
		constInfo.SHOW_FPS = arg

	if constInfo.HIDE_NPC_OPTION:
		def RefreshHideNPC(self):
			for x in xrange(3):
				hide = systemSetting.IsHiddenNPC(x)
				if hide:
					self.hideNPCButtonList[x].Down()

		def __HideNPC(self, arg):
			hide = systemSetting.SetHideNPC(arg, True)

		def __ShowNPC(self, arg):
			hide = systemSetting.SetHideNPC(arg, False)

	if constInfo.SAVE_WINDOW_POSITION:
		def __OnClickSaveWndPosBtn(self, arg):
			self.wndSavePosButtons[arg].Down()
			self.wndSavePosButtons[not arg].SetUp()
			cfg.Set(cfg.SAVE_GENERAL, "save_wnd_pos", arg)
