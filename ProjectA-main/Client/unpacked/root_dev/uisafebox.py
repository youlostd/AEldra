import ui
import mouseModule
import player
import net
import snd
import safebox
import chat
import app
import localeInfo
import uiScriptLocale
import item
import uiCommon
import uiPickMoney
import uiPrivateShopBuilder
import constInfo
import uiInventory

class GuildSafeboxTakeMoneyWindow(ui.ScriptWindow):
	def __init__(self):
		ui.ScriptWindow.__init__(self)

		self.__LoadWindow()

	def __del__(self):
		ui.ScriptWindow.__del__(self)

	def Destroy(self):
		self.ClearDictionary()
		self.Close()

		ui.ScriptWindow.Destroy(self)

	def __LoadWindow(self):
		try:
			pyScrLoader = ui.PythonScriptLoader()
			pyScrLoader.LoadScriptFile(self, "uiscript/guildsafeboxmoneypickwindow.py")
		except:
			import exception
			exception.Abort("GuildChangeTimeWindow.__LoadWindow.LoadScript")

		try:
			GetObject = self.GetChild

			self.board = GetObject("board")
			self.info = GetObject("info")
			self.input = GetObject("input")
			self.give_button = GetObject("give_button")
			self.take_button = GetObject("take_button")
		except:
			import exception
			exception.Abort("GuildChangeTimeWindow.__LoadWindow.BindObject")

		self.board.SetCloseEvent(ui.__mem_func__(self.Close))
		self.give_button.SAFE_SetEvent(self.OnClickGiveButton)
		self.take_button.SAFE_SetEvent(self.OnClickTakeButton)

	def Open(self):
		self.input.SetText("")

		self.SetCenterPosition()
		self.Show()
		self.SetTop()

	def Close(self):
		self.input.KillFocus()
		self.Hide()

	def OnClickGiveButton(self):
		net.SendGuildSafeboxGiveGoldPacket(self.input.GetNumberText())
		self.Close()

	def OnClickTakeButton(self):
		net.SendGuildSafeboxTakeGoldPacket(self.input.GetNumberText())
		self.Close()

	def OnPressEscapeKey(self):
		self.Close()

class GuildSafeboxLogWindow(ui.ScriptWindow):

	class Item(ui.ListBoxEx.Item):
		def __init__(self, interface):
			ui.ListBoxEx.Item.__init__(self)

			self.interface = interface

			self.textLine = ui.ExtendedTextLine()
			self.textLine.SetParent(self)
			self.textLine.SetMouseLeftButtonDownEvent(ui.__mem_func__(self.__CheckForItemLink))
			self.textLine.Show()

		def OnSelectedRender(self):
			pass

		def LoadByIndex(self, index):
			type = safebox.GetGuildLogType(index)
			playerName = safebox.GetGuildLogPlayerName(index)
			time = safebox.GetGuildLogTime(index)
			timeStr = localeInfo.GET_TIME_STRING_BY_TIMESTAMP(time)

			text = "###invalidIndex[%d|%d|%s]" % (index, type, playerName)

			if type == safebox.GUILD_SAFEBOX_LOG_CREATE:
				text = localeInfo.GUILD_SAFEBOX_LOG_TEXT_CREATE % playerName

			elif type == safebox.GUILD_SAFEBOX_LOG_ITEM_GIVE:
				itemVnum, itemCount = safebox.GetGuildLogItemInfo(index)
				itemSocket = ()
				for i in xrange(player.METIN_SOCKET_MAX_NUM):
					itemSocket += (safebox.GetGuildLogItemSocket(index, i),)
				itemAttr = ()
				for i in xrange(player.ATTRIBUTE_SLOT_MAX_NUM):
					attrType, attrVal = safebox.GetGuildLogItemAttribute(index, i)
					itemAttr += (attrType, attrVal)
				itemName = player.GetItemLinkFromData(itemVnum, itemSocket, itemAttr)

				text = localeInfo.GUILD_SAFEBOX_LOG_TEXT_ITEM_GIVE % (playerName, itemCount, itemName)

			elif type == safebox.GUILD_SAFEBOX_LOG_ITEM_TAKE:
				itemVnum, itemCount = safebox.GetGuildLogItemInfo(index)
				itemSocket = ()
				for i in xrange(player.METIN_SOCKET_MAX_NUM):
					itemSocket += (safebox.GetGuildLogItemSocket(index, i),)
				itemAttr = ()
				for i in xrange(player.ATTRIBUTE_SLOT_MAX_NUM):
					attrType, attrVal = safebox.GetGuildLogItemAttribute(index, i)
					itemAttr += (attrType, attrVal)
				itemName = player.GetItemLinkFromData(itemVnum, itemSocket, itemAttr)

				text = localeInfo.GUILD_SAFEBOX_LOG_TEXT_ITEM_TAKE % (playerName, itemCount, itemName)

			elif type == safebox.GUILD_SAFEBOX_LOG_GOLD_GIVE:
				gold = safebox.GetGuildLogGold(index)
				text = localeInfo.GUILD_SAFEBOX_LOG_TEXT_GOLD_GIVE % (playerName, localeInfo.NumberToString(gold))

			elif type == safebox.GUILD_SAFEBOX_LOG_GOLD_TAKE:
				gold = safebox.GetGuildLogGold(index)
				text = localeInfo.GUILD_SAFEBOX_LOG_TEXT_GOLD_TAKE % (playerName, localeInfo.NumberToString(gold))

			elif type == safebox.GUILD_SAFEBOX_LOG_SIZE:
				newSize = safebox.GetGuildLogGold(index)
				text = localeInfo.GUILD_SAFEBOX_LOG_SIZE % (playerName, newSize)

			self.textLine.SetText("%s : %s" % (timeStr, text))

		def __CheckForItemLink(self):
			hyperlink = ui.GetHyperlink()
			if hyperlink:
				self.interface.MakeHyperlinkTooltip(hyperlink)

	def __init__(self, interface):
		ui.ScriptWindow.__init__(self)

		self.interface = interface

		self.__LoadWindow()

	def __del__(self):
		ui.ScriptWindow.__del__(self)

	def Destroy(self):
		self.Close()
		ui.ScriptWindow.Destroy(self)

	def __LoadWindow(self):
		try:
			pyScrLoader = ui.PythonScriptLoader()
			pyScrLoader.LoadScriptFile(self, "uiscript/guildsafeboxlogwindow.py")
		except:
			import exception
			exception.Abort("GuildSafeboxLogWindow.__LoadWindow.LoadScript")

		try:
			GetObject = self.GetChild

			self.board = GetObject("board")

			self.main = {
				"text_list" : GetObject("text_box"),
				"scrollbar" : GetObject("scrollbar"),
			}

		except:
			import exception
			exception.Abort("GuildSafeboxLogWindow.__LoadWindow.BindObject")

		self.board.SetCloseEvent(ui.__mem_func__(self.Close))

		self.main["text_list"].SetScrollBar(self.main["scrollbar"])

	def Open(self):
		self.SetCenterPosition()
		self.Show()
		self.SetTop()

		net.SendChatPacket("/guild_safebox_open_log")

	def Close(self):
		self.Hide()

	def OnPressEscapeKey(self):
		self.Close()
		return True

	def Refresh(self):
		self.RefreshList()

		maxBasePos = self.main["text_list"].GetScrollLen()
		viewCount = self.main["text_list"].GetViewItemCount()
		if maxBasePos > 0:
			self.main["scrollbar"].SetMiddleBarSize(float(viewCount) / float(maxBasePos + viewCount))
		else:
			self.main["scrollbar"].SetMiddleBarSize(1.0)

	def RefreshList(self):
		self.main["text_list"].RemoveAllItems()

		for i in xrange(safebox.GetGuildLogCount()):
			curItem = GuildSafeboxLogWindow.Item(self.interface)
			curItem.LoadByIndex(i)

			self.main["text_list"].AppendItem(curItem, True, False)

		self.main["text_list"].SetBasePos(0)

	def OnAppendItem(self):
		curItem = GuildSafeboxLogWindow.Item(self.interface)
		curItem.LoadByIndex(safebox.GetGuildLogCount() - 1)

		self.main["text_list"].AppendItem(curItem, True)

		maxBasePos = self.main["text_list"].GetScrollLen()
		viewCount = self.main["text_list"].GetViewItemCount()
		if maxBasePos > 0:
			self.main["scrollbar"].SetMiddleBarSize(float(viewCount) / float(maxBasePos + viewCount))
		else:
			self.main["scrollbar"].SetMiddleBarSize(1.0)

