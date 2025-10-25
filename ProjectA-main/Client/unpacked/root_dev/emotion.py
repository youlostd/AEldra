import localeInfo
import player
import chrmgr
import chr
import constInfo

EMOTION_VERSION = 2

if constInfo.ENABLE_NEW_EMOTES:
	EMOTION_VERSION = 3


if EMOTION_VERSION == 3:
	EMOTION_CLAP = 1
	EMOTION_CONGRATULATION = 2
	EMOTION_FORGIVE = 3
	EMOTION_ANGRY = 4
	EMOTION_ATTRACTIVE = 5
	EMOTION_SAD = 6
	EMOTION_SHY = 7
	EMOTION_CHEERUP = 8
	EMOTION_BANTER = 9
	EMOTION_JOY = 10
	EMOTION_CHEERS_1 = 11
	EMOTION_CHEERS_2 = 12
	EMOTION_DANCE_1 = 13
	EMOTION_DANCE_2 = 14
	EMOTION_DANCE_3 = 15
	EMOTION_DANCE_4 = 16
	EMOTION_DANCE_5 = 17
	EMOTION_KISS = 51
	EMOTION_FRENCH_KISS = 52
	EMOTION_SLAP = 53

	EMOTION_NEW_1 = 57
	EMOTION_NEW_2 = 58
	EMOTION_NEW_3 = 59
	EMOTION_NEW_4 = 60
	EMOTION_NEW_5 = 61
	EMOTION_NEW_6 = 62
	EMOTION_NEW_7 = 63
	EMOTION_NEW_8 = 64
	EMOTION_NEW_9 = 65
	EMOTION_NEW_10 = 66
	EMOTION_NEW_11 = 67
	EMOTION_NEW_12 = 68

	EMOTION_DICT = {
		EMOTION_CLAP :			{"name": localeInfo.EMOTION_CLAP, 		"command":"/clap"},
		EMOTION_DANCE_1 :		{"name": localeInfo.EMOTION_DANCE_1, 	"command":"/dance1"},
		EMOTION_DANCE_2 :		{"name": localeInfo.EMOTION_DANCE_2, 	"command":"/dance2"},
		EMOTION_DANCE_3 :		{"name": localeInfo.EMOTION_DANCE_3, 	"command":"/dance3"},
		EMOTION_DANCE_4 :		{"name": localeInfo.EMOTION_DANCE_4, 	"command":"/dance4"},
		EMOTION_DANCE_5 :		{"name": localeInfo.EMOTION_DANCE_5, 	"command":"/dance5"},
		EMOTION_CONGRATULATION :	{"name": localeInfo.EMOTION_CONGRATULATION,	"command":"/congratulation"},
		EMOTION_FORGIVE :		{"name": localeInfo.EMOTION_FORGIVE, 	"command":"/forgive"},
		EMOTION_ANGRY :			{"name": localeInfo.EMOTION_ANGRY, 		"command":"/angry"},
		EMOTION_ATTRACTIVE :		{"name": localeInfo.EMOTION_ATTRACTIVE, 	"command":"/attractive"},
		EMOTION_SAD :			{"name": localeInfo.EMOTION_SAD, 		"command":"/sad"},
		EMOTION_SHY :			{"name": localeInfo.EMOTION_SHY, 		"command":"/shy"},
		EMOTION_CHEERUP :		{"name": localeInfo.EMOTION_CHEERUP, 	"command":"/cheerup"},
		EMOTION_BANTER :		{"name": localeInfo.EMOTION_BANTER, 	"command":"/banter"},
		EMOTION_JOY :			{"name": localeInfo.EMOTION_JOY, 		"command":"/joy"},
		EMOTION_CHEERS_1 :		{"name": localeInfo.EMOTION_CHEERS_1, 	"command":"/cheer1"},
		EMOTION_CHEERS_2 :		{"name": localeInfo.EMOTION_CHEERS_2, 	"command":"/cheer2"},
		EMOTION_KISS :			{"name": localeInfo.EMOTION_CLAP_KISS, 	"command":"/kiss"},
		EMOTION_FRENCH_KISS :		{"name": localeInfo.EMOTION_FRENCH_KISS, 	"command":"/french_kiss"},
		EMOTION_SLAP :			{"name": localeInfo.EMOTION_SLAP, 		"command":"/slap"},

		EMOTION_NEW_1 :			{"name": localeInfo.EMOTION_NOSAY, 		"command":"/new_emote1"},
		EMOTION_NEW_2 :			{"name": localeInfo.EMOTION_SELFIE, 	"command":"/new_emote2"},
		EMOTION_NEW_3 :			{"name": localeInfo.EMOTION_WEATHER_3, 		"command":"/new_emote3"},
		EMOTION_NEW_4 :			{"name": localeInfo.EMOTION_CELEBRATION, 		"command":"/new_emote4"},
		EMOTION_NEW_5 :			{"name": localeInfo.EMOTION_PUSH_UP, 		"command":"/new_emote5"},
		EMOTION_NEW_6 :			{"name": localeInfo.EMOTION_DANCE_7, 		"command":"/new_emote6"},
		EMOTION_NEW_7 :			{"name": localeInfo.EMOTION_WEATHER_2, 		"command":"/new_emote7"},
		EMOTION_NEW_8 :			{"name": localeInfo.EMOTION_DOZE, 		"command":"/new_emote8"},
		EMOTION_NEW_9 :			{"name": localeInfo.EMOTION_CALL, 		"command":"/new_emote9"},
		EMOTION_NEW_10 :		{"name": localeInfo.EMOTION_SIREN, 		"command":"/new_emote10"},
		EMOTION_NEW_11 :		{"name": localeInfo.EMOTION_HUNGRY, 		"command":"/new_emote11"},
		EMOTION_NEW_12 :		{"name": localeInfo.EMOTION_EXERCISE, 		"command":"/new_emote12"},
	}

	ICON_DICT = {
		EMOTION_CLAP 		: 	"d:/ymir work/ui/game/windows/emotion_clap.sub",
		EMOTION_CHEERS_1	:	"d:/ymir work/ui/game/windows/emotion_cheers_1.sub",
		EMOTION_CHEERS_2	:	"d:/ymir work/ui/game/windows/emotion_cheers_2.sub",

		EMOTION_DANCE_1		:	"icon/action/dance1.tga",
		EMOTION_DANCE_2		:	"icon/action/dance2.tga",

		EMOTION_CONGRATULATION	:	"icon/action/congratulation.tga",
		EMOTION_FORGIVE		:	"icon/action/forgive.tga",
		EMOTION_ANGRY		:	"icon/action/angry.tga",
		EMOTION_ATTRACTIVE	:	"icon/action/attractive.tga",
		EMOTION_SAD		:	"icon/action/sad.tga",
		EMOTION_SHY		:	"icon/action/shy.tga",
		EMOTION_CHEERUP		:	"icon/action/cheerup.tga",
		EMOTION_BANTER		:	"icon/action/banter.tga",
		EMOTION_JOY		:	"icon/action/joy.tga",
		EMOTION_DANCE_1		:	"icon/action/dance1.tga",
		EMOTION_DANCE_2		:	"icon/action/dance2.tga",
		EMOTION_DANCE_3		:	"icon/action/dance3.tga",
		EMOTION_DANCE_4		:	"icon/action/dance4.tga",
		EMOTION_DANCE_5		:	"icon/action/dance5.tga",

		EMOTION_KISS		:	"d:/ymir work/ui/game/windows/emotion_kiss.sub",
		EMOTION_FRENCH_KISS	:	"d:/ymir work/ui/game/windows/emotion_french_kiss.sub",
		EMOTION_SLAP		:	"d:/ymir work/ui/game/windows/emotion_slap.sub",

		EMOTION_NEW_1 		: 	"icon/action/nosay.tga",
		EMOTION_NEW_2 		: 	"icon/action/selfie.tga",
		EMOTION_NEW_3 		: 	"icon/action/weather3.tga",
		EMOTION_NEW_4 		: 	"icon/action/celebration.tga",
		EMOTION_NEW_5 		: 	"icon/action/pushup.tga",
		EMOTION_NEW_6 		: 	"icon/action/dance7.tga",
		EMOTION_NEW_7 		: 	"icon/action/weather2.tga",
		EMOTION_NEW_8 		: 	"icon/action/whirl.tga",
		EMOTION_NEW_9 		: 	"icon/action/call.tga",
		EMOTION_NEW_10 		: 	"icon/action/hungry.tga",
		EMOTION_NEW_11 		: 	"icon/action/siren.tga",
		EMOTION_NEW_12 		: 	"icon/action/busy.tga",
	}

	ANI_DICT = {
		chr.MOTION_CLAP :			"clap.msa",
		chr.MOTION_CHEERS_1 :			"cheers_1.msa",
		chr.MOTION_CHEERS_2 :			"cheers_2.msa",
		chr.MOTION_DANCE_1 :			"dance_1.msa",
		chr.MOTION_DANCE_2 :			"dance_2.msa",
		chr.MOTION_DANCE_3 :			"dance_3.msa",
		chr.MOTION_DANCE_4 :			"dance_4.msa",
		chr.MOTION_DANCE_5 :			"dance_5.msa",
		chr.MOTION_CONGRATULATION :		"congratulation.msa",
		chr.MOTION_FORGIVE :			"forgive.msa",
		chr.MOTION_ANGRY :			"angry.msa",
		chr.MOTION_ATTRACTIVE :			"attractive.msa",
		chr.MOTION_SAD :			"sad.msa",
		chr.MOTION_SHY :			"shy.msa",
		chr.MOTION_CHEERUP :			"cheerup.msa",
		chr.MOTION_BANTER :			"banter.msa",
		chr.MOTION_JOY :			"joy.msa",
		chr.MOTION_FRENCH_KISS_WITH_WARRIOR :	"french_kiss_with_warrior.msa",
		chr.MOTION_FRENCH_KISS_WITH_ASSASSIN :	"french_kiss_with_assassin.msa",
		chr.MOTION_FRENCH_KISS_WITH_SURA :	"french_kiss_with_sura.msa",
		chr.MOTION_FRENCH_KISS_WITH_SHAMAN :	"french_kiss_with_shaman.msa",
		# chr.MOTION_FRENCH_KISS_WITH_WOLFMAN :	"french_kiss_with_wolfman.msa",
		chr.MOTION_KISS_WITH_WARRIOR :		"kiss_with_warrior.msa",
		chr.MOTION_KISS_WITH_ASSASSIN :		"kiss_with_assassin.msa",
		chr.MOTION_KISS_WITH_SURA :		"kiss_with_sura.msa",
		chr.MOTION_KISS_WITH_SHAMAN :		"kiss_with_shaman.msa",
		# chr.MOTION_KISS_WITH_WOLFMAN :		"kiss_with_wolfman.msa",
		chr.MOTION_SLAP_HIT_WITH_WARRIOR :	"slap_hit.msa",
		chr.MOTION_SLAP_HIT_WITH_ASSASSIN :	"slap_hit.msa",
		chr.MOTION_SLAP_HIT_WITH_SURA :		"slap_hit.msa",
		chr.MOTION_SLAP_HIT_WITH_SHAMAN :	"slap_hit.msa",
		# chr.MOTION_SLAP_HIT_WITH_WOLFMAN :	"slap_hit.msa",
		chr.MOTION_SLAP_HURT_WITH_WARRIOR :	"slap_hurt.msa",
		chr.MOTION_SLAP_HURT_WITH_ASSASSIN :	"slap_hurt.msa",
		chr.MOTION_SLAP_HURT_WITH_SURA :	"slap_hurt.msa",
		chr.MOTION_SLAP_HURT_WITH_SHAMAN :	"slap_hurt.msa",
		# chr.MOTION_SLAP_HURT_WITH_WOLFMAN :	"slap_hurt.msa",

		chr.NAME_SELFIE :	"selfie.msa",
		chr.NAME_PUSHUP :	"pushup.msa",
		chr.NAME_DANCE7 :	"dance_7.msa",
		chr.NAME_DOZE :		"doze.msa",
		chr.NAME_EXERCISE :	"exercise.msa",
	}

