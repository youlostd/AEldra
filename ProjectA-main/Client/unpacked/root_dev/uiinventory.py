import ui
import player
import mouseModule
import net
import app
import snd
import item
import player
import chat
import grp
import uiScriptLocale
import uiRefine
import uiAttachMetin
import uiSelectMetinDetach
import uiSelectAttrRemove
import uiPickMoney
import uiSplitItem
import uiCommon
import uiPrivateShopBuilder # ���λ��� ������ ItemMove ����
import localeInfo
import constInfo
import ime
import cfg
import wndMgr
import chr
import safebox
import exchange
import uiExchange
import game
import shop
import auction

ITEM_FLAG_APPLICABLE = 1 << 14

def GetEmptyItemPos(itemHeight, pageCount, jump=-1):
	for page in xrange(pageCount):
		curPageGrid = [0 for i in xrange(player.INVENTORY_PAGE_SIZE)]
		for y in xrange(player.INVENTORY_PAGE_Y_SLOTCOUNT - itemHeight + 1):
			for x in xrange(player.INVENTORY_PAGE_X_SLOTCOUNT):
				if jump >= page * player.INVENTORY_PAGE_SIZE + y * player.INVENTORY_PAGE_X_SLOTCOUNT + x:
					continue

				curItemVnumPos = page * player.INVENTORY_PAGE_SIZE + y * player.INVENTORY_PAGE_X_SLOTCOUNT + x
				curItemVnum = player.GetItemIndex(curItemVnumPos)

				if curPageGrid[y * player.INVENTORY_PAGE_X_SLOTCOUNT + x] == 0 and curItemVnum == 0:
					failed = False
					for i in xrange(itemHeight - 1):
						if player.GetItemIndex(page * player.INVENTORY_PAGE_SIZE + y * player.INVENTORY_PAGE_X_SLOTCOUNT + x + i * player.INVENTORY_PAGE_X_SLOTCOUNT) != 0:
							failed = True
							break

					if failed == False:
						return page * player.INVENTORY_PAGE_SIZE + y * player.INVENTORY_PAGE_X_SLOTCOUNT + x
				elif curItemVnum != 0:
					item.SelectItem(1, 2, curItemVnum)
					itemWidth, itemHeight = item.GetItemSize()
					for i in xrange(itemHeight):
						curPageGrid[(y + i) * player.INVENTORY_PAGE_X_SLOTCOUNT + x] = 1

	return -1

if constInfo.USE_COMBINED_CUSTOME_WINDOW:
	class CostumeWindowCombined(ui.ScriptWindow):
		def __init__(self, wndInventory):
			import exception
			
			if not app.ENABLE_COSTUME_SYSTEM:			
				exception.Abort("What do you do?")
				return

			if not wndInventory:
				exception.Abort("wndInventory parameter must be set to InventoryWindow")
				return						
				 	 
			ui.ScriptWindow.__init__(self)
			self.wndInventory = wndInventory;

			self.__LoadWindow()

		def __del__(self):
			ui.ScriptWindow.__del__(self)

		def Show(self):
			self.RefreshCostumeSlot()

			ui.ScriptWindow.Show(self)

		def __LoadWindow(self):
			try:
				pyScrLoader = ui.PythonScriptLoader()
				pyScrLoader.LoadScriptFile(self, "UIScript/CombinedCostumeWindow.py")
			except:
				import exception
				exception.Abort("CostumeWindow.LoadWindow.LoadObject")

			try:
				wndBoard = self.GetChild("board")
				wndCostume = self.GetChild("CostumeSlot")

			except:
				import exception
				exception.Abort("CostumeWindow.LoadWindow.BindObject")

			titleBar = ui.TitleBar()
			titleBar.SetParent(wndBoard)
			titleBar.MakeTitleBar(0, "red")
			if app.GetSelectedDesignName() != "illumina":
				titleBar.SetPosition(8, 7)
			else:
				titleBar.SetPosition(8, 11)
			titleBar.Show()

			titleName = ui.TextLine()
			titleName.SetParent(titleBar)
			titleName.SetPosition(0, 4)
			if app.GetSelectedDesignName() != "illumina":
				titleName.SetPosition(0, 4)
			else:
				titleName.SetPosition(0, 7)
			titleName.SetWindowHorizontalAlignCenter()
			titleName.SetHorizontalAlignCenter()
			titleName.SetText(uiScriptLocale.COSTUME_WINDOW_TITLE)
			titleName.Show()

			self.titleName = titleName
			self.titleBar = titleBar

			self.titleBar.SetWidth(wndBoard.GetWidth() - 15)
			self.titleName.UpdateRect()

			wndCostume.SetOverInItemEvent(ui.__mem_func__(self.wndInventory.OverInItem))
			wndCostume.SetOverOutItemEvent(ui.__mem_func__(self.wndInventory.OverOutItem))
			wndCostume.SetUnselectItemSlotEvent(ui.__mem_func__(self.wndInventory.UseItemSlot))
			wndCostume.SetUseSlotEvent(ui.__mem_func__(self.wndInventory.UseItemSlot))						
			wndCostume.SetSelectEmptySlotEvent(ui.__mem_func__(self.wndInventory.SelectEmptySlot))
			wndCostume.SetSelectItemSlotEvent(ui.__mem_func__(self.wndInventory.SelectItemSlot))

			self.wndBoard = wndBoard
			self.wndCostume = wndCostume

		def RefreshCostumeSlot(self):
			getItemVNum=player.GetItemIndex
			getItemCount=player.GetItemCount
			
			for i in xrange(player.EQUIPMENT_PAGE_COUNT):
				slotNumber = player.EQUIPMENT_SLOT_START + i
				if self.wndCostume.HasSlot(slotNumber):
					itemCount = getItemCount(slotNumber)
					if itemCount <= 1:
						itemCount = 0
					self.wndCostume.SetItemSlot(slotNumber, getItemVNum(slotNumber), itemCount)
			
			for i in xrange(player.SHINING_MAX_NUM):
				slotNumber = player.SHINING_EQUIP_SLOT_START + i
				if self.wndCostume.HasSlot(slotNumber):
					itemCount = getItemCount(slotNumber)
					if itemCount <= 1:
						itemCount = 0
					self.wndCostume.SetItemSlot(slotNumber, getItemVNum(slotNumber), itemCount)

			for i in xrange(player.SKINSYSTEM_EQUIP_SLOT_START):
				slotNumber = player.SKINSYSTEM_EQUIP_SLOT_START + i
				if self.wndCostume.HasSlot(slotNumber):
					itemCount = getItemCount(slotNumber)
					if itemCount <= 1:
						itemCount = 0
					self.wndCostume.SetItemSlot(slotNumber, getItemVNum(slotNumber), itemCount)

			self.wndCostume.RefreshSlot()

		def SetCloseEvent(self, event):
			self.titleBar.SetCloseEvent(ui.__mem_func__(event))

class CostumeWindow(ui.ScriptWindow):

	def __init__(self, wndInventory):
		import exception
		
		if not app.ENABLE_COSTUME_SYSTEM:			
			exception.Abort("What do you do?")
			return

		if not wndInventory:
			exception.Abort("wndInventory parameter must be set to InventoryWindow")
			return						
			 	 
		ui.ScriptWindow.__init__(self)
		self.wndInventory = wndInventory;

		self.__LoadWindow()

	def __del__(self):
		ui.ScriptWindow.__del__(self)

	def Show(self):
		self.RefreshCostumeSlot()

		ui.ScriptWindow.Show(self)

	def __LoadWindow(self):
		try:
			pyScrLoader = ui.PythonScriptLoader()
			if constInfo.USE_NEW_COSTUME_WITH_ACCE:
				pyScrLoader.LoadScriptFile(self, "UIScript/CostumeWindow_New.py")
			else:
				pyScrLoader.LoadScriptFile(self, "UIScript/CostumeWindow.py")
		except:
			import exception
			exception.Abort("CostumeWindow.LoadWindow.LoadObject")

		try:
			wndBoard = self.GetChild("board")
			wndCostume = self.GetChild("CostumeSlot")

		except:
			import exception
			exception.Abort("CostumeWindow.LoadWindow.BindObject")

		wndCostume.SetOverInItemEvent(ui.__mem_func__(self.wndInventory.OverInItem))
		wndCostume.SetOverOutItemEvent(ui.__mem_func__(self.wndInventory.OverOutItem))
		wndCostume.SetUnselectItemSlotEvent(ui.__mem_func__(self.wndInventory.UseItemSlot))
		wndCostume.SetUseSlotEvent(ui.__mem_func__(self.wndInventory.UseItemSlot))						
		wndCostume.SetSelectEmptySlotEvent(ui.__mem_func__(self.wndInventory.SelectEmptySlot))
		wndCostume.SetSelectItemSlotEvent(ui.__mem_func__(self.wndInventory.SelectItemSlot))

		self.wndBoard = wndBoard
		self.wndCostume = wndCostume

	def RefreshCostumeSlot(self):
		getItemVNum=player.GetItemIndex
		getItemCount=player.GetItemCount
		
		for i in xrange(player.EQUIPMENT_PAGE_COUNT):
			slotNumber = player.EQUIPMENT_SLOT_START + i
			if self.wndCostume.HasSlot(slotNumber):
				itemCount = getItemCount(slotNumber)
				if itemCount <= 1:
					itemCount = 0
				self.wndCostume.SetItemSlot(slotNumber, getItemVNum(slotNumber), itemCount)

		self.wndCostume.RefreshSlot()

	def SetCloseEvent(self, event):
		self.wndBoard.SetCloseEvent(ui.__mem_func__(event))

class ShiningWindow(ui.ScriptWindow):

	def __init__(self, wndInventory):
		import exception

		if not wndInventory:
			exception.Abort("wndInventory parameter must be set to InventoryWindow")
			return						
			 	 
		ui.ScriptWindow.__init__(self)
		self.wndInventory = wndInventory;

		self.__LoadWindow()

	def __del__(self):
		ui.ScriptWindow.__del__(self)

	def Show(self):
		self.RefreshShiningSlot()

		if constInfo.SHINING_SYSTEM:
			ui.ScriptWindow.Show(self)

	def __LoadWindow(self):
		try:
			pyScrLoader = ui.PythonScriptLoader()
			pyScrLoader.LoadScriptFile(self, "UIScript/ShiningWindow.py")
		except:
			import exception
			exception.Abort("ShiningWindow.LoadWindow.LoadObject")

		try:
			wndBoard = self.GetChild("board")
			wndShiningArmor = self.GetChild("ShiningSlotArmor")
			wndShiningWeapon = self.GetChild("ShiningSlotWeapon")

		except:
			import exception
			exception.Abort("ShiningWindow.LoadWindow.BindObject")

		for i in (wndShiningArmor, wndShiningWeapon,):
			i.SetOverInItemEvent(ui.__mem_func__(self.wndInventory.OverInItem))
			i.SetOverOutItemEvent(ui.__mem_func__(self.wndInventory.OverOutItem))
			i.SetUnselectItemSlotEvent(ui.__mem_func__(self.wndInventory.UseItemSlot))
			i.SetUseSlotEvent(ui.__mem_func__(self.wndInventory.UseItemSlot))						
			i.SetSelectEmptySlotEvent(ui.__mem_func__(self.wndInventory.SelectEmptySlot))
			i.SetSelectItemSlotEvent(ui.__mem_func__(self.wndInventory.SelectItemSlot))

		self.wndBoard = wndBoard
		self.wndShiningArmor = wndShiningArmor
		self.wndShiningWeapon = wndShiningWeapon

	def RefreshShiningSlot(self):
		getItemVNum=player.GetItemIndex
		getItemCount=player.GetItemCount
		
		for i in xrange(player.SHINING_MAX_NUM):
			slotNumber = player.SHINING_EQUIP_SLOT_START + i
			if self.wndShiningArmor.HasSlot(slotNumber):
				itemCount = getItemCount(slotNumber)
				if itemCount <= 1:
					itemCount = 0
				self.wndShiningArmor.SetItemSlot(slotNumber, getItemVNum(slotNumber), itemCount)

			elif self.wndShiningWeapon.HasSlot(slotNumber):
				itemCount = getItemCount(slotNumber)
				if itemCount <= 1:
					itemCount = 0
				self.wndShiningWeapon.SetItemSlot(slotNumber, getItemVNum(slotNumber), itemCount)

		self.wndShiningArmor.RefreshSlot()
		self.wndShiningWeapon.RefreshSlot()

	def SetCloseEvent(self, event):
		self.wndBoard.SetCloseEvent(ui.__mem_func__(event))

