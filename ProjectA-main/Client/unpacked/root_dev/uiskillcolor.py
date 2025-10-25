import ui
import grp
import player

class SkillColorWindow(ui.ScriptWindow):
	def __init__(self):
		ui.ScriptWindow.__init__(self)
		self.__LoadWindow()
		self.skill = -1
		self.layer = 0
		self.color = [ 0 ] * 5

	def __del__(self):
		ui.ScriptWindow.__del__(self)

	def __LoadWindow(self):
		try:
			pyScrLoader = ui.PythonScriptLoader()
			pyScrLoader.LoadScriptFile(self, "UIScript/SkillColorWindow.py")
		except:
			import exception
			exception.Abort("SkillColorWindow.__LoadWindow.LoadScript")

		try:
			getObject = self.GetChild
			getObject("TitleBar").SetCloseEvent(ui.__mem_func__(self.Close))

			self.saveButton = getObject("SaveButton")
			self.standartButton = getObject("StandardButton")
			self.colorBar = getObject("ColorBar")
		except:
			import exception
			exception.Abort("SkillColorWindow.__LoadWindow.SetObject")

		self.layerButtons = []
		for x in xrange(5):
			layerBtn = getObject("LayerBtn%d" % x)
			layerBtn.SAFE_SetEvent(self.OnClickLayerButton, x)
			self.layerButtons.append(layerBtn)

		self.cursorList = []
		for x in xrange(3):
			cursor = ui.DragButton()
			cursor.AddFlag("movable")
			cursor.AddFlag("restrict_y")
			cursor.SetParent(self.GetChild("ColorBar%d" % x))
			cursor.SetMoveEvent(lambda arg = x: self.__OnSelectColor(arg))
			# cursor.SetUpVisual("d:/ymir work/ui/game/skillcolor/slider.tga")
			# cursor.SetOverVisual("d:/ymir work/ui/game/skillcolor/slider.tga")
			# cursor.SetDownVisual("d:/ymir work/ui/game/skillcolor/slider.tga")
			cursor.SetUpVisual("d:/ymir work/ui/game/offlineshop/tab_sell/arrow2.tga")
			cursor.SetOverVisual("d:/ymir work/ui/game/offlineshop/tab_sell/arrow2.tga")
			cursor.SetDownVisual("d:/ymir work/ui/game/offlineshop/tab_sell/arrow2.tga")
			cursor.SetRestrictMovementArea(-6, 0, 198 + 9 + 5, 0)
			cursor.SetPosition(-6, 1)
			cursor.Show()
			self.cursorList.append(cursor)

		self.saveButton.SAFE_SetEvent(self.__SetColor)
		self.standartButton.SAFE_SetEvent(self.__ResetColor)

	def __SetColor(self):
		if self.skill == -1:
			return

		player.SetSkillColor(self.skill, self.color[0], self.color[1], self.color[2], self.color[3], self.color[4])
		self.Close()

	def __ResetColor(self):
		if self.skill == -1:
			return

		player.SetSkillColor(self.skill, 0, 0, 0, 0, 0)
		self.Close()

	def __OnSelectColor(self, arg):
		pos1 = ((((self.cursorList[0].GetLocalPosition()[0] + 7) * 100)) / 194) / 100.0
		pos2 = ((((self.cursorList[1].GetLocalPosition()[0] + 7) * 100)) / 194) / 100.0
		pos3 = ((((self.cursorList[2].GetLocalPosition()[0] + 7) * 100)) / 194) / 100.0

		self.color[self.layer] = grp.GenerateColor(pos1, pos2, pos3, 0.0)
		self.colorBar.SetColor(grp.GenerateColor(pos1, pos2, pos3, 1.0))

	def OnClickLayerButton(self, arg):
		for x in xrange(5):
			if x != arg:
				self.layerButtons[x].SetUp()
			else:
				self.layerButtons[x].Down()

		for cursor in self.cursorList:
			cursor.SetPosition(-5, 1)

		self.layer = arg
		self.colorBar.SetColor(grp.GenerateColor(0.0, 0.0, 0.0, 1.0))

	def Destroy(self):
		self.ClearDictionary()
		self.saveButton = None
		self.standartButton = None
		self.colorBar = None
		self.layerButtons = []
		self.cursorList = []

	def Open(self, skill):
		self.skill = skill
		self.OnClickLayerButton(0)
		self.Show()

	def Close(self):
		self.skill = -1
		self.Hide()

	def OnPressEscapeKey(self):
		self.Close()
		return True
