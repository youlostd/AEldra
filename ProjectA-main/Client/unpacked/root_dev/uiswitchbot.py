import shop
import player
import item
import ui
import net
import locale
import chat
import grp
import wndMgr
import mouseModule
import uiToolTip
import app
import localeInfo
import uiCommon
import constInfo
from uitooltip import ItemToolTip
# Switchbot by Mijago ; v 2.2.1

WEAR_NAMES = ItemToolTip.WEAR_NAMES


AFFECT_DICT = {
		item.APPLY_MAX_HP : localeInfo.TOOLTIP_MAX_HP,
		item.APPLY_MAX_SP : localeInfo.TOOLTIP_MAX_SP,
		item.APPLY_CON : localeInfo.TOOLTIP_CON,
		item.APPLY_INT : localeInfo.TOOLTIP_INT,
		item.APPLY_STR : localeInfo.TOOLTIP_STR,
		item.APPLY_DEX : localeInfo.TOOLTIP_DEX,
		item.APPLY_ATT_SPEED : localeInfo.TOOLTIP_ATT_SPEED,
		item.APPLY_MOV_SPEED : localeInfo.TOOLTIP_MOV_SPEED,
		item.APPLY_CAST_SPEED : localeInfo.TOOLTIP_CAST_SPEED,
		item.APPLY_HP_REGEN : localeInfo.TOOLTIP_HP_REGEN,
		item.APPLY_SP_REGEN : localeInfo.TOOLTIP_SP_REGEN,
		item.APPLY_POISON_PCT : localeInfo.TOOLTIP_APPLY_POISON_PCT,
		item.APPLY_STUN_PCT : localeInfo.TOOLTIP_APPLY_STUN_PCT,
		item.APPLY_SLOW_PCT : localeInfo.TOOLTIP_APPLY_SLOW_PCT,
		item.APPLY_CRITICAL_PCT : localeInfo.TOOLTIP_APPLY_CRITICAL_PCT,
		item.APPLY_PENETRATE_PCT : localeInfo.TOOLTIP_APPLY_PENETRATE_PCT,

		item.APPLY_ATTBONUS_WARRIOR : localeInfo.TOOLTIP_APPLY_ATTBONUS_WARRIOR,
		item.APPLY_ATTBONUS_ASSASSIN : localeInfo.TOOLTIP_APPLY_ATTBONUS_ASSASSIN,
		item.APPLY_ATTBONUS_SURA : localeInfo.TOOLTIP_APPLY_ATTBONUS_SURA,
		item.APPLY_ATTBONUS_SHAMAN : localeInfo.TOOLTIP_APPLY_ATTBONUS_SHAMAN,
		item.APPLY_ATTBONUS_MONSTER : localeInfo.TOOLTIP_APPLY_ATTBONUS_MONSTER,
		item.APPLY_ATTBONUS_ZODIAC : localeInfo.TOOLTIP_APPLY_ATTBONUS_ZODIAC,

		item.APPLY_ATTBONUS_HUMAN : localeInfo.TOOLTIP_APPLY_ATTBONUS_HUMAN,
		item.APPLY_ATTBONUS_ANIMAL : localeInfo.TOOLTIP_APPLY_ATTBONUS_ANIMAL,
		item.APPLY_ATTBONUS_ORC : localeInfo.TOOLTIP_APPLY_ATTBONUS_ORC,
		item.APPLY_ATTBONUS_MILGYO : localeInfo.TOOLTIP_APPLY_ATTBONUS_MILGYO,
		item.APPLY_ATTBONUS_UNDEAD : localeInfo.TOOLTIP_APPLY_ATTBONUS_UNDEAD,
		item.APPLY_ATTBONUS_DEVIL : localeInfo.TOOLTIP_APPLY_ATTBONUS_DEVIL,
		item.APPLY_STEAL_HP : localeInfo.TOOLTIP_APPLY_STEAL_HP,
		item.APPLY_STEAL_SP : localeInfo.TOOLTIP_APPLY_STEAL_SP,
		item.APPLY_MANA_BURN_PCT : localeInfo.TOOLTIP_APPLY_MANA_BURN_PCT,
		item.APPLY_DAMAGE_SP_RECOVER : localeInfo.TOOLTIP_APPLY_DAMAGE_SP_RECOVER,
		item.APPLY_BLOCK : localeInfo.TOOLTIP_APPLY_BLOCK,
		item.APPLY_DODGE : localeInfo.TOOLTIP_APPLY_DODGE,
		item.APPLY_RESIST_SWORD : localeInfo.TOOLTIP_APPLY_RESIST_SWORD,
		item.APPLY_RESIST_TWOHAND : localeInfo.TOOLTIP_APPLY_RESIST_TWOHAND,
		item.APPLY_RESIST_DAGGER : localeInfo.TOOLTIP_APPLY_RESIST_DAGGER,
		item.APPLY_RESIST_BELL : localeInfo.TOOLTIP_APPLY_RESIST_BELL,
		item.APPLY_RESIST_FAN : localeInfo.TOOLTIP_APPLY_RESIST_FAN,
		item.APPLY_RESIST_BOW : localeInfo.TOOLTIP_RESIST_BOW,
		item.APPLY_RESIST_FIRE : localeInfo.TOOLTIP_RESIST_FIRE,
		item.APPLY_RESIST_ELEC : localeInfo.TOOLTIP_RESIST_ELEC,
		item.APPLY_RESIST_MAGIC : localeInfo.TOOLTIP_RESIST_MAGIC,
		item.APPLY_RESIST_WIND : localeInfo.TOOLTIP_APPLY_RESIST_WIND,
		item.APPLY_REFLECT_MELEE : localeInfo.TOOLTIP_APPLY_REFLECT_MELEE,
		item.APPLY_REFLECT_CURSE : localeInfo.TOOLTIP_APPLY_REFLECT_CURSE,
		item.APPLY_POISON_REDUCE : localeInfo.TOOLTIP_APPLY_POISON_REDUCE,
		item.APPLY_KILL_SP_RECOVER : localeInfo.TOOLTIP_APPLY_KILL_SP_RECOVER,
		item.APPLY_EXP_DOUBLE_BONUS : localeInfo.TOOLTIP_APPLY_EXP_DOUBLE_BONUS,
		item.APPLY_GOLD_DOUBLE_BONUS : localeInfo.TOOLTIP_APPLY_GOLD_DOUBLE_BONUS,
		item.APPLY_ITEM_DROP_BONUS : localeInfo.TOOLTIP_APPLY_ITEM_DROP_BONUS,
		item.APPLY_POTION_BONUS : localeInfo.TOOLTIP_APPLY_POTION_BONUS,
		item.APPLY_KILL_HP_RECOVER : localeInfo.TOOLTIP_APPLY_KILL_HP_RECOVER,
		item.APPLY_IMMUNE_STUN : localeInfo.TOOLTIP_APPLY_IMMUNE_STUN,
		item.APPLY_IMMUNE_SLOW : localeInfo.TOOLTIP_APPLY_IMMUNE_SLOW,
		item.APPLY_IMMUNE_FALL : localeInfo.TOOLTIP_APPLY_IMMUNE_FALL,
		item.APPLY_BOW_DISTANCE : localeInfo.TOOLTIP_BOW_DISTANCE,
		item.APPLY_DEF_GRADE_BONUS : localeInfo.TOOLTIP_DEF_GRADE,
		item.APPLY_ATT_GRADE_BONUS : localeInfo.TOOLTIP_ATT_GRADE,
		item.APPLY_MAGIC_ATT_GRADE : localeInfo.TOOLTIP_MAGIC_ATT_GRADE,
		item.APPLY_MAGIC_DEF_GRADE : localeInfo.TOOLTIP_MAGIC_DEF_GRADE,
		item.APPLY_MAX_STAMINA : localeInfo.TOOLTIP_MAX_STAMINA,
		item.APPLY_MALL_ATTBONUS : localeInfo.TOOLTIP_MALL_ATTBONUS,
		item.APPLY_MALL_DEFBONUS : localeInfo.TOOLTIP_MALL_DEFBONUS,
		item.APPLY_MALL_EXPBONUS : localeInfo.TOOLTIP_MALL_EXPBONUS,
		item.APPLY_MALL_ITEMBONUS : localeInfo.TOOLTIP_MALL_ITEMBONUS,
		item.APPLY_MALL_GOLDBONUS : localeInfo.TOOLTIP_MALL_GOLDBONUS,
		item.APPLY_SKILL_DAMAGE_BONUS : localeInfo.TOOLTIP_SKILL_DAMAGE_BONUS,
		item.APPLY_NORMAL_HIT_DAMAGE_BONUS : localeInfo.TOOLTIP_NORMAL_HIT_DAMAGE_BONUS,
		item.APPLY_SKILL_DEFEND_BONUS : localeInfo.TOOLTIP_SKILL_DEFEND_BONUS,
		item.APPLY_NORMAL_HIT_DEFEND_BONUS : localeInfo.TOOLTIP_NORMAL_HIT_DEFEND_BONUS,
		item.APPLY_RESIST_WARRIOR : localeInfo.TOOLTIP_APPLY_RESIST_WARRIOR,
		item.APPLY_RESIST_ASSASSIN : localeInfo.TOOLTIP_APPLY_RESIST_ASSASSIN,
		item.APPLY_RESIST_SURA : localeInfo.TOOLTIP_APPLY_RESIST_SURA,
		item.APPLY_RESIST_SHAMAN : localeInfo.TOOLTIP_APPLY_RESIST_SHAMAN,
		
		# item.APPLY_BLEEDING_PCT : localeInfo.TOOLTIP_APPLY_BLEEDING_PCT,
		# item.APPLY_BLEEDING_REDUCE : localeInfo.TOOLTIP_APPLY_BLEEDING_REDUCE,
		# item.APPLY_ATTBONUS_WOLFMAN : localeInfo.TOOLTIP_APPLY_ATTBONUS_WOLFMAN,
		# item.APPLY_RESIST_WOLFMAN : localeInfo.TOOLTIP_APPLY_RESIST_WOLFMAN,
		# item.APPLY_RESIST_CLAW : localeInfo.TOOLTIP_APPLY_RESIST_CLAW,

		item.APPLY_ACCEDRAIN_RATE : localeInfo.TOOLTIP_APPLY_ACCEDRAIN_RATE,

		# item.APPLY_PET_EXP_BONUS : localeInfo.TOOLTIP_APPLY_PET_EXP_BONUS,

		item.APPLY_RESIST_MONSTER : localeInfo.TOOLTIP_APPLY_RESIST_MONSTER,
		item.APPLY_ATTBONUS_METIN : localeInfo.TOOLTIP_APPLY_ATTBONUS_METIN,
		item.APPLY_ATTBONUS_BOSS : localeInfo.TOOLTIP_APPLY_ATTBONUS_BOSS,

		item.APPLY_MELEE_MAGIC_ATTBONUS_PER : localeInfo.TOOLTIP_APPLY_MELEE_MAGIC_ATTBONUS_PER,
		item.APPLY_RESIST_SWORD_PEN : localeInfo.TOOLTIP_APPLY_RESIST_SWORD_PEN,
		item.APPLY_RESIST_TWOHAND_PEN : localeInfo.TOOLTIP_APPLY_RESIST_TWOHAND_PEN,
		item.APPLY_RESIST_DAGGER_PEN : localeInfo.TOOLTIP_APPLY_RESIST_DAGGER_PEN,
		item.APPLY_RESIST_BELL_PEN : localeInfo.TOOLTIP_APPLY_RESIST_BELL_PEN,
		item.APPLY_RESIST_FAN_PEN : localeInfo.TOOLTIP_APPLY_RESIST_FAN_PEN,
		item.APPLY_RESIST_BOW_PEN : localeInfo.TOOLTIP_APPLY_RESIST_BOW_PEN,
		item.APPLY_RESIST_ATTBONUS_HUMAN : localeInfo.TOOLTIP_APPLY_RESIST_ATTBONUS_HUMAN,
		item.APPLY_RESIST_ICE : localeInfo.TOOLTIP_APPLY_RESIST_ICE,
		item.APPLY_RESIST_EARTH : localeInfo.TOOLTIP_APPLY_RESIST_EARTH,
		
		item.APPLY_DEFENSE_BONUS : localeInfo.TOOLTIP_APPLY_DEFENSE_BONUS,
		
	}

