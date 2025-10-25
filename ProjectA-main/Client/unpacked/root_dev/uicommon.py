import ui
import localeInfo
import app
import ime
import uiScriptLocale
import cfg
import constInfo
import uiToolTip
import wndMgr
import item

class ItemGrid:
	def __init__(self, width, height):
		self._width = width
		self._height = height
		self._grid = {}

	def width(self):
		return self._width

	def height(self):
		return self._height

	def add(self, pos, height, value):
		for i in xrange(height):
			self._grid[pos + i * self.width()] = value

	def get(self, pos):
		if pos in self._grid:
			return self._grid[pos]

		return None

	def items(self):
		return self._grid.items()

	def is_free(self, pos, height):
		for i in xrange(height):
			if (pos + self.width() * i) in self._grid:
				return False

		return True

	def find_free(self, height):
		for y in xrange(self.height() - (height - 1)):
			for x in xrange(self.width()):
				pos = x + y * self.width()
				if self.is_free(pos, height):
					return pos

		return -1

class ShopSellPopup(ui.Bar):
	def __init__(self):
		ui.Bar.__init__(self)
		
		self.isActiveSlide = False
		self.isActiveSlideOut = False
		self.endTime = 0
		self.wndWidth = 0
		self.ItemVnum = ""
		self.yStep = 0

		self.textLine = ui.TextLine()
		self.textLine.SetParent(self)
		self.textLine.SetWindowVerticalAlignCenter()
		self.textLine.SetVerticalAlignCenter()
		self.textLine.SetPosition(41, 0)
		self.textLine.Show()
		
		self.itemImage = ui.ImageBox()
		self.itemImage.SetParent(self)
		self.itemImage.SetPosition(4, 4)
		self.itemImage.Show()

		
	def __del__(self):
		ui.Bar.__del__(self)

	def SetStep(self,Ypos):
		self.yStep = Ypos

	def SlideIn(self):
		self.Open()
		self.SetTop()
		self.isActiveSlide = True
		self.endTime = app.GetGlobalTimeStamp() + 5

	def Open(self):
		ui.Bar.Show(self)

	def Close(self):
		ui.Bar.Hide(self)

	def Destroy(self):
		self.Close()

	def GetItemVnum(self):
		return self.ItemVnum

	def SetItemVnum(self, vnum, count, price):
		vnum = int(vnum)
		item.SelectItem(1, 2, vnum)
		self.ItemVnum = vnum
		self.textLine.SetText(localeInfo.SHOP_SELL_NOTIFICATION % (" " + str(count) + "x " if count > 1 else "", item.GetItemName(), localeInfo.NumberToString(price)))
		self.itemImage.LoadImage(item.GetIconImageFileName())
		self.wndWidth = self.textLine.GetTextSize()[0] + 60
		wndHeigth = item.GetItemSize()[1] * 32 + 10
		self.SetSize(self.wndWidth, wndHeigth)
		self.SetPosition(-self.wndWidth, wndMgr.GetScreenHeight() - 250 - self.yStep)
	
	def OnMouseLeftButtonDown(self):
		if self.eventFunc:
			apply(self.eventFunc, self.eventArgs)

	def OnUpdate(self):
		if self.isActiveSlide and self.isActiveSlide == True:
			x, y = self.GetLocalPosition()
			if x < 0:
				stepAdd = x + 8
				if stepAdd > 0:
					stepAdd = 0
				self.SetPosition(stepAdd, y)
				
		if self.endTime - app.GetGlobalTimeStamp() <= 0 and self.isActiveSlideOut == False and self.isActiveSlide == True:
			self.isActiveSlide = False
			self.isActiveSlideOut = True
				
		if self.isActiveSlideOut and self.isActiveSlideOut == True:
			x, y = self.GetLocalPosition()
			if x > -(self.wndWidth):
				stepAdd = x - 8
				if stepAdd < -(self.wndWidth):
					stepAdd = -(self.wndWidth)
				self.SetPosition(stepAdd, y)
				
			if x <= -(self.wndWidth):
				self.isActiveSlideOut = False
				self.Close()


class OnlinePopup(ui.Bar):
	def __init__(self):
		ui.Bar.__init__(self)
		
		self.isActiveSlide = False
		self.isActiveSlideOut = False
		self.endTime = 0
		self.wndWidth = 0
		self.userName = ""
		self.yStep = 0
		self.userState = "online"

		self.textLine = ui.TextLine()
		self.textLine.SetParent(self)
		self.textLine.SetWindowHorizontalAlignCenter()
		self.textLine.SetWindowVerticalAlignCenter()
		self.textLine.SetHorizontalAlignCenter()
		self.textLine.SetVerticalAlignCenter()
		self.textLine.SetPosition(10, 0)
		self.textLine.Show()
		
		self.onlineImage = ui.ImageBox()
		self.onlineImage.SetParent(self)
		self.onlineImage.SetPosition(8, 3)
		self.onlineImage.LoadImage("d:/ymir work/ui/game/windows/messenger_list_online.sub")
		self.onlineImage.SAFE_SetStringEvent("MOUSE_OVER_IN", self.__Hover)
		self.onlineImage.Show()

		
	def __del__(self):
		ui.Bar.__del__(self)

	def SetStep(self,Ypos):
		self.yStep = Ypos

	def SlideIn(self):
		self.Open()
		self.SetTop()

		self.isActiveSlide = True
		self.endTime = app.GetGlobalTimeStamp() + 5

	def __Hover(self):
		self.endTime = app.GetGlobalTimeStamp() + 5

	def Open(self):
		ui.Bar.Show(self)

	def Close(self):
		ui.Bar.Hide(self)

	def Destroy(self):
		self.Close()

	def GetUserName(self):
		return self.userName

	def GetUserState(self):
		return self.userState

	def SetUserName(self, name, state):
		self.userName = name
		self.userState = state
		self.textLine.SetText("%s" % name)
		self.onlineImage.LoadImage("d:/ymir work/ui/game/windows/messenger_list_%s.sub" % state)
		self.wndWidth = self.textLine.GetTextSize()[0] + 40
		self.SetSize(self.wndWidth, 25)
		self.SetPosition(-self.wndWidth, wndMgr.GetScreenHeight() - 200 - self.yStep)
	
	def OnMouseLeftButtonDown(self):
		if self.eventFunc:
			apply(self.eventFunc, self.eventArgs)

	def OnUpdate(self):
		if self.isActiveSlide and self.isActiveSlide == True:
			x, y = self.GetLocalPosition()
			if x < 0:
				stepAdd = x + 8
				if stepAdd > 0:
					stepAdd = 0
				self.SetPosition(stepAdd, y)
				
		if self.endTime - app.GetGlobalTimeStamp() <= 0 and self.isActiveSlideOut == False and self.isActiveSlide == True:
			self.isActiveSlide = False
			self.isActiveSlideOut = True
				
		if self.isActiveSlideOut and self.isActiveSlideOut == True:
			x, y = self.GetLocalPosition()
			if x > -(self.wndWidth):
				stepAdd = x - 8
				if stepAdd < -(self.wndWidth):
					stepAdd = -(self.wndWidth)
				self.SetPosition(stepAdd, y)
				
			if x <= -(self.wndWidth):
				self.isActiveSlideOut = False
				self.Close()