class SkinSystemWindow(ui.ScriptWindow):

	def __init__(self, wndInventory):
		import exception

		if not wndInventory:
			exception.Abort("wndInventory parameter must be set to InventoryWindow")
			return						
			 	 
		ui.ScriptWindow.__init__(self)
		self.wndInventory = wndInventory

		self.__LoadWindow()

	def __del__(self):
		ui.ScriptWindow.__del__(self)

	def Show(self):
		self.RefreshCostumeSlot()

		ui.ScriptWindow.Show(self)

	def __LoadWindow(self):
		try:
			pyScrLoader = ui.PythonScriptLoader()
			pyScrLoader.LoadScriptFile(self, "UIScript/skinsystemwindow.py")
		except:
			import exception
			exception.Abort("CostumeWindow.LoadWindow.LoadObject")

		try:
			wndBoard = self.GetChild("board")

			slotPet = self.GetChild("SlotPet")
			slotMount = self.GetChild("SlotMount")
			slotBuffiBody = self.GetChild("SlotBuffiBody")
			slotBuffiWeapon = self.GetChild("SlotBuffiWeapon")

		except:
			import exception
			exception.Abort("SkinSystemWindow.LoadWindow.BindObject")

		for i in (slotPet, slotMount, slotBuffiBody, slotBuffiWeapon,):
			i.SetOverInItemEvent(ui.__mem_func__(self.wndInventory.OverInItem))
			i.SetOverOutItemEvent(ui.__mem_func__(self.wndInventory.OverOutItem))
			i.SetUnselectItemSlotEvent(ui.__mem_func__(self.wndInventory.UseItemSlot))
			i.SetUseSlotEvent(ui.__mem_func__(self.wndInventory.UseItemSlot))						
			i.SetSelectEmptySlotEvent(ui.__mem_func__(self.wndInventory.SelectEmptySlot))
			i.SetSelectItemSlotEvent(ui.__mem_func__(self.wndInventory.SelectItemSlot))

		self.wndBoard = wndBoard

		self.slotPet = slotPet
		self.slotMount = slotMount
		self.slotBuffiBody = slotBuffiBody
		self.slotBuffiWeapon = slotBuffiWeapon

	def RefreshCostumeSlot(self):
		getItemVNum=player.GetItemIndex
		getItemCount=player.GetItemCount
		
		slots = {
			item.SKINSYSTEM_SLOT_PET : self.slotPet,
			item.SKINSYSTEM_SLOT_MOUNT : self.slotMount,
			item.SKINSYSTEM_SLOT_BUFFI_BODY : self.slotBuffiBody,
			item.SKINSYSTEM_SLOT_BUFFI_WEAPON : self.slotBuffiWeapon,
		}

		for slotNum, slot in slots.iteritems():
			
			if slot.HasSlot(slotNum):
				
				itemCount = getItemCount(slotNum)

				if itemCount <= 1:
					itemCount = 0

				slot.SetItemSlot(slotNum, getItemVNum(slotNum), itemCount)

			slot.RefreshSlot()

	def SetCloseEvent(self, event):
		self.wndBoard.SetCloseEvent(ui.__mem_func__(event))

