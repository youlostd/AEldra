import app
import ui
import uiScriptLocale

LOCALE_PATH = uiScriptLocale.MAPNAME_PATH

class MapNameShower(ui.ExpandedImageBox):

	STATE_HIDE = 0
	STATE_FADE_IN = 1
	STATE_SHOW = 2
	STATE_FADE_OUT = 3

	def __init__(self):
		ui.ExpandedImageBox.__init__(self, "TOP_MOST")
		self.AddFlag("not_pick")
		self.__Initialize()

	def __del__(self):
		ui.ExpandedImageBox.__del__(self)

	def __Initialize(self):
		self.floorImage = None
		self.fadeStartTime = 0
		self.state = self.STATE_HIDE
		self.curAlpha = 0.0
		self.SetAlpha(0.0)
		self.SetWindowHorizontalAlignCenter()
		self.SetPosition(0, 80)
		self.Hide()

	def __GetDevilTowerFloor(self, x, y):
		if x > 10000 and y > 58000 and x < 25000 and y < 72000:
			return 1
		elif x > 10000 and y > 35000 and x < 25000 and y < 50000:
			return 2
		elif x > 10000 and y > 10000 and x < 25000 and y < 25000:
			return 3
		elif x > 35000 and y > 61000 and x < 43500 and y < 70500:
			return 4
		elif x > 35000 and y > 38000 and x < 43500 and y < 48000:
			return 5
		elif x > 14000 and y > 14000 and x < 43500 and y < 24500:
			return 6
		elif x > 56000 and y > 60000 and x < 68000 and y < 73000:
			return 7
		elif x > 56000 and y > 38000 and x < 68000 and y < 49000:
			return 8
		elif x > 56000 and y > 13000 and x < 68000 and y < 23000:
			return 9	 
		return 0
	def __GetDevilBase(self, x, y):
		if x > 3000 and y > 4500 and x < 45000 and y < 45000:
			return 1
		elif x > 54000 and y > 3900 and x < 100000 and y < 46200:
			return 2
		elif x > 104800 and y > 3500 and x < 145500 and y < 45800:
			return 3
		elif x > 3100 and y > 54100 and x < 56400 and y < 105800:
			return 4
		elif x > 65000 and y > 54000 and x < 105000 and y < 95500:
			return 5
		elif x > 117500 and y > 57600 and x < 142000 and y < 81000:
			return 6
		return	0
	def ShowMapName(self, mapName, x, y):
		#if not self.MAP_NAME_IMAGE.has_key(mapName):
		#	print " [ERROR] - There is no map name image", mapName
		#	return

		try:
			searchStr = "metin2_map_"
			if mapName.find(searchStr) == -1:
				print " [ERROR] - Cannot get map name image by map name %s" % mapName
				return

			imageName = LOCALE_PATH + mapName[mapName.find(searchStr) + len(searchStr):] + ".tga"
			self.LoadImage(imageName)
		except RuntimeError:
			return

		self.__Initialize()

		if mapName == "metin2_map_deviltower":
			self.SetPosition(-60, 80)

			self.floorImage = ui.ExpandedImageBox()
			self.floorImage.AddFlag("not_pick")
			self.floorImage.SetWindowHorizontalAlignCenter()
			self.floorImage.SetPosition(100, 80)
			self.floorImage.SetAlpha(0.0)
			self.floorImage.Show()

			try:
				floor = self.__GetDevilTowerFloor(x, y)
				print x, y, floor
				self.floorImage.LoadImage(LOCALE_PATH+"deviltower_%d.tga" % floor)
			except RuntimeError:
				self.SetPosition(0, 80)
				self.floorImage.Hide()
				self.floorImage = None
		self.state = self.STATE_FADE_IN
		self.fadeStartTime = app.GetTime() + 1.0
		self.Show()

	def Update(self):

		self.SetAlpha(self.curAlpha)
		if self.floorImage:
			self.floorImage.SetAlpha(self.curAlpha)

		if self.STATE_FADE_IN == self.state:
			if app.GetTime() > self.fadeStartTime:
				self.curAlpha += 0.05

				if self.curAlpha > 0.9:
					self.state = self.STATE_SHOW
					self.fadeStartTime = app.GetTime() + 5.0

		elif self.STATE_SHOW == self.state:
			if app.GetTime() > self.fadeStartTime:
				self.state = self.STATE_FADE_OUT

		elif self.STATE_FADE_OUT == self.state:
			self.curAlpha -= 0.05

			if self.curAlpha < 0.0001:
				self.Hide()
				if self.floorImage:
					self.floorImage.Hide()
					self.floorImage = None
				return
