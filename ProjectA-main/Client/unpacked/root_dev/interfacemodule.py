# SYSTEM
import os

# BUILTIN
import app
import cfg
import net
import shop
import chat
import event
import guild
import player
import wndMgr
import miniMap
import safebox
import systemSetting

# LOCAL
import constInfo
import localeInfo
import item

import uiRank

# INTERFACE
import ui
import uiTip
import uiAcce
import uiCube
import uiGaya
import uiShop
import uiChat
import uiHelp
import uiEvent
import uiCards
import uiGuild
import uiQuest
import uiParty
import uiAnimal
import uiCommon
import uiRefine
import uiSystem
import uiWhisper
import uiTaskBar
import uiRestart
import uiToolTip
import uiMiniMap
import uiSafebox
import uiAuction
import auction
import uiExchange
import uiFakeBuff
import uiAttrTree
import uiCharacter
import uiInventory
import uiMessenger
import uiGameButton
import uiSelectItem
import uiPointReset
import uiItemRefund
import uiDragonSoul
import uiShopSearch
import uiMaintenance
import uiSystemAnnounce
import uiEquipmentDialog
import uiPrivateShopBuilder
import uimasthp
import uieventicon
import uiPlantHp
import uieventannouncement
import uiFractionWar
import uiBattlePass
if app.ENABLE_ZODIAC:
	import uizodiacanimasphere
if constInfo.NEW_QUEST_TIMER:
	import uinewtimer

if app.ENABLE_MELEY_LAIR_DUNGEON:
	import uidragonlairranking

if app.ENABLE_COSTUME_BONUS_TRANSFER:
	import uiCostumeBonusTransfer

if constInfo.NEW_SWITCHBOT_ENABLED:
	import uiSwitchbot2

if constInfo.ENABLE_DMG_METER:
	import uiDmgMeter

import uiblackjack

# RUNE
if constInfo.RUNE_ENABLED:
	import uiRune
# END_OF_RUNE

if app.AHMET_FISH_EVENT_SYSTEM:
	import uiMiniGameFishEvent

if constInfo.ENABLE_XMAS_EVENT:
	import uiXmasEvent

if constInfo.ENABLE_RUNE_PAGES:
	import rune

if constInfo.ENABLE_EQUIPMENT_CHANGER:
	import uiEquipmentChanger

import uiSoulSystem
import uiAffectShower
if constInfo.WHISPER_MANAGER:
	import whispermgr

import uiQuestTask

if constInfo.ENABLE_REACT_EVENT:
	import uiReactEvent

if constInfo.ENABLE_WHEEL_OF_FRIGHT:
	import uiWheelOfFright

if constInfo.ENABLE_BATTLEPASS:
	import uiBattlePass