SWITCH_VNUM = {
					71151 : [0, 40],
					71084 : [0, 105],
					92870 : [0, 105],
				}

# Die folgenden zahlen geben den MINMAX Bereich des Reglers an, der die Zeit angibt.
MIN_SWITCH_DELAY = 35
MAX_SWITCH_DELAY_APPEND = 120

# Max 10!!
MAX_NUM = 7

proposals = {
	1: { # 1 = Weapon
		"PVP (Körper)":[
			[9,10],
			[15,10],
			[17,10],
			[16,10],
			[5,8],
			[3,8],
		],
		"PVP (Mental)":[
			[9,10],
			[15,10],
			[17,10],
			[6,8],
			[5,10],
			[16,10],
		],
		"PVM": [
			[5,10],
			[19,20],
		],
	},
	2: [ # Armor
		[ #BODY,
		],
		[ #HEAD,
		],
		[ #SHIELD,
		],
		[ #WRIST,
		],
		[ #FOOTS,
		],
		[ #NECK,
		],
		[ #EAR,
		],
	],
}

# Farben :)
# COLOR_BG = grp.GenerateColor(0.0, 0.0, 0.0, 0.5)
# COLOR_INACTIVE = grp.GenerateColor(0.0, 0.0, 1.0, 0.2)
# COLOR_ACTIVE   = grp.GenerateColor(0.1, 0.6, 1.0, 0.2)
# COLOR_FINISHED = grp.GenerateColor(0.0, 0.8, 1.0, 0.3)

# COLOR_PIN_HINT = grp.GenerateColor(0.0, 0.5, 1.0, 0.3)

# COLOR_CHECKBOX_NOT_SELECTED = grp.GenerateColor(0.0, 0.3, 1.0, 0.1)
# COLOR_CHECKBOX_SELECTED = grp.GenerateColor(0.0, 0.3, 1.0, 0.3)

# Standardfarben:
COLOR_BG = grp.GenerateColor(0.0, 0.0, 0.0, 0.5)
COLOR_INACTIVE = grp.GenerateColor(1.0, 0.0, 0.0, 0.2)
COLOR_ACTIVE   = grp.GenerateColor(1.0, 0.6, 0.1, 0.2)
COLOR_FINISHED = grp.GenerateColor(0.0, 1.0, 0.0, 0.2)

COLOR_PIN_HINT = grp.GenerateColor(0.0, 0.5, 1.0, 0.3)

COLOR_CHECKBOX_NOT_SELECTED = grp.GenerateColor(1.0, 0.3, 0.0, 0.1)
COLOR_CHECKBOX_SELECTED = grp.GenerateColor(0.3, 1.0, 1.0, 0.3)


DISTANCE_BOTTOM = 36

class Bar(ui.Bar):
	def __init__(self,layer = "UI"):
		ui.Bar.__init__(self,layer)
	def SetColor(self,color):
		wndMgr.SetColor(self.hWnd, color)
		self.color = color


