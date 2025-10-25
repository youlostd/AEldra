import ui
import localeInfo
import constInfo
import net

path = "d:/ymir work/d_rankwindow/"

buttonNames = [
	localeInfo.QUEST_TIMER_AZRAEL,
	localeInfo.QUEST_TIMER_SLIME,
	localeInfo.QUEST_TIMER_FLAME,
	localeInfo.QUEST_TIMER_SNOW,
	localeInfo.QUEST_TIMER_JOTUN,
	localeInfo.QUEST_TIMER_CRYSTALL,
	localeInfo.QUEST_TIMER_THRANDUILS,
	localeInfo.QUEST_TIMER_INFECTED,
]

class RankWindow(ui.ScriptWindow):
	class Rank:
		def __init__(self, parent, arg):
			self.parent = ui.ImageBox()
			self.parent.SetParent(parent)
			self.parent.SetPosition(10,28 * (arg+1) + 80)
			self.parent.LoadImage(path+"field.tga")
			self.parent.Show()

			y = 5

			self.rank = ui.TextLine()
			self.rank.SetParent(self.parent)
			self.rank.SetPosition(23, y)
			self.rank.SetHorizontalAlignCenter()
			self.rank.Show()

			if arg == -1:
				self.parent.LoadImage(path+"base_field.tga")
				self.rank.SetText("#")
			else:
				self.rank.SetText(str(arg+1))

			self.name = ui.TextLine()
			self.name.SetParent(self.parent)
			self.name.SetPosition(115, y)
			self.name.SetHorizontalAlignCenter()
			self.name.Show()

			self.level = ui.TextLine()
			self.level.SetParent(self.parent)
			self.level.SetPosition(206, y)
			self.level.SetHorizontalAlignCenter()
			self.level.Show()

			self.score = ui.TextLine()
			self.score.SetParent(self.parent)
			self.score.SetPosition(293, y)
			self.score.SetHorizontalAlignCenter()
			self.score.Show()

			self.time = ui.TextLine()
			self.time.SetParent(self.parent)
			self.time.SetPosition(392, y)
			self.time.SetHorizontalAlignCenter()
			self.time.Show()

		def SetValues(self,*arg):
			self.name.SetText(arg[0])
			self.level.SetText(arg[1])
			self.score.SetText(arg[2])
			self.time.SetText(arg[3])

		def Destroy(self):
			self.rank = None
			self.name = None
			self.time = None
			self.level = None

	def __init__(self):
		ui.ScriptWindow.__init__(self)
		self.firstOpen = True
		self.__LoadWindow()

	def __del__(self):
		ui.ScriptWindow.__del__(self)

	def Open(self):
		if self.firstOpen:
			self.OnClickButton(0)
			self.firstOpen = False
		self.Show()

	def Close(self):
		self.Hide()

	def OnPressEscapeKey(self):
		self.Close()
		return True

	def __LoadWindow(self):
		try:
			pyScrLoader = ui.PythonScriptLoader()
			pyScrLoader.LoadScriptFile(self, "UIScript/RankWindow.py")
		except:
			import exception
			exception.Abort("RankWindow.LoadWindow.LoadObject")
		
		self.SetCenterPosition()

		self.GetChild("TitleBar").SetCloseEvent(ui.__mem_func__(self.Close))
		self.index = 0
		y = 36
		x = 10
		
		self.hparent = ui.ImageBox()
		self.hparent.SetParent(self)
		self.hparent.SetPosition(13,y)
		self.hparent.LoadImage(path+"base2.tga")
		self.hparent.Show()
		
		self.parent = ui.ImageBox()
		self.parent.SetParent(self)
		self.parent.SetPosition(6,77)
		self.parent.LoadImage(path+"base.tga")
		self.parent.Show()
		
		self.buttonList = []
		for i in xrange(8):
			button = ui.RadioButton()
			button.SetParent(self)
			button.SetPosition(x+10,y)
			button.SetEvent(self.OnClickButton,i)
			button.SetUpVisual(path+"btn1.tga")
			button.SetOverVisual(path+"btn2.tga")
			button.SetDownVisual(path+"btn2.tga")
			button.SetText(buttonNames[i] if len(buttonNames[i]) < 14 else ('%s.' % buttonNames[i][:14]))
			button.Show()
			self.buttonList.append(button)

			x += 106
			if i == 3:
				x = 10
				y += 21

		self.rankList = []

		for x in xrange(10):
			rank = self.Rank(self,x)
			self.rankList.append(rank)

		self.basic = self.Rank(self,-1)
		self.basic.SetValues(localeInfo.DUNGEON_RANKING_NAME, "Level:", localeInfo.DUNGEON_RANKING_COMPLETED, localeInfo.DUNGEON_RANKING_TIME)


	def OnClickButton(self,arg):
		self.index = arg
		for x in xrange(8):
			if x == arg:
				self.buttonList[x].Down()
			else:
				self.buttonList[x].SetUp()
		for x in xrange(10):
			self.rankList[x].SetValues("", "", "", "")

		net.SendChatPacket("/get_dungeon_rank %d" % arg)

	def OnRecvDungeonInfo(self, pos, who, cmplTime, count, level):
		if len(who) == 0:
			self.rankList[int(pos)].SetValues("", "", "", "")
		else:
			self.rankList[int(pos)].SetValues(who, level, count, localeInfo.SecondToDHMS(int(cmplTime)))

	def Destroy(self):
		self.ClearDictionary()
		self.buttonList	= []
		for rank in self.rankList:
			rank.Destroy()
		self.rankList = []
		self.basic = None