class Interface(object):
	CHARACTER_STATUS_TAB = 1
	CHARACTER_SKILL_TAB = 2

	def __init__(self):
		systemSetting.SetInterfaceHandler(self)
		self.windowOpenPosition = 0
		self.dlgWhisperWithoutTarget = None
		self.inputDialog = None
		self.tipBoard = None
		self.bigBoard = None
		if app.ENABLE_ZODIAC:
			self.zodiacBoard = None
			self.wndAnimasphere = None
		if app.ENABLE_HYDRA_DUNGEON:
			self.wndMastHp = None
		self.wndPlantHp = None

		self.refreshCooldowns = False

		# ITEM_MALL
		self.mallPageDlg = None
		# END_OF_ITEM_MALL

		self.wndWeb = None
		self.wndTaskBar = None
		self.wndCharacter = None
		self.wndInventory = None
		self.wndBlackJack = None
		self.wndChat = None
		self.wndMessenger = None
		self.wndMiniMap = None
		self.wndGuild = None
		self.wndGuildBuilding = None
		# ACCE
		self.wndAcce = None
		# END_OF_ACCE
		self.wndSoulRefine = None
		# MAINTENANCE
		self.wndMaintenance = None
		# END_OF_MAINTENANCE
		self.wndSysAnnounce = None
		# ITEM_REFUND
		self.wndItemRefund = None
		# END_OF_ITEM_REFUND
		# AUCTION_SHOP
		self.wndAuction = None
		self.wndAuctionShop = None
		self.wndAuctionGuestShop = None
		self._open_auction_on_refresh = False
		# END_OF_AUCTION_SHOP
		self.wndPet = None
		self.wndMount = None
		# self.wndSideBar = None
		# SWITCHBOT
		self.wndSwitchbot = None
		# END_OF_SWITCHBOT
		self.wndDragonSoul = None
		self.wndDragonSoulRefine = None
		# SHOP_SEARCH
		self.wndShopSearch = None
		# END_OF_SHOP_SEARCH
		# FAKEBUFF
		self.wndFakeBuffSkill = None
		# END_OF_FAKEBUFF
		# ATTRTREE
		self.wndAttrTree = None
		# END_OF_ATTRTREE
		# EVENT_SYSTEM
		self.wndEventJoin = None
		self.wndEventEmpireWarScoreBoard = None
		# END_OF_EVENT_SYSTEM
		if app.ENABLE_COSTUME_BONUS_TRANSFER:
			self.wndCostumeBonusTransfer = None

		self.wndHorseUpgrade = None
		self.wndGayaShop = None
		self.wndNewTimer = None

		# RUNE
		if constInfo.RUNE_ENABLED:
			self.wndRuneMain = None
			self.wndRuneSub = None
		# END_OF_RUNE

		# AFFECT_SHOWER
		self.wndAffect = None
		# END_AFFECT_SHOWER

		if constInfo.ENABLE_CRYSTAL_SYSTEM:
			self.wndCrystalRefineQuestion = None

		self.wndNotificationWindow = [None] * len(uinewtimer.TimerWindow.QUESTS)

		self.battlepassTimeout = {}

		self.listGMName = {}
		self.wndQuestWindow = []
		self.privateShopAdvertisementBoardDict = {}
		self.guildScoreBoardDict = {}
		self.equipmentDialogDict = {}
		event.SetInterfaceWindow(self)

		self.lastUpdateTime = 0

		self.wndEventIcon = None
		self.eventAnnouncementWnd = None

		if constInfo.ENABLE_XMAS_EVENT:
			self.wndXmasEventIcon = None

		if constInfo.ENABLE_EQUIPMENT_CHANGER:
			self.wndEquipmentChanger = None

		# TEST ONLY
		self.wndJigsaw		= None
		self.wndJigsawIcon	= None

		self.wndMovieMaker = None

		if constInfo.ENABLE_ANGELSDEMONS_EVENT:
			self.wndAngelsDemonsSelect = None

		if constInfo.ENABLE_XMAS_EVENT:
			self.wndXmasEvent = None

		if constInfo.ENABLE_DMG_METER:
			self.wndDmgMeter = None
		self.questTaskWnd = None

		if constInfo.ENABLE_REACT_EVENT:
			self.wndReactEvent = None

		if constInfo.ENABLE_WHEEL_OF_FRIGHT:
			self.wndWheelOfFright = None

		if constInfo.NEW_QUEST_TIMER:
			self.wndNewTimer = None

		if constInfo.ENABLE_BATTLEPASS:
			self.wndBattlePass = None

	def __del__(self):
		systemSetting.DestroyInterfaceHandler()
		event.SetInterfaceWindow(None)

	################################
	## Make Windows & Dialogs
	def __MakeUICurtain(self):
		wndUICurtain = ui.Bar("TOP_MOST")
		wndUICurtain.SetSize(wndMgr.GetScreenWidth(), wndMgr.GetScreenHeight())
		wndUICurtain.SetColor(0x77000000)
		wndUICurtain.Hide()
		self.wndUICurtain = wndUICurtain

	def __MakeMessengerWindow(self):
		self.wndMessenger = uiMessenger.MessengerWindow()
		
		from _weakref import proxy
		self.wndMessenger.SetWhisperButtonEvent(lambda n,i=proxy(self):i.OpenWhisperDialog(n))
		self.wndMessenger.SetGuildButtonEvent(ui.__mem_func__(self.ToggleGuildWindow))

	def __MakeGuildWindow(self):
		self.wndGuild = uiGuild.GuildWindow()

	def __MakeChatWindow(self):
		CHAT_WINDOW_WIDTH = 600
		wndChat = uiChat.ChatWindow()
		if app.GetSelectedDesignName() != "illumina":
			wndChat.SetSize(CHAT_WINDOW_WIDTH, 25)
			wndChat.SetPosition(wndMgr.GetScreenWidth()/2 - CHAT_WINDOW_WIDTH/2, wndMgr.GetScreenHeight() - wndChat.GetHeight() - 37)
		else:
			wndChat.SetSize(wndChat.CHAT_WINDOW_WIDTH, 0)	#CHAT HIGHT FROM BOTTOM EDIT HERE STYLE
			wndChat.SetPosition(wndMgr.GetScreenWidth()/2 - wndChat.CHAT_WINDOW_WIDTH/2 - 12, wndMgr.GetScreenHeight() - wndChat.EDIT_LINE_HEIGHT - 49 - 8)
		wndChat.SetHeight(200)
		wndChat.Refresh()
		wndChat.Show()

		self.wndChat = wndChat
		self.wndChat.BindInterface(self)
		self.wndChat.SetSendWhisperEvent(ui.__mem_func__(self.OpenWhisperDialogWithoutTarget))
		self.wndChat.SetOpenChatLogEvent(ui.__mem_func__(self.ToggleChatLogWindow))

	def __MakeTaskBar(self):
		wndTaskBar = uiTaskBar.TaskBar()
		wndTaskBar.LoadWindow()
		self.wndTaskBar = wndTaskBar

	def __MakeParty(self):
		wndParty = uiParty.PartyWindow()
		wndParty.Hide()
		self.wndParty = wndParty
		self.wndParty.BindInterface(self)

	def __MakeGameButtonWindow(self):
		wndGameButton = uiGameButton.GameButtonWindow()
		wndGameButton.SetTop()
		wndGameButton.Show()
		wndGameButton.SetButtonEvent("STATUS", ui.__mem_func__(self.__OnClickStatusPlusButton))
		wndGameButton.SetButtonEvent("SKILL", ui.__mem_func__(self.__OnClickSkillPlusButton))
		wndGameButton.SetButtonEvent("QUEST", ui.__mem_func__(self.__OnClickQuestButton))
		wndGameButton.SetButtonEvent("HELP", ui.__mem_func__(self.__OnClickHelpButton))
		wndGameButton.SetButtonEvent("BUILD", ui.__mem_func__(self.__OnClickBuildButton))
		wndGameButton.SetButtonEvent("BUILD", ui.__mem_func__(self.__OnClickBuildButton))

		self.wndGameButton = wndGameButton

	#def ShowChatColorButton(self):
	#	self.wndGameButton.ShowChatColorButton()

	#def HideChatColorButton(self):
	#	self.wndGameButton.HideChatColorButton()

	def __IsChatOpen(self):
		return True
		
	def __MakeWindows(self):
		import dbg

		# dbg.TraceError(":: wndCharacter", dbg.IsEnabled())
		wndCharacter = uiCharacter.CharacterWindow(self)
		# dbg.TraceError(" :: wndInventory", dbg.IsEnabled())
		wndInventory = uiInventory.InventoryWindow()		
		wndInventory.BindInterface(self)
		# dbg.TraceError(" :: wndMiniMap", dbg.IsEnabled())

		wndBlackJack = uiblackjack.Table()
		wndMiniMap = uiMiniMap.MiniMap()
		if constInfo.NEW_MINIMAP_UI:
			wndMiniMap.BindInterface(self)
		# dbg.TraceError(" :: wndSafebox", dbg.IsEnabled())
		wndSafebox = uiSafebox.SafeboxWindow(self)
		if app.ENABLE_DRAGON_SOUL_SYSTEM:
			wndDragonSoul = uiDragonSoul.DragonSoulWindow()	
			wndDragonSoulRefine = uiDragonSoul.DragonSoulRefineWindow()
			wndDragonSoul.SetRefineOpenFunc(ui.__mem_func__(wndDragonSoulRefine.Show))
		else:
			wndDragonSoul = None
			wndDragonSoulRefine = None

		# GUILD_SAFEBOX
		# dbg.TraceError(" :: wndGuildSafebox", dbg.IsEnabled())
		wndGuildSafebox = uiSafebox.GuildSafeboxWindow(self)
		self.wndGuildSafebox = wndGuildSafebox
		# END_OF_GUILD_SAFEBOX

		wndInventory.SAFE_SetSidebarButtonEvent(wndInventory.SIDEBAR_BTN_STORAGE, self.ToggleSafeboxWindow)
		wndInventory.SAFE_SetSidebarButtonEvent(wndInventory.SIDEBAR_BTN_AUCTION, self.ToggleShopSearchWindow)
		wndInventory.SAFE_SetSidebarButtonEvent(wndInventory.SIDEBAR_BTN_SWITCHBOT, self.ToggleSwitchbotWindow)

		wndInventory.SAFE_SetAuctionShopEvent(self.__OnClickAuctionShopButton)

		wndInventory.SetCTRLClickItemEvent(ui.__mem_func__(self.__OnCTRLClickInventoryItem))
		wndSafebox.SetCTRLClickItemEvent(wndSafebox.BUTTON_NORMAL, ui.__mem_func__(self.__OnCTRLClickSafeboxItem))
		wndSafebox.SetCTRLClickItemEvent(wndSafebox.BUTTON_MALL, ui.__mem_func__(self.__OnCTRLClickMallItem))
		wndSafebox.SetCTRLClickItemEvent(wndSafebox.BUTTON_UPP, ui.__mem_func__(self.__OnCTRLClickInvSafeboxItem))
		wndSafebox.SetCTRLClickItemEvent(wndSafebox.BUTTON_SKILL, ui.__mem_func__(self.__OnCTRLClickInvSafeboxItem))
		wndSafebox.SetCTRLClickItemEvent(wndSafebox.BUTTON_STONE, ui.__mem_func__(self.__OnCTRLClickInvSafeboxItem))
		wndSafebox.SetCTRLClickItemEvent(wndSafebox.BUTTON_ENCHANT, ui.__mem_func__(self.__OnCTRLClickInvSafeboxItem))
		wndSafebox.SetCTRLClickItemEvent(wndSafebox.BUTTON_COSTUME, ui.__mem_func__(self.__OnCTRLClickInvSafeboxItem))

		wndGuildSafebox.SetCTRLClickItemEvent(ui.__mem_func__(self.__OnCTRLClickGuildSafeboxItem))

		# dbg.TraceError(" :: wndChatLog", dbg.IsEnabled())
		wndChatLog = uiChat.ChatLogWindow()
		wndChatLog.BindInterface(self)

		# EVENT_SYSTEM
		wndEventJoin = uiEvent.EventJoinDialog()
		self.wndEventJoin = wndEventJoin
		wndEventEmpireWarScoreBoard = uiEvent.EmpireWarScoreBoard()
		self.wndEventEmpireWarScoreBoard = wndEventEmpireWarScoreBoard
		# END_OF_EVENT_SYSTEM
		
		self.wndCharacter = wndCharacter
		self.wndInventory = wndInventory
		self.wndBlackJack = wndBlackJack
		self.wndMiniMap = wndMiniMap
		self.wndSafebox = wndSafebox
		self.wndDragonSoul = wndDragonSoul
		self.wndDragonSoulRefine = wndDragonSoulRefine
		self.wndChatLog = wndChatLog

		if __SERVER__ == 2:
			self.wndRank = None
		else:
			self.wndRank = uiRank.RankWindow()

		self.wndChFaction = uiFractionWar.FactionWindow()
		self.wndChooseFaction = uiFractionWar.ChooseFactionWindow()
		
		if app.ENABLE_DRAGON_SOUL_SYSTEM:
			self.wndDragonSoul.SetDragonSoulRefineWindow(self.wndDragonSoulRefine)
			self.wndDragonSoulRefine.SetInventoryWindows(self.wndInventory, self.wndDragonSoul)
			self.wndInventory.SetDragonSoulRefineWindow(self.wndDragonSoulRefine)

		if app.ENABLE_COSTUME_BONUS_TRANSFER:
			self.wndCostumeBonusTransfer = uiCostumeBonusTransfer.CostumeBonusTransferWindow()
			self.wndCostumeBonusTransfer.LoadWindow()
		if app.ENABLE_ZODIAC:
			if __SERVER__ == 2:
				self.wndAnimasphere = None
			else:
				self.wndAnimasphere = uizodiacanimasphere.AnimasphereZI()
			
		if constInfo.NEW_QUEST_TIMER:

			if not self.wndNewTimer:
				self.wndNewTimer = uinewtimer.TimerWindow()
				self.wndNewTimer.Close()

			for i in range(0, len(self.wndNewTimer.QUESTS)):
				if self.wndNewTimer.QUESTS[i] == None:
					continue
				self.wndNotificationWindow[i] = uinewtimer.NotificationWindow(self.wndNewTimer.QUESTS[i][0], i)
				self.wndNotificationWindow[i].Close()

			self.refreshCooldowns = True

		if app.ENABLE_HYDRA_DUNGEON:
			self.wndMastHp = uimasthp.MastBoard()
			self.wndMastHp.Hide()

		self.wndPlantHp = uiPlantHp.MastBoard()
		self.wndPlantHp.Hide()

		self.wndEventIcon = uieventicon.EventIconShower()
		self.wndEventIcon.BindInterface(self)
		self.wndEventIcon.Close()
		
		if constInfo.ENABLE_DMG_METER:
			self.wndDmgMeter = uiDmgMeter.DmgMeter()
			self.wndDmgMeter.Init()
			self.wndDmgMeter.BindInterface(self)

		if constInfo.ENABLE_XMAS_EVENT:
			self.wndXmasEvent = uiXmasEvent.XmasEventWindow()
			self.wndXmasEventIcon = uieventicon.EventIconShower()
			self.wndXmasEventIcon.Close()
			self.wndXmasEventIcon.BindInterface(self)

		if constInfo.ENABLE_REACT_EVENT:
			self.wndReactEvent = uiReactEvent.ReactEventWindow()

		if constInfo.ENABLE_WHEEL_OF_FRIGHT:
			self.wndWheelOfFright = uiWheelOfFright.WheelOfFrightWindow()

		if constInfo.ENABLE_BATTLEPASS:
			self.wndBattlePass = uiBattlePass.BattlePassWindow()

	def __MakeDialogs(self):
		self.dlgExchange = uiExchange.ExchangeDialog()
		self.dlgExchange.LoadDialog()
		self.dlgExchange.SetCenterPosition()
		self.dlgExchange.Hide()

		self.dlgPointReset = uiPointReset.PointResetDialog()
		self.dlgPointReset.LoadDialog()
		self.dlgPointReset.Hide()

		self.dlgShop = uiShop.ShopDialog()
		self.dlgShop.LoadDialog()
		self.dlgShop.Hide()

		self.dlgRestart = uiRestart.RestartDialog()
		self.dlgRestart.LoadDialog()
		self.dlgRestart.Hide()

		self.dlgSystem = uiSystem.SystemDialog(self)
		self.dlgSystem.LoadDialog()

		self.dlgSystem.Hide()

		self.hyperlinkItemTooltip = uiToolTip.HyperlinkItemToolTip()
		self.hyperlinkItemTooltip.Hide()

		self.tooltipItem = uiToolTip.ItemToolTip()
		self.tooltipItem.Hide()

		self.tooltipSkill = uiToolTip.SkillToolTip()
		self.tooltipSkill.Hide()

		self.privateShopBuilder = uiPrivateShopBuilder.PrivateShopBuilder()
		self.privateShopBuilder.Hide()

		self.dlgRefineNew = uiRefine.RefineDialogNew()
		self.dlgRefineNew.SetSearchShopFunc(ui.__mem_func__(self.StartShopSearchByVnum))
		self.dlgRefineNew.Hide()

	def __MakeHelpWindow(self):
		self.wndHelp = uiHelp.HelpWindow()
		self.wndHelp.LoadDialog()
		self.wndHelp.SetCloseEvent(ui.__mem_func__(self.CloseHelpWindow))
		self.wndHelp.Hide()

	def __MakeTipBoard(self):
		self.tipBoard = uiTip.TipBoard()
		self.tipBoard.Hide()

		self.bigBoard = uiTip.BigBoard()
		self.bigBoard.Hide()
		if app.ENABLE_ZODIAC:
			self.zodiacBoard = uiTip.ZodiacBoard()
			self.zodiacBoard.Hide()
	def __MakeWebWindow(self):
		if constInfo.IN_GAME_SHOP_ENABLE:
			import uiWeb
			self.wndWeb = uiWeb.WebWindow()
			self.wndWeb.LoadWindow()
			self.wndWeb.Hide()

	if app.ENABLE_MELEY_LAIR_DUNGEON:
		def __MakeMeleyRanking(self):
			self.wndMeleyRanking = uidragonlairranking.Window()
			self.wndMeleyRanking.LoadWindow()
			self.wndMeleyRanking.Hide()

	def __MakeCubeWindow(self):
		self.wndCube = uiCube.CubeWindow()
		self.wndCube.LoadWindow()
		self.wndCube.Hide()

	def __MakeCubeResultWindow(self):
		self.wndCubeResult = uiCube.CubeResultWindow()
		self.wndCubeResult.LoadWindow()
		self.wndCubeResult.Hide()

	# ACCESSORY_REFINE_ADD_METIN_STONE
	def __MakeItemSelectWindow(self):
		self.wndItemSelect = uiSelectItem.SelectItemWindow()
		self.wndItemSelect.Hide()
	# END_OF_ACCESSORY_REFINE_ADD_METIN_STONE

	def __MakeCardsInfoWindow(self):
		self.wndCardsInfo = uiCards.CardsInfoWindow()
		self.wndCardsInfo.LoadWindow()
		self.wndCardsInfo.Hide()
	
	def __MakeCardsWindow(self):
		self.wndCards = uiCards.CardsWindow()
		self.wndCards.LoadWindow()
		self.wndCards.Hide()
	
	def __MakeCardsIconWindow(self):
		self.wndCardsIcon = uiCards.IngameWindow()
		self.wndCardsIcon.LoadWindow()
		self.wndCardsIcon.Hide()

	def __MakeSideBar(self):
		return
		# self.wndSideBar = uiSideBar.SideBar()
		# if app.GetSelectedDesignName() != "illumina":
		#	xPos = -self.wndSideBar.X_POS + 1
		# else:
		#	xPos = -self.wndSideBar.X_POS + 1 - 7
		# self.wndSideBar.SetPosition(xPos, self.wndSideBar.GetTop())

		# self.wndSideBar.SetEnableCheckFunc(uiSideBar.BUTTON_GUILD_SAFEBOX, safebox.IsGuildEnabled)
		# self.wndSideBar.SetEnableCheckFunc(uiSideBar.BUTTON_MOUNT, ui.__mem_func__(self.CanOpenMountWindow))
		# self.wndSideBar.SetEnableCheckFunc(uiSideBar.BUTTON_PET, ui.__mem_func__(self.CanOpenPetWindow))

		# self.wndSideBar.SetButtonFunc(uiSideBar.BUTTON_SAFEBOX, ui.__mem_func__(self.RequestOpenSafeboxWindow))
		# self.wndSideBar.SetButtonFunc(uiSideBar.BUTTON_SWITCHBOT, ui.__mem_func__(self.ToggleSwitchbotWindow))
		# self.wndSideBar.SetButtonFunc(uiSideBar.BUTTON_GUILD_SAFEBOX, ui.__mem_func__(self.RequestOpenGuildSafeboxWindow))
		# self.wndSideBar.SetButtonFunc(uiSideBar.BUTTON_MOUNT, ui.__mem_func__(self.ToggleMountWindow))
		# self.wndSideBar.SetButtonFunc(uiSideBar.BUTTON_PET, ui.__mem_func__(self.TogglePetWindow))

		# self.wndSideBar.Refresh()
		# self.wndSideBar.LoadConfig()

	def MakeInterface(self):

		self.__MakeMessengerWindow()
		self.__MakeGuildWindow()
		self.__MakeChatWindow()
		self.__MakeParty()
		self.__MakeWindows()
		self.__MakeDialogs()
		self.__MakeUICurtain()
		self.__MakeTaskBar()
		self.__MakeGameButtonWindow()
		self.__MakeHelpWindow()
		self.__MakeTipBoard()
		self.__MakeWebWindow()
		self.__MakeCubeWindow()
		self.__MakeCubeResultWindow()
		self.__MakeCardsInfoWindow()
		self.__MakeCardsWindow()
		self.__MakeCardsIconWindow()

		if app.ENABLE_MELEY_LAIR_DUNGEON:
			self.__MakeMeleyRanking()

		# ACCESSORY_REFINE_ADD_METIN_STONE
		self.__MakeItemSelectWindow()
		# END_OF_ACCESSORY_REFINE_ADD_METIN_STONE

		# dbg.TraceError("__MakeSideBar", dbg.IsEnabled())
		# self.__MakeSideBar()

		self.questButtonList = []
		self.whisperButtonList = []
		self.whisperDialogDict = {}
		self.privateShopAdvertisementBoardDict = {}

		self.wndInventory.SetItemToolTip(self.tooltipItem)
		self.wndSafebox.SetItemToolTip(self.tooltipItem)
		self.wndCube.SetItemToolTip(self.tooltipItem)
		self.wndCubeResult.SetItemToolTip(self.tooltipItem)
		if app.ENABLE_DRAGON_SOUL_SYSTEM:
			self.wndDragonSoul.SetItemToolTip(self.tooltipItem)
			self.wndDragonSoulRefine.SetItemToolTip(self.tooltipItem)

		if app.ENABLE_COSTUME_BONUS_TRANSFER:
			self.wndCostumeBonusTransfer.SetItemToolTip(self.tooltipItem)

		# GUILD_SAFEBOX
		self.wndGuildSafebox.SetItemToolTip(self.tooltipItem)
		# END_OF_GUILD_SAFEBOX

		self.wndCharacter.SetSkillToolTip(self.tooltipSkill)
		self.wndTaskBar.SetItemToolTip(self.tooltipItem)
		self.wndTaskBar.SetSkillToolTip(self.tooltipSkill)
		self.wndGuild.SetSkillToolTip(self.tooltipSkill)

		# ACCESSORY_REFINE_ADD_METIN_STONE
		self.wndItemSelect.SetItemToolTip(self.tooltipItem)
		# END_OF_ACCESSORY_REFINE_ADD_METIN_STONE

		self.dlgShop.SetItemToolTip(self.tooltipItem)
		self.dlgExchange.SetItemToolTip(self.tooltipItem)
		self.privateShopBuilder.SetItemToolTip(self.tooltipItem)

		self.__InitWhisper()
		self.DRAGON_SOUL_IS_QUALIFIED = True

		if constInfo.NEW_SWITCHBOT_ENABLED and constInfo.switchbotSave:
			self.wndSwitchbot = constInfo.switchbotSave
			
		# AFFECT_SHOWER
		self.wndAffect = uiAffectShower.AffectShower()
		# END_AFFECT_SHOWER

		if __SERVER__ == 2:
			self.wndRuneMain = None
			self.wndRuneSub = None
		else:
			self.wndRuneMain = uiRune.RuneMainWindow(self.OpenRuneSubWindow)
			self.wndRuneSub = uiRune.RuneSubWindow(self.OpenRuneMainWindow)

		if constInfo.ENABLE_BATTLEPASS:
			if self.wndBattlePass:
				self.wndBattlePass.SetItemToolTip(self.tooltipItem)

	def AnswerOpenLink(self, answer):
		if not self.OpenLinkQuestionDialog:
			return

		self.OpenLinkQuestionDialog.Close()
		self.OpenLinkQuestionDialog = None
		if not answer:
			return
		link = constInfo.link
		os.system(link)

	def MakeHyperlinkTooltip(self, hyperlink):
		tokens = hyperlink.split(":")
		if tokens and len(tokens):
			type = tokens[0]
			if "item" == type:
				self.hyperlinkItemTooltip.SetHyperlinkItem(tokens)
			elif "web" == type and (tokens[1].startswith("httpXxX") or tokens[1].startswith("httpsXxX")):
				whitelisted = False
				constInfo.link = "start " + tokens[1].replace("XxX", "://").replace("&","^&")
				for link in constInfo.LINK_WHITELIST:
					if link in constInfo.link:
						whitelisted = True
						break
				if not whitelisted:
					OpenLinkQuestionDialog = uiCommon.QuestionDialogMultiLine()
					OpenLinkQuestionDialog.SetText(localeInfo.CHAT_OPEN_LINK_DANGER)
					OpenLinkQuestionDialog.SetAcceptEvent(lambda arg=True: self.AnswerOpenLink(arg))
					OpenLinkQuestionDialog.SetCancelEvent(lambda arg=False: self.AnswerOpenLink(arg))
					OpenLinkQuestionDialog.Open()
					self.OpenLinkQuestionDialog = OpenLinkQuestionDialog
				else:
					os.system("start " + tokens[1].replace("XxX", "://"))
			elif "sysweb" == type:
				os.system("start " + tokens[1].replace("XxX", "://"))
			elif "qw" == type:
				if len(tokens[1]) > 0:
					if (app.IsPressed(app.DIK_LCONTROL) or app.IsPressed(app.DIK_RCONTROL)) and player.IsGameMaster():
						import utils
						os.system("start " + "https://" + constInfo.DOMAIN + "/?s=gm^&player=" + utils.quote_plus(tokens[1]))
					elif player.GetName() != tokens[1]:
						self.OpenWhisperDialog(str(tokens[1]))

	def SetBattlepassTimeout(self, catIdx, timeout):
		catIdx = int(catIdx)
		if timeout == 0:
			del self.battlepassTimeout[catIdx]
		else:
			self.battlepassTimeout[catIdx] = app.GetTime() + int(timeout)

	def GetBattlepassTimeLeft(self, catIdx):
		timeLeft = self.battlepassTimeout.get(catIdx, 0) - app.GetTime()
		if timeLeft < 0:
			return 0
		return timeLeft

	## Make Windows & Dialogs
	################################

	def Close(self):

		constInfo.NEW_QUEST_TIMER_LAST_SOUND = 0

		uiPrivateShopBuilder.ClearADBoard()

		if self.dlgWhisperWithoutTarget:
			self.dlgWhisperWithoutTarget.Destroy()
			del self.dlgWhisperWithoutTarget

		if uiQuest.QuestDialog.__dict__.has_key("QuestCurtain"):
			uiQuest.QuestDialog.QuestCurtain.Close()

		if self.wndQuestWindow:
			for eachQuestWindow in self.wndQuestWindow:
				eachQuestWindow.nextCurtainMode = -1
				eachQuestWindow.CloseSelf()
				eachQuestWindow = None

		if self.wndChat:
			self.wndChat.Destroy()

		if self.wndTaskBar:
			self.wndTaskBar.Destroy()

		if self.wndCharacter:
			self.wndCharacter.Destroy()

		if self.wndInventory:
			self.wndInventory.Destroy()

		if self.wndBlackJack:
			self.wndBlackJack.Destroy()

		if self.dlgExchange:
			self.dlgExchange.Destroy()

		if self.dlgPointReset:
			self.dlgPointReset.Destroy()

		if self.dlgShop:
			self.dlgShop.Destroy()

		if self.dlgRestart:
			self.dlgRestart.Destroy()

		if self.dlgSystem:
			self.dlgSystem.Destroy()

		if self.wndMiniMap:
			self.wndMiniMap.Destroy()

		if self.wndSafebox:
			self.wndSafebox.Destroy()

		if self.wndWeb:
			self.wndWeb.Destroy()
			self.wndWeb = None

		# GUILD_SAFEBOX
		if self.wndGuildSafebox:
			self.wndGuildSafebox.Destroy()
		# END_OF_GUILD_SAFEBOX

		if self.wndParty:
			self.wndParty.Destroy()

		if self.wndHelp:
			self.wndHelp.Destroy()

		if app.ENABLE_MELEY_LAIR_DUNGEON and self.wndMeleyRanking:
			self.wndMeleyRanking.Destroy()

		# RUNE
		if constInfo.RUNE_ENABLED:
			if self.wndRuneMain:
				self.wndRuneMain.Destroy()

			if self.wndRuneSub:
				self.wndRuneSub.Destroy()
		# END_OF_RUNE

		if self.wndCube:
			self.wndCube.Destroy()

		if self.wndCubeResult:
			self.wndCubeResult.Destroy()

		if self.wndMessenger:
			self.wndMessenger.Destroy()

		if self.wndGuild:
			self.wndGuild.Destroy()

		if self.privateShopBuilder:
			self.privateShopBuilder.Destroy()

		if self.dlgRefineNew:
			self.dlgRefineNew.Destroy()

		if self.wndGuildBuilding:
			self.wndGuildBuilding.Destroy()

		if self.wndGameButton:
			self.wndGameButton.Destroy()
		if app.ENABLE_ZODIAC:
			if self.wndAnimasphere:
				self.wndAnimasphere.Destroy()
		# ITEM_MALL
		if self.mallPageDlg:
			self.mallPageDlg.Destroy()
		# END_OF_ITEM_MALL

		# ACCESSORY_REFINE_ADD_METIN_STONE
		if self.wndItemSelect:
			self.wndItemSelect.Destroy()
		# END_OF_ACCESSORY_REFINE_ADD_METIN_STONE

		self.wndChatLog.Destroy()
		for btn in self.questButtonList:
			btn.SetEvent(0)
		for btn in self.whisperButtonList:
			btn.SetEvent(0)
		for dlg in self.whisperDialogDict.itervalues():
			dlg.Destroy()
		for brd in self.guildScoreBoardDict.itervalues():
			brd.Destroy()
		for dlg in self.equipmentDialogDict.itervalues():
			dlg.Destroy()
		
		# ACCE
		if self.wndAcce:
			self.wndAcce.Destroy()
		# END_OF_ACCE

		# MAINTENANCE
		if self.wndMaintenance:
			self.wndMaintenance.Destroy()
		# END_OF_MAINTENANCE

		if self.wndSysAnnounce:
			self.wndSysAnnounce.Destroy()

		# ITEM_REFUND
		if self.wndItemRefund:
			self.wndItemRefund.Destroy()
		# END_OF_ITEM_REFUND

		# AUCTION_SHOP
		if self.wndAuction:
			self.wndAuction.Destroy()
		if self.wndAuctionShop:
			self.wndAuctionShop.Destroy()
		if self.wndAuctionGuestShop:
			self.wndAuctionGuestShop.Destroy()
		# END_OF_AUCTION_SHOP

		if self.wndPet:
			self.wndPet.Destroy()

		if self.wndMount:
			self.wndMount.Destroy()

		# if self.wndSideBar:
		#	self.wndSideBar.Destroy()

		# SWITCHBOT
		if self.wndSwitchbot:
			if constInfo.NEW_SWITCHBOT_ENABLED:
				constInfo.switchbotSave = self.wndSwitchbot
				self.wndSwitchbot.Close()
			else:
				self.wndSwitchbot.Destroy()
		# END_OF_SWITCHBOT
			
		if self.wndDragonSoul:
			self.wndDragonSoul.Destroy()

		if self.wndDragonSoulRefine:
			self.wndDragonSoulRefine.Destroy()

		if self.wndHorseUpgrade:
			self.wndHorseUpgrade.Destroy()

		if self.wndGayaShop:
			self.wndGayaShop.Destroy()

		# SHOP_SEARCH
		if self.wndShopSearch:
			self.wndShopSearch.Destroy()
		# END_OF_SHOP_SEARCH
		
		if self.wndCardsInfo:
			self.wndCardsInfo.Destroy()

		if self.wndEventIcon:
			# Close -> wndEventDesc
			self.wndEventIcon.Close()
			self.wndEventIcon.Destroy()

		if constInfo.ENABLE_XMAS_EVENT:
			if self.wndXmasEventIcon:
				self.wndXmasEventIcon.Close()
				self.wndXmasEventIcon.Destroy()

		if constInfo.ENABLE_EQUIPMENT_CHANGER:
			if self.wndEquipmentChanger:
				self.wndEquipmentChanger.Close()
				self.wndEquipmentChanger.Destroy()

		if self.wndCards:
			self.wndCards.Destroy()

		if self.wndCardsIcon:
			self.wndCardsIcon.Destroy()

		# FAKEBUFF
		if self.wndFakeBuffSkill:
			self.wndFakeBuffSkill.Destroy()
			if constInfo.CHANGE_SKILL_COLOR:
				self.wndFakeBuffSkill.Destroy2()
		# END_OF_FAKEBUFF

		# ATTRTREE
		if self.wndAttrTree:
			self.wndAttrTree.Destroy()
		# END_OF_ATTRTREE

		# EVENT_SYSTEM
		if self.wndEventJoin:
			self.wndEventJoin.Destroy()
		if self.wndEventEmpireWarScoreBoard:
			self.wndEventEmpireWarScoreBoard.Destroy()
		# END_OF_EVENT_SYSTEM

		if app.ENABLE_COSTUME_BONUS_TRANSFER:
			self.wndCostumeBonusTransfer.Destroy()

		# ITEM_MALL
		del self.mallPageDlg
		# END_OF_ITEM_MALL

		if app.ENABLE_HYDRA_DUNGEON:

			if self.wndMastHp:
				self.wndMastHp.Destroy()
				del self.wndMastHp

		if self.wndPlantHp:
			self.wndPlantHp.Destroy()
			del self.wndPlantHp

		if self.wndMovieMaker:
			self.wndMovieMaker.Destroy()

		if constInfo.ENABLE_REACT_EVENT:
			if self.wndReactEvent:
				self.wndReactEvent.Destroy()
				del self.wndReactEvent

		if constInfo.ENABLE_WHEEL_OF_FRIGHT:
			if self.wndWheelOfFright:
				self.wndWheelOfFright.Destroy()
				del self.wndWheelOfFright

		if constInfo.NEW_QUEST_TIMER:
			if self.wndNewTimer:
				self.wndNewTimer.Destroy()
				del self.wndNewTimer

		if app.ENABLE_ZODIAC:
			if self.wndAnimasphere:
				self.wndAnimasphere.Destroy()
				self.wndAnimasphere = None

		if constInfo.ENABLE_BATTLEPASS:
			if self.wndBattlePass:
				self.wndBattlePass.Destroy()
				del self.wndBattlePass

		del self.wndMovieMaker
		del self.wndGuild
		del self.wndMessenger
		del self.wndUICurtain
		del self.wndChat
		del self.wndTaskBar
		del self.wndCharacter
		del self.wndInventory
		del self.wndBlackJack
		del self.dlgExchange
		del self.dlgPointReset
		del self.dlgShop
		del self.dlgRestart
		del self.dlgSystem
		del self.hyperlinkItemTooltip
		del self.tooltipItem
		del self.tooltipSkill
		del self.wndMiniMap
		del self.wndSafebox
		# GUILD_SAFEBOX
		del self.wndGuildSafebox
		# END_OF_GUILD_SAFEBOX
		del self.wndParty
		del self.wndHelp
		del self.wndCube
		del self.wndCubeResult
		del self.privateShopBuilder
		del self.inputDialog
		del self.wndChatLog
		del self.dlgRefineNew
		del self.wndGuildBuilding
		del self.wndGameButton
		del self.tipBoard
		del self.bigBoard
		del self.wndItemSelect
		if app.ENABLE_ZODIAC:
			del self.zodiacBoard
			if self.wndAnimasphere:
				del self.wndAnimasphere
		del self.wndEventIcon

		if constInfo.ENABLE_DMG_METER:
			del self.wndDmgMeter
		
		if constInfo.ENABLE_XMAS_EVENT:
			del self.wndXmasEventIcon

		if constInfo.ENABLE_EQUIPMENT_CHANGER:
			del self.wndEquipmentChanger

		if app.ENABLE_MELEY_LAIR_DUNGEON:
			del self.wndMeleyRanking

		# ACCE
		del self.wndAcce
		# END_OF_ACCE

		del self.wndSoulRefine

		# MAINTENANCE
		del self.wndMaintenance
		# END_OF_MAINTENANCE
		del self.wndSysAnnounce

		# ITEM_REFUND
		del self.wndItemRefund
		# END_OF_ITEM_REFUND

		# AUCTION_SHOP
		del self.wndAuction
		del self.wndAuctionShop
		del self.wndAuctionGuestShop
		# END_OF_AUCTION_SHOP

		# RUNE
		if constInfo.RUNE_ENABLED:
			del self.wndRuneMain
			del self.wndRuneSub
		# END_OF_RUNE

		del self.wndPet
		del self.wndMount
		# del self.wndSideBar

		# AFFECT_SHOWER
		self.wndAffect.ClearAllAffects()
		del self.wndAffect
		# END_AFFECT_SHOWER

		# SWITCHBOT
		del self.wndSwitchbot
		# END_OF_SWITCHBOT

		if self.wndDragonSoul:
			del self.wndDragonSoul
		if self.wndDragonSoulRefine:
			del self.wndDragonSoulRefine

		del self.wndHorseUpgrade

		# SHOP_SEARCH
		del self.wndShopSearch
		# END_OF_SHOP_SEARCH
		del self.wndCardsInfo
		del self.wndCards
		del self.wndCardsIcon

		# FAKEBUFF
		del self.wndFakeBuffSkill
		# END_OF_FAKEBUFF

		# ATTRTREE
		del self.wndAttrTree
		# END_OF_ATTRTREE

		# EVENT_SYSTEM
		del self.wndEventJoin
		del self.wndEventEmpireWarScoreBoard
		# END_OF_EVENT_SYSTEM

		if app.ENABLE_COSTUME_BONUS_TRANSFER:
			del self.wndCostumeBonusTransfer

		for notificationWindow in self.wndNotificationWindow:
			if notificationWindow:
				notificationWindow.Close()
				notificationWindow.Destroy()
				del notificationWindow

		if self.eventAnnouncementWnd:
			self.eventAnnouncementWnd.Close()
			del self.eventAnnouncementWnd

		if self.wndJigsaw:
			self.wndJigsaw.Close()
			del self.wndJigsaw

		if self.wndJigsawIcon:
			self.wndJigsawIcon.Hide()
			del self.wndJigsawIcon

		if constInfo.ENABLE_ANGELSDEMONS_EVENT:
			if self.wndAngelsDemonsSelect:
				self.wndAngelsDemonsSelect.Close()
				del self.wndAngelsDemonsSelect

		if constInfo.ENABLE_XMAS_EVENT:
			self.wndXmasEvent.Destroy()
			del self.wndXmasEvent

		self.questButtonList = []
		self.whisperButtonList = []
		self.whisperDialogDict = {}
		self.privateShopAdvertisementBoardDict = {}
		self.guildScoreBoardDict = {}
		self.equipmentDialogDict = {}

		uiChat.DestroyChatInputSetWindow()
		
		if constInfo.ENABLE_CRYSTAL_SYSTEM:
			self.CloseCrystalRefine()
		
		if self.wndRank:
			self.wndRank.Destroy()

		if self.wndChFaction:
			self.wndChFaction.Destroy()

		if self.wndChooseFaction:
			self.wndChooseFaction.Destroy()

		del self.wndRank
		del self.wndChFaction
		del self.wndChooseFaction
		del self.questTaskWnd

	def OnKeyUp(self, key):
		if self.wndInventory:
			self.wndInventory.OnKeyUp(key)

	def GetMastHpWindow(self):
		if not self.wndMastHp:
			self.wndMastHp = uimasthp.MastBoard()
			self.wndMastHp.Hide()

		return self.wndMastHp

	def GetPlantHpWindow(self):
		if not self.wndPlantHp:
			self.wndPlantHp = uiPlantHp.MastBoard()
			self.wndPlantHp.Hide()

		return self.wndPlantHp

	## Skill
	def OnUseSkill(self, slotIndex, coolTime):
		self.wndCharacter.OnUseSkill(slotIndex, coolTime)
		self.wndTaskBar.OnUseSkill(slotIndex, coolTime)
		self.wndGuild.OnUseSkill(slotIndex, coolTime)

	def OnActivateSkill(self, slotIndex):
		self.wndCharacter.OnActivateSkill(slotIndex)
		self.wndTaskBar.OnActivateSkill(slotIndex)

	def OnDeactivateSkill(self, slotIndex):
		self.wndCharacter.OnDeactivateSkill(slotIndex)
		self.wndTaskBar.OnDeactivateSkill(slotIndex)

	def OnChangeCurrentSkill(self, skillSlotNumber):
		self.wndTaskBar.OnChangeCurrentSkill(skillSlotNumber)

	def SelectMouseButtonEvent(self, dir, event):
		self.wndTaskBar.SelectMouseButtonEvent(dir, event)

	## Refresh
	def RefreshAlignment(self):
		self.wndCharacter.RefreshAlignment()

	def RefreshStatus(self):
		self.wndTaskBar.RefreshStatus()
		self.wndCharacter.RefreshStatus()
		if self.wndGayaShop:
			self.wndGayaShop.Refresh()
		if app.ENABLE_DRAGON_SOUL_SYSTEM:
			self.wndDragonSoul.RefreshStatus()

	def RefreshStamina(self):
		self.wndTaskBar.RefreshStamina()

	def RefreshSkill(self):
		self.wndCharacter.RefreshSkill()
		self.wndTaskBar.RefreshSkill()

	def RefreshInventory(self):
		self.wndTaskBar.RefreshQuickSlot()
		self.wndInventory.RefreshItemSlot()
		self.wndSafebox.Refresh()
		if app.ENABLE_DRAGON_SOUL_SYSTEM:
			self.wndDragonSoul.RefreshItemSlot()
		if app.ENABLE_COSTUME_BONUS_TRANSFER:
			self.wndCostumeBonusTransfer.RefreshItemSlotWindow()

	def RefreshInventorySlot(self, window, cell):
		if window == player.INVENTORY:
			self.wndInventory.RefreshSingleBagSlot(cell)
		else:
			self.wndSafebox.RefreshSingleSlot(window, cell)

	def RefreshInventoryMaxNum(self):
		self.wndInventory.RefreshInventoryMaxNum()

	def RefreshCharacter(self):
		self.wndCharacter.RefreshCharacter()
		self.wndTaskBar.RefreshQuickSlot()

	def RefreshQuest(self, refreshCategories=False):
		if app.GetSelectedDesignName() != "illumina":
			self.wndCharacter.RefreshQuest(refreshCategories)
		else:
			self.wndCharacter.RefreshQuest(True)

	def RequestOpenSafeboxWindow(self):
		net.SendChatPacket("/safebox_open")

	def __OnCTRLClickInventoryItem(self, itemSlotIndex):
		if self.dlgExchange.IsShow():
			self.dlgExchange.AppendOwnerItem(itemSlotIndex)
			return True

		elif self.wndSafebox.IsShow():
			self.wndSafebox.AppendOwnerItem(itemSlotIndex)
			return True

		elif self.wndGuildSafebox.IsShow():
			self.wndGuildSafebox.AppendOwnerItem(itemSlotIndex)
			return True

