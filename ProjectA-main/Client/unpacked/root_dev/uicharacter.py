import ui
import uiScriptLocale
import app
import net
import dbg
import snd
import player
import mouseModule
import wndMgr
import skill
import playerSettingModule
import quest
import localeInfo
import uiToolTip
import constInfo
import emotion
import chr
import uistatsboard
import uiPassiveSkill
import cfg
import uiCommon

if constInfo.CHANGE_SKILL_COLOR:
	import uiSkillColor

SHOW_ONLY_ACTIVE_SKILL = False
SHOW_LIMIT_SUPPORT_SKILL_LIST = []
HIDE_SUPPORT_SKILL_POINT = True

FACE_IMAGE_DICT = {
	playerSettingModule.RACE_WARRIOR_M	: "icon/face/warrior_m.tga",
	playerSettingModule.RACE_WARRIOR_W	: "icon/face/warrior_w.tga",
	playerSettingModule.RACE_ASSASSIN_M	: "icon/face/assassin_m.tga",
	playerSettingModule.RACE_ASSASSIN_W	: "icon/face/assassin_w.tga",
	playerSettingModule.RACE_SURA_M		: "icon/face/sura_m.tga",
	playerSettingModule.RACE_SURA_W		: "icon/face/sura_w.tga",
	playerSettingModule.RACE_SHAMAN_M	: "icon/face/shaman_m.tga",
	playerSettingModule.RACE_SHAMAN_W	: "icon/face/shaman_w.tga",
	# playerSettingModule.RACE_WOLFMAN_M	: "icon/face/wolfman_m.tga",
}