class BonusSelector(ui.Bar):
	itemTypes = {
		item.ITEM_TYPE_WEAPON : [-1],
		item.ITEM_TYPE_ARMOR : [item.ARMOR_BODY, item.ARMOR_HEAD, item.ARMOR_SHIELD, item.ARMOR_WRIST, item.ARMOR_FOOTS, item.ARMOR_NECK, item.ARMOR_EAR],
		item.ITEM_TYPE_COSTUME : [item.COSTUME_TYPE_BODY, item.COSTUME_TYPE_HAIR, item.COSTUME_TYPE_WEAPON],
		item.ITEM_TYPE_TOTEM : [-1],
	}

	def Activate(self):
		self.sub_parent.resetSwitch()
		self.Status_new.SetColor(COLOR_ACTIVE)
		self.sub_parent.StatusBar.SetColor(COLOR_ACTIVE)
		self.sub_parent.StatusText.SetText("Aktiv")
		self.Starter.SetText("Switchen ("+str(self.index+1)+") anhalten")
		self.sub_parent.boni_active = 1

		attrStr = " "
		for i in range(0,5):
			if self.boni[5-i][1].selected.value != 0:
				attrStr += str(self.boni[5-i][1].selected.value) + " " + str(self.boni[5-i][3].GetText()) + " "
		net.SendChatPacket("/switchbot_start %d %s" % (self.index, attrStr))

		if self.parentWindow.parentWindow != 0 and self.parentWindow.parentWindow.gameWindow != None:
			self.sub_parent.blockBar.swib_normal.SetColor(COLOR_ACTIVE)
		pass

	def Deactivate(self):
		self.sub_parent.resetSwitch()
		self.Status_new.SetColor(COLOR_INACTIVE)
		self.sub_parent.StatusBar.SetColor(COLOR_INACTIVE)
		self.sub_parent.StatusText.SetText("Inaktiv")
		self.Starter.SetText("Switchen ("+str(self.index+1)+") starten")
		self.sub_parent.boni_active = 0
		net.SendChatPacket("/switchbot_stop %d" % (self.index))
		if self.parentWindow.parentWindow != 0 and self.sub_parent.parentWindow.parentWindow.gameWindow != None:
			self.sub_parent.blockBar.swib_normal.SetColor(COLOR_INACTIVE)
		
	def Finish(self):
		self.Status_new.SetColor(COLOR_FINISHED)
		self.sub_parent.StatusBar.SetColor(COLOR_FINISHED)
		self.sub_parent.StatusText.SetText("Fertig")
		self.Starter.SetText("Switchen ("+str(self.index+1)+") fortsetzen")
		self.sub_parent.boni_active = 0
		app.StartFlashApplication()
		if self.sub_parent.parentWindow.parentWindow != 0 and self.sub_parent.parentWindow.parentWindow.gameWindow != None:
			self.sub_parent.blockBar.swib_normal.SetColor(COLOR_FINISHED)
		
	def Block(self):
		self.BlockBar.Show()
		self.BlockBar.sub.Show()
		self.Starter.Hide()
		pass
	def Unblock(self):
		self.BlockBar.sub.Hide()
		self.BlockBar.Hide()
		self.Starter.Show()
		pass
		
	def __init__(self,sub_parent):
		ui.Bar.__init__(self, "UI")
		self.sub_parent = sub_parent
		self.index = sub_parent.index
		self.SetColor(COLOR_BG)
		self.SetSize(500,195+10)
		self.boni = {}
		self.Status_new = ui.Bar()
		self.Status_new.SetParent(self)
		self.Status_new.SetColor(COLOR_INACTIVE)
		self.Status_new.SetSize(500,5)
		self.Status_new.Show()
		
		self.Starter = ui.ToggleButton()
		self.Starter.SetParent(self)
		self.Starter.SetUpVisual("d:/ymir work/ui/public/XLarge_Button_01.sub")
		self.Starter.SetOverVisual("d:/ymir work/ui/public/XLarge_button_02.sub")
		self.Starter.SetDownVisual("d:/ymir work/ui/public/XLarge_button_03.sub")
		self.Starter.SetText("Switchen starten")
		self.Starter.SetToggleDownEvent(self.Activate)
		self.Starter.SetToggleUpEvent(self.Deactivate)
		self.Starter.Show()

		self.BoniMaxCount = ui.Button()
		self.BoniMaxCount.SetParent(self)
		self.BoniMaxCount.SetUpVisual("d:/ymir work/ui/public/Large_Button_01.sub")
		self.BoniMaxCount.SetOverVisual("d:/ymir work/ui/public/Large_Button_02.sub")
		self.BoniMaxCount.SetDownVisual("d:/ymir work/ui/public/Large_Button_03.sub")
		self.BoniMaxCount.SetText(localeInfo.SWITCHBOT_MAX_USE_SWITCHER_UNLIMITED)
		self.BoniMaxCount.Hide()
		self.BoniMaxCount.value = 0
		self.BoniMaxCount.SAFE_SetEvent(self.__SelectMaxSwitcherCount)

		self.Starter.SetPosition(self.GetWidth()/2-(self.Starter.GetWidth())/2,140)
		self.BoniMaxCount.SetPosition(self.Starter.GetRight() + 5,140)

		self.inputDlg = uiCommon.InputDialogWithDescription()
		self.inputDlg.SetTitle(localeInfo.SWITCHBOT_MAX_USE_QUESTION_TITLE)
		self.inputDlg.SetDescription(localeInfo.SWITCHBOT_MAX_USE_QUESTION_DESC)
		self.inputDlg.SetNumberMode()
		self.inputDlg.SetCancelEvent(self.__CloseInputDialog)
		self.inputDlg.SetBoardWidth(250)
		self.inputDlg.SoftClose()

		for i in range(0,5):
			vas = 5-i
			self.boni[vas] = {}
			self.boni[vas][0] = ui.TextLine()
			self.boni[vas][0].SetParent(self)
			self.boni[vas][0].SetText("Bonus "+str(vas))
			self.boni[vas][0].SetPosition(15,10+25*(vas-1))
			self.boni[vas][0].Show()
			self.boni[vas][1] = DropDown(self,"- Keiner -")
			self.boni[vas][1].SetPosition(70,10+25*(vas-1))
			self.boni[vas][1].OnChange = self.__OnChangeBoni
			self.boni[vas][1].OnChangeArg = (vas,)
			boniList = []
			for itemType in self.itemTypes:
				for itemSubType in self.itemTypes[itemType]:
					for i in xrange(item.GetAttributeCountByItemType(itemType, itemSubType)):
						itemAttrType, itemAttrValue = item.GetAttributeInfoByItemType(itemType, itemSubType, i)
						if itemAttrType in boniList:
							continue
						if itemAttrType == 0:
							continue
						boniList.append(itemAttrType)
						self.boni[vas][1].AppendItem(str(uiToolTip.GET_AFFECT_STRING(itemAttrType, itemAttrValue)),itemAttrType,itemAttrValue)
			self.boni[vas][1].AppendItem(str(uiToolTip.GET_AFFECT_STRING(item.APPLY_NORMAL_HIT_DAMAGE_BONUS,0)),item.APPLY_NORMAL_HIT_DAMAGE_BONUS,0)
			self.boni[vas][1].AppendItem(str(uiToolTip.GET_AFFECT_STRING(item.APPLY_SKILL_DAMAGE_BONUS,0)),item.APPLY_SKILL_DAMAGE_BONUS,0)
			self.boni[vas][1].SetSize(330,20)
			self.boni[vas][1].Show()
			self.boni[vas][2] = ui.Bar("UI")
			self.boni[vas][2].SetParent(self)
			self.boni[vas][2].SetPosition(410,10+25*(vas-1))
			self.boni[vas][2].SetColor(0xC0000000)
			self.boni[vas][2].SetSize(80,20)
			self.boni[vas][2].Show()
			self.boni[vas][3] = Edit2("0",14)
			self.boni[vas][3].SetParent(self.boni[vas][2])
			self.boni[vas][3].SetNumberMode()
			self.boni[vas][3].SetSize(80,20)
			self.boni[vas][3].SetPosition(4,3)
			self.boni[vas][3].Show()
			
		self.BlockBar = ui.Bar()
		self.BlockBar.SetParent(self)
		self.BlockBar.SetColor(COLOR_INACTIVE)
		self.BlockBar.SetPosition(0,5)
		self.BlockBar.SetSize(500,170-5+35+2)
		self.BlockBar.Hide()
		
		self.BlockBar.sub = ui.Bar()
		self.BlockBar.sub.SetParent(self)
		self.BlockBar.sub.SetColor(COLOR_INACTIVE)
		self.BlockBar.sub.SetPosition(500-122,5+170-5+35+2)
		self.BlockBar.sub.SetSize(122,30)
		self.BlockBar.sub.Hide()
		
		self.BlockText = ui.TextLine()
		self.BlockText.SetParent(self.BlockBar)
		self.BlockText.SetWindowHorizontalAlignCenter()
		self.BlockText.SetHorizontalAlignCenter()
		self.BlockText.SetPosition(0,140)
		self.BlockText.SetText("Dieses Item kannst du nicht switchen.")
		self.BlockText.Show()

	def __OnChangeBoni(self, vas):
		self.boni[vas][3].SetText(str(self.boni[vas][1].selected.GetValue2()))

	def __SelectMaxSwitcherCount(self):
		self.inputDlg.SetAcceptEvent(ui.__mem_func__(self.__OnSelectMaxSwitcherCount))
		self.inputDlg.Open()

	def __OnSelectMaxSwitcherCount(self):
		val = int(self.inputDlg.GetText())
		if val < 0:
			val = 0
		self.BoniMaxCount.value = val
		if val > 0:
			self.BoniMaxCount.SetText(localeInfo.NumberToString(val))
		else:
			self.BoniMaxCount.SetText(localeInfo.SWITCHBOT_MAX_USE_SWITCHER_UNLIMITED)

		self.__CloseInputDialog()

	def __CloseInputDialog(self):
		self.inputDlg.SoftClose()

class ItemTabBar(ui.Window):
	
	class BlockBar(ui.Window):
		size_res = 32
		multi = 1
		def SetSize(self,i=1):
			self.multi = i
			ui.Window.SetSize(self,self.size_res,self.size_res*i)
			self.swib_normal.SetSize(self.size_res,self.size_res*i)
			
		def __init__(self):
			ui.Window.__init__(self)
			self.swib_normal = ui.Bar()
			self.swib_normal.SetParent(self)
			self.swib_normal.SetSize(self.size_res,self.size_res*self.multi)
			self.swib_normal.SetColor(COLOR_INACTIVE)
			self.swib_normal.SetPosition(0,0)
			self.swib_normal.Show()
			
			self.SetSize(1)
			
	
	class ItemTab(ui.Bar):
		
		height_selected   = 36*3+8
		height_unselected = 36*3+5
		
		def Destroy(self):
			self.parentWindow.parentWindow.but_speed.SetParent(self.parentWindow.parentWindow)
			# self.parentWindow.parentWindow.help_stop_all.SetParent(self.parentWindow.parentWindow)
			self.parentWindow.parentWindow.help_duration.SetParent(self.parentWindow.parentWindow)
			# self.parentWindow.parentWindow.but_deactivate_all.SetParent(self.parentWindow.parentWindow)
			# self.parentWindow.parentWindow.but_deactivate_all.Hide()
			self.parentWindow.parentWindow.but_speed.Hide()
			
			self.bonusSelector.Hide()
			self.bonusSelector.__del__()
			self.Hide()
			self.__del__()
		
		def DeleteMe(self):
			self.parentWindow.DeleteTab(self.tabnum)
		
		def OnPressEscapeKey(self):
			tchat('esc6')
			# if done:
			self.parentWindow.parentWindow.Hide()
			# else:
			# 	self.parentWindow.parentWindow.PinShow(1)
			return True

		def __init__(self,parent,tabnum,index = 0,vnum = 0): ## Init ItemTab
			ui.Bar.__init__(self)
			self.SetColor(COLOR_BG)
			self.SetSize(self.width,self.height_unselected)
			self.index = index
			self.tabnum = tabnum
			self.vnum = vnum
			self.count = 0
			self.parentWindow = parent
			self.SetParent(parent)

			if self.parentWindow.parentWindow.gameWindow != None:
				self.blockBar = ItemTabBar.BlockBar()
				self.blockBar.SetParent(self.parentWindow.parentWindow.gameWindow.interface.wndInventory.wndItem)
				ipi = self.parentWindow.parentWindow.gameWindow.interface.wndInventory.inventoryPageIndex
				self.blockBar.Show()
				ip2 = self.index - ipi*45
				self.blockBar.SetPosition(((ip2-int(ip2/5)*5)*self.blockBar.size_res),int(ip2/5)*self.blockBar.size_res)
			
			self.ItemIcon = ui.ImageBox()
			self.ItemIcon.SetParent(self)
			self.ItemIcon.AddFlag("not_pick")
			self.ItemIcon.SetWindowHorizontalAlignCenter()
			self.ItemIcon.SetWindowVerticalAlignCenter()
			self.ItemIcon.Show()
			
			self.SlotName = ui.TextLine()
			self.SlotName.SetParent(self)
			self.SlotName.SetWindowHorizontalAlignCenter()
			self.SlotName.SetHorizontalAlignCenter()
			self.SlotName.SetPosition(0,5)
			self.SlotName.SetText("Slot %d" % (self.index+1))
			self.SlotName.AddFlag("not_pick")
			self.SlotName.Show()
			
			self.StatusBar = Bar() # Special Bar
			self.StatusBar.SetParent(self)
			self.StatusBar.SetWindowVerticalAlignBottom()
			self.StatusBar.SetSize(self.width,20)
			self.StatusBar.SetPosition(0,20)
			self.StatusBar.SetColor(COLOR_INACTIVE)
			self.StatusBar.AddFlag("not_pick")
			self.StatusBar.Show()
			
			self.StatusText = ui.TextLine()
			self.StatusText.SetParent(self.StatusBar)
			# self.StatusText.SetParent(self)
			self.StatusText.SetWindowHorizontalAlignCenter()
			self.StatusText.SetWindowVerticalAlignCenter()
			self.StatusText.SetHorizontalAlignCenter()
			self.StatusText.SetVerticalAlignCenter()
			self.StatusText.SetPosition(0,0)
			self.StatusText.SetText("Inaktiv")
			self.StatusText.Show()
			
			self.CloseBut = ui.Button()
			self.CloseBut.SetParent(self)
			self.CloseBut.SetUpVisual("d:/ymir work/ui/public/close_button_01.sub")
			self.CloseBut.SetOverVisual("d:/ymir work/ui/public/close_button_02.sub")
			self.CloseBut.SetDownVisual("d:/ymir work/ui/public/close_button_03.sub")
			self.CloseBut.SetToolTipText("Tab schliessen", 0, -23)
			self.CloseBut.SetEvent(self.DeleteMe)
			self.CloseBut.SetPosition(0,0)
			self.CloseBut.Show()
			
			self.OnMouseLeftButtonDown = lambda: self.Select()
			
			self.boni_active = 0
			
			self.bonusSelector = BonusSelector(self)
			self.bonusSelector.SetParentProxy(self.parentWindow.parentWindow)
			self.bonusSelector.SetPosition(10,35+36*3+4*2)
			self.bonusSelector.Hide()
			self.vnum = 0
			self.SetIndex(index)
			
			self.resetSwitch()

		def IsActive(self):
