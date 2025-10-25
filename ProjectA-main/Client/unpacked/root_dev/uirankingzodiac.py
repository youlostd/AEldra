import app
import exception
import ui
import constInfo
import event
import player
import uiToolTip
import localeInfo

class RankingZodiac(ui.ScriptWindow):
	ZODIAC_GODS_NAME = ( "Zodiac Gods List", "Zi", "Chou", "Yin", "Mao", "Chen", "Si", "Wu", "Wei", "Shen", "You", "Xu", "Hai" )

	def __init__(self):
		ui.ScriptWindow.__init__(self)
		self.LoadWindow()

	def __del__(self):
		ui.ScriptWindow.__del__(self)

	def LoadWindow(self):
		try:
			pyScrLoader = ui.PythonScriptLoader()
			pyScrLoader.LoadScriptFile(self, "UIScript/rankingzodiac.py")
		except:
			exception.Abort("RankingZodiac.LoadDialog.LoadScript")

		try:
			GetObject=self.GetChild
			self.board = GetObject("zirankingboard")
			self.titleBar = GetObject("TitleBar")
			self.titleBar.SetCloseEvent(ui.__mem_func__(self.OnPressEscapeKey))
			
			
			self.Zi_Rank_Name = []
			self.Zi_Rank_Level = []
			self.Zi_Rank_Time = []
			self.Zi_Rank_Date = []

			for i in xrange(0,10+1):
				i = i + 1
				try:
					self.Zi_Rank_Name.append(self.GetChild("Zi_Rank_Name_%d" % i))
					self.Zi_Rank_Level.append(self.GetChild("Zi_Rank_Level_%d" % i))
					self.Zi_Rank_Time.append(self.GetChild("Zi_Rank_Time_%d" % i))
					self.Zi_Rank_Date.append(self.GetChild("Zi_Rank_Date_%d" % i))
					#import chat
					#chat.AppendChat(7,"rank entries built")
				except:
					continue

			self.Zi_RankingWindow = GetObject("TitleName")

		except:
			exception.Abort("RankingZodiac.LoadDialog.BindObject")

		
	def OnUpdate(self):
		ZI_GOD_CODE_TO_NAME = str(self.ZODIAC_GODS_NAME[int(constInfo.ZI_PORTAL)])
		self.Zi_RankingWindow.SetText("%s Guardian Rankings" % ZI_GOD_CODE_TO_NAME)

		for i in xrange(0,10+1):
			itor = 0
			try:
				itor = constInfo.MISSION_X[i+1]
			except:
				#import chat
				#chat.AppendChat(7,"skipping update for entry %d len(%d)" % (i,len(constInfo.MISSION_X)))
				continue

			ZI_Name = itor[0]
			ZI_Level = itor[1]
			ZI_Time = itor[2]
			ZI_Date = itor[3]

			ZI_FIXED_TIME = localeInfo.ZodiacTimeReturn(max(0, int(ZI_Time)))
			#import chat
			#chat.AppendChat(7,"self.Zi_Rank_Name len %d" % len(self.Zi_Rank_Name))

			try:
				self.Zi_Rank_Name[i].SetText(ZI_Name)
				self.Zi_Rank_Level[i].SetText("%d" % ZI_Level)
				self.Zi_Rank_Time[i].SetText(ZI_FIXED_TIME)
				self.Zi_Rank_Date[i].SetText(ZI_Date)
			except:
				pass

	def OnPressEscapeKey(self):
		self.Hide()
		return True
