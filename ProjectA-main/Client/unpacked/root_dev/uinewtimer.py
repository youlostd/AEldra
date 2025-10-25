import ui
import localeInfo
import uiScriptLocale
import app
import item
import net
import player
import uiCommon
import event
import constInfo
import snd
import chat

# need to set position before .Open()
class NotificationWindow(ui.Window):
	WIDTH = 122
	HEIGHT = 46

	def __init__(self, title, index):
		ui.Window.__init__(self)

		self.title 		= title
		self.index 		= index
		self.openTime 	= 0

		self.LoadWindowAndGUI()

	def __del__(self):
		ui.Window.__del__(self)

	def PlayOpenSound(self):
		if not constInfo.NEW_QUEST_TIMER_LAST_SOUND:
			constInfo.NEW_QUEST_TIMER_LAST_SOUND = app.GetTime()
			snd.PlaySound("sound/ui/quest_receive.wav")

		if app.GetTime() > constInfo.NEW_QUEST_TIMER_LAST_SOUND + 5.0:
			snd.PlaySound("sound/ui/quest_receive.wav")
			constInfo.NEW_QUEST_TIMER_LAST_SOUND = app.GetTime()

	def LoadWindowAndGUI(self):
		self.SetSize(self.WIDTH, self.HEIGHT)

		index = int(self.index) + 1

		# main background
		self.backgroundImage = ui.ImageBox()
		self.backgroundImage.SetParent(self)
		self.backgroundImage.SetPosition(0, 0)
		self.backgroundImage.LoadImage("d:/ymir work/ui/game/questtimer/notifications/%s.tga" % str(index))
		self.backgroundImage.Show()

		self.questTitle = ui.TextLine()
		self.questTitle.SetParent(self.backgroundImage)
		self.questTitle.SetPosition(51, 10)
		self.questTitle.SetHorizontalAlignLeft()
		self.questTitle.SetText(self.title)
		self.questTitle.Show()

		self.isAvailableText = ui.TextLine()
		self.isAvailableText.SetParent(self.backgroundImage)
		self.isAvailableText.SetPosition(51, 22)
		self.isAvailableText.SetHorizontalAlignLeft()
		self.isAvailableText.SetText(localeInfo.QUEST_TIMER_AVAILABLE_TEXT)
		self.isAvailableText.Show()

	def CanOpen(self):
		return bool(self.openTime == 0)

	def Open(self):
		if not self.CanOpen():
			return

		if constInfo.NEW_QUEST_TIMER_PLAY_SOUND:
			self.PlayOpenSound()

		self.openTime = app.GetGlobalTime()
		self.Show()

	def Reset(self):
		self.openTime = 0
		self.Close()

	def Close(self):
		self.Hide()

	def OnUpdate(self):
		closeAfterMs = 4000
		timeDiff = app.GetGlobalTime() - self.openTime

		# simple alpha anim (1000)
		if timeDiff >= closeAfterMs - 1000:

			diff = timeDiff - closeAfterMs
			floatDiff = float((float(diff) / 1000.0) * -1)

			# parse
			if floatDiff > 1.0:
				floatDiff = 1.0

			if floatDiff < 0.0:
				floatDiff = 0.0

			self.SetAllAlpha(floatDiff)

		if timeDiff >= closeAfterMs:
			self.Close()

	def Destroy(self):
		self.backgroundImage = None
		self.questTitle = None
		self.isAvailableText = None