class WarningQuestionDialog(ui.ThinBoard):

	Y_BORDER = 8
	X_BORDER = 8
	BOARD_WIDTH = 225

	def __init__(self):
		ui.ThinBoard.__init__(self)
		self.SetSize(self.BOARD_WIDTH, 0)
		self.AddFlag("float")
		self.AddFlag("movable")
		self.AddFlag("attach")

		self.yesEvent = None
		self.yesArgs = None
		self.noEvent = None
		self.noArgs = None

		imgWarning = ui.ImageBox()
		imgWarning.AddFlag("not_pick")
		imgWarning.SetParent(self)
		imgWarning.LoadImage("d:/ymir work/ui/game/warning.tga")
		imgWarning.SetPosition(10, self.Y_BORDER)
		imgWarning.Show()
		self.imgWarning = imgWarning

		wndText = ui.MultiTextLine()
		wndText.SetParent(self)
		wndText.SetPosition(imgWarning.GetRight() + 8, self.Y_BORDER)
		wndText.SetWidth(self.GetWidth() - wndText.GetLeft() - self.X_BORDER)
		wndText.Show()
		self.wndText = wndText

		btnYes = ui.Button()
		btnYes.SetParent(self)
		btnYes.SetUpVisual("d:/ymir work/ui/public/Large_Button_01.sub")
		btnYes.SetOverVisual("d:/ymir work/ui/public/Large_Button_02.sub")
		btnYes.SetDownVisual("d:/ymir work/ui/public/Large_Button_03.sub")
		btnYes.SetPosition(self.GetWidth() * 1 / 4 - btnYes.GetWidth() / 2, self.Y_BORDER + 4 + btnYes.GetHeight())
		btnYes.SetWindowVerticalAlignBottom()
		btnYes.SetText(localeInfo.YES)
		btnYes.SAFE_SetEvent(self.OnClickYesButton)
		btnYes.Show()
		self.btnYes = btnYes

		btnNo = ui.Button()
		btnNo.SetParent(self)
		btnNo.SetUpVisual("d:/ymir work/ui/public/Large_Button_01.sub")
		btnNo.SetOverVisual("d:/ymir work/ui/public/Large_Button_02.sub")
		btnNo.SetDownVisual("d:/ymir work/ui/public/Large_Button_03.sub")
		btnNo.SetPosition(self.GetWidth() * 3 / 4 - btnNo.GetWidth() / 2, self.Y_BORDER + 4 + btnNo.GetHeight())
		btnNo.SetWindowVerticalAlignBottom()
		btnNo.SetText(localeInfo.NO)
		btnNo.SAFE_SetEvent(self.OnClickNoButton)
		btnNo.Show()
		self.btnNo = btnNo

	def SetText(self, text):
		self.wndText.SetText(text)
		self.imgWarning.SetPosition(self.imgWarning.GetLeft(), max(self.Y_BORDER, self.wndText.GetTop() + (self.wndText.GetRealHeight() - self.imgWarning.GetHeight()) / 2))

		self.SetSize(self.GetWidth(), self.wndText.GetBottom() + 5 + 24 + 20)
		self.UpdateRect()

	def SAFE_SetYesEvent(self, eventFunc, *args):
		self.yesEvent = ui.__mem_func__(eventFunc)
		self.yesArgs = args

	def SAFE_SetNoEvent(self, eventFunc, *args):
		self.noEvent = ui.__mem_func__(eventFunc)
		self.noArgs = args

	def Open(self):
		self.Show()
		self.SetTop()
		self.SetCenterPosition()

	def Close(self):
		self.Hide()

	def OnClickYesButton(self):
		self.Close()
		if self.yesEvent:
			apply(self.yesEvent, self.yesArgs)

	def OnClickNoButton(self):
		self.Close()
		if self.noEvent:
			apply(self.noEvent, self.noArgs)

class PopupDialog(ui.ScriptWindow):

	def __init__(self):
		ui.ScriptWindow.__init__(self)
		self.__LoadDialog()
		self.acceptEvent = lambda *arg: None

		self.button_text = ""
		self.is_autoclose = False
		self.autoclose_timer = 0

	def __del__(self):
		ui.ScriptWindow.__del__(self)

	def __LoadDialog(self):
		try:
			PythonScriptLoader = ui.PythonScriptLoader()
			PythonScriptLoader.LoadScriptFile(self, "UIScript/PopupDialog.py")

			self.board = self.GetChild("board")
			self.message = self.GetChild("message")
			self.acceptButton = self.GetChild("accept")
			self.acceptButton.SetEvent(ui.__mem_func__(self.Close))

		except:
			import exception
			exception.Abort("PopupDialog.LoadDialog.BindObject")

	def Open(self):
		self.SetCenterPosition()
		self.SetTop()
		self.Show()

		if self.is_autoclose:
			self.autoclose_timer = app.GetTime() + constInfo.DIALOG_REMAINING_TIME

		buttonText = self.acceptButton.GetText( )

		if not buttonText:
			self.SetButtonName( uiScriptLocale.OK )

	def Close(self):
		self.Hide()
		self.acceptEvent()

		try: # avoiding ReferenceError weakly-referenced object no longer exists
			self.SetButtonName(self.button_text)
			self.is_autoclose = False
		except:
			pass

	def Destroy(self):
		self.Close()
		self.ClearDictionary()
		ui.ScriptWindow.Destroy(self)

	def SetWidth(self, width):
		height = self.board.GetHeight()
		self.message.SetWidth(width - 25 * 2)
		self.board.SetSize(width, height)
		self.SetSize(self.board.GetRealWidth(), self.board.GetRealHeight())
		self.SetCenterPosition()
		self.UpdateRect()
		self.UpdateHeight()

	def SetHeight(self, height):
		width = self.board.GetWidth()
		self.acceptButton.SetPosition(self.acceptButton.GetLeft(), 63 - 105 + height)
		self.board.SetSize(width, height)
		self.SetSize(self.board.GetRealWidth(), self.board.GetRealHeight())
		self.SetCenterPosition()
		self.UpdateRect()

	def SetText(self, text):
		self.message.SetText(text)
		self.UpdateHeight()

	def SetAcceptEvent(self, event):
		self.acceptEvent = event

	def SetButtonName(self, name):
		self.acceptButton.SetText(name)
		self.button_text = name

	"""
		Sets the is_autoclose flag which is used by the OnUpdate method
		to automatical close this dialog after a certain time. Call this
		method before the Open-method.
		
		Parameters
		----------
		flag: bool
			The autoclose flag.
	"""
	def SetAutoClose(self, flag):
		if not constInfo.DIALOG_REMAINING_TIME_ENABLED:
			return

		self.is_autoclose = flag

	def OnPressEscapeKey(self):
		self.Close()
		return True

	def OnIMEReturn(self):
		self.Close()
		return True

	"""
		Used for timing the autoclose functionallity.
		It also refresh the button-text by adding the remaining time.
		After the remaining time is 0 the dialog is closing and the
		is_autoclose flag is set to False again.
	"""
	def OnUpdate(self):
		if self.IsShow() and self.is_autoclose:
			current_time = app.GetTime()

			self.acceptButton.SetText(
				"%s (%.1f Sek)" % (self.button_text, self.autoclose_timer - current_time)
			)

			if self.autoclose_timer < current_time:
				self.Close()

	def UpdateHeight(self):
		height = self.message.GetRealHeight() + self.message.GetTop() + self.acceptButton.GetTop()
		self.board.SetSize(self.board.GetWidth(), height)
		self.SetSize(self.board.GetRealWidth(), self.board.GetRealHeight())
		self.UpdateRect()
		self.SetCenterPosition()

