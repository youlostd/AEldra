import ui
import rune
import app
import grp
import localeInfo
import uiToolTip
import snd
import uiCommon
import item
import player
import uiScriptLocale
import net
import constInfo
import cfg
import chat
import uiAffectShower
import chr

BASE_PATH = "d:/ymir work/ui/game/runes/"

class RuneMainWindow(ui.BaseScriptWindow):

	# permanent alpha change on mainglow
	MAIN_GLOW_ANI_ACTIVE_DURATION = 0.75 # time that the glow needs to get its alpha from inactive -> active
	MAIN_GLOW_ANI_SLEEP_DURATION = 0.3 # time that the glow waits before going from active -> inactive
	MAIN_GLOW_ANI_INACTIVE_DURATION = 1.0 # time that the glow needs to get its alpha from active -> inactive after sleeping
	MAIN_GLOW_ANI_ALPHA_ACTIVE = 1.0 # active alpha of the glow
	MAIN_GLOW_ANI_ALPHA_INACTIVE = 0.3 # inactive alpha of the glow

	SELECT_ANI_ACTIVE_DURATION = 0.4 # time that the objects need to get their alpha from inactive -> active when hovered
	SELECT_ANI_INACTIVE_DURATION = 0.4 # time that the objects need to get their alpha from active -> inactive when unhovered
	SELECT_ANI_ALPHA_ACTIVE = 1.0 # active alpha of the objects
	SELECT_ANI_ALPHA_INACTIVE = 0.0 # expected inactive alpha of the objects

	#################################################
	## MAIN FUNCTIONS
	#################################################

	def __init__(self, openSubWndFunc):
		ui.BaseScriptWindow.__init__(self, "RuneWindow", self.__BindObject)

		self.overGroup = -1
		self.selectAniData = []
		self.openSubWndFunc = ui.__mem_func__(openSubWndFunc)

		self.__LoadWindow()

	def __BindObject(self):
		for i in xrange(rune.GROUP_MAX_NUM):
			self._AddLoadObject("group%d" % i, {
				"wnd" : "main_%d" % (i + 1),
				"circle_glow" : "main_%d_circle_glow" % (i + 1),
				"text_bg" : "main_%d_textbg" % (i + 1),
				"title" : "main_%d_title" % (i + 1),
				"glow" : "main_%d_glow" % (i + 1),
			})

	def __LoadWindow(self):

		for i in xrange(rune.GROUP_MAX_NUM):
			group = self.main["group%d" % i]

			obj = group["glow"]
			obj.SAFE_SetStringEvent("MOUSE_OVER_IN", self.__OnMouseOverGroup, i)
			obj.SAFE_SetStringEvent("MOUSE_OVER_OUT", self.__OnMouseOutGroup, i)
			obj.SAFE_SetStringEvent("MOUSE_LEFT_UP", self.__OnClickGroup, i)

			group["circle_glow"].SetAlpha(self.SELECT_ANI_ALPHA_INACTIVE)

		self.__StartMainGlowAnimation()
		self.Refresh()

		selectedType = rune.PageGetType(False)
		if selectedType >= 0:
			self.__OnClickGroup(selectedType)

		self.GetChild( "title_bar" ).SetCloseEvent( self.Close )

	def Refresh(self):
		pass

	def __OnMouseOverGroup(self, index):
		self.__StopMainGlowAnimation()
		self.main["group%d" % index]["glow"].ClearAlphaLoop()

		self.__StartSelectAnimation(index)
		self.overGroup = index

	def __OnMouseOutGroup(self, index):
		self.__StartUnselectAnimation(index)
		if self.overGroup == index:
			self.overGroup = -1

	def __OnClickGroup(self, index):
		if self.main["group%d" % index]["glow"].IsIn():
			self.Close()
			wnd = self.openSubWndFunc(index)
			if wnd:
				wnd.SetPosition(self.GetLeft(), self.GetTop())
			snd.PlaySound( "sound/ui/click.wav" )

	def OnUpdate(self):
		self.__UpdateAnimations()

	#################################################
	## ANIMATE FUNCTIONS
	#################################################

	def __UpdateAnimations(self):
		## remove list
		removeList = []

		### select animation
		maxTimeDict = {"select" : self.SELECT_ANI_ACTIVE_DURATION, "unselect" : self.SELECT_ANI_INACTIVE_DURATION}
		try:
			for mData in self.selectAniData:
				group = self.main["group%d" % mData["index"]]

				maxTime = maxTimeDict[mData["type"]]
				pct = (app.GetTime() - mData["time"]) / maxTime
				if pct >= 1.0:
					pct = 1.0

				# alpha computing for "select" type
				alphaGlow = mData["alpha"] + (self.MAIN_GLOW_ANI_ALPHA_ACTIVE - mData["alpha"]) * pct
				alphaCircle = self.SELECT_ANI_ALPHA_INACTIVE + (self.SELECT_ANI_ALPHA_ACTIVE - self.SELECT_ANI_ALPHA_INACTIVE) * pct

				# reverse if it's "unselect" type
				if mData["type"] == "unselect":
					alphaGlow = mData["alpha"] + (self.MAIN_GLOW_ANI_ALPHA_INACTIVE - mData["alpha"]) * pct
					alphaCircle = (self.SELECT_ANI_ALPHA_ACTIVE + self.SELECT_ANI_ALPHA_INACTIVE) - alphaCircle
					#alphaText = (alphaTextOver + alphaTextBase) - alphaText

				# set alpha to objects
				group = self.main["group%d" % mData["index"]]
				group["glow"].SetAlpha(alphaGlow)
				group["circle_glow"].SetAlpha(alphaCircle)

				# check if the animation ended
				if pct == 1.0:
					removeList.append(mData["index"])
		except TypeError:
			pass

		## remove all animations
		for index in removeList:
			for i in xrange(len(self.selectAniData)):
				if self.selectAniData[i]["index"] == index:
					del self.selectAniData[i]
					break

		## check for restart of main glow ani
		if len(self.selectAniData) == 0 and len(removeList) > 0 and self.overGroup == -1:
			self.__StartMainGlowAnimation()

	def __StartMainGlowAnimation(self):
		fullDuration = self.MAIN_GLOW_ANI_ACTIVE_DURATION + self.MAIN_GLOW_ANI_SLEEP_DURATION + self.MAIN_GLOW_ANI_INACTIVE_DURATION

		for i in xrange(rune.GROUP_MAX_NUM):
			obj = self.main["group%d" % i]["glow"]
			obj.SetAlpha(self.MAIN_GLOW_ANI_ALPHA_INACTIVE)
			obj.SetAlphaLoop(i * self.MAIN_GLOW_ANI_ACTIVE_DURATION, self.MAIN_GLOW_ANI_ACTIVE_DURATION, self.MAIN_GLOW_ANI_INACTIVE_DURATION,\
				self.MAIN_GLOW_ANI_ALPHA_INACTIVE, self.MAIN_GLOW_ANI_ALPHA_ACTIVE,\
				self.MAIN_GLOW_ANI_SLEEP_DURATION, rune.GROUP_MAX_NUM * self.MAIN_GLOW_ANI_ACTIVE_DURATION - fullDuration)

	def __StopMainGlowAnimation(self):
		for i in xrange(rune.GROUP_MAX_NUM):
			obj = self.main["group%d" % i]["glow"]
			obj.StopAlphaLoop()

	def __StartSelectAnimation(self, index):
		group = self.main["group%d" % index]
		circleAlpha = group["circle_glow"].GetAlpha()

		startTime = app.GetTime() - self.SELECT_ANI_ACTIVE_DURATION * ((circleAlpha - self.SELECT_ANI_ALPHA_INACTIVE) / (self.SELECT_ANI_ALPHA_ACTIVE - self.SELECT_ANI_ALPHA_INACTIVE))

		for i in xrange(len(self.selectAniData)):
			if self.selectAniData[i]["index"] == index:
				del self.selectAniData[i]
				break

		self.selectAniData.append({
			"type" : "select",
			"time" : startTime,
			"alpha" : self.main["group%d" % index]["glow"].GetAlpha(),
			"index" : index,
		})

	def __StartUnselectAnimation(self, index):
		group = self.main["group%d" % index]
		circleAlpha = group["circle_glow"].GetAlpha()

		startTime = app.GetTime() - self.SELECT_ANI_INACTIVE_DURATION * \
			(1.0 - ((circleAlpha - self.SELECT_ANI_ALPHA_INACTIVE) / (self.SELECT_ANI_ALPHA_ACTIVE - self.SELECT_ANI_ALPHA_INACTIVE)))

		for i in xrange(len(self.selectAniData)):
			if self.selectAniData[i]["index"] == index:
				del self.selectAniData[i]
				break

		self.selectAniData.append({
			"type" : "unselect",
			"time" : startTime,
			"alpha" : self.main["group%d" % index]["glow"].GetAlpha(),
			"index" : index,
		})