class CharacterWindow(ui.ScriptWindow):

	ACTIVE_PAGE_SLOT_COUNT = 8
	SUPPORT_PAGE_SLOT_COUNT = 12

	PAGE_SLOT_COUNT = 12
	PAGE_HORSE = 2

	SKILL_GROUP_NAME_DICT = {
		playerSettingModule.JOB_WARRIOR	: { 1 : localeInfo.SKILL_GROUP_WARRIOR_1,	2 : localeInfo.SKILL_GROUP_WARRIOR_2, },
		playerSettingModule.JOB_ASSASSIN	: { 1 : localeInfo.SKILL_GROUP_ASSASSIN_1,	2 : localeInfo.SKILL_GROUP_ASSASSIN_2, },
		playerSettingModule.JOB_SURA		: { 1 : localeInfo.SKILL_GROUP_SURA_1,		2 : localeInfo.SKILL_GROUP_SURA_2, },
		playerSettingModule.JOB_SHAMAN		: { 1 : localeInfo.SKILL_GROUP_SHAMAN_1,	2 : localeInfo.SKILL_GROUP_SHAMAN_2, },
		# playerSettingModule.JOB_WOLFMAN		: { 0 : localeInfo.SKILL_GROUP_WOLFMAN,		1 : localeInfo.SKILL_GROUP_WOLFMAN, },
	}

	STAT_DESCRIPTION =	{
		"HTH" : localeInfo.STAT_TOOLTIP_CON,
		"INT" : localeInfo.STAT_TOOLTIP_INT,
		"STR" : localeInfo.STAT_TOOLTIP_STR,
		"DEX" : localeInfo.STAT_TOOLTIP_DEX,
	}


	STAT_MINUS_DESCRIPTION = localeInfo.STAT_MINUS_DESCRIPTION

	QUEST_CATEGORY_HEIGHT = 20
	QUEST_ENTRY_BASE_HEIGHT = 19
	QUEST_ENTRY_EXTRA_HEIGHT_PER_LINE = 16

	SKILL_GRADE_SLOT_COUNT = 3

	def __init__(self, interfaceHandle):
		ui.ScriptWindow.__init__(self)
		self.state = "STATUS"
		self.isLoaded = 0
		self.interfaceHandle = interfaceHandle

		self.toolTipSkill = 0

		if constInfo.CHANGE_SKILL_COLOR:
			self.skillColorWnd = None

		self.__Initialize()
		self.__LoadWindow()

		self.statusPlusCommandDict={
			"HTH" : "/stat ht",
			"INT" : "/stat iq",
			"STR" : "/stat st",
			"DEX" : "/stat dx",
		}

		self.statusMinusCommandDict={
			"HTH-" : "/stat- ht",
			"INT-" : "/stat- iq",
			"STR-" : "/stat- st",
			"DEX-" : "/stat- dx",
		}

	def __del__(self):
		self.interfaceHandle = None
		ui.ScriptWindow.__del__(self)

	def __Initialize(self):
		self.refreshToolTip = 0
		self.curSelectedSkillGroup = 0
		self.canUseHorseSkill = -1

		self.toolTip = None
		self.toolTipJob = None
		self.toolTipAlignment = None
		self.toolTipSkill = None

		self.faceImage = None
		self.statusPlusLabel = None
		self.statusPlusValue = None
		self.activeSlot = None
		self.tabDict = None
		self.tabButtonDict = None
		self.pageDict = None
		self.titleBarDict = None
		self.statusPlusButtonDict = None
		self.statusMinusButtonDict = None

		self.skillPageDict = None
		self.skillGroupButton = ()

		self.activeSlot = None
		self.activeSkillPointValue = None
		self.supportSkillPointValue = None
		self.skillGroupButton1 = None
		self.specialSkillButton = None
		self.skillGroupButton2 = None
		self.activeSkillGroupName = None
		self.atkspeedlimit = None

		self.guildNameSlot = None
		self.guildNameValue = None
		self.characterNameSlot = None
		self.characterNameValue = None

		self.emotionToolTip = None
		self.soloEmotionSlot = None
		self.dualEmotionSlot = None
		if constInfo.ENABLE_NEW_EMOTES:
			self.newEmoticonSlot = None

		self.questCategories = []
		self.currentQuestCategory = 0
		self.currentQuestMaxBase = 0
		self.currentQuestBase = 0
		self.questShowingStartIndex = 0
		self.inputMoneyDlg = None

		self.uiStatsBoard = None

		if __SERVER__ == 2:
			self.wndPassive = None
		else:
			self.wndPassive = uiPassiveSkill.PassiveSkillWindow()

		if constInfo.CHANGE_SKILL_COLOR:
			self.CUSTOM_SKILL_STATUS = {
				0 : 0,
				1 : 0,
				2 : 0,
				3 : 0,
				4 : 0,
				5 : 0,
			}

			self.open_gui_btn = []
			if not self.skillColorWnd:
				self.skillColorWnd = uiSkillColor.SkillColorWindow()
			else:
				self.skillColorWnd.Destroy()
				del self.skillColorWnd

		if constInfo.LEADERSHIP_EXTENSION:
			self.leadershipWnd = None

	def Show(self):
		self.__LoadWindow()

		ui.ScriptWindow.Show(self)

	def __LoadScript(self, fileName):
		pyScrLoader = ui.PythonScriptLoader()
		pyScrLoader.LoadScriptFile(self, fileName)	
		
	def __BindObject(self):
		self.toolTip = uiToolTip.ToolTip()
		self.toolTipJob = uiToolTip.ToolTip()
		self.toolTipAlignment = uiToolTip.ToolTip(130)		

		self.faceImage = self.GetChild("Face_Image")

		faceSlot=self.GetChild("Face_Slot")

		self.statusPlusLabel = self.GetChild("Status_Plus_Label")
		self.statusPlusValue = self.GetChild("Status_Plus_Value")		

		self.characterNameSlot = self.GetChild("Character_Name_Slot")			
		self.characterNameValue = self.GetChild("Character_Name")
		self.guildNameSlot = self.GetChild("Guild_Name_Slot")
		self.guildNameValue = self.GetChild("Guild_Name")
		self.characterNameSlot.SAFE_SetStringEvent("MOUSE_OVER_IN", self.__ShowAlignmentToolTip)
		self.characterNameSlot.SAFE_SetStringEvent("MOUSE_OVER_OUT", self.__HideAlignmentToolTip)

		self.activeSlot = self.GetChild("Skill_Active_Slot")
		self.activeSkillPointValue = self.GetChild("Active_Skill_Point_Value")
		self.supportSkillPointValue = self.GetChild("Support_Skill_Point_Value")
		self.skillGroupButton1 = self.GetChild("Skill_Group_Button_1")
		self.skillGroupButton2 = self.GetChild("Skill_Group_Button_2")
		self.specialSkillButton = self.GetChild("Special_Skill_Group_Btn")
		if __SERVER__ == 2:
			self.specialSkillButton.Hide()
		self.activeSkillGroupName = self.GetChild("Active_Skill_Group_Name")
		self.atkspeedlimit = self.GetChild("attackspeed_limit_btn")
		# self.atkspeedlimit.Hide()

		self.tabDict = {
			"STATUS"	: self.GetChild("Tab_01"),
			"SKILL"		: self.GetChild("Tab_02"),
			"EMOTICON"	: self.GetChild("Tab_03"),
			"QUEST"		: self.GetChild("Tab_04"),
		}

		self.tabButtonDict = {
			"STATUS"	: self.GetChild("Tab_Button_01"),
			"SKILL"		: self.GetChild("Tab_Button_02"),
			"EMOTICON"	: self.GetChild("Tab_Button_03"),
			"QUEST"		: self.GetChild("Tab_Button_04")
		}

		self.pageDict = {
			"STATUS"	: self.GetChild("Character_Page"),
			"SKILL"		: self.GetChild("Skill_Page"),
			"EMOTICON"	: self.GetChild("Emoticon_Page"),
			"QUEST"		: self.GetChild("Quest_Page")
		}
		self.pageDict['QUEST'].scrollBar = self.GetChild("Quest_ScrollBar")
		self.pageDict['QUEST'].scrollBar.SetScrollEvent(ui.__mem_func__(self.__OnScrollQuest))

		self.titleBarDict = {
			"STATUS"	: self.GetChild("Character_TitleBar"),
			"SKILL"		: self.GetChild("Skill_TitleBar"),
			"EMOTICON"	: self.GetChild("Emoticon_TitleBar"),
			"QUEST"		: self.GetChild("Quest_TitleBar")
		}

		self.statusPlusButtonDict = {
			"HTH"		: self.GetChild("HTH_Plus"),
			"INT"		: self.GetChild("INT_Plus"),
			"STR"		: self.GetChild("STR_Plus"),
			"DEX"		: self.GetChild("DEX_Plus"),
		}

		self.statusMinusButtonDict = {
			"HTH-"		: self.GetChild("HTH_Minus"),
			"INT-"		: self.GetChild("INT_Minus"),
			"STR-"		: self.GetChild("STR_Minus"),
			"DEX-"		: self.GetChild("DEX_Minus"),
		}

		self.skillPageDict = {
			"ACTIVE" : self.GetChild("Skill_Active_Slot"),
			"SUPPORT" : self.GetChild("Skill_ETC_Slot"),
			"HORSE" : self.GetChild("Skill_Active_Slot"),
		}

		self.skillPageStatDict = {
			"SUPPORT"	: player.SKILL_SUPPORT,
			"ACTIVE"	: player.SKILL_ACTIVE,
			"HORSE"		: player.SKILL_MOUNT,
		}

		self.skillGroupButton = (
			self.GetChild("Skill_Group_Button_1"),
			self.GetChild("Skill_Group_Button_2"),
		)

		
		global SHOW_ONLY_ACTIVE_SKILL
		global HIDE_SUPPORT_SKILL_POINT
		if SHOW_ONLY_ACTIVE_SKILL or HIDE_SUPPORT_SKILL_POINT:	
			self.GetChild("Support_Skill_Point_Label").Hide()

		self.soloEmotionSlot = self.GetChild("SoloEmotionSlot")
		self.dualEmotionSlot = self.GetChild("DualEmotionSlot")
		if constInfo.ENABLE_NEW_EMOTES:
			self.newEmoticonSlot = self.GetChild("NewEmotesSlot")
		self.__SetEmotionSlot()

		self.questCategories = []
		self.currentQuestCategory = 0
		self.questShowingStartIndex = 0

		for i in xrange(len(constInfo.QUEST_CATEGORIES)):
			item = ui.RadioButton()
			item.SetParent(self.pageDict['QUEST'])
			item.SetUpVisual('d:/ymir work/ui/game/quest/Quest_Cat_Title_Up.tga')
			item.SetOverVisual('d:/ymir work/ui/game/quest/Quest_Cat_Title_Right.tga')
			item.SetDownVisual('d:/ymir work/ui/game/quest/Quest_Cat_Title_Down.tga')
			item.SAFE_SetEvent(self.__ClickQuestCat, i)
			item.Show()
			item.UpdateRect()
			item.questItems = []

			textLine = ui.TextLine()
			textLine.SetFontName(constInfo.GetChoosenFontName())
			textLine.SetParent(item)
			textLine.SetPosition(28, 1)
			textLine.AddFlag("not_pick")
			textLine.Show()
			item.textLine = textLine

			self.questCategories.append(item)

		if constInfo.BONI_BOARD:

			# init here
			if not self.uiStatsBoard:
				self.uiStatsBoard = uistatsboard.StatsBoard()

			self.MainBoard = self.GetChild("board")
			self.ExpandBtn = ui.MakeButton(self.MainBoard, 240, 120, "", "d:/ymir work/ui/game/belt_inventory/", "btn_minimize_normal.tga", "btn_minimize_over.tga", "btn_minimize_down.tga")
			self.ExpandBtn.SetEvent(ui.__mem_func__(self.__ClickExpandButton))
			self.MinimizeBtn = ui.MakeButton(self.MainBoard, 240, 120, "", "d:/ymir work/ui/game/belt_inventory/", "btn_expand_normal.tga", "btn_expand_over.tga", "btn_expand_down.tga")
			self.MinimizeBtn.SetEvent(ui.__mem_func__(self.__ClickMinimizeButton))

			self.ExpandBtn.Show()
			self.MinimizeBtn.Hide()

		self.atkspeedlimit.SetEvent(ui.__mem_func__(self.__ClickAtkSpeedLimit))
		self.atkspeedlimit.SetTop()
			
	def ResetButtons(self):
		
		if self.ExpandBtn and self.MinimizeBtn:
			self.ExpandBtn.Show()
			self.MinimizeBtn.Hide()

	def __ClickExpandButton(self):

		# should never happen
		if not self.uiStatsBoard:
			self.uiStatsBoard = uistatsboard.StatsBoard()
			self.uiStatsBoard.Show()
		else:
			self.uiStatsBoard.Show()

		# adjust pos
		(x, y) = self.GetGlobalPosition()
		self.uiStatsBoard.SetPosition(x + 251, y + 3)
				
		self.ExpandBtn.Hide()
		self.MinimizeBtn.Show()

	def __ClickMinimizeButton(self):
		self.uiStatsBoard.Hide()
		self.MinimizeBtn.Hide()
		self.ExpandBtn.Show()

	def __ClickAtkSpeedLimit(self):
		self.inputMoneyDlg = uiCommon.InputDialog()
		self.inputMoneyDlg.SetTitle(localeInfo.ATTACKSPEED_LIMIT_DESC % (100, 200))
		self.inputMoneyDlg.SetAcceptEvent(ui.__mem_func__(self.OnAcceptInputMoneyDialog))
		self.inputMoneyDlg.SetCancelEvent(ui.__mem_func__(self.OnCloseInputMoneyDialog))
		self.inputMoneyDlg.SetBoardWidth(260)
		self.inputMoneyDlg.Open()

	def OnAcceptInputMoneyDialog(self):
		if not self.inputMoneyDlg:
			return

		text = self.inputMoneyDlg.GetText()
		if not text:
			return True

		try:
			if int(text) > 0 and (int(text) < 100 or int(text) > 200):
				tchat("not between 100-200")
				return True
		except:
			return True

		tchat("/attackspeed_limit %d" % int(text))
		net.SendChatPacket("/attackspeed_limit %d" % int(text))
		self.OnCloseInputMoneyDialog()
		return True

	def OnCloseInputMoneyDialog(self):
		if self.inputMoneyDlg:
			self.inputMoneyDlg.Close()

		self.inputMoneyDlg = None
		return True

	def OnMoveWindow(self, x, y):
		if self.uiStatsBoard:
			self.uiStatsBoard.AdjustPosition(x, y)

		if constInfo.SAVE_WINDOW_POSITION:
			cfg.Set(cfg.SAVE_GENERAL, "wnd_pos_chr", ("%d %d") % (x, y))

		if constInfo.LEADERSHIP_EXTENSION:
			if self.leadershipWnd:
				self.leadershipWnd.SetPosition(x, y + 365)

	if constInfo.SAVE_WINDOW_POSITION:
		def Show(self):
			if int(cfg.Get(cfg.SAVE_GENERAL, "save_wnd_pos", "0")):
				x, y = map(int, cfg.Get(cfg.SAVE_GENERAL, "wnd_pos_chr", "0 0").split(" "))
				if x and y:
					self.SetPosition(x, y)
			ui.ScriptWindow.Show(self)

	def __SetSkillSlotEvent(self):
		for skillPageValue in self.skillPageDict.itervalues():
			skillPageValue.SetSlotStyle(wndMgr.SLOT_STYLE_NONE)
			skillPageValue.SetSelectItemSlotEvent(ui.__mem_func__(self.SelectSkill))
			skillPageValue.SetSelectEmptySlotEvent(ui.__mem_func__(self.SelectEmptySlot))
			skillPageValue.SetUnselectItemSlotEvent(ui.__mem_func__(self.ClickSkillSlot))
			skillPageValue.SetUseSlotEvent(ui.__mem_func__(self.ClickSkillSlot))
			skillPageValue.SetOverInItemEvent(ui.__mem_func__(self.OverInItem))
			skillPageValue.SetOverOutItemEvent(ui.__mem_func__(self.OverOutItem))
			skillPageValue.SetPressedSlotButtonEvent(ui.__mem_func__(self.OnPressedSlotButton))
			skillPageValue.AppendSlotButton("d:/ymir work/ui/game/windows/btn_plus_up.sub",\
											"d:/ymir work/ui/game/windows/btn_plus_over.sub",\
											"d:/ymir work/ui/game/windows/btn_plus_down.sub")

	def __SetEmotionSlot(self):

		self.emotionToolTip = uiToolTip.ToolTip()

		if constInfo.ENABLE_NEW_EMOTES:
			for slot in (self.soloEmotionSlot, self.dualEmotionSlot, self.newEmoticonSlot):
				slot.SetSlotStyle(wndMgr.SLOT_STYLE_NONE)
				slot.SetSelectItemSlotEvent(ui.__mem_func__(self.__SelectEmotion))
				slot.SetUnselectItemSlotEvent(ui.__mem_func__(self.__ClickEmotionSlot))
				slot.SetUseSlotEvent(ui.__mem_func__(self.__ClickEmotionSlot))
				slot.SetOverInItemEvent(ui.__mem_func__(self.__OverInEmotion))
				slot.SetOverOutItemEvent(ui.__mem_func__(self.__OverOutEmotion))
				slot.AppendSlotButton("d:/ymir work/ui/game/windows/btn_plus_up.sub",\
												"d:/ymir work/ui/game/windows/btn_plus_over.sub",\
												"d:/ymir work/ui/game/windows/btn_plus_down.sub")
		else:
			for slot in (self.soloEmotionSlot, self.dualEmotionSlot):
				slot.SetSlotStyle(wndMgr.SLOT_STYLE_NONE)
				slot.SetSelectItemSlotEvent(ui.__mem_func__(self.__SelectEmotion))
				slot.SetUnselectItemSlotEvent(ui.__mem_func__(self.__ClickEmotionSlot))
				slot.SetUseSlotEvent(ui.__mem_func__(self.__ClickEmotionSlot))
				slot.SetOverInItemEvent(ui.__mem_func__(self.__OverInEmotion))
				slot.SetOverOutItemEvent(ui.__mem_func__(self.__OverOutEmotion))
				slot.AppendSlotButton("d:/ymir work/ui/game/windows/btn_plus_up.sub",\
												"d:/ymir work/ui/game/windows/btn_plus_over.sub",\
												"d:/ymir work/ui/game/windows/btn_plus_down.sub")

		for slotIdx, datadict in emotion.EMOTION_DICT.items():
			emotionIdx = slotIdx

			slot = self.soloEmotionSlot
			if constInfo.ENABLE_NEW_EMOTES:
				if slotIdx > 50 and slotIdx < 57:
					slot = self.dualEmotionSlot
				if slotIdx >= 57:
					slot = self.newEmoticonSlot
			else:
				if slotIdx > 50:
					slot = self.dualEmotionSlot

			slot.SetEmotionSlot(slotIdx, emotionIdx)
			slot.SetCoverButton(slotIdx)

	def __SelectEmotion(self, slotIndex):
		if not slotIndex in emotion.EMOTION_DICT:
			return

		if app.IsPressed(app.DIK_LCONTROL):
			player.RequestAddToEmptyLocalQuickSlot(player.SLOT_TYPE_EMOTION, slotIndex)
			return

		mouseModule.mouseController.AttachObject(self, player.SLOT_TYPE_EMOTION, slotIndex, slotIndex)

	def __ClickEmotionSlot(self, slotIndex):
		if not slotIndex in emotion.EMOTION_DICT or player.IsActingEmotion():
			return

		command = emotion.EMOTION_DICT[slotIndex]["command"]
		if constInfo.ENABLE_NEW_EMOTES:
			if slotIndex > 50 and slotIndex < 57:
				vid = player.GetTargetVID()

				if 0 == vid or vid == player.GetMainCharacterIndex() or chr.IsNPC(vid) or chr.IsEnemy(vid):
					import chat
					chat.AppendChat(chat.CHAT_TYPE_INFO, localeInfo.EMOTION_CHOOSE_ONE)
					return

				command += " \"" + chr.GetNameByVID(vid) + "\""
		elif slotIndex > 50:
			vid = player.GetTargetVID()

			if 0 == vid or vid == player.GetMainCharacterIndex() or chr.IsNPC(vid) or chr.IsEnemy(vid):
				import chat
				chat.AppendChat(chat.CHAT_TYPE_INFO, localeInfo.EMOTION_CHOOSE_ONE)
				return

			command += " \"" + chr.GetNameByVID(vid) + "\""

		net.SendChatPacket(command)

	def ActEmotion(self, emotionIndex):
		self.__ClickEmotionSlot(emotionIndex)

	def __OverInEmotion(self, slotIndex):
		if self.emotionToolTip:

			if not slotIndex in emotion.EMOTION_DICT:
				return

			self.emotionToolTip.ClearToolTip()
			self.emotionToolTip.SetTitle(emotion.EMOTION_DICT[slotIndex]["name"])
			self.emotionToolTip.AlignHorizonalCenter()
			self.emotionToolTip.ShowToolTip()

	def __OverOutEmotion(self):
		if self.emotionToolTip:
			self.emotionToolTip.HideToolTip()

	def OpenSpecialSkill(self):
		if self.wndPassive:
			if self.wndPassive.IsShow():
				self.wndPassive.Close()
			else:
				self.wndPassive.Show()
				self.wndPassive.SetTop()

	def __BindEvent(self):
		for i in xrange(len(self.skillGroupButton)):
			self.skillGroupButton[i].SetEvent(lambda arg=i: self.__SelectSkillGroup(arg))

		self.specialSkillButton.SetEvent(self.OpenSpecialSkill)

		self.RefreshQuest(True)
		self.__HideJobToolTip()

		for (tabKey, tabButton) in self.tabButtonDict.items():
			tabButton.SetEvent(ui.__mem_func__(self.__OnClickTabButton), tabKey)

		for (statusPlusKey, statusPlusButton) in self.statusPlusButtonDict.items():
			statusPlusButton.SAFE_SetEvent(self.__OnClickStatusPlusButton, statusPlusKey)
			statusPlusButton.ShowToolTip = lambda arg=statusPlusKey: self.__OverInStatButton(arg)
			statusPlusButton.HideToolTip = lambda arg=statusPlusKey: self.__OverOutStatButton()

		for (statusMinusKey, statusMinusButton) in self.statusMinusButtonDict.items():
			statusMinusButton.SAFE_SetEvent(self.__OnClickStatusMinusButton, statusMinusKey)
			statusMinusButton.ShowToolTip = lambda arg=statusMinusKey: self.__OverInStatMinusButton(arg)
			statusMinusButton.HideToolTip = lambda arg=statusMinusKey: self.__OverOutStatMinusButton()

		for titleBarValue in self.titleBarDict.itervalues():
			titleBarValue.SetCloseEvent(ui.__mem_func__(self.Close))

	def __LoadWindow(self):
		if self.isLoaded == 1:
			return

		self.isLoaded = 1

		try:
			self.__LoadScript("UIScript/CharacterWindow.py")
			self.__BindObject()
			self.__BindEvent()
		except:
			import exception
			exception.Abort("CharacterWindow.__LoadWindow")

		#self.tabButtonDict["EMOTICON"].Disable()
		self.SetState("STATUS")

	def Destroy(self):
		self.Close()

		self.ClearDictionary()

		if constInfo.LEADERSHIP_EXTENSION:
			if self.leadershipWnd:
				self.leadershipWnd.Destroy()

		self.__Initialize()

	def Close(self):
		if 0 != self.toolTipSkill:
			self.toolTipSkill.Hide()

		if constInfo.BONI_BOARD:
			
			if self.uiStatsBoard:
				self.uiStatsBoard.Close()

			if self.ExpandBtn and self.MinimizeBtn:
				self.ExpandBtn.Show()
				self.MinimizeBtn.Hide()
				
		self.Hide()

		if constInfo.LEADERSHIP_EXTENSION:
			if self.leadershipWnd:
				self.leadershipWnd.Hide()

	def SetSkillToolTip(self, toolTipSkill):
		self.toolTipSkill = toolTipSkill
		if self.wndPassive:
			self.wndPassive.SetToolTip(toolTipSkill)

	def __OnClickStatusPlusButton(self, statusKey):
		try:
			statusPlusCommand=self.statusPlusCommandDict[statusKey]
			if player.GetStatus(player.STAT) and (app.IsPressed(app.DIK_LCONTROL) or app.IsPressed(app.DIK_RCONTROL)):
				net.SendChatPacket("%s 10" % statusPlusCommand)
			else:
				net.SendChatPacket(statusPlusCommand)
		except KeyError, msg:
			dbg.TraceError("CharacterWindow.__OnClickStatusPlusButton KeyError: %s", msg)

	def __OnClickStatusMinusButton(self, statusKey):
		try:
			statusMinusCommand=self.statusMinusCommandDict[statusKey]
			net.SendChatPacket(statusMinusCommand)
		except KeyError, msg:
			dbg.TraceError("CharacterWindow.__OnClickStatusMinusButton KeyError: %s", msg)


	def __OnClickTabButton(self, stateKey):
		self.SetState(stateKey)

	def SetState(self, stateKey):
		
		self.state = stateKey

		for (tabKey, tabButton) in self.tabButtonDict.items():
			if stateKey!=tabKey:
				tabButton.SetUp()

		for tabValue in self.tabDict.itervalues():
			tabValue.Hide()

		for pageValue in self.pageDict.itervalues():
			pageValue.Hide()

		for titleBarValue in self.titleBarDict.itervalues():
			titleBarValue.Hide()

		self.titleBarDict[stateKey].Show()
		self.tabDict[stateKey].Show()
		self.pageDict[stateKey].Show()

		if constInfo.CHANGE_SKILL_COLOR:
			self.__RefreshGUIButtons()

	def GetState(self):
		return self.state

	def __GetTotalAtkText(self):
		minAtk=player.GetStatus(player.ATT_MIN)
		maxAtk=player.GetStatus(player.ATT_MAX)
		atkBonus=player.GetStatus(player.ATT_BONUS)
		attackerBonus=player.GetStatus(player.ATTACKER_BONUS)

		if minAtk==maxAtk:
			return "%d" % (minAtk+atkBonus+attackerBonus)
		else:
			return "%d-%d" % (minAtk+atkBonus+attackerBonus, maxAtk+atkBonus+attackerBonus)

	def __GetTotalMagAtkText(self):
		minMagAtk=player.GetStatus(player.MAG_ATT)+player.GetStatus(player.MIN_MAGIC_WEP)
		maxMagAtk=player.GetStatus(player.MAG_ATT)+player.GetStatus(player.MAX_MAGIC_WEP)

		if minMagAtk==maxMagAtk:
			return "%d" % (minMagAtk)
		else:
			return "%d-%d" % (minMagAtk, maxMagAtk)

	def __GetTotalDefText(self):
		defValue=player.GetStatus(player.DEF_GRADE)
		if constInfo.ADD_DEF_BONUS_ENABLE:
			defValue+=player.GetStatus(player.DEF_BONUS)
		return "%d" % (defValue)

	def RefreshStatus(self):
		if self.isLoaded==0:
			return

		try:
			self.GetChild("Level_Value").SetText(str(player.GetStatus(player.LEVEL)))
			self.GetChild("Exp_Value").SetText(str(player.GetEXP()))
			self.GetChild("RestExp_Value").SetText(str(player.GetStatus(player.NEXT_EXP) - player.GetStatus(player.EXP)))
			self.GetChild("HP_Value").SetText(str(player.GetStatus(player.HP)) + '/' + str(player.GetStatus(player.MAX_HP)))
			self.GetChild("SP_Value").SetText(str(player.GetStatus(player.SP)) + '/' + str(player.GetStatus(player.MAX_SP)))

			self.GetChild("STR_Value").SetText(str(player.GetStatus(player.ST)))
			self.GetChild("DEX_Value").SetText(str(player.GetStatus(player.DX)))
			self.GetChild("HTH_Value").SetText(str(player.GetStatus(player.HT)))
			self.GetChild("INT_Value").SetText(str(player.GetStatus(player.IQ)))

			self.GetChild("ATT_Value").SetText(self.__GetTotalAtkText())
			self.GetChild("DEF_Value").SetText(self.__GetTotalDefText())

			self.GetChild("MATT_Value").SetText(self.__GetTotalMagAtkText())
			#self.GetChild("MATT_Value").SetText(str(player.GetStatus(player.MAG_ATT)))

			self.GetChild("MDEF_Value").SetText(str(player.GetStatus(player.MAG_DEF)))
			self.GetChild("ASPD_Value").SetText(str(player.GetStatus(player.ATT_SPEED)))
			self.GetChild("MSPD_Value").SetText(str(player.GetStatus(player.MOVING_SPEED)))
			self.GetChild("CSPD_Value").SetText(str(player.GetStatus(player.CASTING_SPEED)))
			self.GetChild("ER_Value").SetText(str(player.GetStatus(player.EVADE_RATE)))

		except:
			pass

		self.__RefreshStatusPlusButtonList()
		self.__RefreshStatusMinusButtonList()
		self.RefreshAlignment()

		if self.refreshToolTip:
			self.refreshToolTip()

		if self.uiStatsBoard:
			self.uiStatsBoard.Refresh()

		if constInfo.CHANGE_SKILL_COLOR:
			self.__RefreshGUIButtons()

	def __RefreshStatusPlusButtonList(self):
		if self.isLoaded==0:
			return

		statusPlusPoint=player.GetStatus(player.STAT)

		if statusPlusPoint>0:
			self.statusPlusValue.SetText(str(statusPlusPoint))
			self.statusPlusLabel.Show()
			self.ShowStatusPlusButtonList()

			if player.GetRealStatus(player.ST) >= 90:
				# tchat("player.GetStatus(player.ST) = %d" % player.GetStatus(player.ST))
				self.statusPlusButtonDict["STR"].Hide()

			if player.GetRealStatus(player.DX) >= 90:
				# tchat("player.GetStatus(player.DX) = %d" % player.GetStatus(player.DX))
				self.statusPlusButtonDict["DEX"].Hide()

			if player.GetRealStatus(player.HT) >= 90:
				# tchat("player.GetStatus(player.HT) = %d" % player.GetStatus(player.HT))
				self.statusPlusButtonDict["HTH"].Hide()

			if player.GetRealStatus(player.IQ) >= 90:
				# tchat("player.GetStatus(player.IQ) = %d" % player.GetStatus(player.IQ))
				self.statusPlusButtonDict["INT"].Hide()

		else:
			self.statusPlusValue.SetText(str(0))
			self.statusPlusLabel.Hide()
			self.HideStatusPlusButtonList()

	def __RefreshStatusMinusButtonList(self):
		if self.isLoaded==0:
			return

		statusMinusPoint=self.__GetStatMinusPoint()

		if statusMinusPoint>0:
			self.__ShowStatusMinusButtonList()
		else:
			self.__HideStatusMinusButtonList()

	def RefreshAlignment(self):
		point, grade = player.GetAlignmentData()

		import colorInfo
		COLOR_DICT = {	0 : colorInfo.TITLE_RGB_GOOD_4,
						1 : colorInfo.TITLE_RGB_GOOD_3,
						2 : colorInfo.TITLE_RGB_GOOD_2,
						3 : colorInfo.TITLE_RGB_GOOD_1,
						4 : colorInfo.TITLE_RGB_NORMAL,
						5 : colorInfo.TITLE_RGB_EVIL_1,
						6 : colorInfo.TITLE_RGB_EVIL_2,
						7 : colorInfo.TITLE_RGB_EVIL_3,
						8 : colorInfo.TITLE_RGB_EVIL_4, }
		colorList = COLOR_DICT.get(grade, colorInfo.TITLE_RGB_NORMAL)
		gradeColor = ui.GenerateColor(colorList[0], colorList[1], colorList[2])

		self.toolTipAlignment.ClearToolTip()
		self.toolTipAlignment.AutoAppendTextLine(localeInfo.TITLE_NAME_LIST[grade], gradeColor)
		self.toolTipAlignment.AutoAppendTextLine(localeInfo.ALIGNMENT_NAME + str(point))
		self.toolTipAlignment.AlignHorizonalCenter()

	def __ShowStatusMinusButtonList(self):
		for (stateMinusKey, statusMinusButton) in self.statusMinusButtonDict.items():
			statusMinusButton.Show()

	def __HideStatusMinusButtonList(self):
		for (stateMinusKey, statusMinusButton) in self.statusMinusButtonDict.items():
			statusMinusButton.Hide()

	def ShowStatusPlusButtonList(self):
		for (statePlusKey, statusPlusButton) in self.statusPlusButtonDict.items():
			statusPlusButton.Show()

	def HideStatusPlusButtonList(self):
		for (statePlusKey, statusPlusButton) in self.statusPlusButtonDict.items():
			statusPlusButton.Hide()

	def SelectSkill(self, skillSlotIndex):

		mouseController = mouseModule.mouseController

		if False == mouseController.isAttached():

			srcSlotIndex = self.__RealSkillSlotToSourceSlot(skillSlotIndex)
			selectedSkillIndex = player.GetSkillIndex(srcSlotIndex)

			if constInfo.LEADERSHIP_EXTENSION:
				if selectedSkillIndex == 121 and player.GetSkillGrade(skillSlotIndex) == 4:
					if not self.leadershipWnd:
						self.leadershipWnd = LeadershipWindow()

					x, y = self.GetGlobalPosition()
					self.leadershipWnd.SetPosition(x, y + 365)
					self.leadershipWnd.Show()
					return

			if skill.CanUseSkill(selectedSkillIndex):

				if app.IsPressed(app.DIK_LCONTROL):

					player.RequestAddToEmptyLocalQuickSlot(player.SLOT_TYPE_SKILL, srcSlotIndex)
					return

				mouseController.AttachObject(self, player.SLOT_TYPE_SKILL, srcSlotIndex, selectedSkillIndex)

		else:

			mouseController.DeattachObject()

	def SelectEmptySlot(self, SlotIndex):
		mouseModule.mouseController.DeattachObject()

	## ToolTip
	def OverInItem(self, slotNumber):

		if mouseModule.mouseController.isAttached():
			return

		if 0 == self.toolTipSkill:
			return

		srcSlotIndex = self.__RealSkillSlotToSourceSlot(slotNumber)
		skillIndex = player.GetSkillIndex(srcSlotIndex)
		skillLevel = player.GetSkillLevel(srcSlotIndex)
		skillGrade = player.GetSkillGrade(srcSlotIndex)
		skillType = skill.GetSkillType(skillIndex)

		## ACTIVE
		if skill.SKILL_TYPE_ACTIVE == skillType:
			overInSkillGrade = self.__GetSkillGradeFromSlot(slotNumber)

			if overInSkillGrade == self.SKILL_GRADE_SLOT_COUNT-1 and skillGrade >= self.SKILL_GRADE_SLOT_COUNT:
				self.toolTipSkill.SetSkillNew(srcSlotIndex, skillIndex, skillGrade, skillLevel)
			elif overInSkillGrade == skillGrade:
				self.toolTipSkill.SetSkillNew(srcSlotIndex, skillIndex, overInSkillGrade, skillLevel)
			else:
				self.toolTipSkill.SetSkillOnlyName(srcSlotIndex, skillIndex, overInSkillGrade)

		else:
			self.toolTipSkill.SetSkillNew(srcSlotIndex, skillIndex, skillGrade, skillLevel)

	def OverOutItem(self):
		if 0 != self.toolTipSkill:
			self.toolTipSkill.HideToolTip()

	## Quest
	def __SelectQuest(self, questIndex):
		questIndex = quest.GetQuestIndex(questIndex)

		import event
		event.QuestButtonClick(-2147483648 + questIndex)
		# Hotfix to advoid stacking invisible Window
		self.Hide()

	def DrawQuests(self):
		lastHeight = 0
		curHeight = 0
		currentMaxHeight = 0
		maxHeight = self.pageDict['QUEST'].GetHeight() - self.QUEST_CATEGORY_HEIGHT * len(self.questCategories)
		base = self.currentQuestBase
		for categoryIndex in xrange(len(self.questCategories)):
			catItem = self.questCategories[categoryIndex]

			catItem.textLine.SetText("%s (%d)" % (constInfo.QUEST_CATEGORIES[categoryIndex], len(catItem.questItems)))
			catItem.SetPosition(0, lastHeight)
			lastHeight += self.QUEST_CATEGORY_HEIGHT

			if categoryIndex == self.currentQuestCategory:
				saveLastHeight = lastHeight

				for item in catItem.questItems:
					item.Hide()

					if base > 0:
						base -= 1
						continue

					if currentMaxHeight > maxHeight:
						continue

					item.SetPosition(item.GetLeft(), lastHeight)
					lastHeight += self.QUEST_ENTRY_BASE_HEIGHT
					curHeight = self.QUEST_ENTRY_EXTRA_HEIGHT_PER_LINE
					currentMaxHeight += self.QUEST_ENTRY_BASE_HEIGHT

					for counterTextLine in item.counterTextLines:
						counterTextLine.SetPosition(item.nameTextLine.GetLeft(), curHeight)
						lastHeight += self.QUEST_ENTRY_EXTRA_HEIGHT_PER_LINE
						curHeight += self.QUEST_ENTRY_EXTRA_HEIGHT_PER_LINE
						currentMaxHeight += self.QUEST_ENTRY_EXTRA_HEIGHT_PER_LINE

					if item.timeTextLine.IsShow():
						item.timeTextLine.SetPosition(item.nameTextLine.GetLeft(), curHeight)
						lastHeight += self.QUEST_ENTRY_EXTRA_HEIGHT_PER_LINE
						curHeight += self.QUEST_ENTRY_EXTRA_HEIGHT_PER_LINE
						currentMaxHeight += self.QUEST_ENTRY_EXTRA_HEIGHT_PER_LINE

					if currentMaxHeight > maxHeight:
						continue

					item.Show()

				if self.currentQuestBase > 0 or currentMaxHeight > maxHeight:
					lastHeight = saveLastHeight + maxHeight
			else:
				for item in catItem.questItems:
					item.Hide()

	def RefreshQuest(self, updateCategories = False):
		if self.isLoaded==0:
			return

		if updateCategories:
			questCount = quest.GetQuestCount()

			for item in self.questCategories:
				item.questItems = []

			# tchat("__RefreshQuest")
			# tchat("questCount %d" % questCount)
			for i in xrange(questCount):
				(questName, questIcon, questCounterSize, catId) = quest.GetQuestData(i)

				# tchat("RefreshQuest : %s (%d)" % (questName, catId))

				item = ui.Button()
				item.SetParent(self.pageDict['QUEST'])
				if catId in constInfo.QUEST_CAT_BATTLEPASS:
					item.SetUpVisual('icon/battlepass_scroll_close.tga')
					item.SetOverVisual('icon/battlepass_scroll_open.tga')
					item.SetDownVisual('icon/battlepass_scroll_open.tga')
					item.SetPosition(7, 0)
					xspace = 3
				else:
					item.SetUpVisual('d:/ymir work/ui/game/quest/Quest_Item_Up.tga')
					item.SetOverVisual('d:/ymir work/ui/game/quest/Quest_Item_Down.tga')
					item.SetDownVisual('d:/ymir work/ui/game/quest/Quest_Item_Down.tga')
					xspace = 0
				item.SAFE_SetEvent(self.__SelectQuest, i)
				item.questIndex = i
				item.Hide()

				nameTextLine = ui.TextLine()
				nameTextLine.SetParent(item)
				nameTextLine.SetFontName(constInfo.GetChoosenFontName())
				nameTextLine.SetPosition(45-10+item.GetLeft()+xspace, 1)
				nameTextLine.AddFlag("not_pick")
				nameTextLine.SetText(questName)
				if (catId in constInfo.QUEST_CAT_BATTLEPASS) and questName[0] == '(': # legendary quest
					nameTextLine.SetPackedFontColor(ui.GOLD_COLOR)
				nameTextLine.Show()
				item.nameTextLine = nameTextLine

				item.counterTextLines = []

				timeTextLine = ui.TextLine()
				timeTextLine.SetFontName(constInfo.GetChoosenFontName())
				timeTextLine.SetParent(item)
				timeTextLine.AddFlag("not_pick")
				timeTextLine.Hide()
				item.timeTextLine = timeTextLine

				self.questCategories[catId].questItems.append(item)
				# tchat("AddQuestItem cat %d name %s" % (catId, questName))

		self.__UpdateQuestCounter()
		self.__UpdateQuestClock(True)
		self.__RefreshQuestMaxBase()

		self.DrawQuests()

	def __OnScrollQuest(self):
		if self.currentQuestMaxBase == 0:
			return

		curBase = int(self.currentQuestMaxBase * self.pageDict['QUEST'].scrollBar.GetPos())
		if curBase != self.currentQuestBase:
			self.currentQuestBase = curBase
			self.DrawQuests()

	def __ClickQuestCat(self, index):
		self.currentQuestCategory = index

		for i in xrange(len(self.questCategories)):
			self.questCategories[i].SetUp()
		self.questCategories[index].SetDown()

		self.RefreshQuest()

	def __RefreshQuestMaxBase(self):
		self.currentQuestMaxBase = 0
		self.currentQuestBase = 0

		scrollBar = self.pageDict['QUEST'].scrollBar
		scrollBar.SetPos(0)
		scrollBar.Hide()

		maxHeight = self.pageDict['QUEST'].GetHeight() - self.QUEST_CATEGORY_HEIGHT * len(self.questCategories)
		curHeight = 0

		questItems = self.questCategories[self.currentQuestCategory].questItems
		for i in xrange(len(questItems) - 1, 0 - 1, -1):
			newHeight = curHeight
			newHeight += self.QUEST_ENTRY_BASE_HEIGHT
			newHeight += self.QUEST_ENTRY_EXTRA_HEIGHT_PER_LINE * len(questItems[i].counterTextLines)
			if questItems[i].timeTextLine.IsShow():
				newHeight += self.QUEST_ENTRY_EXTRA_HEIGHT_PER_LINE
			if newHeight > maxHeight:
				scrollBar.SetPosition(scrollBar.GetLeft(), self.QUEST_CATEGORY_HEIGHT * (self.currentQuestCategory + 1))
				scrollBar.SetScrollBarSize(maxHeight)
				scrollBar.SetMiddleBarSize(1.0 - ((i + 1) / float(len(questItems))))
				scrollBar.SetTop()
				scrollBar.Show()

				self.currentQuestMaxBase = i + 1
				return
			curHeight = newHeight

	def __UpdateQuestCounter(self):
		itemList = self.questCategories[self.currentQuestCategory].questItems

		for i in xrange(len(itemList)):
			(questName, questIcon, questCounterSize, catId) = quest.GetQuestData(itemList[i].questIndex)

			lines = itemList[i].counterTextLines
			del lines[:]

			for j in xrange(questCounterSize):
				name, value = quest.GetQuestCounterData(itemList[i].questIndex, j)
				counterTextLine = ui.TextLine()
				counterTextLine.SetParent(itemList[i])
				counterTextLine.AddFlag("not_pick")
				counterTextLine.SetText("%s : %d" % (name, value))
				counterTextLine.Show()

				lines.append(counterTextLine)

	def __UpdateQuestClock(self, force=False):
		if "QUEST" == self.state or force:
			itemList = self.questCategories[self.currentQuestCategory].questItems

			for i in xrange(len(itemList)):
				(lastName, lastTime) = quest.GetQuestLastTime(itemList[i].questIndex)

				clockText = ""
				if len(lastName) > 0:
					if lastTime <= 0:
						clockText = localeInfo.QUEST_TIMEOVER
					else:
						clockText = lastName + " : " + localeInfo.SecondToDHMS(lastTime)
