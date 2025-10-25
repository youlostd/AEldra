import ui
import chat
import time
import net
import uiScriptLocale
import localeInfo
import math
import item
import uiToolTip

class Table(ui.ScriptWindow):
	def __init__(self):
		ui.ScriptWindow.__init__(self)
		self.children = []
	
		self.betAmountWnd = None
		self.betAmountBackground = None
		self.betAmountText = None
		self.betAmountName = None
		self.betAmountMinus = None
		self.betAmountPlus = None
		self.betAmountValues = [10,25,50]
		self.betAmountValueIndex = 0

		self.pointsPCLabel = None
		self.pointsNPCLabel = None
		
		self.currentFadeImage = None
		self.currentFadeImageIsShowed = False
		self.currentFadeDisappearAfter = 0
		#self.currentFadeImageAnimationSpeedDelay = 0

		self.itemToolTip = uiToolTip.ItemToolTip()
		self.itemToolTip.HideToolTip()

		self.popupQueue = []
		self.cardQueue = []
		self.cardAnimationRunning = False
		self.cards_animation_target = [0,0,None,0, 0]
		self.cards_animation_data = []
		self.cardsOnTable = {0:[], 1:[]}
		self.points = [0, 0]

		self.__LoadWindow()

	def __del__(self):
		ui.ScriptWindow.__del__(self)

	def ResetGame(self):
		self.cardQueue = []
		self.popupQueue = []
		for player in self.cardsOnTable:
			for card in self.cardsOnTable[player]:
				card.Hide()
			del self.cardsOnTable[player][:]

		self.points = [0, 0]
		self.cardAnimationRunning = False
		self.cards_animation_target = [0, 0, None, 0, 0]
		self.cards_animation_data = []
		self.pointsPCLabel.SetText(uiScriptLocale.BLACKJACK_YOU)
		self.pointsNPCLabel.SetText(uiScriptLocale.BLACKJACK_DEALER)
		self.ChangeStatus(0)

	def __LoadWindow(self):
		try:
			pyScrLoader = ui.PythonScriptLoader()
			pyScrLoader.LoadScriptFile(self, "uiscript/blackjack.py")
		except:
			import exception
			exception.Abort("uiBlackJack.LoadWindow")

		self.board = self.GetChild("board")
		self.board.AddFlag("attach")

		self.background = self.GetChild("background")
		self.background.AddFlag("attach")

		self.stayButton = self.GetChild("stopButton")
		self.stayButton.SetTextColor(0xffFFFFFF)
		self.stayButton.SAFE_SetEvent(self.Stay)
		self.stayButton.Show()

		self.hitButton = self.GetChild("confirmButton")
		self.hitButton.SetTextColor(0xffFFFFFF)
		self.hitButton.SAFE_SetEvent(self.Hit)
		self.hitButton.Show()

		self.startButton = self.GetChild("startButton")
		self.startButton.SetTextColor(0xffFFFFFF)
		self.startButton.SAFE_SetEvent(self.StartGame)
		self.startButton.Show()

		## Bet Amount
		betBtnWidth = 40
		betBtnHeight = 48
		betBackgroundWidth = 86 - 45

		self.betAmountWnd = ui.Window()
		self.betAmountWnd.SetSize(betBtnWidth+betBackgroundWidth+betBtnWidth,betBtnHeight)
		self.betAmountWnd.SetParent(self.board)
		self.betAmountWnd.SetWindowVerticalAlignBottom()
		self.betAmountWnd.SetPosition(8,100)
		self.betAmountWnd.Show()

		self.betAmountBackground = ui.ImageBox()
		self.betAmountBackground.SetParent(self.betAmountWnd)
		self.betAmountBackground.LoadImage("d:/ymir work/ui/game/blackjack/bet_amount2.tga")
		self.betAmountBackground.SetWindowHorizontalAlignCenter()
		self.betAmountBackground.SetWindowVerticalAlignCenter()
		self.betAmountBackground.SetPosition(0,0)
		self.betAmountBackground.Show()

		item.SelectItem(1, 2, 95221)
		self.betRewardItem = ui.ImageBox()
		self.betRewardItem.SetParent(self.board)
		self.betRewardItem.SetWindowHorizontalAlignCenter()
		self.betRewardItem.SAFE_SetStringEvent("MOUSE_OVER_IN", self.__ShowToolTip)
		self.betRewardItem.SAFE_SetStringEvent("MOUSE_OVER_OUT", self.itemToolTip.HideToolTip)
		self.betRewardItem.LoadImage(item.GetIconImageFileName())
		self.betRewardItem.SetWindowVerticalAlignCenter()
		self.betRewardItem.SetPosition(-141,150)
		self.betRewardItem.Show()


		#todo label add..
		self.betRewardText = ui.TextLine()
		self.betRewardText.SetParent(self.board)
		self.betRewardText.SetText(localeInfo.QUEST_TIMER_REWARDS)
		self.betRewardText.SetWindowHorizontalAlignCenter()
		self.betRewardText.SetHorizontalAlignCenter()
		self.betRewardText.SetWindowVerticalAlignCenter()
		self.betRewardText.SetVerticalAlignCenter()
		self.betRewardText.SetPosition(-130,130)
		self.betRewardText.SetPackedFontColor(0xffFFFFFF)
		self.betRewardText.SetOutline()
		self.betRewardText.Show()


		self.betAmountText = ui.TextLine()
		self.betAmountText.SetParent(self.betAmountBackground)
		self.betAmountText.SetText(self.betAmountValues[self.betAmountValueIndex])
		self.betAmountText.SetWindowHorizontalAlignCenter()
		self.betAmountText.SetHorizontalAlignCenter()
		self.betAmountText.SetWindowVerticalAlignCenter()
		self.betAmountText.SetVerticalAlignCenter()
		self.betAmountText.SetPosition(0,-1)
		self.betAmountText.SetPackedFontColor(0xffFFFFFF)
		self.betAmountText.SetOutline()
		self.betAmountText.Show()

		self.betAmountName = ui.TextLine()
		self.betAmountName.SetParent(self.betAmountWnd)
		self.betAmountName.SetText(uiScriptLocale.BLACKJACK_BET)
		self.betAmountName.SetPosition(0,-6)
		self.betAmountName.SetWindowHorizontalAlignCenter()
		self.betAmountName.SetHorizontalAlignCenter()
		self.betAmountName.SetPackedFontColor(0xffFFFFFF)
		self.betAmountName.SetOutline()
		self.betAmountName.Show()

		self.betAmountMinus = ui.Button()
		self.betAmountMinus.SetParent(self.betAmountWnd)
		self.betAmountMinus.SetSize(47,48)
		self.betAmountMinus.SetUpVisual("d:/ymir work/ui/game/blackjack/btn_minus_normal.tga")
		self.betAmountMinus.SetOverVisual("d:/ymir work/ui/game/blackjack/btn_minus_hover.tga")
		self.betAmountMinus.SetDownVisual("d:/ymir work/ui/game/blackjack/btn_minus_down.tga")
		self.betAmountMinus.SetWindowVerticalAlignCenter()
		self.betAmountMinus.SetPosition(0,0)
		self.betAmountMinus.Show()
		self.betAmountMinus.SAFE_SetEvent(self.DecreaseBetValue)

		self.betAmountPlus = ui.Button()
		self.betAmountPlus.SetParent(self.betAmountWnd)
		self.betAmountPlus.SetSize(47,48)
		self.betAmountPlus.SetUpVisual("d:/ymir work/ui/game/blackjack/btn_plus_normal.tga")
		self.betAmountPlus.SetOverVisual("d:/ymir work/ui/game/blackjack/btn_plus_hover.tga")
		self.betAmountPlus.SetDownVisual("d:/ymir work/ui/game/blackjack/btn_plus_down.tga")
		self.betAmountPlus.SetWindowVerticalAlignCenter()
		self.betAmountPlus.SetPosition(betBtnWidth+betBackgroundWidth-8,0)
		self.betAmountPlus.Show()
		self.betAmountPlus.SAFE_SetEvent(self.IncreaseBetValue)

		self.pointsPCLabel = ui.TextLine()
		self.pointsPCLabel.SetParent(self.board)
		self.pointsPCLabel.SetText(uiScriptLocale.BLACKJACK_YOU)
		self.pointsPCLabel.SetWindowHorizontalAlignCenter()
		self.pointsPCLabel.SetHorizontalAlignCenter()
		self.pointsPCLabel.SetWindowVerticalAlignBottom()
		self.pointsPCLabel.SetPosition(0,120)
		self.pointsPCLabel.SetHorizontalAlignCenter()
		self.pointsPCLabel.SetPackedFontColor(0xffFFFFFF)
		self.pointsPCLabel.SetOutline()
		self.pointsPCLabel.Show()

		self.pointsNPCLabel = ui.TextLine()
		self.pointsNPCLabel.SetParent(self.board)
		self.pointsNPCLabel.SetText(uiScriptLocale.BLACKJACK_DEALER)
		self.pointsNPCLabel.SetWindowHorizontalAlignCenter()
		self.pointsNPCLabel.SetHorizontalAlignCenter()
		self.pointsNPCLabel.SetPosition(0,45)
		self.pointsNPCLabel.SetHorizontalAlignCenter()
		self.pointsNPCLabel.SetPackedFontColor(0xffFFFFFF)
		self.pointsNPCLabel.SetOutline()
		self.pointsNPCLabel.Show()

		self.btnClose = ui.Button()
		self.btnClose.SetParent(self.board)
		self.btnClose.SetSize(23,24)
		self.btnClose.SetUpVisual("d:/ymir work/ui/game/blackjack/btn_x_normal.tga")
		self.btnClose.SetOverVisual("d:/ymir work/ui/game/blackjack/btn_x_hover.tga")
		self.btnClose.SetDownVisual("d:/ymir work/ui/game/blackjack/btn_x_down.tga")
		self.btnClose.SetEvent(ui.__mem_func__(self.Close))	
		self.btnClose.SetToolTipText(localeInfo.UI_CLOSE, 0, -23)
		self.btnClose.SetPosition(self.GetWidth() - self.btnClose.GetWidth() - 3 - 25 + 6, 3 + 5 - 2)
		self.btnClose.Show()

		self.btnForum = ui.Button()
		self.btnForum.SetParent(self.board)
		self.btnForum.SetUpVisual("d:/ymir work/ui/public/Large_Button_01.sub")
		self.btnForum.SetOverVisual("d:/ymir work/ui/public/Large_Button_02.sub")
		self.btnForum.SetDownVisual("d:/ymir work/ui/public/Large_Button_03.sub")
		self.btnForum.SetEvent(ui.__mem_func__(self.OpenForum))	
		self.btnForum.SetText("Forum")
		self.btnForum.SetWindowHorizontalAlignCenter()
		self.btnForum.SetWindowVerticalAlignBottom()
		self.btnForum.SetPosition(150, 35)
		self.btnForum.Show()

		self.ChangeStatus(0)

	def __ShowToolTip(self):
		self.itemToolTip.SetItemToolTip(95221 + self.betAmountValueIndex)

	def GenerateGradientTriangle(self, x1, y1, x2, y2):
		distX = x2 - x1
		distY = y2 - y1
		if math.sqrt(distX*distX) >= math.sqrt(distY*distY):
			if distX > 0:
				factor = float(distY) / float(distX)
				for i in range(distX + 1):
					self.cards_animation_data.append([x1 + i, y1 + i * factor])
			elif distX <0:
				factor = float(distY) / float(distX)
				for i in range((-1) * distX + 1):
					self.cards_animation_data.append([x1 - i, y1 - i * factor])
		elif math.sqrt(distX*distX) < math.sqrt(distY*distY):
			if distY > 0 :
				factor = float(distX) / float(distY)
				for i in range(distY + 1):
					self.cards_animation_data.append([x1 + i * factor, y1 + i])
			elif distY < 0:
				factor = float(distX) / float(distY)
				for i in range((-1) * distY + 1):
					self.cards_animation_data.append([x1 - i * factor, y1 - i])

	def OpenForum(self):
		from os import system
		system("start %s" % "https://%s/l/blackjack" % constInfo.DOMAIN)

	def StartGame(self):
		if self.cardAnimationRunning:
			return

		self.ResetGame()
		net.SendChatPacket('/blackjack %d' % self.betAmountValues[self.betAmountValueIndex])

	def Stay(self):
		if self.cardAnimationRunning:
			return

		net.SendChatPacket("/blackjack 0")

	def Hit(self):
		if self.cardAnimationRunning:
			return

		net.SendChatPacket("/blackjack 1")

	def IncreaseBetValue(self):
		curIndex = self.betAmountValueIndex
		valuesLen = len(self.betAmountValues) - 1

		self.betAmountMinus.SetUp()
		self.betAmountMinus.Enable()

		if curIndex < valuesLen:
			curIndex += 1
			item.SelectItem(1, 2, 95221 + curIndex)
			self.betRewardText.SetText(localeInfo.QUEST_TIMER_REWARDS)
			self.betRewardItem.LoadImage(item.GetIconImageFileName())
			self.itemToolTip.HideToolTip()

		if curIndex == valuesLen:
			self.betAmountPlus.Down()
			self.betAmountPlus.Disable()

		curIndex = min(valuesLen,curIndex)

		self.betAmountValueIndex = curIndex
		self.betAmountText.SetText(str(self.betAmountValues[self.betAmountValueIndex]))

	def DecreaseBetValue(self):
		curIndex = self.betAmountValueIndex
		valuesLen = len(self.betAmountValues) - 1

		self.betAmountPlus.SetUp()
		self.betAmountPlus.Enable()

		if curIndex > 0:
			curIndex -= 1
			item.SelectItem(1, 2, 95221 + curIndex)
			self.betRewardText.SetText(localeInfo.QUEST_TIMER_REWARDS)
			self.betRewardItem.LoadImage(item.GetIconImageFileName())
			self.itemToolTip.HideToolTip()


		if curIndex == 0:
			self.betAmountMinus.Down()
			self.betAmountMinus.Disable()

		curIndex = max(0,curIndex)

		self.betAmountValueIndex = curIndex
		self.betAmountText.SetText(str(self.betAmountValues[self.betAmountValueIndex]))

	def FadeImage(self, imageName):
		tchat("FadeImg %s" % imageName)
		self.currentFadeImageIsShowed = False
		self.currentFadeDisappearAfter = 0

		self.currentFadeImage = ui.ImageBox()
		if self.board:
			self.currentFadeImage.SetParent(self.board)

		if imageName == 'BUSTED':
			imageName = "d:/ymir work/ui/game/blackjack/popup_busted.tga"

		elif imageName == 'BLACKJACK':
			imageName = "d:/ymir work/ui/game/blackjack/popup_blackjack.tga"

		elif imageName in ('NORMAL'):
			imageName = "d:/ymir work/ui/game/blackjack/popup_won.tga"

		elif imageName in ('LOST'):
			imageName = "d:/ymir work/ui/game/blackjack/popup_lost.tga"

		elif imageName in ('DRAW'):
			imageName = "d:/ymir work/ui/game/blackjack/popup_push.tga"

		self.currentFadeImage.LoadImage(imageName)
		self.currentFadeImage.SetPosition(0,0)
		self.currentFadeImage.SetWindowHorizontalAlignCenter()
		self.currentFadeImage.SetWindowVerticalAlignCenter()
		self.currentFadeImage.Show()
		self.currentFadeImage.SetAlpha(0.0)

	def OnRender(self):
		if self.cardAnimationRunning:
			if self.cards_animation_target[2]:
				target_x = self.cards_animation_target[0]
				target_y = self.cards_animation_target[1]
				x,y = self.cards_animation_target[2].GetLocalPosition()
				if len(self.cards_animation_data) == 0 or (x==target_x and y==target_y):
					self.cardAnimationRunning = False
					self.hitButton.Enable()
					self.stayButton.Enable()
					self.DisplayPoints(self.cards_animation_target[3], self.cards_animation_target[4])
				else:
					new_pos = self.cards_animation_data.pop(0)
					if len(self.cards_animation_data)>1:
						self.cards_animation_data.pop(0)
					self.cards_animation_target[2].SetPosition(new_pos[0], new_pos[1])
		else:
			if not self.ProcessCardQueue():
				self.ProcessPopupQueue()

	def OnUpdate(self):
		if self.currentFadeImage and self.currentFadeImage.IsShow():
			howMuchToStay = 3.0
			incrementAlpha = 0.03
			curAlpha = self.currentFadeImage.GetAlpha()

			if not self.currentFadeImageIsShowed:
				if curAlpha < 1.0:
					self.currentFadeImage.SetAlpha(curAlpha + incrementAlpha)
				elif curAlpha >= 1.0:
					self.currentFadeDisappearAfter = time.clock() + howMuchToStay
					self.currentFadeImageIsShowed = True

			if self.currentFadeImageIsShowed:
				if time.clock() > self.currentFadeDisappearAfter:
					if curAlpha > 0.0:
						self.currentFadeImage.SetAlpha(curAlpha - incrementAlpha)
					elif curAlpha <= 0.0:
						self.currentFadeImage.Hide()

	def Close(self):
		ui.ScriptWindow.Hide(self)
		self.itemToolTip.HideToolTip()

	def Open(self):
		ui.ScriptWindow.Show(self)

	def AddPopupQueue(self, arg):
		self.popupQueue.append(arg)

	def ProcessPopupQueue(self):
		if len(self.popupQueue):
			self.FadeImage(self.popupQueue.pop(0))

	def AddCardToQueue(self, owner, card, cValue):
		self.cardQueue.append([owner, card, cValue])

	def ProcessCardQueue(self):
		if len(self.cardQueue):
			card = self.cardQueue.pop(0)
			self.AddCard(card[0], card[1], card[2])
			return True
		return False

	def AddCard(self, owner, card, cValue):
		myCard = ui.ImageBox()
		myCard.SetParent(self.background)
		myCard.AddFlag("attach")
		myCard.LoadImage("d:/ymir work/ui/game/blackjack/cards/%s.tga" % card)
		myCard.SetPosition(325, 56)
		myCard.Show()
		
		self.cards_animation_target[0] = 185 + (len(self.cardsOnTable[owner]) * 14)
		if owner == 1: # npc
			self.cards_animation_target[1] = 84 + 1
		elif owner == 0: # pc
			self.cards_animation_target[1] = 160 + 1

		self.cards_animation_target[2] = myCard
		self.cards_animation_target[3] = owner
		self.cards_animation_target[4] = cValue
		self.cardsOnTable[owner].append(myCard)
		self.GenerateGradientTriangle(325, 56, self.cards_animation_target[0], self.cards_animation_target[1])

		self.cardAnimationRunning = True
		self.hitButton.Disable()
		self.stayButton.Disable()

	def ChangeStatus(self, status):
		if status:
			self.hitButton.Show()
			self.stayButton.Show()
			self.startButton.Hide()
		else:
			self.hitButton.Hide()
			self.stayButton.Hide()
			self.startButton.Show()

	def ReceiveInfo(self, type, arg1, arg2, arg3, arg4):
		if type == 'CARD':
			#player = int(arg1)-1
			#self.points[player] += int(arg3)

			# label = self.pointsNPCLabel if player == 1 else self.pointsPCLabel
			# label.SetText("%s: %s" % 
			# 	(uiScriptLocale.BLACKJACK_DEALER if player==1 else uiScriptLocale.BLACKJACK_YOU, 
			# 		arg4))

			self.AddCardToQueue(int(arg1)-1, arg2, arg4) # arg3 card value
			self.ChangeStatus(1)

		elif type == 'WON':
			self.AddPopupQueue(arg1)
			self.ChangeStatus(0)
		elif type == 'LOST':
			self.AddPopupQueue("LOST")
			self.ChangeStatus(0)

	def DisplayPoints(self, owner, cValue):
		if not self.cardAnimationRunning:
			player = owner
			
			label = self.pointsNPCLabel if player == 1 else self.pointsPCLabel
			label.SetText("%s: %s" % 
				(uiScriptLocale.BLACKJACK_DEALER if player==1 else uiScriptLocale.BLACKJACK_YOU, cValue))

	def Destory(self):
		self.ClearDictionary()
		self.board = None
		self.background = None
		self.stayButton = None
		self.hitButton = None
		self.startButton = None
		self.betAmountWnd = None
		self.betAmountBackground = None
		self.betRewardItem = None
		self.betRewardText = None
		self.betAmountText = None
		self.betAmountName = None
		self.betAmountMinus = None
		self.betAmountPlus = None
		self.pointsPCLabel = None
		self.pointsNPCLabel = None
		self.btnClose = None
		self.btnForum = None