class SafeboxWindow(ui.BaseScriptWindow):

	#################################################
	## Initialize FUNCTIONS
	#################################################

	BUTTON_NORMAL = 0
	BUTTON_MALL = 1
	BUTTON_UPP = 2
	BUTTON_SKILL = 3
	BUTTON_STONE = 4
	BUTTON_ENCHANT = 5
	BUTTON_COSTUME = 6
	BUTTON_GUILD = 7

	PAGE_REQUEST_DATA = {
		BUTTON_NORMAL : {
			"cmd_open" : "safebox_open",
			"cmd_close" : "safebox_close",
			"server_delay" : 10, # delay of the server until you can re-open this safebox
			"close_delay" : 20, # delay after closing page to send close command to the server
		},
		BUTTON_MALL : {
			"cmd_open" : "mall_open",
			"cmd_close" : "mall_close",
			"server_delay" : 10, # delay of the server until you can re-open this safebox
			"close_delay" : 10, # delay after closing page to send close command to the server
		},
	}

	SLOT_DATA = {
		BUTTON_NORMAL : {
			"getItemVnum" : safebox.GetItemID,
			"getItemCount" : safebox.GetItemCount,
			"start" : 0,
			"y_size" : safebox.SAFEBOX_SLOT_Y_COUNT,
			"type" : player.SLOT_TYPE_SAFEBOX,
		},
		BUTTON_MALL : {
			"getItemVnum" : safebox.GetMallItemID,
			"getItemCount" : safebox.GetMallItemCount,
			"start" : 0,
			"y_size" : safebox.SAFEBOX_SLOT_Y_COUNT,
			"type" : player.SLOT_TYPE_MALL,
		},
		BUTTON_UPP : {
			"start" : player.UPPITEM_INV_SLOT_START,
			"y_size" : 50 / safebox.SAFEBOX_SLOT_X_COUNT,
			"page_size" : (player.UPPITEM_INV_SLOT_END - player.UPPITEM_INV_SLOT_START) / 50,
			"type" : player.SLOT_TYPE_UPPITEM_INVENTORY,
		},
		BUTTON_SKILL : {
			"start" : player.SKILLBOOK_INV_SLOT_START,
			"y_size" : 50 / safebox.SAFEBOX_SLOT_X_COUNT,
			"page_size" : (player.SKILLBOOK_INV_SLOT_END - player.SKILLBOOK_INV_SLOT_START) / 50,
			"type" : player.SLOT_TYPE_SKILLBOOK_INVENTORY,
		},
		BUTTON_STONE : {
			"start" : player.STONE_INV_SLOT_START,
			"y_size" : 50 / safebox.SAFEBOX_SLOT_X_COUNT,
			"page_size" : (player.STONE_INV_SLOT_END - player.STONE_INV_SLOT_START) / 50,
			"type" : player.SLOT_TYPE_STONE_INVENTORY,
		},
		BUTTON_ENCHANT : {
			"start" : player.ENCHANT_INV_SLOT_START,
			"y_size" : 50 / safebox.SAFEBOX_SLOT_X_COUNT,
			"page_size" : (player.ENCHANT_INV_SLOT_END - player.ENCHANT_INV_SLOT_START) / 50,
			"type" : player.SLOT_TYPE_ENCHANT_INVENTORY,
		},
		BUTTON_COSTUME : {
			"start" : player.COSTUME_INV_SLOT_START,
			"y_size" : 50 / safebox.SAFEBOX_SLOT_X_COUNT,
			"page_size" : (player.COSTUME_INV_SLOT_END - player.COSTUME_INV_SLOT_START) / 50,
			"type" : player.SLOT_TYPE_COSTUME_INVENTORY,
		},
	}

	def __init__(self, interface):
		ui.BaseScriptWindow.__init__(self, "SafeboxWindow", self.__BindObject)
		if not constInfo.EXPANDED_UPPITEM_ENABLE:
			self.SLOT_DATA[self.BUTTON_UPP]["page_size"] = 3

		self.curPage = -1
		self.pageData = {}

		popupDlg = uiCommon.PopupDialog()
		popupDlg.Close()
		self.popupDlg = popupDlg

		dlgPickMoney = uiPickMoney.PickMoneyDialog()
		dlgPickMoney.LoadDialog()
		dlgPickMoney.Hide()
		self.dlgPickMoney = dlgPickMoney

		self.questionDialog = None
		self.tooltipItem = None

		self.heightWithoutSlot = 0
		self.boardHeightWithoutSlot = 0
		self.eventCTRLClickItem = {}
		self.interface = interface

		self.__LoadWindow()


	def __BindObject(self):
		self._AddLoadObject("slot", "slot")
		self._AddLoadObject("loading", "slot_loading")
		self._AddLoadObject("page_btn", "page_btn_window")
		self._AddLoadObject("btn", {
			self.BUTTON_NORMAL : "btn_normal",
			self.BUTTON_MALL : "btn_mall",
			self.BUTTON_UPP : "btn_upp",
			self.BUTTON_SKILL : "btn_skillbook",
			self.BUTTON_STONE : "btn_stone",
			self.BUTTON_ENCHANT : "btn_enchant",
			self.BUTTON_COSTUME : "btn_costume",
			self.BUTTON_GUILD : "btn_guild",
		})
		if constInfo.SORT_AND_STACK_ITEMS_SAFEBOX:
			self._AddLoadObject("board", "board")
			self._AddLoadObject("btn_stack", "SeparateButton")

	def __LoadSlotEvents(self):
		slot = self.main["slot"]
		slot.SetSelectEmptySlotEvent(ui.__mem_func__(self.SelectEmptySlot))
		slot.SetSelectItemSlotEvent(ui.__mem_func__(self.SelectItemSlot))
		slot.SetUnselectItemSlotEvent(ui.__mem_func__(self.UseItemSlot))
		slot.SetUseSlotEvent(ui.__mem_func__(self.UseItemSlot))
		slot.SetOverInItemEvent(ui.__mem_func__(self.OverInItemSlot))
		slot.SetOverOutItemEvent(ui.__mem_func__(self.OverOutItemSlot))

	def __LoadWindow(self):
		self.main["slot"].lockedSlotImages = []
		self.heightWithoutSlot = self.GetHeight() - self.main["slot"].GetHeight()
		self.boardHeightWithoutSlot = self.board.GetHeight() - self.main["slot"].GetHeight()

		for btnIdx in self.main["btn"]:
			btn = self.main["btn"][btnIdx]
			btn.SAFE_SetEvent(self.__SelectPage, btnIdx)
			
		if not safebox.IsGuildEnabled():
			self.main["btn"][self.BUTTON_GUILD].Hide()
		else:
			self.main["btn"][self.BUTTON_GUILD].Show()

		if not player.ENABLE_COSTUME_INVENTORY:
			self.main["btn"][self.BUTTON_COSTUME].Hide()

		# tchat("guild:%d" % safebox.IsGuildEnabled())
		self.__SelectPage(self.BUTTON_UPP)

		if constInfo.SORT_AND_STACK_ITEMS_SAFEBOX:
			self.main["board"].titleBar.SetWidth(166 - 38)
			self.main["board"].titleBar.SetPosition(8 + 38, 7)
			self.main["btn_stack"].SAFE_SetEvent(self.__StackItems)

		self.questionWnd = uiCommon.QuestionDialog()
		self.questionWnd.SAFE_SetAcceptEvent(self.__StackItemsRequest)
		self.questionWnd.SAFE_SetCancelEvent(self.questionWnd.Close)
		self.questionWnd.SetText(localeInfo.CONFIRM_STACK)

	if constInfo.SORT_AND_STACK_ITEMS_SAFEBOX:
		def __StackItems(self):
			self.questionWnd.Open()

		def __StackItemsRequest(self):
			window = player.SlotTypeToInvenType(self.SLOT_DATA[self.curPage]["type"])
			net.SendChatPacket("/stack %d" % window)
			net.SendChatPacket("/sort %d" % window)
			self.questionWnd.Close()

	def Close(self):
		self.__SetPageData("page_close", app.GetTime())
		self.popupDlg.Close()
		if self.dlgPickMoney:
			self.dlgPickMoney.Close()
		if self.tooltipItem:
			self.tooltipItem.HideToolTip()
		self.OnCloseQuestionDialog()

		ui.BaseScriptWindow.Close(self)

	def Destroy(self):
		self.dlgPickMoney.Destroy()
		self.dlgPickMoney = None

		ui.BaseScriptWindow.Destroy(self)

	#################################################
	## Slot Event FUNCTIONS
	#################################################

	def SelectEmptySlot(self, selectedSlotPos):
		selectedSlotPos = self.__LocalPosToGlobalPos(selectedSlotPos)

		if mouseModule.mouseController.isAttached():
			attachedSlotType = mouseModule.mouseController.GetAttachedType()
			attachedSlotPos = mouseModule.mouseController.GetAttachedSlotNumber()
			attachedItemCount = mouseModule.mouseController.GetAttachedItemCount()

			############################################
			## SAFEBOX HANDLING
			if self.curPage == self.BUTTON_NORMAL:

				if player.SLOT_TYPE_INVENTORY == attachedSlotType:

					if player.ITEM_MONEY == mouseModule.mouseController.GetAttachedItemIndex():
						net.SendSafeboxSaveMoneyPacket(mouseModule.mouseController.GetAttachedItemCount())
						snd.PlaySound("sound/ui/money.wav")

					else:
						window = player.GetWindowBySlot(attachedSlotPos)
						net.SendSafeboxCheckinPacket(window, attachedSlotPos, selectedSlotPos)
						#snd.PlaySound("sound/ui/drop.wav")

				elif player.SLOT_TYPE_SAFEBOX == attachedSlotType:

					net.SendSafeboxItemMovePacket(attachedSlotPos, selectedSlotPos, 0)
					#snd.PlaySound("sound/ui/drop.wav")

			############################################
			## MALL HANDLING
			elif self.curPage == self.BUTTON_MALL:

				chat.AppendChat(chat.CHAT_TYPE_INFO, localeInfo.MALL_CANNOT_INSERT)

			############################################
			## GENERAL HANDLING
			elif self.curPage in (self.BUTTON_UPP, self.BUTTON_SKILL, self.BUTTON_STONE, self.BUTTON_ENCHANT, self.BUTTON_COSTUME):

				if player.SLOT_TYPE_INVENTORY == attachedSlotType or self.SLOT_DATA[self.curPage]["type"] == attachedSlotType:
					self.__SendMoveItemPacket(player.GetWindowBySlot(attachedSlotPos), attachedSlotPos, selectedSlotPos, attachedItemCount)

				elif player.SLOT_TYPE_PRIVATE_SHOP == attachedSlotType or player.SLOT_TYPE_AUCTION_SHOP == attachedSlotType:
					mouseModule.mouseController.RunCallBack("INVENTORY", selectedSlotPos)

				elif player.SLOT_TYPE_SHOP == attachedSlotType:
					net.SendShopBuyPacket(attachedSlotPos)

				elif player.SLOT_TYPE_SAFEBOX == attachedSlotType:
					net.SendSafeboxCheckoutPacket(attachedSlotPos, player.GetWindowBySlot(selectedSlotPos), selectedSlotPos)

				elif player.SLOT_TYPE_MALL == attachedSlotType:
					net.SendMallCheckoutPacket(attachedSlotPos, selectedSlotPos)

				elif player.SLOT_TYPE_GUILD_SAFEBOX == attachedSlotType:
					net.SendGuildSafeboxCheckoutPacket(attachedSlotPos, player.GetWindowBySlot(selectedSlotPos), selectedSlotPos)

			mouseModule.mouseController.DeattachObject()

	def SelectItemSlot(self, selectedSlotPos):
		selectedSlotPos = self.__LocalPosToGlobalPos(selectedSlotPos)

		if mouseModule.mouseController.isAttached():
			attachedSlotType = mouseModule.mouseController.GetAttachedType()
			attachedSlotPos = mouseModule.mouseController.GetAttachedSlotNumber()
			attachedItemCount = mouseModule.mouseController.GetAttachedItemCount()
			attachedItemVID = mouseModule.mouseController.GetAttachedItemIndex()

			############################################
			## SAFEBOX HANDLING
			if self.curPage == self.BUTTON_NORMAL:

				if player.SLOT_TYPE_INVENTORY == attachedSlotType:

					if player.ITEM_MONEY == attachedItemVID:
						net.SendSafeboxSaveMoneyPacket(attachedItemCount)
						snd.PlaySound("sound/ui/money.wav")

				mouseModule.mouseController.DeattachObject()

			############################################
			## MALL HANDLING
			if self.curPage == self.BUTTON_MALL:

				chat.AppendChat(chat.CHAT_TYPE_INFO, localeInfo.MALL_CANNOT_INSERT)

			############################################
			## GENERAL HANDLING
			elif self.curPage in (self.BUTTON_UPP, self.BUTTON_SKILL, self.BUTTON_STONE, self.BUTTON_ENCHANT, self.BUTTON_COSTUME):

				if player.SLOT_TYPE_INVENTORY == attachedSlotType or attachedSlotType == self.SLOT_DATA[self.curPage]["type"]:
					if attachedSlotPos != selectedSlotPos:
						self.__SendMoveItemPacket(player.GetWindowBySlot(attachedSlotPos), attachedSlotPos, selectedSlotPos, 0)

			mouseModule.mouseController.DeattachObject()

		elif (app.IsPressed(app.DIK_LCONTROL) or app.IsPressed(app.DIK_RCONTROL)) and self.eventCTRLClickItem.has_key(self.curPage):
			self.eventCTRLClickItem[self.curPage](selectedSlotPos)

		elif self.SLOT_DATA.has_key(self.curPage):
			slotData = self.SLOT_DATA[self.curPage]

			############################################
			## GENERAL HANDLING
			if self.curPage in (self.BUTTON_UPP, self.BUTTON_SKILL, self.BUTTON_STONE, self.BUTTON_ENCHANT, self.BUTTON_COSTUME):

				curCursorNum = app.GetCursor()
				if app.SELL == curCursorNum:
					self.__SellItem(selectedSlotPos)
					return

				elif app.BUY == curCursorNum:
					chat.AppendChat(chat.CHAT_TYPE_INFO, localeInfo.SHOP_BUY_INFO)
					return

				elif app.IsPressed(app.DIK_LALT):
					link = player.GetItemLink(selectedSlotPos)
					ime.PasteString(link)
					return

				elif app.IsPressed(app.DIK_LSHIFT):
					itemCount = player.GetItemCount(selectedSlotPos)
					
					if itemCount > 1:
						self.dlgPickMoney.SetTitleName(localeInfo.PICK_ITEM_TITLE)
						self.dlgPickMoney.SetAcceptEvent(ui.__mem_func__(self.OnPickItem))
						self.dlgPickMoney.Open(itemCount)
						self.dlgPickMoney.itemGlobalSlotIndex = selectedSlotPos
						return

			getItemVnum = player.GetItemIndex
			if slotData.has_key("getItemVnum"):
				getItemVnum = slotData["getItemVnum"]

			selectedItemID = getItemVnum(selectedSlotPos)
			itemCount = player.GetItemCount(selectedSlotPos)
			mouseModule.mouseController.AttachObject(self, slotData["type"], selectedSlotPos, selectedItemID, itemCount)
			snd.PlaySound("sound/ui/pick.wav")

	def UseItemSlot(self, slotIndex):
		slotIndex = self.__LocalPosToGlobalPos(slotIndex)

		############################################
		## SAFEBOX / MALL HANDLING
		if self.curPage in (self.BUTTON_NORMAL, self.BUTTON_MALL):

			mouseModule.mouseController.DeattachObject()

		############################################
		## GENERAL HANDLING
		elif self.curPage in (self.BUTTON_UPP, self.BUTTON_SKILL, self.BUTTON_STONE, self.BUTTON_ENCHANT, self.BUTTON_COSTUME):

			curCursorNum = app.GetCursor()
			if app.SELL == curCursorNum:
				return

			if constInfo.GET_ITEM_DROP_QUESTION_DIALOG_STATUS():
				return

			if app.IsPressed(app.DIK_LCONTROL) and player.GetItemCount(slotIndex) > 1:
				itemCount = player.GetItemCount(slotIndex)
				itemVnum = player.GetItemIndex(slotIndex)
				itemName = "#ITEM#"
				if item.SelectItem(1, 2, itemVnum):
					itemName = item.GetItemName()

				if self.questionDialog:
					self.questionDialog.Close()
					self.questionDialog = None

				self.questionDialog = uiCommon.QuestionDialog()
				self.questionDialog.SetText(localeInfo.DO_YOU_USE_MULTI_ITEM % (itemCount, itemName))
				self.questionDialog.SetAcceptEvent(ui.__mem_func__(self.MultiUseItemSlot))
				self.questionDialog.SetCancelEvent(ui.__mem_func__(self.OnCloseQuestionDialog))
				self.questionDialog.Open()
				self.questionDialog.index = slotIndex
				self.questionDialog.vnum = itemVnum
				self.questionDialog.count = itemCount
				return

			self.__UseItem(slotIndex)
			mouseModule.mouseController.DeattachObject()
			self.OverOutItemSlot()

	def OverInItemSlot(self, slotIndex):
		slotIndex = self.__LocalPosToGlobalPos(slotIndex)

		self.main["slot"].SetUseMode(False)
		self.main["slot"].SetUsableItem(False)
		self.main["slot"].SetUsableItem2(False)

		if mouseModule.mouseController.isAttached():
			attachedItemType = mouseModule.mouseController.GetAttachedType()
			attachedSlotPos = mouseModule.mouseController.GetAttachedSlotNumber()
			attachedItemVNum = mouseModule.mouseController.GetAttachedItemIndex()

			if player.SLOT_TYPE_INVENTORY == attachedItemType:
				if self.__CanUseSrcItemToDstItem(attachedItemVNum, attachedSlotPos, slotIndex):
					self.main["slot"].SetUsableItem(True)
					self.main["slot"].SetUseMode(True)
			# ENABLE_ITEM_SWAP_SYSTEM
			elif self.SLOT_DATA[self.curPage]["type"] == attachedItemType:
				srcItem = player.GetItemIndex(attachedSlotPos)
				item.SelectItem(1, 2, srcItem)
				item1_size = str(item.GetItemSize())
				
				dstItem = player.GetItemIndex(slotIndex)
				item.SelectItem(1, 2, dstItem)
				item2_size = str(item.GetItemSize())
				
				if item2_size == item1_size:
					if attachedSlotPos != slotIndex:
						self.main["slot"].SetUsableItem2(True)
				
				elif item1_size == "(1, 2)":
					if attachedSlotPos != slotIndex:
						if item2_size == "(1, 1)":
							second_item = player.GetItemIndex(slotIndex+5)
							item.SelectItem(1, 2, second_item)
							second_item_size = str(item.GetItemSize())
							if second_item_size != "(1, 2)" and second_item_size != "(1, 3)":
								self.main["slot"].SetUsableItem2(True)
								
				elif item1_size == "(1, 3)":
					if attachedSlotPos != slotIndex:
						if item2_size == "(1, 1)":
							second_item = player.GetItemIndex(slotIndex+5)
							item.SelectItem(1, 2, second_item)
							second_item_size = str(item.GetItemSize())
							
							if second_item_size != "(1, 3)":
								third_item = player.GetItemIndex(slotIndex+10)
								item.SelectItem(1, 2, third_item)
								third_item_size = str(item.GetItemSize())
								
								if third_item_size != "(1, 2)" and third_item_size != "(1, 3)":
									self.main["slot"].SetUsableItem2(True)

						elif item2_size == "(1, 2)":
							second_item = player.GetItemIndex(slotIndex+10)
							item.SelectItem(1, 2, second_item)
							second_item_size = str(item.GetItemSize())
							
							if second_item_size != "(1, 2)" and second_item_size != "(1, 3)":
								self.main["slot"].SetUsableItem2(True)
			# ENABLE_ITEM_SWAP_SYSTEM

		if not self.tooltipItem:
			return

		if self.curPage == self.BUTTON_NORMAL:
			self.tooltipItem.SetSafeBoxItem(slotIndex)
		elif self.curPage == self.BUTTON_MALL:
			self.tooltipItem.SetMallItem(slotIndex)
		elif self.curPage in (self.BUTTON_UPP, self.BUTTON_SKILL, self.BUTTON_STONE, self.BUTTON_ENCHANT, self.BUTTON_COSTUME):
			self.tooltipItem.SetInventoryItem(slotIndex)

	def OverOutItemSlot(self):
		if not self.tooltipItem:
			return

		self.tooltipItem.HideToolTip()

	#################################################
	## Action Request FUNCTIONS
	#################################################
	
	def __SendMoveItemPacket(self, srcWindow, srcSlotPos, dstSlotPos, srcItemCount):
		if uiPrivateShopBuilder.IsBuildingPrivateShop():
			chat.AppendChat(chat.CHAT_TYPE_INFO, localeInfo.MOVE_ITEM_FAILURE_PRIVATE_SHOP)
			return

		net.SendItemMovePacket(srcWindow, srcSlotPos, player.GetWindowBySlot(dstSlotPos), dstSlotPos, srcItemCount)

	def __SendUseItemToItemPacket(self, srcSlotPos, dstSlotPos):
		if uiPrivateShopBuilder.IsBuildingPrivateShop():
			chat.AppendChat(chat.CHAT_TYPE_INFO, localeInfo.USE_ITEM_FAILURE_PRIVATE_SHOP)
			return

		net.SendItemUseToItemPacket(player.GetWindowBySlot(srcSlotPos), srcSlotPos, player.GetWindowBySlot(dstSlotPos), dstSlotPos)

	def __SellItem(self, itemSlotPos):
		if not player.IsEquipmentSlot(itemSlotPos):
			self.sellingSlotNumber = itemSlotPos
			itemIndex = player.GetItemIndex(itemSlotPos)
			itemCount = player.GetItemCount(itemSlotPos)

			self.sellingSlotitemIndex = itemIndex
			self.sellingSlotitemCount = itemCount

			item.SelectItem(1, 2, itemIndex)
			itemPrice = item.GetIBuyItemPrice()

			if item.Is1GoldItem():
				itemPrice = itemCount / itemPrice / 5
			else:
				itemPrice = itemPrice * itemCount / 5

			item.GetItemName(itemIndex)
			itemName = item.GetItemName()

			self.questionDialog = uiCommon.QuestionDialog()
			self.questionDialog.SetText(localeInfo.DO_YOU_SELL_ITEM(itemName, itemCount, itemPrice))
			self.questionDialog.SetAcceptEvent(ui.__mem_func__(self.SellItem))
			self.questionDialog.SetCancelEvent(ui.__mem_func__(self.OnCloseQuestionDialog))
			self.questionDialog.Open()
			self.questionDialog.count = itemCount
		
			constInfo.SET_ITEM_DROP_QUESTION_DIALOG_STATUS(1)

	def SellItem(self):
		if self.sellingSlotitemIndex == player.GetItemIndex(self.sellingSlotNumber):
			if self.sellingSlotitemCount == player.GetItemCount(self.sellingSlotNumber):
				net.SendShopSellPacketNew(self.sellingSlotNumber, self.questionDialog.count)
				snd.PlaySound("sound/ui/money.wav")

		self.OnCloseQuestionDialog()

	def __OnClosePopupDialog(self):
		self.pop = None
		
	def OnCloseQuestionDialog(self):
		if not self.questionDialog:
			return
		
		self.questionDialog.Close()
		self.questionDialog = None
		constInfo.SET_ITEM_DROP_QUESTION_DIALOG_STATUS(0)

	def OnPickItem(self, count):
		itemSlotIndex = self.dlgPickMoney.itemGlobalSlotIndex
		selectedItemVNum = player.GetItemIndex(itemSlotIndex)
		mouseModule.mouseController.AttachObject(self, player.SLOT_TYPE_INVENTORY, itemSlotIndex, selectedItemVNum, count)

	def __UseItem(self, slotIndex):
		ItemVNum = player.GetItemIndex(slotIndex)
		item.SelectItem(1, 2, ItemVNum)
		if item.IsFlag(item.ITEM_FLAG_CONFIRM_WHEN_USE):
			self.questionDialog = uiCommon.QuestionDialog()
			self.questionDialog.SetText(localeInfo.INVENTORY_REALLY_USE_ITEM)
			self.questionDialog.SetAcceptEvent(ui.__mem_func__(self.__UseItemQuestionDialog_OnAccept))
			self.questionDialog.SetCancelEvent(ui.__mem_func__(self.OnCloseQuestionDialog))
			self.questionDialog.Open()
			self.questionDialog.slotIndex = slotIndex
		
			constInfo.SET_ITEM_DROP_QUESTION_DIALOG_STATUS(1)

		else:
			self.__SendUseItemPacket(slotIndex)	

	def __UseItemQuestionDialog_OnAccept(self):
		self.__SendUseItemPacket(self.questionDialog.slotIndex)
		self.OnCloseQuestionDialog()

	def __SendUseItemPacket(self, slotPos):
		if uiPrivateShopBuilder.IsBuildingPrivateShop():
			chat.AppendChat(chat.CHAT_TYPE_INFO, localeInfo.USE_ITEM_FAILURE_PRIVATE_SHOP)
			return

		net.SendItemUsePacket(player.GetWindowBySlot(slotPos), slotPos)

	def MultiUseItemSlot(self):
		index = self.questionDialog.index
		vnum = self.questionDialog.vnum
		count = self.questionDialog.count

		self.OnCloseQuestionDialog()

		if player.GetItemIndex(index) != vnum:
			return

		if player.GetItemCount(index) < count:
			return

		self.__SendUseMultiItemPacket(index, count)

	def __SendUseMultiItemPacket(self, slotPos, count):
		if uiPrivateShopBuilder.IsBuildingPrivateShop():
			chat.AppendChat(chat.CHAT_TYPE_INFO, localeInfo.USE_ITEM_FAILURE_PRIVATE_SHOP)
			return

		net.SendItemMultiUsePacket(player.GetWindowBySlot(slotPos), slotPos, count)

	def AppendOwnerItem(self, itemSlotPos, onlyStack = True):
		itemID = player.GetItemIndex(itemSlotPos)
		item.SelectItem(1, 2, itemID)

		itemWidth, itemHeight = item.GetItemSize()
		isStackable = item.IsStackable()

		if self.curPage == self.BUTTON_MALL:
			chat.AppendChat(chat.CHAT_TYPE_INFO, localeInfo.MALL_CANNOT_INSERT)
			return

		if not self.SLOT_DATA.has_key(self.curPage):
			return

		slotData = self.SLOT_DATA[self.curPage]
		startPos = slotData["start"]
		getItemVnum = player.GetItemIndex
		if slotData.has_key("getItemVnum"):
			getItemVnum = slotData["getItemVnum"]

		for pageId in xrange(self.__GetPageData("size", 1)):
			for i in xrange((slotData["y_size"] - itemHeight + 1) * safebox.SAFEBOX_SLOT_X_COUNT):
				slot = startPos + pageId * (slotData["y_size"] * safebox.SAFEBOX_SLOT_X_COUNT) + i
				if onlyStack and getItemVnum(slot) == 0:
					continue

				itemCountSafebox = safebox.GetItemCount(i)
				if itemCountSafebox > 0:
					if itemCountSafebox + player.GetItemCount(itemSlotPos) > constInfo.ITEM_MAX_COUNT:
						continue

				failed = False
				for j in xrange(itemHeight):
					curVnum = getItemVnum(slot + j * safebox.SAFEBOX_SLOT_X_COUNT)
					if curVnum != 0:
						if j == 0 and itemHeight == 1 and curVnum == itemID and isStackable:
							continue

						failed = True
						break

				for j in xrange(1, 3):
					curSlot = slot - j * safebox.SAFEBOX_SLOT_X_COUNT
					if curSlot < 0 or curSlot / safebox.SAFEBOX_PAGE_SIZE != slot / safebox.SAFEBOX_PAGE_SIZE:
						break

					curVnum = getItemVnum(curSlot)
					if curVnum != 0:
						item.SelectItem(1, 2, curVnum)
						curWidth, curHeight = item.GetItemSize()
						if curHeight >= 1 + j:
							failed = True
						break

				if not failed and player.GetItemCount(slot) < constInfo.ITEM_MAX_COUNT:
					window = player.GetWindowBySlot(itemSlotPos)
					if self.curPage == self.BUTTON_NORMAL:
						net.SendSafeboxCheckinPacket(window, itemSlotPos, slot)
					else:
						self.__SendMoveItemPacket(window, itemSlotPos, slot, player.GetItemCount(itemSlotPos))
					return

		if onlyStack:
			self.AppendOwnerItem(itemSlotPos, False)

	#################################################
	## Function linking FUNCTIONS
	#################################################

	def SetCTRLClickItemEvent(self, window, event):
		self.eventCTRLClickItem[window] = event

	def SetItemToolTip(self, tooltip):
		self.tooltipItem = tooltip

	#################################################
	## General FUNCTIONS
	#################################################

	def __LocalPosToGlobalPos(self, localPos):
		if not self.SLOT_DATA.has_key(self.curPage):
			return localPos

		slotData = self.SLOT_DATA[self.curPage]
		localPos += slotData["start"]

		subPage = self.__GetPageData("sub_page", 0)
		if subPage == 0:
			return localPos

		pageSize = safebox.SAFEBOX_SLOT_X_COUNT * slotData["y_size"]
		return localPos + self.__GetPageData("sub_page", 0) * pageSize

	def __GetPageData(self, key, default=None, page=-1):
		if page == -1:
			page = self.curPage

		if not self.pageData.has_key(page):
			if default:
				self.__SetPageData(key, default, page)
			return default

		if not self.pageData[page].has_key(key):
			if default:
				self.__SetPageData(key, default, page)
			return default

		return self.pageData[page][key]

	def __SetPageData(self, key, val, page=-1):
		if page == -1:
			page = self.curPage

		if not self.pageData.has_key(page):
			self.pageData[page] = {}

		pageData = self.pageData[page]
		pageData[key] = val

	def __CanOpenPage(self, pageIdx):
		if self.PAGE_REQUEST_DATA.has_key(pageIdx):
			requestData = self.PAGE_REQUEST_DATA[pageIdx]

			isOpen = self.__GetPageData("is_open", False, pageIdx)
			if isOpen:
				return True

			lastClose = self.__GetPageData("server_close", 0, pageIdx)
			if lastClose > 0 and app.GetTime() - lastClose < requestData["server_delay"] + 1: # + 1 sec to make sure server is ready
				self.popupDlg.SetText(localeInfo.SAFEBOX_NEW_CANNOT_OPEN_DELAY)
				self.popupDlg.Open()
				return False

		return True

	def SelectPage(self, pageIdx):
		self.__SelectPage(pageIdx)

	def __SelectPage(self, pageIdx):
		if self.BUTTON_GUILD == pageIdx:
			self.interface.ToggleGuildSafeboxWindow()
			return

		if not self.__CanOpenPage(pageIdx):
			self.main["btn"][pageIdx].SetUp()
			return

		if self.curPage != -1:
			self.__SetPageData("page_close", app.GetTime())

		self.curPage = pageIdx

		for btnIdx in self.main["btn"]:
			btn = self.main["btn"][btnIdx]
			if btn.IsDisabled():
				continue

			if btnIdx == pageIdx:
				btn.Down()
			else:
				btn.SetUp()

		if not self.__GetPageData("size"):
			if self.SLOT_DATA.has_key(self.curPage):
				slotData = self.SLOT_DATA[self.curPage]
				if slotData.has_key("page_size"):
					self.__SetPageData("size", slotData["page_size"])

		self.__RefreshSlotStyle()
		self.__RefreshPageButtons()
		self.__SelectSubPage(self.__GetPageData("sub_page", 0))

		if constInfo.SORT_AND_STACK_ITEMS_SAFEBOX:
			if self.curPage in [ self.BUTTON_NORMAL, self.BUTTON_MALL, self.BUTTON_COSTUME, self.BUTTON_GUILD ]:
				self.main["btn_stack"].Hide()
			else:
				self.main["btn_stack"].Show()

	def __SelectSubPage(self, subPageIdx):
		btnList = self.main["page_btn"].btnList

		if subPageIdx < 0:
			subPageIdx = 0
		if subPageIdx >= len(btnList):
			subPageIdx = len(btnList) - 1

		self.__SetPageData("sub_page", subPageIdx)

		for i in xrange(len(btnList)):
			btn = btnList[i]
			if i == subPageIdx:
				btn.Down()
			else:
				btn.SetUp()

		self.RefreshSafeboxMaxNum()

		self.Refresh()

	def RefreshSafeboxMaxNum(self):
		if self.curPage == self.BUTTON_UPP:
			slotData = self.SLOT_DATA[self.curPage]
			slot = self.main["slot"]
			pageSize = safebox.SAFEBOX_SLOT_X_COUNT * slotData["y_size"]
			startPos = self.__GetPageData("sub_page", 0) * pageSize

			for i in xrange(slotData["y_size"]):
				currPos = startPos + i * safebox.SAFEBOX_SLOT_X_COUNT
				if currPos >= player.GetUppitemInventoryMaxNum():
					slot.lockedSlotImages[i].Show()
				else:
					slot.lockedSlotImages[i].Hide()
		if self.curPage == self.BUTTON_SKILL:
			slotData = self.SLOT_DATA[self.curPage]
			slot = self.main["slot"]
			pageSize = safebox.SAFEBOX_SLOT_X_COUNT * slotData["y_size"]
			startPos = self.__GetPageData("sub_page", 0) * pageSize

			for i in xrange(slotData["y_size"]):
				currPos = startPos + i * safebox.SAFEBOX_SLOT_X_COUNT
				if currPos >= player.GetSkillbookInventoryMaxNum():
					slot.lockedSlotImages[i].Show()
				else:
					slot.lockedSlotImages[i].Hide()
		if self.curPage == self.BUTTON_STONE:
			slotData = self.SLOT_DATA[self.curPage]
			slot = self.main["slot"]
			pageSize = safebox.SAFEBOX_SLOT_X_COUNT * slotData["y_size"]
			startPos = self.__GetPageData("sub_page", 0) * pageSize

			for i in xrange(slotData["y_size"]):
				currPos = startPos + i * safebox.SAFEBOX_SLOT_X_COUNT
				if currPos >= player.GetStoneInventoryMaxNum():
					slot.lockedSlotImages[i].Show()
				else:
					slot.lockedSlotImages[i].Hide()
		if self.curPage == self.BUTTON_ENCHANT:
			slotData = self.SLOT_DATA[self.curPage]
			slot = self.main["slot"]
			pageSize = safebox.SAFEBOX_SLOT_X_COUNT * slotData["y_size"]
			startPos = self.__GetPageData("sub_page", 0) * pageSize

			for i in xrange(slotData["y_size"]):
				currPos = startPos + i * safebox.SAFEBOX_SLOT_X_COUNT
				if currPos >= player.GetEnchantInventoryMaxNum():
					slot.lockedSlotImages[i].Show()
				else:
					slot.lockedSlotImages[i].Hide()

	def Update(self):
		for pageIdx in self.PAGE_REQUEST_DATA:
			if self.IsShow() and self.curPage == pageIdx:
				continue

			requestData = self.PAGE_REQUEST_DATA[pageIdx]
			if self.__GetPageData("is_open", False, pageIdx):
				page_close = self.__GetPageData("page_close", 0, pageIdx)
				closeDelay = requestData["close_delay"]
				if not self.IsShow():
					closeDelay = 1.5
				if app.GetTime() - page_close >= closeDelay:
					net.SendChatPacket("/" + requestData["cmd_close"])
					self.__SetPageData("is_open", False, pageIdx)
					self.__SetPageData("server_close", app.GetTime(), pageIdx)

					if self.curPage == pageIdx:
						self.__SelectPage(self.BUTTON_UPP)

					tchat("Request close Page [%d]" % pageIdx)

	def __CanUseSrcItemToDstItem(self, srcItemVNum, srcSlotPos, dstSlotPos):
		if srcSlotPos == dstSlotPos:
			return False

		if item.IsRefineScroll(srcItemVNum):
			if player.REFINE_OK == player.CanRefine(srcItemVNum, dstSlotPos):
				return True
			if srcItemVNum == player.GetItemIndex(dstSlotPos) and player.GetItemCount(dstSlotPos) < 200:
				return True
		if item.IsMetin(srcItemVNum):
			if player.ATTACH_METIN_OK == player.CanAttachMetin(srcItemVNum, dstSlotPos):
				return True
			if srcItemVNum == player.GetItemIndex(dstSlotPos) and player.GetItemCount(dstSlotPos) < 200:
				return True
		if item.IsArrow(srcItemVNum):
			if item.IsQuiver(player.GetItemIndex(dstSlotPos)):
				quiverArrowVnum = player.GetItemMetinSocket(dstSlotPos, 0)
				if quiverArrowVnum == 0 or quiverArrowVnum == srcItemVNum:
					return True
		if item.IsDetachScroll(srcItemVNum):
			if player.DETACH_METIN_OK == player.CanDetach(srcItemVNum, dstSlotPos):
				return True
			if srcItemVNum == player.GetItemIndex(dstSlotPos) and player.GetItemCount(dstSlotPos) < 200:
				return True
		if item.IsKey(srcItemVNum):
			if player.CanUnlock(srcItemVNum, dstSlotPos):
				return True
			if srcItemVNum == player.GetItemIndex(dstSlotPos) and player.GetItemCount(dstSlotPos) < 200:
				return True
		if (player.GetItemFlags(srcSlotPos) & uiInventory.ITEM_FLAG_APPLICABLE) == uiInventory.ITEM_FLAG_APPLICABLE:
			return True

		else:
			useType=item.GetUseType(srcItemVNum)

			if "USE_CLEAN_SOCKET" == useType:
				if self.__CanCleanBrokenMetinStone(dstSlotPos):
					return True
			elif "USE_CHANGE_ATTRIBUTE" == useType:
				if srcItemVNum == 70064:
					if self.__CanChangeCostumeAttrList(dstSlotPos):
						return True
				else:
					if self.__CanChangeItemAttrList(dstSlotPos):
						return True
			elif "USE_ADD_ATTRIBUTE" == useType:
				if srcItemVNum == 70063:
					if self.__CanAddCostumeAttr(dstSlotPos):
						return True
				else:
					if self.__CanAddItemAttr(dstSlotPos):
						return True
			elif "USE_ADD_ATTRIBUTE2" == useType:
				if self.__CanAddItemAttr(dstSlotPos):
					return True
			elif "USE_ADD_ACCESSORY_SOCKET" == useType:
				if self.__CanAddAccessorySocket(dstSlotPos):
					return True
			elif "USE_PUT_INTO_ACCESSORY_SOCKET" == useType:								
				if self.__CanPutAccessorySocket(dstSlotPos, srcItemVNum):
					return True

				item.SelectItem(1, 2, player.GetItemIndex(dstSlotPos))

		return False

	#################################################
	## Refresh FUNCTIONS
	#################################################

	def RefreshSingleSlot(self, window, cell):
		if not self.SLOT_DATA.has_key(self.curPage):
			return

		slotData = self.SLOT_DATA[self.curPage]
		slot = self.main["slot"]

		slotWindow = player.SlotTypeToInvenType(slotData["type"])
		if slotWindow != window:
			return

		pageSize = safebox.SAFEBOX_SLOT_X_COUNT * slotData["y_size"]
		startPos = slotData["start"] + self.__GetPageData("sub_page", 0) * pageSize
		if cell < startPos or cell >= startPos + pageSize:
			return

		self.__RefreshSingleSlot(cell - startPos, slotData, slot)
		slot.RefreshSlot()

	def __RefreshSingleSlot(self, i, slotData, slot):
		pageSize = safebox.SAFEBOX_SLOT_X_COUNT * slotData["y_size"]
		startPos = slotData["start"] + self.__GetPageData("sub_page", 0) * pageSize

		getItemVnum = player.GetItemIndex
		if slotData.has_key("getItemVnum"):
			getItemVnum = slotData["getItemVnum"]
		getItemCount = player.GetItemCount
		if slotData.has_key("getItemCount"):
			getItemCount = slotData["getItemCount"]

		itemCount = getItemCount(startPos + i)
		if itemCount <= 1:
			itemCount = 0
		slot.SetItemSlot(i, getItemVnum(startPos + i), itemCount)

	def Refresh(self):
		self.main["slot"].Hide()
		self.main["loading"].Hide()
		self.main["page_btn"].Hide()

		if not safebox.IsGuildEnabled():
			self.main["btn"][self.BUTTON_GUILD].Hide()
		else:
			self.main["btn"][self.BUTTON_GUILD].Show()

		if self.PAGE_REQUEST_DATA.has_key(self.curPage):
			if not self.__GetPageData("is_open", False):
				self.main["loading"].Show()

				requestData = self.PAGE_REQUEST_DATA[self.curPage]
				net.SendChatPacket("/" + requestData["cmd_open"])
				
				if test_server:
					chat.AppendChat(chat.CHAT_TYPE_INFO, "Request open Page [%d]" % self.curPage)
				return

		self.main["slot"].Show()
		self.main["page_btn"].Show()

		self.__RefreshSlot()

	def __RefreshSlotStyle(self):
		if not self.SLOT_DATA.has_key(self.curPage):
			return

		slotData = self.SLOT_DATA[self.curPage]
		slot = self.main["slot"]

		slot.ArrangeSlot(0, safebox.SAFEBOX_SLOT_X_COUNT, slotData["y_size"], 32, 32, 0, 0)
		slot.SetSlotBaseImage("d:/ymir work/ui/public/Slot_Base.sub")
		
		slot.lockedSlotImages = []
		for i in xrange(slotData["y_size"]):
			img = ui.ExpandedImageBox()
			img.SetParent(slot)
			img.SetPosition(0, i*32)
			img.LoadImage("d:/ymir work/ui/game/inventory/row_disabled.tga")
			img.Hide()
			slot.lockedSlotImages.append(img)

		self.__LoadSlotEvents()

		newHeight = self.heightWithoutSlot + slot.GetHeight()
		newBoardHeight = self.boardHeightWithoutSlot + slot.GetHeight()
		if newHeight > self.GetHeight():
			self.SetSize(self.GetWidth(), self.heightWithoutSlot + slot.GetHeight())
			self.board.SetSize(self.board.GetWidth(), self.boardHeightWithoutSlot + slot.GetHeight())
			self.UpdateRect()

	def __RefreshSlot(self):
		if not self.SLOT_DATA.has_key(self.curPage):
			return

		slotData = self.SLOT_DATA[self.curPage]
		slot = self.main["slot"]

		pageSize = safebox.SAFEBOX_SLOT_X_COUNT * slotData["y_size"]
		for i in xrange(pageSize):
			self.__RefreshSingleSlot(i, slotData, slot)

		slot.RefreshSlot()

	def __RefreshPageButtons(self):
		btnList = []

		parent = self.main["page_btn"]
		pageCount = self.__GetPageData("size", 1)
		secondCount = 0
		y = 13
		if pageCount > 3:
			secondCount = pageCount - 3
			pageCount = 3
			y = 0
		posX = (parent.GetWidth() - (40 * pageCount) - (3 * (pageCount - 1))) / 2

		text = "I"
		for i in xrange(pageCount):
			btn = ui.RadioButton()
			btn.SetParent(parent)
			btn.SetPosition(posX, y)
			btn.SetUpVisual("d:/ymir work/ui/game/windows/tab_button_smiddle_01.sub")
			btn.SetOverVisual("d:/ymir work/ui/game/windows/tab_button_smiddle_02.sub")
			btn.SetDownVisual("d:/ymir work/ui/game/windows/tab_button_smiddle_03.sub")
			btn.SetText(text)
			btn.SAFE_SetEvent(self.__SelectSubPage, i)
			btn.Show()
			btnList.append(btn)

			posX += 43
			text += "I"

		if secondCount:
			posX = (parent.GetWidth() - (40 * secondCount) - (3 * (secondCount - 1))) / 2
			texts = ["IV", "V", "VI"]
			for i in xrange(secondCount):
				btn = ui.RadioButton()
				btn.SetParent(parent)
				btn.SetPosition(posX, 22)
				btn.SetUpVisual("d:/ymir work/ui/game/windows/tab_button_smiddle_01.sub")
				btn.SetOverVisual("d:/ymir work/ui/game/windows/tab_button_smiddle_02.sub")
				btn.SetDownVisual("d:/ymir work/ui/game/windows/tab_button_smiddle_03.sub")
				if i < len(texts):
					btn.SetText(texts[i])
				btn.SAFE_SetEvent(self.__SelectSubPage, i + 3)
				btn.Show()
				btnList.append(btn)
				posX += 43

		parent.btnList = btnList

	#################################################
	## Request Answer FUNCTIONS
	#################################################
	def OnRecvPageOpen(self, pageID, size):
		self.__SetPageData("size", size / safebox.SAFEBOX_SLOT_Y_COUNT, pageID)
		self.__SetPageData("is_open", True, pageID)

		if self.curPage == pageID:
			self.__RefreshPageButtons()
			self.__SelectSubPage(self.__GetPageData("sub_page", 0))

	def OnSafeboxOpen(self, size):
		self.OnRecvPageOpen(self.BUTTON_NORMAL, size)
		tchat("OnRecvPageOpen normal %d" % size)

	def OnMallOpen(self, size):
		self.OnRecvPageOpen(self.BUTTON_MALL, size)