class InventoryWindow(ui.ScriptWindow):

	USE_TYPE_TUPLE = ("USE_CLEAN_SOCKET", "USE_CHANGE_ATTRIBUTE", "USE_ADD_ATTRIBUTE", "USE_ADD_ATTRIBUTE2", "USE_ADD_ACCESSORY_SOCKET", "USE_PUT_INTO_ACCESSORY_SOCKET", "USE_SPECIAL", "USE_ADD_SPECIFIC_ATTRIBUTE", "USE_PUT_INTO_ACCESSORY_SOCKET_PERMA", "USE_TYPE_SOUL", "USE_CHANGE_SASH_COSTUME_ATTR", "USE_DEL_LAST_PERM_ORE")

	isOpenedCostumeWindowWhenClosingInventory = 0
	wndCostume = None
	wndShining = None
	wndCombinedCostume = None
	wndSkinSystem = None

	SIDEBAR_BTN_STORAGE = 0
	SIDEBAR_BTN_WIKI = 1
	SIDEBAR_BTN_AUCTION = 2
	SIDEBAR_BTN_SWITCHBOT = 3
	SIDEBAR_BTN_MAX_NUM = 4

	SIDEBAR_BTN_ICONS = {
		SIDEBAR_BTN_STORAGE : "d:/ymir work/ui/game/inventory/safebox.tga",
		SIDEBAR_BTN_WIKI : "d:/ymir work/ui/icon/wikibutton.tga",
		SIDEBAR_BTN_AUCTION : "d:/ymir work/ui/game/inventory/shop_search.tga",
		SIDEBAR_BTN_SWITCHBOT : "d:/ymir work/ui/game/inventory/switchbot.tga",
	}

	def __init__(self):
		ui.ScriptWindow.__init__(self)
		self.questionDialog = None
		self.tooltipItem = None
		self.sellingSlotNumber = -1
		self.isLoaded = 0
		# ENABLE_MARK_NEW_ITEM_SYSTEM
		self.liHighlightedItems = []
		# ENABLE_MARK_NEW_ITEM_SYSTEM
		self.liAcceItems =[]
		self.slotDisable = []
		self.slotActive = []

		self.eventCTRLClickItem = None

		self.sidebarButtons = []

		self.sellingItemList = []

		self.interface = None

		if constInfo.FAST_MOVE_ITEM_COOLDOWN:
			self.fastMoveAuctionShopItem = 0

		self.__LoadWindow()
		self.__BuildSidebar()

	def __del__(self):
		ui.ScriptWindow.__del__(self)

	def BindInterface(self, interface):
		self.interface = interface

	def Show(self):
		self.__LoadWindow()
		self.__CheckBaseImg()

		ui.ScriptWindow.Show(self)
		if self.isOpenedCostumeWindowWhenClosingInventory and (self.wndCostume or self.wndCombinedCostume):
			self.OpenCostumeWindow()

		if constInfo.SAVE_WINDOW_POSITION:
			if int(cfg.Get(cfg.SAVE_GENERAL, "save_wnd_pos", "0")):
				x, y = map(int, cfg.Get(cfg.SAVE_GENERAL, "wnd_pos_inv", "0 0").split(" "))
				if x and y:
					self.SetPosition(x, y)
					self.UpdateCostumePosition()
					self.__UpdateSidebarPosition()

		self.__ShowSidebar()

	def Hide(self):
		ui.ScriptWindow.Hide(self)

		try:
			self.__HideSidebar()
		except:
			pass

	def __LoadWindow(self):
		if self.isLoaded == 1:
			return

		self.isLoaded = 1

		try:
			pyScrLoader = ui.PythonScriptLoader()
			pyScrLoader.LoadScriptFile(self, "UIScript/InventoryWindow.py")
		except:
			import exception
			exception.Abort("InventoryWindow.LoadWindow.LoadObject")

		try:
			wndItem = self.GetChild("ItemSlot")
			wndEquip = self.GetChild("EquipmentSlot")
			self.GetChild("TitleBar").SetCloseEvent(ui.__mem_func__(self.Close))
			self.btnOpenCostume = self.GetChild("CostumeButton")
			self.btnAuctionShop = self.GetChild("ShopButton")

			self.inventoryTab = []
			self.inventoryTab.append(self.GetChild("Inventory_Tab_01"))
			self.inventoryTab.append(self.GetChild("Inventory_Tab_02"))
			self.inventoryTab.append(self.GetChild("Inventory_Tab_03"))
			self.inventoryTab.append(self.GetChild("Inventory_Tab_04"))
			if __SERVER__ == 2:
				self.GetChild("Inventory_Tab_05").Hide()
				for i in xrange(4):
					self.inventoryTab[i].SetPosition(2 + (i*(38+1)), 26 + 191)
			self.inventoryTab.append(self.GetChild("Inventory_Tab_05"))


			self.equipmentTab = []
			self.equipmentTab.append(self.GetChild("Equipment_Tab_01"))
			self.equipmentTab.append(self.GetChild("Equipment_Tab_02"))

			self.slotDisable = []
			for i in xrange(player.INVENTORY_PAGE_SIZE/5):
				self.slotDisable.append(self.GetChild("ItemSlotDisable%d" % (i + 1)))

			self.wndEquipBase = self.GetChild("Equipment_Base")

			self.GetChild("DragonSoulButton").SAFE_SetEvent(self.ClickDSSButton)

			# didnt work in uiscript/inventorywindow.py so I moved it here...
			self.dragonSoulActiveEffect = ui.AniImageBox()
			self.dragonSoulActiveEffect.SetParent( self )

			# it goes from 0 to 12
			for i in range( 0, 13 ):
				self.dragonSoulActiveEffect.AppendImage( "d:/ymir work/ui/public/slotactiveeffect/%s.sub" % str( i ).zfill( 2 ) )

			self.dragonSoulActiveEffect.SetPosition( 87, 141 )
			self.dragonSoulActiveEffect.Hide()

			if constInfo.SORT_AND_STACK_ITEMS:
				self.GetChild("SeparateButton").SAFE_SetEvent(self.__StackItems)

		except:
			import exception
			exception.Abort("InventoryWindow.LoadWindow.BindObject")

		## Item
		wndItem.SetSelectEmptySlotEvent(ui.__mem_func__(self.SelectEmptySlot))
		wndItem.SetSelectItemSlotEvent(ui.__mem_func__(self.SelectItemSlot))
		wndItem.SetUnselectItemSlotEvent(ui.__mem_func__(self.UseItemSlot))
		wndItem.SetUseSlotEvent(ui.__mem_func__(self.UseItemSlot))
		wndItem.SetOverInItemEvent(ui.__mem_func__(self.OverInItem))
		wndItem.SetOverOutItemEvent(ui.__mem_func__(self.OverOutItem))

		## Equipment
		wndEquip.SetSelectEmptySlotEvent(ui.__mem_func__(self.SelectEmptySlot))
		wndEquip.SetSelectItemSlotEvent(ui.__mem_func__(self.SelectItemSlot))
		wndEquip.SetUnselectItemSlotEvent(ui.__mem_func__(self.UseItemSlot))
		wndEquip.SetUseSlotEvent(ui.__mem_func__(self.UseItemSlot))
		wndEquip.SetOverInItemEvent(ui.__mem_func__(self.OverInItem))
		wndEquip.SetOverOutItemEvent(ui.__mem_func__(self.OverOutItem))

		## PickMoneyDialog
		dlgPickMoney = uiPickMoney.PickMoneyDialog()
		dlgPickMoney.LoadDialog()
		dlgPickMoney.Hide()

		## SplitItemDialog
		dlgSplitItem = uiSplitItem.SplitItemDialog()
		dlgSplitItem.LoadDialog()
		dlgSplitItem.Hide()

		## RefineDialog
		self.refineDialog = uiRefine.RefineDialog()
		self.refineDialog.Hide()

		## AttachMetinDialog
		self.attachMetinDialog = uiAttachMetin.AttachMetinDialog()
		self.attachMetinDialog.Hide()

		self.detachMetinDialog = uiSelectMetinDetach.SelectMetinDetachWindow()
		self.detachMetinDialog.Close()

		self.removeAttrDialog = uiSelectAttrRemove.SelectAttrRemoveWindow()
		self.removeAttrDialog.Close()

		self.btnOpenCostume.SAFE_SetEvent(self.OpenCostumeWindow)

		self.inventoryTab[0].SetEvent(lambda arg=0: self.SetInventoryPage(arg))
		self.inventoryTab[1].SetEvent(lambda arg=1: self.SetInventoryPage(arg))
		self.inventoryTab[2].SetEvent(lambda arg=2: self.SetInventoryPage(arg))
		self.inventoryTab[3].SetEvent(lambda arg=3: self.SetInventoryPage(arg))
		self.inventoryTab[4].SetEvent(lambda arg=4: self.SetInventoryPage(arg))
		self.inventoryTab[0].Down()

		self.equipmentTab[0].SetEvent(lambda arg=0: self.SetEquipmentPage(arg))
		self.equipmentTab[1].SetEvent(lambda arg=1: self.SetEquipmentPage(arg))
		self.equipmentTab[0].Down()
		self.equipmentTab[0].Hide()
		self.equipmentTab[1].Hide()

		self.wndItem = wndItem
		self.wndEquip = wndEquip
		self.dlgPickMoney = dlgPickMoney
		self.dlgSplitItem = dlgSplitItem

		#####
		self.wndCostume = None
		self.wndShining = None
		self.wndCombinedCostume = None
		self.wndSkinSystem = None

		## Refresh
		self.SetInventoryPage(0)
		self.SetEquipmentPage(0)
		self.RefreshItemSlot()
		if constInfo.SORT_AND_STACK_ITEMS:
			self.questionWnd = uiCommon.QuestionDialog()
			self.questionWnd.SAFE_SetAcceptEvent(self.__StackItemsRequest)
			self.questionWnd.SAFE_SetCancelEvent(self.questionWnd.Close)
			self.questionWnd.SetText(localeInfo.CONFIRM_STACK)

	if constInfo.SORT_AND_STACK_ITEMS:
		def __StackItems(self):
			self.questionWnd.Open()

		def __StackItemsRequest(self):
			net.SendChatPacket("/stack %d" % 1)
			net.SendChatPacket("/sort %d" % 1)
			self.questionWnd.Close()

	def SAFE_SetAuctionShopEvent(self, event):
		self.btnAuctionShop.SAFE_SetEvent(event)

	def EnableSidebarButton(self, btnIdx):
		btn = self.sidebarButtons[btnIdx]
		btn.Enable()
		btn.icon.Show()

	def DisableSidebarButton(self, btnIdx):
		btn = self.sidebarButtons[btnIdx]
		btn.Disable()
		btn.icon.Hide()

	def SAFE_SetSidebarButtonEvent(self, btnIdx, event):
		btn = self.sidebarButtons[btnIdx]
		btn.SAFE_SetEvent(event)

	def OpenWikiWnd(self):
		if self.interface.dlgSystem.wikiWnd.IsShow():
			self.interface.dlgSystem.wikiWnd.Hide()
		else:
			self.interface.dlgSystem.wikiWnd.Show()

	def __HideSidebar(self):
		for btn in self.sidebarButtons:
			btn.Hide()

	def __ShowSidebar(self):
		for btn in self.sidebarButtons:
			btn.Show()

	def __BuildSidebar(self):
		for i in xrange(self.SIDEBAR_BTN_MAX_NUM):
			btn = ui.Button()
			btn.AddFlag("float")
			btn.SetUpVisual("d:/ymir work/ui/game/inventory/sidebutton_normal.tga")
			btn.SetOverVisual("d:/ymir work/ui/game/inventory/sidebutton_hover.tga")
			btn.SetDownVisual("d:/ymir work/ui/game/inventory/sidebutton_down.tga")
			# btn.SetDisableVisual("d:/ymir work/ui/game/inventory/sidebutton_disabled.tga")

			btn.icon = ui.ImageBox()
			btn.icon.SetParent(btn)
			btn.icon.AddFlag("not_pick")
			btn.icon.LoadImage(self.SIDEBAR_BTN_ICONS[i])
			btn.icon.SetWindowHorizontalAlignCenter()
			btn.icon.SetWindowVerticalAlignCenter()
			btn.icon.SetPosition(3 if self.SIDEBAR_BTN_AUCTION == i else 1, 0)
			# tchat('%s %i' % (self.SIDEBAR_BTN_ICONS[i], 3 if self.SIDEBAR_BTN_SWITCHBOT == i else 1))
			btn.icon.Show()

			btn.Hide()
			self.sidebarButtons.append(btn)
		
		self.__UpdateSidebarPosition()
		self.SAFE_SetSidebarButtonEvent(self.SIDEBAR_BTN_WIKI, self.OpenWikiWnd)
 
	def __UpdateSidebarPosition(self):
		invX, invY = self.GetGlobalPosition()
		y = invY + 20

		for i in xrange(self.SIDEBAR_BTN_MAX_NUM):
			btn = self.sidebarButtons[i]

			x = invX - btn.GetWidth() + 2
			btn.SetPosition(x, y)

			y += btn.GetHeight() + 3

	def Destroy(self):
		self.Close()
		self.ClearDictionary()

		self.dlgPickMoney.Destroy()
		self.dlgPickMoney = 0

		self.dlgSplitItem.Destroy()
		self.dlgSplitItem = 0

		self.refineDialog.Destroy()
		self.refineDialog = 0

		self.attachMetinDialog.Destroy()
		self.attachMetinDialog = 0

		self.detachMetinDialog.Destroy()
		self.detachMetinDialog = None

		self.removeAttrDialog.Destroy()
		self.removeAttrDialog = None

		if self.wndCostume:
			self.wndCostume.Destroy()
			self.wndCostume = 0

		if self.wndShining:
			self.wndShining.Destroy()
			self.wndShining = 0

		if app.ENABLE_SKIN_SYSTEM:
			if self.wndSkinSystem:
				self.wndSkinSystem.Destroy()
				self.wndSkinSystem = 0

		if self.wndCombinedCostume:
			self.wndCombinedCostume.Destroy()
			self.wndCombinedCostume = None

		self.__HideSidebar()
		self.sidebarButtons = []

		self.tooltipItem = None
		self.wndItem = 0
		self.wndEquip = 0
		self.questionDialog = None

		self.inventoryTab = []
		self.equipmentTab = []
		self.slotDisable = []

	def Close(self):
		if None != self.tooltipItem:
			self.tooltipItem.inventoryItemSlot = -1
			self.tooltipItem.HideToolTip()

		if self.wndCostume:
			self.isOpenedCostumeWindowWhenClosingInventory = self.wndCostume.IsShow()
			self.CloseCostumeWindow()

		if self.wndCombinedCostume:
			self.isOpenedCostumeWindowWhenClosingInventory = self.wndCombinedCostume.IsShow()
			self.CloseCostumeWindow()

		self.OnCloseQuestionDialog()
		self.dlgPickMoney.Close()
		self.dlgSplitItem.Close()
		self.Hide()

	def OnKeyUp(self, key):
		if (key == app.DIK_LCONTROL and not app.IsPressed(app.DIK_RCONTROL)) or (key == app.DIK_RCONTROL and not app.IsPressed(app.DIK_LCONTROL)):
			if len(self.sellingItemList) > 0:
				self.__SellMultiItem()

	def SetCTRLClickItemEvent(self, event):
		self.eventCTRLClickItem = event

	def __CheckBaseImg(self):
		if app.GetSelectedDesignName() == "illumina":
			sex = chr.RaceToSex(player.GetRace())
			if sex == 0:
				imgName = self.wndEquipBase.GetImageName()
				if imgName.find("_w.sub") == -1:
					imgName = imgName.replace(".sub", "_w.sub")
					self.wndEquipBase.LoadImage(imgName)

	def RefreshInventoryMaxNum(self):
		curIdx = self.__InventoryLocalSlotPosToGlobalSlotPos(0)
		maxIdx = player.GetInventoryMaxNum()
		yCount = 0

		for disableImg in self.slotDisable:
			if curIdx < maxIdx:
				disableImg.Hide()
				yCount += 1
			else:
				disableImg.Show()
			curIdx += 5

		self.wndItem.ArrangeSlot(0, 5, yCount, 32, 32, 0, 0)
		self.wndItem.SetSlotBaseImage("d:/ymir work/ui/public/Slot_Base.sub", 1.0, 1.0, 1.0, 1.0)
		self.RefreshBagSlotWindow()

	def SetInventoryPage(self, page):
		self.inventoryPageIndex = page
		for i in xrange(len(self.inventoryTab)):
			if i != page:
				self.inventoryTab[i].SetUp()
		self.RefreshInventoryMaxNum()
		self.RefreshBagSlotWindow()

	def SetEquipmentPage(self, page):
		self.equipmentPageIndex = page
		self.equipmentTab[1-page].SetUp()
		self.RefreshEquipSlotWindow()

	def GetEmptyItemPos(self, itemHeight, jump=-1):
		return GetEmptyItemPos(itemHeight, player.INVENTORY_PAGE_COUNT, jump)

	def AppendSafeboxItem(self, itemSlotPos):
		itemID = safebox.GetItemID(itemSlotPos)
		item.SelectItem(1, 2, itemID)

		itemWidth, itemHeight = item.GetItemSize()
		emptyPos = self.GetEmptyItemPos(itemHeight)

		if emptyPos == -1:
			return

		net.SendSafeboxCheckoutPacket(itemSlotPos, emptyPos)

	def AppendInvSafeboxItem(self, itemSlotIndex):
		itemID = player.GetItemIndex(itemSlotIndex)
		itemSockets = [player.GetItemMetinSocket(itemSlotIndex, j) for j in xrange(player.METIN_SOCKET_MAX_NUM)]
		item.SelectItem(1, 2, itemID)
		emptyPos = -1
		if item.IsStackable():
			for i in xrange(player.INVENTORY_PAGE_COUNT * player.INVENTORY_PAGE_SIZE):
				curItemID = player.GetItemIndex(i)
				if curItemID == itemID:
					if player.GetItemCount(i) + player.GetItemCount(itemSlotIndex) > constInfo.ITEM_MAX_COUNT:
						continue
					socketCheck = True
					for j in xrange(player.METIN_SOCKET_MAX_NUM):
						if player.GetItemMetinSocket(i, j) != itemSockets[j]:
							socketCheck = False
							break
					if socketCheck:
						emptyPos = i
						break

		if emptyPos == -1:
			itemWidth, itemHeight = item.GetItemSize()
			emptyPos = self.GetEmptyItemPos(itemHeight)

			if emptyPos == -1:
				return

		self.__SendMoveItemPacket(itemSlotIndex, emptyPos, 0)

	def AppendMallItem(self, itemSlotPos):
		itemID = safebox.GetMallItemID(itemSlotPos)
		item.SelectItem(1, 2, itemID)

		itemWidth, itemHeight = item.GetItemSize()
		emptyPos = self.GetEmptyItemPos(itemHeight)

		if emptyPos == -1:
			return

		net.SendMallCheckoutPacket(itemSlotPos, emptyPos)

	def AppendGuildSafeboxItem(self, itemSlotPos):
		itemID = safebox.GetGuildItemID(itemSlotPos)
		item.SelectItem(1, 2, itemID)

		itemWidth, itemHeight = item.GetItemSize()
		emptyPos = self.GetEmptyItemPos(itemHeight)

		if emptyPos == -1:
			return

		net.SendGuildSafeboxCheckoutPacket(itemSlotPos, emptyPos)

	def OnPickItem(self, count):
		itemSlotIndex = self.dlgSplitItem.itemGlobalSlotIndex
		selectedItemVNum = player.GetItemIndex(itemSlotIndex)
		mouseModule.mouseController.AttachObject(self, player.SLOT_TYPE_INVENTORY, itemSlotIndex, selectedItemVNum, count)

	def ClickDSSButton(self):
		self.interface.ToggleDragonSoulWindow()

	def OpenCostumeWindow(self):
		if constInfo.USE_COMBINED_CUSTOME_WINDOW:
			if not self.wndCombinedCostume:
				self.wndCombinedCostume = CostumeWindowCombined(self)
				self.wndCombinedCostume.SetCloseEvent(self.CloseCostumeWindow)
				self.UpdateCostumePosition()
			if self.wndCombinedCostume.IsShow():
				self.wndCombinedCostume.Hide()
				return
			self.wndCombinedCostume.Show()
			self.wndCombinedCostume.SetTop()
		else:
			if not self.wndCostume:
				self.wndCostume = CostumeWindow(self)
				self.wndCostume.SetCloseEvent(self.CloseCostumeWindow)
				self.UpdateCostumePosition()

			if not self.wndShining:
				self.wndShining = ShiningWindow(self)
				self.wndShining.SetCloseEvent(self.CloseCostumeWindow)
				self.UpdateCostumePosition()

			if app.ENABLE_SKIN_SYSTEM:
				if not self.wndSkinSystem:
					self.wndSkinSystem = SkinSystemWindow(self)
					self.wndSkinSystem.SetCloseEvent(self.CloseCostumeWindow)
					self.UpdateCostumePosition()


			if self.wndCostume.IsShow():
				self.wndCostume.Hide()
				self.wndShining.Hide()
				return
			self.wndShining.Show()
			self.wndShining.SetTop()

			self.wndCostume.Show()
			self.wndCostume.SetTop()

			if app.ENABLE_SKIN_SYSTEM:
				self.wndSkinSystem.Show()
				self.wndSkinSystem.SetTop()

	def CloseCostumeWindow(self):
		if constInfo.USE_COMBINED_CUSTOME_WINDOW:
			self.wndCombinedCostume.Hide()
		else:
			self.wndCostume.Hide()
			if self.wndShining:
				self.wndShining.Hide()

			if app.ENABLE_SKIN_SYSTEM:
				if self.wndSkinSystem:
					self.wndSkinSystem.Hide()

	def UpdateCostumePosition(self):
		if constInfo.USE_COMBINED_CUSTOME_WINDOW:
			if self.wndCombinedCostume:
				invX, invY = self.GetGlobalPosition()
				self.wndCombinedCostume.SetPosition(invX - self.wndCombinedCostume.GetWidth() + 4, invY + self.inventoryTab[0].GetTop())
		else:
			if self.wndCostume:
				invX, invY = self.GetGlobalPosition()
				self.wndCostume.SetPosition(invX - self.wndCostume.GetWidth() + 4, invY + self.inventoryTab[0].GetTop())

			if self.wndShining:
				invX, invY = self.GetGlobalPosition()
				self.wndShining.SetPosition(invX - self.wndShining.GetWidth() + 4, invY + self.inventoryTab[0].GetTop() + 160)

			if app.ENABLE_SKIN_SYSTEM:
				if self.wndSkinSystem:
					invX, invY = self.GetGlobalPosition()
					self.wndSkinSystem.SetPosition(invX - self.wndCostume.GetWidth() - self.wndSkinSystem.GetWidth() + 8, invY + self.inventoryTab[0].GetTop())

	def __InventoryLocalSlotPosToGlobalSlotPos(self, local):

		if player.IsEquipmentSlot(local) or player.IsCostumeSlot(local):
			return local

		return self.inventoryPageIndex*player.INVENTORY_PAGE_SIZE + local

	def __InventoryGlobalSlotPosToLocalSlotPos(self, globalPos):
		return globalPos - self.inventoryPageIndex*player.INVENTORY_PAGE_SIZE

	def RefreshSingleBagSlot(self, cell):
		slotNumber = self.__InventoryGlobalSlotPosToLocalSlotPos(cell)
		if slotNumber < 0 or slotNumber >= player.INVENTORY_PAGE_SIZE:
			return

		self.__RefreshBagSlot(slotNumber)
		self.wndItem.RefreshSlot()

		if self.tooltipItem != None and self.tooltipItem.inventoryItemSlot != -1:
			self.__ShowToolTip(self.tooltipItem.inventoryItemSlot)

	def __RefreshBagSlot(self, i):
		getItemVNum=player.GetItemIndex
		getItemCount=player.GetItemCount
		setItemVNum=self.wndItem.SetItemSlot

		slotNumber = self.__InventoryLocalSlotPosToGlobalSlotPos(i)
		itemCount = getItemCount(slotNumber)
		if itemCount <= 1:
			itemCount = 0
			
		itemVnum = getItemVNum(slotNumber)
		metinSlot = [player.GetItemMetinSocket(slotNumber, socket) for socket in xrange(player.METIN_SOCKET_MAX_NUM)]
		setItemVNum(i, itemVnum, itemCount, metinSlot)

		if itemVnum > 0:
			item.SelectItem(1, 2, itemVnum)

		self.wndItem.SetUnusableSlot(i, False)
		if exchange.isTrading():
			if uiExchange.EXCHANGE_TRADING_SLOT.has_key(slotNumber):
				self.wndItem.SetUnusableSlot(i)
			elif itemVnum > 0 and item.IsAntiFlag(item.ANTIFLAG_GIVE):
				self.wndItem.SetUnusableSlot(i)

		# ENABLE_MARK_NEW_ITEM_SYSTEM
		if itemVnum == 0 and slotNumber in self.liHighlightedItems:
			self.liHighlightedItems.remove(slotNumber)
		# ENABLE_MARK_NEW_ITEM_SYSTEM

		## �ڵ����� (#72723, #72724) Ư��ó�� - �������ε��� ���Կ� Ȱ��ȭ/��Ȱ��ȭ ǥ�ø� ���� �۾��� - [hyo]
		#if constInfo.IS_AUTO_POTION(itemVnum):
		#	# metinSocket - [0] : Ȱ��ȭ ����, [1] : ����� ��, [2] : �ִ� �뷮
		#	metinSocket = [player.GetItemMetinSocket(slotNumber, j) for j in xrange(player.METIN_SOCKET_MAX_NUM)]	
		#	
		#	if 0 != int(metinSocket[0]):
		#		self.wndItem.ActivateSlot(i)
		#	else:
		#		self.wndItem.DeactivateSlot(i)

		if constInfo.IS_AUTO_POTION(itemVnum):

			metinSocket = [player.GetItemMetinSocket(slotNumber, j) for j in xrange(player.METIN_SOCKET_MAX_NUM)]
			if slotNumber >= player.INVENTORY_PAGE_SIZE:
				slotNumber -= player.INVENTORY_PAGE_SIZE

			isActivated = 0 != metinSocket[0]

			if isActivated:
				self.wndItem.ActivateSlot(i)
				potionType = 0
				if constInfo.IS_AUTO_POTION_HP(itemVnum):
					potionType = player.AUTO_POTION_TYPE_HP
				elif constInfo.IS_AUTO_POTION_SP(itemVnum):
					potionType = player.AUTO_POTION_TYPE_SP
					
				usedAmount = int(metinSocket[1])
				totalAmount = int(metinSocket[2])
				player.SetAutoPotionInfo(potionType, isActivated, (totalAmount - usedAmount), totalAmount, self.__InventoryLocalSlotPosToGlobalSlotPos(i))
				
			else:
				self.wndItem.DeactivateSlot(slotNumber)

		if constInfo.INFINITY_ITEMS and constInfo.IS_INFINITY_ITEMS(itemVnum):
			metinSocket = [player.GetItemMetinSocket(slotNumber, j) for j in xrange(player.METIN_SOCKET_MAX_NUM)]
			if slotNumber >= player.INVENTORY_PAGE_SIZE:
				slotNumber -= player.INVENTORY_PAGE_SIZE

			isActivated = 1 == metinSocket[2]

			if isActivated:
				self.wndItem.ActivateSlot(i)
			else:
				self.wndItem.DeactivateSlot(slotNumber)

		if itemVnum > 0:
			if item.ITEM_TYPE_PET == item.GetItemType(): # Pet item highlighted if out
				metinSocket = [player.GetItemMetinSocket(slotNumber, j) for j in xrange(player.METIN_SOCKET_MAX_NUM)]
				isActivated = 0 != metinSocket[1]
				if isActivated:
					self.wndItem.ActivateSlot(i)
				else:
					self.wndItem.DeactivateSlot(i)

			elif item.ITEM_TYPE_MOUNT == item.GetItemType(): # Mount item highlighted if out
				metinSocket = [player.GetItemMetinSocket(slotNumber, j) for j in xrange(player.METIN_SOCKET_MAX_NUM)]
				isActivated = 0 != metinSocket[2]
				if isActivated:
					self.wndItem.ActivateSlot(i)
				else:
					self.wndItem.DeactivateSlot(i)

		if slotNumber in self.liAcceItems or slotNumber in self.slotActive:
			self.wndItem.ActivateSlot(self.__InventoryGlobalSlotPosToLocalSlotPos(slotNumber), wndMgr.COLOR_TYPE_GREEN)

	def RefreshBagSlotWindow(self):

		for i in xrange(player.INVENTORY_PAGE_SIZE):
			self.__RefreshBagSlot(i)

		# ENABLE_MARK_NEW_ITEM_SYSTEM		
		self.__RefreshHighlights()
		# ENABLE_MARK_NEW_ITEM_SYSTEM

		self.wndItem.RefreshSlot()

	def ActivateAcceSlot(self, slotPos):
		self.liAcceItems.append(slotPos)
		self.wndItem.ActivateSlot(self.__InventoryGlobalSlotPosToLocalSlotPos(slotPos), wndMgr.COLOR_TYPE_GREEN)

	def DeactivateAcceSlot(self, slotPos):
		self.liAcceItems.remove(slotPos)
		self.wndItem.DeactivateSlot(self.__InventoryGlobalSlotPosToLocalSlotPos(slotPos))

	def RefreshEquipSlotWindow(self):
		getItemVNum=player.GetItemIndex
		getItemCount=player.GetItemCount
		setItemVNum=self.wndEquip.SetItemSlot
		for i in xrange(player.EQUIPMENT_PAGE_COUNT):
			slotNumber = player.EQUIPMENT_SLOT_START + i
			itemCount = getItemCount(slotNumber)
			if itemCount <= 1:
				itemCount = 0
			setItemVNum(slotNumber, getItemVNum(slotNumber), itemCount)

		self.wndEquip.RefreshSlot()

		if constInfo.USE_COMBINED_CUSTOME_WINDOW:
			if self.wndCombinedCostume:
				self.wndCombinedCostume.RefreshCostumeSlot()
		else:
			if self.wndCostume:
				self.wndCostume.RefreshCostumeSlot()

			if self.wndShining:
				self.wndShining.RefreshShiningSlot()

			if app.ENABLE_SKIN_SYSTEM:
				if self.wndSkinSystem:
					self.wndSkinSystem.RefreshCostumeSlot()

	def RefreshItemSlot(self):
		self.RefreshBagSlotWindow()
		self.RefreshEquipSlotWindow()

	def SetItemToolTip(self, tooltipItem):
		self.tooltipItem = tooltipItem
		self.tooltipItem.inventoryItemSlot = -1

	def SellItem(self):

		net.SendShopSellPacketNew(self.sellingSlotNumber, self.questionDialog.count)
		snd.PlaySound("sound/ui/money.wav")
		self.OnCloseQuestionDialog()

	def OnDetachMetinFromItem(self):
		if None == self.questionDialog:
			return
			
		#net.SendItemUseToItemPacket(self.questionDialog.sourcePos, self.questionDialog.targetPos)		
		self.__SendUseItemToItemPacket(self.questionDialog.sourcePos, self.questionDialog.targetPos)
		self.OnCloseQuestionDialog()

	def OnCloseQuestionDialog(self):
		if self.questionDialog:
			self.questionDialog.Close()

		self.questionDialog = None

	## Slot Event
	def SelectEmptySlot(self, selectedSlotPos):
		if constInfo.GET_ITEM_DROP_QUESTION_DIALOG_STATUS() == 1:
			return

		selectedSlotPos = self.__InventoryLocalSlotPosToGlobalSlotPos(selectedSlotPos)

		if mouseModule.mouseController.isAttached():

			attachedSlotType = mouseModule.mouseController.GetAttachedType()
			attachedSlotPos = mouseModule.mouseController.GetAttachedSlotNumber()
			attachedItemCount = mouseModule.mouseController.GetAttachedItemCount()
			attachedItemIndex = mouseModule.mouseController.GetAttachedItemIndex()

			#player.ENABLE_COSTUME_INVENTORY and Type == player.SLOT_TYPE_COSTUME_INVENTORY

			inventoryList = (player.SLOT_TYPE_INVENTORY, player.SLOT_TYPE_DRAGON_SOUL_INVENTORY, player.SLOT_TYPE_SKILLBOOK_INVENTORY, player.SLOT_TYPE_UPPITEM_INVENTORY, player.SLOT_TYPE_STONE_INVENTORY, player.SLOT_TYPE_ENCHANT_INVENTORY, player.SLOT_TYPE_COSTUME_INVENTORY)
			inventoryList2 = (player.SLOT_TYPE_SKILLBOOK_INVENTORY, player.SLOT_TYPE_UPPITEM_INVENTORY, player.SLOT_TYPE_STONE_INVENTORY, player.SLOT_TYPE_ENCHANT_INVENTORY, player.SLOT_TYPE_COSTUME_INVENTORY)

			if attachedSlotType in inventoryList:
				itemCount = player.GetItemCount(attachedSlotPos)
				attachedCount = mouseModule.mouseController.GetAttachedItemCount()
				if attachedSlotType == player.SLOT_TYPE_DRAGON_SOUL_INVENTORY:
					self.__SendSpecificMoveItemPacket(player.DRAGON_SOUL_INVENTORY, attachedSlotPos, player.INVENTORY, selectedSlotPos, attachedCount)
				elif attachedSlotType in inventoryList2:
					self.__SendSpecificMoveItemPacket(player.GetWindowBySlot(attachedSlotPos), attachedSlotPos, player.INVENTORY, selectedSlotPos, attachedCount)
				else:
					self.__SendMoveItemPacket(attachedSlotPos, selectedSlotPos, attachedCount)

				if item.IsRefineScroll(attachedItemIndex):
					self.wndItem.SetUseMode(False)

			elif player.SLOT_TYPE_PRIVATE_SHOP == attachedSlotType or player.SLOT_TYPE_AUCTION_SHOP == attachedSlotType:
				mouseModule.mouseController.RunCallBack("INVENTORY",selectedSlotPos)

			elif player.SLOT_TYPE_SHOP == attachedSlotType:
				net.SendShopBuyPacket(attachedSlotPos)

			elif player.SLOT_TYPE_SAFEBOX == attachedSlotType:

				if player.ITEM_MONEY == attachedItemIndex:
					net.SendSafeboxWithdrawMoneyPacket(mouseModule.mouseController.GetAttachedItemCount())
					snd.PlaySound("sound/ui/money.wav")

				else:
					net.SendSafeboxCheckoutPacket(attachedSlotPos, selectedSlotPos)

			elif player.SLOT_TYPE_GUILD_SAFEBOX == attachedSlotType:
				net.SendGuildSafeboxCheckoutPacket(attachedSlotPos, selectedSlotPos)

			elif player.SLOT_TYPE_MALL == attachedSlotType:
				net.SendMallCheckoutPacket(attachedSlotPos, selectedSlotPos)

			mouseModule.mouseController.DeattachObject()

	def IsAcceWindowOpen( self ):
		return ( self.interface.wndAcce and self.interface.wndAcce.IsShow( ) )

	def IsShopBuilderWindowOpen( self ):
		return ( self.interface.privateShopBuilder and self.interface.privateShopBuilder.IsShow( ) )

	def IsMyAuctionShopWindowOpen( self ):
		return ( self.interface.wndAuctionShop and self.interface.wndAuctionShop.IsShow( ) )
		#return ( self.interface.dlgShop and self.interface.dlgShop.IsShow( ) and self.interface.dlgShop.isMyAuctionShop )

	def TooManyWindowsOpenedError( self ):
		chat.AppendChat( chat.CHAT_TYPE_INFO, "Too many windows opened to use the quick item-move function." )

	def NoEmptySpaceError( self ):
		chat.AppendChat( chat.CHAT_TYPE_INFO, "There is not any empty space!" )

	def ItemIsSash( self, itype, isubtype ):
		return ( itype == item.ITEM_TYPE_COSTUME and ( isubtype == item.COSTUME_TYPE_ACCE or isubtype == item.COSTUME_TYPE_ACCE_COSTUME ) )

	def GetFreeItemSlotInShop( self, getItemInfo, height ):
		
		maxItemCount = auction.SHOP_SLOT_COUNT
		itemInSlot = [ False ] * maxItemCount

		xCount = 10

		for i in xrange( maxItemCount ):
			itemVnum, itemCount, itemPrice = getItemInfo( i )

			item.SelectItem(1, 2, itemVnum )
			itemSize = item.GetItemSize( )

			if itemVnum:
				itemInSlot[ i ] = True

				# height > 1
				if itemSize[ 1 ] > 1:

					for x in xrange( itemSize[ 1 ] - 1 ):
						appendSlot = i + ( xCount * ( x + 1 ) )
						itemInSlot[ appendSlot ] = True

		for i in xrange( maxItemCount ):

			curSlot = itemInSlot[ i ]

			if not curSlot:
				
				if height > 1:
					
					appendSlotsFree = [ False ] * ( height - 1 )
						
					# fix index out of list
					if i > maxItemCount - ( xCount * ( height - 1 ) ) - 1:
						return -1

					for x in xrange( height - 1 ):
						appendSlot = i + ( xCount * ( x + 1 ) )
						
						if itemInSlot[ appendSlot ]:
							break

						appendSlotsFree[ x ] = True

					if appendSlotsFree == ( [ True ] * ( height - 1 ) ):
						return i

					continue

				return i

		return -1

	def GetShopBuilderItemInfo( self, i ):
		
		INVALID = ( 0, 0, 0 )

		if i > auction.SHOP_SLOT_COUNT or not self.interface.privateShopBuilder.itemStock.has_key( i ):
			return INVALID

		pos = self.interface.privateShopBuilder.itemStock[ i ]
		itemVnum = player.GetItemIndex( *pos )

		# we dont need these...
		itemCount = -1
		itemPrice = -1

		return ( itemVnum, itemCount, itemPrice )

	def SelectItemSlot(self, itemSlotIndex):
		if constInfo.GET_ITEM_DROP_QUESTION_DIALOG_STATUS() == 1:
			return

		itemSlotIndex = self.__InventoryLocalSlotPosToGlobalSlotPos(itemSlotIndex)

		if mouseModule.mouseController.isAttached():
			attachedSlotType = mouseModule.mouseController.GetAttachedType()
			attachedSlotPos = mouseModule.mouseController.GetAttachedSlotNumber()
			attachedItemVID = mouseModule.mouseController.GetAttachedItemIndex()

			if player.SLOT_TYPE_INVENTORY == attachedSlotType or \
				player.SLOT_TYPE_STONE_INVENTORY == attachedSlotType or \
				player.SLOT_TYPE_ENCHANT_INVENTORY == attachedSlotType or \
				player.SLOT_TYPE_COSTUME_INVENTORY == attachedSlotType:
				self.__DropSrcItemToDestItemInInventory(attachedItemVID, attachedSlotPos, itemSlotIndex)

			mouseModule.mouseController.DeattachObject()

		else:

			curCursorNum = app.GetCursor()
			if app.SELL == curCursorNum:
				if app.IsPressed(app.DIK_LCONTROL) or app.IsPressed(app.DIK_RCONTROL):
					item.SelectItem(1, 2, player.GetItemIndex(itemSlotIndex))
					if item.IsAntiFlag(item.ITEM_ANTIFLAG_SELL) or player.IsEquipmentSlot(itemSlotIndex):
						chat.AppendChat(chat.CHAT_TYPE_INFO, localeInfo.CANNOT_SELL_ITEM_ANTIFLAG)
						return

					if itemSlotIndex in self.sellingItemList:
						self.sellingItemList.remove(itemSlotIndex)
					else:
						self.sellingItemList.append(itemSlotIndex)
					self.__RefreshSlotHighlight(itemSlotIndex)

				else:
					self.__SellItem(itemSlotIndex)
				
			elif app.BUY == curCursorNum:
				chat.AppendChat(chat.CHAT_TYPE_INFO, localeInfo.SHOP_BUY_INFO)

			elif app.IsPressed(app.DIK_LALT):
				link = player.GetItemLink(itemSlotIndex)
				ime.PasteString(link)

			elif app.IsPressed(app.DIK_LSHIFT):
				itemCount = player.GetItemCount(itemSlotIndex)
				
				if __SERVER__ == 2:
					braveCape = player.GetItemIndex(itemSlotIndex) == 93359 and player.GetItemMetinSocket(itemSlotIndex, 0)
					if itemCount > 1 or braveCape:
						self.dlgSplitItem.SetTitleName(localeInfo.PICK_ITEM_TITLE)
						self.dlgSplitItem.SetAcceptEvent(ui.__mem_func__(self.OnSplitItem))
						self.dlgSplitItem.Open(itemCount if not braveCape else player.GetItemMetinSocket(itemSlotIndex, 0))
						self.dlgSplitItem.itemGlobalSlotIndex = itemSlotIndex
				else:
					if itemCount > 1:
						self.dlgSplitItem.SetTitleName(localeInfo.PICK_ITEM_TITLE)
						self.dlgSplitItem.SetAcceptEvent(ui.__mem_func__(self.OnSplitItem))
						self.dlgSplitItem.Open(itemCount)
						self.dlgSplitItem.itemGlobalSlotIndex = itemSlotIndex

				#else:
					#selectedItemVNum = player.GetItemIndex(itemSlotIndex)
					#mouseModule.mouseController.AttachObject(self, player.SLOT_TYPE_INVENTORY, itemSlotIndex, selectedItemVNum)

			else:
				if not player.IsEquipmentSlot(itemSlotIndex) and not player.IsCostumeSlot(itemSlotIndex) and (app.IsPressed(app.DIK_LCONTROL) or app.IsPressed(app.DIK_RCONTROL)):
					if self.eventCTRLClickItem and self.eventCTRLClickItem(itemSlotIndex):
						return

				if (app.IsPressed(app.DIK_LCONTROL) or app.IsPressed(app.DIK_RCONTROL)):

					itemIndex = player.GetItemIndex( itemSlotIndex )

					# -- fast move function
					if constInfo.FAST_ITEM_MOVE:
						blockInput = False

						acceOpened 			= self.IsAcceWindowOpen( )
						privateShopOpened 	= self.IsShopBuilderWindowOpen( )
						auctionShopOpened 	= self.IsMyAuctionShopWindowOpen( )
						inShop 				= ( privateShopOpened or auctionShopOpened )

						if acceOpened or inShop:
							blockInput = True

						# check if too many windows opened
						if ( acceOpened and inShop ) or ( privateShopOpened and auctionShopOpened ):
							return self.TooManyWindowsOpenedError( )

						item.SelectItem(1, 2, itemIndex )

						itemType 	= item.GetItemType( )
						itemSubType = item.GetItemSubType( )
						itemCount 	= player.GetItemCount( player.SLOT_TYPE_INVENTORY, itemSlotIndex )

						# combine window opened...
						if acceOpened and self.interface.wndAcce.windowType == 1:

							if not self.ItemIsSash( itemType, itemSubType ):
								chat.AppendChat( chat.CHAT_TYPE_INFO, "This item is not a sash!" )
								return

							# item is sash, put it.
							# i think theres no need to check slot type etc. because i use mouse.AttachObject so OnSelectEmptySlot does everything for me...

							firstSlot = player.GetAcceItemID( 0 )
							secondSlot = player.GetAcceItemID( 1 )

							# slots are occupied!
							if firstSlot and secondSlot:
								return self.NoEmptySpaceError( )

							# first slot is free!
							if not firstSlot:
								mouseModule.mouseController.AttachObject( self, player.SLOT_TYPE_INVENTORY, itemSlotIndex, itemIndex, itemCount )
								self.interface.wndAcce.SelectEmptySlot( 0 )
								return

							# second slot is free!
							if not secondSlot:
								mouseModule.mouseController.AttachObject( self, player.SLOT_TYPE_INVENTORY, itemSlotIndex, itemIndex, itemCount )
								self.interface.wndAcce.SelectEmptySlot( 1 )
								return

						if inShop:

							item.SelectItem(1, 2, itemIndex )
							itemCount = player.GetItemCount( player.SLOT_TYPE_INVENTORY, itemSlotIndex )
							itemSize = item.GetItemSize( )

							if privateShopOpened:

								getItemInfo = self.GetShopBuilderItemInfo
								freeSlot = self.GetFreeItemSlotInShop( getItemInfo, itemSize[ 1 ] )
								
								if freeSlot == -1:
									return self.NoEmptySpaceError( )

								mouseModule.mouseController.AttachObject( self, player.SLOT_TYPE_INVENTORY, itemSlotIndex, itemIndex, itemCount )
								self.interface.privateShopBuilder.OnSelectEmptySlot( freeSlot )

							if auctionShopOpened:

								if constInfo.FAST_MOVE_ITEM_COOLDOWN:
									if app.GetGlobalTime() - self.fastMoveAuctionShopItem > 1000:
										self.fastMoveAuctionShopItem = app.GetGlobalTime()
									else:
										return

								getItemInfo = lambda slot: auction.GetItemInfo(auction.CONTAINER_OWNED_SHOP, auction.GetItemIndexByCell(slot))
								freeSlot = self.GetFreeItemSlotInShop( getItemInfo, itemSize[ 1 ] )

								if freeSlot == -1:
									return self.NoEmptySpaceError( )

								mouseModule.mouseController.AttachObject( self, player.SLOT_TYPE_INVENTORY, itemSlotIndex, itemIndex, itemCount )
								self.interface.wndAuctionShop.SelectEmptySlot( freeSlot )

						if not blockInput:
							if True == item.CanAddToQuickSlotItem(itemIndex):
								player.RequestAddToEmptyLocalQuickSlot(player.SLOT_TYPE_INVENTORY, itemSlotIndex)
							else:
								chat.AppendChat(chat.CHAT_TYPE_INFO, localeInfo.QUICKSLOT_REGISTER_DISABLE_ITEM)

						# -- end of fast move
					else:
						if True == item.CanAddToQuickSlotItem(itemIndex):
							player.RequestAddToEmptyLocalQuickSlot(player.SLOT_TYPE_INVENTORY, itemSlotIndex)
						else:
							chat.AppendChat(chat.CHAT_TYPE_INFO, localeInfo.QUICKSLOT_REGISTER_DISABLE_ITEM)
				else:

					selectedItemVNum = player.GetItemIndex(itemSlotIndex)
					itemCount = player.GetItemCount(itemSlotIndex)
					mouseModule.mouseController.AttachObject(self, player.SLOT_TYPE_INVENTORY, itemSlotIndex, selectedItemVNum, itemCount)
					
					if self.__IsUsableItemToItem(selectedItemVNum, itemSlotIndex):				
						self.wndItem.SetUseMode(True)
					else:					
						self.wndItem.SetUseMode(False)

					snd.PlaySound("sound/ui/pick.wav")

	def OnSplitItem(self, count, full_split):
		tchat("OnSplitItem count %d full_split %d slot %d" % (count, full_split, self.dlgSplitItem.itemGlobalSlotIndex))
		if full_split:
			item_vnum = player.GetItemIndex(self.dlgSplitItem.itemGlobalSlotIndex)
			if __SERVER__ == 2:
				item_count = player.GetItemCount(self.dlgSplitItem.itemGlobalSlotIndex) if item_vnum != 93359 else player.GetItemMetinSocket(self.dlgSplitItem.itemGlobalSlotIndex, 0)
			else:
				item_count = player.GetItemCount(self.dlgSplitItem.itemGlobalSlotIndex)
			item.SelectItem(1, 2, item_vnum)
			itemWidth, itemHeight = item.GetItemSize()
			emptyPos = 0
			pageCount = 1

			tchat("item_count / count %d" % (item_count / count))
			for x in xrange(item_count / count):
				emptyPos = self.GetEmptyItemPos(itemHeight, emptyPos)
				tchat("x %d .. empty %d count %d" % (x, emptyPos, count))
				if emptyPos == -1:
					return
				self.__SendMoveItemPacket(self.dlgSplitItem.itemGlobalSlotIndex, emptyPos, count)
			emptyPos = self.GetEmptyItemPos(itemHeight, emptyPos)
			self.__SendMoveItemPacket(self.dlgSplitItem.itemGlobalSlotIndex, emptyPos, count)
		else:
			self.OnPickItem(count)

	if constInfo.BRAVERY_CAPE_STORE:
		def AddCapeToBox(self):
			self.__SendUseItemToItemPacket(self.questionDialog.src, self.questionDialog.dst)
			self.OnCloseQuestionDialog()

		def IsBraveryCape(self, vnum):
			return vnum in [ 70038, 70057, 76007, 93004 ]

	def __DropSrcItemToDestItemInInventory(self, srcItemVID, srcItemSlotPos, dstItemSlotPos):
		dstItemVID = player.GetItemIndex(dstItemSlotPos)

		item.SelectItem(1, 2, srcItemVID)
		src_type = item.GetItemType()
		src_sub_type = item.GetItemSubType()

		if srcItemSlotPos == dstItemSlotPos:
			return


		if dstItemVID == srcItemVID:
			if player.IsEquipmentSlot(dstItemSlotPos):
				if item.IsEquipmentVID(srcItemVID):
					self.__UseItem(srcItemSlotPos)
			else:
				self.__SendMoveItemPacket(srcItemSlotPos, dstItemSlotPos, 0)


		if constInfo.BRAVERY_CAPE_STORE:
			if self.IsBraveryCape(srcItemVID) and player.GetItemIndex(dstItemSlotPos) == 93359:
				self.questionDialog = uiCommon.QuestionDialog()
				self.questionDialog.SetText(localeInfo.STORE_CAPE_ADD_CAPES)
				self.questionDialog.SetAcceptEvent(ui.__mem_func__(self.AddCapeToBox))
				self.questionDialog.SetCancelEvent(ui.__mem_func__(self.OnCloseQuestionDialog))
				self.questionDialog.Open()
				self.questionDialog.src = srcItemSlotPos
				self.questionDialog.dst = dstItemSlotPos
				return

		if srcItemVID >= 95300 and srcItemVID <= 95309 and player.GetItemIndex(dstItemSlotPos) == 95310:
			self.__SendUseItemToItemPacket(srcItemSlotPos, dstItemSlotPos)
			return

		if item.IsRefineScroll(srcItemVID) and srcItemVID != dstItemVID: # bugfix stack scrolls
			self.RefineItem(srcItemSlotPos, dstItemSlotPos)
			self.wndItem.SetUseMode(False)

		elif item.IsMetin(srcItemVID) and player.GetItemIndex(dstItemSlotPos) != srcItemVID and not item.IsMetin(dstItemVID):
			self.AttachMetinToItem(srcItemSlotPos, dstItemSlotPos)

		elif item.IsDetachScroll(srcItemVID):
			item.SelectItem(1, 2, srcItemVID)
			if item.GetItemSubType() == item.USE_DETACH_STONE:
				self.DetachSingleMetinFromItem(srcItemSlotPos, dstItemSlotPos)
			elif item.GetItemSubType() == item.USE_DETACH_ATTR:
				self.RemoveSingleAttrFromItem(srcItemSlotPos, dstItemSlotPos)
			else:
				self.DetachMetinFromItem(srcItemSlotPos, dstItemSlotPos)

		elif item.IsArrow(srcItemVID) and item.IsQuiver(player.GetItemIndex(dstItemSlotPos)):
			self.__SendUseItemToItemPacket(srcItemSlotPos, dstItemSlotPos)

		elif item.IsKey(srcItemVID):
			self.__SendUseItemToItemPacket(srcItemSlotPos, dstItemSlotPos)			

		elif (player.GetItemFlags(srcItemSlotPos) & ITEM_FLAG_APPLICABLE) == ITEM_FLAG_APPLICABLE:
			self.__SendUseItemToItemPacket(srcItemSlotPos, dstItemSlotPos)

		elif item.GetUseType(srcItemVID) in self.USE_TYPE_TUPLE:
			self.__SendUseItemToItemPacket(srcItemSlotPos, dstItemSlotPos)			

		elif constInfo.ENABLE_CRYSTAL_SYSTEM and src_type == item.ITEM_TYPE_CRYSTAL and src_sub_type in (item.CRYSTAL_UPGRADE_SCROLL, item.CRYSTAL_TIME_ELIXIR) and item.IsActiveCrystal(dstItemVID):
			self.__SendUseItemToItemPacket(srcItemSlotPos, dstItemSlotPos)

		else:
			#snd.PlaySound("sound/ui/drop.wav")

			## �̵���Ų ���� ���� ������ ��� �������� ����ؼ� ���� ��Ų�� - [levites]
			if player.IsEquipmentSlot(dstItemSlotPos):

				## ��� �ִ� �������� ����϶���
				if item.IsEquipmentVID(srcItemVID):
					self.__UseItem(srcItemSlotPos)

			else:
				self.__SendMoveItemPacket(srcItemSlotPos, dstItemSlotPos, 0)
				#net.SendItemMovePacket(srcItemSlotPos, dstItemSlotPos, 0)

	def __SellMultiItem(self):
		itemPrice = 0
		itemCount = 0

		if len(self.sellingItemList) == 1:
			slotNumber = self.sellingItemList[0]
			self.sellingItemList = []
			
			self.__SellItem(slotNumber)
			self.__RefreshSlotHighlight(slotNumber)
			return

		for itemSlotPos in self.sellingItemList:
			curItemCount = player.GetItemCount(itemSlotPos)
			curItemPrice = player.GetIBuyItemPrice(itemSlotPos) / 5

			itemPrice += curItemPrice
			itemPrice -= curItemPrice * 3 / 100
			itemCount += curItemCount

		self.questionDialog = uiCommon.QuestionDialog()
		self.questionDialog.SetText(localeInfo.DO_YOU_SELL_MULTI_ITEM(len(self.sellingItemList), itemCount, itemPrice))
		self.questionDialog.SetAcceptEvent(ui.__mem_func__(self.SellMultiItem))
		self.questionDialog.SetCancelEvent(ui.__mem_func__(self.OnCloseMultiQuestionDialog))
		self.questionDialog.Open()
		
		constInfo.SET_ITEM_DROP_QUESTION_DIALOG_STATUS(1)

	def SellMultiItem(self):
		for slot in self.sellingItemList:
			tchat("%d" % slot)
			if slot >= 254: # Hotfix for BYTE issue selling stones from storage
				popup = uiCommon.PopupDialog()
				popup.SetText("Use your inventory to sell this item.")
				popup.SetAcceptEvent(self.__OnClosePopupDialog)
				popup.Open()
				self.popup = popup
				return
			net.SendShopSellPacketNew(slot, player.GetItemCount(slot))
		snd.PlaySound("sound/ui/money.wav")
		self.OnCloseMultiQuestionDialog()

	def OnCloseMultiQuestionDialog(self):
		if not self.questionDialog:
			return
		
		self.questionDialog.Close()
		self.questionDialog = None

		tempList = self.sellingItemList
		self.sellingItemList = []
		for slotIndex in tempList:
			self.wndItem.DeactivateSlot(slotIndex)

		constInfo.SET_ITEM_DROP_QUESTION_DIALOG_STATUS(0)

	def __SellItem(self, itemSlotPos):
		if not player.IsEquipmentSlot(itemSlotPos):
			self.sellingSlotNumber = itemSlotPos
			itemIndex = player.GetItemIndex(itemSlotPos)
			itemCount = player.GetItemCount(itemSlotPos)

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

	def RefineItem(self, scrollSlotPos, targetSlotPos):

		scrollIndex = player.GetItemIndex(scrollSlotPos)
		targetIndex = player.GetItemIndex(targetSlotPos)

		if player.REFINE_OK != player.CanRefine(scrollIndex, targetSlotPos):
			return

		###########################################################
		self.__SendUseItemToItemPacket(scrollSlotPos, targetSlotPos)
		#net.SendItemUseToItemPacket(scrollSlotPos, targetSlotPos)
		return
		###########################################################

		###########################################################
		#net.SendRequestRefineInfoPacket(targetSlotPos)
		#return
		###########################################################

		result = player.CanRefine(scrollIndex, targetSlotPos)

		if player.REFINE_ALREADY_MAX_SOCKET_COUNT == result:
			#snd.PlaySound("sound/ui/jaeryun_fail.wav")
			chat.AppendChat(chat.CHAT_TYPE_INFO, localeInfo.REFINE_FAILURE_NO_MORE_SOCKET)

		elif player.REFINE_NEED_MORE_GOOD_SCROLL == result:
			#snd.PlaySound("sound/ui/jaeryun_fail.wav")
			chat.AppendChat(chat.CHAT_TYPE_INFO, localeInfo.REFINE_FAILURE_NEED_BETTER_SCROLL)

		elif player.REFINE_CANT_MAKE_SOCKET_ITEM == result:
			#snd.PlaySound("sound/ui/jaeryun_fail.wav")
			chat.AppendChat(chat.CHAT_TYPE_INFO, localeInfo.REFINE_FAILURE_SOCKET_DISABLE_ITEM)

		elif player.REFINE_NOT_NEXT_GRADE_ITEM == result:
			#snd.PlaySound("sound/ui/jaeryun_fail.wav")
			chat.AppendChat(chat.CHAT_TYPE_INFO, localeInfo.REFINE_FAILURE_UPGRADE_DISABLE_ITEM)

		elif player.REFINE_CANT_REFINE_METIN_TO_EQUIPMENT == result:
			chat.AppendChat(chat.CHAT_TYPE_INFO, localeInfo.REFINE_FAILURE_EQUIP_ITEM)

		if player.REFINE_OK != result:
			return

		self.refineDialog.Open(scrollSlotPos, targetSlotPos)

	def DetachSingleMetinFromItem(self, srcItemSlotPos, dstItemSlotPos):
		scrollIndex = player.GetItemIndex(srcItemSlotPos)
		if not player.CanDetach(scrollIndex, dstItemSlotPos):
			chat.AppendChat(chat.CHAT_TYPE_INFO, localeInfo.CANT_DETACH_NO_STONE)
			return

		self.detachMetinDialog.Open(srcItemSlotPos, dstItemSlotPos)

	def RemoveSingleAttrFromItem(self, srcItemSlotPos, dstItemSlotPos):
		scrollIndex = player.GetItemIndex(srcItemSlotPos)
		if not player.CanDetach(scrollIndex, dstItemSlotPos):
			chat.AppendChat(chat.CHAT_TYPE_INFO, localeInfo.CANT_DETACH_NO_ATTR)
			return

		self.removeAttrDialog.Open(srcItemSlotPos, dstItemSlotPos)

	def DetachMetinFromItem(self, scrollSlotPos, targetSlotPos):
		scrollIndex = player.GetItemIndex(scrollSlotPos)
		targetIndex = player.GetItemIndex(targetSlotPos)

		if not player.CanDetach(scrollIndex, targetSlotPos):
			chat.AppendChat(chat.CHAT_TYPE_INFO, localeInfo.REFINE_FAILURE_METIN_INSEPARABLE_ITEM)
			return

		self.questionDialog = uiCommon.QuestionDialog()
		self.questionDialog.SetText(localeInfo.REFINE_DO_YOU_SEPARATE_METIN)
		self.questionDialog.SetAcceptEvent(ui.__mem_func__(self.OnDetachMetinFromItem))
		self.questionDialog.SetCancelEvent(ui.__mem_func__(self.OnCloseQuestionDialog))
		self.questionDialog.Open()
		self.questionDialog.sourcePos = scrollSlotPos
		self.questionDialog.targetPos = targetSlotPos

	def AttachMetinToItem(self, metinSlotPos, targetSlotPos):
		metinIndex = player.GetItemIndex(metinSlotPos)
		targetIndex = player.GetItemIndex(targetSlotPos)

		item.SelectItem(1, 2, metinIndex)
		itemName = item.GetItemName()

		result = player.CanAttachMetin(metinIndex, targetSlotPos)

		if player.ATTACH_METIN_NOT_MATCHABLE_ITEM == result:
			chat.AppendChat(chat.CHAT_TYPE_INFO, localeInfo.REFINE_FAILURE_CAN_NOT_ATTACH(itemName))

		if player.ATTACH_METIN_NO_MATCHABLE_SOCKET == result:
			chat.AppendChat(chat.CHAT_TYPE_INFO, localeInfo.REFINE_FAILURE_NO_SOCKET(itemName))

		elif player.ATTACH_METIN_NOT_EXIST_GOLD_SOCKET == result:
			chat.AppendChat(chat.CHAT_TYPE_INFO, localeInfo.REFINE_FAILURE_NO_GOLD_SOCKET(itemName))

		elif player.ATTACH_METIN_CANT_ATTACH_TO_EQUIPMENT == result:
			chat.AppendChat(chat.CHAT_TYPE_INFO, localeInfo.REFINE_FAILURE_EQUIP_ITEM)

		if player.ATTACH_METIN_OK != result:
			return

		self.attachMetinDialog.Open(metinSlotPos, targetSlotPos)


		
	def OverOutItem(self):
		self.wndItem.SetUsableItem(False)
		# ENABLE_ITEM_SWAP_SYSTEM
		self.wndItem.SetUsableItem2(False)
		# ENABLE_ITEM_SWAP_SYSTEM
		if None != self.tooltipItem:
			self.tooltipItem.inventoryItemSlot = -1
			self.tooltipItem.HideToolTip()

	def OverInItem(self, overSlotPos):
		overSlotPosGlobal = self.__InventoryLocalSlotPosToGlobalSlotPos(overSlotPos)
		self.wndItem.SetUsableItem(False)
		# ENABLE_ITEM_SWAP_SYSTEM
		self.wndItem.SetUsableItem2(False)
		# ENABLE_ITEM_SWAP_SYSTEM
		
		if overSlotPosGlobal in self.liHighlightedItems:
			self.liHighlightedItems.remove(overSlotPosGlobal)
			self.wndItem.DeactivateSlot(overSlotPos)

		if mouseModule.mouseController.isAttached():
			attachedItemType = mouseModule.mouseController.GetAttachedType()
			if player.SLOT_TYPE_INVENTORY == attachedItemType or \
				player.SLOT_TYPE_STONE_INVENTORY == attachedItemType or \
				player.SLOT_TYPE_ENCHANT_INVENTORY == attachedItemType or \
				player.SLOT_TYPE_COSTUME_INVENTORY == attachedItemType:

				attachedSlotPos = mouseModule.mouseController.GetAttachedSlotNumber()
				attachedItemVNum = mouseModule.mouseController.GetAttachedItemIndex()
				
				if self.__CanUseSrcItemToDstItem(attachedItemVNum, attachedSlotPos, overSlotPosGlobal):
					self.wndItem.SetUsableItem(True)
					self.__ShowToolTip(overSlotPosGlobal)
					return
				# ENABLE_ITEM_SWAP_SYSTEM
				else:
					srcItem = player.GetItemIndex(attachedSlotPos)
					item.SelectItem(1, 2, srcItem)
					item1_size = str(item.GetItemSize())
					
					dstItem = player.GetItemIndex(overSlotPosGlobal)
					item.SelectItem(1, 2, dstItem)
					item2_size = str(item.GetItemSize())
					
					if item2_size == item1_size:
						if attachedSlotPos != overSlotPosGlobal:
							self.wndItem.SetUsableItem2(True)
							self.__ShowToolTip(overSlotPosGlobal)
							return
					
					if item1_size == "(1, 2)":
						if attachedSlotPos != overSlotPosGlobal:
							if item2_size == "(1, 1)":
								second_item = player.GetItemIndex(overSlotPosGlobal+5)
								item.SelectItem(1, 2, second_item)
								second_item_size = str(item.GetItemSize())
								if second_item_size != "(1, 2)" and second_item_size != "(1, 3)":
									self.wndItem.SetUsableItem2(True)
									self.__ShowToolTip(overSlotPosGlobal)
									return
									
					if item1_size == "(1, 3)":
						if attachedSlotPos != overSlotPosGlobal:
							if item2_size == "(1, 1)":
								second_item = player.GetItemIndex(overSlotPosGlobal+5)
								item.SelectItem(1, 2, second_item)
								second_item_size = str(item.GetItemSize())
								
								if second_item_size != "(1, 3)":
									third_item = player.GetItemIndex(overSlotPosGlobal+10)
									item.SelectItem(1, 2, third_item)
									third_item_size = str(item.GetItemSize())
									
									if third_item_size != "(1, 2)" and third_item_size != "(1, 3)":
										self.wndItem.SetUsableItem2(True)
										self.__ShowToolTip(overSlotPosGlobal)
										return
							elif item2_size == "(1, 2)":
								second_item = player.GetItemIndex(overSlotPosGlobal+10)
								item.SelectItem(1, 2, second_item)
								second_item_size = str(item.GetItemSize())
								
								if second_item_size != "(1, 2)" and second_item_size != "(1, 3)":
									self.wndItem.SetUsableItem2(True)
									self.__ShowToolTip(overSlotPosGlobal)
									return
				# ENABLE_ITEM_SWAP_SYSTEM

		self.__ShowToolTip(overSlotPosGlobal)

	# ENABLE_MARK_NEW_ITEM_SYSTEM
	def HighlightSlot(self, slot):
		if not slot in self.liHighlightedItems:
			self.liHighlightedItems.append(slot)
			# import chat
			# chat.AppendChat(chat.CHAT_TYPE_INFO, "AddHighlightSlot %d" % slot)

	def SetSlotActive(self, slot, is_active):
		if is_active and slot not in self.slotActive:
			self.slotActive.append(slot)
		elif not is_active and slot in self.slotActive:
			self.slotActive.remove(slot)
		else:
			return

		localSlot = self.__InventoryGlobalSlotPosToLocalSlotPos(slot)
		if localSlot >= 0 and self.wndItem.HasSlot(localSlot):
			if is_active:
				self.wndItem.ActivateSlot(localSlot)
			else:
				self.wndItem.DeactivateSlot(localSlot)

	def __RefreshSlotHighlight(self, slot):
		localSlot = self.__InventoryGlobalSlotPosToLocalSlotPos(slot)
		if localSlot < 0 or not self.wndItem.HasSlot(localSlot):
			return

		if slot in self.liHighlightedItems or slot in self.sellingItemList:
			self.wndItem.ActivateSlot(localSlot)

	def __RefreshHighlights(self):
		if cfg.Get(cfg.SAVE_OPTION, "item_highlight", "1") == "0":
			return

		for i in xrange(player.INVENTORY_PAGE_SIZE):
			self.__RefreshSlotHighlight(i)
	# ENABLE_MARK_NEW_ITEM_SYSTEM

	def __IsUsableItemToItem(self, srcItemVNum, srcSlotPos):
		# "�ٸ� �����ۿ� ����� �� �ִ� �������ΰ�?"

		item.SelectItem(1, 2, srcItemVNum)
		item_type = item.GetItemType()
		item_sub_type = item.GetItemSubType()

		if constInfo.BRAVERY_CAPE_STORE:
			if self.IsBraveryCape(srcItemVNum):
				return True

		if item.IsRefineScroll(srcItemVNum):
			return True
		elif item.IsMetin(srcItemVNum):
			return True
		elif item.IsDetachScroll(srcItemVNum):
			return True
		elif item.IsKey(srcItemVNum):
			return True
		elif (player.GetItemFlags(srcSlotPos) & ITEM_FLAG_APPLICABLE) == ITEM_FLAG_APPLICABLE:
			return True
		elif constInfo.ENABLE_CRYSTAL_SYSTEM and item_type == item.ITEM_TYPE_CRYSTAL and item_sub_type in (item.CRYSTAL_UPGRADE_SCROLL, item.CRYSTAL_TIME_ELIXIR):
			return True
		else:
			if item.GetUseType(srcItemVNum) in self.USE_TYPE_TUPLE:
				return True
			
		return False

	def __CanUseSrcItemToDstItem(self, srcItemVNum, srcSlotPos, dstSlotPos):
		# "��� �����ۿ� ����� �� �ִ°�?"

		dstItemVID = player.GetItemIndex(dstSlotPos)

		item.SelectItem(1, 2, srcItemVNum)
		src_type = item.GetItemType()
		src_sub_type = item.GetItemSubType()

		if srcSlotPos == dstSlotPos:
			return False

		if constInfo.BRAVERY_CAPE_STORE:
			if self.IsBraveryCape(srcItemVNum) and player.GetItemIndex(dstSlotPos) == 93359:
				return True

		if item.IsRefineScroll(srcItemVNum):
			if player.REFINE_OK == player.CanRefine(srcItemVNum, dstSlotPos):
				return True
		elif item.IsMetin(srcItemVNum):
			if player.ATTACH_METIN_OK == player.CanAttachMetin(srcItemVNum, dstSlotPos) or srcItemVNum == player.GetItemIndex(dstSlotPos):
				return True
		elif item.IsArrow(srcItemVNum):
			if item.IsQuiver(player.GetItemIndex(dstSlotPos)):
				quiverArrowVnum = player.GetItemMetinSocket(dstSlotPos, 0)
				if quiverArrowVnum == 0 or quiverArrowVnum == srcItemVNum:
					return True
		elif item.IsDetachScroll(srcItemVNum):
			if player.DETACH_METIN_OK == player.CanDetach(srcItemVNum, dstSlotPos):
				return True
		elif item.IsKey(srcItemVNum):
			if player.CanUnlock(srcItemVNum, dstSlotPos):
				return True

		elif constInfo.ENABLE_CRYSTAL_SYSTEM and src_type == item.ITEM_TYPE_CRYSTAL and src_sub_type in (item.CRYSTAL_UPGRADE_SCROLL, item.CRYSTAL_TIME_ELIXIR) and item.IsActiveCrystal(dstItemVID):
			return True

		elif (player.GetItemFlags(srcSlotPos) & ITEM_FLAG_APPLICABLE) == ITEM_FLAG_APPLICABLE:
			return True

		else:
			useType=item.GetUseType(srcItemVNum)

			if "USE_CLEAN_SOCKET" == useType:
				if self.__CanCleanBrokenMetinStone(dstSlotPos):
					return True
			elif "USE_CHANGE_ATTRIBUTE" == useType:
				if self.__CanChangeItemAttrList(dstSlotPos):
					return True
			elif "USE_ADD_ATTRIBUTE" == useType:
				if self.__CanAddItemAttr(dstSlotPos):
					return True
			elif "USE_ADD_ATTRIBUTE2" == useType:
				if self.__CanAddItemAttr2(dstSlotPos):
					return True
			elif "USE_ADD_ACCESSORY_SOCKET" == useType:
				if self.__CanAddAccessorySocket(dstSlotPos):
					return True
			elif "USE_PUT_INTO_ACCESSORY_SOCKET" == useType:								
				if self.__CanPutAccessorySocket(dstSlotPos, srcItemVNum, False):
					return True;
			elif "USE_PUT_INTO_ACCESSORY_SOCKET_PERMA" == useType:								
				if self.__CanPutAccessorySocket(dstSlotPos, srcItemVNum, True):
					return True;
			elif "USE_SPECIAL" == useType:
				if self.__CanUseSpecialItemTo(srcItemVNum, dstSlotPos, player.GetItemIndex(dstSlotPos)):
					return True
			elif "USE_ADD_SPECIFIC_ATTRIBUTE" == useType:
				if self.__CanAddSpecificItemAttr(srcSlotPos, dstSlotPos):
					return True
			elif "USE_TYPE_SOUL" == useType:
				if self.__CanAddSoulToCostumeSash(srcSlotPos, dstSlotPos):
					return True
			elif "USE_CHANGE_SASH_COSTUME_ATTR" == useType:
				if self.__CanChangeSashAttrList(dstSlotPos):
					return True
			elif "USE_DEL_LAST_PERM_ORE" == useType:
				return True

		return False

	def __CanCleanBrokenMetinStone(self, dstSlotPos):
		dstItemVNum = player.GetItemIndex(dstSlotPos)
		if dstItemVNum == 0:
			return False

		item.SelectItem(1, 2, dstItemVNum)
		
		if item.ITEM_TYPE_WEAPON != item.GetItemType():
			return False

		for i in xrange(player.METIN_SOCKET_MAX_NUM):
			if player.GetItemMetinSocket(dstSlotPos, i) == constInfo.ERROR_METIN_STONE:
				return True

		return False

	def __CanChangeItemAttrList(self, dstSlotPos):
		dstItemVNum = player.GetItemIndex(dstSlotPos)
		if dstItemVNum == 0:
			return False

		item.SelectItem(1, 2, dstItemVNum)
		
		if not item.GetItemType() in (item.ITEM_TYPE_WEAPON, item.ITEM_TYPE_ARMOR, item.ITEM_TYPE_TOTEM):	 
			return False

		for i in xrange(player.NORMAL_ATTRIBUTE_SLOT_MAX_NUM):
			if player.GetItemAttribute(dstSlotPos, i) != (0, 0):
				return True

		return False

	def __CanChangeSashAttrList(self, dstSlotPos):
		dstItemVNum = player.GetItemIndex(dstSlotPos)
		if dstItemVNum == 0:
			return False

		item.SelectItem(1, 2, dstItemVNum)

		zodiacArm = [ 310, 1180, 2200, 3220, 5160, 7300 ]
		isZodiac = False
		for i in zodiacArm:
			if dstItemVNum >= i and dstItemVNum < i + 10:
				isZodiac = True
				break

		if isZodiac:
			for i in xrange(player.NORMAL_ATTRIBUTE_SLOT_MAX_NUM):
				if player.GetItemAttribute(dstSlotPos, i) != (0, 0):
					return True
			return False
		
		if item.GetItemType() != item.ITEM_TYPE_COSTUME or item.GetItemSubType() != item.COSTUME_TYPE_ACCE_COSTUME:
			return False

		for i in xrange(player.NORMAL_ATTRIBUTE_SLOT_MAX_NUM):
			if player.GetItemAttribute(dstSlotPos, i) != (0, 0):
				return True

		return False

	def __CanUseSpecialItemTo(self, srcItemVnum, dstSlotPos, dstItemVnum):
		if srcItemVnum == 39046:
			item.SelectItem(1, 2, dstItemVnum)
			if item.GetItemType() == item.ITEM_TYPE_COSTUME and item.GetItemSubType() == item.COSTUME_TYPE_ACCE:
				if player.GetItemMetinSocket(dstSlotPos, 1) != 0:
					return True

			return False

		return False

	def __CanPutAccessorySocket(self, dstSlotPos, mtrlVnum, isPerma):
		dstItemVNum = player.GetItemIndex(dstSlotPos)
		if dstItemVNum == 0:
			return False

		item.SelectItem(1, 2, dstItemVNum)

		if item.GetItemType() == item.ITEM_TYPE_ARMOR:
			if not item.GetItemSubType() in (item.ARMOR_WRIST, item.ARMOR_NECK, item.ARMOR_EAR):
				return False
		

		curCount = player.GetItemMetinSocket(dstSlotPos, 0) & 0xff
		curCount += (player.GetItemMetinSocket(dstSlotPos, 0) >> 8) & 0xff
		currType = player.GetItemMetinSocket(dstSlotPos, 0) >> 16
		if curCount == 0:
			currType = 0
		maxCount = player.GetItemMetinSocket(dstSlotPos, 1)

		specialOres = constInfo.GET_ACCESSORY_MATERIAL_VNUM_BY_TYPE(dstItemVNum, currType, item.GetItemType())
		checkVnum = constInfo.GET_ACCESSORY_MATERIAL_VNUM(dstItemVNum, item.GetItemSubType())
		if item.GetItemType() == item.ITEM_TYPE_BELT:
			if currType:
				isPerma = True
				repl = []
				for i in specialOres:
					if i != 18900:
						repl.append(i)
				specialOres = repl
			elif curCount:
				isPerma = False
				specialOres = [18900]
		if isPerma:
			checkVnum = checkVnum[1]
		else:
			checkVnum = checkVnum[0]

		if mtrlVnum != checkVnum and not mtrlVnum in specialOres:
			return False
		
		if curCount>=maxCount:
			return False

		return True

	def __CanAddAccessorySocket(self, dstSlotPos):
		dstItemVNum = player.GetItemIndex(dstSlotPos)
		if dstItemVNum == 0:
			return False

		item.SelectItem(1, 2, dstItemVNum)

		if item.GetItemType() == item.ITEM_TYPE_ARMOR:
			if not item.GetItemSubType() in (item.ARMOR_WRIST, item.ARMOR_NECK, item.ARMOR_EAR):
				return False
		elif item.GetItemType() == item.ITEM_TYPE_BELT:
			if item.GetValue(0) != 1:
				return False
		else:
			return False

		curCount = player.GetItemMetinSocket(dstSlotPos, 0)
		maxCount = player.GetItemMetinSocket(dstSlotPos, 1)
		
		ACCESSORY_SOCKET_MAX_SIZE = 3
		if maxCount >= ACCESSORY_SOCKET_MAX_SIZE:
			return False

		return True

	def __CanAddSpecificItemAttr(self, srcSlotPos, dstSlotPos):
		dstItemVNum = player.GetItemIndex(dstSlotPos)
		srcItemVnum = player.GetItemIndex(srcSlotPos)
		if not dstItemVNum or not srcItemVnum:
			return False

		item.SelectItem(1, 2, srcItemVnum)
		socketCount = item.GetSocketCount()

		item.SelectItem(1, 2, dstItemVNum)
		
		if not item.GetItemType() in (item.ITEM_TYPE_WEAPON, item.ITEM_TYPE_ARMOR, item.ITEM_TYPE_TOTEM) or socketCount != item.ADDON_COSTUME_NONE: 
			isOk = False
			if item.GetItemType() == item.ITEM_TYPE_COSTUME:
				if item.GetItemSubType() == item.COSTUME_TYPE_BODY and socketCount == item.ADDON_COSTUME_ARMOR:
					isOk = True

				elif item.GetItemSubType() == item.COSTUME_TYPE_HAIR and socketCount == item.ADDON_COSTUME_HAIR:
					isOk = True

				elif item.GetItemSubType() == item.COSTUME_TYPE_WEAPON and socketCount == item.ADDON_COSTUME_WEAPON:
					isOk = True

			if not isOk:
				return False
		
		myAttr = player.GetItemAttribute(srcSlotPos, 0)

		maxAttrCount = player.NORMAL_ATTRIBUTE_SLOT_MAX_NUM
		if item.GetItemType() == item.ITEM_TYPE_TOTEM:
			maxAttrCount = 3
		attrCount = 0
		for i in xrange(maxAttrCount):
			attr = player.GetItemAttribute(dstSlotPos, i)
			if myAttr[0] == attr[0]:
				return False
			elif attr != (0, 0):
				attrCount += 1

		tchat("AttrCount %d AllowCount %d" % (attrCount, maxAttrCount))
		if attrCount < maxAttrCount and not item.IsApplyType(myAttr[0]):
			return True
								
		return False

	def __CanAddSoulToCostumeSash(self, srcSlotPos, dstSlotPos):
		dstItemVNum = player.GetItemIndex(dstSlotPos)
		srcItemVnum = player.GetItemIndex(srcSlotPos)
		if not dstItemVNum or not srcItemVnum:
			return False

		item.SelectItem(1, 2, srcItemVnum)
		subType = item.GetItemSubType()
		soulPower = item.GetValue(3)

		item.SelectItem(1, 2, dstItemVNum)
		sashPower = item.GetValue(3)
		
		if item.GetItemType() != item.ITEM_TYPE_COSTUME or item.GetItemSubType() != item.COSTUME_TYPE_ACCE_COSTUME or soulPower > sashPower and soulPower < 5 or soulPower >= 5 and sashPower != 4:
			return False

		costumeSoulType = player.GetItemMetinSocket(dstSlotPos, 2)
		if costumeSoulType != item.SOUL_NONE and costumeSoulType != subType:
			return False
		
		myAttr = player.GetItemAttribute(srcSlotPos, 0)

		attrCount = 0
		for i in xrange(player.NORMAL_ATTRIBUTE_SLOT_MAX_NUM):
			attr = player.GetItemAttribute(dstSlotPos, i)
			if myAttr[0] == attr[0]:
				return False
			elif attr != (0, 0):
				attrCount += 1

		if attrCount < soulPower - 1:
			return False

		tchat("AttrCount %d AllowCount %d" % (attrCount, player.NORMAL_ATTRIBUTE_SLOT_MAX_NUM))
		if attrCount < player.NORMAL_ATTRIBUTE_SLOT_MAX_NUM and not item.IsApplyType(myAttr[0]):
			return True
								
		return False

	def __CanAddItemAttr2(self, dstSlotPos):
		dstItemVNum = player.GetItemIndex(dstSlotPos)
		if dstItemVNum == 0:
			return False

		item.SelectItem(1, 2, dstItemVNum)
		
		if not item.GetItemType() in (item.ITEM_TYPE_WEAPON, item.ITEM_TYPE_ARMOR):	 
			return False
		
		maxAttrCount = player.NORMAL_ATTRIBUTE_SLOT_MAX_NUM
		
		attrCount = 0
		for i in xrange(maxAttrCount):
			if player.GetItemAttribute(dstSlotPos, i) != (0, 0):
				attrCount += 1

		tchat("AttrCount %d AllowCount %d" % (attrCount, maxAttrCount))
		if attrCount == maxAttrCount - 1:
			return True
								
		return False

	def __CanAddItemAttr(self, dstSlotPos):
		dstItemVNum = player.GetItemIndex(dstSlotPos)
		if dstItemVNum == 0:
			return False

		item.SelectItem(1, 2, dstItemVNum)
		
		if not item.GetItemType() in (item.ITEM_TYPE_WEAPON, item.ITEM_TYPE_ARMOR, item.ITEM_TYPE_TOTEM):	 
			return False
		
		maxAttrCount = player.NORMAL_ATTRIBUTE_SLOT_MAX_NUM - 1
		if item.GetItemType() == item.ITEM_TYPE_TOTEM:
			maxAttrCount = 3
		attrCount = 0
		for i in xrange(maxAttrCount):
			if player.GetItemAttribute(dstSlotPos, i) != (0, 0):
				attrCount += 1

		tchat("AttrCount %d AllowCount %d" % (attrCount, maxAttrCount))
		if attrCount < maxAttrCount:
			return True
								
		return False

	def __ShowToolTip(self, slotIndex):
		if None != self.tooltipItem:
			self.tooltipItem.SetShowSearchItemHotkey(True)
			self.tooltipItem.inventoryItemSlot = slotIndex
			self.tooltipItem.SetInventoryItem(slotIndex)

	def OnTop(self):
		if None != self.tooltipItem:
			self.tooltipItem.SetTop()

		for btn in self.sidebarButtons:
			btn.SetTop()

	def OnPressEscapeKey(self):
		self.Close()
		return True

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

	def UseItemSlot(self, slotIndex):
		if constInfo.GET_ITEM_DROP_QUESTION_DIALOG_STATUS():
			return

		slotIndex = self.__InventoryLocalSlotPosToGlobalSlotPos(slotIndex)

		if app.ENABLE_DRAGON_SOUL_SYSTEM:
			if self.wndDragonSoulRefine.IsShow():
				self.wndDragonSoulRefine.AutoSetItem((player.INVENTORY, slotIndex), 1)
				return

		itemVnum = player.GetItemIndex(slotIndex)
		if (app.IsPressed(app.DIK_LCONTROL) or app.IsPressed(app.DIK_RCONTROL)) and app.IsPressed(app.DIK_LSHIFT):
			if self.interface:
				self.interface.StartShopSearchByVnum(itemVnum)
			return

		# Multi Use Item
		if app.IsPressed(app.DIK_LCONTROL) and player.GetItemCount(slotIndex) > 1:
			item.SelectItem(1, 2, itemVnum)
			if item.GetItemType() != item.ITEM_TYPE_USE or item.GetItemSubType() != item.USE_POTION:
				itemCount = player.GetItemCount(slotIndex)
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
		self.OverOutItem()

	def __UseItem(self, slotIndex):
		ItemVNum = player.GetItemIndex(slotIndex)
		item.SelectItem(1, 2, ItemVNum)
		if item.IsFlag(item.ITEM_FLAG_CONFIRM_WHEN_USE):
			self.questionDialog = uiCommon.QuestionDialog()
			self.questionDialog.SetText(localeInfo.INVENTORY_REALLY_USE_ITEM)
			self.questionDialog.SetAcceptEvent(ui.__mem_func__(self.__UseItemQuestionDialog_OnAccept))
			self.questionDialog.SetCancelEvent(ui.__mem_func__(self.__UseItemQuestionDialog_OnCancel))
			self.questionDialog.Open()
			self.questionDialog.slotIndex = slotIndex

		else:
			self.__SendUseItemPacket(slotIndex)

	def __UseItemQuestionDialog_OnCancel(self):
		self.OnCloseQuestionDialog()

	def __UseItemQuestionDialog_OnAccept(self):
		self.__SendUseItemPacket(self.questionDialog.slotIndex)

		if self.questionDialog:
			self.questionDialog.Close()
		self.questionDialog = None

	def __SendUseItemToItemPacket(self, srcSlotPos, dstSlotPos, check = True):
		if uiPrivateShopBuilder.IsBuildingPrivateShop():
			chat.AppendChat(chat.CHAT_TYPE_INFO, localeInfo.USE_ITEM_FAILURE_PRIVATE_SHOP)
			return
			
		if check and player.IsGMOwner(srcSlotPos) and not player.IsGMOwner(dstSlotPos):
			vnum = player.GetItemIndex(srcSlotPos)
			item.SelectItem(1, 2, vnum)
			tchat("%s is GMFlagged and the other is not" % item.GetItemName())
			if item.IsFlag(item.ITEM_FLAG_CONFIRM_GM_ITEM):
				tchat("Item has confirm gm item flag")	
				self.questionDialog = uiCommon.QuestionDialog()
				self.questionDialog.SetText("The Item will be NOT-tradeable if you do that.")
				self.questionDialog.SetAcceptEvent(ui.__mem_func__(self.__SendUseItemToItemPacket_OnAccpect))
				self.questionDialog.SetCancelEvent(ui.__mem_func__(self.__UseItemQuestionDialog_OnCancel))
				self.questionDialog.Open()
				self.questionDialog.srcSlotPos = srcSlotPos
				self.questionDialog.dstSlotPos = dstSlotPos
				return
		
		net.SendItemUseToItemPacket(srcSlotPos, dstSlotPos)

	def __SendUseItemToItemPacket_OnAccpect(self):
		self.__SendUseItemToItemPacket(self.questionDialog.srcSlotPos, self.questionDialog.dstSlotPos, False)
		
		if self.questionDialog:
			self.questionDialog.Close()
		self.questionDialog = None
		
	def __SendUseItemPacket(self, slotPos):
		if uiPrivateShopBuilder.IsBuildingPrivateShop():
			chat.AppendChat(chat.CHAT_TYPE_INFO, localeInfo.USE_ITEM_FAILURE_PRIVATE_SHOP)
			return

		if app.IsPressed(app.DIK_LCONTROL) or app.IsPressed(app.DIK_LALT):
			if item.IsQuiver(player.GetItemIndex(slotPos)):
				self.__SendUseItemToItemPacket(slotPos, slotPos) # unpack all arrows
				return

		net.SendItemUsePacket(slotPos)
	
	def __SendUseMultiItemPacket(self, slotPos, count):
		if uiPrivateShopBuilder.IsBuildingPrivateShop():
			chat.AppendChat(chat.CHAT_TYPE_INFO, localeInfo.USE_ITEM_FAILURE_PRIVATE_SHOP)
			return

		net.SendItemMultiUsePacket(slotPos, count)
	
	def __SendMoveItemPacket(self, srcSlotPos, dstSlotPos, srcItemCount):
		if uiPrivateShopBuilder.IsBuildingPrivateShop():
			chat.AppendChat(chat.CHAT_TYPE_INFO, localeInfo.MOVE_ITEM_FAILURE_PRIVATE_SHOP)
			return

		self.OnCloseQuestionDialog()
		net.SendItemMovePacket(srcSlotPos, dstSlotPos, srcItemCount)

	def __SendSpecificMoveItemPacket(self, srcWindow, srcSlotPos, dstWindow, dstSlotPos, srcItemCount):
		if uiPrivateShopBuilder.IsBuildingPrivateShop():
			chat.AppendChat(chat.CHAT_TYPE_INFO, localeInfo.MOVE_ITEM_FAILURE_PRIVATE_SHOP)
			return

		self.OnCloseQuestionDialog()
		net.SendItemMovePacket(srcWindow, srcSlotPos, dstWindow, dstSlotPos, srcItemCount)

	def SetDragonSoulRefineWindow(self, wndDragonSoulRefine):
		if app.ENABLE_DRAGON_SOUL_SYSTEM:
			self.wndDragonSoulRefine = wndDragonSoulRefine

	def OnMoveWindow(self, x, y):
		self.UpdateCostumePosition()
		self.__UpdateSidebarPosition()
		if constInfo.SAVE_WINDOW_POSITION:
			cfg.Set(cfg.SAVE_GENERAL, "wnd_pos_inv", ("%d %d") % (x, y))