def IsUniquePopupDialog(name):
	return int(cfg.Get(cfg.SAVE_UNIQUE, name.lower(), "0")) == 0

def SetUniquePopupDialog(name):
	cfg.Set(cfg.SAVE_UNIQUE, name.lower(), "1")

class UniquePopupDialog(ui.ScriptWindow):

	def __init__(self):
		ui.ScriptWindow.__init__(self)
		self.__LoadDialog()
		self.acceptEvent = lambda *arg: None
		self.unqiueName = ""

	def __del__(self):
		ui.ScriptWindow.__del__(self)

	def __LoadDialog(self):
		try:
			PythonScriptLoader = ui.PythonScriptLoader()
			PythonScriptLoader.LoadScriptFile(self, "UIScript/UniquePopupDialog.py")

			self.board = self.GetChild("board")
			self.message = self.GetChild("message")
			self.neverAgain = self.GetChild("never_again")
			self.acceptButton = self.GetChild("accept")
			self.acceptButton.SetEvent(ui.__mem_func__(self.Close))

		except:
			import exception
			exception.Abort("PopupDialog.LoadDialog.BindObject")

	def Open(self, unqiueName = ""):
		self.unqiueName = unqiueName
		self.SetCenterPosition()
		self.SetTop()
		self.Show()

	def Close(self):
		if self.unqiueName and self.neverAgain.IsChecked():
			SetUniquePopupDialog(self.unqiueName)

		self.Hide()
		self.acceptEvent()

	def Destroy(self):
		self.Close()
		self.ClearDictionary()
		ui.ScriptWindow.Destroy(self)

	def SetWidth(self, width):
		height = self.GetHeight()
		self.SetSize(width, height)
		self.messsage.SetWidth(width)
		self.UpdateHeight()

	def SetText(self, text):
		self.message.SetText(text)
		self.UpdateHeight()

	def UpdateHeight(self):
		newHeight = self.message.GetRealHeight() + 100
		self.SetSize(self.GetWidth(), newHeight)
		self.board.SetSize(self.GetWidth(), newHeight)
		self.SetCenterPosition()
		self.UpdateRect()

	def SetAcceptEvent(self, event):
		self.acceptEvent = event

	def SetButtonName(self, name):
		self.acceptButton.SetText(ButtonName)

	def OnPressEscapeKey(self):
		self.Close()
		return True

	def OnIMEReturn(self):
		self.Close()
		return True

class InputDialog(ui.ScriptWindow):

	def __init__(self):
		ui.ScriptWindow.__init__(self)

		self.__CreateDialog()

	def __del__(self):
		ui.ScriptWindow.__del__(self)

	def __CreateDialog(self):

		pyScrLoader = ui.PythonScriptLoader()
		pyScrLoader.LoadScriptFile(self, "uiscript/inputdialog.py")

		getObject = self.GetChild
		self.board = getObject("Board")
		self.acceptButton = getObject("AcceptButton")
		self.cancelButton = getObject("CancelButton")
		self.inputSlot = getObject("InputSlot")
		self.inputValue = getObject("InputValue")

	def Open(self):
		self.inputValue.SetFocus()
		self.SetCenterPosition()
		self.SetTop()
		self.Show()

	def Close(self):
		self.ClearDictionary()
		self.board = None
		self.acceptButton = None
		self.cancelButton = None
		self.inputSlot = None
		self.inputValue = None
		self.Hide()

	def SoftClose(self):
		self.inputValue.KillFocus()
		self.Hide()

	def SetTitle(self, name):
		self.board.SetTitleName(name)

	def SetNumberMode(self):
		self.inputValue.SetNumberMode()

	def SetSecretMode(self):
		self.inputValue.SetSecret()

	def SetFocus(self):
		self.inputValue.SetFocus()

	def SetMaxLength(self, length):
		width = length * 6 + 10 + 50
		self.SetBoardWidth(max(width + 5 * 2, 160))
		self.SetSlotWidth(width)
		self.inputValue.SetMax(length)

	def SetSlotWidth(self, width):
		self.inputSlot.SetSize(width, self.inputSlot.GetHeight())
		self.inputValue.SetSize(width, self.inputValue.GetHeight())
		if self.IsRTL():
			self.inputValue.SetPosition(self.inputValue.GetWidth(), 0)

	def SetBoardWidth(self, width):
		self.board.SetSize(max(width, 160), self.board.GetHeight())	
		self.SetSize(self.board.GetRealWidth(), self.GetHeight())
		if self.IsRTL():
			self.board.SetPosition(self.board.GetWidth(), 0)
		self.UpdateRect()

	def SetAcceptEvent(self, event):
		self.acceptButton.SetEvent(event)
		self.inputValue.SetReturnEvent(event)

	def SetCancelEvent(self, event):
		self.board.SetCloseEvent(event)
		self.cancelButton.SetEvent(event)
		self.inputValue.SetEscapeEvent(event)

	def SetAcceptText(self, text):
		self.acceptButton.SetText(text)

	def ClearText(self):
		self.inputValue.SetText("")

	def SetText(self, text):
		self.inputValue.SetText(text)

	def GetText(self):
		return self.inputValue.GetText()

