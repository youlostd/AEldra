import ui

class ExampleBaseScriptWindow(ui.BaseScriptWindow):

	#################################################
	## MAIN FUNCTIONS
	#################################################

	def __init__(self):
		ui.BaseScriptWindow.__init__(self, "ExampleBaseScriptWindow", self.__BindObject)
		self.__LoadWindow()

	def __BindObject(self):
	#	self._AddLoadObject("VAR_NAME", "OBJECT_NAME")
		pass

	def __LoadWindow(self):
	#	self.main["close"].SAFE_SetEvent(self.Close)

		self.Refresh()

	def Refresh(self):
		pass