class RuneTutorialWindow( ui.ScriptWindow ):

	MIN_PAGE = 0
	MAX_PAGE = 3

	def __init__( self ):

		ui.ScriptWindow.__init__( self )
	
		# Load window and it's elements
		self.LoadWindow( )

		self.choosenPage = self.MIN_PAGE

	def __del__( self ):
		ui.ScriptWindow.__del__( self )

	def LoadWindow( self ):

		try:
			PythonScriptLoader = ui.PythonScriptLoader( )
			PythonScriptLoader.LoadScriptFile( self, "UIScript/runetutorialwindow.py" )

			# Add close event to the title bar
			self.GetChild( "title_bar" ).SetCloseEvent( self.Close )

			# Add events to left/right buttons
			self.GetChild( "button_left" ).SetEvent( self.__LeftButtonClicked )
			self.GetChild( "button_right" ).SetEvent( self.__RightButtonClicked )

			self.background 	= self.GetChild( "background" )
			self.description 	= self.GetChild( "description" )
			self.leftButton 	= self.GetChild( "button_left" )
			self.rightButton 	= self.GetChild( "button_right" )

		except:
			import exception
			exception.Abort( "RuneTutorialWindow.LoadWindow.BindObject" )

	def ChangeText( self, pageIndex ):

		descriptionText = ""

		try:
			descriptionText = localeInfo.GetLocals()[ "RUNE_TUTORIAL_DESC_{}".format( pageIndex + 1 ) ]
		except:
			descriptionText = "None"

		self.description.SetText( descriptionText )

	def Open( self ):
		self.SetCenterPosition( )
		self.SetTop( )
		self.Show( )

		# Open first page
		self.OpenPage( self.MIN_PAGE )

	def GetPreviousPageIndex( self ):

		if self.choosenPage == self.MIN_PAGE:
			return self.choosenPage

		if self.choosenPage <= self.MAX_PAGE:
			return self.choosenPage - 1

	def GetNextPageIndex( self ):

		if self.choosenPage == self.MAX_PAGE:
			return self.choosenPage

		if self.choosenPage >= self.MIN_PAGE:
			return self.choosenPage + 1

	def RefreshButtons( self ):
		
		# Show/hide left button
		if self.choosenPage == self.MIN_PAGE:
			self.leftButton.Hide( )
		else:
			self.leftButton.Show( )

		# Show/hide right button
		if self.choosenPage == self.MAX_PAGE:
			self.rightButton.Hide( )
		else:
			self.rightButton.Show( )

	def OpenPage( self, index ):

		self.choosenPage = index
		
		# Refresh background image
		self.RefreshButtons( )

		# Change background
		self.background.LoadImage( "d:/ymir work/ui/game/runes_tut/bg_{}.tga".format( index + 1 ) )

		# Set text
		self.ChangeText( index )

	def __LeftButtonClicked( self ):
		self.OpenPage( self.GetPreviousPageIndex( ) )

	def __RightButtonClicked( self ):
		self.OpenPage( self.GetNextPageIndex( ) )

	def Close( self ):
		self.Hide( )

	def OnPressEscapeKey( self ):
		self.Close( )
		return True

	def OnUpdate( self ):
		pass

