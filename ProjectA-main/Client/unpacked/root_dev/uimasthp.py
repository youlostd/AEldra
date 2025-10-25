import ui
import localeInfo
import app
import wndMgr
import constInfo

class MastBoard( ui.Window ):

	BOARD_WIDTH 	= 100
	BOARD_HEIGHT 	= 147

	def __init__( self ):

		ui.Window.__init__( self )
		self.__LoadWindow( )

	def __del__( self ):
		ui.Window.__del__( self )

	def __LoadWindow( self ):

		boardX, boardY = ( wndMgr.GetScreenWidth( ) - 246, 5 )

		if constInfo.IS_TEST_SERVER:
			boardX -= 100

		self.SetSize( self.BOARD_WIDTH, self.BOARD_HEIGHT )
		self.SetPosition( boardX, boardY )

		self.background = ui.ImageBox( )
		self.background.SetParent( self )
		self.background.SetPosition( 0, 0 )
		self.background.LoadImage( "d:/ymir work/ui/game/mast/bg.tga" )

		self.mastBlack = ui.ImageBox( )
		self.mastBlack.SetParent( self.background )
		self.mastBlack.SetPosition( 12, 8 )
		self.mastBlack.LoadImage( "d:/ymir work/ui/game/mast/mast_black.tga" )

		self.mastColor = ui.ExpandedImageBox( )
		self.mastColor.SetParent( self.background )
		self.mastColor.SetPosition( 12, 8 )
		self.mastColor.LoadImage( "d:/ymir work/ui/game/mast/mast_color.tga" )

		# Show images
		self.background.Show( )
		self.mastBlack.Show( )
		self.mastColor.Show( )

	def Open( self ):
		self.Show( )

	def UpdateMastHp( self, hpPct ):

		self.Open( )

		hpPercentage = float( hpPct ) / 100.00

		if hpPercentage < 0.00:
			hpPercentage = 0.00

		if hpPercentage > 1.00:
			hpPercentage = 1.00

		hpDiff = 1.0 - hpPercentage
		
		self.mastColor.SetRenderingRect( 0.0, -( hpDiff ), 0.0, 0.0 )

	def OnUpdate( self ):
		pass