#			return self.boni_active == 1
			return False
			
		def SetParentProxy(self,parent):
			ui.Bar.SetParentProxy(self,parent)
		def Select(self):
			for a in self.parentWindow.tabList:
				self.parentWindow.tabList[a].UnSelect()
				self.parentWindow.tabList[a].bonusSelector.Hide()
			self.bonusSelector.Show()
			self.SetSize(self.width,self.height_selected)
			self.Update()
			# self.parentWindow.parentWindow.but_deactivate_all.SetParent(self.bonusSelector)
			# self.parentWindow.parentWindow.but_deactivate_all.SetPosition(415-10,200+10)
			# self.parentWindow.parentWindow.but_deactivate_all.Show()
			self.parentWindow.parentWindow.but_speed.SetParent(self.bonusSelector)
			self.parentWindow.parentWindow.but_speed.SetPosition(0,165+10)
			self.parentWindow.parentWindow.but_speed.Show()
			
			# self.parentWindow.parentWindow.help_stop_all.SetParent(self.bonusSelector)
			self.parentWindow.parentWindow.help_duration.SetParent(self.bonusSelector)
			
			
		def UnSelect(self):
			self.SetSize(self.width,self.height_unselected)
			self.Update()
			
		def Update(self):
			self.StatusBar.SetPosition(0,20)
			self.SetPosition((self.width+self.dist)*self.tabnum,0)
			self.SlotName.SetText("Slot %d" % (self.index+1))
			
		def resetSwitch(self):
			self.values = [0,0,0,0,0]
		
		def Switch(self):
			done = False

			ItemLevel = 0

			tchat(self.index)
			tchat(player.GetItemIndex(self.index))
			item.SelectItem(1, 2, player.GetItemIndex(self.index))

			for i in xrange(item.LIMIT_MAX_NUM):
				(limitType, limitValue) = item.GetLimit(i)

				if item.LIMIT_LEVEL == limitType:
					ItemLevel = limitValue
					break

			for i in range(0, player.INVENTORY_PAGE_X_SLOTCOUNT * player.INVENTORY_PAGE_SIZE):

				curItem = player.GetItemIndex(i)
				
				if curItem in SWITCH_VNUM:
					tchat("item[%d] is switcher" % curItem)
					if ItemLevel == 0 or (SWITCH_VNUM[curItem][0] <= ItemLevel and SWITCH_VNUM[curItem][1] >= ItemLevel):
						net.SendItemUseToItemPacket(i, self.index)
						return
					# tchat("ItemLEvel %d , %d >= , <= %d" % (ItemLevel, SWITCH_VNUM[curItem][0], SWITCH_VNUM[curItem][1]))

			done = True
			self.bonusSelector.Deactivate()
			chat.AppendChat(1, "No switchers left")
			
		def checkSwitch(self):
			ok = 0
			for i in range(0,5):
				if player.GetItemAttribute(self.index, i) != self.values[i]:
					ok = 1
			self.prob = self.GetProb()
			self.StatusText.SetText("Active (%d%%)" %self.prob)
			if ok == 1 or self.prob >= 90:
				if self.prob >= 90:
					chat.AppendChat(1,"Slot %d: done!" % (self.index+1))
					self.bonusSelector.Finish()
					return
				self.values  = [player.GetItemAttribute(self.index, i) for i in range(0,5)]
				self.Switch()
			elif ok == 0 and self.count < 5:
				self.count+=1
			elif ok == 0 and self.count >= 5:
				self.count = 0
				self.Switch()
			# elif self.last_switch > -1 and player.GetItemCount(self.last_switch) == 0:
			# chat.AppendChat(2,"%d"%player.GetItemCount(self.last_switch))
				# self.last_switch = 0
				# self.Switch()
			# else:
				# if self.GetProb() != 100:
					# self.Switch()
			pass

		def UpdateItem(self):
			# try:
			vnum = player.GetItemIndex(self.index)
			if vnum == 0 and self.vnum != 0:
				self.resetSwitch()
				self.vnum = 0
				self.bonusSelector.Deactivate()
				self.bonusSelector.Block()
				self.ItemIcon.Hide()
				if self.parentWindow.parentWindow.gameWindow != None:
					self.blockBar.SetSize(1)
				return
			elif vnum != self.vnum:
				self.resetSwitch()
				self.vnum = vnum
				self.bonusSelector.Deactivate()
				item.SelectItem(1, 2, self.vnum)
				if self.parentWindow.parentWindow.gameWindow != None:
					(w,h) = item.GetItemSize()
					self.blockBar.SetSize(h)
				
				if item.GetItemType() != 1 and item.GetItemType() != 2 and item.GetItemType() != item.ITEM_TYPE_TOTEM:
					self.bonusSelector.Block()
				else:
					self.bonusSelector.Unblock()
				
				
				self.ItemIcon.Show()
				self.ItemIcon.LoadImage(item.GetIconImageFileName())
				# self.values = [player.GetItemAttribute(self.index, i) for i in range(0,5)]
				return
			if self.IsActive():
				self.checkSwitch()
				
			# except:
				# pass
			
		def SetIndex(self,index):
			if self.index != 0:
				net.SendChatPacket("/switchbot_stop %d" % self.index)
			self.index = index
			self.bonusSelector.index = index
			self.bonusSelector.Starter.SetText("Switchen ("+str(index+1)+") starten")
			self.Update()
			self.UpdateItem()
			
		def GetProb(self):
			values = [player.GetItemAttribute(self.index, i) for i in range(0,5)]
			val2 = {}
			# for i in xrange(player.ATTRIBUTE_SLOT_MAX_NUM):
			for i in range(0,5):
				try:
					affectString = AFFECT_DICT[values[i][0]](values[i][1])
					val2[values[i][0]] = values[i][1]
					self.bonusSelector.ibi[i].SetText(affectString)
				except:
					pass
			prob = 0
			max  = 0
			yp = self.GenList()
			for x in yp:
				if yp[x] in val2 and val2[yp[x]] >= int(self.bonusSelector.boni[x][3].GetText()):
					prob = prob+1
				max = max+1
			if max > 0:
				prozent = 100/max*prob
			else:
				prozent = 100
			return prozent
			
		def GenList(self):
			ret = {}
			for i in range(0,5):
				if self.bonusSelector.boni[5-i][1].selected.value != 0:
					ret[5-i] = self.bonusSelector.boni[5-i][1].selected.value
			return ret

	def OnPressEscapeKey(self):
		tchat('esc6')
		# if done:
		self.parentWindow.Hide()
		# else:
		# 	self.parentWindow.PinShow(1)
		return True

	def __init__(self,parent):
		ui.Window.__init__(self)
		self.SetSize(500,36*3+4*2)
		self.tabCount = 0
		self.tabList = {}
		
		self.parentWindow = parent
		self.SetParent(parent)
		self.plusBar = ui.Bar()
		self.plusBar.SetParent(self)
		self.plusBar.SetSize(90,30)
		self.plusBar.SetWindowVerticalAlignCenter()
		self.plusBar.SetColor(COLOR_BG)
		# self.plusBar.OnMouseLeftButtonDown = lambda: self.AddTab_pre()
		self.plusBar.OnMouseLeftButtonUp = lambda: self.AddTab_pre()
		self.OnMouseLeftButtonUp = lambda: self.AddTab_pre()
		self.plusBar.SetPosition(30,0)
		self.plusBar.Show()
		
		self.AddText = ui.TextLine()
		self.AddText.SetParent(self.plusBar)
		self.AddText.SetText("Item hier platzieren")
		self.AddText.SetWindowVerticalAlignCenter()
		self.AddText.SetWindowHorizontalAlignCenter()
		self.AddText.SetVerticalAlignCenter()
		self.AddText.SetHorizontalAlignCenter()
		self.AddText.SetPosition(0,0)
		self.AddText.Show()
		
		dist = [
			[500,  0  ], #1
			[240, 10  ],
			[160, 10  ],
			[117, 10.5],
			# [ 80, 25  ], #5
			[ 92, 10  ], #5
			[ 75, 10  ], #6
			[ 64,  9  ], #7
			[ 56,  7.5], #8
			[ 50,  6.5], #9
			[ 45,  5.5], #10
		][MAX_NUM-1]
		self.ItemTab.width = dist[0]
		self.ItemTab.dist  = dist[1]

		
		#For 8
		# dist  = 9-1.5
		# width = 56
		
		# For 9
		# dist  = 9-2.5
		# width = 50
		
		# For 10
		# dist  = 9-3.5
		# width = 45
		
		
	def DeleteTab(self,id):
		if self.parentWindow.gameWindow != None:
			self.tabList[id].blockBar.Hide()
			self.tabList[id].blockBar.Destroy()
		self.tabList[id].Destroy()
		# del self.tabList[id]
		self.tabCount = self.tabCount -1 
		if self.tabCount > id and id < 5:
			for i in xrange(id,self.tabCount):
				self.tabList[i] = self.tabList[i+1] 
				self.tabList[i].tabnum = i
				self.tabList[i].SetPosition((self.tabList[i].width+self.tabList[i].dist)*i,0)
				
			del self.tabList[self.tabCount]
			
		else:
			del self.tabList[id]
			
		
		if self.tabCount > 0:
			self.tabList[0].Select()
		
		if (self.ItemTab.width+self.ItemTab.dist)*self.tabCount < 20:
			self.parentWindow.SetSize(520,387-210)
			self.parentWindow.but_speed.Hide()
			self.plusBar.SetPosition(20,0)
		else:
			(x,y) = self.tabList[self.tabCount-1].GetLocalPosition()
			self.plusBar.SetPosition(x+self.ItemTab.width+self.ItemTab.dist,0)
			# self.plusBar.SetPosition((self.ItemTab.width+self.ItemTab.dist)*self.tabCount-10,0)
		self.plusBar.Show()
		
	def AddTab_pre(self):
		if mouseModule.mouseController.isAttached():
			attachedSlotType = mouseModule.mouseController.GetAttachedType()
			attachedSlotPos = mouseModule.mouseController.GetAttachedSlotNumber()
			attachedSlotVnum = mouseModule.mouseController.GetAttachedItemIndex()
			
			item.SelectItem(1, 2, attachedSlotVnum)
			if item.GetItemType() != 1 and item.GetItemType() != 2 and item.GetItemType() != item.ITEM_TYPE_TOTEM:
				mouseModule.mouseController.DeattachObject()
				chat.AppendChat(2,"Can't switch this item.")
				return
			
			for a in self.tabList:
				if self.tabList[a].index == attachedSlotPos:
					mouseModule.mouseController.DeattachObject()
					chat.AppendChat(2,"Already used slot!")
					return
			
			if player.SLOT_TYPE_INVENTORY == attachedSlotType:
				self.AddTab(attachedSlotPos,attachedSlotVnum)
				chat.AppendChat(2,"Item added!")

			mouseModule.mouseController.DeattachObject()

	def AddTab(self,id,vnum = 0):
		if self.tabCount < MAX_NUM:
			self.tabList[self.tabCount] = self.ItemTab(self,self.tabCount,id,vnum)
			
			self.tabList[self.tabCount].Select()
			self.tabList[self.tabCount].Show()
			self.tabCount+= 1
			if (self.ItemTab.width+self.ItemTab.dist)*self.tabCount < 20:
				self.plusBar.SetPosition(20,0)
			else:
				(x,y) = self.tabList[self.tabCount-1].GetLocalPosition()
				self.plusBar.SetPosition(x+self.ItemTab.width+self.ItemTab.dist,0)
		
		if self.tabCount == MAX_NUM:
			self.plusBar.Hide()
			
		self.parentWindow.SetSize(520,357+10)
		self.parentWindow.but_speed.Show()
			# return 0