class TimerWindow(ui.Window):
	WIDTH 	= 611
	HEIGHT 	= 612

	PATH_BASE 			= "d:/ymir work/ui/game/questtimer/"
	PATH_ICONS 			= PATH_BASE + "icons/"
	PATH_BANNERS 		= PATH_BASE + "banners/"
	PATH_SCROLLBAR 		= PATH_BASE + "scrollbar/"
	PATH_NOTIFICATIONS 	= PATH_BASE + "notifications/"

	# NAME -> MIN. LEVEL -> GROUP REQ. -> COOLDOWN -> ITEM VNUM -> MAX.
	# BIOLOG QUEST WILL GET OVERWRITTEN

	QUESTS = [
		[localeInfo.QUEST_TIMER_BIOLOG, 		"biolog.txt", 		"None", False, 	"0:00", 0, "None"],
		[localeInfo.QUEST_TIMER_ORKMAZE, 		"orkmaze.txt", 		"55",	False, 	"1 " + localeInfo.HOUR + " 30 " + localeInfo.MINUTE, 94031, "85"],
		[localeInfo.QUEST_TIMER_SPIDER, 		"spider.txt", 		"50",	False, 	"1 " + localeInfo.HOUR, 30324, "85"],
		[localeInfo.QUEST_TIMER_AZRAEL, 		"azrael.txt", 		"75",	False, 	"1 " + localeInfo.HOUR, 76002, "105"],
		[localeInfo.QUEST_TIMER_DRAGON, 		"dragon.txt", 		"75",	False, 	"2 " + localeInfo.HOUR, 30179, "105"],
		[localeInfo.QUEST_TIMER_SNOW, 			"snow.txt", 		"95",	False, 	"1 " + localeInfo.HOUR + " 30 " + localeInfo.MINUTE, 92881, "109"],
		[localeInfo.QUEST_TIMER_FLAME, 			"flame.txt", 		"95",	False, 	"1 " + localeInfo.HOUR + " 30 " + localeInfo.MINUTE, 92882, "109"],
		[localeInfo.QUEST_TIMER_SHIPDEFENSE, 	"shipdefense.txt", 	"105",	True, 	"3 " + localeInfo.HOUR, 31005, "115"],
		[localeInfo.QUEST_TIMER_JOTUN, 			"jotun.txt", 		"105",	False, 	"3 " + localeInfo.HOUR, 30613, "115"],
		[localeInfo.QUEST_TIMER_CRYSTALL, 		"crystall.txt", 	"110",	False, 	"3 " + localeInfo.HOUR, 31006, "115"],
		[localeInfo.QUEST_TIMER_MELEY, 			"meley.txt", 		"75",	False, 	"3 " + localeInfo.HOUR, 0, "115"],
		[localeInfo.QUEST_TIMER_THRANDUILS,		"thranduil.txt", 	"110",	False,	"3 " + localeInfo.HOUR, 93264, "115"],
		[localeInfo.QUEST_TIMER_ZODIAC,			"zodiac.txt",	 	"90",	False,	"0 " + localeInfo.HOUR, 0, 	"115"],
		[localeInfo.QUEST_TIMER_SLIME, "slime.txt",	"75", False,	"90" + localeInfo.MINUTE, 76002, "95"],
		[localeInfo.QUEST_TIMER_INFECTED, "garden.txt",	"110", False,	"3" + localeInfo.HOUR, 93264, "115"],
	]

	BIOLOG = [
		[0, "-"],
		[30006, "0:00 "],
		[30047, "0:00 "],
		[30015, "0:00 "],
		[30050, "0:00 "],
		[30165, "30 " + localeInfo.MINUTE],
		[30166, "30 " + localeInfo.MINUTE],
		[30167, "45 " + localeInfo.MINUTE],
		[30168, "1 " + localeInfo.HOUR],
		[30251, "2 " + localeInfo.HOUR],
		[30252, "2 " + localeInfo.HOUR],
		[93038, "2 " + localeInfo.HOUR], # lvl 108
		[93040, "2 " + localeInfo.HOUR], # lvl 112
	]

	if constInfo.SERVER == 2:
		QUESTS = [
			[localeInfo.QUEST_TIMER_BIOLOG, 		"biolog.txt", 		"None", False, 	"0:00", 0, "None"],
			[localeInfo.QUEST_TIMER_APE, 			"ape.txt", 			"35",	False, 	"1 " + localeInfo.HOUR, 31064, "60"],
			[localeInfo.QUEST_TIMER_DEMON, 			"demontower.txt", 	"40",	False, 	"0:00 ", 0, "105"],
			[localeInfo.QUEST_TIMER_SPIDER, 		"spider.txt", 		"60",	False, 	"1 " + localeInfo.HOUR, 30324, "85"],
			[localeInfo.QUEST_TIMER_AZRAEL, 		"azrael.txt", 		"75",	False, 	"1 " + localeInfo.HOUR, 76002, "105"],
			[localeInfo.QUEST_TIMER_DRAGON, 		"dragon.txt", 		"75",	False, 	"2 " + localeInfo.HOUR, 30179, "105"],
			[localeInfo.QUEST_TIMER_SNOW, 			"snow.txt", 		"100",	False, 	"3 " + localeInfo.HOUR, 71130, "105"],
			[localeInfo.QUEST_TIMER_FLAME, 			"flame.txt", 		"100",	False, 	"3 " + localeInfo.HOUR, 71130, "105"],
		]
		BIOLOG = [
			[0, "-"],
			[30006, "0:00 "],
			[30047, "0:00 "],
			[30015, "0:00 "],
			[30050, "0:00 "],
			[30165, "30 " + localeInfo.MINUTE],
			[30166, "45 " + localeInfo.MINUTE],
			[30167, "4 " + localeInfo.HOUR],
			[30168, "4 " + localeInfo.HOUR],
			[30251, "8 " + localeInfo.HOUR],
			[30252, "8 " + localeInfo.HOUR],
		]

	COOLDOWNS 					= len(QUESTS) * [0]
	NOTIFICATION_ENABLED 		= len(QUESTS) * [0]

	BIOLOG_ZERO_FIX = False

	class DescriptionWindow(ui.ScriptWindow):
		LINES_VIEW_COUNT = 17

		class DescriptionBox(ui.Window):
			def __init__(self):
				ui.Window.__init__(self)
				self.descriptionIndex = 0

			def __del__(self):
				ui.Window.__del__(self)

			def SetIndex(self, index):
				self.descriptionIndex = index

			def OnRender(self):
				event.RenderEventSet(self.descriptionIndex)

		def __init__(self, width, height):
			ui.ScriptWindow.__init__(self)

			self.descriptionIndex = 0
			self.scrollPos = 0

			self.descriptionFile = ""
			self.width = width
			self.height = height

			self.LoadDescriptionWindow()

		def __del__(self):
			ui.ScriptWindow.__del__(self)

		def LoadDescriptionWindow(self):
			self.SetSize(self.width, self.height)
			self.SetPosition(0, 0)

			scrollPath = "d:/ymir work/ui/game/questtimer/scrollbar/"

			self.scrollBar = ui.ScrollBarTemplate()
			self.scrollBar.SetParent(self)
			self.scrollBar.SetPosition(self.width - 5, 0)
			self.scrollBar.SetBarImage(scrollPath + "scrollbar_bg.tga")
			self.scrollBar.SetMiddleImage(scrollPath + "middle.tga")
			self.scrollBar.SetScrollBarSize(286)
			self.scrollBar.SetScrollEvent(self.OnScroll)
			self.scrollBar.Show()

			self.textBoard = ui.Bar()
			self.textBoard.SetParent(self)
			self.textBoard.SetPosition(4, 0)
			self.textBoard.SetSize(self.width - 12, self.height - 2)
			self.textBoard.Show()

		def Open(self):
			event.ClearEventSet(self.descriptionIndex)

			self.__SetDescriptionEvent()
			self.__CreateDescriptionBox()
			self.scrollBar.SetPos(0.0)

			self.Show()
			ui.ScriptWindow.Show(self)

		def OnScroll(self):
			self.scrollPos = int(self.scrollBar.GetPos() * max(0, event.GetLineCount(self.descriptionIndex) + 1 - self.LINES_VIEW_COUNT))
			event.SetVisibleStartLine(self.descriptionIndex, self.scrollPos)
			event.Skip(self.descriptionIndex)

		def OnMouseWheel(self, len):
			lineCount = event.GetTotalLineCount(self.descriptionIndex)

			if self.IsInPosition() and self.scrollBar.IsShow() and lineCount > 0:

				dir = constInfo.WHEEL_TO_SCROLL(len)

				newPos = self.scrollBar.GetPos() + ((1.0 / lineCount) * dir)
				newPos = max(0.0, newPos)
				newPos = min(1.0, newPos)

				self.scrollBar.SetPos(newPos)
				return True

			return False

		def Close(self):
			event.ClearEventSet(self.descriptionIndex)
			self.descriptionIndex = 0
			self.Hide()

		def __SetDescriptionEvent(self):
			event.ClearEventSet(self.descriptionIndex)
			self.descriptionIndex = event.RegisterEventSet("%s/questtimer%s/%s" % (app.GetLocalePath(), "" if constInfo.SERVER == 1 else "_s2", self.descriptionFile))
			event.SetEventSetWidth(self.descriptionIndex, self.textBoard.GetWidth() - 7 * 2)
			event.SetVisibleLineCount(self.descriptionIndex, self.LINES_VIEW_COUNT)

		def __CreateDescriptionBox(self):
			self.descriptionBox = self.DescriptionBox()
			self.descriptionBox.SetParent(self.textBoard)
			self.descriptionBox.Show()

		def OnUpdate(self):
			(xposEventSet, yposEventSet) = self.textBoard.GetGlobalPosition()
			event.UpdateEventSet(self.descriptionIndex, xposEventSet+7, -(yposEventSet+7-(self.scrollPos * 16)))
			self.descriptionBox.SetIndex(self.descriptionIndex)

			linesCount = event.GetTotalLineCount(self.descriptionIndex)

			if linesCount > 0 and linesCount > self.LINES_VIEW_COUNT:
				#self.scrollBar.SetMiddleBarSize(float(self.LINES_VIEW_COUNT) / float(linesCount))
				self.scrollBar.SetMiddleBarSize(0.35)
				self.scrollBar.Show()
			else:
				self.scrollBar.Hide()

		def ChangeDescription(self, fileName):
			self.Close()
			self.descriptionFile = fileName
			self.Open()

		def Destroy(self):
			self.ClearDictionary()
			self.scrollBar = None
			self.descriptionBox = None
			self.textBoard = None

	def __init__(self):	
		ui.Window.__init__(self)

		self.itemToolTip = None
		self.questIndex = None
		self.wndDescription = None
		self.itemVnum = None
		self.lastUpdateTime = 0
		self.initialized = False

		self.LoadWindowAndGUI()

	def __del__(self):
		ui.Window.__del__(self)

	def LoadWindowAndGUI(self):
		self.SetSize(self.WIDTH, self.HEIGHT)
		self.SetCenterPosition()
		self.AddFlag("float")
		self.AddFlag("movable")

		# main background
		self.backgroundImage = ui.ImageBox()
		self.backgroundImage.SetParent(self)
		self.backgroundImage.SetPosition(0, 0)
		if constInfo.QUEST_TIMER_SCROLLBAR:
			self.backgroundImage.LoadImage(self.PATH_BASE + "bg2.tga")
		else:
			self.backgroundImage.LoadImage(self.PATH_BASE + "bg.tga")
		self.backgroundImage.Show()

		# title bar
		self.titleBar = ui.TitleBar()
		self.titleBar.SetParent(self)
		self.titleBar.MakeTitleBar(0, "red")
		self.titleBar.SetPosition(6, 8)
		self.titleBar.SetWidth(self.WIDTH - 18)
		self.titleBar.btnClose.SetEvent(self.Close)
		self.titleBar.Show()

		# title bar name
		self.titleName = ui.TextLine()
		self.titleName.SetParent(self.titleBar)
		self.titleName.SetPosition(0, 3)
		self.titleName.SetWindowHorizontalAlignCenter()
		self.titleName.SetHorizontalAlignCenter()
		self.titleName.SetText(localeInfo.QUEST_TIMER_INFO)
		self.titleName.Show()

		# banner image
		self.bannerImage = ui.ImageBox()
		self.bannerImage.SetParent(self)
		self.bannerImage.SetPosition(334, 34)
		self.bannerImage.LoadImage(self.PATH_BANNERS + "1.tga")
		self.bannerImage.Show()

		# box used to center the text inside it
		self.dungeonNameBox = ui.Window()
		self.dungeonNameBox.SetParent(self)
		self.dungeonNameBox.SetPosition(341, 102)
		self.dungeonNameBox.SetSize(251, 28)
		self.dungeonNameBox.Show()

		# dungeon name text
		self.dungeonName = ui.TextLine()
		self.dungeonName.SetParent(self.dungeonNameBox)
		self.dungeonName.SetPosition(0, 7)
		self.dungeonName.SetWindowHorizontalAlignCenter()
		self.dungeonName.SetHorizontalAlignCenter()
		self.dungeonName.SetText("")
		self.dungeonName.Show()

		# box used to center the text inside it
		self.dungeonDescriptionTitleBox = ui.Window()
		self.dungeonDescriptionTitleBox.SetParent(self)
		self.dungeonDescriptionTitleBox.SetPosition(341, 244)
		self.dungeonDescriptionTitleBox.SetSize(251, 28)
		self.dungeonDescriptionTitleBox.Show()

		# dungeon name text
		self.dungeonDescriptionTitle = ui.TextLine()
		self.dungeonDescriptionTitle.SetParent(self.dungeonDescriptionTitleBox)
		self.dungeonDescriptionTitle.SetPosition(0, 7)
		self.dungeonDescriptionTitle.SetWindowHorizontalAlignCenter()
		self.dungeonDescriptionTitle.SetHorizontalAlignCenter()
		self.dungeonDescriptionTitle.SetText("")
		self.dungeonDescriptionTitle.Show()

		self.dungeonInfo = []

		baseX = 348
		baseY = 131 

		# create box/text with level requirement etc
		for i in range(0, 3):
			infoBox = ui.Window()
			infoBox.SetParent(self)
			infoBox.SetPosition(baseX, baseY + (i * 18))
			infoBox.SetSize(237, 18)
			infoBox.Show()

			infoTitle = ui.TextLine()
			infoTitle.SetParent(infoBox)
			infoTitle.SetPosition(8, 2)
			infoTitle.SetWindowHorizontalAlignLeft()
			infoTitle.SetHorizontalAlignLeft()
			infoTitle.Show()

			infoValue = ui.TextLine()
			infoValue.SetParent(infoBox)
			infoValue.SetPosition(8, 2)
			infoValue.SetWindowHorizontalAlignRight()
			infoValue.SetHorizontalAlignRight()
			infoValue.Show()

			self.dungeonInfo.append([infoBox, infoTitle, infoValue])

		self.dungeonInfo[0][1].SetText(localeInfo.QUEST_TIMER_MINLVL)
		self.dungeonInfo[1][1].SetText(localeInfo.QUEST_TIMER_GROUPREQ)
		self.dungeonInfo[2][1].SetText(localeInfo.QUEST_TIMER_COOLDOWN)

		# passage ticket box
		self.passageTicketBox = ui.Window()
		self.passageTicketBox.SetParent(self)
		self.passageTicketBox.SetPosition(347, 193)
		self.passageTicketBox.SetSize(239, 46)
		self.passageTicketBox.Show()

		# passage ticket text
		self.passageTicketText = ui.TextLine()
		self.passageTicketText.SetParent(self.passageTicketBox)
		self.passageTicketText.SetPosition(10, 15)
		self.passageTicketText.SetHorizontalAlignLeft()
		self.passageTicketText.SetText(localeInfo.QUEST_TIMER_PASSAGETICKET)
		self.passageTicketText.Show()

		# default test image
		item.SelectItem(1, 2, 30179)
		image = item.GetIconImageFileName()

		# passage ticket item
		self.passageTicketItem = ui.ExpandedImageBox()
		self.passageTicketItem.SetParent(self.passageTicketBox)
		self.passageTicketItem.SetWindowHorizontalAlignRight()
		self.passageTicketItem.SetPosition(42, 7)
		self.passageTicketItem.SAFE_SetStringEvent("MOUSE_OVER_IN", self.OnPassageTicketHover)
		self.passageTicketItem.SAFE_SetStringEvent("MOUSE_OVER_OUT", self.OnPassageTicketMouseOut)
		self.passageTicketItem.LoadImage(image)
		self.passageTicketItem.Show()

		self.passageTicketItemNone = ui.TextLine()
		self.passageTicketItemNone.SetParent(self.passageTicketBox)
		self.passageTicketItemNone.SetWindowHorizontalAlignRight()
		self.passageTicketItemNone.SetHorizontalAlignCenter()
		self.passageTicketItemNone.SetPosition(30, 15)
		self.passageTicketItemNone.SetText("")
		self.passageTicketItemNone.Show()

		# alarm image
		self.alarmImage = ui.ImageBox()
		self.alarmImage.SetParent(self)
		self.alarmImage.SetPosition(547, 569)
		self.alarmImage.LoadImage(self.PATH_BASE + "notification.tga")
		self.alarmImage.Show()

		# alarm button
		self.alarmButton = ui.Button()
		self.alarmButton.SetParent(self)
		self.alarmButton.SetUpVisual(self.PATH_BASE + "checkbox_new_unselected.tga")
		self.alarmButton.SetOverVisual(self.PATH_BASE + "checkbox_new_unselected.tga")
		self.alarmButton.SetDownVisual(self.PATH_BASE + "checkbox_new_selected.tga")
		self.alarmButton.SetPosition(569, 571)
		self.alarmButton.SetEvent(self.OnAlarmButton)
		self.alarmButton.Show()

		# teleport button
		self.btnTeleport = ui.Button()
		self.btnTeleport.SetParent(self)
		self.btnTeleport.SetUpVisual(self.PATH_BASE + "teleport_btn_normal.tga")
		self.btnTeleport.SetOverVisual(self.PATH_BASE + "teleport_btn_hover.tga")
		self.btnTeleport.SetDownVisual(self.PATH_BASE + "teleport_btn_down.tga")
		self.btnTeleport.SetPosition(347, 566)
		self.btnTeleport.SetText(uiScriptLocale.EVENT_JOIN_ACCEPT_BUTTON)
		self.btnTeleport.SetEvent(self.OnTeleportButton)
		self.btnTeleport.Show()

		self.wndDescription = self.DescriptionWindow(239, 287)
		self.wndDescription.SetParent(self)
		self.wndDescription.SetPosition(347, 273)
		# self.wndDescription.ChangeDescription(localeInfo.DESCRIPTION_EXAMPLE)
		self.wndDescription.Open()

		self.questElements = []

		questX = 18
		questY = 43

		if constInfo.QUEST_TIMER_SCROLLBAR:
			self.questListBox = ui.ListBoxEx()
			self.questListBox.SetParent(self)
			self.questListBox.SetPosition(questX, questY)
			self.questListBox.SetSize(300, 570)
			self.questListBox.SetItemSize(300, 50)
			self.questListBox.SetItemStep(50)
			self.questListBox.SetViewItemCount(11)
			self.questListBox.Show()

			self.scrollBarQLB = ui.ScrollBarTemplate()
			self.scrollBarQLB.SetParent(self)
			self.scrollBarQLB.SetPosition(305 + questX + 1, questY - 1)
			self.scrollBarQLB.SetMiddleImage("d:/ymir work/ui/game/questtimer/scrollbar/scrollbar2.tga")
			self.scrollBarQLB.SetScrollBarSize(550)
			self.scrollBarQLB.Show()

			self.questListBox.SetScrollBar(self.scrollBarQLB)

		# create quests
		for i in range(len(self.QUESTS)):
			index = i + 1

			if self.QUESTS[i] == None:
				continue

			background = ui.ImageBox()
			if not constInfo.QUEST_TIMER_SCROLLBAR:
				background.SetParent(self)
				background.SetPosition(questX, questY + (i * 50))
			background.LoadImage(self.PATH_BASE + "quest_blue_bg.tga")
			background.SAFE_SetStringEvent("MOUSE_LEFT_DOWN", self.OnClickQuest, i)
			background.Show()

			icon = ui.ImageBox()
			icon.SetParent(background)
			icon.SetPosition(3, 3)
			icon.LoadImage(self.PATH_ICONS + "%d.tga" % index)
			icon.SAFE_SetStringEvent("MOUSE_LEFT_DOWN", self.OnClickQuest, i)
			icon.Show()

			name = ui.TextLine()
			name.SetParent(background)
			name.SetPosition(50, 8)
			name.SetHorizontalAlignLeft()
			name.SetText(self.QUESTS[i][0])
			name.Show()

			cooldown = ui.TextLine()
			cooldown.SetParent(background)
			cooldown.SetPosition(50, 23)
			cooldown.SetHorizontalAlignLeft()
			cooldown.SetText("")
			cooldown.Show()

			state = ui.TextLine()
			state.SetParent(background)
			state.SetPosition(14, 15)
			state.SetWindowHorizontalAlignRight()
			state.SetHorizontalAlignRight()
			state.SetText(localeInfo.QUEST_TIMER_AVAILABLE)
			state.Show()

			self.questElements.append([background, icon, name, cooldown, state])

			if constInfo.QUEST_TIMER_SCROLLBAR:
				self.questListBox.AppendItem(background)

		# open biolog as default
		self.OnClickQuest(0)

		self.initialized = True

	def TimeToString(self, timeLeft):
		timeLeft = int(timeLeft - app.GetTime())

		if timeLeft > 0:

			hours = int(timeLeft / 3600)
			minutes = int((timeLeft - hours * 3600) / 60)
			seconds = int(timeLeft - hours * 3600 - minutes * 60)

			timeLeftString = ""

			if hours < 10:
				timeLeftString += "0"

			timeLeftString += str(hours) + ":"

			if minutes < 10:
				timeLeftString += "0"

			timeLeftString += str(minutes) + ":"

			if seconds < 10:
				timeLeftString += "0"

			return timeLeftString + str(seconds)

		return "00:00:00"

	def UpdateTimers(self, key, value):
		key 	= int(key)
		value 	= float(value)

		if self.COOLDOWNS[key] == 0 and value == 0:
			return

		# fix biolog zero on teleportation :/ thats the simplest way
		if key == 0 and value == 0.0:
			self.COOLDOWNS[0] = 0
			return

		# tchat("UpdateTimers(%s, %s)" % (str(key), str(value)))

		self.COOLDOWNS[key] = app.GetTime() + value

		# tchat(str(self.COOLDOWNS))

	def ChangeAlarmButtonState(self, state):
		# swap visuals -> radio button doesnt work good here...
		visualUp 	= self.PATH_BASE + "checkbox_new_unselected.tga"
		visualDown 	= self.PATH_BASE + "checkbox_new_selected.tga"

		if state:
			self.alarmButton.SetUpVisual(visualDown)
			self.alarmButton.SetDownVisual(visualUp)
			self.alarmButton.SetOverVisual(visualDown)
		else:
			self.alarmButton.SetUpVisual(visualUp)
			self.alarmButton.SetDownVisual(visualDown)
			self.alarmButton.SetOverVisual(visualUp)

	def OnAlarmButton(self):
		isEnabled = bool(self.NOTIFICATION_ENABLED[self.questIndex])

		self.ChangeAlarmButtonState(not isEnabled)
		self.NOTIFICATION_ENABLED[self.questIndex] = not isEnabled

	def OnPassageTicketHover(self):
		self.itemToolTip.SetItemToolTip(self.itemVnum)
		self.itemToolTip.ShowToolTip()

	def OnPassageTicketMouseOut(self):
		self.itemToolTip.HideToolTip()

	def SetItemToolTip(self, itemToolTip):
		self.itemToolTip = itemToolTip

	def OnClickQuest(self, id, isBiologRefresh = False, playSound = True):
		if self.questIndex == id and not isBiologRefresh:
			return

		if self.initialized and playSound:
			snd.PlaySound("sound/ui/click.wav")

		self.questIndex = id

		# change images etc.
		self.ChangeBanner(id)
		self.ChangePassageTicket(id)
		self.ChangeDungeonName(id)

		if not isBiologRefresh:
			self.ChangeDescription(id)
		
		self.ChangeDungeonInfo(id)

		# update button state (checked or not?)
		self.UpdateNotifyButtonState(id)

		if self.IsBiologQuest():
			self.dungeonInfo[0][1].SetText(localeInfo.QUEST_TIMER_CURRENT)
			self.passageTicketText.SetText(localeInfo.QUEST_TIMER_QUESTITEM)
			self.dungeonDescriptionTitle.SetText(localeInfo.QUEST_TIMER_REWARDS)
			self.dungeonInfo[1][1].SetText(localeInfo.QUEST_TIMER_BIOLOGREADY)
			return

		self.dungeonInfo[0][1].SetText(localeInfo.QUEST_TIMER_MINLVL)
		self.passageTicketText.SetText(localeInfo.QUEST_TIMER_PASSAGETICKET)
		self.dungeonDescriptionTitle.SetText(localeInfo.QUEST_TIMER_DUNGEON_DESC)
		self.dungeonInfo[1][1].SetText(localeInfo.QUEST_TIMER_GROUPREQ)

	def UpdateNotifyButtonState(self, id):
			self.ChangeAlarmButtonState(self.NOTIFICATION_ENABLED[self.questIndex])

	def OnTeleportButton(self):
		# tchat("Teleport to: %d" % self.questIndex)

		# dont teleport players below lvl 75 to grotto
		if self.questIndex == 4 and player.GetStatus(player.LEVEL) < 75:
			chat.AppendChat(1, "You need to be level 75 or higher to enter this area!")
			return

		self.dialog = uiCommon.QuestionDialog()
		self.dialog.index = self.questIndex
		self.dialog.SetText(localeInfo.TIMER_WARP_QUESTION)
		self.dialog.SetAcceptText(localeInfo.YES)
		self.dialog.SetCancelText(localeInfo.NO)
		self.dialog.SetAcceptEvent(lambda arg = True: self.SendWarpCommand(arg))
		self.dialog.SetCancelEvent(lambda arg = False: self.SendWarpCommand(arg))
		self.dialog.Open()

	def GetBiologIndexFromLevel(self, currentLevel):
		biologQuests = [
			[0, 0],
			[30, 1],
			[40, 2],
			[50, 3],
			[60, 4],
			[70, 5],
			[80, 6],
			[85, 7],
			[90, 8],
			[92, 9],
			[94, 10],
			[8, 11], 	# 108
			[12, 12], # 112
		]

		for quest in biologQuests:
			if quest[0] == currentLevel:
				return quest[1]

		return 0

	def UpdateBiologInfo(self, currentLevel):
		currentLevel = int(currentLevel)
		biologIndex = self.GetBiologIndexFromLevel(currentLevel)

		# tchat("UpdateBiologInfo(currentLevel: %d => %d)" % (currentLevel, biologIndex))

		levelStr = "None"

		if currentLevel != 0:
			levelStr = str(currentLevel)

		self.QUESTS[0][2] = levelStr
		self.QUESTS[0][4] = str(self.BIOLOG[biologIndex][1])
		self.QUESTS[0][5] = int(self.BIOLOG[biologIndex][0])

		if self.IsBiologQuest():
			self.OnClickQuest(0, True, False)

	def SendWarpCommand(self, answer):
		if answer:
			net.SendChatPacket("/timer_warp %d" % self.dialog.index)
			self.Close()

		self.dialog.Hide()
		self.dialog.Close()

	def ChangeDungeonInfo(self, id):
		minLevel = self.QUESTS[id][2]
		maxLevel = self.QUESTS[id][6]
		groupReq = self.QUESTS[id][3]
		cooldown = self.QUESTS[id][4]

		groupReqStr = localeInfo.NO

		if groupReq:
			groupReqStr = localeInfo.YES

		levelStr = minLevel
		if minLevel != maxLevel and id > 0:
			levelStr = ("%s - %s" % (minLevel, maxLevel))
		elif minLevel == "None" and id > 0:
			levelStr = "-"
			
		self.dungeonInfo[0][2].SetText(levelStr)
		self.dungeonInfo[1][2].SetText(groupReqStr)
		self.dungeonInfo[2][2].SetText(cooldown)

	def ChangeBanner(self, id):
		self.bannerImage.LoadImage(self.PATH_BANNERS + "%s.tga" % str(id + 1))

	def ChangePassageTicket(self, id):
		itemVnum = self.QUESTS[id][5]

		if not itemVnum or itemVnum == 0:
			self.passageTicketItem.Hide()
			self.passageTicketItemNone.Show()
			return

		item.SelectItem(1, 2, itemVnum)
		image = item.GetIconImageFileName()

		self.passageTicketItem.LoadImage(image)
		self.itemVnum = itemVnum
		self.passageTicketItem.Show()
		self.passageTicketItemNone.Hide()
	
	def ChangeDungeonName(self, id):
		dungeonName = self.QUESTS[id][0]
		self.dungeonName.SetText(dungeonName)

	def ChangeDescription(self, id):
		dungeonDescription = self.QUESTS[id][1]
		self.wndDescription.ChangeDescription(dungeonDescription)

	def Close(self):
		self.Hide()
		
	def Open(self):
		if not constInfo.NEW_QUEST_TIMER:
			return

		if not net.IsGamePhase(net.PHASE_WINDOW_GAME):
			return

		net.SendChatPacket("/get_timer_cdrs")
		self.SetCenterPosition()
		self.Show()

	# change only if different string so it wont read it every time it gets called
	def ChangeQuestBackground(self, id, newBackground):
		currentBackground = self.questElements[id][0].GetImageName()
		if currentBackground == newBackground:
			return
		
		self.questElements[id][0].LoadImage(newBackground)

	def OnPressEscapeKey(self):
		self.Close()
		return True

	def IsBiologQuest(self):
		return (self.questIndex == 0)

	def OnUpdate(self):
		for i in range(0, len(self.QUESTS)):
			# WTF ??? 
			# if self.QUESTS[i] == NONE or i not in self.COOLDOWNS:
			# 	tchat(str(self.QUESTS[i]))
			# 	tchat("SKIP %i [%d, %d]" % (i, self.QUESTS[i] == None, i not in self.COOLDOWNS))
			# 	continue
			try:
				cooldownTextLine = self.questElements[i][3]
			except:
				tchat(str(self.questElements[i]))
			cooldown = self.TimeToString(self.COOLDOWNS[i])
			cooldownTextLine.SetText(cooldown)

			isAvailable = (cooldown == "00:00:00")

			if isAvailable:
				self.ChangeQuestBackground(i, self.PATH_BASE + "quest_blue_bg.tga")

				textAvailable = localeInfo.QUEST_TIMER_AVAILABLE

				# fix old label, no need to translate again i think ;d
				if textAvailable.endswith('!'):
					textAvailable = textAvailable[:-1]

				self.questElements[i][4].SetText(textAvailable)

			else:
				self.ChangeQuestBackground(i, self.PATH_BASE + "quest_red_bg.tga")

				self.questElements[i][4].SetText(localeInfo.QUEST_TIMER_LOCKED)

		# biolog quest choosen
		if self.IsBiologQuest():
			
			# quest is ready
			if self.questElements[0][3].GetText() == "00:00:00":
				self.dungeonInfo[1][2].SetText(localeInfo.YES)

			else:
				self.dungeonInfo[1][2].SetText(localeInfo.NO)

	if constInfo.QUEST_TIMER_SCROLLBAR:
		def OnMouseWheel(self, len_):
			if (self.questListBox.IsInPosition() or self.scrollBarQLB.IsInPosition()) and self.scrollBarQLB.IsShow():
				dir_ = constInfo.WHEEL_TO_SCROLL(len_)
				newPos = self.scrollBarQLB.GetPos() + ((1.0 / len(self.QUESTS)) * dir_)
				newPos = max(0.0, newPos)
				newPos = min(1.0, newPos)
				self.scrollBarQLB.SetPos(newPos)
				return True

			return False

	def Destroy(self):
		self.backgroundImage = None
		self.titleBar = None
		self.titleName = None
		self.bannerImage = None
		self.dungeonNameBox = None
		self.dungeonName = None
		self.dungeonDescriptionTitle = None
		self.dungeonInfo = []
		self.passageTicketBox = None
		self.passageTicketText = None
		self.passageTicketItem = None
		self.passageTicketItemNone = None
		self.alarmImage = None
		self.alarmButton = None
		self.btnTeleport = None
		self.wndDescription.Destroy()
		self.wndDescription = None
		self.questElements = []
		self.questListBox = None
		self.scrollBarQLB = None