class InputDialogWithDescription(InputDialog):

	def __init__(self):
		ui.ScriptWindow.__init__(self)

		self.__CreateDialog()

	def __del__(self):
		InputDialog.__del__(self)

	def __CreateDialog(self):

		pyScrLoader = ui.PythonScriptLoader()
		if localeInfo.IsARABIC() :
			pyScrLoader.LoadScriptFile(self, uiScriptLocale.LOCALE_UISCRIPT_PATH + "inputdialogwithdescription.py")
		else:
			pyScrLoader.LoadScriptFile(self, "uiscript/inputdialogwithdescription.py")

		try:
			getObject = self.GetChild
			self.board = getObject("Board")
			self.acceptButton = getObject("AcceptButton")
			self.cancelButton = getObject("CancelButton")
			self.inputSlot = getObject("InputSlot")
			self.inputValue = getObject("InputValue")
			self.description = getObject("Description")

		except:
			import exception
			exception.Abort("InputDialogWithDescription.LoadBoardDialog.BindObject")

	def SetDescription(self, text):
		self.description.SetText(text)

class InputDialogMultilineDescription(InputDialog):
	def __init__(self):
		ui.ScriptWindow.__init__(self)

		self.__CreateDialog()

	def __del__(self):
		InputDialog.__del__(self)

	def __CreateDialog(self):

		pyScrLoader = ui.PythonScriptLoader()
		if localeInfo.IsARABIC() :
			pyScrLoader.LoadScriptFile(self, uiScriptLocale.LOCALE_UISCRIPT_PATH + "inputdialogmultilinedescription.py")
		else:
			pyScrLoader.LoadScriptFile(self, "uiscript/inputdialogmultilinedescription.py")

		try:
			getObject = self.GetChild
			self.board = getObject("Board")
			self.acceptButton = getObject("AcceptButton")
			self.cancelButton = getObject("CancelButton")
			self.inputSlot = getObject("InputSlot")
			self.inputValue = getObject("InputValue")
			self.description = getObject("Description")

		except:
			import exception
			exception.Abort("InputDialogMultilineDescription.LoadBoardDialog.BindObject")

	def SetDescription(self, text):
		self.description.SetText(text)

class InputDialogWithDescription2(InputDialog):

	def __init__(self):
		ui.ScriptWindow.__init__(self)

		self.__CreateDialog()

	def __del__(self):
		InputDialog.__del__(self)

	def __CreateDialog(self):

		pyScrLoader = ui.PythonScriptLoader()
		pyScrLoader.LoadScriptFile(self, "uiscript/inputdialogwithdescription2.py")

		try:
			getObject = self.GetChild
			self.board = getObject("Board")
			self.acceptButton = getObject("AcceptButton")
			self.cancelButton = getObject("CancelButton")
			self.inputSlot = getObject("InputSlot")
			self.inputValue = getObject("InputValue")
			self.description1 = getObject("Description1")
			self.description2 = getObject("Description2")

		except:
			import exception
			exception.Abort("InputDialogWithDescription.LoadBoardDialog.BindObject")

	def SetDescription1(self, text):
		self.description1.SetText(text)

	def SetDescription2(self, text):
		self.description2.SetText(text)

class DoubleInputDialogWithDescription(ui.ScriptWindow):

	def __init__(self):
		ui.ScriptWindow.__init__(self)

		self.__CreateDialog()

	def __del__(self):
		ui.ScriptWindow.__del__(self)

	def __CreateDialog(self):

		pyScrLoader = ui.PythonScriptLoader()
		pyScrLoader.LoadScriptFile(self, "uiscript/doubleinputdialogwithdescription.py")

		getObject = self.GetChild
		self.board = getObject("Board")
		self.acceptButton = getObject("AcceptButton")
		self.cancelButton = getObject("CancelButton")
		self.inputSlot = [getObject("InputSlot1"), getObject("InputSlot2")]
		self.inputValue = [getObject("InputValue1"), getObject("InputValue2")]
		self.description = [getObject("Description1"), getObject("Description2")]
		self.maxLen = [0, 0]

		self.inputValue[0].SAFE_SetReturnEvent(self.inputValue[1].SetFocus)
		self.inputValue[0].SetTabEvent(ui.__mem_func__(self.inputValue[1].SetFocus))

	def Open(self):
		self.SetFocus()
		self.SetCenterPosition()
		self.SetTop()
		self.Show()

	def Close(self):
		self.ClearDictionary()
		self.board = None
		self.acceptButton = None
		self.cancelButton = None
		self.inputSlot = None
		self.inputValue = None
		self.Hide()

	def SoftClose(self):
		for i in xrange(2):
			self.inputValue[i].KillFocus()
		self.Hide()

	def SetTitle(self, name):
		self.board.SetTitleName(name)

	def SetNumberMode(self, index = -1):
		if index == -1:
			for i in xrange(2):
				self.SetNumberMode(i)
		else:
			self.inputValue[index].SetNumberMode()

	def SetSecretMode(self, index = -1):
		if index == -1:
			for i in xrange(2):
				self.SetSecretMode(i)
		else:
			self.inputValue[index].SetSecret()

	def SetFocus(self, index = 0):
		self.inputValue[index].SetFocus()

	def SetMaxLength(self, length, index = -1):
		if index == -1:
			for i in xrange(2):
				self.SetMaxLength(length, i)
		else:
			width = length * 6 + 10
			self.maxLen[index] = width
			maxWidth = max(self.maxLen[1 - index], width)
			self.SetBoardWidth(max(maxWidth + 50, 160))
			self.SetSlotWidth(width, index)
			self.inputValue[index].SetMax(length)

	def SetSlotWidth(self, width, index = -1):
		if index == -1:
			for i in xrange(2):
				self.SetSlotWidth(width, i)
		else:
			self.inputSlot[index].SetSize(width, self.inputSlot[index].GetHeight())
			self.inputValue[index].SetSize(width, self.inputValue[index].GetHeight())
			if self.IsRTL():
				self.inputValue[index].SetPosition(self.inputValue[index].GetWidth(), 0)

	def GetDisplayWidth(self, index):
		return self.inputSlot[index].GetWidth()

	def SetDisplayWidth(self, width, index = -1):
		if index == -1:
			for i in xrange(2):
				self.SetEditWidth(width, i)
		else:
			self.maxLen[index] = width
			maxWidth = max(self.maxLen[1 - index], width)
			self.SetBoardWidth(max(maxWidth + 50, 160))
			self.SetSlotWidth(width, index)

	def SetBoardWidth(self, width):
		self.SetSize(max(width + 50, 160), self.GetHeight())
		self.board.SetSize(max(width + 50, 160), self.GetHeight())	
		if self.IsRTL():
			self.board.SetPosition(self.board.GetWidth(), 0)
		self.UpdateRect()

	def SetAcceptEvent(self, event):
		self.acceptButton.SetEvent(event)
		self.inputValue[1].SetReturnEvent(event)

	def SetCancelEvent(self, event):
		self.board.SetCloseEvent(event)
		self.cancelButton.SetEvent(event)
		for i in xrange(2):
			self.inputValue[i].SetEscapeEvent(event)

	def GetText(self, index):
		return self.inputValue[index].GetText()

	def SetDescription(self, text, index = -1):
		if index == -1:
			for i in xrange(2):
				self.SetDescription(text, i)
		else:
			self.description[index].SetText(text)