class RuneSubWindow(ui.BaseScriptWindow):

	CIRCLE_DIFFUSE_COLOR = [
		## group1
		[1.0, 1.0, 1.0, 1.0],
		## group2
		[120.0/255.0, 0.0, 0.0, 1.0],
		## group3
		[95.0/255.0, 0.0, 1.0, 1.0],
		## group4
		[0.0, 1.0, 1.0, 1.0],
		## group5
		[0.0, 140.0/255.0, 1.0, 1.0],
	]
	CIRCLE_DIFFUSE_DEFAULT_COLOR = [1.0, 1.0, 1.0, 1.0]

	GROUP_LOCALE = [
		{
			"name" : localeInfo.GetLocals()["RUNE_GROUP_%d_NAME" % (i + 1)],
			"desc" : localeInfo.GetLocals()["RUNE_GROUP_%d_DESC" % (i + 1)],
		} for i in xrange(rune.GROUP_MAX_NUM)
	]

	GROUP_TITLE_COLORS = [
		grp.GenerateColor(200.0 / 255.0, 170.0 / 255.0, 110.0 / 255.0, 1.0),
		grp.GenerateColor(212.0 / 255.0,  66.0 / 255.0,  66.0 / 255.0, 1.0),
		grp.GenerateColor(159.0 / 255.0, 170.0 / 255.0, 252.0 / 255.0, 1.0),
		grp.GenerateColor(161.0 / 255.0, 213.0 / 255.0, 134.0 / 255.0, 1.0),
		grp.GenerateColor( 73.0 / 255.0, 170.0 / 255.0, 110.0 / 185.0, 1.0),
	]
	DEFAULT_TITLE_COLOR = grp.GenerateColor(240.0 / 255.0, 230.0 / 255.0, 210.0 / 255.0, 1.0)

	GROUP_NAMES = ["main", "sub"]

	MAIN_RUNE_COUNT = 3
	SUB_RUNE_COUNT = 2
	RUNE_COUNT = {
		"main" : MAIN_RUNE_COUNT,
		"sub" : SUB_RUNE_COUNT,
	}

	RUNE_COUNT_PER_GROUP = 3

	class BuyPointWindow( ui.BoardWithTitleBar ):

		WIDTH 	= 200
		HEIGHT 	= 100

		ELEMENT_START_POS = 10

		def __init__( self ):
			ui.BoardWithTitleBar.__init__( self )

			self.neededItems 			= [ ]
			self.neededItemsElements 	= [ ]
			self.neededYangsAmount 		= 0

			self.elementStartPos 		= self.ELEMENT_START_POS

			self.popupDlg = uiCommon.PopupDialog( )
			self.popupDlg.Close( )

			self.LoadWindow( )

			if constInfo.ENABLE_LEVEL2_RUNES:
				self.runeVnum = -1

		def __del__( self ):
			ui.BoardWithTitleBar.__del__( self )

		def LoadWindow( self ):

			self.AddFlag( "float" )
			self.AddFlag( "movable" )
			self.SetSize( self.WIDTH, self.HEIGHT )
			self.SetCloseEvent( self.Close )
			self.SetTitleName( localeInfo.BUY_POINTS )

			self.upgradeButton = ui.Button( )
			self.upgradeButton.SetParent( self )
			self.upgradeButton.SetUpVisual( "d:/ymir work/ui/public/Middle_Button_01.sub" )
			self.upgradeButton.SetOverVisual( "d:/ymir work/ui/public/Middle_Button_02.sub" )
			self.upgradeButton.SetDownVisual( "d:/ymir work/ui/public/Middle_Button_03.sub" )
			self.upgradeButton.SetWindowVerticalAlignBottom( )
			self.upgradeButton.SetWindowHorizontalAlignCenter( )
			self.upgradeButton.SetPosition( -61 / 2 - 5, 30 )
			self.upgradeButton.SetEvent( self.OnUpgradeButton )
			self.upgradeButton.SetText( uiScriptLocale.ATTRTREE_REFINE_UPGRADE )
			self.upgradeButton.Show( )

			self.cancelButton = ui.Button( )
			self.cancelButton.SetParent( self )
			self.cancelButton.SetUpVisual( "d:/ymir work/ui/public/Middle_Button_01.sub" )
			self.cancelButton.SetOverVisual( "d:/ymir work/ui/public/Middle_Button_02.sub" )
			self.cancelButton.SetDownVisual( "d:/ymir work/ui/public/Middle_Button_03.sub" )
			self.cancelButton.SetWindowVerticalAlignBottom( )
			self.cancelButton.SetWindowHorizontalAlignCenter( )
			self.cancelButton.SetPosition( 61 / 2 + 5, 30 )
			self.cancelButton.SetEvent( self.OnCancelButton )
			self.cancelButton.SetText( uiScriptLocale.ATTRTREE_REFINE_CANCEL )
			self.cancelButton.Show( )

			self.neededYangs = ui.TextLine( )
			self.neededYangs.SetParent( self )
			self.neededYangs.SetWindowVerticalAlignBottom( )
			self.neededYangs.SetWindowHorizontalAlignCenter( )
			self.neededYangs.SetHorizontalAlignCenter( )
			self.neededYangs.SetPosition( 0, 52 )
			self.neededYangs.SetText( "" )
			self.neededYangs.Show( )

		def __OnOverInItem(self, itemVnum):
			if self.tooltip:
				self.tooltip.SetItemToolTip(itemVnum)

		def __OnOverOutItem(self):
			if self.tooltip:
				self.tooltip.HideToolTip()

		def SetToolTip(self, tooltip):
			self.tooltip = tooltip

		def OnUpgradeButton( self ):
			
			# check requirements
			errText = localeInfo.ATTRTREE_UPGRADE_ERROR

			if player.GetElk( ) < self.neededYangsAmount:
				self.popupDlg.SetText( errText % localeInfo.NumberToMoneyString( self.neededYangsAmount ) )
				self.popupDlg.Open( )
				return

			for itemData in self.neededItems:

				if player.GetItemCountByVnum( itemData[ 0 ] ) < itemData[ 1 ]:

					item.SelectItem(1, 2, itemData[ 0 ] )
					self.popupDlg.SetText( errText % ( "%dx %s" % ( itemData[ 1 ], item.GetItemName( ) ) ) )
					self.popupDlg.Open( )
					return

			# upgrade
			if constInfo.ENABLE_LEVEL2_RUNES:
				if self.runeVnum != -1:
					net.SendChatPacket("/level_rune %d" % self.runeVnum)
				else:
					net.SendChatPacket( "/accept_rune_points_buy" )
			else:
				net.SendChatPacket( "/accept_rune_points_buy" )
			self.Close( )

		def OnCancelButton( self ):
			self.Close( )

		def SetNeededItems( self, neededItems ):
			self.neededItems = neededItems

		def SetNeededYangs( self, yangs ):
			self.neededYangsAmount = yangs

		def Close( self ):
			self.Hide( )

		def OnPressEscapeKey( self ):
			self.Close( )
			return True

		def Open( self ):

			# clear elements
			self.neededItemsElements = [ ]
			self.elementStartPos = self.ELEMENT_START_POS

			for item in self.neededItems:
				self.AddNeededItemElement( item[ 0 ], item[ 1 ] )

			self.neededYangs.SetText( localeInfo.TOOLTIP_BUYPRICE % localeInfo.NumberToMoneyString( self.neededYangsAmount ) )

			self.RefreshSize( )

			self.SetCenterPosition( )
			self.SetTop( )
			self.Show( )

		def RefreshSize( self ):
			
			if len( self.neededItemsElements ) < 1:
				self.SetSize( self.WIDTH, self.HEIGHT )
				return

			PADDING 	= 50

			newHeight = 10 + PADDING + ( len( self.neededItemsElements ) * ( self.neededItemsElements[ 0 ][ 0 ].GetHeight( ) + 5 ) )

			self.SetSize( self.WIDTH, newHeight )

		def AddNeededItemElement( self, vnum, count ):
			
			imgSlot = ui.ImageBox( )
			imgSlot.SetParent( self )
			imgSlot.SetPosition( 10, self.elementStartPos )
			imgSlot.LoadImage( "d:/ymir work/ui/public/slot_base.sub" )
			imgSlot.Show( )

			item.SelectItem(1, 2, vnum )

			img = ui.ImageBox( )
			img.SetParent( imgSlot ) 
			img.LoadImage( item.GetIconImageFileName( ) )
			img.Show( )

			img.SAFE_SetStringEvent("MOUSE_OVER_IN", self.__OnOverInItem, vnum)
			img.SAFE_SetStringEvent("MOUSE_OVER_OUT", self.__OnOverOutItem)

			imgSlot.img = img

			text = ui.TextLine( )
			text.SetParent( self )
			text.SetPosition( imgSlot.GetRight( ) + 10, ( imgSlot.GetTop( ) + imgSlot.GetHeight( ) / 2 ) - 2 )
			text.SetVerticalAlignCenter( )
			text.Show( )

			if count > 1:
				text.SetText( "%dx %s" % ( count, item.GetItemName( ) ) )
			else:
				text.SetText( "%s" % item.GetItemName( ) )

			self.elementStartPos += imgSlot.GetHeight( ) + 5
			self.neededItemsElements.append( [ imgSlot, text ] )


	if constInfo.REQ_ITEM_RESET_RUNE:
		class ResetRuneWindow(ui.BoardWithTitleBar):
			def __init__( self ):
				ui.BoardWithTitleBar.__init__(self)
				self.__LoadWindow()

			def __del__( self ):
				ui.BoardWithTitleBar.__del__(self)

			def __LoadWindow(self):
				self.AddFlag("float")
				self.AddFlag("movable")
				self.SetSize(300, 84)
				self.SetCloseEvent(self.Close)
				self.SetTitleName(localeInfo.RUNE_RESET_WINDOW_TITLE)

				self.text = ui.MakeTextLine(self)
				self.text.SetText(localeInfo.CONFIRM_RUNE_RESET)
				self.text.SetPosition(0, -36)

				self.confirm = ui.MakeButton(self, 85, 61, "", "d:/ymir work/ui/public/", "Middle_Button_01.sub", "Middle_Button_02.sub", "Middle_Button_03.sub")
				self.confirm.SetText(localeInfo.YES)
				self.confirm.SetEvent(self.__OnConfirmButton)

				self.cancel = ui.MakeButton(self, 157, 61, "", "d:/ymir work/ui/public/", "Middle_Button_01.sub", "Middle_Button_02.sub", "Middle_Button_03.sub")
				self.cancel.SetText(localeInfo.NO)
				self.cancel.SetEvent(self.__OnCancelButton)

				self.imgSlot = ui.MakeImageBox(self, "d:/ymir work/ui/public/slot_base.sub", 134, 20)

				item.SelectItem(1, 2, 93267)
				img = ui.ImageBox()
				img.SetParent(self.imgSlot)
				img.LoadImage(item.GetIconImageFileName())
				img.Show()
				img.SAFE_SetStringEvent("MOUSE_OVER_IN", self.__OnOverInItem)
				img.SAFE_SetStringEvent("MOUSE_OVER_OUT", self.__OnOverOutItem)

				self.imgSlot.img = img

				# self.text2 = ui.MakeTextLine(self)
				# self.text2.SetText(item.GetItemName())
				# self.text2.SetPosition(27 + 40, -9)

			def __OnOverInItem(self):
				if self.tooltip:
					self.tooltip.SetItemToolTip(93267)

			def __OnOverOutItem(self):
				if self.tooltip:
					self.tooltip.HideToolTip()

			def __OnConfirmButton(self):
				if player.GetItemCountByVnum(93267) < 1:
					item.SelectItem(1, 2, 93267)
					import chat
					chat.AppendChat(chat.CHAT_TYPE_INFO, localeInfo.REQUIRE_ITEM_RESET_RUNE(item.GetItemName()))
				else:
					net.SendChatPacket("/reset_runes")

				self.Close()

			def __OnCancelButton(self):
				self.Close()

			def SetToolTip(self, tooltip):
				self.tooltip = tooltip

			def Open(self):
				self.SetCenterPosition()
				self.SetTop()
				self.Show()

			def Close(self):
				self.Hide()

			def OnPressEscapeKey(self):
				self.Close()
				return True

	#################################################
	## MAIN FUNCTIONS
	#################################################

	def __init__(self, openMainWndFunc):
		ui.BaseScriptWindow.__init__(self, "RuneSubWindow", self.__BindObject)

		self.openMainWndFunc = ui.__mem_func__(openMainWndFunc)
		self.__Initialize()
