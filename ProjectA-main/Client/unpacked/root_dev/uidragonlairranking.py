import ui
import grp
import player
import localeInfo

class Window(ui.ScriptWindow):
	def __init__(self):
		ui.ScriptWindow.__init__(self)
		self.isLoaded = 0
		self.PositionOut = 0
		self.PositionStartX = 0
		self.PositionStartY = 0
		self.titleBar = None
		self.scrollBar = None
		self.rankLine = None
		self.rankDataBackground = None
		self.rankData = None
		if localeInfo.IsARABIC():
			self.LeftTop = None
			self.RightTop = None
			self.LeftBottom = None
			self.RightBottom = None
			self.leftcenterImg = None
			self.rightcenterImg = None
			self.topcenterImg = None
			self.bottomcenterImg = None
			self.centerImg = None
			self.LeftTopSelf = None
			self.RightTopSelf = None
			self.LeftBottomSelf = None
			self.RightBottomSelf = None
			self.topcenterImgSelf = None
			self.bottomcenterImgSelf = None

	def __del__(self):
		ui.ScriptWindow.__del__(self)

	def Destroy(self):
		self.ClearDictionary()
		self.PositionOut = 0
		self.PositionStartX = 0
		self.PositionStartY = 0
		self.titleBar = None
		self.scrollBar = None
		self.rankLine = None
		self.rankDataBackground = None
		self.rankData = None
		if localeInfo.IsARABIC():
			self.LeftTop = None
			self.RightTop = None
			self.LeftBottom = None
			self.RightBottom = None
			self.leftcenterImg = None
			self.rightcenterImg = None
			self.topcenterImg = None
			self.bottomcenterImg = None
			self.centerImg = None
			self.LeftTopSelf = None
			self.RightTopSelf = None
			self.LeftBottomSelf = None
			self.RightBottomSelf = None
			self.topcenterImgSelf = None
			self.bottomcenterImgSelf = None

	def LoadWindow(self):
		if self.isLoaded:
			return
		
		self.isLoaded = 1
		
		try:
			pyScrLoader = ui.PythonScriptLoader()
			pyScrLoader.LoadScriptFile(self, "uiscript/guildwindow_guilddragonlairranking.py")
		except:
			import exception
			exception.Abort("GuildDragonLairWindow.LoadDialog.LoadScript")
		
		self.DIFFERENCE = 17
		self.BOARD_WIDTH = 368
		
		try:
			self.titleBar = self.GetChild("board")
			self.scrollBar = self.GetChild("GuildDragonLairScrollBar")
			self.baseWindow = self.GetChild("BaseWindow")
			self.myRanking = self.GetChild("MyRankingWindow")
			if localeInfo.IsARABIC():
				self.LeftTop = self.GetChild("LeftTop")
				self.RightTop = self.GetChild("RightTop")
				self.LeftBottom = self.GetChild("LeftBottom")
				self.RightBottom = self.GetChild("RightBottom")
				self.leftcenterImg = self.GetChild("leftcenterImg")
				self.rightcenterImg = self.GetChild("rightcenterImg")
				self.topcenterImg = self.GetChild("topcenterImg")
				self.bottomcenterImg = self.GetChild("bottomcenterImg")
				self.centerImg = self.GetChild("centerImg")
				self.LeftTopSelf = self.GetChild("LeftTopSelf")
				self.RightTopSelf = self.GetChild("RightTopSelf")
				self.LeftBottomSelf = self.GetChild("LeftBottomSelf")
				self.RightBottomSelf = self.GetChild("RightBottomSelf")
				self.topcenterImgSelf = self.GetChild("topcenterImgSelf")
				self.bottomcenterImgSelf = self.GetChild("bottomcenterImgSelf")
				
				self.LeftTop.SetPosition(318 + self.DIFFERENCE, 38)
				self.RightTop.SetPosition(17 + self.DIFFERENCE, 38)
				self.LeftBottom.SetPosition(318 + self.DIFFERENCE, 173)
				self.RightBottom.SetPosition(17 + self.DIFFERENCE, 173)
				self.leftcenterImg.SetPosition(317 + self.DIFFERENCE + 1, 38+16)
				self.rightcenterImg.SetPosition(17 + self.DIFFERENCE + 1, 38+16)
				self.topcenterImg.SetPosition(self.BOARD_WIDTH - (17 + 15 + self.DIFFERENCE), 38)
				self.bottomcenterImg.SetPosition(self.BOARD_WIDTH - (17 + 15 + self.DIFFERENCE), 173)
				self.centerImg.SetPosition(self.BOARD_WIDTH - (17 + 15 + self.DIFFERENCE), 38 + 15)
				
				self.LeftTopSelf.SetPosition(318 + self.DIFFERENCE, 190)
				self.RightTopSelf.SetPosition(17 + self.DIFFERENCE, 190)
				self.LeftBottomSelf.SetPosition(318 + self.DIFFERENCE, 190 + 15)
				self.RightBottomSelf.SetPosition(17 + self.DIFFERENCE, 190 + 15)
				
				self.topcenterImgSelf.SetPosition(self.BOARD_WIDTH - (17 + 15 + self.DIFFERENCE), 190)
				self.bottomcenterImgSelf.SetPosition(self.BOARD_WIDTH - (17 + 15 + self.DIFFERENCE),190 + 15)
		except:
			import exception
			exception.Abort("GuildDragonLairWindow.LoadDialog.BindObject")
		
		#build
		self.rankLine = []
		self.rankData = {
							"ID" : [],
							"NAME" : [],
							"MEMBERS" : [],
							"TIME" : [],
		}
		
		self.rankDataBackground = {
							"ID" : [],
							"NAME" : [],
							"MEMBERS" : [],
							"TIME" : [],
		}
		
		if localeInfo.IsARABIC():
			str_lineDown = "d:/ymir work/ui/game/guild/dragonlairranking/line_down_ae.sub"
		else:
			str_lineDown = "d:/ymir work/ui/game/guild/dragonlairranking/line_down.sub"
		
		for i in xrange(6):
			lineStep = 24
			yPos = i * lineStep + 64 - 38
			parent = self.baseWindow
			if i == 5:
				yPos = 5
				parent = self.myRanking
			
			if localeInfo.IsARABIC():
				line = ui.MakeImageBox(parent, str_lineDown, 22 - 17 + self.DIFFERENCE, yPos)
			else:
				line = ui.MakeImageBox(parent, str_lineDown, 22 - 17, yPos)
			
			self.rankLine.append(line)
			
			#ID_BACKGROUND = ui.MakeSlotBar(self.rankLine[i], 6, 2, 31, 16)
			ID_BACKGROUND = ui.Bar("TOP_MOST")
			ID_BACKGROUND.SetParent(self.rankLine[i])
			if localeInfo.IsARABIC():
				ID_BACKGROUND.SetPosition(270, 2)
			else:
				ID_BACKGROUND.SetPosition(6, 2)
			
			ID_BACKGROUND.SetSize(31, 16)
			ID_BACKGROUND.SetColor(grp.GenerateColor(0.0, 0.0, 0.0, 0.0))
			ID_BACKGROUND.Show()
			self.rankDataBackground["ID"].append(ID_BACKGROUND)
			
			#NAME_BACKGROUND = ui.MakeSlotBar(self.rankLine[i], 55, 2, 114, 16)
			NAME_BACKGROUND = ui.Bar("TOP_MOST")
			NAME_BACKGROUND.SetParent(self.rankLine[i])
			if localeInfo.IsARABIC():
				NAME_BACKGROUND.SetPosition(145, 2)
			else:
				NAME_BACKGROUND.SetPosition(55, 2)
			
			NAME_BACKGROUND.SetSize(114, 16)
			NAME_BACKGROUND.SetColor(grp.GenerateColor(0.0, 0.0, 0.0, 0.0))
			NAME_BACKGROUND.Show()
			self.rankDataBackground["NAME"].append(NAME_BACKGROUND)
			
			#MEMBERS_BACKGROUND = ui.MakeSlotBar(self.rankLine[i], 192, 2, 22, 16)
			MEMBERS_BACKGROUND = ui.Bar("TOP_MOST")
			MEMBERS_BACKGROUND.SetParent(self.rankLine[i])
			if localeInfo.IsARABIC():
				MEMBERS_BACKGROUND.SetPosition(92, 2)
			else:
				MEMBERS_BACKGROUND.SetPosition(192, 2)
			
			MEMBERS_BACKGROUND.SetSize(22, 16)
			MEMBERS_BACKGROUND.SetColor(grp.GenerateColor(0.0, 0.0, 0.0, 0.0))
			MEMBERS_BACKGROUND.Show()
			self.rankDataBackground["MEMBERS"].append(MEMBERS_BACKGROUND)
			
			#TIME_BACKGROUND = ui.MakeSlotBar(self.rankLine[i], 237, 2, 61, 16)
			TIME_BACKGROUND = ui.Bar("TOP_MOST")
			TIME_BACKGROUND.SetParent(self.rankLine[i])
			if localeInfo.IsARABIC():
				TIME_BACKGROUND.SetPosition(6, 2)
			else:
				TIME_BACKGROUND.SetPosition(241, 2)
			
			TIME_BACKGROUND.SetSize(61, 16)
			TIME_BACKGROUND.SetColor(grp.GenerateColor(0.0, 0.0, 0.0, 0.0))
			TIME_BACKGROUND.Show()
			self.rankDataBackground["TIME"].append(TIME_BACKGROUND)
			
			ID = ui.MakeTextLine(self.rankDataBackground["ID"][i])
			NAME = ui.MakeTextLine(self.rankDataBackground["NAME"][i])
			MEMBERS = ui.MakeTextLine(self.rankDataBackground["MEMBERS"][i])
			TIME = ui.MakeTextLine(self.rankDataBackground["TIME"][i])
			self.rankData["ID"].append(ID)
			self.rankData["NAME"].append(NAME)
			self.rankData["MEMBERS"].append(MEMBERS)
			self.rankData["TIME"].append(TIME)
		
		#self.AddRank(0, "Staff", "24", "23 minutes")
		self.AddRank(5, "-", "-", "-", "-")
		self.scrollBar.SetMiddleBarSize(0.95)
		self.titleBar.SetCloseEvent(ui.__mem_func__(self.Close))

	def AddRank(self, line, name, members, time, last = None):
		if self.rankData != None:
			if localeInfo.IsARABIC():
				str_lineUp = "d:/ymir work/ui/game/guild/dragonlairranking/line_up_ae.sub"
				str_lineDown = "d:/ymir work/ui/game/guild/dragonlairranking/line_down_ae.sub"
			else:
				str_lineUp = "d:/ymir work/ui/game/guild/dragonlairranking/line_up.sub"
				str_lineDown = "d:/ymir work/ui/game/guild/dragonlairranking/line_down.sub"
			
			if self.rankData["ID"][line]:
				if last != None:
					self.rankData["ID"][line].SetText(str(last))
				else:
					self.rankData["ID"][line].SetText(str(line + 1))
				
				self.rankData["NAME"][line].SetText(str(name))
				self.rankData["MEMBERS"][line].SetText(str(members))
				self.rankData["TIME"][line].SetText(str(time))
				
				if player.GetGuildName() == str(name):
					self.rankLine[line].LoadImage(str_lineUp)
				else:
					self.rankLine[line].LoadImage(str_lineDown)

	def IsOpened(self):
		if self.IsShow() and self.isLoaded:
			return True
		
		return False

	def Open(self):
		if self.IsOpened():
			return
		
		for i in xrange(5):
			self.AddRank(i, "", "", "", "")
		
		self.PositionOut = 0
		(self.PositionStartX, self.PositionStartY, z) = player.GetMainCharacterPosition()
		self.Show()

	def Close(self):
		self.Hide()

	def OnPressEscapeKey(self):
		self.Close()
		return True

	def OnUpdate(self):
		LIMIT_RANGE = 1000
		(x, y, z) = player.GetMainCharacterPosition()
		if abs(x - self.PositionStartX) >= LIMIT_RANGE or abs(y - self.PositionStartY) >= LIMIT_RANGE:
			if not self.PositionOut:
				self.PositionOut += 1
				self.Close()

