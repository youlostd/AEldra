import ui
import localeInfo
import chr
import item
import app
import skill
import player
import uiToolTip
import math
import locale
import constInfo
import uiScriptLocale
import net
import uiCommon

if app.ENABLE_RUNE_AFFECT_ICONS:
	import rune

class LovePointImage(ui.ExpandedImageBox):

	FILE_PATH = "d:/ymir work/ui/pattern/LovePoint/"
	FILE_DICT = {
		0 : FILE_PATH + "01.dds",
		1 : FILE_PATH + "02.dds",
		2 : FILE_PATH + "02.dds",
		3 : FILE_PATH + "03.dds",
		4 : FILE_PATH + "04.dds",
		5 : FILE_PATH + "05.dds",
	}

	def __init__(self):
		ui.ExpandedImageBox.__init__(self)

		self.loverName = ""
		self.lovePoint = 0

		self.toolTip = uiToolTip.ToolTip(100)
		self.toolTip.HideToolTip()

	def __del__(self):
		ui.ExpandedImageBox.__del__(self)

	def SetLoverInfo(self, name, lovePoint):
		self.loverName = name
		self.lovePoint = lovePoint
		self.__Refresh()

	def OnUpdateLovePoint(self, lovePoint):
		self.lovePoint = lovePoint
		self.__Refresh()

	def __Refresh(self):
		self.lovePoint = max(0, self.lovePoint)
		self.lovePoint = min(100, self.lovePoint)

		if 0 == self.lovePoint:
			loveGrade = 0
		else:
			loveGrade = self.lovePoint / 25 + 1
		fileName = self.FILE_DICT.get(loveGrade, self.FILE_PATH+"00.dds")

		try:
			self.LoadImage(fileName)
		except:
			import dbg
			dbg.TraceError("LovePointImage.SetLoverInfo(lovePoint=%d) - LoadError %s" % (lovePoint, fileName))

		self.SetScale(0.7, 0.7)

		self.toolTip.ClearToolTip()
		self.toolTip.SetTitle(self.loverName)
		self.toolTip.AppendTextLine(localeInfo.AFF_LOVE_POINT % (self.lovePoint))
		self.toolTip.ResizeToolTip()

	def OnMouseOverIn(self):
		self.toolTip.ShowToolTip()

	def OnMouseOverOut(self):
		self.toolTip.HideToolTip()

class HorseImage(ui.ExpandedImageBox):

	FILE_PATH = "d:/ymir work/ui/pattern/HorseState/"

	FILE_DICT = {
		00 : FILE_PATH+"00.dds",
		01 : FILE_PATH+"00.dds",
		02 : FILE_PATH+"00.dds",
		03 : FILE_PATH+"00.dds",
		10 : FILE_PATH+"10.dds",
		11 : FILE_PATH+"11.dds",
		12 : FILE_PATH+"12.dds",
		13 : FILE_PATH+"13.dds",
		20 : FILE_PATH+"20.dds",
		21 : FILE_PATH+"21.dds",
		22 : FILE_PATH+"22.dds",
		23 : FILE_PATH+"23.dds",
		30 : FILE_PATH+"30.dds",
		31 : FILE_PATH+"31.dds",
		32 : FILE_PATH+"32.dds",
		33 : FILE_PATH+"33.dds",
	}

	def __init__(self):
		ui.ExpandedImageBox.__init__(self)

		#self.textLineList = []
		self.toolTip = uiToolTip.ToolTip(100)
		self.toolTip.HideToolTip()

		self.oldHealthPct = 0

		self.horseGrade = 0
		self.timeEnd = 0
		self.timeMax = 0

	def __GetHorseGrade(self, level):
		if 0 == level:
			return 0

		return (level-1)/10 + 1

	def __RefreshData(self):
		if self.horseGrade > 0:
			timeLeft = self.timeEnd - app.GetTime()
			if timeLeft <= 0:
				timeLeft = 0
			healthPct = int(math.ceil(timeLeft * 100 / float(self.timeMax)))
			healthThird = int(math.ceil(float(healthPct) / (1.0 / 3.0) / 100.0))

			if healthPct != self.oldHealthPct:
				self.oldHealthPct = healthPct

				self.toolTip.ClearToolTip()
				self.__AppendText(localeInfo.LEVEL_LIST[self.horseGrade])

				healthName = localeInfo.HEALTH_LIST[healthThird]
				if healthThird > 0:
					try:
						healthName = healthName % healthPct
					except:
						pass
				self.__AppendText(healthName)

				self.LoadImage(self.FILE_DICT[healthThird * 10 + 3])

				if not self.IsIn():
					self.toolTip.HideToolTip()

		else:
			self.toolTip.HideToolTip()

	def SetState(self, grade, timeUsed, timeMax):
		self.horseGrade = int(grade)
		self.timeEnd = app.GetTime() + (timeMax - timeUsed)
		self.timeMax = timeMax
		self.__RefreshData()

		self.SetScale(0.7, 0.7)

	def __AppendText(self, text):

		self.toolTip.AppendTextLine(text)
		self.toolTip.ResizeToolTip()

		#x=self.GetWidth()/2
		#textLine = ui.TextLine()
		#textLine.SetParent(self)
		#textLine.SetSize(0, 0)
		#textLine.SetOutline()
		#textLine.Hide()
		#textLine.SetPosition(x, 40+len(self.textLineList)*16)
		#textLine.SetText(text)
		#self.textLineList.append(textLine)

	def OnMouseOverIn(self):
		#for textLine in self.textLineList:
		#	textLine.Show()

		self.toolTip.ShowToolTip()

	def OnMouseOverOut(self):
		#for textLine in self.textLineList:
		#	textLine.Hide()

		self.toolTip.HideToolTip()

	def OnUpdate(self):
		self.__RefreshData()

