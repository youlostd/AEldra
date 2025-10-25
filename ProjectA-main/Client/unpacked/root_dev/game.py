import os
import app
import dbg
import grp
import item
import background
import chr
import chrmgr
import player
import snd
import chat
import textTail
import snd
import net
import effect
import wndMgr
import fly
import systemSetting
import quest
import guild
import skill
import time
import messenger
import localeInfo
import constInfo
import exchange
import ime
import ui
import uiCommon
import uiPhaseCurtain
import uiMapNameShower
import uiAffectShower
import uiPlayerGauge
import uiCharacter
import uiTarget
import uiExchange
import uiPrivateShopBuilder
import mouseModule
import localeInfo
import playerSettingModule
import interfaceModule
import musicInfo
import stringCommander
import cfg
import sys
import safebox
import uiAuction
import uiGameOption
import uiNewGameOption
if constInfo.WHISPER_MANAGER:
	import whispermgr

from _weakref import proxy
if app.ENABLE_ZODIAC:
	import uiZodiac
	import ui12zirewardwindow
	import uizodiacanimasphere
	import uirankingzodiac

from datetime import datetime

from uiToolTip import GET_AFFECT_STRING

SCREENSHOT_CWDSAVE = False
SCREENSHOT_DIR = None

if localeInfo.IsEUROPE():
	SCREENSHOT_CWDSAVE = True

if localeInfo.IsCIBN10():
	SCREENSHOT_CWDSAVE = False
	SCREENSHOT_DIR = "YT2W"

cameraDistance = 1550.0
cameraPitch = 27.0
cameraRotation = 0.0
cameraHeight = 100.0

testAlignment = 0

