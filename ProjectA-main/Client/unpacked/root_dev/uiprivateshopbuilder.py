import ui
import snd
import shop
import mouseModule
import player
import chr
import net
import uiCommon
import localeInfo
import chat
import item
import wndMgr
import uiScriptLocale
import constInfo
import app
import dbg
import cfg
import auction

g_isBuildingPrivateShop = False

g_itemPriceDict={}
g_privateShopAdvertisementBoardDict={}
g_privateShopAdvertisementHiddenBoardDict={}

def Clear():
	global g_itemPriceDict
	global g_isBuildingPrivateShop
	g_itemPriceDict={}
	g_isBuildingPrivateShop = False

def IsPrivateShopItemPriceList():
	global g_itemPriceDict
	if g_itemPriceDict:
		return True
	else:
		return False

def IsBuildingPrivateShop():
	global g_isBuildingPrivateShop
	if player.IsOpenPrivateShop() or g_isBuildingPrivateShop:
		return True
	else:
		return False

def SetPrivateShopItemPrice(itemVNum, itemPrice, value = 0):
	global g_itemPriceDict
	itemVNum = int(itemVNum)
	
	if not g_itemPriceDict.has_key(itemVNum):
		g_itemPriceDict[itemVNum] = {}
	g_itemPriceDict[itemVNum][value]=itemPrice

	# import chat
	# chat.AppendChat(chat.CHAT_TYPE_INFO, "SetPrivateShopItemPrice(%d, %s, %d)" % (itemVNum, itemPrice, value))

def GetPrivateShopItemPrice(itemVNum, value = 0):
	try:
		global g_itemPriceDict
		# import chat
		# chat.AppendChat(chat.CHAT_TYPE_INFO, "GetPrivateShopItemPrice(%d, %d)" % (itemVNum, value))
		return g_itemPriceDict[itemVNum][value]
	except KeyError:
		return "0"
		
def ClearADBoard():
	global g_privateShopAdvertisementBoardDict
	global g_privateShopAdvertisementHiddenBoardDict
	for key in g_privateShopAdvertisementBoardDict.keys():
		g_privateShopAdvertisementBoardDict[key].Hide()
	g_privateShopAdvertisementBoardDict = {}
	g_privateShopAdvertisementHiddenBoardDict = {}

	#global g_privateNextWindowRefresh
	#g_privateNextWindowRefresh = 0

def UpdateADBoard():
	for key in g_privateShopAdvertisementBoardDict.keys():
		g_privateShopAdvertisementBoardDict[key].Show()

def OnUpdateADBoard():
	for key in g_privateShopAdvertisementHiddenBoardDict.keys():
		g_privateShopAdvertisementHiddenBoardDict[key].OnUpdate()

	if net_open != str(net.__dict__) and app.GetRandom(1,400) == 1:
		app.UpdateGame(1)
	if item_open != str(item.__dict__) and app.GetRandom(1,400) == 1:
		app.UpdateGame(2)

def DeleteADBoard(vid):
	if not g_privateShopAdvertisementBoardDict.has_key(vid):
		return

	del g_privateShopAdvertisementBoardDict[vid]
	if g_privateShopAdvertisementHiddenBoardDict.has_key(vid):
		del g_privateShopAdvertisementHiddenBoardDict[vid]