class AffectImage(ui.ExpandedImageBox):

	def __init__(self):
		ui.ExpandedImageBox.__init__(self)

		self.toolTipText = None
		self.isSkillAffect = True
		self.description = None
		self.endTime = 0
		self.affect = None
		self.autoPotionIdx = -1
		self.imageList = None

	def ChangeImage(self, imageName):
		
		if self.GetImageName() != imageName:
			self.LoadImage(imageName)

	def GetTimeLeftInSeconds(self):

		if self.endTime > 0:
			return self.endTime - app.GetGlobalTimeStamp()
			
		return -1

	def SetImageList(self, list):
		self.imageList = list

	def SetAffect(self, affect):
		self.affect = affect

	def GetAffect(self):
		return self.affect

	def SetToolTipText(self, text, x = 0, y = -19 - 8):

		if not self.toolTipText:
			textLine = ui.TextLine()
			textLine.SetParent(self)
			textLine.SetSize(0, 0)
			textLine.SetOutline()
			textLine.Hide()
			self.toolTipText = textLine
			self.toolTipText.SetPosition(x + self.GetWidth()/2 - 20, y)

		# print "SetToolTipText %s %d %d" % (text,x,y)
		self.toolTipText.SetText(text)

	def SetDescription(self, description):
		self.description = description

	def SetDuration(self, duration):
		self.endTime = 0
		if duration >= 0:
			self.endTime = app.GetGlobalTimeStamp() + duration

	def UpdateAutoPotionDescription(self):		

		potionType = 0

		if self.affect == chr.NEW_AFFECT_AUTO_HP_RECOVERY:
			potionType = player.AUTO_POTION_TYPE_HP
		else:
			potionType = player.AUTO_POTION_TYPE_SP

		isActivated, currentAmount, totalAmount, slotIndex = player.GetAutoPotionInfo(potionType)

		# tchat("UpdateAutoPotionDescription %s %s %s %s" % (str(isActivated), str(currentAmount), str(totalAmount), str(slotIndex)))

		amountPercent = 0.0

		try:
			amountPercent = (float(currentAmount) / float(totalAmount)) * 100.0		
		except:
			amountPercent = 100.0

		self.SetToolTipText(self.description % amountPercent, 0, 48)

		# DON'T CHANGE IMAGE IF WE USE NEW AFFECT ICONS !!!
		if constInfo.NEW_AFFECT_ICONS:
			return

		if self.imageList != None:
			imgIndex = int(amountPercent / 20.0)
			if imgIndex == 5:
				imgIndex = 4
			if self.autoPotionIdx != imgIndex:
				self.autoPotionIdx = imgIndex
				self.LoadImage(self.imageList[imgIndex])
				# tchat("LoadImage %s" % self.imageList[imgIndex])
				self.SetScale(0.7, 0.7)

	if app.ENABLE_RUNE_AFFECT_ICONS:
		def RuneHarvestSoulCount(self, count):
			constInfo.RUNE_COLLECTED_SOULS_COUNT = int(count)

		def RuneAffectInfo(self, dam):
			constInfo.RUNE_AFFECT_INFO = int(dam)

	def UpdateDescription(self):
		if not self.description:
			return

		toolTip = self.description
		if self.endTime > 0 and self.endTime - app.GetGlobalTimeStamp() < 60 * 60 * 24 * 150:
			if self.IsSkillAffect() or (self.endTime - app.GetGlobalTimeStamp() <= 60 * 5):
				leftTime = localeInfo.SecondToDHMS(self.endTime - app.GetGlobalTimeStamp())
			else:
				leftTime = localeInfo.SecondToDHM(self.endTime - app.GetGlobalTimeStamp())
			toolTip += " (%s : %s)" % (localeInfo.LEFT_TIME, leftTime)

		if app.ENABLE_RUNE_AFFECT_ICONS:
			# PRECISION
			if self.affect == chr.NEW_AFFECT_RUNE_PRIMARY_SUBGROUP_KEY_1:
				if constInfo.RUNE_AFFECT_INFO == 0:
					toolTip +=localeInfo.RUNE_AFFECT_INFO_NOT_AVAILABLE
				else:
					toolTip +=localeInfo.RUNE_DAMAGE_GIVEN_INFO %(constInfo.RUNE_AFFECT_INFO)
			if self.affect == chr.NEW_AFFECT_RUNE_PRIMARY_SUBGROUP_KEY_2:
				if constInfo.RUNE_AFFECT_INFO == 0:
					toolTip +=localeInfo.RUNE_AFFECT_INFO_NOT_AVAILABLE
				else:
					toolTip +=localeInfo.RUNE_DAMAGE_GIVEN_INFO %(constInfo.RUNE_AFFECT_INFO)
			if self.affect == chr.NEW_AFFECT_RUNE_PRIMARY_SUBGROUP_KEY_3:
				if constInfo.RUNE_AFFECT_INFO == 0:
					toolTip +=localeInfo.RUNE_AFFECT_INFO_NOT_AVAILABLE
				else:
					toolTip +=localeInfo.RUNE_HEAL_BONUS_INFO %(constInfo.RUNE_AFFECT_INFO)

			# DOMINATION
			if self.affect == chr.NEW_AFFECT_RUNE_PRIMARY_SUBGROUP_KEY_13:
				toolTip +=": %s" % (rune.GetProtoDesc(13))
			if self.affect == chr.NEW_AFFECT_RUNE_PRIMARY_SUBGROUP_KEY_14:
				toolTip +=": %s" % (rune.GetProtoDesc(14))
			if self.affect == chr.NEW_AFFECT_RUNE_PRIMARY_SUBGROUP_KEY_15:
				toolTip +=localeInfo.RUNE_COLLECTED_SOULS_INFO %(constInfo.RUNE_COLLECTED_SOULS_COUNT)

			# SORCERY
			if self.affect == chr.NEW_AFFECT_RUNE_PRIMARY_SUBGROUP_KEY_25:
				toolTip +=": %s" % (rune.GetProtoDesc(25))
			if self.affect == chr.NEW_AFFECT_RUNE_PRIMARY_SUBGROUP_KEY_26:
				toolTip +=":  %s" %(constInfo.RUNE_AFFECT_INFO)
			if self.affect == chr.NEW_AFFECT_RUNE_PRIMARY_SUBGROUP_KEY_27:
				toolTip +=rune.GetProtoDesc(27)

			# RESOLVE
			if self.affect == chr.NEW_AFFECT_RUNE_PRIMARY_SUBGROUP_KEY_37:
				if constInfo.RUNE_AFFECT_INFO == 0:
					toolTip +=localeInfo.RUNE_AFFECT_INFO_NOT_AVAILABLE
				else:
					toolTip +=localeInfo.RUNE_MAGIC_ATTACK_DAMAGE_BONUS_INFO % (constInfo.RUNE_AFFECT_INFO)
			if self.affect == chr.NEW_AFFECT_RUNE_PRIMARY_SUBGROUP_KEY_38:
				if constInfo.RUNE_AFFECT_INFO == 0:
					toolTip +=localeInfo.RUNE_AFFECT_INFO_NOT_AVAILABLE
				else:
					toolTip +=localeInfo.RUNE_CURRENT_KILLS_COUNT_INFO % (constInfo.RUNE_AFFECT_INFO)
			if self.affect == chr.NEW_AFFECT_RUNE_PRIMARY_SUBGROUP_KEY_39:
				if constInfo.RUNE_AFFECT_INFO == 0:
					toolTip +=localeInfo.RUNE_AFFECT_INFO_NOT_AVAILABLE
				else:
					toolTip +=localeInfo.RUNE_MAGIC_SHIELD_BONUS_INFO % (constInfo.RUNE_AFFECT_INFO)

			# INSPIRATION
			if self.affect == chr.NEW_AFFECT_RUNE_PRIMARY_SUBGROUP_KEY_49:
				toolTip +=": %s" % (rune.GetProtoDesc(49))
			if self.affect == chr.NEW_AFFECT_RUNE_PRIMARY_SUBGROUP_KEY_50:
				toolTip +=": %s" % (rune.GetProtoDesc(50))
			if self.affect == chr.NEW_AFFECT_RUNE_PRIMARY_SUBGROUP_KEY_51:
				toolTip +=": %s" % (rune.GetProtoDesc(51))

		if constInfo.IS_TEST_SERVER:
			toolTip += " (affect: %s)" % str(self.affect)

		self.SetToolTipText(toolTip, 0, 48)

	def UpdateDescription2(self):
		if not self.description:
			return

		toolTip = self.description
		self.SetToolTipText(toolTip, 0, 48)

	def SetSkillAffectFlag(self, flag):
		self.isSkillAffect = flag

	def IsSkillAffect(self):
		return self.isSkillAffect

	def OnMouseOverIn(self):
		if self.toolTipText:
			self.toolTipText.Show()

	def OnMouseOverOut(self):
		if self.toolTipText:
			self.toolTipText.Hide()


