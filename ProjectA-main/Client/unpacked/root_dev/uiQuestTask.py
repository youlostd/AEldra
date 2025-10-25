import ui
import localeInfo

class QuestTask(ui.Window):
	def __init__(self):
		ui.Window.__init__(self)
		self.__LoadWindow()
		self.tasks = {}

	def __del__(self):
		ui.Window.__del__(self)

	def __LoadWindow(self):
		self.title = ui.TextLine()
		self.title.SetParent(self)
		self.title.SetPosition(0, 0)
		self.title.SetText("Tasks")
		# self.title.SetFontColor(234 / 255.0, 211 / 255.0, 0)
		self.title.SetFontName("Tahoma:18")
		# self.title.SetOutline()
		self.title.Show()

		self.SetSize(555, 555)
		self.SetPosition(0, 200)
		self.Show()

	def AppendTask(self, var, desc, state):
		task = Task(self, desc)
		self.tasks[var] = task
		self.Refresh()

	def Refresh(self):
		y = 30
		for task in self.tasks.values():
			hight = task.desc.GetRealHeight()
			task.SetPosition(y)
			tchat("h %d" % hight)
			y += hight + 15

	def Remove(self, var):
		if var in self.tasks:
			del self.tasks[var]
			self.Refresh()

	def Clear(self):
		for task in self.tasks.values():
			del task
		self.tasks = {}

	def Destroy(self):
		self.title = None
		for task in self.tasks.values():
			task.Hide()
			del task
		self.tasks = {}

class Task:#(ui.Window):
	def __init__(self, parent, desc):
		self.desc = ui.MultiTextLine()
		self.desc.SetParent(parent)
		self.desc.SetPosition(0, 0)
		self.desc.SetWidth(195)
		self.desc.SetText(desc)
		self.desc.SetPackedFontColor(ui.BRIGHT_COLOR)
		self.desc.SetFontName(localeInfo.UI_DEF_FONT_LARGE)
		self.desc.SetOutline()
		self.desc.Show()

	def SetPosition(self, pos):
		self.desc.SetPosition(0, pos)

	def __del__(self):
		self.desc = None
