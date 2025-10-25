import ui
import shop
import item
import app
import net
import uiCommon
import player
import localeInfo
import grp

class GayaShopWindow(ui.BaseScriptWindow):

	DISABLE_COLOR = grp.GenerateColor(0.85, 0.3, 0.3, 0.3)

	#################################################
	## MAIN FUNCTIONS
	#################################################

	def __init__(self, itemTooltip):
		ui.BaseScriptWindow.__init__(self, "GayaShopWindow", self.__BindObject)

		self.itemTooltip = itemTooltip
		self.itemBuyQuestionDialog = None

		self.disablePosList = []
		self.currentSlot = None

		self.__LoadWindow()

	def __BindObject(self):
		self._AddLoadObject("slot", "slot")
		self._AddLoadObject("slot2", "slot2")
		self._AddLoadObject("board", "board")
		self._AddLoadObject("background", "background")

		priceDict = {}
		for i in xrange(shop.GAYA_SHOP_MAX_NUM):
			priceDict[i] = "price%d" % (i + 1)
		self._AddLoadObject("price", priceDict)

		iconDict = {}
		for i in xrange(shop.GAYA_SHOP_MAX_NUM):
			iconDict[i] = "gaya_icon%d" % (i + 1)
		self._AddLoadObject("icon", iconDict)

	def __LoadWindow(self):
		self.main["slot"].SetOverInItemEvent(ui.__mem_func__(self.__OnSlotOverIn))
		self.main["slot"].SetOverOutItemEvent(ui.__mem_func__(self.__OnSlotOverOut))
		self.main["slot"].SAFE_SetButtonEvent("LEFT", "EXIST", self.__OnSlotSelect)
		self.main["slot"].SAFE_SetButtonEvent("RIGHT", "EXIST", self.__OnSlotSelect)

		self.main["slot2"].SetOverInItemEvent(ui.__mem_func__(self.__OnSlotOverIn))
		self.main["slot2"].SetOverOutItemEvent(ui.__mem_func__(self.__OnSlotOverOut))
		self.main["slot2"].SAFE_SetButtonEvent("LEFT", "EXIST", self.__OnSlotSelect)
		self.main["slot2"].SAFE_SetButtonEvent("RIGHT", "EXIST", self.__OnSlotSelect)

		self.Refresh()

	def Refresh(self):
		self.disablePosList = []

		needExtra = False
		for i in xrange(9, shop.GAYA_SHOP_MAX_NUM):
			if shop.GetGayaItemVnum(i):
				needExtra = True
				break

		if needExtra:
			self.main["slot"].Hide()
			self.main["slot2"].Show()
			self.currentSlot = self.main["slot2"]
			self.SetSize(self.GetWidth(), 177 + 7 + 7 + 58)
			self.main["board"].SetSize(self.GetWidth() - 7*2, self.GetHeight())

			for i in xrange(9, shop.GAYA_SHOP_MAX_NUM):
				self.main["icon"][i].Show()

			self.main["background"].LoadImage("d:/ymir work/ui/gemshop/gemshop_001_expanded.tga")
		else:
			self.main["slot2"].Hide()
			self.main["slot"].Show()
			self.currentSlot = self.main["slot"]
			self.SetSize(self.GetWidth(), 177 + 7 + 7)
			self.main["board"].SetSize(self.GetWidth() - 7*2, self.GetHeight())
			for i in xrange(9, shop.GAYA_SHOP_MAX_NUM):
				self.main["icon"][i].Hide()

			self.main["background"].LoadImage("d:/ymir work/ui/gemshop/gemshop_backimg.sub")

		for i in xrange(shop.GAYA_SHOP_MAX_NUM):
			itemVnum = shop.GetGayaItemVnum(i)
			itemCount = shop.GetGayaItemCount(i)
			itemPrice = shop.GetGayaItemPrice(i)

			self.currentSlot.ClearSlot(i)

			if itemVnum > 0 and itemCount > 0:
				self.currentSlot.SetItemSlot(i, itemVnum, itemCount)
				self.main["price"][i].SetText(str(itemPrice))

				if itemPrice > player.GetStatus(player.GAYA):
					self.disablePosList.append(self.currentSlot.GetSlotPosition(i))
			else:
				self.main["price"][i].SetText("")

	def Open(self):
		self.Refresh()
		app.SetCursor(app.BUY)
		ui.BaseScriptWindow.Open(self)

	def Close(self):
		self.__OnSlotOverOut()
		app.SetCursor(app.NORMAL)

		if self.itemBuyQuestionDialog:
			self.itemBuyQuestionDialog.Close()
			self.itemBuyQuestionDialog = None

		ui.BaseScriptWindow.Close(self)

	def __OnSlotOverIn(self, slotIdx):
		itemVnum = shop.GetGayaItemVnum(slotIdx)
		if itemVnum != 0:
			self.itemTooltip.SetItemToolTip(itemVnum)
			self.itemTooltip.AppendGayaPrice(shop.GetGayaItemPrice(slotIdx))

	def __OnSlotOverOut(self):
		self.itemTooltip.HideToolTip()

	def __OnSlotSelect(self, slotIdx):
		itemVnum = shop.GetGayaItemVnum(slotIdx)
		itemCount = shop.GetGayaItemCount(slotIdx)
		itemPrice = shop.GetGayaItemPrice(slotIdx)

		item.SelectItem(1, 2, itemVnum)
		itemName = item.GetItemName()

		itemBuyQuestionDialog = uiCommon.QuestionDialog()
		itemBuyQuestionDialog.SetText(localeInfo.DO_YOU_BUY_ITEM(itemName, itemCount, localeInfo.NumberToGayaString(itemPrice)))
		itemBuyQuestionDialog.SetAcceptEvent(lambda arg=True: self.AnswerBuyItem(arg))
		itemBuyQuestionDialog.SetCancelEvent(lambda arg=False: self.AnswerBuyItem(arg))
		itemBuyQuestionDialog.Open()
		itemBuyQuestionDialog.vnum = itemVnum
		itemBuyQuestionDialog.count = itemCount
		itemBuyQuestionDialog.price = itemPrice
		self.itemBuyQuestionDialog = itemBuyQuestionDialog

	def AnswerBuyItem(self, canBuy):
		if canBuy:
			vnum = self.itemBuyQuestionDialog.vnum
			count = self.itemBuyQuestionDialog.count
			price = self.itemBuyQuestionDialog.price
			net.SendChatPacket("/gaya_shop_buy %d %d %d" % (vnum, count, price))

		self.itemBuyQuestionDialog.Close()
		self.itemBuyQuestionDialog = None

	def OnAfterRender(self):
		global_x, global_y = self.currentSlot.GetGlobalPosition()
		for pos in self.disablePosList:
			sx = global_x + pos[0]
			sy = global_y + pos[1]

			grp.SetColor(self.DISABLE_COLOR)
			grp.RenderBar(sx, sy, 32, 32)
