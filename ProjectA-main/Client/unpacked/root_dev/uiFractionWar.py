import ui
import localeInfo
import constInfo
import net
import uiCommon
import uiScriptLocale

root_dir = "d:/ymir work/ui/fraction_wnd/"

dic = {
	"lock" : root_dir+"slot_locked.tga",
	"active" : root_dir+"slot_active.tga",
	"red" : root_dir+"slot_win_red.tga",
	"blue" : root_dir+"slot_win_blue.tga"
}

dictStatus = {
	0 : "lock",
	1 : "blue",
	2 : "red",
	3 : "active"
}

Desc = [
		[uiScriptLocale.BDAY_EVENT_DESC_D1, uiScriptLocale.BDAY_EVENT_REWARD_D1, "","16.04.2019"],
		[uiScriptLocale.BDAY_EVENT_DESC_D2, uiScriptLocale.BDAY_EVENT_REWARD_D2, "","17.04.2019"],
		[uiScriptLocale.BDAY_EVENT_DESC_D3, uiScriptLocale.BDAY_EVENT_REWARD_D3, "","18.04.2019"],
		[uiScriptLocale.BDAY_EVENT_DESC_D4, uiScriptLocale.BDAY_EVENT_REWARD_D4, "","19.04.2019"],
		[uiScriptLocale.BDAY_EVENT_DESC_D5, uiScriptLocale.BDAY_EVENT_REWARD_D5, "","20.04.2019"],
		[uiScriptLocale.BDAY_EVENT_DESC_D6, uiScriptLocale.BDAY_EVENT_REWARD_D6, "","21.04.2019"],
		[uiScriptLocale.BDAY_EVENT_DESC_D7, uiScriptLocale.BDAY_EVENT_REWARD_D7, "","22.04.2019"],
	]

class ChooseFactionWindow(ui.ScriptWindow):
	TEAM_ANGELS = 1
	TEAM_DEMONS = 2

	TEAM_DICT = {
		TEAM_ANGELS : localeInfo.ANGELSDEMONS_FRACTION_ANGELS,
		TEAM_DEMONS : localeInfo.ANGELSDEMONS_FRACTION_DEMONS,
	}

	def __init__(self):
		ui.ScriptWindow.__init__(self)

		self.dlgQuestion = None
		self.LoadWindow()

	def __del__(self):
		ui.ScriptWindow.__del__(self)

	def LoadWindow(self):

		try:
			PythonScriptLoader = ui.PythonScriptLoader()
			PythonScriptLoader.LoadScriptFile(self, "UIScript/ChooseFractionWindow.py")

			# Add close event to the title bar
			self.GetChild("title_bar").SetCloseEvent(self.Close)

			# Add events to left/right buttons
			self.GetChild("button_join_angels").SetEvent(self.__SelectFraction, self.TEAM_ANGELS)
			self.GetChild("button_join_demons").SetEvent(self.__SelectFraction, self.TEAM_DEMONS)

			self.background 	= self.GetChild("background")
			self.angelsDesc 	= self.GetChild("description_angels")
			self.demonsDesc 	= self.GetChild("description_demons")

			self.angelsDesc.SetWidth(130)
			self.demonsDesc.SetWidth(130)

		except:
			import exception
			exception.Abort("AngelsDemonsSelectFractionWindow.LoadWindow.BindObject")

	def __SelectFraction(self, fraction):
		self.dlgQuestion = uiCommon.QuestionDialog()

		fractionName = str(self.TEAM_DICT[ fraction ])
		questionText = localeInfo.ANGELSDEMONS_ARE_YOU_SURE

		# just in case of bad translation somewhere...
		try:
			questionText = questionText % fractionName
		except:
			questionText = localeInfo.ANGELSDEMONS_ARE_YOU_SURE

		self.dlgQuestion.SetText(questionText)
		self.dlgQuestion.SAFE_SetAcceptEvent(self.SendSelectedFraction, fraction)
		self.dlgQuestion.SetCancelEvent(self.dlgQuestion.Close)
		self.dlgQuestion.Open()

	def SendSelectedFraction(self, fraction):
		net.SendChatPacket("/angelsdemons_select_fraction {}".format(fraction))
		self.dlgQuestion.Close()
		self.Close()

	def Open(self):
		self.SetCenterPosition()
		self.SetTop()
		self.Show()

	def Close(self):
		self.Hide()

	def OnPressEscapeKey(self):
		self.Close()
		return True