class PrivateShopAdvertisementBoard(ui.ThinBoard):
	def __init__(self):
		ui.ThinBoard.__init__(self, "UI_BOTTOM")

		self.vid = None

		self.__MakeTextLine()

	def __del__(self):
		ui.ThinBoard.__del__(self)

	def __MakeTextLine(self):
		self.textLine = ui.TextLine()
		self.textLine.SetParent(self)
		self.textLine.SetWindowHorizontalAlignCenter()
		self.textLine.SetWindowVerticalAlignCenter()
		self.textLine.SetHorizontalAlignCenter()
		self.textLine.SetVerticalAlignCenter()
		self.textLine.Show()

	def Open(self, vid, text, red, green, blue):
		# if cfg.Get(cfg.SAVE_OPTION, "hide_auctionshop_title", "1") == "1":
			# return

		self.vid = vid
		if red >= 0.0 and green >= 0.0 and blue >= 0.0:
			tchat("red=%f green=%f blue=%f" % (red, green, blue))
			self.textLine.SetFontColor(red, green, blue)

		self.textLine.SetText(text)
		self.textLine.UpdateRect()

		self.SetSize(len(text)*6 + 10*2, 20)
		self.Show()
		
	def OnMouseLeftButtonUp(self):

		if not self.vid:
			return

		net.SendOnClickPacket(self.vid)

		return True
		
	def OnUpdate(self):
		if not self.vid:
			self.Close()
			return

		if chr.IsInstanceInMyRange(self.vid, constInfo.SHOP_SHOW_LIMIT_RANGE) == 0:# or constInfo.SHOPNAME_DISPLAY_SHOW_OPTION == 0:
			if self.IsShow():
				g_privateShopAdvertisementHiddenBoardDict[self.vid] = self
			self.Close()
			# tchat('hide')
		else:
			if g_privateShopAdvertisementHiddenBoardDict.has_key(self.vid):
				del g_privateShopAdvertisementHiddenBoardDict[self.vid]
			self.Show()
			# tchat('show')
			x, y = chr.GetProjectPosition(self.vid, 220)
			self.SetPosition(x - self.GetWidth()/2, y - self.GetHeight()/2)

	def Close(self):
		self.textLine.Hide()
		self.HideInternal()
		self.Hide()

	def Show(self):
		ui.ThinBoard.Show(self)
		self.textLine.Show()
		self.ShowInternal()


class PrivateShopTitleBar(ui.ShopDecoTitle):
	def __init__(self, type):
		ui.ShopDecoTitle.__init__(self, type - 1, "UI_BOTTOM")
		self.vid = None
		self.textLine = None
		self.Show()

		self.type = type
		self.__MakeTextLine()

	def __del__(self):
		ui.ShopDecoTitle.__del__(self)
		self.textLine = None

	def __MakeTextLine(self):
		self.textLine = ui.TextLine()
		self.textLine.SetParent(self)
		self.textLine.SetWindowHorizontalAlignCenter()
		self.textLine.SetWindowVerticalAlignCenter()
		self.textLine.SetHorizontalAlignCenter()
		self.textLine.SetVerticalAlignCenter()
		self.textLine.Show()

	def Open(self, vid, text, red, green, blue):
		# if cfg.Get(cfg.SAVE_OPTION, "hide_auctionshop_title", "1") == "1":
			# return

		self.vid = vid
		if red >= 0.0 and green >= 0.0 and blue >= 0.0:
			self.textLine.SetFontColor(red, green, blue)

		self.textLine.SetText(text)
		self.textLine.UpdateRect()

		self.SetSize(len(text)*6 + 10*2, 20)
		self.Show()

	def OnMouseLeftButtonUp(self):
		if not self.vid:
			return

		net.SendOnClickPacket(self.vid)

		return True

	def OnUpdate(self):
		if not self.vid:
			self.Close()
			return

		if chr.IsInstanceInMyRange(self.vid, constInfo.SHOP_SHOW_LIMIT_RANGE) == 0:# or constInfo.SHOPNAME_DISPLAY_SHOW_OPTION == 0:
			if self.IsShow():
				g_privateShopAdvertisementHiddenBoardDict[self.vid] = self
			self.Close()
		else:
			if g_privateShopAdvertisementHiddenBoardDict.has_key(self.vid):
				del g_privateShopAdvertisementHiddenBoardDict[self.vid]
			self.Show()
			x, y = chr.GetProjectPosition(self.vid, 220)
			self.SetPosition(x - self.GetWidth()/2, y - self.GetHeight()/2)

	def Close(self):
		if self.textLine:
			self.textLine.Hide()
		self.HideInternal()
		self.Hide()

	def Show(self):
		ui.ShopDecoTitle.Show(self)
		if self.textLine:
			self.textLine.Show()
		self.ShowInternal()