class QuestionDialog(ui.ScriptWindow):

	def __init__(self, loadPy = True):
		ui.ScriptWindow.__init__(self)
		self.normalCloseEvent = None
		self.allowReturnKey = None
		if loadPy:
			self.__CreateDialog()

	def __del__(self):
		ui.ScriptWindow.__del__(self)

	def __CreateDialog(self):
		pyScrLoader = ui.PythonScriptLoader()
		pyScrLoader.LoadScriptFile(self, "uiscript/questiondialog.py")

		self.board = self.GetChild("board")
		self.textLine = self.GetChild("message")
		self.acceptButton = self.GetChild("accept")
		self.cancelButton = self.GetChild("cancel")

		self.allowReturnKey = True

	def SetReturnKeyAvail(self, isAvail):
		self.allowReturnKey = isAvail

	def Open(self):
		constInfo.HOTFIX_TEMP_IGNORE_CHAT_OPEN = True
		self.SetCenterPosition()
		self.SetTop()
		self.Show()

	def Close(self):
		constInfo.HOTFIX_TEMP_IGNORE_CHAT_OPEN = False
		self.Hide()

	def SetWidth(self, width):
		height = self.GetHeight()
		self.SetSize(width, height)
		self.board.SetSize(width, height)
		self.SetCenterPosition()
		self.UpdateRect()

	def SAFE_SetAcceptEvent(self, event, *args):
		apply(self.acceptButton.SAFE_SetEvent, (event,) + args)

	def SAFE_SetCancelEvent(self, event, *args):
		apply(self.cancelButton.SAFE_SetEvent, (event,) + args)

	def SetAcceptEvent(self, event):
		self.acceptButton.SetEvent(event)

	def SetCancelEvent(self, event):
		self.cancelButton.SetEvent(event)

	def SetText(self, text):
		self.textLine.SetText(text)

	def SetAcceptText(self, text):
		self.acceptButton.SetText(text)

	def SetCancelText(self, text):
		self.cancelButton.SetText(text)

	def SetNormalCloseEvent(self, closeEvent):
		self.normalCloseEvent = closeEvent

	def Accept(self):
		try:
			self.acceptButton.CallEvent()
		except:
			pass

	def OnPressReturnKey(self):
		if self.allowReturnKey:
			self.acceptButton.CallEvent()
			return True

		return False

	def OnPressEscapeKey(self):
		if self.normalCloseEvent:
			self.normalCloseEvent()
		else:
			self.cancelButton.CallEvent()
		return True

class QuestionDialog2(QuestionDialog):

	def __init__(self):
		self.allowReturnKey = None
		QuestionDialog.__init__(self, False)
		self.__CreateDialog()
		

	def __del__(self):
		QuestionDialog.__del__(self)

	def __CreateDialog(self):
		pyScrLoader = ui.PythonScriptLoader()
		pyScrLoader.LoadScriptFile(self, "uiscript/questiondialog2.py")

		self.board = self.GetChild("board")
		self.textLine1 = self.GetChild("message1")
		self.textLine2 = self.GetChild("message2")
		self.acceptButton = self.GetChild("accept")
		self.cancelButton = self.GetChild("cancel")

	def SetText1(self, text):
		self.textLine1.SetText(text)

	def SetText2(self, text):
		self.textLine2.SetText(text)

class QuestionDialogWithDescription(QuestionDialog):

	def __init__(self):
		QuestionDialog.__init__(self, False)
		self.__CreateDialog()

	def __del__(self):
		QuestionDialog.__del__(self)

	def __CreateDialog(self):
		pyScrLoader = ui.PythonScriptLoader()
		pyScrLoader.LoadScriptFile(self, "uiscript/questiondialogwithdescription.py")

		self.board = self.GetChild("board")
		self.textLine = self.GetChild("message")
		self.acceptButton = self.GetChild("accept")
		self.cancelButton = self.GetChild("cancel")

	def SetText(self, text):
		self.textLine.SetText(text)
		self.acceptButton.SetPosition(self.acceptButton.GetLeft(), self.textLine.GetBottom() + 10)
		self.cancelButton.SetPosition(self.cancelButton.GetLeft(), self.textLine.GetBottom() + 10)

		self.SetSize(self.GetWidth(), self.textLine.GetBottom() + 50)
		self.board.SetSize(self.GetWidth(), self.GetHeight())

