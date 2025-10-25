import ui
import localeInfo
import uiToolTip
import item
import playerSettingModule
import wndMgr
import app
import auction
import networkModule
import player
import mouseModule
import skill
import grp
import chat
import cfg
import constInfo
import uiCommon
import snd
import uiPrivateShopBuilder
import uiShop
import net
import datetime

class AuctionWindow(ui.ScriptWindow):

	class PopupDialog(networkModule.PopupDialog):

		def __init__(self):
			networkModule.PopupDialog.__init__(self, False)

		def __del__(self):
			networkModule.PopupDialog.__del__(self)

		def Open(self, msg):
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

			textLine = ui.TextLine()
			textLine.SetParent(self)
			textLine.SetWindowHorizontalAlignCenter()
			textLine.SetHorizontalAlignCenter()
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
			itemVnum = auction.GetItemVnum(itemID)
			tchat("Open [ID %d Vnum %d]" % (itemID, itemVnum))
			item.SelectItem(1, 2, itemVnum)

			self.itemImage.LoadImage(item.GetIconImageFileName())
			self.itemToolTip.SetAuctionItemByID(auction.CONTAINER_SEARCH, itemID)
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

	class ToolTip(ui.Window):

		MIN_X = 5
		MAX_X = wndMgr.GetScreenWidth() - 5
		MIN_Y = 5
		MAX_Y = wndMgr.GetScreenHeight() - 5

		def __init__(self):
			ui.Window.__init__(self)
			self.AddFlag("float")
			self.AddFlag("not_pick")

			textLine = ui.TextLine()
			textLine.SetParent(self)
			textLine.SetFontColor(1.0, 0.7843, 0.0)
			textLine.SetOutline()
			textLine.Show()
			self.textLine = textLine

		def __del__(self):
			ui.Window.__del__(self)

		def SetText(self, text):
			self.textLine.SetText(text)
			self.SetSize(self.textLine.GetTextWidth(), self.textLine.GetTextHeight())

		def ShowToolTip(self):
			self.SetTop()
			self.Show()

		def HideToolTip(self):
			self.Hide()

		def OnUpdate(self):
			(mouseX, mouseY) = wndMgr.GetMousePosition()
			xPos = mouseX - self.GetWidth() / 2
			yPos = mouseY - self.GetHeight() - 5

			if xPos < self.MIN_X:
				xPos = self.MIN_X
			elif xPos > self.MAX_X - self.GetWidth():
				xPos = self.MAX_X - self.GetWidth()
			if yPos < self.MIN_Y:
				yPos = self.MIN_Y
			elif yPos > self.MAX_Y - self.GetHeight():
				yPos = self.MAX_Y - self.GetHeight()

			self.SetPosition(xPos, yPos)

	class AuctionItem(ui.InputField):

		MARGIN = 2

		ITEM_WIDTH = 100
		ITEM_HEIGHT = 32 + MARGIN * 2

		BG_ALPHA = 0.4

		def __init__(self):
			ui.InputField.__init__(self)

			self.oldCursor = -1
			self.isMine = False

			self.SetSize(self.ITEM_WIDTH, self.ITEM_HEIGHT)
			self.SetAlpha(self.BG_ALPHA)

			self.timeEnd = 0

			self.toolTip = uiToolTip.ItemToolTip()
			self.toolTip.HideToolTip()

			self.__BuildWindow()

			self.SetButtonStyleOverOnly(True)

		def __del__(self):
			ui.InputField.__del__(self)

		def __BuildWindow(self):
			itemName = ui.TextLine()
			itemName.SetParent(self)
			itemName.SetPosition(self.MARGIN, self.MARGIN)
			itemName.Show()

			subInfo = ui.ExtendedTextLine()
			subInfo.AddFlag("not_pick")
			subInfo.SetParent(self)
			subInfo.SetWindowVerticalAlignBottom()
			subInfo.SetPosition(self.MARGIN, 0)
			subInfo.Show()

			sellerName = ui.TextLine()
			sellerName.SetParent(self)
			sellerName.SetPosition(self.MARGIN + 175, 0)
			sellerName.SetWindowVerticalAlignCenter()
			sellerName.SetVerticalAlignCenter()
			sellerName.Show()

			timeLeftLine = ui.TextLine()
			timeLeftLine.SetParent(self)
			timeLeftLine.SetWindowHorizontalAlignRight()
			timeLeftLine.SetHorizontalAlignRight()
			timeLeftLine.SetWindowVerticalAlignCenter()
			timeLeftLine.SetVerticalAlignCenter()
			timeLeftLine.SetPosition(10, 0)
			timeLeftLine.Show()

			self.itemName = itemName
			self.subInfo = subInfo
			self.sellerName = sellerName
			self.timeLeftLine = timeLeftLine

		def Hide(self):
			ui.InputField.Hide(self)
			try:
				self.OnMouseOverOut()
			except:
				pass

		def SetItemID(self, itemID):
			self.itemID = itemID
			self.Refresh()

		def Refresh(self):
			if self.itemID < 0:
				return

			itemVnum = auction.GetItemVnum(self.itemID)
			itemCount = auction.GetItemCount(self.itemID)
			itemMetinSlot = [auction.GetItemSocket(self.itemID, i) for i in xrange(player.METIN_SOCKET_MAX_NUM)]
			itemOwnerName = auction.GetItemOwnerName(self.itemID)
			itemPrice = auction.GetItemPrice(self.itemID)
			self.__SetItemData(itemVnum, itemCount, itemMetinSlot, itemPrice, itemOwnerName)

		#	self.timeEnd = auction.GetItemInsertionTime(self.itemID) + 60 * 60 * 24 * 7
			self.timeEnd = auction.GetItemTimeoutTime(self.itemID)
			self.__RefreshTimer()

			self.toolTip.SetAuctionItemByID(auction.CONTAINER_SEARCH, self.itemID)
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
			self.subInfo.SetText(localeInfo.AUCTION_ITEM_SUB_INFO % localeInfo.NumberToMoneyString(price))
			self.subInfo.SetPosition(self.subInfo.GetLeft(), self.MARGIN + 3 + self.subInfo.GetHeight())

			self.sellerName.SetText(owner)

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
			ui.InputField.OnMouseOverIn(self)
			self.ShowToolTip()

			app.SetCursor(self.__GetSelfCursor())

		def OnMouseOverOut(self):
			ui.InputField.OnMouseOverOut(self)
			self.HideToolTip()

			app.SetCursor(0)

		def OnUpdate(self):
			self.__RefreshTimer()

	JOB_IMAGE_ALPHA_UNSELECT = 0.35
	JOB_IMAGE_ALPHA_OVER_UNSELECT = 0.8
	JOB_IMAGE_ALPHA_OVER_SELECT = 0.55
	JOB_IMAGE_ALPHA_SELECT = 1.0
	JOB_TO_ANTIFLAG = [
		item.ITEM_ANTIFLAG_WARRIOR,
		item.ITEM_ANTIFLAG_ASSASSIN,
		item.ITEM_ANTIFLAG_SURA,
		item.ITEM_ANTIFLAG_SHAMAN,
	]

	TEXT_TYPE_LIST = [
		[auction.SEARCH_TYPE_NONE, localeInfo.TEXT_TYPE_NONE, ""],
		[auction.SEARCH_TYPE_ITEM, localeInfo.TEXT_TYPE_ITEMNAME],
		[auction.SEARCH_TYPE_PLAYER, localeInfo.TEXT_TYPE_PLAYERNAME],
	]

	ITEM_TYPE_LIST = [
		[item.ITEM_TYPE_NONE, localeInfo.ITEM_TYPE_NONE, localeInfo.ITEM_TYPE_NONE_DISPLAY],
		[item.ITEM_TYPE_WEAPON, localeInfo.ITEM_TYPE_WEAPON],
		[item.ITEM_TYPE_ARMOR, localeInfo.ITEM_TYPE_ARMOR],
		[item.ITEM_TYPE_METIN, localeInfo.ITEM_TYPE_METIN],
		[item.ITEM_TYPE_FISH, localeInfo.ITEM_TYPE_FISH],
		[item.ITEM_TYPE_QUEST, localeInfo.ITEM_TYPE_QUEST],
		[item.ITEM_TYPE_POLYMORPH, localeInfo.ITEM_TYPE_POLYMORPH],
		[item.ITEM_TYPE_MATERIAL, localeInfo.ITEM_TYPE_MATERIAL],
		[item.ITEM_TYPE_MOUNT, localeInfo.ITEM_TYPE_MOUNT],
		# [item.ITEM_TYPE_SPHAERA, localeInfo.ITEM_TYPE_SPHAERA],
		[item.ITEM_TYPE_COSTUME, localeInfo.ITEM_TYPE_COSTUME],
	]

	ITEM_SUBTYPE_LIST = {
		item.ITEM_TYPE_WEAPON : [
			[0, localeInfo.ITEM_SUBTYPE_NONE, localeInfo.ITEM_SUBTYPE_NONE_DISPLAY],
			[1+item.WEAPON_SWORD, localeInfo.ITEM_SUBTYPE_WEAPON_SWORD],
			[1+item.WEAPON_DAGGER, localeInfo.ITEM_SUBTYPE_WEAPON_DAGGER],
			[1+item.WEAPON_BOW, localeInfo.ITEM_SUBTYPE_WEAPON_BOW],
			[1+item.WEAPON_TWO_HANDED, localeInfo.ITEM_SUBTYPE_WEAPON_TWO_HANDED],
			[1+item.WEAPON_BELL, localeInfo.ITEM_SUBTYPE_WEAPON_BELL],
			[1+item.WEAPON_FAN, localeInfo.ITEM_SUBTYPE_WEAPON_FAN],
			[1+item.WEAPON_ARROW, localeInfo.ITEM_SUBTYPE_WEAPON_ARROW],
		],
		item.ITEM_TYPE_ARMOR : [
			[0, localeInfo.ITEM_SUBTYPE_NONE, localeInfo.ITEM_SUBTYPE_NONE_DISPLAY],
			[1+item.ARMOR_BODY, localeInfo.ITEM_SUBTYPE_ARMOR_BODY],
			[1+item.ARMOR_HEAD, localeInfo.ITEM_SUBTYPE_ARMOR_HEAD],
			[1+item.ARMOR_SHIELD, localeInfo.ITEM_SUBTYPE_ARMOR_SHIELD],
			[1+item.ARMOR_WRIST, localeInfo.ITEM_SUBTYPE_ARMOR_WRIST],
			[1+item.ARMOR_FOOTS, localeInfo.ITEM_SUBTYPE_ARMOR_FOOTS],
			[1+item.ARMOR_NECK, localeInfo.ITEM_SUBTYPE_ARMOR_NECK],
			[1+item.ARMOR_EAR, localeInfo.ITEM_SUBTYPE_ARMOR_EAR],
		],
		item.ITEM_TYPE_FISH : [
			[0, localeInfo.ITEM_SUBTYPE_NONE, localeInfo.ITEM_SUBTYPE_NONE_DISPLAY],
			[1+item.FISH_ALIVE, localeInfo.ITEM_SUBTYPE_FISH_ALIVE],
			[1+item.FISH_DEAD, localeInfo.ITEM_SUBTYPE_FISH_GRILLED],
		],
		item.ITEM_TYPE_MOUNT : [
			[0, localeInfo.ITEM_SUBTYPE_NONE, localeInfo.ITEM_SUBTYPE_NONE_DISPLAY],
			[1+item.MOUNT_SUB_SUMMON, localeInfo.ITEM_SUBTYPE_MOUNT_SUB_SUMMON],
			[1+item.MOUNT_SUB_FOOD, localeInfo.ITEM_SUBTYPE_MOUNT_SUB_FOOD],
			[1+item.MOUNT_SUB_REVIVE, localeInfo.ITEM_SUBTYPE_MOUNT_SUB_REVIVE],
		],
		item.ITEM_TYPE_COSTUME : [
			[0, localeInfo.ITEM_SUBTYPE_NONE, localeInfo.ITEM_SUBTYPE_NONE_DISPLAY],
			[1+item.COSTUME_TYPE_BODY, localeInfo.ITEM_SUBTYPE_COSTUME_BODY],
#			[1+item.COSTUME_TYPE_HAIR+10, localeInfo.ITEM_SUBTYPE_COSTUME_HAIR_M],
#			[1+item.COSTUME_TYPE_HAIR+11, localeInfo.ITEM_SUBTYPE_COSTUME_HAIR_W],
			[1+item.COSTUME_TYPE_ACCE, localeInfo.ITEM_SUBTYPE_COSTUME_ACCE],
		],
	}

	ORDER_STATE_ASC = ui.StateButton.STATE_CLOSED
	ORDER_STATE_DESC = ui.StateButton.STATE_OPEN
	ORDER_STATE_TEXT = {
		ORDER_STATE_ASC : localeInfo.AUCTION_ORDER_TOOLTIP_TEXT_ASC,
		ORDER_STATE_DESC : localeInfo.AUCTION_ORDER_TOOLTIP_TEXT_DESC,
	}
	PRICE_CHANGE_STATE_TEXT = {
		ORDER_STATE_ASC : localeInfo.AUCTION_PRICE_CHANGE_TOOLTIP_TEXT_ASC,
		ORDER_STATE_DESC : localeInfo.AUCTION_PRICE_CHANGE_TOOLTIP_TEXT_DESC,
	}
	PRICE_DISPLAY_STATE_TEXT = {
		ORDER_STATE_ASC : localeInfo.AUCTION_PRICE_DISPLAY_TEXT_ASC,
		ORDER_STATE_DESC : localeInfo.AUCTION_PRICE_DISPLAY_TEXT_DESC,
	}

	ORDER_MOVE_Y_SPEED = 60
	LIST_BOX_MAX_ITEM_COUNT = 8

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
	}

	MAX_PAGE_COUNT_BUTTON_DISPLAY = 9

	def __init__(self):
		ui.ScriptWindow.__init__(self)

		self.AddFlag("float")
		self.AddFlag("movable")

		self.jobSelection = [True for i in xrange(playerSettingModule.JOB_MAX_NUM)]
		self.searchOrderDownIdx = -1
		self.searchOrder = [i for i in xrange(auction.SEARCH_ORDER_MAX_NUM)]
		self.isShowItems = False
		self.curPageIndex = 0
		self.lastBuyID = -1
		self.lastTakeID = -1
		self.sellItemSelected = None

		self.popupWindow = self.PopupDialog()
		# self.popupWindow.LoadDialog()
		self.popupWindow.Close()

		self.questionWindow = self.QuestionDialog()
		self.questionWindow.Close()

		self.premiumToolTip = uiToolTip.ToolTip()
		self.premiumToolTip.HideToolTip()

		self.__LoadWindow()

	def __del__(self):
		ui.ScriptWindow.__del__(self)

	def Destroy(self):
		self.__Search_Save()
		self.Close()
		ui.ScriptWindow.Destroy(self)

	def __LoadWindow_InitListButtonText(self, wnd, listData):
		key = 0
		wnd["button"].key = key
		wnd["button_text"].noneText = listData[key][2]
		wnd["button_text"].SetText(listData[key][2])

		wnd["list_bg"].Hide()

	def __LoadWindow(self):
		try:
			pyScrLoader = ui.PythonScriptLoader()
			pyScrLoader.LoadScriptFile(self, "uiscript/AuctionWindow.py")
		except:
			import exception
			exception.Abort("AuctionWindow.LoadWindow.LoadObject")

		try:
			GetObject = self.GetChild

			self.board = GetObject("board")
			self.main = {
				"search" : {
					"wnd" : GetObject("search_window"),
					"text" : GetObject("search_text_edit_text"),

					"job" : [GetObject("search_race_checkbox%d" % (i + 1)) for i in xrange(playerSettingModule.JOB_MAX_NUM)],

					"levelLimit" : [GetObject("search_level_edit%d" % (i + 1)) for i in xrange(2)],
					"priceLimit" : [GetObject("search_price_edit%d" % (i + 1)) for i in xrange(2)],

					"premium_icon" : GetObject("premium_info_icon"),
					"premium_text" : GetObject("premium_info"),

					"searchBtn" : GetObject("search_button"),
					"resetBtn" : GetObject("search_reset_button"),
				},

				"item_wnd" : GetObject("item_window"),
				"item_list" : GetObject("item_list"),
				"item_scroll" : GetObject("item_scroll"),
				"item_loading" : GetObject("item_loading_image"),
				"item_left_btn" : GetObject("item_page_button_left"),
				"item_right_btn" : GetObject("item_page_button_right"),
			}
		except:
			import exception
			exception.Abort("AuctionWindow.LoadWindow.BindObject")

		try:
			self.toolTip = self.ToolTip()
			self.toolTip.HideToolTip()

			self.itemToolTip = uiToolTip.ItemToolTip()
			self.itemToolTip.HideToolTip()
		except:
			import exception
			exception.Abort("AuctionWindow.LoadWindow.CreateObject")

		# text type
		wnd = self.main["search"]["text"]
		wnd.SetEscapeEvent(ui.__mem_func__(self.OnPressEditEscapeKey), wnd)
		wnd.SetReturnEvent(ui.__mem_func__(self.__Search_OnClickSearchButton))

		wnd = self.main["search"]
		for i in xrange(playerSettingModule.JOB_MAX_NUM):
			wnd["job"][i].SAFE_SetEvent(self.__Search_OnClickJob, i)

		for i in xrange(2):
			wnd["levelLimit"][i].SetEscapeEvent(ui.__mem_func__(self.OnPressEditEscapeKey), wnd["levelLimit"][i])
			wnd["priceLimit"][i].SetEscapeEvent(ui.__mem_func__(self.OnPressEditEscapeKey), wnd["priceLimit"][i])

		wnd["premium_icon"].SAFE_SetStringEvent("MOUSE_OVER_IN", self.ShowPremiumToolTip)
		wnd["premium_icon"].SAFE_SetStringEvent("MOUSE_OVER_OUT", self.premiumToolTip.HideToolTip)

		self.main["search"]["searchBtn"].SAFE_SetEvent(self.__Search_OnClickSearchButton)
		self.main["search"]["resetBtn"].SAFE_SetEvent(self.__Search_OnClickResetButton)

		self.main["item_list"].SetScrollBar(self.main["item_scroll"])
		self.main["item_scroll"].Hide()
		self.main["item_loading"].Hide()
		self.main["item_left_btn"].SAFE_SetEvent(self.__Item_OnClickLeftPageButton)
		self.main["item_left_btn"].Hide()
		self.main["item_right_btn"].SAFE_SetEvent(self.__Item_OnClickRightPageButton)
		self.main["item_right_btn"].Hide()

		self.board.SetCloseEvent(ui.__mem_func__(self.Close))

		self.__Search_Load()
		self.Refresh()

	def __IsPremium(self):
		return constInfo.AUCTION_PREMIUM

	def RefreshPremium(self):
		wndText = self.main["search"]["premium_text"]
		if self.__IsPremium():
			wndText.SetText(localeInfo.AUCTION_PREMIUM_TEXT_ACTIVE)
			wndText.SetPackedFontColor(uiToolTip.ToolTip.POSITIVE_COLOR)
		else:
			wndText.SetText(localeInfo.AUCTION_PREMIUM_TEXT_INACTIVE)
			wndText.SetPackedFontColor(uiToolTip.ToolTip.NEGATIVE_COLOR)

	def ShowPremiumToolTip(self):
		self.premiumToolTip.ClearToolTip()
		if self.__IsPremium():
			self.premiumToolTip.AppendDescription(localeInfo.AUCTION_PREMIUM_INFO_ACTIVE, 26)
		else:
			self.premiumToolTip.AppendDescription(localeInfo.AUCTION_PREMIUM_INFO_INACTIVE, 26)
		self.premiumToolTip.ShowToolTip()

	def OnMouseWheel(self, len):
		if self.main["item_list"].IsInPosition() and self.main["item_scroll"].IsShow():
			basePos = self.main["item_list"].GetBasePos() + constInfo.WHEEL_TO_SCROLL(len)
			if basePos < 0:
				basePos = 0
			maxBasePos = self.main["item_list"].GetScrollLen()
			if basePos > maxBasePos:
				basePos = maxBasePos
			newPos = float(basePos) / float(max(1, maxBasePos))
			self.main["item_scroll"].SetPos(newPos)
			return True

		return False

	def __Item_BuildPageButtons(self, pageCount, curPageIndex = -1):
		self.main["item_page_buttons"] = []

		self.main["item_left_btn"].Hide()
		self.main["item_right_btn"].Hide()

		displayBtnCount = min(pageCount, self.MAX_PAGE_COUNT_BUTTON_DISPLAY)

		maxWidth = (16 + 4) * displayBtnCount - 4
		startX = self.main["item_wnd"].GetLeft() + (self.main["item_wnd"].GetWidth() - maxWidth) / 2

		if curPageIndex == -1:
			startIdx = 0
		else:
			startIdx = max(0, curPageIndex - self.MAX_PAGE_COUNT_BUTTON_DISPLAY / 2)
			if startIdx + self.MAX_PAGE_COUNT_BUTTON_DISPLAY > pageCount:
				startIdx = max(0, pageCount - self.MAX_PAGE_COUNT_BUTTON_DISPLAY)

		if curPageIndex > 0:
			self.main["item_left_btn"].Show()
		if curPageIndex + 1 < pageCount:
			self.main["item_right_btn"].Show()

		for i in xrange(displayBtnCount):
			btn = ui.RadioButton()
			btn.SetParent(self)
			btn.SetUpVisual("d:/ymir work/ui/public/xxsmall_button_01.tga")
			btn.SetOverVisual("d:/ymir work/ui/public/xxsmall_button_02.tga")
			btn.SetDownVisual("d:/ymir work/ui/public/xxsmall_button_03.tga")
			#btn.SetDisableVisual("d:/ymir work/ui/public/small_button_04.sub")
			btn.SetText(str(startIdx + i + 1))
			btn.SetPosition(startX + (btn.GetWidth() + 4) * i, self.main["item_wnd"].GetBottom() + 4)
			if startIdx + i == curPageIndex:
				btn.Down()
			btn.SAFE_SetEvent(self.__Item_OnClickPageButton, startIdx + i)
			btn.Show()
			self.main["item_page_buttons"].append(btn)

	def Open(self):
		self.SetCenterPosition()
		self.Show()

	def Close(self):
		self.Hide()

		# kill focus of editboxes
		self.main["search"]["text"].KillFocus()
		for i in xrange(2):
			self.main["search"]["levelLimit"][i].KillFocus()
			self.main["search"]["priceLimit"][i].KillFocus()

		# hide tooltip
		self.premiumToolTip.HideToolTip()

	def ShowToolTip(self, text):
		self.toolTip.SetText(text)
		self.toolTip.ShowToolTip()

	def ShowItemToolTip(self, pos):
		self.itemToolTip.SetInventoryItem(pos)

	def HideToolTip(self):
		self.toolTip.HideToolTip()
		self.itemToolTip.HideToolTip()

	def __Search_OnClickJob(self, jobIndex):
		wnd = self.main["search"]["job"][jobIndex]

		if wnd.IsChecked():
			self.jobSelection[jobIndex] = True
		else:
			self.jobSelection[jobIndex] = False

	def __Search_LoadListBox(self, wnd, listData):
		height = wnd["list_box"].GetStepSize() * (len(listData) - 1)
		maxHeight = wnd["list_box"].GetStepSize() * self.LIST_BOX_MAX_ITEM_COUNT

		wnd["list_bg"].SetSize(wnd["list_bg"].GetWidth(), min(height, maxHeight) + 4 * 2)
		if height <= maxHeight:
			wnd["list_box"].SetSize(wnd["list_bg"].GetWidth() - 4 * 2, height)
			wnd["list_scroll"].Hide()
		else:
			wnd["list_box"].SetSize(wnd["list_bg"].GetWidth() - ui.ScrollBar.SCROLLBAR_WIDTH - 4 * 2, maxHeight)
			wnd["list_scroll"].LockScroll()
			wnd["list_scroll"].SetScrollBarSize(maxHeight)
			wnd["list_scroll"].SetMiddleBarSize(float(self.LIST_BOX_MAX_ITEM_COUNT) / (len(listData) - 1))
			wnd["list_scroll"].SetPos(0)
			wnd["list_scroll"].UnlockScroll()
			wnd["list_scroll"].Show()

		wnd["list_box"].ClearItem()
		for i in xrange(len(listData)):
			if listData[i][0] == wnd["button"].key:
				continue

			wnd["list_box"].InsertItem(listData[i][0], listData[i][1])

		wnd["list_bg"].SetTop()
		wnd["list_bg"].Show()

	def __Search_ToggleListBox(self, wnd, listData):
		if wnd["list_bg"].IsShow():
			wnd["list_bg"].Hide()
		else:
			self.__Search_HideAllListBox()
			self.__Search_LoadListBox(wnd, listData)

	def __Search_SelectListBoxItem(self, wnd, key, name):
		wnd["button"].key = key
		if self.main["search"]["textType"] != wnd:
			if key != 0:
				wnd["button_text"].SetText(name)
			else:
				wnd["button_text"].SetText(wnd["button_text"].noneText)

		# update item subtype listbox
		if self.main["search"]["textType"] == wnd:
			self.__Search_RefreshText()
		elif self.main["search"]["itemType"] == wnd:
			self.__Search_RefreshItemSubTypeButton()
		# update end

		wnd["list_bg"].Hide()

	def __Search_CompleteTextSearch(self):
		wnd = self.main["search"]["textType"]

		if wnd["button_text_hint"].GetText():
			oldText = wnd["button_text"].GetText()
			wnd["button_text"].SetText(oldText + wnd["button_text_hint"].GetText()[len(oldText)+1:])
			wnd["button_text"].SetEndPosition()

	def __Search_RefreshItemSubTypeButton(self):
		wnd = self.main["search"]

		itemType = wnd["itemType"]["button"].key
		if self.ITEM_SUBTYPE_LIST.has_key(itemType):
			wnd["itemSubType"]["button"].SetButtonStyle(True)
			wnd["itemSubType"]["button"].SetEvent(ui.__mem_func__(self.__Search_ToggleListBox), wnd["itemSubType"], self.ITEM_SUBTYPE_LIST[itemType])
			wnd["itemSubType"]["button_text"].SetText(localeInfo.ITEM_SUBTYPE_NONE_DISPLAY)

		else:
			wnd["itemSubType"]["button"].key = 0
			wnd["itemSubType"]["button"].SetButtonStyle(False)
			wnd["itemSubType"]["button"].ClearEvent()
			wnd["itemSubType"]["button_text"].SetText(localeInfo.ITEM_SUBTYPE_DISABLED)

	def __Search_OnScrollListBox(self, wnd):
		pos = wnd["list_scroll"].GetPos()
		basePos = int((wnd["list_box"].GetItemCount() - self.LIST_BOX_MAX_ITEM_COUNT) * pos)
		if wnd["list_box"].GetBasePos() != basePos:
			wnd["list_box"].SetBasePos(basePos)

	def __Search_GetNextOrderPosition(self, yPos):
		curIdx = 0
		curMin = -1
		for i in xrange(auction.SEARCH_ORDER_MAX_NUM):
			curDif = abs(yPos - self.orderPositions[i])
			if curMin == -1 or curDif < curMin:
				curIdx = i
				curMin = curDif

		return curIdx

	def __Search_OrderMove(self, orderIndex, yPos):
		wnd = self.main["search"]["order"][orderIndex]["button"]

		if wnd.GetTop() == yPos:
			return

		wnd.moveStartTime = app.GetTime()
		wnd.moveStartY = wnd.GetTop()
		wnd.moveEndY = yPos

		if wnd.moveStartY < wnd.moveEndY:
			wnd.moveChangeValue = self.ORDER_MOVE_Y_SPEED
		else:
			wnd.moveChangeValue = -self.ORDER_MOVE_Y_SPEED

	def __Search_OrderMouseDown(self, orderIndex):
		wnd = self.main["search"]["order"][orderIndex]["button"]

		wnd.moveStartTime = 0

		xMouse, yMouse = wndMgr.GetMousePosition()
		wnd.mouseYPos = yMouse
		wnd.mouseWndYPos = wnd.GetTop()
		self.searchOrderDownIdx = orderIndex

		wnd.SetTop()

	def __Search_OrderMouseUp(self, orderIndex):
		wnd = self.main["search"]["order"][orderIndex]["button"]

		orderPos = self.__Search_GetNextOrderPosition(wnd.GetTop())
		wnd.SetPosition(wnd.GetLeft(), self.orderPositions[orderPos])

		self.searchOrderDownIdx = -1

	def __Search_OrderClickDirection(self, orderIndex):
		wnd = self.main["search"]["order"][orderIndex]["direction"]

		wnd.SetState(not wnd.GetState())
		wnd.SetToolTipText(self.ORDER_STATE_TEXT[wnd.GetState()])

	def __Search_OrderClickPriceChange(self):
		wnd = self.main["search"]["order"][auction.SEARCH_ORDER_PRICE]

		wnd["change"].SetState(not wnd["change"].GetState())
		wnd["change"].SetToolTipText(self.PRICE_CHANGE_STATE_TEXT[wnd["change"].GetState()])
		wnd["text"].SetText(self.PRICE_DISPLAY_STATE_TEXT[wnd["change"].GetState()])

	def __Search_GetKey(self, name):
		return self.main["search"][name]["button"].key

	def __Search_GetValue(self, name):
		return self.main["search"][name]["button_text"].GetText()

	def __Search_EnableButton(self):
		self.main["search"]["searchBtn"].Enable()

	def __Search_SetTextSearchOption_CheckSkillBook(self, text):
		if item.SelectByNamePart(text):
			if item.GetItemType() == item.ITEM_TYPE_SKILLBOOK and item.GetItemSubType() == item.SKILLBOOK_NORMAL:
				auction.SetSearchSocket0(item.GetSocket(0))
				item.SelectItem(1, 2, item.GetItemVnum())
				text = item.GetItemName()

		return text

	def __Search_SetTextSearchOption(self, text):
		auction.SetSearchSocket0(-1)
		auction.SetSearchValue0(-1)

		new_text = self.__Search_SetTextSearchOption_CheckSkillBook(text)
		auction.SetSearchText(new_text)

	def __Search_OnClickSearchButton(self):
		wnd = self.main["search"]

		# set settings
		if wnd["text"].GetText():
			auction.SetSearchType(auction.SEARCH_TYPE_ITEM)
		else:
			auction.SetSearchType(auction.SEARCH_TYPE_NONE)
		self.__Search_SetTextSearchOption(wnd["text"].GetText())

		wAntiFlag = 0
		for i in xrange(playerSettingModule.JOB_MAX_NUM):
			if self.jobSelection[i]:
				wAntiFlag = wAntiFlag | self.JOB_TO_ANTIFLAG[i]
		if wAntiFlag == 0:
			self.__ShowMessage(localeInfo.AUCTION_MESSAGE_INVALID_ANTIFLAG)
			return
		auction.SetSearchAntiFlag(wAntiFlag)

		auction.SetSearchItemType(0)

		auction.SetSearchLevelMin(wnd["levelLimit"][0].GetNumberText())
		auction.SetSearchLevelMax(wnd["levelLimit"][1].GetNumberText())
		auction.SetSearchPriceMin(wnd["priceLimit"][0].GetNumberText())
		auction.SetSearchPriceMax(wnd["priceLimit"][1].GetNumberText())
		auction.SetSearchOnlyAHItem(False)
		auction.SetSearchOnlySelfItem(False)

		auction.SetSearchSinglePriceOrder(False)
		auction.SetSearchSortOrderType(0, auction.SEARCH_ORDER_NAME, True) # True == ASC
		auction.SetSearchSortOrderType(1, auction.SEARCH_ORDER_PRICE, True) # True == ASC
		auction.SetSearchSortOrderType(2, auction.SEARCH_ORDER_DATE, True) # True == ASC

		self.__Search_Start()

	def __Search_Start(self):
		# search
		self.curPageIndex = 0
		self.lastTakeID = -1
		self.lastBuyID = -1
		auction.SendSearchPacket(0)
		self.main["search"]["searchBtn"].Disable()

		# set loading animation
		self.isShowItems = False
		self.__Item_BuildPageButtons(0)
		self.main["item_list"].Hide()
		self.main["item_scroll"].Hide()
		self.main["item_loading"].Show()

	def __Search_Load(self):
		wnd = self.main["search"]

	def __Search_Save(self):
		wnd = self.main["search"]

	def __Search_OnClickResetButton(self):
		wnd = self.main["search"]

		wnd["text"].SetText("")

		for jobIndex in xrange(playerSettingModule.JOB_MAX_NUM):
			self.jobSelection[jobIndex] = True
			wnd["job"][jobIndex].SetChecked(True)

		for i in xrange(2):
			wnd["levelLimit"][i].SetText("")
			wnd["priceLimit"][i].SetText("")

	def __ShowMessage(self, msg):
		self.popupWindow.Open(msg)

	def ShowGameMessage(self, msg):
		itemID = 0
		if msg.startswith("ITEM_INSERT_SUCCESS"):
			itemID = int(msg[len("ITEM_INSERT_SUCCESS"):])
			msg = msg[:len("ITEM_INSERT_SUCCESS")]

		if self.GAME_MESSAGE_LIST.has_key(msg):
