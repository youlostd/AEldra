import ui
import localeInfo
import item
import player
import net
import uiCommon

class HorseUpgradeWindow(ui.ScriptWindow):

	UPGRADE_BONUS = 0
	UPGRADE_RAGE = 3

	TITLE_TEXT = {
		UPGRADE_BONUS + 0 : localeInfo.PET_UPGRADE_TITLE_BONUS1,
		UPGRADE_BONUS + 1 : localeInfo.PET_UPGRADE_TITLE_BONUS2,
		UPGRADE_BONUS + 2 : localeInfo.PET_UPGRADE_TITLE_BONUS3,
		UPGRADE_RAGE	  : localeInfo.PET_UPGRADE_TITLE_RAGE,
	}

	RAGE_TIME_TABLE = [
		5 * 60, # 0

		5 * 60 + 54 * 1, # 1
		5 * 60 + 54 * 2, # 2
		5 * 60 + 54 * 3, # 3
		5 * 60 + 54 * 4, # 4
		5 * 60 + 54 * 5, # 5

		5 * 60 + 54 * 6, # 6
		5 * 60 + 54 * 7, # 7
		5 * 60 + 54 * 8, # 8
		5 * 60 + 54 * 9, # 9
		15 * 60, # 10
	]

	#################################################
	## MAIN FUNCTIONS
	#################################################

	def __init__(self):
		ui.ScriptWindow.__init__(self)

		self.refineIndex = 0
		self.currentLevel = 0
		self.cost = 0
		self.materials = []

		self.acceptBtn = None

		self.wndPopup = uiCommon.PopupDialog()
		self.wndPopup.Close()

		self.LoadWindow()

	def __del__(self):
		ui.ScriptWindow.__del__(self)

	def LoadWindow(self):
		try:
			pyScrLoader = ui.PythonScriptLoader()
			pyScrLoader.LoadScriptFile(self, "UIScript/HorseUpgradeWindow.py")
		except:
			import exception
			exception.Abort("HorseUpgradeWindow.LoadDialog.LoadScript")

		try:
			GetObject=self.GetChild
			self.board = GetObject("board")

		except:
			import exception
			exception.Abort("HorseUpgradeWindow.LoadDialog.BindObject")

		self.board.SetCloseEvent(ui.__mem_func__(self.Close))
		self.Clear()

	def Resize(self):
		self.SetSize(self.GetWidth(), self.yPos + 10)
		self.board.SetSize(self.GetWidth(), self.GetHeight())

	def Clear(self):
		self.childs = []
		self.yPos = 65
		self.acceptBtn = None

		self.Resize()

	def BINARY_SetRefineIndex(self, refineIndex):
		self.refineIndex = refineIndex

	def BINARY_SetCurrentLevel(self, currentLevel):
		self.currentLevel = currentLevel

	def BINARY_SetCost(self, cost):
		self.cost = cost

	def BINARY_ClearMaterial(self):
		self.materials = []

	def BINARY_AddMaterial(self, matVnum, matCount):
		self.materials.append((matVnum, matCount))

	def CheckAcceptButton(self):
		if not self.acceptBtn:
			return

		self.acceptBtn.Enable()

		if self.cost > 0 and player.GetMoney() < self.cost:
			self.acceptBtn.Disable()
		else:
			for i in xrange(len(self.materials)):
				itemVnum, itemCount = self.materials[i]
				itemOwnedCount = 0
				for j in xrange(player.INVENTORY_PAGE_SIZE * player.INVENTORY_PAGE_COUNT):
					if player.GetItemIndex(j) == itemVnum:
						itemOwnedCount += player.GetItemCount(j)
						if itemOwnedCount >= itemCount:
							break
				for j in xrange(player.UPPITEM_INVENTORY_SLOT_START, player.UPPITEM_INVENTORY_SLOT_END):
					if player.GetItemIndex(j) == itemVnum:
						itemOwnedCount += player.GetItemCount(j)
						if itemOwnedCount >= itemCount:
							break
				if itemOwnedCount < itemCount:
					self.acceptBtn.Disable()
					break

	def __Load(self):
		self.Clear()

		self.board.SetTitleName(self.TITLE_TEXT[self.refineIndex])

		if self.refineIndex == self.UPGRADE_RAGE:
			self.AppendTextLine(localeInfo.PET_UPGRADE_TEXT_LEVEL % (self.currentLevel, self.currentLevel + 1))
		else:
			bonusIndex = self.refineIndex - self.UPGRADE_BONUS
			texts = [localeInfo.PET_UPGRADE_TEXT_BONUS1, localeInfo.PET_UPGRADE_TEXT_BONUS2, localeInfo.PET_UPGRADE_TEXT_BONUS3]
			applyType, oldApplyValue, itemCount = player.GetHorseBonusProto(bonusIndex, max(self.currentLevel - 1, 0))
			applyType, newApplyValue, itemCount = player.GetHorseBonusProto(bonusIndex, self.currentLevel)
			if self.currentLevel == 0:
				oldApplyValue = 0
			self.AppendTextLine(texts[bonusIndex] % (oldApplyValue, newApplyValue))

		if self.refineIndex == self.UPGRADE_RAGE:
			self.yPos += 5
			self.AppendMultiTextLine(localeInfo.HORSE_UPGRADE_INFO_RAGE % localeInfo.SecondToDHMS(self.RAGE_TIME_TABLE[self.currentLevel + 1]))
			self.yPos += 2

		if self.cost > 0:
			self.AppendTextLine(localeInfo.PET_UPGRADE_PRICE % localeInfo.NumberToMoneyString(self.cost))

		for i in xrange(len(self.materials)):
			itemVnum, itemCount = self.materials[i]
			self.AppendMaterial(itemVnum, itemCount)

		self.AppendButtons()
		self.CheckAcceptButton()

	def OnResult(self, isSuccess):
		if isSuccess:
			self.wndPopup.SetText(localeInfo.KING_HORSE_UPGRADE_SUCCESS)
		else:
			self.wndPopup.SetText(localeInfo.KING_HORSE_UPGRADE_FAIL)
		self.wndPopup.Open()

	def Destroy(self):
		self.Close()

		self.wndPopup.Close()
		self.wndPopup = None

		ui.ScriptWindow.Destroy(self)

	def Open(self):
		self.__Load()
		self.SetCenterPosition()
		self.Show()
		self.SetTop()

	def Close(self):
		self.Hide()

	def OnPressEscapeKey(self):
		self.Close()
		return True

	def AppendChildren(self, child):
		child.SetParent(self)
		self.childs.append(child)
		return child

	def AppendTextLine(self, text):
		textLine = self.AppendChildren(ui.TextLine())
		textLine.SetPosition(0, self.yPos)
		textLine.SetWindowHorizontalAlignCenter()
		textLine.SetHorizontalAlignCenter()
		textLine.SetText(text)
		textLine.Show()

		self.yPos = textLine.GetBottom() + 8
		self.Resize()

		return textLine

	def AppendMultiTextLine(self, text):
		textLine = self.AppendChildren(ui.MultiTextLine())
		textLine.SetPosition(20, self.yPos)
		textLine.SetWidth(self.GetWidth() - 20 - 27)
		textLine.SetTextHorizontalAlignCenter()
		textLine.SetText(text)
		textLine.Show()

		self.yPos = textLine.GetBottom() + 8
		self.Resize()

		return textLine

	def AppendMaterial(self, vnum, count):
		item.SelectItem(1, 2, vnum)
		icon = item.GetIconImageFileName()
		name = item.GetItemName()
		desc = item.GetItemDescription()

		img = self.AppendChildren(ui.ImageBox())
		img.SetPosition(20, self.yPos)
		img.LoadImage(icon)
		img.Show()

		itemName = self.AppendChildren(ui.TextLine())
		itemName.SetPosition(img.GetRight() + 5, self.yPos)
		itemName.SetText(str(count) + "x " + name)
		itemName.Show()

		itemDesc = self.AppendChildren(ui.MultiTextLine())
		itemDesc.SetPosition(img.GetRight() + 5, itemName.GetBottom() + 5)
		itemDesc.SetWidth(self.GetWidth() - itemDesc.GetLeft() - 27)
		itemDesc.SetText(desc)
		itemDesc.Show()

		self.yPos += max(img.GetHeight(), itemDesc.GetTop() - itemName.GetTop() + itemDesc.GetRealHeight()) + 5
		self.Resize()

	def OnClickAcceptButton(self):
		self.Close()
		net.SendChatPacket("/horse_refine %d" % self.refineIndex)

	def AppendButtons(self):
		btnAccept = self.AppendChildren(ui.Button())
		btnAccept.SetPosition(35, self.yPos)
		btnAccept.SetUpVisual("d:/ymir work/ui/public/Large_Button_01.sub")
		btnAccept.SetOverVisual("d:/ymir work/ui/public/Large_Button_02.sub")
		btnAccept.SetDownVisual("d:/ymir work/ui/public/Large_Button_03.sub")
		btnAccept.SetDisableVisual("d:/ymir work/ui/public/Large_Button_04.sub")
		btnAccept.SetText(localeInfo.PET_UPGRADE_ACCEPT_BUTTON_TEXT)
		btnAccept.SAFE_SetEvent(self.OnClickAcceptButton)
		btnAccept.Show()
		self.acceptBtn = btnAccept

		btnCancel = self.AppendChildren(ui.Button())
		btnCancel.SetUpVisual("d:/ymir work/ui/public/Large_Button_01.sub")
		btnCancel.SetOverVisual("d:/ymir work/ui/public/Large_Button_02.sub")
		btnCancel.SetDownVisual("d:/ymir work/ui/public/Large_Button_03.sub")
		btnCancel.SetPosition(self.GetWidth() - btnCancel.GetWidth() - 45, self.yPos)
		btnCancel.SetText(localeInfo.PET_UPGRADE_CANCEL_BUTTON_TEXT)
		btnCancel.SAFE_SetEvent(self.Close)
		btnCancel.Show()

		self.yPos += btnAccept.GetHeight() + 10
		self.Resize()