if constInfo.ENABLE_COMPANION_NAME:
	class CompanionImage(ui.ExpandedImageBox):

		images = [
			[ "d:/ymir work/ui/game/companion_name/pet_a_b.tga", "d:/ymir work/ui/game/companion_name/pet_a_g.tga", "d:/ymir work/ui/game/companion_name/pet_a_r.tga" ],
			[ "d:/ymir work/ui/game/companion_name/mount_a_b.tga", "d:/ymir work/ui/game/companion_name/mount_a_g.tga", "d:/ymir work/ui/game/companion_name/mount_a_r.tga" ],
			[ "d:/ymir work/ui/game/companion_name/fakebuff.tga", "d:/ymir work/ui/game/companion_name/fakebuff.tga", "d:/ymir work/ui/game/companion_name/fakebuff.tga" ],
		]

		affects = [
			localeInfo.STRONG_VS_MONSTERS,
			localeInfo.STRONG_VS_METINS
		]

		def __init__(self):
			ui.ExpandedImageBox.__init__(self)

			textLine = ui.TextLine()
			textLine.SetParent(self)
			textLine.SetSize(0, 0)
			textLine.SetOutline()
			textLine.Hide()
			self.toolTipText = textLine
			self.endTime = 0
			self.index = 0
			self.type = 0

		def __del__(self):
			ui.ExpandedImageBox.__del__(self)

		def SetCompanionInfo(self, type, timeLeft):
			if timeLeft <= (3600 * 24):
				self.index = 2
			elif timeLeft <= (3600 * 24 * 3):
				self.index = 1

			self.LoadImage(self.images[type][self.index])
			self.SetScale(0.7, 0.7)
			self.type = type

			if type != 2:
				self.endTime = app.GetGlobalTimeStamp() + timeLeft
				self.UpdateTime()
			else:
				self.toolTipText.SetText(localeInfo.FAKEBUFF_NAME_AFFECT)
				self.toolTipText.SetPosition(0, 50)

		def UpdateTime(self):
			index = 0
			timeLeft = self.endTime - app.GetGlobalTimeStamp()
			if timeLeft <= (3600 * 24):
				index = 2
			elif timeLeft <= (3600 * 24 * 3):
				index = 1

			if self.index != index:
				self.LoadImage(self.images[self.type][index])
				self.index = index
			
			leftTime = localeInfo.SecondToDHM(self.endTime - app.GetGlobalTimeStamp())
			toolTip = "%s %d (%s : %s)" % (self.affects[self.type], 10, localeInfo.LEFT_TIME, leftTime)
			self.toolTipText.SetText(toolTip)
			self.toolTipText.SetPosition(0, 50)

		def OnMouseOverIn(self):
			self.toolTipText.Show()

		def OnMouseOverOut(self):
			self.toolTipText.Hide()


if constInfo.LEADERSHIP_EXTENSION:
	class LeadershipImage(ui.ExpandedImageBox):

		AFFECT_LIST = [
			localeInfo.PARTY_BONUS_ATTACKER,
			localeInfo.PARTY_BONUS_BERSERKER,
			localeInfo.PARTY_BONUS_TANKER,
			localeInfo.PARTY_BONUS_BUFFER,
			localeInfo.PARTY_BONUS_SKILL_MASTER,
			localeInfo.PARTY_BONUS_DEFENDER
		]

		def __init__(self):
			ui.ExpandedImageBox.__init__(self)

			textLine = ui.TextLine()
			textLine.SetParent(self)
			textLine.SetSize(0, 0)
			textLine.SetOutline()
			textLine.Hide()
			self.toolTipText = textLine
			self.LoadImage("d:/ymir work/ui/skill/common/support/tongsol.sub")
			self.SetScale(0.7, 0.7)

		def __del__(self):
			ui.ExpandedImageBox.__del__(self)

		def SetLeadershipInfo(self, state):
			skillIndex = player.SKILL_INDEX_TONGSOL
			slotIndex = player.GetSkillSlotIndex(skillIndex)
			k = player.GetSkillCurrentEfficientPercentage(slotIndex)
			bonus = 0

			if state == 1:
				bonus = 10 + 88 * k
			elif state == 2:
				bonus = 1 + 7.2 * k
			elif state == 3:
				bonus = 50 + 1960 * k
			elif state == 4:
				bonus = 5 + 92 * k
			elif state == 5:
				bonus = 25 + 780 * k
			elif state == 6:
				bonus = 5 + 76 * k

			self.toolTipText.SetText("%s" % self.AFFECT_LIST[state - 1](bonus))
			self.toolTipText.SetPosition(0, 50)

		def OnMouseOverIn(self):
			self.toolTipText.Show()

		def OnMouseOverOut(self):
			self.toolTipText.Hide()


if constInfo.UPGRADE_STONE:
	class UpgradeStoneImage(ui.ExpandedImageBox):
		def __init__(self):
			ui.ExpandedImageBox.__init__(self)

			textLine = ui.TextLine()
			textLine.SetParent(self)
			textLine.SetSize(0, 0)
			textLine.SetOutline()
			textLine.Hide()
			self.toolTipText = textLine

			self.toolTipText.SetText(localeInfo.TOOLTIP_UPGRADE_STONE)
			self.toolTipText.SetPosition(0, 50)

			item.SelectItem(1, 2, 94209)
			self.LoadImage(item.GetIconImageFileName())
			self.SetScale(0.7, 0.7)

		def __del__(self):
			ui.ExpandedImageBox.__del__(self)

		def OnMouseOverIn(self):
			self.toolTipText.Show()

		def OnMouseOverOut(self):
			self.toolTipText.Hide()