#		self.DEBUG_CurDiffuse = []
#		self.DEBUG_CurIndex = 0

		self.toolTip = uiToolTip.ItemToolTip( 180 )
		self.toolTip.HideToolTip( )

		self.pageId = 0

		self.tutorialWnd = None

		self.normalRunesWithDesc = [30, 57]

		self.popupDlg = uiCommon.PopupDialog( )
		self.popupDlg.Close( )

		self.questionDlg = uiCommon.QuestionDialog( )
		self.questionDlg.Close( )

		self.buyPointWnd = self.BuyPointWindow( )
		self.buyPointWnd.Close( )
		self.buyPointWnd.SetToolTip(self.toolTip)

		self.affectShower = uiAffectShower.AffectShower()

		if constInfo.REQ_ITEM_RESET_RUNE:
			self.wndResetRune = self.ResetRuneWindow()
			self.wndResetRune.SetToolTip(self.toolTip)

		self.__LoadWindow()

	def __Initialize(self):
		self.needRefresh = False
		self.selectStates = {
			"main" : [False for i in xrange(self.MAIN_RUNE_COUNT + 1)],
			"sub" : [False for i in xrange(self.SUB_RUNE_COUNT + 1)],
		}

		self.selectStates["main"][self.MAIN_RUNE_COUNT] = True

	def OpenTutorialWindow( self ):

		if not self.tutorialWnd:
			self.tutorialWnd = RuneTutorialWindow( )

		self.tutorialWnd.Open( )

	def __BindObject(self):
		self._AddLoadObject("background", "background")

		# buttons
		self._AddLoadObject("btn_save", "save_button")
		self._AddLoadObject("btn_reset", "reset_button")
		self._AddLoadObject("btn_add", "addpoint_button")
		self._AddLoadObject("btn_resetpoints", "resetpoint_button")
		self._AddLoadObject("btn_info", "info_button")

		for i in xrange( 5 ):
			self._AddLoadObject("btn_page_%s" % str( i ), "page_%s" % str( i + 1 ) )

		# points
		self._AddLoadObject( "points", "points_bg" )

		# group lines
		self._AddLoadObject( "group_line_long", "group_line_long" )
		self._AddLoadObject( "group_line_short", "group_line_short" )

		# main group
		self._AddLoadObject("main_group", {
			"btn" : "group_circle",
			"below" : "group_circle_below",
			"img" : "group_image",
			"name" : "group_name",
			"desc" : "group_desc",
			"arrow" : "arrow",
			"subtitle_image" : "subtitle_image",
			"subtitle_text" : "subtitle_text",
		})
		# main runes
		self._AddLoadObject("main_rune_main", {
			"btn" : "rune_circle_main",
			"name" : "rune_main_name",
			"noname" : "rune_main_noname",
			"desc" : "rune_main_desc",
			"select_wnd" : "rune_select_main",
			"select" : ["rune_select_main_%d" % (j + 1) for j in xrange(self.RUNE_COUNT_PER_GROUP)],
			"desc2" : "rune_main_desc_2",
		})
		for i in xrange(self.MAIN_RUNE_COUNT):
			self._AddLoadObject("main_rune_%d" % i, {
				"btn" : "rune_circle_%d" % (i + 1),
				"name" : "rune_%d_name" % (i + 1),
				"noname" : "rune_%d_noname" % (i + 1),
				"desc" : "rune_%d_desc" % (i + 1),
				"select_wnd" : "rune_select_%d" % (i + 1),
				"select" : ["rune_select_%d_%d" % (i + 1, j + 1) for j in xrange(self.RUNE_COUNT_PER_GROUP)],
				"arrow" : "arrow", # % (i + 1),
			})

		# sub group
		self._AddLoadObject("sub_group", {
			"btn" : "sub_group_circle",
			"below" : "sub_group_below",
			"name" : "sub_group_name",
			"noname" : "sub_group_noname",
			"desc" : "sub_group_desc",
			"select_wnd" : "sub_group_select",
			"select" : ["sub_group_select_%d" % (j + 1) for j in xrange(rune.GROUP_MAX_NUM - 1)],
		})
		# sub runes
		for i in xrange(self.SUB_RUNE_COUNT):
			self._AddLoadObject("sub_rune_%d" % i, {
				"btn" : "sub_rune_circle_%d" % (i + 1),
				"name" : "sub_rune_name_%d" % (i + 1),
				"noname" : "sub_rune_noname_%d" % (i + 1),
				"nogroup" : "sub_rune_nogroup_%d" % (i + 1),
				"desc" : "sub_rune_desc_%d" % (i + 1),
			})
		# sub rune selector
		self._AddLoadObject("sub_select", {
			"wnd" : "sub_rune_select",
			"select" : ["sub_rune_select_%d_%d" % (1 + j / self.RUNE_COUNT_PER_GROUP, 1 + (j % self.RUNE_COUNT_PER_GROUP)) \
				for j in xrange(rune.SUBGROUP_SECONDARY_MAX * self.RUNE_COUNT_PER_GROUP)],
		})

		if constInfo.ENABLE_RUNE_PAGES:
			for x in xrange(4): # page number
				self._AddLoadObject("btn_select_page_%d" % x, "page_button_%d" % x)

	def __LoadWindow(self):
		#self.main["close"].SAFE_SetEvent( self.Close )

		self.GetChild( "title_bar" ).SetCloseEvent( self.Close )

		self.main["main_group"]["btn"].SAFE_SetEvent(self.BackToMainWindow)

		self.main["btn_reset"].SAFE_SetEvent(self.__Reset)
		self.main["btn_save"].SAFE_SetEvent(self.__Save)
		self.main["btn_add"].SAFE_SetEvent(self.__OnAddPointButton)
		self.main["btn_info"].SAFE_SetEvent(self.__OpenRuneTutorial)
		self.main["btn_resetpoints"].SAFE_SetEvent(self.__OnResetPointsButton)

		for i in range( 5 ):
			self.main[ "btn_page_%s" % str( i ) ].SAFE_SetEvent( self.__ChangePageButton, i )
			self.main[ "btn_page_%s" % str( i ) ].Hide( )
			
		groupName = "main"
		for i in xrange(self.RUNE_COUNT[groupName]):
			curRune = self.main["main_rune_%d" % i]

			curRune["btn"].SAFE_SetEvent(self.__ToggleSelection, groupName, i)
			for j in xrange(self.RUNE_COUNT_PER_GROUP):
				curRune["select"][j].SAFE_SetEvent(self.__SelectRune, groupName, i, j)
				self.main["sub_select"]["select"][i * self.RUNE_COUNT_PER_GROUP + j].SAFE_SetEvent(self.__SelectRune, "sub", i, j)

				# TOOLTIP ON/OUT MOUSE
				curRune["select"][j].SAFE_SetOverInEvent( self.__MouseOnRune, ( groupName, i, j ) )
				curRune["select"][j].SAFE_SetOverOutEvent( self.__MouseOutRune, ( groupName, i, j ) )
				self.main["sub_select"]["select"][i * self.RUNE_COUNT_PER_GROUP + j].SAFE_SetOverInEvent( self.__MouseOnRune, ( "sub", i, j ) )
				self.main["sub_select"]["select"][i * self.RUNE_COUNT_PER_GROUP + j].SAFE_SetOverOutEvent( self.__MouseOutRune, ( "sub", i, j ) )

				# ADD "+" BUTTON
				buttonParent = curRune[ "select" ][ j ]
				( x, y ) = buttonParent.GetLocalPosition( )
				button = ui.MakeButton( curRune[ "select_wnd" ], x + 35, y + 35, "", "d:/ymir work/ui/game/windows/", "btn_plus_up.sub", "btn_plus_over.sub", "btn_plus_down.sub" )
				button.SetEvent( self.OnPlusButton, ( groupName, i, j ) )
				buttonParent.addButton = button

				buttonParent = self.main[ "sub_select" ][ "select" ][ i * self.RUNE_COUNT_PER_GROUP + j ]
				( x, y ) = buttonParent.GetLocalPosition( )
				button = ui.MakeButton( self.main[ "sub_select" ][ "wnd" ], x + 35, y + 35, "", "d:/ymir work/ui/game/windows/", "btn_plus_up.sub", "btn_plus_over.sub", "btn_plus_down.sub" )
				button.SetEvent( self.OnPlusButton, ( "sub", i, j ) )
				buttonParent.addButton = button


		self.main["main_rune_main"]["btn"].SAFE_SetEvent(self.__ToggleSelection, "main", self.MAIN_RUNE_COUNT)
		for j in xrange(self.RUNE_COUNT_PER_GROUP):
			self.main["main_rune_main"]["select"][j].SAFE_SetEvent(self.__SelectRune, "main", self.MAIN_RUNE_COUNT, j)

			# TOOLTIP ON/OUT MOUSE
			self.main["main_rune_main"]["select"][j].SAFE_SetOverInEvent( self.__MouseOnRune, ( "main", self.MAIN_RUNE_COUNT, j ) )
			self.main["main_rune_main"]["select"][j].SAFE_SetOverOutEvent( self.__MouseOutRune, ( "main", self.MAIN_RUNE_COUNT, j ) )

			buttonParent = self.main[ "main_rune_main" ][ "select" ][ j ]
			( x, y ) = buttonParent.GetLocalPosition( )
			button = ui.MakeButton( self.main[ "main_rune_main" ][ "select_wnd" ], x + 35, y + 35, "", "d:/ymir work/ui/game/windows/", "btn_plus_up.sub", "btn_plus_over.sub", "btn_plus_down.sub" )
			button.SetEvent( self.OnPlusButton, ( groupName, self.MAIN_RUNE_COUNT, j ) )
			buttonParent.addButton = button

		# sub group-selector
		self.main["sub_group"]["btn"].SAFE_SetEvent(self.__ToggleSelection, "sub", self.SUB_RUNE_COUNT)
		for i in xrange(rune.GROUP_MAX_NUM - 1):
			self.main["sub_group"]["select"][i].SAFE_SetEvent(self.__SelectSubGroup, i)

		# sub rune-selector
		for i in xrange(self.SUB_RUNE_COUNT):
			self.main["sub_rune_%d" % i]["btn"].SAFE_SetEvent(self.__ToggleSelection, "sub", i)

		self.GetChild( "title_bar" ).SetCloseEvent( self.Close )
		self.GetChild( "subtitle_image" ).SetAlpha( 0.5 )

		#self.__ChangePageButton( 0 )

		if constInfo.ENABLE_RUNE_PAGES:
			self.currentPage = -1
			self.lastPage = -1
			self.firstTime = True
			for x in xrange(4): # page number
				self.main["btn_select_page_%d" % x].SAFE_SetEvent(self.__OnSelectPage, x)

		self.Refresh( )

	if constInfo.ENABLE_RUNE_PAGES:
		def __OnSelectPage(self, page):
			# if not net.IsPrivateMap() and constInfo.RUNE_CHANGE_PULSE + 5 > app.GetTime():
			# 	chat.AppendChat(chat.CHAT_TYPE_INFO, localeInfo.RUNE_PAGE_CANNOT_SAVE_YET)
			# 	for x in xrange(4): # page number
			# 		if x != self.currentPage:
			# 			self.main["btn_select_page_%d" % x].SetUp()
			# 	return

			# constInfo.RUNE_CHANGE_PULSE = app.GetTime()
			self.lastPage = self.currentPage
			self.currentPage = page
			for x in xrange(4): # page number
				if x != page:
					self.main["btn_select_page_%d" % x].SetUp()
			net.SendChatPacket("/get_rune_page %d" % self.currentPage)

		def SetRunePage(self, index, vnum):
			if index == 9999:
				for x in xrange(4): # page number
					if x != self.lastPage:
						self.main["btn_select_page_%d" % x].SetUp()
					self.main["btn_select_page_%d" % self.lastPage].SetDown()
				self.currentPage = self.lastPage
			elif index == -1:
				rune.PageSetType(vnum)
				if vnum == rune.PageGetType(False):
					rune.PageResetNew()

				if vnum == rune.PageGetType(False):
					self.selectStates["main"][self.MAIN_RUNE_COUNT] = False
			else:
				if index < 4: # RUNE_MAIN_COUNT
					rune.PageSetVnum(index, vnum)
				elif index == (4 + 2): # RUNE_MAIN_COUNT + RUNE_SUB_COUNT
					rune.PageSetSubType(vnum)
				else:
					rune.PageSetSubVnum(index - 4, vnum) # RUNE_MAIN_COUNT

			self.__CheckChanged()

			self.__Load()
			self.Refresh()
			self.OnUpdate()
			tchat("%d %d" % (index, vnum))
			rune.PageSaveNew()

		def SelectRunePage(self, page):
			self.currentPage = page
			self.main["btn_select_page_%d" % page].Down()

	def __OnResetPointsButton( self ):
		if constInfo.REQ_ITEM_RESET_RUNE:
			self.wndResetRune.Open()
			return

		net.SendChatPacket( "/reset_runes" )

	def __OpenRuneTutorial( self ):

		if not constInfo.RUNE_TUTORIAL_ENABLED:
			app.ShellExecute( constInfo.URL[ "runeinfo" ], False )
			return

		self.OpenTutorialWindow( )

	def BuyRune( self, vnum ):
		if constInfo.ENABLE_LEVEL2_RUNES:
			if self.__HasRune(vnum):
				net.SendChatPacket("/open_rune_level %d" % vnum)
			else:
				net.SendChatPacket( "/use_buy_rune %d" % vnum )
		else:
			net.SendChatPacket( "/use_buy_rune %d" % vnum )
		self.questionDlg.Close( )

		# Refresh
		self.__Refresh( )

	def OnPlusButton( self, runeData ):

		groupName 	= runeData[ 0 ]
		groupIndex = rune.PageGetType( True )

		if groupName == "sub":
			groupIndex = rune.PageGetSubType( True )

		runeIndex 	= runeData[ 1 ]
		subIndex 	= runeData[ 2 ]

		runeVnum = rune.GetIDByIndex( groupIndex, runeIndex, subIndex )
		runeName = self.GetRuneName( runeVnum )

		askMessage = ""

		try:
			askMessage = localeInfo.RUNE_BUY_MESSAGE % runeName
		except:
			askMessage = localeInfo.RUNE_BUY_MESSAGE

		if constInfo.ENABLE_LEVEL2_RUNES:
			if self.__HasRune(runeVnum):
				askMessage = localeInfo.RUNE_LEVEL_UP_CONFIRM(runeName)

		# Show "are you sure" dialog
		self.questionDlg.SetText( askMessage )
		self.questionDlg.SetWidth( 300 )
		self.questionDlg.SetAcceptText( uiScriptLocale.YES )
		self.questionDlg.SetCancelText( uiScriptLocale.NO )
		# Buy rune
		self.questionDlg.SAFE_SetAcceptEvent( self.BuyRune, runeVnum )
		# Close dialog
		self.questionDlg.SetCancelEvent( self.questionDlg.Close )
		self.questionDlg.Open( )

	def Close( self ):
		self.buyPointWnd.Close( )
		self.Hide( )

		if self.tutorialWnd:
			self.tutorialWnd.Close( )

		if constInfo.REQ_ITEM_RESET_RUNE:
			self.wndResetRune.Close()

	def __ChangePageButton( self, index ):

		clickedPage = index + 1

		self.main[ "btn_page_%d" % index ].SetDown( )

		for i in range( 5 ):
			
			if i == index:
				continue

			self.main[ "btn_page_%d" % i ].SetUp( )

		self.pageId = index

		tchat( "Clicked page: " + str( clickedPage ) )

	def __OnAddPointButton( self ):
		net.SendChatPacket( "/open_rune_points_buy" )

	def OpenRuneRefine(self, refineProto, cost):
		self.buyPointWnd.SetNeededItems(refineProto)
		self.buyPointWnd.SetNeededYangs(cost)
		self.buyPointWnd.Open( )
		if constInfo.ENABLE_LEVEL2_RUNES:
			self.buyPointWnd.SetTitleName( localeInfo.BUY_POINTS )
			self.buyPointWnd.runeVnum = -1

	if constInfo.ENABLE_LEVEL2_RUNES:
		def OpenRuneLevel(self, refineProto, cost, vnum):
			self.buyPointWnd.SetNeededItems(refineProto)
			self.buyPointWnd.SetNeededYangs(cost)
			self.buyPointWnd.Open()
			self.buyPointWnd.SetTitleName(localeInfo.RUNE_LEVEL_UP_REFINE)
			self.buyPointWnd.runeVnum = vnum

	def UpdatePoints( self ):
		amountStr = str( constInfo.RUNE_POINTS )
		self.GetChild( "points_amount" ).SetText( amountStr )

	def GetRuneName( self, runeVnum ):
		
		runeName = "None"

		# return "None", no Vnum specified
		if not runeVnum:
			return runeName

		# try to use the locale name
		try:
			runeName = localeInfo.GetLocals()[ "RUNE_KEYSTONE_NAME_%d" % runeVnum ]
		
		# exception occured, use proto name
		except:
			runeName = rune.GetProtoName( runeVnum )

		return runeName

	def GetAffectStringByRuneVnum( self, runeVnum ):
		if constInfo.ENABLE_LEVEL2_RUNES:
			if self.__HasRune(runeVnum + 100):
				runeVnum += 100
		group, subGroup, subGroupIndex, name, applyType = rune.GetProto( runeVnum )
		applyValue = rune.GetProtoApplyValue( runeVnum )

		if not applyType:
			return "None"

		affectString = uiToolTip.GET_AFFECT_STRING( applyType, applyValue )

		if not affectString:
			return "None"

		return affectString

	def ChangeTooltip( self, runeVnum ):

		runeName 		= self.GetRuneName( runeVnum )
		description 	= rune.GetProtoDesc( runeVnum )
		affectString 	= self.GetAffectStringByRuneVnum( runeVnum )

		self.toolTip.ClearToolTip( )
		self.toolTip.SetTitle( runeName )

		if description:
			self.toolTip.AutoAppendTextLine( description )

		if affectString != "None":
			self.toolTip.AutoAppendTextLine( affectString )

		# it calls .ResizeTooltip so no need to call it twice
		self.toolTip.AlignHorizonalCenter( )

	def __MouseOnRune( self, runeData ):

		groupName 	= runeData[ 0 ]
		groupIndex = rune.PageGetType( True )

		if groupName == "sub":
			groupIndex = rune.PageGetSubType( True )

		runeIndex 	= runeData[ 1 ]
		subIndex 	= runeData[ 2 ]

		hoveredVnum = rune.GetIDByIndex( groupIndex, runeIndex, subIndex )

		self.ChangeTooltip( hoveredVnum )
		self.toolTip.ShowToolTip( )	

	def __MouseOutRune( self, runeId ):
		self.toolTip.HideToolTip( )

	def OnUpdate(self):
		if self.needRefresh:
			self.needRefresh = False
			self.__Refresh()

	def __GetRuneID(self, groupIdx, pos):
		subGroup = (pos / self.MAIN_RUNE_COUNT) - 1
		if subGroup < 0:
			subGroup = rune.SUBGROUP_PRIMARY
		return rune.GetIDByIndex(groupIdx, subGroup, pos % self.MAIN_RUNE_COUNT)

	def __HasRune(self, runeID):
		return rune.HasRune(runeID)

	def __SetObjectColor(self, obj, color):
		return
		#obj.SetDiffuseColor(color[0], color[1], color[2], color[3])

	def __SetRuneColor(self, rune, color):
		self.__SetObjectColor(rune["btn"], color)
		if rune.has_key("select"):
			for i in xrange(self.RUNE_COUNT_PER_GROUP):
				self.__SetObjectColor(rune["select"][i], color)

	def __SetGroupIndex(self, groupName, groupIndex):
		group = self.main["%s_group" % groupName]

		# load group data
		group["img"].LoadImage(BASE_PATH + "rune%d/sub_circle_inner.tga" % (groupIndex + 1))
		group["name"].SetText(self.GROUP_LOCALE[groupIndex]["name"])
		group["desc"].SetText(self.GROUP_LOCALE[groupIndex]["desc"])

		# load group color
		nameColor = self.GROUP_TITLE_COLORS[groupIndex]
		group["name"].SetPackedFontColor(nameColor)

		# load circle colors
		if groupIndex >= 0:
			circleColor = self.CIRCLE_DIFFUSE_COLOR[groupIndex]
		else:
			circleColor = self.CIRCLE_DIFFUSE_DEFAULT_COLOR

		self.__SetObjectColor(group["btn"], circleColor)
		self.__SetObjectColor(group["below"], circleColor)

		if groupName == "main":
			self.__SetRuneColor(self.main["%s_rune_main" % groupName], circleColor)

		for i in xrange(self.RUNE_COUNT[groupName]):
			curRune = self.main["%s_rune_%d" % (groupName, i)]
			self.__SetRuneColor(curRune, circleColor)

		# for main group: load sub group-selector images
		if groupName == "main":
			addGroup = 0
			for i in xrange(rune.GROUP_MAX_NUM - 1):
				if groupIndex == i:
					addGroup = 1
				grpIdx = i + addGroup

				self.main["sub_group"]["select"][i].SetInnerVisual(BASE_PATH + "rune%d/sub_circle_inner.tga" % (grpIdx + 1))

		# load circle images and set name colors
		if groupName == "main":
			self.__RefreshSelectionRunes(groupName)

	def __RefreshSelectionRunes(self, groupName):
		if groupName == "main":
			groupIndex = rune.PageGetType(True)
		else:
			groupIndex = rune.PageGetSubType(True)
		nameColor = self.GROUP_TITLE_COLORS[groupIndex]

		if constInfo.ENABLE_LEVEL2_RUNES:
			groupRunes = []

		if groupName == "main":
			runeNames = ["%s_rune_main" % groupName] + ["%s_rune_%d" % (groupName, i) for i in xrange(self.RUNE_COUNT[groupName])]
			j = 0
			#tchat("-----")
			for name in runeNames:
				curRune = self.main[name]
				curRune["name"].SetPackedFontColor(nameColor)
				for i in xrange(self.RUNE_COUNT_PER_GROUP):
					runeID = self.__GetRuneID(groupIndex, j)
					hasRune = self.__HasRune(runeID)

					#tchat("HasRune[ id: %s, groupIndex: %s ] = %s" % ( str( j ), str( groupIndex ), str( hasRune ) ) )

					grayExt = ""
					if not hasRune:
						grayExt = "_g"

					curRune["select"][i].SetEnabled(hasRune)
					if constInfo.ENABLE_LEVEL2_RUNES:
						if self.__HasRune(runeID + 100):
							curRune["select"][i].SetInnerVisual(BASE_PATH + "lv2/rune%d/rune_%d%s.tga" % (groupIndex + 1, j + 1, grayExt))
						else:
							curRune["select"][i].SetInnerVisual(BASE_PATH + "rune%d/rune_%d%s.tga" % (groupIndex + 1, j + 1, grayExt))
					else:
						curRune["select"][i].SetInnerVisual(BASE_PATH + "rune%d/rune_%d%s.tga" % (groupIndex + 1, j + 1, grayExt))

					if hasRune:
						curRune["select"][ i ].addButton.Hide( )

						if constInfo.ENABLE_LEVEL2_RUNES:
							if not self.__HasRune(runeID + 100) and rune.GetProto(runeID)[1] != rune.SUBGROUP_PRIMARY:
								groupRunes.append(curRune["select"][i])
					else:
						curRune["select"][ i ].addButton.SetTop( )
						curRune["select"][ i ].addButton.Show( )

					j += 1

		if constInfo.ENABLE_LEVEL2_RUNES:
			if self.__HasAllRunes():
				for grR in groupRunes:
					grR.addButton.SetTop()
					grR.addButton.Show()

	if constInfo.ENABLE_LEVEL2_RUNES:
		def __HasAllGroupRunes(self, groupIdx):
			hasAllRunes = True
			for x in xrange(12):
				runeID = self.__GetRuneID(groupIdx, x)
				if not self.__HasRune(runeID):
					hasAllRunes = False
					break
			return hasAllRunes

		def __HasAllRunes(self):
			hasAllRunes = True
			for x in xrange(60):
				if not self.__HasRune(x + 1):
					hasAllRunes = False
					break
			return hasAllRunes

	def __Load(self):
	
		dummy = rune.PageGetType( True )

		self.main["background"].LoadImage( BASE_PATH + "rune1/sub_bg.tga" )
		self.__SetGroupIndex("main", rune.PageGetType( True ) )

