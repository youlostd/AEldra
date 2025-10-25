import chr
import chrmgr
import skill
import net
import item
import player
import effect
import constInfo
import localeInfo
import emotion

import app

JOB_WARRIOR		= 0
JOB_ASSASSIN	= 1
JOB_SURA		= 2
JOB_SHAMAN		= 3
JOB_WOLFMAN		= 4
JOB_MAX_NUM		= 4

RACE_WARRIOR_M	= 0
RACE_ASSASSIN_W	= 1
RACE_SURA_M		= 2
RACE_SHAMAN_W	= 3
RACE_WARRIOR_W	= 4
RACE_ASSASSIN_M	= 5
RACE_SURA_W		= 6
RACE_SHAMAN_M	= 7
RACE_WOLFMAN_M	= 8

COMBO_TYPE_1 = 0
COMBO_TYPE_2 = 1
COMBO_TYPE_3 = 2

COMBO_INDEX_1 = 0
COMBO_INDEX_2 = 1
COMBO_INDEX_3 = 2
COMBO_INDEX_4 = 3
COMBO_INDEX_5 = 4
COMBO_INDEX_6 = 5

HORSE_SKILL_WILDATTACK = chr.MOTION_SKILL+121
HORSE_SKILL_CHARGE = chr.MOTION_SKILL+122
HORSE_SKILL_SPLASH = chr.MOTION_SKILL+123

GUILD_SKILL_DRAGONBLOOD = chr.MOTION_SKILL+101
GUILD_SKILL_DRAGONBLESS = chr.MOTION_SKILL+102
GUILD_SKILL_BLESSARMOR = chr.MOTION_SKILL+103
GUILD_SKILL_SPPEDUP = chr.MOTION_SKILL+104
GUILD_SKILL_DRAGONWRATH = chr.MOTION_SKILL+105
GUILD_SKILL_MAGICUP = chr.MOTION_SKILL+106

NEW_678TH_SKILL_ENABLE = True

BUFFI_SKILLS = (94, 96)

SKILL_INDEX_DICT = {
	JOB_WARRIOR : { 
		1 : (1, 2, 3, 4, 5, 6, 0, 0, 137, 0, 138, 0, 139, 0,), 
		2 : (16, 17, 18, 19, 20, 21, 0, 0, 137, 0, 138, 0, 139, 0,), 
		"SUPPORT" : (122, 121, 129, 163, 164, 0, 0, 0, 0, 0,),
	},
	JOB_ASSASSIN : { 
		1 : (31, 32, 33, 34, 35, 36, 0, 0, 137, 0, 138, 0, 139, 0, 140,), 
		2 : (46, 47, 48, 49, 50, 51, 0, 0, 137, 0, 138, 0, 139, 0, 140,), 
		"SUPPORT" : (122, 121, 129, 163, 164, 0, 0, 0, 0, 0,),
	},
	JOB_SURA : { 
		1 : (61, 62, 63, 64, 65, 66, 0, 0, 137, 0, 138, 0, 139, 0,),
		2 : (76, 77, 78, 79, 80, 81, 0, 0, 137, 0, 138, 0, 139, 0,),
		"SUPPORT" : (122, 121, 129, 163, 164, 0, 0, 0, 0, 0,),
	},
	JOB_SHAMAN : { 
		1 : (91, 92, 93, 94, 95, 96, 0, 0, 137, 0, 138, 0, 139, 0,),
		2 : (106, 107, 108, 109, 110, 111, 0, 0, 137, 0, 138, 0, 139, 0,),
		"SUPPORT" : (122, 121, 129, 163, 164, 0, 0, 0, 0, 0,),
	},
	# JOB_WOLFMAN : {
		# 1 : (170, 171, 172, 173, 174, 175, 0, 0, 137, 0, 138, 0, 139, 0,),
		# 2 : (170, 171, 172, 173, 174, 175, 0, 0, 137, 0, 138, 0, 139, 0,),
		# "SUPPORT" : (122, 123, 121, 124, 125, 129, 0, 0, 130, 0,),
	# },
}

if constInfo.NEW_SUPPORT_SKILL:
	SKILL_INDEX_DICT = {
		JOB_WARRIOR : { 
			1 : [(1, 2, 3, 4, 5, 6, 0, 0, 137, 0, 138, 0, 139, 0,), 174], 
			2 : [(16, 17, 18, 19, 20, 21, 0, 0, 137, 0, 138, 0, 139, 0,), 178], 
			"SUPPORT" : (122, 121, 129, 163, 164, 165, 0, 0, 0, 0,),
		},
		JOB_ASSASSIN : { 
			1 : [(31, 32, 33, 34, 35, 36, 0, 0, 137, 0, 138, 0, 139, 0, 140,), 175], 
			2 : [(46, 47, 48, 49, 50, 51, 0, 0, 137, 0, 138, 0, 139, 0, 140,), 179],
			"SUPPORT" : (122, 121, 129, 163, 164, 165, 0, 0, 0, 0,),
		},
		JOB_SURA : { 
			1 : [(61, 62, 63, 64, 65, 66, 0, 0, 137, 0, 138, 0, 139, 0,), 176],
			2 : [(76, 77, 78, 79, 80, 81, 0, 0, 137, 0, 138, 0, 139, 0,), 180],
			"SUPPORT" : (122, 121, 129, 163, 164, 165, 0, 0, 0, 0,),
		},
		JOB_SHAMAN : { 
			1 : [(91, 92, 93, 94, 95, 96, 0, 0, 137, 0, 138, 0, 139, 0,), 177],
			2 : [(106, 107, 108, 109, 110, 111, 0, 0, 137, 0, 138, 0, 139, 0,), 181],
			"SUPPORT" : (122, 121, 129, 163, 164, 165, 0, 0, 0, 0,),
		},
		# JOB_WOLFMAN : {
			# 1 : (170, 171, 172, 173, 174, 175, 0, 0, 137, 0, 138, 0, 139, 0,),
			# 2 : (170, 171, 172, 173, 174, 175, 0, 0, 137, 0, 138, 0, 139, 0,),
			# "SUPPORT" : (122, 123, 121, 124, 125, 129, 0, 0, 130, 0,),
		# },
	}

if __SERVER__ == 2:
	SKILL_INDEX_DICT = {
		JOB_WARRIOR : { 
			1 : [(1, 2, 3, 4, 5, 6, 0, 0, 137, 0, 138, 0, 139, 0,), 174], 
			2 : [(16, 17, 18, 19, 20, 21, 0, 0, 137, 0, 138, 0, 139, 0,), 178], 
			"SUPPORT" : (122, 121, 129, 0, 0, 0, 0, 0, 0, 0,),
		},
		JOB_ASSASSIN : { 
			1 : [(31, 32, 33, 34, 35, 36, 0, 0, 137, 0, 138, 0, 139, 0, 140,), 175], 
			2 : [(46, 47, 48, 49, 50, 51, 0, 0, 137, 0, 138, 0, 139, 0, 140,), 179],
			"SUPPORT" : (122, 121, 129, 0, 0, 0, 0, 0, 0, 0,),
		},
		JOB_SURA : { 
			1 : [(61, 62, 63, 64, 65, 66, 0, 0, 137, 0, 138, 0, 139, 0,), 176],
			2 : [(76, 77, 78, 79, 80, 81, 0, 0, 137, 0, 138, 0, 139, 0,), 180],
			"SUPPORT" : (122, 121, 129, 0, 0, 0, 0, 0, 0, 0,),
		},
		JOB_SHAMAN : { 
			1 : [(91, 92, 93, 94, 95, 96, 0, 0, 137, 0, 138, 0, 139, 0,), 177],
			2 : [(106, 107, 108, 109, 110, 111, 0, 0, 137, 0, 138, 0, 139, 0,), 181],
			"SUPPORT" : (122, 121, 129, 0, 0, 0, 0, 0, 0, 0,),
		},
		# JOB_WOLFMAN : {
			# 1 : (170, 171, 172, 173, 174, 175, 0, 0, 137, 0, 138, 0, 139, 0,),
			# 2 : (170, 171, 172, 173, 174, 175, 0, 0, 137, 0, 138, 0, 139, 0,),
			# "SUPPORT" : (122, 123, 121, 124, 125, 129, 0, 0, 130, 0,),
		# },
	}

PASSIVE_GUILD_SKILL_INDEX_LIST = ( 151, )
ACTIVE_GUILD_SKILL_INDEX_LIST = ( 152, 153, 154, 155, 156, 157, )

WARD_SKILL_LIST = [166,167,168,169,170,171,172,173]

def RegisterSkill(race, group, empire=0):

	job = chr.RaceToJob(race)

	## Character Skill
	if SKILL_INDEX_DICT.has_key(job):

		if SKILL_INDEX_DICT[job].has_key(group):
		
			activeSkillList = SKILL_INDEX_DICT[job][group][0]
			player.SetSkill(58, SKILL_INDEX_DICT[job][group][1])
			for i in xrange(len(activeSkillList)):
				skillIndex = activeSkillList[i]
				
				## 7번 8번 스킬은 여기서 설정하면 안됨
				if i != 6 and i != 7:
					if NEW_678TH_SKILL_ENABLE or i != 5 or not (job in (JOB_WARRIOR, JOB_ASSASSIN)):
						player.SetSkill(i+1, skillIndex)

		supportSkillList = SKILL_INDEX_DICT[job]["SUPPORT"]

		for i in xrange(len(supportSkillList)):
			player.SetSkill(i+100+1, supportSkillList[i])

	## Language Skill
#	if 0 != empire:
#		languageSkillList = []
#		for i in xrange(3):
#			if (i+1) != empire:
#				languageSkillList.append(player.SKILL_INDEX_LANGUAGE1+i)
#		for i in xrange(len(languageSkillList)):
#			player.SetSkill(107+i, languageSkillList[i])

	for i in xrange(len(BUFFI_SKILLS)):
		if player.GetSkillSlotIndex(BUFFI_SKILLS[i]) == -1:
			player.SetSkill(140+i, BUFFI_SKILLS[i])

	if __SERVER__ == 2:
		player.SetSkill(107, player.SKILL_INDEX_RIDING) # riding skill
	else:
		player.SetSkill(150, player.SKILL_INDEX_RIDING) # riding skill

	## Guild Skill
	for i in xrange(len(PASSIVE_GUILD_SKILL_INDEX_LIST)):
		player.SetSkill(200+i, PASSIVE_GUILD_SKILL_INDEX_LIST[i])

	for i in xrange(len(ACTIVE_GUILD_SKILL_INDEX_LIST)):
		player.SetSkill(210+i, ACTIVE_GUILD_SKILL_INDEX_LIST[i])

	for i in xrange(len(WARD_SKILL_LIST)):
		player.SetSkill(50 + i, WARD_SKILL_LIST[i])

def RegisterSkillAt(race, group, pos, num):
	job = chr.RaceToJob(race)
	tmp = list(SKILL_INDEX_DICT[job][group])
	tmp[pos] = num
	SKILL_INDEX_DICT[job][group] = tuple(tmp)
	player.SetSkill(pos+1, num)

FACE_IMAGE_DICT = {
	RACE_WARRIOR_M	: "d:/ymir work/ui/game/windows/face_warrior.sub",
	RACE_ASSASSIN_W	: "d:/ymir work/ui/game/windows/face_assassin.sub",
	RACE_SURA_M	: "d:/ymir work/ui/game/windows/face_sura.sub",
	RACE_SHAMAN_W	: "d:/ymir work/ui/game/windows/face_shaman.sub",
	# RACE_WOLFMAN_M	: "d:/ymir work/ui/game/windows/face_wolfman.sub",
}

isInitData=0

def SetGeneralMotions(mode, folder):
	chrmgr.SetPathName(folder)
	chrmgr.RegisterMotionMode(mode)
	chrmgr.RegisterCacheMotionData(mode,		chr.MOTION_WAIT,				"wait.msa")
	chrmgr.RegisterCacheMotionData(mode,		chr.MOTION_WALK,				"walk.msa")
	chrmgr.RegisterCacheMotionData(mode,		chr.MOTION_RUN,					"run.msa")
	chrmgr.RegisterCacheMotionData(mode,		chr.MOTION_DAMAGE,				"damage.msa", 50)
	chrmgr.RegisterCacheMotionData(mode,		chr.MOTION_DAMAGE,				"damage_1.msa", 50)
	chrmgr.RegisterCacheMotionData(mode,		chr.MOTION_DAMAGE_BACK,			"damage_2.msa", 50)
	chrmgr.RegisterCacheMotionData(mode,		chr.MOTION_DAMAGE_BACK,			"damage_3.msa", 50)
	chrmgr.RegisterCacheMotionData(mode,		chr.MOTION_DAMAGE_FLYING,		"damage_flying.msa")
	chrmgr.RegisterCacheMotionData(mode,		chr.MOTION_STAND_UP,			"falling_stand.msa")
	chrmgr.RegisterCacheMotionData(mode,		chr.MOTION_DAMAGE_FLYING_BACK,	"back_damage_flying.msa")
	chrmgr.RegisterCacheMotionData(mode,		chr.MOTION_STAND_UP_BACK,		"back_falling_stand.msa")
	chrmgr.RegisterCacheMotionData(mode,		chr.MOTION_DEAD,				"dead.msa")
	chrmgr.RegisterCacheMotionData(mode,		chr.MOTION_DIG,					"dig.msa")

def SetIntroMotions(mode, folder):
	chrmgr.SetPathName(folder)
	chrmgr.RegisterMotionMode(mode)
	chrmgr.RegisterCacheMotionData(mode,		chr.MOTION_INTRO_WAIT,			"wait.msa")
	chrmgr.RegisterCacheMotionData(mode,		chr.MOTION_INTRO_SELECTED,		"selected.msa")
	chrmgr.RegisterCacheMotionData(mode,		chr.MOTION_INTRO_NOT_SELECTED,	"not_selected.msa")



def __InitData():
	global isInitData

	if isInitData:
		return			

	isInitData = 1

	chrmgr.SetDustGap(250)
	chrmgr.SetHorseDustGap(500)

	chrmgr.RegisterCacheEffect(chrmgr.EFFECT_DUST, "", "d:/ymir work/effect/etc/dust/dust.mse")
	chrmgr.RegisterCacheEffect(chrmgr.EFFECT_HORSE_DUST, "", "d:/ymir work/effect/etc/dust/running_dust.mse")
	chrmgr.RegisterCacheEffect(chrmgr.EFFECT_HIT, "", "d:/ymir work/effect/hit/blow_1/blow_1_low.mse")
	if (app.COMBAT_ZONE):
		chrmgr.RegisterCacheEffect(chrmgr.EFFECT_COMBAT_ZONE_POTION, "", "d:/ymir work/effect/etc/buff/buff_item12.mse")

	chrmgr.RegisterCacheEffect(chrmgr.EFFECT_HPUP_RED, "", "d:/ymir work/effect/etc/recuperation/drugup_red.mse")
	chrmgr.RegisterCacheEffect(chrmgr.EFFECT_SPUP_BLUE, "", "d:/ymir work/effect/etc/recuperation/drugup_blue.mse")
	chrmgr.RegisterCacheEffect(chrmgr.EFFECT_AUTO_HPUP, "", "d:/ymir work/effect/etc/recuperation/drugup_red.mse")
	chrmgr.RegisterCacheEffect(chrmgr.EFFECT_AUTO_SPUP, "", "d:/ymir work/effect/etc/recuperation/drugup_blue.mse")
	chrmgr.RegisterCacheEffect(chrmgr.EFFECT_SPEEDUP_GREEN, "", "d:/ymir work/effect/etc/recuperation/drugup_green.mse")
	chrmgr.RegisterCacheEffect(chrmgr.EFFECT_DXUP_PURPLE, "", "d:/ymir work/effect/etc/recuperation/drugup_purple.mse")

	chrmgr.RegisterCacheEffect(chrmgr.EFFECT_PENETRATE, "Bip01", "d:/ymir work/effect/hit/gwantong.mse")
	#chrmgr.RegisterCacheEffect(chrmgr.EFFECT_BLOCK, "", "d:/ymir work/effect/etc/")
	#chrmgr.RegisterCacheEffect(chrmgr.EFFECT_DODGE, "", "d:/ymir work/effect/etc/")
	chrmgr.RegisterCacheEffect(chrmgr.EFFECT_FIRECRACKER, "", "d:/ymir work/effect/etc/firecracker/newyear_firecracker.mse")
	chrmgr.RegisterCacheEffect(chrmgr.EFFECT_SPIN_TOP, "", "d:/ymir work/effect/etc/firecracker/paing_i.mse")
	chrmgr.RegisterCacheEffect(chrmgr.EFFECT_SELECT, "", "d:/ymir work/effect/etc/click/click_select.mse", True)
	chrmgr.RegisterCacheEffect(chrmgr.EFFECT_TARGET, "", "d:/ymir work/effect/etc/click/click_glow_select.mse", True)
	chrmgr.RegisterCacheEffect(chrmgr.EFFECT_STUN, "Bip01 Head", "d:/ymir work/effect/etc/stun/stun.mse", True)
	chrmgr.RegisterCacheEffect(chrmgr.EFFECT_CRITICAL, "Bip01 R Hand", "d:/ymir work/effect/hit/critical.mse")
	player.RegisterCacheEffect(player.EFFECT_PICK, "d:/ymir work/effect/etc/click/click.mse")
	
	
	chrmgr.RegisterCacheEffect(chrmgr.EFFECT_DAMAGE_TARGET, "", "d:/ymir work/effect/affect/damagevalue/target.mse", True)
	chrmgr.RegisterCacheEffect(chrmgr.EFFECT_DAMAGE_NOT_TARGET, "", "d:/ymir work/effect/affect/damagevalue/nontarget.mse", True)
	chrmgr.RegisterCacheEffect(chrmgr.EFFECT_DAMAGE_SELFDAMAGE, "", "d:/ymir work/effect/affect/damagevalue/damage.mse", True)
	chrmgr.RegisterCacheEffect(chrmgr.EFFECT_DAMAGE_SELFDAMAGE2, "", "d:/ymir work/effect/affect/damagevalue/damage_1.mse", True)
	chrmgr.RegisterCacheEffect(chrmgr.EFFECT_DAMAGE_POISON, "", "d:/ymir work/effect/affect/damagevalue/poison.mse", True)
	chrmgr.RegisterCacheEffect(chrmgr.EFFECT_DAMAGE_MISS, "", "d:/ymir work/effect/affect/damagevalue/miss.mse", True)
	chrmgr.RegisterCacheEffect(chrmgr.EFFECT_DAMAGE_TARGETMISS, "", "d:/ymir work/effect/affect/damagevalue/target_miss.mse", True)
	#chrmgr.RegisterCacheEffect(chrmgr.EFFECT_DAMAGE_CRITICAL, "", "d:/ymir work/effect/affect/damagevalue/critical.mse")

	#chrmgr.RegisterCacheEffect(chrmgr.EFFECT_SUCCESS, "",			"d:/ymir work/effect/success.mse")
	#chrmgr.RegisterCacheEffect(chrmgr.EFFECT_FAIL, "",	"d:/ymir work/effect/fail.mse")
	
	# chrmgr.RegisterCacheEffect(chrmgr.EFFECT_LEVELUP_ON_14_FOR_GERMANY, "","d:/ymir work/effect/paymessage_warning.mse")	#레벨업 14일때 ( 독일전용 )
	# chrmgr.RegisterCacheEffect(chrmgr.EFFECT_LEVELUP_UNDER_15_FOR_GERMANY, "", "d:/ymir work/effect/paymessage_decide.mse" )#레벨업 15일때 ( 독일전용 )

	chrmgr.RegisterCacheEffect(chrmgr.EFFECT_PERCENT_DAMAGE1, "", "d:/ymir work/effect/hit/percent_damage1.mse", True)
	chrmgr.RegisterCacheEffect(chrmgr.EFFECT_PERCENT_DAMAGE2, "", "d:/ymir work/effect/hit/percent_damage2.mse", True)
	chrmgr.RegisterCacheEffect(chrmgr.EFFECT_PERCENT_DAMAGE3, "", "d:/ymir work/effect/hit/percent_damage3.mse", True)

	# Not found resources anywhere
	# chrmgr.RegisterCacheEffect(chrmgr.EFFECT_ACCE_SUCESS_ABSORB, "", "d:/ymir work/effect/etc/buff/buff_acce.mse")
	# chrmgr.RegisterCacheEffect(chrmgr.EFFECT_ACCE_EQUIP, "", "d:/ymir work/effect/etc/buff/buff_acce2.mse")
	chrmgr.RegisterCacheEffect(chrmgr.EFFECT_ACCE_BACK, "Bip01", "D:/ymir work/pc/common/effect/armor/acc_01.mse")
	chrmgr.RegisterCacheEffect(chrmgr.EFFECT_ACCE_BACK_WING1, "Bip01 Neck", "D:/ymir work/pc/common/effect/wing/fire_wing_v2.mse")
	chrmgr.RegisterCacheEffect(chrmgr.EFFECT_ACCE_BACK_WING2, "Bip01 Neck", "D:/ymir work/pc/common/effect/wing/wing_2_drshop.mse")
	chrmgr.RegisterCacheEffect(chrmgr.EFFECT_ACCE_BACK_WING3, "Bip01", "D:/ymir work/pc/common/effect/ridack_wing3.mse")
	chrmgr.RegisterCacheEffect(chrmgr.EFFECT_ACCE_BACK_WING4, "Bip01", "D:/ymir work/pc/common/effect/ridack_wing4.mse")
	chrmgr.RegisterCacheEffect(chrmgr.EFFECT_ACCE_BACK_WING5, "Bip01", "D:/ymir work/effect/wings/4.mse")
	chrmgr.RegisterCacheEffect(chrmgr.EFFECT_ACCE_BACK_WING6, "Bip01", "D:/ymir work/effect/wings/5.mse")
	chrmgr.RegisterCacheEffect(chrmgr.EFFECT_ACCE_BACK_WING7, "Bip01", "D:/ymir work/item/wing/ridack2_wing3.mse")

	# Tapferkeitsumhang effekt
	chrmgr.RegisterCacheEffect(chrmgr.EFFECT_AGGREGATE_MONSTER, "", "d:/ymir work/effect/etc/buff/buff_item9.mse")
	chrmgr.RegisterCacheEffect(chrmgr.EFFECT_HEALER, "", "d:/ymir work/effect/monster2/healer/healer_effect.mse")


	##############
	# WARRIOR
	##############
	chrmgr.CreateRace(RACE_WARRIOR_M)
	chrmgr.SelectRace(RACE_WARRIOR_M)	
	chrmgr.LoadLocalRaceData("warrior_m.msm")
	SetIntroMotions(chr.MOTION_MODE_GENERAL, "d:/ymir work/pc/warrior/intro/")

	chrmgr.CreateRace(RACE_WARRIOR_W)
	chrmgr.SelectRace(RACE_WARRIOR_W)	
	chrmgr.LoadLocalRaceData("warrior_w.msm")
	SetIntroMotions(chr.MOTION_MODE_GENERAL, "d:/ymir work/pc2/warrior/intro/")


	##############
	# ASSASSIN
	##############
	chrmgr.CreateRace(RACE_ASSASSIN_W)
	chrmgr.SelectRace(RACE_ASSASSIN_W)
	chrmgr.LoadLocalRaceData("assassin_w.msm")
	SetIntroMotions(chr.MOTION_MODE_GENERAL, "d:/ymir work/pc/assassin/intro/")

	chrmgr.CreateRace(RACE_ASSASSIN_M)
	chrmgr.SelectRace(RACE_ASSASSIN_M)
	chrmgr.LoadLocalRaceData("assassin_m.msm")
	SetIntroMotions(chr.MOTION_MODE_GENERAL, "d:/ymir work/pc2/assassin/intro/")


	##############
	# SURA
	##############
	chrmgr.CreateRace(RACE_SURA_M)
	chrmgr.SelectRace(RACE_SURA_M)	
	chrmgr.LoadLocalRaceData("sura_m.msm")
	SetIntroMotions(chr.MOTION_MODE_GENERAL, "d:/ymir work/pc/sura/intro/")

	chrmgr.CreateRace(RACE_SURA_W)
	chrmgr.SelectRace(RACE_SURA_W)	
	chrmgr.LoadLocalRaceData("sura_w.msm")
	SetIntroMotions(chr.MOTION_MODE_GENERAL, "d:/ymir work/pc2/sura/intro/")


	##############
	# SHAMAN
	##############
	chrmgr.CreateRace(RACE_SHAMAN_W)
	chrmgr.SelectRace(RACE_SHAMAN_W)
	chrmgr.LoadLocalRaceData("shaman_w.msm")
	SetIntroMotions(chr.MOTION_MODE_GENERAL, "d:/ymir work/pc/shaman/intro/")

	chrmgr.CreateRace(RACE_SHAMAN_M)
	chrmgr.SelectRace(RACE_SHAMAN_M)
	chrmgr.LoadLocalRaceData("shaman_m.msm")
	SetIntroMotions(chr.MOTION_MODE_GENERAL, "d:/ymir work/pc2/shaman/intro/")
	
	##############
	# WOLFMAN
	##############
	# chrmgr.CreateRace(RACE_WOLFMAN_M)
	# chrmgr.SelectRace(RACE_WOLFMAN_M)
	# chrmgr.LoadLocalRaceData("wolfman_m.msm")
	# SetIntroMotions(chr.MOTION_MODE_GENERAL, "d:/ymir work/pc3/wolfman/intro/")

def __LoadGameSound():
	item.SetUseSoundFileName(item.USESOUND_DEFAULT, "sound/ui/drop.wav")
	item.SetUseSoundFileName(item.USESOUND_ACCESSORY, "sound/ui/equip_ring_amulet.wav")
	item.SetUseSoundFileName(item.USESOUND_ARMOR, "sound/ui/equip_metal_armor.wav")
	item.SetUseSoundFileName(item.USESOUND_BOW, "sound/ui/equip_bow.wav")
	item.SetUseSoundFileName(item.USESOUND_WEAPON, "sound/ui/equip_metal_weapon.wav")
	item.SetUseSoundFileName(item.USESOUND_POTION, "sound/ui/eat_potion.wav")
	item.SetUseSoundFileName(item.USESOUND_PORTAL, "sound/ui/potal_scroll.wav")

	item.SetDropSoundFileName(item.DROPSOUND_DEFAULT, "sound/ui/drop.wav")
	item.SetDropSoundFileName(item.DROPSOUND_ACCESSORY, "sound/ui/equip_ring_amulet.wav")
	item.SetDropSoundFileName(item.DROPSOUND_ARMOR, "sound/ui/equip_metal_armor.wav")
	item.SetDropSoundFileName(item.DROPSOUND_BOW, "sound/ui/equip_bow.wav")
	item.SetDropSoundFileName(item.DROPSOUND_WEAPON, "sound/ui/equip_metal_weapon.wav")

