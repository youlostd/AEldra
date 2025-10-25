import ui
import constInfo
import item
import uiToolTip
import localeInfo
import auction
import player
import app
import networkModule
import chat
import cfg
import skill

ROOT_PATH = "d:/ymir work/ui/game/shopsearch/"

class ShopSearchWindow(ui.BaseScriptWindow):

	class PopupDialog(networkModule.PopupDialog):

		def __init__(self):
			networkModule.PopupDialog.__init__(self, False)

		def __del__(self):
			networkModule.PopupDialog.__del__(self)

		def Open(self, msg, autoclose):
			networkModule.PopupDialog.SetAutoClose(self, autoclose)
			networkModule.PopupDialog.Open(self, msg, 0, localeInfo.UI_OK)

			self.SetCenterPosition()

		# def LoadDialog(self):
			# networkModule.PopupDialog.LoadDialog(self)

		def ComputeSize(self):
			networkModule.PopupDialog.ComputeSize(self)

			self.GetChild("accept").SetPosition(self.GetChild("accept").GetLeft(), self.GetChild("accept").GetTop() - 5)

			newHeight = self.GetHeight() - 8
			self.SetSize(self.GetWidth(), newHeight)
			self.GetChild("board").SetSize(self.GetWidth(), newHeight)

	class QuestionDialog(ui.BoardWithTitleBar):

		BOARD_WIDTH = 300

		def __init__(self):
			ui.BoardWithTitleBar.__init__(self)
			self.AddFlag("float")
			self.AddFlag("movable")
			self.SetSize(self.BOARD_WIDTH, 0)

			self.closeEvent = None

			self.itemToolTip = uiToolTip.ItemToolTip()
			self.itemToolTip.HideToolTip()

			itemImage = ui.ImageBox()
			itemImage.SetParent(self)
			itemImage.SetWindowHorizontalAlignCenter()
			itemImage.SetPosition(0, 10)
			itemImage.SAFE_SetStringEvent("MOUSE_OVER_IN", self.itemToolTip.ShowToolTip)
			itemImage.SAFE_SetStringEvent("MOUSE_OVER_OUT", self.itemToolTip.HideToolTip)
			itemImage.Show()
			self.itemImage = itemImage

			textLine = ui.MultiTextLine()
			textLine.SetParent(self)
			textLine.SetWindowHorizontalAlignCenter()
			textLine.SetTextHorizontalAlignCenter()
			textLine.SetWidth(self.BOARD_WIDTH - 25 * 2)
			textLine.Show()
			self.text = textLine

			btnYes = ui.Button()
			btnYes.SetParent(self)
			btnYes.SetPosition(20 + (self.GetWidth() - 20 * 2) * 1 / 4 - 88 / 2, 10 + 24)
			btnYes.SetUpVisual("d:/ymir work/ui/public/Large_Button_01.sub")
			btnYes.SetOverVisual("d:/ymir work/ui/public/Large_Button_02.sub")
			btnYes.SetDownVisual("d:/ymir work/ui/public/Large_Button_03.sub")
			btnYes.SetWindowVerticalAlignBottom()
			btnYes.SetText(localeInfo.YES)
			btnYes.Show()
			self.btnYes = btnYes

			btnNo = ui.Button()
			btnNo.SetParent(self)
			btnNo.SetPosition(20 + (self.GetWidth() - 20 * 2) * 3 / 4 - 88 / 2, 10 + 24)
			btnNo.SetUpVisual("d:/ymir work/ui/public/Large_Button_01.sub")
			btnNo.SetOverVisual("d:/ymir work/ui/public/Large_Button_02.sub")
			btnNo.SetDownVisual("d:/ymir work/ui/public/Large_Button_03.sub")
			btnNo.SetWindowVerticalAlignBottom()
			btnNo.SetText(localeInfo.NO)
			btnNo.SAFE_SetEvent(self.Close)
			btnNo.Show()
			self.btnNo = btnNo

		def __del__(self):
			ui.BoardWithTitleBar.__del__(self)

		def SAFE_SetAcceptEvent(self, event, *args):
			apply(self.btnYes.SAFE_SetEvent, (event,) + args)

		def SAFE_SetCloseEvent(self, event):
			self.closeEvent = ui.__mem_func__(event)

		def Open(self, itemID, title, text):
			auction.SetContainerType(auction.CONTAINER_SEARCH)
			
			itemVnum = auction.GetItemVnum(itemID)
			tchat("Open [ID %d Vnum %d]" % (itemID, itemVnum))
			item.SelectItem(1, 2, itemVnum)

			self.itemImage.LoadImage(item.GetIconImageFileName())
			self.itemToolTip.SetAuctionItem(auction.CONTAINER_SEARCH, itemID)
			self.itemToolTip.HideToolTip()

			self.SetTitleName(title)
			self.text.SetPosition(0, self.itemImage.GetBottom() + 6)
			self.text.SetText(text)

			self.SetSize(self.GetWidth(), self.text.GetBottom() + 5 + 24 + 10)
			self.btnYes.UpdateRect()
			self.btnNo.UpdateRect()

			self.SetCenterPosition()
			self.Show()
			self.SetTop()

		def Close(self):
			if not self.IsShow():
				return

			self.Hide()
			self.itemToolTip.Hide()

			if self.closeEvent:
				self.closeEvent()

		def OnPressEscapeKey(self):
			self.Close()

	class Item(ui.Bar):

		MARGIN_X = 4
		MARGIN_Y = 4

		ITEM_HEIGHT = 32 + MARGIN_Y * 2

		def __init__(self, color, whisperFunc):
			ui.Bar.__init__(self)

			self.oldCursor = -1
			self.isMine = False
			self.whisperFunc = whisperFunc
			self.clickEvent = None
			self.clickArgs = None

			self.SetSize(100, self.ITEM_HEIGHT)
			self.SetColor(color)

			self.timeEnd = 0

			self.toolTip = uiToolTip.ItemToolTip()
			self.toolTip.HideToolTip()

			self.__BuildWindow()

		def __del__(self):
			ui.Bar.__del__(self)

		def __BuildWindow(self):
			itemName = ui.TextLine()
			itemName.SetParent(self)
			itemName.SetPosition(self.MARGIN_X, self.MARGIN_Y)
			itemName.Show()

			itemPriceIcon = ui.ImageBox()
			itemPriceIcon.SetParent(self)
			itemPriceIcon.AddFlag("not_pick")
			if __SERVER__ == 1:
				itemPriceIcon.SetPosition(self.MARGIN_X, self.MARGIN_Y + 19)
			elif __SERVER__ == 2:
				itemPriceIcon.SetPosition(-20, 0)
				itemPriceIcon.SetWindowHorizontalAlignCenter()
				itemPriceIcon.SetWindowVerticalAlignCenter()
			itemPriceIcon.LoadImage(ROOT_PATH + "yang icon.tga")
			itemPriceIcon.Show()

			itemPrice = ui.TextLine()
			itemPrice.SetParent(itemPriceIcon)
			itemPrice.SetPosition(itemPriceIcon.GetWidth() + 4, 0)
			itemPrice.SetWindowVerticalAlignCenter()
			itemPrice.SetVerticalAlignCenter()
			itemPrice.Show()

			sellerIcon = ui.ImageBox()
			sellerIcon.SetParent(self)
			sellerIcon.AddFlag("not_pick")
			if __SERVER__ == 1:
				sellerIcon.SetPosition(-20, 0)
				sellerIcon.SetWindowHorizontalAlignCenter()
				sellerIcon.SetWindowVerticalAlignCenter()
			elif __SERVER__ == 2:
				sellerIcon.SetPosition(self.MARGIN_X, self.MARGIN_Y + 19)
			sellerIcon.LoadImage(ROOT_PATH + "brief.tga")
			sellerIcon.Show()

			sellerName = ui.TextLine()
			sellerName.SetParent(sellerIcon)
			sellerName.AddFlag("not_pick")
			sellerName.SetPosition(sellerIcon.GetWidth() + 5, -1)
			sellerName.SetWindowVerticalAlignCenter()
			sellerName.Show()

			timeLeftLine = ui.TextLine()
			timeLeftLine.SetParent(self)
			timeLeftLine.SetWindowHorizontalAlignRight()
			timeLeftLine.SetHorizontalAlignRight()
			timeLeftLine.SetWindowVerticalAlignCenter()
			timeLeftLine.SetVerticalAlignCenter()
			timeLeftLine.SetPosition(self.MARGIN_X, 0)
			timeLeftLine.Show()

			self.itemName = itemName
			self.itemPriceIcon = itemPriceIcon
			self.itemPrice = itemPrice
			self.sellerIcon = sellerIcon
			self.sellerName = sellerName
			self.timeLeftLine = timeLeftLine

		def Hide(self):
			ui.Bar.Hide(self)
			try:
				self.OnMouseOverOut()
			except:
				pass

		def __OnWhisper(self):
			auction.SetContainerType(auction.CONTAINER_SEARCH)
			itemOwnerName = auction.GetItemOwnerName(self.itemID)
			if self.whisperFunc:
				self.whisperFunc(itemOwnerName)

		def SetItemID(self, itemID):
			self.itemID = itemID
			self.Refresh()

		def SetEvent(self, eventFunc, *eventArgs):
			self.clickEvent = eventFunc
			self.clickArgs = eventArgs

		def OnMouseLeftButtonDown(self):
			if self.sellerName.IsInPosition() or self.sellerIcon.IsInPosition():
				self.__OnWhisper()
			elif self.clickEvent:
				apply(self.clickEvent, self.clickArgs)

		def Refresh(self):
			if self.itemID < 0:
				return

			auction.SetContainerType(auction.CONTAINER_SEARCH)
			itemVnum = auction.GetItemVnum(self.itemID)
			itemCount = auction.GetItemCount(self.itemID)
			itemMetinSlot = [auction.GetItemSocket(self.itemID, i) for i in xrange(player.METIN_SOCKET_MAX_NUM)]
			itemOwnerName = auction.GetItemOwnerName(self.itemID)
			itemPrice = auction.GetItemPrice(self.itemID)
			self.__SetItemData(itemVnum, itemCount, itemMetinSlot, itemPrice, itemOwnerName)

			self.timeEnd = auction.GetItemTimeoutTime(self.itemID)
			self.__RefreshTimer()

			self.toolTip.SetAuctionItem(auction.CONTAINER_SEARCH, self.itemID)
			self.toolTip.HideToolTip()
			
			self.isMine = itemOwnerName == player.GetName()

		def __SetItemData(self, vnum, count, metinSlot, price, owner):
			if not item.SelectItem(1, 2, vnum):
				return

			itemName = item.GetItemName()
			if vnum == 50300:
				itemName = skill.GetSkillName(metinSlot[0]) + " " + itemName

			if count <= 1:
				self.itemName.SetText(itemName)
			else:
				self.itemName.SetText("%dx %s" % (count, itemName))
			self.itemPrice.SetText(localeInfo.NumberToMoneyString(price))
			self.sellerName.SetText(owner)
			self.sellerName.AdjustSize()

		def __RefreshTimer(self):
			if self.timeEnd != 0:
				timeLeft = max(0, self.timeEnd - app.GetGlobalTimeStamp())
				if timeLeft == 0:
					self.timeEnd = 0
					self.timeLeftLine.SetPackedFontColor(uiToolTip.ToolTip.DISABLE_COLOR)
					self.timeLeftLine.SetText(localeInfo.AUCTION_ITEM_TIMEOUT_INFO)
				else:
					self.timeLeftLine.SetText(localeInfo.SecondToDHMSShort(timeLeft))

		def ShowToolTip(self):
			self.toolTip.ShowToolTip()

		def HideToolTip(self):
			self.toolTip.HideToolTip()

		def __GetSelfCursor(self):
			if self.isMine:
				return app.PICK
			else:
				return app.BUY

		def OnMouseOverIn(self):
			ui.Bar.OnMouseOverIn(self)
			self.ShowToolTip()

			app.SetCursor(self.__GetSelfCursor())

		def OnMouseOverOut(self):
			ui.Bar.OnMouseOverOut(self)
			self.HideToolTip()

			app.SetCursor(0)

		def OnUpdate(self):
			self.__RefreshTimer()

	CATEGORY_LIST = {
		"all" : {
			"is_mine" : False, #avoid error...
		},
		"weapon" : {
			"type" : item.ITEM_TYPE_WEAPON,
		},
		"armor" : {
			"type" : item.ITEM_TYPE_ARMOR,
			"sub_type" : (
				(item.ARMOR_BODY, item.ARMOR_HEAD, item.ARMOR_SHIELD, item.ARMOR_FOOTS,),
			),
		},
		"jewellery" : {
			"type" : item.ITEM_TYPE_ARMOR,
			"sub_type" : (
				(item.ARMOR_WRIST, item.ARMOR_NECK, item.ARMOR_EAR), # ITEM_TYPE_ARMOR
			),
		},
		"talisman" : {
			"type" : item.ITEM_TYPE_TOTEM,
		},
		"dragonsoul" : {
			"type" : (item.ITEM_TYPE_MATERIAL, item.ITEM_TYPE_DS, item.ITEM_TYPE_SPECIAL_DS, item.ITEM_TYPE_EXTRACT),
			"sub_type" : (
				(item.MATERIAL_DS_REFINE_NORMAL, item.MATERIAL_DS_REFINE_BLESSED, item.MATERIAL_DS_REFINE_HOLLY), # ITEM_TYPE_MATERIAL
				(), (), ()
				)
		},
		"costume" : {
			"type" : item.ITEM_TYPE_COSTUME,
		},
		"costume_boni" : {
			"type" : item.ITEM_TYPE_USE,
			"sub_type" : ((item.USE_ADD_SPECIFIC_ATTRIBUTE,),),
		},
		"skills" : {
			"type" : item.ITEM_TYPE_SKILLBOOK,
		},
		"potions" : {
		# 	"type" : item.ITEM_TYPE_BLEND,
		# 	"sub_type" : (item.ITEM_TYPE_NONE,),
			"type" : (item.ITEM_TYPE_BLEND, item.ITEM_TYPE_USE),
			"sub_type" : ((),(item.USE_POTION,)),
		},

		### TEST CASE
		# "usable" : {
		# 	"type" : item.ITEM_TYPE_BLEND,
		# 	"sub_type" : (item.ITEM_TYPE_NONE,),
		# },

		# "fishs" : {
		# 	"type" : item.ITEM_TYPE_BLEND,
		# 	# "sub_type" :,
		# },

		# "mounts" : {
		# 	"type" : (item.ITEM_TYPE_BLEND, item.ITEM_TYPE_USE),
		# 	"sub_type" : (item.ITEM_TYPE_NONE,item.USE_POTION,),
		# },

		# "pets" : {
		# 	"type" : (item.ITEM_TYPE_BLEND, item.ITEM_TYPE_USE),
		# 	"sub_type" : ((item.ITEM_TYPE_NONE,),(item.USE_POTION,),),
		# },

		# "owned" : {
		# 	"type" : (item.ITEM_TYPE_BLEND, item.ITEM_TYPE_USE),
		# 	"sub_type" : ((item.ITEM_TYPE_NONE,),(item.USE_POTION,),),
		# },
		### TEST CASE

		"usable" : {
			"type" : (item.ITEM_TYPE_USE, item.ITEM_TYPE_MATERIAL),
		},
		"fishs" : {
			"type" : item.ITEM_TYPE_FISH,
		},
		"mounts" : {
			"type" : item.ITEM_TYPE_MOUNT,
		},
		"pets" : {
			"type" : item.ITEM_TYPE_PET,
		},
		"owned" : {
			"is_mine" : True,
		},

	}

	if constInfo.NEW_SEARCH_CATEGORY:
		CATEGORY_LIST["ores"] = {
			"type" : item.ITEM_TYPE_USE,
			"sub_type" : ((21,),), # USE_PUT_INTO_ACCESSORY_SOCKET
		}

	STATE_NONE = 0
	STATE_LOADING = 1
	STATE_DISPLAY = 2

	ITEM_LIST_COLORS = (
		ui.GenerateColor(150, 150, 150, 75),
		ui.GenerateColor(50, 50, 50, 75),
	)

	PAGE_DISPLAY_COUNT = 7
	PAGE_CHANGE_SMALL = 1
	PAGE_CHANGE_BIG = 10

	GAME_MESSAGE_LIST = {
		"ITEM_TAKE_SUCCESS" : localeInfo.AUCTION_GAME_MESSAGE_ITEM_TAKE_SUCCESS,
		"ITEM_TAKE_NOT_EXIST" : localeInfo.AUCTION_GAME_MESSAGE_ITEM_TAKE_NOT_EXIST,
		"ITEM_BUY_SUCCESS" : localeInfo.AUCTION_GAME_MESSAGE_ITEM_BUY_SUCCESS,
		"ITEM_BUY_NOT_EXIST" : localeInfo.AUCTION_GAME_MESSAGE_ITEM_BUY_NOT_EXIST,
		"ITEM_BUY_TIMEOUT" : localeInfo.AUCTION_GAME_MESSAGE_ITEM_BUY_TIMEOUT,
		"ITEM_WRONG_PRICE" : localeInfo.AUCTION_GAME_MESSAGE_ITEM_WRONG_PRICE,
		"ITEM_INSERT_MONEY_ERR" : localeInfo.AUCTION_GAME_MESSAGE_ITEM_PRICE_TOO_HIGH,
		"ITEM_INSERT_SUCCESS" : localeInfo.AUCTION_GAME_MESSAGE_ITEM_INSERT_SUCCESS,
		"NO_ITEMS_FOUND" : localeInfo.AUCTION_GAME_MESSAGE_NO_ITEMS_FOUND,
		"MARK_DONE" : localeInfo.AUCTION_GAME_MESSAGE_MARK_DONE,
		"MARK_NOT_FOUND" : localeInfo.AUCTION_GAME_MESSAGE_MARK_NOT_FOUND,
		"PREMIUM_MARK_DONE" : localeInfo.AUCTION_GAME_MESSAGE_MARK_DONE_PREMIUM,
		"PREMIUM_MARK_NOT_FOUND" : localeInfo.AUCTION_GAME_MESSAGE_MARK_NOT_FOUND_PREMIUM,
	}

	JOB_TO_ANTIFLAG = [
		item.ITEM_ANTIFLAG_WARRIOR,
		item.ITEM_ANTIFLAG_ASSASSIN,
		item.ITEM_ANTIFLAG_SURA,
		item.ITEM_ANTIFLAG_SHAMAN,
	]

	#################################################
	## MAIN FUNCTIONS
	#################################################

	def __init__(self, whisperFunc):
		ui.BaseScriptWindow.__init__(self, "ShopSearchWindow", self.__BindObject)
		self.__Initialize()

		self.whisperFunc = whisperFunc

		self.__LoadWindow()

	def __Initialize(self):
		self.state = self.STATE_NONE
		self.selectedCat = None
		self.currentPage = 0
		self.lastBuyID = -1
		self.lastTakeID = -1
		self.currentSortType = 0
		self.premiumToolTip = None
		# self.sortToolTip = None
		self.popupWindow = None
		self.questionWindow = None
		self.whisperFunc = None
		self.pageBtns = []
		if constInfo.ENABLE_RACE_CATEGORY:
			self.raceCategory = []

		if __SERVER__ == 2:
			self.toolTip = None
			self.infoImage = None

	def __BindObject(self):
		self._AddLoadObject("titlebar", "titlebar")

		# search
		# self._AddLoadObject("sort_icon", "sort_info_icon")
		self._AddLoadObject("premium_icon", "premium_info_icon")
		self._AddLoadObject("premium", "premium_info")
		self._AddLoadObject("strict_search_checkbox", "strict_search_checkbox")

		searchDict = {
			"name_text" : "search_text_edit_text",
			"name_text_hint" : "search_text_edit_text_hint",
			"name_btn" : "search_text_button",

			# "sort" : "search_sort_dropdown",
		}
		for key in self.CATEGORY_LIST:
			searchDict[key] = "search_cat_btn_%s" % key
		self._AddLoadObject("search", searchDict)

		# items
		self._AddLoadObject("item", {
			"wnd" : "item_window",
			"list" : "item_list",
			"scroll" : "item_scrollbar",
			"loading" : "item_loading",
		})

		if constInfo.ENABLE_RACE_CATEGORY:
			self._AddLoadObject("RaceCategory", {
				"cat0" : "CategoryButton0",
				"cat1" : "CategoryButton1",
				"cat2" : "CategoryButton2",
				"cat3" : "CategoryButton3",
			})

	def __LoadWindow(self):
		# create objects
		self.premiumToolTip = uiToolTip.ToolTip()
		self.premiumToolTip.HideToolTip()
		# self.sortToolTip = uiToolTip.ToolTip()
		# self.sortToolTip.HideToolTip()

		self.popupWindow = self.PopupDialog()
		self.popupWindow.Close()

		self.questionWindow = self.QuestionDialog()
		self.questionWindow.Close()

		# main
		self.main["titlebar"].SetCloseEvent(self.Close)

		# search
		# self.main["sort_icon"].SAFE_SetStringEvent("MOUSE_OVER_IN", self.ShowSortToolTip)
		# self.main["sort_icon"].SAFE_SetStringEvent("MOUSE_OVER_OUT", self.sortToolTip.HideToolTip)
		self.main["premium_icon"].SAFE_SetStringEvent("MOUSE_OVER_IN", self.ShowPremiumToolTip)
		self.main["premium_icon"].SAFE_SetStringEvent("MOUSE_OVER_OUT", self.premiumToolTip.HideToolTip)
		self.main["premium"].Hide()
		self.main["premium_icon"].Hide()

		self.main["strict_search_checkbox"].SAFE_SetEvent(self.__OnPressStrictCheckbox)

		wnd = self.main["search"]
		wnd["name_text"].SetEscapeEvent(ui.__mem_func__(self.__OnPressNameEscapeKey))
		wnd["name_text"].SetReturnEvent(ui.__mem_func__(self.__StartSearch))#__OnPressNameReturnKey))
		wnd["name_text"].SetUpdateEvent(ui.__mem_func__(self.__Search_RefreshTextHint))
		wnd["name_text"].SetTabEvent(ui.__mem_func__(self.__Search_CompleteTextSearch))

		wnd["name_btn"].SAFE_SetEvent(self.__StartSearch)
		# wnd["sort"].SetEvent(self.__OnSelectSortType)

		for cat in self.CATEGORY_LIST:
			wnd[cat].SAFE_SetEvent(self.__OnSelectCategory, cat)
			if __SERVER__ == 2:
				if cat == "talisman":
					wnd[cat].Hide()
				elif wnd[cat].GetTop() >= 185 - 47 + (23 + 3) * 4:
					wnd[cat].SetPosition(wnd[cat].GetLeft(), wnd[cat].GetTop() - 26)

		wnd["owned"].Hide()

		# items
		wnd = self.main["item"]
		wnd["scroll"].SetScrollEvent(ui.__mem_func__(self.__OnScrollItemList))

		if constInfo.ENABLE_RACE_CATEGORY:
			wnd = self.main["RaceCategory"]
			for x in xrange(4):
				category = wnd[("cat%d" % x)]
				category.SetToggleDownEvent(ui.__mem_func__(self.__SelectRaceCategory), x)
				category.SetToggleUpEvent(ui.__mem_func__(self.__UnselectRaceCategory), x)
				self.raceCategory.append(category)
			self.jobSelection = [ False ] * 4

		# init
		self.__OnSelectCategory("all")

		# refresh
		self.Refresh()

		if __SERVER__ == 2:
			self.toolTip = uiToolTip.ToolTip(0)
			self.toolTip.AutoAppendTextLine2(localeInfo.TOOLTIP_SHOP_SEARCH_INFO)
			self.toolTip.ResizeToolTip()

			self.infoImage = ui.MakeImageBox(self, "d:/ymir work/ui/game/info/info_normal.tga", 30, 49)
			self.infoImage.SetScale(0.5, 0.5)
			self.infoImage.SAFE_SetStringEvent("MOUSE_OVER_IN", self.ShowToolTipInfo)
			self.infoImage.SAFE_SetStringEvent("MOUSE_OVER_OUT", self.HideToolTipInfo)

	if __SERVER__ == 2:
		def ShowToolTipInfo(self):
			self.infoImage.LoadImage("d:/ymir work/ui/game/info/info_hover.tga")
			self.infoImage.SetScale(0.5, 0.5)
			self.toolTip.ShowToolTip()

		def HideToolTipInfo(self):
			self.infoImage.LoadImage("d:/ymir work/ui/game/info/info_normal.tga")
			self.infoImage.SetScale(0.5, 0.5)
			self.toolTip.HideToolTip()

	def __OnPressStrictCheckbox(self):
		cfg.Set(cfg.SAVE_OPTION, "StrictSearch", self.main["strict_search_checkbox"].IsChecked())
		tchat("pressed")

	def Close(self):
		self.Hide()

		# kill focus of editboxes
		self.main["search"]["name_text"].KillFocus()

		# hide tooltip
		if self.premiumToolTip:
			self.premiumToolTip.HideToolTip()
		# if self.sortToolTip:
		# 	self.sortToolTip.HideToolTip()

	#################################################
	## REFRESH FUNCTIONS
	#################################################

	def Refresh(self):
		self.RefreshPremium()
		self.RefreshState()

	def RefreshPremium(self):
		wndText = self.main["premium"]
		if self.__IsPremium():
			wndText.SetText(localeInfo.AUCTION_PREMIUM_TEXT_ACTIVE)
			wndText.SetPackedFontColor(uiToolTip.ToolTip.POSITIVE_COLOR)
		else:
			wndText.SetText(localeInfo.AUCTION_PREMIUM_TEXT_INACTIVE)
			wndText.SetPackedFontColor(uiToolTip.ToolTip.NEGATIVE_COLOR)

	def RefreshState(self):
		wnd = self.main["item"]
		wnd["list"].Hide()
		wnd["scroll"].Hide()
		wnd["loading"].Hide()
		self.pageBtns = []

		if self.state == self.STATE_LOADING:
			wnd["loading"].Show()
		elif self.state == self.STATE_DISPLAY:
			self.RefreshItems()
			wnd["list"].Show()

	def RefreshItems(self):
		wnd = self.main["item"]

		auction.SetContainerType(auction.CONTAINER_SEARCH)
		itemMaxCount = auction.GetItemMaxCount()
		isScrollBar = itemMaxCount > wnd["list"].GetViewItemCount()
		if isScrollBar:
			wnd["scroll"].SetMiddleBarSize(float(wnd["list"].GetViewItemCount()) / itemMaxCount)
			wnd["scroll"].Show()

		wnd["list"].RemoveAllItems()
		for i in xrange(itemMaxCount):
			newItem = self.Item(self.ITEM_LIST_COLORS[i % len(self.ITEM_LIST_COLORS)], self.whisperFunc)
			newItem.SetItemID(i)
			if auction.GetItemOwnerName(i) == player.GetName():
				newItem.SetEvent(ui.__mem_func__(self.OnItemQuestionTake), i)
			else:
				newItem.SetEvent(ui.__mem_func__(self.OnItemMark), i)
			wnd["list"].AppendItem(newItem)

		self.__BuildPageButtons()

	def __Search_RefreshTextHint(self):
		wnd = self.main["search"]

		wnd["name_text"].SetFontColor(0.8549, 0.8549, 0.8549)
		wnd["name_text_hint"].SetText("")

		if wnd["name_text"].GetText():
			if not item.SelectByNamePart(wnd["name_text"].GetText()):
				wnd["name_text"].SetFontColor(1.0, 0.2, 0.2)
			else:
				itemName = item.GetItemName()
				if itemName.endswith("+0"):
					if item.GetItemType() == item.ITEM_TYPE_WEAPON or item.GetItemType() == item.ITEM_TYPE_ARMOR:
						itemName = itemName[:-2] + "+9"
					elif item.GetItemType() == item.ITEM_TYPE_METIN:
						itemName = itemName[:-2] + "+5"
				wnd["name_text_hint"].SetText(wnd["name_text"].GetText() + " " + itemName[len(wnd["name_text"].GetText()):])


	#################################################
	## AUTO COMPLETION FUNCTIONS
	#################################################

	def __Search_CompleteTextSearch(self):
		wnd = self.main["search"]

		if wnd["name_text_hint"].GetText():
			oldText = wnd["name_text"].GetText()
			wnd["name_text"].SetText(oldText + wnd["name_text_hint"].GetText()[len(oldText)+1:])
			wnd["name_text"].SetEndPosition()
			self.__Search_RefreshTextHint()

	#################################################
	## HELPER FUNCTIONS
	#################################################

	def __IsPremium(self):
		return constInfo.AUCTION_PREMIUM

	def __ShowMessage(self, msg, autoclose = False):
		self.popupWindow.Open(msg, autoclose)

	def __BuildPageButtons_NewButton(self, xpos, ypos):
		btn = ui.StateButton()
		btn.SetParent(self.main["item"]["wnd"])
		btn.SetUpVisual(False, ROOT_PATH + "page_inactive_normal.tga")
		btn.SetOverVisual(False, ROOT_PATH + "page_inactive_hover.tga")
		btn.SetDownVisual(False, ROOT_PATH + "page_inactive_down.tga")
		btn.SetUpVisual(True, ROOT_PATH + "page_active_normal.tga")
		btn.SetOverVisual(True, ROOT_PATH + "page_active_normal.tga")
		btn.SetDownVisual(True, ROOT_PATH + "page_active_normal.tga")
		btn.SetPosition(xpos, ypos - btn.GetHeight())
		self.pageBtns.append(btn)
		return btn

	def __BuildPageButtons(self):
		wnd = self.main["item"]["wnd"]
		self.pageBtns = []

		btnWidth = 15
		btnSpace = 5
		btnCount = 4 + min(self.PAGE_DISPLAY_COUNT, auction.GetMaxPageCount() + 1)
		width = (btnWidth + btnSpace) * btnCount - btnSpace
		xpos = (wnd.GetWidth() - width) / 2
		ypos = wnd.GetHeight() - 7

		# page change back
		btn = self.__BuildPageButtons_NewButton(xpos, ypos)
		btn.SetText("<<")
		btn.SAFE_SetEvent(self.__OnChangeItemPage, -self.PAGE_CHANGE_BIG)
		btn.Show()
		xpos += btnWidth + btnSpace

		btn = self.__BuildPageButtons_NewButton(xpos, ypos)
		btn.SetText("<")
		btn.SAFE_SetEvent(self.__OnChangeItemPage, -self.PAGE_CHANGE_SMALL)
		btn.Show()
		xpos += btnWidth + btnSpace

		# pages around current
		curIdx = self.currentPage
		aroundCount = (self.PAGE_DISPLAY_COUNT - 1) / 2
		minIdx = max(0, curIdx - aroundCount)
		maxIdx = min(auction.GetMaxPageCount(), minIdx + self.PAGE_DISPLAY_COUNT - 1)
		for i in xrange(maxIdx - minIdx + 1):
			btn = self.__BuildPageButtons_NewButton(xpos, ypos)
			btn.SetText(str(1 + minIdx + i))
			if minIdx + i != curIdx:
				btn.SAFE_SetEvent(self.__OnChangeItemPage, minIdx + i - curIdx)
			else:
				btn.SetState(True)
			btn.Show()
			xpos += btnWidth + btnSpace

		# page change next
		btn = self.__BuildPageButtons_NewButton(xpos, ypos)
		btn.SetText(">")
		btn.SAFE_SetEvent(self.__OnChangeItemPage, self.PAGE_CHANGE_SMALL)
		btn.Show()
		xpos += btnWidth + btnSpace

		btn = self.__BuildPageButtons_NewButton(xpos, ypos)
		btn.SetText(">>")
		btn.SAFE_SetEvent(self.__OnChangeItemPage, self.PAGE_CHANGE_BIG)
		btn.Show()

	#################################################
	## TOOLTIP FUNCTIONS
	#################################################

	def ShowPremiumToolTip(self):
		self.premiumToolTip.ClearToolTip()
		if self.__IsPremium():
			self.premiumToolTip.AppendDescription(localeInfo.AUCTION_PREMIUM_INFO_ACTIVE, 26)
		else:
			self.premiumToolTip.AppendDescription(localeInfo.AUCTION_PREMIUM_INFO_INACTIVE, 26)
		self.premiumToolTip.ShowToolTip()

	# def ShowSortToolTip(self):
	# 	self.sortToolTip.ClearToolTip()
	# 	self.sortToolTip.AppendDescription(localeInfo.SORT_DISABLED_INFO, 26)
	# 	self.sortToolTip.ShowToolTip()

	#################################################
	## CALL FUNCTIONS
	#################################################

	def __OnPressNameEscapeKey(self):
		wnd = self.main["search"]["name_text"]
		if not wnd.IsShowCursor() or wnd.GetText() == "":
			self.OnPressEscapeKey()
		else:
			wnd.SetText("")

	# def __OnPressNameReturnKey(self):
	# 	pass

	# def __OnSelectSortType(self, sortID):
	# 	self.currentSortType = sortID

	def __OnSelectCategory(self, sel_cat, force = False):
		wnd = self.main["search"]

		if self.selectedCat == sel_cat and not force:
			return

		self.selectedCat = sel_cat
		self.__StartSearch()

		for cat in self.CATEGORY_LIST:
			try:
				wnd[cat].SetState(cat == sel_cat)
			except:
				tchat("broken %s == %s" % (str(cat), str(sel_cat)))

	if constInfo.ENABLE_RACE_CATEGORY:
		def __SelectRaceCategory(self, category):
			self.jobSelection[category] = True

		def __UnselectRaceCategory(self, category):
			self.jobSelection[category] = False

	def __StartSearch(self):
		wnd = self.main["search"]

		auction.ClearSearchData()

		# text
		searchText = wnd["name_text"].GetText()
		if searchText:
			auction.SetSearchType(auction.SEARCH_TYPE_ITEM if not self.main["strict_search_checkbox"].IsChecked() else auction.SEARCH_TYPE_ITEM_STRICT)
			auction.SetSearchText(searchText)

		# sort
		auction.SetSearchSinglePriceOrder(True)
		if self.currentSortType == 1:
			auction.SetSearchSortOrderType(0, auction.SEARCH_ORDER_NAME, False)
		elif self.currentSortType > 1:
			auction.SetSearchSortOrderType(1, auction.SEARCH_ORDER_NAME, True)
			if self.currentSortType == 2:
				auction.SetSearchSortOrderType(0, auction.SEARCH_ORDER_PRICE, True)
			elif self.currentSortType == 3:
				auction.SetSearchSortOrderType(0, auction.SEARCH_ORDER_PRICE, False)

		# category
		catOption = self.CATEGORY_LIST[self.selectedCat]
		if catOption.has_key("type"):
			auction.SetSearchItemTypes(catOption["type"])
			if catOption.has_key("sub_type"):
				try:
					auction.SetSearchItemSubTypes(catOption["sub_type"])
				except:
					tchat("error at %s" % str(catOption["sub_type"]))
		if catOption.has_key("is_mine"):
			auction.SetSearchOnlySelfItem(catOption["is_mine"])

		if constInfo.ENABLE_RACE_CATEGORY:
			wIncludeAntiFlagMax = 0
			for x in xrange(4):
				wIncludeAntiFlagMax += self.JOB_TO_ANTIFLAG[x]

			wIncludeAntiFlag = wIncludeAntiFlagMax
			for x in xrange(4):
				if not self.jobSelection[x]:
					wIncludeAntiFlag -= self.JOB_TO_ANTIFLAG[x]
			if wIncludeAntiFlag == 0:
				wIncludeAntiFlag = wIncludeAntiFlagMax

			auction.SetSearchAntiFlag(wIncludeAntiFlag)

		# cooldown
		if searchText in constInfo.LAST_SHOP_SEARCH:
			if constInfo.LAST_SHOP_SEARCH[searchText] > app.GetTime() - 3:
				chat.AppendChat(1, localeInfo.AUCTION_COOLDOWN % 3)
				return
		constInfo.LAST_SHOP_SEARCH[searchText] = app.GetTime()

		# search
		self.currentPage = 0
		self.lastBuyID = -1
		self.lastTakeID = -1
		self.lastMarkID = -1
		auction.SendSearchPacket(0)

		# change state
		self.state = self.STATE_LOADING
		self.RefreshState()

	def __OnChangeItemPage(self, change):
		auction.SetContainerType(auction.CONTAINER_SEARCH)
		newPage = min(auction.GetMaxPageCount(), max(0, self.currentPage + change))
		if self.currentPage == newPage:
			return

		# search
		self.currentPage = newPage
		auction.SendSearchPacket(newPage)

		# change state
		self.state = self.STATE_LOADING
		self.RefreshState()

	def __OnScrollItemList(self):
		wnd = self.main["item"]

		maxBasePos = wnd["list"].GetScrollLen()
		basePos = int(wnd["scroll"].GetPos() * maxBasePos)
		if basePos != wnd["list"].GetBasePos():
			wnd["list"].SetBasePos(basePos)

	def OnMouseWheel(self, len):
		wnd = self.main["item"]

		if wnd["list"].IsInPosition() and wnd["scroll"].IsShow():
			basePos = wnd["list"].GetBasePos() + constInfo.WHEEL_TO_SCROLL(len)
			if basePos < 0:
				basePos = 0
			maxBasePos = wnd["list"].GetScrollLen()
			if basePos > maxBasePos:
				basePos = maxBasePos
			newPos = float(basePos) / float(max(1, maxBasePos))
			wnd["scroll"].SetPos(newPos)
			return True

		return False

	def OnItemQuestionTake(self, itemID):
		if self.lastTakeID != -1:
			return

		auction.SetContainerType(auction.CONTAINER_SEARCH)
		item.SelectItem(1, 2, auction.GetItemVnum(itemID))
		w, h = item.GetItemSize()

		if player.FindEmptyInventory(h) == -1:
			self.__ShowMessage(localeInfo.SHOP_INVENTORY_FULL)
			return

		self.questionWindow.SAFE_SetAcceptEvent(self.OnItemTake, itemID)
		self.questionWindow.Open(itemID, localeInfo.AUCTION_QUESTION_REALLY_TAKE_ITEM_TITLE, localeInfo.AUCTION_QUESTION_REALLY_TAKE_ITEM)

	def OnItemTake(self, itemID):
		if self.lastTakeID != -1:
			return

		auction.SetContainerType(auction.CONTAINER_SEARCH)
		auction.SendTakeItemPacket(auction.GetItemID(itemID))
		self.lastTakeID = itemID

		self.questionWindow.Hide()

	def OnItemMark(self, itemID):
		if self.lastMarkID != -1:
			return

		self.lastMarkID = itemID
		auction.SetContainerType(auction.CONTAINER_SEARCH)
		auction.SendMarkShopPacket(auction.GetItemID(itemID))

	def OnItemBuy(self, itemID):
		if self.lastBuyID != -1:
			return

		auction.SetContainerType(auction.CONTAINER_SEARCH)
		itemPrice = auction.GetItemPrice(itemID)

		if itemPrice > player.GetElk():
			self.__ShowMessage(localeInfo.AUCTION_MESSAGE_NOT_ENOUGH_MONEY, True)
		else:
			vnum = auction.GetItemVnum(itemID)
			item.SelectItem(1, 2, vnum)
			w, h = item.GetItemSize()
			tchat("vnum " + str(vnum) + " h " + str(h) + " cell " + str(player.FindEmptyInventory(h)))

			if player.FindEmptyInventory(h) == -1:
				self.__ShowMessage(localeInfo.SHOP_INVENTORY_FULL)
			else:
				auction.SendBuyItemPacket(auction.GetItemID(itemID), auction.GetItemPrice(itemID))
				self.lastBuyID = itemID

		self.questionWindow.Hide()

	#################################################
	## EXTERN FUNCTIONS
	#################################################

	def ShowItems(self):
		self.state = self.STATE_DISPLAY
		self.RefreshState()

	def SearchItemVnum(self, vnum):
		wnd = self.main["search"]

		item.SelectItem(1, 2, vnum)
		wnd["name_text"].SetText(item.GetItemName())
		self.__OnSelectCategory("all", True)

	def ShowGameMessage(self, msg):
		wnd = self.main["item"]

		if self.GAME_MESSAGE_LIST.has_key(msg):
			if msg.startswith("MARK_"):
				itemID = self.lastMarkID
				self.lastMarkID = -1
				if self.__IsPremium():
					msg = "PREMIUM_" + msg
					itemPrice = auction.GetItemPrice(itemID)
					self.questionWindow.SAFE_SetAcceptEvent(self.OnItemBuy, itemID)
					self.questionWindow.Open(itemID, localeInfo.AUCTION_QUESTION_REALLY_BUY_ITEM_TITLE, self.GAME_MESSAGE_LIST[msg] % localeInfo.NumberToMoneyString(itemPrice))
					return

			self.__ShowMessage(self.GAME_MESSAGE_LIST[msg], True)

			auction.SetContainerType(auction.CONTAINER_SEARCH)
			if self.lastTakeID != -1 and (msg == "ITEM_TAKE_NOT_EXIST" or msg == "ITEM_TAKE_SUCCESS"):
				auction.RemoveItem(self.lastTakeID)
				oldPos = wnd["scroll"].GetPos()
				self.RefreshItems()
				if wnd["scroll"].IsShow():
					wnd["scroll"].SetPos(oldPos)
				self.lastTakeID = -1

			if self.lastBuyID != -1 and (msg == "ITEM_BUY_SUCCESS" or msg == "ITEM_BUY_NOT_EXIST" or msg == "ITEM_WRONG_PRICE" or msg == "ITEM_BUY_TIMEOUT"):
				auction.RemoveItem(self.lastBuyID)
				oldPos = wnd["scroll"].GetPos()
				self.RefreshItems()
				if wnd["scroll"].IsShow():
					wnd["scroll"].SetPos(oldPos)
				self.lastBuyID = -1
		else:
			self.__ShowMessage("Unknown message: \"%s\"" % msg)

		# stop loading on message
		if self.state == self.STATE_LOADING:
			self.state = self.STATE_NONE
			self.RefreshState()
