import ui

class DesignSelectorWindow(ui.ScriptWindow):

	def __init__(self):
		ui.ScriptWindow.__init__(self)
		self.__LoadWindow()

	def __del__(self):
		ui.ScriptWindow.__del__(self)
		
	def __LoadWindow(self):
		try:
			pyScrLoader = ui.PythonScriptLoader()
			pyScrLoader.LoadScriptFile(self, "uiscript/DesignSelectorWindow.py")
		except:
			import exception
			exception.Abort("DesignSelectorWindow.LoadWindow.LoadObject")

		try:
			self.board = self.GetChild("board")
		except:
			import exception
			exception.Abort("DesignSelectorWindow.LoadWindow.BindObject")

		self.board.SetCloseEvent(self.Close)

	def Destroy(self):
		self.Close()
		ui.ScriptWindow.Destroy(self)

	def Open(self):
		self.SetTop()
		self.Show()

	def Close(self):
		self.Hide()

	def OnPressEscapeKey(self):
		self.Close()