class QuestionDialog3(ui.ScriptWindow):

	def __init__(self):
		ui.ScriptWindow.__init__(self)
		self.__CreateDialog()

	def __del__(self):
		ui.ScriptWindow.__del__(self)

	def __CreateDialog(self):
		pyScrLoader = ui.PythonScriptLoader()
		pyScrLoader.LoadScriptFile(self, "uiscript/questiondialog3.py")

		self.board = self.GetChild("board")
		self.textLine = self.GetChild("message")
		self.accept1Button = self.GetChild("accept1")
		self.accept2Button = self.GetChild("accept2")
		self.cancelButton = self.GetChild("cancel")

	def Open(self):
		constInfo.HOTFIX_TEMP_IGNORE_CHAT_OPEN = True
		self.SetCenterPosition()
		self.SetTop()
		self.Show()

	def Close(self):
		constInfo.HOTFIX_TEMP_IGNORE_CHAT_OPEN = False
		self.Hide()

	def SetWidth(self, width):
		height = self.GetHeight()
		self.SetSize(width, height)
		self.board.SetSize(width, height)
		self.SetCenterPosition()
		self.UpdateRect()

	def SAFE_SetAccept1Event(self, event, *args):
		apply(self.accept1Button.SAFE_SetEvent, (event,) + args)

	def SAFE_SetAccept2Event(self, event, *args):
		apply(self.accept2Button.SAFE_SetEvent, (event,) + args)

	def SAFE_SetCancelEvent(self, event):
		self.cancelButton.SAFE_SetEvent(event)

	def SetAccept1Event(self, event, *args):
		apply(self.accept1Button.SetEvent, (event,) + args)

	def SetAccept2Event(self, event, *args):
		apply(self.accept2Button.SetEvent, (event,) + args)

	def SetCancelEvent(self, event):
		self.cancelButton.SetEvent(event)

	def SetText(self, text):
		self.textLine.SetText(text)

	def SetAccept1Text(self, text):
		self.accept1Button.SetText(text)

	def SetAccept2Text(self, text):
		self.accept2Button.SetText(text)

	def SetCancelText(self, text):
		self.cancelButton.SetText(text)

	def OnPressEscapeKey(self):
		self.Close()
		return True

	def OnPressReturnKey(self):
		self.accept1Button.CallEvent()
		return True

class QuestionDialogWithTimeLimit(QuestionDialog2):

	def __init__(self):
		ui.ScriptWindow.__init__(self)

		self.__CreateDialog()
		self.endTime = 0

	def __del__(self):
		QuestionDialog2.__del__(self)

	def __CreateDialog(self):
		pyScrLoader = ui.PythonScriptLoader()
		pyScrLoader.LoadScriptFile(self, "uiscript/questiondialog2.py")

		self.board = self.GetChild("board")
		self.textLine1 = self.GetChild("message1")
		self.textLine2 = self.GetChild("message2")
		self.acceptButton = self.GetChild("accept")
		self.cancelButton = self.GetChild("cancel")

	def Open(self, msg, timeout):
		self.SetCenterPosition()
		self.SetTop()
		self.Show()

		self.SetText1(msg)
		self.endTime = app.GetTime() + timeout

	def OnUpdate(self):
		leftTime = max(0, self.endTime - app.GetTime())
		self.SetText2(localeInfo.UI_LEFT_TIME % (leftTime))

class QuestionDialogMultiLine(ui.ScriptWindow):

	def __init__(self):
		ui.ScriptWindow.__init__(self)
		self.__CreateDialog()

	def __del__(self):
		ui.ScriptWindow.__del__(self)

	def __CreateDialog(self):
		pyScrLoader = ui.PythonScriptLoader()
		pyScrLoader.LoadScriptFile(self, "uiscript/questiondialogmultiline.py")

		self.board = self.GetChild("board")
		self.textLine = self.GetChild("message")
		self.acceptButton = self.GetChild("accept")
		self.cancelButton = self.GetChild("cancel")

	def Open(self):
		self.SetCenterPosition()
		self.SetTop()
		self.Show()

	def Close(self):
		self.Hide()

	def SetWidth(self, width):
		height = self.GetHeight()
		self.SetSize(width, height)
		self.board.SetSize(width, height)
		self.SetCenterPosition()
		self.UpdateRect()

	def SAFE_SetAcceptEvent(self, event, *args):
		apply(self.acceptButton.SAFE_SetEvent, (event,) + args)

	def SAFE_SetCancelEvent(self, event, *args):
		apply(self.cancelButton.SAFE_SetEvent, (event,) + args)

	def SetAcceptEvent(self, event, *args):
		apply(self.acceptButton.SetEvent, (event,) + args)

	def SetCancelEvent(self, event, *args):
		apply(self.cancelButton.SetEvent, (event,) + args)

	def SetText(self, text):
		self.textLine.SetText(text)
		self.UpdateSize()

	def SetAcceptText(self, text):
		self.acceptButton.SetText(text)

	def SetCancelText(self, text):
		self.cancelButton.SetText(text)

	def Accept(self):
		self.acceptButton.SimulClick()

	def UpdateSize(self):
		self.acceptButton.SetPosition(self.acceptButton.GetLeft(), self.textLine.GetBottom() + 15)
		self.cancelButton.SetPosition(self.cancelButton.GetLeft(), self.textLine.GetBottom() + 15)
		self.SetSize(self.GetWidth(), self.textLine.GetBottom() + 57)
		self.board.SetSize(self.GetWidth(), self.GetHeight())

	def OnPressEscapeKey(self):
		self.Close()
		return True

class MoneyInputDialog(ui.ScriptWindow):

	def __init__(self):
		ui.ScriptWindow.__init__(self)

		self.moneyHeaderText = localeInfo.MONEY_INPUT_DIALOG_SELLPRICE
		self.realMoneyHeaderText = localeInfo.MONEY_INPUT_DIALOG_RECVPRICE
		self.__CreateDialog()
		self.SetMaxLength(9)

	def __del__(self):
		ui.ScriptWindow.__del__(self)

	def __CreateDialog(self):

		pyScrLoader = ui.PythonScriptLoader()
		pyScrLoader.LoadScriptFile(self, "uiscript/moneyinputdialog.py")

		getObject = self.GetChild
		self.board = self.GetChild("board")
		self.acceptButton = getObject("AcceptButton")
		self.cancelButton = getObject("CancelButton")
		self.inputValue = getObject("InputValue")
		self.inputValue.SetNumberMode()
		self.inputValue.OnIMEUpdate = ui.__mem_func__(self.__OnValueUpdate)
		self.moneyText = getObject("MoneyValue")
		self.realMoneyText = self.GetChild2("RealMoneyValue")

	def Open(self, tax = 0):
		self.tax = tax
		self.inputValue.SetText("")
		self.inputValue.SetFocus()
		self.__OnValueUpdate()
		self.SetCenterPosition()
		self.SetTop()
		self.Show()

		if self.realMoneyText:
			if tax == 0:
				self.realMoneyText.Hide()
				self.acceptButton.SetPosition(self.acceptButton.GetLeft(), 106)
				self.cancelButton.SetPosition(self.cancelButton.GetLeft(), 106)
				self.SetSize(self.GetWidth(), 147)

	def Close(self):
		self.ClearDictionary()
		self.board = None
		self.acceptButton = None
		self.cancelButton = None
		self.inputValue = None
		self.Hide()

	def SetTitle(self, name):
		self.board.SetTitleName(name)

	def SetFocus(self):
		self.inputValue.SetFocus()

	def SetMaxLength(self, length):
		length = min(9, length)
		self.inputValue.SetMax(length)

	def SetMoneyHeaderText(self, text):
		self.moneyHeaderText = text

	def SetAcceptEvent(self, event):
		self.acceptButton.SetEvent(event)
		self.inputValue.OnIMEReturn = event

	def SetCancelEvent(self, event):
		self.board.SetCloseEvent(event)
		self.cancelButton.SetEvent(event)
		self.inputValue.OnPressEscapeKey = event

	def SetValue(self, value):
		value=str(value)
		self.inputValue.SetText(value)
		self.__OnValueUpdate()
		ime.MoveEnd()

	def GetText(self):
		return self.inputValue.GetText()

	def GetMoney(self):
		return int(self.__ConvertMoneyText(self.GetText()))

	def __ConvertMoneyText(self, text):
		resultText = text

		while resultText.find("k") != -1:
			pos = resultText.find("k")
			resultText = resultText[:pos] + "000" + resultText[pos+1:]

		return resultText

	def __OnValueUpdate(self):
		ui.EditLine.OnIMEUpdate(self.inputValue)

		text = self.inputValue.GetText()

		money = 0
		if text:
			money = self.GetMoney()

		self.moneyText.SetText(self.moneyHeaderText % localeInfo.NumberToMoneyString(money))
		if self.realMoneyText:
			self.realMoneyText.SetText(self.realMoneyHeaderText % (localeInfo.NumberToMoneyString(money * (100 - self.tax) / 100), self.tax))


