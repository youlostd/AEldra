import ui
import app
import net
import uiToolTip
import item
import uiScriptLocale
import localeInfo

class NotificationWindow(ui.BaseScriptWindow):

	def __init__(self, mainwnd):
		ui.BaseScriptWindow.__init__(self, "shopsellnotification")
		self.vnum = 0
		self.count = 0
		self.mainwnd = mainwnd
		self.tooltipItem = self.mainwnd.tooltipItem
		self.__LoadWindow()

	def __del__(self):
		ui.BaseScriptWindow.__del__(self)

	def __LoadWindow(self):
		try:
			self.board = self.GetChild("board")
			self.titlebar = self.GetChild("titlebar")
			self.titlebar.SetCloseEvent(ui.__mem_func__(self.Close))
			self.titlebarText = self.GetChild("TitleName")
			self.titlebarText.SetText(uiScriptLocale.HALLOWEEN_GAME_WIN_TITLE)
			self.message = self.GetChild("message")
			self.acceptButton = self.GetChild("accept")
			self.acceptButton.SAFE_SetEvent(self.Close)
		except:
			import exception
			exception.Abort("shopsellnotification.LoadDialog.BindObject")

		self.soldItem = ui.SlotWindow()
		self.soldItem.AppendSlot(0, 0, 0, 32, 32)
		self.soldItem.SetParent(self.board)
		self.soldItem.SetWindowHorizontalAlignCenter()
		self.soldItem.SetOverInItemEvent(ui.__mem_func__(self.__OnOverInItem))
		self.soldItem.SetOverOutItemEvent(ui.__mem_func__(self.__OnOverOutItem))
		self.soldItem.SetWindowVerticalAlignCenter()
		self.soldItem.SetPosition(-16, 10)
		self.soldItem.Show()

	def Open(self):
		self.SetCenterPosition()
		self.SetTop()
		self.Show()

	def Close(self):
		self.mainwnd.Reset()
		self.Hide()

	def OnUpdate(self):
		self.SetTop()

	def SetData(self, vnum, count):
		self.vnum = int(vnum)
		self.message.SetText(uiScriptLocale.HALLOWEEN_GAME_WIN_TEXT % item.GetItemName(self.vnum))
		item.SelectItem(1, 2, self.vnum)
		(widthI, heightI) = item.GetItemSize()
		self.soldItem.SetItemSlot(0, self.vnum, int(count))
		self.soldItem.RefreshSlot()
		self.acceptButton.SetPosition(self.acceptButton.GetLeft(), self.acceptButton.GetHeight() + 5)
		self.titlebar.SetWidth(self.board.GetWidth())
		self.board.SetSize(self.board.GetWidth(), 120 + (32 * heightI) )
		self.SetSize(self.GetWidth(), 120 + (32 * heightI))
		self.UpdateRect()

	def OnPressEscapeKey(self):
		self.Close()
		return True

	def __OnOverInItem(self, slotIndex):
		if self.tooltipItem:
			self.tooltipItem.SetItemToolTip(self.vnum)

	def __OnOverOutItem(self):
		if self.tooltipItem:
			self.tooltipItem.HideToolTip()