#			if msg != "NO_ITEMS_FOUND" or auction.GetCurrentWindow() != auction.WINDOW_SELL:
			self.__ShowMessage(self.GAME_MESSAGE_LIST[msg])

			auction.SetContainerType(auction.CONTAINER_SEARCH)
			if self.lastTakeID != -1 and (msg == "ITEM_TAKE_NOT_EXIST" or msg == "ITEM_TAKE_SUCCESS"):
				auction.RemoveItem(self.lastTakeID)
				oldPos = self.main["item_scroll"].GetPos()
				self.__RefreshItems()
				if self.main["item_scroll"].IsShow():
					self.main["item_scroll"].SetPos(oldPos)
				self.lastTakeID = -1

			if self.lastBuyID != -1 and (msg == "ITEM_BUY_SUCCESS" or msg == "ITEM_BUY_NOT_EXIST" or msg == "ITEM_WRONG_PRICE" or msg == "ITEM_BUY_TIMEOUT"):
				auction.RemoveItem(self.lastBuyID)
				oldPos = self.main["item_scroll"].GetPos()
				self.__RefreshItems()
				if self.main["item_scroll"].IsShow():
					self.main["item_scroll"].SetPos(oldPos)
				self.lastBuyID = -1

#			if msg == "ITEM_INSERT_SUCCESS" and auction.GetCurrentWindow() == auction.WINDOW_SELL:
#				auction.AddInsertedItem(itemID)
#				self.__RefreshItems()
		else:
			self.__ShowMessage("Unknown message: \"%s\"" % msg)

		# stop loading on message
		self.main["item_loading"].Hide()
		self.__Search_EnableButton()

	def __RefreshItems(self):
		if self.isShowItems == False:
			return

		auction.SetContainerType(auction.CONTAINER_SEARCH)

		itemMaxCount = auction.GetItemMaxCount()
		isScrollBar = itemMaxCount > self.main["item_list"].GetViewItemCount()
		if isScrollBar:
			self.main["item_scroll"].SetMiddleBarSize(float(self.main["item_list"].GetViewItemCount()) / itemMaxCount)
			self.main["item_scroll"].Show()
			self.main["item_list"].SetItemSize(self.main["item_scroll"].GetLeft() - self.main["item_list"].GetLeft(), self.main["item_list"].GetItemHeight())
		else:
			self.main["item_scroll"].Hide()
			self.main["item_list"].SetItemSize(self.main["item_scroll"].GetRight() - self.main["item_list"].GetLeft(), self.main["item_list"].GetItemHeight())

		self.main["item_list"].RemoveAllItems()
		for i in xrange(itemMaxCount):
			newItem = self.AuctionItem()
			newItem.SetItemID(i)
			if auction.GetItemOwnerName(i) == player.GetName():
				newItem.SetEvent(ui.__mem_func__(self.__Item_OnQuestionTake), i)
			else:
				newItem.SetEvent(ui.__mem_func__(self.__Item_OnQuestionBuy), i)
			self.main["item_list"].AppendItem(newItem)

		self.main["item_list"].Show()
		self.main["item_loading"].Hide()

		if itemMaxCount > 0:
			self.__Item_BuildPageButtons(auction.GetMaxPageCount() + 1, min(self.curPageIndex, auction.GetMaxPageCount()))
		else:
			self.__Item_BuildPageButtons(0)

		self.__Search_EnableButton()

	def __Item_OnQuestionTake(self, itemID):
		if self.lastTakeID != -1:
			return

		self.questionWindow.SAFE_SetAcceptEvent(self.__Item_OnTake, itemID)
		self.questionWindow.Open(itemID, localeInfo.AUCTION_QUESTION_REALLY_TAKE_ITEM_TITLE, localeInfo.AUCTION_QUESTION_REALLY_TAKE_ITEM)

	def __Item_OnTake(self, itemID):
		if self.lastTakeID != -1:
			return

		auction.SendTakeItemPacket(auction.GetItemID(itemID))
		self.lastTakeID = itemID

		self.questionWindow.Hide()

	def __Item_OnQuestionBuy(self, itemID):
		if self.lastTakeID != -1:
			return

		if not self.__IsPremium():
			auction.SendMarkShopPacket(auction.GetItemOwnerID(itemID))

		else:
			itemPrice = auction.GetItemPrice(itemID)

			if itemPrice > player.GetElk():
				self.__ShowMessage(localeInfo.AUCTION_MESSAGE_NOT_ENOUGH_MONEY)
			else:
				self.questionWindow.SAFE_SetAcceptEvent(self.__Item_OnBuy, itemID)
				self.questionWindow.Open(itemID, localeInfo.AUCTION_QUESTION_REALLY_BUY_ITEM_TITLE, localeInfo.AUCTION_QUESTION_REALLY_BUY_ITEM % localeInfo.NumberToMoneyString(itemPrice))

	def __Item_OnBuy(self, itemID):
		if self.lastBuyID != -1:
			return

		itemPrice = auction.GetItemPrice(itemID)

		if itemPrice > player.GetElk():
			self.__ShowMessage(localeInfo.AUCTION_MESSAGE_NOT_ENOUGH_MONEY)
		else:
			auction.SendBuyItemPacket(auction.GetItemID(itemID), auction.GetItemOwnerName(itemID), auction.GetItemPrice(itemID))
			self.lastBuyID = itemID

		self.questionWindow.Hide()

	def ChangePage(self, pageIdx):
		self.curPageIndex = pageIdx
		self.lastBuyID = -1
		self.lastTakeID = -1
		auction.SendSearchPacket(pageIdx)

		for i in xrange(len(self.main["item_page_buttons"])):
			if i != pageIdx:
				self.main["item_page_buttons"][i].Disable()
		self.main["search"]["searchBtn"].Disable()
		self.main["left_page_button"][not auction.GetCurrentWindow()].Disable()

		self.isShowItems = False
		self.main["item_list"].Hide()
		self.main["item_scroll"].Hide()
		self.main["item_loading"].Show()

	def __Item_OnClickPageButton(self, pageIdx):
		self.curPageIndex = pageIdx
		self.lastBuyID = -1
		self.lastTakeID = -1
		auction.SendSearchPacket(pageIdx)

		for i in xrange(len(self.main["item_page_buttons"])):
			if i != pageIdx:
				self.main["item_page_buttons"][i].Disable()
		self.main["search"]["searchBtn"].Disable()

		self.isShowItems = False
		self.main["item_list"].Hide()
		self.main["item_scroll"].Hide()
		self.main["item_loading"].Show()

	def __Item_OnClickLeftPageButton(self):
		self.__Item_OnClickPageButton(max(0, self.curPageIndex - 10))
		
	def __Item_OnClickRightPageButton(self):
		self.__Item_OnClickPageButton(self.curPageIndex + 10)

	def Refresh(self):
		self.__RefreshItems()
		self.RefreshPremium()

	def ShowItems(self):
		self.isShowItems = True
		self.__RefreshItems()

	def OnPressEditEscapeKey(self, wnd):
		if not wnd.IsShowCursor() or wnd.GetText() == "":
			self.OnPressEscapeKey()
		else:
			wnd.SetText("")

	def OnPressEscapeKey(self):
		self.Close()
		return True

