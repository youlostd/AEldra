import ui
import app
import localeInfo
import wndMgr

class MaintenanceBoard(ui.ScriptWindow):

	def __init__(self):
		ui.ScriptWindow.__init__(self)

		self.timeEnd = 0
		self.duration = 0

		self.LoadWindow()

	def __del__(self):
		ui.ScriptWindow.__del__(self)

	def Destroy(self):
		self.Close()
		ui.ScriptWindow.Destroy(self)

	def LoadWindow(self):
		try:
			pyScrLoader = ui.PythonScriptLoader()
			pyScrLoader.LoadScriptFile(self, "UIScript/MaintenanceWindow.py")
		except:
			import exception
			exception.Abort("MaintenanceBoard.LoadDialog.LoadScript")

		try:
			GetObject=self.GetChild
			self.board = GetObject("board")
			self.desc = GetObject("desc")

		except:
			import exception
			exception.Abort("MaintenanceBoard.LoadDialog.BindObject")

		self.board.HideCorners(ui.ThinBoard.LT)
		self.board.HideCorners(ui.ThinBoard.RT)
		self.board.HideLine(ui.ThinBoard.T)

	def Open(self, message):
		self.desc.SetText('<TEXT text="%s" r=255 g=0 b=0 font_size="LARGE">' % message)
		self.Refresh(message)
		self.Show()

	def Close(self):
		self.Hide()

	def Refresh(self, new_size = False):
		if new_size == True or self.desc.GetWidth() + 30 > self.GetWidth():
			self.SetSize(self.desc.GetWidth() + 30, self.GetHeight())
			self.board.SetSize(self.GetWidth(), self.GetHeight())
			self.SetPosition((wndMgr.GetScreenWidth() - self.GetWidth()) / 2, self.GetTop())
			self.desc.UpdateRect()

	# def OnUpdate(self):
	# 	self.Refresh()