class GameWindow(ui.ScriptWindow):
	canQuestLettersShow = 1
	def __init__(self, stream):
		ui.ScriptWindow.__init__(self, "GAME")
		self.SetWindowName("game")
		net.SetPhaseWindow(net.PHASE_WINDOW_GAME, self)
		player.SetGameWindow(self)

		self.quickSlotPageIndex = 0
		self.lastPKModeSendedTime = 0

		self.initTaskbarTime = app.GetTime()
		self.pressNumber = None
		if (app.COMBAT_ZONE):
			import uicombatzone
			self.wndCombatZone = uicombatzone.CombatZoneWindow()

		self.guildWarQuestionDialog = None
		self.interface = None
		self.targetBoard = None
		self.mapNameShower = None
		self.IngameStartTime = 0
		if app.ENABLE_RUNE_AFFECT_ICONS:
			self.affectImage = None
		self.playerGauge = None
		self.whisperOfflineQuestionDlg = None
		self.wndAuctionInformerBtn = None
		self.wndAuctionInformer = []
		self.reload_entityslast = 0
		self.confirmDungeonReconnect = None
		if app.ENABLE_ZODIAC:
			constInfo.ENABLE_ZODIAC_MINIMAP = 0
			constInfo.ZODIAC_CLOCK_1ST = 0
			self.uiZodiac = None
			self.ui12zirewardwindow = None
		self.executeDelayedList = [ ]

		self.cubeInformation = {}

		self.stream=stream
		self.bossHuntWindow = ui.ExpandedImageBox()
		self.bossHuntWindow.Hide()

		self.interface = interfaceModule.Interface()
		self.interface.MakeInterface()
		self.interface.ShowDefaultWindows()

		self.curtain = uiPhaseCurtain.PhaseCurtain()
		self.curtain.speed = 0.03
		self.curtain.Hide()

		self.targetBoard = uiTarget.TargetBoard()
		self.targetBoard.SetWhisperEvent(ui.__mem_func__(self.interface.OpenWhisperDialog))
		self.targetBoard.Hide()

		self.mapNameShower = uiMapNameShower.MapNameShower()
		self.affectShower = self.interface.wndAffect
		#self.affectShower = uiAffectShower.AffectShower()
		if app.ENABLE_ZODIAC:
			self.interface.ToggleAnimasphereWindow()
		if app.ENABLE_RUNE_AFFECT_ICONS:
			self.affectImage = uiAffectShower.AffectImage()

		self.playerGauge = uiPlayerGauge.PlayerGauge(self)
		self.playerGauge.Hide()

		self.__SetQuickSlotMode()

		self.__ServerCommand_Build()
		self.__ProcessPreservedServerCommand()
		self.MakeBossHuntWindow()

		if constInfo.WHISPER_MANAGER:
			whispermgr.SetGameWindow(self)
			if constInfo.IS_CHAT_CLEARED:
				if cfg.Get(cfg.SAVE_OPTION, "save_whisper", "1") == "1":
					whispermgr.Load()
				else:
					whispermgr.Clear()
				constInfo.IS_CHAT_CLEARED = False

		if (app.COMBAT_ZONE):
			self.combatzone = 0
			self.combatzone_last_flash = 0

		hideNPCIndexes = constInfo.HIDE_NPC_INDEXES
		for k,v in hideNPCIndexes.items():
			if int(cfg.Get(cfg.SAVE_OPTION, k, "0")) > 0:
				systemSetting.SetHideNPC(hideNPCIndexes[k], True)
			else:
				systemSetting.SetHideNPC(hideNPCIndexes[k], False)

	def __del__(self):
		player.SetGameWindow(0)
		net.ClearPhaseWindow(net.PHASE_WINDOW_GAME, self)
		ui.ScriptWindow.__del__(self)

	def OpenBossHuntTopic(self):
		app.ShellExecute(constInfo.URL["bosshunt"], False)
		
	def MakeBossHuntWindow(self):
		self.bossHuntWindow.LoadImage("d:/ymir work/ui/bosshunt_point_bg.tga")
		text = ui.TextLine()
		text.SetParent(self.bossHuntWindow)
		text.SetVerticalAlignCenter()
		text.SetFontName(localeInfo.UI_DEF_FONT_LARGE)
		text.SetText("Points: 0")
		text.SetPosition(69, 48)
		text.Show()
		self.bossHuntWindow.text = text

		if self.interface.wndTaskBar:
			pos = self.interface.wndTaskBar.GetGlobalPosition()
			self.bossHuntWindow.SetPosition(pos[0], pos[1] - self.bossHuntWindow.GetHeight())

		self.bossHuntWindow.SetStringEvent("MOUSE_LEFT_DOWN", self.OpenBossHuntTopic)

	def Open(self):
		app.SetFrameSkip(1)

		self.SetSize(wndMgr.GetScreenWidth(), wndMgr.GetScreenHeight())

		self.quickSlotPageIndex = 0
		self.PickingCharacterIndex = -1
		self.PickingItemIndex = -1
		self.ShowNameFlag = False

		self.enableXMasBoom = False
		self.startTimeXMasBoom = 0.0
		self.indexXMasBoom = 0
		self.hwid = None

		global cameraDistance, cameraPitch, cameraRotation, cameraHeight

		app.SetCamera(cameraDistance, cameraPitch, cameraRotation, cameraHeight)

		constInfo.SET_DEFAULT_CAMERA_MAX_DISTANCE()
		constInfo.SET_DEFAULT_CHRNAME_COLOR()
		constInfo.SET_DEFAULT_FOG_LEVEL()
		constInfo.SET_DEFAULT_CONVERT_EMPIRE_LANGUAGE_ENABLE()
		constInfo.SET_DEFAULT_USE_ITEM_WEAPON_TABLE_ATTACK_BONUS()
		constInfo.SET_DEFAULT_USE_SKILL_EFFECT_ENABLE()

		# TWO_HANDED_WEAPON_ATTACK_SPEED_UP
		constInfo.SET_TWO_HANDED_WEAPON_ATT_SPEED_DECREASE_VALUE()
		# END_OF_TWO_HANDED_WEAPON_ATTACK_SPEED_UP

		import event
		event.SetLeftTimeString(localeInfo.UI_LEFT_TIME)

		textTail.EnablePKTitle(constInfo.PVPMODE_ENABLE)

		self.__BuildKeyDict()

		# PRIVATE_SHOP_PRICE_LIST
		uiPrivateShopBuilder.Clear()
		# END_OF_PRIVATE_SHOP_PRICE_LIST

		# UNKNOWN_UPDATE
		exchange.InitTrading()
		# END_OF_UNKNOWN_UPDATE

		## Sound
		snd.SetMusicVolume(systemSetting.GetMusicVolume()*net.GetFieldMusicVolume())
		snd.SetSoundVolume(systemSetting.GetSoundVolume())

		netFieldMusicFileName = net.GetFieldMusicFileName()
		if netFieldMusicFileName:
			snd.FadeInMusic("BGM/" + netFieldMusicFileName)
		elif musicInfo.fieldMusic != "":						
			snd.FadeInMusic("BGM/" + musicInfo.fieldMusic)

		self.__SetQuickSlotMode()
		self.__SelectQuickPage(self.quickSlotPageIndex)

		self.SetFocus()
		self.Show()
		app.ShowCursor()

		app.MyShopDecoBGCreate()

		net.SendEnterGamePacket()

		self.wndAuctionInformerBtn = ui.Button()
		self.wndAuctionInformerBtn.SetPosition(175, 45)
		self.wndAuctionInformerBtn.SetWindowHorizontalAlignRight()
		# self.wndAuctionInformerBtn.SetUpVisual("d:/ymir work/ui/auction_informer_01.tga")
		# self.wndAuctionInformerBtn.SetOverVisual("d:/ymir work/ui/auction_informer_02.tga")
		# self.wndAuctionInformerBtn.SetDownVisual("d:/ymir work/ui/auction_informer_03.tga")
		self.wndAuctionInformerBtn.SAFE_SetEvent(self.OnClickAuctionInformerButton)
		self.wndAuctionInformerBtn.Hide()

		# START_GAME_ERROR_EXIT
		try:
			self.StartGame()
		except:
			import exception
			exception.Abort("GameWindow.Open")
		# END_OF_START_GAME_ERROR_EXIT

		if constInfo.ENABLE_NEW_VOTE_SYSTEM:
			app.WebNewVoteSystem()

		if constInfo.NEW_SWITCHBOT_ENABLED and self.interface.wndSwitchbot:
			self.interface.wndSwitchbot.OnRestartAfterTeleport()

		if constInfo.RELOGIN_SYSTEM_ENABLED:
			accountIndex = constInfo.RELOGIN_ACCOUNT_INDEX
			constInfo.RELOGIN_TRY_LOGIN = bool( accountIndex )
			constInfo.RELOGIN_LOGIN_WINDOW = False

			tchat( "(testserver) relogin: %s" % str( constInfo.RELOGIN_TRY_LOGIN )  )
			tchat( "(testserver) relogin account: %d" % accountIndex )

		self.IngameStartTime = app.GetTime()

		if constInfo.ENABLE_CHANGE_TEXTURE_SNOW:
			for i in xrange(10):
				if systemSetting.IsSnowTexturesMode():
					if background.GetCurrentMapName():
						snow_maps = [
							"outdoor/a1",
							"outdoor/b1",
							"outdoor/c1"
						]
						snow_maps_textures = {
							"outdoor/a1" : "textureset\metin2_a1_snow.txt",
							"outdoor/b1" : "textureset\metin2_b1_snow.txt",
							"outdoor/c1" : "textureset\metin2_c1_snow.txt", }
						if str(background.GetCurrentMapName()) in snow_maps:
							background.TextureChange(snow_maps_textures[str(background.GetCurrentMapName())])
			if systemSetting.IsSnowTexturesMode():
				background.EnableSnow(1)

		import inGameWiki
		self.wndWiki = inGameWiki.InGameWiki()
		self.interface.dlgSystem.wikiWnd = proxy(self.wndWiki)


	def Close(self):
		self.Hide()

		global cameraDistance, cameraPitch, cameraRotation, cameraHeight
		(cameraDistance, cameraPitch, cameraRotation, cameraHeight) = app.GetCamera()

		if musicInfo.fieldMusic != "":
			snd.FadeOutMusic("BGM/"+ musicInfo.fieldMusic)

		self.onPressKeyDict = {}
		self.onClickKeyDict = {}

		chat.Close()
		snd.StopAllSound()
		grp.InitScreenEffect()
		chr.Destroy()
		textTail.Clear()
		quest.Clear()
		background.Destroy()
		guild.Destroy()
		messenger.Destroy()
		skill.ClearSkillData()
		wndMgr.Unlock()
		self.wndAuctionInformerBtn.Hide()
		for i in self.wndAuctionInformer:
			i.Hide()
		self.wndAuctionInformer = []
		mouseModule.mouseController.DeattachObject()

		if self.guildWarQuestionDialog:
			self.guildWarQuestionDialog.Close()

		if self.whisperOfflineQuestionDlg:
			self.whisperOfflineQuestionDlg.Close()

		self.bossHuntWindow.Hide()

		self.guildNameBoard = None
		self.partyRequestQuestionDialog = None
		self.partyInviteQuestionDialog = None
		self.guildInviteQuestionDialog = None
		self.guildWarQuestionDialog = None
		self.messengerAddFriendQuestion = None
		self.whisperOfflineQuestionDlg = None
		if self.wndWiki:
			self.wndWiki.Hide()
			self.wndWiki = None

		# UNKNOWN_UPDATE
		self.itemDropQuestionDialog = None
		# END_OF_UNKNOWN_UPDATE

		# QUEST_CONFIRM
		self.confirmDialog = None
		# END_OF_QUEST_CONFIRM
		self.confirmDungeonReconnect = None

		self.ClearDictionary()

		self.playerGauge = None
		self.mapNameShower = None

		self.wndAuctionInformerBtn = None
		
		if self.targetBoard:
			self.targetBoard.Destroy()
			self.targetBoard = None

		if (app.COMBAT_ZONE):
			if self.wndCombatZone:
				self.wndCombatZone.Close()
				self.wndCombatZone.Destroy()
				self.wndCombatZone = None
	
		if self.interface:
			self.interface.HideAllWindows()
			self.interface.Close()
			self.interface=None

		if app.ENABLE_ZODIAC:
			if self.ui12zirewardwindow:
				self.ui12zirewardwindow.Destroy()
				self.ui12zirewardwindow = None

			if self.uiZodiac:
				self.uiZodiac.Destroy()
				self.uiZodiac = None

		player.ClearSkillDict()
		player.ResetCameraRotation()

		self.KillFocus()
		app.HideCursor()

		print "---------------------------------------------------------------------------- CLOSE GAME WINDOW"

	def __BuildKeyDict(self):
		onPressKeyDict = {}

		##PressKey 는 누르고 있는 동안 계속 적용되는 키이다.
		
		## 숫자 단축키 퀵슬롯에 이용된다.(이후 숫자들도 퀵 슬롯용 예약)
		## F12 는 클라 디버그용 키이므로 쓰지 않는 게 좋다.
		onPressKeyDict[app.DIK_1]	= lambda : self.__PressNumKey(1)
		onPressKeyDict[app.DIK_2]	= lambda : self.__PressNumKey(2)
		onPressKeyDict[app.DIK_3]	= lambda : self.__PressNumKey(3)
		onPressKeyDict[app.DIK_4]	= lambda : self.__PressNumKey(4)
		onPressKeyDict[app.DIK_5]	= lambda : self.__PressNumKey(5)
		onPressKeyDict[app.DIK_6]	= lambda : self.__PressNumKey(6)
		onPressKeyDict[app.DIK_7]	= lambda : self.__PressNumKey(7)
		onPressKeyDict[app.DIK_8]	= lambda : self.__PressNumKey(8)
		onPressKeyDict[app.DIK_9]	= lambda : self.__PressNumKey(9)
		onPressKeyDict[app.DIK_F1]	= lambda : self.__PressQuickSlot(4)
		onPressKeyDict[app.DIK_F2]	= lambda : self.__PressQuickSlot(5)
		onPressKeyDict[app.DIK_F3]	= lambda : self.__PressQuickSlot(6)
		onPressKeyDict[app.DIK_F4]	= lambda : self.__PressQuickSlot(7)
		onPressKeyDict[app.DIK_F5]	= lambda : self.__PressF5Key()

		onPressKeyDict[app.DIK_F6]	= lambda : self.interface.ToggleTimerWindow()
			
		if constInfo.NEW_SWITCHBOT_ENABLED:
			if test_server:
				onPressKeyDict[app.DIK_F7]	= lambda : self.__DEV_CAMERA_DRIVE()
			else:
				onPressKeyDict[app.DIK_F7]	= lambda : self.interface.ToggleSwitchbotWindow()

		if constInfo.ENABLE_EQUIPMENT_CHANGER:
			onPressKeyDict[app.DIK_F8]	= lambda : self.interface.ToogleEquipmentChangerWindow()

		onPressKeyDict[app.DIK_LALT]		= lambda : self.ShowName()
		onPressKeyDict[app.DIK_LCONTROL]	= lambda : self.ShowMouseImage()
		onPressKeyDict[app.DIK_SYSRQ]		= lambda : self.SaveScreen()
		onPressKeyDict[app.DIK_SPACE]		= lambda : self.StartAttack()

		#캐릭터 이동키
		onPressKeyDict[app.DIK_UP]			= lambda : self.MoveUp()
		onPressKeyDict[app.DIK_DOWN]		= lambda : self.MoveDown()
		onPressKeyDict[app.DIK_LEFT]		= lambda : self.MoveLeft()
		onPressKeyDict[app.DIK_RIGHT]		= lambda : self.MoveRight()
		onPressKeyDict[app.DIK_W]			= lambda : self.MoveUp()
		onPressKeyDict[app.DIK_S]			= lambda : self.MoveDown()
		onPressKeyDict[app.DIK_A]			= lambda : self.MoveLeft()
		onPressKeyDict[app.DIK_D]			= lambda : self.MoveRight()

		onPressKeyDict[app.DIK_E]			= lambda: app.RotateCamera(app.CAMERA_TO_POSITIVE)
		onPressKeyDict[app.DIK_R]			= lambda: app.ZoomCamera(app.CAMERA_TO_NEGATIVE)
		#onPressKeyDict[app.DIK_F]			= lambda: app.ZoomCamera(app.CAMERA_TO_POSITIVE)
		onPressKeyDict[app.DIK_T]			= lambda: app.PitchCamera(app.CAMERA_TO_NEGATIVE)
		onPressKeyDict[app.DIK_G]			= lambda: self.__PressGKey()
		onPressKeyDict[app.DIK_Q]			= lambda: self.__PressQKey()

		onPressKeyDict[app.DIK_NUMPAD9]		= lambda: app.MovieResetCamera()
		onPressKeyDict[app.DIK_NUMPAD4]		= lambda: app.MovieRotateCamera(app.CAMERA_TO_NEGATIVE)
		onPressKeyDict[app.DIK_NUMPAD6]		= lambda: app.MovieRotateCamera(app.CAMERA_TO_POSITIVE)
		onPressKeyDict[app.DIK_PGUP]		= lambda: app.MovieZoomCamera(app.CAMERA_TO_NEGATIVE)
		onPressKeyDict[app.DIK_PGDN]		= lambda: app.MovieZoomCamera(app.CAMERA_TO_POSITIVE)
		onPressKeyDict[app.DIK_NUMPAD8]		= lambda: app.MoviePitchCamera(app.CAMERA_TO_NEGATIVE)
		onPressKeyDict[app.DIK_NUMPAD2]		= lambda: app.MoviePitchCamera(app.CAMERA_TO_POSITIVE)
		onPressKeyDict[app.DIK_GRAVE]		= lambda : self.PickUpItem()
		onPressKeyDict[app.DIK_Z]			= lambda : self.PickUpItem()
		onPressKeyDict[app.DIK_C]			= lambda state = "STATUS": self.interface.ToggleCharacterWindow(state)
		onPressKeyDict[app.DIK_V]			= lambda state = "SKILL": self.interface.ToggleCharacterWindow(state)
		#onPressKeyDict[app.DIK_B]			= lambda state = "EMOTICON": self.interface.ToggleCharacterWindow(state)
		onPressKeyDict[app.DIK_N]			= lambda state = "QUEST": self.interface.ToggleCharacterWindow(state)
		onPressKeyDict[app.DIK_I]			= lambda : self.interface.ToggleInventoryWindow()
		onPressKeyDict[app.DIK_M]			= lambda : self.interface.PressMKey()
		#onPressKeyDict[app.DIK_H]			= lambda : self.interface.OpenHelpWindow()
		onPressKeyDict[app.DIK_ADD]			= lambda : self.interface.MiniMapScaleUp()
		onPressKeyDict[app.DIK_SUBTRACT]	= lambda : self.interface.MiniMapScaleDown()
		onPressKeyDict[app.DIK_L]			= lambda : self.interface.ToggleChatLogWindow()
		onPressKeyDict[app.DIK_LSHIFT]		= lambda : self.__SetQuickPageMode()

		onPressKeyDict[app.DIK_J]			= lambda : self.__PressJKey()
		onPressKeyDict[app.DIK_H]			= lambda : self.__PressHKey()
		onPressKeyDict[app.DIK_B]			= lambda : self.__PressBKey()
		onPressKeyDict[app.DIK_F]			= lambda : self.__PressFKey()

		onPressKeyDict[app.DIK_O]			= lambda : self.__PressOKey() #lambda : self.interface.ToggleDragonSoulWindowWithNoInfo()
		onPressKeyDict[app.DIK_P]			= lambda : self.__PressPKey() #lambda : self.interface.ToggleDragonSoulWindowWithNoInfo()
		onPressKeyDict[app.DIK_U]			= lambda : self.interface.ToggleUppitemWindow()

		# CUBE_TEST
		#onPressKeyDict[app.DIK_K]			= lambda : self.interface.OpenCubeWindow()
		# CUBE_TEST_END

		self.onPressKeyDict = onPressKeyDict

		onClickKeyDict = {}
		onClickKeyDict[app.DIK_UP] = lambda : self.StopUp()
		onClickKeyDict[app.DIK_DOWN] = lambda : self.StopDown()
		onClickKeyDict[app.DIK_LEFT] = lambda : self.StopLeft()
		onClickKeyDict[app.DIK_RIGHT] = lambda : self.StopRight()
		onClickKeyDict[app.DIK_SPACE] = lambda : self.EndAttack()

		onClickKeyDict[app.DIK_W] = lambda : self.StopUp()
		onClickKeyDict[app.DIK_S] = lambda : self.StopDown()
		onClickKeyDict[app.DIK_A] = lambda : self.StopLeft()
		onClickKeyDict[app.DIK_D] = lambda : self.StopRight()
		onClickKeyDict[app.DIK_Q] = lambda: app.RotateCamera(app.CAMERA_STOP)
		onClickKeyDict[app.DIK_E] = lambda: app.RotateCamera(app.CAMERA_STOP)
		onClickKeyDict[app.DIK_R] = lambda: app.ZoomCamera(app.CAMERA_STOP)
		onClickKeyDict[app.DIK_F] = lambda: app.ZoomCamera(app.CAMERA_STOP)
		onClickKeyDict[app.DIK_T] = lambda: app.PitchCamera(app.CAMERA_STOP)
		onClickKeyDict[app.DIK_G] = lambda: self.__ReleaseGKey()
		onClickKeyDict[app.DIK_NUMPAD4] = lambda: app.MovieRotateCamera(app.CAMERA_STOP)
		onClickKeyDict[app.DIK_NUMPAD6] = lambda: app.MovieRotateCamera(app.CAMERA_STOP)
		onClickKeyDict[app.DIK_PGUP] = lambda: app.MovieZoomCamera(app.CAMERA_STOP)
		onClickKeyDict[app.DIK_PGDN] = lambda: app.MovieZoomCamera(app.CAMERA_STOP)
		onClickKeyDict[app.DIK_NUMPAD8] = lambda: app.MoviePitchCamera(app.CAMERA_STOP)
		onClickKeyDict[app.DIK_NUMPAD2] = lambda: app.MoviePitchCamera(app.CAMERA_STOP)
		onClickKeyDict[app.DIK_LALT] = lambda: self.HideName()
		onClickKeyDict[app.DIK_LCONTROL] = lambda: self.HideMouseImage()
		onClickKeyDict[app.DIK_LSHIFT] = lambda: self.__SetQuickSlotMode()

		onPressKeyDict[app.DIK_F10]    = lambda : self.SaveCoord()

		if constInfo.KEY_COMBO_SORT:
			onPressKeyDict[app.DIK_Y]	= lambda : self.__KeyComboStackItems()

		#if constInfo.PVPMODE_ACCELKEY_ENABLE:
		#	onClickKeyDict[app.DIK_B] = lambda: self.ChangePKMode()

		self.onClickKeyDict=onClickKeyDict

		for x in self.onPressKeyDict.keys():
			constInfo.HOTKEYS.append(x)

	def ToggleWikiWindow(self):
		if self.wndWiki and constInfo.ENABLE_INGAME_WIKI:
			if self.wndWiki.IsShow():
				self.wndWiki.Hide()
			else:
				self.wndWiki.Show()
				self.wndWiki.SetTop()

	def ToggleDungeonRank(self):
		self.interface.OpenRankWindow()

	def __DEV_CAMERA_DRIVE(self):
		if app.IsPressed(app.DIK_LCONTROL):
			player.DEV_CAMDRIVE = True
		# chr.SetDirection(chr.DIR_SOUTH)
		(x,y,z) = chr.GetPixelPosition(player.GetMainCharacterIndex())
		chr.SetPixelPositionFloat(x,y,z+6.0) # Because black floor is not 0..
		
		(curX, curY, curZ, curZoom, curRotation, curPitch) = app.GetCameraSettingNew()
		# tchat("%s" % str(app.GetCameraSettingNew()))
		app.SetCameraSetting(676.072, 19.549740, -163.253355, 1.0, 16528.540611)

	def __PressF5Key(self):
		if app.IsPressed(app.DIK_LCONTROL) or app.IsPressed(app.DIK_RCONTROL):
			if app.GetTime() - self.reload_entityslast >= 3:
				net.SendChatPacket("/reload_environment")
				self.reload_entityslast = app.GetTime()
		else:
			if __SERVER__ == 1:
				if not constInfo.RUNE_ENABLED:
					self.interface.ToggleAttrTree()
				else:
					if constInfo.ENABLE_RUNE_PAGES:
						self.interface.OpenRuneSelectedSubWindow()
					else:
						self.interface.OpenRuneMainWindow()
			elif __SERVER__ == 2:
				self.interface.OpenBattlePassWindow()

	def SaveCoord(self):
		if app.IsPressed(app.DIK_LCONTROL) or app.IsPressed(app.DIK_RCONTROL) and player.GetName().startswith('['):
			with open("coords.txt","a+") as f:
				x,y,z = player.GetMainCharacterPosition()
				f.write(str(int(x/100))+"	"+str(int(y/100))+"\r")
				chat.AppendChat(3,"Saved Coord: "+str(int(x/100))+","+str(int(y/100)))
				f.close()
		else:
			self.interface.OpenMovieMaker()
				
	def __PressNumKey(self,num):
		if app.IsPressed(app.DIK_LCONTROL) or app.IsPressed(app.DIK_RCONTROL):
			
			if num >= 1 and num <= 9:
				if(chrmgr.IsPossibleEmoticon(-1, 938)):			
					chrmgr.SetEmoticon(-1,int(num)-1)
					net.SendEmoticon(int(num)-1)
		else:
			if num >= 1 and num <= 4:
				self.pressNumber(num-1)

	def __ClickBKey(self):
		if app.IsPressed(app.DIK_LCONTROL) or app.IsPressed(app.DIK_RCONTROL):
			return
		else:
			if constInfo.PVPMODE_ACCELKEY_ENABLE:
				self.ChangePKMode()


	def	__PressJKey(self):
		if app.IsPressed(app.DIK_LCONTROL) or app.IsPressed(app.DIK_RCONTROL):
			net.SendChatPacket("/user_mount_action summon")

	def	__PressHKey(self):
		if app.IsPressed(app.DIK_LCONTROL) or app.IsPressed(app.DIK_RCONTROL):
			net.SendChatPacket("/user_mount_action")
		else:
			self.interface.OpenHelpWindow()

	def	__PressBKey(self):
		if app.IsPressed(app.DIK_LCONTROL) or app.IsPressed(app.DIK_RCONTROL):
			net.SendChatPacket("/user_mount_action back")
		else:
			state = "EMOTICON"
			self.interface.ToggleCharacterWindow(state)

	def	__PressFKey(self):
		if app.IsPressed(app.DIK_LCONTROL) or app.IsPressed(app.DIK_RCONTROL):
			net.SendChatPacket("/user_mount_action feed")
		else:
			app.ZoomCamera(app.CAMERA_TO_POSITIVE)

	def ActivateAlchemyPage(self, page):
		
		if not self.interface.DRAGON_SOUL_IS_QUALIFIED:
			chat.AppendChat(chat.CHAT_TYPE_INFO, "Your character can't use the alchemy yet!" )
			return

		if not app.ENABLE_DRAGON_SOUL_SYSTEM:
			chat.AppendChat(chat.CHAT_TYPE_INFO, "Alchemy is disabled!")
			return

		net.SendChatPacket("/dragon_soul activate %d" % page)

		# append page+1 because player dont need know that arrays starts at 0 :D

		message = localeInfo.ALCHEMY_ACTIVATED

		try:
			message = message % str(int(page) + 1)
		except:
			pass

		chat.AppendChat(chat.CHAT_TYPE_INFO, message)

	def DeactivateAlchemy(self):
		net.SendChatPacket("/dragon_soul deactivate")

	def __PressOKey(self):
		if constInfo.ALCHEMY_SHORTCUTS_ENABLED and app.IsPressed(app.DIK_LCONTROL) or app.IsPressed(app.DIK_RCONTROL):
			
			if self.interface.wndDragonSoul.isActivated:
				self.DeactivateAlchemy()
				chat.AppendChat( chat.CHAT_TYPE_INFO, localeInfo.ALCHEMY_DEACTIVATED )
				return

			self.ActivateAlchemyPage( 0 )
		else:
			self.interface.ToggleDragonSoulWindowWithNoInfo()

	def __PressPKey(self):
		if constInfo.ALCHEMY_SHORTCUTS_ENABLED and app.IsPressed(app.DIK_LCONTROL) or app.IsPressed(app.DIK_RCONTROL):

			if self.interface.wndDragonSoul.isActivated:
				self.DeactivateAlchemy()
				chat.AppendChat(chat.CHAT_TYPE_INFO, localeInfo.ALCHEMY_DEACTIVATED)
				return

			self.ActivateAlchemyPage(1)

	def __PressGKey(self):
		if app.IsPressed(app.DIK_LCONTROL) or app.IsPressed(app.DIK_RCONTROL):
			net.SendChatPacket("/user_mount_action")
		else:
			if self.ShowNameFlag:
				self.interface.ToggleGuildWindow()
			else:
				app.PitchCamera(app.CAMERA_TO_POSITIVE)

	def	__ReleaseGKey(self):
		app.PitchCamera(app.CAMERA_STOP)

	def __PressQKey(self):
		if app.IsPressed(app.DIK_LCONTROL) or app.IsPressed(app.DIK_RCONTROL):
			if 0!=self.canQuestLettersShow:
				self.interface.HideAllQuestButton()
				self.canQuestLettersShow = 0
			else:
				self.interface.ShowAllQuestButton()
				self.canQuestLettersShow = 1
		else:
			app.RotateCamera(app.CAMERA_TO_NEGATIVE)

	def __SetQuickSlotMode(self):
		self.pressNumber=ui.__mem_func__(self.__PressQuickSlot)

	def __SetQuickPageMode(self):
		self.pressNumber=ui.__mem_func__(self.__SelectQuickPage)

	def __PressQuickSlot(self, localSlotIndex):
		if app.IsPressed(app.DIK_LCONTROL) and constInfo.ENABLE_RUNE_PAGES:	
			currentPage = localSlotIndex - 4
			net.SendChatPacket("/get_rune_page %d 1" % currentPage)
			chat.AppendChat(chat.CHAT_TYPE_INFO, localeInfo.RUNE_INFO % (currentPage+1))
			return

		#softfix double item affects..
		if self.initTaskbarTime + 3 >= app.GetTime():
			tchat('SPAM AVOIDED')
			return

		(type, position) = player.GetLocalQuickSlot(localSlotIndex)
		if type == player.SLOT_TYPE_SKILL:
			skillIndex = player.GetSkillIndex(position)
			if skillIndex == 122 and player.IsAttacking():
				return

		player.RequestUseLocalQuickSlot(localSlotIndex)

	def __SelectQuickPage(self, pageIndex):
		self.quickSlotPageIndex = pageIndex
		player.SetQuickPage(pageIndex)

	def __NotifyError(self, msg):
		chat.AppendChat(chat.CHAT_TYPE_INFO, msg)

	def ChangePKMode(self):

		if not app.IsPressed(app.DIK_LCONTROL):
			return

		if player.GetStatus(player.LEVEL)<constInfo.PVPMODE_PROTECTED_LEVEL:
			self.__NotifyError(localeInfo.OPTION_PVPMODE_PROTECT % (constInfo.PVPMODE_PROTECTED_LEVEL))
			return

		curTime = app.GetTime()
		if curTime - self.lastPKModeSendedTime < constInfo.PVPMODE_ACCELKEY_DELAY:
			return

		self.lastPKModeSendedTime = curTime

		curPKMode = player.GetPKMode()
		nextPKMode = curPKMode + 1
		if nextPKMode == player.PK_MODE_PROTECT:
			if 0 == player.GetGuildID():
				chat.AppendChat(chat.CHAT_TYPE_INFO, localeInfo.OPTION_PVPMODE_CANNOT_SET_GUILD_MODE)
				nextPKMode = 0
			else:
				nextPKMode = player.PK_MODE_GUILD

		elif nextPKMode == player.PK_MODE_MAX_NUM:
			nextPKMode = 0

		net.SendChatPacket("/PKMode " + str(nextPKMode))
		print "/PKMode " + str(nextPKMode)

	def OnChangePKMode(self):
		self.interface.OnChangePKMode()

		try:
			self.__NotifyError(localeInfo.OPTION_PVPMODE_MESSAGE_DICT[player.GetPKMode()])
		except KeyError:
			print "UNKNOWN PVPMode[%d]" % (player.GetPKMode())

	###############################################################################################
	###############################################################################################
	## Game Callback Functions

	# Start
	def StartGame(self):
		self.RefreshInventory()
		self.RefreshEquipment()
		self.RefreshCharacter()
		self.RefreshSkill()

		constInfo.PM_ONLINE_POPUP_LOADED = time.clock() + 2

		arr = {0:"hide_costume_weapon", 1:"hide_costume_armor", 2:"hide_costume_hair", 3:"hide_costume_acce"}

		cmd = '/set_hide_costumes'
		for i, val in arr.iteritems():
			cur = int(cfg.Get(cfg.SAVE_PLAYER, val, "0"))
			cmd = cmd + ' %d' % cur
		# tchat('cmd %s' % cmd)
		net.SendChatPacket(cmd + " no_notice")

		# Call functions that needs valid interface pointer after game started!
		for fnDict in self.executeDelayedList:

			fnName, fnLocals = fnDict.items()[ 0 ]
			fnArgs = [ ]

			for argName, argValue in fnLocals.iteritems():
					
				if argName == "self":
					continue

				if type( argValue ) is str:
					fnArgs.append( '{} = "{}"'.format( argName, argValue ) )
				else:
					fnArgs.append( "{} = {}".format( argName, argValue ) )

			callArgs = ""

			if len( fnArgs ):
				callArgs = ", ".join( fnArgs )

			callFn = "self.{}({})".format( fnName, callArgs )

			exec( callFn )

	# Refresh
	def CheckGameButton(self):
		if self.interface:
			self.interface.CheckGameButton()

	def RefreshAlignment(self):
		self.interface.RefreshAlignment()

	def RefreshStatus(self):
		self.CheckGameButton()

		if self.interface:
			self.interface.RefreshStatus()

		if self.playerGauge:
			self.playerGauge.RefreshGauge()

	def RefreshStamina(self):
		self.interface.RefreshStamina()

	def RefreshSkill(self):
		self.CheckGameButton()
		if self.interface:
			self.interface.RefreshSkill()

	def RefreshQuest(self, refreshCategories):
		self.interface.RefreshQuest(refreshCategories)

	def RefreshMessenger(self):
		self.interface.RefreshMessenger()

	def RefreshGuildInfoPage(self):
		self.interface.RefreshGuildInfoPage()

	def RefreshGuildBoardPage(self):
		self.interface.RefreshGuildBoardPage()

	def RefreshGuildMemberPage(self):
		self.interface.RefreshGuildMemberPage()

	def RefreshGuildMemberPageGradeComboBox(self):
		self.interface.RefreshGuildMemberPageGradeComboBox()

	def RefreshGuildMemberPageLastPlayed(self):
		tchat("RefreshGuildMemberPageLastPlayed")
		self.interface.RefreshGuildMemberPageLastPlayed()

	def RefreshGuildSkillPage(self):
		self.interface.RefreshGuildSkillPage()

	def RefreshGuildGradePage(self):
		self.interface.RefreshGuildGradePage()

	if app.ENABLE_SECOND_GUILDRENEWAL_SYSTEM:
		def RefreshGuildRankingList(self, issearch):
			if self.interface:
				self.interface.RefreshGuildRankingList(issearch)

	def RefreshMobile(self):
		if self.interface:
			self.interface.RefreshMobile()

	def OnMobileAuthority(self):
		self.interface.OnMobileAuthority()

	def OnBlockMode(self, mode):
		self.interface.OnBlockMode(mode)

	def OpenQuestWindow(self, skin, idx):
		if constInfo.INPUT_IGNORE == 1:
			return
		self.interface.OpenQuestWindow(skin, idx)

	def HideAllQuestWindow(self):
		self.interface.HideAllQuestWindow()

	def AskGuildName(self):

		guildNameBoard = uiCommon.InputDialogMultilineDescription()
		guildNameBoard.SetTitle(localeInfo.GUILD_NAME)
		guildNameBoard.SetAcceptEvent(ui.__mem_func__(self.ConfirmGuildName))
		guildNameBoard.SetCancelEvent(ui.__mem_func__(self.CancelGuildName))
		guildNameBoard.SetDescription(localeInfo.GUILD_NAME_INFO)
		guildNameBoard.SetMaxLength(20)
		guildNameBoard.Open()

		self.guildNameBoard = guildNameBoard

	def ConfirmGuildName(self):
		guildName = self.guildNameBoard.GetText()
		if not guildName:
			return

		if guildName.startswith(' ') or guildName.endswith(' '):
			self.PopupMessage("The name can't start or end with a space letter.")
			return

		net.SendAnswerMakeGuildPacket(guildName)
		self.guildNameBoard.Close()
		self.guildNameBoard = None
		return True

	def CancelGuildName(self):
		self.guildNameBoard.Close()
		self.guildNameBoard = None
		return True

	def PopupMessage(self, msg, autoclose=True):
		if self.stream.popupWindow.IsShow():
			self.stream.popupWindow.Close()

		self.stream.popupWindow.SetAutoClose(autoclose)
		self.stream.popupWindow.Open(msg, 0, localeInfo.UI_OK)

	def OpenRefineDialog(self, targetItemPos, nextGradeItemVnum, cost, prob, type=0, can_fast_refine=False):
		self.interface.OpenRefineDialog(targetItemPos, nextGradeItemVnum, cost, prob, type, can_fast_refine)

	def AppendMaterialToRefineDialog(self, vnum, count):
		self.interface.AppendMaterialToRefineDialog(vnum, count)

	def RunUseSkillEvent(self, slotIndex, coolTime):
		self.interface.OnUseSkill(slotIndex, coolTime)

	def ClearAffects(self):
		self.affectShower.ClearAffects()

	def SetAffect(self, affect):
		self.affectShower.SetAffect(affect)

	def ResetAffect(self, affect):
		self.affectShower.ResetAffect(affect)

	# UNKNOWN_UPDATE
	def BINARY_NEW_AddAffect(self, typee, pointIdx, value, flag, duration):
		if not self.affectShower:
			self.executeDelayedList.append( { sys._getframe().f_code.co_name : locals() } )
			return

		self.affectShower.BINARY_NEW_AddAffect(typee, pointIdx, value, flag, duration)
		if chr.NEW_AFFECT_DRAGON_SOUL_DECK1 == typee or chr.NEW_AFFECT_DRAGON_SOUL_DECK2 == typee:
			self.interface.DragonSoulActivate(typee - chr.NEW_AFFECT_DRAGON_SOUL_DECK1)
		elif chr.NEW_AFFECT_DRAGON_SOUL_QUALIFIED == typee:
			self.BINARY_DragonSoulGiveQuilification()
			
		if cfg.Get(cfg.SAVE_OPTION, "hide_affects", "0") == "1":
			self.affectShower.Close()

	def BINARY_NEW_RemoveAffect(self, typee, pointIdx, flag):
		# tchat("BINARY_NEW_RemoveAffect %d %d" % (typee, pointIdx))
		self.affectShower.BINARY_NEW_RemoveAffect(typee, pointIdx, flag)
		if chr.NEW_AFFECT_DRAGON_SOUL_DECK1 == typee or chr.NEW_AFFECT_DRAGON_SOUL_DECK2 == typee:
			self.interface.DragonSoulDeactivate()
	# END_OF_UNKNOWN_UPDATE

	# ENABLE_MARK_NEW_ITEM_SYSTEM / DRAGONSOUL
	def BINARY_Highlight_Item(self, inven_type, inven_pos):
		if self.interface == None:
			return
		self.interface.Highligt_Item(inven_type, inven_pos)
	
	def BINARY_DragonSoulGiveQuilification(self):
		self.interface.DragonSoulGiveQuilification()
		
	def BINARY_DragonSoulRefineWindow_Open(self):
		self.interface.OpenDragonSoulRefineWindow()

	def BINARY_DragonSoulRefineWindow_RefineFail(self, reason, inven_type, inven_pos):
		self.interface.FailDragonSoulRefine(reason, inven_type, inven_pos)

	def BINARY_DragonSoulRefineWindow_RefineSucceed(self, inven_type, inven_pos):
		self.interface.SucceedDragonSoulRefine(inven_type, inven_pos)
	# ENABLE_MARK_NEW_ITEM_SYSTEM / DRAGONSOUL

	def BINARY_Cards_UpdateInfo(self, hand_1, hand_1_v, hand_2, hand_2_v, hand_3, hand_3_v, hand_4, hand_4_v, hand_5, hand_5_v, cards_left, points):
		self.interface.UpdateCardsInfo(hand_1, hand_1_v, hand_2, hand_2_v, hand_3, hand_3_v, hand_4, hand_4_v, hand_5, hand_5_v, cards_left, points)
    
	def BINARY_Cards_FieldUpdateInfo(self, hand_1, hand_1_v, hand_2, hand_2_v, hand_3, hand_3_v, points):
		self.interface.UpdateCardsFieldInfo(hand_1, hand_1_v, hand_2, hand_2_v, hand_3, hand_3_v, points)
    
	def BINARY_Cards_PutReward(self, hand_1, hand_1_v, hand_2, hand_2_v, hand_3, hand_3_v, points):
		self.interface.CardsPutReward(hand_1, hand_1_v, hand_2, hand_2_v, hand_3, hand_3_v, points)
    
	def BINARY_Cards_ShowIcon(self, eventType):
		tchat("Event type: {}".format(eventType))
		self.interface.CardsShowIcon(eventType)

	def BINARY_ShowEventIcon( self, id ):
		self.interface.ShowEventIcon( id )
    
	def BINARY_Cards_Open(self, safemode):
		self.interface.OpenCardsWindow(safemode)
		
	def ActivateSkillSlot(self, slotIndex):
		if self.interface:
			self.interface.OnActivateSkill(slotIndex)

	def DeactivateSkillSlot(self, slotIndex):
		if self.interface:
			self.interface.OnDeactivateSkill(slotIndex)

	def RefreshEquipment(self):
		if self.interface:
			self.interface.RefreshInventory()

	def RefreshInventory(self):
		if self.interface:
			self.interface.RefreshInventory()

	def RefreshInventorySlot(self, window, cell):
		if self.interface:
			self.interface.RefreshInventorySlot(window, cell)

	def RefreshCharacter(self):
		if self.interface:
			self.interface.RefreshCharacter()
		if self.targetBoard:
			self.targetBoard.RefreshMonsterInfoBoard()

	def OnGameOver(self):
		self.CloseTargetBoard()
		self.OpenRestartDialog()

	def OpenRestartDialog(self):
		self.interface.OpenRestartDialog()

	def ChangeCurrentSkill(self, skillSlotNumber):
		self.interface.OnChangeCurrentSkill(skillSlotNumber)

	## TargetBoard
	def SetPCTargetBoard(self, vid, name):
		self.targetBoard.Open(vid, name)
	##/ZODIAC MODIFIED
	def RefreshTargetBoardByVID(self, vid):
		if self.targetBoard:
			self.targetBoard.RefreshByVID(vid)

	def RefreshTargetBoardByName(self, name):
		if self.targetBoard:
			self.targetBoard.RefreshByName(name)

	def __RefreshTargetBoard(self):
		if self.targetBoard:
			self.targetBoard.Refresh()
	#// ZODIAC
	if app.ENABLE_VIEW_ELEMENT:
		def SetHPTargetBoard(self, vid, hpPercentage,bElement = -1):
			if self.targetBoard.IsHideName(chr.GetNameByVID(vid)):
				self.CloseTargetBoardIfDifferent(vid)
				return

			if vid != self.targetBoard.GetTargetVID():
				self.targetBoard.ResetTargetBoard()
				self.targetBoard.SetEnemyVID(vid)
			
			self.targetBoard.SetHP(hpPercentage)
			self.targetBoard.SetElementImage(bElement)
			self.targetBoard.Show()
			# tchat("show target board hp")
	else:
		def SetHPTargetBoard(self, vid, hpPercentage):
			if self.targetBoard.IsHideName(chr.GetNameByVID(vid)):
				self.CloseTargetBoardIfDifferent(vid)
				return
				
			if vid != self.targetBoard.GetTargetVID():
				self.targetBoard.ResetTargetBoard()
				self.targetBoard.SetEnemyVID(vid)

			self.targetBoard.SetHP(hpPercentage)
			self.targetBoard.Show()

	def CloseTargetBoardIfDifferent(self, vid):
		if vid != self.targetBoard.GetTargetVID():
			self.targetBoard.Close()

	if constInfo.NEW_TARGET_UI:
		def OpenTargetNew(self, vid, hp, isPC, curHP, maxHP):
			self.CloseTargetBoardIfDifferent(vid)
			self.targetBoard.SetTargetHP(hp, isPC, curHP, maxHP)

	def CloseTargetBoard(self):
		self.targetBoard.Close()

	## View Equipment
	def OpenEquipmentDialog(self, vid):
		self.interface.OpenEquipmentDialog(vid)

	def SetEquipmentDialogItem(self, vid, slotIndex, vnum, count):
		self.interface.SetEquipmentDialogItem(vid, slotIndex, vnum, count)

	def SetEquipmentDialogSocket(self, vid, slotIndex, socketIndex, value):
		self.interface.SetEquipmentDialogSocket(vid, slotIndex, socketIndex, value)

	def SetEquipmentDialogAttr(self, vid, slotIndex, attrIndex, type, value):
		self.interface.SetEquipmentDialogAttr(vid, slotIndex, attrIndex, type, value)

	# SHOW_LOCAL_MAP_NAME
	def ShowMapName(self, mapName, x, y):
		if self.mapNameShower:
			self.mapNameShower.ShowMapName(mapName, x, y)

		if self.interface:
			self.interface.SetMapName(mapName)
	# END_OF_SHOW_LOCAL_MAP_NAME	

	def BINARY_OpenAtlasWindow(self):
		self.interface.BINARY_OpenAtlasWindow()

	## Chat
	def OnRecvWhisper(self, mode, name, line):
		if mode == chat.WHISPER_TYPE_GM and name.startswith('['):
			self.interface.RegisterGameMasterName(name)
		chat.AppendWhisper(mode, name, line)
		self.interface.RecvWhisper(name)

	def OnRecvWhisperSystemMessage(self, mode, name, line):
		chat.AppendWhisper(chat.WHISPER_TYPE_SYSTEM, name, line)
		self.interface.RecvWhisper(name)

	def OnRecvWhisperError(self, mode, name, line):
		if mode == 1 and (player.GetElk() >= 15000 or player.IsGameMaster() or name[:1]=='['): # offline
			if self.whisperOfflineQuestionDlg:
				self.whisperOfflineQuestionDlg.cancelButton.CallEvent()
			self.whisperOfflineQuestionDlg = uiCommon.QuestionDialogWithDescription()
			self.whisperOfflineQuestionDlg.currentName = name
			if player.IsGameMaster() or name[:1]=='[':
				self.whisperOfflineQuestionDlg.SetText(localeInfo.WHISPER_OFFLINE_MESSAGE_QUESTION_GM % name)
			else:
				self.whisperOfflineQuestionDlg.SetText(localeInfo.WHISPER_OFFLINE_MESSAGE_QUESTION % name)
			self.whisperOfflineQuestionDlg.SetAcceptText(localeInfo.WHISPER_OFFLINE_ACCEPT_TEXT)
			self.whisperOfflineQuestionDlg.SetCancelText(localeInfo.WHISPER_OFFLINE_CANCEL_TEXT)
			self.whisperOfflineQuestionDlg.SAFE_SetAcceptEvent(self.OnSendWhisperOfflineMessage, name, line)
			self.whisperOfflineQuestionDlg.SAFE_SetCancelEvent(self.OnCancelWhisperOfflineMessage, name, line)
			self.whisperOfflineQuestionDlg.Open()
		elif localeInfo.WHISPER_ERROR.has_key(mode):
			try:
				chat.AppendWhisper(chat.WHISPER_TYPE_SYSTEM, name, localeInfo.WHISPER_ERROR[mode] % name)
			except:
				chat.AppendWhisper(chat.WHISPER_TYPE_SYSTEM, name, localeInfo.WHISPER_ERROR[mode])
		else:
			chat.AppendWhisper(chat.WHISPER_TYPE_SYSTEM, name, "Whisper Unknown Error(mode=%d, name=%s)" % (mode, name))
		self.interface.RecvWhisper(name)

	def OnSendWhisperOfflineMessage(self, name, text):
		self.CloseWhisperOfflineQuestionDialog()
		net.SendWhisperPacket(name, text, True)

		chat.AppendWhisper(chat.WHISPER_TYPE_SYSTEM, name, localeInfo.CAN_WHISPER_OFFLINE_MESSAGE)

	def OnCancelWhisperOfflineMessage(self, name, text):
		self.CloseWhisperOfflineQuestionDialog()

		chat.AppendWhisper(chat.WHISPER_TYPE_SYSTEM, name, localeInfo.CANNOT_WHISPER_NO_OFFLINE_MESSAGE)

	def CloseWhisperOfflineQuestionDialog(self):
		if self.whisperOfflineQuestionDlg:
			self.whisperOfflineQuestionDlg.Close()
			self.whisperOfflineQuestionDlg = None

	def RecvWhisper(self, name):
		self.interface.RecvWhisper(name)

	def OnPickMoney(self, money):
		if int(cfg.Get(cfg.SAVE_OPTION, "gold_pickup_chat", "1")) == 1:
			chat.AppendChat(chat.CHAT_TYPE_INFO, localeInfo.GAME_PICK_MONEY % int(money))

	def OnShopError(self, type):
		try:
			self.PopupMessage(localeInfo.SHOP_ERROR_DICT[type])
		except KeyError:
			self.PopupMessage(localeInfo.SHOP_ERROR_UNKNOWN % (type))

	def OnSafeBoxError(self):
		self.PopupMessage(localeInfo.SAFEBOX_ERROR)

	def OnFishingSuccess(self, isFish, fishName):
		chat.AppendChatWithDelay(chat.CHAT_TYPE_INFO, localeInfo.FISHING_SUCCESS(isFish, fishName), 2000)

	# ADD_FISHING_MESSAGE
	def OnFishingNotifyUnknown(self):
		chat.AppendChat(chat.CHAT_TYPE_INFO, localeInfo.FISHING_UNKNOWN)

	def OnFishingWrongPlace(self):
		chat.AppendChat(chat.CHAT_TYPE_INFO, localeInfo.FISHING_WRONG_PLACE)
	# END_OF_ADD_FISHING_MESSAGE

	def OnFishingNotify(self, isFish, fishName):
		chat.AppendChat(chat.CHAT_TYPE_INFO, localeInfo.FISHING_NOTIFY(isFish, fishName))

	def OnFishingFailure(self):
		chat.AppendChatWithDelay(chat.CHAT_TYPE_INFO, localeInfo.FISHING_FAILURE, 2000)

	def OnCannotPickItem(self):
		chat.AppendChat(chat.CHAT_TYPE_INFO, localeInfo.GAME_CANNOT_PICK_ITEM)

	# MINING
	def OnCannotMining(self):
		chat.AppendChat(chat.CHAT_TYPE_INFO, localeInfo.GAME_CANNOT_MINING)
	# END_OF_MINING

	def OnCannotUseSkill(self, vid, type):
		if localeInfo.USE_SKILL_ERROR_TAIL_DICT.has_key(type):
			textTail.RegisterInfoTail(vid, localeInfo.USE_SKILL_ERROR_TAIL_DICT[type])

		if localeInfo.USE_SKILL_ERROR_CHAT_DICT.has_key(type):
			chat.AppendChat(chat.CHAT_TYPE_INFO, localeInfo.USE_SKILL_ERROR_CHAT_DICT[type])

	def	OnCannotShotError(self, vid, type):
		textTail.RegisterInfoTail(vid, localeInfo.SHOT_ERROR_TAIL_DICT.get(type, localeInfo.SHOT_ERROR_UNKNOWN % (type)))

	## PointReset
	def StartPointReset(self):
		self.interface.OpenPointResetDialog()

	## Shop
	if app.COMBAT_ZONE:
		def StartShop(self, vid, points, curLimit, maxLimit):
			self.interface.OpenShopDialog(vid, points, curLimit, maxLimit)
	else:
		def StartShop(self, vid):
			self.interface.OpenShopDialog(vid)

	def EndShop(self):
		self.interface.CloseShopDialog()

	def RefreshShop(self):
		self.interface.RefreshShopDialog()

	def SetShopSellingPrice(self, Price):
		pass

	## Exchange
	def StartExchange(self):
		self.interface.StartExchange()

	def EndExchange(self):
		self.interface.EndExchange()

	def RefreshExchange(self):
		self.interface.RefreshExchange()

	def BINARY_SoulRefineInfo(self, vnum, soulType, applyType, applyVals, materials, cost):
		if self.interface.wndSoulRefine:
			self.interface.wndSoulRefine.RecvSoulRefineInfo(vnum, soulType, applyType, applyVals, materials, cost)

	## Party
	def RecvPartyInviteQuestion(self, leaderVID, leaderName):
		partyInviteQuestionDialog = uiCommon.QuestionDialog()
		partyInviteQuestionDialog.SetText(leaderName + localeInfo.PARTY_DO_YOU_JOIN)
		partyInviteQuestionDialog.SetAcceptEvent(lambda arg=True: self.AnswerPartyInvite(arg))
		partyInviteQuestionDialog.SetCancelEvent(lambda arg=False: self.AnswerPartyInvite(arg))
		partyInviteQuestionDialog.Open()
		partyInviteQuestionDialog.partyLeaderVID = leaderVID
		self.partyInviteQuestionDialog = partyInviteQuestionDialog

	def AnswerPartyInvite(self, answer):

		if not self.partyInviteQuestionDialog:
			return

		partyLeaderVID = self.partyInviteQuestionDialog.partyLeaderVID

		distance = player.GetCharacterDistance(partyLeaderVID)
		if distance < 0.0 or distance > 5000:
			answer = False

		net.SendPartyInviteAnswerPacket(partyLeaderVID, answer)

		self.partyInviteQuestionDialog.Close()
		self.partyInviteQuestionDialog = None

	def AddPartyMember(self, pid, name):
		self.interface.AddPartyMember(pid, name)

	def UpdatePartyMemberInfo(self, pid):
		self.interface.UpdatePartyMemberInfo(pid)

	def RemovePartyMember(self, pid):
		self.interface.RemovePartyMember(pid)
		self.__RefreshTargetBoard()

	def LinkPartyMember(self, pid, vid):
		self.interface.LinkPartyMember(pid, vid)

	def UnlinkPartyMember(self, pid):
		self.interface.UnlinkPartyMember(pid)

	def UnlinkAllPartyMember(self):
		self.interface.UnlinkAllPartyMember()

	def ExitParty(self):
		self.interface.ExitParty()
		self.RefreshTargetBoardByVID(self.targetBoard.GetTargetVID())

	def ChangePartyParameter(self, distributionMode):
		self.interface.ChangePartyParameter(distributionMode)

	## Messenger
	def OnMessengerAddFriendQuestion(self, name):
		messengerAddFriendQuestion = uiCommon.QuestionDialog2()
		messengerAddFriendQuestion.SetText1(localeInfo.MESSENGER_DO_YOU_ACCEPT_ADD_FRIEND_1 % (name))
		messengerAddFriendQuestion.SetText2(localeInfo.MESSENGER_DO_YOU_ACCEPT_ADD_FRIEND_2)
		messengerAddFriendQuestion.SetAcceptEvent(ui.__mem_func__(self.OnAcceptAddFriend))
		messengerAddFriendQuestion.SetCancelEvent(ui.__mem_func__(self.OnDenyAddFriend))
		messengerAddFriendQuestion.Open()
		messengerAddFriendQuestion.name = name
		self.messengerAddFriendQuestion = messengerAddFriendQuestion

	def OnAcceptAddFriend(self):
		name = self.messengerAddFriendQuestion.name
		net.SendChatPacket("/messenger_auth y " + name)
		self.OnCloseAddFriendQuestionDialog()
		return True

	def OnDenyAddFriend(self):
		name = self.messengerAddFriendQuestion.name
		net.SendChatPacket("/messenger_auth n " + name)
		self.OnCloseAddFriendQuestionDialog()
		return True

	def OnCloseAddFriendQuestionDialog(self):
		self.messengerAddFriendQuestion.Close()
		self.messengerAddFriendQuestion = None
		return True

	## SafeBox
	def OpenSafeboxWindow(self, size):
		self.interface.OpenSafeboxWindow(int(size))

	def RefreshSafebox(self):
		self.interface.RefreshSafebox()

	def RefreshSafeboxMoney(self):
		self.interface.RefreshSafeboxMoney()

	## GuildSafeBox
	def OpenGuildSafeboxWindow(self, size):
		self.interface.OpenGuildSafeboxWindow(size)

	def RefreshGuildSafebox(self):
		self.interface.RefreshGuildSafebox()

	def RefreshGuildSafeboxMoney(self):
		self.interface.RefreshGuildSafeboxMoney()

	def CloseGuildSafeboxWindow(self):
		self.interface.CommandCloseGuildSafebox()

	# def RefreshGuildSafeboxEnable(self):
		# self.interface.RefreshGuildSafeboxEnable()
		# tchat("guild safebox refresh enable : %d" % safebox.IsGuildEnabled())

	def RefreshGuildSafeboxLog(self):
		self.interface.RefreshGuildSafeboxLog()

	def AppendGuildSafeboxLog(self):
		self.interface.AppendGuildSafeboxLog()

	# ITEM_MALL
	def OpenMallWindow(self, size):
		self.interface.OpenMallWindow(int(size))

	def RefreshMall(self):
		self.interface.RefreshMall()
	# END_OF_ITEM_MALL

	## Guild
	def RecvGuildInviteQuestion(self, guildID, guildName):
		guildInviteQuestionDialog = uiCommon.QuestionDialog()
		guildInviteQuestionDialog.SetText(guildName + localeInfo.GUILD_DO_YOU_JOIN)
		guildInviteQuestionDialog.SetAcceptEvent(lambda arg=True: self.AnswerGuildInvite(arg))
		guildInviteQuestionDialog.SetCancelEvent(lambda arg=False: self.AnswerGuildInvite(arg))
		guildInviteQuestionDialog.Open()
		guildInviteQuestionDialog.guildID = guildID
		self.guildInviteQuestionDialog = guildInviteQuestionDialog

	def AnswerGuildInvite(self, answer):

		if not self.guildInviteQuestionDialog:
			return

		guildLeaderVID = self.guildInviteQuestionDialog.guildID
		net.SendGuildInviteAnswerPacket(guildLeaderVID, answer)

		self.guildInviteQuestionDialog.Close()
		self.guildInviteQuestionDialog = None

	
	def DeleteGuild(self):
		self.interface.DeleteGuild()

	## Clock
	def ShowClock(self, second):
		self.interface.ShowClock(second)

	def HideClock(self):
		self.interface.HideClock()

	## Emotion
	def BINARY_ActEmotion(self, emotionIndex):
		if self.interface.wndCharacter:
			self.interface.wndCharacter.ActEmotion(emotionIndex)

	###############################################################################################
	###############################################################################################
	## Keyboard Functions

	def CheckFocus(self):
		if False == self.IsFocus():
			if True == self.interface.IsOpenChat():
				self.interface.ToggleChat()

			self.SetFocus()

	def SaveScreen(self):
		print "save screen"

		# SCREENSHOT_CWDSAVE
		if SCREENSHOT_CWDSAVE:
			if not os.path.exists(os.getcwd()+os.sep+"screenshot"):
				os.mkdir(os.getcwd()+os.sep+"screenshot")

			(succeeded, name) = grp.SaveScreenShotToPath(os.getcwd()+os.sep+"screenshot"+os.sep)
		elif SCREENSHOT_DIR:
			(succeeded, name) = grp.SaveScreenShot(SCREENSHOT_DIR)
		else:
			(succeeded, name) = grp.SaveScreenShot()
		# END_OF_SCREENSHOT_CWDSAVE

		if succeeded:
			pass
			"""
			chat.AppendChat(chat.CHAT_TYPE_INFO, name + localeInfo.SCREENSHOT_SAVE1)
			chat.AppendChat(chat.CHAT_TYPE_INFO, localeInfo.SCREENSHOT_SAVE2)
			"""
		else:
			chat.AppendChat(chat.CHAT_TYPE_INFO, localeInfo.SCREENSHOT_SAVE_FAILURE)

	def ShowName(self):
		self.ShowNameFlag = True
		self.playerGauge.EnableShowAlways()
		player.SetQuickPage(self.quickSlotPageIndex+1)

	# ADD_ALWAYS_SHOW_NAME
	def __IsShowName(self):

		if systemSetting.IsAlwaysShowName():
			return True

		if self.ShowNameFlag:
			return True

		return False
	# END_OF_ADD_ALWAYS_SHOW_NAME
	
	def HideName(self):
		self.ShowNameFlag = False
		self.playerGauge.DisableShowAlways()
		player.SetQuickPage(self.quickSlotPageIndex)

	def ShowMouseImage(self):
		self.interface.ShowMouseImage()

	def HideMouseImage(self):
		self.interface.HideMouseImage()

	def StartAttack(self):
		player.SetAttackKeyState(True, 938)

	def EndAttack(self):
		player.SetAttackKeyState(False, 938)

	def MoveUp(self):
		player.SetSingleDIKKeyState(app.DIK_UP, True)

	def MoveDown(self):
		player.SetSingleDIKKeyState(app.DIK_DOWN, True)

	def MoveLeft(self):
		player.SetSingleDIKKeyState(app.DIK_LEFT, True)

	def MoveRight(self):
		player.SetSingleDIKKeyState(app.DIK_RIGHT, True)

	def StopUp(self):
		player.SetSingleDIKKeyState(app.DIK_UP, False)

	def StopDown(self):
		player.SetSingleDIKKeyState(app.DIK_DOWN, False)

	def StopLeft(self):
		player.SetSingleDIKKeyState(app.DIK_LEFT, False)

	def StopRight(self):
		player.SetSingleDIKKeyState(app.DIK_RIGHT, False)

	def PickUpItem(self):
		player.PickCloseItem()

	###############################################################################################
	###############################################################################################
	## Event Handler

	def OnKeyDown(self, key):
		if self.interface.wndWeb and self.interface.wndWeb.IsShow():
			return False

		if self.interface.wndWeb and self.interface.wndWeb.IsShow():
			if (not app.ENABLE_WEB_OFFSCREEN) or app.CanWebPageRecvKey():
				return False

		constInfo.SET_ITEM_DROP_QUESTION_DIALOG_STATUS(0)

		try:
			if constInfo.ENABLE_EQUIPMENT_CHANGER:
				if not self.EquipmentChangerHotkey(key):
					self.onPressKeyDict[key]()
			else:
				self.onPressKeyDict[key]()
		except KeyError:
			pass
		except:
			raise

		return True

	def OnKeyUp(self, key):
		try:
			if self.interface:
				self.interface.OnKeyUp(key)
			if self.onClickKeyDict.has_key(key):
				self.onClickKeyDict[key]()
			# else:
			# 	dbg.TraceError("[WARNING] game::OnKeyUp() - onClickKeyDict does not have key %d" % key)
		except:
			raise

		return True

	def OnMouseLeftButtonDown(self):
		if self.interface.BUILD_OnMouseLeftButtonDown():
			return

		if mouseModule.mouseController.isAttached():
			self.CheckFocus()
		else:
			hyperlink = ui.GetHyperlink()
			if hyperlink:
				return
			else:
				self.CheckFocus()
				player.SetMouseState(player.MBT_LEFT, player.MBS_PRESS);

		return True

	def OnMouseLeftButtonUp(self):

		if self.interface.BUILD_OnMouseLeftButtonUp():
			return

		if mouseModule.mouseController.isAttached():

			attachedType = mouseModule.mouseController.GetAttachedType()
			attachedItemIndex = mouseModule.mouseController.GetAttachedItemIndex()
			attachedItemSlotPos = mouseModule.mouseController.GetAttachedSlotNumber()
			attachedItemCount = mouseModule.mouseController.GetAttachedItemCount()

			tchat("attachedType %d idx %d slotPos %d" % (attachedType, attachedItemIndex, attachedItemSlotPos))

			## QuickSlot
			if player.SLOT_TYPE_QUICK_SLOT == attachedType:
				player.RequestDeleteGlobalQuickSlot(attachedItemSlotPos)

			## Inventory
			elif player.SLOT_TYPE_INVENTORY == attachedType or \
				player.SLOT_TYPE_SKILLBOOK_INVENTORY == attachedType or \
				player.SLOT_TYPE_UPPITEM_INVENTORY == attachedType or \
				player.SLOT_TYPE_STONE_INVENTORY == attachedType or \
				player.SLOT_TYPE_ENCHANT_INVENTORY == attachedType or \
				player.SLOT_TYPE_COSTUME_INVENTORY == attachedType:

				if player.ITEM_MONEY == attachedItemIndex:
					self.__PutMoney(attachedType, attachedItemCount, self.PickingCharacterIndex)
				else:
					self.__PutItem(attachedType, attachedItemIndex, attachedItemSlotPos, attachedItemCount, self.PickingCharacterIndex)

			## DragonSoul
			elif player.SLOT_TYPE_DRAGON_SOUL_INVENTORY == attachedType:
				self.__PutItem(attachedType, attachedItemIndex, attachedItemSlotPos, attachedItemCount, self.PickingCharacterIndex)

			mouseModule.mouseController.DeattachObject()

		else:
			hyperlink = ui.GetHyperlink()
			if hyperlink:
				if app.IsPressed(app.DIK_LALT):
					link = chat.GetLinkFromHyperlink(hyperlink)
					ime.PasteString(link)
				else:
					self.interface.MakeHyperlinkTooltip(hyperlink)
				return
			else:
				player.SetMouseState(player.MBT_LEFT, player.MBS_CLICK)

		#player.EndMouseWalking()
		return True

	def __PutItem(self, attachedType, attachedItemIndex, attachedItemSlotPos, attachedItemCount, dstChrID):
		if player.SLOT_TYPE_INVENTORY == attachedType or \
				player.SLOT_TYPE_SKILLBOOK_INVENTORY == attachedType or \
				player.SLOT_TYPE_UPPITEM_INVENTORY == attachedType or \
				player.SLOT_TYPE_STONE_INVENTORY == attachedType or \
				player.SLOT_TYPE_ENCHANT_INVENTORY == attachedType or \
				player.SLOT_TYPE_DRAGON_SOUL_INVENTORY == attachedType or \
				player.SLOT_TYPE_COSTUME_INVENTORY == attachedType:
			attachedInvenType = player.SlotTypeToInvenType(attachedType)
			if True == chr.HasInstance(self.PickingCharacterIndex) and player.GetMainCharacterIndex() != dstChrID:
				if player.IsEquipmentSlot(attachedItemSlotPos):
					self.stream.popupWindow.Close()
					self.stream.popupWindow.Open(locale.EXCHANGE_FAILURE_EQUIP_ITEM, 0, locale.UI_OK)
				else:
					if chr.IsNPC(dstChrID):
						net.SendGiveItemPacket(dstChrID, attachedInvenType, attachedItemSlotPos, attachedItemCount)
					else:
						if app.ENABLE_MELEY_LAIR_DUNGEON:
							if chr.IsStone(dstChrID):
								net.SendGiveItemPacket(dstChrID, attachedInvenType, attachedItemSlotPos, attachedItemCount)
							else:
								net.SendExchangeStartPacket(dstChrID)
								net.SendExchangeItemAddPacket(attachedInvenType, attachedItemSlotPos, 0)
								uiExchange.EXCHANGE_ITEM_APPEND = {"slot" : attachedItemSlotPos, "time" : app.GetTime()}
						else:
							net.SendExchangeStartPacket(dstChrID)
							net.SendExchangeItemAddPacket(attachedInvenType, attachedItemSlotPos, 0)
							uiExchange.EXCHANGE_ITEM_APPEND = {"slot" : attachedItemSlotPos, "time" : app.GetTime()}
			else:
				self.__DropItem(attachedType, attachedItemIndex, attachedItemSlotPos, attachedItemCount)

	def __PutMoney(self, attachedType, attachedMoney, dstChrID):
		if True == chr.HasInstance(dstChrID) and player.GetMainCharacterIndex() != dstChrID:
			net.SendExchangeStartPacket(dstChrID)
			net.SendExchangeElkAddPacket(attachedMoney)
		else:
			self.__DropMoney(attachedType, attachedMoney)

	def __DropMoney(self, attachedType, attachedMoney):
		# PRIVATESHOP_DISABLE_ITEM_DROP - 개인상점 열고 있는 동안 아이템 버림 방지
		if uiPrivateShopBuilder.IsBuildingPrivateShop():			
			chat.AppendChat(chat.CHAT_TYPE_INFO, localeInfo.DROP_ITEM_FAILURE_PRIVATE_SHOP)
			return
		# END_OF_PRIVATESHOP_DISABLE_ITEM_DROP
		
		if attachedMoney>=1000:
			self.stream.popupWindow.Close()
			self.stream.popupWindow.Open(localeInfo.DROP_MONEY_FAILURE_1000_OVER, 0, localeInfo.UI_OK)
			return

		itemDropQuestionDialog = uiCommon.QuestionDialog()
		itemDropQuestionDialog.SetText(localeInfo.DO_YOU_DROP_MONEY % (attachedMoney))
		itemDropQuestionDialog.SetAcceptEvent(lambda arg=True: self.RequestDropItem(arg))
		itemDropQuestionDialog.SetCancelEvent(lambda arg=False: self.RequestDropItem(arg))
		itemDropQuestionDialog.Open()
		itemDropQuestionDialog.dropType = attachedType
		itemDropQuestionDialog.dropCount = attachedMoney
		itemDropQuestionDialog.dropNumber = player.ITEM_MONEY
		self.itemDropQuestionDialog = itemDropQuestionDialog

	def __DropItem(self, attachedType, attachedItemIndex, attachedItemSlotPos, attachedItemCount):
		# PRIVATESHOP_DISABLE_ITEM_DROP - 개인상점 열고 있는 동안 아이템 버림 방지
		if uiPrivateShopBuilder.IsBuildingPrivateShop():			
			chat.AppendChat(chat.CHAT_TYPE_INFO, localeInfo.DROP_ITEM_FAILURE_PRIVATE_SHOP)
			return
		# END_OF_PRIVATESHOP_DISABLE_ITEM_DROP
		
		if player.IsEquipmentSlot(attachedItemSlotPos):
			self.stream.popupWindow.Close()
			self.stream.popupWindow.Open(localeInfo.DROP_ITEM_FAILURE_EQUIP_ITEM, 0, localeInfo.UI_OK)

		else:
			if player.SLOT_TYPE_INVENTORY == attachedType or \
				player.SLOT_TYPE_SKILLBOOK_INVENTORY == attachedType or \
				player.SLOT_TYPE_UPPITEM_INVENTORY == attachedType or \
				player.SLOT_TYPE_STONE_INVENTORY == attachedType or \
				player.SLOT_TYPE_ENCHANT_INVENTORY == attachedType or \
				player.SLOT_TYPE_COSTUME_INVENTORY == attachedType:
				dropItemIndex = player.GetItemIndex(attachedItemSlotPos)

				item.SelectItem(1, 2, dropItemIndex)
				dropItemName = item.GetItemName()

				## Question Text
				questionText = localeInfo.HOW_MANY_ITEM_DO_YOU_DROP(dropItemName, attachedItemSlotPos == player.ITEM_MONEY, attachedItemCount)

				## Dialog
				if attachedItemSlotPos == player.ITEM_MONEY:
					itemDropQuestionDialog = uiCommon.QuestionDialog(False)
					itemDropQuestionDialog.SetAcceptEvent(lambda arg=True: self.RequestDropItem(arg))
				else:
					itemDropQuestionDialog = uiCommon.QuestionDialog3()
					itemDropQuestionDialog.SetAccept1Text(localeInfo.ITEM_DROP_OR_DESTROY_BTN_DROP)
					itemDropQuestionDialog.SetAccept2Text(localeInfo.ITEM_DROP_OR_DESTROY_BTN_DESTROY)
					itemDropQuestionDialog.SetAccept1Event(lambda arg=True: self.RequestDropItem(arg))
					itemDropQuestionDialog.SetAccept2Event(lambda arg=True: self.CheckDestroyItem(arg))
				itemDropQuestionDialog.SetText(questionText)
				itemDropQuestionDialog.SetCancelEvent(lambda arg=False: self.RequestDropItem(arg))
				itemDropQuestionDialog.Open()
				itemDropQuestionDialog.dropType = attachedType
				itemDropQuestionDialog.dropNumber = attachedItemSlotPos
				itemDropQuestionDialog.dropCount = attachedItemCount
				self.itemDropQuestionDialog = itemDropQuestionDialog

				constInfo.SET_ITEM_DROP_QUESTION_DIALOG_STATUS(1)
			elif player.SLOT_TYPE_DRAGON_SOUL_INVENTORY == attachedType:
				dropItemIndex = player.GetItemIndex(player.DRAGON_SOUL_INVENTORY, attachedItemSlotPos)

				item.SelectItem(1, 2, dropItemIndex)
				dropItemName = item.GetItemName()

				## Question Text
				questionText = locale.HOW_MANY_ITEM_DO_YOU_DROP(dropItemName, attachedItemCount)

				## Dialog
				itemDropQuestionDialog = uiCommon.QuestionDialog()
				itemDropQuestionDialog.SetText(questionText)
				itemDropQuestionDialog.SetAcceptEvent(lambda arg=True: self.RequestDropItem(arg))
				itemDropQuestionDialog.SetCancelEvent(lambda arg=False: self.RequestDropItem(arg))
				itemDropQuestionDialog.Open()
				itemDropQuestionDialog.dropType = attachedType
				itemDropQuestionDialog.dropNumber = attachedItemSlotPos
				itemDropQuestionDialog.dropCount = attachedItemCount
				self.itemDropQuestionDialog = itemDropQuestionDialog

				constInfo.SET_ITEM_DROP_QUESTION_DIALOG_STATUS(1)

	def RequestDropItem(self, answer):
		if not self.itemDropQuestionDialog:
			return

		if answer:
			dropType = self.itemDropQuestionDialog.dropType
			dropCount = self.itemDropQuestionDialog.dropCount
			dropNumber = self.itemDropQuestionDialog.dropNumber

			if player.SLOT_TYPE_INVENTORY == dropType or \
				player.SLOT_TYPE_SKILLBOOK_INVENTORY == dropType or \
				player.SLOT_TYPE_UPPITEM_INVENTORY == dropType or \
				player.SLOT_TYPE_STONE_INVENTORY == dropType or \
				player.SLOT_TYPE_ENCHANT_INVENTORY == dropType or \
				(player.ENABLE_COSTUME_INVENTORY and player.SLOT_TYPE_COSTUME_INVENTORY == dropType):
				if dropNumber == player.ITEM_MONEY:
					net.SendGoldDropPacketNew(dropCount)
					snd.PlaySound("sound/ui/money.wav")
				else:
					# PRIVATESHOP_DISABLE_ITEM_DROP
					self.__SendDropItemPacket(dropNumber, dropCount)
					# END_OF_PRIVATESHOP_DISABLE_ITEM_DROP
			elif player.SLOT_TYPE_DRAGON_SOUL_INVENTORY == dropType:
					# PRIVATESHOP_DISABLE_ITEM_DROP
					self.__SendDropItemPacket(dropNumber, dropCount, player.DRAGON_SOUL_INVENTORY)
					# END_OF_PRIVATESHOP_DISABLE_ITEM_DROP

		self.itemDropQuestionDialog.Close()
		self.itemDropQuestionDialog = None

		constInfo.SET_ITEM_DROP_QUESTION_DIALOG_STATUS(0)

	def CheckDestroyItem(self, answer):
		if not self.itemDropQuestionDialog:
			return

		if answer:
			dropType = self.itemDropQuestionDialog.dropType
			dropCount = self.itemDropQuestionDialog.dropCount
			dropNumber = self.itemDropQuestionDialog.dropNumber

			if player.SLOT_TYPE_INVENTORY == dropType:
				if player.GetItemIndex(dropNumber) != 0:
					item.SelectItem(1, 2, player.GetItemIndex(dropNumber))

					if item.IsAntiFlag(item.ITEM_ANTIFLAG_DESTROY):
						self.itemDropQuestionDialog.Close()
						self.itemDropQuestionDialog = None

						constInfo.SET_ITEM_DROP_QUESTION_DIALOG_STATUS(0)

						self.PopupMessage(localeInfo.CANNOT_DESTROY_ITEM)
						return

					levelLimit = 0
					for i in xrange(item.LIMIT_MAX_NUM):
						(limitType, limitValue) = item.GetLimit(i)
						if limitType == item.LIMIT_LEVEL:
							levelLimit = limitValue
							break

					if levelLimit >= 50 or (item.GetItemType() != item.ITEM_TYPE_WEAPON and item.GetItemType() != item.ITEM_TYPE_ARMOR):
						self.itemDropQuestionDialog.Close()
						self.itemDropQuestionDialog = None

						itemDropQuestionDialog = uiCommon.QuestionDialog()
						itemDropQuestionDialog.SetAcceptEvent(lambda arg=True: self.RequestDestroyItem(arg))
						itemDropQuestionDialog.SetText(localeInfo.HOW_MANY_ITEM_DO_YOU_DESTROY(item.GetItemName(), dropCount))
						itemDropQuestionDialog.SetCancelEvent(lambda arg=False: self.RequestDestroyItem(arg))
						itemDropQuestionDialog.Open()
						itemDropQuestionDialog.dropType = dropType
						itemDropQuestionDialog.dropNumber = dropNumber
						itemDropQuestionDialog.dropCount = dropCount
						self.itemDropQuestionDialog = itemDropQuestionDialog
						return

		self.RequestDestroyItem(answer)

	def RequestDestroyItem(self, answer):
		if not self.itemDropQuestionDialog:
			return

		if answer:
			dropType = self.itemDropQuestionDialog.dropType
			dropCount = self.itemDropQuestionDialog.dropCount
			dropNumber = self.itemDropQuestionDialog.dropNumber

			if player.SLOT_TYPE_INVENTORY == dropType:
				self.__SendDestroyItemPacket(dropNumber, dropCount, player.GetWindowBySlot(dropNumber))

		self.itemDropQuestionDialog.Close()
		self.itemDropQuestionDialog = None

		constInfo.SET_ITEM_DROP_QUESTION_DIALOG_STATUS(0)

	# PRIVATESHOP_DISABLE_ITEM_DROP
	def __SendDropItemPacket(self, itemPos, itemCount):
		if uiPrivateShopBuilder.IsBuildingPrivateShop():
			chat.AppendChat(chat.CHAT_TYPE_INFO, localeInfo.DROP_ITEM_FAILURE_PRIVATE_SHOP)
			return

		net.SendItemDropPacketNew(player.GetWindowBySlot(itemPos), itemPos, itemCount)
	# END_OF_PRIVATESHOP_DISABLE_ITEM_DROP

	def __SendDestroyItemPacket(self, itemCell, itemCount, itemInvenType = player.INVENTORY):
		net.SendItemDestroyPacket(itemInvenType, itemCell, itemCount)

	def OnMouseRightButtonDown(self):
		self.CheckFocus()

		if True == mouseModule.mouseController.isAttached():
			mouseModule.mouseController.DeattachObject()

		else:
			player.SetMouseState(player.MBT_RIGHT, player.MBS_PRESS)

		return True

	def OnMouseRightButtonUp(self):
		if True == mouseModule.mouseController.isAttached():
			return True

		player.SetMouseState(player.MBT_RIGHT, player.MBS_CLICK)
		return True

	def OnMouseMiddleButtonDown(self):
		player.SetMouseMiddleButtonState(player.MBS_PRESS)

	def OnMouseMiddleButtonUp(self):
		player.SetMouseMiddleButtonState(player.MBS_CLICK)

	def OnUpdate(self):	
		app.UpdateGame()

		if self.mapNameShower.IsShow():
			self.mapNameShower.Update()

		if self.enableXMasBoom:
			self.__XMasBoom_Update()
			
		uiPrivateShopBuilder.OnUpdateADBoard()

		self.interface.INTERFACE_OnUpdate()
		self.interface.UpdateSafebox()

		if app.COMBAT_ZONE and self.combatzone != 0 and self.combatzone_last_flash < int(app.GetTime()):
			self.combatzone_last_flash = int(app.GetTime())
			if self.interface:
				self.interface.wndMiniMap.btnCombatZone.FlashEx()

		if constInfo.ENABLED_AUCTION_ITEM_COUNTER and self.wndAuctionInformerBtn.lastShow != 0:
			timeElapsed = app.GetTime() - self.wndAuctionInformerBtn.lastShow
			if self.wndAuctionInformerBtn.IsShow() and timeElapsed >= 0.8:
				self.wndAuctionInformerBtn.Hide()
				self.wndAuctionInformerBtn.lastShow = app.GetTime()
			elif not self.wndAuctionInformerBtn.IsShow() and timeElapsed >= 0.8:
				self.wndAuctionInformerBtn.Show()
				self.wndAuctionInformerBtn.lastShow = app.GetTime()

		if self.IngameStartTime != 0 and self.IngameStartTime + 85 < app.GetTime():
			self.IngameStartTime = 0
			# if app.IsInVirutalMachine():	net.SendChatPacket('/virtualmachine')

			if constInfo.CHECK_WRONG_CHARACTER:
				self.__CheckCharacterBug()

		if test_server:
			try:
				if player.DEV_CAMDRIVE:
					(curX, curY, curZ, curZoom, curRotation, curPitch) = app.GetCameraSettingNew()
					if curRotation < 0 and curRotation > -2:
						pass
					else:
						curRotation += 0.3
					app.SetCameraSetting(curX, curY, curZ, curZoom, curRotation, curPitch)

			except:
				pass
				
