import ui
import uiScriptLocale
import net
import app
import dbg
import player
import background
import wndMgr

import localeInfo
import chrmgr
import colorInfo
import constInfo

import playerSettingModule
import stringCommander
import emotion

####################################
# ���� ������ ���� ��� �ε� �д�
####################################
import uiRefine
import uiToolTip
import uiAttachMetin
import uiPickMoney
import uiChat
import uiMessenger
import uiHelp
import uiWhisper
import uiPointReset
import uiShop
import uiExchange
import uiSystem
import uiOption
import uiRestart
import cfg
####################################

class LoadingWindow(ui.ScriptWindow):
	def __init__(self, stream):
		print "NEW LOADING WINDOW -------------------------------------------------------------------------------"
		ui.Window.__init__(self)
		net.SetPhaseWindow(net.PHASE_WINDOW_LOAD, self)

		self.stream=stream
		self.loadingImage=0
		self.loadingGage=0
		self.errMsg=0
		self.update=0
		self.playerX=0
		self.playerY=0
		self.loadStepList=[]

	def __del__(self):
		print "---------------------------------------------------------------------------- DELETE LOADING WINDOW"
		net.SetPhaseWindow(net.PHASE_WINDOW_LOAD, 0)
		ui.Window.__del__(self)

	def Open(self):
		print "OPEN LOADING WINDOW -------------------------------------------------------------------------------"

		#app.HideCursor()

		try:
			pyScrLoader = ui.PythonScriptLoader()
			
			print localeInfo.IsVIETNAM()
			if localeInfo.IsVIETNAM():
				print uiScriptLocale.LOCALE_UISCRIPT_PATH + "LoadingWindow.py"
				pyScrLoader.LoadScriptFile(self, uiScriptLocale.LOCALE_UISCRIPT_PATH + "LoadingWindow.py")
			else:			
				pyScrLoader.LoadScriptFile(self, "UIScript/LoadingWindow.py")
		except:
			import exception
			exception.Abort("LodingWindow.Open - LoadScriptFile Error")

		constInfo.FONTS[ 0 ] = localeInfo.UI_DEF_FONT

		choosenFont = cfg.Get( cfg.SAVE_OPTION, "choosen_font", "0" )
		choosenFont = int( choosenFont )

		constInfo.CHOOSEN_FONT = 0

		if choosenFont >= 0 and choosenFont <= 2 and constInfo.ENABLE_NEW_FONTS:
			constInfo.CHOOSEN_FONT = choosenFont

		app.SetUseNewFont( constInfo.CHOOSEN_FONT )

		try:
			self.loadingImage=self.GetChild("BackGround")
			self.errMsg=self.GetChild("ErrorMessage")
			self.loadingGage=self.GetChild("FullGage")
		except:
			import exception
			exception.Abort("LodingWindow.Open - LoadScriptFile Error")

		self.errMsg.Hide()

		imgFileNameDict = {
			0 : "d:/ymir work/ui/intro/loading/1.jpg",
			1 : "d:/ymir work/ui/intro/loading/3.jpg",
			2 : "d:/ymir work/ui/intro/loading/4.jpg",
			3 : "d:/ymir work/ui/intro/loading/5.jpg",
			4 : "d:/ymir work/ui/intro/loading/2.jpg",
			5 : "d:/ymir work/ui/intro/loading/0.jpg",
		}
		
		if __SERVER__ == 2:
			imgFileNameDict = {
				0 : "d:/ymir work/uiloading/background_loading_assassin.sub",
				1 : "d:/ymir work/uiloading/background_loading_assassin2.sub",
				2 : "d:/ymir work/uiloading/background_loading_assassin3.sub",
				3 : "d:/ymir work/uiloading/background_loading_samahi1.sub",
				4 : "d:/ymir work/uiloading/background_loading_shaman.sub",
				5 : "d:/ymir work/uiloading/background_loading_sura.sub",
				6 : "d:/ymir work/uiloading/background_loading_sura.sub",
				7 : "d:/ymir work/uiloading/background_loading_sura2.sub",
				8 : "d:/ymir work/uiloading/background_loading_warrior.sub",
				9 : "d:/ymir work/uiloading/background_loading_warrior5.sub",
				10 : "d:/ymir work/uiloading/background_loading_warriorghist1.sub",
			}

		try:
			imgFileName = imgFileNameDict[int(app.GetTime() * 1000.0) % len(imgFileNameDict)]

			print imgFileName
			self.loadingImage.LoadImage(imgFileName)
		except:
			print "LoadingWindow.Open.LoadImage - %s File Load Error" % (imgFileName)
			self.loadingImage.Hide()

		if self.loadingImage.GetWidth() != 0 and self.loadingImage.GetHeight() != 0:
			width = max(1.0, float(wndMgr.GetScreenWidth()) / float(self.loadingImage.GetWidth()))
			height = max(1.0, float(wndMgr.GetScreenHeight()) / float(self.loadingImage.GetHeight()))

			self.loadingImage.SetScale(width, height)
		self.loadingGage.SetPercentage(2, 100)

		self.Show()

		chrSlot=self.stream.GetCharacterSlot()
		net.SendSelectCharacterPacket(chrSlot)

		app.SetFrameSkip(0)
		if __SERVER__ == 1:
			constInfo.AUCTION_PREMIUM = False

	def Close(self):
		print "---------------------------------------------------------------------------- CLOSE LOADING WINDOW"

		app.SetFrameSkip(1)

		self.loadStepList=[]
		self.loadingImage=0
		self.loadingGage=0
		self.errMsg=0
		self.ClearDictionary()
		self.Hide()

	def OnPressEscapeKey(self):
		app.SetFrameSkip(1)
		self.stream.SetLoginPhase()
		return True

	def __SetNext(self, next):
		if next:
			self.update=ui.__mem_func__(next)
		else:
			self.update=0

	def __SetProgress(self, p):
		if self.loadingGage:
			self.loadingGage.SetPercentage(p, 100)

	def DEBUG_LoadData(self, playerX, playerY):
		self.playerX=playerX
		self.playerY=playerY

		self.__RegisterSkill() ## �ε� �߰��� ���� �ϸ� ���� �߻�
		self.__RegisterTitleName()
		self.__RegisterColor()
		self.__InitData()
		self.__LoadMap()
		self.__LoadSound()
		self.__LoadEffect()
		self.__LoadWarrior()
		self.__LoadAssassin()
		self.__LoadSura()
		self.__LoadShaman()
		# self.__LoadWolfman()
		self.__LoadSkill()
		self.__LoadEnemy()
		self.__LoadNPC()
		self.__LoadGuildBuilding()
		self.__LoadRaceHeight()
		self.__LoadRaceSpecular()
		self.__StartGame()

		return True

	def LoadData(self, playerX, playerY):
		isDebug = False
		if isDebug and self.DEBUG_LoadData(playerX, playerY):
			return

		self.playerX=playerX
		self.playerY=playerY

		self.__RegisterDungeonMapName()
		self.__RegisterSkill() ## �ε� �߰��� ���� �ϸ� ���� �߻�
		self.__RegisterTitleName()
		self.__RegisterColor()
		self.__RegisterEmotionIcon()

		self.loadStepList=[
			(0, ui.__mem_func__(self.__InitData)),
			(10, ui.__mem_func__(self.__LoadMap)),
			(30, ui.__mem_func__(self.__LoadSound)),
			(40, ui.__mem_func__(self.__LoadEffect)),
			(50, ui.__mem_func__(self.__LoadWarrior)),
			(60, ui.__mem_func__(self.__LoadAssassin)),
			(70, ui.__mem_func__(self.__LoadSura)),
			(80, ui.__mem_func__(self.__LoadShaman)),
			(90, ui.__mem_func__(self.__LoadMotions)),
			# (90, ui.__mem_func__(self.__LoadWolfman)),
			(93, ui.__mem_func__(self.__LoadSkill)),
			(96, ui.__mem_func__(self.__LoadEnemy)),
			(97, ui.__mem_func__(self.__LoadNPC)),
			(98, ui.__mem_func__(self.__LoadGuildBuilding)),	
			(98, ui.__mem_func__(self.__LoadRaceHeight)),
			(99, ui.__mem_func__(self.__LoadRaceSpecular)),
			(100, ui.__mem_func__(self.__StartGame)),
		]

		tmpLoadStepList = tuple(zip(*self.loadStepList))[0]
		for progress in range(tmpLoadStepList[0], tmpLoadStepList[-1] + 1):
			if progress not in tmpLoadStepList:
				self.loadStepList.append((progress, lambda: None))
		self.loadStepList.sort()

		self.__SetProgress(0)
		#self.__SetNext(self.__LoadMap)

	def OnUpdate(self):
		if len(self.loadStepList)>0:
			(progress, runFunc)=self.loadStepList[0]

			try:
				runFunc()
			except:
				self.errMsg.Show()
				self.loadStepList=[]

				## �̰����� syserr.txt �� ������.

				import dbg
				import sys
				dbg.TraceError(" !!! Failed to load game data : STEP [%d] : %s" % (progress, sys.exc_info()[0]))

				#import shutil
				#import os
				#shutil.copyfile("syserr.txt", "errorlog.txt")
				#os.system("errorlog.exe")

				app.Exit()

				return

			self.loadStepList.pop(0)

			self.__SetProgress(progress)

	def __InitData(self):
		playerSettingModule.LoadGameData("INIT")

	def __RegisterDungeonMapName(self):
		background.RegisterDungeonMapName("metin2_map_spiderdungeon")
		background.RegisterDungeonMapName("metin2_map_monkeydungeon")
		background.RegisterDungeonMapName("metin2_map_monkeydungeon_02")
		background.RegisterDungeonMapName("metin2_map_monkeydungeon_03")
		background.RegisterDungeonMapName("metin2_map_deviltower1")

	def __RegisterSkill(self):

		race = net.GetMainActorRace()
		group = net.GetMainActorSkillGroup()
		empire = net.GetMainActorEmpire()

		playerSettingModule.RegisterSkill(race, group, empire)

	def __RegisterTitleName(self):
		for i in xrange(len(localeInfo.TITLE_NAME_LIST)):
			chrmgr.RegisterTitleName(i, localeInfo.TITLE_NAME_LIST[i])

	def __RegisterColor(self):

		## Name
		NAME_COLOR_DICT = {
			chrmgr.NAMECOLOR_PC : colorInfo.CHR_NAME_RGB_PC,
			chrmgr.NAMECOLOR_NPC : colorInfo.CHR_NAME_RGB_NPC,
			chrmgr.NAMECOLOR_MOB : colorInfo.CHR_NAME_RGB_MOB,
			chrmgr.NAMECOLOR_PVP : colorInfo.CHR_NAME_RGB_PVP,
			chrmgr.NAMECOLOR_PK : colorInfo.CHR_NAME_RGB_PK,
			chrmgr.NAMECOLOR_PARTY : colorInfo.CHR_NAME_RGB_PARTY,
			chrmgr.NAMECOLOR_WARP : colorInfo.CHR_NAME_RGB_WARP,
			chrmgr.NAMECOLOR_BOSS : colorInfo.CHR_NAME_RGB_BOSS,
			chrmgr.NAMECOLOR_STONE : colorInfo.CHR_NAME_RGB_STONE,
			chrmgr.NAMECOLOR_WAYPOINT : colorInfo.CHR_NAME_RGB_WAYPOINT,

			chrmgr.NAMECOLOR_EMPIRE_MOB : colorInfo.CHR_NAME_RGB_EMPIRE_MOB,
			chrmgr.NAMECOLOR_EMPIRE_NPC : colorInfo.CHR_NAME_RGB_EMPIRE_NPC,
			chrmgr.NAMECOLOR_EMPIRE_PC+1 : colorInfo.CHR_NAME_RGB_EMPIRE_PC_A,
			chrmgr.NAMECOLOR_EMPIRE_PC+2 : colorInfo.CHR_NAME_RGB_EMPIRE_PC_B,
			chrmgr.NAMECOLOR_EMPIRE_PC+3 : colorInfo.CHR_NAME_RGB_EMPIRE_PC_C,
		}
		for name, rgb in NAME_COLOR_DICT.items():
			chrmgr.RegisterNameColor(name, rgb[0], rgb[1], rgb[2])

		## Title
		TITLE_COLOR_DICT = (	colorInfo.TITLE_RGB_GOOD_4,
								colorInfo.TITLE_RGB_GOOD_3,
								colorInfo.TITLE_RGB_GOOD_2,
								colorInfo.TITLE_RGB_GOOD_1,
								colorInfo.TITLE_RGB_NORMAL,
								colorInfo.TITLE_RGB_EVIL_1,
								colorInfo.TITLE_RGB_EVIL_2,
								colorInfo.TITLE_RGB_EVIL_3,
								colorInfo.TITLE_RGB_EVIL_4,	)
		count = 0
		for rgb in TITLE_COLOR_DICT:
			chrmgr.RegisterTitleColor(count, rgb[0], rgb[1], rgb[2])
			count += 1

	def __RegisterEmotionIcon(self):
		emotion.RegisterEmotionIcons()

	def __LoadMap(self):
		net.Warp(self.playerX, self.playerY)

	def __LoadSound(self):
		playerSettingModule.LoadGameData("SOUND")

	def __LoadEffect(self):
		playerSettingModule.LoadGameData("EFFECT")

	def __LoadWarrior(self):
		playerSettingModule.LoadGameData("WARRIOR")

	def __LoadAssassin(self):
		playerSettingModule.LoadGameData("ASSASSIN")

	def __LoadSura(self):
		playerSettingModule.LoadGameData("SURA")

	def __LoadShaman(self):
		playerSettingModule.LoadGameData("SHAMAN")

	# def __LoadWolfman(self):
		# playerSettingModule.LoadGameData("WOLFMAN")

	def __LoadMotions(self):
		playerSettingModule.LoadGameData("MOTION")

	def __LoadSkill(self):
		playerSettingModule.LoadGameData("SKILL")

	def __LoadEnemy(self):
		playerSettingModule.LoadGameData("ENEMY")

	def __LoadNPC(self):
		playerSettingModule.LoadGameData("NPC")

	def __LoadGuildBuilding(self):
		playerSettingModule.LoadGuildBuildingList(localeInfo.GUILD_BUILDING_LIST_TXT, localeInfo.GUILD_BUILDING_NAME_LIST_TXT)
	
	def __LoadRaceHeight(self):
		playerSettingModule.LoadGameData("RACE_HEIGHT")

	def __LoadRaceSpecular(self):
		playerSettingModule.LoadGameData("RACE_SPECULAR")

	def __StartGame(self):
		background.SetViewDistanceSet(background.DISTANCE0, 25600)
		background.SelectViewDistanceNum(background.DISTANCE0)
		app.SetGlobalCenterPosition(self.playerX, self.playerY)

		background.RegisterEnvironmentData(1, constInfo.ENVIRONMENT_NIGHT)
		if cfg.Get(cfg.SAVE_OPTION, "use_night", "0") == "1":
			background.SetEnvironmentData(1)

		net.StartGame()