elif EMOTION_VERSION == 2:
	EMOTION_CLAP = 1
	EMOTION_CONGRATULATION = 2
	EMOTION_FORGIVE = 3
	EMOTION_ANGRY = 4
	EMOTION_ATTRACTIVE = 5
	EMOTION_SAD = 6
	EMOTION_SHY = 7
	EMOTION_CHEERUP = 8
	EMOTION_BANTER = 9
	EMOTION_JOY = 10
	EMOTION_CHEERS_1 = 11
	EMOTION_CHEERS_2 = 12
	EMOTION_DANCE_1 = 13
	EMOTION_DANCE_2 = 14
	EMOTION_DANCE_3 = 15
	EMOTION_DANCE_4 = 16
	EMOTION_DANCE_5 = 17
	EMOTION_KISS = 51
	EMOTION_FRENCH_KISS = 52
	EMOTION_SLAP = 53

	EMOTION_DICT = {
		EMOTION_CLAP :			{"name": localeInfo.EMOTION_CLAP, 		"command":"/clap"},
		EMOTION_DANCE_1 :		{"name": localeInfo.EMOTION_DANCE_1, 	"command":"/dance1"},
		EMOTION_DANCE_2 :		{"name": localeInfo.EMOTION_DANCE_2, 	"command":"/dance2"},
		EMOTION_DANCE_3 :		{"name": localeInfo.EMOTION_DANCE_3, 	"command":"/dance3"},
		EMOTION_DANCE_4 :		{"name": localeInfo.EMOTION_DANCE_4, 	"command":"/dance4"},
		EMOTION_DANCE_5 :		{"name": localeInfo.EMOTION_DANCE_5, 	"command":"/dance5"},
		EMOTION_CONGRATULATION :	{"name": localeInfo.EMOTION_CONGRATULATION,	"command":"/congratulation"},
		EMOTION_FORGIVE :		{"name": localeInfo.EMOTION_FORGIVE, 	"command":"/forgive"},
		EMOTION_ANGRY :			{"name": localeInfo.EMOTION_ANGRY, 		"command":"/angry"},
		EMOTION_ATTRACTIVE :		{"name": localeInfo.EMOTION_ATTRACTIVE, 	"command":"/attractive"},
		EMOTION_SAD :			{"name": localeInfo.EMOTION_SAD, 		"command":"/sad"},
		EMOTION_SHY :			{"name": localeInfo.EMOTION_SHY, 		"command":"/shy"},
		EMOTION_CHEERUP :		{"name": localeInfo.EMOTION_CHEERUP, 	"command":"/cheerup"},
		EMOTION_BANTER :		{"name": localeInfo.EMOTION_BANTER, 	"command":"/banter"},
		EMOTION_JOY :			{"name": localeInfo.EMOTION_JOY, 		"command":"/joy"},
		EMOTION_CHEERS_1 :		{"name": localeInfo.EMOTION_CHEERS_1, 	"command":"/cheer1"},
		EMOTION_CHEERS_2 :		{"name": localeInfo.EMOTION_CHEERS_2, 	"command":"/cheer2"},
		EMOTION_KISS :			{"name": localeInfo.EMOTION_CLAP_KISS, 	"command":"/kiss"},
		EMOTION_FRENCH_KISS :		{"name": localeInfo.EMOTION_FRENCH_KISS, 	"command":"/french_kiss"},
		EMOTION_SLAP :			{"name": localeInfo.EMOTION_SLAP, 		"command":"/slap"},
	}

	ICON_DICT = {
		EMOTION_CLAP 		: 	"d:/ymir work/ui/game/windows/emotion_clap.sub",
		EMOTION_CHEERS_1	:	"d:/ymir work/ui/game/windows/emotion_cheers_1.sub",
		EMOTION_CHEERS_2	:	"d:/ymir work/ui/game/windows/emotion_cheers_2.sub",

		EMOTION_DANCE_1		:	"icon/action/dance1.tga",
		EMOTION_DANCE_2		:	"icon/action/dance2.tga",

		EMOTION_CONGRATULATION	:	"icon/action/congratulation.tga",
		EMOTION_FORGIVE		:	"icon/action/forgive.tga",
		EMOTION_ANGRY		:	"icon/action/angry.tga",
		EMOTION_ATTRACTIVE	:	"icon/action/attractive.tga",
		EMOTION_SAD		:	"icon/action/sad.tga",
		EMOTION_SHY		:	"icon/action/shy.tga",
		EMOTION_CHEERUP		:	"icon/action/cheerup.tga",
		EMOTION_BANTER		:	"icon/action/banter.tga",
		EMOTION_JOY		:	"icon/action/joy.tga",
		EMOTION_DANCE_1		:	"icon/action/dance1.tga",
		EMOTION_DANCE_2		:	"icon/action/dance2.tga",
		EMOTION_DANCE_3		:	"icon/action/dance3.tga",
		EMOTION_DANCE_4		:	"icon/action/dance4.tga",
		EMOTION_DANCE_5		:	"icon/action/dance5.tga",

		EMOTION_KISS		:	"d:/ymir work/ui/game/windows/emotion_kiss.sub",
		EMOTION_FRENCH_KISS	:	"d:/ymir work/ui/game/windows/emotion_french_kiss.sub",
		EMOTION_SLAP		:	"d:/ymir work/ui/game/windows/emotion_slap.sub",
	}

	ANI_DICT = {
		chr.MOTION_CLAP :			"clap.msa",
		chr.MOTION_CHEERS_1 :			"cheers_1.msa",
		chr.MOTION_CHEERS_2 :			"cheers_2.msa",
		chr.MOTION_DANCE_1 :			"dance_1.msa",
		chr.MOTION_DANCE_2 :			"dance_2.msa",
		chr.MOTION_DANCE_3 :			"dance_3.msa",
		chr.MOTION_DANCE_4 :			"dance_4.msa",
		chr.MOTION_DANCE_5 :			"dance_5.msa",
		chr.MOTION_CONGRATULATION :		"congratulation.msa",
		chr.MOTION_FORGIVE :			"forgive.msa",
		chr.MOTION_ANGRY :			"angry.msa",
		chr.MOTION_ATTRACTIVE :			"attractive.msa",
		chr.MOTION_SAD :			"sad.msa",
		chr.MOTION_SHY :			"shy.msa",
		chr.MOTION_CHEERUP :			"cheerup.msa",
		chr.MOTION_BANTER :			"banter.msa",
		chr.MOTION_JOY :			"joy.msa",
		chr.MOTION_FRENCH_KISS_WITH_WARRIOR :	"french_kiss_with_warrior.msa",
		chr.MOTION_FRENCH_KISS_WITH_ASSASSIN :	"french_kiss_with_assassin.msa",
		chr.MOTION_FRENCH_KISS_WITH_SURA :	"french_kiss_with_sura.msa",
		chr.MOTION_FRENCH_KISS_WITH_SHAMAN :	"french_kiss_with_shaman.msa",
		# chr.MOTION_FRENCH_KISS_WITH_WOLFMAN :	"french_kiss_with_wolfman.msa",
		chr.MOTION_KISS_WITH_WARRIOR :		"kiss_with_warrior.msa",
		chr.MOTION_KISS_WITH_ASSASSIN :		"kiss_with_assassin.msa",
		chr.MOTION_KISS_WITH_SURA :		"kiss_with_sura.msa",
		chr.MOTION_KISS_WITH_SHAMAN :		"kiss_with_shaman.msa",
		# chr.MOTION_KISS_WITH_WOLFMAN :		"kiss_with_wolfman.msa",
		chr.MOTION_SLAP_HIT_WITH_WARRIOR :	"slap_hit.msa",
		chr.MOTION_SLAP_HIT_WITH_ASSASSIN :	"slap_hit.msa",
		chr.MOTION_SLAP_HIT_WITH_SURA :		"slap_hit.msa",
		chr.MOTION_SLAP_HIT_WITH_SHAMAN :	"slap_hit.msa",
		# chr.MOTION_SLAP_HIT_WITH_WOLFMAN :	"slap_hit.msa",
		chr.MOTION_SLAP_HURT_WITH_WARRIOR :	"slap_hurt.msa",
		chr.MOTION_SLAP_HURT_WITH_ASSASSIN :	"slap_hurt.msa",
		chr.MOTION_SLAP_HURT_WITH_SURA :	"slap_hurt.msa",
		chr.MOTION_SLAP_HURT_WITH_SHAMAN :	"slap_hurt.msa",
		# chr.MOTION_SLAP_HURT_WITH_WOLFMAN :	"slap_hurt.msa",
	}