def __LoadGameEffect():
	chrmgr.RegisterEffect(chrmgr.EFFECT_SPAWN_APPEAR, "Bip01", "d:/ymir work/effect/etc/appear_die/monster_appear.mse")
	chrmgr.RegisterEffect(chrmgr.EFFECT_SPAWN_DISAPPEAR, "Bip01", "d:/ymir work/effect/etc/appear_die/monster_die.mse")		
	chrmgr.RegisterEffect(chrmgr.EFFECT_FLAME_ATTACK, "equip_right_hand", "d:/ymir work/effect/hit/blow_flame/flame_3_weapon.mse")
	chrmgr.RegisterEffect(chrmgr.EFFECT_FLAME_HIT, "", "d:/ymir work/effect/hit/blow_flame/flame_3_blow.mse")
	chrmgr.RegisterEffect(chrmgr.EFFECT_FLAME_ATTACH, "", "d:/ymir work/effect/hit/blow_flame/flame_3_body.mse")
	chrmgr.RegisterEffect(chrmgr.EFFECT_ELECTRIC_ATTACK, "equip_right", "d:/ymir work/effect/hit/blow_electric/light_1_weapon.mse")
	chrmgr.RegisterEffect(chrmgr.EFFECT_ELECTRIC_HIT, "", "d:/ymir work/effect/hit/blow_electric/light_1_blow.mse")
	chrmgr.RegisterEffect(chrmgr.EFFECT_ELECTRIC_ATTACH, "", "d:/ymir work/effect/hit/blow_electric/light_1_body.mse")
	
	chrmgr.RegisterEffect(chrmgr.EFFECT_LEVELUP, "", "d:/ymir work/effect/etc/levelup_1/level_up.mse")
	chrmgr.RegisterEffect(chrmgr.EFFECT_SKILLUP, "", "d:/ymir work/effect/etc/skillup/skillup_1.mse")
	
	if __SERVER__ == 2:	
		chrmgr.RegisterEffect(chrmgr.EFFECT_EMPIRE+1, "Bip01", "d:/ymir work/effect/etc/empire_original/empire_A.mse", True)
		chrmgr.RegisterEffect(chrmgr.EFFECT_EMPIRE+2, "Bip01", "d:/ymir work/effect/etc/empire_original/empire_B.mse", True)
		chrmgr.RegisterEffect(chrmgr.EFFECT_EMPIRE+3, "Bip01", "d:/ymir work/effect/etc/empire_original/empire_C.mse", True)
	else:
		chrmgr.RegisterEffect(chrmgr.EFFECT_EMPIRE+1, "Bip01", "d:/ymir work/effect/etc/empire/empire_A.mse", True)
		chrmgr.RegisterEffect(chrmgr.EFFECT_EMPIRE+2, "Bip01", "d:/ymir work/effect/etc/empire/empire_B.mse", True)
		chrmgr.RegisterEffect(chrmgr.EFFECT_EMPIRE+3, "Bip01", "d:/ymir work/effect/etc/empire/empire_C.mse", True)

	chrmgr.RegisterEffect(chrmgr.EFFECT_WEAPON+1, "equip_right_hand", "d:/ymir work/pc/warrior/effect/geom_sword_loop.mse")
	chrmgr.RegisterEffect(chrmgr.EFFECT_WEAPON+2, "equip_right_hand", "d:/ymir work/pc/warrior/effect/geom_spear_loop.mse")
	chrmgr.RegisterEffect(chrmgr.EFFECT_WEAPON_LEGENDARY+1, "equip_right_hand", "d:/ymir work/pc/warrior/effect/geom_5_sword_loop.mse")
	chrmgr.RegisterEffect(chrmgr.EFFECT_WEAPON_LEGENDARY+2, "equip_right_hand", "d:/ymir work/pc/warrior/effect/geom_5_spear_loop.mse")

	# LOCALE
	chrmgr.RegisterEffect(chrmgr.EFFECT_AFFECT+0, "Bip01", localeInfo.FN_GM_MARK)
	chrmgr.RegisterEffect(chrmgr.EFEKT_BOSSA, "", "d:/ymir work/effect/boss.mse")
	# END_OF_LOCALE
	
	chrmgr.RegisterEffect(chrmgr.EFFECT_AFFECT+chr.AFFECT_POISON, "Bip01", "d:/ymir work/effect/hit/blow_poison/poison_loop.mse", True) ## 중독
	chrmgr.RegisterEffect(chrmgr.EFFECT_AFFECT+chr.AFFECT_SLOW, "", "d:/ymir work/effect/affect/slow.mse", True)
	chrmgr.RegisterEffect(chrmgr.EFFECT_AFFECT+chr.AFFECT_STUN, "Bip01 Head", "d:/ymir work/effect/etc/stun/stun_loop.mse", True)
	#chrmgr.RegisterEffect(chrmgr.EFFECT_AFFECT+8, "", "d:/ymir work/guild/effect/10_construction.mse")
	#chrmgr.RegisterEffect(chrmgr.EFFECT_AFFECT+9, "", "d:/ymir work/guild/effect/20_construction.mse")
	#chrmgr.RegisterEffect(chrmgr.EFFECT_AFFECT+10, "", "d:/ymir work/guild/effect/20_upgrade.mse")
	chrmgr.RegisterEffect(chrmgr.EFFECT_AFFECT+chr.AFFECT_CHEONGEUN, "", "d:/ymir work/pc/warrior/effect/gyeokgongjang_loop.mse", True) ## 천근추 (밑에도 있따-_-)
	chrmgr.RegisterEffect(chrmgr.EFFECT_AFFECT+chr.AFFECT_CHEONGEUN_PERFECT, "", "d:/ymir work/pc/warrior/effect/gyeokgongjang_loop_5.mse", True)
	chrmgr.RegisterEffect(chrmgr.EFFECT_AFFECT+chr.AFFECT_GYEONGGONG, "", "d:/ymir work/pc/assassin/effect/gyeonggong_loop.mse", True) ## 자객 - 경공
	chrmgr.RegisterEffect(chrmgr.EFFECT_AFFECT+chr.AFFECT_GWIGEOM, "Bip01 R Finger2", "d:/ymir work/pc/sura/effect/gwigeom_loop.mse", True)
	chrmgr.RegisterEffect(chrmgr.EFFECT_AFFECT+chr.AFFECT_GWIGEOM_PERFECT, "Bip01 R Finger2", "d:/ymir work/pc/sura/effect/gwigeom_5_loop.mse", True)
	chrmgr.RegisterEffect(chrmgr.EFFECT_AFFECT+chr.AFFECT_GONGPO, "", "d:/ymir work/pc/sura/effect/fear_loop.mse", True) ## 수라 - 공포
	chrmgr.RegisterEffect(chrmgr.EFFECT_AFFECT+chr.AFFECT_GONGPO_PERFECT, "", "d:/ymir work/pc/sura/effect/fear_5_loop.mse", True)
	chrmgr.RegisterEffect(chrmgr.EFFECT_AFFECT+chr.AFFECT_JUMAGAP, "", "d:/ymir work/pc/sura/effect/jumagap_loop.mse", True) ## 수라 - 주마갑
	chrmgr.RegisterEffect(chrmgr.EFFECT_AFFECT+chr.AFFECT_HOSIN, "", "d:/ymir work/pc/shaman/effect/3hosin_loop.mse", True) ## 무당 - 호신
	chrmgr.RegisterEffect(chrmgr.EFFECT_AFFECT+chr.AFFECT_HOSIN_PERFECT, "", "d:/ymir work/pc/shaman/effect/hosin_loop_5.mse", True)
	chrmgr.RegisterEffect(chrmgr.EFFECT_AFFECT+chr.AFFECT_BOHO, "", "d:/ymir work/pc/shaman/effect/boho_loop.mse", True) ## 무당 - 보호
	chrmgr.RegisterEffect(chrmgr.EFFECT_AFFECT+chr.AFFECT_KWAESOK, "", "d:/ymir work/pc/shaman/effect/10kwaesok_loop.mse", True) ## 무당 - 쾌속
	chrmgr.RegisterEffect(chrmgr.EFFECT_AFFECT+chr.AFFECT_JEUNGRYEOK, "Bip01 L Hand", "d:/ymir work/pc/shaman/effect/jeungryeok_hand.mse", True)
#	chrmgr.RegisterEffect(chrmgr.EFFECT_AFFECT+chr.AFFECT_JEUNGRYEOK_MASTER, "Bip01 L Hand", "d:/ymir work/pc/shaman/effect/jeungryeok_hand_2.mse")
#	chrmgr.RegisterEffect(chrmgr.EFFECT_AFFECT+chr.AFFECT_JEUNGRYEOK_GRANDMASTER, "Bip01 L Hand", "d:/ymir work/pc/shaman/effect/jeungryeok_hand_3.mse")
#	chrmgr.RegisterEffect(chrmgr.EFFECT_AFFECT+chr.AFFECT_JEUNGRYEOK_PERFECT, "Bip01 L Hand", "d:/ymir work/pc/shaman/effect/jeungryeok_hand_4.mse")
	chrmgr.RegisterEffect(chrmgr.EFFECT_AFFECT+chr.AFFECT_HEUKSIN, "", "d:/ymir work/pc/sura/effect/heuksin_loop.mse", True)
	chrmgr.RegisterEffect(chrmgr.EFFECT_AFFECT+chr.AFFECT_HEUKSIN_PERFECT, "", "d:/ymir work/pc/sura/effect/heuksin_5_loop.mse", True)
	chrmgr.RegisterEffect(chrmgr.EFFECT_AFFECT+chr.AFFECT_MUYEONG, "", "d:/ymir work/pc/sura/effect/muyeong_loop.mse", True)
	chrmgr.RegisterEffect(chrmgr.EFFECT_AFFECT+chr.AFFECT_FIRE, "Bip01", "d:/ymir work/effect/hit/blow_flame/flame_loop.mse", True)
	chrmgr.RegisterEffect(chrmgr.EFFECT_AFFECT+chr.AFFECT_GICHEON, "Bip01 R Hand", "d:/ymir work/pc/shaman/effect/6gicheon_hand.mse", True)
	chrmgr.RegisterEffect(chrmgr.EFFECT_AFFECT+chr.AFFECT_GICHEON_PERFECT, "Bip01 R Hand", "d:/ymir work/pc/shaman/effect/6gicheon_hand_5.mse", True)
	chrmgr.RegisterEffect(chrmgr.EFFECT_AFFECT+chr.AFFECT_PABEOP, "Bip01 Head", "d:/ymir work/pc/sura/effect/pabeop_loop.mse", True)
	chrmgr.RegisterEffect(chrmgr.EFFECT_AFFECT+chr.AFFECT_FALLEN_CHEONGEUN, "", "d:/ymir work/pc/warrior/effect/gyeokgongjang_loop.mse", True) ## 천근추 (Fallen)
	# chrmgr.RegisterEffect(chrmgr.EFFECT_AFFECT+chr.AFFECT_RED_POSSESSION, "Bip01", "d:/ymir work/effect/hit/blow_flame/flame_loop_w.mse")
	# chrmgr.RegisterEffect(chrmgr.EFFECT_AFFECT+chr.AFFECT_BLUE_POSSESSION, "", "d:/ymir work/pc3/common/effect/buff/blue_possession.mse")
	## 34 Polymoph
	chrmgr.RegisterEffect(chrmgr.EFFECT_AFFECT+chr.AFFECT_WAR_FLAG1, "", "d:/ymir work/effect/etc/guild_war_flag/flag_red.mse")
	chrmgr.RegisterEffect(chrmgr.EFFECT_AFFECT+chr.AFFECT_WAR_FLAG2, "", "d:/ymir work/effect/etc/guild_war_flag/flag_blue.mse")
	chrmgr.RegisterEffect(chrmgr.EFFECT_AFFECT+chr.AFFECT_WAR_FLAG3, "", "d:/ymir work/effect/etc/guild_war_flag/flag_yellow.mse")
	# OFFLINE SHOP
	chrmgr.RegisterEffect(chrmgr.EFFECT_AFFECT+chr.AFFECT_AUCTION_SHOP_OWNER, "", "d:/ymir work/effect/etc/levelup_2/3.mse")

	chrmgr.RegisterEffect(chrmgr.EFFECT_REFINED+chrmgr.EFFECT_SWORD_REFINED7+0, "PART_WEAPON", "D:/ymir work/pc/common/effect/sword/sword_7.mse")
	chrmgr.RegisterEffect(chrmgr.EFFECT_REFINED+chrmgr.EFFECT_SWORD_REFINED7+1, "PART_WEAPON", "D:/ymir work/pc/common/effect/sword/sword_8.mse")
	chrmgr.RegisterEffect(chrmgr.EFFECT_REFINED+chrmgr.EFFECT_SWORD_REFINED7+2, "PART_WEAPON", "D:/ymir work/pc/common/effect/sword/sword_9.mse")

	chrmgr.RegisterEffect(chrmgr.EFFECT_REFINED+chrmgr.EFFECT_BOW_REFINED7+0, "PART_WEAPON_LEFT", "D:/ymir work/pc/common/effect/sword/sword_7_b.mse")
	chrmgr.RegisterEffect(chrmgr.EFFECT_REFINED+chrmgr.EFFECT_BOW_REFINED7+1, "PART_WEAPON_LEFT", "D:/ymir work/pc/common/effect/sword/sword_8_b.mse")
	chrmgr.RegisterEffect(chrmgr.EFFECT_REFINED+chrmgr.EFFECT_BOW_REFINED7+2, "PART_WEAPON_LEFT", "D:/ymir work/pc/common/effect/sword/sword_9_b.mse")

	chrmgr.RegisterEffect(chrmgr.EFFECT_REFINED+chrmgr.EFFECT_FANBELL_REFINED7+0, "PART_WEAPON", "D:/ymir work/pc/common/effect/sword/sword_7_f.mse")
	chrmgr.RegisterEffect(chrmgr.EFFECT_REFINED+chrmgr.EFFECT_FANBELL_REFINED7+1, "PART_WEAPON", "D:/ymir work/pc/common/effect/sword/sword_8_f.mse")
	chrmgr.RegisterEffect(chrmgr.EFFECT_REFINED+chrmgr.EFFECT_FANBELL_REFINED7+2, "PART_WEAPON", "D:/ymir work/pc/common/effect/sword/sword_9_f.mse")

	chrmgr.RegisterEffect(chrmgr.EFFECT_REFINED+chrmgr.EFFECT_SMALLSWORD_REFINED7+0, "PART_WEAPON", "D:/ymir work/pc/common/effect/sword/sword_7_s.mse")
	chrmgr.RegisterEffect(chrmgr.EFFECT_REFINED+chrmgr.EFFECT_SMALLSWORD_REFINED7+1, "PART_WEAPON", "D:/ymir work/pc/common/effect/sword/sword_8_s.mse")
	chrmgr.RegisterEffect(chrmgr.EFFECT_REFINED+chrmgr.EFFECT_SMALLSWORD_REFINED7+2, "PART_WEAPON", "D:/ymir work/pc/common/effect/sword/sword_9_s.mse")

	chrmgr.RegisterEffect(chrmgr.EFFECT_REFINED+chrmgr.EFFECT_SMALLSWORD_REFINED7_LEFT+0, "PART_WEAPON_LEFT", "D:/ymir work/pc/common/effect/sword/sword_7_s.mse")
	chrmgr.RegisterEffect(chrmgr.EFFECT_REFINED+chrmgr.EFFECT_SMALLSWORD_REFINED7_LEFT+1, "PART_WEAPON_LEFT", "D:/ymir work/pc/common/effect/sword/sword_8_s.mse")
	chrmgr.RegisterEffect(chrmgr.EFFECT_REFINED+chrmgr.EFFECT_SMALLSWORD_REFINED7_LEFT+2, "PART_WEAPON_LEFT", "D:/ymir work/pc/common/effect/sword/sword_9_s.mse")

	chrmgr.RegisterEffect(chrmgr.EFFECT_REFINED+chrmgr.EFFECT_BODYARMOR_REFINED7+0, "Bip01", "D:/ymir work/pc/common/effect/armor/armor_7.mse")
	chrmgr.RegisterEffect(chrmgr.EFFECT_REFINED+chrmgr.EFFECT_BODYARMOR_REFINED7+1, "Bip01", "D:/ymir work/pc/common/effect/armor/armor_8.mse")
	chrmgr.RegisterEffect(chrmgr.EFFECT_REFINED+chrmgr.EFFECT_BODYARMOR_REFINED7+2, "Bip01", "D:/ymir work/pc/common/effect/armor/armor_9.mse")
	chrmgr.RegisterEffect(chrmgr.EFFECT_REFINED+chrmgr.EFFECT_BODYARMOR_SPECIAL3, "Bip01", "D:/ymir work/pc/common/effect/armor/armor_v3_orange.mse")
	
	chrmgr.RegisterEffect(chrmgr.EFFECT_REFINED+chrmgr.EFFECT_BODYARMOR_SPECIAL4, "Bip01", "D:/ymir work/effect/armor_assassin3.mse") #rot
	chrmgr.RegisterEffect(chrmgr.EFFECT_REFINED+chrmgr.EFFECT_BODYARMOR_SPECIAL5, "Bip01", "D:/ymir work/effect/armor_assassin4.mse") #blau
	chrmgr.RegisterEffect(chrmgr.EFFECT_REFINED+chrmgr.EFFECT_BODYARMOR_SPECIAL6, "Bip01", "D:/ymir work/effect/armor_assassin5.mse") #grün
	chrmgr.RegisterEffect(chrmgr.EFFECT_REFINED+chrmgr.EFFECT_BODYARMOR_SPECIAL7, "Bip01", "D:/ymir work/effect/armor_assassin6.mse") #orange
	chrmgr.RegisterEffect(chrmgr.EFFECT_REFINED+chrmgr.EFFECT_BODYARMOR_SPECIAL8, "Bip01", "D:/ymir work/effect/armor_assassin7.mse") #lila

	chrmgr.RegisterEffect(chrmgr.EFFECT_REFINED+chrmgr.EFFECT_BODYARMOR_SPECIAL+0, "Bip01", "D:/ymir work/pc/common/effect/armor/armor-4-2-1.mse")
	chrmgr.RegisterEffect(chrmgr.EFFECT_REFINED+chrmgr.EFFECT_BODYARMOR_SPECIAL+1, "Bip01", "D:/ymir work/pc/common/effect/armor/armor-4-2-2.mse")
	chrmgr.RegisterEffect(chrmgr.EFFECT_REFINED + chrmgr.EFFECT_WEAPON_SPD1, "PART_WEAPON", "D:/ymir work/pc/common/effect/animated_weapons/sword_s_red.mse")
	chrmgr.RegisterEffect(chrmgr.EFFECT_REFINED + chrmgr.EFFECT_WEAPON_SPD, "PART_WEAPON", "D:/ymir work/pc/common/effect/animated_weapons/sword_red.mse")
	chrmgr.RegisterEffect(chrmgr.EFFECT_REFINED + chrmgr.EFFECT_WEAPON_PUGN, "PART_WEAPON", "D:/ymir work/pc/common/effect/animated_weapons/knife_red.mse")
	chrmgr.RegisterEffect(chrmgr.EFFECT_REFINED + chrmgr.EFFECT_WEAPON_PUGN2, "PART_WEAPON_LEFT", "D:/ymir work/pc/common/effect/animated_weapons/knife_red.mse")
	chrmgr.RegisterEffect(chrmgr.EFFECT_REFINED + chrmgr.EFFECT_WEAPON_SPADONE, "PART_WEAPON", "D:/ymir work/pc/common/effect/animated_weapons/2hand_red.mse")
	chrmgr.RegisterEffect(chrmgr.EFFECT_REFINED + chrmgr.EFFECT_WEAPON_ARC, "PART_WEAPON_LEFT", "D:/ymir work/pc/common/effect/animated_weapons/bow_red.mse")
	chrmgr.RegisterEffect(chrmgr.EFFECT_REFINED + chrmgr.EFFECT_WEAPON_CMP, "PART_WEAPON", "D:/ymir work/pc/common/effect/animated_weapons/bell_red.mse")
	chrmgr.RegisterEffect(chrmgr.EFFECT_REFINED + chrmgr.EFFECT_WEAPON_VENT, "PART_WEAPON", "D:/ymir work/pc/common/effect/animated_weapons/fan_red.mse")
	chrmgr.RegisterEffect(chrmgr.EFFECT_REFINED + chrmgr.EFFECT_WEAPON_SPD1_2, "PART_WEAPON", "D:/ymir work/pc/common/effect/animated_weapons_9/sura_sword.mse")
	chrmgr.RegisterEffect(chrmgr.EFFECT_REFINED + chrmgr.EFFECT_WEAPON_SPD_2, "PART_WEAPON", "D:/ymir work/pc/common/effect/animated_weapons_9/sword.mse")
	chrmgr.RegisterEffect(chrmgr.EFFECT_REFINED + chrmgr.EFFECT_WEAPON_PUGN_2, "PART_WEAPON", "D:/ymir work/pc/common/effect/animated_weapons_9/ninja.mse")
	chrmgr.RegisterEffect(chrmgr.EFFECT_REFINED + chrmgr.EFFECT_WEAPON_PUGN2_2, "PART_WEAPON_LEFT", "D:/ymir work/pc/common/effect/animated_weapons_9/ninja.mse")
	chrmgr.RegisterEffect(chrmgr.EFFECT_REFINED + chrmgr.EFFECT_WEAPON_SPADONE_2, "PART_WEAPON", "D:/ymir work/pc/common/effect/animated_weapons_9/2hand.mse")
	chrmgr.RegisterEffect(chrmgr.EFFECT_REFINED + chrmgr.EFFECT_WEAPON_ARC_2, "PART_WEAPON_LEFT", "D:/ymir work/pc/common/effect/animated_weapons_9/bow.mse")
	chrmgr.RegisterEffect(chrmgr.EFFECT_REFINED + chrmgr.EFFECT_WEAPON_CMP_2, "PART_WEAPON", "D:/ymir work/pc/common/effect/animated_weapons_9/bell.mse")
	chrmgr.RegisterEffect(chrmgr.EFFECT_REFINED + chrmgr.EFFECT_WEAPON_VENT_2, "PART_WEAPON", "D:/ymir work/pc/common/effect/animated_weapons_9/fan.mse")
	chrmgr.RegisterEffect(chrmgr.EFFECT_REFINED + chrmgr.EFFECT_WEAPON_FMS, "PART_WEAPON", "D:/ymir work/pc/common/effect/animated_30/fms.mse")
	chrmgr.RegisterEffect(chrmgr.EFFECT_REFINED + chrmgr.EFFECT_WEAPON_KOZIK_2, "PART_WEAPON", "D:/ymir work/pc/common/effect/animated_30/kozik.mse")
	chrmgr.RegisterEffect(chrmgr.EFFECT_REFINED + chrmgr.EFFECT_WEAPON_KOZIK, "PART_WEAPON_LEFT", "D:/ymir work/pc/common/effect/animated_30/kozik.mse")
	chrmgr.RegisterEffect(chrmgr.EFFECT_REFINED + chrmgr.EFFECT_WEAPON_RIB, "PART_WEAPON", "D:/ymir work/pc/common/effect/animated_30/rib.mse")
	chrmgr.RegisterEffect(chrmgr.EFFECT_REFINED + chrmgr.EFFECT_WEAPON_JELONEK, "PART_WEAPON_LEFT", "D:/ymir work/pc/common/effect/animated_30/jelonek.mse")
	chrmgr.RegisterEffect(chrmgr.EFFECT_REFINED + chrmgr.EFFECT_WEAPON_ANTYK, "PART_WEAPON", "D:/ymir work/pc/common/effect/animated_30/antyk.mse")
	chrmgr.RegisterEffect(chrmgr.EFFECT_REFINED + chrmgr.EFFECT_WEAPON_JESION, "PART_WEAPON", "D:/ymir work/pc/common/effect/animated_30/jesion.mse")
	chrmgr.RegisterEffect(chrmgr.EFFECT_REFINED + chrmgr.EFFECT_WEAPON_ZATRUTY2, "PART_WEAPON", "D:/ymir work/pc/common/effect/animated_75/zatruty2.mse")
	chrmgr.RegisterEffect(chrmgr.EFFECT_REFINED + chrmgr.EFFECT_WEAPON_LWI, "PART_WEAPON", "D:/ymir work/pc/common/effect/animated_75/lwi.mse")
	chrmgr.RegisterEffect(chrmgr.EFFECT_REFINED + chrmgr.EFFECT_WEAPON_SKRZYDLA, 	"PART_WEAPON_LEFT", "D:/ymir work/pc/common/effect/animated_75/skrzydla.mse")
	chrmgr.RegisterEffect(chrmgr.EFFECT_REFINED + chrmgr.EFFECT_WEAPON_SKRZYDLA_2, 	"PART_WEAPON", 		"D:/ymir work/pc/common/effect/animated_75/skrzydla.mse")
	chrmgr.RegisterEffect(chrmgr.EFFECT_REFINED + chrmgr.EFFECT_WEAPON_ZAL, "PART_WEAPON", "D:/ymir work/pc/common/effect/animated_75/zal.mse")
	chrmgr.RegisterEffect(chrmgr.EFFECT_REFINED + chrmgr.EFFECT_WEAPON_KRUK, "PART_WEAPON_LEFT", "D:/ymir work/pc/common/effect/animated_75/kruk.mse")
	chrmgr.RegisterEffect(chrmgr.EFFECT_REFINED + chrmgr.EFFECT_WEAPON_BAMBUS, "PART_WEAPON", "D:/ymir work/pc/common/effect/animated_75/bambus.mse")
	chrmgr.RegisterEffect(chrmgr.EFFECT_REFINED + chrmgr.EFFECT_WEAPON_TRYTON, "PART_WEAPON", "D:/ymir work/pc/common/effect/animated_90/tryton.mse")
	chrmgr.RegisterEffect(chrmgr.EFFECT_REFINED + chrmgr.EFFECT_WEAPON_SWIETY, "PART_WEAPON", "D:/ymir work/pc/common/effect/animated_90/swiety.mse")
	chrmgr.RegisterEffect(chrmgr.EFFECT_REFINED + chrmgr.EFFECT_WEAPON_BEZDUSZNE, 	"PART_WEAPON_LEFT", "D:/ymir work/pc/common/effect/animated_90/bezduszne.mse")
	chrmgr.RegisterEffect(chrmgr.EFFECT_REFINED + chrmgr.EFFECT_WEAPON_BEZDUSZNE_2, "PART_WEAPON", 		"D:/ymir work/pc/common/effect/animated_90/bezduszne.mse")
	chrmgr.RegisterEffect(chrmgr.EFFECT_REFINED + chrmgr.EFFECT_WEAPON_PIEKIELNE, "PART_WEAPON", "D:/ymir work/pc/common/effect/animated_90/piekielne.mse")
	chrmgr.RegisterEffect(chrmgr.EFFECT_REFINED + chrmgr.EFFECT_WEAPON_DIABLA_L, "PART_WEAPON_LEFT", "D:/ymir work/pc/common/effect/animated_90/diabla_l.mse")
	chrmgr.RegisterEffect(chrmgr.EFFECT_REFINED + chrmgr.EFFECT_WEAPON_SZCZEKI, "PART_WEAPON", "D:/ymir work/pc/common/effect/animated_90/szczeki.mse")
	chrmgr.RegisterEffect(chrmgr.EFFECT_REFINED + chrmgr.EFFECT_WEAPON_DIABLA_W, "PART_WEAPON", "D:/ymir work/pc/common/effect/animated_90/diabla_w.mse")
	chrmgr.RegisterEffect(chrmgr.EFFECT_REFINED + chrmgr.EFFECT_WEAPON_ANGEL_SW, "PART_WEAPON", "D:/ymir work/pc/common/effect/angel/ridack_sword.mse")
	chrmgr.RegisterEffect(chrmgr.EFFECT_REFINED + chrmgr.EFFECT_WEAPON_ANGEL_TW, "PART_WEAPON", "D:/ymir work/pc/common/effect/angel/ridack_spear.mse")
	chrmgr.RegisterEffect(chrmgr.EFFECT_REFINED + chrmgr.EFFECT_WEAPON_ANGEL_DA, "PART_WEAPON_LEFT", "D:/ymir work/pc/common/effect/angel/ridack_knife.mse")
	chrmgr.RegisterEffect(chrmgr.EFFECT_REFINED + chrmgr.EFFECT_WEAPON_ANGEL_DA2, "PART_WEAPON", "D:/ymir work/pc/common/effect/angel/ridack_knife.mse")
	chrmgr.RegisterEffect(chrmgr.EFFECT_REFINED + chrmgr.EFFECT_WEAPON_ANGEL_BO, "PART_WEAPON_LEFT", "D:/ymir work/pc/common/effect/angel/ridack_bow.mse")
	chrmgr.RegisterEffect(chrmgr.EFFECT_REFINED + chrmgr.EFFECT_WEAPON_ANGEL_BE, "PART_WEAPON", "D:/ymir work/pc/common/effect/angel/ridack_bell.mse")
	chrmgr.RegisterEffect(chrmgr.EFFECT_REFINED + chrmgr.EFFECT_WEAPON_ANGEL_FA, "PART_WEAPON", "D:/ymir work/pc/common/effect/angel/ridack_fan.mse")
	chrmgr.RegisterEffect(chrmgr.EFFECT_REFINED + chrmgr.EFFECT_WEAPON_DEMON_SW, "PART_WEAPON", "D:/ymir work/pc/common/effect/demon/ridack_sword.mse")
	chrmgr.RegisterEffect(chrmgr.EFFECT_REFINED + chrmgr.EFFECT_WEAPON_DEMON_TW, "PART_WEAPON", "D:/ymir work/pc/common/effect/demon/ridack_spear.mse")
	chrmgr.RegisterEffect(chrmgr.EFFECT_REFINED + chrmgr.EFFECT_WEAPON_DEMON_DA, "PART_WEAPON_LEFT", "D:/ymir work/pc/common/effect/demon/ridack_knife.mse")
	chrmgr.RegisterEffect(chrmgr.EFFECT_REFINED + chrmgr.EFFECT_WEAPON_DEMON_DA2, "PART_WEAPON", "D:/ymir work/pc/common/effect/demon/ridack_knife.mse")
	chrmgr.RegisterEffect(chrmgr.EFFECT_REFINED + chrmgr.EFFECT_WEAPON_DEMON_BO, "PART_WEAPON_LEFT", "D:/ymir work/pc/common/effect/demon/ridack_bow.mse")
	chrmgr.RegisterEffect(chrmgr.EFFECT_REFINED + chrmgr.EFFECT_WEAPON_DEMON_BE, "PART_WEAPON", "D:/ymir work/pc/common/effect/demon/ridack_bell.mse")
	chrmgr.RegisterEffect(chrmgr.EFFECT_REFINED + chrmgr.EFFECT_WEAPON_DEMON_FA, "PART_WEAPON", "D:/ymir work/pc/common/effect/demon/ridack_fan.mse")
	
	chrmgr.RegisterEffect(chrmgr.EFFECT_REFINED + chrmgr.EFFECT_JULY_SW, "PART_WEAPON", "D:/ymir work/item/costume/achievement_mec.mse")
	chrmgr.RegisterEffect(chrmgr.EFFECT_REFINED + chrmgr.EFFECT_WEAPON_JULY_TW, "PART_WEAPON", "D:/ymir work/item/costume/achievement_cepel.mse")
	chrmgr.RegisterEffect(chrmgr.EFFECT_REFINED + chrmgr.EFFECT_WEAPON_JULY_DA, "PART_WEAPON_LEFT", "D:/ymir work/item/costume/achievement_dyky.mse")
	chrmgr.RegisterEffect(chrmgr.EFFECT_REFINED + chrmgr.EFFECT_WEAPON_JULY_DA2, "PART_WEAPON", "D:/ymir work/item/costume/achievement_dyky.mse")
	chrmgr.RegisterEffect(chrmgr.EFFECT_REFINED + chrmgr.EFFECT_WEAPON_JULY_BO, "PART_WEAPON_LEFT", "D:/ymir work/item/costume/achievement_luk.mse")
	chrmgr.RegisterEffect(chrmgr.EFFECT_REFINED + chrmgr.EFFECT_WEAPON_JULY_BE, "PART_WEAPON", "D:/ymir work/item/costume/achievement_zvon.mse")
	chrmgr.RegisterEffect(chrmgr.EFFECT_REFINED + chrmgr.EFFECT_WEAPON_JULY_FA, "PART_WEAPON", "D:/ymir work/item/costume/achievement_vejir.mse")
	
	chrmgr.RegisterEffect(chrmgr.EFFECT_REFINED + chrmgr.EFFECT_WEAPON_AUG_SW, "PART_WEAPON", "D:/ymir work/item/costume/set_34_sword_s.mse")
	chrmgr.RegisterEffect(chrmgr.EFFECT_REFINED + chrmgr.EFFECT_WEAPON_AUG_SW_2, "PART_WEAPON", "D:/ymir work/item/costume/set_34_sword.mse")
	chrmgr.RegisterEffect(chrmgr.EFFECT_REFINED + chrmgr.EFFECT_WEAPON_AUG_TW, "PART_WEAPON", "D:/ymir work/item/costume/set_34_spear.mse")
	chrmgr.RegisterEffect(chrmgr.EFFECT_REFINED + chrmgr.EFFECT_WEAPON_AUG_DA, "PART_WEAPON_LEFT", "D:/ymir work/item/costume/set_34_knife.mse")
	chrmgr.RegisterEffect(chrmgr.EFFECT_REFINED + chrmgr.EFFECT_WEAPON_AUG_DA2, "PART_WEAPON", "D:/ymir work/item/costume/set_34_knife.mse")
	chrmgr.RegisterEffect(chrmgr.EFFECT_REFINED + chrmgr.EFFECT_WEAPON_AUG_BO, "PART_WEAPON_LEFT", "D:/ymir work/item/costume/set_34_bow.mse")
	chrmgr.RegisterEffect(chrmgr.EFFECT_REFINED + chrmgr.EFFECT_WEAPON_AUG_BE, "PART_WEAPON", "D:/ymir work/item/costume/set_34_bell.mse")
	chrmgr.RegisterEffect(chrmgr.EFFECT_REFINED + chrmgr.EFFECT_WEAPON_AUG_FA, "PART_WEAPON", "D:/ymir work/item/costume/set_34_range.mse")
    
	chrmgr.RegisterEffect(chrmgr.EFFECT_REFINED + chrmgr.EFFECT_WEAPON_GAL_SW, "PART_WEAPON", "D:/ymir work/item/weapon/ridack_sword.mse")
	chrmgr.RegisterEffect(chrmgr.EFFECT_REFINED + chrmgr.EFFECT_WEAPON_GAL_SW_2, "PART_WEAPON", "D:/ymir work/item/weapon/ridack_swords.mse")
	chrmgr.RegisterEffect(chrmgr.EFFECT_REFINED + chrmgr.EFFECT_WEAPON_GAL_TW, "PART_WEAPON", "D:/ymir work/item/weapon/ridack_spear.mse")
	chrmgr.RegisterEffect(chrmgr.EFFECT_REFINED + chrmgr.EFFECT_WEAPON_GAL_DA, "PART_WEAPON_LEFT", "D:/ymir work/item/weapon/ridack_knife.mse")
	chrmgr.RegisterEffect(chrmgr.EFFECT_REFINED + chrmgr.EFFECT_WEAPON_GAL_DA2, "PART_WEAPON", "D:/ymir work/item/weapon/ridack_knife.mse")
	chrmgr.RegisterEffect(chrmgr.EFFECT_REFINED + chrmgr.EFFECT_WEAPON_GAL_BO, "PART_WEAPON_LEFT", "D:/ymir work/item/weapon/ridack_bow.mse")
	chrmgr.RegisterEffect(chrmgr.EFFECT_REFINED + chrmgr.EFFECT_WEAPON_GAL_BE, "PART_WEAPON", "D:/ymir work/item/weapon/ridack_bell.mse")
	chrmgr.RegisterEffect(chrmgr.EFFECT_REFINED + chrmgr.EFFECT_WEAPON_GAL_FA, "PART_WEAPON", "D:/ymir work/item/weapon/ridack_fan.mse")
    