class AuctionInformerWindow(ui.ScriptWindow):

	def __init__(self):
		ui.ScriptWindow.__init__(self)

		self.itemToolTip = uiToolTip.ItemToolTip()
		self.itemToolTip.HideToolTip()

		self.closeEvent = None
		self.closeArgs = None

		self.__LoadWindow()

	def __del__(self):
		ui.ScriptWindow.__del__(self)

	def Destroy(self):
		self.closeEvent = None
		self.closeArgs = None
		self.Close()

	def __LoadWindow(self):
		try:
			pyScrLoader = ui.PythonScriptLoader()
			pyScrLoader.LoadScriptFile(self, "uiscript/AuctionInformerWindow.py")
		except:
			import exception
			exception.Abort("AuctionInformerWindow.LoadWindow.LoadObject")

		try:
			GetObject = self.GetChild

			self.board = GetObject("board")
			self.info = GetObject("info")
			self.icon = GetObject("icon")
			self.received_gold = GetObject("received_gold")
			self.close = GetObject("close")
		except:
			import exception
			exception.Abort("AuctionInformerWindow.LoadWindow.BindObject")

		self.icon.SAFE_SetStringEvent("MOUSE_OVER_IN", self.itemToolTip.ShowToolTip)
		self.icon.SAFE_SetStringEvent("MOUSE_OVER_OUT", self.itemToolTip.HideToolTip)
		self.close.SAFE_SetEvent(self.Close)

	def Open(self):
		itemVnum = auction.GetSoldItemVnum()
		itemCount = auction.GetSoldItemCount()
		itemMetin = [auction.GetSoldItemSocket(i) for i in xrange(player.METIN_SOCKET_MAX_NUM)]
		itemAttr = [(auction.GetSoldItemAttr(i)) for i in xrange(player.ATTRIBUTE_SLOT_MAX_NUM)]
		itemData = auction.GetSoldItemData()
		auctionType = auction.GetSoldItemAuctionType()
		paidGold = auction.GetSoldItemPaidGold()
		receivedGold = auction.GetSoldItemRecvGold()

		self.itemToolTip.ClearToolTip()
		self.itemToolTip.AddItemData(itemVnum, itemMetin, itemAttr)#, None, itemData)
		self.itemToolTip.HideToolTip()

		item.SelectItem(1, 2, itemVnum)

		itemName = item.GetItemName()
		if itemVnum == 50300:
			itemName = skill.GetSkillName(itemMetin[0]) + " " + itemName

		if itemCount == 1:
			self.info.SetText(localeInfo.AUCTION_INFORMER_INFO_TEXT % (itemName, localeInfo.NumberToMoneyString(paidGold)))
		else:
			self.info.SetText(localeInfo.AUCTION_INFORMER_INFO_MULTI_TEXT % (itemCount, itemName, localeInfo.NumberToMoneyString(paidGold)))
		self.icon.LoadImage(item.GetIconImageFileName())
		self.received_gold.SetText(localeInfo.AUCTION_INFORMER_RECEIVED_GOLD_TEXT % localeInfo.NumberToMoneyString(receivedGold))

		self.SetSize(self.GetWidth(), 65 + 20 + 18 + 24 + 20 + self.icon.GetHeight())
		self.board.SetSize(self.GetWidth(), self.GetHeight())

		self.SetCenterPosition()
		self.Show()
		self.SetTop()

	def SAFE_SetCloseEvent(self, event, *args):
		self.closeEvent = ui.__mem_func__(event)
		self.closeArgs = args

	def Close(self):
		self.Hide()
		self.itemToolTip.HideToolTip()

		if self.closeEvent:
			apply(self.closeEvent, self.closeArgs)

	def OnPressEscapeKey(self):
		self.Close()
		return True