#		elif self.wndSashCombine and self.wndSashCombine.IsShow():
#			self.wndSashCombine.AddInventoryItem(itemSlotIndex, player.GetItemIndex(itemSlotIndex))
#			return True

		return False

	def __OnCTRLClickSafeboxItem(self, itemSlotIndex):
		self.wndInventory.AppendSafeboxItem(itemSlotIndex)

	def __OnCTRLClickInvSafeboxItem(self, itemSlotIndex):
		self.wndInventory.AppendInvSafeboxItem(itemSlotIndex)

	def __OnCTRLClickGuildSafeboxItem(self, itemSlotIndex):
		self.wndInventory.AppendGuildSafeboxItem(itemSlotIndex)

	def __OnCTRLClickMallItem(self, itemSlotIndex):
		self.wndInventory.AppendMallItem(itemSlotIndex)

	def RefreshSafebox(self):
		self.wndSafebox.Refresh()

	def RefreshSafeboxMaxNum(self):
		self.wndSafebox.RefreshSafeboxMaxNum()

	def UpdateSafebox(self):
		self.wndSafebox.Update()

	# ITEM_MALL
	def RefreshMall(self):
		self.wndSafebox.Refresh()

	def OpenItemMall(self):
		pass
	# END_OF_ITEM_MALL

	def OpenRankWindow(self):
		if constInfo.ENABLE_DUNGEON_RANKING:
			if not self.wndRank:
				return

			if self.wndRank.IsShow():
				self.wndRank.Close()
			else:
				self.wndRank.Open()

	def ToogleFractionWarWindow(self):
		if self.wndChFaction.IsShow():
			self.wndChFaction.Hide()
		else:
			self.wndChFaction.Open()

	def OpenChooseFractionWarWindow(self):
		self.wndChooseFaction.Open()

	# GUILD_SAFEBOX
	def ToggleGuildSafeboxWindow(self):
		if self.wndGuildSafebox.IsShow():
			net.SendChatPacket("/guild_safebox_close")
		else:
			self.RequestOpenGuildSafeboxWindow()

	def RequestOpenGuildSafeboxWindow(self):
		net.SendGuildSafeboxOpenPacket()

	def RefreshGuildSafebox(self):
		self.wndGuildSafebox.RefreshGuildSafebox()

	def OpenGuildSafeboxWindow(self, size):
		self.wndGuildSafebox.ShowWindow(size)

	def RefreshGuildSafeboxMoney(self):
		self.wndGuildSafebox.RefreshGuildSafeboxMoney()

	def CommandCloseGuildSafebox(self):
		self.wndGuildSafebox.CommandCloseGuildSafebox()

	# def RefreshGuildSafeboxEnable(self):
	#	self.wndInventory.RefreshGuildSafeboxEnable()

	def RefreshGuildSafeboxLog(self):
		self.wndGuildSafebox.RefreshLog()

	def AppendGuildSafeboxLog(self):
		self.wndGuildSafebox.AppendLog()
	# END_OF_GUILD_SAFEBOX

	def RefreshMessenger(self):
		self.wndMessenger.RefreshMessenger()

	def RefreshGuildInfoPage(self):
		self.wndGuild.RefreshGuildInfoPage()

	def RefreshGuildBoardPage(self):
		self.wndGuild.RefreshGuildBoardPage()

	def RefreshGuildMemberPage(self):
		self.wndGuild.RefreshGuildMemberPage()

	def RefreshGuildMemberPageLastPlayed(self):
		self.wndGuild.RefreshGuildMemberPageLastPlayed()


	def RefreshGuildMemberPageGradeComboBox(self):
		self.wndGuild.RefreshGuildMemberPageGradeComboBox()

	def RefreshGuildSkillPage(self):
		self.wndGuild.RefreshGuildSkillPage()
		if app.ENABLE_GUILDRENEWAL_SYSTEM:
			self.wndGuild.RefreshGuildWarInfoPage()

	def RefreshGuildGradePage(self):
		self.wndGuild.RefreshGuildGradePage()

	if app.ENABLE_SECOND_GUILDRENEWAL_SYSTEM:
		def RefreshGuildRankingList(self, issearch):
			if self.wndGuild:
				self.wndGuild.RefreshGuildRankingList(issearch)

		def CloseGuildRankWindow(self):
			if self.wndGuild:
				self.wndGuild.CloseGuildListDialog()
				
		def ShowGuildWarButton(self):
			if self.wndGameButton:
				self.wndGameButton.ShowGuildWarButton()
		
		def HideGuildWarButton(self):
			if self.wndGameButton:
				self.wndGameButton.HideGuildWarButton()

	def DeleteGuild(self):
		self.wndMessenger.ClearGuildMember()
		self.wndGuild.DeleteGuild()

	def RefreshMobile(self):
		self.dlgSystem.RefreshMobile()

	def OnMobileAuthority(self):
		self.dlgSystem.OnMobileAuthority()

	def OnBlockMode(self, mode):
		self.dlgSystem.OnBlockMode(mode)

	## Calling Functions
	# PointReset
	def OpenPointResetDialog(self):
		self.dlgPointReset.Show()
		self.dlgPointReset.SetTop()

	def ClosePointResetDialog(self):
		self.dlgPointReset.Close()

	# Shop
	if (app.COMBAT_ZONE):
		def OpenShopDialog(self, vid, points, curLimit, maxLimit):
			self.wndInventory.Show()
			self.wndInventory.SetTop()
			if constInfo.ENABLE_BATTLEPASS and constInfo.BATTLEPASS_TEMP:
				self.wndBattlePass.LoadShop()
				tchat("battlepass shop!")
				constInfo.BATTLEPASS_TEMP = False
			else:
				self.dlgShop.Open(vid, points, curLimit, maxLimit)
				self.dlgShop.SetTop()
	else:
		def OpenShopDialog(self, vid):
			self.wndInventory.Show()
			self.wndInventory.SetTop()
			if constInfo.ENABLE_BATTLEPASS and constInfo.BATTLEPASS_TEMP:
				tchat("battlepass shop!")
				self.wndBattlePass.LoadShop()
				constInfo.BATTLEPASS_TEMP = False
			else:
				self.dlgShop.Open(vid)
				self.dlgShop.SetTop()

	def CloseShopDialog(self):
		self.dlgShop.Close()

	def RefreshShopDialog(self):
		self.dlgShop.Refresh()

	def OpenCostumeWindow(self):
		if not self.wndInventory.IsShow():
			self.wndInventory.Show()
			self.wndInventory.SetTop()
		self.wndInventory.OpenCostumeWindow()

	## Quest
	def OpenCharacterWindowQuestPage(self):
		self.wndCharacter.Show()
		self.wndCharacter.SetState("QUEST")

	def OpenQuestWindow(self, skin, idx):

		wnds = ()

		q = uiQuest.QuestDialog(skin, idx)
		q.SetWindowName("QuestWindow" + str(idx))
		q.Show()
		if skin:
			q.Lock()
			wnds = self.__HideWindows()

			# UNKNOWN_UPDATE
			q.AddOnDoneEvent(lambda tmp_self, args=wnds: self.__ShowWindows(args))
			# END_OF_UNKNOWN_UPDATE

		if skin:
			q.AddOnCloseEvent(q.Unlock)
		q.AddOnCloseEvent(lambda s = self, qw = q: s.__dict__.__getitem__("wndQuestWindow").remove(qw))

		# UNKNOWN_UPDATE
		self.wndQuestWindow.append(q)
		# END_OF_UNKNOWN_UPDATE

	## Exchange
	def StartExchange(self):
		self.dlgExchange.OpenDialog()
		self.dlgExchange.Refresh()
		self.RefreshInventory()

	def EndExchange(self):
		self.dlgExchange.CloseDialog()
		self.RefreshInventory()

	def RefreshExchange(self):
		self.dlgExchange.Refresh()
		self.RefreshInventory()

	## Party
	def AddPartyMember(self, pid, name):
		self.wndParty.AddPartyMember(pid, name)

		self.__ArrangeQuestButton()

	def UpdatePartyMemberInfo(self, pid):
		self.wndParty.UpdatePartyMemberInfo(pid)

	def RemovePartyMember(self, pid):
		self.wndParty.RemovePartyMember(pid)
		self.__ArrangeQuestButton()

	def LinkPartyMember(self, pid, vid):
		self.wndParty.LinkPartyMember(pid, vid)

	def UnlinkPartyMember(self, pid):
		self.wndParty.UnlinkPartyMember(pid)

	def UnlinkAllPartyMember(self):
		self.wndParty.UnlinkAllPartyMember()

	def ExitParty(self):
		self.wndParty.ExitParty()
		self.__ArrangeQuestButton()

	def PartyHealReady(self):
		self.wndParty.PartyHealReady()

	def ChangePartyParameter(self, distributionMode):
		self.wndParty.ChangePartyParameter(distributionMode)

	## Safebox
	def AskSafeboxPassword(self):
		self.ToggleSafeboxWindow()
		return

		if self.wndSafebox.IsShow():
			return

		# SAFEBOX_PASSWORD
		self.dlgPassword.SetTitle(localeInfo.PASSWORD_TITLE)
		self.dlgPassword.SetSendMessage("/safebox_password ")
		# END_OF_SAFEBOX_PASSWORD

		self.dlgPassword.ShowDialog()

	def ToggleSafeboxWindow(self):
		if not self.wndSafebox.IsShow():
			self.OpenSafeboxWindow()
		else:
			self.wndSafebox.Close()

	def ToggleUppitemWindow(self):
		if not self.wndSafebox.IsShow():
			self.OpenSafeboxWindow()
		else:
			self.wndSafebox.Close()
		self.wndSafebox.SelectPage(self.wndSafebox.BUTTON_UPP)

	def OpenSafeboxWindow(self, size=0):
		if size > 0:
			self.wndSafebox.OnSafeboxOpen(size)
		else:
			self.wndSafebox.Open()

	def CommandCloseSafebox(self):
		pass

	# ITEM_MALL
	def AskMallPassword(self):
		tchat("x")
		pass

	def OpenMallWindow(self, size):
		self.wndSafebox.OnMallOpen(size)

	def CommandCloseMall(self):
		pass
	# END_OF_ITEM_MALL

	## Guild
	def OnStartGuildWar(self, guildSelf, guildOpp):
		self.wndGuild.OnStartGuildWar(guildSelf, guildOpp)

		guildWarScoreBoard = uiGuild.GuildWarScoreBoard()
		guildWarScoreBoard.Open(guildSelf, guildOpp)
		guildWarScoreBoard.Show()
		self.guildScoreBoardDict[uiGuild.GetGVGKey(guildSelf, guildOpp)] = guildWarScoreBoard

	def OnEndGuildWar(self, guildSelf, guildOpp):
		self.wndGuild.OnEndGuildWar(guildSelf, guildOpp)

		key = uiGuild.GetGVGKey(guildSelf, guildOpp)

		if not self.guildScoreBoardDict.has_key(key):
			return

		self.guildScoreBoardDict[key].Destroy()
		del self.guildScoreBoardDict[key]

	# GUILDWAR_MEMBER_COUNT
	def UpdateMemberCount(self, gulidID1, memberCount1, guildID2, memberCount2):
		key = uiGuild.GetGVGKey(gulidID1, guildID2)

		if not self.guildScoreBoardDict.has_key(key):
			return

		self.guildScoreBoardDict[key].UpdateMemberCount(gulidID1, memberCount1, guildID2, memberCount2)
	# END_OF_GUILDWAR_MEMBER_COUNT

	def OnRecvGuildWarPoint(self, gainGuildID, opponentGuildID, point):
		key = uiGuild.GetGVGKey(gainGuildID, opponentGuildID)
		if not self.guildScoreBoardDict.has_key(key):
			return

		guildBoard = self.guildScoreBoardDict[key]
		guildBoard.SetScore(gainGuildID, opponentGuildID, point)

	## PK Mode
	def OnChangePKMode(self):
		self.wndCharacter.RefreshAlignment()
		self.dlgSystem.OnChangePKMode()

	## Refine
	def OpenRefineDialog(self, targetItemPos, nextGradeItemVnum, cost, prob, type, can_fast_refine):
		self.dlgRefineNew.Open(targetItemPos, nextGradeItemVnum, cost, prob, type, can_fast_refine)

	def AppendMaterialToRefineDialog(self, vnum, count):
		self.dlgRefineNew.AppendMaterial(vnum, count)

	def CloseRefinedDialog(self):
		if self.dlgRefineNew and self.dlgRefineNew.IsShow():
			if self.dlgRefineNew.IsRefined():
				self.dlgRefineNew.Close()

	## Show & Hide
	def ShowDefaultWindows(self):
		self.wndTaskBar.Show()
		self.wndMiniMap.Show()
		self.wndMiniMap.ShowMiniMap()

		self.wndTaskBar.SetToggleButtonEvent(uiTaskBar.TaskBar.BUTTON_CHARACTER, ui.__mem_func__(self.ToggleCharacterWindowStatusPage))
		self.wndTaskBar.SetToggleButtonEvent(uiTaskBar.TaskBar.BUTTON_INVENTORY, ui.__mem_func__(self.ToggleInventoryWindow))
		self.wndTaskBar.SetToggleButtonEvent(uiTaskBar.TaskBar.BUTTON_MESSENGER, ui.__mem_func__(self.ToggleMessenger))
		self.wndTaskBar.SetToggleButtonEvent(uiTaskBar.TaskBar.BUTTON_SYSTEM, ui.__mem_func__(self.ToggleSystemDialog))
		self.wndTaskBar.SetToggleButtonEvent(uiTaskBar.TaskBar.BUTTON_CHAT, ui.__mem_func__(self.ToggleChat))
		if app.GetSelectedDesignName() == "illumina":
			self.wndMiniMap.SetToggleButtonEvent(uiMiniMap.MiniMap.BUTTON_CHARACTER, ui.__mem_func__(self.ToggleCharacterWindowStatusPage))
			self.wndMiniMap.SetToggleButtonEvent(uiMiniMap.MiniMap.BUTTON_INVENTORY, ui.__mem_func__(self.ToggleInventoryWindow))
			self.wndMiniMap.SetToggleButtonEvent(uiMiniMap.MiniMap.BUTTON_MESSENGER, ui.__mem_func__(self.ToggleMessenger))
			self.wndMiniMap.SetToggleButtonEvent(uiMiniMap.MiniMap.BUTTON_SYSTEM, ui.__mem_func__(self.ToggleSystemDialog))
			self.wndMiniMap.SetToggleButtonEvent(uiMiniMap.MiniMap.BUTTON_CHAT, ui.__mem_func__(self.ToggleChat))


	def ShowAllWindows(self):
		self.wndChat.Show()
		self.wndMiniMap.Show()
		if self.wndAnimasphere:
			self.wndAnimasphere.Show()
		self.wndTaskBar.Show()
		if self.wndAffect:
			self.wndAffect.Open()
		if self.wndEventIcon:
			self.wndEventIcon.Show()

	def HideAllWindows(self):
		self.__HideWindows()
		if self.wndAuctionShop:
			self.wndAuctionShop.Hide()
		if self.wndPet:
			self.wndPet.Hide()
		if self.wndMount:
			self.wndMount.Hide()
		if self.wndSwitchbot:
			self.wndSwitchbot.Hide()
		if self.wndShopSearch:
			self.wndShopSearch.Hide()
		if self.wndGayaShop:
			self.wndGayaShop.Hide()
		if self.wndWeb:
			self.wndWeb.Hide()
		if self.dlgWhisperWithoutTarget:
			self.dlgWhisperWithoutTarget.Hide()
		if self.wndAcce:
			self.wndAcce.Hide()
		if self.wndSoulRefine:
			self.wndSoulRefine.Hide()
		if self.wndItemRefund:
			self.wndItemRefund.Hide()
		if self.wndEventJoin:
			self.wndEventJoin.Hide()
		if self.wndAffect:
			self.wndAffect.Close()
		if constInfo.ENABLE_BATTLEPASS:
			if self.wndBattlePass:
				self.wndBattlePass.Hide()

	def ShowMouseImage(self):
		self.wndTaskBar.ShowMouseImage()

	def HideMouseImage(self):
		self.wndTaskBar.HideMouseImage()

	def ToggleChat(self):
		if constInfo.HOTFIX_TEMP_IGNORE_CHAT_OPEN:
			constInfo.HOTFIX_TEMP_IGNORE_CHAT_OPEN = False
			return

		if True == self.wndChat.IsEditMode():
			self.wndChat.CloseChat()
		else:
			if self.wndWeb and self.wndWeb.IsShow() and ((not app.ENABLE_WEB_OFFSCREEN) or app.CanWebPageRecvKey()):
				pass
			else:
				self.wndChat.OpenChat()

	def IsOpenChat(self):
		return self.wndChat.IsEditMode()

	def SetChatFocus(self):
		self.wndChat.SetChatFocus()

	def OpenRestartDialog(self):
		self.dlgRestart.OpenDialog()
		self.dlgRestart.SetTop()

	def CloseRestartDialog(self):
		self.dlgRestart.Close()

	def ToggleSystemDialog(self):
		if False == self.dlgSystem.IsShow():
			self.dlgSystem.OpenDialog()
			self.dlgSystem.SetTop()
		else:
			self.dlgSystem.Close()

	def OpenSystemDialog(self):
		self.dlgSystem.OpenDialog()
		self.dlgSystem.SetTop()

	def ToggleMessenger(self):
		if self.wndMessenger.IsShow():
			self.wndMessenger.Hide()
		else:
			self.wndMessenger.Show()
			self.wndMessenger.SetTop()

	def ToggleMiniMap(self):
		if app.IsPressed(app.DIK_LSHIFT) or app.IsPressed(app.DIK_RSHIFT):
			if False == self.wndMiniMap.isShowMiniMap():
				self.wndMiniMap.ShowMiniMap()
				self.wndMiniMap.SetTop()
			else:
				self.wndMiniMap.HideMiniMap()

		else:
			self.wndMiniMap.ToggleAtlasWindow()

	def PressMKey(self):
		if app.IsPressed(app.DIK_LALT) or app.IsPressed(app.DIK_RALT):
			self.ToggleMessenger()

		else:
			self.ToggleMiniMap()

	def SetMapName(self, mapName):
		self.wndMiniMap.SetMapName(mapName)

	def MiniMapScaleUp(self):
		self.wndMiniMap.ScaleUp()

	def MiniMapScaleDown(self):
		self.wndMiniMap.ScaleDown()

	def OpenCardsInfoWindow(self):
		self.wndCardsInfo.Open()

	def ShowEventIcon(self, eventId):

		tchat("ShowEventIcon: {}".format(eventId))

		# if self.wndCardsIcon and self.wndCardsIcon.IsShow():
		# 	return

		# if self.wndJigsawIcon and self.wndJigsawIcon.IsShow():
		# 	return

		if constInfo.ENABLE_EVENT_ICONS:
			if constInfo.ENABLE_XMAS_EVENT:	 # had to do it fast
				if eventId == 11:
					self.wndXmasEventIcon.Open(eventId)
				else:
					self.wndEventIcon.Open(eventId)
			else:
				self.wndEventIcon.Open(eventId)

	def OpenEventAnnouncement(self, eventId, finishTimeStamp):

		if not eventId or not finishTimeStamp:

			if self.eventAnnouncementWnd:
				self.eventAnnouncementWnd.Close()

			return

		if not self.eventAnnouncementWnd:
			self.eventAnnouncementWnd = uieventannouncement.EventAnnouncement()

		self.eventAnnouncementWnd.BindInterface(self)
		self.eventAnnouncementWnd.OpenWithType(eventId, finishTimeStamp)

	def OpenCardsWindow(self, safemode):
		self.wndCards.ChangeDesign(constInfo.RUMI_EVENT_DESIGN_TYPE)
		self.wndCards.Open(safemode)
	
	def UpdateCardsInfo(self, hand_1, hand_1_v, hand_2, hand_2_v, hand_3, hand_3_v, hand_4, hand_4_v, hand_5, hand_5_v, cards_left, points):
		self.wndCards.UpdateCardsInfo(hand_1, hand_1_v, hand_2, hand_2_v, hand_3, hand_3_v, hand_4, hand_4_v, hand_5, hand_5_v, cards_left, points)
	
	def UpdateCardsFieldInfo(self, hand_1, hand_1_v, hand_2, hand_2_v, hand_3, hand_3_v, points):
		self.wndCards.UpdateCardsFieldInfo(hand_1, hand_1_v, hand_2, hand_2_v, hand_3, hand_3_v, points)
	
	def CardsPutReward(self, hand_1, hand_1_v, hand_2, hand_2_v, hand_3, hand_3_v, points):
		self.wndCards.CardsPutReward(hand_1, hand_1_v, hand_2, hand_2_v, hand_3, hand_3_v, points)
	
	def CardsShowIcon(self, eventType):
		self.wndCardsIcon.ChangeDesign(eventType)
		self.wndCardsIcon.Show()

	def ToggleCharacterWindow(self, state):
		if False == player.IsObserverMode():
			if False == self.wndCharacter.IsShow():
				self.OpenCharacterWindowWithState(state)
			else:
				if state == self.wndCharacter.GetState():
					self.wndCharacter.OverOutItem()
					self.wndCharacter.Hide()
					
					if constInfo.BONI_BOARD and self.wndCharacter.uiStatsBoard:
						self.wndCharacter.uiStatsBoard.Close()
						self.wndCharacter.ResetButtons()
				else:
					self.wndCharacter.SetState(state)

	def OpenCharacterWindowWithState(self, state):
		if False == player.IsObserverMode():
			self.wndCharacter.SetState(state)
			self.wndCharacter.Show()
			self.wndCharacter.SetTop()

	def ToggleCharacterWindowStatusPage(self):
		self.ToggleCharacterWindow("STATUS")

	def ToggleInventoryWindow(self):
		if False == player.IsObserverMode():
			if False == self.wndInventory.IsShow():
				self.wndInventory.Show()
				self.wndInventory.SetTop()
			else:
				self.wndInventory.OverOutItem()
				self.wndInventory.Close()

	def ToggleGuildWindow(self):
		if not self.wndGuild.IsShow():
			if self.wndGuild.CanOpen():
				self.wndGuild.Open()
			else:
				chat.AppendChat(chat.CHAT_TYPE_INFO, localeInfo.GUILD_YOU_DO_NOT_JOIN)
		else:
			self.wndGuild.OverOutItem()
			self.wndGuild.Close()

	def ToggleChatLogWindow(self):
		if self.wndChatLog.IsShow():
			self.wndChatLog.Hide()
		else:
			self.wndChatLog.Show()

	def ToggleBlackJackWindow(self):
		if self.wndBlackJack:
			if self.wndBlackJack.IsShow():
				self.wndBlackJack.Close()
			else:
				self.wndBlackJack.Open()

	def CheckGameButton(self):
		if self.wndGameButton:
			self.wndGameButton.CheckGameButton()

	def __OnClickStatusPlusButton(self):
		self.ToggleCharacterWindow("STATUS")

	def __OnClickSkillPlusButton(self):
		self.ToggleCharacterWindow("SKILL")

	def __OnClickQuestButton(self):
		self.ToggleCharacterWindow("QUEST")

	def __OnClickHelpButton(self):
		player.SetPlayTime(1)
		self.CheckGameButton()
		self.OpenHelpWindow()

	def __OnClickBuildButton(self):
		self.BUILD_OpenWindow()

	def OpenHelpWindow(self):
		self.wndUICurtain.Show()
		self.wndHelp.Open()

	def CloseHelpWindow(self):
		self.wndUICurtain.Hide()
		self.wndHelp.Close()

	def GetWebWindowSize(self):
		return self.wndWeb.GetWindowSize()

	if app.ENABLE_MELEY_LAIR_DUNGEON:
		def OpenMeleyRanking(self):
			self.wndMeleyRanking.Open()

		def RankMeleyRanking(self, line, name, members, time):
			self.wndMeleyRanking.AddRank(line, name, members, time)

	def OpenWebWindow(self, url, title):
		self.wndWeb.SetTitle(title)
		self.wndWeb.Open(url)

	def CloseWebLoadingWindow(self):
		self.wndWeb.CloseLoading()

	def CloseWebWindow(self):
		self.wndWeb.Close()

	def OpenCubeWindow(self):
		self.wndCube.Open()

		if False == self.wndInventory.IsShow():
			self.wndInventory.Show()

	def UpdateCubeInfo(self, gold, itemVnum, count):
		self.wndCube.UpdateInfo(gold, itemVnum, count)

	def CloseCubeWindow(self):
		self.wndCube.Close()
		
	def FailedCubeWork(self):
		self.wndCube.Refresh()

	def SucceedCubeWork(self, itemVnum, count):
		self.wndCube.Clear()
		
		print "SucceedCubeWork: [%d:%d]" % (itemVnum, count)

		if 0:
			self.wndCubeResult.SetPosition(*self.wndCube.GetGlobalPosition())
			self.wndCubeResult.SetCubeResultItem(itemVnum, count)
			self.wndCubeResult.Open()
			self.wndCubeResult.SetTop()

	def __HideWindows(self):
		hideWindows = self.wndTaskBar,\
							self.wndCharacter,\
							self.wndInventory,\
							self.wndMiniMap,\
							self.wndGuild,\
							self.wndMessenger,\
							self.wndChat,\
							self.wndParty,\
							self.wndGameButton, \
							self.wndEventIcon, \
							self.wndTaskBar.GetMoneyWindow(),

		if self.wndInventory.wndCostume:
			hideWindows += self.wndInventory.wndCostume,

		if self.wndInventory.wndShining:
			hideWindows += self.wndInventory.wndShining,

		if self.wndMessenger:
			self.wndMessenger.HideAllOnlinePopups()

		if app.ENABLE_SKIN_SYSTEM:
			if self.wndInventory.wndSkinSystem:
				hideWindows += self.wndInventory.wndSkinSystem,

		if app.ENABLE_DRAGON_SOUL_SYSTEM:
			hideWindows += self.wndDragonSoul,\
						self.wndDragonSoulRefine,

		if app.ENABLE_COSTUME_BONUS_TRANSFER:
			hideWindows += self.wndCostumeBonusTransfer,

		if app.ENABLE_ZODIAC:
			if self.wndAnimasphere:
				hideWindows += self.wndAnimasphere,

		if constInfo.ENABLE_BATTLEPASS:
			if self.wndBattlePass:
				hideWindows += self.wndBattlePass,

		hideWindows += self.wndBlackJack,

		hideWindows = filter(lambda x:x.IsShow(), hideWindows)
		map(lambda x:x.Hide(), hideWindows)

		self.HideAllQuestButton()
		self.HideAllWhisperButton()

		if self.wndChat.IsEditMode():
			self.wndChat.CloseChat()

		return hideWindows

	def __ShowWindows(self, wnds):
		map(lambda x:x.Show(), wnds)
		self.ShowAllQuestButton()
		self.ShowAllWhisperButton()

	def BINARY_OpenAtlasWindow(self):
		if self.wndMiniMap:
			self.wndMiniMap.ShowAtlas()

	def BINARY_SetObserverMode(self, flag):
		self.wndGameButton.SetObserverMode(flag)

	# ACCESSORY_REFINE_ADD_METIN_STONE
	def BINARY_OpenSelectItemWindow(self):
		self.wndItemSelect.Open()
	# END_OF_ACCESSORY_REFINE_ADD_METIN_STONE

	def OpenRuneMainWindow(self):
		if not constInfo.RUNE_ENABLED:
			return None

		if __SERVER__ == 2:
			return None

		if self.wndRuneSub and self.wndRuneSub.IsShow():
			self.wndRuneSub.Close()

		if not self.wndRuneMain:
			self.wndRuneMain = uiRune.RuneMainWindow(self.OpenRuneSubWindow)

		if self.wndRuneMain and self.wndRuneMain.IsShow():
			self.wndRuneMain.Close()
		else:
			self.wndRuneMain.Open()

		return self.wndRuneMain

	def OpenRuneSubWindow(self, groupIndex):
		if not constInfo.RUNE_ENABLED:
			return None

		if __SERVER__ == 2:
			return None

		if not self.wndRuneSub:
			self.wndRuneSub = uiRune.RuneSubWindow(self.OpenRuneMainWindow)
		self.wndRuneSub.Open(groupIndex)
		return self.wndRuneSub

	if constInfo.ENABLE_RUNE_PAGES:
		def OpenRuneSelectedSubWindow(self):
			if not constInfo.RUNE_ENABLED:
				return

			if __SERVER__ == 2:
				return None

			if not self.wndRuneMain:
				self.wndRuneMain = uiRune.RuneMainWindow(self.OpenRuneSubWindow)

			if self.wndRuneMain and self.wndRuneMain.IsShow():
				self.wndRuneMain.Close()
				return

			if self.wndRuneSub and self.wndRuneSub.IsShow():
				self.wndRuneSub.Close()
				return

			group = rune.PageGetType(False) if rune.PageGetType(False) > -1 else 0
			self.OpenRuneSubWindow(group)

	def RefreshRuneWindow(self):
		if not constInfo.RUNE_ENABLED:
			return

		if self.wndRuneSub:
			self.wndRuneSub.Refresh()

	def OpenRuneRefine(self, refineProto, cost):
		if self.wndRuneSub:
			self.wndRuneSub.OpenRuneRefine(refineProto, cost)

	if constInfo.ENABLE_LEVEL2_RUNES:
		def OpenRuneLevel(self, refineProto, cost, vnum):
			if self.wndRuneSub:
				self.wndRuneSub.OpenRuneLevel(refineProto, cost, vnum)

	def RefreshRunePoints(self, points):
		constInfo.RUNE_POINTS = points
		if self.wndRuneSub:
			self.wndRuneSub.UpdatePoints()

	#####################################################################################
	### Private Shop ###

	def OpenPrivateShopInputNameDialog(self, isAuctionShop = False):
		#if player.IsInSafeArea():
		#	chat.AppendChat(chat.CHAT_TYPE_INFO, localeInfo.CANNOT_OPEN_PRIVATE_SHOP_IN_SAFE_AREA)
		#	return

		if app.ENABLE_COSTUME_BONUS_TRANSFER:
			if self.wndCostumeBonusTransfer.IsShow():
				chat.AppendChat(chat.CHAT_TYPE_INFO, localeInfo.COMB_ITEM_NOTICE)
				return

		inputDialog = uiCommon.InputDialog()
		if isAuctionShop:
			inputDialog.SetTitle(localeInfo.OFFLINE_SHOP_INPUT_NAME_DIALOG_TITLE)
		else:
			inputDialog.SetTitle(localeInfo.PRIVATE_SHOP_INPUT_NAME_DIALOG_TITLE)
		inputDialog.SetMaxLength(32)
		inputDialog.SetAcceptEvent(ui.__mem_func__(self.OpenPrivateShopBuilder))
		inputDialog.SetCancelEvent(ui.__mem_func__(self.ClosePrivateShopInputNameDialog))
		inputDialog.isAuctionShop = isAuctionShop
		inputDialog.Open()
		self.inputDialog = inputDialog

	def CloseShopBuilder_BootTime(self):
		self.ClosePrivateShopInputNameDialog()
		tmpPopUpDialog = uiCommon.PopupDialog()
		tmpPopUpDialog.SetText(localeInfo.OFFLINE_SHOP_SERVERBOOT_EARLY)
		tmpPopUpDialog.Open()
		self.inputDialog = tmpPopUpDialog

	def ClosePrivateShopInputNameDialog(self):
		self.inputDialog = None
		return True

	def OpenPrivateShopBuilder(self):

		if not self.inputDialog:
			return True

		if not len(self.inputDialog.GetText()):
			return True

		self.privateShopBuilder.Open(self.inputDialog.GetText(), self.inputDialog.isAuctionShop, constInfo.IS_PRIVATE_AUCTION_SHOP_COLOR)
		self.ClosePrivateShopInputNameDialog()
		constInfo.IS_PRIVATE_AUCTION_SHOP = False
		constInfo.IS_PRIVATE_AUCTION_SHOP_COLOR = False
		return True

	def AppearPrivateShop(self, vid, text, red, green, blue, style):
		if cfg.Get(cfg.SAVE_OPTION, "hide_auctionshop_title", "1") == "1":
			return

		board = (uiPrivateShopBuilder.PrivateShopAdvertisementBoard() if not style else uiPrivateShopBuilder.PrivateShopTitleBar(style))
		board.Open(vid, text, red, green, blue)

		self.privateShopAdvertisementBoardDict[vid] = board

	def DisappearPrivateShop(self, vid):

		if not self.privateShopAdvertisementBoardDict.has_key(vid):
			return

		del self.privateShopAdvertisementBoardDict[vid]
		uiPrivateShopBuilder.DeleteADBoard(vid)

	#####################################################################################
	### Equipment ###

	def OpenEquipmentDialog(self, vid):
		dlg = uiEquipmentDialog.EquipmentDialog()
		dlg.SetItemToolTip(self.tooltipItem)
		dlg.SetCloseEvent(ui.__mem_func__(self.CloseEquipmentDialog))
		dlg.Open(vid)

		self.equipmentDialogDict[vid] = dlg

	def SetEquipmentDialogItem(self, vid, slotIndex, vnum, count):
		if not vid in self.equipmentDialogDict:
			return
		self.equipmentDialogDict[vid].SetEquipmentDialogItem(slotIndex, vnum, count)

	def SetEquipmentDialogSocket(self, vid, slotIndex, socketIndex, value):
		if not vid in self.equipmentDialogDict:
			return
		self.equipmentDialogDict[vid].SetEquipmentDialogSocket(slotIndex, socketIndex, value)

	def SetEquipmentDialogAttr(self, vid, slotIndex, attrIndex, type, value):
		if not vid in self.equipmentDialogDict:
			return
		self.equipmentDialogDict[vid].SetEquipmentDialogAttr(slotIndex, attrIndex, type, value)

	def CloseEquipmentDialog(self, vid):
		if not vid in self.equipmentDialogDict:
			return
		del self.equipmentDialogDict[vid]

	#####################################################################################

	def GetLink(self, text):
		start = text.find("http://")
		if start == -1:
			start = text.find("https://")
		if start == -1:
			return ""
		return text[start:len(text)].split(" ")[0]

	#####################################################################################
	### Quest ###	
	def BINARY_ClearQuest(self, index):
		btn = self.__FindQuestButton(index)
		if 0 != btn:
			self.__DestroyQuestButton(btn)		
	
	def RecvQuest(self, index, cat_idx, name):
		# QUEST_LETTER_IMAGE
		self.BINARY_RecvQuest(index, cat_idx, name, "file", localeInfo.GetLetterImageName(cat_idx))
		# END_OF_QUEST_LETTER_IMAGE

	def BINARY_RecvQuest(self, index, cat_idx, name, iconType, iconName):

		btn = self.__FindQuestButton(index)
		if 0 != btn:
			self.__DestroyQuestButton(btn)

		btn = uiWhisper.WhisperButton()

		# QUEST_LETTER_IMAGE
		import item
		if "item"==iconType:
			item.SelectItem(1, 2, int(iconName))
			buttonImageFileName=item.GetIconImageFileName()
		else:
			buttonImageFileName=iconName

		if localeInfo.IsEUROPE():
			btn.SetUpVisual(localeInfo.GetLetterCloseImageName(cat_idx))
			btn.SetOverVisual(localeInfo.GetLetterOpenImageName(cat_idx))
			btn.SetDownVisual(localeInfo.GetLetterOpenImageName(cat_idx))
		else:
			btn.SetUpVisual(buttonImageFileName)
			btn.SetOverVisual(buttonImageFileName)
			btn.SetDownVisual(buttonImageFileName)
			btn.Flash()
		# END_OF_QUEST_LETTER_IMAGE

		if localeInfo.IsARABIC():
			btn.SetToolTipText(name, 0, 35)
			btn.ToolTipText.SetHorizontalAlignCenter()
		else:
			btn.SetToolTipText(name, -20, 35)
			btn.ToolTipText.SetHorizontalAlignLeft()
			
		btn.SetEvent(ui.__mem_func__(self.__StartQuest), btn)
		if self.__IsShowQuestLetter():
			btn.Show()
		else:
			btn.Hide()

		btn.index = index
		btn.name = name

		self.questButtonList.insert(0, btn)
		self.__ArrangeQuestButton()

		#chat.AppendChat(chat.CHAT_TYPE_NOTICE, localeInfo.QUEST_APPEND)

	def __ArrangeQuestButton(self):

		screenWidth = wndMgr.GetScreenWidth()
		screenHeight = wndMgr.GetScreenHeight()

		if self.wndParty.IsShow():
			xPos = 100 + 30
		else:
			xPos = 20

		if localeInfo.IsARABIC():
			xPos = xPos + 15

		yPos = 170 * screenHeight / 600
		yCount = (screenHeight - 330) / 63

		count = 0
		for btn in self.questButtonList:

			btn.SetPosition(xPos + (int(count/yCount) * 100), yPos + (count%yCount * 63))
			count += 1

	def __StartQuest(self, btn):
		event.QuestButtonClick(btn.index)
		self.__DestroyQuestButton(btn)

	def __FindQuestButton(self, index):
		for btn in self.questButtonList:
			if btn.index == index:
				return btn

		return 0

	def __DestroyQuestButton(self, btn):
		btn.SetEvent(0)
		self.questButtonList.remove(btn)
		self.__ArrangeQuestButton()

	def HideAllQuestButton(self):
		for btn in self.questButtonList:
			btn.Hide()

	def ShowAllQuestButton(self):
		if self.__IsShowQuestLetter():
			for btn in self.questButtonList:
				btn.Show()

	def __IsShowQuestLetter(self):
		return cfg.Get(cfg.SAVE_OPTION, "quest_letter_show", "1") == "1"

	def RefreshQuestLetterVisibility(self):
		if self.__IsShowQuestLetter():
			self.ShowAllQuestButton()
		else:
			self.HideAllQuestButton()
	#####################################################################################

	#####################################################################################
	### Whisper ###

	def __InitWhisper(self):
		chat.InitWhisper(self)

	def OpenWhisperDialogWithoutTarget(self):
		if not self.dlgWhisperWithoutTarget:
			dlgWhisper = uiWhisper.WhisperDialog(self.MinimizeWhisperDialog, self.CloseWhisperDialog)
			dlgWhisper.BindInterface(self)
			dlgWhisper.LoadDialog()
			dlgWhisper.OpenWithoutTarget(self.RegisterTemporaryWhisperDialog)
			dlgWhisper.SetPosition(self.windowOpenPosition*30,self.windowOpenPosition*30)
			dlgWhisper.Show()
			self.dlgWhisperWithoutTarget = dlgWhisper

			self.windowOpenPosition = (self.windowOpenPosition+1) % 5

		else:
			self.dlgWhisperWithoutTarget.SetTop()
			self.dlgWhisperWithoutTarget.OpenWithoutTarget(self.RegisterTemporaryWhisperDialog)

	def RegisterTemporaryWhisperDialog(self, name):
		if not self.dlgWhisperWithoutTarget:
			return

		btn = self.__FindWhisperButton(name)
		if 0 != btn:
			self.__DestroyWhisperButton(btn)

		elif self.whisperDialogDict.has_key(name):
			oldDialog = self.whisperDialogDict[name]
			oldDialog.Destroy()
			del self.whisperDialogDict[name]

		self.whisperDialogDict[name] = self.dlgWhisperWithoutTarget
		self.dlgWhisperWithoutTarget.OpenWithTarget(name)
		self.dlgWhisperWithoutTarget = None
		self.__CheckGameMaster(name)

	def OpenWhisperDialog(self, name, is_load = False):
		if not self.whisperDialogDict.has_key(name):
			dlg = self.__MakeWhisperDialog(name)
			dlg.OpenWithTarget(name)
			dlg.chatLine.SetFocus()
			dlg.Show()

			self.__CheckGameMaster(name)
			btn = self.__FindWhisperButton(name)
			if 0 != btn:
				self.__DestroyWhisperButton(btn)

			if constInfo.WHISPER_MANAGER:
				if is_load == False:
					whispermgr.OpenWhisper(name)

	def RecvWhisper(self, name, is_load = False):
		if not self.whisperDialogDict.has_key(name):
			btn = self.__FindWhisperButton(name)
			if 0 == btn:
				btn = self.__MakeWhisperButton(name)
				if is_load == False:
					btn.Flash()
					app.StartFlashApplication()
					chat.AppendChat(chat.CHAT_TYPE_NOTICE, localeInfo.RECEIVE_MESSAGE % (name))
			elif is_load == False:
				btn.Flash()
				app.StartFlashApplication()
		elif self.IsGameMasterName(name):
			dlg = self.whisperDialogDict[name]
			dlg.SetGameMasterLook()

	def MakeWhisperButton(self, name):
		self.__MakeWhisperButton(name)

	def ShowWhisperDialog(self, btn):
		try:
			self.__MakeWhisperDialog(btn.name)
			dlgWhisper = self.whisperDialogDict[btn.name]
			dlgWhisper.OpenWithTarget(btn.name)
			dlgWhisper.Show()
			self.__CheckGameMaster(btn.name)

			if constInfo.WHISPER_MANAGER:
				whispermgr.OpenWhisper(btn.name)

		except:
			import dbg
			dbg.TraceError("interface.ShowWhisperDialog - Failed to find key")

		self.__DestroyWhisperButton(btn)

	def MinimizeWhisperDialog(self, name):

		if 0 != name:
			self.__MakeWhisperButton(name)

			if constInfo.WHISPER_MANAGER:
				whispermgr.CloseWhisper(name)


		self.CloseWhisperDialog(name)

	def CloseWhisperDialog(self, name):

		if 0 == name:

			if self.dlgWhisperWithoutTarget:
				self.dlgWhisperWithoutTarget.Destroy()
				self.dlgWhisperWithoutTarget = None

			return

		try:
			dlgWhisper = self.whisperDialogDict[name]
			dlgWhisper.Destroy()
			del self.whisperDialogDict[name]
		except:
			import dbg
			dbg.TraceError("interface.CloseWhisperDialog - Failed to find key")

	def __ArrangeWhisperButton(self):

		screenWidth = wndMgr.GetScreenWidth()
		screenHeight = wndMgr.GetScreenHeight()

		xPos = screenWidth - 70
		yPos = 170 * screenHeight / 600
		yCount = (screenHeight - 330) / 63
		#yCount = (screenHeight - 285) / 63

		count = 0
		for button in self.whisperButtonList:

			button.SetPosition(xPos + (int(count/yCount) * -50), yPos + (count%yCount * 63))
			count += 1

	def __FindWhisperButton(self, name):
		for button in self.whisperButtonList:
			if button.name == name:
				return button

		return 0

	def __MakeWhisperDialog(self, name):
		dlgWhisper = uiWhisper.WhisperDialog(self.MinimizeWhisperDialog, self.CloseWhisperDialog)
		dlgWhisper.BindInterface(self)
		dlgWhisper.LoadDialog()
		dlgWhisper.SetPosition(self.windowOpenPosition*30,self.windowOpenPosition*30)
		self.whisperDialogDict[name] = dlgWhisper

		self.windowOpenPosition = (self.windowOpenPosition+1) % 5

		return dlgWhisper

	def __OnClickWhisperButton(self,whisperButton):
		if app.IsPressed(app.DIK_LCONTROL) or app.IsPressed(app.DIK_RCONTROL):
			try:
				if constInfo.WHISPER_MANAGER:
					whispermgr.ClearWhisper(whisperButton.name)
				chat.ClearWhisper(whisperButton.name)
			except:
				pass
			self.__DestroyWhisperButton(whisperButton)
			return
		self.ShowWhisperDialog(whisperButton)

	def __MakeWhisperButton(self, name):
		whisperButton = uiWhisper.WhisperButton()
		whisperButton.SetUpVisual("d:/ymir work/ui/game/windows/btn_mail_up.sub")
		whisperButton.SetOverVisual("d:/ymir work/ui/game/windows/btn_mail_up.sub")
		whisperButton.SetDownVisual("d:/ymir work/ui/game/windows/btn_mail_up.sub")
		if self.IsGameMasterName(name):
			whisperButton.SetToolTipTextWithColor(name, 0xffffa200)
		else:
			whisperButton.SetToolTipText(name)
		whisperButton.ToolTipText.SetHorizontalAlignCenter()
		whisperButton.SetEvent(ui.__mem_func__(self.__OnClickWhisperButton), whisperButton)
		whisperButton.Show()
		whisperButton.name = name

		self.whisperButtonList.insert(0, whisperButton)
		self.__ArrangeWhisperButton()

		return whisperButton

	def __DestroyWhisperButton(self, button):
		button.SetEvent(0)
		self.whisperButtonList.remove(button)
		self.__ArrangeWhisperButton()

	def HideAllWhisperButton(self):
		for btn in self.whisperButtonList:
			btn.Hide()

	def ShowAllWhisperButton(self):
		for btn in self.whisperButtonList:
			btn.Show()

	def __CheckGameMaster(self, name):
		if not self.listGMName.has_key(name):
			return
		if self.whisperDialogDict.has_key(name):
			dlg = self.whisperDialogDict[name]
			dlg.SetGameMasterLook()

	def RegisterGameMasterName(self, name):
		if self.listGMName.has_key(name):
			return
		self.listGMName[name] = "GM"

	def IsGameMasterName(self, name):
		if self.listGMName.has_key(name) and name.startswith('['):
			return True
		else:
			return False
			
	# ENABLE_MARK_NEW_ITEM_SYSTEM
	def Highligt_Item(self, inven_type, inven_pos):
		if player.SLOT_TYPE_INVENTORY == inven_type:
			self.wndInventory.HighlightSlot(inven_pos)
		elif player.DRAGON_SOUL_INVENTORY == inven_type:
			if app.ENABLE_DRAGON_SOUL_SYSTEM:
				self.wndDragonSoul.HighlightSlot(inven_pos)
	# ENABLE_MARK_NEW_ITEM_SYSTEM

	#####################################################################################

	def UpdateNotifications(self):

		# first open the windows we need
		if self.wndNewTimer:

			for i in range(0, len(self.wndNewTimer.QUESTS)):
				if self.wndNewTimer.QUESTS[i] == None:
					continue
					
				isEnabled = self.wndNewTimer.NOTIFICATION_ENABLED[i]

				if not isEnabled:
					self.wndNotificationWindow[i].Reset()
					continue

				cooldown = self.wndNewTimer.COOLDOWNS[i]

				# fix biolog quest... if time => 0 then open notification (part of this fix is in UpdateTimers)
				if i == 0 and cooldown == 0:
					self.wndNotificationWindow[i].Open()
					continue

				timeleft = int(cooldown - app.GetTime())

				if timeleft <= 0:
					self.wndNotificationWindow[i].Open()
				else:
					self.wndNotificationWindow[i].Reset()

	def DrawNotifications(self):

		openedNotifications = []

		for notification in self.wndNotificationWindow:

			if notification and notification.IsShow():

				notificationTime = notification.openTime
				globalTime = app.GetGlobalTime()

				# fix bug when teleporting / changing character with GlobalTime
				if notificationTime > globalTime:
					tchat("(testserver) notification fix [%s -> %s]" % (str(notificationTime), str(globalTime)))
					notification.openTime = app.GetGlobalTime()

				openedNotifications.append(notification)

		if not len(openedNotifications):
			return

		# 46 + 4px padding
		imageWidth	= openedNotifications[0].backgroundImage.GetRight()
		imageHeight = openedNotifications[0].backgroundImage.GetBottom()

		imageStep = imageHeight + 4

		screenHeight	= wndMgr.GetScreenHeight()
		screenWidth		= wndMgr.GetScreenWidth()

		elementsPositionStart = 80
		drawX = (screenWidth / 2) - (imageWidth / 2) 

		for i in range(0, len(openedNotifications)):
			openedNotifications[i].SetPosition(drawX, elementsPositionStart + (imageStep * i))

	def DoAlchemyEffect(self):

		if self.wndInventory.dragonSoulActiveEffect and self.wndDragonSoul:

			isActivated = self.wndDragonSoul.isActivated

			if isActivated:
				self.wndInventory.dragonSoulActiveEffect.Show()
			else:
				self.wndInventory.dragonSoulActiveEffect.Hide()

	def DoQuestTimerNotifications(self):

		# thats the only way to make it work, refresh cdrs every teleportation etc.
		if self.refreshCooldowns:

			if not self.wndNewTimer:
				return

			# notifications not enabled
			if self.wndNewTimer.NOTIFICATION_ENABLED == [0] * len(self.wndNewTimer.QUESTS):
				return

			net.SendChatPacket("/get_timer_cdrs")
			self.UpdateNotifications()
			self.refreshCooldowns = False

		if (app.GetTime() - self.lastUpdateTime) >= 3.0:
			self.lastUpdateTime = app.GetTime()
			self.UpdateNotifications()

		self.DrawNotifications()

	def INTERFACE_OnUpdate(self):

		self.BUILD_OnUpdate()

		if constInfo.ALCHEMY_EFFECT_ON_ENABLED:
			self.DoAlchemyEffect()

		if constInfo.NEW_QUEST_TIMER:
			self.DoQuestTimerNotifications()

	# ACCE
	def ActivateAcceSlot(self, slotPos):
		self.wndInventory.ActivateAcceSlot(slotPos)

	def DeactivateAcceSlot(self, slotPos):
		self.wndInventory.DeactivateAcceSlot(slotPos)

	def RefreshAcce(self):
		if self.wndAcce:
			self.wndAcce.RefreshAcceWindow()

	def	OpenAcceWindow(self, type):
		if not self.wndAcce:
			self.wndAcce = uiAcce.AcceWindow()
			self.wndAcce.SetItemToolTip(self.tooltipItem)

		self.wndAcce.Open(type)

	def CloseAcceWindow(self):
		if self.wndAcce:
			self.wndAcce.Close()
	# END_OF_ACCE

	def OpenSoulRefineWindow(self):
		if not self.wndSoulRefine:
			self.wndSoulRefine = uiSoulSystem.SoulRefineWindow()

		self.wndSoulRefine.Show()

	def ToggleTimerWindow(self):
		if constInfo.NEW_QUEST_TIMER:
			if not self.wndNewTimer:
				self.wndNewTimer = uinewtimer.TimerWindow()

			if self.wndNewTimer.IsShow():
				self.wndNewTimer.Close()
			else:
				self.wndNewTimer.Open()
				self.wndNewTimer.SetItemToolTip(self.tooltipItem)
			return

	def UpdateBiologInfo(self, currentLevel):
		if constInfo.NEW_QUEST_TIMER and self.wndNewTimer:
			self.wndNewTimer.UpdateBiologInfo(currentLevel)

	def UpdateTimerWindow(self, key, value):
		if constInfo.NEW_QUEST_TIMER and self.wndNewTimer:
			self.wndNewTimer.UpdateTimers(key, value)

	#AUCTION

	#AUCTION
	def ToggleAuctionWindow(self):	
		if not self.wndAuction:
			self.wndAuction = uiAuction.AuctionWindow()

		if self.wndAuction.IsShow():
			self.wndAuction.Close()
		else:
			self.wndAuction.Open()

	def RefreshAuctionPremium(self):
		if self.wndAuction:
			self.wndAuction.RefreshPremium()
		if self.wndShopSearch:
			self.wndShopSearch.RefreshPremium()

	def RefreshAuctionItem(self):
		if self.wndAuction:
			self.wndAuction.ShowItems()
		if self.wndShopSearch:
			self.wndShopSearch.ShowItems()

	def ShowAuctionMessage(self, message):
		if self.wndAuction:
			self.wndAuction.ShowGameMessage(message)
		if self.wndShopSearch:
			self.wndShopSearch.ShowGameMessage(message)

	def __OnClickAuctionShopButton(self):
		if auction.HasMyShop():
			if auction.IsMyShopLoaded():
				self.ToggleAuctionShopWindow()
			else:
				auction.SendRequestShopViewPacket()
				self._open_auction_on_refresh = True
		else:
			if player.GetMoney() < 100000:
				chat.AppendChat(1, localeInfo.OFFLINE_SHOP_CREATE_PRICE_FAIL)
				return

			self.OpenPrivateShopInputNameDialog(True)

	def OpenAuctionShopWindow(self):
		if not self.wndAuctionShop:
			self.wndAuctionShop = uiAuction.AuctionShopWindow()
			self.wndAuctionShop.whisperFn = self.OpenWhisperDialog
			self.wndAuctionShop.SetItemToolTip(self.tooltipItem)

		self.wndAuctionShop.Open()

	def ToggleAuctionShopWindow(self):
		if self.wndAuctionShop and self.wndAuctionShop.IsShow():
			self.wndAuctionShop.Close()
		else:
			self.OpenAuctionShopWindow()

	def RefreshAuctionShop(self):
		if self._open_auction_on_refresh:
			self._open_auction_on_refresh = False
			self.OpenAuctionShopWindow()
		elif self.wndAuctionShop:
			self.wndAuctionShop.Refresh()

	def RefreshAuctionShopGold(self):
		if self.wndAuctionShop:
			self.wndAuctionShop.RefreshGold()

	def RefreshAuctionShopHistory(self):
		if self.wndAuctionShop:
			self.wndAuctionShop.RefreshHistory()

	def RecvAuctionAveragePrice(self, requestor, price):
		if requestor == 0 and self.privateShopBuilder:
			self.privateShopBuilder.OpenSellWindow(price)
		elif requestor == 1 and self.wndAuctionShop:
			self.wndAuctionShop.OpenSellWindow(price)

	def OpenAuctionGuestShop(self):
		if not self.wndAuctionGuestShop:
			self.wndAuctionGuestShop = uiAuction.AuctionGuestShopWindow()
			self.wndAuctionGuestShop.SetItemToolTip(self.tooltipItem)

		self.wndAuctionGuestShop.Open()

	def RefreshAuctionGuestShop(self):
		if self.wndAuctionGuestShop:
			self.wndAuctionGuestShop.Refresh()

	def CloseAuctionGuestShop(self):
		if self.wndAuctionGuestShop:
			self.wndAuctionGuestShop.OnClose()

	def OpenAuctionWindowWithVnum(self, vnum):
	#	if not self.wndAuction or not self.wndAuction.IsShow():
	#		self.ToggleAuctionWindow()

	#	self.wndAuction.Search_StartByVnum(vnum)
		pass
	#END_OF_AUCTION

	if constInfo.ENABLE_DMG_METER:
		def ToggleDmgMeter(self):
			if self.wndDmgMeter.IsShow():
				self.wndDmgMeter.Close()
			else:
				self.wndDmgMeter.Open()

	# SHOP_SEARCH
	def ToggleShopSearchWindow(self):
		if not self.wndShopSearch:
			self.wndShopSearch = uiShopSearch.ShopSearchWindow(ui.__mem_func__(self.OpenWhisperDialog))

		if self.wndShopSearch.IsShow():
			self.wndShopSearch.Close()
		else:
			self.wndShopSearch.Open()

	def StartShopSearchByVnum(self, vnum):
		if not self.wndShopSearch or not self.wndShopSearch.IsShow():
			self.ToggleShopSearchWindow()

		self.wndShopSearch.SearchItemVnum(vnum)
	# END_OF_SHOP_SEARCH

	# MAINTENANCE
	def ShowMaintenanceSign(self, timeLeft, duration):
		if not self.wndMaintenance:
			self.wndMaintenance = uiMaintenance.MaintenanceBoard()
		self.wndMaintenance.Open(timeLeft, duration)

	def HideMaintenanceSign(self):
		if self.wndMaintenance:
			self.wndMaintenance.Close()
	# END_OF_MAINTENANCE

	# ANNOUNCE
	def ShowSysAnnounceSign(self, message):
		if not self.wndSysAnnounce:
			self.wndSysAnnounce = uiSystemAnnounce.MaintenanceBoard()
		self.wndSysAnnounce.Open(message)

	def HideSysAnnounceSign(self):
		if self.wndSysAnnounce:
			self.wndSysAnnounce.Close()
	# END_OF_ANNOUNCE

	# ITEM_REFUND
	def CreateItemRefundWindow(self):
		if not self.wndItemRefund:
			self.wndItemRefund = uiItemRefund.ItemRefundBoard()
			self.wndItemRefund.Close()

	def ClearItemRefund(self):
		self.CreateItemRefundWindow()

		self.wndItemRefund.Clear()

	def AddItemRefund(self, cell):
		self.CreateItemRefundWindow()

		self.wndItemRefund.AppendItem(int(cell))

	def OpenItemRefund(self, gold):
		self.CreateItemRefundWindow()
		self.wndItemRefund.Open(int(gold))
	# END_OF_ITEM_REFUND

	if app.ENABLE_ZODIAC:
		def ToggleAnimasphereWindow(self):
			if not self.wndAnimasphere:
				return
			if False == player.IsObserverMode():
				if False == self.wndAnimasphere.IsShow():
					self.wndAnimasphere.Show()
					self.wndAnimasphere.SetTop()
				else:
					self.wndAnimasphere.Close()
	# PET_SYSTEM
	def CanOpenPetWindow(self):
		if not self.wndPet:
			self.wndPet = uiAnimal.PetWindow()

		return self.wndPet.CanOpen()

	def TogglePetWindow(self):
		if not self.wndPet:
			self.wndPet = uiAnimal.PetWindow()

		if self.wndPet.IsShow():
			self.wndPet.Close()
		elif self.wndPet.CanOpen():
			self.wndPet.Open()

	def RefreshPetWindow(self):
		if self.wndPet:
			self.wndPet.Refresh()
		# if self.wndSideBar:
		#	self.wndSideBar.Refresh()
	# END_OF_PET_SYSTEM

	# MOUNT_SYSTEM
	def CanOpenMountWindow(self):
		if not self.wndMount:
			self.wndMount = uiAnimal.MountWindow()

		return self.wndMount.CanOpen()

	def ToggleMountWindow(self):
		if not self.wndMount:
			self.wndMount = uiAnimal.MountWindow()

		if self.wndMount.IsShow():
			self.wndMount.Close()
		elif self.wndMount.CanOpen():
			self.wndMount.Open()

	def RefreshMountWindow(self):
		if self.wndMount:
			self.wndMount.Refresh()
		# if self.wndSideBar:
		#	self.wndSideBar.Refresh()
	# END_OF_MOUNT_SYSTEM

	## SWITCHBOT
	def ToggleSwitchbotWindow(self):
		if constInfo.NEW_SWITCHBOT_ENABLED:
			if not self.wndSwitchbot:
				if constInfo.switchbotSave:
					self.wndSwitchbot = constInfo.switchbotSave
				else:
					self.wndSwitchbot = uiSwitchbot2.SwitchbotWindow()
			
			if self.wndSwitchbot.IsShow():
				self.wndSwitchbot.Close()
			else:
				self.wndSwitchbot.Open()

		else:
			if self.wndSwitchbot and self.wndSwitchbot.IsShow():
				self.wndSwitchbot.Hide()
			else:
				if not self.wndSwitchbot:
					import uiSwitchBot
					self.wndSwitchbot = uiSwitchBot.SwitchBot()
				self.wndSwitchbot.Show()

	def OnSwitchbotEnd(self, slotIdx):
		if self.wndSwitchbot:
			self.wndSwitchbot.GAME_OnEnd(slotIdx)

	def OnSwitchbotFinish(self, slotIdx, realSlotIdx):
		if self.wndSwitchbot:
			self.wndSwitchbot.GAME_OnFinish(slotIdx)

		self.tooltipItem.SetInventoryItem(int(realSlotIdx))

	def OnSwitchbotUseSwitcher(self, slot):
		if constInfo.NEW_SWITCHBOT_ENABLED and self.wndSwitchbot:
			self.wndSwitchbot.GAME_OnUpdateConsumption(int(slot))
	## END_OF_SWITCHBOT

	## DRAGONSOUL
	def DragonSoulActivate(self, deck):
		if app.ENABLE_DRAGON_SOUL_SYSTEM:
			self.wndDragonSoul.ActivateDragonSoulByExtern(deck)

	def DragonSoulDeactivate(self):
		if app.ENABLE_DRAGON_SOUL_SYSTEM:
			self.wndDragonSoul.DeactivateDragonSoul()
			
	def DragonSoulGiveQuilification(self):
		self.DRAGON_SOUL_IS_QUALIFIED = True