#Halloween2019
	chrmgr.RegisterEffect(chrmgr.EFFECT_REFINED + chrmgr.EFFECT_WEAPON_HALLOWEEN_SW, "PART_WEAPON", "D:/ymir work/effect/plechito/weapons/h2019_set/sword.mse")
	chrmgr.RegisterEffect(chrmgr.EFFECT_REFINED + chrmgr.EFFECT_WEAPON_HALLOWEEN_TW, "PART_WEAPON", "D:/ymir work/effect/plechito/weapons/h2019_set/twohand.mse")
	chrmgr.RegisterEffect(chrmgr.EFFECT_REFINED + chrmgr.EFFECT_WEAPON_HALLOWEEN_DA, "PART_WEAPON_LEFT", "D:/ymir work/effect/plechito/weapons/h2019_set/dagger.mse")
	chrmgr.RegisterEffect(chrmgr.EFFECT_REFINED + chrmgr.EFFECT_WEAPON_HALLOWEEN_DA2, "PART_WEAPON", "D:/ymir work/effect/plechito/weapons/h2019_set/dagger.mse")
	chrmgr.RegisterEffect(chrmgr.EFFECT_REFINED + chrmgr.EFFECT_WEAPON_HALLOWEEN_BO, "PART_WEAPON_LEFT", "D:/ymir work/effect/plechito/weapons/h2019_set/bow.mse")
	chrmgr.RegisterEffect(chrmgr.EFFECT_REFINED + chrmgr.EFFECT_WEAPON_HALLOWEEN_BE, "PART_WEAPON", "D:/ymir work/effect/plechito/weapons/h2019_set/bell.mse")
	chrmgr.RegisterEffect(chrmgr.EFFECT_REFINED + chrmgr.EFFECT_WEAPON_HALLOWEEN_FA, "PART_WEAPON", "D:/ymir work/effect/plechito/weapons/h2019_set/fan.mse")
	chrmgr.RegisterEffect(chrmgr.EFFECT_REFINED+chrmgr.EFFECT_BODYARMOR_SPECIAL9, "Bip01", "D:/ymir work/effect/ridack_zombie.mse")


	chrmgr.RegisterShiningEffect(0, item.WEAPON_NUM_TYPES, "D:/ymir work/pc/common/effect/armor/armor_legend_9.mse")
	chrmgr.RegisterShiningEffect(1, item.WEAPON_NUM_TYPES, "D:/ymir work/pc/common/effect/armor/armor_legend_9_black.mse")
	chrmgr.RegisterShiningEffect(2, item.WEAPON_NUM_TYPES, "D:/ymir work/pc/common/effect/armor/armor_legend_9_blue.mse")
	chrmgr.RegisterShiningEffect(3, item.WEAPON_NUM_TYPES, "D:/ymir work/pc/common/effect/armor/armor_legend_9_green.mse")
	chrmgr.RegisterShiningEffect(4, item.WEAPON_NUM_TYPES, "D:/ymir work/pc/common/effect/armor/armor_legend_9_orange.mse")
	chrmgr.RegisterShiningEffect(5, item.WEAPON_NUM_TYPES, "D:/ymir work/pc/common/effect/armor/armor_legend_9_red.mse")
	chrmgr.RegisterShiningEffect(6, item.WEAPON_NUM_TYPES, "D:/ymir work/pc/common/effect/armor/armor_legend_9_violet.mse")
	chrmgr.RegisterShiningEffect(7, item.WEAPON_NUM_TYPES, "D:/ymir work/pc/common/effect/armor/armor_legend_9_yellow.mse")
	chrmgr.RegisterShiningEffect(8, item.WEAPON_NUM_TYPES, "D:/ymir work/pc/common/effect/armor/armor-4-2-1.mse")
	chrmgr.RegisterShiningEffect(8, item.WEAPON_NUM_TYPES, "D:/ymir work/pc/common/effect/armor/armor-4-2-2.mse")
	chrmgr.RegisterShiningEffect(9, item.WEAPON_NUM_TYPES, "D:/ymir work/pc/common/effect/armor/armor-4-2-3.mse")
	chrmgr.RegisterShiningEffect(9, item.WEAPON_NUM_TYPES, "D:/ymir work/pc/common/effect/armor/armor-4-2-4.mse")
	chrmgr.RegisterShiningEffect(10, item.WEAPON_NUM_TYPES, "D:/ymir work/pc/common/effect/armor/armor-4-2-5.mse")
	chrmgr.RegisterShiningEffect(10, item.WEAPON_NUM_TYPES, "D:/ymir work/pc/common/effect/armor/armor-4-2-6.mse")
	chrmgr.RegisterShiningEffect(11, item.WEAPON_NUM_TYPES, "D:/ymir work/pc/common/effect/armor/armor-4-2-7.mse")
	chrmgr.RegisterShiningEffect(11, item.WEAPON_NUM_TYPES, "D:/ymir work/pc/common/effect/armor/armor-4-2-8.mse")
	chrmgr.RegisterShiningEffect(12, item.WEAPON_NUM_TYPES, "D:/ymir work/pc/common/effect/armor/armor-4-2-9.mse")
	chrmgr.RegisterShiningEffect(12, item.WEAPON_NUM_TYPES, "D:/ymir work/pc/common/effect/armor/armor-4-2-10.mse")
	chrmgr.RegisterShiningEffect(13, item.WEAPON_NUM_TYPES, "D:/ymir work/pc/common/effect/armor/armor-4-2-11.mse")
	chrmgr.RegisterShiningEffect(13, item.WEAPON_NUM_TYPES, "D:/ymir work/pc/common/effect/armor/armor-4-2-12.mse")
	chrmgr.RegisterShiningEffect(14, item.WEAPON_NUM_TYPES, "D:/ymir work/pc/common/effect/armor/armor-4-2-13_1.mse")
	chrmgr.RegisterShiningEffect(14, item.WEAPON_NUM_TYPES, "D:/ymir work/pc/common/effect/armor/armor-4-2-13_2.mse")
	chrmgr.RegisterShiningEffect(15, item.WEAPON_NUM_TYPES, "D:/ymir work/pc/common/effect/armor/armor-4-2-14_1.mse")
	chrmgr.RegisterShiningEffect(15, item.WEAPON_NUM_TYPES, "D:/ymir work/pc/common/effect/armor/armor-4-2-14_2.mse")
	chrmgr.RegisterShiningEffect(16, item.WEAPON_NUM_TYPES, "D:/ymir work/pc/common/effect/armor/vip.mse")
	chrmgr.RegisterShiningEffect(17, item.WEAPON_NUM_TYPES, "D:/ymir work/pc/common/effect/armor/gelb.mse")
	chrmgr.RegisterShiningEffect(18, item.WEAPON_NUM_TYPES, "D:/ymir work/pc/common/effect/armor/grun.mse")
	chrmgr.RegisterShiningEffect(19, item.WEAPON_NUM_TYPES, "D:/ymir work/pc/common/effect/armor/orange.mse")
	chrmgr.RegisterShiningEffect(20, item.WEAPON_NUM_TYPES, "D:/ymir work/pc/common/effect/armor/rot.mse")
	chrmgr.RegisterShiningEffect(21, item.WEAPON_NUM_TYPES, "D:/ymir work/pc/common/effect/armor/violett.mse")
	chrmgr.RegisterShiningEffect(22, item.WEAPON_NUM_TYPES, "D:/ymir work/pc/common/effect/armor/blau.mse")
	chrmgr.RegisterShiningEffect(23, item.WEAPON_NUM_TYPES, "D:/ymir work/pc/common/effect/armor/weiss.mse")
	chrmgr.RegisterShiningEffect(24, item.WEAPON_SWORD, "D:/ymir work/pc/common/effect/sword/sword_10_red.mse")
	chrmgr.RegisterShiningEffect(24, item.WEAPON_DAGGER, "D:/ymir work/pc/common/effect/sword/sword_10_s_red.mse")
	chrmgr.RegisterShiningEffect(24, item.WEAPON_BOW, "D:/ymir work/pc/common/effect/sword/sword_10_b_red.mse")
	chrmgr.RegisterShiningEffect(24, item.WEAPON_TWO_HANDED, "D:/ymir work/pc/common/effect/sword/sword_10_red.mse")
	chrmgr.RegisterShiningEffect(24, item.WEAPON_FAN, "D:/ymir work/pc/common/effect/sword/sword_10_f_red.mse")
	chrmgr.RegisterShiningEffect(24, item.WEAPON_BELL, "D:/ymir work/pc/common/effect/sword/sword_10_f_red.mse")
	chrmgr.RegisterShiningEffect(25, item.WEAPON_SWORD, "D:/ymir work/pc/common/effect/sword/sword_10_blue.mse")
	chrmgr.RegisterShiningEffect(25, item.WEAPON_DAGGER, "D:/ymir work/pc/common/effect/sword/sword_10_s_blue.mse")
	chrmgr.RegisterShiningEffect(25, item.WEAPON_BOW, "D:/ymir work/pc/common/effect/sword/sword_10_b_blue.mse")
	chrmgr.RegisterShiningEffect(25, item.WEAPON_TWO_HANDED, "D:/ymir work/pc/common/effect/sword/sword_10_blue.mse")
	chrmgr.RegisterShiningEffect(25, item.WEAPON_FAN, "D:/ymir work/pc/common/effect/sword/sword_10_f_blue.mse")
	chrmgr.RegisterShiningEffect(25, item.WEAPON_BELL, "D:/ymir work/pc/common/effect/sword/sword_10_f_blue.mse")
	chrmgr.RegisterShiningEffect(26, item.WEAPON_SWORD, "D:/ymir work/pc/common/effect/sword/sword_10_green.mse")
	chrmgr.RegisterShiningEffect(26, item.WEAPON_DAGGER, "D:/ymir work/pc/common/effect/sword/sword_10_s_green.mse")
	chrmgr.RegisterShiningEffect(26, item.WEAPON_BOW, "D:/ymir work/pc/common/effect/sword/sword_10_b_green.mse")
	chrmgr.RegisterShiningEffect(26, item.WEAPON_TWO_HANDED, "D:/ymir work/pc/common/effect/sword/sword_10_green.mse")
	chrmgr.RegisterShiningEffect(26, item.WEAPON_FAN, "D:/ymir work/pc/common/effect/sword/sword_10_f_green.mse")
	chrmgr.RegisterShiningEffect(26, item.WEAPON_BELL, "D:/ymir work/pc/common/effect/sword/sword_10_f_green.mse")
	chrmgr.RegisterShiningEffect(27, item.WEAPON_SWORD, "D:/ymir work/pc/common/effect/sword/sword_10_orange.mse")
	chrmgr.RegisterShiningEffect(27, item.WEAPON_DAGGER, "D:/ymir work/pc/common/effect/sword/sword_10_s_orange.mse")
	chrmgr.RegisterShiningEffect(27, item.WEAPON_BOW, "D:/ymir work/pc/common/effect/sword/sword_10_b_orange.mse")
	chrmgr.RegisterShiningEffect(27, item.WEAPON_TWO_HANDED, "D:/ymir work/pc/common/effect/sword/sword_10_orange.mse")
	chrmgr.RegisterShiningEffect(27, item.WEAPON_FAN, "D:/ymir work/pc/common/effect/sword/sword_10_f_orange.mse")
	chrmgr.RegisterShiningEffect(27, item.WEAPON_BELL, "D:/ymir work/pc/common/effect/sword/sword_10_f_orange.mse")
	chrmgr.RegisterShiningEffect(28, item.WEAPON_SWORD, "D:/ymir work/pc/common/effect/sword/sword_10_violet.mse")
	chrmgr.RegisterShiningEffect(28, item.WEAPON_DAGGER, "D:/ymir work/pc/common/effect/sword/sword_10_s_violet.mse")
	chrmgr.RegisterShiningEffect(28, item.WEAPON_BOW, "D:/ymir work/pc/common/effect/sword/sword_10_b_violet.mse")
	chrmgr.RegisterShiningEffect(28, item.WEAPON_TWO_HANDED, "D:/ymir work/pc/common/effect/sword/sword_10_violet.mse")
	chrmgr.RegisterShiningEffect(28, item.WEAPON_FAN, "D:/ymir work/pc/common/effect/sword/sword_10_f_violet.mse")
	chrmgr.RegisterShiningEffect(28, item.WEAPON_BELL, "D:/ymir work/pc/common/effect/sword/sword_10_f_violet.mse")
	chrmgr.RegisterShiningEffect(29, item.WEAPON_SWORD, "D:/ymir work/pc/common/effect/sword/sword_10_white.mse")
	chrmgr.RegisterShiningEffect(29, item.WEAPON_DAGGER, "D:/ymir work/pc/common/effect/sword/sword_10_s_white.mse")
	chrmgr.RegisterShiningEffect(29, item.WEAPON_BOW, "D:/ymir work/pc/common/effect/sword/sword_10_b_white.mse")
	chrmgr.RegisterShiningEffect(29, item.WEAPON_TWO_HANDED, "D:/ymir work/pc/common/effect/sword/sword_10_white.mse")
	chrmgr.RegisterShiningEffect(29, item.WEAPON_FAN, "D:/ymir work/pc/common/effect/sword/sword_10_f_white.mse")
	chrmgr.RegisterShiningEffect(29, item.WEAPON_BELL, "D:/ymir work/pc/common/effect/sword/sword_10_f_white.mse")
	chrmgr.RegisterShiningEffect(30, item.WEAPON_SWORD, "D:/ymir work/pc/common/effect/sword/sword_10_yellow.mse")
	chrmgr.RegisterShiningEffect(30, item.WEAPON_DAGGER, "D:/ymir work/pc/common/effect/sword/sword_10_s_yellow.mse")
	chrmgr.RegisterShiningEffect(30, item.WEAPON_BOW, "D:/ymir work/pc/common/effect/sword/sword_10_b_yellow.mse")
	chrmgr.RegisterShiningEffect(30, item.WEAPON_TWO_HANDED, "D:/ymir work/pc/common/effect/sword/sword_10_yellow.mse")
	chrmgr.RegisterShiningEffect(30, item.WEAPON_FAN, "D:/ymir work/pc/common/effect/sword/sword_10_f_yellow.mse")
	chrmgr.RegisterShiningEffect(30, item.WEAPON_BELL, "D:/ymir work/pc/common/effect/sword/sword_10_f_yellow.mse")
	chrmgr.RegisterShiningEffect(31, item.WEAPON_NUM_TYPES, "D:/ymir work/pc/common/effect/armor/armor_20.mse")
	chrmgr.RegisterShiningEffect(32, item.WEAPON_NUM_TYPES, "D:/ymir work/pc/common/effect/armor/armor_21.mse")
	chrmgr.RegisterShiningEffect(33, item.WEAPON_NUM_TYPES, "D:/ymir work/pc/common/effect/armor/armor_22.mse")
	chrmgr.RegisterShiningEffect(34, item.WEAPON_NUM_TYPES, "D:/ymir work/pc/common/effect/armor/armor_23.mse")
	chrmgr.RegisterShiningEffect(35, item.WEAPON_NUM_TYPES, "D:/ymir work/pc/common/effect/armor/armor_24.mse")
	chrmgr.RegisterShiningEffect(36, item.WEAPON_NUM_TYPES, "D:/ymir work/pc/common/effect/armor/armor_25.mse")
	chrmgr.RegisterShiningEffect(37, item.WEAPON_NUM_TYPES, "D:/ymir work/pc/common/effect/armor/armor_fire.mse")
	chrmgr.RegisterShiningEffect(38, item.WEAPON_SWORD, "D:/ymir work/pc/common/effect/sword/sword_20.mse")
	chrmgr.RegisterShiningEffect(38, item.WEAPON_DAGGER, "D:/ymir work/pc/common/effect/sword/sword_20_s.mse")
	chrmgr.RegisterShiningEffect(38, item.WEAPON_BOW, "D:/ymir work/pc/common/effect/sword/sword_20_b.mse")
	chrmgr.RegisterShiningEffect(38, item.WEAPON_TWO_HANDED, "D:/ymir work/pc/common/effect/sword/sword_20.mse")
	chrmgr.RegisterShiningEffect(38, item.WEAPON_FAN, "D:/ymir work/pc/common/effect/sword/sword_20_f.mse")
	chrmgr.RegisterShiningEffect(38, item.WEAPON_BELL, "D:/ymir work/pc/common/effect/sword/sword_20_f.mse")
	chrmgr.RegisterShiningEffect(39, item.WEAPON_SWORD, "D:/ymir work/pc/common/effect/sword/sword_21.mse")
	chrmgr.RegisterShiningEffect(39, item.WEAPON_DAGGER, "D:/ymir work/pc/common/effect/sword/sword_21_s.mse")
	chrmgr.RegisterShiningEffect(39, item.WEAPON_BOW, "D:/ymir work/pc/common/effect/sword/sword_21_b.mse")
	chrmgr.RegisterShiningEffect(39, item.WEAPON_TWO_HANDED, "D:/ymir work/pc/common/effect/sword/sword_21.mse")
	chrmgr.RegisterShiningEffect(39, item.WEAPON_FAN, "D:/ymir work/pc/common/effect/sword/sword_21_f.mse")
	chrmgr.RegisterShiningEffect(39, item.WEAPON_BELL, "D:/ymir work/pc/common/effect/sword/sword_21_f.mse")
	chrmgr.RegisterShiningEffect(40, item.WEAPON_SWORD, "D:/ymir work/pc/common/effect/sword/sword_22.mse")
	chrmgr.RegisterShiningEffect(40, item.WEAPON_DAGGER, "D:/ymir work/pc/common/effect/sword/sword_22_s.mse")
	chrmgr.RegisterShiningEffect(40, item.WEAPON_BOW, "D:/ymir work/pc/common/effect/sword/sword_22_b.mse")
	chrmgr.RegisterShiningEffect(40, item.WEAPON_TWO_HANDED, "D:/ymir work/pc/common/effect/sword/sword_22.mse")
	chrmgr.RegisterShiningEffect(40, item.WEAPON_FAN, "D:/ymir work/pc/common/effect/sword/sword_22_f.mse")
	chrmgr.RegisterShiningEffect(40, item.WEAPON_BELL, "D:/ymir work/pc/common/effect/sword/sword_22_f.mse")
	chrmgr.RegisterShiningEffect(41, item.WEAPON_SWORD, "D:/ymir work/pc/common/effect/sword/sword_23.mse")
	chrmgr.RegisterShiningEffect(41, item.WEAPON_DAGGER, "D:/ymir work/pc/common/effect/sword/sword_23_s.mse")
	chrmgr.RegisterShiningEffect(41, item.WEAPON_BOW, "D:/ymir work/pc/common/effect/sword/sword_23_b.mse")
	chrmgr.RegisterShiningEffect(41, item.WEAPON_TWO_HANDED, "D:/ymir work/pc/common/effect/sword/sword_23.mse")
	chrmgr.RegisterShiningEffect(41, item.WEAPON_FAN, "D:/ymir work/pc/common/effect/sword/sword_23_f.mse")
	chrmgr.RegisterShiningEffect(41, item.WEAPON_BELL, "D:/ymir work/pc/common/effect/sword/sword_23_f.mse")
	chrmgr.RegisterShiningEffect(42, item.WEAPON_SWORD, "D:/ymir work/pc/common/effect/sword/sword_24.mse")
	chrmgr.RegisterShiningEffect(42, item.WEAPON_DAGGER, "D:/ymir work/pc/common/effect/sword/sword_24_s.mse")
	chrmgr.RegisterShiningEffect(42, item.WEAPON_BOW, "D:/ymir work/pc/common/effect/sword/sword_24_b.mse")
	chrmgr.RegisterShiningEffect(42, item.WEAPON_TWO_HANDED, "D:/ymir work/pc/common/effect/sword/sword_24.mse")
	chrmgr.RegisterShiningEffect(42, item.WEAPON_FAN, "D:/ymir work/pc/common/effect/sword/sword_24_f.mse")
	chrmgr.RegisterShiningEffect(42, item.WEAPON_BELL, "D:/ymir work/pc/common/effect/sword/sword_24_f.mse")
	chrmgr.RegisterShiningEffect(43, item.WEAPON_SWORD, "D:/ymir work/pc/common/effect/sword/sword_25.mse")
	chrmgr.RegisterShiningEffect(43, item.WEAPON_DAGGER, "D:/ymir work/pc/common/effect/sword/sword_25_s.mse")
	chrmgr.RegisterShiningEffect(43, item.WEAPON_BOW, "D:/ymir work/pc/common/effect/sword/sword_25_b.mse")
	chrmgr.RegisterShiningEffect(43, item.WEAPON_TWO_HANDED, "D:/ymir work/pc/common/effect/sword/sword_25.mse")
	chrmgr.RegisterShiningEffect(43, item.WEAPON_FAN, "D:/ymir work/pc/common/effect/sword/sword_25_f.mse")
	chrmgr.RegisterShiningEffect(43, item.WEAPON_BELL, "D:/ymir work/pc/common/effect/sword/sword_25_f.mse")
	chrmgr.RegisterShiningEffect(44, item.WEAPON_SWORD, "D:/ymir work/pc/common/effect/sword/sword_v2_blue.mse")
	chrmgr.RegisterShiningEffect(44, item.WEAPON_DAGGER, "D:/ymir work/pc/common/effect/sword/sword_s_v2_blue.mse")
	chrmgr.RegisterShiningEffect(44, item.WEAPON_BOW, "D:/ymir work/pc/common/effect/sword/sword_b_v2_blue.mse")
	chrmgr.RegisterShiningEffect(44, item.WEAPON_TWO_HANDED, "D:/ymir work/pc/common/effect/sword/sword_v2_blue.mse")
	chrmgr.RegisterShiningEffect(44, item.WEAPON_FAN, "D:/ymir work/pc/common/effect/sword/sword_f_v2_blue.mse")
	chrmgr.RegisterShiningEffect(44, item.WEAPON_BELL, "D:/ymir work/pc/common/effect/sword/sword_f_v2_blue.mse")
	chrmgr.RegisterShiningEffect(45, item.WEAPON_SWORD, "D:/ymir work/pc/common/effect/sword/sword_v2_red.mse")
	chrmgr.RegisterShiningEffect(45, item.WEAPON_DAGGER, "D:/ymir work/pc/common/effect/sword/sword_s_v2_red.mse")
	chrmgr.RegisterShiningEffect(45, item.WEAPON_BOW, "D:/ymir work/pc/common/effect/sword/sword_b_v2_red.mse")
	chrmgr.RegisterShiningEffect(45, item.WEAPON_TWO_HANDED, "D:/ymir work/pc/common/effect/sword/sword_v2_red.mse")
	chrmgr.RegisterShiningEffect(45, item.WEAPON_FAN, "D:/ymir work/pc/common/effect/sword/sword_f_v2_red.mse")
	chrmgr.RegisterShiningEffect(45, item.WEAPON_BELL, "D:/ymir work/pc/common/effect/sword/sword_f_v2_red.mse")
	chrmgr.RegisterShiningEffect(46, item.WEAPON_SWORD, "D:/ymir work/pc/common/effect/sword/sword_v2_orange.mse")
	chrmgr.RegisterShiningEffect(46, item.WEAPON_DAGGER, "D:/ymir work/pc/common/effect/sword/sword_s_v2_orange.mse")
	chrmgr.RegisterShiningEffect(46, item.WEAPON_BOW, "D:/ymir work/pc/common/effect/sword/sword_b_v2_orange.mse")
	chrmgr.RegisterShiningEffect(46, item.WEAPON_TWO_HANDED, "D:/ymir work/pc/common/effect/sword/sword_v2_orange.mse")
	chrmgr.RegisterShiningEffect(46, item.WEAPON_FAN, "D:/ymir work/pc/common/effect/sword/sword_f_v2_orange.mse")
	chrmgr.RegisterShiningEffect(46, item.WEAPON_BELL, "D:/ymir work/pc/common/effect/sword/sword_f_v2_orange.mse")
	chrmgr.RegisterShiningEffect(47, item.WEAPON_SWORD, "D:/ymir work/pc/common/effect/sword/sword_v2_yellow.mse")
	chrmgr.RegisterShiningEffect(47, item.WEAPON_DAGGER, "D:/ymir work/pc/common/effect/sword/sword_s_v2_yellow.mse")
	chrmgr.RegisterShiningEffect(47, item.WEAPON_BOW, "D:/ymir work/pc/common/effect/sword/sword_b_v2_yellow.mse")
	chrmgr.RegisterShiningEffect(47, item.WEAPON_TWO_HANDED, "D:/ymir work/pc/common/effect/sword/sword_v2_yellow.mse")
	chrmgr.RegisterShiningEffect(47, item.WEAPON_FAN, "D:/ymir work/pc/common/effect/sword/sword_f_v2_yellow.mse")
	chrmgr.RegisterShiningEffect(47, item.WEAPON_BELL, "D:/ymir work/pc/common/effect/sword/sword_f_v2_yellow.mse")
	chrmgr.RegisterShiningEffect(48, item.WEAPON_SWORD, "D:/ymir work/pc/common/effect/sword/sword_v2_white.mse")
	chrmgr.RegisterShiningEffect(48, item.WEAPON_DAGGER, "D:/ymir work/pc/common/effect/sword/sword_s_v2_white.mse")
	chrmgr.RegisterShiningEffect(48, item.WEAPON_BOW, "D:/ymir work/pc/common/effect/sword/sword_b_v2_white.mse")
	chrmgr.RegisterShiningEffect(48, item.WEAPON_TWO_HANDED, "D:/ymir work/pc/common/effect/sword/sword_v2_white.mse")
	chrmgr.RegisterShiningEffect(48, item.WEAPON_FAN, "D:/ymir work/pc/common/effect/sword/sword_f_v2_white.mse")
	chrmgr.RegisterShiningEffect(48, item.WEAPON_BELL, "D:/ymir work/pc/common/effect/sword/sword_f_v2_white.mse")
	chrmgr.RegisterShiningEffect(49, item.WEAPON_SWORD, "D:/ymir work/pc/common/effect/sword/sword_v2_violet.mse")
	chrmgr.RegisterShiningEffect(49, item.WEAPON_DAGGER, "D:/ymir work/pc/common/effect/sword/sword_s_v2_violet.mse")
	chrmgr.RegisterShiningEffect(49, item.WEAPON_BOW, "D:/ymir work/pc/common/effect/sword/sword_b_v2_violet.mse")
	chrmgr.RegisterShiningEffect(49, item.WEAPON_TWO_HANDED, "D:/ymir work/pc/common/effect/sword/sword_v2_violet.mse")
	chrmgr.RegisterShiningEffect(49, item.WEAPON_FAN, "D:/ymir work/pc/common/effect/sword/sword_f_v2_violet.mse")
	chrmgr.RegisterShiningEffect(49, item.WEAPON_BELL, "D:/ymir work/pc/common/effect/sword/sword_f_v2_violet.mse")
	chrmgr.RegisterShiningEffect(50, item.WEAPON_SWORD, "D:/ymir work/pc/common/effect/sword/sword_v2_green.mse")
	chrmgr.RegisterShiningEffect(50, item.WEAPON_DAGGER, "D:/ymir work/pc/common/effect/sword/sword_s_v2_green.mse")
	chrmgr.RegisterShiningEffect(50, item.WEAPON_BOW, "D:/ymir work/pc/common/effect/sword/sword_b_v2_green.mse")
	chrmgr.RegisterShiningEffect(50, item.WEAPON_TWO_HANDED, "D:/ymir work/pc/common/effect/sword/sword_v2_green.mse")
	chrmgr.RegisterShiningEffect(50, item.WEAPON_FAN, "D:/ymir work/pc/common/effect/sword/sword_f_v2_green.mse")
	chrmgr.RegisterShiningEffect(50, item.WEAPON_BELL, "D:/ymir work/pc/common/effect/sword/sword_f_v2_green.mse")
	chrmgr.RegisterShiningEffect(51, item.WEAPON_NUM_TYPES, "D:/ymir work/pc/common/effect/armor/armor_v3_blue.mse")
	chrmgr.RegisterShiningEffect(52, item.WEAPON_NUM_TYPES, "D:/ymir work/pc/common/effect/armor/armor_v3_red.mse")
	chrmgr.RegisterShiningEffect(53, item.WEAPON_NUM_TYPES, "D:/ymir work/pc/common/effect/armor/armor_v3_yellow.mse")
	chrmgr.RegisterShiningEffect(54, item.WEAPON_NUM_TYPES, "D:/ymir work/pc/common/effect/armor/armor_v3_orange.mse")
	chrmgr.RegisterShiningEffect(55, item.WEAPON_NUM_TYPES, "D:/ymir work/pc/common/effect/armor/armor_v3_white.mse")
	chrmgr.RegisterShiningEffect(56, item.WEAPON_NUM_TYPES, "D:/ymir work/pc/common/effect/armor/armor_v3_green.mse")
	chrmgr.RegisterShiningEffect(57, item.WEAPON_NUM_TYPES, "D:/ymir work/pc/common/effect/armor/armor_v3_violet.mse")
	chrmgr.RegisterShiningEffect(58, item.WEAPON_NUM_TYPES, "d:/ymir work/pc/common/effect/armor/armor_v4_blue.mse")
	chrmgr.RegisterShiningEffect(59, item.WEAPON_NUM_TYPES, "D:/ymir work/pc/common/effect/armor/armor_v4_red.mse")
	chrmgr.RegisterShiningEffect(60, item.WEAPON_NUM_TYPES, "D:/ymir work/pc/common/effect/armor/armor_v4_yellow.mse")
	chrmgr.RegisterShiningEffect(61, item.WEAPON_NUM_TYPES, "D:/ymir work/pc/common/effect/armor/armor_v4_orange.mse")
	chrmgr.RegisterShiningEffect(62, item.WEAPON_NUM_TYPES, "D:/ymir work/pc/common/effect/armor/armor_v4_white.mse")
	chrmgr.RegisterShiningEffect(63, item.WEAPON_NUM_TYPES, "D:/ymir work/pc/common/effect/armor/armor_v4_green.mse")
	chrmgr.RegisterShiningEffect(64, item.WEAPON_NUM_TYPES, "D:/ymir work/pc/common/effect/armor/armor_v4_violet.mse")
	chrmgr.RegisterShiningEffect(65, item.WEAPON_NUM_TYPES, "D:/ymir work/pc/common/effect/armor/armor-5-1_2.mse")
	chrmgr.RegisterShiningEffect(66, item.WEAPON_NUM_TYPES, "D:/ymir work/pc/common/effect/armor/armor-5-1_3.mse")
	chrmgr.RegisterShiningEffect(67, item.WEAPON_NUM_TYPES, "D:/ymir work/pc/common/effect/armor/armor-5-1_4.mse")
	chrmgr.RegisterShiningEffect(68, item.WEAPON_NUM_TYPES, "D:/ymir work/pc/common/effect/armor/armor-5-1_5.mse")
	chrmgr.RegisterShiningEffect(69, item.WEAPON_NUM_TYPES, "D:/ymir work/pc/common/effect/armor/armor-5-1_6.mse")
	chrmgr.RegisterShiningEffect(70, item.WEAPON_NUM_TYPES, "D:/ymir work/pc/common/effect/armor/armor-5-1.mse")
	chrmgr.RegisterShiningEffect(71, item.WEAPON_NUM_TYPES, "D:/ymir work/pc/common/effect/armor/armor-5-1_7.mse")
	chrmgr.RegisterShiningEffect(72, item.WEAPON_SWORD, "D:/ymir work/effect/plechito/weapons/valentine2019/sword.mse")
	chrmgr.RegisterShiningEffect(72, item.WEAPON_DAGGER, "D:/ymir work/effect/plechito/weapons/valentine2019/dagger.mse")
	chrmgr.RegisterShiningEffect(72, item.WEAPON_BOW, "D:/ymir work/effect/plechito/weapons/valentine2019/bow.mse")
	chrmgr.RegisterShiningEffect(72, item.WEAPON_TWO_HANDED, "D:/ymir work/effect/plechito/weapons/valentine2019/twohand.mse")
	chrmgr.RegisterShiningEffect(72, item.WEAPON_FAN, "D:/ymir work/effect/plechito/weapons/valentine2019/fan.mse")
	chrmgr.RegisterShiningEffect(72, item.WEAPON_BELL, "D:/ymir work/effect/plechito/weapons/valentine2019/bell.mse")
	chrmgr.RegisterShiningEffect(73, item.WEAPON_NUM_TYPES, "D:/ymir work/pc/common/effect/RidackBlue/ridack_armorbv2.mse")
	chrmgr.RegisterShiningEffect(74, item.WEAPON_NUM_TYPES, "D:/ymir work/pc/common/effect/RidackFire/ridack_armorfv2.mse")
	chrmgr.RegisterShiningEffect(75, item.WEAPON_NUM_TYPES, "D:/ymir work/pc/common/effect/RidackWhite/ridack_armorwv2.mse")
	chrmgr.RegisterShiningEffect(76, item.WEAPON_NUM_TYPES, "D:/ymir work/pc/common/effect/RidackPurple/ridack_armorpv2.mse")
	chrmgr.RegisterShiningEffect(77, item.WEAPON_SWORD, "D:/ymir work/pc/common/effect/RidackBlue/weaponblue_9.mse")
	chrmgr.RegisterShiningEffect(77, item.WEAPON_DAGGER, "D:/ymir work/pc/common/effect/RidackBlue/weaponblue_9_s.mse")
	chrmgr.RegisterShiningEffect(77, item.WEAPON_BOW, "D:/ymir work/pc/common/effect/RidackBlue/weaponblue_9_b.mse")
	chrmgr.RegisterShiningEffect(77, item.WEAPON_TWO_HANDED, "D:/ymir work/pc/common/effect/RidackBlue/weaponblue_9_2h.mse")
	chrmgr.RegisterShiningEffect(77, item.WEAPON_FAN, "D:/ymir work/pc/common/effect/RidackBlue/weaponblue_9_f.mse")
	chrmgr.RegisterShiningEffect(77, item.WEAPON_BELL, "D:/ymir work/pc/common/effect/RidackBlue/weaponblue_9_s.mse")
	chrmgr.RegisterShiningEffect(78, item.WEAPON_SWORD, "D:/ymir work/pc/common/effect/RidackFire/weaponfire_9.mse")
	chrmgr.RegisterShiningEffect(78, item.WEAPON_DAGGER, "D:/ymir work/pc/common/effect/RidackFire/weaponfire_9_s.mse")
	chrmgr.RegisterShiningEffect(78, item.WEAPON_BOW, "D:/ymir work/pc/common/effect/RidackFire/weaponfire_9_b.mse")
	chrmgr.RegisterShiningEffect(78, item.WEAPON_TWO_HANDED, "D:/ymir work/pc/common/effect/RidackFire/weaponfire_9_2h.mse")
	chrmgr.RegisterShiningEffect(78, item.WEAPON_FAN, "D:/ymir work/pc/common/effect/RidackFire/weaponfire_9_f.mse")
	chrmgr.RegisterShiningEffect(78, item.WEAPON_BELL, "D:/ymir work/pc/common/effect/RidackFire/weaponfire_9_s.mse")
	chrmgr.RegisterShiningEffect(79, item.WEAPON_SWORD, "D:/ymir work/pc/common/effect/RidackWhite/weaponwhite_9.mse")
	chrmgr.RegisterShiningEffect(79, item.WEAPON_DAGGER, "D:/ymir work/pc/common/effect/RidackWhite/weaponwhite_9_s.mse")
	chrmgr.RegisterShiningEffect(79, item.WEAPON_BOW, "D:/ymir work/pc/common/effect/RidackWhite/weaponwhite_9_b.mse")
	chrmgr.RegisterShiningEffect(79, item.WEAPON_TWO_HANDED, "D:/ymir work/pc/common/effect/RidackWhite/weaponwhite_9_2h.mse")
	chrmgr.RegisterShiningEffect(79, item.WEAPON_FAN, "D:/ymir work/pc/common/effect/RidackWhite/weaponwhite_9_f.mse")
	chrmgr.RegisterShiningEffect(79, item.WEAPON_BELL, "D:/ymir work/pc/common/effect/RidackWhite/weaponwhite_9_s.mse")
	chrmgr.RegisterShiningEffect(80, item.WEAPON_SWORD, "D:/ymir work/pc/common/effect/RidackPurple/weaponpurple_9.mse")
	chrmgr.RegisterShiningEffect(80, item.WEAPON_DAGGER, "D:/ymir work/pc/common/effect/RidackPurple/weaponpurple_9_s.mse")
	chrmgr.RegisterShiningEffect(80, item.WEAPON_BOW, "D:/ymir work/pc/common/effect/RidackPurple/weaponpurple_9_b.mse")
	chrmgr.RegisterShiningEffect(80, item.WEAPON_TWO_HANDED, "D:/ymir work/pc/common/effect/RidackPurple/weaponpurple_9_2h.mse")
	chrmgr.RegisterShiningEffect(80, item.WEAPON_FAN, "D:/ymir work/pc/common/effect/RidackPurple/weaponpurple_9_f.mse")
	chrmgr.RegisterShiningEffect(80, item.WEAPON_BELL, "D:/ymir work/pc/common/effect/RidackPurple/weaponpurple_9_s.mse")
	chrmgr.RegisterShiningEffect(81, item.WEAPON_NUM_TYPES, "D:/ymir work/effect/pc/armor/ridack_armor.mse")
	chrmgr.RegisterShiningEffect(82, item.WEAPON_NUM_TYPES, "D:/ymir work/effect/pc/armor/ridack_armorangel.mse")
	chrmgr.RegisterShiningEffect(83, item.WEAPON_NUM_TYPES, "D:/ymir work/effect/pc/armor/ridack_armordevil.mse")
	chrmgr.RegisterShiningEffect(84, item.WEAPON_NUM_TYPES, "D:/ymir work/effect/armor_assassin3.mse") #rot
	chrmgr.RegisterShiningEffect(85, item.WEAPON_NUM_TYPES, "D:/ymir work/effect/armor_assassin4.mse") #blau
	chrmgr.RegisterShiningEffect(86, item.WEAPON_NUM_TYPES, "D:/ymir work/effect/armor_assassin5.mse") #grün
	chrmgr.RegisterShiningEffect(87, item.WEAPON_NUM_TYPES, "D:/ymir work/effect/armor_assassin6.mse") #orange
	chrmgr.RegisterShiningEffect(88, item.WEAPON_NUM_TYPES, "D:/ymir work/effect/armor_assassin7.mse") #lila
	chrmgr.RegisterShiningEffect(89, item.WEAPON_NUM_TYPES, "D:/ymir work/effect/armor_assassin8.mse") #weiß
	chrmgr.RegisterShiningEffect(90, item.WEAPON_NUM_TYPES, "D:/ymir work/pc/common/effect/armor/armor_7th_01.mse") #+15update
	chrmgr.RegisterShiningEffect(91, item.WEAPON_SWORD, "D:/ymir work/pc/common/effect/sword/sword_7th.mse") #+15update
	chrmgr.RegisterShiningEffect(91, item.WEAPON_DAGGER, "D:/ymir work/pc/common/effect/sword/sword_7th_s.mse") #+15update
	chrmgr.RegisterShiningEffect(91, item.WEAPON_BOW, "D:/ymir work/pc/common/effect/sword/sword_7th_b.mse") #+15update
	chrmgr.RegisterShiningEffect(91, item.WEAPON_TWO_HANDED, "D:/ymir work/pc/common/effect/sword/sword_7th.mse") #+15update #+15update
	chrmgr.RegisterShiningEffect(91, item.WEAPON_FAN, "D:/ymir work/pc/common/effect/sword/sword_7th_f.mse") #+15update
	chrmgr.RegisterShiningEffect(91, item.WEAPON_BELL, "D:/ymir work/pc/common/effect/sword/sword_7th_s.mse") #+15update
	chrmgr.RegisterShiningEffect(92, item.WEAPON_NUM_TYPES, "D:/ymir work/effect/shining_1.mse") #cosmos
	chrmgr.RegisterShiningEffect(93, item.WEAPON_NUM_TYPES, "D:/ymir work/effect/ridack_work/ridack_armor.mse") #galaxy

	chrmgr.RegisterShiningEffect(94, item.WEAPON_SWORD, "D:/ymir work/effect/plechito/weapons/sword.mse") #+15update
	chrmgr.RegisterShiningEffect(94, item.WEAPON_DAGGER, "D:/ymir work/effect/plechito/weapons/dagger.mse") #+15update
	chrmgr.RegisterShiningEffect(94, item.WEAPON_BOW, "D:/ymir work/effect/plechito/weapons/bow.mse") #+15update
	chrmgr.RegisterShiningEffect(94, item.WEAPON_TWO_HANDED, "D:/ymir work/effect/plechito/weapons/twohand.mse") #+15update #+15update
	chrmgr.RegisterShiningEffect(94, item.WEAPON_FAN, "D:/ymir work/effect/plechito/weapons/fan.mse") #+15update
	chrmgr.RegisterShiningEffect(94, item.WEAPON_BELL, "D:/ymir work/effect/plechito/weapons/bell.mse") #+15update

	
	if app.ENABLE_MELEY_LAIR_DUNGEON:
		chrmgr.RegisterEffect(chrmgr.EFFECT_AFFECT + chr.AFFECT_STATUE1, "", "d:/ymir work/effect/monster2/redd_moojuk.mse")
		chrmgr.RegisterEffect(chrmgr.EFFECT_AFFECT + chr.AFFECT_STATUE2, "", "d:/ymir work/effect/monster2/redd_moojuk.mse")
		chrmgr.RegisterEffect(chrmgr.EFFECT_AFFECT + chr.AFFECT_STATUE3, "", "d:/ymir work/effect/monster2/redd_moojuk_blue.mse")
		chrmgr.RegisterEffect(chrmgr.EFFECT_AFFECT + chr.AFFECT_STATUE4, "", "d:/ymir work/effect/monster2/redd_moojuk_green.mse")

	if app.ENABLE_HYDRA_DUNGEON:
		chrmgr.RegisterEffect(chrmgr.EFFECT_AFFECT + chr.AFFECT_HYDRA, "Bip01 Head", "d:/ymir work/effect/hit/blow_poison/bleeding_loop.mse", True)

	## FlyData
	effect.RegisterIndexedFlyData(effect.FLY_EXP, effect.INDEX_FLY_TYPE_NORMAL, "d:/ymir work/effect/etc/gathering/ga_piece_yellow_small2.msf")				## 노란색 (EXP)
	effect.RegisterIndexedFlyData(effect.FLY_HP_MEDIUM, effect.INDEX_FLY_TYPE_NORMAL, "d:/ymir work/effect/etc/gathering/ga_piece_red_small.msf")			## 빨간색 (HP) 작은거
	effect.RegisterIndexedFlyData(effect.FLY_HP_BIG, effect.INDEX_FLY_TYPE_NORMAL, "d:/ymir work/effect/etc/gathering/ga_piece_red_big.msf")				## 빨간색 (HP) 큰거
	effect.RegisterIndexedFlyData(effect.FLY_SP_SMALL, effect.INDEX_FLY_TYPE_NORMAL, "d:/ymir work/effect/etc/gathering/ga_piece_blue_warrior_small.msf")	## 파란색 꼬리만 있는거
	effect.RegisterIndexedFlyData(effect.FLY_SP_MEDIUM, effect.INDEX_FLY_TYPE_NORMAL, "d:/ymir work/effect/etc/gathering/ga_piece_blue_small.msf")			## 파란색 작은거
	effect.RegisterIndexedFlyData(effect.FLY_SP_BIG, effect.INDEX_FLY_TYPE_NORMAL, "d:/ymir work/effect/etc/gathering/ga_piece_blue_big.msf")				## 파란색 큰거
	effect.RegisterIndexedFlyData(effect.FLY_FIREWORK1, effect.INDEX_FLY_TYPE_FIRE_CRACKER, "d:/ymir work/effect/etc/firecracker/firecracker_1.msf")		## 폭죽 1
	effect.RegisterIndexedFlyData(effect.FLY_FIREWORK2, effect.INDEX_FLY_TYPE_FIRE_CRACKER, "d:/ymir work/effect/etc/firecracker/firecracker_2.msf")		## 폭죽 2
	effect.RegisterIndexedFlyData(effect.FLY_FIREWORK3, effect.INDEX_FLY_TYPE_FIRE_CRACKER, "d:/ymir work/effect/etc/firecracker/firecracker_3.msf")		## 폭죽 3
	effect.RegisterIndexedFlyData(effect.FLY_FIREWORK4, effect.INDEX_FLY_TYPE_FIRE_CRACKER, "d:/ymir work/effect/etc/firecracker/firecracker_4.msf")		## 폭죽 4
	effect.RegisterIndexedFlyData(effect.FLY_FIREWORK5, effect.INDEX_FLY_TYPE_FIRE_CRACKER, "d:/ymir work/effect/etc/firecracker/firecracker_5.msf")		## 폭죽 5
	effect.RegisterIndexedFlyData(effect.FLY_FIREWORK6, effect.INDEX_FLY_TYPE_FIRE_CRACKER, "d:/ymir work/effect/etc/firecracker/firecracker_6.msf")		## 폭죽 6
	effect.RegisterIndexedFlyData(effect.FLY_FIREWORK_XMAS, effect.INDEX_FLY_TYPE_FIRE_CRACKER, "d:/ymir work/effect/etc/firecracker/firecracker_xmas.msf")	## 폭죽 X-Mas
	effect.RegisterIndexedFlyData(effect.FLY_CHAIN_LIGHTNING, effect.INDEX_FLY_TYPE_NORMAL, "d:/ymir work/pc/shaman/effect/pokroe.msf")						## 폭뢰격
	effect.RegisterIndexedFlyData(effect.FLY_HP_SMALL, effect.INDEX_FLY_TYPE_NORMAL, "d:/ymir work/effect/etc/gathering/ga_piece_red_smallest.msf")			## 빨간색 매우 작은거
	effect.RegisterIndexedFlyData(effect.FLY_SKILL_MUYEONG, effect.INDEX_FLY_TYPE_AUTO_FIRE, "d:/ymir work/pc/sura/effect/muyeong_fly.msf")					## 무영진

	#########################################################################################
	## Emoticon
	EmoticonStr = "d:/ymir work/effect/etc/emoticon/"

	chrmgr.RegisterEffect(chrmgr.EFFECT_EMOTICON+0, "", EmoticonStr+"sweat.mse")
	net.RegisterEmoticonString("(황당)")

	chrmgr.RegisterEffect(chrmgr.EFFECT_EMOTICON+1, "", EmoticonStr+"money.mse")
	net.RegisterEmoticonString("(돈)")

	chrmgr.RegisterEffect(chrmgr.EFFECT_EMOTICON+2, "", EmoticonStr+"happy.mse")
	net.RegisterEmoticonString("(기쁨)")

	chrmgr.RegisterEffect(chrmgr.EFFECT_EMOTICON+3, "", EmoticonStr+"love_s.mse")
	net.RegisterEmoticonString("(좋아)")

	chrmgr.RegisterEffect(chrmgr.EFFECT_EMOTICON+4, "", EmoticonStr+"love_l.mse")
	net.RegisterEmoticonString("(사랑)")

	chrmgr.RegisterEffect(chrmgr.EFFECT_EMOTICON+5, "", EmoticonStr+"angry.mse")
	net.RegisterEmoticonString("(분노)")

	chrmgr.RegisterEffect(chrmgr.EFFECT_EMOTICON+6, "", EmoticonStr+"aha.mse")
	net.RegisterEmoticonString("(아하)")

	chrmgr.RegisterEffect(chrmgr.EFFECT_EMOTICON+7, "", EmoticonStr+"gloom.mse")
	net.RegisterEmoticonString("(우울)")

	chrmgr.RegisterEffect(chrmgr.EFFECT_EMOTICON+8, "", EmoticonStr+"sorry.mse")
	net.RegisterEmoticonString("(죄송)")

	chrmgr.RegisterEffect(chrmgr.EFFECT_EMOTICON+9, "", EmoticonStr+"!_mix_back.mse")
	net.RegisterEmoticonString("(!)")

	chrmgr.RegisterEffect(chrmgr.EFFECT_EMOTICON+10, "", EmoticonStr+"question.mse")
	net.RegisterEmoticonString("(?)")

	chrmgr.RegisterEffect(chrmgr.EFFECT_EMOTICON+11, "", EmoticonStr+"fish.mse")
	net.RegisterEmoticonString("(fish)")

	if constInfo.ENABLE_NEW_EMOTES:
		chrmgr.RegisterEffect(chrmgr.EFFECT_EMOTICON+12, "", EmoticonStr+"nosay.mse")
		chrmgr.RegisterEffect(chrmgr.EFFECT_EMOTICON+13, "", EmoticonStr+"weather3.mse")
		chrmgr.RegisterEffect(chrmgr.EFFECT_EMOTICON+14, "", EmoticonStr+"celebration.mse")
		chrmgr.RegisterEffect(chrmgr.EFFECT_EMOTICON+15, "", EmoticonStr+"weather2.mse")
		chrmgr.RegisterEffect(chrmgr.EFFECT_EMOTICON+16, "", EmoticonStr+"call.mse")
		chrmgr.RegisterEffect(chrmgr.EFFECT_EMOTICON+17, "", EmoticonStr+"hungry.mse")
		chrmgr.RegisterEffect(chrmgr.EFFECT_EMOTICON+18, "", EmoticonStr+"siren.mse")

	## Emoticon
	#########################################################################################