import item, shop
class SellItemDialog(ui.ScriptWindow):
	def __init__(self):
		ui.ScriptWindow.__init__(self)
		self.length = 196
		self.__LoadWindow()

		self.itemVNum = 0
		self.sourceSlotPos = 0
		self.targetSlotPos = 0
		self.sellForAverage = False
		self.tax = 0
		self.average = 0
		# self.checkAverage = False
		self.setPrice = 0
		self.update = False

	def __del__(self):
		ui.ScriptWindow.__del__(self)

	def __LoadWindow(self):
		try:
			PythonScriptLoader = ui.PythonScriptLoader()
			PythonScriptLoader.LoadScriptFile(self, "UIScript/newofflineshopwindow_selldialog.py")
		except:
			import exception
			exception.Abort("NewOfflineShopSellItemDialog.LoadDialog.LoadObject")

		try:
			self.background = self.GetChild("background")
			self.btnSell 	= self.GetChild("button_sell")
			self.btnClose 	= self.GetChild("button_close")
			self.priceLine 		= self.GetChild("price_editline")
			self.realPrice 		= self.GetChild("real_price_text")
			# self.priceArrow 	= self.GetChild("price_arrow")
			# self.colorbar 		= self.GetChild("colorbar")
			self.itemIcon 		= self.GetChild("item_icon")
			self.itemName		= self.GetChild("item_name")
			self.btnAveragePrice = self.GetChild("button_set_avg_price")
			self.averagePriceText = self.GetChild("average_price_text")
		except:
			import exception
			exception.Abort("NewOfflineShopSellItemDialog.LoadDialog.BindObject")

		self.priceLine.SetFontName(localeInfo.UI_DEF_FONT_LARGE)
		# enable to not allow writing letters
		# self.priceLine.SetNumberMode()
		self.priceLine.OnIMEUpdate = self.__OnValueUpdate
		self.priceLine.SetMax(12)

		self.btnAveragePrice.SetToggleUpEvent(ui.__mem_func__(self.__OnSetForAverage), False)
		self.btnAveragePrice.SetToggleDownEvent(ui.__mem_func__(self.__OnSetForAverage), True)

		# cursor = ui.DragButton()
		# cursor.AddFlag("movable")
		# cursor.AddFlag("restrict_y")
		# cursor.SetParent(self.GetChild("colorbar"))
		# cursor.SetMoveEvent(ui.__mem_func__(self.__OnMove))
		# cursor.SetUpVisual("d:/ymir work/ui/game/offlineshop/tab_sell/arrow2.tga")
		# cursor.SetOverVisual("d:/ymir work/ui/game/offlineshop/tab_sell/arrow2.tga")
		# cursor.SetDownVisual("d:/ymir work/ui/game/offlineshop/tab_sell/arrow2.tga")
		# cursor.Show()
		# self.cursor = cursor
		# self.cursor.SetRestrictMovementArea(-7, 1, self.length + 18, 0)
		# self.pageSize = self.length - self.cursor.GetWidth()

		# (percentage, percentagePositive) = shop.GetSellMarginPercent()
		# tooltip = uiToolTip.ToolTip()
		# tooltip.HideToolTip()
		# tooltip.AppendDescription(localeInfo.OFFLINE_SHOP_AVG_INFO % (percentage, percentagePositive), 26)
		# self.GetChild("button_set_avg_price").SetToolTipWindow(tooltip)

	def __OnMove(self):
		if self.sellForAverage:
			self.__OnSetForAverage(False)
		self.priceLine.SetFocus()
		self.update = True

	def OnUpdate(self): # to avoid recursion
		if not self.average or self.sellForAverage or not self.update:
			return

		# pos = self.cursor.GetLocalPosition()[0] + 7
		# (percentage, percentagePositive) = shop.GetSellMarginPercent()
		# if constInfo.OFFLINE_SHOP_AVG_SHOW_POSITIVE_MARGIN:
		# 	min = float(self.average * (1.0 - (percentage / 100.0)))
		# 	max = float(self.average * (1.0 + (percentagePositive / 100.0)))
		# else:
		# 	min = float(self.average * (1.0 - (percentage / 100.0)))
		# 	max = float(self.average * (1.0 + (percentage / 100.0)))

		# price = (((max - min) * pos) / self.length) + min
		# self.SetValue(int(price))

	def __OnValueUpdate(self):
		ui.EditLine.OnIMEUpdate(self.priceLine)
		self.update = False

		money = 0
		if self.sellForAverage:
			money = self.average
			self.priceLine.SetText(str(money))
			self.priceLine.SetEndPosition()
		else:
			if self.priceLine.GetText():
				money = self.GetMoney()

		self.realPrice.SetText(localeInfo.NumberToMoneyString(money * (100 - self.tax) / 100))

		# (percentage, percentagePositive) = shop.GetSellMarginPercent()
		# if constInfo.OFFLINE_SHOP_AVG_SHOW_POSITIVE_MARGIN:
		# 	min = float(self.average * (1.0 - (percentage / 100.0)))
		# 	max = float(self.average * (1.0 + (percentagePositive / 100.0)))
		# else:
		# 	min = float(self.average * (1.0 - (percentage / 100.0)))
		# 	max = float(self.average * (1.0 + (percentage / 100.0)))

		# if max - min == 0:
		# 	pos = 0
		# else:
		# 	pos = (self.length * (money - min)) / (max - min)

		# if pos < 0:
		# 	pos = 0
		# elif pos > self.length:
		# 	pos = self.length

		# self.priceArrow.SetPosition(int(pos + 0.5) - 5, 1)
		# self.cursor.SetPosition(int(pos + 0.5) - 7, 1)

	def __OnSetForAverage(self, arg):
		if not self.average:
			self.sellForAverage = False
			self.btnAveragePrice.SetUp()
			return

		self.sellForAverage = arg
		if self.sellForAverage:
			self.btnAveragePrice.SetDown()
		else:
			self.btnAveragePrice.SetUp()
		self.__OnValueUpdate()

	def UpdateItemData(self):
		item.SelectItem(1, 2, self.itemVNum)
		self.itemIcon.LoadImage(item.GetIconImageFileName())
		itemNameText = item.GetItemName()
		self.itemName.SetText(itemNameText)
		# self.__SetCheckAverage()

	def Open(self, tax):
		self.UpdateItemData()

		self.averagePriceText.SetText(localeInfo.NumberToMoneyString(self.average))
		self.priceLine.SetText("")
		self.priceLine.SetFocus()
		self.tax = tax
		self.__OnValueUpdate()

		self.SetTop()
		self.SetCenterPosition()
		self.Show()

	def SetAcceptEvent(self, event):
		self.btnSell.SetEvent(event)
		self.priceLine.OnIMEReturn = event

	def SetCancelEvent(self, event):
		self.btnClose.SetEvent(event)
		self.priceLine.OnPressEscapeKey = event

	def GetText(self):
		return self.priceLine.GetText()

	def GetMoney(self):
		return int(self.__ConvertMoneyText(self.GetText()))

	def __ConvertMoneyText(self, text):
		resultText = text

		while resultText.find("k") != -1:
			pos = resultText.find("k")
			resultText = resultText[:pos] + "000" + resultText[pos+1:]

		return resultText

	def SetValue(self, value):
		self.priceLine.SetText(str(value))
		self.__OnValueUpdate()
		ime.MoveEnd()

	# def __SetCheckAverage(self):
	# 	if item.GetItemType() not in (item.ITEM_TYPE_WEAPON,item.ITEM_TYPE_ARMOR,item.ITEM_TYPE_BELT,item.ITEM_TYPE_DS,item.ITEM_TYPE_COSTUME,item.ITEM_TYPE_SKILLBOOK,item.ITEM_TYPE_SKILLFORGET,item.ITEM_TYPE_BLEND,item.ITEM_TYPE_SOUL):
	# 		self.checkAverage = True
	# 	else:
	# 		self.checkAverage = False
	# 	tchat("__SetCheckAverage (%d)" % self.checkAverage)

	def Close(self):
		self.ClearDictionary()
		self.background = None
		self.btnSell = None
		self.btnClose = None
		self.priceLine = None
		self.realPrice = None
		# self.priceArrow = None
		# self.colorbar = None
		self.itemIcon = None
		self.itemName = None
		self.btnAveragePrice = None
		self.averagePriceText = None
		# self.cursor = None
		self.Hide()


