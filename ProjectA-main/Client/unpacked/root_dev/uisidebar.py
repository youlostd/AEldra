import ui
import app
import wndMgr
import localeInfo
import cfg

BUTTON_SAFEBOX = 0
BUTTON_SWITCHBOT = 1
BUTTON_OFFLINE_SHOP = 2
BUTTON_GUILD_SAFEBOX = 3
BUTTON_MOUNT = 4
BUTTON_PET = 5

class SideBar(ui.Board):

	ROOT_PATH = "d:/ymir work/ui/game/sidebar/%s_%s.tga"
	BUTTON_LIST = [
		"safebox",
		"switchbot",
		"shop",
		"guild_safebox",
		"mount",
		"pet",
	]
	BUTTON_TITLE_LIST = [
		localeInfo.SIDEBAR_TOOLTIP_SAFEBOX,
		localeInfo.SIDEBAR_TOOLTIP_SWITCHBOT,
		localeInfo.SIDEBAR_TOOLTIP_SHOP,
		localeInfo.SIDEBAR_TOOLTIP_GUILD_SAFEBOX,
		localeInfo.SIDEBAR_TOOLTIP_MOUNT,
		localeInfo.SIDEBAR_TOOLTIP_PET,
	]

	X_POS = 100
	START_Y_POS = 7

	SHOW_BASE_COUNT = 2
	SHOW_BASE_ALPHA = 0.3
	SHOW_TOGGLE_ALPHA = 0.8
	SHOW_TOGGLE_TIME = 0.6

	BOARD_WIDTH = X_POS + 30 + 5

	def __init__(self):
		ui.Board.__init__(self)

		self.enableDict = {}
		self.eventDict = {}

		self.startTime = 0
		self.endTime = 0
		self.isMouseIn = False

		self.btnToggleIn = None
		self.btnToggleOut = None

		self.AddFlag("float")

		self.__LoadWindow()

	def __del__(self):
		ui.Board.__del__(self)

	def __MakeToggleButton(self, type):
		btn = ui.Button()
		btn.SetUpVisual("d:/ymir work/ui/game/sidebar/sidebar_%s.tga" % type)
		btn.SetOverVisual("d:/ymir work/ui/game/sidebar/sidebar_%s_hover.tga" % type)
		btn.SetDownVisual("d:/ymir work/ui/game/sidebar/sidebar_%s_down.tga" % type)
		btn.SAFE_SetEvent(self.__OnClickToggleButton, type)
		btn.SetAlpha(self.SHOW_BASE_ALPHA)
		btn.Hide()

		yPos = self.GetTop() + (self.GetRealHeight() - btn.GetHeight()) / 2
		if type == "in":
			btn.SetPosition(self.GetLeft() + self.GetRealWidth() - self.MARGIN[self.R], yPos)
		else:
			btn.SetPosition(0, yPos)

		return btn
	
	def __LoadWindow(self):
		self.btnList = []
		yPos = self.START_Y_POS

		for btnName in self.BUTTON_LIST:
			btn = ui.Button()
			btn.SetParent(self)
			btn.SetPosition(self.X_POS, yPos)
			btn.SetUpVisual(self.ROOT_PATH % (btnName, "normal"))
			btn.SetOverVisual(self.ROOT_PATH % (btnName, "hover"))
			btn.SetDownVisual(self.ROOT_PATH % (btnName, "down"))
			btn.SetDisableVisual(self.ROOT_PATH % (btnName, "disable"))
			btn.SAFE_SetEvent(self.__OnClickButton, len(self.btnList))
			btn.SetToolTipText(self.BUTTON_TITLE_LIST[len(self.btnList)], btn.GetWidth() - 13, -10, False)
			btn.Show()
			yPos += btn.GetHeight() + 4

			self.btnList.append(btn)

		self.SetAllAlpha(self.SHOW_BASE_ALPHA)
		self.SetSize(self.BOARD_WIDTH, self.__GetHeightByCount(self.SHOW_BASE_COUNT))

	def Destroy(self):
		self.Hide()
		self.btnToggleIn.Hide()
		self.btnToggleOut.Hide()

		self.btnToggleIn = None
		self.btnToggleOut = None

		ui.Board.Destroy(self)

	def Open(self):
		self.btnToggleIn.Show()
		self.btnToggleOut.Hide()
		self.SetTop()
		self.Show()

		cfg.Set(cfg.SAVE_GENERAL, "sidebar_open", "1")

	def Close(self):
		self.Hide()
		self.btnToggleIn.Hide()
		self.btnToggleOut.Show()

		cfg.Set(cfg.SAVE_GENERAL, "sidebar_open", "0")

	def __GetHeightByCount(self, count):
		return self.START_Y_POS + self.START_Y_POS + count * 30 + (max(1, count) - 1) * 4

	def SetSize(self, width, height):
		ui.Board.SetSize(self, width, height)
		self.SetPosition(self.GetLeft(), (wndMgr.GetScreenHeight() - self.GetRealHeight()) / 2)

		height -= self.START_Y_POS # - bottom margin
		for btn in self.btnList:
			ys = btn.GetTop()

			if ys >= height:
				btn.SetRenderingRect(0.0, 0.0, 0.0, -1.0)
			else:
				btn.SetRenderingRect(0.0, 0.0, 0.0, min(0.0, -1.0 + float(height - ys) / float(btn.GetHeight())))

	def SetEnableCheckFunc(self, idx, func):
		self.enableDict[idx] = func

	def SetButtonFunc(self, idx, func):
		self.eventDict[idx] = func

	def Refresh(self):
		for key in self.enableDict:
			self.btnList[key].SetEnabled(self.enableDict[key]())

	def __OnClickButton(self, btnIndex):
		if self.eventDict.has_key(btnIndex):
			self.eventDict[btnIndex]()

	def __OnClickToggleButton(self, type):
		if type == "in":
			self.Close()
		else:
			self.Open()

	def LoadConfig(self):
		if not self.btnToggleIn:
			self.btnToggleIn = self.__MakeToggleButton("in")
		if not self.btnToggleOut:
			self.btnToggleOut = self.__MakeToggleButton("out")

		if cfg.Get(cfg.SAVE_GENERAL, "sidebar_open", "1") != "0":
			self.Open()
		else:
			self.Close()

	def SetAllAlpha(self, alpha):
		ui.Board.SetAllAlpha(self, alpha)
		if self.btnToggleIn:
			self.btnToggleIn.SetAlpha(alpha)
		if self.btnToggleOut:
			self.btnToggleOut.SetAlpha(alpha)

	def GAME_OnUpdate(self):
		isMouseIn = self.IsIn(True) or self.btnToggleIn.IsIn() or self.btnToggleOut.IsIn()
		if isMouseIn != self.isMouseIn:
			pct = 1.0
			if self.startTime != 0:
				pct = (app.GetTime() - self.startTime) / (self.endTime - self.startTime)
				if pct > 1.0:
					pct = 1.0

			self.startTime = app.GetTime() - self.SHOW_TOGGLE_TIME * (1.0 - pct)
			self.endTime = self.startTime + self.SHOW_TOGGLE_TIME
			self.isMouseIn = isMouseIn
			if isMouseIn:
				self.SetTop()

		if self.startTime != 0:
			startHeight = self.__GetHeightByCount(self.SHOW_BASE_COUNT)
			endHeight = self.__GetHeightByCount(len(self.btnList))

			pct = (app.GetTime() - self.startTime) / (self.endTime - self.startTime)
			if pct >= 1.0:
				self.startTime = 0
				self.endTime = 0
				pct = 1.0

			if not isMouseIn:
				pct = 1.0 - pct

			self.SetAllAlpha(self.SHOW_BASE_ALPHA + (self.SHOW_TOGGLE_ALPHA - self.SHOW_BASE_ALPHA) * pct)
			self.SetSize(self.GetWidth(), int(startHeight + (endHeight - startHeight) * pct))
