import app
import exception
import ui
import constInfo
import event
import player
import uiToolTip
import uiScriptLocale

class zi_Reward_Window(ui.ScriptWindow):
	COLUMN_ITEM_LIST = ( 33001, 33007, 33002, 33008, 33003, 33009, 33004, 33010, 33005, 33011, 33006, 33012, 33013, 33014, 33015, 33016, 33017, 33018, 33019, 33020, 33021, 33022 )
	testttttz = ( 
		uiScriptLocale.DAY, 
		uiScriptLocale.BATTLE_FIELD_MONDAY, 
		uiScriptLocale.BATTLE_FIELD_TUESDAY, 
		uiScriptLocale.BATTLE_FIELD_WEDNESDAY, 
		uiScriptLocale.BATTLE_FIELD_THURSDAY, 
		uiScriptLocale.BATTLE_FIELD_FRIDAY, 
		uiScriptLocale.BATTLE_FIELD_SATURDAY, 
		"Guardian Insignia", 
		"Zi Insignia", 
		"Chou Insignia", 
		"Yin Insignia", 
		"Mao Insignia", 
		"Chen Insignia", 
		"Si Insignia", 
		"Wu Insignia", 
		"Wei Insignia", 
		"Shen Insignia", 
		"You Insignia", 
		"Xu Insignia", 
		"Hai Insignia", 
		"Number in inventory", 
		uiScriptLocale.REQUIRED_AMOUNT, 
		uiScriptLocale.DAY, 
		uiScriptLocale.BATTLE_FIELD_MONDAY, 
		uiScriptLocale.BATTLE_FIELD_TUESDAY, 
		uiScriptLocale.BATTLE_FIELD_WEDNESDAY, 
		uiScriptLocale.BATTLE_FIELD_THURSDAY, 
		uiScriptLocale.BATTLE_FIELD_FRIDAY, 
		"%s/%s" % (uiScriptLocale.BATTLE_FIELD_SATURDAY, uiScriptLocale.BATTLE_FIELD_SUNDAY), 
		"Zodiac Insignia", 
		"Jia Insignia", 
		"Yi Insignia", 
		"Bing Insignia", 
		"Ding Insignia", 
		"Mu Insignia", 
		"Ji Insignia", 
		"Geng Insignia", 
		"Xin Insignia", 
		"Ren Insignia", 
		"Gui Insignia", 
		"Number in inventory", 
		uiScriptLocale.REQUIRED_AMOUNT
	)

	def __init__(self):
		ui.ScriptWindow.__init__(self)
		constInfo.ZODIAC_WINDOW_FIX = 1
		self.LoadWindow()

	def __del__(self):
		ui.ScriptWindow.__del__(self)

	def LoadWindow(self):
		try:
			pyScrLoader = ui.PythonScriptLoader()
			pyScrLoader.LoadScriptFile(self, "UIScript/zirewardwindow.py")
		except:
			exception.Abort("zi_Reward_Window.LoadDialog.LoadScript")

		try:
			GetObject=self.GetChild
			self.board = GetObject("board")
			self.titleBar = GetObject("TitleBar")
			self.titleBar.SetCloseEvent(ui.__mem_func__(self.OnPressEscapeKey))
			self.YellowInactive = GetObject("YellowInactive")
			self.GreenInactive = GetObject("GreenInactive")
			self.AllClearButtonInactive = GetObject("AllClearButtonInactive")
			self.muietiger0 = GetObject("muietiger0")
			self.muietiger1 = GetObject("muietiger1")

			self.Gods = []
			for a in xrange(22):
				self.Gods.append(self.GetChild("muiezenu%d" % (a)))
				
			self.Tool = []
			for b in xrange(42):
				self.Tool.append(self.GetChild("bg_weekly_row_%d" % (b)))
				testttt = self.testttttz[b]
				self.Tool[b].SetToolTipWindow(self.__CreateGameTypeToolTip(testttt))
				
			self.YellowBTN = []
			for c in xrange(30):
				self.YellowBTN.append(self.GetChild("YellowBTN_%d" % (c)))
				self.YellowBTN[c].SetEvent(lambda arg=c: self.__yellow_check_box(arg))

			self.GreenBTN = []
			for d in xrange(33):
				self.GreenBTN.append(self.GetChild("GreenBTN_%d" % (d)))
				self.GreenBTN[d].SetEvent(lambda arg=d + 30: self.__yellow_check_box(arg))

		except:
			exception.Abort("zi_Reward_Window.LoadDialog.BindObject")

	def OnUpdate(self):
		arra = constInfo.ZODIAC_RETURN_YELLOW_CHECKBOX
		for e in xrange(30):
			if int(arra[e]) == 1:
				self.YellowBTN[e].Hide()
			else:
				self.YellowBTN[e].Show()

		for f in xrange(30):
			if int(arra[f + 30]) == 1:
				self.GreenBTN[f].Hide()
			else:
				self.GreenBTN[f].Show()

		for l in xrange(2):
			if int(arra[l + 60]) == 2 or int(arra[l + 60]) == 0:
				self.GreenBTN[l + 30].Hide()
			else:
				self.GreenBTN[l + 30].Show()

		if int(arra[62]) >= 1 and int(arra[63]) >= 1:
			self.GreenBTN[32].Show()
			self.muietiger0.SetText("%d" % int(arra[62]))
			self.muietiger1.SetText("%d" % int(arra[63]))
		else:
			self.GreenBTN[32].Hide()
			self.muietiger0.SetText("%d" % int(arra[62]))
			self.muietiger1.SetText("%d" % int(arra[63]))

		for g in xrange(22):
			itemCount = player.GetItemCountByVnum(self.COLUMN_ITEM_LIST[g])
			self.Gods[g].SetText("%d" % itemCount)

	def __yellow_check_box(self, box):
		constInfo.ZODIAC_CHECKBOX_REMEMBER = str(box + 1)
		yellow_check_box_1 = constInfo.ZODIAC_YELLOW_CHECKBOX
		event.QuestButtonClick(yellow_check_box_1)

	def OnPressEscapeKey(self):
		constInfo.ZODIAC_WINDOW_FIX = 0
		self.Hide()
		return True

	def __CreateGameTypeToolTip(self, descList):
		toolTip = uiToolTip.ToolTip()
		toolTip.AutoAppendTextLine(descList)
		toolTip.AlignHorizonalCenter()
		toolTip.SetAlwaysUp(True)
		return toolTip

	def Destroy(self):
		self.ClearDictionary()
		self.board = None
		self.titleBar = None
		self.YellowInactive = None
		self.GreenInactive = None
		self.AllClearButtonInactive = None
		self.muietiger0 = None
		self.muietiger1 = None
		self.Gods = None
		self.Tool = None
		self.YellowBTN = None
		self.GreenBTN = None