elif EMOTION_VERSION == 1:
	EMOTION_CLAP = 1
	EMOTION_CHEERS_1 = 2
	EMOTION_CHEERS_2 = 3
	EMOTION_DANCE_1 = 4
	EMOTION_DANCE_2 = 5
	EMOTION_KISS = 51
	EMOTION_FRENCH_KISS = 52
	EMOTION_SLAP = 53

	EMOTION_DICT = {
		EMOTION_CLAP :			{"name": localeInfo.EMOTION_CLAP, 		"command":"/clap"},
		EMOTION_CHEERS_1 :		{"name": localeInfo.EMOTION_CHEERS_1, 	"command":"/cheer1"},
		EMOTION_CHEERS_2 :		{"name": localeInfo.EMOTION_CHEERS_2, 	"command":"/cheer2"},
		EMOTION_DANCE_1 :		{"name": localeInfo.EMOTION_DANCE_1, 	"command":"/dance1"},
		EMOTION_DANCE_2 :		{"name": localeInfo.EMOTION_DANCE_2, 	"command":"/dance2"},
		EMOTION_KISS :			{"name": localeInfo.EMOTION_CLAP_KISS, 	"command":"/kiss"},
		EMOTION_FRENCH_KISS :		{"name": localeInfo.EMOTION_FRENCH_KISS, 	"command":"/french_kiss"},
		EMOTION_SLAP :			{"name": localeInfo.EMOTION_SLAP, 		"command":"/slap"},
	}

	ICON_DICT = {
		EMOTION_CLAP 		: 	"d:/ymir work/ui/game/windows/emotion_clap.sub",
		EMOTION_CHEERS_1	:	"d:/ymir work/ui/game/windows/emotion_cheers_1.sub",
		EMOTION_CHEERS_2	:	"d:/ymir work/ui/game/windows/emotion_cheers_2.sub",

		EMOTION_DANCE_1		:	"icon/action/dance1.tga",
		EMOTION_DANCE_2		:	"icon/action/dance2.tga",

		EMOTION_KISS		:	"d:/ymir work/ui/game/windows/emotion_kiss.sub",
		EMOTION_FRENCH_KISS	:	"d:/ymir work/ui/game/windows/emotion_french_kiss.sub",
		EMOTION_SLAP		:	"d:/ymir work/ui/game/windows/emotion_slap.sub",
	}

	ANI_DICT = {
		chr.MOTION_CLAP :			"clap.msa",
		chr.MOTION_CHEERS_1 :			"cheers_1.msa",
		chr.MOTION_CHEERS_2 :			"cheers_2.msa",
		chr.MOTION_DANCE_1 :			"dance_1.msa",
		chr.MOTION_DANCE_2 :			"dance_2.msa",
		chr.MOTION_FRENCH_KISS_WITH_WARRIOR :	"french_kiss_with_warrior.msa",
		chr.MOTION_FRENCH_KISS_WITH_ASSASSIN :	"french_kiss_with_assassin.msa",
		chr.MOTION_FRENCH_KISS_WITH_SURA :	"french_kiss_with_sura.msa",
		chr.MOTION_FRENCH_KISS_WITH_SHAMAN :	"french_kiss_with_shaman.msa",
		chr.MOTION_KISS_WITH_WARRIOR :		"kiss_with_warrior.msa",
		chr.MOTION_KISS_WITH_ASSASSIN :		"kiss_with_assassin.msa",
		chr.MOTION_KISS_WITH_SURA :		"kiss_with_sura.msa",
		chr.MOTION_KISS_WITH_SHAMAN :		"kiss_with_shaman.msa",
		chr.MOTION_SLAP_HIT_WITH_WARRIOR :	"slap_hit.msa",
		chr.MOTION_SLAP_HIT_WITH_ASSASSIN :	"slap_hit.msa",
		chr.MOTION_SLAP_HIT_WITH_SURA :		"slap_hit.msa",
		chr.MOTION_SLAP_HIT_WITH_SHAMAN :	"slap_hit.msa",
		chr.MOTION_SLAP_HURT_WITH_WARRIOR :	"slap_hurt.msa",
		chr.MOTION_SLAP_HURT_WITH_ASSASSIN :	"slap_hurt.msa",
		chr.MOTION_SLAP_HURT_WITH_SURA :	"slap_hurt.msa",
		chr.MOTION_SLAP_HURT_WITH_SHAMAN :	"slap_hurt.msa",
	}