def __LoadGameWarrior():
	__LoadGameWarriorEx(RACE_WARRIOR_M, "d:/ymir work/pc/warrior/")
	__LoadGameWarriorEx(RACE_WARRIOR_W, "d:/ymir work/pc2/warrior/")

def __LoadGameAssassin():
	__LoadGameAssassinEx(RACE_ASSASSIN_W, "d:/ymir work/pc/assassin/")
	__LoadGameAssassinEx(RACE_ASSASSIN_M, "d:/ymir work/pc2/assassin/")

def __LoadGameSura():
	__LoadGameSuraEx(RACE_SURA_M, "d:/ymir work/pc/sura/")
	__LoadGameSuraEx(RACE_SURA_W, "d:/ymir work/pc2/sura/")

def __LoadGameShaman():
	__LoadGameShamanEx(RACE_SHAMAN_W, "d:/ymir work/pc/shaman/")
	__LoadGameShamanEx(RACE_SHAMAN_M, "d:/ymir work/pc2/shaman/")
	
# def __LoadGameWolfman():
	# __LoadGameWolfmanEx(RACE_WOLFMAN_M, "d:/ymir work/pc3/wolfman/")

def __LoadGameWarriorEx(race, path):

	## Warrior
	#########################################################################################
	chrmgr.SelectRace(race)

	## GENERAL MODE
	SetGeneralMotions(chr.MOTION_MODE_GENERAL, path + "general/")
	chrmgr.SetMotionRandomWeight(chr.MOTION_MODE_GENERAL, chr.MOTION_WAIT, 0, 70)
	chrmgr.RegisterCacheMotionData(chr.MOTION_MODE_GENERAL, chr.MOTION_WAIT, "wait_1.msa", 30)
	chrmgr.RegisterCacheMotionData(chr.MOTION_MODE_GENERAL, chr.MOTION_COMBO_ATTACK_1, "attack.msa", 50)
	chrmgr.RegisterCacheMotionData(chr.MOTION_MODE_GENERAL, chr.MOTION_COMBO_ATTACK_1, "attack_1.msa", 50)

	## SKILL
	chrmgr.SetPathName(path + "skill/")
	for i in xrange(skill.SKILL_EFFECT_COUNT):
		END_STRING = ""
		if i != 0: END_STRING = "_%d" % (i+1)
		chrmgr.RegisterCacheMotionData(chr.MOTION_MODE_GENERAL, chr.MOTION_SKILL+(i*skill.SKILL_GRADEGAP)+1, "samyeon" + END_STRING + ".msa")
		chrmgr.RegisterCacheMotionData(chr.MOTION_MODE_GENERAL, chr.MOTION_SKILL+(i*skill.SKILL_GRADEGAP)+2, "palbang" + END_STRING + ".msa")
		chrmgr.RegisterCacheMotionData(chr.MOTION_MODE_GENERAL, chr.MOTION_SKILL+(i*skill.SKILL_GRADEGAP)+3, "jeongwi" + END_STRING + ".msa")
		chrmgr.RegisterCacheMotionData(chr.MOTION_MODE_GENERAL, chr.MOTION_SKILL+(i*skill.SKILL_GRADEGAP)+4, "geomgyeong" + END_STRING + ".msa")
		chrmgr.RegisterCacheMotionData(chr.MOTION_MODE_GENERAL, chr.MOTION_SKILL+(i*skill.SKILL_GRADEGAP)+5, "tanhwan" + END_STRING + ".msa")
		if NEW_678TH_SKILL_ENABLE:
			chrmgr.RegisterCacheMotionData(chr.MOTION_MODE_GENERAL, chr.MOTION_SKILL+(i*skill.SKILL_GRADEGAP)+6, "gihyeol" + END_STRING + ".msa")
		chrmgr.RegisterCacheMotionData(chr.MOTION_MODE_GENERAL, chr.MOTION_SKILL+(i*skill.SKILL_GRADEGAP)+16, "gigongcham" + END_STRING + ".msa")
		chrmgr.RegisterCacheMotionData(chr.MOTION_MODE_GENERAL, chr.MOTION_SKILL+(i*skill.SKILL_GRADEGAP)+17, "gyeoksan" + END_STRING + ".msa")
		chrmgr.RegisterCacheMotionData(chr.MOTION_MODE_GENERAL, chr.MOTION_SKILL+(i*skill.SKILL_GRADEGAP)+18, "daejin" + END_STRING + ".msa")
		chrmgr.RegisterCacheMotionData(chr.MOTION_MODE_GENERAL, chr.MOTION_SKILL+(i*skill.SKILL_GRADEGAP)+19, "cheongeun" + END_STRING + ".msa")
		chrmgr.RegisterCacheMotionData(chr.MOTION_MODE_GENERAL, chr.MOTION_SKILL+(i*skill.SKILL_GRADEGAP)+20, "geompung" + END_STRING + ".msa")
		if NEW_678TH_SKILL_ENABLE:
			chrmgr.RegisterCacheMotionData(chr.MOTION_MODE_GENERAL, chr.MOTION_SKILL+(i*skill.SKILL_GRADEGAP)+21, "noegeom" + END_STRING + ".msa")
		# PLS USE if test_server: !!
		# import dbg
		# dbg.TraceError("i*skill_gradegap+4 => %d*%d+4 => %s" % (i, skill.SKILL_GRADEGAP, "geomgyeong" + END_STRING + ".msa"))

	chrmgr.RegisterCacheMotionData(chr.MOTION_MODE_GENERAL, GUILD_SKILL_DRAGONBLOOD, "guild_yongsinuipi.msa")
	chrmgr.RegisterCacheMotionData(chr.MOTION_MODE_GENERAL, GUILD_SKILL_DRAGONBLESS, "guild_yongsinuichukbok.msa")
	chrmgr.RegisterCacheMotionData(chr.MOTION_MODE_GENERAL, GUILD_SKILL_BLESSARMOR, "guild_seonghwigap.msa")
	chrmgr.RegisterCacheMotionData(chr.MOTION_MODE_GENERAL, GUILD_SKILL_SPPEDUP, "guild_gasokhwa.msa")
	chrmgr.RegisterCacheMotionData(chr.MOTION_MODE_GENERAL, GUILD_SKILL_DRAGONWRATH, "guild_yongsinuibunno.msa")
	chrmgr.RegisterCacheMotionData(chr.MOTION_MODE_GENERAL, GUILD_SKILL_MAGICUP, "guild_jumunsul.msa")

	chrmgr.ReserveComboAttackNew(chr.MOTION_MODE_GENERAL, COMBO_TYPE_1, 1)
	chrmgr.RegisterComboAttackNew(chr.MOTION_MODE_GENERAL, COMBO_TYPE_1, COMBO_INDEX_1, chr.MOTION_COMBO_ATTACK_1)

	## EMOTION
	emotion.RegisterEmotionAnis(path)

	## ONEHAND_SWORD BATTLE
	chrmgr.SetPathName(path + "onehand_sword/")
	chrmgr.RegisterMotionMode(chr.MOTION_MODE_ONEHAND_SWORD)
	chrmgr.RegisterCacheMotionData(chr.MOTION_MODE_ONEHAND_SWORD, chr.MOTION_WAIT,				"wait.msa", 50)
	chrmgr.RegisterCacheMotionData(chr.MOTION_MODE_ONEHAND_SWORD, chr.MOTION_WAIT,				"wait_1.msa", 50)
	chrmgr.RegisterCacheMotionData(chr.MOTION_MODE_ONEHAND_SWORD, chr.MOTION_WALK,				"walk.msa")
	chrmgr.RegisterCacheMotionData(chr.MOTION_MODE_ONEHAND_SWORD, chr.MOTION_RUN,				"run.msa")
	chrmgr.RegisterCacheMotionData(chr.MOTION_MODE_ONEHAND_SWORD, chr.MOTION_DAMAGE,			"damage.msa", 50)
	chrmgr.RegisterCacheMotionData(chr.MOTION_MODE_ONEHAND_SWORD, chr.MOTION_DAMAGE,			"damage_1.msa", 50)
	chrmgr.RegisterCacheMotionData(chr.MOTION_MODE_ONEHAND_SWORD, chr.MOTION_DAMAGE_BACK,		"damage_2.msa", 50)
	chrmgr.RegisterCacheMotionData(chr.MOTION_MODE_ONEHAND_SWORD, chr.MOTION_DAMAGE_BACK,		"damage_3.msa", 50)
	chrmgr.RegisterCacheMotionData(chr.MOTION_MODE_ONEHAND_SWORD, chr.MOTION_COMBO_ATTACK_1,	"combo_01.msa")
	chrmgr.RegisterCacheMotionData(chr.MOTION_MODE_ONEHAND_SWORD, chr.MOTION_COMBO_ATTACK_2,	"combo_02.msa")
	chrmgr.RegisterCacheMotionData(chr.MOTION_MODE_ONEHAND_SWORD, chr.MOTION_COMBO_ATTACK_3,	"combo_03.msa")
	chrmgr.RegisterCacheMotionData(chr.MOTION_MODE_ONEHAND_SWORD, chr.MOTION_COMBO_ATTACK_4,	"combo_04.msa")
	chrmgr.RegisterCacheMotionData(chr.MOTION_MODE_ONEHAND_SWORD, chr.MOTION_COMBO_ATTACK_5,	"combo_05.msa")
	chrmgr.RegisterCacheMotionData(chr.MOTION_MODE_ONEHAND_SWORD, chr.MOTION_COMBO_ATTACK_6,	"combo_06.msa")
	chrmgr.RegisterCacheMotionData(chr.MOTION_MODE_ONEHAND_SWORD, chr.MOTION_COMBO_ATTACK_7,	"combo_07.msa")

	## Combo Type 1
	chrmgr.ReserveComboAttackNew(chr.MOTION_MODE_ONEHAND_SWORD, COMBO_TYPE_1, 4)
	chrmgr.RegisterComboAttackNew(chr.MOTION_MODE_ONEHAND_SWORD, COMBO_TYPE_1, COMBO_INDEX_1, chr.MOTION_COMBO_ATTACK_1)
	chrmgr.RegisterComboAttackNew(chr.MOTION_MODE_ONEHAND_SWORD, COMBO_TYPE_1, COMBO_INDEX_2, chr.MOTION_COMBO_ATTACK_2)
	chrmgr.RegisterComboAttackNew(chr.MOTION_MODE_ONEHAND_SWORD, COMBO_TYPE_1, COMBO_INDEX_3, chr.MOTION_COMBO_ATTACK_3)
	chrmgr.RegisterComboAttackNew(chr.MOTION_MODE_ONEHAND_SWORD, COMBO_TYPE_1, COMBO_INDEX_4, chr.MOTION_COMBO_ATTACK_4)
	## Combo Type 2
	chrmgr.ReserveComboAttackNew(chr.MOTION_MODE_ONEHAND_SWORD, COMBO_TYPE_2, 5)
	chrmgr.RegisterComboAttackNew(chr.MOTION_MODE_ONEHAND_SWORD, COMBO_TYPE_2, COMBO_INDEX_1, chr.MOTION_COMBO_ATTACK_1)
	chrmgr.RegisterComboAttackNew(chr.MOTION_MODE_ONEHAND_SWORD, COMBO_TYPE_2, COMBO_INDEX_2, chr.MOTION_COMBO_ATTACK_2)
	chrmgr.RegisterComboAttackNew(chr.MOTION_MODE_ONEHAND_SWORD, COMBO_TYPE_2, COMBO_INDEX_3, chr.MOTION_COMBO_ATTACK_3)
	chrmgr.RegisterComboAttackNew(chr.MOTION_MODE_ONEHAND_SWORD, COMBO_TYPE_2, COMBO_INDEX_4, chr.MOTION_COMBO_ATTACK_5)
	chrmgr.RegisterComboAttackNew(chr.MOTION_MODE_ONEHAND_SWORD, COMBO_TYPE_2, COMBO_INDEX_5, chr.MOTION_COMBO_ATTACK_7)
	## Combo Type 3
	chrmgr.ReserveComboAttackNew(chr.MOTION_MODE_ONEHAND_SWORD, COMBO_TYPE_3, 6)
	chrmgr.RegisterComboAttackNew(chr.MOTION_MODE_ONEHAND_SWORD, COMBO_TYPE_3, COMBO_INDEX_1, chr.MOTION_COMBO_ATTACK_1)
	chrmgr.RegisterComboAttackNew(chr.MOTION_MODE_ONEHAND_SWORD, COMBO_TYPE_3, COMBO_INDEX_2, chr.MOTION_COMBO_ATTACK_2)
	chrmgr.RegisterComboAttackNew(chr.MOTION_MODE_ONEHAND_SWORD, COMBO_TYPE_3, COMBO_INDEX_3, chr.MOTION_COMBO_ATTACK_3)
	chrmgr.RegisterComboAttackNew(chr.MOTION_MODE_ONEHAND_SWORD, COMBO_TYPE_3, COMBO_INDEX_4, chr.MOTION_COMBO_ATTACK_5)
	chrmgr.RegisterComboAttackNew(chr.MOTION_MODE_ONEHAND_SWORD, COMBO_TYPE_3, COMBO_INDEX_5, chr.MOTION_COMBO_ATTACK_6)
	chrmgr.RegisterComboAttackNew(chr.MOTION_MODE_ONEHAND_SWORD, COMBO_TYPE_3, COMBO_INDEX_6, chr.MOTION_COMBO_ATTACK_4)

	## TWOHAND_SWORD BATTLE
	chrmgr.SetPathName(path + "twohand_sword/")
	chrmgr.RegisterMotionMode(chr.MOTION_MODE_TWOHAND_SWORD)
	chrmgr.RegisterCacheMotionData(chr.MOTION_MODE_TWOHAND_SWORD, chr.MOTION_WAIT,				"wait.msa", 70)
	chrmgr.RegisterCacheMotionData(chr.MOTION_MODE_TWOHAND_SWORD, chr.MOTION_WAIT,				"wait_1.msa", 30)
	chrmgr.RegisterCacheMotionData(chr.MOTION_MODE_TWOHAND_SWORD, chr.MOTION_WALK,				"walk.msa")
	chrmgr.RegisterCacheMotionData(chr.MOTION_MODE_TWOHAND_SWORD, chr.MOTION_RUN,				"run.msa")
	chrmgr.RegisterCacheMotionData(chr.MOTION_MODE_TWOHAND_SWORD, chr.MOTION_DAMAGE,			"damage.msa", 50)
	chrmgr.RegisterCacheMotionData(chr.MOTION_MODE_TWOHAND_SWORD, chr.MOTION_DAMAGE,			"damage_1.msa", 50)
	chrmgr.RegisterCacheMotionData(chr.MOTION_MODE_TWOHAND_SWORD, chr.MOTION_DAMAGE_BACK,		"damage_2.msa", 50)
	chrmgr.RegisterCacheMotionData(chr.MOTION_MODE_TWOHAND_SWORD, chr.MOTION_DAMAGE_BACK,		"damage_3.msa", 50)
	chrmgr.RegisterCacheMotionData(chr.MOTION_MODE_TWOHAND_SWORD, chr.MOTION_COMBO_ATTACK_1,	"combo_01.msa")
	chrmgr.RegisterCacheMotionData(chr.MOTION_MODE_TWOHAND_SWORD, chr.MOTION_COMBO_ATTACK_2,	"combo_02.msa")
	chrmgr.RegisterCacheMotionData(chr.MOTION_MODE_TWOHAND_SWORD, chr.MOTION_COMBO_ATTACK_3,	"combo_03.msa")
	chrmgr.RegisterCacheMotionData(chr.MOTION_MODE_TWOHAND_SWORD, chr.MOTION_COMBO_ATTACK_4,	"combo_04.msa")
	chrmgr.RegisterCacheMotionData(chr.MOTION_MODE_TWOHAND_SWORD, chr.MOTION_COMBO_ATTACK_5,	"combo_05.msa")
	chrmgr.RegisterCacheMotionData(chr.MOTION_MODE_TWOHAND_SWORD, chr.MOTION_COMBO_ATTACK_6,	"combo_06.msa")
	chrmgr.RegisterCacheMotionData(chr.MOTION_MODE_TWOHAND_SWORD, chr.MOTION_COMBO_ATTACK_7,	"combo_07.msa")

	## Combo Type 1
	chrmgr.ReserveComboAttackNew(chr.MOTION_MODE_TWOHAND_SWORD, COMBO_TYPE_1, 4)
	chrmgr.RegisterComboAttackNew(chr.MOTION_MODE_TWOHAND_SWORD, COMBO_TYPE_1, COMBO_INDEX_1, chr.MOTION_COMBO_ATTACK_1)
	chrmgr.RegisterComboAttackNew(chr.MOTION_MODE_TWOHAND_SWORD, COMBO_TYPE_1, COMBO_INDEX_2, chr.MOTION_COMBO_ATTACK_2)
	chrmgr.RegisterComboAttackNew(chr.MOTION_MODE_TWOHAND_SWORD, COMBO_TYPE_1, COMBO_INDEX_3, chr.MOTION_COMBO_ATTACK_3)
	chrmgr.RegisterComboAttackNew(chr.MOTION_MODE_TWOHAND_SWORD, COMBO_TYPE_1, COMBO_INDEX_4, chr.MOTION_COMBO_ATTACK_4)
	## Combo Type 2
	chrmgr.ReserveComboAttackNew(chr.MOTION_MODE_TWOHAND_SWORD, COMBO_TYPE_2, 5)
	chrmgr.RegisterComboAttackNew(chr.MOTION_MODE_TWOHAND_SWORD, COMBO_TYPE_2, COMBO_INDEX_1, chr.MOTION_COMBO_ATTACK_1)
	chrmgr.RegisterComboAttackNew(chr.MOTION_MODE_TWOHAND_SWORD, COMBO_TYPE_2, COMBO_INDEX_2, chr.MOTION_COMBO_ATTACK_2)
	chrmgr.RegisterComboAttackNew(chr.MOTION_MODE_TWOHAND_SWORD, COMBO_TYPE_2, COMBO_INDEX_3, chr.MOTION_COMBO_ATTACK_3)
	chrmgr.RegisterComboAttackNew(chr.MOTION_MODE_TWOHAND_SWORD, COMBO_TYPE_2, COMBO_INDEX_4, chr.MOTION_COMBO_ATTACK_5)
	chrmgr.RegisterComboAttackNew(chr.MOTION_MODE_TWOHAND_SWORD, COMBO_TYPE_2, COMBO_INDEX_5, chr.MOTION_COMBO_ATTACK_7)
	## Combo Type 3
	chrmgr.ReserveComboAttackNew(chr.MOTION_MODE_TWOHAND_SWORD, COMBO_TYPE_3, 6)
	chrmgr.RegisterComboAttackNew(chr.MOTION_MODE_TWOHAND_SWORD, COMBO_TYPE_3, COMBO_INDEX_1, chr.MOTION_COMBO_ATTACK_1)
	chrmgr.RegisterComboAttackNew(chr.MOTION_MODE_TWOHAND_SWORD, COMBO_TYPE_3, COMBO_INDEX_2, chr.MOTION_COMBO_ATTACK_2)
	chrmgr.RegisterComboAttackNew(chr.MOTION_MODE_TWOHAND_SWORD, COMBO_TYPE_3, COMBO_INDEX_3, chr.MOTION_COMBO_ATTACK_3)
	chrmgr.RegisterComboAttackNew(chr.MOTION_MODE_TWOHAND_SWORD, COMBO_TYPE_3, COMBO_INDEX_4, chr.MOTION_COMBO_ATTACK_5)
	chrmgr.RegisterComboAttackNew(chr.MOTION_MODE_TWOHAND_SWORD, COMBO_TYPE_3, COMBO_INDEX_5, chr.MOTION_COMBO_ATTACK_6)
	chrmgr.RegisterComboAttackNew(chr.MOTION_MODE_TWOHAND_SWORD, COMBO_TYPE_3, COMBO_INDEX_6, chr.MOTION_COMBO_ATTACK_4)

	## FISHING
	chrmgr.SetPathName(path + "fishing/")
	chrmgr.RegisterMotionMode(chr.MOTION_MODE_FISHING)
	chrmgr.RegisterCacheMotionData(chr.MOTION_MODE_FISHING, chr.MOTION_WAIT,			"wait.msa")
	chrmgr.RegisterCacheMotionData(chr.MOTION_MODE_FISHING, chr.MOTION_WALK,			"walk.msa")
	chrmgr.RegisterCacheMotionData(chr.MOTION_MODE_FISHING, chr.MOTION_RUN,				"run.msa")
	chrmgr.RegisterCacheMotionData(chr.MOTION_MODE_FISHING, chr.MOTION_FISHING_THROW,	"throw.msa")
	chrmgr.RegisterCacheMotionData(chr.MOTION_MODE_FISHING, chr.MOTION_FISHING_WAIT,	"fishing_wait.msa")
	chrmgr.RegisterCacheMotionData(chr.MOTION_MODE_FISHING, chr.MOTION_FISHING_STOP,	"fishing_cancel.msa")
	chrmgr.RegisterCacheMotionData(chr.MOTION_MODE_FISHING, chr.MOTION_FISHING_REACT,	"fishing_react.msa")
	chrmgr.RegisterCacheMotionData(chr.MOTION_MODE_FISHING, chr.MOTION_FISHING_CATCH,	"fishing_catch.msa")
	chrmgr.RegisterCacheMotionData(chr.MOTION_MODE_FISHING, chr.MOTION_FISHING_FAIL,	"fishing_fail.msa")

	## HORSE
	chrmgr.SetPathName(path + "horse/")
	chrmgr.RegisterMotionMode(chr.MOTION_MODE_HORSE)
	chrmgr.RegisterCacheMotionData(chr.MOTION_MODE_HORSE, chr.MOTION_WAIT,				"wait.msa", 90)
	chrmgr.RegisterCacheMotionData(chr.MOTION_MODE_HORSE, chr.MOTION_WAIT,				"wait_1.msa", 9)
	chrmgr.RegisterCacheMotionData(chr.MOTION_MODE_HORSE, chr.MOTION_WAIT,				"wait_2.msa", 1)
	chrmgr.RegisterCacheMotionData(chr.MOTION_MODE_HORSE, chr.MOTION_WALK,				"walk.msa")
	chrmgr.RegisterCacheMotionData(chr.MOTION_MODE_HORSE, chr.MOTION_RUN,				"run.msa")
	chrmgr.RegisterCacheMotionData(chr.MOTION_MODE_HORSE, chr.MOTION_DAMAGE,			"damage.msa")
	chrmgr.RegisterCacheMotionData(chr.MOTION_MODE_HORSE, chr.MOTION_DAMAGE_BACK,		"damage.msa")
	chrmgr.RegisterCacheMotionData(chr.MOTION_MODE_HORSE, chr.MOTION_DEAD,				"dead.msa")
	chrmgr.RegisterCacheMotionData(chr.MOTION_MODE_HORSE, HORSE_SKILL_CHARGE,			"skill_charge.msa")

	## HORSE_ONEHAND_SWORD
	chrmgr.SetPathName(path + "horse_onehand_sword/")
	chrmgr.RegisterMotionMode(chr.MOTION_MODE_HORSE_ONEHAND_SWORD)
	chrmgr.RegisterCacheMotionData(chr.MOTION_MODE_HORSE_ONEHAND_SWORD, chr.MOTION_COMBO_ATTACK_1, "combo_01.msa")
	chrmgr.RegisterCacheMotionData(chr.MOTION_MODE_HORSE_ONEHAND_SWORD, chr.MOTION_COMBO_ATTACK_2, "combo_02.msa")
	chrmgr.RegisterCacheMotionData(chr.MOTION_MODE_HORSE_ONEHAND_SWORD, chr.MOTION_COMBO_ATTACK_3, "combo_03.msa")
	chrmgr.ReserveComboAttackNew(chr.MOTION_MODE_HORSE_ONEHAND_SWORD, COMBO_TYPE_1, 3)
	chrmgr.RegisterComboAttackNew(chr.MOTION_MODE_HORSE_ONEHAND_SWORD, COMBO_TYPE_1, COMBO_INDEX_1, chr.MOTION_COMBO_ATTACK_1)
	chrmgr.RegisterComboAttackNew(chr.MOTION_MODE_HORSE_ONEHAND_SWORD, COMBO_TYPE_1, COMBO_INDEX_2, chr.MOTION_COMBO_ATTACK_2)
	chrmgr.RegisterComboAttackNew(chr.MOTION_MODE_HORSE_ONEHAND_SWORD, COMBO_TYPE_1, COMBO_INDEX_3, chr.MOTION_COMBO_ATTACK_3)
	chrmgr.RegisterCacheMotionData(chr.MOTION_MODE_HORSE_ONEHAND_SWORD, HORSE_SKILL_WILDATTACK, "skill_wildattack.msa")
	chrmgr.RegisterCacheMotionData(chr.MOTION_MODE_HORSE_ONEHAND_SWORD, HORSE_SKILL_SPLASH, "skill_splash.msa")

	## HORSE_TWOHAND_SWORD
	chrmgr.SetPathName(path + "horse_twohand_sword/")
	chrmgr.RegisterMotionMode(chr.MOTION_MODE_HORSE_TWOHAND_SWORD)
	chrmgr.RegisterCacheMotionData(chr.MOTION_MODE_HORSE_TWOHAND_SWORD, chr.MOTION_COMBO_ATTACK_1, "combo_01.msa")
	chrmgr.RegisterCacheMotionData(chr.MOTION_MODE_HORSE_TWOHAND_SWORD, chr.MOTION_COMBO_ATTACK_2, "combo_02.msa")
	chrmgr.RegisterCacheMotionData(chr.MOTION_MODE_HORSE_TWOHAND_SWORD, chr.MOTION_COMBO_ATTACK_3, "combo_03.msa")
	chrmgr.ReserveComboAttackNew(chr.MOTION_MODE_HORSE_TWOHAND_SWORD, COMBO_TYPE_1, 3)
	chrmgr.RegisterComboAttackNew(chr.MOTION_MODE_HORSE_TWOHAND_SWORD, COMBO_TYPE_1, COMBO_INDEX_1, chr.MOTION_COMBO_ATTACK_1)
	chrmgr.RegisterComboAttackNew(chr.MOTION_MODE_HORSE_TWOHAND_SWORD, COMBO_TYPE_1, COMBO_INDEX_2, chr.MOTION_COMBO_ATTACK_2)
	chrmgr.RegisterComboAttackNew(chr.MOTION_MODE_HORSE_TWOHAND_SWORD, COMBO_TYPE_1, COMBO_INDEX_3, chr.MOTION_COMBO_ATTACK_3)
	chrmgr.RegisterCacheMotionData(chr.MOTION_MODE_HORSE_TWOHAND_SWORD, HORSE_SKILL_WILDATTACK, "skill_wildattack.msa")
	chrmgr.RegisterCacheMotionData(chr.MOTION_MODE_HORSE_TWOHAND_SWORD, HORSE_SKILL_SPLASH, "skill_splash.msa")

	## Bone
	chrmgr.RegisterAttachingBoneName(chr.PART_WEAPON, "equip_right_hand")