class SwitchBot(ui.BoardWithTitleBar):
	class PinGroup(ui.Bar):
		def OnUpdate(self):
			## Now check position.
			(x,y) = self.GetGlobalPosition()
			max_x = wndMgr.GetScreenWidth()-self.GetWidth()
			max_y = wndMgr.GetScreenHeight()-self.GetHeight()-DISTANCE_BOTTOM
			if not x == self.pos_x  or not y == self.pos_y:
				old_dir = self.dir
				if self.pos_x == 0 and not self.pos_y == 0 and not self.pos_y == max_y and old_dir != 1:
					self.parse_dir(1)
				elif self.pos_x == max_x and not self.pos_y == 0 and not self.pos_y == max_y and old_dir != 2:
					self.parse_dir(2)
				elif self.pos_y == max_y and not self.pos_x == 0 and not self.pos_x == max_x and old_dir != 4:
					self.parse_dir(4)
				elif self.pos_y == 0 and not self.pos_x == 0 and not self.pos_x == max_x and old_dir != 3:
					self.parse_dir(3)
					
				max_x = wndMgr.GetScreenWidth()-self.GetWidth()
				max_y = wndMgr.GetScreenHeight()-self.GetHeight()-DISTANCE_BOTTOM	
					
				
				if self.pos_x == 0 and not self.pos_y == 0 and not self.pos_y == max_y:
					x = 0
				elif self.pos_x == max_x and not self.pos_y == 0 and not self.pos_y == max_y:
					x = max_x
				elif self.pos_y == 0 and not self.pos_x == 0 and not self.pos_x == max_x:
					y = 0
				elif self.pos_y == max_y and not self.pos_x == 0 and not self.pos_x == max_x:
					y = max_y
				if x > 0 and x < max_x and y > 0 and y < max_y:
					if y < int(max_y/2):
						y = 0
					else:
						y = max_y
					
					if x < int(max_x/2):
						x = 0
					else:
						x = max_x
						
				
				x = min(max(0,x),wndMgr.GetScreenWidth()-self.GetWidth())
				y = min(max(0,y),wndMgr.GetScreenHeight()-self.GetHeight()-DISTANCE_BOTTOM)
				self.SetPosition(x,y)
				self.pos_x = x
				self.pos_y = y
			# (self.pos_x,self.pos_y) = self.GetGlobalPosition()
			self.parent.OnUpdate()
			for c in self.txtlist:
				c.SetColor(c.item.StatusBar.color)
				c.txt2.SetText("Status: %s" % c.item.StatusText.GetText())
				
		def ShowMainWindow(self):
			(x,y) = self.parent.GetGlobalPosition()
			x = min(max(32,x),wndMgr.GetScreenWidth()-self.parent.GetWidth()-32)
			y = min(max(32,y),wndMgr.GetScreenHeight()-self.parent.GetHeight()-DISTANCE_BOTTOM-32)
			self.parent.SetPosition(x,y)
			self.parent.SpecialPinShow()
			self.parent.PinGroupBox=None
			self.__del__()
		def parse_dir(self,dir):
			self.dir = dir
			w,h = 100,50
			for listWin in self.txtlist:
				itm = listWin.item
				listWin.AddFlag("not_pick")
				if dir >= 3:
					listWin.SetPosition(w,4)
					listWin.SetSize(90,h-8)
					w+=92
				else:
					listWin.SetPosition(0,h)
					listWin.SetSize(w,4+12+12+2)
					
					h+=4+12+12+4
			self.SetSize(w,h)
		
		def __init__(self,parent,dir = 1):
			self.parent = parent
			self.dir = dir
			ui.Bar.__init__(self)
			# Direction: 1 = left; 2 = right; 3 = top
			self.SetColor(COLOR_BG)
			w,h = 100,50
			
			self.AddFlag("float")
			self.AddFlag("movable")

			
			
			self.maximise_but = ui.Button()
			self.maximise_but.SetParent(self)
			self.maximise_but.SetPosition(4,4)
			self.maximise_but.SetUpVisual("d:/ymir work/ui/public/large_button_01.sub")
			self.maximise_but.SetOverVisual("d:/ymir work/ui/public/large_button_02.sub")
			self.maximise_but.SetDownVisual("d:/ymir work/ui/public/large_button_03.sub")
			self.maximise_but.SetText("Vergrössern")
			self.maximise_but.SetEvent(self.ShowMainWindow)
			self.maximise_but.Show()
			
			self.stop_but = ui.Button()
			self.stop_but.SetParent(self)
			self.stop_but.SetPosition(4,24)
			self.stop_but.SetUpVisual("d:/ymir work/ui/public/large_button_01.sub")
			self.stop_but.SetOverVisual("d:/ymir work/ui/public/large_button_02.sub")
			self.stop_but.SetDownVisual("d:/ymir work/ui/public/large_button_03.sub")
			self.stop_but.SetText("Alle Deaktivieren")
			self.stop_but.SetEvent(self.parent.deactivate_all)
			self.stop_but.Show()
			
			self.txtlist = []
			for a in self.parent.itemTabBar.tabList:
				itm = self.parent.itemTabBar.tabList[a]
				
				listWin = ui.Bar()
				listWin.item = itm
				self.txtlist.append(listWin)
				listWin.SetColor(itm.StatusBar.color)
				listWin.SetParent(self)
				listWin.AddFlag("not_pick")
				listWin.Show()
				
				listWin.txt1 = ui.TextLine()
				listWin.txt1.SetParent(listWin)
				listWin.txt1.SetText("Slot %d:" %(itm.index+1))
				listWin.txt1.Show()
				listWin.txt1.SetPosition(4,2)
				
				listWin.txt2 = ui.TextLine()
				listWin.txt2.SetParent(listWin)
				listWin.txt2.SetText("Status: %s" % itm.StatusText.GetText())
				listWin.txt2.SetPosition(4,2+12)
				listWin.txt2.Show()
				
				if dir >= 3:
					listWin.SetPosition(w,4)
					listWin.SetSize(90,h-8)
					w+=92
				else:
					listWin.SetPosition(0,h)
					listWin.SetSize(w,4+12+12+2)
					
					h+=4+12+12+4
				# else:
					
				# self.txtlist.append(itl)
			
			self.SetSize(w,h)
			(x,y) = self.parent.GetGlobalPosition()
			
			x = min(max(0,x),wndMgr.GetScreenWidth()-self.GetWidth())
			y = min(max(0,y),wndMgr.GetScreenHeight()-self.GetHeight()-DISTANCE_BOTTOM)
			if dir == 1:
				# self.SetWindowHorizontalAlignLeft()
				self.SetPosition(0,y)
			elif dir == 2:
				# self.SetWindowHorizontalAlignRight()
				self.SetPosition(wndMgr.GetScreenWidth()-self.GetWidth(),y)
			elif dir == 3:
				# self.SetWindowVerticalAlignTop()
				self.SetPosition(x,0)
			else:
				# self.SetWindowVerticalAlignBottom()
				self.SetPosition(x,wndMgr.GetScreenHeight()-(DISTANCE_BOTTOM+h))
				
			(self.pos_x,self.pos_y) = self.GetGlobalPosition()
				
			self.parse_dir(dir)
			# if dir == 1:
				# self.SetWindowHorizontalAlignLeft()
				# self.SetPosition(0,0)
			# elif dir == 2:
				# self.SetWindowHorizontalAlignRight()
				# self.SetPosition(self.GetWidth(),0)
			# elif dir == 3:
				# self.SetWindowHorizontalAlignCenter()
				# self.SetPosition(0,0)
			# elif dir == 4:
				# self.SetWindowHorizontalAlignCenter()
				# self.SetPosition(0,36+h)
			# else:
				# return # ERR
	
	pinhint = 0
	def ShowPinHint(self,type):
		self.pinhint = type
		if type == 0:
			self.PinHint.Hide()
			return
		# type=2
		
		(x,y) = self.GetGlobalPosition()
		if type == 1:  # Left
			self.PinHint.SetWindowHorizontalAlignLeft()
			self.PinHint.SetWindowVerticalAlignCenter()
			self.PinHint.SetSize(max(min(30,30-x),3),wndMgr.GetScreenHeight())
			self.PinHint.SetPosition(0,0)
		elif type == 2: # Right
			self.PinHint.SetWindowHorizontalAlignRight()
			self.PinHint.SetWindowVerticalAlignCenter()
			self.PinHint.SetSize(30,wndMgr.GetScreenHeight())
			self.PinHint.SetPosition(max(min(30,30-(wndMgr.GetScreenWidth()-(x+self.GetWidth()))),3),0)
		elif type == 3: # Top
			self.PinHint.SetWindowHorizontalAlignCenter()
			self.PinHint.SetWindowVerticalAlignTop()
			self.PinHint.SetSize(wndMgr.GetScreenWidth(),max(min(30,30-y),3))
			self.PinHint.SetPosition(0,0)
		elif type == 4: # Top
			self.PinHint.SetWindowHorizontalAlignCenter()
			self.PinHint.SetWindowVerticalAlignBottom()
			self.PinHint.SetSize(wndMgr.GetScreenWidth(),30)
			self.PinHint.SetPosition(0,36+max(min(30,30-(wndMgr.GetScreenHeight()-36-(y+self.GetHeight()))),3))
		self.PinHint.Show()
		# else:
			
	
	def Destroy(self):
		if self.PinGroupBox:
			self.PinGroupBox.Hide()
			del self.PinGroupBox

	def __init__(self):
		ui.BoardWithTitleBar.__init__(self)
		self.gameWindow = None
		
		self.SetTitleName("Switchbot")
		self.AddFlag("float")
		self.AddFlag("movable")
		self.SetPosition(30,30)
		# self.SetSize(520,387)
		# self.SetSize(520,387-210)
		self.SetSize(520,387-210)
		
		self.PinHint = ui.Bar()
		self.PinHint.SetColor(COLOR_PIN_HINT)
		self.PinHint.Show()
			
		self.PinGroupBox=None

		self.parentWnd.OnMouseLeftButtonDown = self.drag_start
		self.parentWnd.OnMouseLeftButtonUp   = self.drag_end
		
		self.titleBar.MinimizeBut = ui.Button()
		self.titleBar.MinimizeBut.SetParent(self.titleBar)
		self.titleBar.MinimizeBut.SetUpVisual("d:/ymir work/ui/public/minimize_button_01.sub")
		self.titleBar.MinimizeBut.SetOverVisual("d:/ymir work/ui/public/minimize_button_02.sub")
		self.titleBar.MinimizeBut.SetDownVisual("d:/ymir work/ui/public/minimize_button_03.sub")
		self.titleBar.MinimizeBut.SetToolTipText("Minimize", 0, -23)
		self.titleBar.MinimizeBut.SetPosition(520 - self.titleBar.btnClose.GetWidth()-3- 32 - 3, 3)
		self.titleBar.MinimizeBut.SetEvent(lambda: self.PinShow(1))
		self.titleBar.MinimizeBut.Show()
		
		self.titleBar.HelpBut = ui.ToggleButton()
		self.titleBar.HelpBut.SetParent(self.titleBar)
		self.titleBar.HelpBut.SetUpVisual("d:/ymir work/ui/public/small_button_01.sub")
		self.titleBar.HelpBut.SetOverVisual("d:/ymir work/ui/public/small_button_02.sub")
		self.titleBar.HelpBut.SetDownVisual("d:/ymir work/ui/public/small_button_03.sub")
		self.titleBar.HelpBut.SetToolTipText("Ausfuehrliche Hilfe", 0, -23)
		self.titleBar.HelpBut.SetText("Hilfe")
		self.titleBar.HelpBut.SetPosition(3, 0)
		self.titleBar.HelpBut.SetToggleDownEvent(lambda: self.ToggleHelp(1))
		self.titleBar.HelpBut.SetToggleUpEvent(lambda: self.ToggleHelp(0))
		self.titleBar.HelpBut.Hide()
		
		
		self.but_deactivate_all = ui.Button()
		# self.but_deactivate_all.SetParent(self)
		self.but_deactivate_all.SetParent(self.titleBar)
		# self.but_deactivate_all.SetPosition(415,350)
		self.but_deactivate_all.SetPosition(3+5+self.titleBar.HelpBut.GetWidth(), 0)
		self.but_deactivate_all.SetUpVisual("d:/ymir work/ui/public/large_button_01.sub")
		self.but_deactivate_all.SetOverVisual("d:/ymir work/ui/public/large_button_02.sub")
		self.but_deactivate_all.SetDownVisual("d:/ymir work/ui/public/large_button_03.sub")
		self.but_deactivate_all.SetText("Stop all")
		self.but_deactivate_all.SetEvent(self.deactivate_all)
		self.but_deactivate_all.Show()
		
		self.titleBar.but_deactivate_all = ui.Button()
		self.titleBar.but_deactivate_all.SetParent(self.titleBar)
		self.titleBar.but_deactivate_all.SetPosition(3+5+self.titleBar.HelpBut.GetWidth()+5+self.but_deactivate_all.GetWidth(), 0)
		self.titleBar.but_deactivate_all.SetUpVisual("d:/ymir work/ui/public/small_button_01.sub")
		self.titleBar.but_deactivate_all.SetOverVisual("d:/ymir work/ui/public/small_button_02.sub")
		self.titleBar.but_deactivate_all.SetDownVisual("d:/ymir work/ui/public/small_button_03.sub")
		self.titleBar.but_deactivate_all.SetText("Info")
		self.titleBar.but_deactivate_all.SetEvent(self.about)
		self.titleBar.but_deactivate_all.Show()
		self.titleName.SetPosition(60, 4)
		
		self.but_speed = ui.SliderBar()
		self.but_speed.SetParent(self)
		self.but_speed.SetWindowHorizontalAlignCenter()
		self.but_speed.SetPosition(0,310)
		# self.but_speed.SetToolTipText("Switch-Geschwindigkeit", 0, -23)
		# self.but_speed.Show()
		if constInfo.AUCTION_PREMIUM:
			self.but_speed.minVal = 150
			self.but_speed.curVal = 350
		else:
			self.but_speed.minVal = 400
			self.but_speed.curVal = 700
		self.but_speed.maxVal = 1500
		self.but_speed.SetEvent(self.__OnChangeSpeed)
		self.but_speed.SetSliderPos(1.0 - (self.but_speed.curVal - self.but_speed.minVal) / float(self.but_speed.maxVal - self.but_speed.minVal))
		self.but_speed.Hide()
		
		self.itemTabBar = ItemTabBar(self)
		self.itemTabBar.AddFlag("attach")
		self.itemTabBar.SetPosition(10,35)
		self.itemTabBar.Show()
		
		self.SetCloseEvent(self._Hide)
		
		self.Hide = self._Hide
		
		
		### NOW initialize the HELP stuff!
		
		self.help_add_item = HelpBar(0.8,'Drag an Drop an Item here.')
		self.help_add_item.SetParent(self)
		self.help_add_item.SetPosition(60,50)
		
		self.help_minimize = HelpBar(0.8,'Move the window to the side of the screen to minimize!',1)
		self.help_minimize.SetParent(self.titleBar)
		self.help_minimize.SetWindowHorizontalAlignCenter()
		self.help_minimize.SetPosition(100,-30)
		
		self.help_stop_all = HelpBar(0.8,'Stop everything!',1)
		self.help_stop_all.SetParent(self.titleBar)
		self.help_stop_all.SetPosition(3+5+self.titleBar.HelpBut.GetWidth()*1.2,-30)
		
		self.help_duration = HelpBar(0.8,'Slows the bot down.',1)
		self.help_duration.SetParent(self)

	def __OnChangeSpeed(self):
		pos = self.but_speed.GetSliderPos()
		curVal = int(self.but_speed.minVal + (self.but_speed.maxVal - self.but_speed.minVal) * (1.0 - pos))
		if curVal * 25 / 1000 != self.but_speed.curVal:
			self.but_speed.curVal = curVal
			tchat("switchspeedclient %d" % curVal)
			net.SendChatPacket("/switchbot_change_speed %d" % curVal)

	def OnPressEscapeKey(self):
		self.Close()
		return True
		
	def ToggleHelp(self,val):
		self.help_on = val
	
	def Show(self):
		if self.PinGroupBox:
			self.PinGroupBox.ShowMainWindow()
		else:
			self.SpecialPinShow()

	def SpecialPinShow(self):
		ui.BoardWithTitleBar.Show(self)
		self.bot_shown = 1
		
	def _Hide(self):
		## ONLY FOR TESTING
		# for a in range(0,self.itemTabBar.tabCount):
			# self.itemTabBar.DeleteTab(0)
		
		ui.BoardWithTitleBar.Hide(self)
		self.bot_shown = 0
		
		
	def deactivate_all(self):
		for a in self.itemTabBar.tabList:
			self.itemTabBar.tabList[a].bonusSelector.Deactivate()
			self.itemTabBar.tabList[a].bonusSelector.Starter.SetUp()
			self.itemTabBar.tabList[a].bonusSelector.Starter.OnToggleUp()
			net.SendChatPacket("/switchbot_stop %d" % self.itemTabBar.tabList[a].index)

	def GAME_OnEnd(self, slotIndex):
		for a in self.itemTabBar.tabList:
			if self.itemTabBar.tabList[a].index == int(slotIndex):
				self.itemTabBar.tabList[a].bonusSelector.Starter.SetUp()
				self.itemTabBar.tabList[a].bonusSelector.Deactivate()
				return

		import chat
		chat.AppendChat(chat.CHAT_TYPE_INFO, "ERR: cannot find slot idx %d" % int(slotIndex))

	def GAME_OnFinish(self, slotIndex):
		for a in self.itemTabBar.tabList:
			if self.itemTabBar.tabList[a].index == int(slotIndex):
				self.itemTabBar.tabList[a].bonusSelector.Starter.SetUp()
				self.itemTabBar.tabList[a].bonusSelector.Finish()
				return

		import chat
		chat.AppendChat(chat.CHAT_TYPE_INFO, "ERR2: cannot find slot idx %d" % int(slotIndex))
		
	drag = 0
	def drag_start(self):
		self.drag = 1
		
	def drag_end(self):
		self.drag = 0
		if self.pinhint > 0:
			self.PinShow(self.pinhint)
			# self.PinGroupBox = self.PinGroup()
			pass
		self.ShowPinHint(0)
		
	def PinShow(self,dir):
		self.PinGroupBox = self.PinGroup(self,dir)
		self.Hide()
		self.PinGroupBox.Show()
		
	def EnableInventoryTweak(self,gameWindow):
		self.gameWindow=gameWindow
		self.gameWindow.interface.wndInventory.inventoryTab[0].SetEvent(lambda arg=0: self.__SetInventoryPage(arg))
		self.gameWindow.interface.wndInventory.inventoryTab[1].SetEvent(lambda arg=1: self.__SetInventoryPage(arg))
		self.gameWindow.interface.wndInventory.inventoryTab[2].SetEvent(lambda arg=1: self.__SetInventoryPage(arg))
		self.gameWindow.interface.wndInventory.inventoryTab[3].SetEvent(lambda arg=1: self.__SetInventoryPage(arg))
		self.gameWindow.interface.wndInventory.inventoryTab[4].SetEvent(lambda arg=1: self.__SetInventoryPage(arg))
	def __SetInventoryPage(self,arg):
		self.gameWindow.interface.wndInventory.SetInventoryPage(arg)
		for a in self.itemTabBar.tabList:
			itm = self.itemTabBar.tabList[a]
			if itm.index >= arg*45 and itm.index < (arg+1)*45:
				itm.blockBar.Show()
			else:
				itm.blockBar.Hide()
	help_on = 0
	counter = 0
	AboutWindow = None
	def OnUpdate(self):
		if self.AboutWindow:
			if self.AboutWindow.x_counter > 1:
				self.AboutWindow.x_counter -=1
				self.AboutWindow.text6.SetText("Zeit: %0.1f" % (self.AboutWindow.x_counter/45.0))
			elif self.AboutWindow.x_counter == 1:
				self.AboutWindow.Hide()
				# self.AboutWindow.Delete()
				
		if self.help_on == 1:
			(x,y) = self.itemTabBar.plusBar.GetLocalPosition()
			self.help_add_item.SetPosition(x+20,50)
			self.help_add_item.Show()
			self.help_stop_all.Show()
			
			self.help_minimize.Show()
			if self.itemTabBar.tabCount > 0:
				# self.help_duration.SetPosition(300,180)
				self.help_duration.SetPosition(190-5.5+self.but_speed.GetSliderPos()*int(35.5+self.but_speed.GetWidth()/2),180)
				self.help_duration.Show()
				
			else:
				self.help_duration.Hide()
			
		else:
			self.help_add_item.Hide()
			self.help_minimize.Hide()
			self.help_stop_all.Hide()
			self.help_duration.Hide()
			
		if self.drag == 1:
			(x1, y1) = self.GetGlobalPosition()
			# if x1 < 0:
				# x1 = 0
			# elif x1 > wndMgr.GetScreenWidth()-520:
				# x1 = wndMgr.GetScreenWidth()-520
			# if y1 < 0:
				# y1 = 0
			# elif y1 > wndMgr.GetScreenHeight()-36-self.GetHeight():
				# y1 = wndMgr.GetScreenHeight()-36-self.GetHeight()
			x1 = max(min(wndMgr.GetScreenWidth()-520,x1),0)
			y1 = max(min(wndMgr.GetScreenHeight()-36-self.GetHeight(),y1),0)
			self.SetPosition(x1,y1)
			if x1 < 30:
				self.ShowPinHint(1)
			elif wndMgr.GetScreenWidth()-x1-520 < 30:
				self.ShowPinHint(2)
			elif y1 < 30:
				self.ShowPinHint(3)
			elif wndMgr.GetScreenHeight()-y1-self.GetHeight() < 60:
				self.ShowPinHint(4)
			else:
				self.ShowPinHint(0)
			# self.SetPosition(x1+(x-self.drag_pos[0]),y1)
			pass
		
		if self.gameWindow != None:
			for a in self.itemTabBar.tabList:
				itm = self.itemTabBar.tabList[a]
			
			
			
		self.counter+=1
		if self.counter >= int(self.but_speed.GetSliderPos()*MAX_SWITCH_DELAY_APPEND+MIN_SWITCH_DELAY):
			self.counter = 0
			for a in self.itemTabBar.tabList:
				itm = self.itemTabBar.tabList[a]
				itm.UpdateItem()
				# if itm.
				

	def about(self):
			
		self.AboutWindow = ui.ThinBoard()
		self.AboutWindow.SetParent(self)
		self.AboutWindow.SetSize(250,40)
		self.AboutWindow.SetWindowHorizontalAlignCenter()
		self.AboutWindow.SetWindowVerticalAlignCenter()
		self.AboutWindow.SetPosition(0,0)
		self.AboutWindow.Show()
		self.AboutWindow.x_counter = 450
		
		self.AboutWindow.text1 = ui.TextLine()
		self.AboutWindow.text1.SetParent(self.AboutWindow)
		self.AboutWindow.text1.SetWindowHorizontalAlignCenter()
		self.AboutWindow.text1.SetHorizontalAlignCenter()
		self.AboutWindow.text1.SetPosition(0,5)
		self.AboutWindow.text1.SetText("Switchbot base by Mijago, Serverside switching AE")
		self.AboutWindow.text1.SetPackedFontColor(ui.GenerateColor(58, 141, 221))
		self.AboutWindow.text1.Show()
		
		self.AboutWindow.text6 = ui.TextLine()
		self.AboutWindow.text6.SetParent(self.AboutWindow)
		self.AboutWindow.text6.SetPosition(200,18+13*5)
		self.AboutWindow.text6.SetText("Zeit: %d" % self.AboutWindow.x_counter)
		self.AboutWindow.text6.Show()
		