class WheelOfFrightWindow(ui.ScriptWindow):
	def __init__(self):
		ui.ScriptWindow.__init__(self)
		self.__LoadWindow()
		self.tooltipItem = None
		self.itemsArr = []
		self.spin = False
		self.spins = 0
		self.degree = 0
		self.endDegree = 0
		self.totalDegree = 0
		self.successWnd = None

	def __del__(self):
		ui.ScriptWindow.__del__(self)

	def __LoadWindow(self):
		try:
			pyScrLoader = ui.PythonScriptLoader()
			pyScrLoader.LoadScriptFile(self, "uiscript/WheelOfFright.py")
		except:
			import exception
			exception.Abort("WheelOfFrightWindow.LoadWindow.LoadObject")

		try:
			self.GetChild("TitleBar").SetCloseEvent(ui.__mem_func__(self.Close))
			self.pointer = self.GetChild("WheelPointer")
			self.pointer.Hide()
			self.startBtn = self.GetChild("WheelStartButton")
			self.startBtn.SAFE_SetEvent(self.StartSpin)
			self.infoBtn = self.GetChild("InfoButton")
			self.infoBtn.SAFE_SetEvent(self.Info)
			# self.startBtn.SAFE_SetStringEvent("MOUSE_LEFT_DOWN", self.StartSpin)
			self.itemSlots = self.GetChild("ItemSlots")
			self.itemSlots.SetOverInItemEvent(ui.__mem_func__(self.__OnOverInItem))
			self.itemSlots.SetOverOutItemEvent(ui.__mem_func__(self.__OnOverOutItem))
		except:
			import exception
			exception.Abort("WheelOfFrightWindow.LoadWindow.BindObject")

		self.sliceImgList = []
		for x in xrange(10):
			img = self.GetChild("Slice%d" % (x + 1))
			img.SetAlpha(0.0)
			img.Show()
			self.sliceImgList.append(img)

		start, end, add = -18, 18, 36
		self.slicesPos = []
		for x in xrange(10):
			dX = start + (add * x)
			dY = end + (add * x)
			dA = dX + end
			self.slicesPos.append([dX, dY, dA])

	def Info(self):
		import constInfo
		app.ShellExecute("https://%s/l/Halloween" % constInfo.DOMAIN, False)

	def StartSpin(self):
		net.SendChatPacket("/halloween_minigame")

	def Spin(self, spins, items):
		self.pointer.Show()
		self.startBtn.Hide()
		self.spins = spins
		tchat("Spin(%d, %s)" % (spins, items))
		self.spin = True
		self.degree = 0
		self.endDegree = app.GetRandom(-12, 12) + spins * 36
		self.totalDegree = 0

		itemList = items.split("#")
		x = 0
		self.itemsArr = []
		for item in itemList:
			vnum, count = item.split("|")
			self.itemSlots.SetItemSlot(x, int(vnum), int(count))
			self.itemsArr.append([int(vnum), int(count)])
			x += 1

	def RenderSlices(self):
		for i in range(len(self.sliceImgList)):
			if self.degree >= self.slicesPos[i][0] and self.degree <= self.slicesPos[i][1]:
				self.sliceImgList[i].SetAlpha(1.0)
			else:
				self.sliceImgList[i].SetAlpha(0.5)

	def OnUpdate(self):
		if not self.spin:
			return

		self.pointer.SetRotation(self.degree)
		self.RenderSlices()

		slice1 = 36
		move = 0

		if self.totalDegree + slice1*4 >= self.endDegree:
			move = 0.7
		if self.totalDegree + slice1*6 >= self.endDegree:
			move = 1
		elif self.totalDegree + slice1*10 >= self.endDegree:
			move = 2
		elif self.totalDegree + slice1*18 >= self.endDegree:
			move = 3
		elif self.totalDegree + slice1*30 >= self.endDegree:
			move = 4
		else:
			move = 5

		self.degree += move
		self.totalDegree += move

		if self.degree >= 360 - 18:
			self.degree = -18

		if self.totalDegree >= self.endDegree:
			self.spin = False
			# self.pointer.Hide()
			# self.startBtn.Show()
			idx = self.spins - int(self.spins / 10)*10
			self.successWnd = NotificationWindow(self)
			self.successWnd.SetData(self.itemsArr[idx][0], self.itemsArr[idx][1])
			self.successWnd.Open()

	def __OnOverInItem(self, slotIndex):
		if self.tooltipItem:
			self.tooltipItem.SetItemToolTip(self.itemsArr[slotIndex][0])

	def __OnOverOutItem(self):
		if self.tooltipItem:
			self.tooltipItem.HideToolTip()

	def Open(self):
		self.Show()

	def Close(self):
		self.Hide()

	def OnPressEscapeKey(self):
		self.Close()
		return True

	def Reset(self):
		self.pointer.Hide()
		self.startBtn.Show()
		# self.itemSlots.ClearSlot(0)

	def Destroy(self):
		self.ClearDictionary()
		self.pointer = None
		self.itemSlots = None
		self.sliceImgList = []
		self.spins = 0
		self.itemsArr = []
		self.successWnd = None
	
	def SetItemToolTip(self, itemTooltip):
		self.tooltipItem = itemTooltip
