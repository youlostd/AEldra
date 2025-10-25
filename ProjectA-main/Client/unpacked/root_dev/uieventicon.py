import ui
import localeInfo
import constInfo
import wndMgr
import snd
import interfaceModule
from os import system
import uiScriptLocale
import net

class EventDescriptionWindow(ui.BoardWithTitleBar):
	BOARD_WIDTH 	= 300
	BOARD_HEIGHT 	= 300

	## Next time when creating a new number for an event, search in FR folder for pattern "event_" and sort the results by name to see what numbers are used already
	EVENT_NAMES = {
		1 : "EMPIREWAR",
		2 : "HEXA",
		3 : "PVP",
		4 : "MOONLIGHT",
		5 : "BOSSHUNT",
		6 : "DROP",
		7 : "XP",
		8 : "YANG",
		10 : "ANGELSDEMONS",
		11 : "XMASCALENDAR",
		14 : "BLACKJACK",
		19 : "SUNDAE",
		20 : "HALLOWEEN",
	}

	def __init__(self):
		self.eventId = 0
		ui.BoardWithTitleBar.__init__(self)
		self.__LoadGUI()

	def __del__(self):
		ui.BoardWithTitleBar.__del__(self)

	def GetLocaleText(self, eventId):
		if "EVENT_DESC_{}".format(self.EVENT_NAMES[ eventId ]) not in localeInfo.GetLocals():
			return ""
		return localeInfo.GetLocals()[ "EVENT_DESC_{}".format(self.EVENT_NAMES[ eventId ]) ]

	def __LoadGUI(self):

		self.SetSize(self.BOARD_WIDTH, self.BOARD_HEIGHT)
		self.SetCenterPosition()

		self.AddFlag("float")
		self.AddFlag("movable")

		self.SetTitleName(localeInfo.EVENT_DESCRIPTION_WINDOW_TITLE)

		self.eventIconWnd = ui.Window()
		self.eventIconWnd.SetParent(self)
		self.eventIconWnd.SetPosition(0, 10)
		self.eventIconWnd.SetSize(100, 70)
		self.eventIconWnd.SetWindowHorizontalAlignCenter()
		self.eventIconWnd.SetWindowVerticalAlignTop()
		self.eventIconWnd.Show()

		self.eventIcon = ui.ImageBox()
		self.eventIcon.SetParent(self.eventIconWnd)
		self.eventIcon.SetPosition(0, 0)
		self.eventIcon.LoadImage("d:/ymir work/ui/game/event_icons/event_1.tga")
		self.eventIcon.SetWindowHorizontalAlignCenter()
		self.eventIcon.SetWindowVerticalAlignCenter()
		self.eventIcon.Show()

		self.eventDesc = ui.MultiTextLine()
		self.eventDesc.SetParent(self)
		self.eventDesc.SetPosition(0, 90)
		self.eventDesc.SetTextHorizontalAlignCenter()
		self.eventDesc.SetTextVerticalAlignCenter()
		self.eventDesc.SetWindowHorizontalAlignCenter()
		self.eventDesc.SetWidth(200)
		self.eventDesc.Show()

	def EventSpecificUI(self):
		if self.eventId == 14:
			self.eventDesc.Hide()
			self.SetSize(self.BOARD_WIDTH / 2, self.BOARD_HEIGHT / 2)

			self.btnTeleport = ui.Button()
			self.btnTeleport.SetParent(self)
			self.btnTeleport.SetUpVisual("d:/ymir work/ui/public/Large_Button_01.sub")
			self.btnTeleport.SetOverVisual("d:/ymir work/ui/public/Large_Button_02.sub")
			self.btnTeleport.SetDownVisual("d:/ymir work/ui/public/Large_Button_03.sub")
			self.btnTeleport.SetEvent(ui.__mem_func__(self.Warp))	
			self.btnTeleport.SetText(uiScriptLocale.EVENT_JOIN_ACCEPT_BUTTON)
			self.btnTeleport.SetWindowHorizontalAlignCenter()
			self.btnTeleport.SetWindowVerticalAlignBottom()
			self.btnTeleport.SetPosition(0, 65)
			self.btnTeleport.Show()

			self.btnForum = ui.Button()
			self.btnForum.SetParent(self)
			self.btnForum.SetUpVisual("d:/ymir work/ui/public/Large_Button_01.sub")
			self.btnForum.SetOverVisual("d:/ymir work/ui/public/Large_Button_02.sub")
			self.btnForum.SetDownVisual("d:/ymir work/ui/public/Large_Button_03.sub")
			self.btnForum.SetEvent(ui.__mem_func__(self.OpenForum))	
			self.btnForum.SetText("Forum")
			self.btnForum.SetWindowHorizontalAlignCenter()
			self.btnForum.SetWindowVerticalAlignBottom()
			self.btnForum.SetPosition(0, 35)
			self.btnForum.Show()

			self.SetCenterPosition()

		if self.eventId == 19:
			self.SetSize(self.BOARD_WIDTH / 2, self.BOARD_HEIGHT / 2)

			self.btnForum = ui.Button()
			self.btnForum.SetParent(self)
			self.btnForum.SetUpVisual("d:/ymir work/ui/public/Large_Button_01.sub")
			self.btnForum.SetOverVisual("d:/ymir work/ui/public/Large_Button_02.sub")
			self.btnForum.SetDownVisual("d:/ymir work/ui/public/Large_Button_03.sub")
			self.btnForum.SetEvent(ui.__mem_func__(self.OpenForum))	
			self.btnForum.SetText("Forum")
			self.btnForum.SetWindowHorizontalAlignCenter()
			self.btnForum.SetWindowVerticalAlignBottom()
			self.btnForum.SetPosition(0, 35)
			self.btnForum.Show()

			self.SetCenterPosition()

	def OpenForum(self):
		if self.eventId == 14:
			system("start %s" % "https://%s/l/blackjack" % constInfo.DOMAIN)
		if self.eventId == 19:
			system("start %s" % "https://%s/l/sundea" % constInfo.DOMAIN)

	def Warp(self):
		if self.eventId == 14:
			net.SendChatPacket('/user_warp blackjack')

	def ChangeEventText(self, eventId):
		localeText = self.GetLocaleText(eventId)
		self.eventDesc.SetText(localeText)

	def ChangeEventImage(self, eventId):
		self.eventIcon.LoadImage("d:/ymir work/ui/game/event_icons/event_{}.tga".format(eventId))

	def Open(self, eventId):
		self.eventId = eventId
		self.ChangeEventImage(eventId)
		self.ChangeEventText(eventId)
		self.EventSpecificUI()
		self.Show()

	def Close(self):
		self.Hide()

	def OnPressEscapeKey(self):
		self.Close()
		return True

	def OnUpdate(self):
		pass