def __LoadGameAssassinEx(race, path):
	## Assassin
	#########################################################################################
	chrmgr.SelectRace(race)

	## GENERAL MOTION MODE
	SetGeneralMotions(chr.MOTION_MODE_GENERAL, path + "general/")
	chrmgr.SetMotionRandomWeight(chr.MOTION_MODE_GENERAL, chr.MOTION_WAIT, 0, 70)
	chrmgr.RegisterCacheMotionData(chr.MOTION_MODE_GENERAL, chr.MOTION_WAIT, "wait_1.msa", 30)
	chrmgr.RegisterCacheMotionData(chr.MOTION_MODE_GENERAL, chr.MOTION_COMBO_ATTACK_1, "attack.msa", 50)
	chrmgr.RegisterCacheMotionData(chr.MOTION_MODE_GENERAL, chr.MOTION_COMBO_ATTACK_1, "attack_1.msa", 50)

	chrmgr.ReserveComboAttackNew(chr.MOTION_MODE_GENERAL, COMBO_TYPE_1, 1)
	chrmgr.RegisterComboAttackNew(chr.MOTION_MODE_GENERAL, COMBO_TYPE_1, COMBO_INDEX_1, chr.MOTION_COMBO_ATTACK_1)

	## SKILL
	chrmgr.SetPathName(path + "skill/")
	for i in xrange(skill.SKILL_EFFECT_COUNT):
		END_STRING = ""
		if i != 0: END_STRING = "_%d" % (i+1)
		chrmgr.RegisterCacheMotionData(chr.MOTION_MODE_GENERAL, chr.MOTION_SKILL+(i*skill.SKILL_GRADEGAP)+1, "amseup" + END_STRING + ".msa")
		chrmgr.RegisterCacheMotionData(chr.MOTION_MODE_GENERAL, chr.MOTION_SKILL+(i*skill.SKILL_GRADEGAP)+2, "gungsin" + END_STRING + ".msa")
		chrmgr.RegisterCacheMotionData(chr.MOTION_MODE_GENERAL, chr.MOTION_SKILL+(i*skill.SKILL_GRADEGAP)+3, "charyun" + END_STRING + ".msa")
		chrmgr.RegisterCacheMotionData(chr.MOTION_MODE_GENERAL, chr.MOTION_SKILL+(i*skill.SKILL_GRADEGAP)+4, "eunhyeong" + END_STRING + ".msa")
		chrmgr.RegisterCacheMotionData(chr.MOTION_MODE_GENERAL, chr.MOTION_SKILL+(i*skill.SKILL_GRADEGAP)+5, "sangong" + END_STRING + ".msa")
		if NEW_678TH_SKILL_ENABLE:
			chrmgr.RegisterCacheMotionData(chr.MOTION_MODE_GENERAL, chr.MOTION_SKILL+(i*skill.SKILL_GRADEGAP)+6, "seomjeon" + END_STRING + ".msa")
		chrmgr.RegisterCacheMotionData(chr.MOTION_MODE_GENERAL, chr.MOTION_SKILL+(i*skill.SKILL_GRADEGAP)+16, "yeonsa" + END_STRING + ".msa")
		chrmgr.RegisterCacheMotionData(chr.MOTION_MODE_GENERAL, chr.MOTION_SKILL+(i*skill.SKILL_GRADEGAP)+17, "gwangyeok" + END_STRING + ".msa")
		chrmgr.RegisterCacheMotionData(chr.MOTION_MODE_GENERAL, chr.MOTION_SKILL+(i*skill.SKILL_GRADEGAP)+18, "hwajo" + END_STRING + ".msa")
		chrmgr.RegisterCacheMotionData(chr.MOTION_MODE_GENERAL, chr.MOTION_SKILL+(i*skill.SKILL_GRADEGAP)+19, "gyeonggong" + END_STRING + ".msa")
		chrmgr.RegisterCacheMotionData(chr.MOTION_MODE_GENERAL, chr.MOTION_SKILL+(i*skill.SKILL_GRADEGAP)+20, "dokgigung" + END_STRING + ".msa")
		if NEW_678TH_SKILL_ENABLE:
			chrmgr.RegisterCacheMotionData(chr.MOTION_MODE_GENERAL, chr.MOTION_SKILL+(i*skill.SKILL_GRADEGAP)+21, "seomgwang" + END_STRING + ".msa")

	chrmgr.RegisterCacheMotionData(chr.MOTION_MODE_GENERAL, GUILD_SKILL_DRAGONBLOOD, "guild_yongsinuipi.msa")
	chrmgr.RegisterCacheMotionData(chr.MOTION_MODE_GENERAL, GUILD_SKILL_DRAGONBLESS, "guild_yongsinuichukbok.msa")
	chrmgr.RegisterCacheMotionData(chr.MOTION_MODE_GENERAL, GUILD_SKILL_BLESSARMOR, "guild_seonghwigap.msa")
	chrmgr.RegisterCacheMotionData(chr.MOTION_MODE_GENERAL, GUILD_SKILL_SPPEDUP, "guild_gasokhwa.msa")
	chrmgr.RegisterCacheMotionData(chr.MOTION_MODE_GENERAL, GUILD_SKILL_DRAGONWRATH, "guild_yongsinuibunno.msa")
	chrmgr.RegisterCacheMotionData(chr.MOTION_MODE_GENERAL, GUILD_SKILL_MAGICUP, "guild_jumunsul.msa")

	## EMOTION
	emotion.RegisterEmotionAnis(path)

	## ONEHAND_SWORD BATTLE
	chrmgr.SetPathName(path + "onehand_sword/")
	chrmgr.RegisterMotionMode(chr.MOTION_MODE_ONEHAND_SWORD)
	chrmgr.RegisterCacheMotionData(chr.MOTION_MODE_ONEHAND_SWORD, chr.MOTION_WAIT,		"wait.msa", 70)
	chrmgr.RegisterCacheMotionData(chr.MOTION_MODE_ONEHAND_SWORD, chr.MOTION_WAIT,		"wait_1.msa", 30)
	chrmgr.RegisterCacheMotionData(chr.MOTION_MODE_ONEHAND_SWORD, chr.MOTION_WALK,		"walk.msa")
	chrmgr.RegisterCacheMotionData(chr.MOTION_MODE_ONEHAND_SWORD, chr.MOTION_RUN,		"run.msa")
	chrmgr.RegisterCacheMotionData(chr.MOTION_MODE_ONEHAND_SWORD, chr.MOTION_DAMAGE,		"damage.msa", 50)
	chrmgr.RegisterCacheMotionData(chr.MOTION_MODE_ONEHAND_SWORD, chr.MOTION_DAMAGE,		"damage_1.msa", 50)
	chrmgr.RegisterCacheMotionData(chr.MOTION_MODE_ONEHAND_SWORD, chr.MOTION_DAMAGE_BACK,	"damage_2.msa", 50)
	chrmgr.RegisterCacheMotionData(chr.MOTION_MODE_ONEHAND_SWORD, chr.MOTION_DAMAGE_BACK,	"damage_3.msa", 50)
	chrmgr.RegisterCacheMotionData(chr.MOTION_MODE_ONEHAND_SWORD, chr.MOTION_COMBO_ATTACK_1, "combo_01.msa")
	chrmgr.RegisterCacheMotionData(chr.MOTION_MODE_ONEHAND_SWORD, chr.MOTION_COMBO_ATTACK_2, "combo_02.msa")
	chrmgr.RegisterCacheMotionData(chr.MOTION_MODE_ONEHAND_SWORD, chr.MOTION_COMBO_ATTACK_3, "combo_03.msa")
	chrmgr.RegisterCacheMotionData(chr.MOTION_MODE_ONEHAND_SWORD, chr.MOTION_COMBO_ATTACK_4, "combo_04.msa")
	chrmgr.RegisterCacheMotionData(chr.MOTION_MODE_ONEHAND_SWORD, chr.MOTION_COMBO_ATTACK_5, "combo_05.msa")
	chrmgr.RegisterCacheMotionData(chr.MOTION_MODE_ONEHAND_SWORD, chr.MOTION_COMBO_ATTACK_6, "combo_06.msa")
	chrmgr.RegisterCacheMotionData(chr.MOTION_MODE_ONEHAND_SWORD, chr.MOTION_COMBO_ATTACK_7, "combo_07.msa")

	## Combo Type 1
	chrmgr.ReserveComboAttackNew(chr.MOTION_MODE_ONEHAND_SWORD, COMBO_TYPE_1, 4)
	chrmgr.RegisterComboAttackNew(chr.MOTION_MODE_ONEHAND_SWORD, COMBO_TYPE_1, COMBO_INDEX_1, chr.MOTION_COMBO_ATTACK_1)
	chrmgr.RegisterComboAttackNew(chr.MOTION_MODE_ONEHAND_SWORD, COMBO_TYPE_1, COMBO_INDEX_2, chr.MOTION_COMBO_ATTACK_2)
	chrmgr.RegisterComboAttackNew(chr.MOTION_MODE_ONEHAND_SWORD, COMBO_TYPE_1, COMBO_INDEX_3, chr.MOTION_COMBO_ATTACK_3)
	chrmgr.RegisterComboAttackNew(chr.MOTION_MODE_ONEHAND_SWORD, COMBO_TYPE_1, COMBO_INDEX_4, chr.MOTION_COMBO_ATTACK_4)
	## Combo Type 2
	chrmgr.ReserveComboAttackNew(chr.MOTION_MODE_ONEHAND_SWORD, COMBO_TYPE_2, 5)
	chrmgr.RegisterComboAttackNew(chr.MOTION_MODE_ONEHAND_SWORD, COMBO_TYPE_2, COMBO_INDEX_1, chr.MOTION_COMBO_ATTACK_1)
	chrmgr.RegisterComboAttackNew(chr.MOTION_MODE_ONEHAND_SWORD, COMBO_TYPE_2, COMBO_INDEX_2, chr.MOTION_COMBO_ATTACK_2)
	chrmgr.RegisterComboAttackNew(chr.MOTION_MODE_ONEHAND_SWORD, COMBO_TYPE_2, COMBO_INDEX_3, chr.MOTION_COMBO_ATTACK_3)
	chrmgr.RegisterComboAttackNew(chr.MOTION_MODE_ONEHAND_SWORD, COMBO_TYPE_2, COMBO_INDEX_4, chr.MOTION_COMBO_ATTACK_5)
	chrmgr.RegisterComboAttackNew(chr.MOTION_MODE_ONEHAND_SWORD, COMBO_TYPE_2, COMBO_INDEX_5, chr.MOTION_COMBO_ATTACK_7)
	## Combo Type 3
	chrmgr.ReserveComboAttackNew(chr.MOTION_MODE_ONEHAND_SWORD, COMBO_TYPE_3, 6)
	chrmgr.RegisterComboAttackNew(chr.MOTION_MODE_ONEHAND_SWORD, COMBO_TYPE_3, COMBO_INDEX_1, chr.MOTION_COMBO_ATTACK_1)
	chrmgr.RegisterComboAttackNew(chr.MOTION_MODE_ONEHAND_SWORD, COMBO_TYPE_3, COMBO_INDEX_2, chr.MOTION_COMBO_ATTACK_2)
	chrmgr.RegisterComboAttackNew(chr.MOTION_MODE_ONEHAND_SWORD, COMBO_TYPE_3, COMBO_INDEX_3, chr.MOTION_COMBO_ATTACK_3)
	chrmgr.RegisterComboAttackNew(chr.MOTION_MODE_ONEHAND_SWORD, COMBO_TYPE_3, COMBO_INDEX_4, chr.MOTION_COMBO_ATTACK_5)
	chrmgr.RegisterComboAttackNew(chr.MOTION_MODE_ONEHAND_SWORD, COMBO_TYPE_3, COMBO_INDEX_5, chr.MOTION_COMBO_ATTACK_6)
	chrmgr.RegisterComboAttackNew(chr.MOTION_MODE_ONEHAND_SWORD, COMBO_TYPE_3, COMBO_INDEX_6, chr.MOTION_COMBO_ATTACK_4)

	## DUALHAND_SWORD BATTLE
	chrmgr.SetPathName(path + "dualhand_sword/")
	chrmgr.RegisterMotionMode(chr.MOTION_MODE_DUALHAND_SWORD)
	chrmgr.RegisterCacheMotionData(chr.MOTION_MODE_DUALHAND_SWORD, chr.MOTION_WAIT,			"wait.msa", 70)
	chrmgr.RegisterCacheMotionData(chr.MOTION_MODE_DUALHAND_SWORD, chr.MOTION_WAIT,			"wait_1.msa", 30)
	chrmgr.RegisterCacheMotionData(chr.MOTION_MODE_DUALHAND_SWORD, chr.MOTION_WALK,			"walk.msa")
	chrmgr.RegisterCacheMotionData(chr.MOTION_MODE_DUALHAND_SWORD, chr.MOTION_RUN,			"run.msa")
	chrmgr.RegisterCacheMotionData(chr.MOTION_MODE_DUALHAND_SWORD, chr.MOTION_DAMAGE,		"damage.msa", 50)
	chrmgr.RegisterCacheMotionData(chr.MOTION_MODE_DUALHAND_SWORD, chr.MOTION_DAMAGE,		"damage_1.msa", 50)
	chrmgr.RegisterCacheMotionData(chr.MOTION_MODE_DUALHAND_SWORD, chr.MOTION_DAMAGE_BACK,	"damage_2.msa", 50)
	chrmgr.RegisterCacheMotionData(chr.MOTION_MODE_DUALHAND_SWORD, chr.MOTION_DAMAGE_BACK,	"damage_3.msa", 50)
	chrmgr.RegisterCacheMotionData(chr.MOTION_MODE_DUALHAND_SWORD, chr.MOTION_COMBO_ATTACK_1, "combo_01.msa")
	chrmgr.RegisterCacheMotionData(chr.MOTION_MODE_DUALHAND_SWORD, chr.MOTION_COMBO_ATTACK_2, "combo_02.msa")
	chrmgr.RegisterCacheMotionData(chr.MOTION_MODE_DUALHAND_SWORD, chr.MOTION_COMBO_ATTACK_3, "combo_03.msa")
	chrmgr.RegisterCacheMotionData(chr.MOTION_MODE_DUALHAND_SWORD, chr.MOTION_COMBO_ATTACK_4, "combo_04.msa")
	chrmgr.RegisterCacheMotionData(chr.MOTION_MODE_DUALHAND_SWORD, chr.MOTION_COMBO_ATTACK_5, "combo_05.msa")
	chrmgr.RegisterCacheMotionData(chr.MOTION_MODE_DUALHAND_SWORD, chr.MOTION_COMBO_ATTACK_6, "combo_06.msa")
	chrmgr.RegisterCacheMotionData(chr.MOTION_MODE_DUALHAND_SWORD, chr.MOTION_COMBO_ATTACK_7, "combo_07.msa")
	chrmgr.RegisterCacheMotionData(chr.MOTION_MODE_DUALHAND_SWORD, chr.MOTION_COMBO_ATTACK_8, "combo_08.msa")

	## Combo Type 1
	chrmgr.ReserveComboAttackNew(chr.MOTION_MODE_DUALHAND_SWORD, COMBO_TYPE_1, 4)
	chrmgr.RegisterComboAttackNew(chr.MOTION_MODE_DUALHAND_SWORD, COMBO_TYPE_1, COMBO_INDEX_1, chr.MOTION_COMBO_ATTACK_1)
	chrmgr.RegisterComboAttackNew(chr.MOTION_MODE_DUALHAND_SWORD, COMBO_TYPE_1, COMBO_INDEX_2, chr.MOTION_COMBO_ATTACK_2)
	chrmgr.RegisterComboAttackNew(chr.MOTION_MODE_DUALHAND_SWORD, COMBO_TYPE_1, COMBO_INDEX_3, chr.MOTION_COMBO_ATTACK_3)
	chrmgr.RegisterComboAttackNew(chr.MOTION_MODE_DUALHAND_SWORD, COMBO_TYPE_1, COMBO_INDEX_4, chr.MOTION_COMBO_ATTACK_4)
	## Combo Type 2
	chrmgr.ReserveComboAttackNew(chr.MOTION_MODE_DUALHAND_SWORD, COMBO_TYPE_2, 5)
	chrmgr.RegisterComboAttackNew(chr.MOTION_MODE_DUALHAND_SWORD, COMBO_TYPE_2, COMBO_INDEX_1, chr.MOTION_COMBO_ATTACK_1)
	chrmgr.RegisterComboAttackNew(chr.MOTION_MODE_DUALHAND_SWORD, COMBO_TYPE_2, COMBO_INDEX_2, chr.MOTION_COMBO_ATTACK_2)
	chrmgr.RegisterComboAttackNew(chr.MOTION_MODE_DUALHAND_SWORD, COMBO_TYPE_2, COMBO_INDEX_3, chr.MOTION_COMBO_ATTACK_3)
	chrmgr.RegisterComboAttackNew(chr.MOTION_MODE_DUALHAND_SWORD, COMBO_TYPE_2, COMBO_INDEX_4, chr.MOTION_COMBO_ATTACK_5)
	chrmgr.RegisterComboAttackNew(chr.MOTION_MODE_DUALHAND_SWORD, COMBO_TYPE_2, COMBO_INDEX_5, chr.MOTION_COMBO_ATTACK_7)
	## Combo Type 3
	chrmgr.ReserveComboAttackNew(chr.MOTION_MODE_DUALHAND_SWORD, COMBO_TYPE_3, 6)
	chrmgr.RegisterComboAttackNew(chr.MOTION_MODE_DUALHAND_SWORD, COMBO_TYPE_3, COMBO_INDEX_1, chr.MOTION_COMBO_ATTACK_1)
	chrmgr.RegisterComboAttackNew(chr.MOTION_MODE_DUALHAND_SWORD, COMBO_TYPE_3, COMBO_INDEX_2, chr.MOTION_COMBO_ATTACK_2)
	chrmgr.RegisterComboAttackNew(chr.MOTION_MODE_DUALHAND_SWORD, COMBO_TYPE_3, COMBO_INDEX_3, chr.MOTION_COMBO_ATTACK_3)
	chrmgr.RegisterComboAttackNew(chr.MOTION_MODE_DUALHAND_SWORD, COMBO_TYPE_3, COMBO_INDEX_4, chr.MOTION_COMBO_ATTACK_5)
	chrmgr.RegisterComboAttackNew(chr.MOTION_MODE_DUALHAND_SWORD, COMBO_TYPE_3, COMBO_INDEX_5, chr.MOTION_COMBO_ATTACK_6)
	chrmgr.RegisterComboAttackNew(chr.MOTION_MODE_DUALHAND_SWORD, COMBO_TYPE_3, COMBO_INDEX_6, chr.MOTION_COMBO_ATTACK_8)

	## BOW BATTLE
	chrmgr.SetPathName(path + "bow/")
	chrmgr.RegisterMotionMode(chr.MOTION_MODE_BOW)
	chrmgr.RegisterCacheMotionData(chr.MOTION_MODE_BOW, chr.MOTION_WAIT,			"wait.msa", 70)
	chrmgr.RegisterCacheMotionData(chr.MOTION_MODE_BOW, chr.MOTION_WAIT,			"wait_1.msa", 30)
	chrmgr.RegisterCacheMotionData(chr.MOTION_MODE_BOW, chr.MOTION_WALK,			"walk.msa")
	chrmgr.RegisterCacheMotionData(chr.MOTION_MODE_BOW, chr.MOTION_RUN,			"run.msa")
	chrmgr.RegisterCacheMotionData(chr.MOTION_MODE_BOW, chr.MOTION_DAMAGE,		"damage.msa", 50)
	chrmgr.RegisterCacheMotionData(chr.MOTION_MODE_BOW, chr.MOTION_DAMAGE,		"damage_1.msa", 50)
	chrmgr.RegisterCacheMotionData(chr.MOTION_MODE_BOW, chr.MOTION_DAMAGE_BACK,	"damage_2.msa", 50)
	chrmgr.RegisterCacheMotionData(chr.MOTION_MODE_BOW, chr.MOTION_DAMAGE_BACK,	"damage_3.msa", 50)
	chrmgr.RegisterCacheMotionData(chr.MOTION_MODE_BOW, chr.MOTION_COMBO_ATTACK_1,		"attack.msa")
	chrmgr.ReserveComboAttackNew(chr.MOTION_MODE_BOW, COMBO_TYPE_1, 1)
	chrmgr.RegisterComboAttackNew(chr.MOTION_MODE_BOW, COMBO_TYPE_1, COMBO_INDEX_1, chr.MOTION_COMBO_ATTACK_1)

	## FISHING
	chrmgr.SetPathName(path + "fishing/")
	chrmgr.RegisterMotionMode(chr.MOTION_MODE_FISHING)
	chrmgr.RegisterCacheMotionData(chr.MOTION_MODE_FISHING, chr.MOTION_WAIT,					"wait.msa")
	chrmgr.RegisterCacheMotionData(chr.MOTION_MODE_FISHING, chr.MOTION_WALK,					"walk.msa")
	chrmgr.RegisterCacheMotionData(chr.MOTION_MODE_FISHING, chr.MOTION_RUN,					"run.msa")
	chrmgr.RegisterCacheMotionData(chr.MOTION_MODE_FISHING, chr.MOTION_FISHING_THROW,		"throw.msa")
	chrmgr.RegisterCacheMotionData(chr.MOTION_MODE_FISHING, chr.MOTION_FISHING_WAIT,			"fishing_wait.msa")
	chrmgr.RegisterCacheMotionData(chr.MOTION_MODE_FISHING, chr.MOTION_FISHING_STOP,			"fishing_cancel.msa")
	chrmgr.RegisterCacheMotionData(chr.MOTION_MODE_FISHING, chr.MOTION_FISHING_REACT,		"fishing_react.msa")
	chrmgr.RegisterCacheMotionData(chr.MOTION_MODE_FISHING, chr.MOTION_FISHING_CATCH,		"fishing_catch.msa")
	chrmgr.RegisterCacheMotionData(chr.MOTION_MODE_FISHING, chr.MOTION_FISHING_FAIL,			"fishing_fail.msa")

	## HORSE
	chrmgr.SetPathName(path + "horse/")
	chrmgr.RegisterMotionMode(chr.MOTION_MODE_HORSE)
	chrmgr.RegisterCacheMotionData(chr.MOTION_MODE_HORSE, chr.MOTION_WAIT,				"wait.msa", 90)
	chrmgr.RegisterCacheMotionData(chr.MOTION_MODE_HORSE, chr.MOTION_WAIT,				"wait_1.msa", 9)
	chrmgr.RegisterCacheMotionData(chr.MOTION_MODE_HORSE, chr.MOTION_WAIT,				"wait_2.msa", 1)
	chrmgr.RegisterCacheMotionData(chr.MOTION_MODE_HORSE, chr.MOTION_WALK,				"walk.msa")
	chrmgr.RegisterCacheMotionData(chr.MOTION_MODE_HORSE, chr.MOTION_RUN,				"run.msa")
	chrmgr.RegisterCacheMotionData(chr.MOTION_MODE_HORSE, chr.MOTION_DAMAGE,			"damage.msa")
	chrmgr.RegisterCacheMotionData(chr.MOTION_MODE_HORSE, chr.MOTION_DAMAGE_BACK,		"damage.msa")
	chrmgr.RegisterCacheMotionData(chr.MOTION_MODE_HORSE, chr.MOTION_DEAD,				"dead.msa")
	chrmgr.RegisterCacheMotionData(chr.MOTION_MODE_HORSE, HORSE_SKILL_CHARGE, "skill_charge.msa")

	## HORSE_ONEHAND_SWORD
	chrmgr.SetPathName(path + "horse_onehand_sword/")
	chrmgr.RegisterMotionMode(chr.MOTION_MODE_HORSE_ONEHAND_SWORD)
	chrmgr.RegisterCacheMotionData(chr.MOTION_MODE_HORSE_ONEHAND_SWORD, chr.MOTION_COMBO_ATTACK_1, "combo_01.msa")
	chrmgr.RegisterCacheMotionData(chr.MOTION_MODE_HORSE_ONEHAND_SWORD, chr.MOTION_COMBO_ATTACK_2, "combo_02.msa")
	chrmgr.RegisterCacheMotionData(chr.MOTION_MODE_HORSE_ONEHAND_SWORD, chr.MOTION_COMBO_ATTACK_3, "combo_03.msa")
	chrmgr.RegisterCacheMotionData(chr.MOTION_MODE_HORSE_ONEHAND_SWORD, HORSE_SKILL_WILDATTACK, "skill_wildattack.msa")
	chrmgr.RegisterCacheMotionData(chr.MOTION_MODE_HORSE_ONEHAND_SWORD, HORSE_SKILL_SPLASH, "skill_splash.msa")
	chrmgr.ReserveComboAttackNew(chr.MOTION_MODE_HORSE_ONEHAND_SWORD, COMBO_TYPE_1, 3)
	chrmgr.RegisterComboAttackNew(chr.MOTION_MODE_HORSE_ONEHAND_SWORD, COMBO_TYPE_1, COMBO_INDEX_1, chr.MOTION_COMBO_ATTACK_1)
	chrmgr.RegisterComboAttackNew(chr.MOTION_MODE_HORSE_ONEHAND_SWORD, COMBO_TYPE_1, COMBO_INDEX_2, chr.MOTION_COMBO_ATTACK_2)
	chrmgr.RegisterComboAttackNew(chr.MOTION_MODE_HORSE_ONEHAND_SWORD, COMBO_TYPE_1, COMBO_INDEX_3, chr.MOTION_COMBO_ATTACK_3)

	## HORSE_DUALHAND_SWORD
	chrmgr.SetPathName(path + "horse_dualhand_sword/")
	chrmgr.RegisterMotionMode(chr.MOTION_MODE_HORSE_DUALHAND_SWORD)
	chrmgr.RegisterCacheMotionData(chr.MOTION_MODE_HORSE_DUALHAND_SWORD, chr.MOTION_COMBO_ATTACK_1, "combo_01.msa")
	chrmgr.RegisterCacheMotionData(chr.MOTION_MODE_HORSE_DUALHAND_SWORD, chr.MOTION_COMBO_ATTACK_2, "combo_02.msa")
	chrmgr.RegisterCacheMotionData(chr.MOTION_MODE_HORSE_DUALHAND_SWORD, chr.MOTION_COMBO_ATTACK_3, "combo_03.msa")
	chrmgr.RegisterCacheMotionData(chr.MOTION_MODE_HORSE_DUALHAND_SWORD, HORSE_SKILL_WILDATTACK, "skill_wildattack.msa")
	chrmgr.RegisterCacheMotionData(chr.MOTION_MODE_HORSE_DUALHAND_SWORD, HORSE_SKILL_SPLASH, "skill_splash.msa")
	chrmgr.ReserveComboAttackNew(chr.MOTION_MODE_HORSE_DUALHAND_SWORD, COMBO_TYPE_1, 3)
	chrmgr.RegisterComboAttackNew(chr.MOTION_MODE_HORSE_DUALHAND_SWORD, COMBO_TYPE_1, COMBO_INDEX_1, chr.MOTION_COMBO_ATTACK_1)
	chrmgr.RegisterComboAttackNew(chr.MOTION_MODE_HORSE_DUALHAND_SWORD, COMBO_TYPE_1, COMBO_INDEX_2, chr.MOTION_COMBO_ATTACK_2)
	chrmgr.RegisterComboAttackNew(chr.MOTION_MODE_HORSE_DUALHAND_SWORD, COMBO_TYPE_1, COMBO_INDEX_3, chr.MOTION_COMBO_ATTACK_3)

	## HORSE_BOW
	chrmgr.SetPathName(path + "horse_bow/")
	chrmgr.RegisterMotionMode(chr.MOTION_MODE_HORSE_BOW)
	chrmgr.RegisterCacheMotionData(chr.MOTION_MODE_HORSE_BOW, chr.MOTION_WAIT,				"wait.msa", 90)
	chrmgr.RegisterCacheMotionData(chr.MOTION_MODE_HORSE_BOW, chr.MOTION_WAIT,				"wait_1.msa", 9)
	chrmgr.RegisterCacheMotionData(chr.MOTION_MODE_HORSE_BOW, chr.MOTION_WAIT,				"wait_2.msa", 1)
	chrmgr.RegisterCacheMotionData(chr.MOTION_MODE_HORSE_BOW, chr.MOTION_RUN,				"run.msa")
	chrmgr.RegisterCacheMotionData(chr.MOTION_MODE_HORSE_BOW, chr.MOTION_DAMAGE,			"damage.msa")
	chrmgr.RegisterCacheMotionData(chr.MOTION_MODE_HORSE_BOW, chr.MOTION_DEAD,				"dead.msa")
	chrmgr.RegisterCacheMotionData(chr.MOTION_MODE_HORSE_BOW, chr.MOTION_COMBO_ATTACK_1,	"attack.msa")
	chrmgr.RegisterCacheMotionData(chr.MOTION_MODE_HORSE_BOW, HORSE_SKILL_WILDATTACK,		"skill_wildattack.msa")
	chrmgr.RegisterCacheMotionData(chr.MOTION_MODE_HORSE_BOW, HORSE_SKILL_SPLASH,			"skill_splash.msa")
	chrmgr.ReserveComboAttackNew(chr.MOTION_MODE_HORSE_BOW, COMBO_TYPE_1, 1)
	chrmgr.RegisterComboAttackNew(chr.MOTION_MODE_HORSE_BOW, COMBO_TYPE_1, COMBO_INDEX_1, chr.MOTION_COMBO_ATTACK_1)

	chrmgr.RegisterAttachingBoneName(chr.PART_WEAPON, "equip_right")
	chrmgr.RegisterAttachingBoneName(chr.PART_WEAPON_LEFT, "equip_left")