#						questLastMinute = lastTime / 60
#						questLastSecond = lastTime % 60
#
#						clockText = lastName + " : "
#
#						if questLastMinute > 0:
#							clockText += str(questLastMinute) + localeInfo.QUEST_MIN
#							if questLastSecond > 0:
#								clockText += " "
#
#						if questLastSecond > 0:
#							clockText += str(questLastSecond) + localeInfo.QUEST_SEC

				if clockText:
					itemList[i].timeTextLine.SetText(clockText)
					itemList[i].timeTextLine.Show()
				else:
					itemList[i].timeTextLine.Hide()

	def OnMouseWheel(self, length):
		if "QUEST" != self.state:
			return False
		
		categories = self.questCategories
		current = self.currentQuestCategory
		scrollBar = self.pageDict['QUEST'].scrollBar
		
		lineCount = len(categories[current].questItems) - 1

		if self.IsInPosition() and scrollBar.IsShow() and lineCount > 0:
			dir = constInfo.WHEEL_TO_SCROLL(length)
			new_pos = scrollBar.GetPos() + ((1.0 / lineCount) * dir)
			new_pos = max(0.0, new_pos)
			new_pos = min(1.0, new_pos)
			scrollBar.SetPos(new_pos)
			return True
		return False

	def __UpdateQuestBattlepass(self):
		catIdxList = constInfo.QUEST_CAT_BATTLEPASS

		for catIdx in catIdxList:
			catItem = self.questCategories[catIdx]
			timeLeft = self.interfaceHandle.GetBattlepassTimeLeft(catIdx)
			if timeLeft <= 0 or (catIdx != constInfo.QUEST_CAT_BATTLEPASS_MAIN and len(catItem.questItems) == 0):
				catItem.textLine.SetText("%s (%d)" % (constInfo.QUEST_CATEGORIES[catIdx], len(catItem.questItems)))
			else:
				catItem.textLine.SetText("%s (%d) [%s]" % (constInfo.QUEST_CATEGORIES[catIdx], len(catItem.questItems), localeInfo.SecondToDHMS(timeLeft)))

	def __GetStatMinusPoint(self):
		POINT_STAT_RESET_COUNT = 112
		return player.GetStatus(POINT_STAT_RESET_COUNT)

	def __OverInStatMinusButton(self, stat):
		try:
			self.__ShowStatToolTip(self.STAT_MINUS_DESCRIPTION[stat] % self.__GetStatMinusPoint())
		except KeyError:
			pass

		self.refreshToolTip = lambda arg=stat: self.__OverInStatMinusButton(arg) 

	def __OverOutStatMinusButton(self):
		self.__HideStatToolTip()
		self.refreshToolTip = 0

	def __OverInStatButton(self, stat):	
		try:
			self.__ShowStatToolTip(self.STAT_DESCRIPTION[stat])
		except KeyError:
			pass

	def __OverOutStatButton(self):
		self.__HideStatToolTip()

	def __ShowStatToolTip(self, statDesc):
		self.toolTip.ClearToolTip()
		self.toolTip.AppendTextLine(statDesc)
		self.toolTip.Show()

	def __HideStatToolTip(self):
		self.toolTip.Hide()

	def OnPressEscapeKey(self):
		self.Close()
		return True

	def OnUpdate(self):
		self.__UpdateQuestClock()
		self.__UpdateQuestBattlepass()

	## Skill Process
	def __RefreshSkillPage(self, name, slotCount):
		global SHOW_LIMIT_SUPPORT_SKILL_LIST

		skillPage = self.skillPageDict[name]

		startSlotIndex = skillPage.GetStartIndex()
		if "ACTIVE" == name:
			if self.PAGE_HORSE == self.curSelectedSkillGroup:
				startSlotIndex += slotCount

		getSkillType=skill.GetSkillType
		getSkillIndex=player.GetSkillIndex
		getSkillGrade=player.GetSkillGrade
		getSkillLevel=player.GetSkillLevel
		getSkillLevelUpPoint=skill.GetSkillLevelUpPoint
		getSkillMaxLevel=skill.GetSkillMaxLevel
		for i in xrange(slotCount+1):

			slotIndex = i + startSlotIndex
			skillIndex = getSkillIndex(slotIndex)

			for j in xrange(self.SKILL_GRADE_SLOT_COUNT):
				skillPage.ClearSlot(self.__GetRealSkillSlot(j, i))

			if 0 == skillIndex:
				continue

			skillGrade = getSkillGrade(slotIndex)
			skillLevel = getSkillLevel(slotIndex)
			skillType = getSkillType(skillIndex)

			## �¸� ��ų ���� ó��
			if player.SKILL_INDEX_RIDING == skillIndex:
				skillPage.SetSkillSlotNew(slotIndex, skillIndex, max(skillLevel-1, 0), skillLevel)
				skillPage.SetSlotCount(slotIndex, skillLevel)

			## ACTIVE
			elif skill.SKILL_TYPE_ACTIVE == skillType:
				for j in xrange(self.SKILL_GRADE_SLOT_COUNT):
					realSlotIndex = self.__GetRealSkillSlot(j, slotIndex)

					if (skillGrade >= self.SKILL_GRADE_SLOT_COUNT) and j == (self.SKILL_GRADE_SLOT_COUNT-1):
						skillPage.SetSkillSlotNew(realSlotIndex, skillIndex, skillGrade, skillLevel)
						skillPage.SetCoverButton(realSlotIndex)
						skillPage.SetSlotCountNew(realSlotIndex, skillGrade, skillLevel)
					else:
						skillPage.SetSkillSlotNew(realSlotIndex, skillIndex, j, skillLevel)
						skillPage.SetCoverButton(realSlotIndex)
						if (not self.__CanUseSkillNow()) or (skillGrade != j):
							skillPage.SetSlotCount(realSlotIndex, 0)
							skillPage.DisableCoverButton(realSlotIndex)
						else:
							skillPage.SetSlotCountNew(realSlotIndex, skillGrade, skillLevel)

			## �׿�
			else:
				if not SHOW_LIMIT_SUPPORT_SKILL_LIST or skillIndex in SHOW_LIMIT_SUPPORT_SKILL_LIST:
					realSlotIndex = self.__GetETCSkillRealSlotIndex(slotIndex)
					skillPage.SetSkillSlot(realSlotIndex, skillIndex, skillLevel)
					skillPage.SetSlotCountNew(realSlotIndex, skillGrade, skillLevel)

					if skill.CanUseSkill(skillIndex):
						skillPage.SetCoverButton(realSlotIndex)

			skillPage.RefreshSlot()


	def RefreshSkill(self):

		if self.isLoaded==0:
			return

		if self.__IsChangedHorseRidingSkillLevel():
			self.RefreshCharacter()
			return


		global SHOW_ONLY_ACTIVE_SKILL
		if SHOW_ONLY_ACTIVE_SKILL:
			self.__RefreshSkillPage("ACTIVE", self.ACTIVE_PAGE_SLOT_COUNT)
		else:
			self.__RefreshSkillPage("ACTIVE", self.ACTIVE_PAGE_SLOT_COUNT)
			self.__RefreshSkillPage("SUPPORT", self.SUPPORT_PAGE_SLOT_COUNT)

		if self.wndPassive:
			self.wndPassive.RefleshSkill()

		self.RefreshSkillPlusButtonList()

	def CanShowPlusButton(self, skillIndex, skillLevel, curStatPoint):

		## ��ų�� ������
		if 0 == skillIndex:
			return False

		## ������ ������ �����Ѵٸ�
		if not skill.CanLevelUpSkill(skillIndex, skillLevel):
			return False

		return True

	def __RefreshSkillPlusButton(self, name):
		global HIDE_SUPPORT_SKILL_POINT
		if HIDE_SUPPORT_SKILL_POINT and "SUPPORT" == name:
			return

		slotWindow = self.skillPageDict[name]
		slotWindow.HideAllSlotButton()

		slotStatType = self.skillPageStatDict[name]
		if 0 == slotStatType:
			return

		statPoint = player.GetStatus(slotStatType)
		startSlotIndex = slotWindow.GetStartIndex()
		if "HORSE" == name:
			startSlotIndex += self.ACTIVE_PAGE_SLOT_COUNT

		if statPoint > 0:
			for i in xrange(self.PAGE_SLOT_COUNT):
				slotIndex = i + startSlotIndex
				skillIndex = player.GetSkillIndex(slotIndex)
				skillGrade = player.GetSkillGrade(slotIndex)
				skillLevel = player.GetSkillLevel(slotIndex)

				if skillIndex == 0:
					continue
				if skillGrade != 0:
					continue

				if name == "HORSE":
					if player.GetStatus(player.LEVEL) >= skill.GetSkillLevelLimit(skillIndex):
						if skillLevel < 20:
							slotWindow.ShowSlotButton(self.__GetETCSkillRealSlotIndex(slotIndex))

				else:
					if "SUPPORT" == name:						
						if not SHOW_LIMIT_SUPPORT_SKILL_LIST or skillIndex in SHOW_LIMIT_SUPPORT_SKILL_LIST:
							if self.CanShowPlusButton(skillIndex, skillLevel, statPoint):
								slotWindow.ShowSlotButton(slotIndex)
					else:
						if self.CanShowPlusButton(skillIndex, skillLevel, statPoint):
							slotWindow.ShowSlotButton(slotIndex)
					

	def RefreshSkillPlusButtonList(self):

		if self.isLoaded==0:
			return

		self.RefreshSkillPlusPointLabel()

		if not self.__CanUseSkillNow():
			return

		try:
			if self.PAGE_HORSE == self.curSelectedSkillGroup:
				self.__RefreshSkillPlusButton("HORSE")
			else:
				self.__RefreshSkillPlusButton("ACTIVE")

			self.__RefreshSkillPlusButton("SUPPORT")

		except:
			import exception
			exception.Abort("CharacterWindow.RefreshSkillPlusButtonList.BindObject")

	def RefreshSkillPlusPointLabel(self):
		if self.isLoaded==0:
			return

		if self.PAGE_HORSE == self.curSelectedSkillGroup:
			activeStatPoint = player.GetStatus(player.SKILL_MOUNT)
			self.activeSkillPointValue.SetText(str(activeStatPoint))

		else:
			activeStatPoint = player.GetStatus(player.SKILL_ACTIVE)
			self.activeSkillPointValue.SetText(str(activeStatPoint))

		supportStatPoint = max(0, player.GetStatus(player.SKILL_SUPPORT))
		self.supportSkillPointValue.SetText(str(supportStatPoint))

	## Skill Level Up Button
	def OnPressedSlotButton(self, slotNumber):
		srcSlotIndex = self.__RealSkillSlotToSourceSlot(slotNumber)

		skillIndex = player.GetSkillIndex(srcSlotIndex)
		curLevel = player.GetSkillLevel(srcSlotIndex)
		maxLevel = skill.GetSkillMaxLevel(skillIndex)

		net.SendChatPacket("/skillup " + str(skillIndex))

	## Use Skill
	def ClickSkillSlot(self, slotIndex):

		srcSlotIndex = self.__RealSkillSlotToSourceSlot(slotIndex)
		skillIndex = player.GetSkillIndex(srcSlotIndex)
		skillType = skill.GetSkillType(skillIndex)

		if constInfo.LEADERSHIP_EXTENSION:
			if skillIndex == 121 and player.GetSkillGrade(slotIndex) == 4:
				if not self.leadershipWnd:
					self.leadershipWnd = LeadershipWindow()

				x, y = self.GetGlobalPosition()
				self.leadershipWnd.SetPosition(x, y + 365)
				self.leadershipWnd.Show()
				return
		
		if skillIndex == 122 and player.IsAttacking():
			return

		if not self.__CanUseSkillNow():
			if skill.SKILL_TYPE_ACTIVE == skillType:
				return

		for slotWindow in self.skillPageDict.values():
			if slotWindow.HasSlot(slotIndex):
				if skill.CanUseSkill(skillIndex):
					player.ClickSkillSlot(srcSlotIndex)
					return

		mouseModule.mouseController.DeattachObject()

	## FIXME : ��ų�� ��������� ���� ��ȣ�� ������ �ش� ������ ã�Ƽ� ������Ʈ �Ѵ�.
	##         �ſ� ���ո�. ���� ��ü�� �����ؾ� �ҵ�.
	def OnUseSkill(self, slotIndex, coolTime):

		skillIndex = player.GetSkillIndex(slotIndex)
		skillType = skill.GetSkillType(skillIndex)

		## ACTIVE
		if skill.SKILL_TYPE_ACTIVE == skillType:
			skillGrade = player.GetSkillGrade(slotIndex)
			slotIndex = self.__GetRealSkillSlot(skillGrade, slotIndex)
		## ETC
		else:
			slotIndex = self.__GetETCSkillRealSlotIndex(slotIndex)

		for slotWindow in self.skillPageDict.values():
			if slotWindow.HasSlot(slotIndex):
				slotWindow.SetSlotCoolTime(slotIndex, coolTime)
				return

	def OnActivateSkill(self, slotIndex):

		skillGrade = player.GetSkillGrade(slotIndex)
		slotIndex = self.__GetRealSkillSlot(skillGrade, slotIndex)

		for slotWindow in self.skillPageDict.values():
			if slotWindow.HasSlot(slotIndex):
				slotWindow.ActivateSlot(slotIndex)
				return

	def OnDeactivateSkill(self, slotIndex):

		skillGrade = player.GetSkillGrade(slotIndex)
		slotIndex = self.__GetRealSkillSlot(skillGrade, slotIndex)

		for slotWindow in self.skillPageDict.values():
			if slotWindow.HasSlot(slotIndex):
				slotWindow.DeactivateSlot(slotIndex)
				return

	def __ShowJobToolTip(self):
		self.toolTipJob.ShowToolTip()

	def __HideJobToolTip(self):
		self.toolTipJob.HideToolTip()

	def __SetJobText(self, mainJob, subJob):
		if player.GetStatus(player.LEVEL)<5:
			subJob=0

	def __ShowAlignmentToolTip(self):
		self.toolTipAlignment.ShowToolTip()

	def __HideAlignmentToolTip(self):
		self.toolTipAlignment.HideToolTip()

	def RefreshCharacter(self):

		if self.isLoaded==0:
			return

		## Name
		try:
			characterName = player.GetName()
			guildName = player.GetGuildName()
			self.characterNameValue.SetText(characterName)
			self.guildNameValue.SetText(guildName)
			if not guildName:
				if localeInfo.IsARABIC():
					self.characterNameSlot.SetPosition(190, 34)
				else:
					self.characterNameSlot.SetPosition(109, 34)

				self.guildNameSlot.Hide()
			else:
				if localeInfo.IsJAPAN():
					self.characterNameSlot.SetPosition(143, 34)
				else:
					self.characterNameSlot.SetPosition(153, 34)
				self.guildNameSlot.Show()
		except:
			import exception
			exception.Abort("CharacterWindow.RefreshCharacter.BindObject")

		race = net.GetMainActorRace()
		group = net.GetMainActorSkillGroup()
		empire = net.GetMainActorEmpire()

		## Job Text
		job = chr.RaceToJob(race)
		self.__SetJobText(job, group)

		## FaceImage
		try:
			faceImageName = FACE_IMAGE_DICT[race]

			try:
				self.faceImage.LoadImage(faceImageName)
			except:
				print "CharacterWindow.RefreshCharacter(race=%d, faceImageName=%s)" % (race, faceImageName)
				self.faceImage.Hide()

		except KeyError:
			self.faceImage.Hide()

		## GroupName
		self.__SetSkillGroupName(race, group)

		## Skill
		if 0 == group:
			self.__SelectSkillGroup(0)

		else:
			self.__SetSkillSlotData(race, group, empire)

			if self.__CanUseHorseSkill():
				self.__SelectSkillGroup(0)

		if constInfo.CHANGE_SKILL_COLOR:
			self.__RefreshOpenGUIButton()

	def __SetSkillGroupName(self, race, group):

		job = chr.RaceToJob(race)

		if not self.SKILL_GROUP_NAME_DICT.has_key(job):
			return

		nameList = self.SKILL_GROUP_NAME_DICT[job]

		if 0 == group and job != playerSettingModule.JOB_WOLFMAN:
			self.skillGroupButton1.SetText(nameList[1])
			self.skillGroupButton2.SetText(nameList[2])
			self.skillGroupButton1.Show()
			self.skillGroupButton2.Show()
			self.activeSkillGroupName.Hide()
			self.specialSkillButton.Hide()
			if self.wndPassive:
				self.wndPassive.Close()

		else:
			if __SERVER__ != 2:
				self.specialSkillButton.Show()
			if self.__CanUseHorseSkill():
				self.activeSkillGroupName.Hide()
				self.skillGroupButton1.SetText(nameList.get(group, "Noname"))
				self.skillGroupButton2.SetText(localeInfo.SKILL_GROUP_HORSE)
				self.skillGroupButton1.Show()
				self.skillGroupButton2.Show()

			else:
				self.activeSkillGroupName.SetText(nameList.get(group, "Noname"))
				self.activeSkillGroupName.Show()
				self.skillGroupButton1.Hide()
				self.skillGroupButton2.Hide()

	def __SetSkillSlotData(self, race, group, empire=0):

		## SkillIndex
		playerSettingModule.RegisterSkill(race, group, empire)

		## Event
		self.__SetSkillSlotEvent()

		## Refresh
		self.RefreshSkill()

	def __SelectSkillGroup(self, index):
		for btn in self.skillGroupButton:
			btn.SetUp()
		self.skillGroupButton[index].Down()

		if self.__CanUseHorseSkill() and net.GetMainActorSkillGroup() != 0:
			if 0 == index:
				index = net.GetMainActorSkillGroup()-1
			elif 1 == index:
				index = self.PAGE_HORSE

		self.curSelectedSkillGroup = index
		self.__SetSkillSlotData(net.GetMainActorRace(), index+1, net.GetMainActorEmpire())

		if constInfo.CHANGE_SKILL_COLOR:
			self.__RefreshGUIButtons()

	def __CanUseSkillNow(self):
		if 0 == net.GetMainActorSkillGroup():
			return False

		return True

	def __CanUseHorseSkill(self):

		slotIndex = player.GetSkillSlotIndex(player.SKILL_INDEX_RIDING)

		if not slotIndex:
			return False

		level = player.GetSkillLevel(slotIndex)
		if level >= 2:
			return True

		return False

	def __IsChangedHorseRidingSkillLevel(self):
		ret = False

		if -1 == self.canUseHorseSkill:
			self.canUseHorseSkill = self.__CanUseHorseSkill()

		if self.canUseHorseSkill != self.__CanUseHorseSkill():
			ret = True

		self.canUseHorseSkill = self.__CanUseHorseSkill()
		return ret

	def __GetRealSkillSlot(self, skillGrade, skillSlot):
		return skillSlot + min(self.SKILL_GRADE_SLOT_COUNT - 1, skillGrade)*skill.SKILL_GRADE_STEP_COUNT

	def __GetETCSkillRealSlotIndex(self, skillSlot):
		if skillSlot > 100:
			return skillSlot
		return skillSlot % self.ACTIVE_PAGE_SLOT_COUNT

	def __RealSkillSlotToSourceSlot(self, realSkillSlot):
		if realSkillSlot > 100:
			return realSkillSlot
		if self.PAGE_HORSE == self.curSelectedSkillGroup:
			return realSkillSlot + self.ACTIVE_PAGE_SLOT_COUNT
		return realSkillSlot % skill.SKILL_GRADE_STEP_COUNT

	def __GetSkillGradeFromSlot(self, skillSlot):
		return int(skillSlot / skill.SKILL_GRADE_STEP_COUNT)

	def SelectSkillGroup(self, index):
		self.__SelectSkillGroup(index)

	if constInfo.CHANGE_SKILL_COLOR:
		def __RefreshOpenGUIButton(self):
			posx, posy = 0, 0
			for i in xrange(6):
				if i == 1 or i == 3 or i == 5:
					posx = 121 + 107
					posy = i * 18 + 45
				else:
					posx = 9 + 107
					posy = i * 18 + 63

				if len(self.open_gui_btn) == i:
					btn = ui.Button()
					btn.SetParent(self)
					btn.SetUpVisual("d:/ymir work/ui/chat/color_icon.tga")
					btn.SetOverVisual("d:/ymir work/ui/chat/color_icon.tga")
					btn.SetDownVisual("d:/ymir work/ui/chat/color_icon.tga")
					btn.SetPosition(posx, posy)
					btn.SetEvent(lambda arg = i: self.__OnPressOpenGUIButton(arg))
					btn.Show()

					self.open_gui_btn.append(btn)

		def __RefreshGUIButtons(self):
			if not len(self.open_gui_btn):
				return

			for x in xrange(6):
				if self.state == "SKILL" and self.curSelectedSkillGroup != 2:
					# if player.GetSkillGrade(x + 1) == 4:
					if self.CUSTOM_SKILL_STATUS[x]:
						self.open_gui_btn[x].Show()
					else:
						self.open_gui_btn[x].Hide()
					# else:
						# self.open_gui_btn[x].Hide()
				else:
					self.open_gui_btn[x].Hide()

		def __OnPressOpenGUIButton(self, arg):
			self.skillColorWnd.Open(arg)

		def SetUnlockedSkill(self, skill):
			self.CUSTOM_SKILL_STATUS[skill] = 1
			self.__RefreshGUIButtons()

	if constInfo.LEADERSHIP_EXTENSION:
		def Hide(self):
			ui.ScriptWindow.Hide(self)

			try: # 'CharacterWindow' object has no attribute 'leadershipWnd', called to soon, ez way to deal with
				if self.leadershipWnd:
					self.leadershipWnd.Hide()
			except:
				pass

if constInfo.LEADERSHIP_EXTENSION:
	class LeadershipWindow(ui.ScriptWindow):
		def __init__(self):
			ui.ScriptWindow.__init__(self)
			self.__LoadWindow()

		def __del__(self):
			ui.ScriptWindow.__del__(self)

		def __LoadWindow(self):
			self.paths = [
				"d:/ymir work/ui/game/windows/party_state_attacker",
				"d:/ymir work/ui/game/windows/party_state_berserker",
				"d:/ymir work/ui/game/windows/party_state_tanker",
				"d:/ymir work/ui/game/windows/party_state_defender",
				"d:/ymir work/ui/game/windows/party_state_buffer",
				"d:/ymir work/ui/game/windows/party_state_skill_master",
			]

			self.buttons = [ None ] * 6

			for x in xrange(6):
				btn = ui.MakeButton(self, 22 * x, 0, "", self.paths[x], "_01.sub", "_02.sub", "_03.sub")
				btn.SAFE_SetEvent(self.__OnSelectState, x)
				self.buttons.append(btn)

			self.SetSize(22 * 6, 36)

		def __OnSelectState(self, x):
			net.SendChatPacket("/leadership_state %d" % x)
			self.Hide()

		def Destroy(self):
			self.buttons = []
