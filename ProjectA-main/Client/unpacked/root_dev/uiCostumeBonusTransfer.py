import ui
import app
import localeInfo
import uiScriptLocale
import net
import item
import player
import uiCommon
import snd
import chat
import mouseModule

USE_WINDOW_LIMIT_RANGE = 500

class CostumeBonusTransferWindow(ui.ScriptWindow):
	tooltipItem = None
	popupDialog = None
	questionDialog = None

	xCombWindowStart = 0
	yCombWindowStart = 0
	isLoaded = 0
	def __init__(self):
		if not app.ENABLE_COSTUME_BONUS_TRANSFER:
			import exception
			exception.Abort("What do you do?")
			return

		ui.ScriptWindow.__init__(self)

	def __del__(self):
		ui.ScriptWindow.__del__(self)

	def Destroy(self):
		self.ClearDictionary()

		self.tooltipItem = None
		if self.popupDialog:
			self.popupDialog.Hide()
		self.popupDialog = None
		self.questionDialog = None

		self.xCombWindowStart = 0
		self.yCombWindowStart = 0

	def LoadWindow(self):
		if self.isLoaded == 1:
			return

		try:
			pyScrLoader = ui.PythonScriptLoader()
			pyScrLoader.LoadScriptFile(self, "UIScript/CostumeBonusTransferWindow.py")
		except:
			import exception
			exception.Abort("CostumeBonusTransferWindow.LoadWindow.LoadScript")

		try:
			self.GetChild("TitleBar").SetCloseEvent(ui.__mem_func__(self.Cancel))
			self.GetChild("AcceptButton").SetEvent(self.Accept)
			self.GetChild("CancelButton").SetEvent(self.Cancel)
			wndCombItem = self.GetChild("CombItemSlot")
		except:
			import exception
			exception.Abort("CostumeBonusTransferWindow.LoadWindow.BindObject")

		## Item
		wndCombItem.SetSelectEmptySlotEvent(ui.__mem_func__(self.SelectEmptySlot))
		wndCombItem.SetSelectItemSlotEvent(ui.__mem_func__(self.SelectItemSlot))
		wndCombItem.SetUnselectItemSlotEvent(ui.__mem_func__(self.UseItemSlot))
		wndCombItem.SetUseSlotEvent(ui.__mem_func__(self.UseItemSlot))
		wndCombItem.SetOverInItemEvent(ui.__mem_func__(self.OverInItem))
		wndCombItem.SetOverOutItemEvent(ui.__mem_func__(self.OverOutItem))
		self.wndCombItem = wndCombItem

		# PopupDlg
		self.popupDialog = uiCommon.PopupDialog()
		self.popupDialog.Hide()

		self.isLoaded = 1

	def CloseDialog(self):
		if self.popupDialog:
			self.popupDialog.Hide()
		self.OnDialogCancelEvent()
		if self.toolTipItem:
			self.toolTipItem.HideToolTip()

		self.Hide()

	def Open(self):
		self.LoadWindow()

		(self.xCombWindowStart, self.yCombWindowStart, z) = player.GetMainCharacterPosition()

		player.SetCostumeBonusTransferWindowOpen()
		self.SetCenterPosition()
		self.SetTop()
		self.Show()

	def Cancel(self):
		net.SendCostumeBonusTransferCancel()

	def OnDialogAcceptEvent(self):
		if self.questionDialog:
			self.questionDialog.Close()
		net.SendCostumeBonusTransferAccept()

	def OnDialogCancelEvent(self):
		if self.questionDialog:
			self.questionDialog.Close()
		self.questionDialog = None

	def Accept(self):
		if player.GetCurrentCostumeBonusTransferItemCount() <> player.CBT_SLOT_MAX:
			chat.AppendChat(chat.CHAT_TYPE_INFO, localeInfo.COMB_NOT_ALL_SLOT_APPEND_ITEM)
		else:
			self.questionDialog = uiCommon.QuestionDialog2()
			self.questionDialog.SetAcceptEvent(ui.__mem_func__(self.OnDialogAcceptEvent))
			self.questionDialog.SetCancelEvent(ui.__mem_func__(self.OnDialogCancelEvent))
			self.questionDialog.SetText1(localeInfo.COMB_MATERIAL_ATTR_WILL_TRANSFER)
			self.questionDialog.SetText2(localeInfo.COMB_IS_CONTINUE_PROCESS)
			self.questionDialog.Open()

	def CanAttachSlot(self, selectedSlotPos, attachedSlotType, attachedSlotPos):
		if player.IsEquipmentSlot(attachedSlotPos):
			chat.AppendChat(chat.CHAT_TYPE_INFO, localeInfo.COMB_NOT_ITEM_IN_INVENTORY)
			return False

		attachedInvenType = player.SlotTypeToInvenType(attachedSlotType)
		if selectedSlotPos == player.CBT_SLOT_MEDIUM and player.GetItemIndex(attachedInvenType, attachedSlotPos) == player.CBT_MEDIUM_ITEM_VNUM:
			return True

		if selectedSlotPos == player.CBT_SLOT_MATERIAL or selectedSlotPos == player.CBT_SLOT_TARGET:
			if player.GetCostumeBonusTransferItemID(selectedSlotPos) == 0:
				item.SelectItem(1, 2, player.GetItemIndex(attachedInvenType, attachedSlotPos))
				if item.GetItemType() == item.ITEM_TYPE_COSTUME:
					return True

		return False

	## Slot Event
	def SelectEmptySlot(self, selectedSlotPos):
		if mouseModule.mouseController.isAttached():
			attachedSlotType = mouseModule.mouseController.GetAttachedType()
			attachedInvenType = player.SlotTypeToInvenType(attachedSlotType)
			attachedSlotPos = mouseModule.mouseController.GetAttachedSlotNumber()
			if self.CanAttachSlot(selectedSlotPos, attachedSlotType, attachedSlotPos):
				snd.PlaySound("sound/ui/drop.wav")

				if player.GetCurrentCostumeBonusTransferItemCount() == player.CBT_SLOT_MAX:
					self.popupDialog.SetText(localeInfo.COMB_MATERIAL_ATTR_WILL_TRANSFER)
					self.popupDialog.Open()

				net.SendCostumeBonusTransferCheckIn(attachedInvenType, attachedSlotPos, selectedSlotPos)

			mouseModule.mouseController.DeattachObject()

	def SelectItemSlot(self, selectedSlotPos):
		if mouseModule.mouseController.isAttached():
			mouseModule.mouseController.DeattachObject()
			snd.PlaySound("sound/ui/drop.wav")

	def UseItemSlot(self, selectedSlotPos):
		if mouseModule.mouseController.isAttached():
			mouseModule.mouseController.DeattachObject()

		if selectedSlotPos == player.CBT_SLOT_RESULT:
			return

		net.SendCostumeBonusTransferCheckOut(selectedSlotPos)
		snd.PlaySound("sound/ui/drop.wav")
		self.OverOutItem()

	def SetItemToolTip(self, itemTooltip):
		self.toolTipItem = itemTooltip

	def __ShowToolTip(self, selectedSlotPos):
		if self.toolTipItem:
			self.toolTipItem.SetCostumeBonusTransferWindowItem(selectedSlotPos)

	def OverInItem(self, selectedSlotPos):
		self.wndCombItem.SetUsableItem(False)
		self.__ShowToolTip(selectedSlotPos)

	def OverOutItem(self):
		self.wndCombItem.SetUsableItem(False)
		if self.toolTipItem:
			self.toolTipItem.HideToolTip()

	def RefreshItemSlotWindow(self):
		if self.wndCombItem:
			getItemID=player.GetCostumeBonusTransferItemID
			getItemCount=player.GetCostumeBonusTransferItemCount
			setItemID=self.wndCombItem.SetItemSlot
			for i in xrange(player.CBT_SLOT_MAX):
				setItemID(i, getItemID(i), getItemCount(i))

			self.wndCombItem.RefreshSlot()

	def OnUpdate(self):
		(x, y, z) = player.GetMainCharacterPosition()
		if abs(x - self.xCombWindowStart) > USE_WINDOW_LIMIT_RANGE or abs(y - self.yCombWindowStart) > USE_WINDOW_LIMIT_RANGE:
			self.Cancel()

	def OnPressEscapeKey(self):
		self.Cancel()