class AuctionShopWindow(ui.ScriptWindow):

	class HistoryEntry(ui.Window):

		def __init__(self, name, price, buyer, date, isEven, whisperFn):
			ui.Window.__init__(self)

			self.name = name
			self.price = price
			self.buyer = buyer
			self.date = date
			self.isEven = isEven

			self.whisperFn = whisperFn
			self.LoadWindow()

		def __del__(self):
			ui.Window.__del__(self)

		def WhisperTo(self, playerName):
			if self.itemBuyerMsgIcon.IsInPosition() or self.itemBuyer.IsInPosition():
				if self.whisperFn:
					self.whisperFn(playerName)

		def LoadWindow(self):
			self.SetSize(314, 44)
			self.SetPosition(0, 0)

			self.background = ui.ImageBox()
			self.background.SetParent(self)
			self.background.LoadImage("d:/ymir work/ui/game/offlineshop/tab_main/history_bg{}.tga".format("_2" if self.isEven else ""))
			self.background.Show()

			if len(self.name) >= 19:
				self.name = self.name[ :16 ] + "..."

			self.itemName = ui.TextLine()
			self.itemName.SetParent(self.background)
			self.itemName.SetPosition(52 - 13, 14)
			self.itemName.SetHorizontalAlignCenter()
			self.itemName.SetText(self.name)
			self.itemName.Show()

			self.itemPrice = ui.TextLine()
			self.itemPrice.SetParent(self.background)
			self.itemPrice.SetPosition(130 - 1, 14)
			self.itemPrice.SetHorizontalAlignCenter()
			self.itemPrice.SetText(self.price[:-5])
			self.itemPrice.Show()

			self.yangIcon = ui.ImageBox()
			self.yangIcon.SetParent(self.itemPrice)
			self.yangIcon.LoadImage("d:/ymir work/ui/game/offlineshop/tab_sell/yang.tga")
			self.yangIcon.SetPosition(-(self.itemPrice.GetTextWidth() / 2) - 15, 1)
			self.yangIcon.Show()

			self.itemBuyer = ui.TextLine()
			self.itemBuyer.SetParent(self.background)
			self.itemBuyer.SetPosition(180 + 20 - 3, 14)
			self.itemBuyer.SetHorizontalAlignLeft()
			self.itemBuyer.SetText(self.buyer)
			self.itemBuyer.Show()

			self.itemBuyerMsgIcon = ui.ImageBox()
			self.itemBuyerMsgIcon.SetParent(self)
			self.itemBuyerMsgIcon.LoadImage("d:/ymir work/ui/game/offlineshop/tab_main/mail.tga")
			self.itemBuyerMsgIcon.SetPosition(180 - 3, 17)
			self.itemBuyerMsgIcon.SetStringEvent("MOUSE_LEFT_DOWN", self.WhisperTo, self.buyer)
			self.itemBuyerMsgIcon.Show()

			self.itemDate = ui.TextLine()
			self.itemDate.SetParent(self.background)
			self.itemDate.SetPosition(286, 14)
			self.itemDate.SetHorizontalAlignCenter()
			self.itemDate.SetText(self.date)
			self.itemDate.Show()

	def __init__(self):
		ui.ScriptWindow.__init__(self)
		self.questionDialog = None
		self.inputMoneyDlg = None
		self.offlineTakeMoneyDialog = uiShop.ShopDialog.InputTakeMoneyDialog(0)
		self.offlineTakeMoneyDialog.SAFE_SetOKEvent(self.OnTakeOfflineShopMoney)
		self.popup = None
		self.isTimeout = False
		self.tooltipItem = None

		self.itemPriceList = {}

		#new ones
		self.historyOpened = False
		self.isEven = False
		self.whisperFn = None

		self.timeHistory = 0

		if constInfo.FAST_MOVE_ITEM_COOLDOWN:
			self.fastMoveOfflineShopItem = 0

		self.__LoadDialog()

	def __del__(self):
		ui.ScriptWindow.__del__(self)

	def Refresh(self):
		if not auction.HasMyShop():
			self.Close()
			return

		self.RefreshTimeout()

		self.itemPriceList = {}

		for i in xrange(auction.SHOP_SLOT_COUNT):
			self.itemSlotWindow.ClearSlot(i)

		auction.SetContainerType(auction.CONTAINER_OWNED_SHOP)

		setItemInfo=self.itemSlotWindow.SetItemSlot
		for i in xrange(auction.GetItemMaxCount()):
			slot = auction.GetItemCell(i)
			vnum = auction.GetItemVnum(i)
			count = auction.GetItemCount(i)
			price = auction.GetItemPrice(i)

			if count <= 1:
				count = 0
			setItemInfo(slot, vnum, count)

			try:
				self.itemPriceList[vnum] = price
			except:
				pass

		self.itemSlotWindow.RefreshSlot()

		self.offlineMoneyText.SetText(localeInfo.NumberToMoneyString(auction.GetMyShopGold()))
		self.shopSign.SetText(auction.GetMyShopName())

	def RefreshTimeout(self):
		timeLeft = auction.GetMyShopTimeout()
		self.isTimeout = timeLeft == 0

		if self.isTimeout:
			# self.timeoutText.SetText(localeInfo.OFFLINE_SHOP_TIMEOUT_TEXT_TIMEOUT)
			self.timeoutText.SetText(localeInfo.SecondToDHMS(0, 60*60*24)) # display 0 seconds
			self.btnRenew.Enable()
		elif timeLeft > 0:
			self.timeoutText.SetText(localeInfo.SecondToDHMS(timeLeft, 60*60*24))
			self.btnRenew.Enable()
		else:
			self.timeoutText.SetText(localeInfo.OFFLINE_SHOP_TIMEOUT_TEXT_NOTIMEOUT)
			self.btnRenew.Disable()

	def __LoadDialog(self):
		try:
			PythonScriptLoader = ui.PythonScriptLoader()
			PythonScriptLoader.LoadScriptFile(self, "UIScript/AuctionShopWindow.py")
		except:
			import exception
			exception.Abort("OfflineShopWindow.LoadDialog.LoadObject")

		try:
			GetObject = self.GetChild
			self.board = GetObject("board")
			self.timeoutText = GetObject("TimeLeftText")
			self.itemSlotWindow = GetObject("ItemSlot")
			self.offlineMoneySlot = GetObject("Money_Slot")
			self.offlineMoneyText = GetObject("Money")
			self.btnClose = GetObject("CloseButton")
			self.btnRenew = GetObject("RenewButton")
			self.GetChild("title_bar").SetCloseEvent(ui.__mem_func__(self.Close))
			self.shopSign = GetObject("shop_name_text")
			self.btnHistory = self.GetChild("button_history")
			self.historyTab = self.GetChild("history")
			self.historyList = self.GetChild("history_listbox")
			self.scrollBar = self.GetChild("history_scrollbar")
			self.bottomBar = self.GetChild("bottom_bar")
		except:
			import exception
			exception.Abort("OfflineShopWindow.LoadDialog.BindObject")

		self.itemSlotWindow.SAFE_SetButtonEvent("LEFT", "EMPTY", self.SelectEmptySlot)
		self.itemSlotWindow.SAFE_SetButtonEvent("LEFT", "EXIST", self.SelectItemSlot)
		self.itemSlotWindow.SAFE_SetButtonEvent("RIGHT", "EXIST", self.UnselectItemSlot)

		self.itemSlotWindow.SetOverInItemEvent(ui.__mem_func__(self.OverInItem))
		self.itemSlotWindow.SetOverOutItemEvent(ui.__mem_func__(self.OverOutItem))

		self.offlineMoneySlot.SetEvent(ui.__mem_func__(self.TakeOfflineShopMoney))

		self.btnClose.SetEvent(ui.__mem_func__(self.AskCloseShop))
		self.btnRenew.SAFE_SetEvent(self.AskRenewShop)

		self.btnHistory.SetEvent(self.__OnBtnHistory)
		self.historyList.SetScrollBar(self.scrollBar)
		self.historyList.Show()
		self.historyTab.Hide()

		self.Refresh()

	def Destroy(self):
		self.Close()
		self.ClearDictionary()

		self.board = None
		self.tooltipItem = 0
		self.itemSlotWindow = 0
		self.btnClose = 0
		self.btnRenew = 0
		self.questionDialog = None
		self.inputMoneyDlg = None
		self.offlineTakeMoneyDialog = None
		self.popup = None

		self.shopSign = None
		self.btnHistory = None
		self.historyTab = None
		self.historyList = None
		self.scrollBar = None
		self.bottomBar = None

		ui.ScriptWindow.Destroy(self)

	def Open(self):
		self.offlineTakeMoneyDialog.UpdateMaxGold(auction.GetMyShopGold())
		# bugfix add items switch slots
		uiPrivateShopBuilder.g_isBuildingPrivateShop = True

		self.Refresh()
		self.SetTop()
		self.Show()

		if self.historyOpened:
			self.bottomBar.Show()
			self.itemSlotWindow.Show()
			self.ChangeBackgroundImage(True)
			self.historyTab.Hide()
			self.historyOpened = False

	def Close(self):
		self.OnCloseQuestionDialog()
		self.OnCloseInputMoneyDialog()
		self.offlineTakeMoneyDialog.Close()
		if self.tooltipItem:
			self.tooltipItem.HideToolTip()

		# bugfix add items switch slots
		uiPrivateShopBuilder.g_isBuildingPrivateShop = False
		self.Hide()

	def RefreshGold(self):
		self.offlineTakeMoneyDialog.UpdateMaxGold(auction.GetMyShopGold())
		self.Refresh()

	def CanTakeOutAllItems(self):
		inventory_grid = []
		# add pages
		max_slots = player.GetInventoryMaxNum()
		for page in xrange(player.INVENTORY_PAGE_COUNT):
			start_slot = player.INVENTORY_PAGE_SIZE * page
			if start_slot >= max_slots:
				break
			cur_slot_count = min(max_slots, start_slot + player.INVENTORY_PAGE_SIZE) - start_slot
			
			grid = uiCommon.ItemGrid(player.INVENTORY_PAGE_X_SLOTCOUNT, cur_slot_count / player.INVENTORY_PAGE_X_SLOTCOUNT)
			inventory_grid.append(grid)
			for i in xrange(player.INVENTORY_PAGE_SIZE):
				vnum = player.GetItemIndex(start_slot + i)
				if vnum == 0:
					continue

				item.SelectItem(1, 2, vnum)
				sockets = [player.GetItemMetinSocket(start_slot + i, j) for j in xrange(player.METIN_SOCKET_MAX_NUM)]
				w, h = item.GetItemSize()
				grid.add(i, h, (vnum, player.GetItemCount(start_slot + i), sockets))

		# try to add shop items
		auction.SetContainerType(auction.CONTAINER_OWNED_SHOP)
		for index in xrange(auction.GetItemMaxCount()):
			vnum = auction.GetItemVnum(index)
			count = auction.GetItemCount(index)
			item.SelectItem(1, 2, vnum)
			w, h = item.GetItemSize()
			sockets = [auction.GetItemSocket(index, i) for i in xrange(player.METIN_SOCKET_MAX_NUM)]

			if item.IsStackable():
				for grid in inventory_grid:
					if count <= 0:
						break

					for local_slot, slot_data in grid.items():
						slot_vnum = slot_data[0]
						slot_count = slot_data[1]
						slot_sockets = slot_data[2]

						if slot_vnum != vnum:
							continue

						check_sockets = True
						for i in xrange(player.METIN_SOCKET_MAX_NUM):
							if sockets[i] != slot_sockets[i]:
								check_sockets = False
								break

						if check_sockets:
							add_count = min(constInfo.ITEM_MAX_COUNT - slot_count, count)
							slot_data[1] += add_count
							count -= add_count
							if count <= 0:
								break

			if count > 0:
				grid_idx = 0
				for grid in inventory_grid:
					grid_idx += 1
					empty_pos = grid.find_free(h)
					if empty_pos < 0:
						continue

					grid.add(empty_pos, h, (vnum, count, sockets))
					count = 0
					break

			if count > 0:
				return False

		return True

	def AskCloseShop(self):
		if not self.CanTakeOutAllItems():
			popup = uiCommon.PopupDialog()
			popup.SetText(localeInfo.SHOP_INVENTORY_FULL)
			popup.SetAcceptEvent(self.__OnClosePopupDialog)
			popup.Open()
			self.popup = popup
			return

		questionDialog = uiCommon.QuestionDialog()
		questionDialog.SetText(localeInfo.OFFLINE_SHOP_CLOSE_QUESTION)
		questionDialog.SetAcceptEvent(ui.__mem_func__(self.OnCloseShop))
		questionDialog.SetCancelEvent(ui.__mem_func__(self.OnCloseQuestionDialog))
		questionDialog.Open()
		self.questionDialog = questionDialog

		return True

	def AskRenewShop(self):
		cost = 2500000 # 2.500.000

		questionDialog = uiCommon.QuestionDialog()
		questionDialog.SetText(localeInfo.OFFLINE_SHOP_RENEW_QUESTION % localeInfo.NumberToMoneyString(cost))
		questionDialog.SetAcceptEvent(ui.__mem_func__(self.OnRenewShop))
		questionDialog.SetCancelEvent(ui.__mem_func__(self.OnCloseQuestionDialog))
		questionDialog.Open()
		self.questionDialog = questionDialog

		return True

	def AskTakeOfflineShopMoney(self):
		self.offlineTakeMoneyDialog.Open()

	def OnCloseShop(self):
		self.OnCloseQuestionDialog()

