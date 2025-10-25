import ui
import uiCommon
import mouseModule
import player
import net
import app
import localeInfo
import constInfo
import uihotkey
import cfg

MAX_PAGE_COUNT = 10


class EquipmentChangerWindow(ui.ScriptWindow):
	def __init__(self):
		ui.ScriptWindow.__init__(self)
		self.isLoaded = 0
		self.timeout = 0

		self.deletePageQuestionDialog = None
		self.newPageInputDialog = None
		self.__LoadWindow()

	def __del__(self):
		ui.ScriptWindow.__del__(self)

	def __LoadWindow(self):
		try:
			pyScrLoader = ui.PythonScriptLoader()
			pyScrLoader.LoadScriptFile(self, "uiscript/equipmentchanger.py")
		except:
			import exception
			exception.Abort("EquipmentChangerWindow.LoadWindow.LoadObject")

		try:
			# self.saveBtn = self.GetChild("SaveButton")
			# self.loadBtn = self.GetChild("LoadButton")
			self.infoBtn = self.GetChild("InfoButton")
			self.hotkeyBtn = self.GetChild("hotkey_button")
			self.eqSlots = self.GetChild("EquipmentSlot")
			self.runeBtn = self.GetChild("rune_page_circle")
			self.eqCostumeSlots = self.GetChild("EquipmentCostumesSlot")
		except:
			import exception
			exception.Abort("EquipmentChangerWindow.LoadWindow.BindObject")

		self.GetChild("titlebar").SetCloseEvent(ui.__mem_func__(self.Close))
		# self.saveBtn.SAFE_SetEvent(self.__SavePageEquipment)
		# self.loadBtn.SAFE_SetEvent(self.__LoadPageEquipment)
		self.infoBtn.SAFE_SetEvent(self.__InfoButtonClick)
		self.hotkeyBtn.SAFE_SetEvent(self.__HotkeyButtonClick)

		self.tooltipItem = None
		self.hotkeywnd = None

		# self.eqSlots.SetSelectEmptySlotEvent(ui.__mem_func__(self.__OnSelectEmptySlot))
		# self.eqSlots.SetSelectItemSlotEvent(ui.__mem_func__(self.__OnSelectItemSlot))
		self.eqSlots.SetOverInItemEvent(ui.__mem_func__(self.__OnOverInItem))
		self.eqSlots.SetOverOutItemEvent(ui.__mem_func__(self.__OnOverOutItem))

		# self.eqCostumeSlots.SetSelectEmptySlotEvent(ui.__mem_func__(self.__OnSelectEmptySlot))
		# self.eqCostumeSlots.SetSelectItemSlotEvent(ui.__mem_func__(self.__OnSelectItemSlot))
		self.eqCostumeSlots.SetOverInItemEvent(ui.__mem_func__(self.__OnOverInItem))
		self.eqCostumeSlots.SetOverOutItemEvent(ui.__mem_func__(self.__OnOverOutItem))

		self.pageList = ui.ListBoxEx()
		self.pageList.SetParent(self)
		self.pageList.SetItemSize(158, 23)
		self.pageList.SetItemStep(23 + 5)
		self.pageList.SetViewItemCount(6)
		self.pageList.SetSize(158 + 20, (23 + 5) * 6)
		self.pageList.SetPosition(193, 50)
		self.pageList.Show()

		self.scrollBar = ui.ScrollBar()
		self.scrollBar.SetParent(self.pageList)
		self.scrollBar.SetScrollBarSize((23 + 5) * 6)
		self.scrollBar.SetWindowHorizontalAlignRight()
		self.scrollBar.SetPosition(16, 0)
		self.scrollBar.Show()
		self.pageList.SetScrollBar(self.scrollBar)

		self.posInInventory = []
		self.pageListItems = []
		self.pageListCloseBtns = []
		self.__InitPages()

	def __InitPages(self):
		for x in xrange(len(self.pageListItems)):
			self.pageListItems[x].Hide()
		for x in xrange(len(self.pageListCloseBtns)):
			self.pageListCloseBtns[x].Hide()

		self.pageList.RemoveAllItems()
		self.pageListItems = []
		self.pageListCloseBtns = []

		pageCount = player.GetEquipmentPageCount()
		for x in xrange(pageCount):
			btn = ui.MakeButton(self.pageList, 0, 0, "", "d:/ymir work/ui/game/eqchanger/", "slot_normal.tga", "slot_hover.tga", "slot_active.tga", "slot_active.tga")
			btn.Show()
			btn.SetText(player.GetEquipmentPageName(x))
			btn.SAFE_SetEvent(self.OnClickEquipmentPage, x)

			delete_btn = ui.MakeButton(btn, btn.GetWidth() - 21, 4, "", "d:/ymir work/ui/public/", "close_button_01.sub", "close_button_02.sub", "close_button_03.sub")
			delete_btn.Show()
			delete_btn.SAFE_SetEvent(self.OnDeletePage, x, player.GetEquipmentPageName(x))

			self.pageList.AppendItem(btn)
			self.pageListItems.append(btn)
			self.pageListCloseBtns.append(delete_btn)

		if player.GetEquipmentPageSelected() < len(self.pageListItems):
			self.pageListItems[player.GetEquipmentPageSelected()].Disable()
			self.SetEquipmentVisualSlots(player.GetEquipmentPageSelected())

		if len(self.pageListItems) >= MAX_PAGE_COUNT:
			return

		btn = ui.MakeButton(self.pageList, 0, 0, "", "d:/ymir work/ui/game/eqchanger/", "slot_normal.tga", "slot_hover.tga", "slot_active.tga")
		btn.Show()
		btn.SetText("+")
		btn.SAFE_SetEvent(self.OnClickEquipmentPage, 999)
		self.pageList.AppendItem(btn)
		self.pageListItems.append(btn)

	def __HotkeyButtonClick(self):
		tchat("__HotkeyButtonClick")

		if self.hotkeywnd:
			del self.hotkeywnd 
			self.hotkeywnd = None

		hotkeywnd = uihotkey.HotkeyWindow()
		hotkeywnd.Open(player.GetEquipmentPageName(player.GetEquipmentPageSelected()))
		self.hotkeywnd = hotkeywnd

	def __RefreshScroll(self):
		if self.pageList.GetViewItemCount() > self.pageList.GetItemCount():
			self.pageScroll.SetMiddleBarSize(1.0)
		else:
			self.pageScroll.SetMiddleBarSize(self.pageList.GetViewItemCount() / float(self.pageList.GetItemCount()))

	def OnMouseWheel(self, len):
		lineCount = self.pageList.GetItemCount()
		if self.IsInPosition() and self.scrollBar.IsShow() and lineCount > 0:
			dir = constInfo.WHEEL_TO_SCROLL(len)
			new_pos = self.scrollBar.GetPos() + ((1.0 / lineCount) * dir)
			new_pos = max(0.0, new_pos)
			new_pos = min(1.0, new_pos)
			self.scrollBar.SetPos(new_pos)
			return True
		return False

	def Refresh(self):
		self.__InitPages()

	def SetEquipmentVisualSlots(self, page):
		tchat("SetEquipmentVisualSlots %d" % page)
		self.posInInventory = []
		for x in xrange(player.EQUIPMENT_PAGE_MAX_PARTS):
			slot = player.GetEquipmentPageWearCell(page, x)
			self.posInInventory.append(slot)
			index = player.GetItemIndex(slot)

			if x not in (9,10,11): # costume slots
				self.eqSlots.SetItemSlot(x, index)
			else:
				self.eqCostumeSlots.SetItemSlot(x, index)
		self.runeBtn.SetText(str(player.GetEquipmentPageRuneSet(page) + 1))
		
		pagename = player.GetEquipmentPageName(page).replace(' ','')

		try:
			isCtrl = int(cfg.Get(cfg.SAVE_PLAYER, "hotkey_ctrl_%s" % pagename, "0"))
			isAlt = int(cfg.Get(cfg.SAVE_PLAYER, "hotkey_alt_%s" % pagename, "0"))
			key = int(cfg.Get(cfg.SAVE_PLAYER, "hotkey_%s" % pagename, "0"))
		except:
			isCtrl, isAlt, key = (0, 0, 0)

		if key == '0':
			self.hotkeyBtn.SetText(localeInfo.HOTKEY)
		else:
			if key != 0 and key in localeInfo.AVAIL_KEY_LIST:
				text = localeInfo.AVAIL_KEY_LIST[key]
			else:
				text = "?"
			if isAlt:
				text = localeInfo.HOTKEY_ALT + " + " + text
			if isCtrl:
				text = localeInfo.HOTKEY_CONTROL + " + " + text

			self.hotkeyBtn.SetText(text)

	def OnClickEquipmentPage(self, page):
		if page == 999: #add page
			dlg = uiCommon.InputDialogWithDescription()
			dlg.item = None
			dlg.SetTitle(localeInfo.EQUIPMENT_PAGE_ADD_TITLE)
			dlg.SetDescription(localeInfo.EQUIPMENT_PAGE_ADD_DESCRIPTION)
			dlg.SetMaxLength(30)
			dlg.SetAcceptEvent(self.OnNewPageAccept)
			dlg.SetCancelEvent(self.OnNewPageCancel)
			dlg.Open()
			self.newPageInputDialog = dlg
			return

		if page == player.GetEquipmentPageSelected():
			return

		if app.GetTime() <= self.timeout:
			tchat("timeout")
			return

		pageCount = player.GetEquipmentPageCount()
		for x in xrange(pageCount):
			self.pageListItems[x].Enable()

		self.pageListItems[page].Disable()

		self.timeout = app.GetTime() + 3

		player.SetEquipmentPageSelected(page)
		net.SendEquipmentPageSelectPacket(page)

		self.SetEquipmentVisualSlots(page)


	def OnDeletePage(self, item, name):
		dlg = uiCommon.QuestionDialog()
		dlg.item = item
		dlg.SetText(localeInfo.EQUIPMENT_PAGE_DELETE_TEXT % name)
		dlg.SetAcceptText(localeInfo.EQUIPMENT_PAGE_DELETE_ACCEPT_TEXT)
		dlg.SAFE_SetAcceptEvent(self.OnDeletePageAccept)
		dlg.SAFE_SetCancelEvent(self.OnDeletePageCancel)
		dlg.Open()
		self.deletePageQuestionDialog = dlg

		cfg.Set(cfg.SAVE_PLAYER, "hotkey_ctrl_%s" % name.replace(' ',''), "")
		cfg.Set(cfg.SAVE_PLAYER, "hotkey_alt_%s" % name.replace(' ',''), "")
		cfg.Set(cfg.SAVE_PLAYER, "hotkey_%s" % name.replace(' ',''), "")

	def OnDeletePageAccept(self):
		item = self.deletePageQuestionDialog.item
		player.RemoveEquipmentPage(item)
		net.SendEquipmentPageDeletePacket(item)
		self.OnDeletePageCancel()

	def OnDeletePageCancel(self):
		self.deletePageQuestionDialog.Close()
		self.deletePageQuestionDialog = None

	def OnNewPageAccept(self):
		pageName = self.newPageInputDialog.GetText()
		if pageName and pageName.replace(" ", "") != "":
			net.SendEquipmentPageAddPacket(pageName)

		self.OnNewPageCancel()

		return True

	def OnNewPageCancel(self):
		self.newPageInputDialog.Close()
		self.newPageInputDialog = None
		return True

	def __SavePageEquipment(self):
		self.Refresh()

	def __LoadPageEquipment(self):
		self.Refresh()

	def __InfoButtonClick(self):
		from os import system
		system("start %s" % constInfo.URL['eqchanger'])
		tchat("start %s" % constInfo.URL['eqchanger'])

	def SetItemToolTip(self, tooltip):
		self.tooltipItem = tooltip

	def __OnSelectEmptySlot(self, selectedSlotPos):
		isAttached = mouseModule.mouseController.isAttached()
		if isAttached:
			attachedSlotType = mouseModule.mouseController.GetAttachedType()
			attachedSlotPos = mouseModule.mouseController.GetAttachedSlotNumber()
			mouseModule.mouseController.DeattachObject()

			if attachedSlotType != player.SLOT_TYPE_INVENTORY:
				return

			index = player.GetItemIndex(attachedSlotPos)
			self.eqSlots.SetItemSlot(selectedSlotPos, index, 0)

	def __OnSelectItemSlot(self, selectedSlotPos):
		isAttached = mouseModule.mouseController.isAttached()
		if isAttached:
			attachedSlotType = mouseModule.mouseController.GetAttachedType()
			attachedSlotPos = mouseModule.mouseController.GetAttachedSlotNumber()
			mouseModule.mouseController.DeattachObject()

			if attachedSlotType != player.SLOT_TYPE_INVENTORY:
				return

			index = player.GetItemIndex(attachedSlotPos)
			self.eqSlots.SetItemSlot(selectedSlotPos, index, 0)
		else:
			self.eqSlots.SetItemSlot(selectedSlotPos, 0, 0)

	def __OnOverInItem(self, slotIndex):
		self.tooltipItem.SetInventoryItem(self.posInInventory[slotIndex])
		tchat("slotIndex %d" % slotIndex)

	def __OnOverOutItem(self):
		self.tooltipItem.HideToolTip()

	def Open(self):
		if not self.isLoaded:
			self.isLoaded = 1
			net.SendChatPacket('/equipment_changer_load')
		self.Show()

	def Close(self):
		self.Hide()

	def Destroy(self):
		self.ClearDictionary()
		self.saveBtn = None
		self.eqSlots = None
		self.pageList = None
		self.scrollBar = None
		self.hotkeyBtn = None
		self.eqCostumeSlots = None
		self.pageListItems = []
		self.hotkeywnd = None

	def OnPressEscapeKey(self):
		self.Close()
		return True
