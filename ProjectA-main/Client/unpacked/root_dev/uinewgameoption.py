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
import uiScriptLocale

SMALL_BUTTON	= 45
MIDDLE_BUTTON = 65

ROOT_DIR = "d:/ymir work/ui/game/new_gameoption_ui/"
ROOT_PATH = "d:/ymir work/ui/public/"

blockMode = 0
viewChatMode = 0

MOBILE = False

if constInfo.ITEM_TEXTAIL_OPTION:
	ONLY_ITEM_TEXTAIL = int(cfg.Get(cfg.SAVE_GENERAL, "only_item_textail", "0"))

BUTTON_IMG_DICT = {
	MIDDLE_BUTTON : [ "Middle_Button_01.sub", "Middle_Button_02.sub", "Middle_Button_03.sub" ],
	SMALL_BUTTON : [ "small_Button_01.sub", "small_Button_02.sub", "small_Button_03.sub" ]
}

LOAD = 0

OPTION_LIST = [
	{
		"name" : uiScriptLocale.OPTION_NAME_COLOR,
		"buttons" :
		[
			[ uiScriptLocale.OPTION_NAME_COLOR_NORMAL, "radio_button", MIDDLE_BUTTON ],
			[ uiScriptLocale.OPTION_NAME_COLOR_EMPIRE, "radio_button", MIDDLE_BUTTON ]
		],
	},
	{
		"name" : uiScriptLocale.OPTION_TARGET_BOARD,
		"buttons" :
		[
			[ uiScriptLocale.OPTION_TARGET_BOARD_NO_VIEW, "radio_button", MIDDLE_BUTTON ],
			[ uiScriptLocale.OPTION_TARGET_BOARD_VIEW, "radio_button", MIDDLE_BUTTON ]
		],
	},
	{
		"name" : uiScriptLocale.OPTION_PVPMODE,
		"buttons" :
		[
			[ uiScriptLocale.OPTION_PVPMODE_PEACE, "radio_button", SMALL_BUTTON ],
			[ uiScriptLocale.OPTION_PVPMODE_REVENGE, "radio_button", SMALL_BUTTON ],
			[ uiScriptLocale.OPTION_PVPMODE_GUILD, "radio_button", SMALL_BUTTON ],
			[ uiScriptLocale.OPTION_PVPMODE_FREE, "radio_button", SMALL_BUTTON ],
		],
	},
	{
		"name" : uiScriptLocale.OPTION_BLOCK,
		"buttons" :
		[
			[ uiScriptLocale.OPTION_BLOCK_EXCHANGE, "toggle_button", MIDDLE_BUTTON ],
			[ uiScriptLocale.OPTION_BLOCK_PARTY, "toggle_button", MIDDLE_BUTTON ],
			[ uiScriptLocale.OPTION_BLOCK_GUILD, "toggle_button", MIDDLE_BUTTON ],
			
		],
	},
	{
		"name" : " ",
		"buttons" :
		[
			[ uiScriptLocale.OPTION_BLOCK_WHISPER, "toggle_button", MIDDLE_BUTTON ],
			[ uiScriptLocale.OPTION_BLOCK_FRIEND, "toggle_button", MIDDLE_BUTTON ],
			[ uiScriptLocale.OPTION_BLOCK_PARTY_REQUEST, "toggle_button", MIDDLE_BUTTON ],
			
		],
	},
	{
		"name" : uiScriptLocale.OPTION_VIEW_CHAT,
		"buttons" :
		[
			[ uiScriptLocale.OPTION_VIEW_CHAT_ON, "radio_button", MIDDLE_BUTTON ],
			[ uiScriptLocale.OPTION_VIEW_CHAT_OFF, "radio_button", MIDDLE_BUTTON ],
		],
	},
	{
		"name" : uiScriptLocale.OPTION_ALWAYS_SHOW_NAME,
		"buttons" :
		[
			[ uiScriptLocale.OPTION_ALWAYS_SHOW_NAME_ON, "radio_button", MIDDLE_BUTTON ],
			[ uiScriptLocale.OPTION_ALWAYS_SHOW_NAME_OFF, "radio_button", MIDDLE_BUTTON ],
		],
	},
	{
		"name" : uiScriptLocale.OPTION_EFFECT,
		"buttons" :
		[
			[ uiScriptLocale.OPTION_VIEW_CHAT_ON, "radio_button", MIDDLE_BUTTON ],
			[ uiScriptLocale.OPTION_VIEW_CHAT_OFF, "radio_button", MIDDLE_BUTTON ],
		],
	},
	{
		"name" : uiScriptLocale.OPTION_ITEM_HIGHLIGHT,
		"buttons" :
		[
			[ uiScriptLocale.OPTION_ITEM_HIGHLIGHT_ON, "radio_button", MIDDLE_BUTTON ],
			[ uiScriptLocale.OPTION_ITEM_HIGHLIGHT_OFF, "radio_button", MIDDLE_BUTTON ],
		],
	},
	{
		"name" : uiScriptLocale.OPTION_GOLD_PICKUP,
		"buttons" :
		[
			[ uiScriptLocale.OPTION_GOLD_PICKUP_ON, "radio_button", MIDDLE_BUTTON ],
			[ uiScriptLocale.OPTION_GOLD_PICKUP_OFF, "radio_button", MIDDLE_BUTTON ],
		],
	},
	{
		"name" : uiScriptLocale.OPTION_QUEST_LETTER,
		"buttons" :
		[
			[ uiScriptLocale.OPTION_QUEST_LETTER_SHOW, "radio_button", MIDDLE_BUTTON ],
			[ uiScriptLocale.OPTION_QUEST_LETTER_HIDE, "radio_button", MIDDLE_BUTTON ],
		],
	},
	{
		"name" : uiScriptLocale.OPTION_USENIGHT,
		"buttons" :
		[
			[ uiScriptLocale.OPTION_GOLD_PICKUP_ON, "radio_button", MIDDLE_BUTTON ],
			[ uiScriptLocale.OPTION_GOLD_PICKUP_OFF, "radio_button", MIDDLE_BUTTON ],
		],
	},
	{
		"name" : uiScriptLocale.OPTION_SHOP_TITLE,
		"buttons" :
		[
			[ uiScriptLocale.OPTION_QUEST_LETTER_SHOW, "radio_button", MIDDLE_BUTTON ],
			[ uiScriptLocale.OPTION_QUEST_LETTER_HIDE, "radio_button", MIDDLE_BUTTON ],
		],
	},
	{
		"name" : uiScriptLocale.RENDER_OPT,
		"buttons" :
		[
			[ uiScriptLocale.RENDER_OPT_LOW, "radio_button", MIDDLE_BUTTON ],
			[ uiScriptLocale.RENDER_OPT_MEDIUM, "radio_button", MIDDLE_BUTTON ],
			[ uiScriptLocale.RENDER_OPT_HIGH, "radio_button", MIDDLE_BUTTON ],
		],
	},
]