def __LoadGameSuraEx(race, path):
	## Sura
	#########################################################################################
	chrmgr.SelectRace(race)

	## GENERAL MOTION MODE
	SetGeneralMotions(chr.MOTION_MODE_GENERAL, path + "general/")
	chrmgr.RegisterCacheMotionData(chr.MOTION_MODE_GENERAL, chr.MOTION_COMBO_ATTACK_1,	"attack.msa", 50)
	chrmgr.RegisterCacheMotionData(chr.MOTION_MODE_GENERAL, chr.MOTION_COMBO_ATTACK_1,	"attack_1.msa", 50)

	chrmgr.ReserveComboAttackNew(chr.MOTION_MODE_GENERAL, COMBO_TYPE_1, 1)
	chrmgr.RegisterComboAttackNew(chr.MOTION_MODE_GENERAL, COMBO_TYPE_1, COMBO_INDEX_1, chr.MOTION_COMBO_ATTACK_1)

	## SKILL
	chrmgr.SetPathName(path + "skill/")
	# chrmgr.RegisterCacheMotionData(chr.MOTION_MODE_GENERAL, chr.MOTION_SKILL+4, "geongon.msa")

	for i in xrange(skill.SKILL_EFFECT_COUNT):
		END_STRING = ""
		if i != 0: END_STRING = "_%d" % (i+1)
		chrmgr.RegisterCacheMotionData(chr.MOTION_MODE_GENERAL, chr.MOTION_SKILL+(i*skill.SKILL_GRADEGAP)+1, "swaeryeong" + END_STRING + ".msa")
		chrmgr.RegisterCacheMotionData(chr.MOTION_MODE_GENERAL, chr.MOTION_SKILL+(i*skill.SKILL_GRADEGAP)+2, "yonggwon" + END_STRING + ".msa")
		chrmgr.RegisterCacheMotionData(chr.MOTION_MODE_GENERAL, chr.MOTION_SKILL+(i*skill.SKILL_GRADEGAP)+3, "gwigeom" + END_STRING + ".msa")
		chrmgr.RegisterCacheMotionData(chr.MOTION_MODE_GENERAL, chr.MOTION_SKILL+(i*skill.SKILL_GRADEGAP)+4, "gongpo" + END_STRING + ".msa")
		chrmgr.RegisterCacheMotionData(chr.MOTION_MODE_GENERAL, chr.MOTION_SKILL+(i*skill.SKILL_GRADEGAP)+5, "jumagap" + END_STRING + ".msa")
		chrmgr.RegisterCacheMotionData(chr.MOTION_MODE_GENERAL, chr.MOTION_SKILL+(i*skill.SKILL_GRADEGAP)+6, "pabeop" + END_STRING + ".msa")
		chrmgr.RegisterCacheMotionData(chr.MOTION_MODE_GENERAL, chr.MOTION_SKILL+(i*skill.SKILL_GRADEGAP)+16, "maryeong" + END_STRING + ".msa")
		chrmgr.RegisterCacheMotionData(chr.MOTION_MODE_GENERAL, chr.MOTION_SKILL+(i*skill.SKILL_GRADEGAP)+17, "hwayeom" + END_STRING + ".msa")
		chrmgr.RegisterCacheMotionData(chr.MOTION_MODE_GENERAL, chr.MOTION_SKILL+(i*skill.SKILL_GRADEGAP)+18, "muyeong" + END_STRING + ".msa")
		chrmgr.RegisterCacheMotionData(chr.MOTION_MODE_GENERAL, chr.MOTION_SKILL+(i*skill.SKILL_GRADEGAP)+19, "heuksin" + END_STRING + ".msa")
		chrmgr.RegisterCacheMotionData(chr.MOTION_MODE_GENERAL, chr.MOTION_SKILL+(i*skill.SKILL_GRADEGAP)+20, "tusok" + END_STRING + ".msa")
		chrmgr.RegisterCacheMotionData(chr.MOTION_MODE_GENERAL, chr.MOTION_SKILL+(i*skill.SKILL_GRADEGAP)+21, "mahwan" + END_STRING + ".msa")

	chrmgr.RegisterCacheMotionData(chr.MOTION_MODE_GENERAL, GUILD_SKILL_DRAGONBLOOD, "guild_yongsinuipi.msa")
	chrmgr.RegisterCacheMotionData(chr.MOTION_MODE_GENERAL, GUILD_SKILL_DRAGONBLESS, "guild_yongsinuichukbok.msa")
	chrmgr.RegisterCacheMotionData(chr.MOTION_MODE_GENERAL, GUILD_SKILL_BLESSARMOR, "guild_seonghwigap.msa")
	chrmgr.RegisterCacheMotionData(chr.MOTION_MODE_GENERAL, GUILD_SKILL_SPPEDUP, "guild_gasokhwa.msa")
	chrmgr.RegisterCacheMotionData(chr.MOTION_MODE_GENERAL, GUILD_SKILL_DRAGONWRATH, "guild_yongsinuibunno.msa")
	chrmgr.RegisterCacheMotionData(chr.MOTION_MODE_GENERAL, GUILD_SKILL_MAGICUP, "guild_jumunsul.msa")

	## EMOTION
	emotion.RegisterEmotionAnis(path)

	## ONEHAND_SWORD BATTLE
	chrmgr.SetPathName(path + "onehand_sword/")
	chrmgr.RegisterMotionMode(chr.MOTION_MODE_ONEHAND_SWORD)
	chrmgr.RegisterCacheMotionData(chr.MOTION_MODE_ONEHAND_SWORD, chr.MOTION_WAIT,				"wait.msa")
	chrmgr.RegisterCacheMotionData(chr.MOTION_MODE_ONEHAND_SWORD, chr.MOTION_WALK,				"walk.msa")
	chrmgr.RegisterCacheMotionData(chr.MOTION_MODE_ONEHAND_SWORD, chr.MOTION_RUN,				"run.msa")
	chrmgr.RegisterCacheMotionData(chr.MOTION_MODE_ONEHAND_SWORD, chr.MOTION_DAMAGE,			"damage.msa")
	chrmgr.RegisterCacheMotionData(chr.MOTION_MODE_ONEHAND_SWORD, chr.MOTION_DAMAGE,			"damage.msa", 50)
	chrmgr.RegisterCacheMotionData(chr.MOTION_MODE_ONEHAND_SWORD, chr.MOTION_DAMAGE,			"damage_1.msa", 50)
	chrmgr.RegisterCacheMotionData(chr.MOTION_MODE_ONEHAND_SWORD, chr.MOTION_DAMAGE_BACK,		"damage_2.msa", 50)
	chrmgr.RegisterCacheMotionData(chr.MOTION_MODE_ONEHAND_SWORD, chr.MOTION_DAMAGE_BACK,		"damage_3.msa", 50)
	chrmgr.RegisterCacheMotionData(chr.MOTION_MODE_ONEHAND_SWORD, chr.MOTION_COMBO_ATTACK_1,	"combo_01.msa")
	chrmgr.RegisterCacheMotionData(chr.MOTION_MODE_ONEHAND_SWORD, chr.MOTION_COMBO_ATTACK_2,	"combo_02.msa")
	chrmgr.RegisterCacheMotionData(chr.MOTION_MODE_ONEHAND_SWORD, chr.MOTION_COMBO_ATTACK_3,	"combo_03.msa")
	chrmgr.RegisterCacheMotionData(chr.MOTION_MODE_ONEHAND_SWORD, chr.MOTION_COMBO_ATTACK_4,	"combo_04.msa")
	chrmgr.RegisterCacheMotionData(chr.MOTION_MODE_ONEHAND_SWORD, chr.MOTION_COMBO_ATTACK_5,	"combo_05.msa")
	chrmgr.RegisterCacheMotionData(chr.MOTION_MODE_ONEHAND_SWORD, chr.MOTION_COMBO_ATTACK_6,	"combo_06.msa")
	chrmgr.RegisterCacheMotionData(chr.MOTION_MODE_ONEHAND_SWORD, chr.MOTION_COMBO_ATTACK_7,	"combo_07.msa")

	## Combo Type 1
	chrmgr.ReserveComboAttackNew(chr.MOTION_MODE_ONEHAND_SWORD, COMBO_TYPE_1, 4)
	chrmgr.RegisterComboAttackNew(chr.MOTION_MODE_ONEHAND_SWORD, COMBO_TYPE_1, COMBO_INDEX_1, chr.MOTION_COMBO_ATTACK_1)
	chrmgr.RegisterComboAttackNew(chr.MOTION_MODE_ONEHAND_SWORD, COMBO_TYPE_1, COMBO_INDEX_2, chr.MOTION_COMBO_ATTACK_2)
	chrmgr.RegisterComboAttackNew(chr.MOTION_MODE_ONEHAND_SWORD, COMBO_TYPE_1, COMBO_INDEX_3, chr.MOTION_COMBO_ATTACK_3)
	chrmgr.RegisterComboAttackNew(chr.MOTION_MODE_ONEHAND_SWORD, COMBO_TYPE_1, COMBO_INDEX_4, chr.MOTION_COMBO_ATTACK_4)
	## Combo Type 2
	chrmgr.ReserveComboAttackNew(chr.MOTION_MODE_ONEHAND_SWORD, COMBO_TYPE_2, 5)
	chrmgr.RegisterComboAttackNew(chr.MOTION_MODE_ONEHAND_SWORD, COMBO_TYPE_2, COMBO_INDEX_1, chr.MOTION_COMBO_ATTACK_1)
	chrmgr.RegisterComboAttackNew(chr.MOTION_MODE_ONEHAND_SWORD, COMBO_TYPE_2, COMBO_INDEX_2, chr.MOTION_COMBO_ATTACK_2)
	chrmgr.RegisterComboAttackNew(chr.MOTION_MODE_ONEHAND_SWORD, COMBO_TYPE_2, COMBO_INDEX_3, chr.MOTION_COMBO_ATTACK_3)
	chrmgr.RegisterComboAttackNew(chr.MOTION_MODE_ONEHAND_SWORD, COMBO_TYPE_2, COMBO_INDEX_4, chr.MOTION_COMBO_ATTACK_5)
	chrmgr.RegisterComboAttackNew(chr.MOTION_MODE_ONEHAND_SWORD, COMBO_TYPE_2, COMBO_INDEX_5, chr.MOTION_COMBO_ATTACK_7)
	## Combo Type 3
	chrmgr.ReserveComboAttackNew(chr.MOTION_MODE_ONEHAND_SWORD, COMBO_TYPE_3, 6)
	chrmgr.RegisterComboAttackNew(chr.MOTION_MODE_ONEHAND_SWORD, COMBO_TYPE_3, COMBO_INDEX_1, chr.MOTION_COMBO_ATTACK_1)
	chrmgr.RegisterComboAttackNew(chr.MOTION_MODE_ONEHAND_SWORD, COMBO_TYPE_3, COMBO_INDEX_2, chr.MOTION_COMBO_ATTACK_2)
	chrmgr.RegisterComboAttackNew(chr.MOTION_MODE_ONEHAND_SWORD, COMBO_TYPE_3, COMBO_INDEX_3, chr.MOTION_COMBO_ATTACK_3)
	chrmgr.RegisterComboAttackNew(chr.MOTION_MODE_ONEHAND_SWORD, COMBO_TYPE_3, COMBO_INDEX_4, chr.MOTION_COMBO_ATTACK_5)
	chrmgr.RegisterComboAttackNew(chr.MOTION_MODE_ONEHAND_SWORD, COMBO_TYPE_3, COMBO_INDEX_5, chr.MOTION_COMBO_ATTACK_6)
	chrmgr.RegisterComboAttackNew(chr.MOTION_MODE_ONEHAND_SWORD, COMBO_TYPE_3, COMBO_INDEX_6, chr.MOTION_COMBO_ATTACK_4)

	## FISHING
	chrmgr.SetPathName(path + "fishing/")
	chrmgr.RegisterMotionMode(chr.MOTION_MODE_FISHING)
	chrmgr.RegisterCacheMotionData(chr.MOTION_MODE_FISHING, chr.MOTION_WAIT,					"wait.msa")
	chrmgr.RegisterCacheMotionData(chr.MOTION_MODE_FISHING, chr.MOTION_WALK,					"walk.msa")
	chrmgr.RegisterCacheMotionData(chr.MOTION_MODE_FISHING, chr.MOTION_RUN,						"run.msa")
	chrmgr.RegisterCacheMotionData(chr.MOTION_MODE_FISHING, chr.MOTION_FISHING_THROW,			"throw.msa")
	chrmgr.RegisterCacheMotionData(chr.MOTION_MODE_FISHING, chr.MOTION_FISHING_WAIT,			"fishing_wait.msa")
	chrmgr.RegisterCacheMotionData(chr.MOTION_MODE_FISHING, chr.MOTION_FISHING_STOP,			"fishing_cancel.msa")
	chrmgr.RegisterCacheMotionData(chr.MOTION_MODE_FISHING, chr.MOTION_FISHING_REACT,			"fishing_react.msa")
	chrmgr.RegisterCacheMotionData(chr.MOTION_MODE_FISHING, chr.MOTION_FISHING_CATCH,			"fishing_catch.msa")
	chrmgr.RegisterCacheMotionData(chr.MOTION_MODE_FISHING, chr.MOTION_FISHING_FAIL,			"fishing_fail.msa")

	## HORSE
	chrmgr.SetPathName(path + "horse/")
	chrmgr.RegisterMotionMode(chr.MOTION_MODE_HORSE)
	chrmgr.RegisterCacheMotionData(chr.MOTION_MODE_HORSE, chr.MOTION_WAIT,				"wait.msa", 90)
	chrmgr.RegisterCacheMotionData(chr.MOTION_MODE_HORSE, chr.MOTION_WAIT,				"wait_1.msa", 9)
	chrmgr.RegisterCacheMotionData(chr.MOTION_MODE_HORSE, chr.MOTION_WAIT,				"wait_2.msa", 1)
	chrmgr.RegisterCacheMotionData(chr.MOTION_MODE_HORSE, chr.MOTION_WALK,				"walk.msa")
	chrmgr.RegisterCacheMotionData(chr.MOTION_MODE_HORSE, chr.MOTION_RUN,				"run.msa")
	chrmgr.RegisterCacheMotionData(chr.MOTION_MODE_HORSE, chr.MOTION_DAMAGE,			"damage.msa")
	chrmgr.RegisterCacheMotionData(chr.MOTION_MODE_HORSE, chr.MOTION_DAMAGE_BACK,		"damage.msa")
	chrmgr.RegisterCacheMotionData(chr.MOTION_MODE_HORSE, chr.MOTION_DEAD,				"dead.msa")
	chrmgr.RegisterCacheMotionData(chr.MOTION_MODE_HORSE, HORSE_SKILL_CHARGE,			"skill_charge.msa")
	chrmgr.RegisterCacheMotionData(chr.MOTION_MODE_HORSE, HORSE_SKILL_SPLASH,			"skill_splash.msa")

	## HORSE_ONEHAND_SWORD
	chrmgr.SetPathName(path + "horse_onehand_sword/")
	chrmgr.RegisterMotionMode(chr.MOTION_MODE_HORSE_ONEHAND_SWORD)
	chrmgr.RegisterCacheMotionData(chr.MOTION_MODE_HORSE_ONEHAND_SWORD, chr.MOTION_COMBO_ATTACK_1, "combo_01.msa")
	chrmgr.RegisterCacheMotionData(chr.MOTION_MODE_HORSE_ONEHAND_SWORD, chr.MOTION_COMBO_ATTACK_2, "combo_02.msa")
	chrmgr.RegisterCacheMotionData(chr.MOTION_MODE_HORSE_ONEHAND_SWORD, chr.MOTION_COMBO_ATTACK_3, "combo_03.msa")
	chrmgr.ReserveComboAttackNew(chr.MOTION_MODE_HORSE_ONEHAND_SWORD, COMBO_TYPE_1, 3)
	chrmgr.RegisterComboAttackNew(chr.MOTION_MODE_HORSE_ONEHAND_SWORD, COMBO_TYPE_1, COMBO_INDEX_1, chr.MOTION_COMBO_ATTACK_1)
	chrmgr.RegisterComboAttackNew(chr.MOTION_MODE_HORSE_ONEHAND_SWORD, COMBO_TYPE_1, COMBO_INDEX_2, chr.MOTION_COMBO_ATTACK_2)
	chrmgr.RegisterComboAttackNew(chr.MOTION_MODE_HORSE_ONEHAND_SWORD, COMBO_TYPE_1, COMBO_INDEX_3, chr.MOTION_COMBO_ATTACK_3)
	chrmgr.RegisterCacheMotionData(chr.MOTION_MODE_HORSE_ONEHAND_SWORD, HORSE_SKILL_WILDATTACK, "skill_wildattack.msa")

	chrmgr.RegisterAttachingBoneName(chr.PART_WEAPON, "equip_right")

