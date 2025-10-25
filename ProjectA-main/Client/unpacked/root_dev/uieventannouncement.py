import ui
import localeInfo
import app
import constInfo
import time
import wndMgr

class EventAnnouncement( ui.ScriptWindow ):

	def __init__( self ):

		ui.ScriptWindow.__init__( self )
		self.LoadWindow( )

		self.eventId 	= 0
		self.timeStamp 	= 0
		self.interface = None

	def __del__( self ):
		ui.ScriptWindow.__del__( self )

	def LoadWindow( self ):

		try:
			PythonScriptLoader = ui.PythonScriptLoader( )
			PythonScriptLoader.LoadScriptFile( self, "UIScript/eventannouncement.py" )

			self.background 	= self.GetChild( "background" )
			self.timeLeft		= self.GetChild( "time_left_text" )
			self.threadBtn 		= self.GetChild( "open_thread_btn" )

			self.threadBtn.SetEvent( self.OpenThread )

		except:
			import exception
			exception.Abort( "EventAnnouncement.LoadWindow.BindObject" )

		
	def OpenThread( self ):
		url = constInfo.EVENTS[ self.eventId ][ 1 ]
		app.ShellExecute( url, False )

	def OpenWithType( self, eventId, finishTimeStamp ):

		# Hide if eventId is 0
		if not eventId:
			self.Close( )
			return

		if eventId > len( constInfo.EVENTS ):
			return

		self.eventId = eventId
		self.timeStamp = finishTimeStamp

		# Change background
		image 	= constInfo.EVENTS[ eventId ][ 0 ]


		# Show the window
		self.Open( )

	def Open( self ):

		if not constInfo.ENABLE_EVENT_ANNOUNCEMENTS:
			return

		self.Show( )

	def Close( self ):
		self.Hide( )

	def BindInterface( self, interface ):
		self.interface = interface

	def OnUpdate( self ):

		if self.IsShow( ):

			difference = self.timeStamp - int( app.GetTime( ) )

			if difference < 0:
				self.Close( )
				return

			hours 	= int( difference / 3600 )
			minutes = int( ( difference - hours * 3600 ) / 60 )
			seconds = int( difference - hours * 3600 - minutes * 60 )

			newTime = "{:02}:{:02}:{:02}".format( hours, minutes, seconds )

			self.timeLeft.SetText( newTime )

			if self.interface:

				shiftWindow = False

				if self.interface.wndEventIcon and self.interface.wndEventIcon.IsShow() or \
					self.interface.wndCardsIcon and self.interface.wndCardsIcon.IsShow() or \
					self.interface.wndJigsawIcon and self.interface.wndJigsawIcon.IsShow():
					shiftWindow = True

				if shiftWindow:
					(x, y) = (wndMgr.GetScreenWidth() - 180 - 184 - 80, 38)
					self.SetPosition(x, y)