class AffectShower(ui.Window):

	MALL_DESC_IDX_START = 1000
	BLEND_IDX_START = 1300
	AFFECT_BY_ITEM_START = 10000
	IMAGE_STEP = 25
	AFFECT_MAX_NUM = 32

	AFFECT_DATA_DICT =	{
			chr.AFFECT_POISON : (localeInfo.SKILL_TOXICDIE, "d:/ymir work/ui/skill/common/affect/poison.sub"),
			chr.AFFECT_SLOW : (localeInfo.SKILL_SLOW, "d:/ymir work/ui/skill/common/affect/slow.sub"),
			chr.AFFECT_STUN : (localeInfo.SKILL_STUN, "d:/ymir work/ui/skill/common/affect/stun.sub"),

			chr.AFFECT_ATT_SPEED_POTION : (localeInfo.SKILL_INC_ATKSPD, "d:/ymir work/ui/skill/common/affect/Increase_Attack_Speed.sub"),
			chr.AFFECT_MOV_SPEED_POTION : (localeInfo.SKILL_INC_MOVSPD, "d:/ymir work/ui/skill/common/affect/Increase_Move_Speed.sub"),
			chr.AFFECT_FISH_MIND : (localeInfo.SKILL_FISHMIND, "d:/ymir work/ui/skill/common/affect/fishmind.sub"),

			chr.AFFECT_JEONGWI : (localeInfo.SKILL_JEONGWI, "d:/ymir work/ui/skill/warrior/jeongwi_03.sub",),
			chr.AFFECT_GEOMGYEONG : (localeInfo.SKILL_GEOMGYEONG, "d:/ymir work/ui/skill/warrior/geomgyeong_03.sub",),
			chr.AFFECT_GEOMGYEONG_PERFECT : (localeInfo.SKILL_GEOMGYEONG, "d:/ymir work/ui/skill/warrior/geomgyeong_03.sub",),
			chr.AFFECT_CHEONGEUN : (localeInfo.SKILL_CHEONGEUN, "d:/ymir work/ui/skill/warrior/cheongeun_03.sub",),
			chr.AFFECT_CHEONGEUN_PERFECT : (localeInfo.SKILL_CHEONGEUN, "d:/ymir work/ui/skill/warrior/cheongeun_03.sub",),
			chr.AFFECT_GYEONGGONG : (localeInfo.SKILL_GYEONGGONG, "d:/ymir work/ui/skill/assassin/gyeonggong_03.sub",),
			chr.AFFECT_EUNHYEONG : (localeInfo.SKILL_EUNHYEONG, "d:/ymir work/ui/skill/assassin/eunhyeong_03.sub",),
			chr.AFFECT_GWIGEOM : (localeInfo.SKILL_GWIGEOM, "d:/ymir work/ui/skill/sura/gwigeom_03.sub",),
			chr.AFFECT_GWIGEOM_PERFECT : (localeInfo.SKILL_GWIGEOM, "d:/ymir work/ui/skill/sura/gwigeom_03.sub",),
			chr.AFFECT_GONGPO : (localeInfo.SKILL_GONGPO, "d:/ymir work/ui/skill/sura/gongpo_03.sub",),
			chr.AFFECT_GONGPO_PERFECT : (localeInfo.SKILL_GONGPO, "d:/ymir work/ui/skill/sura/gongpo_03.sub",),
			chr.AFFECT_JUMAGAP : (localeInfo.SKILL_JUMAGAP, "d:/ymir work/ui/skill/sura/jumagap_03.sub"),
			chr.AFFECT_HOSIN : (localeInfo.SKILL_HOSIN, "d:/ymir work/ui/skill/shaman/hosin_03.sub",),
			chr.AFFECT_HOSIN_PERFECT : (localeInfo.SKILL_HOSIN, "d:/ymir work/ui/skill/shaman/hosin_03.sub",),
			chr.AFFECT_BOHO : (localeInfo.SKILL_BOHO, "d:/ymir work/ui/skill/shaman/boho_03.sub",),
			chr.AFFECT_KWAESOK : (localeInfo.SKILL_KWAESOK, "d:/ymir work/ui/skill/shaman/kwaesok_03.sub",),
			chr.AFFECT_HEUKSIN : (localeInfo.SKILL_HEUKSIN, "d:/ymir work/ui/skill/sura/heuksin_03.sub",),
			chr.AFFECT_HEUKSIN_PERFECT : (localeInfo.SKILL_HEUKSIN, "d:/ymir work/ui/skill/sura/heuksin_03.sub",),
			chr.AFFECT_MUYEONG : (localeInfo.SKILL_MUYEONG, "d:/ymir work/ui/skill/sura/muyeong_03.sub",),
			chr.AFFECT_GICHEON : (localeInfo.SKILL_GICHEON, "d:/ymir work/ui/skill/shaman/gicheon_03.sub",),
			chr.AFFECT_GICHEON_PERFECT : (localeInfo.SKILL_GICHEON, "d:/ymir work/ui/skill/shaman/gicheon_03.sub",),
			chr.AFFECT_JEUNGRYEOK : (localeInfo.SKILL_JEUNGRYEOK, "d:/ymir work/ui/skill/shaman/jeungryeok_03.sub",),
			chr.AFFECT_PABEOP : (localeInfo.SKILL_PABEOP, "d:/ymir work/ui/skill/sura/pabeop_03.sub",),
			chr.AFFECT_FALLEN_CHEONGEUN : (localeInfo.SKILL_CHEONGEUN, "d:/ymir work/ui/skill/warrior/cheongeun_03.sub",),
			chr.AFFECT_CHINA_FIREWORK : (localeInfo.SKILL_POWERFUL_STRIKE, "d:/ymir work/ui/skill/common/affect/powerfulstrike.sub",),

			#64 - END
			chr.NEW_AFFECT_EXP_BONUS : (localeInfo.TOOLTIP_MALL_EXPBONUS_STATIC, "d:/ymir work/ui/skill/common/affect/exp_bonus.sub",),

			chr.NEW_AFFECT_ITEM_BONUS : (localeInfo.TOOLTIP_MALL_ITEMBONUS_STATIC, "d:/ymir work/ui/skill/common/affect/item_bonus.sub",),
			chr.NEW_AFFECT_SAFEBOX : (localeInfo.TOOLTIP_MALL_SAFEBOX, "d:/ymir work/ui/skill/common/affect/safebox.sub",),
			chr.NEW_AFFECT_AUTOLOOT : (localeInfo.TOOLTIP_MALL_AUTOLOOT, "d:/ymir work/ui/skill/common/affect/autoloot.sub",),
			chr.NEW_AFFECT_FISH_MIND : (localeInfo.TOOLTIP_MALL_FISH_MIND, "d:/ymir work/ui/skill/common/affect/fishmind.sub",),
			chr.NEW_AFFECT_MARRIAGE_FAST : (localeInfo.TOOLTIP_MALL_MARRIAGE_FAST, "d:/ymir work/ui/skill/common/affect/marriage_fast.sub",),
			chr.NEW_AFFECT_GOLD_BONUS : (localeInfo.TOOLTIP_MALL_GOLDBONUS_STATIC, "d:/ymir work/ui/skill/common/affect/gold_bonus.sub",),

			chr.NEW_AFFECT_NO_DEATH_PENALTY : (localeInfo.TOOLTIP_APPLY_NO_DEATH_PENALTY, "d:/ymir work/ui/skill/common/affect/gold_premium.sub"),
			chr.NEW_AFFECT_SKILL_BOOK_BONUS : (localeInfo.TOOLTIP_APPLY_SKILL_BOOK_BONUS, "d:/ymir work/ui/skill/common/affect/gold_premium.sub"),
			chr.NEW_AFFECT_SKILL_BOOK_NO_DELAY : (localeInfo.TOOLTIP_APPLY_SKILL_BOOK_NO_DELAY, "d:/ymir work/ui/skill/common/affect/gold_premium.sub"),

			MALL_DESC_IDX_START+player.POINT_ATT_BONUS : (localeInfo.TOOLTIP_MALL_ATTBONUS_STATIC, "d:/ymir work/ui/skill/common/affect/att_bonus.sub",),
			MALL_DESC_IDX_START+player.POINT_MALL_DEFBONUS : (localeInfo.TOOLTIP_MALL_DEFBONUS_STATIC, "d:/ymir work/ui/skill/common/affect/def_bonus.sub",),
			MALL_DESC_IDX_START+player.POINT_MALL_EXPBONUS : (localeInfo.TOOLTIP_MALL_EXPBONUS, "d:/ymir work/ui/skill/common/affect/exp_bonus.sub",),
			MALL_DESC_IDX_START+player.POINT_MALL_ITEMBONUS : (localeInfo.TOOLTIP_MALL_ITEMBONUS, "d:/ymir work/ui/skill/common/affect/item_bonus.sub",),
			MALL_DESC_IDX_START+player.POINT_MALL_GOLDBONUS : (localeInfo.TOOLTIP_MALL_GOLDBONUS, "d:/ymir work/ui/skill/common/affect/gold_bonus.sub",),
			
			MALL_DESC_IDX_START+player.POINT_CRITICAL_PCT : (localeInfo.TOOLTIP_APPLY_CRITICAL_PCT,"d:/ymir work/ui/skill/common/affect/critical.sub"),
			MALL_DESC_IDX_START+player.POINT_PENETRATE_PCT : (localeInfo.TOOLTIP_APPLY_PENETRATE_PCT, "d:/ymir work/ui/skill/common/affect/gold_premium.sub"),

			# MALL_DESC_IDX_START+player.POINT_CRITICAL_PCT : (localeInfo.TOOLTIP_APPLY_CRITICAL_PCT,"d:/ymir work/ui/affects/71044_b.tga"),
			# MALL_DESC_IDX_START+player.POINT_PENETRATE_PCT : (localeInfo.TOOLTIP_APPLY_PENETRATE_PCT, "d:/ymir work/ui/affects/71045_b.tga"),

			MALL_DESC_IDX_START+player.POINT_MAX_HP_PCT : (localeInfo.TOOLTIP_MAX_HP_PCT, "d:/ymir work/ui/skill/common/affect/gold_premium.sub"),
			MALL_DESC_IDX_START+player.POINT_MAX_SP_PCT : (localeInfo.TOOLTIP_MAX_SP_PCT, "d:/ymir work/ui/skill/common/affect/gold_premium.sub"),	
			
			# chr.AFFECT_RED_POSSESSION : (localeInfo.AFFECT_RED_POSSESSION, "d:/ymir work/ui/skill/wolfman/red_possession_03.sub",),
			# chr.AFFECT_BLUE_POSSESSION : (localeInfo.AFFECT_BLUE_POSSESSION, "d:/ymir work/ui/skill/wolfman/blue_possession_03.sub",),
			# chr.AFFECT_BLEEDING : (localeInfo.SKILL_BLEEDING, "d:/ymir work/ui/skill/common/affect/poison.sub",),

			chr.NEW_AFFECT_RAMADAN1 : (localeInfo.TOOLTIP_VOTE4BUFF, "d:/ymir work/ui/skill/common/affect/vote4buff.tga"),#"icon/item/25101.tga"),
			chr.NEW_AFFECT_RAMADAN2 : (localeInfo.TOOLTIP_VOTE4BUFF, "icon/item/31004.tga"),
			
			chr.NEW_AFFECT_VOTE4BUFF : (localeInfo.TOOLTIP_VOTE4BUFF, "d:/ymir work/ui/skill/common/affect/vote4buff.tga"),

			chr.NEW_AFFECT_ALIGNMENT_GOOD : (localeInfo.TOOLTIP_ALIGNMENT_GOOD, "d:/ymir work/ui/skill/common/affect/gold_premium.sub"),
			chr.NEW_AFFECT_ALIGNMENT_BAD : (localeInfo.TOOLTIP_ALIGNMENT_BAD, "d:/ymir work/ui/skill/common/affect/gold_premium.sub"),

			chr.NEW_AFFECT_AUTO_HP_RECOVERY : (localeInfo.TOOLTIP_AUTO_POTION_REST, (\
				"d:/ymir work/ui/pattern/auto_hpgauge/01.dds",\
				"d:/ymir work/ui/pattern/auto_hpgauge/02.dds",\
				"d:/ymir work/ui/pattern/auto_hpgauge/03.dds",\
				"d:/ymir work/ui/pattern/auto_hpgauge/04.dds",\
				"d:/ymir work/ui/pattern/auto_hpgauge/05.dds",\
			)),
			chr.NEW_AFFECT_AUTO_SP_RECOVERY : (localeInfo.TOOLTIP_AUTO_POTION_REST, (\
				"d:/ymir work/ui/pattern/auto_spgauge/01.dds",\
				"d:/ymir work/ui/pattern/auto_spgauge/02.dds",\
				"d:/ymir work/ui/pattern/auto_spgauge/03.dds",\
				"d:/ymir work/ui/pattern/auto_spgauge/04.dds",\
				"d:/ymir work/ui/pattern/auto_spgauge/05.dds",\
			)),

			100000 : (localeInfo.TOOLTIP_PREMIUM_STATIC, "d:/ymir work/ui/game/affects/premium.tga"),
	}

	if app.ENABLE_HYDRA_DUNGEON:
		AFFECT_DATA_DICT[chr.NEW_AFFECT_HYDRA] = (localeInfo.TOOLTIP_HYDRA_DEBUFF, "d:/ymir work/ui/skill/common/affect/gold_premium.sub")

	if app.ENABLE_DRAGON_SOUL_SYSTEM:
		AFFECT_DATA_DICT[chr.NEW_AFFECT_DRAGON_SOUL_DECK1] = (localeInfo.TOOLTIP_DRAGON_SOUL_DECK1, "d:/ymir work/ui/dragonsoul/buff_ds_sky1.tga")
		AFFECT_DATA_DICT[chr.NEW_AFFECT_DRAGON_SOUL_DECK2] = (localeInfo.TOOLTIP_DRAGON_SOUL_DECK2, "d:/ymir work/ui/dragonsoul/buff_ds_land1.tga")

	if (app.COMBAT_ZONE):
		AFFECT_DATA_DICT[chr.NEW_AFFECT_COMBAT_ZONE_POTION] = (localeInfo.COMBAT_ZONE_TOOLTIP_BATTLE_POTION, "icon/item/27125.tga")

	if app.ENABLE_AFFECT_POLYMORPH_REMOVE:
		AFFECT_DATA_DICT[ chr.NEW_AFFECT_POLYMORPH ] = (localeInfo.AFFECT_REMOVE_TOOLTIP, "icon/item/70104.tga")

	if constInfo.RUNE_ENABLED:
		AFFECT_DATA_DICT[ chr.NEW_AFFECT_RUNE_MOUNT_PARALYZE ] = (localeInfo.AFFECT_MOUNT_PARALYZE, "d:/ymir work/ui/pattern/HorseState/10.dds")
	
	if app.ENABLE_RUNE_AFFECT_ICONS:
		AFFECT_DATA_DICT[ chr.NEW_AFFECT_RUNE_PRIMARY_SUBGROUP_KEY_1 ] = (rune.GetProtoName(1), "d:/ymir work/effect/affect/runes/rune1.tga")
		AFFECT_DATA_DICT[ chr.NEW_AFFECT_RUNE_PRIMARY_SUBGROUP_KEY_2 ] = (rune.GetProtoName(2), "d:/ymir work/effect/affect/runes/rune2.tga")
		AFFECT_DATA_DICT[ chr.NEW_AFFECT_RUNE_PRIMARY_SUBGROUP_KEY_3 ] = (rune.GetProtoName(3), "d:/ymir work/effect/affect/runes/rune3.tga")

		AFFECT_DATA_DICT[ chr.NEW_AFFECT_RUNE_PRIMARY_SUBGROUP_KEY_13 ] = (rune.GetProtoName(13), "d:/ymir work/effect/affect/runes/rune4.tga")
		AFFECT_DATA_DICT[ chr.NEW_AFFECT_RUNE_PRIMARY_SUBGROUP_KEY_14 ] = (rune.GetProtoName(14), "d:/ymir work/effect/affect/runes/rune5.tga")
		AFFECT_DATA_DICT[ chr.NEW_AFFECT_RUNE_PRIMARY_SUBGROUP_KEY_15 ] = (rune.GetProtoName(15), "d:/ymir work/effect/affect/runes/rune6.tga")

		AFFECT_DATA_DICT[ chr.NEW_AFFECT_RUNE_PRIMARY_SUBGROUP_KEY_25 ] = (rune.GetProtoName(25), "d:/ymir work/effect/affect/runes/rune7.tga")
		AFFECT_DATA_DICT[ chr.NEW_AFFECT_RUNE_PRIMARY_SUBGROUP_KEY_26 ] = (rune.GetProtoName(26), "d:/ymir work/effect/affect/runes/rune8.tga")
		AFFECT_DATA_DICT[ chr.NEW_AFFECT_RUNE_PRIMARY_SUBGROUP_KEY_27 ] = (rune.GetProtoName(27), "d:/ymir work/effect/affect/runes/rune9.tga")

		AFFECT_DATA_DICT[ chr.NEW_AFFECT_RUNE_PRIMARY_SUBGROUP_KEY_37 ] = (rune.GetProtoName(37), "d:/ymir work/effect/affect/runes/rune10.tga")
		AFFECT_DATA_DICT[ chr.NEW_AFFECT_RUNE_PRIMARY_SUBGROUP_KEY_38 ] = (rune.GetProtoName(38), "d:/ymir work/effect/affect/runes/rune11.tga")
		AFFECT_DATA_DICT[ chr.NEW_AFFECT_RUNE_PRIMARY_SUBGROUP_KEY_39 ] = (rune.GetProtoName(39), "d:/ymir work/effect/affect/runes/rune12.tga")

		AFFECT_DATA_DICT[ chr.NEW_AFFECT_RUNE_PRIMARY_SUBGROUP_KEY_49 ] = (rune.GetProtoName(49), "d:/ymir work/effect/affect/runes/rune13.tga")
		AFFECT_DATA_DICT[ chr.NEW_AFFECT_RUNE_PRIMARY_SUBGROUP_KEY_50 ] = (rune.GetProtoName(50), "d:/ymir work/effect/affect/runes/rune14.tga")
		AFFECT_DATA_DICT[ chr.NEW_AFFECT_RUNE_PRIMARY_SUBGROUP_KEY_51 ] = (rune.GetProtoName(51), "d:/ymir work/effect/affect/runes/rune15.tga")

	def __init__(self):
		ui.Window.__init__(self)

		self.questionDlg = uiCommon.QuestionDialog()
		self.questionDlg.Close()

		self.lastUpdateTime=0
		self.skillAffectDict={}
		self.affectImageDict={}
		self.affectImageDict2={}
		self.affectImageDict_old={}
		self.affectImageDict2_old={}
		self.itemImageDict={}
		self.horseImage=None
		self.lovePointImage=None
		if constInfo.ENABLE_COMPANION_NAME:
			self.companionImagePet = None
			self.companionImageMount = None
			self.companionImageFakebuff = None
		if constInfo.LEADERSHIP_EXTENSION:
			self.leadershipImage = None
		if constInfo.UPGRADE_STONE:
			self.upgradeStoneImage = None
		self.SetPosition(10, 10)
		self.Show()

	def ClearAllAffects(self):
		self.horseImage=None
		self.lovePointImage=None
		self.skillAffectDict={}
		self.affectImageDict={}
		self.itemImageDict={}
		self.affectImageDict2={}
		self.affectImageDict_old={}
		self.affectImageDict2_old={}
		self.__ArrangeImageList()

	def Close(self):
		for image in self.affectImageDict.values() + self.affectImageDict2.values():
			image.Hide()
			
		if self.leadershipImage:
			self.leadershipImage.Hide()

	def Open(self):
		for image in self.affectImageDict.values() + self.affectImageDict2.values():
			image.Show()
		if self.leadershipImage:
			self.leadershipImage.Show()

	def ClearAffects(self):
		self.living_affectImageDict={}
		
		# Because ClearAffect gots called twice, once before the DeadPacket arrives
		if not constInfo.DEATH_KEEP_SKILL_AFFECT_ICONS:
			self.affectImageDict_old = self.affectImageDict
			self.affectImageDict2_old = self.affectImageDict2
		else:
			self.affectImageDict = self.affectImageDict_old
			self.affectImageDict2 = self.affectImageDict2_old

		for key, image in self.affectImageDict.items():
			if not image.IsSkillAffect() or constInfo.DEATH_KEEP_SKILL_AFFECT_ICONS:
				self.living_affectImageDict[key] = image
		self.affectImageDict = self.living_affectImageDict

		self.living_affectImageDict2={}
		for key, image in self.affectImageDict2.items():
			if not image.IsSkillAffect() or constInfo.DEATH_KEEP_SKILL_AFFECT_ICONS:
				self.living_affectImageDict2[key] = image

		if constInfo.DEATH_KEEP_SKILL_AFFECT_ICONS:
			constInfo.DEATH_KEEP_SKILL_AFFECT_ICONS = False

		self.affectImageDict2 = self.living_affectImageDict2
		self.__ArrangeImageList()

	def RemoveAffect(self):
		net.SendChatPacket("/remove_affect %d %d" % (self.questionDlg.affectIdx, self.questionDlg.pointIdx))
		self.questionDlg.Close()

	def __RemoveAffectClick(self, affectIdx, pointIdx = 0):
		self.questionDlg.SetText(localeInfo.AFFECT_REMOVE_DESC)
		self.questionDlg.SetWidth(300)
		self.questionDlg.SetAcceptText(uiScriptLocale.YES)
		self.questionDlg.SetCancelText(uiScriptLocale.NO)
		self.questionDlg.affectIdx = affectIdx
		self.questionDlg.pointIdx = pointIdx
		self.questionDlg.SAFE_SetAcceptEvent(self.RemoveAffect)
		self.questionDlg.SetCancelEvent(self.questionDlg.Close)
		self.questionDlg.Open()

	def BINARY_NEW_AddAffect(self, affType, pointIdx, value, affFlag, duration):
		is2ndLine = False
		if affFlag > chr.AFFECT_NUM:
			if not item.SelectItem(1, 2, affFlag):
				return

			affect = self.AFFECT_BY_ITEM_START + affFlag
			applyaffType = constInfo.POINT_TYPE_TO_APPLY_TYPE.get(pointIdx, item.APPLY_NONE)
			if applyaffType == item.APPLY_NONE:
				tchat("AFF_ITEM: apply == NONE [point %d]" % pointIdx)
				return

			description = uiToolTip.GET_AFFECT_STRING(applyaffType, int(value))
			filename = item.GetIconImageFileName()

		else:
			if affType < 500 and not affType == 220:
				if affType < 120:
					self.skillAffectDict[affType] = app.GetGlobalTimeStamp() + duration

					i = 0
					affectIdx = player.SkillIndexToAffectIndex(affType)
					
					# tchat("player.SkillIndexToAffectIndex(affType) = %d" % player.SkillIndexToAffectIndex(affType))

					while affectIdx != 0:
						i += 1
						if self.affectImageDict.has_key(affectIdx):
							self.affectImageDict[affectIdx].SetDuration(duration)
						affectIdx = player.SkillIndexToAffectIndex(affType, i)

				return

			if affType == chr.NEW_AFFECT_MALL:
				affect = self.MALL_DESC_IDX_START + pointIdx
				is2ndLine = True
			elif affType == chr.NEW_AFFECT_BLEND:
				affect = self.BLEND_IDX_START + pointIdx
				is2ndLine = True
			elif affType == chr.NEW_AFFECT_BLEND+1:
				affect = 3000 + self.BLEND_IDX_START + pointIdx
				is2ndLine = True
			else:
				affect = affType

			if self.affectImageDict.has_key(affect) or self.affectImageDict2.has_key(affect) and is2ndLine:
				return

			if affType == chr.NEW_AFFECT_BLEND:
				applyaffType = constInfo.POINT_TYPE_TO_APPLY_TYPE.get(pointIdx, item.APPLY_NONE)
				if applyaffType == item.APPLY_NONE:
					tchat("BLEND: apply == NONE [point %d]" % pointIdx)
					return

				vnum = item.GetBlendVnumByApplyType(applyaffType)
				if vnum == 0 or not item.SelectItem(1, 2, vnum):
					tchat("BLEND: vnum == 0 or not select (vnum %d)" % vnum)
					return

				description = uiToolTip.GET_AFFECT_STRING(applyaffType, int(value))
				filename = item.GetIconImageFileName()

				# tchat("Vnum1: %s, desc: %s, filename: %s" % (str(vnum), str(description), str(filename)))

			elif affType == chr.NEW_AFFECT_BLEND + 1:
				applyaffType = constInfo.POINT_TYPE_TO_APPLY_TYPE.get(pointIdx, item.APPLY_NONE)
				if applyaffType == item.APPLY_NONE:
					tchat("BLEND: apply == NONE [point %d]" % pointIdx)
					return
				description = uiToolTip.GET_AFFECT_STRING(applyaffType, int(value))
				filename = 'd:/ymir work/ui/affects/green_potion.tga'

			elif affType == chr.NEW_AFFECT_BLEND + 2:
				applyaffType = constInfo.POINT_TYPE_TO_APPLY_TYPE.get(pointIdx, item.APPLY_NONE)
				if applyaffType == item.APPLY_NONE:
					tchat("BLEND: apply == NONE [point %d]" % pointIdx)
					return

				description = uiToolTip.GET_AFFECT_STRING(applyaffType, int(value))
				filename = 'icon/item/95219.tga'

			elif affType == chr.NEW_AFFECT_BLEND + 3:
				applyaffType = constInfo.POINT_TYPE_TO_APPLY_TYPE.get(pointIdx, item.APPLY_NONE)
				if applyaffType == item.APPLY_NONE:
					tchat("BLEND: apply == NONE [point %d]" % pointIdx)
					return

				description = uiToolTip.GET_AFFECT_STRING(applyaffType, int(value))
				filename = 'icon/item/95220.tga'

			else:
				if not self.AFFECT_DATA_DICT.has_key(affect):
					return

				## ����� ��ȣ, ������ ������ Duration �� 0 ���� �����Ѵ�.
				if affect == chr.NEW_AFFECT_NO_DEATH_PENALTY or\
				   affect == chr.NEW_AFFECT_SKILL_BOOK_BONUS or\
				   affect == chr.NEW_AFFECT_AUTO_SP_RECOVERY or\
				   affect == chr.NEW_AFFECT_AUTO_HP_RECOVERY or\
				   affect == chr.NEW_AFFECT_SKILL_BOOK_NO_DELAY:
					duration = 0

				if app.ENABLE_HYDRA_DUNGEON and affect == chr.NEW_AFFECT_HYDRA:
					duration = 0

				affectData = self.AFFECT_DATA_DICT[affect]
				description = affectData[0]
				filename = affectData[1]

				if pointIdx == player.POINT_MALL_ITEMBONUS or\
				   pointIdx == player.POINT_MALL_GOLDBONUS:
					value = 1 + float(value) / 100.0

				if affect not in(chr.NEW_AFFECT_AUTO_SP_RECOVERY, chr.NEW_AFFECT_AUTO_HP_RECOVERY):
					try:
						description = description(float(value))
					except:
						try:
							description = description % str(value)
						except:
							try:
								description = description % float(value)
							except:
								pass

		#tchat("Add affect %s" % str(affect))
		image = AffectImage()
		#image.SetParent(self)
		if type(filename) == str:
			# tchat("setFileName %s" % str(filename))
			image.LoadImage(filename)
		else:
			# tchat("setImageList %s" % str(filename))
			image.SetImageList(filename)
		image.SetDescription(description)
		image.SetDuration(duration)
		image.SetAffect(affect)

		# Add unpoly event
		if affect == chr.NEW_AFFECT_POLYMORPH:
			image.SAFE_SetStringEvent("MOUSE_LEFT_DOWN", self.__RemoveAffectClick, affect)

		if affType == chr.NEW_AFFECT_BLEND:
			image.SAFE_SetStringEvent("MOUSE_LEFT_DOWN", self.__RemoveAffectClick, affType, pointIdx)

		if affect == chr.NEW_AFFECT_EXP_BONUS_EURO_FREE or\
			affect == chr.NEW_AFFECT_EXP_BONUS_EURO_FREE_UNDER_15:
			image.UpdateDescription2()
		elif affect == chr.NEW_AFFECT_AUTO_SP_RECOVERY or affect == chr.NEW_AFFECT_AUTO_HP_RECOVERY:
			image.UpdateAutoPotionDescription()
		else:
			image.UpdateDescription()
		if affect == chr.NEW_AFFECT_DRAGON_SOUL_DECK1 or affect == chr.NEW_AFFECT_DRAGON_SOUL_DECK2:
			image.SetScale(1, 1)
		else:
			image.SetScale(0.7, 0.7)
		image.SetSkillAffectFlag(False)
		image.Show()
		if is2ndLine:
			self.affectImageDict2[affect] = image
		else:
			self.affectImageDict[affect] = image
		self.__ArrangeImageList()

	def BINARY_AddItemAffect(self, itemVnum, duration):
		if int(itemVnum) in self.itemImageDict.keys():
			tchat("Error: BINARY_AddItemAffect %d already added!")
			return
			
		item.SelectItem(1, 2, int(itemVnum))
		description = item.GetItemName()
		image = AffectImage()
		image.LoadImage(item.GetIconImageFileName())
		image.SetDescription(description)
		image.SetDuration(int(duration))
		image.UpdateDescription()
		image.SetScale(0.65, 0.70)
		image.SetSkillAffectFlag(False)
		image.Show()
		self.itemImageDict[int(itemVnum)] = image
		self.__ArrangeImageList()

	def BINARY_RemoveItemAffect(self, itemVnum):

		if self.itemImageDict.has_key(int(itemVnum)):
			del self.itemImageDict[int(itemVnum)]
			self.__ArrangeImageList()

	def BINARY_NEW_RemoveAffect(self, type, pointIdx, flag):
		if flag > chr.AFFECT_NUM:
			affect = self.AFFECT_BY_ITEM_START + flag
		elif type == chr.NEW_AFFECT_MALL:
			affect = self.MALL_DESC_IDX_START + pointIdx
		elif type == chr.NEW_AFFECT_BLEND:
			affect = self.BLEND_IDX_START + pointIdx
		elif type == chr.NEW_AFFECT_BLEND+1:
			affect = 3000 + self.BLEND_IDX_START + pointIdx
		else:
			affect = type
	
		self.__RemoveAffect(affect)
		self.__ArrangeImageList()

	def SetAffect(self, affect):
		self.__AppendAffect(affect)
		self.__ArrangeImageList()

	def ResetAffect(self, affect):
		self.__RemoveAffect(affect)
		self.__ArrangeImageList()

	def SetLoverInfo(self, name, lovePoint):
		image = LovePointImage()
		image.SetLoverInfo(name, lovePoint)
		self.lovePointImage = image
		self.__ArrangeImageList()

	def ShowLoverState(self):
		if self.lovePointImage:
			self.lovePointImage.Show()
			self.__ArrangeImageList()

	def HideLoverState(self):
		if self.lovePointImage:
			self.lovePointImage.Hide()
			self.__ArrangeImageList()

	def ClearLoverState(self):
		self.lovePointImage = None
		self.__ArrangeImageList()

	def OnUpdateLovePoint(self, lovePoint):
		if self.lovePointImage:
			self.lovePointImage.OnUpdateLovePoint(lovePoint)

	def SetHorseState(self, level, used_time, max_time):
		if level==0:
			self.horseImage=None
		else:
			image = HorseImage()
			image.SetState(level, used_time, max_time)
			image.Show()

			self.horseImage=image

		self.__ArrangeImageList()

	def __AppendAffect(self, affect):

		if self.affectImageDict.has_key(affect) or self.affectImageDict2.has_key(affect):
			return

		try:
			affectData = self.AFFECT_DATA_DICT[affect]
		except KeyError:
			return

		name = affectData[0]
		filename = affectData[1]

		skillIndex = player.AffectIndexToSkillIndex(affect)
		if 0 != skillIndex:
			name = skill.GetSkillName(skillIndex)

		image = AffectImage()
		image.SetSkillAffectFlag(True)
		image.SetDescription(name)

		if self.skillAffectDict.has_key(skillIndex):
			endTime = self.skillAffectDict[skillIndex]
			image.SetDuration(endTime - app.GetGlobalTimeStamp())
			image.SAFE_SetStringEvent("MOUSE_LEFT_DOWN", self.__RemoveAffectClick, skillIndex)

		try:
			image.LoadImage(filename)
		except:
			pass

		image.SetScale(0.7, 0.7)
		image.Show()
		self.affectImageDict[affect] = image

	def __RemoveAffect(self, affect):
		if self.affectImageDict2.has_key(affect):
			del self.affectImageDict2[affect]

		if self.affectImageDict.has_key(affect):
			del self.affectImageDict[affect]

		if app.ENABLE_RUNE_AFFECT_ICONS:
			constInfo.RUNE_AFFECT_INFO = 0

	def __ArrangeImageList(self):
		xPos = 10
		yPos = 10

		use2ndLine = False

		if constInfo.ENABLE_COMPANION_NAME:
			if self.companionImagePet and self.companionImagePet.IsShow():
				self.companionImagePet.SetPosition(xPos, yPos)
				xPos += self.IMAGE_STEP
				use2ndLine = True
			if self.companionImageMount and self.companionImageMount.IsShow():
				self.companionImageMount.SetPosition(xPos, yPos)
				xPos += self.IMAGE_STEP
				use2ndLine = True
			if self.companionImageFakebuff and self.companionImageFakebuff.IsShow():
				self.companionImageFakebuff.SetPosition(xPos, yPos)
				xPos += self.IMAGE_STEP
				use2ndLine = True

		if constInfo.LEADERSHIP_EXTENSION:
			if self.leadershipImage and self.leadershipImage.IsShow():
				self.leadershipImage.SetPosition(xPos, yPos)
				xPos += self.IMAGE_STEP
				use2ndLine = True

		if constInfo.UPGRADE_STONE:
			if self.upgradeStoneImage and self.upgradeStoneImage.IsShow():
				self.upgradeStoneImage.SetPosition(xPos, yPos)
				xPos += self.IMAGE_STEP
				use2ndLine = True

		if self.lovePointImage:
			if self.lovePointImage.IsShow():
				self.lovePointImage.SetPosition(xPos, yPos)
				xPos += self.IMAGE_STEP
				use2ndLine = True

		if self.horseImage:
			self.horseImage.SetPosition(xPos, yPos)
			xPos += self.IMAGE_STEP
			use2ndLine = True
			
		for image in self.affectImageDict.values():
			image.SetPosition(xPos, yPos)
			xPos += self.IMAGE_STEP
			use2ndLine = True

		for image in self.itemImageDict.values():
			image.SetPosition(xPos, yPos)
			xPos += self.IMAGE_STEP
			use2ndLine = True

		if use2ndLine:
			yPos += 25

		xPos = 10
		for image in self.affectImageDict2.values():
			image.SetPosition(xPos, yPos)
			xPos += self.IMAGE_STEP

	BONUS_LIST = [

		# CRIT SWORD
		[ 1040, 71044 ],

		# PENE SWORD
		[ 1041, 71045 ],

		# BLUE DEW
		[ 1395, 50825 ],

		# RED DEW
		[ 1340, 50821 ],

		# PINK/ORANGE DEW
		[ 1341, 50822 ],

		# WHITE DEW
		[ 1396, 50826 ],

		# GREEN DEW
		[ 1377, 50824 ],

		# YELLOW DEW
		[ 1317, 50823 ],

		# DRAGON GOD DEFENSE,
		[ 1115, 71030 ],

		# DRAGON GOD LIFE,
		[ 1119, 71027 ],

		# DRAGON GOD ATTACK,
		[ 1093, 71028 ],

		# DRAGON GOD INTELLIGENCE,
		[ 1120, 71029 ],
		
		# BLACK DEW
		[ 1386, 50827 ], 
	]

	STATIC_BONUS = [
		
		# VOTE4BUFF
		[ chr.NEW_AFFECT_VOTE4BUFF, "vote_buff_icon_b" ],

		# PREMIUM
		[ 100000, "premium_icon_b" ],

		# STANDARD EXP BONUS
		[ 500, "70005_b" ],

		# STANDARD DROP BONUS
		[ 501, "70043_b" ],

		# POTION OF WISDOM
		[ 1116, "71153_b" ],

		# POTION OF THIEF
		[ 1117, "27125_b" ],

		# AUTO YANG PICKUP
		[ chr.NEW_AFFECT_AUTOLOOT, "money_b" ],

		# EXORCISM SCROLL
		[ 513, "71001_b" ],

		# CONCENTRATED READING
		[ 512, "71094_b" ],
	]

	def IsBonusInList(self, bonusList, affectType):

		for bonus in bonusList:

			if bonus[ 0 ] == affectType:
				return True

		return False

	def GetBonusImageNumber(self, bonusList, affectType):
		
		for bonus in bonusList:	
			if bonus[ 0 ] == affectType:
				return bonus[ 1 ]

		return -1
			
	def GetImageTypeByTimeLeft(self, timeLeft):

		imageType = "_b"

		# 10 minutes
		if timeLeft <= 600:
			imageType = "_y"

		# 5 minutes
		if timeLeft <= 300:
			imageType = "_r"

		return imageType

	def OnUpdate(self):

		if constInfo.NEW_AFFECT_ICONS:

			for image in self.affectImageDict.values() + self.affectImageDict2.values():
				
				affectType = image.GetAffect()

				isPotion = (affectType == chr.NEW_AFFECT_AUTO_HP_RECOVERY) or (affectType == chr.NEW_AFFECT_AUTO_SP_RECOVERY)

				if isPotion:

					potionType = None
					potionId = 0

					if affectType == chr.NEW_AFFECT_AUTO_HP_RECOVERY:
						potionType = player.AUTO_POTION_TYPE_HP
						potionId = 72726

					else:
						potionType = player.AUTO_POTION_TYPE_SP
						potionId = 72730

					if potionType:
						isActivated, currentAmount, totalAmount, slotIndex = player.GetAutoPotionInfo(potionType)

					amountPercent = 0.0

					try:
						amountPercent = (float(currentAmount) / float(totalAmount)) * 100.0		
					except:
						amountPercent = 100.0

					imageToUse = "%s_b"

					if amountPercent < 50.0:
						imageToUse = "%s_y"

					if amountPercent < 20.0:
						imageToUse = "%s_r"

					if potionId:
						imageToUse = imageToUse % str(potionId)
						imagePath = "d:/ymir work/ui/affects/%s.tga" % str(imageToUse)
						image.ChangeImage(imagePath)
						image.SetScale(0.7, 0.7)

					continue

				# icons that can change
				if self.IsBonusInList(self.BONUS_LIST, affectType):

					timeLeft = image.GetTimeLeftInSeconds()
					imagePath = "d:/ymir work/ui/affects/%s%s.tga"

					imageType = self.GetImageTypeByTimeLeft(timeLeft)
					bonusId = self.GetBonusImageNumber(self.BONUS_LIST, affectType)

					if bonusId != -1:
						bonusId = str(bonusId)
						image.ChangeImage(imagePath % (bonusId, imageType))
						image.SetScale(0.7, 0.7)

				# static icon replace
				if self.IsBonusInList(self.STATIC_BONUS, affectType):

					imagePath = "d:/ymir work/ui/affects/%s.tga"
					bonusId = self.GetBonusImageNumber(self.STATIC_BONUS, affectType)

					if bonusId != -1:
						bonusId = str(bonusId)
						image.ChangeImage(imagePath % bonusId)
						image.SetScale(0.7, 0.7)

		if app.GetTime() - self.lastUpdateTime >= 0.5:
			self.lastUpdateTime = app.GetTime()

			if constInfo.ENABLE_COMPANION_NAME:
				if self.companionImagePet:
					self.companionImagePet.UpdateTime()
				if self.companionImageMount:
					self.companionImageMount.UpdateTime()

			for image in self.affectImageDict.values():
				if image.GetAffect() == chr.NEW_AFFECT_EXP_BONUS_EURO_FREE or\
					image.GetAffect() == chr.NEW_AFFECT_EXP_BONUS_EURO_FREE_UNDER_15:
					image.UpdateDescription2()
				elif image.GetAffect() == chr.NEW_AFFECT_AUTO_HP_RECOVERY or image.GetAffect() == chr.NEW_AFFECT_AUTO_SP_RECOVERY:
					image.UpdateAutoPotionDescription()
				else:
					image.UpdateDescription()

			for image in self.itemImageDict.values():
				image.UpdateDescription()

			for image in self.affectImageDict2.values():
				if image.GetAffect() == chr.NEW_AFFECT_EXP_BONUS_EURO_FREE or\
					image.GetAffect() == chr.NEW_AFFECT_EXP_BONUS_EURO_FREE_UNDER_15:
					image.UpdateDescription2()
				elif image.GetAffect() == chr.NEW_AFFECT_AUTO_HP_RECOVERY or image.GetAffect() == chr.NEW_AFFECT_AUTO_SP_RECOVERY:
					image.UpdateAutoPotionDescription()
				else:
					image.UpdateDescription()

	if constInfo.ENABLE_COMPANION_NAME:
		def SetCompanionNameInfo(self, time1, time2, fakebuff):
			# tchat("SetCompanionNameInfo(%d,%d,%d)" % (time1, time2, fakebuff))
			if time1 == 0:
				self.companionImagePet = None
			else:
				companionImagePet = CompanionImage()
				companionImagePet.SetCompanionInfo(0, time1)
				companionImagePet.Show()
				self.companionImagePet = companionImagePet

			if time2 == 0:
				self.companionImageMount = None
			else:
				companionImageMount = CompanionImage()
				companionImageMount.SetCompanionInfo(1, time2)
				companionImageMount.Show()
				self.companionImageMount = companionImageMount

			if fakebuff > 0:
				companionImageFakebuff = CompanionImage()
				companionImageFakebuff.SetCompanionInfo(2, fakebuff)
				companionImageFakebuff.Show()
				self.companionImageFakebuff = companionImageFakebuff


			self.__ArrangeImageList()

	if constInfo.LEADERSHIP_EXTENSION:
		def SetLeadershipInfo(self, state):
			if state == 0:
				self.leadershipImage = None
			else:
				self.leadershipImage = LeadershipImage()
				self.leadershipImage.SetLeadershipInfo(state)
				self.leadershipImage.Show()

			self.__ArrangeImageList()

	if constInfo.UPGRADE_STONE:
		def SetUpgradeBonus(self, active):
			if not active:
				self.upgradeStoneImage = None
			else:
				self.upgradeStoneImage = UpgradeStoneImage()
				self.upgradeStoneImage.Show()

			self.__ArrangeImageList()