def __LoadGameShamanEx(race, path):
	## Shaman
	#########################################################################################
	chrmgr.SelectRace(race)

	## GENERAL MOTION MODE
	SetGeneralMotions(chr.MOTION_MODE_GENERAL, path + "general/")
	chrmgr.RegisterCacheMotionData(chr.MOTION_MODE_GENERAL, chr.MOTION_COMBO_ATTACK_1,	"attack.msa", 50)
	chrmgr.RegisterCacheMotionData(chr.MOTION_MODE_GENERAL, chr.MOTION_COMBO_ATTACK_1,	"attack_1.msa", 50)

	chrmgr.ReserveComboAttackNew(chr.MOTION_MODE_GENERAL, COMBO_TYPE_1, 1)
	chrmgr.RegisterComboAttackNew(chr.MOTION_MODE_GENERAL, COMBO_TYPE_1, COMBO_INDEX_1, chr.MOTION_COMBO_ATTACK_1)

	## EMOTION
	emotion.RegisterEmotionAnis(path)

	## Fan
	chrmgr.SetPathName(path + "fan/")
	chrmgr.RegisterMotionMode(chr.MOTION_MODE_FAN)
	chrmgr.RegisterCacheMotionData(chr.MOTION_MODE_FAN, chr.MOTION_WAIT,			"wait.msa")
	chrmgr.RegisterCacheMotionData(chr.MOTION_MODE_FAN, chr.MOTION_WALK,			"walk.msa")
	chrmgr.RegisterCacheMotionData(chr.MOTION_MODE_FAN, chr.MOTION_RUN,				"run.msa")
	chrmgr.RegisterCacheMotionData(chr.MOTION_MODE_FAN, chr.MOTION_DAMAGE,			"damage.msa", 50)
	chrmgr.RegisterCacheMotionData(chr.MOTION_MODE_FAN, chr.MOTION_DAMAGE,			"damage_1.msa", 50)
	chrmgr.RegisterCacheMotionData(chr.MOTION_MODE_FAN, chr.MOTION_DAMAGE_BACK,		"damage_2.msa", 50)
	chrmgr.RegisterCacheMotionData(chr.MOTION_MODE_FAN, chr.MOTION_DAMAGE_BACK,		"damage_3.msa", 50)
	chrmgr.RegisterCacheMotionData(chr.MOTION_MODE_FAN, chr.MOTION_COMBO_ATTACK_1,	"combo_01.msa")
	chrmgr.RegisterCacheMotionData(chr.MOTION_MODE_FAN, chr.MOTION_COMBO_ATTACK_2,	"combo_02.msa")
	chrmgr.RegisterCacheMotionData(chr.MOTION_MODE_FAN, chr.MOTION_COMBO_ATTACK_3,	"combo_03.msa")
	chrmgr.RegisterCacheMotionData(chr.MOTION_MODE_FAN, chr.MOTION_COMBO_ATTACK_4,	"combo_04.msa")
	chrmgr.RegisterCacheMotionData(chr.MOTION_MODE_FAN, chr.MOTION_COMBO_ATTACK_5,	"combo_05.msa")
	chrmgr.RegisterCacheMotionData(chr.MOTION_MODE_FAN, chr.MOTION_COMBO_ATTACK_6,	"combo_06.msa")
	chrmgr.RegisterCacheMotionData(chr.MOTION_MODE_FAN, chr.MOTION_COMBO_ATTACK_7,	"combo_07.msa")

	## Combo Type 1
	chrmgr.ReserveComboAttackNew(chr.MOTION_MODE_FAN, COMBO_TYPE_1, 4)
	chrmgr.RegisterComboAttackNew(chr.MOTION_MODE_FAN, COMBO_TYPE_1, COMBO_INDEX_1, chr.MOTION_COMBO_ATTACK_1)
	chrmgr.RegisterComboAttackNew(chr.MOTION_MODE_FAN, COMBO_TYPE_1, COMBO_INDEX_2, chr.MOTION_COMBO_ATTACK_2)
	chrmgr.RegisterComboAttackNew(chr.MOTION_MODE_FAN, COMBO_TYPE_1, COMBO_INDEX_3, chr.MOTION_COMBO_ATTACK_3)
	chrmgr.RegisterComboAttackNew(chr.MOTION_MODE_FAN, COMBO_TYPE_1, COMBO_INDEX_4, chr.MOTION_COMBO_ATTACK_4)
	## Combo Type 2
	chrmgr.ReserveComboAttackNew(chr.MOTION_MODE_FAN, COMBO_TYPE_2, 5)
	chrmgr.RegisterComboAttackNew(chr.MOTION_MODE_FAN, COMBO_TYPE_2, COMBO_INDEX_1, chr.MOTION_COMBO_ATTACK_1)
	chrmgr.RegisterComboAttackNew(chr.MOTION_MODE_FAN, COMBO_TYPE_2, COMBO_INDEX_2, chr.MOTION_COMBO_ATTACK_2)
	chrmgr.RegisterComboAttackNew(chr.MOTION_MODE_FAN, COMBO_TYPE_2, COMBO_INDEX_3, chr.MOTION_COMBO_ATTACK_3)
	chrmgr.RegisterComboAttackNew(chr.MOTION_MODE_FAN, COMBO_TYPE_2, COMBO_INDEX_4, chr.MOTION_COMBO_ATTACK_5)
	chrmgr.RegisterComboAttackNew(chr.MOTION_MODE_FAN, COMBO_TYPE_2, COMBO_INDEX_5, chr.MOTION_COMBO_ATTACK_7)
	## Combo Type 3
	chrmgr.ReserveComboAttackNew(chr.MOTION_MODE_FAN, COMBO_TYPE_3, 6)
	chrmgr.RegisterComboAttackNew(chr.MOTION_MODE_FAN, COMBO_TYPE_3, COMBO_INDEX_1, chr.MOTION_COMBO_ATTACK_1)
	chrmgr.RegisterComboAttackNew(chr.MOTION_MODE_FAN, COMBO_TYPE_3, COMBO_INDEX_2, chr.MOTION_COMBO_ATTACK_2)
	chrmgr.RegisterComboAttackNew(chr.MOTION_MODE_FAN, COMBO_TYPE_3, COMBO_INDEX_3, chr.MOTION_COMBO_ATTACK_3)
	chrmgr.RegisterComboAttackNew(chr.MOTION_MODE_FAN, COMBO_TYPE_3, COMBO_INDEX_4, chr.MOTION_COMBO_ATTACK_5)
	chrmgr.RegisterComboAttackNew(chr.MOTION_MODE_FAN, COMBO_TYPE_3, COMBO_INDEX_5, chr.MOTION_COMBO_ATTACK_6)
	chrmgr.RegisterComboAttackNew(chr.MOTION_MODE_FAN, COMBO_TYPE_3, COMBO_INDEX_6, chr.MOTION_COMBO_ATTACK_4)

	## Bell
	chrmgr.SetPathName(path + "Bell/")
	chrmgr.RegisterMotionMode(chr.MOTION_MODE_BELL)
	chrmgr.RegisterCacheMotionData(chr.MOTION_MODE_BELL, chr.MOTION_WAIT,			"wait.msa")
	chrmgr.RegisterCacheMotionData(chr.MOTION_MODE_BELL, chr.MOTION_WALK,			"walk.msa")
	chrmgr.RegisterCacheMotionData(chr.MOTION_MODE_BELL, chr.MOTION_RUN,			"run.msa")
	chrmgr.RegisterCacheMotionData(chr.MOTION_MODE_BELL, chr.MOTION_DAMAGE,			"damage.msa", 50)
	chrmgr.RegisterCacheMotionData(chr.MOTION_MODE_BELL, chr.MOTION_DAMAGE,			"damage_1.msa", 50)
	chrmgr.RegisterCacheMotionData(chr.MOTION_MODE_BELL, chr.MOTION_DAMAGE_BACK,	"damage_2.msa", 50)
	chrmgr.RegisterCacheMotionData(chr.MOTION_MODE_BELL, chr.MOTION_DAMAGE_BACK,	"damage_3.msa", 50)
	chrmgr.RegisterCacheMotionData(chr.MOTION_MODE_BELL, chr.MOTION_COMBO_ATTACK_1,	"combo_01.msa")
	chrmgr.RegisterCacheMotionData(chr.MOTION_MODE_BELL, chr.MOTION_COMBO_ATTACK_2,	"combo_02.msa")
	chrmgr.RegisterCacheMotionData(chr.MOTION_MODE_BELL, chr.MOTION_COMBO_ATTACK_3,	"combo_03.msa")
	chrmgr.RegisterCacheMotionData(chr.MOTION_MODE_BELL, chr.MOTION_COMBO_ATTACK_4,	"combo_04.msa")
	chrmgr.RegisterCacheMotionData(chr.MOTION_MODE_BELL, chr.MOTION_COMBO_ATTACK_5,	"combo_05.msa")
	chrmgr.RegisterCacheMotionData(chr.MOTION_MODE_BELL, chr.MOTION_COMBO_ATTACK_6,	"combo_06.msa")
	chrmgr.RegisterCacheMotionData(chr.MOTION_MODE_BELL, chr.MOTION_COMBO_ATTACK_7,	"combo_07.msa")

	## Combo Type 1
	chrmgr.ReserveComboAttackNew(chr.MOTION_MODE_BELL, COMBO_TYPE_1, 4)
	chrmgr.RegisterComboAttackNew(chr.MOTION_MODE_BELL, COMBO_TYPE_1, COMBO_INDEX_1, chr.MOTION_COMBO_ATTACK_1)
	chrmgr.RegisterComboAttackNew(chr.MOTION_MODE_BELL, COMBO_TYPE_1, COMBO_INDEX_2, chr.MOTION_COMBO_ATTACK_2)
	chrmgr.RegisterComboAttackNew(chr.MOTION_MODE_BELL, COMBO_TYPE_1, COMBO_INDEX_3, chr.MOTION_COMBO_ATTACK_3)
	chrmgr.RegisterComboAttackNew(chr.MOTION_MODE_BELL, COMBO_TYPE_1, COMBO_INDEX_4, chr.MOTION_COMBO_ATTACK_4)
	## Combo Type 2
	chrmgr.ReserveComboAttackNew(chr.MOTION_MODE_BELL, COMBO_TYPE_2, 5)
	chrmgr.RegisterComboAttackNew(chr.MOTION_MODE_BELL, COMBO_TYPE_2, COMBO_INDEX_1, chr.MOTION_COMBO_ATTACK_1)
	chrmgr.RegisterComboAttackNew(chr.MOTION_MODE_BELL, COMBO_TYPE_2, COMBO_INDEX_2, chr.MOTION_COMBO_ATTACK_2)
	chrmgr.RegisterComboAttackNew(chr.MOTION_MODE_BELL, COMBO_TYPE_2, COMBO_INDEX_3, chr.MOTION_COMBO_ATTACK_3)
	chrmgr.RegisterComboAttackNew(chr.MOTION_MODE_BELL, COMBO_TYPE_2, COMBO_INDEX_4, chr.MOTION_COMBO_ATTACK_5)
	chrmgr.RegisterComboAttackNew(chr.MOTION_MODE_BELL, COMBO_TYPE_2, COMBO_INDEX_5, chr.MOTION_COMBO_ATTACK_7)
	## Combo Type 3
	chrmgr.ReserveComboAttackNew(chr.MOTION_MODE_BELL, COMBO_TYPE_3, 6)
	chrmgr.RegisterComboAttackNew(chr.MOTION_MODE_BELL, COMBO_TYPE_3, COMBO_INDEX_1, chr.MOTION_COMBO_ATTACK_1)
	chrmgr.RegisterComboAttackNew(chr.MOTION_MODE_BELL, COMBO_TYPE_3, COMBO_INDEX_2, chr.MOTION_COMBO_ATTACK_2)
	chrmgr.RegisterComboAttackNew(chr.MOTION_MODE_BELL, COMBO_TYPE_3, COMBO_INDEX_3, chr.MOTION_COMBO_ATTACK_3)
	chrmgr.RegisterComboAttackNew(chr.MOTION_MODE_BELL, COMBO_TYPE_3, COMBO_INDEX_4, chr.MOTION_COMBO_ATTACK_5)
	chrmgr.RegisterComboAttackNew(chr.MOTION_MODE_BELL, COMBO_TYPE_3, COMBO_INDEX_5, chr.MOTION_COMBO_ATTACK_6)
	chrmgr.RegisterComboAttackNew(chr.MOTION_MODE_BELL, COMBO_TYPE_3, COMBO_INDEX_6, chr.MOTION_COMBO_ATTACK_4)

	## SKILL
	chrmgr.SetPathName(path + "skill/")
	chrmgr.RegisterCacheMotionData(chr.MOTION_MODE_GENERAL, chr.MOTION_SKILL+1,		"bipabu.msa")
	chrmgr.RegisterCacheMotionData(chr.MOTION_MODE_GENERAL, chr.MOTION_SKILL+2,		"yongpa.msa")
	chrmgr.RegisterCacheMotionData(chr.MOTION_MODE_GENERAL, chr.MOTION_SKILL+3,		"paeryong.msa")
	chrmgr.RegisterCacheMotionData(chr.MOTION_MODE_GENERAL, chr.MOTION_SKILL+4,		"hosin_target.msa")
	chrmgr.RegisterCacheMotionData(chr.MOTION_MODE_GENERAL, chr.MOTION_SKILL+5,	"boho_target.msa")
	chrmgr.RegisterCacheMotionData(chr.MOTION_MODE_GENERAL, chr.MOTION_SKILL+6,	"gicheon_target.msa")
	chrmgr.RegisterCacheMotionData(chr.MOTION_MODE_GENERAL, chr.MOTION_SKILL+16,	"noejeon.msa")
	chrmgr.RegisterCacheMotionData(chr.MOTION_MODE_GENERAL, chr.MOTION_SKILL+17,	"byeorak.msa")
	chrmgr.RegisterCacheMotionData(chr.MOTION_MODE_GENERAL, chr.MOTION_SKILL+18,		"pokroe.msa")
	chrmgr.RegisterCacheMotionData(chr.MOTION_MODE_GENERAL, chr.MOTION_SKILL+19,		"jeongeop_target.msa")
	chrmgr.RegisterCacheMotionData(chr.MOTION_MODE_GENERAL, chr.MOTION_SKILL+20,		"kwaesok_target.msa")
	chrmgr.RegisterCacheMotionData(chr.MOTION_MODE_GENERAL, chr.MOTION_SKILL+21,	"jeungryeok_target.msa")
	#chrmgr.RegisterCacheMotionData(chr.MOTION_MODE_GENERAL, chr.MOTION_SKILL+10,	"budong.msa")

	START_INDEX = 0
	#skill.SKILL_EFFECT_COUNT 까지//
	for i in (1, 2, 3, 4):
		END_STRING = ""
		if i != 0: END_STRING = "_%d" % (i+1)
		chrmgr.RegisterCacheMotionData(chr.MOTION_MODE_GENERAL, chr.MOTION_SKILL+(i*skill.SKILL_GRADEGAP)+1,	"bipabu" + END_STRING + ".msa")
		chrmgr.RegisterCacheMotionData(chr.MOTION_MODE_GENERAL, chr.MOTION_SKILL+(i*skill.SKILL_GRADEGAP)+2,	"yongpa" + END_STRING + ".msa")
		chrmgr.RegisterCacheMotionData(chr.MOTION_MODE_GENERAL, chr.MOTION_SKILL+(i*skill.SKILL_GRADEGAP)+3,	"paeryong" + END_STRING + ".msa")
		chrmgr.RegisterCacheMotionData(chr.MOTION_MODE_GENERAL, chr.MOTION_SKILL+(i*skill.SKILL_GRADEGAP)+4,	"hosin" + END_STRING + ".msa")
		chrmgr.RegisterCacheMotionData(chr.MOTION_MODE_GENERAL, chr.MOTION_SKILL+(i*skill.SKILL_GRADEGAP)+5,	"boho" + END_STRING + ".msa")
		chrmgr.RegisterCacheMotionData(chr.MOTION_MODE_GENERAL, chr.MOTION_SKILL+(i*skill.SKILL_GRADEGAP)+6,	"gicheon" + END_STRING + ".msa")
		chrmgr.RegisterCacheMotionData(chr.MOTION_MODE_GENERAL, chr.MOTION_SKILL+(i*skill.SKILL_GRADEGAP)+16,	"noejeon" + END_STRING + ".msa")
		chrmgr.RegisterCacheMotionData(chr.MOTION_MODE_GENERAL, chr.MOTION_SKILL+(i*skill.SKILL_GRADEGAP)+17,	"byeorak" + END_STRING + ".msa")
		chrmgr.RegisterCacheMotionData(chr.MOTION_MODE_GENERAL, chr.MOTION_SKILL+(i*skill.SKILL_GRADEGAP)+18,	"pokroe" + END_STRING + ".msa")
		chrmgr.RegisterCacheMotionData(chr.MOTION_MODE_GENERAL, chr.MOTION_SKILL+(i*skill.SKILL_GRADEGAP)+19,	"jeongeop" + END_STRING + ".msa")
		chrmgr.RegisterCacheMotionData(chr.MOTION_MODE_GENERAL, chr.MOTION_SKILL+(i*skill.SKILL_GRADEGAP)+20,	"kwaesok" + END_STRING + ".msa")
		chrmgr.RegisterCacheMotionData(chr.MOTION_MODE_GENERAL, chr.MOTION_SKILL+(i*skill.SKILL_GRADEGAP)+21,	"jeungryeok" + END_STRING + ".msa")
		#chrmgr.RegisterCacheMotionData(chr.MOTION_MODE_GENERAL, chr.MOTION_SKILL+(i*skill.SKILL_GRADEGAP)+10,	"budong" + END_STRING + ".msa")

	chrmgr.RegisterCacheMotionData(chr.MOTION_MODE_GENERAL, GUILD_SKILL_DRAGONBLOOD, "guild_yongsinuipi.msa")
	chrmgr.RegisterCacheMotionData(chr.MOTION_MODE_GENERAL, GUILD_SKILL_DRAGONBLESS, "guild_yongsinuichukbok.msa")
	chrmgr.RegisterCacheMotionData(chr.MOTION_MODE_GENERAL, GUILD_SKILL_BLESSARMOR, "guild_seonghwigap.msa")
	chrmgr.RegisterCacheMotionData(chr.MOTION_MODE_GENERAL, GUILD_SKILL_SPPEDUP, "guild_gasokhwa.msa")
	chrmgr.RegisterCacheMotionData(chr.MOTION_MODE_GENERAL, GUILD_SKILL_DRAGONWRATH, "guild_yongsinuibunno.msa")
	chrmgr.RegisterCacheMotionData(chr.MOTION_MODE_GENERAL, GUILD_SKILL_MAGICUP, "guild_jumunsul.msa")

	## FISHING
	chrmgr.SetPathName(path + "fishing/")
	chrmgr.RegisterMotionMode(chr.MOTION_MODE_FISHING)
	chrmgr.RegisterCacheMotionData(chr.MOTION_MODE_FISHING, chr.MOTION_WAIT,				"wait.msa")
	chrmgr.RegisterCacheMotionData(chr.MOTION_MODE_FISHING, chr.MOTION_WALK,				"walk.msa")
	chrmgr.RegisterCacheMotionData(chr.MOTION_MODE_FISHING, chr.MOTION_RUN,					"run.msa")
	chrmgr.RegisterCacheMotionData(chr.MOTION_MODE_FISHING, chr.MOTION_FISHING_THROW,		"throw.msa")
	chrmgr.RegisterCacheMotionData(chr.MOTION_MODE_FISHING, chr.MOTION_FISHING_WAIT,		"fishing_wait.msa")
	chrmgr.RegisterCacheMotionData(chr.MOTION_MODE_FISHING, chr.MOTION_FISHING_STOP,		"fishing_cancel.msa")
	chrmgr.RegisterCacheMotionData(chr.MOTION_MODE_FISHING, chr.MOTION_FISHING_REACT,		"fishing_react.msa")
	chrmgr.RegisterCacheMotionData(chr.MOTION_MODE_FISHING, chr.MOTION_FISHING_CATCH,		"fishing_catch.msa")
	chrmgr.RegisterCacheMotionData(chr.MOTION_MODE_FISHING, chr.MOTION_FISHING_FAIL,		"fishing_fail.msa")

	## HORSE
	chrmgr.SetPathName(path + "horse/")
	chrmgr.RegisterMotionMode(chr.MOTION_MODE_HORSE)
	chrmgr.RegisterCacheMotionData(chr.MOTION_MODE_HORSE, chr.MOTION_WAIT,				"wait.msa", 90)
	chrmgr.RegisterCacheMotionData(chr.MOTION_MODE_HORSE, chr.MOTION_WAIT,				"wait_1.msa", 9)
	chrmgr.RegisterCacheMotionData(chr.MOTION_MODE_HORSE, chr.MOTION_WAIT,				"wait_2.msa", 1)
	chrmgr.RegisterCacheMotionData(chr.MOTION_MODE_HORSE, chr.MOTION_WALK,				"walk.msa")
	chrmgr.RegisterCacheMotionData(chr.MOTION_MODE_HORSE, chr.MOTION_RUN,				"run.msa")
	chrmgr.RegisterCacheMotionData(chr.MOTION_MODE_HORSE, chr.MOTION_DAMAGE,			"damage.msa")
	chrmgr.RegisterCacheMotionData(chr.MOTION_MODE_HORSE, chr.MOTION_DAMAGE_BACK,		"damage.msa")
	chrmgr.RegisterCacheMotionData(chr.MOTION_MODE_HORSE, chr.MOTION_DEAD,				"dead.msa")
	chrmgr.RegisterCacheMotionData(chr.MOTION_MODE_HORSE, HORSE_SKILL_CHARGE,			"skill_charge.msa")
	chrmgr.RegisterCacheMotionData(chr.MOTION_MODE_HORSE, HORSE_SKILL_SPLASH,			"skill_splash.msa")

	## HORSE_FAN
	chrmgr.SetPathName(path + "horse_fan/")
	chrmgr.RegisterMotionMode(chr.MOTION_MODE_HORSE_FAN)
	chrmgr.RegisterCacheMotionData(chr.MOTION_MODE_HORSE_FAN, chr.MOTION_COMBO_ATTACK_1, "combo_01.msa")
	chrmgr.RegisterCacheMotionData(chr.MOTION_MODE_HORSE_FAN, chr.MOTION_COMBO_ATTACK_2, "combo_02.msa")
	chrmgr.RegisterCacheMotionData(chr.MOTION_MODE_HORSE_FAN, chr.MOTION_COMBO_ATTACK_3, "combo_03.msa")
	chrmgr.ReserveComboAttackNew(chr.MOTION_MODE_HORSE_FAN, COMBO_TYPE_1, 3)
	chrmgr.RegisterComboAttackNew(chr.MOTION_MODE_HORSE_FAN, COMBO_TYPE_1, COMBO_INDEX_1, chr.MOTION_COMBO_ATTACK_1)
	chrmgr.RegisterComboAttackNew(chr.MOTION_MODE_HORSE_FAN, COMBO_TYPE_1, COMBO_INDEX_2, chr.MOTION_COMBO_ATTACK_2)
	chrmgr.RegisterComboAttackNew(chr.MOTION_MODE_HORSE_FAN, COMBO_TYPE_1, COMBO_INDEX_3, chr.MOTION_COMBO_ATTACK_3)
	chrmgr.RegisterCacheMotionData(chr.MOTION_MODE_HORSE_FAN, HORSE_SKILL_WILDATTACK, "skill_wildattack.msa")

	## HORSE_BELL
	chrmgr.SetPathName(path + "horse_bell/")
	chrmgr.RegisterMotionMode(chr.MOTION_MODE_HORSE_BELL)
	chrmgr.RegisterCacheMotionData(chr.MOTION_MODE_HORSE_BELL, chr.MOTION_COMBO_ATTACK_1, "combo_01.msa")
	chrmgr.RegisterCacheMotionData(chr.MOTION_MODE_HORSE_BELL, chr.MOTION_COMBO_ATTACK_2, "combo_02.msa")
	chrmgr.RegisterCacheMotionData(chr.MOTION_MODE_HORSE_BELL, chr.MOTION_COMBO_ATTACK_3, "combo_03.msa")
	chrmgr.ReserveComboAttackNew(chr.MOTION_MODE_HORSE_BELL, COMBO_TYPE_1, 3)
	chrmgr.RegisterComboAttackNew(chr.MOTION_MODE_HORSE_BELL, COMBO_TYPE_1, COMBO_INDEX_1, chr.MOTION_COMBO_ATTACK_1)
	chrmgr.RegisterComboAttackNew(chr.MOTION_MODE_HORSE_BELL, COMBO_TYPE_1, COMBO_INDEX_2, chr.MOTION_COMBO_ATTACK_2)
	chrmgr.RegisterComboAttackNew(chr.MOTION_MODE_HORSE_BELL, COMBO_TYPE_1, COMBO_INDEX_3, chr.MOTION_COMBO_ATTACK_3)
	chrmgr.RegisterCacheMotionData(chr.MOTION_MODE_HORSE_BELL, HORSE_SKILL_WILDATTACK, "skill_wildattack.msa")

	chrmgr.RegisterAttachingBoneName(chr.PART_WEAPON, "equip_right")
	chrmgr.RegisterAttachingBoneName(chr.PART_WEAPON_LEFT, "equip_left")