class OptionDialog(ui.ScriptWindow):
	class Option(ui.Window):
		def Init(self, index, function):
			self.buttonList = {}
			self.buttonNameList = []
			self.Event = function
			
			self.SetSize(277,32)
			
			self.Text = ui.TextLine()
			self.Text.SetParent(self)
			self.Text.SetPosition(10,9)
			self.Text.SetText(OPTION_LIST[index]["name"])
			self.Text.Show()
			
			i = 0
			for BUTTON in OPTION_LIST[index]["buttons"]:
				if BUTTON[0] == "":
					i += 1
					continue
				if BUTTON[1] == "toggle_button":
					button = ui.ToggleButton()
				else:
					button = ui.RadioButton()
				button.SetParent(self)
				button.SetPosition(95+(BUTTON[2]*i), 5)
				button.SetUpVisual(ROOT_PATH+BUTTON_IMG_DICT[BUTTON[2] ][0])
				button.SetOverVisual(ROOT_PATH+BUTTON_IMG_DICT[BUTTON[2] ][1])
				button.SetDownVisual(ROOT_PATH+BUTTON_IMG_DICT[BUTTON[2] ][2])
				if BUTTON[1] == "toggle_button":
					button.SetToggleUpEvent(self.__Function, BUTTON[0], OPTION_LIST[index]["name"], "UP")
					button.SetToggleDownEvent(self.__Function, BUTTON[0], OPTION_LIST[index]["name"], "DOWN")
				else:
					button.SAFE_SetEvent(self.__Function, BUTTON[0], OPTION_LIST[index]["name"], None)
				button.SetText(BUTTON[0])
				button.Show()
				i += 1
				self.buttonList[BUTTON[0]] = button
				self.buttonNameList.append(BUTTON[0])
				
		def RefreshRadioButton(self, index):
			for button in self.buttonList:
				self.buttonList[button].SetUp()
			self.buttonList[self.buttonNameList[index]].SetDown()
			
		def RefreshToggleButton(self, index, arg):
			if arg == "UP":
				self.buttonList[self.buttonNameList[index]].SetUp()
			else:
				self.buttonList[self.buttonNameList[index]].Down()
		
		def __Function(self, index, name, type):
			if type == None:
				for button in self.buttonList:
					self.buttonList[button].SetUp()
				self.buttonList[index].SetDown()
			self.Event(index, name)

	def __init__(self,interfaceHandle):
		ui.ScriptWindow.__init__(self)
		self.interfaceHandle = interfaceHandle
		self.__LoadWindow()

	def __del__(self):
		ui.ScriptWindow.__del__(self)

	def Close(self):
		self.Hide()

	def __Initialize(self):
		self.refreshInventoryBagSlot = None
		self.renderDistances = [15000.0, 5000.0, 1500.0]
		
	def __Refresh(self):
		self.RefreshHideCostumes()
		self.RefreshName()
		self.RefreshViewTarget()
		self.RefreshPvp()
		self.RefreshBlock()
		self.RefreshViewChat()
		self.RefreshAlwaysShowName()
		self.RefreshShowDamage()
		self.RefreshItemHighlight()
		self.RefreshGoldPickupChat()
		self.RefreshQuestLetter()
		self.RefreshUseNight()
		self.RefreshHideShopAds()
		self.RefreshFPS()
		self.RefreshMessengerNotification()
		self.RefreshShopNotification()
		self.RefreshRenderOpt()
		if constInfo.ENABLE_CHANGE_TEXTURE_SNOW:
			self.UpdateSnow()
		if constInfo.HIDE_NPC_OPTION:
			self.RefreshHideNPC()
		if constInfo.SAVE_WINDOW_POSITION:
			self.RefreshSave()
		self.RefreshWhisperTimeStamp()
		self.RefreshWhisperSave()
		if constInfo.AFFECT_GAME_OPTION:
			self.RefreshAffectIcons()

	def __LoadWindow(self):
		self.__Initialize()
		global OPTION_LIST
		try:
			pyScrLoader = ui.PythonScriptLoader()
			pyScrLoader.LoadScriptFile(self, "UIScript/NewGameOptionDialog.py")
		except:
			import exception
			exception.Abort("OptionDialog.LoadWindow.LoadObject")

		self.GetChild("TitleBar").SetCloseEvent(ui.__mem_func__(self.Close))
		self.bg = self.GetChild("board")
		self.SetCenterPosition()
		self.hideCostumesButtonList = []
		self.hideCostumesButtonList.append(self.GetChild("hide_costume_weapon"))
		self.hideCostumesButtonList.append(self.GetChild("hide_costume_armor"))
		self.hideCostumesButtonList.append(self.GetChild("hide_costume_hair"))
		self.hideCostumesButtonList.append(self.GetChild("hide_costume_acce"))
		
		self.hideCostumesButtonList[0].SetToggleDownEvent(self.__OnChangeHideCostumesOn, 0)
		self.hideCostumesButtonList[1].SetToggleDownEvent(self.__OnChangeHideCostumesOn, 1)
		self.hideCostumesButtonList[2].SetToggleDownEvent(self.__OnChangeHideCostumesOn, 2)
		self.hideCostumesButtonList[3].SetToggleDownEvent(self.__OnChangeHideCostumesOn, 3)

		self.hideCostumesButtonList[0].SetToggleUpEvent(self.__OnChangeHideCostumesOff, 0)
		self.hideCostumesButtonList[1].SetToggleUpEvent(self.__OnChangeHideCostumesOff, 1)
		self.hideCostumesButtonList[2].SetToggleUpEvent(self.__OnChangeHideCostumesOff, 2)
		self.hideCostumesButtonList[3].SetToggleUpEvent(self.__OnChangeHideCostumesOff, 3)

		global LOAD
		if LOAD == 0:
			LOAD = 1
			if constInfo.ITEM_TEXTAIL_OPTION:
				OPTION_LIST[6]["buttons"].append([ "Drop", "radio_button", MIDDLE_BUTTON ])
				
			if constInfo.ENABLE_CHANGE_TEXTURE_SNOW:
				OPTION_LIST.append(
					{
						"name" : uiScriptLocale.OPTION_SNOW, 
						"buttons" :[
							[ uiScriptLocale.OPTION_GOLD_PICKUP_ON, "radio_button", MIDDLE_BUTTON ],
							[ uiScriptLocale.OPTION_GOLD_PICKUP_OFF, "radio_button", MIDDLE_BUTTON ]
						],
					}
				)

			if constInfo.HIDE_NPC_OPTION:
				OPTION_LIST.append(
					{
						"name" : uiScriptLocale.OPTION_HIDE_NPC_TITLE, 
						"buttons" :[
							[ uiScriptLocale.OPTION_HIDE_NPC_CAT1, "toggle_button", MIDDLE_BUTTON ],
							[ uiScriptLocale.OPTION_HIDE_NPC_CAT2, "toggle_button", MIDDLE_BUTTON ],
							[ uiScriptLocale.OPTION_HIDE_NPC_CAT3, "toggle_button", MIDDLE_BUTTON ]
						],
					}
				)
				OPTION_LIST.append(
					{
						"name" : "  ", 
						"buttons" :[
							[ uiScriptLocale.OPTION_HIDE_NPC_CAT4, "toggle_button", MIDDLE_BUTTON ],
						],
					}
				)
				
			if constInfo.SAVE_WINDOW_POSITION:
				OPTION_LIST.append(
					{
						"name" : uiScriptLocale.SAVE_WINDOW_POS, 
						"buttons" :[
							[ "", "radio_button", MIDDLE_BUTTON ],
							[ uiScriptLocale.NO, "radio_button", MIDDLE_BUTTON ],
							[ uiScriptLocale.YES, "radio_button", MIDDLE_BUTTON ]
						],
					}
				)
				
			OPTION_LIST.append(
				{
					"name" : uiScriptLocale.OPTION_WHISPER_TIMESTAMP, 
					"buttons" :[
						[ uiScriptLocale.NO, "radio_button", MIDDLE_BUTTON ],
						[ uiScriptLocale.YES, "radio_button", MIDDLE_BUTTON ]
					],
				}
			)
			
			if constInfo.WHISPER_MANAGER:
				OPTION_LIST.append(
					{
						"name" : uiScriptLocale.OPTION_SAVE_WHISPERS, 
						"buttons" :[
							[ uiScriptLocale.NO, "radio_button", MIDDLE_BUTTON ],
							[ uiScriptLocale.YES, "radio_button", MIDDLE_BUTTON ]
						],
					}
				)
				
			if constInfo.AFFECT_GAME_OPTION:
				OPTION_LIST.append(
					{
						"name" : uiScriptLocale.AFFECT_GAME_OPTION, 
						"buttons" :[
							[ uiScriptLocale.OPTION_QUEST_LETTER_SHOW, "radio_button", MIDDLE_BUTTON ],
							[ uiScriptLocale.OPTION_QUEST_LETTER_HIDE, "radio_button", MIDDLE_BUTTON ],
						],
					}
				)
			OPTION_LIST.append(
				{
					"name" : "FPS", 
					"buttons" :[
						[ uiScriptLocale.OPTION_VIEW_CHAT_OFF, "radio_button", MIDDLE_BUTTON ],
						[ uiScriptLocale.OPTION_VIEW_CHAT_ON, "radio_button", MIDDLE_BUTTON ],
					],
				}
			)
			OPTION_LIST.append(
				{
					"name" : uiScriptLocale.OPTION_MESSENGER_NOTIFICATION, 
					"buttons" :[
						[ uiScriptLocale.NO, "radio_button", MIDDLE_BUTTON ],
						[ uiScriptLocale.YES, "radio_button", MIDDLE_BUTTON ],
					],
				}
			)
			OPTION_LIST.append(
				{
					"name" : uiScriptLocale.OPTION_SELL_NOTIFICATION, 
					"buttons" :[
						[ uiScriptLocale.NO, "radio_button", MIDDLE_BUTTON ],
						[ uiScriptLocale.YES, "radio_button", MIDDLE_BUTTON ],
					],
				}
			)

		self.listBox = ui.ListBoxEx()
		self.listBox.SetParent(self.bg)
		self.listBox.SetPosition(5,30)
		self.listBox.SetItemSize(277,32)
		self.listBox.SetItemStep(32)
		self.listBox.SetViewItemCount(13)
		self.listBox.SetScrollBar(self.GetChild("ScrollBar"))
		self.listBox.Show()
		
		self.funcDict = {
			uiScriptLocale.OPTION_NAME_COLOR : {
				uiScriptLocale.OPTION_NAME_COLOR_NORMAL : self.__OnClickNameColorModeNormalButton, 
				uiScriptLocale.OPTION_NAME_COLOR_EMPIRE : self.__OnClickNameColorModeEmpireButton,
			},
			
			uiScriptLocale.OPTION_TARGET_BOARD : {
				uiScriptLocale.OPTION_TARGET_BOARD_NO_VIEW : self.__OnClickTargetBoardViewButton,
				uiScriptLocale.OPTION_TARGET_BOARD_VIEW : self.__OnClickTargetBoardNoViewButton,
			},
			
			uiScriptLocale.OPTION_PVPMODE : {
				uiScriptLocale.OPTION_PVPMODE_PEACE : self.__OnClickPvPModePeaceButton,
				uiScriptLocale.OPTION_PVPMODE_REVENGE : self.__OnClickPvPModeRevengeButton,
				uiScriptLocale.OPTION_PVPMODE_GUILD : self.__OnClickPvPModeGuildButton,
				uiScriptLocale.OPTION_PVPMODE_FREE : self.__OnClickPvPModeFreeButton,
			},
			
			uiScriptLocale.OPTION_BLOCK : {
				uiScriptLocale.OPTION_BLOCK_EXCHANGE : self.__OnClickBlockExchangeButton,
				uiScriptLocale.OPTION_BLOCK_PARTY : self.__OnClickBlockPartyButton,
				uiScriptLocale.OPTION_BLOCK_GUILD : self.__OnClickBlockGuildButton,
			},
			
			" " : {
				uiScriptLocale.OPTION_BLOCK_WHISPER : self.__OnClickBlockWhisperButton,
				uiScriptLocale.OPTION_BLOCK_FRIEND : self.__OnClickBlockFriendButton,
				uiScriptLocale.OPTION_BLOCK_PARTY_REQUEST : self.__OnClickBlockPartyRequest,
			},
			
			uiScriptLocale.OPTION_VIEW_CHAT : {
				uiScriptLocale.OPTION_VIEW_CHAT_OFF : self.__OnClickViewChatOffButton,
				uiScriptLocale.OPTION_VIEW_CHAT_ON : self.__OnClickViewChatOnButton,
			},
			
			 uiScriptLocale.OPTION_ALWAYS_SHOW_NAME : {
				uiScriptLocale.OPTION_ALWAYS_SHOW_NAME_ON : self.__OnClickAlwaysShowNameOnButton,
				uiScriptLocale.OPTION_ALWAYS_SHOW_NAME_OFF : self.__OnClickAlwaysShowNameOffButton,
				"Drop" : self.__OnClickOnlyShowItemOnButton,
			},
			
			uiScriptLocale.OPTION_EFFECT : {
				uiScriptLocale.OPTION_VIEW_CHAT_OFF : self.__OnClickShowDamageOffButton,
				uiScriptLocale.OPTION_VIEW_CHAT_ON : self.__OnClickShowDamageOnButton,
			},
			
			uiScriptLocale.OPTION_ITEM_HIGHLIGHT : {
				uiScriptLocale.OPTION_ITEM_HIGHLIGHT_OFF : self.__OnClickItemHighlightOffButton,
				uiScriptLocale.OPTION_ITEM_HIGHLIGHT_ON : self.__OnClickItemHighlightOnButton,
			},
			
			uiScriptLocale.OPTION_GOLD_PICKUP : {
				uiScriptLocale.OPTION_GOLD_PICKUP_ON : self.__OnClickGoldPickupChatOnButton,
				uiScriptLocale.OPTION_GOLD_PICKUP_OFF : self.__OnClickGoldPickupChatOffButton,
			},
			
			uiScriptLocale.OPTION_QUEST_LETTER : {
				uiScriptLocale.OPTION_QUEST_LETTER_SHOW : self.__OnClickQuestLetterOnButton,
				uiScriptLocale.OPTION_QUEST_LETTER_HIDE : self.__OnClickQuestLetterOffButton,
			},
			
			uiScriptLocale.OPTION_USENIGHT : {
				uiScriptLocale.OPTION_GOLD_PICKUP_ON : self.__OnClickUseNightOnButton,
				uiScriptLocale.OPTION_GOLD_PICKUP_OFF : self.__OnClickUseNightOffButton,
			},
			
			uiScriptLocale.OPTION_SHOP_TITLE : {
				uiScriptLocale.OPTION_QUEST_LETTER_HIDE : self.__OnClickHideShopAdsOnButton,
				uiScriptLocale.OPTION_QUEST_LETTER_SHOW : self.__OnClickHideShopAdsOffButton,
			},
			
			uiScriptLocale.RENDER_OPT : {
				uiScriptLocale.RENDER_OPT_LOW : self.__OnClickLowRenderOpt,
				uiScriptLocale.RENDER_OPT_MEDIUM : self.__OnClickMediumRenderOpt,
				uiScriptLocale.RENDER_OPT_HIGH : self.__OnClickHighRenderOpt,
			},
			
			uiScriptLocale.OPTION_SNOW : {
				uiScriptLocale.OPTION_GOLD_PICKUP_ON : self.__SnowOn,
				uiScriptLocale.OPTION_GOLD_PICKUP_OFF : self.__SnowOff,
			},
			
			uiScriptLocale.OPTION_HIDE_NPC_TITLE : {
				uiScriptLocale.OPTION_HIDE_NPC_CAT1 : self.__HideBuffis,
				uiScriptLocale.OPTION_HIDE_NPC_CAT2 : self.__HideMounts,
				uiScriptLocale.OPTION_HIDE_NPC_CAT3 : self.__HidePets,
			},

			"  " : {
				uiScriptLocale.OPTION_HIDE_NPC_CAT4 : self.__HideShops,
			},
			
			uiScriptLocale.SAVE_WINDOW_POS : {
				uiScriptLocale.NO : self.__OnClickSaveWndPosOff,
				uiScriptLocale.YES : self.__OnClickSaveWndPosOn,
			},
			
			uiScriptLocale.OPTION_WHISPER_TIMESTAMP : {
				uiScriptLocale.NO : self.__OnClickTimeWhsiper,
				uiScriptLocale.YES : self.__OnClickTimeWhsiper,
			},
			
			uiScriptLocale.OPTION_SAVE_WHISPERS : {
				uiScriptLocale.NO : self.__OnClickSaveWhsiper,
				uiScriptLocale.YES : self.__OnClickSaveWhsiper,
			},
			
			uiScriptLocale.AFFECT_GAME_OPTION : {
				uiScriptLocale.OPTION_QUEST_LETTER_SHOW : self.__OnClickToggleAffects,
				uiScriptLocale.OPTION_QUEST_LETTER_HIDE : self.__OnClickToggleAffects,
			},

			"FPS" : {
				uiScriptLocale.OPTION_VIEW_CHAT_OFF : self.__OnClickToggleFPS,
				uiScriptLocale.OPTION_VIEW_CHAT_ON : self.__OnClickToggleFPS,
			},
			uiScriptLocale.OPTION_MESSENGER_NOTIFICATION : {
				uiScriptLocale.NO : self.__OnClickToggleMessengerNotification,
				uiScriptLocale.YES : self.__OnClickToggleMessengerNotification,
			},
			uiScriptLocale.OPTION_SELL_NOTIFICATION : {
				uiScriptLocale.NO : self.__OnClickToggleSellNotification,
				uiScriptLocale.YES : self.__OnClickToggleSellNotification,
			},
		}
		
		for x in xrange(len(OPTION_LIST)):
			option = self.Option()
			option.Init(x,self.Function)
			option.Show()
			self.listBox.AppendItem(option)
		
		self.__Refresh()

	def __OnClickSaveWhsiper(self):
		if cfg.Get(cfg.SAVE_OPTION, "save_whisper", "1") == "1":
			cfg.Set(cfg.SAVE_OPTION, "save_whisper", "0")
		else:
			cfg.Set(cfg.SAVE_OPTION, "save_whisper", "1")

	def __OnClickToggleAffects(self):
		if cfg.Get(cfg.SAVE_OPTION, "hide_affects", "1") == "1":
			self.interfaceHandle.wndAffect.Open()
			cfg.Set(cfg.SAVE_OPTION, "hide_affects", "0")
		else:
			self.interfaceHandle.wndAffect.Close()
			cfg.Set(cfg.SAVE_OPTION, "hide_affects", "1")

	def __OnClickToggleFPS(self):
		fpsState = int(cfg.Get(cfg.SAVE_OPTION, "SHOW_FPS", "0"))
		if fpsState == 0:
			constInfo.SHOW_FPS = 1
		else:
			constInfo.SHOW_FPS = 0
		cfg.Set(cfg.SAVE_OPTION, "SHOW_FPS", constInfo.SHOW_FPS)

	def __OnClickToggleMessengerNotification(self):
		notifState = int(cfg.Get(cfg.SAVE_OPTION, "SHOW_MESSENGER_NOTIFICATION", "1"))
		if notifState == 0:
			constInfo.SHOW_MESSENGER_NOTIFICATION = 1
		else:
			constInfo.SHOW_MESSENGER_NOTIFICATION = 0
		cfg.Set(cfg.SAVE_OPTION, "SHOW_MESSENGER_NOTIFICATION", constInfo.SHOW_MESSENGER_NOTIFICATION)

	def __OnClickToggleSellNotification(self):
		notifState = int(cfg.Get(cfg.SAVE_OPTION, "SHOW_SELL_NOTIFICATION", "1"))
		if notifState == 0:
			notifState = 1
		else:
			notifState = 0
		cfg.Set(cfg.SAVE_OPTION, "SHOW_SELL_NOTIFICATION", notifState)

	def __OnClickTimeWhsiper(self):
		if cfg.Get(cfg.SAVE_OPTION, "whisper_timestamp", "0") == "1":
			cfg.Set(cfg.SAVE_OPTION, "whisper_timestamp", "0")
		else:
			cfg.Set(cfg.SAVE_OPTION, "whisper_timestamp", "1")

	def __OnClickSaveWndPosOff(self):
		cfg.Set(cfg.SAVE_GENERAL, "save_wnd_pos", "0")

	def Function(self, index, name):
		func = self.funcDict[name][index]
		func()

	def RefreshAffectIcons(self):
		self.listBox.GetItemAtIndex(19+1).RefreshRadioButton(int(cfg.Get(cfg.SAVE_OPTION, "hide_affects", "1")))

	def RefreshWhisperSave(self):
		self.listBox.GetItemAtIndex(18+1).RefreshRadioButton(int(cfg.Get(cfg.SAVE_OPTION, "save_whisper", "1")))

	def RefreshWhisperTimeStamp(self):
		self.listBox.GetItemAtIndex(17+1).RefreshRadioButton(int(cfg.Get(cfg.SAVE_OPTION, "whisper_timestamp", "0")))

	def RefreshSave(self):
		saved = int(cfg.Get(cfg.SAVE_GENERAL, "save_wnd_pos", "0"))
		self.listBox.GetItemAtIndex(16+1).RefreshRadioButton(saved)

	def RefreshHideNPC(self):
		for x in xrange(4):
			hide = systemSetting.IsHiddenNPC(x)
			if hide:
				self.listBox.GetItemAtIndex(15 if x < 3 else 16).RefreshToggleButton(x if x < 3 else 0, "DOWN")
			else:
				self.listBox.GetItemAtIndex(15 if x < 3 else 16).RefreshToggleButton(x if x < 3 else 0, "UP")

	def UpdateSnow(self):
		if systemSetting.IsSnowTexturesMode():
			self.listBox.GetItemAtIndex(14).RefreshRadioButton(0)
		else:
			self.listBox.GetItemAtIndex(14).RefreshRadioButton(1)

	def RefreshRenderOpt(self):
		cur = float(cfg.Get(cfg.SAVE_OPTION, "perf_tree_range", self.renderDistances[2]))
		for i in xrange(len(self.renderDistances)):
			if cur >= self.renderDistances[i]:
				if i == 0 or i > 0 and cur < self.renderDistances[i-1]:
					self.listBox.GetItemAtIndex(13).RefreshRadioButton(i)

	def RefreshHideShopAds(self):
		if cfg.Get(cfg.SAVE_OPTION, "hide_auctionshop_title", "1") == "1":
			self.listBox.GetItemAtIndex(12).RefreshRadioButton(1)
		else:
			self.listBox.GetItemAtIndex(12).RefreshRadioButton(0)

	def RefreshFPS(self):
		self.listBox.GetItemAtIndex(20+1).RefreshRadioButton(int(cfg.Get(cfg.SAVE_OPTION, "SHOW_FPS", "0")))

	def RefreshMessengerNotification(self):
		self.listBox.GetItemAtIndex(21+1).RefreshRadioButton(int(cfg.Get(cfg.SAVE_OPTION, "SHOW_MESSENGER_NOTIFICATION", "1")))

	def RefreshShopNotification(self):
		self.listBox.GetItemAtIndex(22+1).RefreshRadioButton(int(cfg.Get(cfg.SAVE_OPTION, "SHOW_SELL_NOTIFICATION", "1")))

	def RefreshUseNight(self):
		if cfg.Get(cfg.SAVE_OPTION, "use_night", "0") == "1":
			self.listBox.GetItemAtIndex(11).RefreshRadioButton(0)
		else:
			self.listBox.GetItemAtIndex(11).RefreshRadioButton(1)

	def RefreshQuestLetter(self):
		if cfg.Get(cfg.SAVE_OPTION, "quest_letter_show", "1") == "1":
			self.listBox.GetItemAtIndex(10).RefreshRadioButton(0)
		else:
			self.listBox.GetItemAtIndex(10).RefreshRadioButton(1)

	def RefreshGoldPickupChat(self):
		if cfg.Get(cfg.SAVE_OPTION, "gold_pickup_chat", "1") == "1":
			self.listBox.GetItemAtIndex(9).RefreshRadioButton(0)
		else:
			self.listBox.GetItemAtIndex(9).RefreshRadioButton(1)
			
	def RefreshItemHighlight(self):
		if cfg.Get(cfg.SAVE_OPTION, "item_highlight", "1") == "1":
			self.listBox.GetItemAtIndex(8).RefreshRadioButton(0)
		else:
			self.listBox.GetItemAtIndex(8).RefreshRadioButton(1)
			
	def RefreshShowDamage(self):
		if systemSetting.IsShowDamage():
			self.listBox.GetItemAtIndex(7).RefreshRadioButton(0)
		else:
			self.listBox.GetItemAtIndex(7).RefreshRadioButton(1)

	def RefreshAlwaysShowName(self):
		if systemSetting.IsAlwaysShowName():
			self.listBox.GetItemAtIndex(6).RefreshRadioButton(0)
		elif constInfo.ITEM_TEXTAIL_OPTION and ONLY_ITEM_TEXTAIL:
			self.listBox.GetItemAtIndex(6).RefreshRadioButton(2)
		else:
			self.listBox.GetItemAtIndex(6).RefreshRadioButton(1)

	def RefreshViewChat(self):
		if systemSetting.IsViewChat():
			self.listBox.GetItemAtIndex(5).RefreshRadioButton(0)
		else:
			self.listBox.GetItemAtIndex(5).RefreshRadioButton(1)

	def RefreshBlock(self):
		global blockMode
		for i in xrange(3):
			if 0 != (blockMode & (1 << i)):
				self.listBox.GetItemAtIndex(3).RefreshToggleButton(i, "DOWN")
			else:
				self.listBox.GetItemAtIndex(3).RefreshToggleButton(i, "UP")

		for i in xrange(3):
			if 0 != (blockMode & (1 << (i+3))):
				self.listBox.GetItemAtIndex(4).RefreshToggleButton(i, "DOWN")
			else:
				self.listBox.GetItemAtIndex(4).RefreshToggleButton(i, "UP")

	def RefreshViewTarget(self):
		self.listBox.GetItemAtIndex(1).RefreshRadioButton(constInfo.GET_VIEW_OTHER_EMPIRE_PLAYER_TARGET_BOARD())

	def RefreshName(self):
		self.listBox.GetItemAtIndex(0).RefreshRadioButton(constInfo.GET_CHRNAME_COLOR_INDEX())

	def RefreshPvp(self):
		if player.GetPKMode() == 4:
			self.listBox.GetItemAtIndex(2).RefreshRadioButton(2)
		elif player.GetPKMode() == 2:
			self.listBox.GetItemAtIndex(2).RefreshRadioButton(3)
		else:
			self.listBox.GetItemAtIndex(2).RefreshRadioButton(player.GetPKMode())

	def __OnClickSaveWndPosOn(self):
		cfg.Set(cfg.SAVE_GENERAL, "save_wnd_pos", "1")

	def __OnClickSaveWndPosOff(self):
		cfg.Set(cfg.SAVE_GENERAL, "save_wnd_pos", "0")

	def __ToggleNPC(self, arg):
		hideNPCIndexes = constInfo.HIDE_NPC_INDEXES

		if hideNPCIndexes.has_key(arg):
			if systemSetting.IsHiddenNPC(hideNPCIndexes[arg]):
				systemSetting.SetHideNPC(hideNPCIndexes[arg], False)
				cfg.Set(cfg.SAVE_OPTION, arg, 0)
			else:
				systemSetting.SetHideNPC(hideNPCIndexes[arg], True)
				cfg.Set(cfg.SAVE_OPTION, arg, 1)

	def __HideBuffis(self):
		self.__ToggleNPC("HIDE_NPC_BUFFI")
		
	def __HideMounts(self):
		self.__ToggleNPC("HIDE_NPC_MOUNT")
		
	def __HidePets(self):
		self.__ToggleNPC("HIDE_NPC_PET")

	def __HideShops(self):
		self.__ToggleNPC("HIDE_NPC_SHOP")
		
	def __SnowOn(self):
		systemSetting.SetSnowTexturesMode(True)
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

	def __OnClickRenderOpt(self, flag):
		cfg.Set(cfg.SAVE_OPTION, "perf_tree_range", self.renderDistances[flag])
		cfg.Set(cfg.SAVE_OPTION, "perf_gravel_range", self.renderDistances[flag])
		cfg.Set(cfg.SAVE_OPTION, "perf_effect_range", self.renderDistances[flag])
		cfg.Set(cfg.SAVE_OPTION, "perf_shop_range", self.renderDistances[flag])
		background.SetForceRefreshTree()
		background.SetForceRefreshGravel()
		background.RefreshShopRange()

	def __OnClickLowRenderOpt(self):
		self.__OnClickRenderOpt(0)
		
	def __OnClickMediumRenderOpt(self):
		self.__OnClickRenderOpt(1)
		
	def __OnClickHighRenderOpt(self):
		self.__OnClickRenderOpt(2)

	def __OnClickHideShopAdsOnButton(self):
		cfg.Set(cfg.SAVE_OPTION, "hide_auctionshop_title", "1")
		# net.SendChatPacket("/reload_environment")
		# chat.AppendChat(1, "Change apply after restart")
		constInfo.SHOP_SHOW_LIMIT_RANGE = 0

	def __OnClickHideShopAdsOffButton(self):
		cfg.Set(cfg.SAVE_OPTION, "hide_auctionshop_title", "0")
		# net.SendChatPacket("/reload_environment")
		# chat.AppendChat(1, "Change apply after restart")
		constInfo.SHOP_SHOW_LIMIT_RANGE = 1000

	def __OnClickUseNightOnButton(self):
		cfg.Set(cfg.SAVE_OPTION, "use_night", "1")
		background.SetEnvironmentData(1)

	def __OnClickUseNightOffButton(self):
		cfg.Set(cfg.SAVE_OPTION, "use_night", "0")
		background.SetEnvironmentData(0)

	def __OnClickQuestLetterOnButton(self):
		cfg.Set(cfg.SAVE_OPTION, "quest_letter_show", "1")
		self.interfaceHandle.RefreshQuestLetterVisibility()

	def __OnClickQuestLetterOffButton(self):
		cfg.Set(cfg.SAVE_OPTION, "quest_letter_show", "0")
		self.interfaceHandle.RefreshQuestLetterVisibility()

	def __OnClickGoldPickupChatOnButton(self):
		cfg.Set(cfg.SAVE_OPTION, "gold_pickup_chat", "1")

	def __OnClickGoldPickupChatOffButton(self):
		cfg.Set(cfg.SAVE_OPTION, "gold_pickup_chat", "0")

	def __OnClickItemHighlightOnButton(self):
		cfg.Set(cfg.SAVE_OPTION, "item_highlight", "1")
		if self.refreshInventoryBagSlot:
			self.refreshInventoryBagSlot()

	def __OnClickItemHighlightOffButton(self):
		cfg.Set(cfg.SAVE_OPTION, "item_highlight", "0")
		if self.refreshInventoryBagSlot:
			self.refreshInventoryBagSlot()

	def SetRefreshInventoryBagSlotFunc(self, func):
		self.refreshInventoryBagSlot = func

	def __OnClickBlockExchangeButton(self):
		global blockMode
		net.SendChatPacket("/setblockmode " + str(blockMode ^ player.BLOCK_EXCHANGE))
	def __OnClickBlockPartyButton(self):
		global blockMode
		net.SendChatPacket("/setblockmode " + str(blockMode ^ player.BLOCK_PARTY))
	def __OnClickBlockGuildButton(self):
		global blockMode
		net.SendChatPacket("/setblockmode " + str(blockMode ^ player.BLOCK_GUILD))
	def __OnClickBlockWhisperButton(self):
		global blockMode
		net.SendChatPacket("/setblockmode " + str(blockMode ^ player.BLOCK_WHISPER))
	def __OnClickBlockFriendButton(self):
		global blockMode
		net.SendChatPacket("/setblockmode " + str(blockMode ^ player.BLOCK_FRIEND))
	def __OnClickBlockPartyRequest(self):
		global blockMode
		net.SendChatPacket("/setblockmode " + str(blockMode ^ player.BLOCK_PARTY_REQUEST))
	def __SetNameColorMode(self, index):
		constInfo.SET_CHRNAME_COLOR_INDEX(index)

	def __SetTargetBoardViewMode(self, flag):
		constInfo.SET_VIEW_OTHER_EMPIRE_PLAYER_TARGET_BOARD(flag)

	def __OnClickNameColorModeNormalButton(self):
		self.__SetNameColorMode(0)

	def __OnClickNameColorModeEmpireButton(self):
		self.__SetNameColorMode(1)

	def __OnClickTargetBoardViewButton(self):
		self.__SetTargetBoardViewMode(0)

	def __OnClickTargetBoardNoViewButton(self):
		self.__SetTargetBoardViewMode(1)

	def __OnClickPvPModePeaceButton(self):
		if app.ENABLE_MELEY_LAIR_DUNGEON:
			if self.isMeleyMap(player.PK_MODE_PEACE):
				return
		if self.__CheckPvPProtectedLevelPlayer():
			return

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

		if 0 == player.GetGuildID():
			chat.AppendChat(chat.CHAT_TYPE_INFO, localeInfo.OPTION_PVPMODE_CANNOT_SET_GUILD_MODE)
			return

		if constInfo.PVPMODE_ENABLE:
			net.SendChatPacket("/pkmode 4", chat.CHAT_TYPE_TALKING)
		else:
			chat.AppendChat(chat.CHAT_TYPE_INFO, localeInfo.OPTION_PVPMODE_NOT_SUPPORT)

	def __CheckPvPProtectedLevelPlayer(self):	
		if player.GetStatus(player.LEVEL)<constInfo.PVPMODE_PROTECTED_LEVEL:
			self.__SetPeacePKMode()
			chat.AppendChat(chat.CHAT_TYPE_INFO, localeInfo.OPTION_PVPMODE_PROTECT % (constInfo.PVPMODE_PROTECTED_LEVEL))
			return 1

		return 0

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

	def OnBlockMode(self, mode):
		global blockMode
		blockMode = mode

	def Destroy(self):
		self.ClearDictionary()

	def __OnClickViewChatOnButton(self):
		global viewChatMode
		viewChatMode = 1
		systemSetting.SetViewChatFlag(viewChatMode)
	def __OnClickViewChatOffButton(self):
		global viewChatMode
		viewChatMode = 0
		systemSetting.SetViewChatFlag(viewChatMode)

	def __OnClickOnlyShowItemOnButton(self):
		if constInfo.ITEM_TEXTAIL_OPTION:
			global ONLY_ITEM_TEXTAIL
			ONLY_ITEM_TEXTAIL = 1
			systemSetting.SetAlwaysShowNameFlag(False)
			cfg.Set(cfg.SAVE_GENERAL, "only_item_textail", "1")

	def __OnClickAlwaysShowNameOnButton(self):
		if constInfo.ITEM_TEXTAIL_OPTION:
			global ONLY_ITEM_TEXTAIL
			ONLY_ITEM_TEXTAIL = 0
			cfg.Set(cfg.SAVE_GENERAL, "only_item_textail", "0")
		systemSetting.SetAlwaysShowNameFlag(True)

	def __OnClickAlwaysShowNameOffButton(self):
		if constInfo.ITEM_TEXTAIL_OPTION:
			global ONLY_ITEM_TEXTAIL
			ONLY_ITEM_TEXTAIL = 0
			cfg.Set(cfg.SAVE_GENERAL, "only_item_textail", "0")
		systemSetting.SetAlwaysShowNameFlag(False)

	def __OnClickShowDamageOnButton(self):
		systemSetting.SetShowDamageFlag(True)

	def __OnClickShowDamageOffButton(self):
		systemSetting.SetShowDamageFlag(False)

	def __OnClickItemHighlightButton(self):
		cfg.Set(cfg.SAVE_OPTION, "item_highlight", "1")
		
	def OnMouseWheel(self, len):
		lineCount = self.listBox.GetItemCount()
		if self.IsInPosition():
			dir = constInfo.WHEEL_TO_SCROLL(len)
			new_pos = self.GetChild("ScrollBar").GetPos() + ((1.0 / lineCount) * dir)
			new_pos = max(0.0, new_pos)
			new_pos = min(1.0, new_pos)
			self.GetChild("ScrollBar").SetPos(new_pos)
			return True
		return False
		
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
		if __SERVER__ == 2:
			self.hideCostumesButtonList[3].Hide()

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

	def OnChangePKMode(self):
		pass