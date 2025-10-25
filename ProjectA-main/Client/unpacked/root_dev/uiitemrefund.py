import ui
import localeInfo
import uiToolTip
import player
import item

class ItemRefundBoard(ui.BoardWithTitleBar):

	BOARD_WIDTH = 350

	def __init__(self):
		ui.BoardWithTitleBar.__init__(self)

		self.itemCellList = []
		self.itemObjList = []
		self.lastY = 0

		self.toolTip = uiToolTip.ItemToolTip()
		self.toolTip.HideToolTip()

		self.__LoadBaseWindow()

	def __del__(self):
		ui.BoardWithTitleBar.__del__(self)

	def __LoadBaseWindow(self):
		self.AddFlag("float")
		self.AddFlag("movable")
		self.SetSize(self.BOARD_WIDTH, 0)
		self.SetCloseEvent(ui.__mem_func__(self.Close))
		self.SetTitleName(localeInfo.ITEM_REFUND_WINDOW_TITLE)

		desc1 = ui.MultiTextLine()
		desc1.SetParent(self)
		desc1.SetPosition(20, 25)
		desc1.SetWidth(self.GetWidth() - 20 * 2)
		desc1.SetText(localeInfo.ITEM_REFUND_DESCRIPTION1)
		desc1.Show()
		self.desc1 = desc1

		desc2 = ui.TextLine()
		desc2.SetParent(self)
		desc2.SetPosition(20, desc1.GetBottom() + 10)
		desc2.SetText(localeInfo.ITEM_REFUND_DESCRIPTION2)
		desc2.Show()
		self.desc2 = desc2
		self.lastY = self.desc2.GetBottom()

		self.SetSize(self.GetWidth(), desc2.GetBottom() + 15)

	def AppendItem(self, cell):
		itemVnum = player.GetItemIndex(cell)
		if itemVnum == 0 or not item.SelectItem(1, 2, itemVnum):
			import dbg
			dbg.TraceError("ItemRefund::AppendItem: invalid call with cell %d (no item)" % cell)
			return

		self.itemCellList.append(cell)

		img = ui.ImageBox()
		img.SetParent(self)
		img.SetPosition(35, self.lastY + 8)
		img.LoadImage(item.GetIconImageFileName())
		img.SAFE_SetStringEvent("MOUSE_OVER_IN", self.OnMouseOverIn, len(self.itemObjList), itemVnum)
		img.SAFE_SetStringEvent("MOUSE_OVER_OUT", self.OnMouseOverOut)
		img.Show()
		self.lastY = img.GetBottom()

		itemName = item.GetItemName()
		itemCount = player.GetItemCount(cell)
		if itemCount > 1:
			itemName = "%dx %s" % (itemCount, itemName)

		name = ui.TextLine()
		name.SetParent(img)
		name.SetPosition(img.GetWidth() + 7, 0)
		name.SetText(itemName)
		name.SetWindowVerticalAlignCenter()
		name.SetVerticalAlignCenter()
		name.Show()

		self.itemObjList.append([img, name])
		self.SetSize(self.GetWidth(), self.lastY + 15)

	def AppendGold(self, gold):
		if gold == 0:
			return

		itemVnum = 1
		item.SelectItem(1, 2, itemVnum)

		img = ui.ImageBox()
		img.SetParent(self)
		img.SetPosition(35, self.lastY + 8)
		img.LoadImage(item.GetIconImageFileName())
		img.Show()
		self.lastY = img.GetBottom()

		name = ui.TextLine()
		name.SetParent(img)
		name.SetPosition(img.GetWidth() + 7, 0)
		name.SetText(localeInfo.NumberToMoneyString(gold))
		name.SetWindowVerticalAlignCenter()
		name.SetVerticalAlignCenter()
		name.Show()

		self.itemObjList.append([img, name])
		self.SetSize(self.GetWidth(), self.lastY + 15)

	def Clear(self):
		self.itemCellList = []
		self.itemObjList = []
		self.lastY = self.desc2.GetBottom()

	def Open(self, refundedGold):
		self.AppendGold(refundedGold)

		self.SetCenterPosition()
		self.SetTop()
		self.Show()

	def Close(self):
		self.toolTip.HideToolTip()
		self.Hide()

	def OnPressEscapeKey(self):
		self.Close()
		return True

	def OnMouseOverIn(self, index, itemVnum):
		cell = self.itemCellList[index]
		if player.GetItemIndex(cell) == itemVnum:
			self.toolTip.SetInventoryItem(cell)

	def OnMouseOverOut(self):
		self.toolTip.HideToolTip()