class FactionWindow(ui.ScriptWindow):
	class Row:
		def __init__(self,parent,arg):
			self.row = ui.ImageBox()
			self.row.SetParent(parent)
			self.row.SetPosition(5,(arg * 67) + 5.5)
			self.Set(0,"","","","")
			self.row.Show()
			
			self.qDesc = ui.TextLine()
			self.qDesc.SetParent(self.row)
			
			self.rewDesc = ui.TextLine()
			self.rewDesc.SetParent(self.row)
			
			self.date = ui.TextLine()
			self.date.SetParent(self.row)
			
			self.time = ui.TextLine()
			self.time.SetParent(self.row)

		def Set(self,arg,a,b,c,d):
			self.row.LoadImage(dic[dictStatus[arg]])
			self.Init(arg,a,b,c,d)
			
		def Init(self,arg,quest_desc,rew_desc,a_time,a_date):
			if dictStatus[arg] == "lock":
				pass
			elif dictStatus[arg] == "active":
				self.qDesc.SetWindowHorizontalAlignCenter()
				self.qDesc.SetHorizontalAlignCenter()
				self.qDesc.SetPosition(0,10)
				#self.qDesc.SetOutline()
				self.qDesc.SetFontName("Tahoma:16")
				self.qDesc.SetText(quest_desc)
				self.qDesc.Show()
				
				self.rewDesc.SetWindowHorizontalAlignCenter()
				self.rewDesc.SetHorizontalAlignCenter()
				self.rewDesc.SetPosition(0,40)
				#self.rewDesc.SetOutline()
				self.rewDesc.SetFontName("Tahoma:16")
				self.rewDesc.SetText(rew_desc)
				self.rewDesc.Show()
			elif dictStatus[arg] == "red" or dictStatus[arg] == "blue":
				self.rewDesc.SetWindowHorizontalAlignLeft()
				self.rewDesc.SetHorizontalAlignLeft()
				self.rewDesc.SetPosition(10,7)
				self.rewDesc.SetFontName("Tahoma:16")
				self.rewDesc.SetText(rew_desc)
				self.rewDesc.Show()
				
				self.time.SetWindowHorizontalAlignLeft()
				self.time.SetHorizontalAlignLeft()
				self.time.SetPosition(10,24)
				self.time.SetFontName("Tahoma:16")
				self.time.SetText(a_time)
				self.time.Show()
				
				self.date.SetWindowHorizontalAlignLeft()
				self.date.SetHorizontalAlignLeft()
				self.date.SetPosition(10,40)
				self.date.SetFontName("Tahoma:16")
				self.date.SetText(a_date)
				self.date.Show()
		
		def Destroy(self):
			self.time = None
			self.rewDesc = None
			self.qDesc = None
			self.date = None
			
	def __init__(self):
		ui.ScriptWindow.__init__(self)
		self.__LoadWindow()

	def __del__(self):
		ui.ScriptWindow.__del__(self)

	def Open(self):
		self.Show()

	def Close(self):
		self.Hide()

	def __LoadWindow(self):
		try:
			pyScrLoader = ui.PythonScriptLoader()
			pyScrLoader.LoadScriptFile(self, "UIScript/FractionWindow.py")
		except:
			import exception
			exception.Abort("FactionWindow.LoadWindow.LoadObject")
			
		self.header = self.GetChild("header")
		self.base = self.GetChild("board")
		self.button = self.GetChild("button")
		self.angelProgress = self.GetChild("blue_bar")
		self.ball = self.GetChild("ball")
		
		self.button.SAFE_SetEvent(self.toggle)

		self.rows = []
		for x in xrange(7):
			row = self.Row(self.base,x)
			self.rows.append(row)
		self.base.Hide()

		self.Update(1,1)

	def Update(self,angel,demon):
		max = angel + demon
		if max == 0:
			angel = 1
			demon = 1
			max = 2
		self.angelProgress.SetPercentage(angel, max)
		self.ball.SetPosition(((174 * angel) / max) - 10, -7)

	def Set(self,*args):
		i = 0
		found = False
		for a in args:
			if a == 0 and not found:
				found = True
				a = 3
			self.rows[i].Set(a,*Desc[i])
			i += 1
			
	def toggle(self):
		if self.base.IsShow():
			self.base.Hide()
			self.SetSize(335,119) 
		else:
			self.base.Show()
			self.SetSize(335,119+479) 
	
	def Destroy(self):
		self.ClearDictionary()
		
	def OnPressEscapeKey(self):
		self.Close()
		return True