class HelpBar(ui.Window):
	def __init__(self,width,text,centered = 0):
		ui.Window.__init__(self)
		self.AddFlag("not_pick")
		self.AddFlag("attach")
		
		img = ui.ExpandedImageBox()
		
		img.SetParent(self)
		img.LoadImage("d:/ymir work/ui/pattern/help_stick.tga")
		img.SetRenderingRect(0.0, -width, 0.0, 0.0)
		img.Show()
		
		self.img = img
		
		txt = ui.TextLine()
		
		txt=ui.TextLine()
		txt.SetParent(self)
		txt.SetText(text)
		txt.Show()
		
		img.SetPosition(0,18-width*img.GetHeight())
		txt.SetPosition(0,0)
		txt.SetWindowHorizontalAlignCenter()
		if centered != 0:
			txt.SetHorizontalAlignCenter()
		# txt.SetPosition(0,0)
		
		self.txt = txt
	
class DropDown(ui.Window):
	dropped  = 0
	dropstat = 0
	last = 0
	lastS = 0
	maxh = 95
	OnChange = None
	OnChangeArg = None
	class Item(ui.ListBoxEx.Item):
		def __init__(self,parent, text,value=0,value2=0):
			ui.ListBoxEx.Item.__init__(self)

			self.textBox=ui.TextLine()
			self.textBox.SetParent(self)
			self.textBox.SetText(text)
			# self.textBox.SetLimitWidth(parent.GetWidth()-132)
			self.textBox.Show()
			self.value = value
			self.value2 = value2
		def GetValue(self):
			return self.value
		def GetValue2(self):
			return self.value2
		def __del__(self):
			ui.ListBoxEx.Item.__del__(self)
			
	def __init__(self,parent,tt = "",down=1):
		ui.Window.__init__(self,"TOP_MOST")
		self.down = down
		self.SetParentProxy(parent)
		self.bg = ui.Bar("TOP_MOST")
		self.bg.SetParent(self)
		self.bg.SetPosition(0,0)
		self.bg.SetColor(0xc0000000)
		self.bg.OnMouseOverIn = self.bgMouseIn
		self.bg.OnMouseOverOut = self.bgMouseOut
		self.bg.OnMouseLeftButtonDown = self.ExpandMe
		self.bg.Show()
		self.act = ui.TextLine()
		self.act.SetParent(self.bg)
		self.act.SetPosition(4,2)
		self.act.SetText(tt)
		self.act.Show()
		self.GetText = self.act.GetText
		
		self.Drop = ui.Bar("TOP_MOST")
		self.Drop.SetParent(self.GetParentProxy())
		self.Drop.SetPosition(0,21)
		# self.Drop.SetSize(150,95)
		self.Drop.SetSize(150,0)
		# self.Drop.SetColor(0xc00a0a0a)
		self.Drop.SetColor(0xff0a0a0a)
		
		
		self.ScrollBar = ui.ThinScrollBar()
		self.ScrollBar.SetParent(self.Drop)
		self.ScrollBar.SetPosition(132,0)
		# self.ScrollBar.SetScrollBarSize(95)
		self.ScrollBar.SetScrollBarSize(0)
		# self.ScrollBar.Show()
		
		self.DropList = ui.ListBoxEx()
		self.DropList.SetParent(self.Drop)
		self.DropList.itemHeight = 12
		self.DropList.itemStep = 13
		self.DropList.SetPosition(0,0)
		# self.DropList.SetSize(132,self.maxh)
		self.DropList.SetSize(132,13) 
		self.DropList.SetScrollBar(self.ScrollBar)
		self.DropList.SetSelectEvent(self.SetTitle)
		self.DropList.SetViewItemCount(0)
		self.DropList.Show()
		if tt != "":
			self.AppendItemAndSelect(tt)
		self.selected = self.DropList.GetSelectedItem()
		
			
		self.SetSize(120,20)
	def __del__(self): 
		ui.Window.__del__(self)
	c = 1
	def AppendItem(self,text,value=0,value2=0):
		self.c+=1   
		self.DropList.AppendItem(self.Item(self,text,value,value2))
		self.maxh = min(95,13*self.c)
		if self.c > 7:
			self.ScrollBar.Show()
			
		
	def AppendItemAndSelect(self,text,value=0,value2=0):
		self.DropList.AppendItem(self.Item(self,text,value,value2))
		self.DropList.SelectIndex(len(self.DropList.itemList)-1)
		
	def SelectByAffectId(self,id):
		for x in self.DropList.itemList:
			if x.value == id:
				self.DropList.SelectItem(x)
				break
				
	def SetTitle(self,item):
		self.act.SetText(str(item.textBox.GetText()))
		self.last = self.DropList.basePos
		self.lastS = self.ScrollBar.GetPos()
		self.dropped = 0
		self.selected = item
		if self.OnChange:
			apply(self.OnChange, self.OnChangeArg)
		# self.Drop.Hide()
		
	def SetPosition(self,w,h):
		ui.Window.SetPosition(self,w,h)
		if self.down == 1:
			self.Drop.SetPosition(w,h+21)
		else:
			self.Drop.SetPosition(w,h-self.Drop.GetHeight())
		
	def SetSize(self,w,h):
		ui.Window.SetSize(self,w,h)
		self.bg.SetSize(w,h)
		self.Drop.SetSize(w,0)
		self.DropList.SetSize(w-18,self.maxh)
		for x in self.DropList.itemList:
			x.SetSize(w-18,12)
		self.ScrollBar.SetPosition(w-18,0)
		
		
	def ExpandMe(self):
		if self.dropped == 1:
			# self.Drop.Hide()
			self.dropped = 0
		else:
			# self.Drop.Show()
			self.dropped = 1
			
	def OnUpdate(self):
		iter = 6
		if self.Drop.GetHeight() < 50:
			self.ScrollBar.Hide()
		else:
			self.ScrollBar.Show()
			
		if self.dropped == 0 and self.dropstat == 1:
			if self.Drop.GetHeight() <=0:
				self.dropstat = 0
				self.Drop.SetSize(self.Drop.GetWidth(),0)
				self.ScrollBar.SetScrollBarSize(self.Drop.GetHeight())
				self.Drop.Hide()
			else:
				if self.Drop.GetHeight()-iter < 0:
					self.Drop.SetSize(self.Drop.GetWidth(),0)
				else:
					self.Drop.SetSize(self.Drop.GetWidth(),self.Drop.GetHeight()-iter)
					(w,h) = self.GetLocalPosition()
					self.SetPosition(w,h)
						
					
				self.ScrollBar.SetScrollBarSize(self.Drop.GetHeight())
			self.DropList.SetViewItemCount(int(self.Drop.GetHeight()/13))
			self.DropList.SetBasePos(self.last+1)
			self.DropList.SetBasePos(self.last)
		elif self.dropped == 1 and self.dropstat == 0:
			self.Drop.Show()
			self.SetTop()
			if self.Drop.GetHeight() >=self.maxh:
				self.Drop.SetSize(self.Drop.GetWidth(),self.maxh)
				self.ScrollBar.SetScrollBarSize(self.maxh)
				self.dropstat = 1
				self.DropList.SetViewItemCount(7)
				self.ScrollBar.SetPos(self.lastS)
			else:
				self.ScrollBar.SetScrollBarSize(self.Drop.GetHeight()+iter)
				self.Drop.SetSize(self.Drop.GetWidth(),self.Drop.GetHeight()+iter)
				(w,h) = self.GetLocalPosition()
				self.SetPosition(w,h)
			self.DropList.SetViewItemCount(int(self.Drop.GetHeight()/13))
			self.DropList.SetBasePos(self.last+1)
			self.DropList.SetBasePos(self.last)
		
	## BG Hover
	def bgMouseIn(self):
		self.bg.SetColor(0xc00a0a0a)
	def bgMouseOut(self):
		self.bg.SetColor(0xc0000000)
		

