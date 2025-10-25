"""
Created on Thu July 5 9:02:30 2018
Simple module holding classes for the Switchbot.
@author: .Various

Last modified: 04.08.2018
"""

# BUILTIN
import app
import net
import chat
import item
import time
import player
import wndMgr

# LOCAL
import ui
import utils
import constInfo
import localeInfo
import uiToolTip
import uiScriptLocale
from uiToolTip import ToolTip, GET_AFFECT_STRING
from mouseModule import mouseController as mc

SLOT_DEFAULT = "default"
SLOT_ACTIVE = "active"
SLOT_FINISHED = "finished"

STATE_TO_SLOT_DICT = {
	0: SLOT_ACTIVE,
	1: SLOT_DEFAULT,
	2: SLOT_FINISHED,
}

SLOT_TYPE_NORMAL = "slot_normal"
SLOT_TYPE_BIG = "slot_big"

SPEED_SLOW = 0
SPEED_MEDIUM = 1
SPEED_NORMAL = 2
SPEED_PREMIUM = 3

TIME_DEFAULT_STR = "00:00:00:00"

SPEED_DICT = {
	SPEED_SLOW : 1000, # in ms
	SPEED_MEDIUM : 700,
	SPEED_NORMAL : 400,
	SPEED_PREMIUM : 150,
}

class SwitchbotMinimizeWindow(ui.Bar):
	class Item(ui.Bar):
		def __init__(self, slot_index, state):
			ui.Bar.__init__(self)

			t = ui.TextLine()
			t.SetParent(self)
			t.SetPackedFontColor(0xFFFFFFFF)
			t.SetText("Slot-Index: %d" % slot_index)
			t.Show()
			self.text_slot_index = t

			t = ui.TextLine()
			t.SetParent(self)
			t.SetPackedFontColor(0xFFFFFFFF)
			t.SetText("Status: %s" % STATE_TO_SLOT_DICT[state])
			t.Show()
			self.text_state = t

		def __del__(self):
			ui.Bar.__del__(self)

		def SetSize(self, width, height):
			ui.Bar.SetSize(self, width, height)
			self.text_slot_index.SetWindowHorizontalAlignCenter()
			self.text_slot_index.SetHorizontalAlignCenter()
			self.text_slot_index.SetPosition(0, 2)
			self.text_state.SetWindowHorizontalAlignCenter()
			self.text_state.SetHorizontalAlignCenter()
			self.text_state.SetPosition(0, 16)

		def SetState(self, state):
			self.text_state.SetText("Status: %s" % STATE_TO_SLOT_DICT[state])

	WINDOW_BACKGROUND_COLOR = 0x77000000

	COLOR_ACTIVE = 0x77D16262
	COLOR_FINISHED = 0x7763D363
	COLOR_INACTIVE = 0x77777777

	INDEX_SLOT = 1
	INDEX_STATE = 2

	STATE_ACTIVE = 0
	STATE_INACTIVE = 1
	STATE_FINISHED = 2

	def __init__(self, layer="UI"):
		self._data = {}
		self._slots = {}
		self._event = None
		self._button_maximize = None

		ui.Bar.__init__(self, layer)

		self.AddFlag("movable")

		self._button_maximize = ui.Button()
		self._button_maximize.SetParent(self)
		self._button_maximize.SetUpVisual("d:/ymir work/ui/public/minimize_button_01.sub")
		self._button_maximize.SetOverVisual("d:/ymir work/ui/public/minimize_button_02.sub")
		self._button_maximize.SetDownVisual("d:/ymir work/ui/public/minimize_button_03.sub")
		self._button_maximize.SAFE_SetEvent(self.OnMaximize)
		self._button_maximize.Hide()

		self.SetColor(self.WINDOW_BACKGROUND_COLOR)
	def __del__(self):
		ui.Bar.__del__(self)

	def SetData(self, data):
		self._slots = {}
		self._data = data

		for slot, prop in data.iteritems():
			bar = self.Item(prop[self.INDEX_SLOT], prop[self.INDEX_STATE])
			bar.SetParent(self)
			bar.SetColor(self.__GetColorByProperty(prop))
			bar.SetSize(100, 50)
			bar.SetPosition(len(self._slots)*100, 0)
			bar.Hide()
			self._slots[slot] = bar
		self.SetSize(len(self._slots)*100 + 10 + self._button_maximize.GetWidth(), 50)
		self._button_maximize.SetPosition(self.GetWidth() - 5 - self._button_maximize.GetWidth(), 5)

	def Show(self):
		tchat("Show MinimizeWindow")
		ui.Bar.Show(self)
		self._button_maximize.Show()
		map(lambda x:x.Show(), self._slots.values())

	def Hide(self):
		tchat("Hide MinimizeWindow")
		if self._button_maximize:
			self._button_maximize.Hide()
			map(lambda x:x.Hide(), self._slots.values())
		ui.Bar.Hide(self)

	def SetMaximizeEvent(self, event):
		self._event = event

	def OnMaximize(self):
		if self._event:
			self.Hide()
			self._event()

	def OnUpdate(self):
		(x,y) = self.GetGlobalPosition()
		if x >= y:
			self.SetPosition(min(max(x, 0), wndMgr.GetScreenWidth() - self.GetWidth()), 0)
		else:
			self.SetPosition(0, min(max(y, 0), wndMgr.GetScreenHeight() - self.GetHeight() - 36))

		wSize = 0
		hSize = 0
		for slot, prop in self._data.iteritems():
			self._slots[slot].SetColor(self.__GetColorByProperty(prop))
			self._slots[slot].SetState(prop[self.INDEX_STATE])
			wSize = self._slots[slot].GetWidth()
			hSize = self._slots[slot].GetHeight()
			if x >= y:
				self._slots[slot].SetPosition(slot*self._slots[slot].GetWidth(), 0)
			else:
				self._slots[slot].SetPosition(0, slot * self._slots[slot].GetHeight())

		if x >= y:
			self.SetSize(10 + self._button_maximize.GetWidth() + wSize * len(self._slots), hSize)
		else:
			self.SetSize(10 + self._button_maximize.GetWidth() + wSize, hSize * len(self._slots))

		self._button_maximize.SetPosition(self.GetWidth() - 5 - self._button_maximize.GetWidth(), 5)

	def __GetColorByProperty(self, prop):
		if prop[self.INDEX_STATE] == self.STATE_ACTIVE:
			return self.COLOR_ACTIVE
		elif prop[self.INDEX_STATE] == self.STATE_FINISHED:
			return self.COLOR_FINISHED
		else:
			return self.COLOR_INACTIVE