class GuildSafeboxWindow(ui.ScriptWindow):

	BOX_WIDTH = 170

	def __init__(self, interface):
		ui.ScriptWindow.__init__(self)
		self.tooltipItem = None
		self.sellingSlotNumber = -1
		self.pageButtonList = []
		self.curPageIndex = 0
		self.isLoaded = 0
		self.xSafeBoxStart = 0
		self.ySafeBoxStart = 0
		self.eventCTRLClickItem = None

		self.wndLogWindow = GuildSafeboxLogWindow(interface)
		self.wndLogWindow.Close()

		self.__LoadWindow()

	def __del__(self):
		ui.ScriptWindow.__del__(self)

	def Show(self):
		self.__LoadWindow()

		ui.ScriptWindow.Show(self)		

	def Destroy(self):
		self.ClearDictionary()

		self.dlgPickMoney.Destroy()
		self.dlgPickMoney = None

		self.tooltipItem = None
		self.wndMoneySlot = None
		self.wndMoney = None
		self.wndBoard = None
		self.wndItem = None

		self.pageButtonList = []

		ui.ScriptWindow.Destroy(self)

	def __LoadWindow(self):
		if self.isLoaded == 1:
			return

		self.isLoaded = 1

		pyScrLoader = ui.PythonScriptLoader()
		pyScrLoader.LoadScriptFile(self, "UIScript/GuildSafeboxWindow.py")

		from _weakref import proxy

		self.board = self.GetChild("board")

		## Item
		wndItem = ui.GridSlotWindow()
		wndItem.SetParent(self.board)
		wndItem.SetPosition(3, 3)
		wndItem.SetSelectEmptySlotEvent(ui.__mem_func__(self.SelectEmptySlot))
		wndItem.SetSelectItemSlotEvent(ui.__mem_func__(self.SelectItemSlot))
		wndItem.SetUnselectItemSlotEvent(ui.__mem_func__(self.UseItemSlot))
		wndItem.SetUseSlotEvent(ui.__mem_func__(self.UseItemSlot))
		wndItem.SetOverInItemEvent(ui.__mem_func__(self.OverInItem))
		wndItem.SetOverOutItemEvent(ui.__mem_func__(self.OverOutItem))
		wndItem.Show()

		## PickMoneyDialog
		dlgPickMoney = GuildSafeboxTakeMoneyWindow()
		dlgPickMoney.Hide()

		## Close Button
		self.board.SetCloseEvent(ui.__mem_func__(self.Close))
		self.GetChild("ExitButton").SetEvent(ui.__mem_func__(self.Close))
		self.GetChild("LogButton").SAFE_SetEvent(self.OpenGuildLogWindow)

		self.wndItem = wndItem
		self.dlgPickMoney = dlgPickMoney
		self.wndBoard = self.GetChild("board")
		self.wndMoney = self.GetChild("Money")
		self.wndMoneySlot = self.GetChild("Money_Slot")
		self.wndMoneySlot.SetEvent(ui.__mem_func__(self.OpenPickMoneyDialog))

		## Initialize
		self.SetTableSize(1)
		self.RefreshGuildSafeboxMoney()

	def SetCTRLClickItemEvent(self, event):
		self.eventCTRLClickItem = event

	def OpenPickMoneyDialog(self):

		if mouseModule.mouseController.isAttached():

			attachedSlotPos = mouseModule.mouseController.GetAttachedSlotNumber()
			if player.SLOT_TYPE_INVENTORY == mouseModule.mouseController.GetAttachedType():

				if player.ITEM_MONEY == mouseModule.mouseController.GetAttachedItemIndex():
					net.SendGuildSafeboxGiveGoldPacket(mouseModule.mouseController.GetAttachedItemCount())
					snd.PlaySound("sound/ui/money.wav")

			mouseModule.mouseController.DeattachObject()

		else:
			self.dlgPickMoney.Open()

	def ShowWindow(self, size):

		(self.xSafeBoxStart, self.ySafeBoxStart, z) = player.GetMainCharacterPosition()

		self.SetTableSize(size)
		self.Show()

	def AppendOwnerItem(self, itemSlotPos):
		itemID = player.GetItemIndex(itemSlotPos)
		item.SelectItem(1, 2, itemID)

		itemWidth, itemHeight = item.GetItemSize(1,2,3)
		for page in xrange(len(self.pageButtonList)):
			for y in xrange(safebox.SAFEBOX_SLOT_Y_COUNT - itemHeight + 1):
				for x in xrange(safebox.SAFEBOX_SLOT_X_COUNT):
					slot = page * safebox.SAFEBOX_PAGE_SIZE + y * safebox.SAFEBOX_SLOT_X_COUNT + x
					if safebox.GetGuildItemID(slot) == 0:
						failed = False
						for i in xrange(itemHeight - 1):
							if safebox.GetGuildItemID(slot + i * safebox.SAFEBOX_SLOT_X_COUNT) != 0:
								failed = True
								break

						for j in xrange(1, 3):
							curSlot = slot - j * safebox.SAFEBOX_SLOT_X_COUNT
							if curSlot < 0 or curSlot / safebox.SAFEBOX_PAGE_SIZE != slot / safebox.SAFEBOX_PAGE_SIZE:
								break

							curVnum = safebox.GetGuildItemID(curSlot)
							if curVnum != 0:
								item.SelectItem(1, 2, curVnum)
								curWidth, curHeight = item.GetItemSize(1,2,3)
								if curHeight >= 1 + j:
									failed = True
								break

						if failed == False:
							net.SendGuildSafeboxCheckinPacket(itemSlotPos, page * safebox.SAFEBOX_PAGE_SIZE + y * safebox.SAFEBOX_SLOT_X_COUNT + x)
							return

	def __MakePageButton(self, pageCount):

		self.curPageIndex = 0
		self.pageButtonList = []

		text = "I"
		yPos = 74
		restartPos = -1
		if pageCount < 4:
			pos = (self.BOX_WIDTH - (52 * pageCount)) / 2 - 4
		else:
			pos = (self.BOX_WIDTH - (52 * 2)) / 2 - 4
			restartPos = pos
			yPos += 19 + 2

		for i in xrange(pageCount):
			button = ui.RadioButton()
			button.SetParent(self.board)
			button.SetUpVisual("d:/ymir work/ui/game/windows/tab_button_middle_01.sub")
			button.SetOverVisual("d:/ymir work/ui/game/windows/tab_button_middle_02.sub")
			button.SetDownVisual("d:/ymir work/ui/game/windows/tab_button_middle_03.sub")
			button.SetWindowVerticalAlignBottom()
			button.SetPosition(pos, yPos)
			button.SetText(text)
			button.SetEvent(lambda arg=i: self.SelectPage(arg))
			button.Show()
			self.pageButtonList.append(button)

			pos += 52
			if restartPos != -1 and i == 1:
				pos = restartPos
				yPos -= 19 + 2

			text += "I"
			if len(text) == 4:
				text = "IV"

		self.pageButtonList[0].Down()

	def SelectPage(self, index):

		self.curPageIndex = index

		for btn in self.pageButtonList:
			btn.SetUp()

		self.pageButtonList[index].Down()
		self.RefreshGuildSafebox()

	def __LocalPosToGlobalPos(self, local):
		return self.curPageIndex*safebox.SAFEBOX_PAGE_SIZE + local

	def SetTableSize(self, size):

		pageCount = max(1, size / safebox.SAFEBOX_SLOT_Y_COUNT)
		pageCount = min(4, pageCount)
		size = safebox.SAFEBOX_SLOT_Y_COUNT

		self.__MakePageButton(pageCount)

		self.wndItem.ArrangeSlot(0, safebox.SAFEBOX_SLOT_X_COUNT, size, 32, 32, 0, 0)
		self.wndItem.RefreshSlot()
		self.wndItem.SetSlotBaseImage("d:/ymir work/ui/public/Slot_Base.sub", 1.0, 1.0, 1.0, 1.0)

		wnd_height = self.wndItem.GetTop() + 32 * size + 19 + 7 + self.wndMoneySlot.GetTop()
		if pageCount == 4:
			wnd_height += 19 + 2

		self.wndBoard.SetSize(self.BOX_WIDTH, wnd_height)
		self.SetSize(self.wndBoard.GetRealWidth(), self.wndBoard.GetRealHeight())
		self.UpdateRect()

	def RefreshGuildSafebox(self):
		getItemID=safebox.GetGuildItemID
		getItemCount=safebox.GetGuildItemCount
		setItemID=self.wndItem.SetItemSlot

		for i in xrange(safebox.SAFEBOX_PAGE_SIZE):
			slotIndex = self.__LocalPosToGlobalPos(i)
			itemCount = getItemCount(slotIndex)
			if itemCount <= 1:
				itemCount = 0
			setItemID(i, getItemID(slotIndex), itemCount)

		self.wndItem.RefreshSlot()

	def RefreshGuildSafeboxMoney(self):
		self.wndMoney.SetText(localeInfo.NumberToMoneyString(safebox.GetGuildMoney()))

	def SetItemToolTip(self, tooltip):
		self.tooltipItem = tooltip

	def Close(self):
		net.SendChatPacket("/guild_safebox_close")

	def CommandCloseGuildSafebox(self):
		if self.tooltipItem:
			self.tooltipItem.HideToolTip()

		self.CloseGuildLogWindow()
		self.dlgPickMoney.Close()
		self.Hide()

	## Slot Event
	def SelectEmptySlot(self, selectedSlotPos):

		selectedSlotPos = self.__LocalPosToGlobalPos(selectedSlotPos)

		if mouseModule.mouseController.isAttached():

			attachedSlotType = mouseModule.mouseController.GetAttachedType()
			attachedSlotPos = mouseModule.mouseController.GetAttachedSlotNumber()

			if player.SLOT_TYPE_GUILD_SAFEBOX == attachedSlotType:

				net.SendGuildSafeboxItemMovePacket(attachedSlotPos, selectedSlotPos, 0)
				#snd.PlaySound("sound/ui/drop.wav")
			else:
				attachedInvenType = player.SlotTypeToInvenType(attachedSlotType)
				if player.RESERVED_WINDOW == attachedInvenType:
					return
					
				if player.ITEM_MONEY == mouseModule.mouseController.GetAttachedItemIndex():
					net.SendGuildSafeboxSaveMoneyPacket(mouseModule.mouseController.GetAttachedItemCount())
					snd.PlaySound("sound/ui/money.wav")

				else:
					net.SendGuildSafeboxCheckinPacket(attachedInvenType, attachedSlotPos, selectedSlotPos)
					#snd.PlaySound("sound/ui/drop.wav")
			
			mouseModule.mouseController.DeattachObject()

	def SelectItemSlot(self, selectedSlotPos):

		selectedSlotPos = self.__LocalPosToGlobalPos(selectedSlotPos)

		if mouseModule.mouseController.isAttached():

			attachedSlotType = mouseModule.mouseController.GetAttachedType()

			if player.SLOT_TYPE_INVENTORY == attachedSlotType:

				if player.ITEM_MONEY == mouseModule.mouseController.GetAttachedItemIndex():
					net.SendGuildSafeboxSaveMoneyPacket(mouseModule.mouseController.GetAttachedItemCount())
					snd.PlaySound("sound/ui/money.wav")

				else:
					attachedSlotPos = mouseModule.mouseController.GetAttachedSlotNumber()
					#net.SendGuildSafeboxCheckinPacket(attachedSlotPos, selectedSlotPos)
					#snd.PlaySound("sound/ui/drop.wav")

			mouseModule.mouseController.DeattachObject()

		else:

			curCursorNum = app.GetCursor()
			if app.SELL == curCursorNum:
				chat.AppendChat(chat.CHAT_TYPE_INFO, localeInfo.SAFEBOX_SELL_DISABLE_SAFEITEM)

			elif app.BUY == curCursorNum:
				chat.AppendChat(chat.CHAT_TYPE_INFO, localeInfo.SHOP_BUY_INFO)

			elif app.IsPressed(app.DIK_LCONTROL) and self.eventCTRLClickItem:
				self.eventCTRLClickItem(selectedSlotPos)

			else:
				selectedItemID = safebox.GetGuildItemID(selectedSlotPos)
				mouseModule.mouseController.AttachObject(self, player.SLOT_TYPE_GUILD_SAFEBOX, selectedSlotPos, selectedItemID)
				snd.PlaySound("sound/ui/pick.wav")

	def UseItemSlot(self, slotIndex):
		mouseModule.mouseController.DeattachObject()

	def __ShowToolTip(self, slotIndex):
		if self.tooltipItem:
			self.tooltipItem.SetGuildSafeBoxItem(slotIndex)

	def OverInItem(self, slotIndex):
		slotIndex = self.__LocalPosToGlobalPos(slotIndex)
		self.wndItem.SetUsableItem(False)
		self.__ShowToolTip(slotIndex)

	def OverOutItem(self):
		self.wndItem.SetUsableItem(False)
		if self.tooltipItem:
			self.tooltipItem.HideToolTip()

	def OnPickMoney(self, money):
		mouseModule.mouseController.AttachMoney(self, player.SLOT_TYPE_GUILD_SAFEBOX, money)

	def OnPressEscapeKey(self):
		self.Close()
		return True

	# auto close wnd when moving...
	# def OnUpdate(self):
	# 	USE_SAFEBOX_LIMIT_RANGE = 1000

	# 	(x, y, z) = player.GetMainCharacterPosition()
	# 	if abs(x - self.xSafeBoxStart) > USE_SAFEBOX_LIMIT_RANGE or abs(y - self.ySafeBoxStart) > USE_SAFEBOX_LIMIT_RANGE:
	# 		self.Close()

	def OpenGuildLogWindow(self):
		self.wndLogWindow.Open()

	def CloseGuildLogWindow(self):
		self.wndLogWindow.Close()

	def RefreshLog(self):
		self.wndLogWindow.Refresh()

	def AppendLog(self):
		self.wndLogWindow.OnAppendItem()

if __name__ == "__main__":

	import app
	import wndMgr
	import systemSetting
	import mouseModule
	import grp
	import ui
	import chr
	import background
	import player

	#wndMgr.SetOutlineFlag(True)

	app.SetMouseHandler(mouseModule.mouseController)
	app.SetHairColorEnable(True)
	wndMgr.SetMouseHandler(mouseModule.mouseController)
	wndMgr.SetScreenSize(systemSetting.GetWidth(), systemSetting.GetHeight())
	app.Create("METIN2 CLOSED BETA", systemSetting.GetWidth(), systemSetting.GetHeight(), 1)
	mouseModule.mouseController.Create()


	wnd = SafeboxWindow()
	wnd.ShowWindow(1)
	
	app.Loop()
