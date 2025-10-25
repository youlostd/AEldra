import ui
import app
import net
import constInfo
import shop
import quest as quest_module
import localeInfo
import item
import uiCommon

IMAGE_PATH = "d:/ymir work/ui/battlepass/"
BANNER_PATH = "d:/ymir work/ui/game/battlepass/%s.tga"
QUEST_TYPE_NORMAL = 0
QUEST_TYPE_LEGENDARY = 1

class BattlePassWindow(ui.ScriptWindow):

	def __init__(self):
		ui.ScriptWindow.__init__(self)
		self.questDict = {}
		self.itemToolTip = None
		self.shop = False
		self.itemBuyQuestionDialog = None
		self.visualSlot = {}
		self.__LoadWindow()

	def __del__(self):
		ui.ScriptWindow.__del__(self)

	def __LoadWindow(self):
		try:
			pyScrLoader = ui.PythonScriptLoader()
			pyScrLoader.LoadScriptFile(self, "uiscript/battlepass.py")
		except:
			import exception
			exception.Abort("BattlePassWindow.LoadWindow.LoadObject")

		try:
			self.GetChild("TitleBar").SetCloseEvent(ui.__mem_func__(self.Close))
			self.showQuestBtn = self.GetChild("QuestButton")
			self.showShopBtn = self.GetChild("ShopButton")
			self.itemGrid = self.GetChild("ItemGrid")
		except:
			import exception
			exception.Abort("BattlePassWindow.LoadWindow.BindObject")

		self.showQuestBtn.SAFE_SetEvent(self.OnShowQuest)
		self.showShopBtn.SAFE_SetEvent(self.OnShowShop)

		self.itemGrid.SetOverInItemEvent(ui.__mem_func__(self.__OnOverInItem))
		self.itemGrid.SetOverOutItemEvent(ui.__mem_func__(self.__OnOverOutItem))
		self.itemGrid.SAFE_SetButtonEvent("LEFT", "EXIST", self.__OnSelectItem)
		self.itemGrid.SAFE_SetButtonEvent("RIGHT", "EXIST", self.__OnSelectItem)
		self.itemGrid.Hide()

		self.banner = ui.MakeImageBox(self, BANNER_PATH % "banner1", 11, 34)
		# self.banner.UpdateRect()
		# self.banner.SetMouseLeftButtonDownEvent(app.ShellExecute, constInfo.URL["battlepass"], False) # TODO

		self.questListBox = ui.ListBoxEx()
		self.questListBox.SetParent(self)
		self.questListBox.SetPosition(122, 141)
		self.questListBox.SetSize(180, 328)
		self.questListBox.SetItemSize(328, 57-19)
		self.questListBox.SetItemStep(61-18)
		self.questListBox.SetViewItemCount(4)
		self.questListBox.Show()

		self.scrollBar = ui.ScrollBarTemplate()
		self.scrollBar.SetParent(self)
		self.scrollBar.SetPosition(457, 141)
		self.scrollBar.SetBarImage(IMAGE_PATH + "scrollbar_2.tga")
		self.scrollBar.SetMiddleImage(IMAGE_PATH + "scrollbar_1.tga")
		self.scrollBar.SetScrollBarSize(179)
		self.scrollBar.Show()

		self.questListBox.SetScrollBar(self.scrollBar)

	def OnSelectQuest(self, questBoard):
		for i in xrange(quest_module.GetQuestCount()):
			(questName, questIcon, questCounterSize, catId) = quest_module.GetQuestData(i)
			if questName.endswith(questBoard.GetTaskName()):
				from event import QuestButtonClick
				QuestButtonClick(-2147483648 + quest_module.GetQuestIndex(i))
				break

		questBoard.OnMouseOverOut()

	def OnShowQuest(self):
		self.questListBox.Show()
		self.scrollBar.Show()
		self.itemGrid.Hide()

	def OnShowShop(self):
		tchat("show shop")
		constInfo.BATTLEPASS_TEMP = True
		net.SendChatPacket("/battlepass_shop 55")
		self.questListBox.Hide()
		self.scrollBar.Hide()
		self.itemGrid.Show()

	def SetItemToolTip(self, tooltip):
		self.tooltipItem = tooltip

	def __OnOverInItem(self, slotIndex):
		if slotIndex in self.visualSlot:
			self.tooltipItem.SetShopItem(self.visualSlot[slotIndex])
		tchat("slotIndex %d" % slotIndex)

	def __OnOverOutItem(self):
		self.tooltipItem.HideToolTip()

	def __OnSelectItem(self, slotIndex):
		if slotIndex in self.visualSlot:
			self.AskBuyItem(self.visualSlot[slotIndex])

	def AskBuyItem(self, slotPos):
		itemIndex = shop.GetItemID(slotPos)
		itemPrice = shop.GetItemPrice(slotPos)
		itemCount = shop.GetItemCount(slotPos)

		item.SelectItem(1, 2, itemIndex)
		itemName = item.GetItemName()

		itemBuyQuestionDialog = uiCommon.QuestionDialog()
		itemBuyQuestionDialog.SetText(localeInfo.DO_YOU_BUY_ITEM(itemName, itemCount, localeInfo.NumberToMoneyString(itemPrice)))
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

	def SetData(self, index, progress, name, task, vnum, count):
		if index > 10:
			return

		isLegendary = index>=7
		if index in self.questDict:
			self.questDict[index].SetType(isLegendary)
			self.questDict[index].SetInfo(name, task + ": " + str(count), progress>=100)
			self.questDict[index].Show()
		else: #create
			quest = Quest()
			quest.SetEvent(self.OnSelectQuest)
			quest.SetType(isLegendary)
			quest.SetInfo(name, task + ": " + str(count), progress>=100)
			quest.idx = index

			self.questDict[index] = quest
			self.questListBox.RemoveAllItems()
			questList = self.questDict.values()
			questList.sort(key = lambda x : x.idx, reverse = False)
			for quest in questList:
				self.questListBox.AppendItem(quest, True)

	# 	self.Refresh()

	# def Refresh(self):
	# 	for quest in questList:
			

	def LoadShop(self):
		self.shop = True
		tchat("LoadShop :)")
		self.__RefreshSlot()

	def __RefreshSlot(self):
		self.visualSlot = {}
		getItemID=shop.GetItemID
		getItemCount=shop.GetItemCount
		setItemID=self.itemGrid.SetItemSlot

		for x in xrange(shop.SHOP_SLOT_COUNT):
			itemVnum = getItemID(x)
			itemCount = getItemCount(x)
			if itemCount == 1:
				itemCount = 0
			for slot in xrange(shop.SHOP_SLOT_COUNT):
				if self.itemGrid.IsEmptySlot(slot):
					self.visualSlot[slot] = x
					setItemID(slot, itemVnum, itemCount)
					break

		self.itemGrid.RefreshSlot()

	def Open(self):
		# net.SendChatPacket("/battlepass_data")
		self.Show()
		self.OnShowQuest()

	def Close(self):
		if self.shop:
			tchat("shop close")
			self.ClearSlots()
			shop.Close()
			net.SendShopEndPacket()
			self.shop = False
		self.Hide()

	def ClearSlots(self):
		for x in xrange(shop.SHOP_SLOT_COUNT):
			self.itemGrid.SetItemSlot(x, 0, 0)

	def OnMouseWheel(self, len):
		if len >= 0:
			self.scrollBar.OnUp()
		else:
			self.scrollBar.OnDown()
		return True

	def OnPressEscapeKey(self):
		self.Close()
		return True

	def Destroy(self):
		self.ClearDictionary()
		shop.Close()
		self.showQuestBtn = None
		self.showShopBtn = None
		self.itemGrid = None
		self.banner = None
		self.questListBox = None
		self.scrollBar = None
		for quest in self.questDict.values():
			quest.Destroy()
		self.questDict = {}
		self.tooltipItem = None
		self.itemBuyQuestionDialog = None