#	def DEBUG_RefreshDiffuse(self):
#		circles = ["group_btn", "rune_main_btn", "rune_0_btn", "rune_1_btn", "rune_2_btn"]
#		color = self.DEBUG_CurDiffuse
#		tchat("COLOR[%3d, %3d, %3d]" % (color[0], color[1], color[2]))
#		for objName in circles:
#			self.main[objName].SetDiffuseColor(color[0] / 255.0, color[1] / 255.0, color[2] / 255.0, color[3] / 255.0)
#
#	def OnKeyDown(self, key):
#		if app.IsPressed(app.DIK_LCONTROL):
#			change = 20
#		else:
#			change = 1
#
#		if key == 19:
#			self.DEBUG_CurIndex = 0
#		elif key == 34:
#			self.DEBUG_CurIndex = 1
#		elif key == 48:
#			self.DEBUG_CurIndex = 2
#		elif key == 27:
#			self.DEBUG_CurDiffuse[self.DEBUG_CurIndex] = min(255, self.DEBUG_CurDiffuse[self.DEBUG_CurIndex] + change)
#			self.DEBUG_RefreshDiffuse()
#		elif key == 53:
#			self.DEBUG_CurDiffuse[self.DEBUG_CurIndex] = max(0, self.DEBUG_CurDiffuse[self.DEBUG_CurIndex] - change)
#			self.DEBUG_RefreshDiffuse()

	def Refresh(self):
		self.needRefresh = True

	def __Refresh(self):
		## set selection visibilities
		for i in xrange(self.RUNE_COUNT["main"]):
			self.__Refresh_Rune("main", i)
		# refresh selection for main side
		self.__RefreshSelectionRunes("main")
		## selection visiblity for main rune
		self.__Refresh_Rune("main", self.MAIN_RUNE_COUNT)
		## selection visiblity for sub group select
		self.__Refresh_Rune("sub", self.SUB_RUNE_COUNT)
		## selection visiblity for sub rune select
		self.__Refresh_SubRune()
		## save / reset enable
		self.__CheckChanged()
		self.UpdatePoints()

	def __GetRuneIconPath(self, groupIndex, vnum):
		group, subGroup, subGroupIndex, name, applyType = rune.GetProto(vnum)
		subGroup = subGroup + 1

		#largeStr = ""
		#if subGroup == rune.SUBGROUP_MAX_NUM:
		#	subGroup = 0
		#	largeStr = "_large"

		if subGroup == rune.SUBGROUP_MAX_NUM:
			subGroup = 0
			return BASE_PATH + "rune%d/main_rune%d.tga" % (groupIndex + 1, 1 + subGroup * self.RUNE_COUNT_PER_GROUP + subGroupIndex)

		if constInfo.ENABLE_LEVEL2_RUNES:
			if self.__HasRune(vnum + 100):
				return BASE_PATH + "lv2/rune%d/rune_%d.tga" % (groupIndex + 1, 1 + subGroup * self.RUNE_COUNT_PER_GROUP + subGroupIndex)
			else:
				return BASE_PATH + "rune%d/rune_%d.tga" % (groupIndex + 1, 1 + subGroup * self.RUNE_COUNT_PER_GROUP + subGroupIndex)
		else:
			return BASE_PATH + "rune%d/rune_%d.tga" % (groupIndex + 1, 1 + subGroup * self.RUNE_COUNT_PER_GROUP + subGroupIndex)

	def __Refresh_Rune(self, groupName, index):

		if groupName == "main":
			if index < self.RUNE_COUNT[groupName]:
				runeDict = self.main["%s_rune_%d" % (groupName, index)]
			else:
				runeDict = self.main["%s_rune_main" % groupName]
		elif groupName == "sub":
			if index < self.RUNE_COUNT[groupName]:
				pass
			else:
				runeDict = self.main["sub_group"]

		# get data
		defaultNameList = ["name", "noname", "desc"]
		selectName = "select_wnd"

		isRune = groupName != "sub" or index < self.RUNE_COUNT[groupName]

		# load rune inner image
		if isRune:
			vnum = self.__GetSelectedRune(groupName, index)

			if vnum == 0:
				runeDict["btn"].ClearInnerVisual()
			else:
				innerVisualPath = self.__GetRuneIconPath(rune.PageGetType(True), vnum)
				runeDict["btn"].SetInnerVisual( innerVisualPath )
		else:
			if rune.PageGetSubType(True) < 0:
				runeDict["btn"].ClearInnerVisual()
				for i in xrange(self.SUB_RUNE_COUNT):
					self.main["sub_rune_%d" % i]["btn"].Disable()
			else:
				runeDict["btn"].SetInnerVisual(BASE_PATH + "rune%d/sub_circle_inner.tga" % (rune.PageGetSubType(True) + 1))
				for i in xrange(self.SUB_RUNE_COUNT):
					self.main["sub_rune_%d" % i]["btn"].Enable()

		# check for selection open / closed -> update & show objects
		if self.__IsSelectionOpen(groupName, index):
			for objName in defaultNameList:
				runeDict[objName].Hide()

				if index == 3:
					runeDict[ "desc2" ].Hide( )

			runeDict[selectName].Show()

		else:
			for objName in defaultNameList:
				runeDict[objName].Show()

				if index == 3:
					runeDict[ "desc2" ].Hide( )

			runeDict[selectName].Hide()

			if (isRune and vnum == 0) or ((not isRune) and rune.PageGetSubType(True) < 0):
				runeDict["noname"].Show()
				runeDict["name"].SetText("")
				runeDict["desc"].SetText("")
				
				if index == 3:
					runeDict[ "desc2" ].SetText( "" )

			else:

				runeDict["noname"].Hide()

				if isRune:
					runeDict["name"].SetText( self.GetRuneName( vnum ) )
					runeDict["desc"].SetWidth(222)
					runeDict["desc"].SetLineHeight(11)


					if index == 3:
						runeDict["desc"].SetText( rune.GetProtoDesc( vnum ) )

					# Leadership and mount paralyze, they are not main runes but they contain special bonuses...
					elif vnum in self.normalRunesWithDesc:
						runeDict["desc"].SetText( rune.GetProtoDesc( vnum ) )

					else:
						runeDict["desc"].SetText( self.GetAffectStringByRuneVnum( vnum ) )

				else:
					runeDict["name"].SetPackedFontColor(self.GROUP_TITLE_COLORS[rune.PageGetSubType(True)])
					runeDict["name"].SetText(self.GROUP_LOCALE[rune.PageGetSubType(True)]["name"])
					runeDict["desc"].SetText(self.GROUP_LOCALE[rune.PageGetSubType(True)]["desc"])

	def __Refresh_SubRune(self):
		for i in xrange(self.SUB_RUNE_COUNT):
			btn = self.main["sub_rune_%d" % i]["btn"]
			vnum = self.__GetSelectedRune("sub", i)
			if vnum == 0:
				btn.ClearInnerVisual()
			else:
				btn.SetInnerVisual(self.__GetRuneIconPath(rune.PageGetSubType(True), vnum))

		# load circle colors
		if rune.PageGetSubType(True) >= 0:
			circleColor = self.CIRCLE_DIFFUSE_COLOR[rune.PageGetSubType(True)]
		else:
			circleColor = self.CIRCLE_DIFFUSE_DEFAULT_COLOR

		self.__SetObjectColor(self.main["sub_group"]["btn"], circleColor)
		self.__SetObjectColor(self.main["sub_group"]["below"], circleColor)
		for i in xrange(self.SUB_RUNE_COUNT):
			self.__SetObjectColor(self.main["sub_rune_%d" % i]["btn"], circleColor)
		for groupIdx in xrange(self.MAIN_RUNE_COUNT):
			for i in xrange(self.RUNE_COUNT_PER_GROUP):
				listIdx = groupIdx * self.RUNE_COUNT_PER_GROUP + i
				obj = self.main["sub_select"]["select"][listIdx]
				self.__SetObjectColor(obj, circleColor)

		# set visiblities
		defaultNameList = ["name", "noname", "nogroup", "desc"]
		isOpen = self.__IsSelectionOpen("sub", 0)

		for i in xrange(self.SUB_RUNE_COUNT):
			for objName in defaultNameList:
				self.main["sub_rune_%d" % i][objName].SetVisible(not isOpen)
		self.main["sub_select"]["wnd"].SetVisible(isOpen)

		if isOpen:
			if constInfo.ENABLE_LEVEL2_RUNES:
				groupRunes = []

			for groupIdx in xrange(self.MAIN_RUNE_COUNT):
				for i in xrange(self.RUNE_COUNT_PER_GROUP):
					listIdx = groupIdx * self.RUNE_COUNT_PER_GROUP + i

					runeID = self.__GetRuneID(rune.PageGetSubType(True), listIdx + self.RUNE_COUNT_PER_GROUP)
					hasRune = self.__HasRune(runeID)

					#tchat("HasSubRune[ id: %s ] = %s" % ( str( listIdx + self.RUNE_COUNT_PER_GROUP ), str( hasRune ) ) )

					grayExt = ""
					if not hasRune:
						grayExt = "_g"

					obj = self.main["sub_select"]["select"][listIdx]
					obj.SetEnabled(hasRune)
					if constInfo.ENABLE_LEVEL2_RUNES:
						if self.__HasRune(runeID + 100):
							obj.SetInnerVisual(BASE_PATH + "lv2/rune%d/rune_%d%s.tga" % (rune.PageGetSubType(True) + 1, listIdx + self.RUNE_COUNT_PER_GROUP + 1, grayExt))
						else:
							obj.SetInnerVisual(BASE_PATH + "rune%d/rune_%d%s.tga" % (rune.PageGetSubType(True) + 1, listIdx + self.RUNE_COUNT_PER_GROUP + 1, grayExt))
					else:
						obj.SetInnerVisual(BASE_PATH + "rune%d/rune_%d%s.tga" % (rune.PageGetSubType(True) + 1, listIdx + self.RUNE_COUNT_PER_GROUP + 1, grayExt))

					if hasRune:
						obj.addButton.Hide( )

						if constInfo.ENABLE_LEVEL2_RUNES:
							if not self.__HasRune(runeID + 100):
								groupRunes.append(obj)
					else:
						obj.addButton.SetTop( )
						obj.addButton.Show( )

			if constInfo.ENABLE_LEVEL2_RUNES:
				if self.__HasAllRunes():
					for grR in groupRunes:
						grR.addButton.SetTop()
						grR.addButton.Show()
		else:
			for i in xrange(self.SUB_RUNE_COUNT):
				obj = self.main["sub_rune_%d" % i]

				obj["desc"].SetWidth(222)
				obj["desc"].SetLineHeight(11)
				vnum = self.__GetSelectedRune("sub", i)
				if rune.PageGetSubType(True) < 0:
					obj["name"].Hide()
					obj["noname"].Hide()
					obj["desc"].SetText(localeInfo.SUB_RUNE_NOGROUP_DESC)
				else:
					obj["nogroup"].Hide()
					if vnum == 0:
						obj["name"].Hide()
						obj["desc"].Hide()
						obj["noname"].SetPackedFontColor(self.GROUP_TITLE_COLORS[rune.PageGetSubType(True)])
					else:
						obj["noname"].Hide()
						obj["name"].SetPackedFontColor(self.GROUP_TITLE_COLORS[rune.PageGetSubType(True)])
						obj["name"].SetText( self.GetRuneName( vnum ) )

						# Leadership and mount paralyze, they are not main runes but they contain special bonuses...
						if vnum in self.normalRunesWithDesc:
							obj["desc"].SetText( rune.GetProtoDesc( vnum ) )
						else:
							obj["desc"].SetText( self.GetAffectStringByRuneVnum( vnum ) )

	def BackToMainWindow(self):
		self.Close()
		wnd = self.openMainWndFunc()
		if wnd:
			wnd.SetPosition(self.GetLeft(), self.GetTop())

	def Open(self, groupIndex):

		rune.PageSetType(groupIndex)
		if groupIndex == rune.PageGetType(False):
			rune.PageResetNew()
		self.__Initialize()
		if groupIndex == rune.PageGetType(False):
			self.selectStates["main"][self.MAIN_RUNE_COUNT] = False

		self.__Load()
		self.Refresh()
		self.OnUpdate()

		ui.BaseScriptWindow.Open(self)

		if constInfo.RUNE_TUTORIAL_ENABLED:

			runeTutorial = cfg.Get( cfg.SAVE_OPTION, "rune_tut" )

			if not runeTutorial:
				self.OpenTutorialWindow( )
				cfg.Set( cfg.SAVE_OPTION, "rune_tut", True )

		if constInfo.ENABLE_RUNE_PAGES:
			# if not net.IsPrivateMap() and constInfo.RUNE_CHANGE_PULSE + 5 > app.GetTime():
			# 	chat.AppendChat(chat.CHAT_TYPE_INFO, localeInfo.RUNE_PAGE_CANNOT_SAVE_YET)
			# 	return

			# constInfo.RUNE_CHANGE_PULSE = app.GetTime()

			if self.firstTime:
				self.firstTime = False
				net.SendChatPacket("/get_selected_page %d %d %d %d %d %d %d %d" % (rune.PageGetType(True), rune.PageGetVnum(0), rune.PageGetVnum(1), rune.PageGetVnum(2), rune.PageGetVnum(3), rune.PageGetSubType(True), rune.PageGetSubVnum(0), rune.PageGetSubVnum(1)))

			net.SendChatPacket("/get_rune_page %d" % self.currentPage)

	## selector functions
	def __OpenSelection(self, groupName, index):
		self.selectStates[groupName][index] = True
		self.Refresh()

	def __CloseSelection(self, groupName, index):
		self.selectStates[groupName][index] = False
		self.Refresh()

	def __IsSelectionOpen(self, groupName, index):
		return self.selectStates[groupName][index]

	def __ToggleSelection(self, groupName, index):

		pageType = rune.PageGetType( True )

		# Should never happen so no translation needed
		if pageType == -1:
			self.popupDlg.SetText( "You need to select rune group first!" )
			self.popupDlg.Open( )
			return

		realIdx = index
		if index != 0 and index != self.SUB_RUNE_COUNT and groupName == "sub":
			realIdx = 0

		isOpen = self.__IsSelectionOpen(groupName, realIdx)
		if isOpen:
			self.__CloseSelection(groupName, realIdx)
		else:
			self.__OpenSelection(groupName, realIdx)

		if groupName == "sub":
			if isOpen:
				for i in xrange(1, self.SUB_RUNE_COUNT):
					self.__CloseSelection(groupName, i)
			elif index != realIdx:
				self.__OpenSelection(groupName, index)

	def __GetSelectedRune(self, groupName, index):
		if groupName == "main":
			return rune.PageGetVnum(index, True)
		else:
			return rune.PageGetSubVnum(index, True)

	def __SetSelectedRune(self, groupName, index, vnum):

		tchat( "Group: " + str( groupName ) )
		tchat( "Index: " + str( index ) )
		tchat( "Vnum: " + str( vnum ) )

		if groupName == "main":
			rune.PageSetVnum(index, vnum)
		else:
			rune.PageSetSubVnum(index, vnum)
		self.__CheckChanged()
		self.Refresh()

		if constInfo.ENABLE_RUNE_PAGES:
			if self.currentPage == -1 or vnum == 0:
				return
			if groupName == "main":
				net.SendChatPacket("/select_rune %d %d %d %d %d" % (rune.PageGetType(True), self.currentPage, 0, index, vnum))
			else:
				net.SendChatPacket("/select_rune %d %d %d %d %d" % (rune.PageGetType(True), self.currentPage, 3, index, rune.PageGetSubType(True)))
				net.SendChatPacket("/select_rune %d %d %d %d %d" % (rune.PageGetType(True), self.currentPage, 1, index, vnum))

	## ui funcs
	def __SelectRune(self, groupName, index, sub_index):

		groupIndex = rune.PageGetType(True)
		if groupName == "sub":
			groupIndex = rune.PageGetSubType(True)

		runeID = rune.GetIDByIndex(groupIndex, index, sub_index)
		if runeID == 0:
			import dbg
			dbg.TraceError("cannot select rune [%d, %d, %d] => runeID == 0" % (groupIndex, index, sub_index))
			return

		#tchat("groupName[%s] groupIndex[%d] index[%d] sub_index[%d] runeID[%d]" % (groupName, groupIndex, index, sub_index, runeID))

		if groupName == "sub":
			index = 0
			for i in xrange(1, self.SUB_RUNE_COUNT):
				if self.__IsSelectionOpen("sub", i):
					index = i
					break
			if index != 0:
				self.__CloseSelection(groupName, 0)

		self.__SetSelectedRune(groupName, index, runeID)
		self.__CloseSelection(groupName, index)

	def __SelectSubGroup(self, index):
		if index >= rune.PageGetType(True):
			index = index + 1

		rune.PageSetSubType(index)
		for i in xrange(self.SUB_RUNE_COUNT):
			self.__SetSelectedRune("sub", i, 0)
		self.__CloseSelection("sub", self.SUB_RUNE_COUNT)
		self.__CheckChanged()

		if constInfo.ENABLE_RUNE_PAGES:
			if self.currentPage == -1:
				return
			net.SendChatPacket("/select_rune %d %d %d %d %d" % (rune.PageGetType(True), self.currentPage, 2, index, index))

	def __CheckChanged(self):
		isChanged = rune.PageIsNewChanged()
		self.main["btn_save"].SetEnabled(isChanged)
		self.main["btn_reset"].SetEnabled(isChanged)

	def __Save(self):
		if constInfo.ENABLE_RUNE_PAGES:
			# if not net.IsPrivateMap() and constInfo.RUNE_CHANGE_PULSE + 5 > app.GetTime():
			# 	chat.AppendChat(chat.CHAT_TYPE_INFO, localeInfo.RUNE_PAGE_CANNOT_SAVE_YET)
			# 	return

			# constInfo.RUNE_CHANGE_PULSE = app.GetTime()
			rune.PageSaveNew()

	def __Reset( self ):
		if constInfo.ENABLE_RUNE_PAGES:
			net.SendChatPacket("/reset_rune_page %d" % self.currentPage)
			net.SendChatPacket("/get_rune_page %d" % self.currentPage)
		else:
			self.Open( rune.PageGetType( False ) )
