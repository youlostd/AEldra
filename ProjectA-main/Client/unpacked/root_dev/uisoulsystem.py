import ui
import localeInfo
import mouseModule
import uiToolTip
import item
import player
import net
import uiCommon

class SoulRefineWindow(ui.Window):
	def __init__(self):
		ui.Window.__init__(self)
		self.AddFlag("movable")
		self.AddFlag("float")

		self.base = ui.BoardWithTitleBar()
		self.base.SetParent(self)
		self.base.SetTitleName(localeInfo.SOUL_REFINE_TITLE)
		self.base.SetCloseEvent(ui.__mem_func__(self.Close))
		self.base.Show()

		self.bg = ui.ExpandedImageBox()
		self.bg.SetParent(self.base)
		self.bg.LoadImage("D:/Ymir Work/ui/soul_system/bg.tga")
		self.bg.Show()
		
		self.base.SetSize(self.bg.GetWidth(), self.bg.GetHeight())
		self.SetSize(self.base.GetRealWidth(), self.base.GetRealHeight())

		self.btnUpgrade = ui.Button()
		self.btnUpgrade.SetParent(self.bg)
		self.btnUpgrade.SetUpVisual("D:/Ymir Work/ui/soul_system/btn_normal.tga")
		self.btnUpgrade.SetOverVisual("D:/Ymir Work/ui/soul_system/btn_hover.tga")
		self.btnUpgrade.SetDownVisual("D:/Ymir Work/ui/soul_system/btn_down.tga")
		self.btnUpgrade.SetPosition(20, 215)
		self.btnUpgrade.SetText(localeInfo.SOUL_REFINE_UPGRADE)
		self.btnUpgrade.SetEvent(ui.__mem_func__(self.AskUpgrade))
		self.btnUpgrade.Show()

		self.btnCancel = ui.Button()
		self.btnCancel.SetParent(self.bg)
		self.btnCancel.SetUpVisual("D:/Ymir Work/ui/soul_system/btn_normal.tga")
		self.btnCancel.SetOverVisual("D:/Ymir Work/ui/soul_system/btn_hover.tga")
		self.btnCancel.SetDownVisual("D:/Ymir Work/ui/soul_system/btn_down.tga")
		self.btnCancel.SetPosition(85, 215)
		self.btnCancel.SetText(localeInfo.SOUL_REFINE_CANCEL)
		self.btnCancel.SetEvent(ui.__mem_func__(self.CancelRefine))
		self.btnCancel.Show()

		self.improveText = self.__GenerateMultiLine(localeInfo.SOUL_REFINE_INFO_TEXT, 110, 80, 45, 13)

		self.needText = ui.TextLine()
		self.needText.SetParent(self.bg)
		self.needText.SetHorizontalAlignCenter()
		self.needText.SetPosition(191, 45)
		self.needText.SetText(localeInfo.SOUL_REFINE_NEED_TEXT)
		self.needText.Show()

		self.moneyText = ui.TextLine()
		self.moneyText.SetParent(self.bg)
		self.moneyText.SetPosition(174, 219)
		self.SetUpgradeCost(0)
		self.moneyText.Show()

		self.matGrid = ui.GridSlotWindow()
		self.matGrid.SetParent(self.bg)
		self.matGrid.SetPosition(176, 62)
		self.matGrid.ArrangeSlot(2, 1, 4, 32, 32, 0, 6)
		self.matGrid.SetSlotBaseImage("d:/ymir work/ui/public/Slot_Base.sub", 1.0, 1.0, 1.0, 1.0)
		#self.matGrid.SetOverInItemEvent(self.OnOverInItem)
		#self.matGrid.SetOverOutItemEvent(self.OnOverOutItem)
		#self.matGrid.SetUnselectItemSlotEvent(self.OnSelectItemSlot)
		#self.matGrid.SetSelectItemSlotEvent(self.OnClickItemSlot)
		self.matGrid.Show()

		self.refineItems = ui.SlotWindow()
		self.refineItems.SetParent(self.bg)
		self.refineItems.SetSize(32, 110)
		self.refineItems.SetPosition(66, 89)
		self.refineItems.AppendSlot(0, 0, 0, 32, 32)
		self.refineItems.AppendSlot(1, 0, 110-32, 32, 32)
		self.refineItems.SetSelectEmptySlotEvent(ui.__mem_func__(self.OnSelectEmptySlot))
		self.refineItems.SetUnselectItemSlotEvent(ui.__mem_func__(self.OnSelectItemSlot))
		self.refineItems.SetSlotBaseImage("d:/ymir work/ui/public/Slot_Base.sub", 1.0, 1.0, 1.0, 1.0)
		self.refineItems.Show()

		self.itemDict = [[-1, 0], [-1, 0], [-1, 0], [-1, 0], [-1, 0], [-1, 0]]
		self.toolTip = uiToolTip.ItemToolTip()
		self.dlgQuestion = None

		self.refineItems.SetOverInItemEvent(ui.__mem_func__(self.OnOverInItem))
		self.refineItems.SetOverOutItemEvent(ui.__mem_func__(self.OnOverOutItem))
		self.matGrid.SetOverInItemEvent(ui.__mem_func__(self.OnOverInItem))
		self.matGrid.SetOverOutItemEvent(ui.__mem_func__(self.OnOverOutItem))

		self.SetCenterPosition()
		self.Hide()

	def CancelRefine(self):
		if self.itemDict[0][0] != -1:
			self.ClearWindow()
		else:
			self.Close()

	def OnSelectItemSlot(self, pos):
		if pos == 0:
			self.ClearWindow()

	def DoUpgrade(self):
		if self.itemDict[0][0] != -1:
			net.SendChatPacket("/refine_soul_item " + str(self.itemDict[0][0]))

	def OnTop(self):
		if self.dlgQuestion and self.dlgQuestion.IsShow():
			self.dlgQuestion.SetTop()

	def AskUpgrade(self):
		if self.itemDict[0][0] == -1 or (self.dlgQuestion and self.dlgQuestion.IsShow()):
			return

		dlgQuestion = uiCommon.QuestionDialog2()
		dlgQuestion.SetText2(localeInfo.REFINE_WARNING2)
		dlgQuestion.SetAcceptEvent(ui.__mem_func__(self.DoUpgrade))
		dlgQuestion.SetCancelEvent(ui.__mem_func__(dlgQuestion.Close))
		dlgQuestion.SetText1(localeInfo.REFINE_DESTROY_WARNING)

		dlgQuestion.Open()
		self.dlgQuestion = dlgQuestion

	def RecvSoulRefineInfo(self, vnum, soulType, applyType, applyVals, materials, cost):
		self.itemDict[1][1] = vnum
		self.itemDict[1][0] = (applyType, applyVals)
		self.refineItems.SetItemSlot(1, vnum, 0)
		self.refineItems.RefreshSlot()
		for i in xrange(len(materials)):
			self.itemDict[i+2][1] = materials[i][0]

			self.matGrid.SetItemSlot(i+2, materials[i][0], materials[i][1])
			self.matGrid.RefreshSlot()
		self.SetUpgradeCost(cost)

	def OnSelectEmptySlot(self, pos):
		if mouseModule.mouseController.isAttached() and pos == 0:
			attachedItemID = mouseModule.mouseController.GetAttachedItemIndex()
			attachedSlotType = mouseModule.mouseController.GetAttachedType()
			attachedSlotPos = mouseModule.mouseController.GetAttachedSlotNumber()
			item.SelectItem(1, 2, attachedItemID)

			if player.SLOT_TYPE_INVENTORY == attachedSlotType and item.GetItemType() == item.ITEM_TYPE_SOUL and item.GetItemRefinedVnum():
				self.itemDict[0][0] = attachedSlotPos
				self.itemDict[0][1] = attachedItemID
				self.refineItems.SetItemSlot(pos, attachedItemID, 0)
				self.refineItems.RefreshSlot()
				net.SendChatPacket("/refine_soul_item_info " + str(attachedSlotPos))
				mouseModule.mouseController.DeattachObject()

	def SetUpgradeCost(self, money):
		money = str(money)
		original = money
		sLen = len(original)
		while sLen > 3 and original[sLen-3:] == "000":
			money = money[::-1].replace("000"[::-1], "k"[::-1], 1)[::-1]
			original = original[:sLen - 3]
			sLen -= 3
		self.moneyText.SetText(money)

	def OnPressEscapeKey(self):
		self.Close()
		return True

	def OnUpdate(self):
		if self.itemDict[0][0] >= 0:
			currVnum = player.GetItemIndex(self.itemDict[0][0])
			if currVnum != self.itemDict[0][1]:
				self.ClearWindow()

	def ClearWindow(self):
		self.itemDict = [[-1, 0], [-1, 0], [-1, 0], [-1, 0], [-1, 0], [-1, 0]]
		self.refineItems.ClearSlot(0)
		self.refineItems.ClearSlot(1)
		self.refineItems.RefreshSlot()
		self.SetUpgradeCost(0)

		for i in xrange(4):
			self.matGrid.ClearSlot(i + 2)
		self.matGrid.RefreshSlot()
		self.dlgQuestion = None

	def Close(self):
		self.ClearWindow()
		self.Hide()

	def OnOverOutItem(self):
		self.toolTip.Hide()

	def OnOverInItem(self, pos):
		self.toolTip.ClearToolTip()

		if pos == 0:
			self.toolTip.SetInventoryItem(self.itemDict[pos][0])
		else:
			self.toolTip.AddItemData(self.itemDict[pos][1], 0, 0)

		if pos == 1 and self.itemDict[pos][0] != -1:
			affectString = uiToolTip.GET_AFFECT_STRING(self.itemDict[1][0][0], 0)

			needPCT = False
			if affectString.find("%") != -1:
				needPCT = True

			if affectString.rfind(" ") != -1:
				affectString = affectString[:affectString.rfind(" ")]

			affectString += " " + str(self.itemDict[1][0][1][0])
			for i in xrange(3):
				affectString += "/" + str(self.itemDict[1][0][1][i + 1])
				
			if needPCT:
				affectString += "%"

			self.toolTip.AppendTextLine(affectString, self.toolTip.SPECIAL_POSITIVE_COLOR)
		
	def __GenerateMultiLine(self, text, maxWidth, xStart, yStart, padding):
		currY = yStart
		currText = self.__GenerateSingleLine(xStart, currY)
		textHolder = []

		tempText = ui.TextLine()
		tempText.Hide()
		
		splt = text.split(" ")
		currText.SetText(splt[0])
		splt = splt[1:]
		for i in splt:
			tempText.SetText(" " + i)
			if tempText.GetTextWidth() + currText.GetTextWidth() > maxWidth:
				currText.AdjustSize()
				textHolder.append(currText)
				currY += padding
				currText = self.__GenerateSingleLine(xStart, currY)
				currText.SetText(i)
			else:
				currText.SetText(currText.GetText() + " " + i)

		textHolder.append(currText)
		return textHolder

	def __GenerateSingleLine(self, x, y):
		text = ui.TextLine()
		text.SetParent(self.bg)
		text.SetHorizontalAlignCenter()
		text.SetPosition(x, y)
		text.Show()
		return text