class Quest(ui.ImageBox):
	def __init__(self):
		ui.ImageBox.__init__(self)
		self.type = 0
		self.event = None
		self.selected = False
		self.idx = 0
		self.__LoadWindow()

	def __del__(self):
		ui.ImageBox.__del__(self)

	def __LoadWindow(self):
		self.title = ui.TextLine()
		self.title.SetParent(self)
		self.title.SetPosition(10+4, 6)
		self.title.Show()

		self.firstTask = ui.TextLine()
		self.firstTask.SetParent(self)
		self.firstTask.SetPosition(13+4, 21)
		self.firstTask.Show()

		self.statusImage = ui.MakeImageBox(self, IMAGE_PATH + "active.tga", 281, 11-10)
		self.statusImage.Hide()

	def SetType(self, type):
		self.type = type
		if type == QUEST_TYPE_NORMAL:
			self.LoadImage(IMAGE_PATH + "quest_normal_normal.tga")
		elif type == QUEST_TYPE_LEGENDARY:
			self.LoadImage(IMAGE_PATH + "quest_legendary_normal.tga")

	def SetEvent(self, event):
		self.event = event

	def OnMouseLeftButtonUp(self):
		self.selected = True

		if self.type == QUEST_TYPE_NORMAL:
			if self.selected:
				self.LoadImage(IMAGE_PATH + "quest_normal_down.tga")
		elif self.type == QUEST_TYPE_LEGENDARY:
			if self.selected:
				self.LoadImage(IMAGE_PATH + "quest_legendary_down.tga")

		if self.event:
			self.event(self)

	def OnMouseOverIn(self):
		if self.type == QUEST_TYPE_NORMAL:
			self.LoadImage(IMAGE_PATH + "quest_normal_hover.tga")
		elif self.type == QUEST_TYPE_LEGENDARY:
			self.LoadImage(IMAGE_PATH + "quest_legendary_hover.tga")

		tchat("idx %d" % self.idx)

	def OnMouseOverOut(self):
		if self.type == QUEST_TYPE_NORMAL:
			if self.selected:
				self.LoadImage(IMAGE_PATH + "quest_normal_down.tga")
			else:
				self.LoadImage(IMAGE_PATH + "quest_normal_normal.tga")
		elif self.type == QUEST_TYPE_LEGENDARY:
			if self.selected:
				self.LoadImage(IMAGE_PATH + "quest_legendary_down.tga")
			else:
				self.LoadImage(IMAGE_PATH + "quest_legendary_normal.tga")

	def SetInfo(self, title, task1, status):
		self.title.SetText(title)
		self.firstTask.SetText(task1)

		if not status:
			self.statusImage.LoadImage(IMAGE_PATH + "active.tga")
		else:
			self.statusImage.LoadImage(IMAGE_PATH + "done.tga")
		self.statusImage.Show()

	def GetTaskName(self):
		return self.title.GetText()

	def Destroy(self):
		self.event = None
		self.title = None
		self.firstTask = None
		self.statusImage = None