class ShopSellNotification(ui.BaseScriptWindow):

	def __init__(self):
		ui.BaseScriptWindow.__init__(self, "shopsellnotification")
		self.itemToolTip = uiToolTip.ItemToolTip()
		self.itemToolTip.HideToolTip()
		self.soldItemVnum = 0
		self.__LoadWindow()

	def __del__(self):
		ui.BaseScriptWindow.__del__(self)

	def __LoadWindow(self):
		try:
			self.board = self.GetChild("board")
			self.titlebar = self.GetChild("titlebar")
			self.GetChild("titlebar").SetCloseEvent(ui.__mem_func__(self.Close))
			self.message = self.GetChild("message")
			self.acceptButton = self.GetChild("accept")
		except:
			import exception
			exception.Abort("shopsellnotification.LoadDialog.BindObject")

		item.SelectItem(1, 2, 19)
		self.soldItem = ui.ImageBox()
		self.soldItem.SetParent(self.board)
		self.soldItem.SetWindowHorizontalAlignCenter()
		self.soldItem.SAFE_SetStringEvent("MOUSE_OVER_IN", self.__ShowToolTip)
		self.soldItem.SAFE_SetStringEvent("MOUSE_OVER_OUT", self.itemToolTip.HideToolTip)
		self.soldItem.LoadImage(item.GetIconImageFileName())
		self.soldItem.SetWindowVerticalAlignCenter()
		self.soldItem.SetPosition(0, 20)
		self.soldItem.Show()

	def Open(self):
		self.SetCenterPosition()
		self.SetTop()
		self.Show()

	def Close(self):
		self.Hide()
		self.itemToolTip.HideToolTip()

	def SetAcceptEvent(self,event,*arg):
		if self.acceptButton:
			self.acceptButton.SAFE_SetEvent(event,arg)

	def SetData(self, vnum, count, price):
		self.message.SetText(uiScriptLocale.SHOP_SELL_NOTIFICATION % (count, item.GetItemName(int(vnum)), localeInfo.NumberToString(int(price))))
		item.SelectItem(1, 2, int(vnum))
		self.itemToolTip.SetItemToolTip(int(vnum))
		self.soldItemVnum = int(vnum)
		self.soldItem.LoadImage(item.GetIconImageFileName())
		self.itemToolTip.HideToolTip()
		(widthI, heightI) = item.GetItemSize()
		self.acceptButton.SetPosition(self.acceptButton.GetLeft(), self.acceptButton.GetHeight() + 5)
		self.titlebar.SetWidth(self.board.GetWidth())
		self.board.SetSize(self.board.GetWidth(), 120 + (32 * heightI) )
		self.SetSize(self.GetWidth(), 120 + (32 * heightI) )

		# self.SetCenterPosition()
		self.UpdateRect()
		# tchat("Y:%d %d" % (self.GetGlobalPosition()[1], self.board.GetGlobalPosition()[1]))
		tchat("height: %d ,, %d" % (self.GetHeight(), self.board.GetHeight()))

	def OnPressEscapeKey(self):
		self.Close()
		return True

	def __ShowToolTip(self):
		self.itemToolTip.SetItemToolTip(self.soldItemVnum)

