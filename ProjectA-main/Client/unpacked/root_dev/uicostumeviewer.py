import ui
import app
import wndMgr
import player
import constInfo
import chr
import localeInfo

class CharacterIds( ):

	INVALID_CHARACTER = -1

	SEX_FEMALE 	= 0
	SEX_MALE 	= 1

	WARRIOR_M 	= 0
	ASSASSIN_W 	= 1
	SURA_M 		= 2
	SHAMAN_W 	= 3
	WARRIOR_W 	= 4
	ASSASSIN_M 	= 5
	SURA_W 		= 6
	SHAMAN_M 	= 7
	MAX_NUM 	= 8

	ASSASSINS 	= [ ASSASSIN_W, ASSASSIN_M ]
	WARRIORS 	= [ WARRIOR_W, WARRIOR_M ]
	SURAS 		= [ SURA_W, SURA_M ]
	SHAMANS 	= [ SHAMAN_W, SHAMAN_M ]

class CostumeViewerWindow(ui.Window):

	BOARD_WIDTH = 339
	BOARD_HEIGHT = 455

	MARGIN_RIGHT = -2

	def __init__(self):
		ui.Window.__init__(self)

		self.currentShape = 0
		self.__LoadWindow()
		self.__LoadGUI()
		self.characterId = CharacterIds.INVALID_CHARACTER

	def __del__(self):
		ui.Window.__del__(self)

	def __LoadWindow(self):
		self.SetSize(self.BOARD_WIDTH, self.BOARD_HEIGHT)
		self.SetCenterPosition()

	def __LoadGUI(self):
		self.viewerBg = ui.ImageBox()
		self.viewerBg.SetParent(self)
		self.viewerBg.SetPosition(0, 2)
		self.viewerBg.AddFlag("attach")
		self.viewerBg.AddFlag("not_pick")
		self.viewerBg.LoadImage("d:/ymir work/ui/game/costume_preview/bg3.tga")
		self.viewerBg.Show()

		# tchat( str( self.viewerBg.GetRight( ) ) )
		# tchat( str( self.viewerBg.GetBottom( ) ) )

		self.renderTarget = ui.RenderTarget()
		self.renderTarget.SetParent(self)
		self.renderTarget.SetSize(339, 453)
		self.renderTarget.AddFlag("attach")
		self.renderTarget.AddFlag("not_pick")
		self.renderTarget.SetPosition(0, 0)
		self.renderTarget.SetRenderTarget(app.RENDER_TARGET_MYSHOPDECO)
		#self.renderTarget.OnMouseRightButtonDown = self.MouseRightClickDown
		#self.renderTarget.OnMouseRightButtonUp = self.MouseRightClickUp
		self.renderTarget.Show()

		viewerBgWidth = 339

		self.titleBar = ui.TitleBar()
		self.titleBar.SetParent(self)
		self.titleBar.MakeTitleBar(0, "red")
		self.titleBar.SetPosition(8, 12)
		self.titleBar.AddFlag("attach")
		self.titleBar.AddFlag("not_pick")
		self.titleBar.SetWidth( viewerBgWidth - 16 )
		self.titleBar.btnClose.SetEvent( ui.__mem_func__(self.OnClose) )
		self.titleBar.Show()

		self.titleName = ui.TextLine()
		self.titleName.SetParent(self.titleBar)
		self.titleName.SetPosition(0, 4)
		self.titleName.AddFlag("attach")
		self.titleName.AddFlag("not_pick")
		self.titleName.SetWindowHorizontalAlignCenter()
		self.titleName.SetHorizontalAlignCenter()
		self.titleName.Show()
		self.titleName.SetText( localeInfo.COSTUME_VIEWER )

	def ResetCharacter( self, characterId ):
		
		if characterId >= 8 or characterId < 0:
			tchat( "invalid character id, setting to 0" )
			characterId = 0

		self.characterId = characterId
		player.SelectShopModel(characterId)
		#player.SetShopModelHair(0)

		# set assasin items
		if characterId in CharacterIds.ASSASSINS:
			#player.SetShopModelWeapon(1179)
			player.SetShopModelArmor(11499)

		# set warrior items
		if characterId in CharacterIds.WARRIORS:
			#player.SetShopModelWeapon(299)
			player.SetShopModelArmor(11299)

		if characterId in CharacterIds.SURAS:
			#player.SetShopModelWeapon(299)
			player.SetShopModelArmor(11699)
		
		if characterId in CharacterIds.SHAMANS:
			#player.SetShopModelWeapon(5119)
			player.SetShopModelArmor(11899)

	def CharacterInList( self, character, charlist ):
		
		for characterClass in charlist:
			if characterClass[ 0 ] == character or characterClass[ 1 ] == character:
				return True

		return False

	def SetProperCharacter( self, ITEM_CHARACTERS, ITEM_SEX, callback, callback_arg ):

		playerCharacter = self.GetPlayerCharacter( )
		playerSex 		= self.GetPlayerSex( )

		# use our player character
		if self.CharacterInList( playerCharacter, ITEM_CHARACTERS ) and playerSex in ITEM_SEX:
					
			# our character can use the item, either use already existing (if its our) or create new with playerchar
			if self.GetCurrentRenderCharacter( ) == playerCharacter:
				callback( callback_arg )
			else:
				self.ResetCharacter( playerCharacter )
				callback( callback_arg )

		# player character cannot be used, check if the already existing char can be used
		elif self.CharacterInList( self.GetCurrentRenderCharacter( ), ITEM_CHARACTERS ) and self.GetCurrentRenderCharacter( ) != playerCharacter:
			callback( callback_arg )

		# cannot use any of chars, get random from ITEM_CHARACTERS and use that instead
		else:
			newCharacter = ITEM_CHARACTERS[ app.GetRandom( 0, len( ITEM_CHARACTERS ) - 1 ) ][ ITEM_SEX[ 0 ] ]
			self.ResetCharacter( newCharacter )
			callback( callback_arg )

	def SetWeapon( self, vnum ):
		player.SetShopModelWeapon( vnum )

	def SetArmor( self, vnum ):
		self.currentShape = vnum
		player.SetShopModelArmor( vnum )

	def SetHair( self, hairNum ):
		if self.currentShape != 94135:
			if not player.SetShopModelHair( hairNum ):
				tchat("costumeviewer SetHair(%d) returns false" % hairNum)

	def SetMonster(self, vnum):
		self.characterId = vnum
		player.SelectShopModel(vnum)

	def GetPlayerCharacter( self ):
		race = player.GetRace( )

		if race >= CharacterIds.MAX_NUM:
			return CharacterIds.WARRIOR_M

		return race

	def GetPlayerSex( self ):
		return chr.RaceToSex( self.GetPlayerCharacter( ) )

	def GetCurrentRenderCharacter( self ):
		return self.characterId

	def OnMouseRightButtonDown(self):
		player.SetMouseState(player.MBT_RIGHT, player.MBS_PRESS_SHOPDECO);
		return True

	def OnMouseRightButtonUp(self):
		player.SetMouseState(player.MBT_RIGHT, player.MBS_CLICK);
		return True

	def Open(self):
		if not constInfo.COSTUME_VIEWER_ENABLED:
			return

		ui.Window.Show(self)
		player.MyShopDecoShow(True)

		# set player character as the first one :)
		self.ResetCharacter( self.GetPlayerCharacter( ) )

		tchat( "PlayerCharacter: " + str( self.GetPlayerCharacter( ) ) )
		tchat( "PlayerSex: " + str( self.GetPlayerSex( ) ) )

	def OnShopClose(self):
		player.MyShopDecoShow(False)
		self.Hide()
		return 1

	def OnClose(self):
		self.OnShopClose()
		return 1

	def OnPressEscapeKey(self):
		self.OnClose()
		return 1

	def OnUpdate(self):
		pass