#		if auction.GetItemMaxCount(auction.CONTAINER_OWNED_SHOP) != 0:
#			popup = uiCommon.PopupDialog()
#			popup.SetText(localeInfo.OFFLINE_SHOP_CANNOT_CLOSE_TAKE_ITEMS)
#			popup.SetAcceptEvent(self.__OnClosePopupDialog)
#			popup.Open()
#			self.popup = popup
#			return

#		if auction.GetMyShopGold() > 0:
#			popup = uiCommon.PopupDialog()
#			popup.SetText(localeInfo.OFFLINE_SHOP_CANNOT_CLOSE_TAKE_MONEY)
#			popup.SetAcceptEvent(self.__OnClosePopupDialog)
#			popup.Open()
#			self.popup = popup
#			return

		auction.SendShopClosePacket()

	def OnRenewShop(self):
		self.OnCloseQuestionDialog()
		auction.SendShopRenewPacket()

	def OnPressEscapeKey(self):
		self.Close()
		return True

	def OnPressExitKey(self):
		self.Close()
		return True

	def TakeOfflineShopMoney(self):
		if auction.GetMyShopGold() == 0:
			popup = uiCommon.PopupDialog()
			popup.SetText(localeInfo.SHOP_CANNOT_TAKE_OFFLINE_SHOP_MONEY_NO_MONEY)
			popup.SetAcceptEvent(self.__OnClosePopupDialog)
			popup.Open()
			self.popup = popup
			return

		self.AskTakeOfflineShopMoney()

	def OnTakeOfflineShopMoney(self, money):
		auction.SendTakeShopGoldPacket(money)
		self.OnCloseQuestionDialog()
		return True

	def __OnClosePopupDialog(self):
		self.popup = None

	def OnCloseQuestionDialog(self):
		if self.questionDialog:
			self.questionDialog.Close()

		self.questionDialog = None

	def SelectEmptySlot(self, selectedSlotPos):
		if not mouseModule.mouseController.isAttached():
			return

		attachedSlotType = mouseModule.mouseController.GetAttachedType()
		attachedSlotPos = mouseModule.mouseController.GetAttachedSlotNumber()
		attachedItemCount = mouseModule.mouseController.GetAttachedItemCount()
		attachedItemIndex = mouseModule.mouseController.GetAttachedItemIndex()

		if attachedItemIndex == 50255 and attachedItemCount < 25:
			chat.AppendChat(chat.CHAT_TYPE_INFO, localeInfo.SELL_AT_LEAST % (25))
			return mouseModule.mouseController.DeattachObject()

		# gemstone
		if attachedItemIndex == 50926 and attachedItemCount < 10:
			chat.AppendChat(chat.CHAT_TYPE_INFO, localeInfo.SELL_AT_LEAST % (10))
			return mouseModule.mouseController.DeattachObject()

		if attachedItemIndex == 71084 and attachedItemCount < 50:
			chat.AppendChat(chat.CHAT_TYPE_INFO, localeInfo.SELL_AT_LEAST % (50))
			return mouseModule.mouseController.DeattachObject()

		invenType = -1

		if player.SLOT_TYPE_INVENTORY == attachedSlotType:
			invenType = player.INVENTORY
		elif player.SLOT_TYPE_SKILLBOOK_INVENTORY == attachedSlotType:
			invenType = player.SKILLBOOK_INVENTORY
		elif player.SLOT_TYPE_UPPITEM_INVENTORY == attachedSlotType:
			invenType = player.UPPITEM_INVENTORY
		elif player.SLOT_TYPE_STONE_INVENTORY == attachedSlotType:
			invenType = player.STONE_INVENTORY
		elif player.SLOT_TYPE_ENCHANT_INVENTORY == attachedSlotType:
			invenType = player.ENCHANT_INVENTORY
		elif player.SLOT_TYPE_COSTUME_INVENTORY == attachedSlotType:
			invenType = player.COSTUME_INVENTORY

		if invenType != -1:
			if constInfo.OFFLINE_SHOP_ITEM_ENABLED == False:
				popup = uiCommon.PopupDialog()
				popup.SetText(localeInfo.OFFLINE_SHOP_ITEM_DISABLED)
				popup.SetAcceptEvent(self.__OnClosePopupDialog)
				popup.Open()
				self.popup = popup

				mouseModule.mouseController.DeattachObject()
				return

			if auction.GetMyShopTimeout() == 0:
				popup = uiCommon.PopupDialog()
				popup.SetWidth(300)
				popup.SetHeight(110)
				popup.SetText(localeInfo.SHOP_CANNOT_INSERT_ITEM_OFFLINE_SHOP_TIMEOUT)
				popup.SetAcceptEvent(self.__OnClosePopupDialog)
				popup.Open()
				self.popup = popup

				mouseModule.mouseController.DeattachObject()
				return

			item.SelectItem(1, 2, attachedItemIndex)
			for i in xrange(item.LIMIT_MAX_NUM):
				(limitType, limitValue) = item.GetLimit(i)
				if limitType == item.LIMIT_REAL_TIME or limitType == item.LIMIT_REAL_TIME_START_FIRST_USE:
					timeEnd = player.GetItemMetinSocket(invenType, attachedSlotPos, 0)
					if timeEnd != 0 and timeEnd != limitValue:
						if timeEnd - app.GetGlobalTimeStamp() < 2 * 24 * 60 * 60:
							popup = uiCommon.PopupDialog()
							popup.SetWidth(300)
							popup.SetHeight(110)
							popup.SetText(localeInfo.PRIVATE_SHOP_CANNOT_SELL_ITEM_TIME)
							popup.SetAcceptEvent(self.__OnClosePopupDialog)
							popup.Open()
							self.popup = popup

							mouseModule.mouseController.DeattachObject()
							return

			if constInfo.FAST_MOVE_ITEM_COOLDOWN:
				if app.GetGlobalTime() - self.fastMoveOfflineShopItem > 1000:
					self.fastMoveOfflineShopItem = app.GetGlobalTime()
				else:
					return

			if not self.inputMoneyDlg:
				self.inputMoneyDlg = uiCommon.SellItemDialog()

			self.inputMoneyDlg.invenType = invenType
			self.inputMoneyDlg.itemVNum = attachedItemIndex
			self.inputMoneyDlg.sourceSlotPos = attachedSlotPos
			self.inputMoneyDlg.targetSlotPos = selectedSlotPos

			self.inputMoneyDlg.SetAcceptEvent(ui.__mem_func__(self.OnAcceptInputMoneyDialog))
			self.inputMoneyDlg.SetCancelEvent(ui.__mem_func__(self.OnCloseInputMoneyDialog))

			if self.itemPriceList.has_key(attachedItemIndex):
				self.inputMoneyDlg.setPrice = self.itemPriceList[attachedItemIndex]

			auction.SendRequestAveragePricePacket(1, attachedItemIndex, attachedItemCount)
		else:
			tchat("attached slot type %d is not allowed" % attachedSlotType)

		mouseModule.mouseController.DeattachObject()

	def OpenSellWindow(self, price):
		if not self.inputMoneyDlg:
			return

		self.inputMoneyDlg.average = price
		self.inputMoneyDlg.Open(auction.TAX_SHOP_OWNER)
		if self.inputMoneyDlg.setPrice:
			self.inputMoneyDlg.SetValue(self.inputMoneyDlg.setPrice)

	def UnselectItemSlot(self, selectedSlotPos):
		self.AskTakeItem(selectedSlotPos)

	def SelectItemSlot(self, selectedSlotPos):
		auction.SetContainerType(auction.CONTAINER_OWNED_SHOP)
		itemIndex = auction.GetItemIndexByCell(selectedSlotPos)
		itemVnum = auction.GetItemVnum(itemIndex)
		itemCount = auction.GetItemCount(itemIndex)

		if not mouseModule.mouseController.isAttached() and app.IsPressed(app.DIK_LALT):
			if 0 == itemVnum:
				return
				
			metinSlot = ()
			for i in xrange(player.METIN_SOCKET_MAX_NUM):
				metinSlot += (auction.GetItemSocket(itemIndex, i),)

			attrSlot = ()
			for i in xrange(player.ATTRIBUTE_SLOT_MAX_NUM):
				attrType, attrVal = auction.GetItemAttribute(itemIndex, i)
				attrSlot += (attrType, attrVal)

			link = player.GetItemLinkFromData(itemVnum, metinSlot, attrSlot)
			ime.PasteString(link)
			return

		mouseModule.mouseController.AttachObject(self, player.SLOT_TYPE_AUCTION_SHOP, selectedSlotPos, itemVnum, itemCount)
		mouseModule.mouseController.SetCallBack("INVENTORY", ui.__mem_func__(self.DropToInventory))
		snd.PlaySound("sound/ui/pick.wav")

	def DropToInventory(self, dstSlotPos):
		attachedSlotPos = mouseModule.mouseController.GetAttachedSlotNumber()
		self.AskTakeItem(attachedSlotPos, dstSlotPos)

	def AskTakeItem(self, slotPos, dstSlotPos = -1):
		if constInfo.OFFLINE_SHOP_ITEM_ENABLED == False:
			popup = uiCommon.PopupDialog()
			popup.SetText(localeInfo.OFFLINE_SHOP_ITEM_DISABLED)
			popup.SetAcceptEvent(self.__OnClosePopupDialog)
			popup.Open()
			self.popup = popup
			return

		auction.SetContainerType(auction.CONTAINER_OWNED_SHOP)
		itemIndex = auction.GetItemIndexByCell(slotPos)
		itemID = auction.GetItemID(itemIndex)
		itemVnum = auction.GetItemVnum(itemIndex)
		itemCount = auction.GetItemCount(itemIndex)

		item.SelectItem(1, 2, itemVnum)
		itemName = item.GetItemName()
		w, h = item.GetItemSize()

		if player.FindEmptyInventory(h) == -1:
			popup = uiCommon.PopupDialog()
			popup.SetText(localeInfo.SHOP_INVENTORY_FULL)
			popup.SetAcceptEvent(self.__OnClosePopupDialog)
			popup.Open()
			self.popup = popup
			return

		questionDialog = uiCommon.QuestionDialog()
		questionDialog.SetText(localeInfo.DO_YOU_TAKE_OUT_ITEM(itemName, itemCount))
		questionDialog.SetAcceptEvent(self.TakeOutItem)
		questionDialog.SetCancelEvent(self.OnCloseQuestionDialog)
		questionDialog.Open()
		questionDialog.pos = slotPos
		questionDialog.id = itemID
		questionDialog.dstPos = dstSlotPos
		self.questionDialog = questionDialog

	def TakeOutItem(self):
		pos = self.questionDialog.pos
		id = self.questionDialog.id
		if self.questionDialog.dstPos >= 0:
			auction.SendTakeItemPacket(id, self.questionDialog.dstPos)
		else:
			auction.SendTakeItemPacket(id)

		self.OnCloseQuestionDialog()

	def SetItemToolTip(self, tooltipItem):
		self.tooltipItem = tooltipItem

	def OverInItem(self, slotIndex):
		if mouseModule.mouseController.isAttached():
			return

		if 0 != self.tooltipItem:
			self.tooltipItem.SetAuctionItem(auction.CONTAINER_OWNED_SHOP, auction.GetItemIndexByCell(auction.CONTAINER_OWNED_SHOP, slotIndex))

	def OverOutItem(self):
		if 0 != self.tooltipItem:
			self.tooltipItem.HideToolTip()

	def OnIMEReturn(self):
		if self.questionDialog:
			self.questionDialog.Accept()
			return True

	def OnAcceptInputMoneyDialog(self):
		if not self.inputMoneyDlg:
			return

		text = self.inputMoneyDlg.GetText()

		if not text:
			return True

		invenType = self.inputMoneyDlg.invenType
		sourceSlotPos = self.inputMoneyDlg.sourceSlotPos
		targetSlotPos = self.inputMoneyDlg.targetSlotPos

		price = self.inputMoneyDlg.GetMoney()

		# if self.inputMoneyDlg.average and self.inputMoneyDlg.checkAverage:
		# 	(percentage, percentagePositive) = shop.GetSellMarginPercent()
		# 	min = float(self.inputMoneyDlg.average * (1.0 - percentage / 100.0))
		# 	max = float(self.inputMoneyDlg.average * (1.0 + percentagePositive / 100.0))

		# 	if price < min or price > max:
		# 		chat.AppendChat(chat.CHAT_TYPE_INFO, localeInfo.SHOP_PRICE_OVER_MARGIN)
		# 		return

		auction.SendInsertItemPacket(invenType, sourceSlotPos, targetSlotPos, price)
		snd.PlaySound("sound/ui/drop.wav")

		self.OnCloseInputMoneyDialog()

		return True

	def OnCloseInputMoneyDialog(self):
		if self.inputMoneyDlg:
			self.inputMoneyDlg.Close()

		self.inputMoneyDlg = None
		return True

	def OnUpdate(self):
		if not self.isTimeout:
			self.RefreshTimeout()

	def OnMouseWheel(self, scrollLen):
		if self.IsInPosition() and self.scrollBar.IsShow():
			basePos = self.historyList.GetBasePos() + constInfo.WHEEL_TO_SCROLL(scrollLen)

			if basePos < 0:
				basePos = 0

			maxBasePos = self.historyList.GetScrollLen()

			if basePos > maxBasePos:
				basePos = maxBasePos

			newPos = float(basePos) / float(max(1, maxBasePos))
			self.scrollBar.SetPos(newPos)
			return True

		return False

	def __OnBtnHistory(self):
		self.ClearHistory()

		if not self.historyOpened:
			if self.timeHistory + 3 > app.GetTime():
				chat.AppendChat(chat.CHAT_TYPE_INFO, "You need to wait 3 seconds to view the history again.")
				return

			self.timeHistory = app.GetTime()

			self.bottomBar.Hide()
			self.itemSlotWindow.Hide()
			self.ChangeBackgroundImage(False)
			self.historyTab.Show()

			auction.SendShopRequestHistoryPacket()
		else:
			self.bottomBar.Show()
			self.itemSlotWindow.Show()
			self.ChangeBackgroundImage(True)
			self.historyTab.Hide()

		self.historyOpened = not self.historyOpened

	def RefreshHistory(self):
		self.ClearHistory()

		for i in xrange(auction.GetShopHistoryCount()):
			vnum, price, buyer, date = auction.GetShopHistory(i)
			self.AddHistory(vnum, price, buyer, date)

	def AddHistory(self, vnum, price, buyer, date):
		item.SelectItem(1, 2, vnum)
		timestamp = datetime.datetime.fromtimestamp(date)
		historyEntry = self.HistoryEntry(item.GetItemName(), localeInfo.NumberToMoneyString(price), buyer, timestamp.strftime('%d-%m-%Y'), self.isEven, self.whisperFn)
		self.historyList.AppendItem(historyEntry)
		self.isEven = not self.isEven

		self.RefreshScrollbar()

	def RefreshScrollbar(self):
		scrollbarVisible = (self.historyList.GetItemCount() > 7)

		if scrollbarVisible and self.historyTab.IsShow():
			itemCount 	= float(self.historyList.GetItemCount())
			viewCount 	= float(7.0)
			newSize 	= float(viewCount / itemCount)

			self.scrollBar.SetMiddleBarSize(newSize)
			self.scrollBar.Show()
		else:
			self.scrollBar.Hide()

	def ClearHistory(self):
		for i in range(0, self.historyList.GetItemCount()):
			element = self.historyList.GetItemAtIndex(i)

			if not element:
				continue

			element.Hide()

		self.historyList.RemoveAllItems()

	def ChangeBackgroundImage(self, isMainTab):
		self.board.LoadImage("d:/ymir work/ui/game/offlineshop/tab_main/bg{}.tga".format("_2" if isMainTab else ""))