else:
	EMOTION_CLAP = 1
	EMOTION_CHEERS_1 = 2
	EMOTION_CHEERS_2 = 3
	EMOTION_KISS = 51
	EMOTION_FRENCH_KISS = 52
	EMOTION_SLAP = 53

	EMOTION_DICT = {
		EMOTION_CLAP :			{"name": localeInfo.EMOTION_CLAP, 		"command":"/clap"},
		EMOTION_CHEERS_1 :		{"name": localeInfo.EMOTION_CHEERS_1, 	"command":"/cheer1"},
		EMOTION_CHEERS_2 :		{"name": localeInfo.EMOTION_CHEERS_2, 	"command":"/cheer2"},
		EMOTION_KISS :			{"name": localeInfo.EMOTION_CLAP_KISS, 	"command":"/kiss"},
		EMOTION_FRENCH_KISS :		{"name": localeInfo.EMOTION_FRENCH_KISS, 	"command":"/french_kiss"},
		EMOTION_SLAP :			{"name": localeInfo.EMOTION_SLAP, 		"command":"/slap"},
	}

	ICON_DICT = {
		EMOTION_CLAP 		: 	"d:/ymir work/ui/game/windows/emotion_clap.sub",
		EMOTION_CHEERS_1	:	"d:/ymir work/ui/game/windows/emotion_cheers_1.sub",
		EMOTION_CHEERS_2	:	"d:/ymir work/ui/game/windows/emotion_cheers_2.sub",

		EMOTION_KISS		:	"d:/ymir work/ui/game/windows/emotion_kiss.sub",
		EMOTION_FRENCH_KISS	:	"d:/ymir work/ui/game/windows/emotion_french_kiss.sub",
		EMOTION_SLAP		:	"d:/ymir work/ui/game/windows/emotion_slap.sub",
	}

	ANI_DICT = {
		chr.MOTION_CLAP :			"clap.msa",
		chr.MOTION_CHEERS_1 :			"cheers_1.msa",
		chr.MOTION_CHEERS_2 :			"cheers_2.msa",
		chr.MOTION_FRENCH_KISS_WITH_WARRIOR :	"french_kiss_with_warrior.msa",
		chr.MOTION_FRENCH_KISS_WITH_ASSASSIN :	"french_kiss_with_assassin.msa",
		chr.MOTION_FRENCH_KISS_WITH_SURA :	"french_kiss_with_sura.msa",
		chr.MOTION_FRENCH_KISS_WITH_SHAMAN :	"french_kiss_with_shaman.msa",
		chr.MOTION_KISS_WITH_WARRIOR :		"kiss_with_warrior.msa",
		chr.MOTION_KISS_WITH_ASSASSIN :		"kiss_with_assassin.msa",
		chr.MOTION_KISS_WITH_SURA :		"kiss_with_sura.msa",
		chr.MOTION_KISS_WITH_SHAMAN :		"kiss_with_shaman.msa",
		chr.MOTION_SLAP_HIT_WITH_WARRIOR :	"slap_hit.msa",
		chr.MOTION_SLAP_HIT_WITH_ASSASSIN :	"slap_hit.msa",
		chr.MOTION_SLAP_HIT_WITH_SURA :		"slap_hit.msa",
		chr.MOTION_SLAP_HIT_WITH_SHAMAN :	"slap_hit.msa",
		chr.MOTION_SLAP_HURT_WITH_WARRIOR :	"slap_hurt.msa",
		chr.MOTION_SLAP_HURT_WITH_ASSASSIN :	"slap_hurt.msa",
		chr.MOTION_SLAP_HURT_WITH_SURA :	"slap_hurt.msa",
		chr.MOTION_SLAP_HURT_WITH_SHAMAN :	"slap_hurt.msa",
	}


