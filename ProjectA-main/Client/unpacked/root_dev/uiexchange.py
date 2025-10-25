import player
import exchange
import net
import localeInfo
import chat
import item
import app

import ui
import mouseModule
import uiPickMoney
import wndMgr

EXCHANGE_TRADING_SLOT = {}
EXCHANGE_ITEM_APPEND = None

###################################################################################################
## Exchange
class ExchangeDialog(ui.ScriptWindow):

	def __init__(self):
		ui.ScriptWindow.__init__(self)
		self.TitleName = 0
		self.tooltipItem = 0
		self.xStart = 0
		self.yStart = 0

	def __del__(self):
		ui.ScriptWindow.__del__(self)

	def LoadDialog(self):
		PythonScriptLoader = ui.PythonScriptLoader()
		PythonScriptLoader.LoadScriptFile(self, "UIScript/exchangedialog.py")

		## Owner
		self.OwnerSlot = self.GetChild("Owner_Slot")
		self.OwnerSlot.SetSelectEmptySlotEvent(ui.__mem_func__(self.SelectOwnerEmptySlot))
		self.OwnerSlot.SetSelectItemSlotEvent(ui.__mem_func__(self.SelectOwnerItemSlot))
		self.OwnerSlot.SetOverInItemEvent(ui.__mem_func__(self.OverInOwnerItem))
		self.OwnerSlot.SetOverOutItemEvent(ui.__mem_func__(self.OverOutItem))
		self.OwnerMoney = self.GetChild("Owner_Money_Value")
		self.OwnerAcceptLight = self.GetChild("Owner_Accept_Light")
		self.OwnerAcceptLight.Disable()
		self.OwnerMoneyButton = self.GetChild("Owner_Money")
		self.OwnerMoneyButton.SetEvent(ui.__mem_func__(self.OpenPickMoneyDialog))

		## Target
		self.TargetSlot = self.GetChild("Target_Slot")
		self.TargetSlot.SetOverInItemEvent(ui.__mem_func__(self.OverInTargetItem))
		self.TargetSlot.SetOverOutItemEvent(ui.__mem_func__(self.OverOutItem))
		self.TargetMoney = self.GetChild("Target_Money_Value")
		self.TargetAcceptLight = self.GetChild("Target_Accept_Light")
		self.TargetAcceptLight.Disable()

		## PickMoneyDialog
		dlgPickMoney = uiPickMoney.PickMoneyDialog()
		dlgPickMoney.LoadDialog()
		dlgPickMoney.SetAcceptEvent(ui.__mem_func__(self.OnPickMoney))
		dlgPickMoney.SetTitleName(localeInfo.EXCHANGE_MONEY)
		dlgPickMoney.SetMax(7)
		dlgPickMoney.Hide()
		self.dlgPickMoney = dlgPickMoney

		## Button
		self.AcceptButton = self.GetChild("Owner_Accept_Button")
		self.AcceptButton.SetToggleDownEvent(ui.__mem_func__(self.AcceptExchange))

		self.TitleName = self.GetChild("TitleName")
		self.GetChild("TitleBar").SetCloseEvent(net.SendExchangeExitPacket)

	def Destroy(self):
		print "---------------------------------------------------------------------------- DESTROY EXCHANGE"
		self.ClearDictionary()
		self.dlgPickMoney.Destroy()
		self.dlgPickMoney = 0
		self.OwnerSlot = 0
		self.OwnerMoney = 0
		self.OwnerAcceptLight = 0
		self.OwnerMoneyButton = 0
		self.TargetSlot = 0
		self.TargetMoney = 0
		self.TargetAcceptLight = 0
		self.TitleName = 0
		self.AcceptButton = 0
		self.tooltipItem = 0

	def OpenDialog(self):
		global EXCHANGE_TRADING_SLOT
		global EXCHANGE_ITEM_APPEND
		EXCHANGE_TRADING_SLOT.clear()

		if EXCHANGE_ITEM_APPEND:
			if app.GetTime() - EXCHANGE_ITEM_APPEND["time"] <= 3:
				EXCHANGE_TRADING_SLOT[EXCHANGE_ITEM_APPEND["slot"]] = 1
			EXCHANGE_ITEM_APPEND = None

		self.TitleName.SetText(localeInfo.EXCHANGE_WITH % exchange.GetNameFromTarget())	# str(localeInfo.EXCHANGE_TITLE % (exchange.GetNameFromTarget(), 0)).replace('(0)',''))
		self.GetChild('Target_Name').SetText(exchange.GetNameFromTarget())
		self.GetChild('Owner_Name').SetText(player.GetName())
		self.AcceptButton.Enable()
		self.AcceptButton.SetUp()
		self.Show()

		(self.xStart, self.yStart, z) = player.GetMainCharacterPosition()

	def CloseDialog(self):
		wndMgr.OnceIgnoreMouseLeftButtonUpEvent()

		if 0 != self.tooltipItem:
			self.tooltipItem.HideToolTip()

		self.dlgPickMoney.Close()
		self.Hide()

	def SetItemToolTip(self, tooltipItem):
		self.tooltipItem = tooltipItem

	def OpenPickMoneyDialog(self):

		if exchange.GetElkFromSelf() > 0:
			chat.AppendChat(chat.CHAT_TYPE_INFO, localeInfo.EXCHANGE_CANT_EDIT_MONEY)
			return

		self.dlgPickMoney.Open(player.GetElk())

	def OnPickMoney(self, money):
		max_money = 5 * 1000 * 1000 * 1000 # 5kkk
		if money > max_money:
			money = max_money
		net.SendExchangeElkAddPacket(money)

	def AcceptExchange(self):
		net.SendExchangeAcceptPacket()
		self.AcceptButton.Disable()

	def AppendOwnerItem(self, SlotIndex):
		global EXCHANGE_TRADING_SLOT

		itemID = player.GetItemIndex(SlotIndex)
		item.SelectItem(1, 2, itemID)

		if item.IsAntiFlag(item.ITEM_ANTIFLAG_GIVE):
			chat.AppendChat(chat.CHAT_TYPE_INFO, localeInfo.EXCHANGE_CANNOT_GIVE)
			mouseModule.mouseController.DeattachObject()
			return

		for i in xrange(exchange.EXCHANGE_ITEM_MAX_NUM):
			if not exchange.GetItemVnumFromSelf(i):
				tchat("net.SendExchangeItemAddPacket(%d,%d,%d)" % (player.INVENTORY, SlotIndex, i))
				net.SendExchangeItemAddPacket(player.INVENTORY, SlotIndex, i)
				EXCHANGE_TRADING_SLOT[SlotIndex] = 1

	def SelectOwnerEmptySlot(self, SlotIndex):
		global EXCHANGE_TRADING_SLOT

		if False == mouseModule.mouseController.isAttached():
			return

		if mouseModule.mouseController.IsAttachedMoney():
			net.SendExchangeElkAddPacket(mouseModule.mouseController.GetAttachedMoneyAmount())
		else:
			attachedSlotType = mouseModule.mouseController.GetAttachedType()
			if (player.SLOT_TYPE_INVENTORY == attachedSlotType
				or player.SLOT_TYPE_DRAGON_SOUL_INVENTORY == attachedSlotType or attachedSlotType == player.SLOT_TYPE_SKILLBOOK_INVENTORY
				or attachedSlotType == player.SLOT_TYPE_UPPITEM_INVENTORY or attachedSlotType == player.SLOT_TYPE_STONE_INVENTORY
				or attachedSlotType == player.SLOT_TYPE_ENCHANT_INVENTORY or ( player.ENABLE_COSTUME_INVENTORY and attachedSlotType == player.SLOT_TYPE_COSTUME_INVENTORY )):

				attachedInvenType = player.SlotTypeToInvenType(attachedSlotType)
				SrcSlotNumber = mouseModule.mouseController.GetAttachedSlotNumber()
				DstSlotNumber = SlotIndex

				itemID = player.GetItemIndex(attachedInvenType, SrcSlotNumber)
				item.SelectItem(1, 2, itemID)

				if item.IsAntiFlag(item.ITEM_ANTIFLAG_GIVE):
					chat.AppendChat(chat.CHAT_TYPE_INFO, localeInfo.EXCHANGE_CANNOT_GIVE)
					mouseModule.mouseController.DeattachObject()
					return

				net.SendExchangeItemAddPacket(attachedInvenType, SrcSlotNumber, DstSlotNumber)
				EXCHANGE_TRADING_SLOT[SrcSlotNumber] = 1

		mouseModule.mouseController.DeattachObject()

	def SelectOwnerItemSlot(self, SlotIndex):

		if player.ITEM_MONEY == mouseModule.mouseController.GetAttachedItemIndex():

			money = mouseModule.mouseController.GetAttachedItemCount()
			net.SendExchangeElkAddPacket(money)

	def RefreshOwnerSlot(self):
		for i in xrange(exchange.EXCHANGE_ITEM_MAX_NUM):
			itemIndex = exchange.GetItemVnumFromSelf(i)
			itemCount = exchange.GetItemCountFromSelf(i)
			if 1 == itemCount:
				itemCount = 0
			metinSlot = [exchange.GetItemMetinSocketFromSelf(i, socket) for socket in xrange(player.METIN_SOCKET_MAX_NUM)]
			self.OwnerSlot.SetItemSlot(i, itemIndex, itemCount, metinSlot)
		self.OwnerSlot.RefreshSlot()

	def RefreshTargetSlot(self):
		for i in xrange(exchange.EXCHANGE_ITEM_MAX_NUM):
			itemIndex = exchange.GetItemVnumFromTarget(i)
			itemCount = exchange.GetItemCountFromTarget(i)
			if 1 == itemCount:
				itemCount = 0
			metinSlot = [exchange.GetItemMetinSocketFromTarget(i, socket) for socket in xrange(player.METIN_SOCKET_MAX_NUM)]
			self.TargetSlot.SetItemSlot(i, itemIndex, itemCount, metinSlot)
		self.TargetSlot.RefreshSlot()

	def Refresh(self):

		self.RefreshOwnerSlot()
		self.RefreshTargetSlot()

		self.OwnerMoney.SetText(localeInfo.NumberToString(exchange.GetElkFromSelf()))
		self.TargetMoney.SetText(localeInfo.NumberToString(exchange.GetElkFromTarget()))

		if True == exchange.GetAcceptFromSelf():
			self.OwnerAcceptLight.Down()
		else:
			self.AcceptButton.Enable()
			self.AcceptButton.SetUp()
			self.OwnerAcceptLight.SetUp()

		if True == exchange.GetAcceptFromTarget():
			self.TargetAcceptLight.Down()
		else:
			self.TargetAcceptLight.SetUp()

	def OverInOwnerItem(self, slotIndex):

		if 0 != self.tooltipItem:
			self.tooltipItem.SetExchangeOwnerItem(slotIndex)

	def OverInTargetItem(self, slotIndex):

		if 0 != self.tooltipItem:
			self.tooltipItem.SetExchangeTargetItem(slotIndex)

	def OverOutItem(self):

		if 0 != self.tooltipItem:
			self.tooltipItem.HideToolTip()

	def OnTop(self):
		self.tooltipItem.SetTop()

	def OnUpdate(self):

		USE_EXCHANGE_LIMIT_RANGE = 1000

		(x, y, z) = player.GetMainCharacterPosition()
		if abs(x - self.xStart) > USE_EXCHANGE_LIMIT_RANGE or abs(y - self.yStart) > USE_EXCHANGE_LIMIT_RANGE:
			(self.xStart, self.yStart, z) = player.GetMainCharacterPosition()
			net.SendExchangeExitPacket()
