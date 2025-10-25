import app
import exception
import wndMgr
import chat
import constInfo
import ui
import time
import localeInfo
import player

muietiger = { 7, 14, 21, 28, 35, 36, 37, 38, 39, 40 }

class ZodiacMap(ui.ScriptWindow):
	def __init__(self):
		ui.ScriptWindow.__init__(self)
		self.LeftTime = None
		self.CurrentFloor = None
		self.LoadWindow()
		self.timeEnd = 0

	def __del__(self):
		ui.ScriptWindow.__del__(self)

	def Destroy(self):
		self.Close()

	def LoadWindow(self):
		try:
			pyScrLoader = ui.PythonScriptLoader()
			pyScrLoader.LoadScriptFile(self, "UIScript/zodiac.py")
		except:
			exception.Abort("ZodiacMap.LoadDialog.LoadScript")

		try:
			GetObject=self.GetChild
			self.ZodiacWindow = GetObject("ZodiacWindow")
			self.ZodiacBG = GetObject("ZodiacBG")
			self.JumpStep = self.GetChild("JumpStep")
			self.LeftTime = self.GetChild("LeftTime")
			self.CurrentFloor = self.GetChild("CurrentFloor")
			self.ZodiacFrame = ui.ImageBox()
		except:
			exception.Abort("ZodiacMap.LoadDialog.BindObject")

	def Open(self, timeLeft):
		self.timeEnd = app.GetTime() + timeLeft

	def OnUpdate(self):
		if constInfo.ENABLE_ZODIAC_MINIMAP == 0:
			self.Close()
			self.ZodiacFrame.Hide()
		else:
			ZI_FLOOR = constInfo.ZODIAC_TEMPLE['FLOOR']
			CHECK_ELAPSED_TIME = self.timeEnd - app.GetTime()

			if constInfo.ZODIAC_TEMPLE['FLOOR'] != constInfo.ZODIAC_SAVE_FLOOR:
				constInfo.ZODIAC_SAVE_FLOOR = constInfo.ZODIAC_TEMPLE['FLOOR']
				constInfo.ZODIAC_CLOCK = 1
				self.Open(9)


			else:
				if ZI_FLOOR == 1:
					if constInfo.ZODIAC_CLOCK_1ST == 0:
						self.Open(9)
						constInfo.ZODIAC_CLOCK_1ST = 1
		
					if constInfo.ZODIAC_CLOCK_1ST == 1:
						if CHECK_ELAPSED_TIME <= 0:
							self.Open(600)
							constInfo.ZODIAC_CLOCK = 2

				else:
					if constInfo.ZODIAC_CLOCK == 1:
						if CHECK_ELAPSED_TIME <= 0:
							if ZI_FLOOR in muietiger:
								self.Open(300)
							else:
								self.Open(600)
							constInfo.ZODIAC_CLOCK = 2

				self.CurrentFloor.SetText("%d%s" % (constInfo.ZODIAC_TEMPLE['FLOOR'], "F"))
				self.JumpStep.SetText("%d%s" % (constInfo.ZODIAC_TEMPLE['JUMP'], "F"))

				if constInfo.ZODIAC_CLOCK_1ST == 2:
					muita =  self.timeEnd - app.GetTime()
					cacat = muita/600 * 100
					invertedprocent = 100 - cacat
				
				if constInfo.ZODIAC_CLOCK == 1:
					muita =  self.timeEnd - app.GetTime()
					cacat = muita/9 * 100
					invertedprocent = 100 - cacat
				
				if constInfo.ZODIAC_CLOCK == 2:
					muita =  self.timeEnd - app.GetTime()
					if ZI_FLOOR in muietiger:
						cacat = muita/300 * 100
					else:
						cacat = muita/600 * 100
					invertedprocent = 100 - cacat
					
				truevalue = int(invertedprocent/4)
				
				if truevalue >= 0 and truevalue <= 25:
					self.ZodiacFrame.LoadImage("d:/ymir work/ui/zodiac/12zi/frames/" + str(truevalue) + ".tga")
					self.ZodiacFrame.SetPosition(wndMgr.GetScreenWidth() - 126, 10)
					self.ZodiacFrame.SetSize(0, 0)
					self.ZodiacFrame.Show()
				else:
					self.ZodiacFrame.LoadImage("d:/ymir work/ui/zodiac/12zi/frames/0.tga")
					self.ZodiacFrame.SetPosition(wndMgr.GetScreenWidth() - 126, 10)
					self.ZodiacFrame.SetSize(0, 0)
					self.ZodiacFrame.Show()

				self.LeftTime.SetText("%02s" % (localeInfo.SecondToDHMS(max(0, int(self.timeEnd - app.GetTime())))))

	def Close(self):
		self.Hide()

	def Destroy(self):
		self.ClearDictionary()
		self.ZodiacWindow = None
		self.ZodiacBG = None
		self.JumpStep = None
		self.LeftTime = None
		self.CurrentFloor = None
		self.ZodiacFrame = None