def __RegisterSharedEmotionAnis(mode, path):
	chrmgr.SetPathName(path)
	chrmgr.RegisterMotionMode(mode)

	for key, val in ANI_DICT.items():
		chrmgr.RegisterMotionData(mode, key, val)

def RegisterEmotionAnis(path):
	actionPath = path + "action/"
	weddingPath = path + "wedding/"

	__RegisterSharedEmotionAnis(chr.MOTION_MODE_GENERAL, actionPath)
	__RegisterSharedEmotionAnis(chr.MOTION_MODE_WEDDING_DRESS, actionPath)

	chrmgr.SetPathName(weddingPath)
	chrmgr.RegisterMotionMode(chr.MOTION_MODE_WEDDING_DRESS)
	chrmgr.RegisterMotionData(chr.MOTION_MODE_WEDDING_DRESS, chr.MOTION_WAIT, "wait.msa")
	chrmgr.RegisterMotionData(chr.MOTION_MODE_WEDDING_DRESS, chr.MOTION_WALK, "walk.msa")
	chrmgr.RegisterMotionData(chr.MOTION_MODE_WEDDING_DRESS, chr.MOTION_RUN, "walk.msa")

def RegisterEmotionIcons():
	for key, val in ICON_DICT.items():
		player.RegisterEmotionIcon(key, val)

