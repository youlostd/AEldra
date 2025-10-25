import app
import ui
import player
import net
import wndMgr
import messenger
import guild
import chr
import nonplayer
import localeInfo
import constInfo
import uiToolTip
import item
import chrmgr
import background
from math import pow

if app.ENABLE_VIEW_ELEMENT:
	ELEMENT_IMAGE_DIC = {1: "elect", 2: "wind", 3: "earth", 4: "dark", 5: "fire", 6: "ice"}
	ELEMENT_NAME_DIC = {
		1 : localeInfo.TOOLTP_ELEMENT_NAME_ELECT,
		2 : localeInfo.TOOLTP_ELEMENT_NAME_WIND,
		3 : localeInfo.TOOLTP_ELEMENT_NAME_EARTH,
		4 : localeInfo.TOOLTP_ELEMENT_NAME_DARK,
		5 : localeInfo.TOOLTP_ELEMENT_NAME_FIRE,
		6 : localeInfo.TOOLTP_ELEMENT_NAME_ICE,
	}

def HAS_FLAG(value, flag):
	return (value & flag) == flag

CLASS_THINBOARD = ui.ThinBoard
if constInfo.NEW_TARGET_UI:
	import mouseModule
	CLASS_THINBOARD = ui.ThinBoardTarget

class TargetBoard(CLASS_THINBOARD):

	class InfoBoard(ui.ThinBoard):

		class ItemListBoxItem(ui.ListBoxExNew.Item):

			def __init__(self, width, parent):
				ui.ListBoxExNew.Item.__init__(self)

				image = ui.ExpandedImageBox()
				image.SetParent(self)
				image.Show()
				self.image = image
				self.myparent = parent

				nameLine = ui.TextLine()
				nameLine.SetParent(self)
				nameLine.SetPosition(32 + 5, 0)
				nameLine.Show()
				self.nameLine = nameLine

				self.SetSize(width, 32 + 5)

			def LoadImage(self, image):
				self.image.LoadImage(image)
				self.SetSize(self.GetWidth(), max(32, self.image.GetHeight()) + 5 * (max(32, self.image.GetHeight()) / 32))

			def SetText(self, text):
				self.nameLine.SetText(text)
				
			def OnMouseWheel(self, len):
				return self.myparent.OnMouseWheel(len)

			def RefreshHeight(self):
				ui.ListBoxExNew.Item.RefreshHeight(self)
				self.image.SetRenderingRect(0.0, 0.0 - float(self.removeTop) / float(self.GetHeight()), 0.0, 0.0 - float(self.removeBottom) / float(self.GetHeight()))
				self.image.SetPosition(0, - self.removeTop)

		MAX_ITEM_COUNT = 5

		EXP_BASE_LVDELTA = [
			1,  #  -15 0
			5,  #  -14 1
			10, #  -13 2
			20, #  -12 3
			30, #  -11 4
			50, #  -10 5
			70, #  -9  6
			80, #  -8  7
			85, #  -7  8
			90, #  -6  9
			92, #  -5  10
			94, #  -4  11
			96, #  -3  12
			98, #  -2  13
			100,	#  -1  14
			100,	#  0   15
			105,	#  1   16
			110,	#  2   17
			115,	#  3   18
			120,	#  4   19
			125,	#  5   20
			130,	#  6   21
			135,	#  7   22
			140,	#  8   23
			145,	#  9   24
			150,	#  10  25
			155,	#  11  26
			160,	#  12  27
			165,	#  13  28
			170,	#  14  29
			180,	#  15  30
		]

		RACE_FLAG_TO_NAME = {
			nonplayer.RACE_FLAG_ANIMAL : localeInfo.TARGET_INFO_RACE_ANIMAL,
			nonplayer.RACE_FLAG_UNDEAD : localeInfo.TARGET_INFO_RACE_UNDEAD,
			nonplayer.RACE_FLAG_DEVIL : localeInfo.TARGET_INFO_RACE_DEVIL,
			nonplayer.RACE_FLAG_HUMAN : localeInfo.TARGET_INFO_RACE_HUMAN,
			nonplayer.RACE_FLAG_ORC : localeInfo.TARGET_INFO_RACE_ORC,
			nonplayer.RACE_FLAG_MILGYO : localeInfo.TARGET_INFO_RACE_MILGYO,
			nonplayer.RACE_FLAG_TREE : localeInfo.TARGET_INFO_RACE_TREE,
			nonplayer.RACE_FLAG_ZODIAC : localeInfo.TARGET_INFO_RACE_ZODIAC,
		}
		SUB_RACE_FLAG_TO_NAME = {
			nonplayer.RACE_FLAG_ELEC : localeInfo.TARGET_INFO_RACE_ELEC,
			nonplayer.RACE_FLAG_FIRE : localeInfo.TARGET_INFO_RACE_FIRE,
			nonplayer.RACE_FLAG_ICE : localeInfo.TARGET_INFO_RACE_ICE,
			nonplayer.RACE_FLAG_WIND : localeInfo.TARGET_INFO_RACE_WIND,
			nonplayer.RACE_FLAG_EARTH : localeInfo.TARGET_INFO_RACE_EARTH,
			nonplayer.RACE_FLAG_DARK : localeInfo.TARGET_INFO_RACE_DARK,
		}

		STONE_START_VNUM = 28030
		STONE_LAST_VNUM = 28042

		BOARD_WIDTH = 250

		def __init__(self):
			ui.ThinBoard.__init__(self)

			self.HideCorners(self.LT)
			self.HideCorners(self.RT)
			self.HideLine(self.T)

			self.race = 0
			self.hasItems = False

			self.itemTooltip = uiToolTip.ItemToolTip()
			self.itemTooltip.HideToolTip()

			self.stoneImg = None
			self.lastStoneVnum = 0
			self.nextStoneIconChange = 0
			self.itemScrollBar = None

			self.SetSize(self.BOARD_WIDTH, 0)

		def __del__(self):
			ui.ThinBoard.__del__(self)

		def __UpdatePosition(self, targetBoard):
			self.SetPosition(targetBoard.GetLeft() + (targetBoard.GetWidth() - self.GetWidth()) / 2, targetBoard.GetBottom())

		def Open(self, targetBoard, race):
			self.__LoadInformation(race)

			self.SetSize(self.BOARD_WIDTH, self.yPos + 10)
			self.__UpdatePosition(targetBoard)

			self.Show()

		def Refresh(self):
			self.__LoadInformation(self.race)
			self.SetSize(self.BOARD_WIDTH, self.yPos + 10)

		def Close(self):
			self.itemTooltip.HideToolTip()
			self.Hide()

		def __LoadInformation(self, race):
			if self.race == race and self.hasItems == constInfo.MONSTER_INFO_DATA[race]["recv"]:
				return

			self.yPos = 7
			self.children = []
			self.race = race
			self.stoneImg = None
			self.nextStoneIconChange = 0
			self.hasItems = constInfo.MONSTER_INFO_DATA[race]["recv"]

			self.__LoadInformation_Default(race)
			self.__LoadInformation_Race(race)
			self.__LoadInformation_Drops(race)

		def __LoadInformation_Default_GetHitRate(self, race):
			attacker_dx = nonplayer.GetMonsterDX(race)
			attacker_level = nonplayer.GetMonsterLevel(race)

			self_dx = player.GetStatus(player.DX)
			self_level = player.GetStatus(player.LEVEL)

			iARSrc = min(90, (attacker_dx * 4 + attacker_level * 2) / 6)
			iERSrc = min(90, (self_dx * 4 + self_level * 2) / 6)

			fAR = (float(iARSrc) + 210.0) / 300.0
			fER = (float(iERSrc) * 2 + 5) / (float(iERSrc) + 95) * 3.0 / 10.0

			return fAR - fER

		def __LoadInformation_Default(self, race):
			self.AppendTextLine(localeInfo.TARGET_INFO_MAX_HP % localeInfo.NumberToString(nonplayer.GetMonsterMaxHP(race)))

			# calc att damage
			monsterLevel = nonplayer.GetMonsterLevel(race)
			if not nonplayer.IsMonsterStone(race):
				fHitRate = self.__LoadInformation_Default_GetHitRate(race)
				iDamMin, iDamMax = nonplayer.GetMonsterDamage(race)
				iDamMin = int((iDamMin + nonplayer.GetMonsterST(race)) * 2 * fHitRate) + monsterLevel * 2
				iDamMax = int((iDamMax + nonplayer.GetMonsterST(race)) * 2 * fHitRate) + monsterLevel * 2
				iDef = player.GetStatus(player.DEF_GRADE) * (100 + player.GetStatus(player.DEF_BONUS)) / 100
				fDamMulti = nonplayer.GetMonsterDamageMultiply(race)
				iDamMin = int(max(0, iDamMin - iDef) * fDamMulti)
				iDamMax = int(max(0, iDamMax - iDef) * fDamMulti)
				if iDamMin < 1:
					iDamMin = 1
				if iDamMax < 5:
					iDamMax = 5
				self.AppendTextLine(localeInfo.TARGET_INFO_DAMAGE % (localeInfo.NumberToString(iDamMin), localeInfo.NumberToString(iDamMax)))

		#	iDef = monsterLevel + nonplayer.GetMonsterHT(race) + nonplayer.GetMonsterDefense(race)
		#	self.AppendTextLine(localeInfo.TARGET_INFO_DEFENSE % localeInfo.NumberToString(iDef))

			idx = min(len(self.EXP_BASE_LVDELTA) - 1, max(0, (monsterLevel + 15) - player.GetStatus(player.LEVEL)))
			iExp = nonplayer.GetMonsterExp(race) * self.EXP_BASE_LVDELTA[idx] / 100
			self.AppendTextLine(localeInfo.TARGET_INFO_EXP % localeInfo.NumberToString(iExp))

		def __LoadInformation_Race(self, race):
			dwRaceFlag = nonplayer.GetMonsterRaceFlag(race)
			self.AppendSeperator()

			mainrace = ""
			subrace = ""
			for i in xrange(nonplayer.RACE_FLAG_MAX_NUM):
				curFlag = 1 << i
				if HAS_FLAG(dwRaceFlag, curFlag):
					if self.RACE_FLAG_TO_NAME.has_key(curFlag):
						mainrace += self.RACE_FLAG_TO_NAME[curFlag] + ", "
					elif self.SUB_RACE_FLAG_TO_NAME.has_key(curFlag):
						subrace += self.SUB_RACE_FLAG_TO_NAME[curFlag] + ", "
			if nonplayer.IsMonsterStone(race):
				mainrace += localeInfo.TARGET_INFO_RACE_METIN + ", "
			if mainrace == "":
				mainrace = localeInfo.TARGET_INFO_NO_RACE
			else:
				mainrace = mainrace[:-2]
			if subrace == "":
				subrace = localeInfo.TARGET_INFO_NO_RACE
			else:
				subrace = subrace[:-2]

			self.AppendTextLine(localeInfo.TARGET_INFO_MAINRACE % mainrace)
			self.AppendTextLine(localeInfo.TARGET_INFO_SUBRACE % subrace)

		def __LoadInformation_Drops(self, race):
			self.AppendSeperator()

			if self.hasItems:
				if len(constInfo.MONSTER_INFO_DATA[race]["items"]) == 0:
					self.AppendTextLine(localeInfo.TARGET_INFO_NO_ITEM_TEXT)
				else:
					itemListBox = ui.ListBoxExNew(32 + 5, self.MAX_ITEM_COUNT)
					itemListBox.SetSize(self.GetWidth() - 15 * 2 - ui.ScrollBar.SCROLLBAR_WIDTH, (32 + 5) * self.MAX_ITEM_COUNT)
					height = 0

					# tchat(str(constInfo.MONSTER_INFO_DATA[race]["items"]))
					for curItem in constInfo.MONSTER_INFO_DATA[race]["items"]:
						if curItem.has_key('vnum') and 50513 == curItem['vnum'] and constInfo.MONSTER_INFO_DATA[race]["items"][0].has_key('vnum') and constInfo.MONSTER_INFO_DATA[race]["items"][0]['vnum'] > 0:
							idx = constInfo.MONSTER_INFO_DATA[race]["items"].index(curItem)
							tmp_item = constInfo.MONSTER_INFO_DATA[race]["items"][0]
							constInfo.MONSTER_INFO_DATA[race]["items"][0] = constInfo.MONSTER_INFO_DATA[race]["items"][idx]
							constInfo.MONSTER_INFO_DATA[race]["items"][idx] = tmp_item
							# tchat(str(constInfo.MONSTER_INFO_DATA[race]["items"]))

					for curItem in constInfo.MONSTER_INFO_DATA[race]["items"]:
						if curItem.has_key("vnum_list"):
							height += self.AppendItem(itemListBox, curItem["level"], curItem["vnum_list"], curItem["count"])
						else:
							height += self.AppendItem(itemListBox, curItem["level"], curItem["vnum"], curItem["count"])
					if height < itemListBox.GetHeight():
						itemListBox.SetSize(itemListBox.GetWidth(), height)
					self.AppendWindow(itemListBox, 15)
					itemListBox.SetBasePos(0)

					if len(constInfo.MONSTER_INFO_DATA[race]["items"]) > itemListBox.GetViewItemCount():
						itemScrollBar = ui.ScrollBar()
						itemScrollBar.SetParent(self)
						itemScrollBar.SetPosition(itemListBox.GetRight(), itemListBox.GetTop())
						itemScrollBar.SetScrollBarSize(32 * self.MAX_ITEM_COUNT + 5 * (self.MAX_ITEM_COUNT - 1))
						itemScrollBar.SetMiddleBarSize(float(self.MAX_ITEM_COUNT) / float(height / (32 + 5)))
						self.itemScrollBar = itemScrollBar
						self.itemScrollBar.Show()
						itemListBox.SetScrollBar(itemScrollBar)
					else:
						if self.itemScrollBar:
							self.itemScrollBar.Hide()
			else:
				imgWaiting = ui.AniImageBox()
				imgWaiting.SetDelay(6)
				for i in xrange(8):
					imgWaiting.AppendImage("d:/ymir work/ui/loading_ani/%02d.tga" % i)
				self.AppendWindow(imgWaiting, 0, 16, 16)

		def AppendTextLine(self, text, color=None):
			textLine = ui.TextLine()
			textLine.SetParent(self)
			textLine.SetWindowHorizontalAlignCenter()
			textLine.SetHorizontalAlignCenter()
			textLine.SetText(text)
			textLine.SetPosition(0, self.yPos)
			if color:
				textLine.SetPackedFontColor(color)
			textLine.Show()

			self.children.append(textLine)
			self.yPos += 17

		def AppendSeperator(self):
			img = ui.ImageBox()
			img.LoadImage("d:/ymir work/ui/seperator.tga")
			self.AppendWindow(img)
			img.SetPosition(img.GetLeft(), img.GetTop() - 15)
			self.yPos -= 15

		def AppendItem(self, listBox, levellimit, vnums, count):
			if type(vnums) == int:
				vnum = vnums
			else:
				vnum = vnums[0]
			
			if not item.SelectItem(1, 2, vnum):
				return 0

			itemName = item.GetItemName()
			if type(vnums) != int and len(vnums) > 1:
				vnums = sorted(vnums)
				realName = itemName[:itemName.find("+")]
				if item.GetItemType() == item.ITEM_TYPE_METIN:
					realName = localeInfo.TARGET_INFO_STONE_NAME
					minLv = vnums[0] % 1000 / 100
					maxLv = vnums[len(vnums) - 1] % 1000 / 100
					if minLv != maxLv:
						itemName = realName + "+" + str(minLv) + " - +" + str(maxLv)
					else:
						itemName = realName + "+" + str(maxLv)
				else:
					itemName = realName + "+" + str(vnums[0] % 10) + " - +" + str(vnums[len(vnums) - 1] % 10)
				vnum = vnums[len(vnums) - 1]

			iconName = item.GetIconImageFileName()

			myItem = self.ItemListBoxItem(listBox.GetWidth(), self)
			myItem.LoadImage(iconName)

			name = itemName
			if count > 1:
				name = str(count) + "x " + name
			if levellimit > 1:
				name = name + " " + (localeInfo.TARGET_INFO_LEVELLIMIT % levellimit)
			myItem.SetText(name)

			myItem.SAFE_SetOverInEvent(self.OnShowItemTooltip, vnum)
			myItem.SAFE_SetOverOutEvent(self.OnHideItemTooltip)
			listBox.AppendItem(myItem)

			if item.GetItemType() == item.ITEM_TYPE_METIN:
				self.stoneImg = myItem
				self.lastStoneVnum = self.STONE_LAST_VNUM + vnums[len(vnums) - 1] % 1000 / 100 * 100

			return myItem.GetHeight()

		def OnShowItemTooltip(self, vnum):
			item.SelectItem(1, 2, vnum)
			if item.GetItemType() == item.ITEM_TYPE_METIN:
				self.itemTooltip.SetItemToolTip(self.lastStoneVnum)
				self.itemTooltip.isStone = True
			else:
				self.itemTooltip.SetItemToolTip(vnum)
				self.itemTooltip.isStone = False

		def OnHideItemTooltip(self):
			self.itemTooltip.HideToolTip()

		def AppendWindow(self, wnd, x=0, width=0, height=0):
			if width == 0:
				width = wnd.GetWidth()
			if height == 0:
				height = wnd.GetHeight()

			wnd.SetParent(self)
			if x == 0:
				wnd.SetPosition((self.GetWidth() - width) / 2, self.yPos)
			else:
				wnd.SetPosition(x, self.yPos)
			wnd.Show()

			self.children.append(wnd)
			self.yPos += height + 5

		def OnMouseWheel(self, len2):
			lineCount = len(constInfo.MONSTER_INFO_DATA[self.race]["items"])
			if self.hasItems and self.itemScrollBar and self.itemScrollBar.IsShow() and lineCount > 0: #'NoneType' object has no attribute 'IsShow'
				dir = constInfo.WHEEL_TO_SCROLL(len2)
				new_pos = self.itemScrollBar.GetPos() + ((1.0 / lineCount) * dir)
				new_pos = max(0.0, new_pos)
				new_pos = min(1.0, new_pos)
				self.itemScrollBar.SetPos(new_pos)
				return True
			return False

		def OnUpdate(self):
			if self.stoneImg != None and app.GetTime() >= self.nextStoneIconChange:
				nextImg = self.lastStoneVnum + 1
				if nextImg % 100 > self.STONE_LAST_VNUM % 100:
					nextImg -= (self.STONE_LAST_VNUM - self.STONE_START_VNUM) + 1
				self.lastStoneVnum = nextImg
				self.nextStoneIconChange = app.GetTime() + 2.5

				item.SelectItem(1, 2, nextImg)
				self.stoneImg.LoadImage(item.GetIconImageFileName())

				if self.itemTooltip.IsShow() and self.itemTooltip.isStone:
					self.itemTooltip.SetItemToolTip(nextImg)

	if constInfo.NEW_TARGET_UI:
		class TextToolTip(ui.Window):
			def __init__(self):
				ui.Window.__init__(self, "TOP_MOST")

				textLine = ui.TextLine()
				textLine.SetParent(self)
				textLine.SetHorizontalAlignCenter()
				textLine.SetOutline()
				textLine.Show()
				self.textLine = textLine

			def __del__(self):
				ui.Window.__del__(self)

			def SetText(self, text):
				self.textLine.SetText(text)

			def OnRender(self):
				(mouseX, mouseY) = wndMgr.GetMousePosition()
				self.textLine.SetPosition(mouseX, mouseY - 15)

	BUTTON_NAME_LIST = ( 
		localeInfo.TARGET_BUTTON_WHISPER, 
		localeInfo.TARGET_BUTTON_EXCHANGE, 
		localeInfo.TARGET_BUTTON_FIGHT, 
		localeInfo.TARGET_BUTTON_ACCEPT_FIGHT, 
		localeInfo.TARGET_BUTTON_AVENGE, 
		localeInfo.TARGET_BUTTON_FRIEND, 
		localeInfo.TARGET_BUTTON_INVITE_PARTY, 
		localeInfo.TARGET_BUTTON_LEAVE_PARTY, 
		localeInfo.TARGET_BUTTON_EXCLUDE, 
		localeInfo.TARGET_BUTTON_INVITE_GUILD,
		localeInfo.TARGET_BUTTON_DISMOUNT,
		localeInfo.TARGET_BUTTON_EXIT_OBSERVER,
		localeInfo.TARGET_BUTTON_VIEW_EQUIPMENT,
		localeInfo.TARGET_BUTTON_REQUEST_ENTER_PARTY,
		localeInfo.TARGET_BUTTON_BUILDING_DESTROY,
		localeInfo.TARGET_BUTTON_EMOTION_ALLOW,
		localeInfo.TARGET_BUTTON_BLOCK,
		localeInfo.TARGET_BUTTON_UNBLOCK,
		
	)

	GRADE_NAME =	{
						nonplayer.PAWN : localeInfo.TARGET_LEVEL_PAWN,
						nonplayer.S_PAWN : localeInfo.TARGET_LEVEL_S_PAWN,
						nonplayer.KNIGHT : localeInfo.TARGET_LEVEL_KNIGHT,
						nonplayer.S_KNIGHT : localeInfo.TARGET_LEVEL_S_KNIGHT,
						nonplayer.BOSS : localeInfo.TARGET_LEVEL_BOSS,
						nonplayer.KING : localeInfo.TARGET_LEVEL_KING,
					}
	EXCHANGE_LIMIT_RANGE = 3000

	def __init__(self):
		CLASS_THINBOARD.__init__(self)

		name = ui.TextLine()
		name.SetParent(self)
		name.SetDefaultFontName()
		name.SetOutline()
		name.Show()

		hpDmgGauge = ui.Gauge()
		hpDmgGauge.SetParent(self)
		hpDmgGauge.SetPosition(180, 17)
		hpDmgGauge.MakeGauge(130, "orange")
		hpDmgGauge.SetWindowHorizontalAlignRight()
		hpDmgGauge.Hide()
		hpDmgGauge.nextUpdate = 0.0
		hpDmgGauge.updateInterval = 0.0

		hpGauge = ui.Gauge()
		hpGauge.SetParent(self)
		hpGauge.SetPosition(180, 17)
		hpGauge.MakeGauge(130, "red")
		hpGauge.SetWindowHorizontalAlignRight()
		hpGauge.imgRight.Hide()
		hpGauge.imgLeft.Hide()
		hpGauge.imgCenter.Hide()
		hpGauge.Hide()

		hpPoisonGauge = ui.Gauge()
		hpPoisonGauge.SetParent(self)
		hpPoisonGauge.SetPosition(180, 17)
		hpPoisonGauge.MakeGauge(130, "green")
		hpPoisonGauge.SetWindowHorizontalAlignRight()
		hpPoisonGauge.imgRight.Hide()
		hpPoisonGauge.imgLeft.Hide()
		hpPoisonGauge.imgCenter.Hide()
		hpPoisonGauge.Hide()

		hpBurnGauge = ui.Gauge()
		hpBurnGauge.SetParent(self)
		hpBurnGauge.SetPosition(180, 17)
		hpBurnGauge.MakeGauge(130, "yellow")
		hpBurnGauge.SetWindowHorizontalAlignRight()
		hpBurnGauge.imgRight.Hide()
		hpBurnGauge.imgLeft.Hide()
		hpBurnGauge.imgCenter.Hide()
		hpBurnGauge.Hide()

		hpText = ui.TextLine()
		hpText.SetParent(hpGauge)
		hpText.SetHorizontalAlignCenter()
		hpText.SetWindowHorizontalAlignCenter()
		hpText.SetPosition(0, -14)
		hpText.SetOutline()
		hpText.Hide()

		hpGauge.hpText = hpText

		infoButton = ui.Button()
		infoButton.SetParent(self)
		infoButton.SetUpVisual("d:/ymir work/ui/game/target/mob_info_01.tga")
		infoButton.SetOverVisual("d:/ymir work/ui/game/target/mob_info_02.tga")
		infoButton.SetDownVisual("d:/ymir work/ui/game/target/mob_info_03.tga")
		infoButton.SetPosition(50, 11)
		infoButton.SetWindowHorizontalAlignRight()
		infoButton.SetEvent(ui.__mem_func__(self.OnPressedInfoButton))
		infoButton.Hide()

		infoBoard = self.InfoBoard()
		infoBoard.Hide()
		infoButton.showWnd = infoBoard

		closeButton = ui.Button()
		closeButton.SetParent(self)
		closeButton.SetUpVisual("d:/ymir work/ui/public/close_button_01.sub")
		closeButton.SetOverVisual("d:/ymir work/ui/public/close_button_02.sub")
		closeButton.SetDownVisual("d:/ymir work/ui/public/close_button_03.sub")
		closeButton.SetPosition(30, 13)
		closeButton.SetWindowHorizontalAlignRight()
		closeButton.SetEvent(ui.__mem_func__(self.OnPressedCloseButton))
		closeButton.Show()

		self.buttonDict = {}
		self.showingButtonList = []
		for buttonName in self.BUTTON_NAME_LIST:
			button = ui.Button()
			button.SetParent(self)
			if constInfo.NEW_TARGET_UI:
				button.SetUpVisual("d:/ymir work/ui/new_target/button_normal.tga")
				button.SetOverVisual("d:/ymir work/ui/new_target/button_hover.tga")
				button.SetDownVisual("d:/ymir work/ui/new_target/button_down.tga")
			else:
				button.SetUpVisual("d:/ymir work/ui/public/small_thin_button_01.sub")
				button.SetOverVisual("d:/ymir work/ui/public/small_thin_button_02.sub")
				button.SetDownVisual("d:/ymir work/ui/public/small_thin_button_03.sub")
			button.SetWindowHorizontalAlignCenter()
			button.SetText(buttonName)
			button.Hide()
			self.buttonDict[buttonName] = button
			self.showingButtonList.append(button)

		self.buttonDict[localeInfo.TARGET_BUTTON_WHISPER].SetEvent(ui.__mem_func__(self.OnWhisper))
		self.buttonDict[localeInfo.TARGET_BUTTON_EXCHANGE].SetEvent(ui.__mem_func__(self.OnExchange))
		self.buttonDict[localeInfo.TARGET_BUTTON_FIGHT].SetEvent(ui.__mem_func__(self.OnPVP))
		self.buttonDict[localeInfo.TARGET_BUTTON_ACCEPT_FIGHT].SetEvent(ui.__mem_func__(self.OnPVP))
		self.buttonDict[localeInfo.TARGET_BUTTON_AVENGE].SetEvent(ui.__mem_func__(self.OnPVP))
		self.buttonDict[localeInfo.TARGET_BUTTON_FRIEND].SetEvent(ui.__mem_func__(self.OnAppendToMessenger))
		self.buttonDict[localeInfo.TARGET_BUTTON_FRIEND].SetEvent(ui.__mem_func__(self.OnAppendToMessenger))
		self.buttonDict[localeInfo.TARGET_BUTTON_INVITE_PARTY].SetEvent(ui.__mem_func__(self.OnPartyInvite))
		self.buttonDict[localeInfo.TARGET_BUTTON_LEAVE_PARTY].SetEvent(ui.__mem_func__(self.OnPartyExit))
		self.buttonDict[localeInfo.TARGET_BUTTON_EXCLUDE].SetEvent(ui.__mem_func__(self.OnPartyRemove))
		# if app.ENABLE_MESSENGER_BLOCK:
		# 	self.buttonDict[localeInfo.TARGET_BUTTON_BLOCK].SetEvent(ui.__mem_func__(self.OnAppendToBlockMessenger))
		# 	self.buttonDict[localeInfo.TARGET_BUTTON_UNBLOCK].SetEvent(ui.__mem_func__(self.OnRemoveToBlockMessenger))

		self.buttonDict[localeInfo.TARGET_BUTTON_INVITE_GUILD].SAFE_SetEvent(self.__OnGuildAddMember)
		self.buttonDict[localeInfo.TARGET_BUTTON_DISMOUNT].SAFE_SetEvent(self.__OnDismount)
		self.buttonDict[localeInfo.TARGET_BUTTON_EXIT_OBSERVER].SAFE_SetEvent(self.__OnExitObserver)
		self.buttonDict[localeInfo.TARGET_BUTTON_VIEW_EQUIPMENT].SAFE_SetEvent(self.__OnViewEquipment)
		self.buttonDict[localeInfo.TARGET_BUTTON_REQUEST_ENTER_PARTY].SAFE_SetEvent(self.__OnRequestParty)
		self.buttonDict[localeInfo.TARGET_BUTTON_BUILDING_DESTROY].SAFE_SetEvent(self.__OnDestroyBuilding)
		self.buttonDict[localeInfo.TARGET_BUTTON_EMOTION_ALLOW].SAFE_SetEvent(self.__OnEmotionAllow)

		self.infoButton = infoButton
		self.name = name
		
		self.hpGauge = hpGauge
		self.hpPoisonGauge = hpPoisonGauge
		self.hpBurnGauge = hpBurnGauge

		self.hpDmgGauge = hpDmgGauge
		self.closeButton = closeButton
		self.nameString = 0
		self.nameLength = 0
		self.vid = 0
		self.vnum = 0
		self.eventWhisper = None
		self.isShowButton = False
		if app.ENABLE_VIEW_ELEMENT:
			self.elementImage = None
			self.toolTip = uiToolTip.ToolTip()
			self.toolTip.HideToolTip()

		if constInfo.NEW_TARGET_UI:
			self.tooltipHP = self.TextToolTip()

			self.cirleBGImg = ui.ImageBox()
			self.cirleBGImg.LoadImage("d:/ymir work/ui/new_target/circle_bg.tga")
			self.cirleBGImg.SetParent(self)
			self.cirleBGImg.SetWindowVerticalAlignCenter()
			self.cirleBGImg.SetPosition(-50, 0)

			self.cirleHPImg = ui.ImageBox()
			self.cirleHPImg.SetParent(self.cirleBGImg)
			self.cirleHPImg.SetPosition(0, 0)
			self.cirleHPImg.Show()

			self.cirleRaceImg = ui.ImageBox()
			self.cirleRaceImg.SetParent(self.cirleBGImg)
			self.cirleRaceImg.SetPosition(0, 0)
			self.cirleRaceImg.Show()

		self.__Initialize()
		self.ResetTargetBoard()

	def __del__(self):
		CLASS_THINBOARD.__del__(self)

		print "===================================================== DESTROYED TARGET BOARD"

	def __Initialize(self):
		self.nameString = ""
		self.nameLength = 0
		self.vid = 0
		self.vnum = 0
		self.isShowButton = False
		if app.ENABLE_VIEW_ELEMENT:
			self.elementImage = None
			self.toolTip.HideToolTip()

	def Destroy(self):
		self.eventWhisper = None
		self.closeButton = None
		self.showingButtonList = None
		self.infoButton = None
		self.buttonDict = None
		self.name = None
		self.hpGauge = None
		self.hpPoisonGauge = None
		self.hpBurnGauge = None
		self.hpDmgGauge = None
		self.__Initialize()
		if app.ENABLE_VIEW_ELEMENT:
			self.elementImage = None

			self.toolTip.HideToolTip()
			self.toolTip = None
			
		if constInfo.NEW_TARGET_UI:
			self.cirleBGImg = None
			self.cirleHPImg = None
			self.cirleRaceImg = None
			self.tooltipHP = None

	def OnPressedCloseButton(self):
		player.ClearTarget()
		self.Close()

	def RefreshMonsterInfoBoard(self):
		if not self.infoButton.showWnd.IsShow():
			return

		self.infoButton.showWnd.Refresh()

	def OnPressedInfoButton(self):
		if self.infoButton.showWnd.IsShow():
			self.infoButton.showWnd.Close()
		elif self.vnum != 0:
			if constInfo.MONSTER_INFO_DATA.has_key(self.vnum):
				data = constInfo.MONSTER_INFO_DATA[self.vnum]
				if data["recv"] == False and app.GetTime() - data["recv_time"] > 5:
					del constInfo.MONSTER_INFO_DATA[self.vnum]

			if not constInfo.MONSTER_INFO_DATA.has_key(self.vnum):
				constInfo.MONSTER_INFO_DATA[self.vnum] = {"recv":False,"recv_time":app.GetTime(),"items":[]}
				net.SendTargetMonsterDropInfo(self.vnum)

			self.infoButton.showWnd.Open(self, self.vnum)

	def Close(self):
		self.__Initialize()
		self.infoButton.showWnd.Close()
		self.Hide()
		
	def IsHideName(self, name):
		hiddenNames = ["'s Ditto", "(Ditto)", "'s Buffi", "(Buffi)", "'s Heilerin", "(Heilerin)"]
		for hiddenName in hiddenNames:
			if hiddenName in name:
				return True
		return False

	def Open(self, vid, name):
		if self.IsHideName(name):
			self.Hide()
			return


		if not constInfo.GET_VIEW_OTHER_EMPIRE_PLAYER_TARGET_BOARD():
			if not player.IsSameEmpire(vid):
				self.Hide()
				return

		if vid != self.GetTargetVID():
			self.ResetTargetBoard()
			self.SetTargetVID(vid)
			self.SetTargetName(name)

		if player.IsMainCharacterIndex(vid):
			self.__ShowMainCharacterMenu()			
		elif chr.INSTANCE_TYPE_BUILDING == chr.GetInstanceType(self.vid):
			self.Hide()
		else:
			self.RefreshButton()
			self.Show()
	
	def Refresh(self):
		if self.IsShow():
			if self.IsShowButton():			
				self.RefreshButton()		

	def RefreshByVID(self, vid):
		if vid == self.GetTargetVID():			
			self.Refresh()
			
	def RefreshByName(self, name):
		if name == self.GetTargetName():
			self.Refresh()

	def __ShowMainCharacterMenu(self):
		canShow=0

		self.HideAllButton()

		if player.IsMountingHorse():
			self.__ShowButton(localeInfo.TARGET_BUTTON_DISMOUNT)
			canShow=1

		if player.IsObserverMode():
			self.__ShowButton(localeInfo.TARGET_BUTTON_EXIT_OBSERVER)
			canShow=1

		if canShow:
			self.__ArrangeButtonPosition()
			self.Show()
		else:
			self.Hide()

	def SetWhisperEvent(self, event):
		self.eventWhisper = event

	def UpdatePosition(self):
		if constInfo.NEW_TARGET_UI:
			self.SetPosition(wndMgr.GetScreenWidth()/2 - self.GetWidth()/2 + 25, 20)
		else:
			self.SetPosition(wndMgr.GetScreenWidth()/2 - self.GetWidth()/2, 10)
		self.RefreshElementPos()

	def ResetTargetBoard(self):

		for btn in self.buttonDict.values():
			btn.Hide()

		self.__Initialize()

		self.name.SetPosition(0, 13)
		self.name.SetHorizontalAlignCenter()
		self.name.SetWindowHorizontalAlignCenter()

		self.hpGauge.Hide()
		self.hpGauge.hpText.Hide()

		self.hpPoisonGauge.Hide( )
		self.hpBurnGauge.Hide( )

		self.hpDmgGauge.Hide()
		if app.ENABLE_VIEW_ELEMENT and self.elementImage:
			self.elementImage = None
			self.toolTip.HideToolTip()
		self.infoButton.Hide()
		self.infoButton.showWnd.Close()

		self.SetSize(250, 40)
		self.RefreshElementPos()

		# tchat("HideInfo On Reset")

	def RefreshElementPos(self):
		if app.ENABLE_VIEW_ELEMENT and self.elementImage and self.elementImage.IsShow():
			self.elementImage.SetPosition(self.GetGlobalPosition()[0] - 2 - self.elementImage.GetWidth(), self.GetGlobalPosition()[1] + self.GetHeight() / 2 - self.elementImage.GetHeight() / 2)
		
	if app.ENABLE_VIEW_ELEMENT:
		def SetElementImage(self,elementId = -1):
			if elementId == -1:
				return
				
			if elementId > 0 and elementId in ELEMENT_IMAGE_DIC.keys():
				self.elementImage = ui.ImageBox()
				self.elementImage.LoadImage("d:/ymir work/ui/game/12zi/element/%s.sub" % (ELEMENT_IMAGE_DIC[elementId]))
				self.elementImage.SAFE_SetStringEvent("MOUSE_OVER_IN", self.ShowElementToolTip)
				self.elementImage.SAFE_SetStringEvent("MOUSE_OVER_OUT", self.toolTip.HideToolTip)
				self.elementImage.elementId = elementId
				self.elementImage.Show()
				self.RefreshElementPos()

		def ShowElementToolTip(self):
			self.toolTip.ClearToolTip()
			self.toolTip.toolTipWidth = self.toolTip.AppendTextLine(ELEMENT_NAME_DIC[self.elementImage.elementId]).GetTextSize()[0] + 20
			self.toolTip.AlignHorizonalCenter()
			self.toolTip.ShowToolTip()
				
	def SetTargetVID(self, vid):
		self.vid = vid
		self.vnum = 0

	def SetEnemyVID(self, vid):
		self.SetTargetVID(vid)

		name = chr.GetNameByVID(vid)
		vnum = nonplayer.GetRaceNumByVID(vid)
		level = nonplayer.GetLevelByVID(vid)
		grade = nonplayer.GetGradeByVID(vid)

		if test_server:
			name = "%s(%d)" % (name, vnum)

		nameFront = ""
		if -1 != level:
			nameFront += "Lv." + str(level) + " "
		if self.GRADE_NAME.has_key(grade):
			nameFront += "(" + self.GRADE_NAME[grade] + ") "

		self.SetTargetName(nameFront + name)

		self.vnum = vnum
		self.infoButton.Show()

	def GetTargetVID(self):
		return self.vid

	def GetTargetName(self):
		return self.nameString

	def SetTargetName(self, name):
		self.nameString = name
		self.nameLength = len(name)
		self.name.SetText(name)

	def SetHP(self, hpPercentage):
		if not self.hpGauge.IsShow():
			self.name.SetPosition(23, 13)
			self.name.SetWindowHorizontalAlignLeft()
			self.name.SetHorizontalAlignLeft()
			self.hpGauge.Show()
			self.hpGauge.hpText.Show()
			self.SetSize(200 + 7*self.nameLength, self.GetHeight())
			self.UpdatePosition()

		if self.hpDmgGauge.IsShow():
			dif = self.hpDmgGauge.GetPercentage()[0] - hpPercentage
			if dif > 0:
				self.hpDmgGauge.SetPercentage(self.hpGauge.GetPercentage()[0], self.hpGauge.GetPercentage()[1])
				self.hpDmgGauge.updateInterval = 0.75 / float(dif)
				self.hpDmgGauge.nextUpdate = app.GetTime() + self.hpDmgGauge.updateInterval
		else:
			self.hpDmgGauge.SetPercentage(hpPercentage, 100)
			self.hpDmgGauge.Show()

		self.hpGauge.SetPercentage(hpPercentage, 100)
		self.hpGauge.hpText.SetText(str(hpPercentage) + "%")

		self.hpPoisonGauge.SetPercentage(hpPercentage, 100)
		self.hpBurnGauge.SetPercentage(hpPercentage, 100)

		if constInfo.NEW_TARGET_UI:
			self.cirleBGImg.Hide()
			self.SetPosition(wndMgr.GetScreenWidth()/2 - self.GetWidth()/2, 10)

	def ShowDefaultButton(self):
		self.isShowButton = True
		self.showingButtonList.append(self.buttonDict[localeInfo.TARGET_BUTTON_WHISPER])
		self.showingButtonList.append(self.buttonDict[localeInfo.TARGET_BUTTON_EXCHANGE])
		self.showingButtonList.append(self.buttonDict[localeInfo.TARGET_BUTTON_FIGHT])
		self.showingButtonList.append(self.buttonDict[localeInfo.TARGET_BUTTON_EMOTION_ALLOW])
		for button in self.showingButtonList:
			button.Show()

	def HideAllButton(self):
		self.isShowButton = False
		if app.ENABLE_VIEW_ELEMENT:
			self.elementImage = None
			self.toolTip.HideToolTip()
		for button in self.showingButtonList:
			button.Hide()
		self.showingButtonList = []

	def __ShowButton(self, name):

		if not self.buttonDict.has_key(name):
			return

		self.buttonDict[name].Show()
		self.showingButtonList.append(self.buttonDict[name])

	def __HideButton(self, name):

		if not self.buttonDict.has_key(name):
			return

		button = self.buttonDict[name]
		button.Hide()

		for btnInList in self.showingButtonList:
			if btnInList == button:
				self.showingButtonList.remove(button)
				break

	def OnWhisper(self):
		if None != self.eventWhisper:
			self.eventWhisper(self.nameString)

	def OnExchange(self):
		net.SendExchangeStartPacket(self.vid)

	def OnPVP(self):
		net.SendChatPacket("/pvp %d" % (self.vid))

	def OnAppendToMessenger(self):
		net.SendMessengerAddByVIDPacket(self.vid)
		
	# if app.ENABLE_MESSENGER_BLOCK:
	# 	def OnAppendToBlockMessenger(self):
	# 		net.SendMessengerAddBlockByVIDPacket(self.vid)
	# 	def OnRemoveToBlockMessenger(self):
	# 		messenger.RemoveBlock(constInfo.ME_KEY)
	# 		net.SendMessengerRemoveBlockPacket(constInfo.ME_KEY, chr.GetNameByVID(self.vid))

	def OnPartyInvite(self):
		net.SendPartyInvitePacket(self.vid)

	def OnPartyExit(self):
		net.SendPartyExitPacket()

	def OnPartyRemove(self):
		net.SendPartyRemovePacket(self.vid)

	def __OnGuildAddMember(self):
		net.SendGuildAddMemberPacket(self.vid)

	def __OnDismount(self):
		net.SendChatPacket("/unmount")

	def __OnExitObserver(self):
		net.SendChatPacket("/observer_exit")

	def __OnViewEquipment(self):
		net.SendChatPacket("/view_equip " + str(self.vid))

	def __OnRequestParty(self):
		net.SendChatPacket("/party_request " + str(self.vid))

	def __OnDestroyBuilding(self):
		net.SendChatPacket("/build d %d" % (self.vid))

	def __OnEmotionAllow(self):
		net.SendChatPacket("/emotion_allow %d" % (self.vid))

	def OnPressEscapeKey(self):
		self.OnPressedCloseButton()
		return True

	def IsShowButton(self):
		return self.isShowButton

	def RefreshButton(self):
		self.HideAllButton()

		if chr.INSTANCE_TYPE_BUILDING == chr.GetInstanceType(self.vid):
			#self.__ShowButton(localeInfo.TARGET_BUTTON_BUILDING_DESTROY)
			#self.__ArrangeButtonPosition()
			return
		
		if player.IsPVPInstance(self.vid) or player.IsObserverMode():
			# PVP_INFO_SIZE_BUG_FIX
			self.SetSize(200 + 7*self.nameLength, 40)
			self.UpdatePosition()
			# END_OF_PVP_INFO_SIZE_BUG_FIX			
			return	

		self.ShowDefaultButton()

		if guild.MainPlayerHasAuthority(guild.AUTH_ADD_MEMBER):
			if not guild.IsMemberByName(self.nameString):
				if 0 == chr.GetGuildID(self.vid):
					self.__ShowButton(localeInfo.TARGET_BUTTON_INVITE_GUILD)

		if not messenger.IsFriendByName(self.nameString):
			self.__ShowButton(localeInfo.TARGET_BUTTON_FRIEND)

		# if app.ENABLE_MESSENGER_BLOCK and not str(self.nameString)[0] == "[":
		# 	if not messenger.IsBlockByName(self.nameString):
		# 		self.__ShowButton(localeInfo.TARGET_BUTTON_BLOCK)
		# 		self.__HideButton(localeInfo.TARGET_BUTTON_UNBLOCK)
		# 	else:
		# 		self.__ShowButton(localeInfo.TARGET_BUTTON_UNBLOCK)
		# 		self.__HideButton(localeInfo.TARGET_BUTTON_BLOCK)

		if player.IsPartyMember(self.vid):

			self.__HideButton(localeInfo.TARGET_BUTTON_FIGHT)

			if player.IsPartyLeader(self.vid):
				self.__ShowButton(localeInfo.TARGET_BUTTON_LEAVE_PARTY)
			elif player.IsPartyLeader(player.GetMainCharacterIndex()):
				self.__ShowButton(localeInfo.TARGET_BUTTON_EXCLUDE)

		else:
			if player.IsPartyMember(player.GetMainCharacterIndex()):
				if player.IsPartyLeader(player.GetMainCharacterIndex()):
					self.__ShowButton(localeInfo.TARGET_BUTTON_INVITE_PARTY)
			else:
				if chr.IsPartyMember(self.vid):
					self.__ShowButton(localeInfo.TARGET_BUTTON_REQUEST_ENTER_PARTY)
				else:
					self.__ShowButton(localeInfo.TARGET_BUTTON_INVITE_PARTY)

			if player.IsRevengeInstance(self.vid):
				self.__HideButton(localeInfo.TARGET_BUTTON_FIGHT)
				self.__ShowButton(localeInfo.TARGET_BUTTON_AVENGE)
			elif player.IsChallengeInstance(self.vid):
				self.__HideButton(localeInfo.TARGET_BUTTON_FIGHT)
				self.__ShowButton(localeInfo.TARGET_BUTTON_ACCEPT_FIGHT)
			elif player.IsCantFightInstance(self.vid):
				self.__HideButton(localeInfo.TARGET_BUTTON_FIGHT)

			if not player.IsSameEmpire(self.vid):
				self.__HideButton(localeInfo.TARGET_BUTTON_INVITE_PARTY)
				# self.__HideButton(localeInfo.TARGET_BUTTON_FRIEND)
				self.__HideButton(localeInfo.TARGET_BUTTON_FIGHT)

		distance = player.GetCharacterDistance(self.vid)
		if distance > self.EXCHANGE_LIMIT_RANGE:
			self.__HideButton(localeInfo.TARGET_BUTTON_EXCHANGE)
			self.__ArrangeButtonPosition()

		self.__ArrangeButtonPosition()

	def __ArrangeButtonPosition(self):
		showingButtonCount = len(self.showingButtonList)
		
		if constInfo.NEW_TARGET_UI:
			pos = (-(showingButtonCount / 2) * 96) + 5
			if 0 == showingButtonCount % 2:
				pos += 44

			for button in self.showingButtonList:
				button.SetPosition(pos, 33)
				pos += 96

			self.SetSize(showingButtonCount * 103 + 10, 65)
		else:
			pos = -(showingButtonCount / 2) * 68
			if 0 == showingButtonCount % 2:
				pos += 34

			for button in self.showingButtonList:
				button.SetPosition(pos, 33)
				pos += 68

			self.SetSize(max(150, showingButtonCount * 75), 65)

		self.UpdatePosition()

	def IsTargetBurning( self ):
		return chrmgr.HasAffectByVID( self.GetTargetVID( ), chr.AFFECT_FIRE ) != 0

	def IsTargetPoisoned( self  ):
		return chrmgr.HasAffectByVID( self.GetTargetVID( ), chr.AFFECT_POISON ) != 0

	def OnUpdate(self):

		if constInfo.NEW_HP_EFFECTS and self.hpGauge and self.hpGauge.IsShow( ):

			isBurning = self.IsTargetBurning( )
			isPoisoned = self.IsTargetPoisoned( )

			# hpTextContent = self.hpGauge.hpText.GetText( )
			# hpPercentage = self.hpGauge.GetPercentage( )[ 0 ]

			# burning only
			if isBurning and not isPoisoned:
				self.hpBurnGauge.Show( )
				self.hpPoisonGauge.Hide( )

			# poisoned only
			if isPoisoned and not isBurning:
				self.hpBurnGauge.Hide( )
				self.hpPoisonGauge.Show( )

			# both -> poison should have priority imo
			if isPoisoned and isBurning:
				self.hpBurnGauge.Hide( )
				self.hpPoisonGauge.Show( )

			# no effects
			if not isPoisoned and not isBurning:
				self.hpBurnGauge.Hide( )
				self.hpPoisonGauge.Hide( )
				
		if self.hpDmgGauge and self.hpDmgGauge.IsShow() and self.hpDmgGauge.nextUpdate <= app.GetTime():
			dif = self.hpDmgGauge.GetPercentage()[0] - self.hpGauge.GetPercentage()[0]
			if dif > 0:
				val = max(1, int(dif / 3))
				self.hpDmgGauge.nextUpdate = app.GetTime() + self.hpDmgGauge.updateInterval
				self.hpDmgGauge.SetPercentage(self.hpDmgGauge.GetPercentage()[0] - val, self.hpDmgGauge.GetPercentage()[1])

		if self.isShowButton:

			exchangeButton = self.buttonDict[localeInfo.TARGET_BUTTON_EXCHANGE]
			distance = player.GetCharacterDistance(self.vid)

			if distance < 0:
				return

			if exchangeButton.IsShow():
				if distance > self.EXCHANGE_LIMIT_RANGE:
					self.RefreshButton()

			else:
				if distance < self.EXCHANGE_LIMIT_RANGE:
					self.RefreshButton()

		if constInfo.NEW_TARGET_UI:
			if self.cirleBGImg.IsShow():
				if self.IsTargetPoisoned():
					self.cirleHPImg.LoadImage("d:/ymir work/ui/new_target/circle_green.tga")
				elif self.IsTargetBurning():
					self.cirleHPImg.LoadImage("d:/ymir work/ui/new_target/circle_orange.tga")
				else:
					self.cirleHPImg.LoadImage("d:/ymir work/ui/new_target/circle_red.tga")

				radius = 39
				mouse = mouseModule.mouseController
				x, y = self.cirleBGImg.GetGlobalPosition()
				posX = mouse.x - (x + radius)
				posY = mouse.y - (y + radius)

				if pow(posX, 2) + pow(posY, 2) <= pow(radius, 2):
					self.tooltipHP.Show()
				else:
					self.tooltipHP.Hide()

	if constInfo.NEW_TARGET_UI:
		def SetTargetHP(self, hp, isPC, curHP, maxHP):
			if isPC:
				self.cirleBGImg.Show()
				self.cirleHPImg.DisplayProcent(hp)
				self.cirleRaceImg.LoadImage("d:/ymir work/ui/new_target/circle_%d.tga" % nonplayer.GetRaceNumByVID(self.vid))
			else:
				self.cirleBGImg.Hide()

			self.tooltipHP.SetText("%s : %d / %d" % (localeInfo.TASKBAR_HP, curHP, maxHP))