class AuctionGuestShopWindow(ui.BaseScriptWindow):

	#################################################
	## MAIN FUNCTIONS
	#################################################

	def __init__(self):
		ui.BaseScriptWindow.__init__(self, "AuctionGuestShopWindow", self.__BindObject)

		self.tooltipItem = None
		self.questionDialog = None
		self.popup = None
		self.itemBuyQuestionDialog = None

		self.xShopStart = 0
		self.yShopStart = 0

		self.__LoadWindow()

	def __BindObject(self):
		self._AddLoadObject("board", "board")
		self._AddLoadObject("slot", "ItemSlot")
		self._AddLoadObject("buy", "BuyButton")
		self._AddLoadObject("sell", "SellButton")

	def __LoadWindow(self):
		self.main["slot"].SetSelectEmptySlotEvent(ui.__mem_func__(self.SelectEmptySlot))
		self.main["slot"].SetSelectItemSlotEvent(ui.__mem_func__(self.SelectItemSlot))
		self.main["slot"].SetUnselectItemSlotEvent(ui.__mem_func__(self.UnselectItemSlot))
		self.main["slot"].SetOverInItemEvent(ui.__mem_func__(self.OverInItem))
		self.main["slot"].SetOverOutItemEvent(ui.__mem_func__(self.OverOutItem))

		self.main["buy"].SetToggleUpEvent(ui.__mem_func__(self.CancelShopping))
		self.main["buy"].SetToggleDownEvent(ui.__mem_func__(self.OnBuy))

		self.main["sell"].SetToggleUpEvent(ui.__mem_func__(self.CancelShopping))
		self.main["sell"].SetToggleDownEvent(ui.__mem_func__(self.OnSell))

	def Open(self):
		ui.BaseScriptWindow.Open(self)
		(self.xShopStart, self.yShopStart, z) = player.GetMainCharacterPosition()
		self.Refresh()

	def Destroy(self):
		self.tooltipItem = None
		self.questionDialog = None
		self.popup = None
		self.itemBuyQuestionDialog = None

		self.OnClose()

		ui.BaseScriptWindow.Destroy(self)

	def Close(self):
		auction.SendShopGuestCancelPacket()
		self.OnCloseQuestionDialog()

	def OnClose(self):
		ui.BaseScriptWindow.Close(self)

	def Refresh(self):
		self.main["board"].SetTitleName(auction.GetGuestShopName())

		for i in xrange(auction.SHOP_SLOT_COUNT):
			self.main["slot"].ClearSlot(i)

		auction.SetContainerType(auction.CONTAINER_SHOP)
		for i in xrange(auction.GetItemMaxCount()):
			slot = auction.GetItemCell(i)
			vnum = auction.GetItemVnum(i)
			count = auction.GetItemCount(i)

			if count <= 1:
				count = 0

			self.main["slot"].SetItemSlot(slot, vnum, count)

		self.main["slot"].RefreshSlot()

	def SelectEmptySlot(self, selectedSlotPos):
		if mouseModule.mouseController.isAttached():
			self.SellAttachedItem()

	def UnselectItemSlot(self, selectedSlotPos):
		self.AskBuyItem(selectedSlotPos)

	def SelectItemSlot(self, selectedSlotPos):
		if mouseModule.mouseController.isAttached():
			self.SellAttachedItem()

		else:
			curCursorNum = app.GetCursor()
			if app.BUY == curCursorNum:
				self.AskBuyItem(selectedSlotPos)

			elif app.SELL == curCursorNum:
				chat.AppendChat(chat.CHAT_TYPE_INFO, localeInfo.SHOP_SELL_INFO)

			else:
				auction.SetContainerType(auction.CONTAINER_SHOP)

				itemIndex = auction.GetItemIndexByCell(selectedSlotPos)

				itemVnum = auction.GetItemVnum(itemIndex)
				itemCount = auction.GetItemCount(itemIndex)

				mouseModule.mouseController.AttachObject(self, player.SLOT_TYPE_AUCTION_SHOP, selectedSlotPos, itemVnum, itemCount)
				mouseModule.mouseController.SetCallBack("INVENTORY", ui.__mem_func__(self.DropToInventory))
				snd.PlaySound("sound/ui/pick.wav")

	def OverInItem(self, slotIndex):
		if mouseModule.mouseController.isAttached():
			return

		if self.tooltipItem is not None:
			self.tooltipItem.SetAuctionItem(auction.CONTAINER_SHOP, auction.GetItemIndexByCell(auction.CONTAINER_SHOP, slotIndex))

	def OverOutItem(self):
		if self.tooltipItem is not None:
			self.tooltipItem.HideToolTip()

	def ShowPopup(self, text):
		popup = uiCommon.PopupDialog()
		popup.SetText(text)
		popup.SetAcceptEvent(self.__OnClosePopupDialog)
		popup.Open()
		self.popup = popup

	def SellAttachedItem(self):
		attachedSlotType = mouseModule.mouseController.GetAttachedType()
		attachedSlotPos = mouseModule.mouseController.GetAttachedSlotNumber()
		attachedCount = mouseModule.mouseController.GetAttachedItemCount()
		if player.SLOT_TYPE_INVENTORY == attachedSlotType:

			itemIndex = player.GetItemIndex(attachedSlotPos)
			item.SelectItem(1, 2, itemIndex)

			if item.IsAntiFlag(item.ITEM_ANTIFLAG_SELL):
				self.ShowPopup(localeInfo.SHOP_CANNOT_SELL_ITEM)

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
		tchat("sell %s %s" % (str(slotPos), str(count)))
		net.SendShopSellPacketNew(slotPos, count)
		snd.PlaySound("sound/ui/money.wav")
		self.OnCloseQuestionDialog()

	def OnCloseQuestionDialog(self):
		if self.questionDialog:
			self.questionDialog.Close()

		self.questionDialog = None

	def DropToInventory(self):
		attachedSlotPos = mouseModule.mouseController.GetAttachedSlotNumber()
		self.AskBuyItem(attachedSlotPos)

	def AskBuyItem(self, slotPos):
		auction.SetContainerType(auction.CONTAINER_SHOP)

		itemIndex = auction.GetItemIndexByCell(slotPos)
		itemVnum = auction.GetItemVnum(itemIndex)
		itemPrice = auction.GetItemPrice(itemIndex)
		itemCount = auction.GetItemCount(itemIndex)

		item.SelectItem(1, 2, itemVnum)
		itemName = item.GetItemName()
		w, h = item.GetItemSize()

		if player.FindEmptyInventory(h) == -1:
			self.ShowPopup(localeInfo.SHOP_INVENTORY_FULL)
			return

		itemBuyQuestionDialog = uiCommon.QuestionDialog()
		itemBuyQuestionDialog.SetText(localeInfo.DO_YOU_BUY_ITEM(itemName, itemCount, localeInfo.NumberToMoneyString(itemPrice)))
		itemBuyQuestionDialog.SetAcceptEvent(lambda arg=True: self.AnswerBuyItem(arg))
		itemBuyQuestionDialog.SetCancelEvent(lambda arg=False: self.AnswerBuyItem(arg))
		itemBuyQuestionDialog.Open()
		itemBuyQuestionDialog.id = auction.GetItemID(itemIndex)
		itemBuyQuestionDialog.price = auction.GetItemPrice(itemIndex)
		self.itemBuyQuestionDialog = itemBuyQuestionDialog

	def AnswerBuyItem(self, flag):
		if flag:
			if player.GetElk() < self.itemBuyQuestionDialog.price:
				self.ShowPopup(localeInfo.SHOP_NOT_ENOUGH_MONEY_EX)
			else:
				auction.SendBuyItemPacket(self.itemBuyQuestionDialog.id, self.itemBuyQuestionDialog.price)

		self.itemBuyQuestionDialog.Close()
		self.itemBuyQuestionDialog = None

	def SetItemToolTip(self, tooltipItem):
		self.tooltipItem = tooltipItem

	def OnUpdate(self):

		USE_SHOP_LIMIT_RANGE = 1000

		(x, y, z) = player.GetMainCharacterPosition()
		if abs(x - self.xShopStart) > USE_SHOP_LIMIT_RANGE or abs(y - self.yShopStart) > USE_SHOP_LIMIT_RANGE:
			self.Close()

	def OnBuy(self):
		chat.AppendChat(chat.CHAT_TYPE_INFO, localeInfo.SHOP_BUY_INFO)
		app.SetCursor(app.BUY)
		self.main["sell"].SetUp()

	def OnSell(self):
		chat.AppendChat(chat.CHAT_TYPE_INFO, localeInfo.SHOP_SELL_INFO)
		app.SetCursor(app.SELL)
		self.main["buy"].SetUp()

	def CancelShopping(self):
		self.main["buy"].SetUp()
		self.main["sell"].SetUp()
		app.SetCursor(app.NORMAL)

	def OnPressEscapeKey(self):
		self.Close()
		return True

	def OnPressExitKey(self):
		self.Close()
		return True

	def __OnClosePopupDialog(self):
		self.popup = None