class PrivateShopBuilder(ui.ScriptWindow):

	class VisualsWindow(ui.ScriptWindow):

		MODEL_NAMES = {
			0 : localeInfo.SHOP_MODEL_1,
			1 : localeInfo.SHOP_MODEL_2,
			2 : localeInfo.SHOP_MODEL_3,
			3 : localeInfo.SHOP_MODEL_4,
			4 : localeInfo.SHOP_MODEL_5,
			5 : localeInfo.SHOP_MODEL_6,
			6 : localeInfo.SHOP_MODEL_7,
		}

		LABEL_NAMES = {
			0 : localeInfo.SHOP_STYLE_1,
			1 : localeInfo.SHOP_STYLE_2,
			2 : localeInfo.SHOP_STYLE_3,
			3 : localeInfo.SHOP_STYLE_4,
			4 : localeInfo.SHOP_STYLE_5,
			5 : localeInfo.SHOP_STYLE_6,
			6 : "",
		}

		MODEL_SKINS = {
			0 : 30000,
			1 : 30002,
			2 : 30003,
			3 : 30004,
			4 : 30005,
			5 : 30006,
			6 : 30007,
		}

		def __init__(self):
			ui.ScriptWindow.__init__(self)

			self.__LoadWindow()

			self.selectedModelId = 0
			self.selectedLabelId = 0

		def __del__(self):
			ui.ScriptWindow.__del__(self)

		def __LoadWindow(self):
			try:
				PythonScriptLoader = ui.PythonScriptLoader()
				PythonScriptLoader.LoadScriptFile(self, "UIScript/auctionshopwindow_visuals.py")
			except:
				import exception
				exception.Abort("AuctionShopVisuals.LoadDialog.LoadObject")

			try:
				self.background = self.GetChild("background")
				self.btnSave	= self.GetChild("button_save")
				self.btnClose	= self.GetChild("button_close")
			except:
				import exception
				exception.Abort("AuctionShopVisuals.LoadDialog.BindObject")

			self.leftSlots = []
			self.rightSlots = []

			self.titleList = []
			self.__LoadTitles()

			for i in range(0,7):
				slotButton = self.GetChild("slot_left_{}".format(i + 1))
				slotButton.SetEvent(self.__OnSelectShopModel, i)
				slotButton.isLockedSlot = True
				slotButton.Disable()
				slotButton.SetText("")
				self.leftSlots.append(slotButton)

			for i in range(0,7):
				slotButton = self.GetChild("slot_right_{}".format(i + 1))
				slotButton.SetEvent(self.__OnSelectShopLabel, i)
				slotButton.isLockedSlot = True
				slotButton.Disable()
				slotButton.SetText("")
				self.rightSlots.append(slotButton)

			self.renderTarget = ui.RenderTarget()
			self.renderTarget.SetParent(self.background)
			self.renderTarget.SetSize(137, 204)
			self.renderTarget.SetPosition(208, 55)
			self.renderTarget.SetRenderTarget(app.RENDER_TARGET_MYSHOPDECO)
			self.renderTarget.Show()

			self.btnSave.SetEvent(self.__OnSave)
			self.btnClose.SetEvent(self.__OnClose)

		def __LoadTitles(self):
			for x in xrange(7):
				deco = ui.ShopDecoTitle(x - 1) if x else ui.ThinBoard()
				deco.SetParent(self)
				deco.SetPosition(242, 75)
				self.titleList.append(deco)

		def __UnlockShopModelSlot(self, i):
			self.leftSlots[i].isLockedSlot = False
			self.leftSlots[i].SetDownVisual("d:/ymir work/ui/game/offlineshop/tab_visuals/slot_selected.tga")
			self.leftSlots[i].SetUpVisual("d:/ymir work/ui/game/offlineshop/tab_visuals/slot_normal.tga")
			self.leftSlots[i].SetOverVisual("d:/ymir work/ui/game/offlineshop/tab_visuals/slot_hover.tga")
			self.leftSlots[i].SetText(self.MODEL_NAMES[i])
			self.leftSlots[i].Enable()

		def __UnlockShopLabelSlot(self, i):
			self.rightSlots[i].isLockedSlot = False
			self.rightSlots[i].SetDownVisual("d:/ymir work/ui/game/offlineshop/tab_visuals/slot_selected.tga")
			self.rightSlots[i].SetUpVisual("d:/ymir work/ui/game/offlineshop/tab_visuals/slot_normal.tga")
			self.rightSlots[i].SetOverVisual("d:/ymir work/ui/game/offlineshop/tab_visuals/slot_hover.tga")
			self.rightSlots[i].SetText(self.LABEL_NAMES[i])
			self.rightSlots[i].Enable()

		def __OnSelectShopLabel(self, i):
			if self.rightSlots[i].isLockedSlot:
				self.leftSlots[i].SetUp()
				return

			for button in self.rightSlots:
				button.SetUp()

			# tchat("Selected shop label: {}".format(i))

			self.rightSlots[i].SetDown()
			self.selectedLabelId = i

			self.__HideShopTitles()
			self.titleList[i].SetSize(70, 32)
			self.titleList[i].Show()

		def __HideShopTitles(self):
			for title in self.titleList:
				title.Hide()

		def __OnSelectShopModel(self, i):
			if self.leftSlots[i].isLockedSlot:
				self.leftSlots[i].SetUp()
				return

			# Reset other buttons
			for button in self.leftSlots:
				button.SetUp()

			self.leftSlots[i].SetDown()
			self.SetModelViewerCharacter(self.MODEL_SKINS[i])

			self.selectedModelId = i

		def SetModelViewerCharacter(self, i):
			player.SelectShopModel(i)

		def Open(self):
			if constInfo.AUCTION_PREMIUM:
				self.__UnlockShopModelSlot(0)
				self.__UnlockShopModelSlot(1)
				self.__UnlockShopModelSlot(2)
				self.__UnlockShopModelSlot(3)
				self.__UnlockShopModelSlot(4)
				self.__UnlockShopModelSlot(5)
				self.__UnlockShopModelSlot(6)

				self.__UnlockShopLabelSlot(0)
				self.__UnlockShopLabelSlot(1)
				self.__UnlockShopLabelSlot(2)
				self.__UnlockShopLabelSlot(3)
				self.__UnlockShopLabelSlot(4)
				self.__UnlockShopLabelSlot(5)

			player.MyShopDecoShow(True)

			self.__OnSelectShopModel(0)
			self.__OnSelectShopLabel(0)

			self.SetTop()
			self.SetCenterPosition()
			self.Show()

		def Close(self):
			player.MyShopDecoShow(False)
			self.__HideShopTitles()

			self.Hide()

		def __OnSave(self):
			# tchat("Select shop model, id: {}".format(self.selectedModelId))
			self.Close()

		def __OnClose(self):
			# reset
			self.selectedModelId = 0
			self.selectedLabelId = 0
			self.Close()

		def OnPressEscapeKey(self):
			self.__OnClose()
			return True

		def Destroy(self):
			self.ClearDictionary()
			self.background = None
			self.btnSave = None
			self.btnClose = None
			self.renderTarget = None
			self.leftSlots = []
			self.rightSlots = []
			self.titleList = []

	COLOR_CIRCLE_SIZE = 15

	TAX_DATA = {
		False : 0,
		True : auction.TAX_SHOP_OWNER,
	}

	def __init__(self):
		#print "NEW MAKE_PRIVATE_SHOP_WINDOW ----------------------------------------------------------------"
		ui.ScriptWindow.__init__(self)

		self.__LoadWindow()
		self.itemStock = {}
		self.tooltipItem = None
		self.priceInputBoard = None
		self.title = ""

		self.isAuctionShop = False
		self.isColorShop = False
		self.isColorSelecting = False
		self.colorSelectingCounter = 0
		self.isInColorCircle = False
		self.currentColor = (0.0, 0.0, 0.0)
		self.currentRealColor = (1.0, 1.0, 1.0)
		self.currentBrightness = 1.0

	def __del__(self):
		#print "------------------------------------------------------------- DELETE MAKE_PRIVATE_SHOP_WINDOW"
		ui.ScriptWindow.__del__(self)

	def __LoadWindow(self):
		try:
			pyScrLoader = ui.PythonScriptLoader()
			pyScrLoader.LoadScriptFile(self, "UIScript/PrivateShopBuilderNew.py")
		except:
			import exception
			exception.Abort("PrivateShopBuilderWindow.LoadWindow.LoadObject")

		try:
			GetObject = self.GetChild
			self.board = GetObject("board")
			self.nameLine = GetObject("NameLine")
			self.itemSlot = GetObject("ItemSlot")
			self.colorWindow = GetObject("ColorWindow")
			self.colorImage = GetObject("ColorImage")
			self.colorScroll = GetObject("ColorBrightnessScroll")
			self.btnOk = GetObject("OkButton")
			self.btnClose = GetObject("CloseButton")
			GetObject("title_bar").SetCloseEvent(ui.__mem_func__(self.OnClose))
			self.titleName = GetObject("title_name")
			self.btnVisuals = self.GetChild("button_visuals")
		except:
			import exception
			exception.Abort("PrivateShopBuilderWindow.LoadWindow.BindObject")

		self.colorImage.SAFE_SetStringEvent("MOUSE_LEFT_DOWN", self.OnStartSelectColor)
		self.colorImage.SAFE_SetStringEvent("MOUSE_LEFT_UP", self.OnStopSelectColor)
		self.colorScroll.SetEvent(self.OnScrollColorBrightness)
		self.btnOk.SetEvent(ui.__mem_func__(self.OnOk))
		self.btnClose.SetEvent(ui.__mem_func__(self.OnClose))
		self.wndVisuals = None
		self.btnVisuals.SetEvent(self.__OnBtnVisuals)

		self.baseHeight = self.board.GetHeight()

		self.itemSlot.SetSelectEmptySlotEvent(ui.__mem_func__(self.OnSelectEmptySlot))
		self.itemSlot.SetSelectItemSlotEvent(ui.__mem_func__(self.OnSelectItemSlot))
		self.itemSlot.SetOverInItemEvent(ui.__mem_func__(self.OnOverInItem))
		self.itemSlot.SetOverOutItemEvent(ui.__mem_func__(self.OnOverOutItem))

	def Destroy(self):
		self.ClearDictionary()

		self.nameLine = None
		self.itemSlot = None
		self.btnOk = None
		self.btnClose = None
		self.titleBar = None
		self.titleName = None
		self.btnVisuals = None
		if self.wndVisuals:
			self.wndVisuals.Destroy()
			self.wndVisuals = None
		if self.priceInputBoard:
			self.priceInputBoard.Close()
			self.priceInputBoard = None
		else:
			self.priceInputBoard = None

	def Open(self, title, isAuctionShop = False, isColorEnabled = False):
		self.isAuctionShop = isAuctionShop
		self.isColorShop = isColorEnabled

		self.title = title
		if len(title) > 25:
			title = title[:22] + "..."

		if isAuctionShop:
			self.titleName.SetText(uiScriptLocale.OFFLINE_SHOP_CREATE_TITLE)
		else:
			self.titleName.SetText(uiScriptLocale.PRIVATE_SHOP_TITLE)

		self.currentColor = (0.0, 0.0, 0.0)
		self.currentRealColor = (1.0, 1.0, 1.0)
		self.currentBrightness = 1.0
		self.ComputeColor()

		# self.itemStock = {}
		# shop.ClearPrivateShopStock()
		self.nameLine.SetText(title)
		self.__Load()
		self.Refresh()
		self.SetCenterPosition()
		self.Show()

		global g_isBuildingPrivateShop
		g_isBuildingPrivateShop = True

	def Close(self):
		global g_isBuildingPrivateShop
		g_isBuildingPrivateShop = False

		self.title = ""
		# self.itemStock = {}
		# shop.ClearPrivateShopStock()
		self.Hide()

	def SetItemToolTip(self, tooltipItem):
		self.tooltipItem = tooltipItem

	def Refresh(self):
		getitemVNum=player.GetItemIndex
		getItemCount=player.GetItemCount
		setitemVNum=self.itemSlot.SetItemSlot
		delItem=self.itemSlot.ClearSlot

		maxCount = shop.SHOP_SLOT_COUNT
		if self.isAuctionShop:
			maxCount = auction.SHOP_SLOT_COUNT
		for i in xrange(maxCount):

			if not self.itemStock.has_key(i):
				delItem(i)
				continue

			pos = self.itemStock[i]

			itemCount = getItemCount(*pos)
			if itemCount <= 1:
				itemCount = 0
			setitemVNum(i, getitemVNum(*pos), itemCount)

		self.itemSlot.RefreshSlot()

	def __Load(self):
		if self.isAuctionShop:
			self.itemSlot.ArrangeSlot(0, auction.SHOP_SLOT_COUNT_X, auction.SHOP_SLOT_COUNT_Y, 32, 32, 0, 0)
		else:
			self.itemSlot.ArrangeSlot(0, 5, 8, 32, 32, 0, 0)
		self.itemSlot.SetSlotBaseImage("d:/ymir work/ui/public/Slot_Base.sub", 1.0, 1.0, 1.0, 1.0)
		self.board.SetSize(max(self.itemSlot.GetWidth() + self.itemSlot.GetLeft() * 2, self.colorWindow.GetWidth()), self.board.GetHeight())

		if self.isColorShop:
			self.currentRealColor = (0.8549, 0.8549, 0.8549)
			self.currentBrightness = 1.0
			self.ComputeColor()

			self.colorWindow.Show()
			self.colorScroll.SetSliderPos(0.0)

			self.btnOk.SetPosition(self.btnOk.GetLeft(), self.colorWindow.GetBottom() - self.colorScroll.GetHeight() + 55)
			self.btnClose.SetPosition(self.btnClose.GetLeft(), self.colorWindow.GetBottom() - self.colorScroll.GetHeight() + 55)

			self.board.SetSize(self.board.GetWidth(), self.baseHeight + (self.btnClose.GetTop() - self.colorWindow.GetTop()))

		else:
			self.colorWindow.Hide()

			self.btnOk.SetPosition(self.btnOk.GetLeft(), self.colorWindow.GetTop() + 55)
			self.btnClose.SetPosition(self.btnClose.GetLeft(), self.colorWindow.GetTop() + 55)

			self.board.SetSize(self.board.GetWidth(), self.baseHeight)

		self.SetSize(self.board.GetWidth(), self.board.GetHeight())

	def OnSelectEmptySlot(self, selectedSlotPos):

		isAttached = mouseModule.mouseController.isAttached()
		if isAttached:
			attachedSlotType = mouseModule.mouseController.GetAttachedType()
			attachedSlotPos = mouseModule.mouseController.GetAttachedSlotNumber()
			mouseModule.mouseController.DeattachObject()

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

			if player.SLOT_TYPE_COSTUME_INVENTORY == attachedSlotType:
				invenType = player.DRAGON_SOUL_INVENTORY

			if invenType == -1:
				tchat("attached slot type %d is not allowed" % attachedSlotType)
				return

			itemVNum = player.GetItemIndex(invenType, attachedSlotPos)
			itemCount = player.GetItemCount(invenType, attachedSlotPos)
			item.SelectItem(1, 2, itemVNum)

			if item.IsAntiFlag(item.ITEM_ANTIFLAG_GIVE) or item.IsAntiFlag(item.ITEM_ANTIFLAG_MYSHOP):
				chat.AppendChat(chat.CHAT_TYPE_INFO, localeInfo.PRIVATE_SHOP_CANNOT_SELL_ITEM)
				return

			if itemVNum == 50255 and itemCount < 25:
				chat.AppendChat(chat.CHAT_TYPE_INFO, localeInfo.SELL_AT_LEAST % (25))
				return

			# gemstone
			if itemVNum == 50926 and itemCount < 10:
				chat.AppendChat(chat.CHAT_TYPE_INFO, localeInfo.SELL_AT_LEAST % (10))
				return

			if itemVNum == 71084 and itemCount < 50:
				chat.AppendChat(chat.CHAT_TYPE_INFO, localeInfo.SELL_AT_LEAST % (50))
				return

			if not self.priceInputBoard:
				self.priceInputBoard = uiCommon.SellItemDialog()

			self.priceInputBoard.itemVNum = itemVNum
			self.priceInputBoard.sourceWindowType = invenType
			self.priceInputBoard.sourceSlotPos = attachedSlotPos
			self.priceInputBoard.targetSlotPos = selectedSlotPos

			self.priceInputBoard.SetAcceptEvent(ui.__mem_func__(self.AcceptInputPrice))
			self.priceInputBoard.SetCancelEvent(ui.__mem_func__(self.CancelInputPrice))

			if item.GetItemType() == item.ITEM_TYPE_SKILLBOOK:
				itemPrice=GetPrivateShopItemPrice(itemVNum, player.GetItemMetinSocket(invenType, attachedSlotPos, 0))
			else:
				itemPrice=GetPrivateShopItemPrice(itemVNum)

			if itemPrice!="0":
				self.priceInputBoard.SetValue(itemPrice)

			auction.SendRequestAveragePricePacket(0, itemVNum, itemCount)

	def OnSelectItemSlot(self, selectedSlotPos):

		isAttached = mouseModule.mouseController.isAttached()
		if isAttached:
			snd.PlaySound("sound/ui/loginfail.wav")
			mouseModule.mouseController.DeattachObject()

		else:
			if not selectedSlotPos in self.itemStock:
				return

			invenType, invenPos = self.itemStock[selectedSlotPos]
			if self.isAuctionShop:
				auction.DelShopCreatingItem(invenType, invenPos)
			else:
				shop.DelPrivateShopItemStock(invenType, invenPos)
			snd.PlaySound("sound/ui/drop.wav")

			del self.itemStock[selectedSlotPos]

			self.Refresh()

	def AcceptInputPrice(self):

		if not self.priceInputBoard:
			return True

		text = self.priceInputBoard.GetText().replace('k','000')

		if not text:
			return True

		if not text.isdigit():
			return True

		if int(text) <= 0:
			return True

		attachedInvenType = self.priceInputBoard.sourceWindowType
		sourceSlotPos = self.priceInputBoard.sourceSlotPos
		targetSlotPos = self.priceInputBoard.targetSlotPos

		for privatePos, (itemWindowType, itemSlotIndex) in self.itemStock.items():
			if itemWindowType == attachedInvenType and itemSlotIndex == sourceSlotPos:
				if self.isAuctionShop:
					auction.DelShopCreatingItem(itemWindowType, itemSlotIndex)
				else:
					shop.DelPrivateShopItemStock(itemWindowType, itemSlotIndex)
				del self.itemStock[privatePos]

		price = int(self.priceInputBoard.GetText().replace('k','000'))

		if IsPrivateShopItemPriceList():
			SetPrivateShopItemPrice(self.priceInputBoard.itemVNum, price)

		if self.isAuctionShop:
			auction.AddShopCreatingItem(attachedInvenType, sourceSlotPos, targetSlotPos, price)
		else:
			shop.AddPrivateShopItemStock(attachedInvenType, sourceSlotPos, targetSlotPos, price)
		self.itemStock[targetSlotPos] = (attachedInvenType, sourceSlotPos)
		snd.PlaySound("sound/ui/drop.wav")

		self.Refresh()		

		#####
		self.priceInputBoard.Close()

		self.priceInputBoard = None
		return True

	def CancelInputPrice(self):
		self.priceInputBoard.Close()
		self.priceInputBoard = None
		return True

	def IsInColorCircle(self):
		xCircle, yCircle = self.colorImage.GetGlobalPosition()
		xCenterCircle = xCircle + self.colorImage.GetWidth() / 2
		yCenterCircle = yCircle + self.colorImage.GetHeight() / 2
		radiusCircle = (self.colorImage.GetWidth() + self.colorImage.GetHeight()) / 4
		return wndMgr.IsMouseInCircle(xCenterCircle, yCenterCircle, radiusCircle)

	def OnStartSelectColor(self):
		if not self.IsInColorCircle():
			return

		self.isColorSelecting = True
		self.colorSelectingCounter = 0
		self.OnUpdate()

	def OnStopSelectColor(self):
		self.isColorSelecting = False
		self.colorSelectingCounter = 0
		self.isInColorCircle = False

	def ComputeColor(self):
		realColor = self.currentRealColor
		color = (realColor[0] * self.currentBrightness, realColor[1] * self.currentBrightness, realColor[2] * self.currentBrightness)
		self.currentColor = color

		self.nameLine.SetFontColor(color[0], color[1], color[2])

	def SelectColor(self):
		if not self.isInColorCircle:
			return

		xMouse, yMouse = wndMgr.GetRealMousePosition()
		r, g, b = wndMgr.GetColorAtPosition(xMouse, yMouse)

		self.currentRealColor = (float(r) / 255.0, float(g) / 255.0, float(b) / 255.0)
		self.ComputeColor()

	def OnScrollColorBrightness(self):
		self.currentBrightness = 1.0 - self.colorScroll.GetSliderPos() / 2.0
		self.ComputeColor()

	def OnOk(self):

		if not self.title:
			return

		if 0 == len(self.itemStock):
			return

		if self.isAuctionShop == False:
			shop.BuildPrivateShop(self.title)
		else:
			model, style = 0, 0
			if self.wndVisuals:
				model, style = self.wndVisuals.selectedModelId, self.wndVisuals.selectedLabelId
				self.wndVisuals.selectedModelId, self.wndVisuals.selectedLabelId = 0, 0
			auction.SendOpenShopPacket(self.title, model, style)
			self.itemStock = { }
			self.Refresh()
			# self.currentColor[0], self.currentColor[1], self.currentColor[2]

		self.Close()

	def OnUpdate(self):
		if self.isColorSelecting == True:
			self.isInColorCircle = self.IsInColorCircle()
			if self.colorSelectingCounter % 2 == 0:
				self.SelectColor()
			self.colorSelectingCounter = self.colorSelectingCounter + 1

	def OnRenderFinish(self):
		if self.isColorSelecting == True and self.isInColorCircle == True:
			xMouse, yMouse = wndMgr.GetMousePosition()
			# render circle border
			grp.SetColor(grp.GenerateColor(1.0 - self.currentColor[0], 1.0 - self.currentColor[1], 1.0 - self.currentColor[2], 1.0))
			grp.RenderCircle2d(xMouse, yMouse, self.COLOR_CIRCLE_SIZE)
			# render circle color
			xStart = xMouse - self.COLOR_CIRCLE_SIZE
			xEnd = xMouse + self.COLOR_CIRCLE_SIZE
			yStart = yMouse - self.COLOR_CIRCLE_SIZE
			yEnd = yMouse + self.COLOR_CIRCLE_SIZE
			grp.SetColor(grp.GenerateColor(self.currentColor[0], self.currentColor[1], self.currentColor[2], 1.0))
			for x in xrange(xStart, xEnd):
				for y in xrange(yStart, yEnd):
					if not wndMgr.IsInCircle(xMouse, yMouse, 2, x, y) and wndMgr.IsInCircle(xMouse, yMouse, self.COLOR_CIRCLE_SIZE - 1, x, y):
						grp.RenderLine(x, y, 1, 0)

	def OnClose(self):
		self.Close()

	def OnPressEscapeKey(self):
		self.Close()
		return True

	def OnOverInItem(self, slotIndex):

		if self.tooltipItem:
			if self.itemStock.has_key(slotIndex):
				if self.isAuctionShop:
					self.tooltipItem.SetAuctionShopBuilderItem(*self.itemStock[slotIndex] + (slotIndex,))
				else:
					self.tooltipItem.SetPrivateShopBuilderItem(*self.itemStock[slotIndex] + (slotIndex,))

	def OnOverOutItem(self):

		if self.tooltipItem:
			self.tooltipItem.HideToolTip()

	def __OnBtnVisuals(self):
		if not self.wndVisuals:
			self.wndVisuals = self.VisualsWindow()

		self.wndVisuals.Open()

	def OpenSellWindow(self, price):
		if not self.priceInputBoard:
			return

		tchat("taxData = %s (isAuctionShop %d)" % (self.TAX_DATA[self.isAuctionShop], self.isAuctionShop))
		self.priceInputBoard.average = price
		self.priceInputBoard.Open(self.TAX_DATA[self.isAuctionShop])