class Edit2(ui.EditLine):
	def __init__(self,main = "",ml = 99):
		ui.EditLine.__init__(self)
		self.SetText(main)
		self.main = main
		self.SetMax(ml)
		self.SetUserMax(ml)
	def GetText(self):
		res = ui.EditLine.GetText(self)
		if res == "":
			return "0"
		else:
			return res
			
	def __del__(self):
		ui.EditLine.__del__(self)
	def OnSetFocus(self):
		ui.EditLine.OnSetFocus(self)
		if ui.EditLine.GetText(self) == self.main:
			self.SetText("")
	def OnKillFocus(self):
		ui.EditLine.OnKillFocus(self)
		if ui.EditLine.GetText(self) == "":
			self.SetText(self.main)
			

class CheckBox(ui.Window):
	checked = 0
	eventUp  =None
	eventDown=None
	def __init__(self,cont = ""):
		ui.Window.__init__(self)
		self.BG = ui.Bar("UI")
		self.BG.SetParent(self)
		self.BG.SetPosition(0,0)
		self.BG.SetSize(20,20)
		# self.BG.SetColor(0xc00b0b0b)
		self.BG.SetColor(COLOR_CHECKBOX_NOT_SELECTED)
		self.BG.OnMouseLeftButtonUp = self.Toggle
		self.OnMouseLeftButtonUp = self.Toggle
		self.BG.Show()
		self.Title = ui.TextLine()
		self.Title.SetParent(self)
		self.Title.SetPosition(25,2)
		self.Title.SetText(cont)
		self.Title.Show()
		self.stat = ui.TextLine()
		self.stat.SetParent(self.BG)
		self.stat.SetPosition(0,0)
		self.stat.SetWindowHorizontalAlignCenter()
		self.stat.SetWindowVerticalAlignCenter()
		self.stat.SetHorizontalAlignCenter()
		self.stat.SetVerticalAlignCenter()
		self.stat.SetSize(0,0)
		self.stat.SetText("")
		self.SetSize(25+self.Title.GetTextSize()[0]+5,20)
		self.stat.Show()
	def __del__(self):
		ui.ToggleButton.__del__(self)
	def Toggle(self):
		if self.checked == 1:
			self.OnToggleUp()
		else:
			self.OnToggleDown()
	def OnToggleUp(self):
		self.stat.SetText("")
		# self.BG.SetColor(0xc00b0b0b)
		self.BG.SetColor(COLOR_CHECKBOX_NOT_SELECTED)
		self.checked = 0
		if self.eventUp:
			self.eventUp()
	def OnToggleDown(self):
		# self.BG.SetColor(0xf00b0b0b)
		self.BG.SetColor(COLOR_CHECKBOX_SELECTED) 
		self.stat.SetText("X")
		self.checked = 1
		if self.eventDown:
			self.eventDown()
