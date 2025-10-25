import exception
import ui
import player

class AnimasphereZI(ui.ScriptWindow):
	def __init__(self):
		ui.ScriptWindow.__init__(self)
		self.LoadWindow()

	def __del__(self):
		ui.ScriptWindow.__del__(self)

	def LoadWindow(self):
		try:
			pyScrLoader = ui.PythonScriptLoader()
			pyScrLoader.LoadScriptFile(self, "UIScript/animasphere.py")
		except:
			exception.Abort("AnimasphereZI.LoadDialog.LoadScript")

		try:
			GetObject=self.GetChild
			self.LabadeUrs = GetObject("LabadeUrs")
			self.ZTAnimasphere2 = GetObject("Animasphere2")

		except:
			exception.Abort("AnimasphereZI.LoadDialog.BindObject")

	def OnUpdate(self):
		self.ZTAnimasphere2.SetText(str(player.GetAnimasphere()))

	def Close(self):
		self.Hide()
		return True

	def Destroy(self):
		self.ClearDictionary()
		self.LabadeUrs = None
		self.ZTAnimasphere2 = None