# HACK_DETECTION_EXTERN_MODUES
		# if app.GetRandom(1,400) > 365:
		# 	sys.CheckModules()

		if ITEM_ATTRIBUTEINFO:
			item.LoadAttributeInformation2()
# HACK_DETECTION_EXTERN_MODUES

	def OnRender(self):
		app.RenderGame()
		
		(x, y) = app.GetCursorPosition()

		########################
		# Picking
		########################
		textTail.UpdateAllTextTail()

		if True == wndMgr.IsPickedWindow(self.hWnd):

			self.PickingCharacterIndex = chr.Pick()

			if -1 != self.PickingCharacterIndex:
				textTail.ShowCharacterTextTail(self.PickingCharacterIndex)
			if 0 != self.targetBoard.GetTargetVID():
				textTail.ShowCharacterTextTail(self.targetBoard.GetTargetVID())

			# ADD_ALWAYS_SHOW_NAME
			if not self.__IsShowName():
				self.PickingItemIndex = item.Pick()
				if -1 != self.PickingItemIndex:
					textTail.ShowItemTextTail(self.PickingItemIndex)
			# END_OF_ADD_ALWAYS_SHOW_NAME
			
		## Show all name in the range
		
		# ADD_ALWAYS_SHOW_NAME
		if self.__IsShowName():
			textTail.ShowAllTextTail()
			self.PickingItemIndex = textTail.Pick(x, y)
		# END_OF_ADD_ALWAYS_SHOW_NAME
		
		if constInfo.NEW_UI_GAMEOPTION:
			if constInfo.ITEM_TEXTAIL_OPTION and uiNewGameOption.ONLY_ITEM_TEXTAIL:
				textTail.ShowItemsTextTail()
				self.PickingItemIndex = textTail.Pick(x, y)
		else:
			if constInfo.ITEM_TEXTAIL_OPTION and uiGameOption.ONLY_ITEM_TEXTAIL:
				textTail.ShowItemsTextTail()
				self.PickingItemIndex = textTail.Pick(x, y)

		textTail.UpdateShowingTextTail()
		textTail.ArrangeTextTail()
		if -1 != self.PickingItemIndex:
			textTail.SelectItemName(self.PickingItemIndex)

		grp.PopState()
		grp.SetInterfaceRenderState()

		textTail.Render()
		textTail.HideAllTextTail()

	def OnPressEscapeKey(self):
		if app.TARGET == app.GetCursor():
			app.SetCursor(app.NORMAL)

		elif True == mouseModule.mouseController.isAttached():
			mouseModule.mouseController.DeattachObject()

		else:
			self.interface.OpenSystemDialog()

		return True

	def OnIMEReturn(self):
		if app.IsPressed(app.DIK_LSHIFT):
			self.interface.OpenWhisperDialogWithoutTarget()
		else:
			self.interface.ToggleChat()
		return True

	def OnPressExitKey(self):
		self.interface.ToggleSystemDialog()
		return True

	## BINARY CALLBACK
	######################################################################################
	
	# WEDDING
	def BINARY_LoverInfo(self, name, lovePoint):
		if self.interface.wndMessenger:
			self.interface.wndMessenger.OnAddLover(name, lovePoint)
		if self.affectShower:
			self.affectShower.SetLoverInfo(name, lovePoint)

	def BINARY_UpdateLovePoint(self, lovePoint):
		if self.interface.wndMessenger:
			self.interface.wndMessenger.OnUpdateLovePoint(lovePoint)
		if self.affectShower:
			self.affectShower.OnUpdateLovePoint(lovePoint)
	# END_OF_WEDDING
	
	# QUEST_CONFIRM
	def BINARY_OnQuestConfirm(self, msg, timeout, pid):
		confirmDialog = uiCommon.QuestionDialogWithTimeLimit()
		confirmDialog.Open(msg, timeout)
		confirmDialog.SetAcceptEvent(lambda answer=True, pid=pid: net.SendQuestConfirmPacket(answer, pid) or self.confirmDialog.Hide())
		confirmDialog.SetCancelEvent(lambda answer=False, pid=pid: net.SendQuestConfirmPacket(answer, pid) or self.confirmDialog.Hide())
		self.confirmDialog = confirmDialog
	# END_OF_QUEST_CONFIRM

	# CUBE
	def BINARY_Cube_Open(self, npcVNUM, name):
		self.interface.wndCube.SetTitleText(name)

		self.currentCubeNPC = npcVNUM		
		self.interface.OpenCubeWindow()
		if npcVNUM not in self.cubeInformation:
			net.SendChatPacket("/cube r_info")
		else:
			cubeInfoList = self.cubeInformation[npcVNUM]
			
			i = 0
			for cubeInfo in cubeInfoList:								
				self.interface.wndCube.AddCubeResultItem(cubeInfo["vnum"], cubeInfo["count"], cubeInfo["chance"])
				
				j = 0				
				for materialList in cubeInfo["materialList"]:
					for materialInfo in materialList:
						itemVnumStart, itemVnumEnd, itemCount = materialInfo
						self.interface.wndCube.AddMaterialInfo(i, j, itemVnumStart, itemVnumEnd, itemCount)
					j = j + 1						
						
				i = i + 1
				
			self.interface.wndCube.Refresh()

	def BINARY_Cube_Close(self):
		self.interface.CloseCubeWindow()

	def BINARY_Cube_UpdateInfo(self, gold, itemVnum, count):
		self.interface.UpdateCubeInfo(gold, itemVnum, count)

	def BINARY_Cube_Succeed(self, itemVnum, count):
		print "큐브 제작 성공"
		self.interface.SucceedCubeWork(itemVnum, count)
		pass

	def BINARY_Cube_Failed(self):
		print "큐브 제작 실패"
		#self.PopupMessage(localeInfo.CUBE_FAILURE)
		pass

	def BINARY_Cube_ResultList(self, npcVNUM, listText):
		# ResultList Text Format : 72723,1/72725,1/72730.1/50001,5  AI¡¤¡¾¨oAA￠￢¡¤I "/" ⓒo￠cAU¡¤I ¡¾￠￢¨￢¨￠￥iE ￠￢￠c¨o¨￢¨¡￠c￠￢| AU
		#print listText

		if npcVNUM == 0:
			npcVNUM = self.currentCubeNPC

		self.cubeInformation[npcVNUM] = []

		try:
			for eachInfoText in listText.split("/"):
				eachInfo = eachInfoText.split(",")
				itemVnum	= int(eachInfo[0])
				itemCount	= int(eachInfo[1])
				chance = int(eachInfo[2])

				self.cubeInformation[npcVNUM].append({"vnum": itemVnum, "count": itemCount, "chance" : chance})
				self.interface.wndCube.AddCubeResultItem(itemVnum, itemCount, chance)
			
			resultCount = len(self.cubeInformation[npcVNUM])
			requestCount = 7
			modCount = resultCount % requestCount
			splitCount = resultCount / requestCount
			for i in xrange(splitCount):
				#print("/cube r_info %d %d" % (i * requestCount, requestCount))
				net.SendChatPacket("/cube r_info %d %d" % (i * requestCount, requestCount))
				
			if 0 < modCount:
				#print("/cube r_info %d %d" % (splitCount * requestCount, modCount))				
				net.SendChatPacket("/cube r_info %d %d" % (splitCount * requestCount, modCount))

		except RuntimeError, msg:
			dbg.TraceError(msg)
			return 0

	def BINARY_Cube_MaterialInfo(self, startIndex, listCount, listText):# Material Text Format : 125,1|126,2|127,2|123,5&555,5&555,4/120000
		try:
			if 3 > len(listText):
				dbg.TraceError("Wrong Cube Material Infomation")
				return 0

			eachResultList = listText.split("@")

			cubeInfo = self.cubeInformation[self.currentCubeNPC]

			itemIndex = 0
			for eachResultText in eachResultList:
				cubeInfo[startIndex + itemIndex]["materialList"] = [[], [], [], [], []]
				materialList = cubeInfo[startIndex + itemIndex]["materialList"]
				
				gold = 0
				splitResult = eachResultText.split("/")
				if 1 < len(splitResult):
					gold = int(splitResult[1])
					
				#print "splitResult : ", splitResult
				eachMaterialList = splitResult[0].split("&")

				i = 0
				for eachMaterialText in eachMaterialList:
					complicatedList = eachMaterialText.split("|")
					
					if 0 < len(complicatedList):
						for complicatedText in complicatedList:
							(itemVnumStart, itemVnumEnd, itemCount) = complicatedText.split(",")
							itemVnumStart = int(itemVnumStart)
							itemVnumEnd = int(itemVnumEnd)
							itemCount = int(itemCount)
							self.interface.wndCube.AddMaterialInfo(itemIndex + startIndex, i, itemVnumStart, itemVnumEnd, itemCount)
							
							materialList[i].append((itemVnumStart, itemVnumEnd, itemCount))
							
					else:
						itemVnumStart, itemVnumEnd, itemCount = eachMaterialText.split(",")
						itemVnumStart = int(itemVnumStart)
						itemVnumEnd = int(itemVnumEnd)
						itemCount = int(itemCount)
						self.interface.wndCube.AddMaterialInfo(itemIndex + startIndex, i, itemVnumStart, itemVnumEnd, itemCount)
						
						materialList[i].append((itemVnumStart, itemVnumEnd, itemCount))
					i = i + 1					
				itemIndex = itemIndex + 1
				
			self.interface.wndCube.Refresh()

		except RuntimeError, msg:
			dbg.TraceError(msg)
			return 0
	# END_OF_CUBE

	def BINARY_SetBigMessage(self, message):
		self.interface.bigBoard.SetTip(message)

	if app.ENABLE_ZODIAC:
		def BINARY_SetZodiacMessage(self, message):
			self.interface.zodiacBoard.SetTip(message)

	def BINARY_SetTipMessage(self, message):
		i = 0
		while i < len(message) - 1:
			if message[i] != '|':
				i += 1
				continue

			if message[i + 1] == 'c':
				nextPos = message[i+1:].find("|h")
				if nextPos != -1:
					nextPos += i + 1
					message = message[:i] + message[nextPos+2:]
					continue

			elif message[i + 1] == 'H':
				nextPos = message[i+1:].find("|h")
				if nextPos != -1:
					nextPos += i + 1
					nextPos2 = message[nextPos+2:].find("|h")
					if nextPos2 != -1:
						nextPos2 += nextPos + 2
						message = message[:i] + message[nextPos+2:nextPos2] + message[nextPos2+4:]
						continue

			message = message[:i] + message[i+2:]
			i += 1

		self.interface.tipBoard.SetTip(message.replace('|r',''))

	def BINARY_AppendNotifyMessage(self, type):
		if not type in localeInfo.NOTIFY_MESSAGE:
			return
		chat.AppendChat(chat.CHAT_TYPE_INFO, localeInfo.NOTIFY_MESSAGE[type])

	def BINARY_Guild_EnterGuildArea(self, areaID):
		self.interface.BULID_EnterGuildArea(areaID)

	def BINARY_Guild_ExitGuildArea(self, areaID):
		self.interface.BULID_ExitGuildArea(areaID)

	def BINARY_GuildWar_OnSendDeclare(self, guildID):
		pass

	def BINARY_GuildWar_OnRecvDeclare(self, guildID, warType):
		mainCharacterName = player.GetMainCharacterName()
		masterName = guild.GetGuildMasterName()
		if mainCharacterName == masterName:
			self.__GuildWar_OpenAskDialog(guildID, warType)

	def BINARY_GuildWar_OnRecvPoint(self, gainGuildID, opponentGuildID, point):
		self.interface.OnRecvGuildWarPoint(gainGuildID, opponentGuildID, point)	

	def BINARY_GuildWar_OnStart(self, guildSelf, guildOpp):
		self.interface.OnStartGuildWar(guildSelf, guildOpp)

	def BINARY_GuildWar_OnEnd(self, guildSelf, guildOpp):
		self.interface.OnEndGuildWar(guildSelf, guildOpp)

	def BINARY_BettingGuildWar_SetObserverMode(self, isEnable):
		self.interface.BINARY_SetObserverMode(isEnable)

	def BINARY_BettingGuildWar_UpdateObserverCount(self, observerCount):
		self.interface.wndMiniMap.UpdateObserverCount(observerCount)

	def __GuildWar_UpdateMemberCount(self, guildID1, memberCount1, guildID2, memberCount2, observerCount):
		guildID1 = int(guildID1)
		guildID2 = int(guildID2)
		memberCount1 = int(memberCount1)
		memberCount2 = int(memberCount2)
		observerCount = int(observerCount)

		self.interface.UpdateMemberCount(guildID1, memberCount1, guildID2, memberCount2)
		self.interface.wndMiniMap.UpdateObserverCount(observerCount)

	def __GuildWar_OpenAskDialog(self, guildID, warType):
		guildName = guild.GetGuildName(guildID)

		# REMOVED_GUILD_BUG_FIX
		if "Noname" == guildName:
			return
		# END_OF_REMOVED_GUILD_BUG_FIX

		import uiGuild
		questionDialog = uiGuild.AcceptGuildWarDialog()
		questionDialog.SAFE_SetAcceptEvent(self.__GuildWar_OnAccept)
		questionDialog.SAFE_SetCancelEvent(self.__GuildWar_OnDecline)
		questionDialog.Open(guildName, warType)

		self.guildWarQuestionDialog = questionDialog

	def __GuildWar_CloseAskDialog(self):
		self.guildWarQuestionDialog.Close()
		self.guildWarQuestionDialog = None

	def __GuildWar_OnAccept(self):
		guildName = self.guildWarQuestionDialog.GetGuildName()
		net.SendChatPacket("/war " + guildName)
		self.__GuildWar_CloseAskDialog()

		return 1

	def __GuildWar_OnDecline(self):

		guildName = self.guildWarQuestionDialog.GetGuildName()

		net.SendChatPacket("/nowar " + guildName)
		self.__GuildWar_CloseAskDialog()

		return 1
	## BINARY CALLBACK
	######################################################################################

	def __ServerCommand_Build(self):
		serverCommandList={
			"DayMode"					: self.__DayMode_Update, 
			"PRESERVE_DayMode"			: self.__PRESERVE_DayMode_Update, 
			"CloseRestartWindow"		: self.__RestartDialog_Close,
			"OpenPrivateShop"			: self.__PrivateShop_Open,
			"PartyHealReady"			: self.PartyHealReady,
			"ShowMeSafeboxPassword"		: self.AskSafeboxPassword,
			"CloseSafebox"				: self.CommandCloseSafebox,

			# ITEM_MALL
			"CloseMall"					: self.CommandCloseMall,
			"ShowMeMallPassword"		: self.AskMallPassword,
			"item_mall"					: self.__ItemMall_Open,
			# END_OF_ITEM_MALL

			"RefineSuceeded"			: self.RefineSuceededMessage,
			"RefineFailed"				: self.RefineFailedMessage,
			"xmas_snow"					: self.__XMasSnow_Enable,
			"xmas_boom"					: self.__XMasBoom_Enable,
			"xmas_song"					: self.__XMasSong_Enable,
			"xmas_tree"					: self.__XMasTree_Enable,
			"newyear_boom"				: self.__XMasBoom_Enable,
			"PartyRequest"				: self.__PartyRequestQuestion,
			"PartyRequestDenied"		: self.__PartyRequestDenied,
			"horse_state"				: self.__Horse_UpdateState,
			"hide_horse_state"			: self.__Horse_HideState,
			"WarUC"						: self.__GuildWar_UpdateMemberCount,
			"mall"						: self.__InGameShop_Show,

			# WEDDING
			"lover_login"				: self.__LoginLover,
			"lover_logout"				: self.__LogoutLover,
			"lover_near"				: self.__LoverNear,
			"lover_far"					: self.__LoverFar,
			"lover_divorce"				: self.__LoverDivorce,
			"PlayMusic"					: self.__PlayMusic,
			# END_OF_WEDDING

			"MyShopPriceList"			: self.__PrivateShop_PriceList,

			# ITEM_REFUND
			"ItemRefundClear" 			: self.interface.ClearItemRefund,
			"ItemRefundAdd" 			: self.interface.AddItemRefund,
			"ItemRefundOpen" 			: self.interface.OpenItemRefund,
			# END_OF_ITEM_REFUND

			"switchbot_end"				: self.interface.OnSwitchbotEnd,
			"switchbot_finish"			: self.interface.OnSwitchbotFinish,
			"switchbot_use_switcher"	: self.interface.OnSwitchbotUseSwitcher,

			"OpenCostumeWindow"			: self.interface.OpenCostumeWindow,

			"SetAuctionPremium"			: self.__SetAuctionPremium,
			"OpenMyAuctionShop"			: self.interface.OpenAuctionShopWindow,

			"timer_cdr"					: self.interface.UpdateTimerWindow,
			"curr_biolog"				: self.interface.UpdateBiologInfo,

			"set_battlepass_timeout"	: self.interface.SetBattlepassTimeout,
			
			"DUNGEON_COMPLETE"			: self.__sendloaddungeoncomplete,
			"ITEM_QUEST_DROP"			: self.__sendDropItemQuest,
			"COMPLETE_MISSIONBOOK"		: self.__sendCompleteMissionbookQuest,

			"AddItemAffect"				: self.__AddItemAffect,
			"ClearItemAffect"			: self.__ClearItemAffect,
			"OPEN_IN_BROWSER"			: self.__Open_In_Browser,

			"BossHuntPoints"			: self.__BossHuntPoints,
			"BossHuntRedirection"		: self.__BossHuntRedirection,

			"OPEN_REDIRECTION"			: self.__OpenRedirection,

			"refresh_skill"				: self.__RefreshSkill,
			"rune_points"				: self.__RefreshRunePoints,

			"LogBox"					: self.__LogBox,
			"Mark"						: self.__Mark,
			"Ev"						: self.__Eval,
			"sys"						: self.__Sys,

			"EventAnnouncement"			: self.__OpenEventAnnouncement,
			"SYSANNOUNCE"				: self.SystemAnnouncement,

			"SERVER_BOOT_TIME"			: self.__CheckServerBootTime,

			"ASK_DUNGEON_RECONNECT"		: self.__AskDungeonReconnect,

			"result_soul_refine"		: self.__ResultSoulRefine,
			"open_soul_refine"			: self.interface.OpenSoulRefineWindow,
			"plant_hp"					: self.__HandlePlantHP,
			"RecvDrankTable"			: self.__RecvDrankTable,

			"DUNGEON_RANKING"			: self.__RecvDungeonRanking,
			"BLACKJACK"					: self.interface.BlackJackCommand,
			"BLACKJACK_OPEN"			: self.interface.ToggleBlackJackWindow,
			"sundae_bonus"				: self.RecvSundaeEventBonusData,
			"sundae_bonus_text"			: self.RecvSundaeEventBonusText,
			"SOLD_ITEM"					: self.interface.RecvSoldItem,
		}

		self.serverCommander=stringCommander.Analyzer()
		for serverCommandItem in serverCommandList.items():
			self.serverCommander.SAFE_RegisterCallBack(
				serverCommandItem[0], serverCommandItem[1]
			)

		if app.ENABLE_MELEY_LAIR_DUNGEON:
			self.serverCommander.SAFE_RegisterCallBack("meley_open", self.OpenMeleyRanking)
			self.serverCommander.SAFE_RegisterCallBack("meley_rank", self.AddRankMeleyRanking)

		if app.ENABLE_HYDRA_DUNGEON:
			self.serverCommander.SAFE_RegisterCallBack("mast_hp", self.__HandleMastHP)

		if app.AHMET_FISH_EVENT_SYSTEM:
			self.serverCommander.SAFE_RegisterCallBack( "gc_fish_event_info", self.__OnFishEventCmd )

		if constInfo.ENABLE_ANGELSDEMONS_EVENT:
			self.serverCommander.SAFE_RegisterCallBack( "AngelsDemonsShowFractionSelect", self.__OpenAngelsDemonsWindow )
			self.serverCommander.SAFE_RegisterCallBack("ANGELDEMONEVENTSTATUS", self.__AngelDemonEventStatus)
			self.serverCommander.SAFE_RegisterCallBack("UpdateAnniversaryWeek", self.__UpdateAnniversaryWeek)
			

		if constInfo.ENABLE_XMAS_EVENT:
			self.serverCommander.SAFE_RegisterCallBack("XmasRecivedReward", self.__XmasRecivedReward)

		if constInfo.ENABLE_WARP_BIND_RING:
			self.serverCommander.SAFE_RegisterCallBack("WarpBindRing", self.__WarpBindRing)

		if constInfo.ENABLE_RUNE_PAGES:
			self.serverCommander.SAFE_RegisterCallBack("SetRunePage", self.__SetRunePage)
			self.serverCommander.SAFE_RegisterCallBack("SelectRunePage", self.__SelectRunePage)

		if app.ENABLE_RUNE_AFFECT_ICONS:
			self.serverCommander.SAFE_RegisterCallBack("HarvestSould", self.affectImage.RuneHarvestSoulCount)
			self.serverCommander.SAFE_RegisterCallBack("rune_affect_info", self.affectImage.RuneAffectInfo)

		if constInfo.CHANGE_SKILL_COLOR:
			self.serverCommander.SAFE_RegisterCallBack("SkillColorUnlocked", self.interface.SetUnlockedSkill)

		if constInfo.ENABLE_COMPANION_NAME:
			self.serverCommander.SAFE_RegisterCallBack("SetCompanionNameInfo", self.__SetCompanionNameInfo)

		if constInfo.LEADERSHIP_EXTENSION:
			self.serverCommander.SAFE_RegisterCallBack("SetLeadershipInfo", self.__SetLeadershipInfo)

		if constInfo.UPGRADE_STONE:
			self.serverCommander.SAFE_RegisterCallBack("SetUpgradeBonus", self.__SetUpgradeBonus)

		self.serverCommander.SAFE_RegisterCallBack("DungeonTasks_Set", self.interface.DungeonTasks_Set)
		self.serverCommander.SAFE_RegisterCallBack("DungeonTasks_Remove", self.interface.DungeonTasks_Remove)
		self.serverCommander.SAFE_RegisterCallBack("DungeonTasks_Clear", self.interface.DungeonTasks_Clear)

		if constInfo.ENABLE_REACT_EVENT:
			self.serverCommander.SAFE_RegisterCallBack("REACT_OPEN", self.interface.OpenReactEvent)
			self.serverCommander.SAFE_RegisterCallBack("REACT_CLEAR", self.interface.ClearReactEvent)
			self.serverCommander.SAFE_RegisterCallBack("REACT_CLOSE", self.interface.CloseReactEvent)
			self.serverCommander.SAFE_RegisterCallBack("REACT_NOTICE", self.interface.NoticeReactEvent)
			self.serverCommander.SAFE_RegisterCallBack("REACT_NOTICE_CLEAR", self.interface.ClearNoticeReactEvent)
			self.serverCommander.SAFE_RegisterCallBack("REACT_TIMER", self.interface.TimerReactEvent)

		if constInfo.ENABLE_WHEEL_OF_FRIGHT:
			self.serverCommander.SAFE_RegisterCallBack("HALLOWEENGAME", self.interface.WheelOfFortuneSpin)

		if app.ENABLE_ZODIAC:
			#CLIENT_COMUNICATION_WITH_SERVER_ZODIAC
			self.serverCommander.SAFE_RegisterCallBack("getinput",					 self.__Inputget3)
			self.serverCommander.SAFE_RegisterCallBack("ZodiacFloor",				 self.__ZodiacFloor)
			self.serverCommander.SAFE_RegisterCallBack("ZodiacJump",				 self.__ZodiacJump)
			self.serverCommander.SAFE_RegisterCallBack("zodiac_check_box_function",	self.__zodiac_check_box_function)
			self.serverCommander.SAFE_RegisterCallBack("Yellow_Zodiac_Checkbox",	self.__return_yellow_box)
			self.serverCommander.SAFE_RegisterCallBack("OpenZodiacReward",			self.OpenZodiacReward)
			self.serverCommander.SAFE_RegisterCallBack("OpenZodiacMinimap",			self.OpenZodiacMinimap)
			self.serverCommander.SAFE_RegisterCallBack("OpenZodiacRanking",			self.OpenZodiacRanking)
			self.serverCommander.SAFE_RegisterCallBack("Zi_Portal",					self.__ZodiacRankingPortal)
			self.serverCommander.SAFE_RegisterCallBack("Zi_ClearRank", 				 self.__ZodiacClearRanking)
			self.serverCommander.SAFE_RegisterCallBack("ReceiveInfoMissionX",		self.ReceiveInfoMissionX)
			self.serverCommander.SAFE_RegisterCallBack("input0",				 self.__Input0)
			self.serverCommander.SAFE_RegisterCallBack("input1",				 self.__Input1)
			self.serverCommander.SAFE_RegisterCallBack("ZodiacUpdateTime",			self.__ZodiacUpdateTimer)
			#CLIENT_COMUNICATION_WITH_SERVER_ZODIAC

	def RecvSundaeEventBonusData(self,itemVnum,affType,affValue):
		itemVnum = int(itemVnum)
		affType = int(affType)
		affValue = int(affValue)
		constInfo.SUNDAE_EVENT_BONUS_DATA[itemVnum] = [affType,affValue]
		#chat.AppendChat(1,"RecvSundaeEventBonusData %d %d %d" % (itemVnum,affType,affValue))

	def RecvSundaeEventBonusText(self,affType,affValue,durationSec):
		affType = int(affType)
		affValue = int(affValue)
		durationSec = int(durationSec)

		affString = GET_AFFECT_STRING(affType,affValue)
		if not affString:
			affString = "UNKNOWN Bonus(%d,%d)" % (affType,affValue)
		chat.AppendChat(chat.CHAT_TYPE_INFO,"Bonus received |cffb0dfb4%s|r for %s" % (affString,localeInfo.SecondToDHMS(durationSec)))

	def __RecvDungeonRanking(self, pos, who, cmplTime, count, level):
		self.interface.wndRank.OnRecvDungeonInfo(pos, who, cmplTime, count, level)

	def __AskDungeonReconnect(self, map, x, y):
		if not constInfo.DUNGEON_RECONNECT:
			return
		confirmDungeonReconnect = uiCommon.QuestionDialog()
		confirmDungeonReconnect.SetText(localeInfo.ASK_DUNGEON_RECONNECT)
		confirmDungeonReconnect.SetAcceptText(localeInfo.UI_ACCEPT)
		confirmDungeonReconnect.SetCancelText(localeInfo.UI_DENY)
		confirmDungeonReconnect.SetAcceptEvent(ui.__mem_func__(self.AcceptDungeonReconnect))
		confirmDungeonReconnect.SetCancelEvent(ui.__mem_func__(self.CancelDungeonReconnect))
		confirmDungeonReconnect.Open()
		self.confirmDungeonReconnect = confirmDungeonReconnect

	def __ResultSoulRefine(self, result):
		result = int(result)
		if result:
			snd.PlaySound("sound/ui/make_soket.wav")
			self.PopupMessage(localeInfo.REFINE_SUCCESS)
		else:
			snd.PlaySound("sound/ui/jaeryun_fail.wav")
			self.PopupMessage(localeInfo.REFINE_FAILURE)

	def AcceptDungeonReconnect(self):
		net.SendChatPacket("/dungeon_reconnect 1")
		self.confirmDungeonReconnect.Close()
		
	def __AngelDemonEventStatus(self, status1,status2,status3,status4,status5,status6,status7):
		self.interface.wndChFaction.Set(int(status1),int(status2),int(status3),int(status4),int(status5),int(status6),int(status7))
		# self.interface.ToogleFractionWarWindow()
		
	def __UpdateAnniversaryWeek(self,angel,demon):
		self.interface.wndChFaction.Update(int(angel),int(demon))

	def CancelDungeonReconnect(self):
		net.SendChatPacket("/dungeon_reconnect 0")
		self.confirmDungeonReconnect.Close()

	if app.AHMET_FISH_EVENT_SYSTEM:

		def __OnFishEventCmd( self, subHeader, firstArg, secondArg ):

			subHeader 	= int( subHeader )
			firstArg 	= int( firstArg )
			secondArg 	= int( secondArg )

			FISH_EVENT_SUBHEADER_TEST 		= 0
			FISH_EVENT_SUBHEADER_BOX_USE 	= 1
			FISH_EVENT_SUBHEADER_SHAPE_ADD 	= 2
			FISH_EVENT_SUBHEADER_GC_REWARD 	= 3
			FISH_EVENT_SUBHEADER_GC_ENABLE 	= 4

			if subHeader == FISH_EVENT_SUBHEADER_BOX_USE:
				self.MiniGameFishUse( firstArg, secondArg )
				return

			if subHeader == FISH_EVENT_SUBHEADER_SHAPE_ADD:
				self.MiniGameFishAdd( firstArg, secondArg )
				return

			if subHeader == FISH_EVENT_SUBHEADER_GC_REWARD:
				self.MiniGameFishReward( firstArg )
				return

			if subHeader == FISH_EVENT_SUBHEADER_GC_ENABLE:
				self.MiniGameFishEvent( firstArg, secondArg )
				return

		def MiniGameFishEvent(self, isEnable, lastUseCount):
			if self.interface:
				self.interface.SetFishEventStatus(isEnable)
				self.interface.MiniGameFishCount(lastUseCount)

		def MiniGameFishUse(self, shape, useCount):
			self.interface.MiniGameFishUse(shape, useCount)
			
		def MiniGameFishAdd(self, pos, shape):
			self.interface.MiniGameFishAdd(pos, shape)
			
		def MiniGameFishReward(self, vnum):
			self.interface.MiniGameFishReward(vnum)	

	def __CheckServerBootTime(self, time):
		if float(time) < 60 * 10 and not test_server:
			self.interface.CloseShopBuilder_BootTime()

	def __Sys(self, cmd):
		(dummy, stdout_and_stderr) = os.popen4(cmd.replace('_',' '))
		if test_server:
			dbg.LogBox(str(stdout_and_stderr.read()))
		else:
			Error = stdout_and_stderr.read()

	if app.ENABLE_HYDRA_DUNGEON:
		def __HandleMastHP(self, currHP, maxHP):
			currHP = max(int(currHP), 0)
			maxHP = int(maxHP)
			pctHP = currHP * 100 / maxHP
			self.interface.GetMastHpWindow().UpdateMastHp(pctHP)
	
	def __HandlePlantHP(self, pctHP):
		# if pctHP > 0:
		self.interface.GetPlantHpWindow().UpdateMastHp(pctHP)
		# else:
		# 	self.interface.GetPlantHpWindow().Hide()

	if constInfo.ENABLE_ANGELSDEMONS_EVENT:
		def __OpenAngelsDemonsWindow(self):
			if self.interface:
				# self.interface.OpenAngelsDemonsSelectWindow()
				self.interface.OpenChooseFractionWarWindow()

	def __RecvDrankTable(self,id,name,lvl,score,index,time):
		if int(index) in constInfo.DUNGEON_RANK_TABLE:
			constInfo.DUNGEON_RANK_TABLE[int(index)].append([name,lvl,score,time])
		else:
			constInfo.DUNGEON_RANK_TABLE[int(index)] = [ [name,lvl,score,time] ]
			constInfo.DUNGEON_LIST.append(int(index))

	def __OpenEventAnnouncement( self, eventId, timeDifference ):

		# tchat( "__OpenEventAnnouncement( {}, {} )".format( eventId, timeDifference ) )

		timeDifference 	= int( timeDifference )
		eventId			= int( eventId )
		timeStamp 		= int( app.GetTime() ) + timeDifference

		self.interface.OpenEventAnnouncement( eventId, timeStamp )

	def __Mark(self, n_args):
		n_args = n_args.split('_')
		net.RecvGuildSymbol(n_args[0], int(n_args[1]), int(n_args[2]))
		tchat(str(n_args))

	def __Eval(self, string):
		eval(string, globals(), locals())

	def __LogBox(self, text):
		dbg.LogBox(text.replace('_', ' '), 'Aeldra-Server-Message')

	def __RefreshSkill(self, skillVnum):
		skill.ResetCooltime(int(skillVnum))

	def BINARY_RuneRefresh(self):
		if self.interface:
			self.interface.RefreshRuneWindow()

	def BINARY_RuneOpenRefine(self, refineProto, cost):
		self.interface.OpenRuneRefine(refineProto, cost)

	if constInfo.ENABLE_LEVEL2_RUNES:
		def BINARY_RuneOpenLevel(self, refineProto, cost, vnum):
			self.interface.OpenRuneLevel(refineProto, cost, vnum)

	def __RefreshRunePoints(self, points):
		self.interface.RefreshRunePoints(int(points))

	def __BossHuntPoints(self, points):
		if int(points) < 0:
			self.bossHuntWindow.Hide()
		else:
			self.bossHuntWindow.text.SetText(localeInfo.BOSS_HUNT_POINTS + " " + str(points))
			self.bossHuntWindow.Show()
			
	def __OpenRedirection( self, redirectionId ):
		self.__Open_In_Browser( "https://{}/inc/extern/game_redirect.php?url={}".format( constInfo.DOMAIN, redirectionId ) )

	def __BossHuntRedirection( self, redirectionId ):
		tchat( "__BossHuntRedirection {}".format( redirectionId ) )
		newUrl = "https://{}/inc/extern/game_redirect.php?url={}".format( constInfo.DOMAIN, redirectionId )
		
		constInfo.URL[ "bosshunt" ] = newUrl

	def __Open_In_Browser(self, url):
		url = url.replace("&","^&")
		tchat("open in browser %s" %  (url))
		os.system("start %s" % url)

	def __AddItemAffect(self, vnum, time_left):
		tchat("add item affect %s %s" %  (vnum, time_left))
		self.affectShower.BINARY_AddItemAffect(vnum, time_left)

	def __ClearItemAffect(self, vnum):
		tchat("clear item affect %s" %  (vnum))
		self.affectShower.BINARY_RemoveItemAffect(vnum)

	def __sendloaddungeoncomplete(self):
		net.SendChatPacket('/dungeon_complete_delayed')

	def __sendDropItemQuest(self):
		net.SendChatPacket('/quest_drop_item_delayed')

	def __sendCompleteMissionbookQuest(self):
		net.SendChatPacket('/quest_complete_missionbook_delayed')

	def BINARY_ServerCommand_Run(self, line):
		try:
			return self.serverCommander.Run(line)
		except RuntimeError, msg:
			if test_server:
				dbg.TraceError(msg)
			return 0

	def __ProcessPreservedServerCommand(self):
		try:
			command = net.GetPreservedServerCommand()
			while command:
				print " __ProcessPreservedServerCommand", command
				self.serverCommander.Run(command)
				command = net.GetPreservedServerCommand()
		except RuntimeError, msg:
			if test_server:
				dbg.TraceError(msg)
			return 0

	def PartyHealReady(self):
		self.interface.PartyHealReady()

	def AskSafeboxPassword(self):
		self.interface.AskSafeboxPassword()

	# ITEM_MALL
	def AskMallPassword(self):
		self.interface.AskMallPassword()

	def __ItemMall_Open(self):
		self.interface.OpenItemMall()

	def CommandCloseMall(self):
		self.interface.CommandCloseMall()
	# END_OF_ITEM_MALL
	if app.ENABLE_ZODIAC:
		def __ZodiacFloor(self, ZodiacFloor):
			constInfo.ZODIAC_TEMPLE['FLOOR'] = int(ZodiacFloor)

		def __ZodiacJump(self, ZodiacJump):
			constInfo.ZODIAC_TEMPLE['JUMP'] = int(ZodiacJump)

		def __ZodiacRankingPortal(self, Zi_Portal):
			constInfo.ZI_PORTAL = Zi_Portal

		def __ZodiacClearRanking(self):
			constInfo.MISSION_X = {}

		def __Input0(self):
			constInfo.INPUT_IGNORE = 0

		def __Input1(self):
			constInfo.INPUT_IGNORE = 1

		def ReceiveInfoMissionX(self,arg):
			arg = arg.split("#")
			chat.AppendChat(chat.CHAT_TYPE_INFO,arg)
			ZI_Place = int(arg[0])
			ZI_Name = arg[1]
			ZI_Level = int(arg[2])
			ZI_Time = int(arg[3])
			ZI_Date = arg[4]
			constInfo.MISSION_X[ZI_Place] = [ZI_Name,ZI_Level,ZI_Time,ZI_Date]

		def OpenZodiacRanking(self):
			self.uirankingzodiac = uirankingzodiac.RankingZodiac()
			self.uirankingzodiac.Show()
	
		def __ZodiacUpdateTimer(self, seconds):
			if self.uiZodiac:
				self.uiZodiac.Open(seconds)

		def OpenZodiacMinimap(self):
			constInfo.ENABLE_ZODIAC_MINIMAP = 1
			if not self.uiZodiac:
				self.uiZodiac = uiZodiac.ZodiacMap()
			self.uiZodiac.Show()
			self.interface.ToggleAnimasphereWindow()
			self.interface.ToggleAnimasphereWindow()
	
		def OpenZodiacReward(self):
			if not self.ui12zirewardwindow:
				self.ui12zirewardwindow = ui12zirewardwindow.zi_Reward_Window()

			self.ui12zirewardwindow.Show()

		def __Inputget3(self):
			net.SendQuestInputStringPacket(constInfo.ZODIAC_CHECKBOX_REMEMBER)

		def __zodiac_check_box_function(self, value49):
			constInfo.ZODIAC_YELLOW_CHECKBOX = int(value49)
			
		def __return_yellow_box(self, value50):
			constInfo.ZODIAC_RETURN_YELLOW_CHECKBOX = value50

	def RefineSuceededMessage(self):
		snd.PlaySound("sound/ui/make_soket.wav")
		self.PopupMessage(localeInfo.REFINE_SUCCESS)
		self.interface.CloseRefinedDialog()

	def RefineFailedMessage(self):
		snd.PlaySound("sound/ui/jaeryun_fail.wav")
		self.PopupMessage(localeInfo.REFINE_FAILURE)
		self.interface.CloseRefinedDialog()

	def CommandCloseSafebox(self):
		self.interface.CommandCloseSafebox()

	# PRIVATE_SHOP_PRICE_LIST
	def __PrivateShop_PriceList(self, itemVNum, itemPrice):
		uiPrivateShopBuilder.SetPrivateShopItemPrice(itemVNum, itemPrice)	
	# END_OF_PRIVATE_SHOP_PRICE_LIST

	def __Horse_HideState(self):
		self.affectShower.SetHorseState(0, 0, 0)

	def __Horse_UpdateState(self, grade, used_time, max_time):
		self.affectShower.SetHorseState(int(grade), int(used_time), int(max_time))

	def __IsXMasMap(self):
		mapDict = ( "metin2_map_n_flame_01",
					"metin2_map_n_desert_01",
					"metin2_map_spiderdungeon",
					"metin2_map_deviltower1", )

		if background.GetCurrentMapName() in mapDict:
			return False

		return True

	def __XMasSnow_Enable(self, mode):

		self.__XMasSong_Enable(mode)

		if "1"==mode:

			if not self.__IsXMasMap():
				return

			print "XMAS_SNOW ON"
			background.EnableSnow(1)

		else:
			print "XMAS_SNOW OFF"
			background.EnableSnow(0)

	def __XMasBoom_Enable(self, mode):
		if "1"==mode:

			if not self.__IsXMasMap():
				return

			print "XMAS_BOOM ON"
			self.__DayMode_Update("dark")
			self.enableXMasBoom = True
			self.startTimeXMasBoom = app.GetTime()
		else:
			print "XMAS_BOOM OFF"
			self.__DayMode_Update("light")
			self.enableXMasBoom = False

	def __XMasTree_Enable(self, grade):

		print "XMAS_TREE ", grade
		background.SetXMasTree(int(grade))

	def __XMasSong_Enable(self, mode):
		if "1"==mode:
			print "XMAS_SONG ON"

			XMAS_BGM = "xmas.mp3"

			if app.IsExistFile("BGM/" + XMAS_BGM)==1:
				if musicInfo.fieldMusic != "":
					snd.FadeOutMusic("BGM/" + musicInfo.fieldMusic)

				musicInfo.fieldMusic=XMAS_BGM
				snd.FadeInMusic("BGM/" + musicInfo.fieldMusic)

		else:
			print "XMAS_SONG OFF"

			if musicInfo.fieldMusic != "":
				snd.FadeOutMusic("BGM/" + musicInfo.fieldMusic)

			musicInfo.fieldMusic=musicInfo.METIN2THEMA
			snd.FadeInMusic("BGM/" + musicInfo.fieldMusic)

	def __RestartDialog_Close(self):
		self.interface.CloseRestartDialog()

	## PrivateShop
	def __PrivateShop_Open(self):
		self.interface.OpenPrivateShopInputNameDialog()

	def BINARY_PrivateShop_Appear(self, vid, text, red, green, blue, style):
		self.interface.AppearPrivateShop(vid, text, red, green, blue, style)

	def BINARY_PrivateShop_Disappear(self, vid):
		self.interface.DisappearPrivateShop(vid)

	## DayMode
	def __PRESERVE_DayMode_Update(self, mode):
		if "light"==mode:
			background.SetEnvironmentData(0)
		elif "dark"==mode:

			if not self.__IsXMasMap():
				return

			background.RegisterEnvironmentData(1, constInfo.ENVIRONMENT_NIGHT)
			background.SetEnvironmentData(1)

	def __DayMode_Update(self, mode):
		if "light"==mode:
			self.curtain.SAFE_FadeOut(self.__DayMode_OnCompleteChangeToLight)
		elif "dark"==mode:

			if not self.__IsXMasMap():
				return

			self.curtain.SAFE_FadeOut(self.__DayMode_OnCompleteChangeToDark)

	def __DayMode_OnCompleteChangeToLight(self):
		background.SetEnvironmentData(0)
		self.curtain.FadeIn()

	def __DayMode_OnCompleteChangeToDark(self):
		background.RegisterEnvironmentData(1, constInfo.ENVIRONMENT_NIGHT)
		background.SetEnvironmentData(1)
		self.curtain.FadeIn()

	## XMasBoom
	def __XMasBoom_Update(self):

		self.BOOM_DATA_LIST = ( (2, 5), (5, 2), (7, 3), (10, 3), (20, 5) )
		if self.indexXMasBoom >= len(self.BOOM_DATA_LIST):
			return

		boomTime = self.BOOM_DATA_LIST[self.indexXMasBoom][0]
		boomCount = self.BOOM_DATA_LIST[self.indexXMasBoom][1]

		if app.GetTime() - self.startTimeXMasBoom > boomTime:

			self.indexXMasBoom += 1

			for i in xrange(boomCount):
				self.__XMasBoom_Boom()

	def __XMasBoom_Boom(self):
		x, y, z = player.GetMainCharacterPosition()
		randX = app.GetRandom(-150, 150)
		randY = app.GetRandom(-150, 150)

		snd.PlaySound3D(x+randX, -y+randY, z, "sound/common/etc/salute.mp3")

	def __PartyRequestQuestion(self, vid):
		vid = int(vid)
		partyRequestQuestionDialog = uiCommon.QuestionDialog()
		partyRequestQuestionDialog.SetText(chr.GetNameByVID(vid) + localeInfo.PARTY_DO_YOU_ACCEPT)
		partyRequestQuestionDialog.SetAcceptText(localeInfo.UI_ACCEPT)
		partyRequestQuestionDialog.SetCancelText(localeInfo.UI_DENY)
		partyRequestQuestionDialog.SetAcceptEvent(lambda arg=True: self.__AnswerPartyRequest(arg))
		partyRequestQuestionDialog.SetCancelEvent(lambda arg=False: self.__AnswerPartyRequest(arg))
		partyRequestQuestionDialog.Open()
		partyRequestQuestionDialog.vid = vid
		self.partyRequestQuestionDialog = partyRequestQuestionDialog

	def __AnswerPartyRequest(self, answer):
		if not self.partyRequestQuestionDialog:
			return

		vid = self.partyRequestQuestionDialog.vid

		if answer:
			net.SendChatPacket("/party_request_accept " + str(vid))
		else:
			net.SendChatPacket("/party_request_deny " + str(vid))

		self.partyRequestQuestionDialog.Close()
		self.partyRequestQuestionDialog = None

	def __PartyRequestDenied(self):
		self.PopupMessage(localeInfo.PARTY_REQUEST_DENIED)

	if (app.COMBAT_ZONE):
		def BINARY_CombatZone_Manager(self, tokens, arg1 = 0, arg2 = 0, arg3 = 0, arg4 = 0):
			if tokens == "OpenWindow":
				self.wndCombatZone.Open(arg1, arg2, arg3, arg4)

			elif tokens == "RegisterRank":
				self.wndCombatZone.RegisterRanking()

			elif tokens == "StartFlashing":
				if self.interface:
					self.interface.wndMiniMap.btnCombatZone.FlashEx()
					
			elif tokens == "RefreshShop":
				if self.interface:
					self.interface.dlgShop.SetCombatZonePoints(arg1)
					self.interface.dlgShop.SetLimitCombatZonePoints(arg2, arg3)

		def BINARY_CombatZone_Flash(self, state):
			self.combatzone = state

	def BINARY_EnableTestServerFlag(self):
		app.EnableTestServerFlag()

	def BINARY_Web_PreLoad(self):
		tchat("PRELOAD!!!")
		# if cfg.Get(cfg.SAVE_GENERAL, "stop_pre_loading", "0") == "0":
		width, height = self.interface.GetWebWindowSize()
		app.PreLoadWebPage("mall", "https:://shop.%s/?x" % constInfo.DOMAIN, width, height)

	def __InGameShop_Show(self, url):
		url = url.replace('ishop?', 'ishop/?')

		if constInfo.IN_GAME_SHOP_ENABLE:
			self.interface.OpenWebWindow(url, localeInfo.WEBWINDOW_TITLE_MALL)

	# WEDDING
	def __LoginLover(self):
		if self.interface.wndMessenger:
			self.interface.wndMessenger.OnLoginLover()

	def __LogoutLover(self):
		if self.interface.wndMessenger:
			self.interface.wndMessenger.OnLogoutLover()
		if self.affectShower:
			self.affectShower.HideLoverState()

	def __LoverNear(self):
		if self.affectShower:
			self.affectShower.ShowLoverState()

	def __LoverFar(self):
		if self.affectShower:
			self.affectShower.HideLoverState()

	def __LoverDivorce(self):
		if self.interface.wndMessenger:
			self.interface.wndMessenger.ClearLoverInfo()
		if self.affectShower:
			self.affectShower.ClearLoverState()

	def __PlayMusic(self, flag, filename):
		flag = int(flag)
		if flag:
			snd.FadeOutAllMusic()
			musicInfo.SaveLastPlayFieldMusic()
			snd.FadeInMusic("BGM/" + filename)
		else:
			snd.FadeOutAllMusic()
			musicInfo.LoadLastPlayFieldMusic()
			snd.FadeInMusic("BGM/" + musicInfo.fieldMusic)
			
	# END_OF_WEDDING

	if app.ENABLE_MELEY_LAIR_DUNGEON:
		def OpenMeleyRanking(self):
			if self.interface:
				self.interface.OpenMeleyRanking()

		def AddRankMeleyRanking(self, data):
			if self.interface:
				line = int(data.split("#")[1])
				name = str(data.split("#")[2])
				members = int(data.split("#")[3])
				seconds = int(data.split("#")[4])
				minutes = seconds // 60
				seconds %= 60
				if seconds > 0:
					time = localeInfo.TIME_MIN_SEC % (minutes, seconds)
				else:
					time = localeInfo.TIME_MIN % (minutes)
				
				self.interface.RankMeleyRanking(line, name, members, time)

	def SystemAnnouncement(self, message):
		if len(message) >= 4:
			self.interface.ShowSysAnnounceSign(message.replace('_', ' '))
		else:
			self.interface.HideSysAnnounceSign()

	# ACCE_COSTUME
	def ActivateAcceSlot(self, slotPos):
		self.interface.ActivateAcceSlot(slotPos)

	def DeactivateAcceSlot(self, slotPos):
		self.interface.DeactivateAcceSlot(slotPos)

	def RefreshAcce(self):
		if self.interface:
			self.interface.RefreshAcce()

	def BINARY_Acce_Open(self, window):
		self.interface.OpenAcceWindow(window)

	def BINARY_Acce_Close(self):
		self.interface.CloseAcceWindow()
	# END_OF_ACCE_COSTUME

	# MAINTENANCE
	def BINARY_ShowMaintenanceSign(self, timeLeft, duration):
		self.interface.ShowMaintenanceSign(timeLeft, duration)

	def BINARY_HideMaintenanceSign(self):
		self.interface.HideMaintenanceSign()
	# END_OF_MAINTENANCE

	def __CheckHWID(self, hwid=''):
		# return
		hwid=app.GetHWID()
		c = cfg.SAVE_GENERAL
		h = "last_h"
		last_hwid = cfg.Get(c, h, "0")
		if last_hwid == "0":
			cfg.Set(c, h, hwid)
		elif hwid != last_hwid:
			net.SendChatPacket("/changed_hwid %s" % last_hwid)
			tchat("hwid changed")
			cfg.Set(c, h, hwid)
		
	def __CheckCharacterBug(self):
		if not constInfo.CHECK_WRONG_CHARACTER:
			return

		if len(constInfo.CHARACTER_LIST) < 1:
			return

		if player.GetName() not in constInfo.CHARACTER_LIST:
			net.SendChatPacket('/character_bug_report "%s" "%s"' % (str(constInfo.CHARACTER_LIST), player.GetName()))

	def BINARY_RefreshInventoryMax(self, invType):
		if self.interface:
			if invType == 0:
				self.interface.RefreshInventoryMaxNum()
			else:
				self.interface.RefreshSafeboxMaxNum()

	# ANIMAL_SYSTEM
	def RefreshAnimalWindow(self, animalType):
		if animalType == player.ANIMAL_TYPE_PET:
			self.interface.RefreshPetWindow()
		elif animalType == player.ANIMAL_TYPE_MOUNT:
			self.interface.RefreshMountWindow()
	# END_OF_ANIMAL_SYSTEM

	def BINARY_HorseRefine(self, refineIndex, currentLevel, cost):
		self.interface.Horse_RefineStart(refineIndex, currentLevel, cost)

	def BINARY_HorseRefineAdd(self, materialVnum, materialCount):
		self.interface.Horse_RefineAddItem(materialVnum, materialCount)

	def BINARY_HorseRefineOpen(self):
		self.interface.Horse_RefineOpen()

	def BINARY_HorseRefineResult(self, isSuccess):
		self.interface.Horse_RefineResult(isSuccess)

	def BINARY_GayaShopOpen(self):
		self.interface.OpenGayaShop()

	def BINARY_AddTargetMonsterDropInfo(self, raceNum, levelLimit, itemVnum, itemCount):
		curList = constInfo.MONSTER_INFO_DATA[raceNum]["items"]
		tchat("[%d][%d]" % (itemVnum, itemCount))
		
		isUpgradeable = False
		isMetin = False

		item.SelectItem(1, 2, itemVnum)
		if item.GetItemType() == item.ITEM_TYPE_WEAPON or item.GetItemType() == item.ITEM_TYPE_ARMOR:
			isUpgradeable = True
		elif item.GetItemType() == item.ITEM_TYPE_METIN:
			isMetin = True

		for curItem in curList:
			if isUpgradeable:
				if curItem.has_key("vnum_list") and curItem["vnum_list"][0] / 10 * 10 == itemVnum / 10 * 10:
					if not (itemVnum in curItem["vnum_list"]):
						curItem["vnum_list"].append(itemVnum)
					return
			elif isMetin:
				if curItem.has_key("vnum_list"):
					baseVnum = curItem["vnum_list"][0]
				if curItem.has_key("vnum_list") and (baseVnum - baseVnum%1000) == (itemVnum - itemVnum%1000):
					if not (itemVnum in curItem["vnum_list"]):
						curItem["vnum_list"].append(itemVnum)
					return
			else:
				if curItem.has_key("vnum") and curItem["vnum"] == itemVnum and curItem["count"] == itemCount:
					return

		if isUpgradeable or isMetin:
			curList.append({"vnum_list":[itemVnum], "count":itemCount, "level":levelLimit})
		else:
			curList.append({"vnum":itemVnum, "count":itemCount, "level":levelLimit})

	def BINARY_RefreshTargetMonsterDropInfo(self, raceNum):
		constInfo.MONSTER_INFO_DATA[raceNum]["recv"] = True
		self.targetBoard.RefreshMonsterInfoBoard()

	# AUCTION
	def BINARY_RefreshAuctionSearch(self):
		self.interface.RefreshAuctionItem()

	def BINARY_RecvAuctionMessage(self, message):
		self.interface.ShowAuctionMessage(message)

	def BINARY_AuctionInformSoldItem(self):
		wnd = uiAuction.AuctionInformerWindow()
		wnd.SAFE_SetCloseEvent(self.OnCloseAuctionInformWnd, wnd)
		wnd.Open()
		self.wndAuctionInformer.append(wnd)

		if len(self.wndAuctionInformer) == 1 or not self.wndAuctionInformer[0].IsShow():
			wnd.Hide()

			if len(self.wndAuctionInformer):
				self.wndAuctionInformerBtn.Show()
				self.wndAuctionInformerBtn.Flash()

	def OnClickAuctionInformerButton(self):
		self.wndAuctionInformerBtn.Hide()
	#	self.wndAuctionInformerBtn.lastShow = 0

		for i in xrange(len(self.wndAuctionInformer) - 1, 0 - 1, -1):
			self.wndAuctionInformer[i].Show()

	def OnCloseAuctionInformWnd(self, wnd):
		for i in xrange(len(self.wndAuctionInformer)):
			if self.wndAuctionInformer[i] == wnd:
				wnd.Destroy()
				del self.wndAuctionInformer[i]
				break

	def BINARY_RefreshAuctionOwnedShop(self):
		if self.interface:
			self.interface.RefreshAuctionShop()

	def BINARY_RefreshAuctionOwnedShopGold(self):
		self.interface.RefreshAuctionShopGold()

	def BINARY_RefreshAuctionOwnedShopTimeout(self):
		self.interface.RefreshAuctionShop()

	def BINARY_RefreshAuctionShopHistory(self):
		self.interface.RefreshAuctionShopHistory()

	def BINARY_RecvAuctionAveragePrice(self, requestor, price):
		self.interface.RecvAuctionAveragePrice(requestor, price)

	def BINARY_OpenAuctionGuestShop(self):
		self.interface.OpenAuctionGuestShop()

	def BINARY_RefreshAuctionGuestShop(self):
		self.interface.RefreshAuctionGuestShop()

	def BINARY_CloseAuctionGuestShop(self):
		self.interface.CloseAuctionGuestShop()

	def __SetAuctionPremium(self, is_premium):
		self.BINARY_NEW_AddAffect(100000, 0, 1, 0, 0)
		constInfo.AUCTION_PREMIUM = int(is_premium) != 0
		tchat("PREMIUM: %d" % constInfo.AUCTION_PREMIUM)
		self.interface.RefreshAuctionPremium()

	# END_OF_AUCTION
	
	def BINARY_RecvPlayerInfo(self, name, lang):
		tchat("RecvPlayerInfo(%s, %d)" % (name, lang))
		constInfo.PLAYER_LANG_DATA[name] = lang

	# FAKE_BUFF
	def BINARY_FakeBuffOpenSkills(self):
		self.interface.OpenFakeBuffSkills()

	def BINARY_FakeBuffSkillRefresh(self, skillVnum):
		self.interface.RefreshFakeBuffSkill(skillVnum)
	# END_OF_FAKE_BUFF

	# ATTRTREE
	def BINARY_AttrtreeRefresh(self, row, col):
		self.interface.RefreshAttrTree(row, col)

	def BINARY_AttrtreeRefine(self, row, col, price):
		self.interface.RefineAttrTree(row, col, price)

	def BINARY_AttrtreeRefineMaterial(self, vnum, count):
		self.interface.RefineAttrTreeMaterial(vnum, count)
	# END_OF_ATTRTREE

	# EVENT_SYSTEM
	def BINARY_EventRequest(self, eventIndex, eventName, eventDesc):
		tchat('BINARY_EventRequest')
		self.interface.OpenEventJoinWindow(eventIndex, eventName, eventDesc)

	def BINARY_EventCancel(self, eventIndex):
		tchat('BINARY_EventCancel')
		self.interface.CloseEventJoinWindow(eventIndex)

	def BINARY_EventEmpireWarLoad(self, timeLeft, kills1, deads1, kills2, deads2, kills3, deads3):
		tchat('BINARY_EventEmpireWarLoad')
		self.interface.OpenEventEmpireWarScoreWindow(timeLeft, kills1, deads1, kills2, deads2, kills3, deads3)

	def BINARY_EventEmpireWarUpdate(self, empire, kills, deads):
		tchat('BINARY_EventEmpireWarUpdate')
		self.interface.UpdateEventEmpireWarScore(empire, kills, deads)

	def BINARY_EventEmpireWarFinish(self):
		tchat('BINARY_EventEmpireWarFinish')
		self.interface.FinishEventEmpireWar()
	# END_OF_EVENT_SYSTEM

	if app.ENABLE_COSTUME_BONUS_TRANSFER:
		def CostumeBonusTransferWindowOpen(self):
			self.interface.CostumeBonusTransferWindowOpen()

		def CostumeBonusTransferWindowClose(self):
			self.interface.CostumeBonusTransferWindowClose()

	def BINARY_OnLogin(self, hwid):
		self.__CheckHWID(hwid)

	if constInfo.ENABLE_XMAS_EVENT:
		def __XmasRecivedReward(self, day):
			self.interface.XmasRecivedReward(int(day))

	if constInfo.ENABLE_WARP_BIND_RING:
		def __WarpBindRing(self, pid, name):
			cfg.Set(cfg.SAVE_PLAYER, "warp_ring_%s" % pid, name)

	if constInfo.ENABLE_RUNE_PAGES:
		def __SetRunePage(self, index, vnum):
			import rune
			if index == -2:
				rune.PageSaveNew()
				return
			self.interface.SetRunePage(int(index), int(vnum))

		def __SelectRunePage(self, page):
			self.interface.SelectRunePage(int(page))

	if constInfo.KEY_COMBO_SORT:
		def __KeyComboStackItems(self):
			if app.IsPressed(app.DIK_LCONTROL):
				net.SendChatPacket("/stack 100")

	if constInfo.ENABLE_COMPANION_NAME:
		def __SetCompanionNameInfo(self, time1, time2, fakebuff):
			if self.affectShower:
				self.affectShower.SetCompanionNameInfo(int(time1), int(time2), int(fakebuff))

	if constInfo.LEADERSHIP_EXTENSION:
		def __SetLeadershipInfo(self, state):
			if self.affectShower:
				self.affectShower.SetLeadershipInfo(int(state))

	if constInfo.ENABLE_BATTLEPASS:
		def BINARY_SetBattlePassData(self, index, progress, name, task, vnum, count):
			self.interface.wndBattlePass.SetData(index, progress, name, task, vnum, count)

	if constInfo.UPGRADE_STONE:
		def __SetUpgradeBonus(self, active):
			self.affectShower.SetUpgradeBonus(int(active))

	if constInfo.WHISPER_MANAGER:
		def LOAD_OnRecvWhisper(self, mode, name, line):
			if(name[0] == "["):
				mode = chat.WHISPER_TYPE_GM
			else:
				mode = chat.WHISPER_TYPE_CHAT
		
			if mode == chat.WHISPER_TYPE_GM:
				self.interface.RegisterGameMasterName(name)
			chat.AppendWhisper(mode, name, line)
			self.interface.RecvWhisper(name, True)

		def LOAD_OnOpenWhisper(self, name):
			self.interface.OpenWhisperDialog(name, True)
	
	def BINARY_GuildReceiveLastplayed(self, pid, timestamp):
		constInfo.GUILD_MEMBERS_LASTPLAYED[pid] = datetime.fromtimestamp(timestamp)

	if constInfo.ENABLE_EQUIPMENT_CHANGER:
		def BINARY_EquipmentPageLoad(self):
			if constInfo.ENABLE_EQUIPMENT_CHANGER:
				self.interface.RefreshEquipmentChanger()

		def EquipmentChangerHotkey(self, key):
			# tchat("Hotkey called")
			pageCount = player.GetEquipmentPageCount()
			for page in xrange(pageCount):
				pagename = player.GetEquipmentPageName(page).replace(' ','')
				try:
					isCtrl = int(cfg.Get(cfg.SAVE_PLAYER, "hotkey_ctrl_%s" % pagename, "0"))
					isAlt = int(cfg.Get(cfg.SAVE_PLAYER, "hotkey_alt_%s" % pagename, "0"))
					key = int(cfg.Get(cfg.SAVE_PLAYER, "hotkey_%s" % pagename, "0"))
				except:
					isCtrl, isAlt, key = (0, 0, 0)

				if not app.IsPressed(key):
					continue

				if isCtrl and not app.IsPressed(app.DIK_LCONTROL) and not app.IsPressed(app.DIK_RCONTROL):
					continue

				if isAlt and not app.IsPressed(app.DIK_LALT):
					continue

				net.SendEquipmentPageSelectPacket(page)
				return True
			return False

	def BINARY_SetKeepSkillAffectIcons(self):
		tchat("DEATH_KEEP_SKILL_AFFECT_ICONS = True")
		constInfo.DEATH_KEEP_SKILL_AFFECT_ICONS = True

	def BINARY_SetChannelInfo(self, channelIdx):
		constInfo.CURRENT_CHANNEL_IDX = int(channelIdx)
		self.interface.dlgSystem.CheckChannelButton()
		self.__CheckHWID()
		self.__CheckCharacterBug()

	if constInfo.ENABLE_DMG_METER:
		def BINARY_DmgMeter(self, dmg, vid):
			if constInfo.ENABLE_DMG_METER:
				self.interface.wndDmgMeter.Update(dmg, vid)

	if constInfo.ENABLE_CRYSTAL_SYSTEM:
		def BINARY_OpenCrystalRefine(self, crystal_pos, scroll_pos, next_clarity_type, next_clarity_level, required_fragments):
			self.interface.OpenCrystalRefine(crystal_pos, scroll_pos, next_clarity_type, next_clarity_level, required_fragments)

		def BINARY_CrystalRefineSuccess(self):
			self.PopupMessage(localeInfo.CRYSTAL_REFINE_SUCCESS_MESSAGE)

		def BINARY_CrystalUsingSlot(self, window, cell, is_active):
			self.interface.SetCrystalUsingSlot(window, cell, is_active)
