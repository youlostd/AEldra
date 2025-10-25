import ui
import app
import localeInfo
import net
import item
import player
import uiCommon
import constInfo
import chr

UISTATSBOARD_PATH = "d:/ymir work/ui/stats_board/"
UISTATSBOARD_ITEM_HEIGHT = 30

class StatsBoard(ui.ScriptWindow):

	class KillStat(ui.Bar):

		def __init__(self, point, name, image = "kill_normal.tga"):
			ui.Bar.__init__(self)

			self.clickEvent = None
			self.clickArgs = None

			self.name = name
			self.point = point
			self.image = image

			self.BuildWindow()

		def __del__(self):
			ui.Bar.__del__(self)

		def BuildWindow(self):
			self.SetSize(239, UISTATSBOARD_ITEM_HEIGHT)
			self.SetPosition(0, 0)

			self.killStatNameImg = ui.ImageBox()
			self.killStatNameImg.SetParent(self)
			self.killStatNameImg.SetPosition(0, 0)
			self.killStatNameImg.LoadImage(UISTATSBOARD_PATH + self.image)

			self.killStatName = ui.TextLine()
			self.killStatName.SetParent(self.killStatNameImg)
			self.killStatName.SetPosition(116 / 2, 4)
			self.killStatName.SetHorizontalAlignCenter()
			self.killStatName.SetLimitWidth(116)

			self.killStatValueImg = ui.ImageBox()
			self.killStatValueImg.SetParent(self)
			self.killStatValueImg.SetPosition(126, 0)
			self.killStatValueImg.LoadImage(UISTATSBOARD_PATH + "kill_numberfield.tga")

			self.killStatValue = ui.TextLine()
			self.killStatValue.SetParent(self.killStatValueImg)
			self.killStatValue.SetPosition(83 / 2, 4)
			self.killStatValue.SetHorizontalAlignCenter()
			self.killStatValue.SetLimitWidth(83)

			self.SetName(self.name)
			self.SetValue("0")

			# show elements
			self.killStatNameImg.Show()
			self.killStatName.Show()
			self.killStatValueImg.Show()
			self.killStatValue.Show()

		def SetName(self, name):
			self.killStatName.SetText(name)

		def SetValue(self, value):
			self.killStatValue.SetText(value)

		# update value with this callback
		def RefreshCallback(self):
			if self.point == -1:
				self.SetValue(str(player.GetRealStatus(player.POINT_EMPIRE_A_KILLED) + player.GetRealStatus(player.POINT_EMPIRE_B_KILLED) + player.GetRealStatus(player.POINT_EMPIRE_C_KILLED)))
			else:
				self.SetValue(str(player.GetRealStatus(self.point)))

		def Hide(self):
			ui.Bar.Hide(self)

		def Close(self):
			self.Hide()

	class BonusCategory(ui.Bar):

		def __init__(self, name):
			ui.Bar.__init__(self)

			self.clickEvent = None
			self.clickArgs = None
			self.name = name

			self.BuildWindow()

		def __del__(self):
			ui.Bar.__del__(self)

		def BuildWindow(self):
			self.SetSize(218, UISTATSBOARD_ITEM_HEIGHT)
			self.SetPosition(0, 0)

			self.bonusCategoryImg = ui.ImageBox()
			self.bonusCategoryImg.SetParent(self)
			self.bonusCategoryImg.LoadImage(UISTATSBOARD_PATH + "boni_textfield1.tga")

			center = (218 / 2) - (129 / 2) - 10

			self.bonusCategoryImg.SetPosition(center, 0)

			self.bonusCategory = ui.TextLine()
			self.bonusCategory.SetParent(self.bonusCategoryImg)
			self.bonusCategory.SetPosition(129 / 2, 4)
			self.bonusCategory.SetHorizontalAlignCenter()
			self.bonusCategory.SetLimitWidth(218)

			self.SetCategoryName(self.name)

			# show elements
			self.bonusCategoryImg.Show()
			self.bonusCategory.Show()

		def SetCategoryName(self, name):
			self.bonusCategory.SetText(name)

		def RefreshCallback(self):
			pass

		def Hide(self):
			ui.Bar.Hide(self)

		def Close(self):
			self.Hide()

	class BonusInfo(ui.Bar):

		def __init__(self, name, point):
			ui.Bar.__init__(self)

			self.clickEvent = None
			self.clickArgs = None
			self.name = name
			self.point = point

			self.BuildWindow()

		def __del__(self):
			ui.Bar.__del__(self)

		def BuildWindow(self):
			self.SetSize(239, UISTATSBOARD_ITEM_HEIGHT)
			self.SetPosition(0, 0)

			self.bonusNameImg = ui.ImageBox()
			self.bonusNameImg.SetParent(self)
			self.bonusNameImg.SetPosition(0, 0)
			self.bonusNameImg.LoadImage(UISTATSBOARD_PATH + "boni_textfield1.tga")

			self.bonusName = ui.TextLine()
			self.bonusName.SetParent(self.bonusNameImg)
			self.bonusName.SetPosition(129 / 2, 4)
			self.bonusName.SetHorizontalAlignCenter()
			self.bonusName.SetLimitWidth(129)

			self.bonusValueImg = ui.ImageBox()
			self.bonusValueImg.SetParent(self)
			self.bonusValueImg.SetPosition(139, 0)
			self.bonusValueImg.LoadImage(UISTATSBOARD_PATH + "boni_textfield2.tga")

			self.bonusValue = ui.TextLine()
			self.bonusValue.SetParent(self.bonusValueImg)
			self.bonusValue.SetPosition(60 / 2, 4)
			self.bonusValue.SetHorizontalAlignCenter()
			self.bonusValue.SetLimitWidth(60)

			self.SetBonusName(self.name)
			self.SetBonusValue("0")

			# show elements
			self.bonusNameImg.Show()
			self.bonusName.Show()
			self.bonusValueImg.Show()
			self.bonusValue.Show()

		def SetBonusName(self, name):
			self.bonusName.SetText(name)

		def SetBonusValue(self, value):
			self.bonusValue.SetText(value)

		# update value with this callback
		def RefreshCallback(self):
			
				# bonusValue = player.GetStatus(self.point)
				# bonusValue = str(bonusValue)
				pointsVal = item.GetApplyPoint(self.point)
				bonusValue = player.GetStatus(pointsVal) - player.GetRealStatus(pointsVal)
				if self.point == item.APPLY_CAST_SPEED:
					bonusValue -= 100
				if self.point == item.APPLY_RESIST_HUMAN:
					pointsVal = item.GetApplyPoint(item.APPLY_RESIST_ATTBONUS_HUMAN)
					bonusValue += player.GetStatus(pointsVal) - player.GetRealStatus(pointsVal)
				bonusValue = str(bonusValue)

				self.SetBonusValue(bonusValue)

		def Hide(self):
			ui.Bar.Hide(self)

		def Close(self):
			self.Hide()

	WIDTH 	= 239
	HEIGHT 	= 359

	# Internal width: 	223
	# Internal height: 	305

	MARGIN_X = 18
	MARGIN_Y = 44

	# CATEGORIES FOR LIST
	TYPE_CATEGORY 		= 0
	TYPE_BONUS 			= 1
	TYPE_KILL 			= 2
	TYPE_KILL_JINNO 	= 3
	TYPE_KILL_SHINSOO 	= 4
	TYPE_KILL_CHUNJO 	= 5

	TAB_BONUS = [

		# PvM Category
		BonusCategory(localeInfo.CATEGORY_PVM),
		BonusInfo(localeInfo.STRONG_VS_MONSTERS, 	item.APPLY_ATTBONUS_MONSTER),
		BonusInfo(localeInfo.STRONG_VS_METINS, 	item.APPLY_ATTBONUS_METIN),
		BonusInfo(localeInfo.STRONG_VS_BOSSES, 	item.APPLY_ATTBONUS_BOSS),
		BonusInfo(localeInfo.STRONG_VS_UNDEAD, 	item.APPLY_ATTBONUS_UNDEAD),
		BonusInfo(localeInfo.STRONG_VS_DEVILS, 	item.APPLY_ATTBONUS_DEVIL),
		BonusInfo(localeInfo.STRONG_VS_ORCS,  		item.APPLY_ATTBONUS_ORC),
		BonusInfo(localeInfo.STRONG_VS_ANIMALS, 	item.APPLY_ATTBONUS_ANIMAL),
		BonusInfo(localeInfo.STRONG_VS_ZODIAC, 	item.APPLY_ATTBONUS_ZODIAC),

		# PvP Category
		BonusCategory(localeInfo.CATEGORY_PVP),
		BonusInfo(localeInfo.STRONG_VS_HALFHUMANS, 	item.APPLY_ATTBONUS_HUMAN),
		BonusInfo(localeInfo.STRONG_VS_WARRIOR, 		item.APPLY_ATTBONUS_WARRIOR),
		BonusInfo(localeInfo.STRONG_VS_SURA, 			item.APPLY_ATTBONUS_SURA),
		BonusInfo(localeInfo.STRONG_VS_ASSASSIN, 		item.APPLY_ATTBONUS_ASSASSIN),
		BonusInfo(localeInfo.STRONG_VS_SHAMAN, 		item.APPLY_ATTBONUS_SHAMAN),

		BonusInfo(localeInfo.WARRIOR_RESISTANCE, 	item.APPLY_RESIST_WARRIOR),
		BonusInfo(localeInfo.SURA_RESISTANCE, 		item.APPLY_RESIST_SURA),
		BonusInfo(localeInfo.ASSASSIN_RESISTANCE, 	item.APPLY_RESIST_ASSASSIN),
		BonusInfo(localeInfo.SHAMAN_RESISTANCE, 	item.APPLY_RESIST_SHAMAN),

		# General Category
		BonusCategory(localeInfo.CATEGORY_GENERAL),
		BonusInfo(localeInfo.SKILL_DAMAGE_BONUS, 	item.APPLY_SKILL_DAMAGE_BONUS),
		BonusInfo(localeInfo.NORMAL_HIT_DAMAGE_BONUS, 	item.APPLY_NORMAL_HIT_DAMAGE_BONUS),
		BonusInfo(localeInfo.GENERAL_HP_STEAL, 	item.APPLY_STEAL_HP),
		BonusInfo(localeInfo.GENERAL_SP_STEAL, 	item.APPLY_STEAL_SP),
		BonusInfo(localeInfo.GENERAL_MAX_HP, 		item.APPLY_MAX_HP),
		BonusInfo(localeInfo.GENERAL_MAX_SP, 		item.APPLY_MAX_SP),
		BonusInfo(localeInfo.GENERAL_HP_REGEN, 	item.APPLY_HP_REGEN),
		BonusInfo(localeInfo.GENERAL_SP_REGEN, 	item.APPLY_SP_REGEN),
		BonusInfo(localeInfo.GENERAL_BLOCK, 			item.APPLY_BLOCK),
		BonusInfo(localeInfo.GENERAL_DODGE, 			item.APPLY_DODGE),
		BonusInfo(localeInfo.GENERAL_REFLECT_HIT, 		item.APPLY_REFLECT_MELEE),
		BonusInfo(localeInfo.GENERAL_CRIT_CHANCE, 		item.APPLY_CRITICAL_PCT),
		BonusInfo(localeInfo.GENERAL_PENE_CHANCE, 		item.APPLY_PENETRATE_PCT),
		BonusInfo(localeInfo.GENERAL_IGNORE_BLOCK, 	item.APPLY_BLOCK_IGNORE_BONUS),
		BonusInfo(localeInfo.GENERAL_CASTING_SPEED, 	item.APPLY_CAST_SPEED),
		BonusInfo(localeInfo.MELEE_MAGIC_ATTBONUS_PER, 	item.APPLY_MELEE_MAGIC_ATTBONUS_PER),

		# Resistance Category
		BonusCategory(localeInfo.CATEGORY_RESISTANCE),
		BonusInfo(localeInfo.RESIST_SWORDS, 	item.APPLY_RESIST_SWORD),
		BonusInfo(localeInfo.RESIST_TWOHAND, 	item.APPLY_RESIST_TWOHAND),
		BonusInfo(localeInfo.RESIST_DAGGERS, 	item.APPLY_RESIST_DAGGER),
		BonusInfo(localeInfo.RESIST_BELLS,		item.APPLY_RESIST_BELL),
		BonusInfo(localeInfo.RESIST_FANS, 		item.APPLY_RESIST_FAN),
		BonusInfo(localeInfo.RESIST_ARROWS,	item.APPLY_RESIST_BOW),
		BonusInfo(localeInfo.RESIST_MAGIC, 	item.APPLY_RESIST_MAGIC),
		BonusInfo(localeInfo.SKILL_DEFEND_BONUS, 	item.APPLY_SKILL_DEFEND_BONUS),
		BonusInfo(localeInfo.NORMAL_HIT_DEFEND_BONUS, 	item.APPLY_NORMAL_HIT_DEFEND_BONUS),
		BonusInfo(localeInfo.RESIST_HUMAN, 	item.APPLY_RESIST_HUMAN),
		BonusInfo(localeInfo.RESIST_MONSTER, 	item.APPLY_RESIST_MONSTER),

	]

	if __SERVER__ == 2:
		TAB_BONUS = [

			# PvM Category
			BonusCategory(localeInfo.CATEGORY_PVM),
			BonusInfo(localeInfo.STRONG_VS_MONSTERS, 	item.APPLY_ATTBONUS_MONSTER),
			BonusInfo(localeInfo.STRONG_VS_METINS, 	item.APPLY_ATTBONUS_METIN),
			BonusInfo(localeInfo.STRONG_VS_BOSSES, 	item.APPLY_ATTBONUS_BOSS),
			BonusInfo(localeInfo.STRONG_VS_UNDEAD, 	item.APPLY_ATTBONUS_UNDEAD),
			BonusInfo(localeInfo.STRONG_VS_DEVILS, 	item.APPLY_ATTBONUS_DEVIL),
			BonusInfo(localeInfo.STRONG_VS_ORCS,  		item.APPLY_ATTBONUS_ORC),
			BonusInfo(localeInfo.STRONG_VS_ANIMALS, 	item.APPLY_ATTBONUS_ANIMAL),
			# BonusInfo(localeInfo.STRONG_VS_ZODIAC, 	item.APPLY_ATTBONUS_ZODIAC),

			# PvP Category
			BonusCategory(localeInfo.CATEGORY_PVP),
			BonusInfo(localeInfo.STRONG_VS_HALFHUMANS, 	item.APPLY_ATTBONUS_HUMAN),
			BonusInfo(localeInfo.STRONG_VS_WARRIOR, 		item.APPLY_ATTBONUS_WARRIOR),
			BonusInfo(localeInfo.STRONG_VS_SURA, 			item.APPLY_ATTBONUS_SURA),
			BonusInfo(localeInfo.STRONG_VS_ASSASSIN, 		item.APPLY_ATTBONUS_ASSASSIN),
			BonusInfo(localeInfo.STRONG_VS_SHAMAN, 		item.APPLY_ATTBONUS_SHAMAN),

			BonusInfo(localeInfo.WARRIOR_RESISTANCE, 	item.APPLY_RESIST_WARRIOR),
			BonusInfo(localeInfo.SURA_RESISTANCE, 		item.APPLY_RESIST_SURA),
			BonusInfo(localeInfo.ASSASSIN_RESISTANCE, 	item.APPLY_RESIST_ASSASSIN),
			BonusInfo(localeInfo.SHAMAN_RESISTANCE, 	item.APPLY_RESIST_SHAMAN),

			# General Category
			BonusCategory(localeInfo.CATEGORY_GENERAL),
			BonusInfo(localeInfo.SKILL_DAMAGE_BONUS, 	item.APPLY_SKILL_DAMAGE_BONUS),
			BonusInfo(localeInfo.NORMAL_HIT_DAMAGE_BONUS, 	item.APPLY_NORMAL_HIT_DAMAGE_BONUS),
			BonusInfo(localeInfo.GENERAL_HP_STEAL, 	item.APPLY_STEAL_HP),
			BonusInfo(localeInfo.GENERAL_SP_STEAL, 	item.APPLY_STEAL_SP),
			BonusInfo(localeInfo.GENERAL_MAX_HP, 		item.APPLY_MAX_HP),
			BonusInfo(localeInfo.GENERAL_MAX_SP, 		item.APPLY_MAX_SP),
			BonusInfo(localeInfo.GENERAL_HP_REGEN, 	item.APPLY_HP_REGEN),
			BonusInfo(localeInfo.GENERAL_SP_REGEN, 	item.APPLY_SP_REGEN),
			BonusInfo(localeInfo.GENERAL_BLOCK, 			item.APPLY_BLOCK),
			BonusInfo(localeInfo.GENERAL_DODGE, 			item.APPLY_DODGE),
			BonusInfo(localeInfo.GENERAL_REFLECT_HIT, 		item.APPLY_REFLECT_MELEE),
			BonusInfo(localeInfo.GENERAL_CRIT_CHANCE, 		item.APPLY_CRITICAL_PCT),
			BonusInfo(localeInfo.GENERAL_PENE_CHANCE, 		item.APPLY_PENETRATE_PCT),
			BonusInfo(localeInfo.GENERAL_IGNORE_BLOCK, 	item.APPLY_BLOCK_IGNORE_BONUS),
			BonusInfo(localeInfo.GENERAL_CASTING_SPEED, 	item.APPLY_CAST_SPEED),
			BonusInfo(localeInfo.MELEE_MAGIC_ATTBONUS_PER, 	item.APPLY_MELEE_MAGIC_ATTBONUS_PER),
			BonusInfo(localeInfo.TOOLTIP_CHANCE_EXP_BONUS, 	item.APPLY_EXP_DOUBLE_BONUS),
			BonusInfo(localeInfo.TOOLTIP_CHANCE_YANG_DROP, 	item.APPLY_GOLD_DOUBLE_BONUS),
			BonusInfo(localeInfo.TOOLTIP_CHANCE_ITEM_DROP, 	item.APPLY_ITEM_DROP_BONUS),

			# Resistance Category
			BonusCategory(localeInfo.CATEGORY_RESISTANCE),
			BonusInfo(localeInfo.RESIST_SWORDS, 	item.APPLY_RESIST_SWORD),
			BonusInfo(localeInfo.RESIST_TWOHAND, 	item.APPLY_RESIST_TWOHAND),
			BonusInfo(localeInfo.RESIST_DAGGERS, 	item.APPLY_RESIST_DAGGER),
			BonusInfo(localeInfo.RESIST_BELLS,		item.APPLY_RESIST_BELL),
			BonusInfo(localeInfo.RESIST_FANS, 		item.APPLY_RESIST_FAN),
			BonusInfo(localeInfo.RESIST_ARROWS,	item.APPLY_RESIST_BOW),
			BonusInfo(localeInfo.RESIST_MAGIC, 	item.APPLY_RESIST_MAGIC),
			BonusInfo(localeInfo.SKILL_DEFEND_BONUS, 	item.APPLY_SKILL_DEFEND_BONUS),
			BonusInfo(localeInfo.NORMAL_HIT_DEFEND_BONUS, 	item.APPLY_NORMAL_HIT_DEFEND_BONUS),
			BonusInfo(localeInfo.RESIST_HUMAN, 	item.APPLY_RESIST_HUMAN),
			BonusInfo(localeInfo.RESIST_MONSTER, 	item.APPLY_RESIST_MONSTER),
			BonusInfo(localeInfo.RESIST_BOSS, 	item.APPLY_RESIST_BOSS),
			BonusInfo(localeInfo.TOOLTIP_RESISTANCE_FIRE, 	item.APPLY_RESIST_FIRE),
			BonusInfo(localeInfo.TOOLTIP_RESISTANCE_ICE, 	item.APPLY_RESIST_ICE),
			BonusInfo(localeInfo.TOOLTIP_RESISTANCE_EARTH, 	item.APPLY_RESIST_EARTH),
			BonusInfo(localeInfo.TOOLTIP_RESISTANCE_WIND, 	item.APPLY_RESIST_WIND),
			BonusInfo(localeInfo.TOOLTIP_RESISTANCE_DARKNESS, 	item.APPLY_RESIST_DARK),
			BonusInfo(localeInfo.TOOLTIP_RESISTANCE_LIGHTNING, 	item.APPLY_RESIST_ELEC),
		]

	TAB_KILLSTATS = [

		# KINGDOM KILLS
		KillStat(player.POINT_EMPIRE_C_KILLED, localeInfo.EMPIRE_C, "kill_blue.tga"),
		KillStat(player.POINT_EMPIRE_A_KILLED, localeInfo.EMPIRE_A, "kill_red.tga"),
		KillStat(player.POINT_EMPIRE_B_KILLED, localeInfo.EMPIRE_B, "kill_yellow.tga"),

		KillStat(-1, localeInfo.TOTAL_PLAYERS_KILLED),
		KillStat(player.POINT_DUELS_WON, localeInfo.DUELS_WON),
		KillStat(player.POINT_DUELS_LOST, localeInfo.DUELS_LOST),
		KillStat(player.POINT_MONSTERS_KILLED, localeInfo.MONSTERS_KILLED),
		KillStat(player.POINT_BOSSES_KILLED, localeInfo.BOSSES_KILLED),
		KillStat(player.POINT_STONES_DESTROYED, localeInfo.METINS_KILLED),

	]

	def __init__(self):
		ui.ScriptWindow.__init__(self)

		self.currentTabId = 0

		self.LoadWindowAndGUI()

	def __del__(self):
		ui.ScriptWindow.__del__(self)

	def Destroy(self):
		pass

	def LoadWindowAndGUI(self):

		# set window size and put it in center		
		self.SetSize(self.WIDTH, self.HEIGHT)

		# main background
		self.backgroundImage = ui.ImageBox()
		self.backgroundImage.SetParent(self)
		self.backgroundImage.SetPosition(0, 0)
		self.backgroundImage.LoadImage(UISTATSBOARD_PATH+ "bg_boni.tga")

		# bonus tab
		self.btnBoni = ui.RadioButton()
		self.btnBoni.SetParent(self)
		self.btnBoni.SetUpVisual(UISTATSBOARD_PATH + "slot_normal.tga")
		self.btnBoni.SetOverVisual(UISTATSBOARD_PATH + "slot_hover.tga")
		self.btnBoni.SetDownVisual(UISTATSBOARD_PATH + "slot_active.tga")
		self.btnBoni.SetPosition(25, 10)
		self.btnBoni.SetText(localeInfo.BONI_BOARD)
		self.btnBoni.SetEvent(self.OnBoniButton)

		# kills tab
		self.btnKills = ui.RadioButton()
		self.btnKills.SetParent(self)
		self.btnKills.SetUpVisual(UISTATSBOARD_PATH + "slot_normal.tga")
		self.btnKills.SetOverVisual(UISTATSBOARD_PATH + "slot_hover.tga")
		self.btnKills.SetDownVisual(UISTATSBOARD_PATH + "slot_active.tga")
		self.btnKills.SetPosition(126, 10)
		self.btnKills.SetText(localeInfo.KILL_STATS)
		self.btnKills.SetEvent(self.OnKillStatsButton)

		# declare the item height for lists
		self.VIEW_COUNT = 10

		self.boniTab = ui.ListBoxEx()
		self.boniTab.SetParent(self)
		self.boniTab.SetPosition(self.MARGIN_X, self.MARGIN_Y)
		self.boniTab.SetSize(229, UISTATSBOARD_ITEM_HEIGHT * self.VIEW_COUNT)
		self.boniTab.SetItemSize(0, UISTATSBOARD_ITEM_HEIGHT)
		self.boniTab.SetViewItemCount(self.VIEW_COUNT)
		self.boniTab.SetItemStep(UISTATSBOARD_ITEM_HEIGHT)

		self.killTab = ui.ListBoxEx()
		self.killTab.SetParent(self)
		self.killTab.SetPosition(self.MARGIN_X, self.MARGIN_Y)
		self.killTab.SetSize(229, UISTATSBOARD_ITEM_HEIGHT * self.VIEW_COUNT)
		self.killTab.SetItemSize(0, UISTATSBOARD_ITEM_HEIGHT)
		self.killTab.SetViewItemCount(self.VIEW_COUNT)
		self.killTab.SetItemStep(UISTATSBOARD_ITEM_HEIGHT)

		# initialize boni board
		for element in self.TAB_BONUS:
			self.boniTab.AppendItem(element)

		# initialize kill stats
		for element in self.TAB_KILLSTATS:
			self.killTab.AppendItem(element)

		# scrollbar is only for boni board
		self.scrollBar = ui.ScrollBarTemplate()
		self.scrollBar.SetParent(self)
		self.scrollBar.SetPosition(226, 40)

		scrollPath = UISTATSBOARD_PATH + "scroll/"

		self.scrollBar.SetBarPartImages(scrollPath + "scroll_top.tga", scrollPath + "scroll_center.tga", scrollPath + "scroll_bottom.tga")
		self.scrollBar.SetMiddleImage(scrollPath + "scrollbar_new.tga")
		self.scrollBar.SetScrollBarSize(UISTATSBOARD_ITEM_HEIGHT * self.VIEW_COUNT)
		self.scrollBar.SetScrollEvent(self.OnScrollItemList)

		# show elements
		self.backgroundImage.Show()
		self.btnBoni.Show()
		self.btnKills.Show()
		self.boniTab.Show()

		# refresh current tab etc...
		self.ChangeTab(0)
		self.Refresh()

	def GetCurrentTabId(self):
		return self.currentTabId

	def GetCurrentTab(self):

		if self.GetCurrentTabId() == 0:
			return self.boniTab
		
		if self.GetCurrentTabId() == 1:
			return self.killTab

		return None

	def ChangeTab(self, tabId):

		if tabId == 0:
			self.btnKills.SetUp()
			self.btnBoni.Down()

			self.killTab.Hide()
			self.boniTab.Show()

		elif tabId == 1:
			self.btnBoni.SetUp()
			self.btnKills.Down()

			self.boniTab.Hide()
			self.killTab.Show()

		self.currentTabId = tabId
		self.Refresh()

	def OnBoniButton(self):
		self.ChangeTab(0)

	def OnKillStatsButton(self):
		self.ChangeTab(1)

	def Refresh(self):
		currentTabId = self.GetCurrentTabId()
		currentTab = self.GetCurrentTab()
		elementsCount = currentTab.GetItemCount()

		# should scroll be visible?
		scrollbarVisible = (elementsCount > self.VIEW_COUNT)

		if scrollbarVisible and self.GetCurrentTabId() == 0:
			self.scrollBar.SetMiddleBarSize(float(self.VIEW_COUNT) / float(elementsCount))
			self.scrollBar.Show()
		
		else:
			self.scrollBar.Hide()

		for i in range(0, elementsCount):
			
			element = currentTab.GetItemAtIndex(i)

			if not element:
				tchat("get element failure for boni board")
				continue

			element.RefreshCallback()

	def AdjustPosition(self, x, y):
		# + size of character window
		self.SetPosition(x + 251, y + 3)

	def OnScrollItemList(self):

		if not self.IsShow():
			return

		maxBasePos = self.GetCurrentTab().GetScrollLen()
		basePos = int(self.scrollBar.GetPos() * maxBasePos)

		if basePos != self.GetCurrentTab().GetBasePos():
			self.GetCurrentTab().SetBasePos(basePos)

	def OnMouseWheel(self, len):

		if self.IsInPosition() and self.scrollBar.IsShow():

			basePos = self.GetCurrentTab().GetBasePos() + constInfo.WHEEL_TO_SCROLL(len)

			if basePos < 0:
				basePos = 0

			maxBasePos = self.GetCurrentTab().GetScrollLen()

			if basePos > maxBasePos:
				basePos = maxBasePos

			newPos = float(basePos) / float(max(1, maxBasePos))
			self.scrollBar.SetPos(newPos)
			return True

		return False

	def Close(self):
		self.Hide()
		return True
		
	def Open(self):

		if not constInfo.BONI_BOARD:
			return

		self.Show()
		ui.ScriptWindow.Show(self)