#		self.wndExpandedTaskBar.SetToolTipText(uiTaskBar.ExpandedTaskBar.BUTTON_DRAGON_SOUL, uiScriptLocale.TASKBAR_DRAGON_SOUL)

	def ToggleDragonSoulWindow(self):
		if False == player.IsObserverMode():
			if app.ENABLE_DRAGON_SOUL_SYSTEM:
				if False == self.wndDragonSoul.IsShow():
					if self.DRAGON_SOUL_IS_QUALIFIED:
						self.wndDragonSoul.Show()
						self.wndDragonSoul.SetTop()
					else:
						try:
							self.wndPopupDialog.SetText(localeInfo.DRAGON_SOUL_UNQUALIFIED)
							self.wndPopupDialog.Open()
						except:
							self.wndPopupDialog = uiCommon.PopupDialog()
							self.wndPopupDialog.SetText(localeInfo.DRAGON_SOUL_UNQUALIFIED)
							self.wndPopupDialog.Open()
				else:
					self.wndDragonSoul.Close()
		
	def ToggleDragonSoulWindowWithNoInfo(self):
		if False == player.IsObserverMode():
			if app.ENABLE_DRAGON_SOUL_SYSTEM:
				if False == self.wndDragonSoul.IsShow():
					if self.DRAGON_SOUL_IS_QUALIFIED:
						self.wndDragonSoul.Show()
				else:
					self.wndDragonSoul.Close()
				
	def FailDragonSoulRefine(self, reason, inven_type, inven_pos):
		if False == player.IsObserverMode():
			if app.ENABLE_DRAGON_SOUL_SYSTEM:
				if True == self.wndDragonSoulRefine.IsShow():
					self.wndDragonSoulRefine.RefineFail(reason, inven_type, inven_pos)
 
	def SucceedDragonSoulRefine(self, inven_type, inven_pos):
		if False == player.IsObserverMode():
			if app.ENABLE_DRAGON_SOUL_SYSTEM:
				if True == self.wndDragonSoulRefine.IsShow():
					self.wndDragonSoulRefine.RefineSucceed(inven_type, inven_pos)
 
	def OpenDragonSoulRefineWindow(self):
		if False == player.IsObserverMode():
			if app.ENABLE_DRAGON_SOUL_SYSTEM:
				if False == self.wndDragonSoulRefine.IsShow():
					self.wndDragonSoulRefine.Show()
					if None != self.wndDragonSoul:
						if False == self.wndDragonSoul.IsShow():
							self.wndDragonSoul.Show()

	def CloseDragonSoulRefineWindow(self):
		if False == player.IsObserverMode():
			if app.ENABLE_DRAGON_SOUL_SYSTEM:
				if True == self.wndDragonSoulRefine.IsShow():
					self.wndDragonSoulRefine.Close()
	## END_OF_DRAGONSOUL

	def Horse_UpdateRage(self, rageLevel, ragePct):
		if self.wndTaskBar:
			self.wndTaskBar.SetRage(int(rageLevel), int(ragePct))

	def Horse_RefineStart(self, refineIndex, currentLevel, cost):
		if not self.wndHorseUpgrade:
			self.wndHorseUpgrade = uiHorseUpgrade.HorseUpgradeWindow()

		self.wndHorseUpgrade.BINARY_ClearMaterial()
		self.wndHorseUpgrade.BINARY_SetRefineIndex(refineIndex)
		self.wndHorseUpgrade.BINARY_SetCurrentLevel(currentLevel)
		self.wndHorseUpgrade.BINARY_SetCost(cost)

	def Horse_RefineAddItem(self, vnum, count):
		self.wndHorseUpgrade.BINARY_AddMaterial(vnum, count)

	def Horse_RefineOpen(self):
		self.wndHorseUpgrade.Open()

	def Horse_RefineResult(self, success):
		self.wndHorseUpgrade.OnResult(success)

	def OpenGayaShop(self):
		if not self.wndGayaShop:
			self.wndGayaShop = uiGaya.GayaShopWindow(self.tooltipItem)
		self.wndGayaShop.Open()

	# FAKEBUFF
	def OpenFakeBuffSkills(self):
		if not self.wndFakeBuffSkill:
			self.wndFakeBuffSkill = uiFakeBuff.FakeBuffSkillWindow()
		self.wndFakeBuffSkill.Open()

	def RefreshFakeBuffSkill(self, skillVnum):
		if self.wndFakeBuffSkill:
			self.wndFakeBuffSkill.RefreshBySkill(skillVnum)
	# END_OF_FAKEBUFF

	# ATTRTREE
	def ToggleAttrTree(self):
		if self.wndAttrTree and self.wndAttrTree.IsShow():
			self.wndAttrTree.Close()
		else:
			self.OpenAttrTree()

	def OpenAttrTree(self):
		if not self.wndAttrTree:
			self.wndAttrTree = uiAttrTree.AttrTreeWindow()
		self.wndAttrTree.Open()

	def RefreshAttrTree(self, row, col):
		if self.wndAttrTree:
			self.wndAttrTree.RefreshCell(row, col)

	def RefineAttrTree(self, row, col, price):
		self.wndAttrTree.OpenRefineDialog(row, col, price)

	def RefineAttrTreeMaterial(self, vnum, count):
		self.wndAttrTree.AppendRefineMaterial(vnum, count)
	# END_OF_ATTRTREE

	# EVENT_SYSTEM
	def OpenEventJoinWindow(self, eventIndex, eventName, eventDesc):
		self.wndEventJoin.Open(eventIndex, eventName, eventDesc)

	def CloseEventJoinWindow(self, eventIndex):
		if self.wndEventJoin.GetEventIndex() == eventIndex:
			self.wndEventJoin.Close()

	def OpenEventEmpireWarScoreWindow(self, timeLeft, kills1, deads1, kills2, deads2, kills3, deads3):
		self.wndEventEmpireWarScoreBoard.Open(timeLeft, kills1, deads1, kills2, deads2, kills3, deads3)

	def UpdateEventEmpireWarScore(self, empire, kills, deads):
		self.wndEventEmpireWarScoreBoard.UpdateScore(empire, kills, deads)

	def FinishEventEmpireWar(self):
		self.wndEventEmpireWarScoreBoard.OnFinish()
	# END_OF_EVENT_SYSTEM

	if app.ENABLE_COSTUME_BONUS_TRANSFER:
		def CostumeBonusTransferWindowOpen(self):
			if self.wndCostumeBonusTransfer.IsShow():
				return

			if self.inputDialog or self.privateShopBuilder.IsShow():
				chat.AppendChat(chat.CHAT_TYPE_INFO, localeInfo.COMB_ITEM_NOTICE_NOT_OPEN)
				return

			if self.dlgRefineNew and self.dlgRefineNew.IsShow():
				chat.AppendChat(chat.CHAT_TYPE_INFO, localeInfo.COMB_ITEM_NOTICE_NOT_OPEN2)
				return

			if not self.wndInventory.IsShow():
				self.wndInventory.Show()

			self.wndCostumeBonusTransfer.Open()

		def CostumeBonusTransferWindowClose(self):
			if not self.wndCostumeBonusTransfer.IsShow():
				return

			self.wndCostumeBonusTransfer.CloseDialog()

	if constInfo.ENABLE_CRYSTAL_SYSTEM:
		def OpenCrystalRefine(self, crystal_pos, scroll_pos, next_clarity_type, next_clarity_level, required_fragments):
			self.CloseCrystalRefine()

			owned_fragments = 0
			for i in xrange(player.INVENTORY_SLOT_COUNT):
				vnum = player.GetItemIndex(i)
				if vnum != 0:
					item.SelectItem(1, 2, vnum)
					if item.GetItemType() == item.ITEM_TYPE_CRYSTAL and item.GetItemSubType() == item.CRYSTAL_FRAGMENT:
						owned_fragments += player.GetItemCount(i)
						if owned_fragments >= required_fragments:
							break

			if owned_fragments < required_fragments:
				wnd = uiCommon.PopupDialog()
				wnd.SetText(localeInfo.CRYSTAL_REFINE_INFO_TEXT % required_fragments)
				wnd.SetAcceptEvent(ui.__mem_func__(self.CloseCrystalRefine))
				wnd.Open()

			else:
				wnd = uiCommon.QuestionDialog()
				wnd.SetText((localeInfo.CRYSTAL_REFINE_INFO_TEXT % required_fragments) + " " + localeInfo.CRYSTAL_REFINE_INFO_QUESTION)
				wnd.SAFE_SetAcceptEvent(self.AcceptCrystalRefine)
				wnd.SAFE_SetCancelEvent(self.CloseCrystalRefine)
				wnd.crystal_pos = crystal_pos
				wnd.scroll_pos = scroll_pos
				wnd.Open()

			self.wndCrystalRefineQuestion = wnd

		def AcceptCrystalRefine(self):
			wnd = self.wndCrystalRefineQuestion
			net.SendCrystalRefinePacket(wnd.crystal_pos[0], wnd.crystal_pos[1], wnd.scroll_pos[0], wnd.scroll_pos[1])

			self.CloseCrystalRefine()

		def CloseCrystalRefine(self):
			if self.wndCrystalRefineQuestion:
				self.wndCrystalRefineQuestion.Hide()
				self.wndCrystalRefineQuestion = None

		def SetCrystalUsingSlot(self, window, cell, is_active):
			if window == player.INVENTORY:
				self.wndInventory.SetSlotActive(cell, is_active)

	#####################################################################################
	### Guild Building ###

	def BUILD_OpenWindow(self):
		self.wndGuildBuilding = uiGuild.BuildGuildBuildingWindow()
		self.wndGuildBuilding.Open()
		self.wndGuildBuilding.wnds = self.__HideWindows()
		self.wndGuildBuilding.SetCloseEvent(ui.__mem_func__(self.BUILD_CloseWindow))

	def BUILD_CloseWindow(self):
		self.__ShowWindows(self.wndGuildBuilding.wnds)
		self.wndGuildBuilding = None

	def BUILD_OnUpdate(self):
		if not self.wndGuildBuilding:
			return

		if self.wndGuildBuilding.IsPositioningMode():
			import background
			x, y, z = background.GetPickingPoint()
			self.wndGuildBuilding.SetBuildingPosition(x, y, z)

	def BUILD_OnMouseLeftButtonDown(self):
		if not self.wndGuildBuilding:
			return

		# GUILD_BUILDING
		if self.wndGuildBuilding.IsPositioningMode():
			self.wndGuildBuilding.SettleCurrentPosition()
			return True
		elif self.wndGuildBuilding.IsPreviewMode():
			pass
		else:
			return True
		# END_OF_GUILD_BUILDING
		return False

	def BUILD_OnMouseLeftButtonUp(self):
		if not self.wndGuildBuilding:
			return

		if not self.wndGuildBuilding.IsPreviewMode():
			return True

		return False

	def BULID_EnterGuildArea(self, areaID):
		# GUILD_BUILDING
		mainCharacterName = player.GetMainCharacterName()
		masterName = guild.GetGuildMasterName()

		if mainCharacterName != masterName:
			return

		if areaID != player.GetGuildID():
			return
		# END_OF_GUILD_BUILDING

		self.wndGameButton.ShowBuildButton()

	def BULID_ExitGuildArea(self, areaID):
		self.wndGameButton.HideBuildButton()

	#####################################################################################

	def IsEditLineFocus(self):
		if self.ChatWindow.chatLine.IsFocus():
			return 1

		if self.ChatWindow.chatToLine.IsFocus():
			return 1

		return 0

	if app.AHMET_FISH_EVENT_SYSTEM:

		def MiniGameFishUse(self, shape, useCount):

			if self.wndJigsaw:
				self.wndJigsaw.MiniGameFishUse(shape, useCount)
			
		def MiniGameFishAdd(self, pos, shape):

			if self.wndJigsaw:
				self.wndJigsaw.MiniGameFishAdd(pos, shape)
			
		def MiniGameFishReward(self, vnum):

			if self.wndJigsaw:
				self.wndJigsaw.MiniGameFishReward(vnum)
				
		def MiniGameFishCount(self, count):

			if self.wndJigsaw:
				self.wndJigsaw.MiniGameFishCount(count)

		def OpenJigsawEvent(self):
			
			if not self.wndJigsaw:
				self.wndJigsaw = uiMiniGameFishEvent.MiniGameFish()
			
			if self.tooltipItem:
				self.wndJigsaw.SetItemToolTip(self.tooltipItem)

			self.wndJigsaw.Open()


		def SetFishEventStatus(self, isEnable):
			
			if isEnable:
				self.wndJigsawIcon = uiMiniGameFishEvent.JigsawIcon()
				self.wndJigsawIcon.SetOnClickGame(self.OpenJigsawEvent)
				self.wndJigsawIcon.SetTop()
				self.wndJigsawIcon.Show() 

	def OpenMovieMaker(self):
		# if test_server or player.GetName().startswith("["):
		if not self.wndMovieMaker:
			import uiMovieMaker
			self.wndMovieMaker = uiMovieMaker.MovieMakerWindow(self)

		self.wndMovieMaker.Open()

	if constInfo.ENABLE_ANGELSDEMONS_EVENT:
		def OpenAngelsDemonsSelectWindow(self):
			tchat("OpenAngelsDemonsSelectWindow")
			
			if not self.wndAngelsDemonsSelect:
				self.wndAngelsDemonsSelect = uiEvent.AngelsDemonsSelectFractionWindow()

			self.wndAngelsDemonsSelect.Open()

	def HideAllQuestWindow(self):
		
		if uiQuest.QuestDialog.__dict__.has_key("QuestCurtain"):
			uiQuest.QuestDialog.QuestCurtain.Close()

		if self.wndQuestWindow:
			for q in self.wndQuestWindow:
				q.OnCancel()
				q.Hide()

	def EmptyFunction(self):
		pass

	if constInfo.ENABLE_XMAS_EVENT:
		def OpenXmasEventWindow(self):
			self.wndXmasEvent.Open()

		def XmasRecivedReward(self, day):
			self.wndXmasEvent.RecivedReward(day)

	if constInfo.ENABLE_EQUIPMENT_CHANGER:
		def ToogleEquipmentChangerWindow(self):
			if __SERVER__ == 2:
				return
			if not self.wndEquipmentChanger:
				self.wndEquipmentChanger = uiEquipmentChanger.EquipmentChangerWindow()
				self.wndEquipmentChanger.SetItemToolTip(self.tooltipItem)
			if self.wndEquipmentChanger.IsShow():
				self.wndEquipmentChanger.Hide()
			else:
				self.wndEquipmentChanger.Open()

		def RefreshEquipmentChanger(self):
			if self.wndEquipmentChanger:
				self.wndEquipmentChanger.Refresh()

	if constInfo.ENABLE_RUNE_PAGES:
		def SetRunePage(self, index, vnum):
			if self.wndRuneSub:
				self.wndRuneSub.SetRunePage(index, vnum)

		def SelectRunePage(self, page):
			if self.wndRuneSub:
				self.wndRuneSub.SelectRunePage(page)

	if constInfo.CHANGE_SKILL_COLOR:
		def SetUnlockedSkill(self, skill):
			skill = int(skill)
			if skill <= 5:
				self.wndCharacter.SetUnlockedSkill(skill)
			else:
				uiFakeBuff.SetUnlockedSkill(skill) # like this because the instance might not be created at this point

	if constInfo.ENABLE_REACT_EVENT:
		def OpenReactEvent(self):
			self.wndReactEvent.Open()

		def ClearReactEvent(self):
			self.wndReactEvent.Clear()

		def CloseReactEvent(self):
			self.wndReactEvent.Close()

		def NoticeReactEvent(self, text):
			text = text.replace("#", " ")
			self.wndReactEvent.Notice(text)

		def ClearNoticeReactEvent(self):
			self.wndReactEvent.ClearNotice()

		def TimerReactEvent(self, text):
			self.wndReactEvent.SetTimer(text)

	if constInfo.ENABLE_WHEEL_OF_FRIGHT:
		def OpenWheelOfFright(self):
			self.wndWheelOfFright.Open()
			if constInfo.ENABLE_WHEEL_OF_FRIGHT:
				self.wndWheelOfFright.SetItemToolTip(self.tooltipItem)

		def WheelOfFortuneSpin(self, spins, items):
			self.wndWheelOfFright.Spin(int(spins), items)

	if constInfo.ENABLE_BATTLEPASS:
		def OpenBattlePassWindow(self):
			if not self.wndBattlePass.IsShow():
				self.wndBattlePass.Open()
			else:
				self.wndBattlePass.Hide()

	def BlackJackCommand(self, type, arg1, arg2, arg3, arg4):
		if self.wndBlackJack.IsShow():
			self.wndBlackJack.ReceiveInfo(type, arg1, arg2, arg3, arg4)

	def RecvSoldItem(self, vnum, count, price):
		constInfo.SOLD_ITEMS_QUEUE.append([vnum, count, price])
		self.wndGameButton.ShowSoldItemButton(vnum, count, price)

	def DungeonTasks_Set(self, var, text, state):
		if not constInfo.DUNGEON_TASKS:
			return
		if not self.questTaskWnd:
			self.questTaskWnd = uiQuestTask.QuestTask()
		if not self.questTaskWnd.IsShow():
			self.questTaskWnd.Show()

		self.questTaskWnd.AppendTask(var, text, state)

	def DungeonTasks_Remove(self, var):
		if not constInfo.DUNGEON_TASKS:
			return
		if self.questTaskWnd:
			self.questTaskWnd.Remove(var)

	def DungeonTasks_Clear(self):
		if not constInfo.DUNGEON_TASKS:
			return
		if self.questTaskWnd:
			self.questTaskWnd.Clear()
			self.questTaskWnd.Hide()