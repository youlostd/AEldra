import net
import player
import item
import snd
import shop
import net
import wndMgr
import app
import chat

import ui
import uiCommon
import mouseModule
import localeInfo

# costume viewer includes
import nonplayer
import constInfo
from uicostumeviewer import CharacterIds, CostumeViewerWindow

###################################################################################################
## Shop
class ShopDialog(ui.ScriptWindow):

	class InputTakeMoneyDialog(ui.BoardWithTitleBar):

		BOARD_WIDTH = 230
		BOARD_HEIGHT = 95

		def __init__(self, maxGold):
			ui.BoardWithTitleBar.__init__(self)
			self.AddFlag("float")
			self.SetSize(self.BOARD_WIDTH, self.BOARD_HEIGHT)
			self.SetTitleName(localeInfo.SHOP_INPUT_TAKE_MONEY_TITLE)

			self.maxGold = maxGold

			questionText = ui.TextLine()
			questionText.SetParent(self)
			questionText.SetPosition(0, 5)
			questionText.SetWindowHorizontalAlignCenter()
			questionText.SetHorizontalAlignCenter()
			questionText.SetText(localeInfo.SHOP_OFFLINE_TAKE_MONEY_QUESTION)
			questionText.Show()
			self.questionText = questionText

			editField = ui.InputField()
			editField.SetParent(self)
			editField.SetPosition(0, 25)
			editField.SetSize(150, 19)
			editField.SetWindowHorizontalAlignCenter()
			editField.Show()
			self.editField = editField

			editLine = ui.EditLine()
			editLine.SetParent(editField)
			editLine.SetPosition(4, 4)
			editLine.SetSize(editField.GetWidth() - 4 * 2, editField.GetHeight() - 4 * 2)
			editLine.SetMax(10)
			editLine.SetNumberMode()
			editLine.SetOverlayText("0")
			editLine.SetEscapeEvent(ui.__mem_func__(self.OnPressEscapeKey))
			editLine.Show()
			self.editLine = editLine

			displayText = ui.TextLine()
			displayText.SetParent(self)
			displayText.SetPosition(0, 49)
			displayText.SetWindowHorizontalAlignCenter()
			displayText.SetHorizontalAlignCenter()
			displayText.Show()
			self.displayText = displayText

			btnOK = ui.Button()
			btnOK.SetParent(self)
			btnOK.SetPosition(20 + (self.GetWidth() - 20 - 25) / 2 - 88 - 5, 3 + 24)
			btnOK.SetUpVisual("d:/ymir work/ui/public/Large_Button_01.sub")
			btnOK.SetOverVisual("d:/ymir work/ui/public/Large_Button_02.sub")
			btnOK.SetDownVisual("d:/ymir work/ui/public/Large_Button_03.sub")
			btnOK.SAFE_SetEvent(self.OnClickOKButton)
			btnOK.SetText(localeInfo.UI_OK)
			btnOK.SetWindowVerticalAlignBottom()
			btnOK.Show()
			self.btnOK = btnOK

			btnCancel = ui.Button()
			btnCancel.SetParent(self)
			btnCancel.SetPosition(20 + (self.GetWidth() - 20 - 25) / 2 + 5, 3 + 24)
			btnCancel.SetUpVisual("d:/ymir work/ui/public/Large_Button_01.sub")
			btnCancel.SetOverVisual("d:/ymir work/ui/public/Large_Button_02.sub")
			btnCancel.SetDownVisual("d:/ymir work/ui/public/Large_Button_03.sub")
			btnCancel.SAFE_SetEvent(self.Close)
			btnCancel.SetText(localeInfo.UI_CLOSE)
			btnCancel.SetWindowVerticalAlignBottom()
			btnCancel.Show()
			self.btnCancel = btnCancel

		def __del__(self):
			ui.BoardWithTitleBar.__del__(self)

		def Open(self):
			self.editLine.SetText("")
			self.OnUpdate()
			self.SetCenterPosition()
			self.Show()
			self.SetTop()

		def Close(self):
			self.editLine.KillFocus()
			self.Hide()

		def SAFE_SetOKEvent(self, event):
			self.okEvent = ui.__mem_func__(event)

		def OnClickOKButton(self):
			if self.okEvent and self.maxGold > 0:
				curYang = self.editLine.GetNumberText()
				if curYang == 0 or curYang > self.maxGold:
					curYang = self.maxGold
				self.okEvent(curYang)
			self.Close()

		def UpdateMaxGold(self, maxGold):
			self.maxGold = maxGold

		def OnUpdate(self):
			curYang = self.editLine.GetNumberText()
			if curYang == 0 or curYang > self.maxGold:
				curYang = self.maxGold
			self.displayText.SetText(localeInfo.SHOP_OFFLINE_TAKE_MONEY_DISPLAY % localeInfo.NumberToMoneyString(curYang))

		def OnPressEscapeKey(self):
			self.Close()
			return True

	def __init__(self):
		ui.ScriptWindow.__init__(self)
		self.isMyOfflineShop = False
		self.isOfflineShop = False
		self.offlineShopGold = 0
		self.tooltipItem = 0
		self.xShopStart = 0
		self.yShopStart = 0
		self.questionDialog = None
		self.offlineTakeMoneyDialog = self.InputTakeMoneyDialog(0)
		self.offlineTakeMoneyDialog.SAFE_SetOKEvent(self.OnTakeOfflineShopMoney)
		self.popup = None
		self.itemBuyQuestionDialog = None
		self.pageBtns = []
		self.selectedPageIdx = 0
		self.wndCostumeViewer = None

	def __del__(self):
		ui.ScriptWindow.__del__(self)

	def __GetPageCount(self):
		tabCount = 1
		for page in xrange(1, shop.SHOP_TAB_COUNT_MAX):
			for i in xrange(shop.SHOP_SLOT_COUNT):
				if shop.GetItemID(page * shop.SHOP_SLOT_COUNT + i) != 0:
					tabCount = 1 + page
		return tabCount

	def Refresh(self):
		if self.isOfflineShop:
			self.itemSlotWindow.ArrangeSlot(0, player.OFFLINE_SHOP_MAX_WIDTH, player.OFFLINE_SHOP_MAX_HEIGHT, 32, 32, 0, 0)
		else:
			self.itemSlotWindow.ArrangeSlot(0, 5, 8, 32, 32, 0, 0)
		self.itemSlotWindow.SetSlotBaseImage("d:/ymir work/ui/public/Slot_Base.sub", 1.0, 1.0, 1.0, 1.0)
		self.board.SetSize(self.itemSlotWindow.GetWidth() + self.itemSlotWindow.GetLeft() * 2, self.board.GetHeight())

		self.__RefreshSlot()

		self.offlineMoneySlot.Hide()
		if self.isMyOfflineShop == False:
			self.btnClose.SetPosition(self.btnClose.GetLeft(), self.baseY)
			self.board.SetSize(self.board.GetWidth(), self.baseHeight)
		else:
			btnY = self.baseY + self.offlineMoneySlot.GetHeight() + 5
			self.offlineMoneySlot.Show()
			self.offlineMoneyText.SetText(localeInfo.NumberToMoneyString(self.offlineShopGold))
			self.btnClose.SetPosition(self.btnClose.GetLeft(), btnY)
			self.board.SetSize(self.board.GetWidth(), self.baseHeight + self.offlineMoneySlot.GetHeight() + 5)
			self.offlineMoneySlot.UpdateRect()

		self.pageBtns = []
		if not self.isOfflineShop:
			pageCount = self.__GetPageCount()
			if pageCount == 1:
				self.btnBuy.Show()
				self.btnSell.Show()
			else:
				self.btnBuy.Hide()
				self.btnSell.Hide()

				for i in xrange(pageCount):
					btn = ui.RadioButton()
					btn.SetParent(self.board)
					btn.SetUpVisual("d:/ymir work/ui/public/small_button_01.sub")
					btn.SetOverVisual("d:/ymir work/ui/public/small_button_02.sub")
					btn.SetDownVisual("d:/ymir work/ui/public/small_button_03.sub")
					btn.SetText(str(i + 1))
					btn.SAFE_SetEvent(self.__OnSelectPage, i)
					btn.Show()

					if self.selectedPageIdx == i:
						btn.Down()

					fullWidth = btn.GetWidth() * pageCount + 5 * (pageCount - 1)
					btn.SetPosition((self.board.GetWidth() - fullWidth) / 2 + (btn.GetWidth() + 5) * i, self.btnBuy.GetTop())

					self.pageBtns.append(btn)
		# else:
			# self.btnSell.Hide()

		self.SetSize(self.board.GetRealWidth(), self.board.GetRealHeight())

	def __RefreshSlot(self):
		getItemID=shop.GetItemID
		getItemCount=shop.GetItemCount
		setItemID=self.itemSlotWindow.SetItemSlot
		maxCount = shop.SHOP_SLOT_COUNT
		if self.isOfflineShop:
			maxCount = player.OFFLINE_SHOP_ITEM_MAX_COUNT
		for i in xrange(maxCount):
			itemCount = getItemCount(self.__ConvertSlot(i))
			if itemCount <= 1:
				itemCount = 0
			setItemID(i, getItemID(self.__ConvertSlot(i)), itemCount)

		self.itemSlotWindow.RefreshSlot()

	def __OnSelectPage(self, pageIdx):
		if len(self.pageBtns) > 0:
			for btn in self.pageBtns:
				btn.SetUp()
			self.pageBtns[pageIdx].Down()

		self.selectedPageIdx = pageIdx
		self.__RefreshSlot()

	def __ConvertSlot(self, slot):
		return self.selectedPageIdx * shop.SHOP_SLOT_COUNT + slot

	def SetItemData(self, pos, itemID, itemCount, itemPrice):
		shop.SetItemData(pos, itemID, itemCount, itemPrice)

	def LoadDialog(self):
		try:
			PythonScriptLoader = ui.PythonScriptLoader()
			PythonScriptLoader.LoadScriptFile(self, "UIScript/shopdialog.py")
		except:
			import exception
			exception.Abort("ShopDialog.LoadDialog.LoadObject")

		try:
			GetObject = self.GetChild
			self.board = GetObject("board")
			self.itemSlotWindow = GetObject("ItemSlot")
			self.offlineMoneySlot = GetObject("OfflineMoney_Slot")
			self.offlineMoneyText = GetObject("OfflineMoney")
			self.btnBuy = GetObject("BuyButton")
			self.btnSell = GetObject("SellButton")
			self.btnClose = GetObject("CloseButton")

			if (app.COMBAT_ZONE):
				self.boardBattleShop = GetObject("BattleShopSubBoard")
				self.curPoints = GetObject("BattleShopSubInfo1")
				self.curLimitPoints = GetObject("BattleShopSubInfo2")
		except:
			import exception
			exception.Abort("ShopDialog.LoadDialog.BindObject")

		self.itemSlotWindow.SetSlotStyle(wndMgr.SLOT_STYLE_NONE)
		self.itemSlotWindow.SAFE_SetButtonEvent("LEFT", "EMPTY", self.SelectEmptySlot)
		self.itemSlotWindow.SAFE_SetButtonEvent("LEFT", "EXIST", self.SelectItemSlot)
		self.itemSlotWindow.SAFE_SetButtonEvent("RIGHT", "EXIST", self.UnselectItemSlot)

		self.itemSlotWindow.SetOverInItemEvent(ui.__mem_func__(self.OverInItem))
		self.itemSlotWindow.SetOverOutItemEvent(ui.__mem_func__(self.OverOutItem))

		self.offlineMoneySlot.SAFE_SetEvent(self.TakeOfflineShopMoney)

		self.btnBuy.SetToggleUpEvent(ui.__mem_func__(self.CancelShopping))
		self.btnBuy.SetToggleDownEvent(ui.__mem_func__(self.OnBuy))

		self.btnSell.SetToggleUpEvent(ui.__mem_func__(self.CancelShopping))
		self.btnSell.SetToggleDownEvent(ui.__mem_func__(self.OnSell))

		self.btnClose.SetEvent(ui.__mem_func__(self.AskClosePrivateShop))

		self.board.SetCloseEvent(ui.__mem_func__(self.Close))

		self.baseHeight = self.board.GetHeight()
		self.baseY = self.btnBuy.GetTop()

		if (app.COMBAT_ZONE):
			self.tabIdx = 0

		self.Refresh()

	def Destroy(self):
		self.Close()
		self.ClearDictionary()

		if self.wndCostumeViewer:
			self.wndCostumeViewer.OnShopClose()
			self.wndCostumeViewer = None

		self.tooltipItem = 0
		self.isOfflineShop = False
		self.isMyOfflineShop = False
		self.itemSlotWindow = 0
		self.offlineShopGold = 0
		self.btnBuy = 0
		self.btnSell = 0
		self.btnClose = 0
		if (app.COMBAT_ZONE):
			self.boardBattleShop = 0
			self.curPoints = 0
			self.curLimitPoints = 0
		self.questionDialog = None
		self.offlineTakeMoneyDialog = None
		self.popup = None

	if (app.COMBAT_ZONE):
		def SetCombatZoneBoard(self, flag):
			if flag:
				self.boardBattleShop.Show()
			else:
				self.boardBattleShop.Hide()
	
		def SetCombatZonePoints(self, points):
			self.curPoints.SetText(localeInfo.COMBAT_ZONE_CURRENT_REAL_POINTS % points)
			
		def SetLimitCombatZonePoints(self, curLimit, maxLimit):
			self.curLimitPoints.SetText(localeInfo.COMBAT_ZONE_LIMIT_SHOP_POINTS % (curLimit, maxLimit))

	if (app.COMBAT_ZONE):
		def Open(self, vid, points, curLimit, maxLimit):

			isPrivateShop = False
			isMainPlayerPrivateShop = False

			import chr
			if vid == 0 or chr.IsNPC(vid):
				isPrivateShop = False
			else:
				isPrivateShop = True

			self.vid = vid
			self.isOfflineShop = False
			self.isMyOfflineShop = False
			self.offlineShopGold = 0

			self.selectedPageIdx = 0

			if player.IsMainCharacterIndex(vid):

				isMainPlayerPrivateShop = True

				self.btnBuy.Hide()
				self.btnSell.Hide()
				self.btnClose.Show()

			else:

				isMainPlayerPrivateShop = False

				self.btnBuy.Show()
				self.btnSell.Show()
				self.btnClose.Hide()

			shop.Open(isPrivateShop, isMainPlayerPrivateShop)
			self.Refresh()
			self.SetTop()
			if shop.SHOP_COIN_TYPE_COMBAT_ZONE == shop.GetTabCoinType(self.tabIdx):
				self.SetCombatZonePoints(points)
				self.SetLimitCombatZonePoints(curLimit, maxLimit)
				self.SetCombatZoneBoard(True)
			else:
				self.SetCombatZoneBoard(False)
			self.Show()

			self.btnBuy.UpdateRect()
			self.btnSell.UpdateRect()
			self.btnClose.UpdateRect()

			(self.xShopStart, self.yShopStart, z) = player.GetMainCharacterPosition()

			# filter shops
			if self.vid and constInfo.COSTUME_VIEWER_ENABLED:

				shopModelVnum = nonplayer.GetRaceNumByVID( self.vid )

				# shop found in list
				if shopModelVnum in constInfo.COSTUME_VIEWER_ENABLE_ON_VNUM:

					if not self.wndCostumeViewer:
						self.wndCostumeViewer = CostumeViewerWindow()

					shopWindowX, shopWindowY = self.GetGlobalPosition()

					self.wndCostumeViewer.SetPosition( shopWindowX - self.wndCostumeViewer.BOARD_WIDTH - self.wndCostumeViewer.MARGIN_RIGHT, shopWindowY )
					#self.wndCostumeViewer.titleName.SetText( constInfo.COSTUME_VIEWER_LABEL )
					self.wndCostumeViewer.Open()
	else:
		def Open(self, vid):

			isPrivateShop = False
			isMainPlayerPrivateShop = False

			import chr
			if vid == 0 or chr.IsNPC(vid):
				isPrivateShop = False
			else:
				isPrivateShop = True

			self.vid = vid
			self.isOfflineShop = False
			self.isMyOfflineShop = False
			self.offlineShopGold = 0

			self.selectedPageIdx = 0

			if player.IsMainCharacterIndex(vid):

				isMainPlayerPrivateShop = True

				self.btnBuy.Hide()
				self.btnSell.Hide()
				self.btnClose.Show()

			else:

				isMainPlayerPrivateShop = False

				self.btnBuy.Show()
				self.btnSell.Show()
				self.btnClose.Hide()

			shop.Open(isPrivateShop, isMainPlayerPrivateShop)
			self.Refresh()
			self.SetTop()
			self.Show()

			self.btnBuy.UpdateRect()
			self.btnSell.UpdateRect()
			self.btnClose.UpdateRect()

			(self.xShopStart, self.yShopStart, z) = player.GetMainCharacterPosition()

			# filter shops
			if self.vid and constInfo.COSTUME_VIEWER_ENABLED:

				shopModelVnum = nonplayer.GetRaceNumByVID( self.vid )

				# shop found in list
				if shopModelVnum in constInfo.COSTUME_VIEWER_ENABLE_ON_VNUM:

					if not self.wndCostumeViewer:
						self.wndCostumeViewer = CostumeViewerWindow()

					shopWindowX, shopWindowY = self.GetGlobalPosition()

					self.wndCostumeViewer.SetPosition( shopWindowX - self.wndCostumeViewer.BOARD_WIDTH - self.wndCostumeViewer.MARGIN_RIGHT, shopWindowY )
					#self.wndCostumeViewer.titleName.SetText( constInfo.COSTUME_VIEWER_LABEL )
					self.wndCostumeViewer.Open()

	def Close(self):
		self.OnCloseQuestionDialog()
		self.offlineTakeMoneyDialog.Close()
		shop.Close()
		net.SendShopEndPacket()
		self.CancelShopping()
		self.tooltipItem.HideToolTip()

		if self.wndCostumeViewer:
			self.wndCostumeViewer.OnShopClose()
		
		self.Hide()

	def UpdateOfflineShopGold(self, gold):
		self.offlineShopGold = gold
		self.offlineTakeMoneyDialog.UpdateMaxGold(gold)
		self.Refresh()

	def AskClosePrivateShop(self):
		questionDialog = uiCommon.QuestionDialog()
		questionDialog.SetText(localeInfo.PRIVATE_SHOP_CLOSE_QUESTION)
		questionDialog.SetAcceptEvent(ui.__mem_func__(self.OnClosePrivateShop))
		questionDialog.SetCancelEvent(ui.__mem_func__(self.OnCloseQuestionDialog))
		questionDialog.Open()
		self.questionDialog = questionDialog

		return True

	def AskTakeOfflineShopMoney(self, money):
		self.offlineTakeMoneyDialog.Open()

		return True

	def OnClosePrivateShop(self):
		if self.isMyOfflineShop == False:
			net.SendChatPacket("/close_shop")
		else:
			shop.SendOfflineShopClosePacket()
		self.OnCloseQuestionDialog()
		return True

	def OnPressEscapeKey(self):
		self.Close()
		return True

	def OnPressExitKey(self):
		self.Close()
		return True

	def OnBuy(self):
		chat.AppendChat(chat.CHAT_TYPE_INFO, localeInfo.SHOP_BUY_INFO)
		app.SetCursor(app.BUY)
		self.btnSell.SetUp()

	def OnSell(self):
		chat.AppendChat(chat.CHAT_TYPE_INFO, localeInfo.SHOP_SELL_INFO)
		app.SetCursor(app.SELL)
		self.btnBuy.SetUp()

	def TakeOfflineShopMoney(self):
		if self.offlineShopGold == 0:
			popup = uiCommon.PopupDialog()
			popup.SetText(localeInfo.SHOP_CANNOT_TAKE_OFFLINE_SHOP_MONEY_NO_MONEY)
			popup.SetAcceptEvent(self.__OnClosePopupDialog)
			popup.Open()
			self.popup = popup
			return
		elif player.GetElk() + self.offlineShopGold > 15000000000:
			popup = uiCommon.PopupDialog()
			popup.SetText(localeInfo.SHOP_CANNOT_TAKE_OFFLINE_SHOP_MONEY)
			popup.SetAcceptEvent(self.__OnClosePopupDialog)
			popup.Open()
			self.popup = popup
			return

		self.AskTakeOfflineShopMoney(localeInfo.NumberToMoneyString(self.offlineShopGold))
		return True

	def OnTakeOfflineShopMoney(self, money):
		shop.SendOfflineShopTakeMoneyPacket(money)
		self.OnCloseQuestionDialog()
		return True

	def CancelShopping(self):
		self.btnBuy.SetUp()
		self.btnSell.SetUp()
		app.SetCursor(app.NORMAL)

	def __OnClosePopupDialog(self):
		self.pop = None

	def SellAttachedItem(self):

		if shop.IsPrivateShop():
			mouseModule.mouseController.DeattachObject()
			return

		if (app.COMBAT_ZONE):
			if shop.SHOP_COIN_TYPE_COMBAT_ZONE == shop.GetTabCoinType(self.tabIdx):
				mouseModule.mouseController.DeattachObject()
				return

		attachedSlotType = mouseModule.mouseController.GetAttachedType()
		attachedSlotPos = mouseModule.mouseController.GetAttachedSlotNumber()
		attachedCount = mouseModule.mouseController.GetAttachedItemCount()
		tchat("AttachedSlotType %d invType %d" % (attachedSlotType, player.SLOT_TYPE_INVENTORY))
		if player.SLOT_TYPE_INVENTORY == attachedSlotType:

			itemIndex = player.GetItemIndex(attachedSlotPos)
			item.SelectItem(1, 2, itemIndex)

			if item.IsAntiFlag(item.ITEM_ANTIFLAG_SELL):
				popup = uiCommon.PopupDialog()
				popup.SetText(localeInfo.SHOP_CANNOT_SELL_ITEM)
				popup.SetAcceptEvent(self.__OnClosePopupDialog)
				popup.Open()
				self.popup = popup

			elif player.IsValuableItem(attachedSlotPos):

				itemPrice = item.GetIBuyItemPrice()

				if item.Is1GoldItem():
					itemPrice = attachedCount / itemPrice / 5
				else:
					itemPrice = itemPrice * max(1, attachedCount) / 5

				itemName = item.GetItemName()

				questionDialog = uiCommon.QuestionDialog()
				questionDialog.SetText(localeInfo.DO_YOU_SELL_ITEM(itemName, attachedCount, itemPrice))

				questionDialog.SetAcceptEvent(lambda arg1=attachedSlotPos, arg2=attachedCount: self.OnSellItem(arg1, arg2))
				questionDialog.SetCancelEvent(ui.__mem_func__(self.OnCloseQuestionDialog))
				questionDialog.Open()
				self.questionDialog = questionDialog

			else:
				self.OnSellItem(attachedSlotPos, attachedCount)

		else:
			snd.PlaySound("sound/ui/loginfail.wav")

		mouseModule.mouseController.DeattachObject()

	def OnSellItem(self, slotPos, count):
		net.SendShopSellPacketNew(slotPos, count)
		snd.PlaySound("sound/ui/money.wav")
		self.OnCloseQuestionDialog()

	def OnCloseQuestionDialog(self):
		if self.questionDialog:
			self.questionDialog.Close()

		self.questionDialog = None

	def SelectEmptySlot(self, selectedSlotPos):

		isAttached = mouseModule.mouseController.isAttached()
		if isAttached:
			self.SellAttachedItem()

	def UnselectItemSlot(self, selectedSlotPos):
		selectedSlotPos = self.__ConvertSlot(selectedSlotPos)

		if shop.IsPrivateShop() or self.isOfflineShop:
			self.AskBuyItem(selectedSlotPos)
		else:
			if (app.COMBAT_ZONE):
				if shop.SHOP_COIN_TYPE_COMBAT_ZONE == shop.GetTabCoinType(self.tabIdx):
					self.AskBuyItem(selectedSlotPos)
				else:
					if self.vid and nonplayer.GetRaceNumByVID(self.vid) in constInfo.COSTUME_VIEWER_ENABLE_ON_VNUM:
						self.AskBuyItemPrice(selectedSlotPos)
					else:
						net.SendShopBuyPacket(selectedSlotPos)	
			else:		
				if self.vid and nonplayer.GetRaceNumByVID(self.vid) in constInfo.COSTUME_VIEWER_ENABLE_ON_VNUM:
					self.AskBuyItemPrice(selectedSlotPos)
				else:
					net.SendShopBuyPacket(selectedSlotPos)

	def SelectItemSlot(self, selectedSlotPos):
		selectedSlotPos = self.__ConvertSlot(selectedSlotPos)

		isAttached = mouseModule.mouseController.isAttached()
		if isAttached:
			self.SellAttachedItem()

		else:

			if True == shop.IsMainPlayerPrivateShop():
				return

			curCursorNum = app.GetCursor()
			if app.BUY == curCursorNum:
				self.AskBuyItem(selectedSlotPos)

			elif app.SELL == curCursorNum:
				chat.AppendChat(chat.CHAT_TYPE_INFO, localeInfo.SHOP_SELL_INFO)

			else:
				selectedItemID = shop.GetItemID(selectedSlotPos)
				itemCount = shop.GetItemCount(selectedSlotPos)

				type = player.SLOT_TYPE_SHOP
				if shop.IsPrivateShop():
					type = player.SLOT_TYPE_PRIVATE_SHOP

				mouseModule.mouseController.AttachObject(self, type, selectedSlotPos, selectedItemID, itemCount)
				mouseModule.mouseController.SetCallBack("INVENTORY", ui.__mem_func__(self.DropToInventory))
				snd.PlaySound("sound/ui/pick.wav")

	def DropToInventory(self):
		attachedSlotPos = mouseModule.mouseController.GetAttachedSlotNumber()
		self.AskBuyItem(attachedSlotPos)

	def AskBuyItem(self, slotPos):
		slotPos = self.__ConvertSlot(slotPos)

		itemIndex = shop.GetItemID(slotPos)
		itemPrice = shop.GetItemPrice(slotPos)
		itemCount = shop.GetItemCount(slotPos)

		item.SelectItem(1, 2, itemIndex)
		itemName = item.GetItemName()

		itemBuyQuestionDialog = uiCommon.QuestionDialog()
		if (app.COMBAT_ZONE):
			if shop.SHOP_COIN_TYPE_COMBAT_ZONE == shop.GetTabCoinType(self.tabIdx):
				itemBuyQuestionDialog.SetText(localeInfo.DO_YOU_BUY_ITEM(itemName, itemCount, localeInfo.NumberToCombatZoneCoinString(itemPrice)))
			else:
				if self.vid == 0 or not player.IsMainCharacterIndex(self.vid):
					itemBuyQuestionDialog.SetText(localeInfo.DO_YOU_BUY_ITEM(itemName, itemCount, localeInfo.NumberToMoneyString(itemPrice)))
				else:
					itemBuyQuestionDialog.SetText(localeInfo.DO_YOU_TAKE_OUT_ITEM(itemName, itemCount))			
		else:
			if self.vid == 0 or not player.IsMainCharacterIndex(self.vid):
				itemBuyQuestionDialog.SetText(localeInfo.DO_YOU_BUY_ITEM(itemName, itemCount, localeInfo.NumberToMoneyString(itemPrice)))
			else:
				itemBuyQuestionDialog.SetText(localeInfo.DO_YOU_TAKE_OUT_ITEM(itemName, itemCount))
		itemBuyQuestionDialog.SetAcceptEvent(lambda arg=True: self.AnswerBuyItem(arg))
		itemBuyQuestionDialog.SetCancelEvent(lambda arg=False: self.AnswerBuyItem(arg))
		itemBuyQuestionDialog.Open()
		itemBuyQuestionDialog.pos = slotPos
		self.itemBuyQuestionDialog = itemBuyQuestionDialog

	def AskBuyItemPrice(self, slotPos):
		slotPos = self.__ConvertSlot(slotPos)

		itemIndex = shop.GetItemID(slotPos)
		itemPrice = shop.GetItemPrice(slotPos)
		itemCount = shop.GetItemCount(slotPos)

		priceVnum = shop.GetItemPriceItem(slotPos)
		item.SelectItem(1, 2, priceVnum)
		priceName = item.GetItemName()

		item.SelectItem(1, 2, itemIndex)
		itemName = item.GetItemName()

		itemBuyQuestionDialog = uiCommon.QuestionDialogMultiLine()
		itemBuyQuestionDialog.SetText(localeInfo.DO_YOU_REALLY_BUY % (itemName, itemPrice, priceName))
		itemBuyQuestionDialog.SetAcceptEvent(lambda arg=True: self.AnswerBuyItem(arg))
		itemBuyQuestionDialog.SetCancelEvent(lambda arg=False: self.AnswerBuyItem(arg))
		itemBuyQuestionDialog.Open()
		itemBuyQuestionDialog.pos = slotPos
		self.itemBuyQuestionDialog = itemBuyQuestionDialog

	def AnswerBuyItem(self, flag):

		if flag:
			pos = self.itemBuyQuestionDialog.pos
			net.SendShopBuyPacket(pos)

		self.itemBuyQuestionDialog.Close()
		self.itemBuyQuestionDialog = None

	def SetItemToolTip(self, tooltipItem):
		self.tooltipItem = tooltipItem

	def OverInItem(self, slotIndex):
		if mouseModule.mouseController.isAttached():
			return

		if 0 != self.tooltipItem:
			self.tooltipItem.SetShopItem(self.__ConvertSlot(slotIndex))

		# costume viewer todo
		if not self.IsShow():
			return

		if not self.wndCostumeViewer:
			return

		if not self.wndCostumeViewer.IsShow():
			return

		realSlotIndex = self.__ConvertSlot( slotIndex )
		itemVnum = shop.GetItemID( realSlotIndex )
		item.SelectItem(1, 2, itemVnum )
		ITEM_TYPE = item.GetItemType( )

		tchat( "Hovered item: " + item.GetItemName( ) )

		if not ITEM_TYPE in (item.ITEM_TYPE_COSTUME, item.ITEM_TYPE_PET, item.ITEM_TYPE_MOUNT):
			tchat( "this item is not a costume or pet or mount !" )
			return

		ITEM_SUB_TYPE = item.GetItemSubType( )

		# what characters can wear it
		ITEM_CHARACTERS = [ CharacterIds.ASSASSINS, CharacterIds.WARRIORS, CharacterIds.SURAS, CharacterIds.SHAMANS ]
		# what sex can wear it
		ITEM_SEX = [ 0, 1 ]

		# anti flag male -> remove male from ITEM_SEX
		if item.IsAntiFlag( item.ITEM_ANTIFLAG_MALE ):
			ITEM_SEX.remove( CharacterIds.SEX_MALE )

		# anti flag female -> remove female from ITEM_SEX
		if item.IsAntiFlag( item.ITEM_ANTIFLAG_FEMALE ):
			ITEM_SEX.remove( CharacterIds.SEX_FEMALE )

		# Someone: get characters that can use it, bit ghetto code
		if item.IsAntiFlag( item.ITEM_ANTIFLAG_WARRIOR ):
			ITEM_CHARACTERS.remove( CharacterIds.WARRIORS )

		if item.IsAntiFlag( item.ITEM_ANTIFLAG_SURA ):
			ITEM_CHARACTERS.remove( CharacterIds.SURAS )

		if item.IsAntiFlag( item.ITEM_ANTIFLAG_ASSASSIN ):
			ITEM_CHARACTERS.remove( CharacterIds.ASSASSINS )

		if item.IsAntiFlag( item.ITEM_ANTIFLAG_SHAMAN ):
			ITEM_CHARACTERS.remove( CharacterIds.SHAMANS )

		tchat( "Item for sex: " + str( ITEM_SEX ) )
		tchat( "Item for characters: " + str( ITEM_CHARACTERS ) )

		# Pets & Mounts
		if ITEM_TYPE in (item.ITEM_TYPE_PET, item.ITEM_TYPE_MOUNT) or (ITEM_TYPE == item.ITEM_TYPE_COSTUME and (ITEM_SUB_TYPE == item.COSTUME_TYPE_MOUNT or ITEM_SUB_TYPE == item.COSTUME_TYPE_PET)):
			tchat( "Item %d ITEM_TYPE %d ITEM_SUB_TYPE %d gets SetMonster func called: " % (itemVnum,ITEM_TYPE,ITEM_SUB_TYPE))
			monsterNum = item.GetValue( 0 )
			self.wndCostumeViewer.SetProperCharacter( ITEM_CHARACTERS, ITEM_SEX, self.wndCostumeViewer.SetMonster, monsterNum  )
		else:
			if ITEM_SUB_TYPE == item.COSTUME_TYPE_WEAPON: # item is costume weapon, check what character can use it only...
				self.wndCostumeViewer.SetProperCharacter( ITEM_CHARACTERS, ITEM_SEX, self.wndCostumeViewer.SetWeapon, itemVnum  )
				#self.wndCostumeViewer.SetWeapon( itemVnum )
			elif ITEM_SUB_TYPE == item.COSTUME_TYPE_HAIR: # item is hairstyle costume, check sex & character
				hairNum = item.GetValue( 3 )
				self.wndCostumeViewer.SetProperCharacter( ITEM_CHARACTERS, ITEM_SEX, self.wndCostumeViewer.SetHair, hairNum  )
			elif ITEM_SUB_TYPE == item.COSTUME_TYPE_BODY: # item is body costume, check sex & character
				self.wndCostumeViewer.SetProperCharacter( ITEM_CHARACTERS, ITEM_SEX, self.wndCostumeViewer.SetArmor, itemVnum  )


	def OverOutItem(self):
		if 0 != self.tooltipItem:
			self.tooltipItem.HideToolTip()

	def OnUpdate(self):

		USE_SHOP_LIMIT_RANGE = 1000

		(x, y, z) = player.GetMainCharacterPosition()
		if abs(x - self.xShopStart) > USE_SHOP_LIMIT_RANGE or abs(y - self.yShopStart) > USE_SHOP_LIMIT_RANGE:
			self.Close()

		# refresh costume viewer position
		if self.wndCostumeViewer and self.wndCostumeViewer.IsShow() and self.IsShow():
			shopWindowX, shopWindowY = self.GetGlobalPosition()

			self.wndCostumeViewer.SetPosition( shopWindowX - self.wndCostumeViewer.BOARD_WIDTH - self.wndCostumeViewer.MARGIN_RIGHT, shopWindowY )
			#self.wndCostumeViewer.Open()

class MallPageDialog(ui.ScriptWindow):
	def __init__(self):
		ui.ScriptWindow.__init__(self)

	def __del__(self):
		ui.ScriptWindow.__del__(self)

	def Destroy(self):
		self.ClearDictionary()

	def Open(self):
		scriptLoader = ui.PythonScriptLoader()
		scriptLoader.LoadScriptFile(self, "uiscript/mallpagedialog.py")

		self.GetChild("titlebar").SetCloseEvent(ui.__mem_func__(self.Close))
		
		(x, y)=self.GetGlobalPosition()
		x+=10
		y+=30
		
		MALL_PAGE_WIDTH = 600
		MALL_PAGE_HEIGHT = 480
		
		app.ShowWebPage(
			"http://metin2.co.kr/08_mall/game_mall/login_fail.htm", 
			(x, y, x+MALL_PAGE_WIDTH, y+MALL_PAGE_HEIGHT))

		self.Lock()
		self.Show()
		
	def Close(self):			
		app.HideWebPage()
		self.Unlock()
		self.Hide()
		
	def OnPressEscapeKey(self):
		self.Close()
		return True
