import ui
import app
import net
import wndMgr
import localeInfo
import uiCommon

class EventJoinDialog(ui.ScriptWindow):
	def __init__(self):
		ui.ScriptWindow.__init__(self)

		self.eventIndex = 0

		self.LoadWindow()

	def __del__(self):
		ui.ScriptWindow.__del__(self)

	def LoadWindow(self):
		try:
			pyScrLoader = ui.PythonScriptLoader()
			pyScrLoader.LoadScriptFile(self, "uiscript/EventJoinDialog.py")
		except:
			import exception
			exception.Abort("EventJoinDialog.LoadWindow.LoadScript")

		try:
			GetObject=self.GetChild
			self.board = GetObject("board")
			self.eventName = GetObject("event_name_text")
			self.eventDesc = GetObject("event_desc_text")
			self.acceptBtn = GetObject("accept_button")
			self.declineBtn = GetObject("decline_button")
		except:
			import exception
			exception.Abort("EventJoinDialog.LoadWindow.BindObject")

		self.board.SetCloseEvent(self.Close)
		self.acceptBtn.SAFE_SetEvent(self.OnClickAcceptButton)
		self.declineBtn.SAFE_SetEvent(self.DeclineRequest)

	def Destroy(self):
		self.Close()
		ui.ScriptWindow.Destroy(self)

	def Open(self, eventIndex, eventName, eventDesc):
		self.eventIndex = eventIndex

		self.eventName.SetText(eventName)
		self.eventDesc.SetText(eventDesc)

		self.acceptBtn.SetPosition(self.acceptBtn.GetLeft(), self.eventDesc.GetBottom() + 8)
		self.declineBtn.SetPosition(self.declineBtn.GetLeft(), self.eventDesc.GetBottom() + 8)

		self.SetSize(self.GetWidth(), self.acceptBtn.GetBottom() + 15 + 5)
		self.board.SetSize(self.GetWidth(), self.GetHeight())

		self.SetCenterPosition()
		self.Show()

	def DeclineRequest(self):
		net.SendEventRequestAnswerPacket(self.eventIndex, False)
		self.Close()

	def Close(self):
		self.Hide()

	def OnPressEscapeKey(self):
		self.DeclineRequest()
		return True

	def OnClickAcceptButton(self):
		net.SendEventRequestAnswerPacket(self.eventIndex, True)
		self.Close()

	def GetEventIndex(self):
		return self.eventIndex

class EmpireWarScoreBoard(ui.ThinBoard):

	def __init__(self):
		ui.ThinBoard.__init__(self)
		self.Initialize()

	def __del__(self):
		ui.ThinBoard.__del__(self)

	def Destroy(self):
		self.Hide()
		self.Initialize()

	def Initialize(self):
		self.title = None
		self.dataDict = [0, {}, {}, {}]
		self.timeLine = None
		self.isRunning = False
		self.finishTimeout = 0

	def Open(self, timeLeft, kills1, deads1, kills2, deads2, kills3, deads3):
		self.Initialize()
		self.isRunning = True

		# title
		title = ui.TextLine()
		title.SetParent(self)
		title.SetPosition(0, 5)
		title.SetFontName(localeInfo.UI_DEF_FONT_LARGE)
		title.SetWindowHorizontalAlignCenter()
		title.SetHorizontalAlignCenter()
		title.Show()
		self.title = title

		# timeleft
		timeLine = ui.TextLine()
		timeLine.SetParent(self)
		timeLine.SetWindowHorizontalAlignCenter()
		timeLine.SetHorizontalAlignCenter()
		self.timeLine = timeLine
		if timeLeft != 0:
			timeLine.Show()
			self.dataDict[0] = app.GetTime() + timeLeft
		else:
			timeLine.Hide()
			self.dataDict[0] = 0

		# first empire
		empire = 1
		nameLine = ui.TextLine()
		nameLine.SetParent(self)
		nameLine.SetText(localeInfo.EMPIRE_A + ":")
		if empire != net.GetEmpireID():
			nameLine.SetFontColor(1.0, 0.32, 0.32)
		nameLine.Show()
		scoreLine = ui.ExtendedTextLine()
		scoreLine.SetParent(self)
		scoreLine.Show()

		self.dataDict[empire]["NAME"] = nameLine
		self.dataDict[empire]["SCORE"] = scoreLine

		# second empire
		empire = 2
		nameLine = ui.TextLine()
		nameLine.SetParent(self)
		nameLine.SetText(localeInfo.EMPIRE_B + ":")
		if empire != net.GetEmpireID():
			nameLine.SetFontColor(1.0, 0.32, 0.32)
		nameLine.Show()
		scoreLine = ui.ExtendedTextLine()
		scoreLine.SetParent(self)
		scoreLine.Show()

		self.dataDict[empire]["NAME"] = nameLine
		self.dataDict[empire]["SCORE"] = scoreLine

		# second empire
		empire = 3
		nameLine = ui.TextLine()
		nameLine.SetParent(self)
		nameLine.SetText(localeInfo.EMPIRE_C + ":")
		if empire != net.GetEmpireID():
			nameLine.SetFontColor(1.0, 0.32, 0.32)
		nameLine.Show()
		scoreLine = ui.ExtendedTextLine()
		scoreLine.SetParent(self)
		scoreLine.Show()

		self.dataDict[empire]["NAME"] = nameLine
		self.dataDict[empire]["SCORE"] = scoreLine

		self.Refresh(1, kills1, deads1)
		self.Refresh(2, kills2, deads2)
		self.Refresh(3, kills3, deads3)

		self.UpdateSize()
		# self.FadeIn(1, 0, True)
		self.Show()

	def Close(self):
		self.Initialize()
		self.Hide()

	def UpdateSize(self):
		yPos = 25

		if self.timeLine.IsShow():
			self.timeLine.SetPosition(0, yPos)
			self.timeLine.UpdateRect()
			yPos += 20

		for i in xrange(1, 3 + 1):
			self.dataDict[i]["NAME"].SetPosition(10, yPos)
			self.dataDict[i]["NAME"].UpdateRect()
			self.dataDict[i]["SCORE"].SetPosition(self.dataDict[i]["SCORE"].GetLeft(), yPos)
			self.dataDict[i]["SCORE"].UpdateRect()
			yPos += 18

		self.SetSize(200, yPos + 4)
		self.SetPosition(5, wndMgr.GetScreenHeight() - self.GetHeight() - 125)

	def UpdateScore(self, empire, kills, deads):
		self.Refresh(empire, kills, deads)

	def Refresh(self, empire, kills, deads):
		self.title.SetText(localeInfo.EMPIREWAR_SCORE_TITLE)
		self.title.UpdateRect()

		# text
		perc = float(kills) / float(max(1, deads))
		if kills == 0 and deads == 0:
			perc = 1.0
		percColor = "r="+str(int(255 - (255 - 35) * perc + 0.5))+" g="+str(int(35 + (255 - 35) * perc + 0.5))+" b=35"
		scoreLine = self.dataDict[empire]["SCORE"]
		scoreLine.SetText(("<TEXT r=35 g=255 b=35 text=\"%03d\"> / <TEXT r=255 g=35 b=35 text=\"%03d\"> (<TEXT "+percColor+" text=\"%06.02f%%\">)") % (kills, deads, perc * 100))
		# position
		scoreValueLeft = max(self.dataDict[1]["NAME"].GetRight(), self.dataDict[2]["NAME"].GetRight(), self.dataDict[3]["NAME"].GetRight()) + 6
		for i in xrange(3):
			self.dataDict[i + 1]["SCORE"].SetPosition(scoreValueLeft + 10, self.dataDict[i + 1]["SCORE"].GetTop())

	def OnUpdate(self):
		# ui.Window.OnUpdate(self)
		
		if self.isRunning:
			if self.dataDict[0] != 0:
				secLeft = max(int(self.dataDict[0] - app.GetTime()), 0)
				self.timeLine.SetText("Endet in %s" % localeInfo.SecondToDHMS(secLeft))
				self.timeLine.UpdateRect()

		else:
			if self.finishTimeout != 0 and max(int(self.finishTimeout - app.GetTime()), 0) == 0:
				self.finishTimeout = 0
				# self.FadeOut(2, 0, True)
				self.Hide()

	def OnFinish(self):
		self.isRunning = False
		self.finishTimeout = app.GetTime() + 60 # close window after 60 seconds

		self.timeLine.SetText("Beendet")
		self.timeLine.Show()
		self.UpdateSize()


