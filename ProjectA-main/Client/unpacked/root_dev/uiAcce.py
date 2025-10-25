import localeInfo
import uiCommon
import uiRefine
import constInfo
import exception
import item
import player
import net
import snd
import grp
import app
import uiScriptLocale
import ui
import mouseModule
import dbg

class AcceWindow(ui.ScriptWindow):

	isLoaded = 0
	tooltip = None
	wndItem = None
	popupDialog = None
	questionDialog = None

	highlightedSlotList = []
	windowType = 0
	xAcceWindowStart = 0
	yAcceWindowStart = 0
	Cost = None

	combineBoard 	= None
	absorbBoard 	= None
	
	def __init__(self):
		ui.ScriptWindow.__init__(self)
		

	def __del__(self):
		ui.ScriptWindow.__del__(self)
		
	def __LoadWindow(self, type):
		if type == 0:
			try:
				pyScrLoader = ui.PythonScriptLoader()
				pyScrLoader.LoadScriptFile(self, "uiscript/Acce_AbsorbWindow.py")
			except:
				import exception
				exception.Abort("AcceWindow.LoadWindow.LoadObject")
		else:
			try:
				pyScrLoader = ui.PythonScriptLoader()
				pyScrLoader.LoadScriptFile(self, "uiscript/Acce_CombineWindow.py")
			except:
				import exception
				exception.Abort("AcceWindow.LoadWindow.LoadObject")

		try:
			self.wndItem = self.GetChild("AcceSlot")
			self.GetChild("board").SetCloseEvent(ui.__mem_func__(self.Close))

			if type == 0:
				self.absorbBoard = self.GetChild("board")
			else:
				self.combineBoard = self.GetChild("board")

			if type == 1:
				self.Cost = self.GetChild("Cost")
			self.GetChild("AcceptButton").SetEvent(self.Accept)
			self.GetChild("CancelButton").SetEvent(self.OnAcceCloseEvent)
			self.wndItem.SetSelectEmptySlotEvent(ui.__mem_func__(self.SelectEmptySlot))
			self.wndItem.SetSelectItemSlotEvent(ui.__mem_func__(self.SelectItemSlot))
			self.wndItem.SetOverInItemEvent(ui.__mem_func__(self.OverInItem))
			self.wndItem.SetOverOutItemEvent(ui.__mem_func__(self.OverOutItem))
			self.wndItem.SetUseSlotEvent(ui.__mem_func__(self.UseItemSlot))
			self.wndItem.SetUnselectItemSlotEvent(ui.__mem_func__(self.UseItemSlot))
			if self.Cost:
				self.Cost.SetText(localeInfo.ACCE_ABSORB_COST % (0))
		except:
			import exception
			exception.Abort("AcceWindow.LoadWindow.BindObject")

	def Destroy(self):
		self.tooltip = None
		self.wndItem = None
		self.popupDialog = None
		self.questionDialog = None

		self.highlightedSlotList = []
		self.windowType = 0
		self.xAcceWindowStart = 0
		self.yAcceWindowStart = 0
		self.Cost = None

		ui.ScriptWindow.Destroy(self)

	def Accept(self):
		if self.windowType == 1:
			self.Combine()
		else:
			self.Absorb()
		

	def Absorb(self):
		self.questionDialog = uiCommon.QuestionDialog()
		self.questionDialog.SetText(localeInfo.ACCE_DEL_ABSORDITEM)
		self.questionDialog.SetAcceptEvent(ui.__mem_func__(self.OnAcceAcceptEvent))
		self.questionDialog.SetCancelEvent(ui.__mem_func__(self.OnAcceQuestionCancel))
		self.questionDialog.Open()
		constInfo.SET_ITEM_DROP_QUESTION_DIALOG_STATUS(1)

		
	def Combine(self):
		net.SendAcceRefineAccept(self.windowType)

	def Open(self, type):
		self.__LoadWindow(type)
		self.windowType = type
		(x, y, z) = player.GetMainCharacterPosition()
		self.xAcceWindowStart = x
		self.yAcceWindowStart = y

		self.SetTop()
		self.SetCenterPosition()
		self.Show()

		if type == 0:
			
			if self.combineBoard:
				self.combineBoard.Hide()

		else:

			if self.absorbBoard:
				self.absorbBoard.Hide()

	def Close(self):
		net.SendAcceRefineCanCancel()
		if None != self.tooltipItem:
			self.tooltipItem.HideToolTip()
		self.Hide()
		
	def SetItemToolTip(self, itemTooltip):
		self.tooltipItem = itemTooltip
		
	def __ShowToolTip(self, slotIndex):
		if self.tooltipItem:
			self.tooltipItem.SetAcceWindowItem(slotIndex)

	def OverInItem(self, slotIndex):
		slotIndex = slotIndex
		self.wndItem.SetUsableItem(False)
		self.__ShowToolTip(slotIndex)
		
	def OverOutItem(self):
		self.wndItem.SetUsableItem(False)
		if self.tooltipItem:
			self.tooltipItem.HideToolTip()

	def OnAcceAcceptEvent(self):
		self.OnCloseQuestionDialog()
		net.SendAcceRefineAccept(self.windowType)

	def OnAcceCloseEvent(self):
		self.Close()
		
	def OnAcceQuestionCancel(self):
		self.OnCloseQuestionDialog()
		
	def OnCloseQuestionDialog(self):
		if not self.questionDialog:
			return
		
		self.questionDialog.Close()
		self.questionDialog = None
		constInfo.SET_ITEM_DROP_QUESTION_DIALOG_STATUS(0)

	## Slot Event
	def SelectEmptySlot(self, selectedSlotPos):
		if mouseModule.mouseController.isAttached():
			attachedSlotType = mouseModule.mouseController.GetAttachedType()
			attachedSlotPos = mouseModule.mouseController.GetAttachedSlotNumber()
			
			attachedInvenType = player.SlotTypeToInvenType(attachedSlotType)
			if player.RESERVED_WINDOW == attachedInvenType:
				return
			
			if player.INVENTORY == attachedInvenType:
				player.SetAcceActivedItemSlot(selectedSlotPos, attachedSlotPos)
				#self.highlightedSlotList[selectedSlotPos] = attachedSlotPos

				itemVnum = player.GetItemIndex(attachedSlotPos)

				item.SelectItem(1, 2, itemVnum)

				itemType 	= item.GetItemType()
				itemSubType = item.GetItemSubType()

				occupiedSlot = -1

				firstSlot = player.GetAcceItemID(0)
				secondSlot = player.GetAcceItemID(1)

				if firstSlot:
					occupiedSlot = 0

				if secondSlot:
					occupiedSlot = 1

				if firstSlot and secondSlot:
					occupiedSlot = -1

				if self.windowType == 1 and player.IsAcceWindowEmpty():

					if occupiedSlot == -1:
						return

					itemInside = player.GetAcceItemID(occupiedSlot)
					item.SelectItem(1, 2, itemInside)
					itemInsideSubType 	= item.GetItemSubType() 

					if itemType == item.ITEM_TYPE_COSTUME and itemSubType == itemInsideSubType:

						self.popupDialog = uiCommon.PopupDialog()
						self.popupDialog.SetText(localeInfo.ACCE_DEL_SERVEITEM)
						self.popupDialog.SetButtonName(localeInfo.UI_OK)
						self.popupDialog.SetAutoClose(True)
						self.popupDialog.Open()

				if self.windowType == 0:
					if itemType == item.ITEM_TYPE_COSTUME and itemSubType == item.COSTUME_TYPE_ACCE_COSTUME:
						self.popupDialog = uiCommon.PopupDialog()
						self.popupDialog.SetText(localeInfo.ACCE_WINDOW_CANT_ABSORB)
						self.popupDialog.SetButtonName(localeInfo.UI_OK)
						self.popupDialog.SetAutoClose(True)
						self.popupDialog.Open()
						return

				net.SendAcceRefineCheckIn(attachedInvenType, attachedSlotPos, selectedSlotPos)
			
			mouseModule.mouseController.DeattachObject()

	def SelectItemSlot(self, selectedSlotPos):

		if mouseModule.mouseController.isAttached():
			attachedSlotType = mouseModule.mouseController.GetAttachedType()

			if player.SLOT_TYPE_INVENTORY == attachedSlotType:
					attachedSlotPos = mouseModule.mouseController.GetAttachedSlotNumber()
					#net.SendSafeboxCheckinPacket(attachedSlotPos, selectedSlotPos)
					#snd.PlaySound("sound/ui/drop.wav")

			mouseModule.mouseController.DeattachObject()
		else:
			net.SendAcceRefineCheckOut(selectedSlotPos)

	def UseItemSlot(self, slotIndex):
		net.SendAcceRefineCheckOut(slotIndex)
		mouseModule.mouseController.DeattachObject()
		self.OverOutItem()

	def RefreshAcceWindow(self):
		if self.wndItem:
			for i in xrange(3):
				self.wndItem.SetItemSlot(i, player.GetAcceItemID(i), 0)
				if self.windowType == 1:
					if i == 0:
						text = localeInfo.ACCE_ABSORB_COST.replace("%d", "%s")
						if player.GetAcceItemID(i) != 0:
							item.SelectItem(1, 2, player.GetAcceItemID(i))
							self.Cost.SetText(text % localeInfo.NumberToMoneyString(item.GetIBuyItemPrice()))
						else:
							self.Cost.SetText(text % ("0"))
			
			self.wndItem.RefreshSlot()


	def __OnClosePopupDialog(self):
		pass
	
	def OnUpdate(self):
		USE_ACCEWINDOW_LIMIT_RANGE = 2500

		(x, y, z) = player.GetMainCharacterPosition()
		if abs(x - self.xAcceWindowStart) > USE_ACCEWINDOW_LIMIT_RANGE or abs(y - self.yAcceWindowStart) > USE_ACCEWINDOW_LIMIT_RANGE:
			self.Close()

	def OnPressEscapeKey(self):
		self.Close()