class SwitchbotWindow(ui.ScriptWindow):

	MAX_SLOT_COUNT = 10

	INDEX_VNUM = 0
	INDEX_SLOT = 1
	INDEX_STATE = 2
	INDEX_START_TIME = 3
	INDEX_START_TIME_STR = 4
	INDEX_CONSUMPTION = 5
	INDEX_SPEED = 6
	INDEX_BONIS = 7
	INDEX_PREM_BONIS = 8

	STATE_ACTIVE = 0
	STATE_INACTIVE = 1
	STATE_FINISHED = 2

	SLOT_VISUAL_DEFAULT = "d:/ymir work/ui/switchbot/{}/slot_default_0{}.tga"
	SLOT_VISUAL_ACTIVE = "d:/ymir work/ui/switchbot/{}/slot_active_0{}.tga"
	SLOT_VISUAL_FINISHED = "d:/ymir work/ui/switchbot/{}/slot_finished_0{}.tga"
	SLOT_VISUAL_DISABLE = "d:/ymir work/ui/switchbot/slot_normal/slot_disabled.tga"

	ITEM_TYPES = {
		item.ITEM_TYPE_WEAPON : [-1],
		item.ITEM_TYPE_ARMOR : [item.ARMOR_BODY, item.ARMOR_HEAD, item.ARMOR_SHIELD, item.ARMOR_WRIST, item.ARMOR_FOOTS, item.ARMOR_NECK, item.ARMOR_EAR],
		item.ITEM_TYPE_COSTUME : [item.COSTUME_TYPE_BODY, item.COSTUME_TYPE_HAIR, item.COSTUME_TYPE_WEAPON],
		item.ITEM_TYPE_TOTEM : [-1],
	}

	TEMPLATE_LEFT_DICT = [
		# ("name", [[bindex1, bvalue1], [bindex2, bvalue2], ... [bindex5, bvalue5]],),
		(
			"PvM Armor",
			[[1, 2500], [23, 10], [34, 15], [36, 15], [53, 50]],
		),
		(
			"PvM Helmet",
			[[19, 20], [21, 20], [22, 20], [7, 8], [28, 15]],
		),
		(
			"PvM Necklace",
			[[1, 2500], [15, 10], [34, 15], [13, 8], [10, 20]],
		),
		(
			"PvM Bracelet",
			[[1, 2500], [23, 10], [16, 10], [21, 20], [22, 20]],
		),
		(
			"PvM Boots",
			[[1, 2500], [15, 10], [34, 15], [13, 8], [7, 8]],
		),
		(
			"PvM Shield",
			[[48, 1], [27, 10], [21, 20], [22, 20], []],
		),
		(
			"PvM Earrings",
			[[19, 20], [21, 20], [22, 20], [34, 15], [41, 10]],
		),
		(
			"OPVP Armor",
			[[1, 2500], [29, 15], [30, 15], [31, 15], [34, 15]],
		),
		(
			"OPVP Helmet",
			[[17, 10], [37, 15], [28, 15], [12, 8], [7, 8]],
		),
		(
			"OPVP Necklace",
			[[1, 2500], [29, 15], [30, 15], [31, 15], [34, 15]],
		),
		(
			"OPVP Bracelet",
			[[1, 2500], [17, 10], [16, 10], [37, 15], []],
		),
		(
			"OPVP Earrings",
			[[17, 10], [29, 15], [30, 15], [31, 15], [34, 15]],
		),
		(
			"OPVP Boots",
			[[1, 2500], [29, 15], [30, 15], [31, 15], [34, 15]],
		),
		(
			"OPVP Shield",
			[[48, 1], [17, 10], [27, 10], [], []],
		),
		(
			"OPVP Weapon",
			[[17, 10], [15, 10], [16, 10], [9, 20], []],
		),
	]

	TEMPLATE_RIGHT_DICT = [
		# ("name", [[bindex1, bvalue1], [bindex2, bvalue2], ... [bindex5, bvalue5]],),
		(
			"PvM Armor",
			[[1, 2500], [23, 10], [34, 15], [36, 15], [53, 50]],
		),
		(
			"PvM Helmet",
			[[19, 20], [21, 20], [22, 20], [7, 8], [28, 15]],
		),
		(
			"PvM Necklace",
			[[1, 2500], [15, 10], [34, 15], [13, 8], [10, 20]],
		),
		(
			"PvM Bracelet",
			[[1, 2500], [23, 10], [16, 10], [21, 20], [22, 20]],
		),
		(
			"PvM Boots",
			[[1, 2500], [15, 10], [34, 15], [13, 8], [7, 8]],
		),
		(
			"PvM Shield",
			[[48, 1], [27, 10], [21, 20], [22, 20], []],
		),
		(
			"PvM Earrings",
			[[19, 20], [21, 20], [22, 20], [34, 15], [41, 10]],
		),
		(
			"OPVP Armor",
			[[1, 2500], [29, 15], [30, 15], [31, 15], [34, 15]],
		),
		(
			"OPVP Helmet",
			[[17, 10], [37, 15], [28, 15], [12, 8], [7, 8]],
		),
		(
			"OPVP Necklace",
			[[1, 2500], [29, 15], [30, 15], [31, 15], [34, 15]],
		),
		(
			"OPVP Bracelet",
			[[1, 2500], [17, 10], [16, 10], [37, 15], []],
		),
		(
			"OPVP Earrings",
			[[17, 10], [29, 15], [30, 15], [31, 15], [34, 15]],
		),
		(
			"OPVP Boots",
			[[1, 2500], [29, 15], [30, 15], [31, 15], [34, 15]],
		),
		(
			"OPVP Shield",
			[[48, 1], [17, 10], [27, 10], [], []],
		),
		(
			"OPVP Weapon",
			[[17, 10], [15, 10], [16, 10], [9, 20], []],
		),
	]

	def __init__(self):
		ui.ScriptWindow.__init__(self)
		self.__Initialize()
		self.__LoadWindow()

	def __del__(self):
		ui.ScriptWindow.__del__(self)

	##########################################################
	### --------------------- PRIVATE -------------------- ###
	##########################################################
	def __Initialize(self):
		"""
			Creates all needed class variables.
		"""
		# The data-dict is holding every item and the needed
		# properties like inventory-slot_index, etc.
		# For more details see - Append - method.
		self._data = {}
		
		# Contains the slot-buttons
		self._slots = []

		# Current selected slot
		self._selected_slot = -1

		# Contains speed-radio-buttons
		self._speed_selection = []

		# Current selected Speed
		self._speed = SPEED_NORMAL

		self.take_input_once = False

		self.wndSwitchbotMinimize = None

	def __LoadWindow(self):
		"""
			Loads the uiscript-file of the window. This method should
			only be called once.
		"""
		try:
			script_loader = ui.PythonScriptLoader()
			script_loader.LoadScriptFile(self, "uiscript/switchbotwindow.py")
		except:
			import exception
			exception.Abort("SwitchbotWindow.__LoadWindow.LoadObject")
		
		self.GetChild("bg_default").Hide()
		self.GetChild("titlebar").SetCloseEvent(self.Close)
		self.GetChild("start_button").SAFE_SetEvent(self.OnStart)
		self.GetChild("reset_button").SAFE_SetEvent(self.OnReset)
		self.GetChild("delete_button").SAFE_SetEvent(self.OnDelete)
		self.GetChild("minimize_button").SAFE_SetEvent(self.OnMinimize)

		for type, name in enumerate(["slow", "medium", "normal", "premium"]):
			btn = self.GetChild("speed_{}_button".format(name))
			btn.SAFE_SetEvent(self.__SelectSpeed, type)
			if name == "premium" and __SERVER__ == 2:
				btn_text = self.GetChild("speed_premium_select_text")
				btn_text.SetText(localeInfo.SWITCHBOT_SPEED_PREMIUM_ELONIA)
			self._speed_selection.append(btn)
		self.__SelectSpeed(SPEED_NORMAL)

		# Disable premium-features
		if not constInfo.AUCTION_PREMIUM:
			self._speed_selection[SPEED_PREMIUM].Disable()
			self.GetChild("premium_section_bg").LoadImage("d:/ymir work/ui/switchbot/premium_inactive.tga")

			# apply premium tooltip as info
			tooltip = ToolTip()
			tooltip.HideToolTip()
			tooltip.AppendDescription(localeInfo.CHAT_COLOR_PREMIUM_INFO, 26)

			self.GetChild("premium_info").SetToolTipWindow(tooltip)
		else:
			self.GetChild("premium_info").Hide()

		# Create slot-buttons with default look
		for i in xrange(self.MAX_SLOT_COUNT):
			btn = ui.Button()
			btn.SetParent(self)
			btn.SetUpVisual(self.SLOT_VISUAL_DEFAULT.format(SLOT_TYPE_NORMAL, 1))
			btn.SetOverVisual(self.SLOT_VISUAL_DEFAULT.format(SLOT_TYPE_NORMAL, 2))
			btn.SetDownVisual(self.SLOT_VISUAL_DEFAULT.format(SLOT_TYPE_NORMAL, 3))
			btn.SetDisableVisual(self.SLOT_VISUAL_DISABLE)
			btn.SetText(uiScriptLocale.SWITCHBOT_SLOT_NAME % (i+1))
			btn.SAFE_SetEvent(self.__Select, i)
			btn.SetPosition(39 + (i*54), 39)
			btn.Disable()
			btn.Show()
			self._slots.append(btn)

		self.GetChild("dropdown_01").SetIndex(0)
		self.GetChild("dropdown_02").SetIndex(1)
		self.GetChild("dropdown_03").SetIndex(2)
		self.GetChild("dropdown_04").SetIndex(3)
		self.GetChild("dropdown_04").SetOpenEvent(self.__HideTemplateByDropdown)
		self.GetChild("dropdown_04").SetCloseEvent(self.__ShowTemplateByDropdown)
		self.GetChild("dropdown_05").SetIndex(4)
		self.GetChild("dropdown_05").SetOpenEvent(self.__HideTemplateByDropdown)
		self.GetChild("dropdown_05").SetCloseEvent(self.__ShowTemplateByDropdown)

		self.GetChild("prem_dropdown_01").SetIndex(5)
		self.GetChild("prem_dropdown_02").SetIndex(6)
		self.GetChild("prem_dropdown_03").SetIndex(7)
		self.GetChild("prem_dropdown_04").SetIndex(8)
		self.GetChild("prem_dropdown_04").SetOpenEvent(self.__HidePremiumTemplateByDropdown)
		self.GetChild("prem_dropdown_04").SetCloseEvent(self.__ShowPremiumTemplateByDropdown)
		self.GetChild("prem_dropdown_05").SetIndex(9)
		self.GetChild("prem_dropdown_05").SetOpenEvent(self.__HidePremiumTemplateByDropdown)
		self.GetChild("prem_dropdown_05").SetCloseEvent(self.__ShowPremiumTemplateByDropdown)

		for i in xrange(player.NORMAL_ATTRIBUTE_SLOT_MAX_NUM):
			# inputs
			self.GetChild("input_0{}".format(i+1)).SetUpdateEvent(lambda x=i: self.__OnChangeInput(x))
			self.GetChild("input_0{}".format(i+1)).SetEscapeEvent(self.OnPressEscapeKeyInput, None)

			self.GetChild("prem_input_0{}".format(i+1)).SetUpdateEvent(lambda x=i+5: self.__OnChangeInput(x))
			self.GetChild("prem_input_0{}".format(i+1)).SetEscapeEvent(self.OnPressEscapeKeyInput, None)

			# dropdowns
			dd = self.GetChild("dropdown_0{}".format(i+1))
			prem_dd = self.GetChild("prem_dropdown_0{}".format(i+1))

			dd.Append(uiScriptLocale.SWITCHBOT_SELECT_DEFAULT, -1, -1)
			prem_dd.Append(uiScriptLocale.SWITCHBOT_SELECT_DEFAULT, -1, -1)

			boni_list = []
			for item_type in self.ITEM_TYPES:
				for item_subtype in self.ITEM_TYPES[item_type]:
					for i in xrange(item.GetAttributeCountByItemType(item_type, item_subtype)):
						attr_type, attr_value = item.GetAttributeInfoByItemType(item_type, item_subtype, i)
						if attr_type in boni_list:
							continue
						elif attr_type == 0:
							continue
						boni_list.append(attr_type)
						attr_str = str(GET_AFFECT_STRING(attr_type, attr_value))
						dd.Append(attr_str, attr_type, attr_value)
						prem_dd.Append(attr_str, attr_type, attr_value)

			dd.Append(str(GET_AFFECT_STRING(item.APPLY_NORMAL_HIT_DAMAGE_BONUS,0)),item.APPLY_NORMAL_HIT_DAMAGE_BONUS,0)
			dd.Append(str(GET_AFFECT_STRING(item.APPLY_SKILL_DAMAGE_BONUS,0)),item.APPLY_SKILL_DAMAGE_BONUS,0)

			prem_dd.Append(str(GET_AFFECT_STRING(item.APPLY_NORMAL_HIT_DAMAGE_BONUS,0)),item.APPLY_NORMAL_HIT_DAMAGE_BONUS,0)
			prem_dd.Append(str(GET_AFFECT_STRING(item.APPLY_SKILL_DAMAGE_BONUS,0)),item.APPLY_SKILL_DAMAGE_BONUS,0)

			dd.SetSelectEvent(self.__SelectBonus)
			prem_dd.SetSelectEvent(self.__SelectBonus)

		self.templates = []
		x, y = self.GetGlobalPosition()

		t1 = ui.TextDropdown()
		t1.AddFlag("float")
		t1.Create(195, 24, 15)
		t1.SetViewItemCount(6)
		t1.SetDefaultText(uiScriptLocale.SWITCHBOT_TEMPLATE_TITLE)
		t1.SetSelectEvent(self.__SelectTemplate)
		for t in self.TEMPLATE_LEFT_DICT:
			t1.Append(t[0], t[1])
		t1.Hide()

		t2 = ui.TextDropdown()
		t2.AddFlag("float")
		t2.Create(195, 24, 15)
		t2.SetViewItemCount(6)
		t2.SetDefaultText(uiScriptLocale.SWITCHBOT_TEMPLATE_TITLE)
		t2.SetSelectEvent(self.__SelectPremiumTemplate)
		for t in self.TEMPLATE_RIGHT_DICT:
			t2.Append(t[0], t[1])
		t2.Hide()

		self.templates.append(t1)
		self.templates.append(t2)
	
		self.__Disable()

		self.wndSwitchbotMinimize = SwitchbotMinimizeWindow()
		self.wndSwitchbotMinimize.SetMaximizeEvent(self.Open)
		self.wndSwitchbotMinimize.Hide()

	def __Append(self, islot_index):
		"""
			Inserts a item and all the other relevant properties
			into the data-dict of the switchbot.

			Parameters
			----------
			islot_index: int
				Inventory slot index.
		"""
		if self.__IsAlreadyAttached(islot_index):
			self.__Notify(uiScriptLocale.SWITCHBOT_ALREADY_ATTACHED)
			self.__Select(self.__GetSlotByInventoryIndex(islot_index))
		else:
			slot = self.__GetEmptySlot()

			if slot is None:
				self.__Notify(uiScriptLocale.SWITCHBOT_MAXIMUM_SLOT_REACHED)
				return

			# set default properties
			properties = {}
			properties[self.INDEX_VNUM] = player.GetItemIndex(islot_index)
			properties[self.INDEX_SLOT] = islot_index
			properties[self.INDEX_STATE] = self.STATE_INACTIVE
			properties[self.INDEX_START_TIME] = 0
			properties[self.INDEX_CONSUMPTION] = 0
			properties[self.INDEX_SPEED] = SPEED_NORMAL
			properties[self.INDEX_START_TIME_STR] = TIME_DEFAULT_STR
			properties[self.INDEX_BONIS] = [[],[],[],[],[]]
			properties[self.INDEX_PREM_BONIS] = [[],[],[],[],[]]

			# Append and select the new slot
			self._data[slot] = properties
			self._slots[slot].Enable()
			self.__Select(slot)

	def __GetEmptySlot(self):
		if len(self._data) >= self.MAX_SLOT_COUNT:
			return None
		
		for i in range(self.MAX_SLOT_COUNT):
			if i not in self._data:
				return i

		return None

	def __FindNextSlot(self):
		if len(self._data) == 0:
			return -1
		
		for i in range(self.MAX_SLOT_COUNT):
			if i in self._data:
				return i

		return -1

	def __IsAlreadyAttached(self, islot_index):
		"""
			Checks whether an item is already attached to the
			switchbot or not.

			Returns
			-------
			bool
				True if the item is already attached, otherwise False
		"""
		for _, prop in self._data.iteritems():
			if islot_index == prop[self.INDEX_SLOT]:
				return True
		return False
	
	def __GetSlotByInventoryIndex(self, islot_index):
		"""
			Gets a switchbot slot by an inventory slot, if exist.

			Returns
			-------
			int
				Switchbot slot, if exist, otherwise -1
		"""
		for slot, prop in self._data.iteritems():
			if islot_index == prop[self.INDEX_SLOT]:
				return slot
		return -1

	def __Select(self, slot):
		"""
			Selects a specific slot and calls changes the
			gui representation.

			Parameters
			----------
			slot: int
				Slot that should be selected (not inventory-slot!).
		"""
		if slot == self._selected_slot:
			return

		prop = self._data.get(slot, None)

		if not prop:
			return

		self.__ChangeSlot(slot)

		self._selected_slot = slot

		item.SelectItem(1, 2, prop[self.INDEX_VNUM])

		img = self.GetChild("icon")
		img.LoadImage(item.GetIconImageFileName())

		_, height = item.GetItemSize()
		height *= 32

		img.SetPosition(49 + 15, 85 + (100 - height)/2)

		self.__RefreshCurrentSlot()

		self.take_input_once = True
		for i, d in enumerate(prop[self.INDEX_BONIS]):
			dd = self.GetChild("dropdown_0{}".format(i+1))
			self.GetChild("input_0{}".format(i+1)).KillFocus()
			if d:
				dd.SelectItemByArg(0, d[0])
			else:
				dd.SelectItemByArg(0, -1)

		for i, d in enumerate(prop[self.INDEX_PREM_BONIS]):
			dd = self.GetChild("prem_dropdown_0{}".format(i+1))
			self.GetChild("prem_input_0{}".format(i+1)).KillFocus()
			if d:
				dd.SelectItemByArg(0, d[0])
			else:
				dd.SelectItemByArg(0, -1)
		self.take_input_once = False

		self.GetChild("consumption").SetText(str(prop[self.INDEX_CONSUMPTION]))

	def __RefreshCurrentSlot(self):
		prop = self._data.get(self._selected_slot, None)

		if not prop:
			return

		self.GetChild("starttime").SetText("{}".format(prop[self.INDEX_START_TIME_STR]))

		if prop[self.INDEX_START_TIME] == 0:
			self.GetChild("alltime").SetText(TIME_DEFAULT_STR)

		if prop[self.INDEX_STATE] == self.STATE_ACTIVE:
			self.GetChild("start_button").SetText(uiScriptLocale.SWITCHBOT_BUTTON_STOP)
			self.GetChild("start_button").SAFE_SetEvent(self.OnStop)
			self.__Disable()
		else:
			self.GetChild("start_button").SetText(uiScriptLocale.SWITCHBOT_BUTTON_START)
			self.GetChild("start_button").SAFE_SetEvent(self.OnStart)
			self.__Enable()

		self.__ChangeSlot(self._selected_slot)

	def __ChangeSlot(self, slot):
		"""
			Resets the visuals of the old slot,
			sets the visuals of the new slot.

			Parameters
			----------
			slot: int
				The new selected slot.
		"""
		# OLD_SLOT
		if self._selected_slot != -1:
			old_slot = self._slots[self._selected_slot]
			old_slot.SetPosition(39 + (self._selected_slot*54), 39)

			prop = self._data.get(self._selected_slot, None)
			if prop is not None:
				state = prop[self.INDEX_STATE]
				self.__MakeButtonVisual(old_slot, STATE_TO_SLOT_DICT[state], SLOT_TYPE_NORMAL)
			else:
				self.__MakeButtonVisual(old_slot, SLOT_DEFAULT, SLOT_TYPE_NORMAL)
	
		# NEW_SLOT
		if slot != -1:
			new_slot = self._slots[slot]
			new_slot.SetPosition(39 + (slot*54), 35)

			prop = self._data.get(slot, None)
			if prop is not None:
				state = prop[self.INDEX_STATE]
				self.__MakeButtonVisual(new_slot, STATE_TO_SLOT_DICT[state], SLOT_TYPE_BIG)
			else:
				self.__MakeButtonVisual(new_slot, SLOT_DEFAULT, SLOT_TYPE_BIG)
	

	def __MakeButtonVisual(self, btn, type=SLOT_ACTIVE, subtype=SLOT_TYPE_NORMAL):
		"""
			Updates the button-visuals by a given type and subtype.

			Parameters
			----------
			btn: Window.Button
				The Button which should be changed.
			
			type: int
				The Type of the button (default, active or finished)
			
			subtype: int
				The Subtype of the button (normal, big)
		"""
		if type == SLOT_DEFAULT:
			btn.SetUpVisual(self.SLOT_VISUAL_DEFAULT.format(subtype, 1))
			btn.SetOverVisual(self.SLOT_VISUAL_DEFAULT.format(subtype, 2))
			btn.SetDownVisual(self.SLOT_VISUAL_DEFAULT.format(subtype, 3))
		elif type == SLOT_ACTIVE:
			btn.SetUpVisual(self.SLOT_VISUAL_ACTIVE.format(subtype, 1))
			btn.SetOverVisual(self.SLOT_VISUAL_ACTIVE.format(subtype, 2))
			btn.SetDownVisual(self.SLOT_VISUAL_ACTIVE.format(subtype, 3))
		elif type == SLOT_FINISHED:
			btn.SetUpVisual(self.SLOT_VISUAL_FINISHED.format(subtype, 1))
			btn.SetOverVisual(self.SLOT_VISUAL_FINISHED.format(subtype, 2))
			btn.SetDownVisual(self.SLOT_VISUAL_FINISHED.format(subtype, 3))

	def __Notify(self, msg):
		"""
			Prints a message to the chat.

			Parameters
			----------
			msg: str
				Message that should be printed out.
		"""
		chat.AppendChat(chat.CHAT_TYPE_INFO, msg)

	def __IsSwitchableItemAttached(self):
		"""
			Checks whether an item is attached and is switchable.

			Returns
			-------
			bool
				True if the item is attached and the item is switchable,
				otherwise False
		"""
		if not mc.isAttached():
			return False
		
		if mc.GetAttachedType() != player.SLOT_TYPE_INVENTORY:
			return False
		
		item_vnum = mc.GetAttachedItemIndex()
		return utils.ItemIsSwitchable(item_vnum)

	def __ShowContent(self):
		for slot in self._slots:
			slot.Show()
		for t in self.templates:
			t.Show()
		self.GetChild("icon").Show()

	def __HideContent(self):
		for slot in self._slots:
			slot.Hide()
		for t in self.templates:
			t.Hide()
		self.GetChild("icon").Hide()

	def __SelectSpeed(self, type):
		map(lambda x: x.SetUp(), self._speed_selection)
		self._speed_selection[type].SetDown()
		self._speed = type
		self.GetChild("speed").SetText("{}ms".format(SPEED_DICT[type]))

		if not constInfo.AUCTION_PREMIUM:
			self._speed_selection[SPEED_PREMIUM].Enable()
			self._speed_selection[SPEED_PREMIUM].Disable()
		net.SendChatPacket("/switchbot_change_speed {}".format(SPEED_DICT[type]))

	def __ClearInfo(self):
		self.OnReset()
		self.GetChild("icon").LoadImage("d:/ymir work/ui/switchbot/empty.tga")

	def __OnChangeInput(self, index):
		tchat("__OnChangeInput {}".format(index))
		prop = self._data.get(self._selected_slot, None)
		if prop is not None:
			prop_index = self.INDEX_BONIS
			if index in range(5, 10):
				prop_index = self.INDEX_PREM_BONIS
				index -= 5

			if prop[prop_index][index]:
				value = self.GetChild("input_0{}".format(index+1)).GetText()
				if prop_index == self.INDEX_PREM_BONIS:
					value = self.GetChild("prem_input_0{}".format(index+1)).GetText()

				if not value:
					value = "0"
				prop[prop_index][index][1] = int(value)

	def __SelectBonus(self, dropdown, item):
		index = dropdown.GetIndex()
		bonus, value = item.GetArgs()
		tchat("__SelectBonus: {} -> ({}, {})".format(index, bonus, value))

		prop = self._data.get(self._selected_slot, None)
		if prop is not None:

			prop_index = self.INDEX_BONIS
			if index in range(5, 10):
				prop_index = self.INDEX_PREM_BONIS
				index -= 5

			if self.take_input_once and prop[prop_index][index]:
				value = prop[prop_index][index][1]

			if value == -1:
				if prop_index == self.INDEX_PREM_BONIS:
					tchat("prem_input_0{} -> {}".format(index+1, ""))
					self.GetChild("prem_input_0{}".format(index+1)).SetText("")
				else:
					self.GetChild("input_0{}".format(index+1)).SetText("")
			else:
				if prop_index == self.INDEX_PREM_BONIS:
					tchat("prem_input_0{} -> {}".format(index+1, value))
					self.GetChild("prem_input_0{}".format(index+1)).SetText(str(value))
				else:
					self.GetChild("input_0{}".format(index+1)).SetText(str(value))
			
			dropdown.SetDefaultText(item.GetText())
			if dropdown.IsOpen():
				dropdown.Toggle()
		
			if value == -1:
				prop[prop_index][index] = []
			else:
				prop[prop_index][index] = [bonus, value]

	def __Enable(self):
		for i in xrange(player.NORMAL_ATTRIBUTE_SLOT_MAX_NUM):
			#self.GetChild("input_0{}".format(i+1)).Enable()
			self.GetChild("dropdown_0{}".format(i+1)).Enable()
			if constInfo.AUCTION_PREMIUM:
				self.GetChild("prem_dropdown_0{}".format(i+1)).Enable()
		for t in self.templates:
			t.Enable()

		if not constInfo.AUCTION_PREMIUM:
			self.templates[1].Disable()

	def __Disable(self):
		for i in xrange(player.NORMAL_ATTRIBUTE_SLOT_MAX_NUM):
			#self.GetChild("input_0{}".format(i+1)).Disable()
			self.GetChild("dropdown_0{}".format(i+1)).Disable()
			self.GetChild("prem_dropdown_0{}".format(i+1)).Disable()
		for t in self.templates:
			t.Disable()

	def __SelectTemplate(self, dropdown, item):
		data = item.GetArgs()[0]

		for i, boni in enumerate(data):
			if boni:
				type = boni[0]
			else:
				type = -1

			self.GetChild("dropdown_0{}".format(i+1)).SelectItemByArg(0, type)

		dropdown.Toggle()

	def __SelectPremiumTemplate(self, dropdown, item):
		data = item.GetArgs()[0]

		for i, boni in enumerate(data):
			if boni:
				type = boni[0]
			else:
				type = -1

			self.GetChild("prem_dropdown_0{}".format(i+1)).SelectItemByArg(0, type)

		dropdown.Toggle()

	def __HidePremiumTemplateByDropdown(self):
		self.templates[1].Hide()

	def __ShowPremiumTemplateByDropdown(self):
		self.templates[1].Show()

	def __HideTemplateByDropdown(self):
		self.templates[0].Hide()

	def __ShowTemplateByDropdown(self):
		self.templates[0].Show()


	##########################################################
	### --------------------- PUBLIC --------------------- ###
	##########################################################
	def Destroy(self):
		"""
			'Destroys' the object by clearing the 
			element-dictionary and deletes all class-variables.
		"""
		if self.IsShow():
			self.Close()
			for btn in self._slots:
				btn.Hide()

		del self._data
		del self._slots[:]
		del self._slots
		del self._selected_slot
		del self._speed_selection[:]
		del self._speed_selection
		del self._speed

		self.ClearDictionary()

	def Open(self):
		"""
			Makes the switchbot gui visible.
		"""
		self.SetTop()
		self.Show()

		for t in self.templates:
			t.Show()
			t.SetTop()

	def Close(self):
		"""
			Makes the switchbot gui invisible.
		"""
		self.Hide()

		for t in self.templates:
			t.Hide()

	def OnStart(self):
		prop = self._data.get(self._selected_slot, None)
		if not prop:
			return

		data = ""
		for d in prop[self.INDEX_BONIS]:
			if d:
				data += "{} {} ".format(d[0], d[1])

		prem_data = ""
		for d in prop[self.INDEX_PREM_BONIS]:
			if d:
				prem_data += "{} {} ".format(d[0], d[1])

		if data:

			prop[self.INDEX_START_TIME] = app.GetTime()
			prop[self.INDEX_START_TIME_STR] = time.strftime("%H:%M:%S")
			prop[self.INDEX_STATE] = self.STATE_ACTIVE

			self.__RefreshCurrentSlot()

			net.SendChatPacket("/switchbot_start {} {}".format(prop[self.INDEX_SLOT], data))

			if prem_data and constInfo.AUCTION_PREMIUM:
				tchat("switch start")
				net.SendChatPacket("/switchbot_start_premium {} {}".format(prop[self.INDEX_SLOT], prem_data))

	def OnRestartAfterTeleport(self):
		for slot, prop in self._data.iteritems():
			if prop[self.INDEX_STATE] == self.STATE_ACTIVE:
				data = ""
				for d in prop[self.INDEX_BONIS]:
					if d:
						data += "{} {} ".format(d[0], d[1])

				prem_data = ""
				for d in prop[self.INDEX_PREM_BONIS]:
					if d:
						prem_data += "{} {} ".format(d[0], d[1])

				net.SendChatPacket("/switchbot_start {} {}".format(prop[self.INDEX_SLOT], data))

				if prem_data:
					net.SendChatPacket("/switchbot_start_premium {} {}".format(prop[self.INDEX_SLOT], prem_data))

		net.SendChatPacket("/switchbot_change_speed {}".format(SPEED_DICT[self._speed]))

	def OnStop(self):
		prop = self._data.get(self._selected_slot, None)
		if prop is None:
			return
		
		net.SendChatPacket("/switchbot_stop {}".format(prop[self.INDEX_SLOT]))

	def OnReset(self):
		for key in self._data:
			prop = self._data[key]
			prop[self.INDEX_START_TIME] = 0
			prop[self.INDEX_START_TIME_STR] = TIME_DEFAULT_STR

			prop[self.INDEX_BONIS] = [[], [], [], [], []]

			if prop[self.INDEX_STATE] == self.STATE_ACTIVE:
				net.SendChatPacket("/switchbot_stop {}".format(prop[self.INDEX_SLOT]))

		for i in xrange(player.NORMAL_ATTRIBUTE_SLOT_MAX_NUM):
			self.GetChild("dropdown_0{}".format(i+1)).SelectItemByArg(0, -1)
			self.GetChild("prem_dropdown_0{}".format(i+1)).SelectItemByArg(0, -1)

		self.__RefreshCurrentSlot()

	def OnDelete(self):
		if self._selected_slot not in self._data:
			return

		old_slot = self._selected_slot
		prop = self._data.get(old_slot, None)
		if prop is not None:
			net.SendChatPacket("/switchbot_stop {}".format(prop[self.INDEX_SLOT]))

		del self._data[old_slot]

		new_slot = self.__FindNextSlot()
		if new_slot in self._data:
			self.__Select(new_slot)
		else:
			self.__ChangeSlot(new_slot)
			self._selected_slot = new_slot
		
		self._slots[old_slot].Disable()

		# check if this was the last existing slot
		if len(self._data) == 0:
			self.__ClearInfo()
			#self.__Disable()

	def OnMinimize(self):
		if len(self._data) > 0:
			self.wndSwitchbotMinimize.SetData(self._data)
			self.wndSwitchbotMinimize.Show()
			self.Close()
		else:
			tchat("TCHAT: Keine Daten vorhanden!")

	##########################################################
	### --------------------- GAME ----------------------- ###
	##########################################################
	def GAME_OnEnd(self, islot_index):
		slot = self.__GetSlotByInventoryIndex(int(islot_index))
		prop = self._data.get(slot, None)

		if prop is not None:
			prop[self.INDEX_STATE] = self.STATE_INACTIVE

			if slot == self._selected_slot:
				self.__RefreshCurrentSlot()

	def GAME_OnFinish(self, islot_index):
		slot = self.__GetSlotByInventoryIndex(int(islot_index))
		prop = self._data.get(slot, None)

		if prop is not None:
			prop[self.INDEX_STATE] = self.STATE_FINISHED

			if slot == self._selected_slot:
				self.__RefreshCurrentSlot()

	def GAME_OnUpdateConsumption(self, islot_index):
		for slot, prop in self._data.iteritems():
			if prop[self.INDEX_SLOT] == islot_index:
				prop[self.INDEX_CONSUMPTION] += 1
				if slot == self._selected_slot:
					self.GetChild("consumption").SetText(str(prop[self.INDEX_CONSUMPTION]))

	##########################################################
	### --------------------- BUILTIN -------------------- ###
	##########################################################
	def OnPressEscapeKeyInput(self, args):
		self.OnPressEscapeKey()
		return True

	def OnPressEscapeKey(self):
		self.Close()
		return True

	def OnMouseLeftButtonDown(self):
		if self.__IsSwitchableItemAttached():
			islot_index = mc.GetAttachedSlotNumber()
			self.__Append(islot_index)
			mc.DeattachObject()

	def OnRender(self):
		if self.IsInPosition() and self.__IsSwitchableItemAttached():
			self.GetChild("bg").Hide()
			self.GetChild("bg_default").Show()
			self.__HideContent()
		else:
			if not self.GetChild("bg").IsShow():
				self.GetChild("bg").Show()
				self.GetChild("bg_default").Hide()
				self.__ShowContent()

		x, y = self.GetGlobalPosition()
		t1 = self.templates[0]
		t1.SetPosition(x + 32, y + 471)
		t1.SetTop()

		t2 = self.templates[1]
		t2.SetPosition(x + self.GetWidth() - 25 - t2.GetWidth(), y + 471)
		t2.SetTop()

	def OnUpdate(self):
		# tooltip-update
		btn = self.GetChild("premium_info")
		if btn.IsIn():
			if not btn.IsToolTipShow():
				btn.ShowToolTip()
		else:
			if btn.IsToolTipShow():
				btn.HideToolTip()

		# alltime-update
		prop = self._data.get(self._selected_slot, None)
		if prop is not None:
			if prop[self.INDEX_STATE] == self.STATE_ACTIVE:
				start_time = prop[self.INDEX_START_TIME]
				if start_time != 0:
					current_time = app.GetTime()
					alltime = localeInfo.SecondToDHMSShort(current_time - start_time)
					self.GetChild("alltime").SetText(alltime)