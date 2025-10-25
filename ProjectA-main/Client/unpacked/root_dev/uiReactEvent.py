import ui
import chat
import net
import uiTip
import app
import localeInfo
import emotion

IMAGE_PATH = "d:/ymir work/ui/react_event/"

class ReactEventWindow(ui.ScriptWindow):
	def __init__(self):
		ui.ScriptWindow.__init__(self)
		self.__LoadWindow()
		self.nextRound = 0

	def __del__(self):
		ui.ScriptWindow.__del__(self)

	def __LoadWindow(self):
		try:
			pyScrLoader = ui.PythonScriptLoader()
			pyScrLoader.LoadScriptFile(self, "uiscript/reactevent.py")
		except:
			import exception
			exception.Abort("ReactEventWindow.LoadWindow.LoadObject")

		try:
			# self.GetChild("TitleBar").SetCloseEvent(ui.__mem_func__(self.Close))
			self.GetChild("ClearButton").SAFE_SetEvent(self.__OnClear)
			self.GetChild("EnterButton").SAFE_SetEvent(self.__OnEnter)
			self.numberLine = self.GetChild("InputNumber")
			self.GetChild("TitleBar").btnClose.Hide()
			# self.wordLine = self.GetChild("InputWord")
			# self.wordLine.SetEscapeEvent(ui.__mem_func__(self.Close))
		except:
			import exception
			exception.Abort("ReactEventWindow.LoadWindow.BindObject")

		self.numButtonList = []

		for x in xrange(9):
			posX = 40 + (62 * (x % 3))
			posY = 212 - (41 * (x / 3))
			index = x + 1
			button = ui.MakeButton(self, posX, posY, "", IMAGE_PATH, "button_s_normal.tga", "button_s_hover.tga", "button_s_down.tga")
			button.SAFE_SetEvent(self.__OnPressNumButton, index)
			button.SetText(str(index))
			self.numButtonList.append(button)

		self.symbolImageList = []

		for x in xrange(5):
			posX = 26 + (41 * x)
			button = ui.MakeButton(self, posX, 47, "", "icon/emoji/", "circle_%d.tga" % (x + 1), "circle_%d_hover.tga" % (x + 1), "circle_%d_down.tga" % (x + 1))
			button.SAFE_SetEvent(self.__OnPressSymbolImage, x)
			self.symbolImageList.append(button)

		self.timer = ui.ThinBoard()
		self.timer.SetParent(self)
		self.timer.SetSize(180, 15)
		self.timer.SetWindowHorizontalAlignCenter()
		self.timer.SetPosition(0, 342)
		self.timer.Show()

		self.timertxt = ui.TextLine()
		self.timertxt.SetParent(self.timer)
		self.timertxt.SetWindowHorizontalAlignCenter()
		self.timertxt.SetHorizontalAlignCenter()
		self.timertxt.SetPosition(0, 7)
		self.timertxt.Show()
		
		self.symbolInput = ""
		self.symbolImageInputList = []

		self.reactNotice = uiTip.ReactBoard()

	def __OnPressSymbolImage(self, index):
		if len(self.symbolImageInputList) >= 2:
			return

		self.symbolInput += "Symbol" + str(index + 1)

		imageName = "icon/emoji/circle_%d_down.tga" % (index + 1)
		image = ui.MakeImageBox(self, imageName, 0, 0)
		image.SetScale(0.8, 0.8)
		self.symbolImageInputList.append(image)
		self.__AlignSymbolInput()

	def __AlignSymbolInput(self):
		count = len(self.symbolImageInputList)
		span = count * 31
		start = 125 - (span / 2)
		x = 0
		for image in self.symbolImageInputList:
			posX = start + (x * 31)
			x += 1
			image.SetPosition(posX, 296)

	def __OnPressNumButton(self, index):
		text = self.numberLine.GetText()

		if len(text) == 4:
			return

		self.numberLine.SetText(text + str(index))

	def __OnClear(self):
		self.numberLine.SetText("")
		# self.wordLine.SetText("")
		self.symbolInput = ""

		for image in self.symbolImageInputList:
			image.Hide()

		del self.symbolImageInputList[:]

	def __OnEnter(self):
		type = 0
		# text = self.wordLine.GetDisplayText()
		text = self.numberLine.GetText()

		# if not len(text):
			# type = 1
			# text = self.numberLine.GetText()

		if not len(text):
			type = 1
			text = self.symbolInput

		net.SendChatPacket("/react_event %s %d" % (text, type))
		self.__OnClear()

	def SetTimer(self, sec):
		self.__OnClear()
		self.nextRound = app.GetTime() + int(sec)

	def OnUpdate(self):
		if not self.timer.IsShow() and self.nextRound > app.GetTime():
			self.timer.Show()
		elif self.timer.IsShow() and self.nextRound < app.GetTime():
			self.timer.Hide()
			return

		self.timertxt.SetText(localeInfo.REACT_EVENT_NEXT_ROUND % (self.nextRound - app.GetTime()))

	def Clear(self):
		self.ClearNotice()
		self.__OnClear()

	def Open(self):
		self.Show()

	def Close(self):
		self.ClearNotice()
		self.Hide()

	def Notice(self, text):
		if "EMOTION/" in text:
			emo_name = text.split('EMOTION')[1]
			for y in emotion.EMOTION_DICT:
				if emotion.EMOTION_DICT[y]["command"] == emo_name:
					text = text[:text.find("EMOTION/")] + emotion.EMOTION_DICT[y]["name"]
		self.reactNotice.Show()
		self.reactNotice.SetTip(text)

	def ClearNotice(self):
		self.reactNotice.Hide()

	def Destroy(self):
		self.ClearDictionary()
		self.numButtonList = []
		self.symbolImageList = []
		self.numberLine = None
		# self.wordLine = None
		self.symbolImageInputList = []
		self.reactNotice = None
		self.timertxt = None
		self.timer = None
		self.nextRound = None

	# def OnPressEscapeKey(self):
		# self.Close()