class AngelsDemonsSelectFractionWindow( ui.ScriptWindow ):

	TEAM_ANGELS = 1
	TEAM_DEMONS = 2

	TEAM_DICT = {
		TEAM_ANGELS : localeInfo.ANGELSDEMONS_FRACTION_ANGELS,
		TEAM_DEMONS : localeInfo.ANGELSDEMONS_FRACTION_DEMONS,
	}

	def __init__( self ):

		ui.ScriptWindow.__init__( self )

		self.dlgQuestion = None
		self.LoadWindow( )

	def __del__( self ):
		ui.ScriptWindow.__del__( self )

	def LoadWindow( self ):

		try:
			PythonScriptLoader = ui.PythonScriptLoader( )
			PythonScriptLoader.LoadScriptFile( self, "UIScript/angeldemonselectwindow.py" )

			# Add close event to the title bar
			self.GetChild( "title_bar" ).SetCloseEvent( self.Close )

			# Add events to left/right buttons
			self.GetChild( "button_join_angels" ).SetEvent( self.__SelectFraction, self.TEAM_ANGELS )
			self.GetChild( "button_join_demons" ).SetEvent( self.__SelectFraction, self.TEAM_DEMONS )

			self.background 	= self.GetChild( "background" )
			self.angelsDesc 	= self.GetChild( "description_angels" )
			self.demonsDesc 	= self.GetChild( "description_demons" )

			self.angelsDesc.SetWidth( 130 )
			self.demonsDesc.SetWidth( 130 )

		except:
			import exception
			exception.Abort( "AngelsDemonsSelectFractionWindow.LoadWindow.BindObject" )

	def __SelectFraction( self, fraction ):
		self.dlgQuestion = uiCommon.QuestionDialog( )

		fractionName = str( self.TEAM_DICT[ fraction ] )
		questionText = localeInfo.ANGELSDEMONS_ARE_YOU_SURE

		# just in case of bad translation somewhere...
		try:
			questionText = questionText % fractionName
		except:
			questionText = localeInfo.ANGELSDEMONS_ARE_YOU_SURE

		self.dlgQuestion.SetText( questionText )
		self.dlgQuestion.SAFE_SetAcceptEvent( self.SendSelectedFraction, fraction )
		self.dlgQuestion.SetCancelEvent( self.dlgQuestion.Close )
		self.dlgQuestion.Open( )

	def SendSelectedFraction( self, fraction ):
		net.SendChatPacket( "/angelsdemons_select_fraction {}".format( fraction ) )
		self.dlgQuestion.Close( )
		self.Close( )

	def Open( self ):
		self.SetCenterPosition( )
		self.SetTop( )
		self.Show( )

	def Close( self ):
		self.Hide( )

	def OnPressEscapeKey( self ):
		self.Close( )
		return True