# def __LoadGameWolfmanEx(race, path):
	# Warrior
	########################################################################################
	# chrmgr.SelectRace(RACE_WOLFMAN_M)

	# GENERAL MODE
	# chrmgr.SetPathName(path + "general/")
	# chrmgr.RegisterMotionMode(chr.MOTION_MODE_GENERAL)
	# chrmgr.RegisterCacheMotionData(chr.MOTION_MODE_GENERAL,		chr.MOTION_WAIT,				"wait.msa")
	# chrmgr.RegisterCacheMotionData(chr.MOTION_MODE_GENERAL,		chr.MOTION_WALK,				"walk.msa")
	# chrmgr.RegisterCacheMotionData(chr.MOTION_MODE_GENERAL,		chr.MOTION_RUN,					"run.msa")
	# chrmgr.RegisterCacheMotionData(chr.MOTION_MODE_GENERAL,		chr.MOTION_DAMAGE,				"front_damage.msa", 50)
	# chrmgr.RegisterCacheMotionData(chr.MOTION_MODE_GENERAL,		chr.MOTION_DAMAGE,				"front_damage1.msa", 50)
	# chrmgr.RegisterCacheMotionData(chr.MOTION_MODE_GENERAL,		chr.MOTION_DAMAGE_BACK,			"back_damage.msa", 50)
	# chrmgr.RegisterCacheMotionData(chr.MOTION_MODE_GENERAL,		chr.MOTION_DAMAGE_BACK,			"back_damage1.msa", 50)
	# chrmgr.RegisterCacheMotionData(chr.MOTION_MODE_GENERAL,		chr.MOTION_DAMAGE_FLYING,		"front_damage_flying.msa")
	# chrmgr.RegisterCacheMotionData(chr.MOTION_MODE_GENERAL,		chr.MOTION_STAND_UP,			"front_falling_standup.msa")
	# chrmgr.RegisterCacheMotionData(chr.MOTION_MODE_GENERAL,		chr.MOTION_DAMAGE_FLYING_BACK,	"back_damage_flying.msa")
	# chrmgr.RegisterCacheMotionData(chr.MOTION_MODE_GENERAL,		chr.MOTION_STAND_UP_BACK,		"back_falling_standup.msa")
	# chrmgr.RegisterCacheMotionData(chr.MOTION_MODE_GENERAL,		chr.MOTION_DEAD,				"dead.msa")
	# chrmgr.RegisterCacheMotionData(chr.MOTION_MODE_GENERAL,		chr.MOTION_DIG,					"dig.msa")
	
	# chrmgr.SetMotionRandomWeight(chr.MOTION_MODE_GENERAL, chr.MOTION_WAIT, 0, 70)
	# chrmgr.RegisterCacheMotionData(chr.MOTION_MODE_GENERAL, chr.MOTION_WAIT, "wait1.msa", 30)
	# chrmgr.RegisterCacheMotionData(chr.MOTION_MODE_GENERAL, chr.MOTION_COMBO_ATTACK_1, "attack1.msa", 50)
	# chrmgr.RegisterCacheMotionData(chr.MOTION_MODE_GENERAL, chr.MOTION_COMBO_ATTACK_1, "attack2.msa", 50)

	# Combo Type 1
	# chrmgr.ReserveComboAttackNew(chr.MOTION_MODE_GENERAL, COMBO_TYPE_1, 1)
	# chrmgr.RegisterComboAttackNew(chr.MOTION_MODE_GENERAL, COMBO_TYPE_1, COMBO_INDEX_1, chr.MOTION_COMBO_ATTACK_1)
	
	# SKILL
	# chrmgr.SetPathName(path + "skill/")
	# for i in range(skill.SKILL_EFFECT_COUNT):
		# END_STRING = ""
		# if i != 0: END_STRING = "_%d" % (i)
		# chrmgr.RegisterCacheMotionData(chr.MOTION_MODE_GENERAL, chr.MOTION_SKILL+(i*skill.SKILL_GRADEGAP)+1, "split_slash" + END_STRING + ".msa")
		# chrmgr.RegisterCacheMotionData(chr.MOTION_MODE_GENERAL, chr.MOTION_SKILL+(i*skill.SKILL_GRADEGAP)+2, "wind_death" + END_STRING + ".msa")
		# chrmgr.RegisterCacheMotionData(chr.MOTION_MODE_GENERAL, chr.MOTION_SKILL+(i*skill.SKILL_GRADEGAP)+3, "reef_attack" + END_STRING + ".msa")
		# chrmgr.RegisterCacheMotionData(chr.MOTION_MODE_GENERAL, chr.MOTION_SKILL+(i*skill.SKILL_GRADEGAP)+4, "wreckage" + END_STRING + ".msa")
		# chrmgr.RegisterCacheMotionData(chr.MOTION_MODE_GENERAL, chr.MOTION_SKILL+(i*skill.SKILL_GRADEGAP)+5, "red_possession" + END_STRING + ".msa")
		# chrmgr.RegisterCacheMotionData(chr.MOTION_MODE_GENERAL, chr.MOTION_SKILL+(i*skill.SKILL_GRADEGAP)+6, "blue_possession" + END_STRING + ".msa")

	# chrmgr.RegisterCacheMotionData(chr.MOTION_MODE_GENERAL, GUILD_SKILL_DRAGONBLOOD, "guild_yongsinuipi.msa")
	# chrmgr.RegisterCacheMotionData(chr.MOTION_MODE_GENERAL, GUILD_SKILL_DRAGONBLESS, "guild_yongsinuichukbok.msa")
	# chrmgr.RegisterCacheMotionData(chr.MOTION_MODE_GENERAL, GUILD_SKILL_BLESSARMOR, "guild_seonghwigap.msa")
	# chrmgr.RegisterCacheMotionData(chr.MOTION_MODE_GENERAL, GUILD_SKILL_SPPEDUP, "guild_gasokhwa.msa")
	# chrmgr.RegisterCacheMotionData(chr.MOTION_MODE_GENERAL, GUILD_SKILL_DRAGONWRATH, "guild_yongsinuibunno.msa")
	# chrmgr.RegisterCacheMotionData(chr.MOTION_MODE_GENERAL, GUILD_SKILL_MAGICUP, "guild_jumunsul.msa")

	# MOTION
	# emotion.RegisterEmotionAnis(path)

	# CLAW BATTLE
	# chrmgr.SetPathName(path + "claw/")
	# chrmgr.RegisterMotionMode(chr.MOTION_MODE_CLAW)
	# chrmgr.RegisterCacheMotionData(chr.MOTION_MODE_CLAW, chr.MOTION_WAIT,				"wait.msa", 70)
	# chrmgr.RegisterCacheMotionData(chr.MOTION_MODE_CLAW, chr.MOTION_WAIT,				"wait1.msa", 30)
	# chrmgr.RegisterCacheMotionData(chr.MOTION_MODE_CLAW, chr.MOTION_WALK,				"walk.msa")
	# chrmgr.RegisterCacheMotionData(chr.MOTION_MODE_CLAW, chr.MOTION_RUN,				"run.msa")
	# chrmgr.RegisterCacheMotionData(chr.MOTION_MODE_CLAW, chr.MOTION_DAMAGE,			"front_damage.msa", 50)
	# chrmgr.RegisterCacheMotionData(chr.MOTION_MODE_CLAW, chr.MOTION_DAMAGE,			"front_damage1.msa", 50)
	# chrmgr.RegisterCacheMotionData(chr.MOTION_MODE_CLAW, chr.MOTION_DAMAGE_BACK,		"back_damage.msa", 50)
	# chrmgr.RegisterCacheMotionData(chr.MOTION_MODE_CLAW, chr.MOTION_DAMAGE_BACK,		"back_damage1.msa", 50)


	# chrmgr.RegisterCacheMotionData(chr.MOTION_MODE_CLAW, chr.MOTION_COMBO_ATTACK_1,	"combo_01.msa")
	# chrmgr.RegisterCacheMotionData(chr.MOTION_MODE_CLAW, chr.MOTION_COMBO_ATTACK_2,	"combo_02.msa")
	# chrmgr.RegisterCacheMotionData(chr.MOTION_MODE_CLAW, chr.MOTION_COMBO_ATTACK_3,	"combo_03.msa")
	# chrmgr.RegisterCacheMotionData(chr.MOTION_MODE_CLAW, chr.MOTION_COMBO_ATTACK_4,	"combo_04.msa")
	# chrmgr.RegisterCacheMotionData(chr.MOTION_MODE_CLAW, chr.MOTION_COMBO_ATTACK_5,	"combo_05.msa")
	# chrmgr.RegisterCacheMotionData(chr.MOTION_MODE_CLAW, chr.MOTION_COMBO_ATTACK_6,	"combo_06.msa")
	# chrmgr.RegisterCacheMotionData(chr.MOTION_MODE_CLAW, chr.MOTION_COMBO_ATTACK_7,	"combo_07.msa")

	# Combo Type 1
	# chrmgr.ReserveComboAttackNew(chr.MOTION_MODE_CLAW, COMBO_TYPE_1, 4)
	# chrmgr.RegisterComboAttackNew(chr.MOTION_MODE_CLAW, COMBO_TYPE_1, COMBO_INDEX_1, chr.MOTION_COMBO_ATTACK_1)
	# chrmgr.RegisterComboAttackNew(chr.MOTION_MODE_CLAW, COMBO_TYPE_1, COMBO_INDEX_2, chr.MOTION_COMBO_ATTACK_2)
	# chrmgr.RegisterComboAttackNew(chr.MOTION_MODE_CLAW, COMBO_TYPE_1, COMBO_INDEX_3, chr.MOTION_COMBO_ATTACK_3)
	# chrmgr.RegisterComboAttackNew(chr.MOTION_MODE_CLAW, COMBO_TYPE_1, COMBO_INDEX_4, chr.MOTION_COMBO_ATTACK_4)
	# Combo Type 2
	# chrmgr.ReserveComboAttackNew(chr.MOTION_MODE_CLAW, COMBO_TYPE_2, 5)
	# chrmgr.RegisterComboAttackNew(chr.MOTION_MODE_CLAW, COMBO_TYPE_2, COMBO_INDEX_1, chr.MOTION_COMBO_ATTACK_1)
	# chrmgr.RegisterComboAttackNew(chr.MOTION_MODE_CLAW, COMBO_TYPE_2, COMBO_INDEX_2, chr.MOTION_COMBO_ATTACK_2)
	# chrmgr.RegisterComboAttackNew(chr.MOTION_MODE_CLAW, COMBO_TYPE_2, COMBO_INDEX_3, chr.MOTION_COMBO_ATTACK_3)
	# chrmgr.RegisterComboAttackNew(chr.MOTION_MODE_CLAW, COMBO_TYPE_2, COMBO_INDEX_4, chr.MOTION_COMBO_ATTACK_5)
	# chrmgr.RegisterComboAttackNew(chr.MOTION_MODE_CLAW, COMBO_TYPE_2, COMBO_INDEX_5, chr.MOTION_COMBO_ATTACK_7)
	# Combo Type 3
	# chrmgr.ReserveComboAttackNew(chr.MOTION_MODE_CLAW, COMBO_TYPE_3, 6)
	# chrmgr.RegisterComboAttackNew(chr.MOTION_MODE_CLAW, COMBO_TYPE_3, COMBO_INDEX_1, chr.MOTION_COMBO_ATTACK_1)
	# chrmgr.RegisterComboAttackNew(chr.MOTION_MODE_CLAW, COMBO_TYPE_3, COMBO_INDEX_2, chr.MOTION_COMBO_ATTACK_2)
	# chrmgr.RegisterComboAttackNew(chr.MOTION_MODE_CLAW, COMBO_TYPE_3, COMBO_INDEX_3, chr.MOTION_COMBO_ATTACK_3)
	# chrmgr.RegisterComboAttackNew(chr.MOTION_MODE_CLAW, COMBO_TYPE_3, COMBO_INDEX_4, chr.MOTION_COMBO_ATTACK_5)
	# chrmgr.RegisterComboAttackNew(chr.MOTION_MODE_CLAW, COMBO_TYPE_3, COMBO_INDEX_5, chr.MOTION_COMBO_ATTACK_6)
	# chrmgr.RegisterComboAttackNew(chr.MOTION_MODE_CLAW, COMBO_TYPE_3, COMBO_INDEX_6, chr.MOTION_COMBO_ATTACK_4)

	# FISHING
	# chrmgr.SetPathName(path + "fishing/")
	# chrmgr.RegisterMotionMode(chr.MOTION_MODE_FISHING)
	# chrmgr.RegisterCacheMotionData(chr.MOTION_MODE_FISHING, chr.MOTION_WAIT,			"wait.msa")
	# chrmgr.RegisterCacheMotionData(chr.MOTION_MODE_FISHING, chr.MOTION_WALK,			"walk.msa")
	# chrmgr.RegisterCacheMotionData(chr.MOTION_MODE_FISHING, chr.MOTION_RUN,				"run.msa")
	# chrmgr.RegisterCacheMotionData(chr.MOTION_MODE_FISHING, chr.MOTION_FISHING_THROW,	"throw.msa")
	# chrmgr.RegisterCacheMotionData(chr.MOTION_MODE_FISHING, chr.MOTION_FISHING_WAIT,	"fishing_wait.msa")
	# chrmgr.RegisterCacheMotionData(chr.MOTION_MODE_FISHING, chr.MOTION_FISHING_STOP,	"fishing_cancel.msa")
	# chrmgr.RegisterCacheMotionData(chr.MOTION_MODE_FISHING, chr.MOTION_FISHING_CATCH,	"fishing_catch.msa")
	# chrmgr.RegisterCacheMotionData(chr.MOTION_MODE_FISHING, chr.MOTION_FISHING_FAIL,	"fishing_fail.msa")

	# HORSE
	# chrmgr.SetPathName(path + "horse/")
	# chrmgr.RegisterMotionMode(chr.MOTION_MODE_HORSE)
	# chrmgr.RegisterCacheMotionData(chr.MOTION_MODE_HORSE, chr.MOTION_WAIT,				"wait.msa", 90)
	# chrmgr.RegisterCacheMotionData(chr.MOTION_MODE_HORSE, chr.MOTION_WAIT,				"wait1.msa", 9)
	# chrmgr.RegisterCacheMotionData(chr.MOTION_MODE_HORSE, chr.MOTION_WAIT,				"wait2.msa", 1)
	# chrmgr.RegisterCacheMotionData(chr.MOTION_MODE_HORSE, chr.MOTION_WALK,				"walk.msa")
	# chrmgr.RegisterCacheMotionData(chr.MOTION_MODE_HORSE, chr.MOTION_RUN,				"run.msa")
	# chrmgr.RegisterCacheMotionData(chr.MOTION_MODE_HORSE, chr.MOTION_DAMAGE,			"front_damage.msa")
	# chrmgr.RegisterCacheMotionData(chr.MOTION_MODE_HORSE, chr.MOTION_DAMAGE_BACK,		"front_damage.msa")
	# chrmgr.RegisterCacheMotionData(chr.MOTION_MODE_HORSE, chr.MOTION_DEAD,				"dead.msa")
	# chrmgr.RegisterCacheMotionData(chr.MOTION_MODE_HORSE, HORSE_SKILL_CHARGE,			"skill_charge.msa")
	# chrmgr.RegisterCacheMotionData(chr.MOTION_MODE_HORSE, HORSE_SKILL_SPLASH,			"skill_splash.msa")

	# HORSE_CLAW
	# chrmgr.SetPathName(path + "horse_claw/")
	# chrmgr.RegisterMotionMode(chr.MOTION_MODE_HORSE_CLAW)
	# chrmgr.RegisterCacheMotionData(chr.MOTION_MODE_HORSE_CLAW, chr.MOTION_COMBO_ATTACK_1, "combo_01.msa")
	# chrmgr.RegisterCacheMotionData(chr.MOTION_MODE_HORSE_CLAW, chr.MOTION_COMBO_ATTACK_2, "combo_02.msa")
	# chrmgr.RegisterCacheMotionData(chr.MOTION_MODE_HORSE_CLAW, chr.MOTION_COMBO_ATTACK_3, "combo_03.msa")
	# chrmgr.ReserveComboAttackNew(chr.MOTION_MODE_HORSE_CLAW, COMBO_TYPE_1, 3)
	# chrmgr.RegisterComboAttackNew(chr.MOTION_MODE_HORSE_CLAW, COMBO_TYPE_1, COMBO_INDEX_1, chr.MOTION_COMBO_ATTACK_1)
	# chrmgr.RegisterComboAttackNew(chr.MOTION_MODE_HORSE_CLAW, COMBO_TYPE_1, COMBO_INDEX_2, chr.MOTION_COMBO_ATTACK_2)
	# chrmgr.RegisterComboAttackNew(chr.MOTION_MODE_HORSE_CLAW, COMBO_TYPE_1, COMBO_INDEX_3, chr.MOTION_COMBO_ATTACK_3)
	# chrmgr.RegisterCacheMotionData(chr.MOTION_MODE_HORSE_CLAW, HORSE_SKILL_WILDATTACK, "skill_wildattack.msa")

	# Bone
	# chrmgr.RegisterAttachingBoneName(chr.PART_WEAPON, "equip_right_weapon")
	# chrmgr.RegisterAttachingBoneName(chr.PART_WEAPON_LEFT, "equip_left_weapon")

def __LoadGameSkill():

	try:
		skill.LoadSkillData()
	except:
		import exception
		exception.Abort("__LoadGameSkill")

def __LoadGameEnemy():
	pass

def __LoadGameNPC():
	try:
		lines = pack_open("npclist.txt", "r").readlines()
	except IOError:
		import dbg
		dbg.LogBox("LoadLocaleError(%(srcFileName)s)" % locals())
		app.Abort()

	for line in lines:
		tokens = line[:-1].split("\t")
		if len(tokens) == 0 or not tokens[0]:
			continue

		try:
			vnum = int(tokens[0])
		except ValueError:
			import dbg
			dbg.LogBox("LoadGameNPC() - %s - line #%d: %s" % (tokens, lines.index(line), line))
			app.Abort()			

		try:
			if vnum:
				chrmgr.RegisterRaceName(vnum, tokens[1].strip())
			else:
				chrmgr.RegisterRaceSrcName(tokens[1].strip(), tokens[2].strip())
		except IndexError:
			import dbg
			dbg.LogBox("LoadGameNPC() - %d, %s - line #%d: %s " % (vnum, tokens, lines.index(line), line))
			app.Abort()

def __LoadMotions():
	for i in xrange(8):
		chrmgr.LoadRaceMotions(i)

	mountVnums = [
		20107,
		20209,
		20210,
		20211,
		20212,
		20245,
		20244,
		20119,
		20201,
		20205
	]

	for i in mountVnums:
		chrmgr.LoadRaceMotions(i)

	for i in xrange(34000, 34039 + 1):
		chrmgr.LoadRaceMotions(i)

	for i in xrange(35000, 35005 + 1):
		chrmgr.LoadRaceMotions(i)

# GUILD_BUILDING
def LoadGuildBuildingList(filename, localeFileName):
	# import dbg
	# dbg.TraceError("00")
	import uiGuild
	uiGuild.BUILDING_DATA_LIST = []

	localeNameList = {}
	localeFileData = pack_open(localeFileName, "r").readlines()
	for line in localeFileData:
		tokens = line.replace("\n", "").split("\t")
		if len(tokens) != 2 or not tokens[0].isdigit():
			continue
		localeNameList[int(tokens[0])] = tokens[1]

	handle = app.OpenTextFile(filename)
	count = app.GetTextFileLineCount(handle)
	for i in xrange(count):
		line = app.GetTextFileLine(handle, i)
		tokens = line.split("\t")

		TOKEN_VNUM = 0
		TOKEN_TYPE = 1
		TOKEN_NAME = 2
		NO_USE_TOKEN_SIZE_1 = 3
		NO_USE_TOKEN_SIZE_2 = 4
		NO_USE_TOKEN_SIZE_3 = 5
		NO_USE_TOKEN_SIZE_4 = 6
		TOKEN_X_ROT_LIMIT = 7
		TOKEN_Y_ROT_LIMIT = 8
		TOKEN_Z_ROT_LIMIT = 9
		TOKEN_PRICE = 10
		TOKEN_MATERIAL = 11
		TOKEN_NPC = 12
		TOKEN_GROUP = 13
		TOKEN_DEPEND_GROUP = 14
		TOKEN_ENABLE_FLAG = 15
		LIMIT_TOKEN_COUNT = 16

		if not tokens[TOKEN_VNUM].isdigit():
			continue

		if len(tokens) < LIMIT_TOKEN_COUNT:
			import dbg
			dbg.TraceError("Strange token count [%d/%d] [%s]" % (len(tokens), TOKEN_COUNT, line))
			continue

		ENABLE_FLAG_TYPE_NOT_USE = False
		ENABLE_FLAG_TYPE_USE = True
		ENABLE_FLAG_TYPE_USE_BUT_HIDE = 2

		if ENABLE_FLAG_TYPE_NOT_USE == int(tokens[TOKEN_ENABLE_FLAG]):
			continue

		vnum = int(tokens[TOKEN_VNUM])
		type = tokens[TOKEN_TYPE]
		name = tokens[TOKEN_NAME]
		localName = "unknown name"
		xRotLimit = int(tokens[TOKEN_X_ROT_LIMIT])
		yRotLimit = int(tokens[TOKEN_Y_ROT_LIMIT])
		zRotLimit = int(tokens[TOKEN_Z_ROT_LIMIT])
		price = tokens[TOKEN_PRICE]
		material = tokens[TOKEN_MATERIAL]

		if localeNameList.has_key(vnum):
			localName = localeNameList[vnum]
		
		folderName = ""
		if "HEADQUARTER" == type:
			folderName = "headquarter"
		elif "FACILITY" == type:
			folderName = "facility"
		elif "OBJECT" == type:
			folderName = "object"
		elif "WALL" == type:
			folderName = "fence"

		materialList = ["0", "0", "0"]
		if material:
			if material[0] == "\"":
				material = material[1:]
			if material[-1] == "\"":
				material = material[:-1]
			for one in material.split("/"):
				data = one.split(",")
				if 2 != len(data):
					continue
				itemID = int(data[0])
				count = data[1]

				if itemID == uiGuild.MATERIAL_STONE_ID:
					materialList[uiGuild.MATERIAL_STONE_INDEX] = count
				elif itemID == uiGuild.MATERIAL_LOG_ID:
					materialList[uiGuild.MATERIAL_LOG_INDEX] = count
				elif itemID == uiGuild.MATERIAL_PLYWOOD_ID:
					materialList[uiGuild.MATERIAL_PLYWOOD_INDEX] = count

		## GuildSymbol 은 일반 NPC 들과 함께 등록한다.
		import chrmgr
		chrmgr.RegisterRaceSrcName(name, folderName)
		chrmgr.RegisterRaceName(vnum, name)

		appendingData = { "VNUM":vnum,
						  "TYPE":type,
						  "NAME":name,
						  "LOCAL_NAME":localName,
						  "X_ROT_LIMIT":xRotLimit,
						  "Y_ROT_LIMIT":yRotLimit,
						  "Z_ROT_LIMIT":zRotLimit,
						  "PRICE":price,
						  "MATERIAL":materialList,
						  "SHOW" : True }

		if ENABLE_FLAG_TYPE_USE_BUT_HIDE == int(tokens[TOKEN_ENABLE_FLAG]):
			appendingData["SHOW"] = False

		uiGuild.BUILDING_DATA_LIST.append(appendingData)

	app.CloseTextFile(handle)

# END_OF_GUILD_BUILDING

# SetRaceHeight
def __LoadRaceHeight():
	try:
		lines = pack_open("race_height.txt", "r").readlines()
	except IOError:
		import dbg
		dbg.TraceError("Cant read race_heights")
		return

	for line in lines:
		tokens = line[:-1].split("\t")
		if len(tokens) == 0 or not tokens[0]:
			continue

		vnum = int(tokens[0])
		height = float(tokens[1])

		chrmgr.SetRaceHeight(vnum, height)
# SetRaceSpecular
def __LoadRaceSpecular():
	try:
		lines = pack_open("race_specular.txt", "r").readlines()
	except IOError:
		import dbg
		dbg.TraceError("Cant read race_speculars")
		return

	for line in lines:
		tokens = line[:-1].split("\t")
		if len(tokens) == 0 or not tokens[0]:
			continue

		vnum = int(tokens[0])
		height = float(tokens[1])
		chrmgr.SetRaceSpecular(vnum, height)

loadGameDataDict={
	"INIT" : __InitData,
	"SOUND" : __LoadGameSound,
	"EFFECT" : __LoadGameEffect,
	"WARRIOR" : __LoadGameWarrior,
	"ASSASSIN" : __LoadGameAssassin,
	"SURA" : __LoadGameSura,
	"SHAMAN" : __LoadGameShaman,
	# "WOLFMAN" : __LoadGameWolfman,
	"SKILL" : __LoadGameSkill,
	"ENEMY" : __LoadGameEnemy,
	"NPC" : __LoadGameNPC,
	"MOTION" : __LoadMotions,
	"RACE_HEIGHT" : __LoadRaceHeight,
	"RACE_SPECULAR" : __LoadRaceSpecular,
}

def LoadGameData(name):
	global loadGameDataDict

	load=loadGameDataDict.get(name, 0)
	if load:
		loadGameDataDict[name]=0
		try:
			load()
		except:
			print name
			import exception
			exception.Abort("LoadGameData")
			raise


## NPC

def SetMovingNPC(race, name):
	chrmgr.CreateRace(race)
	chrmgr.SelectRace(race)

	## RESERVED
	chrmgr.SetPathName("d:/ymir work/npc/" + name + "/")
	chrmgr.RegisterMotionMode(chr.MOTION_MODE_GENERAL)
	chrmgr.RegisterMotionData(chr.MOTION_MODE_GENERAL, chr.MOTION_WAIT, "wait.msa")
	chrmgr.RegisterMotionData(chr.MOTION_MODE_GENERAL, chr.MOTION_WALK, "walk.msa")
	chrmgr.RegisterMotionData(chr.MOTION_MODE_GENERAL, chr.MOTION_RUN, "run.msa")
	chrmgr.RegisterMotionData(chr.MOTION_MODE_GENERAL, chr.MOTION_DEAD, "die.msa")
	chrmgr.LoadRaceData(name + ".msm")

def SetOneNPC(race, name):
	chrmgr.CreateRace(race)
	chrmgr.SelectRace(race)

	## RESERVED
	chrmgr.SetPathName("d:/ymir work/npc/" + name + "/")
	chrmgr.RegisterMotionMode(chr.MOTION_MODE_GENERAL)
	chrmgr.RegisterMotionData(chr.MOTION_MODE_GENERAL, chr.MOTION_WAIT, "wait.msa")
	chrmgr.LoadRaceData(name + ".msm")

def SetGuard(race, name):
	chrmgr.CreateRace(race)
	chrmgr.SelectRace(race)

	## Script Data
	chrmgr.SetPathName("d:/ymir work/npc/" + name + "/")
	chrmgr.LoadRaceData(name + ".msm")

	## GENERAL
	chrmgr.RegisterMotionMode(chr.MOTION_MODE_GENERAL)
	chrmgr.RegisterMotionData(chr.MOTION_MODE_GENERAL, chr.MOTION_SPAWN,		"00.msa")
	chrmgr.RegisterMotionData(chr.MOTION_MODE_GENERAL, chr.MOTION_WAIT,			"00.msa")
	chrmgr.RegisterMotionData(chr.MOTION_MODE_GENERAL, chr.MOTION_RUN,			"03.msa")

	chrmgr.RegisterMotionData(chr.MOTION_MODE_GENERAL, chr.MOTION_DAMAGE,		"30.msa", 50)
	chrmgr.RegisterMotionData(chr.MOTION_MODE_GENERAL, chr.MOTION_DAMAGE,		"30_1.msa", 50)

	chrmgr.RegisterMotionData(chr.MOTION_MODE_GENERAL, chr.MOTION_DAMAGE_BACK,	"34.msa", 50)
	chrmgr.RegisterMotionData(chr.MOTION_MODE_GENERAL, chr.MOTION_DAMAGE_BACK,	"34_1.msa", 50)

	chrmgr.RegisterMotionData(chr.MOTION_MODE_GENERAL, chr.MOTION_DAMAGE_FLYING,"32.msa")
	chrmgr.RegisterMotionData(chr.MOTION_MODE_GENERAL, chr.MOTION_STAND_UP,		"33.msa")

	chrmgr.RegisterMotionData(chr.MOTION_MODE_GENERAL, chr.MOTION_DAMAGE_FLYING_BACK,	"35.msa")
	chrmgr.RegisterMotionData(chr.MOTION_MODE_GENERAL, chr.MOTION_STAND_UP_BACK,		"36.msa")

	chrmgr.RegisterMotionData(chr.MOTION_MODE_GENERAL, chr.MOTION_DEAD,					"31.msa")
	chrmgr.RegisterMotionData(chr.MOTION_MODE_GENERAL, chr.MOTION_DEAD_BACK,			"37.msa")

	chrmgr.RegisterMotionData(chr.MOTION_MODE_GENERAL, chr.MOTION_NORMAL_ATTACK,		"20.msa")

	## Attacking Data
	chrmgr.RegisterNormalAttack(chr.MOTION_MODE_GENERAL, chr.MOTION_NORMAL_ATTACK)

def SetWarp(race):
	chrmgr.CreateRace(race)
	chrmgr.SelectRace(race)

	chrmgr.SetPathName("d:/ymir work/npc/warp/")
	chrmgr.LoadRaceData("warp.msm")

	## GENERAL
	chrmgr.RegisterMotionMode(chr.MOTION_MODE_GENERAL)
	chrmgr.RegisterMotionData(chr.MOTION_MODE_GENERAL, chr.MOTION_WAIT, "wait.msa")

def SetDoor(race, name):
	chrmgr.CreateRace(race)
	chrmgr.SelectRace(race)
	chrmgr.SetPathName("d:/ymir work/npc/"+name+"/")
	chrmgr.LoadRaceData(name + ".msm")
	chrmgr.RegisterMotionMode(chr.MOTION_MODE_GENERAL)
	chrmgr.RegisterMotionData(chr.MOTION_MODE_GENERAL, chr.MOTION_WAIT, "close_wait.msa")
	chrmgr.RegisterMotionData(chr.MOTION_MODE_GENERAL, chr.MOTION_DEAD, "open.msa")

def SetGuildBuilding(race, name, grade):
	chrmgr.CreateRace(race)
	chrmgr.SelectRace(race)
	chrmgr.SetPathName("d:/ymir work/guild/building/%s/" % name)
	chrmgr.LoadRaceData("%s%02d.msm" % (name, grade))
	chrmgr.RegisterMotionMode(chr.MOTION_MODE_GENERAL)