class EventIconShower(ui.Window):

	BOARD_WIDTH 	= 100
	BOARD_HEIGHT 	= 100

	def __init__(self):

		ui.Window.__init__(self)

		self.wndEventDescription = None
		self.eventId = None

		self.__LoadWindow()

	def __del__(self):
		ui.Window.__del__(self)

	def __LoadWindow(self):
		if constInfo.NEW_MINIMAP_UI:
			boardX, boardY = (wndMgr.GetScreenWidth() - 236 - 30, 15 + 30)
		else:
			boardX, boardY = (wndMgr.GetScreenWidth() - 236, 15 + 30)

		self.SetSize(self.BOARD_WIDTH, self.BOARD_HEIGHT)
		self.SetPosition(boardX, boardY)

		self.eventIcon = ui.ImageBox()
		self.eventIcon.SetParent(self)
		self.eventIcon.SetPosition(0, 0)
		self.eventIcon.LoadImage("d:/ymir work/ui/game/event_icons/event_1.tga")
		
		# Align image
		self.eventIcon.SetWindowHorizontalAlignCenter()
		self.eventIcon.SetWindowVerticalAlignTop()

		self.eventIcon.SAFE_SetStringEvent("MOUSE_LEFT_DOWN", self.OpenEventDescription)

		# Show images
		self.eventIcon.Show()

	def ChangeEventImage(self, eventId):
		self.eventIcon.LoadImage("d:/ymir work/ui/game/event_icons/event_{}.tga".format(eventId))

	def OpenEventDescription(self):
		if constInfo.ENABLE_XMAS_EVENT:
			if self.eventId == 11:
				self.interface.OpenXmasEventWindow()
				return
		if constInfo.ENABLE_WHEEL_OF_FRIGHT:
			if self.eventId == 20:
				self.interface.OpenWheelOfFright()
				return
				
		if constInfo.ENABLE_ANGELSDEMONS_EVENT and self.eventId == 10:
			self.interface.ToogleFractionWarWindow()
			return

		if self.eventId == 18:
			system("start %s" % "https://%s/l/easter" % constInfo.DOMAIN)
			return
			
		if self.eventId == 13:
			system("start %s" % "https://%s/l/football" % constInfo.DOMAIN)
			return

		# if self.eventId == 14:
		# 	system("start %s" % "https://%s/l/blackjack" % constInfo.DOMAIN)

		if not self.wndEventDescription:
			self.wndEventDescription = EventDescriptionWindow()

		snd.PlaySound("sound/ui/click.wav")
		self.wndEventDescription.Open(self.eventId)

	def Open(self, eventId):
		if constInfo.ENABLE_XMAS_EVENT:
			if eventId == 11:
				self.SetPosition(wndMgr.GetScreenWidth() - 110, 180)

		self.eventId = eventId

		self.ChangeEventImage(eventId)
		self.Show()

	def Close(self):
		if self.wndEventDescription:
			self.wndEventDescription.Close()

		self.Hide()

	def BindInterface(self, interface):
		self.interface = interface
