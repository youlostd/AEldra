import os
import dbg
import uiScriptLocale
import cfg
import app
import localeInfo

SERVER = 1	# localhost
# SERVER = 2	# FreeBSD

AUCTION_PREMIUM = False


DOMAIN = "aeldra.net"

PM_ONLINE_POPUP_DICT = {}
PM_ONLINE_POPUP_LOADED = 0

if test_server:
	WINDOW_COUNT_OBJ = False
	WINDOW_OBJ_COUNT = 0
	WINDOW_OBJ_LIST = {}
	WINDOW_OBJ_TRACE = []
	WINDOW_TOTAL_OBJ_COUNT = 0

URL_NAME_TYPES = {
	"shop.%s" % DOMAIN : "mall",
	"example.org" : "preload",
}

HIDE_NPC_INDEXES = {
	"HIDE_NPC_MOUNT" : 0,
	"HIDE_NPC_PET" : 1,
	"HIDE_NPC_SHOP" : 2
}

AE_DEV = '127.0.0.1'
TEST_SERVER_INFO = {
	"data" : {
		"channel1"	: [AE_DEV, 30002],
		"channel2"	: [AE_DEV, 30002],
		"channel3"	: [AE_DEV, 30002],
		"channel4"	: [AE_DEV, 30002],
		"auth1"		: [AE_DEV, 30001],
		"mark"		: [AE_DEV, 30003],
	},
	"channel_count" : 4,
	"auth_count" : 1,
}

if SERVER == 2:
	EL_DEV = '127.0.0.1'
	TEST_SERVER_INFO = {
		"data" : {
			"channel1"	: [EL_DEV, 30003],
			"channel2"	: [EL_DEV, 30003],
			"channel3"	: [EL_DEV, 30003],
			"channel4"	: [EL_DEV, 30003],
			"auth1"		: [EL_DEV, 30001],
			"mark"		: [EL_DEV, 30003],
		},
		"channel_count" : 4,
		"auth_count" : 1,
	}

BETA_SERVER_IP = "127.0.0.1"
BETA_SERVER_INFO = {
	"data" : {
		"channel1"	: [BETA_SERVER_IP, 22110],
		"auth1"		: [BETA_SERVER_IP, 21050],
		"mark"		: [BETA_SERVER_IP, 21060],
	},
	"channel_count" : 1,
	"auth_count" : 1,
}

AE_LIVE = '127.0.0.1'
LIVE_SERVER_INFO = {
	"data" : {
		"channel1"	: [AE_LIVE,	22110],
		"channel2"	: [AE_LIVE,	22210],
		"channel3"	: [AE_LIVE,	22310],
		"channel4"	: [AE_LIVE,	22410],
		"channel5"	: [AE_LIVE,	22510],
		"mark"		: [AE_LIVE,	21060],
		"auth1"		: [AE_LIVE,	21090],
		"whitelist"	: [AE_LIVE,	33333],
	},
	"channel_count" : 5,
	"auth_count" : 1,
}

if __SERVER__ == 2:
	EL_LIVE = '127.0.0.1'
	LIVE_SERVER_INFO = {
		"data" : {
			"channel1"	: [EL_LIVE,	22110],
			"channel2"	: [EL_LIVE,	22210],
			"channel3"	: [EL_LIVE,	22310],
			"channel4"	: [EL_LIVE,	22410],
			"mark"		: [EL_LIVE,	21060],
			"auth1"		: [EL_LIVE,	20050],
			"whitelist"	: [EL_LIVE,	33333],
		},
		"channel_count" : 4,
		"auth_count" : 1,
	}


SERVER_INFO = LIVE_SERVER_INFO

BETA_SERVER_ENABLED = False
IS_BETA_SERVER = False

DUNGEON_RANK_TABLE = { }
DUNGEON_LIST = []
DUNGEON_NAME = [
	"Razador",
]

LINK_WHITELIST = ['https://www.twitch.tv', 'https://youtu.be', 'https://www.youtube.com', 'https://%s' % DOMAIN, 'https://board.%s' % DOMAIN]

DUNGEON_TASKS = test_server
ENABLE_DMG_METER = test_server
ENABLE_EQUIPMENT_CHANGER = True
ENABLE_DUNGEON_RANKING = False
COMBAT_ZONE = True
SHOW_MESSENGER_NOTIFICATION = True

FAST_MOVE_ITEM_COOLDOWN = False
CUBE_MAKE_ALL = True

DEATH_KEEP_SKILL_AFFECT_ICONS = False

NEW_UI_GAMEOPTION = True
ENABLE_COMPANION_NAME = True
IS_CHAT_CLEARED = False

AFFECT_GAME_OPTION = True

CHECK_WRONG_CHARACTER = True
CHARACTER_LIST = []

HOTFIX_TEMP_IGNORE_CHAT_OPEN = False

SOLD_ITEMS_QUEUE = []
SUNDAE_EVENT_BONUS_DATA = {}
SHOW_FPS =  int(cfg.Get(cfg.SAVE_OPTION, "SHOW_FPS", "0"))


# update 3.1.0
HOTKEYS = []
UPGRADE_STONE = True
SAVE_WINDOW_POSITION = True
NEW_TARGET_UI = True
ENABLE_INGAME_WIKI = True
NEW_MINIMAP_UI = True
FRACTION_WND = True
LEADERSHIP_EXTENSION = True
WHISPER_MANAGER = True
ITEM_TEXTAIL_OPTION = True
ENABLE_LEVEL_LIMIT_MAX = True

# update 3.0.0
SECOND_ITEM_PRICE = True
ENABLE_NEW_EMOTES = True
ENABLE_EMOJI = True
CHANGE_SKILL_COLOR = True
ENABLE_LEVEL2_RUNES = True
QUEST_TIMER_SCROLLBAR = True
SPECIAL_NAME_LETTERS = True
INPUT_IGNORE = 0

if app.ENABLE_ZODIAC:
	ZODIAC_TEMPLE = {}
	ZODIAC_TEMPLE['FLOOR'] = 1
	ZODIAC_TEMPLE['JUMP'] = 0
	ZODIAC_SAVE_FLOOR = 0
	ZODIAC_YELLOW_CHECKBOX = 0
	ZODIAC_CHECKBOX_REMEMBER = ""
	ZODIAC_RETURN_YELLOW_CHECKBOX = 0
	ENABLE_ZODIAC_MINIMAP = 0
	ZODIAC_WINDOW_FIX = 0
	ZODIAC_AFTER_CD = 0
	ZI_PORTAL = 0
	## Rank
	MISSION_X = {}
	#CLOCK NEW FIX
	ZODIAC_CLOCK_1ST = 0
	ZODIAC_CLOCK = 0

# update 2.4.0
ITEM_MAX_COUNT = 1000 # 200 Elonia
INFINITY_ITEMS = True
KEY_COMBO_SORT = True
ENABLE_RUNE_PAGES = True
SORT_AND_STACK_ITEMS = True
SORT_AND_STACK_ITEMS_SAFEBOX = True
# end

DUNGEON_RECONNECT = True
OFFLINE_SHOP_AVG_SHOW_POSITIVE_MARGIN = False
HIDE_NPC_OPTION = True
NEW_PICKUP_FILTER = True
DS_NO_CONFIRM_EQUIP = True
BRAVERY_CAPE_STORE = True
NEW_SUPPORT_SKILL = True
DRAGONSOUL_SET_BONUS = True
REQ_ITEM_RESET_RUNE = True
ENABLE_RACE_CATEGORY = True
NEW_SEARCH_CATEGORY = True

ENABLE_CHANGE_TEXTURE_SNOW = True
ENABLE_PERMANENT_POTIONS = True
ENABLE_WARP_BIND_RING = True
ENABLE_XMAS_EVENT = True

ENABLE_CRYSTAL_SYSTEM = False # Elonia

USE_NEW_COSTUME_WITH_ACCE = True

NEW_QUEST_TIMER = True
NEW_QUEST_TIMER_PLAY_SOUND = True			# notification sound
NEW_QUEST_TIMER_LAST_SOUND = 0 				# dont change, its for time measuring

ENABLE_REACT_EVENT = True
ENABLE_WHEEL_OF_FRIGHT = True
ENABLE_BATTLEPASS = False # Elonia
BATTLEPASS_DATA = []
BATTLEPASS_TEMP = None

LAST_SHOP_SEARCH = {}
GUILD_MEMBERS_LASTPLAYED = {}

# AUTO RELOGIN FUNCTION
RELOGIN_SYSTEM_ENABLED = False
RELOGIN_PICK_CHARATER = False

# dont touch these below
RELOGIN_ACCOUNT_INDEX = -1
RELOGIN_TRY_LOGIN = False
RELOGIN_LOGIN_WINDOW = False

RUNE_POINTS = 0
RUNE_COLLECTED_SOULS_COUNT = 0
RUNE_AFFECT_INFO = 0

MONSTER_INFO_DATA = {}
PLAYER_LANG_DATA = {}
# PLAYER_COOLDOWN_DATA = {}
LAST_CHAT_LINES = []

DEFAULT_SHOP_SHOW_LIMIT_RANGE = 1000
if cfg.Get(cfg.SAVE_OPTION, "hide_auctionshop_title", "1") == "0":
	SHOP_SHOW_LIMIT_RANGE = DEFAULT_SHOP_SHOW_LIMIT_RANGE
else:
	SHOP_SHOW_LIMIT_RANGE = 0

# option
URL = {
	"register" : "https://%s/r/introLogin" % DOMAIN,
	"password" : "https://%s/password" % DOMAIN,
	"bosshunt" : "https://%s/l/bosshunt" % DOMAIN,
	"runeinfo" : "https://%s/l/rune_info" % DOMAIN,
	"blackjack" : "https://%s/l/blackjack" % DOMAIN,
    "sundea" : "https://%s/l/sundea" % DOMAIN,
    "eqchanger" : "https://%s/l/eqchanger" % DOMAIN,
    "battlepass" : "https://%s/l/battlepass" % DOMAIN,
}

ENABLE_ANGELSDEMONS_EVENT = False
ENABLE_EVENT_ANNOUNCEMENTS = True

EVENTS = {
	1 	: [ "announce_battlepass.tga", 		"https://%s/l/battlepass" % DOMAIN],
	2 	: [ "announce_empirewar.tga", 		"https://%s/l/empirewar" % DOMAIN],
	3 	: [ "announce_pvptournament.tga", 	"https://%s/l/pvptournament" % DOMAIN],
	4 	: [ "announce_wheeloffortune.tga", 	"https://%s/l/wheel" % DOMAIN],
	5 	: [ "announce_fishpuzzle.tga", 		"https://%s/l/fish" % DOMAIN],
	6 	: [ "announce_warangels.tga",		"https://%s/l/angels" % DOMAIN],
	7 	: [ "announce_halloween.tga",		"https://%s/l/halloween" % DOMAIN],
	8	: ["announce_christmas.tga", 		"https://%s/l/xmas" % DOMAIN],
	9 	: [ "announce_football.tga",		"https://%s/1/football" % DOMAIN],
}


# fastly move item to offline shop or combine sash window using ctrl + lmb
FAST_ITEM_MOVE = True

BONI_BOARD = True
NEW_AFFECT_ICONS = True

#blockfunction
ME_KEY = 0

# chat premium system: change color of the chat-text
PREMIUM_CHAT_COLOR_ENABLED = True
# CHATCOLOR_PREMIUM = True

DIALOG_REMAINING_TIME_ENABLED = True
# automatical closing-time for popupdialogs at refine, shopsearch etc.
DIALOG_REMAINING_TIME = 2.5 # in seconds

NEW_WEBBROWSER = True
ENABLE_NEW_VOTE_SYSTEM = app.ENABLE_VOTEBOT
OFFLINE_SHOP_ITEM_ENABLED = True
IS_PRIVATE_AUCTION_SHOP = False
IS_PRIVATE_AUCTION_SHOP_COLOR = False

NEW_SWITCHBOT_ENABLED = True
switchbotSave = None
FIX_CH_COMMAND = True

BLOCK_TIME_EXTRACT_FROM_LEGENDARY_STONES = True

# TRANSLATE CHARACTER WINDOW
TRANSLATE_CHARACTER_WINDOW = True

RUMI_EVENT_DESIGN_TYPE = None

def GetCharacterWindowPath( ):

	if not TRANSLATE_CHARACTER_WINDOW:
		return uiScriptLocale.WINDOWS_PATH

	userLanguage = app.GetLanguage( )
	shortName = app.GetShortLanguageName( userLanguage )

	if shortName:
		return "d:/ymir work/ui/character_wnd/%s/" % shortName
	
	return uiScriptLocale.WINDOWS_PATH

# NEW FONTS ( the first font is going to be replaced )
ENABLE_NEW_FONTS = True
FONTS = [ "#", "Tahoma-12", "Arial:14" ]
CHOOSEN_FONT = 0

def GetChoosenFontName( ):

	if CHOOSEN_FONT < 0 or CHOOSEN_FONT > 2 or not ENABLE_NEW_FONTS:
		return FONTS[ 0 ]

	return FONTS[ CHOOSEN_FONT ]

# poison / burn effect on mob
NEW_HP_EFFECTS = True

ENABLE_LEGENDARY_SKILLS = True
app.SetUseLegendarySkills(ENABLE_LEGENDARY_SKILLS)

IN_GAME_SHOP_ENABLE = 1
CONSOLE_ENABLE = 0

CURRENT_CHANNEL_IDX = 99

CANNOT_SEE_INFO_MAP_DICT = {
	"metin2_map_monkeydungeon" : False,
	"metin2_map_monkeydungeon_02" : False,
	"metin2_map_monkeydungeon_03" : False,
}
 
IS_TEST_SERVER = os.path.isfile("________dev.txt") or os.path.isfile("dev.txt")
IS_WOLFMAN = False

SHINING_SYSTEM = True
EXPANDED_UPPITEM_ENABLE = True

RUNE_ENABLED = True
RUNE_TUTORIAL_ENABLED = True

ENABLE_EVENT_ICONS = True

ALCHEMY_SHORTCUTS_ENABLED = True
ALCHEMY_EFFECT_ON_ENABLED = True

# costume shop model vnums
COSTUME_VIEWER_ENABLED = True
COSTUME_VIEWER_ENABLE_ON_VNUM = [ 30006, 30007, 20400 ]

USE_COMBINED_CUSTOME_WINDOW = True

DEBUG_ENABLED = False
dbg.SetEnabled(DEBUG_ENABLED)

QUEST_CATEGORIES = (
	uiScriptLocale.QUEST_CATEGORIE_1,
	uiScriptLocale.QUEST_CATEGORIE_2,
	uiScriptLocale.QUEST_CATEGORIE_3,
	uiScriptLocale.QUEST_CATEGORIE_4,
)

QUEST_CAT_BATTLEPASS_MAIN = 1
QUEST_CAT_BATTLEPASS = (QUEST_CAT_BATTLEPASS_MAIN, 2, 3)

PVPMODE_ENABLE = 1
PVPMODE_ACCELKEY_ENABLE = 1
PVPMODE_ACCELKEY_DELAY = 0.5
PVPMODE_PROTECTED_LEVEL = 30

FOG_LEVEL0 = 4800.0
FOG_LEVEL1 = 9600.0
FOG_LEVEL2 = 12800.0
FOG_LEVEL_LIST=[FOG_LEVEL0, FOG_LEVEL1, FOG_LEVEL2]
try:
	FOG_LEVEL = FOG_LEVEL_LIST[int(cfg.Get(cfg.SAVE_OPTION, "FogLevel", '2'))]
except:
	FOG_LEVEL = 0

CAMERA_MAX_DISTANCE_SHORT = 2500.0
CAMERA_MAX_DISTANCE_LONG = 3500.0
CAMERA_MAX_DISTANCE_HUGE = 4500.0
CAMERA_MAX_DISTANCE_LIST=[CAMERA_MAX_DISTANCE_SHORT, CAMERA_MAX_DISTANCE_LONG, CAMERA_MAX_DISTANCE_HUGE]
try:
	CAMERA_MAX_DISTANCE = float(cfg.Get(cfg.SAVE_OPTION, "CameraMaxDistance", str(CAMERA_MAX_DISTANCE_LONG)))
except:
	CAMERA_MAX_DISTANCE = CAMERA_MAX_DISTANCE_SHORT

CHRNAME_COLOR_INDEX = 0

HAS_SHOWN_INFO_SKILLBOOK_SAFEBOX = False

ENVIRONMENT_NIGHT="d:/ymir work/environment/moonlight04.msenv"

ENABLED_AUCTION_ITEM_COUNTER = False
AUCTION_INSERT_ITEM_ENABLED = False

# constant
HIGH_PRICE = 500000
MIDDLE_PRICE = 50000
GAYA_HIGH_PRICE = 650
GAYA_MIDDLE_PRICE = 250
ERROR_METIN_STONE = 28960
CONVERT_EMPIRE_LANGUAGE_ENABLE = 1
USE_ITEM_WEAPON_TABLE_ATTACK_BONUS = 0
USE_SKILL_EFFECT_UPGRADE_ENABLE = 1
VIEW_OTHER_EMPIRE_PLAYER_TARGET_BOARD = 1
GUILD_MONEY_PER_GSP = 100
GUILD_WAR_TYPE_SELECT_ENABLE = 1
HAIR_COLOR_ENABLE = 1
ARMOR_SPECULAR_ENABLE = 1
WEAPON_SPECULAR_ENABLE = 1
SEQUENCE_PACKET_ENABLE = 0
KEEP_ACCOUNT_CONNETION_ENABLE = 1
MINIMAP_POSITIONINFO_ENABLE = 0
CONVERT_EMPIRE_LANGUAGE_ENABLE = 0
USE_ITEM_WEAPON_TABLE_ATTACK_BONUS = 0
ADD_DEF_BONUS_ENABLE = 0

PVPMODE_PROTECTED_LEVEL = 15
TWO_HANDED_WEAPON_ATT_SPEED_DECREASE_VALUE = 10

isItemDropQuestionDialog = 0

def GET_ITEM_DROP_QUESTION_DIALOG_STATUS():
	global isItemDropQuestionDialog
	return isItemDropQuestionDialog

def SET_ITEM_DROP_QUESTION_DIALOG_STATUS(flag):
	global isItemDropQuestionDialog
	isItemDropQuestionDialog = flag

import app
import net

########################

def SET_DEFAULT_FOG_LEVEL():
	global FOG_LEVEL
	app.SetMinFog(FOG_LEVEL)

def SET_FOG_LEVEL_INDEX(index):
	global FOG_LEVEL
	global FOG_LEVEL_LIST
	try:
		FOG_LEVEL=FOG_LEVEL_LIST[index]
	except IndexError:
		FOG_LEVEL=FOG_LEVEL_LIST[0]
	cfg.Set(cfg.SAVE_OPTION, "FogLevel", int(index))
	app.SetMinFog(FOG_LEVEL)

def GET_FOG_LEVEL_INDEX():
	global FOG_LEVEL
	global FOG_LEVEL_LIST
	try:
		return FOG_LEVEL_LIST.index(FOG_LEVEL)
	except IndexError:
		return 2
	except ValueError:
		return 1

########################

def SET_DEFAULT_CAMERA_MAX_DISTANCE():
	global CAMERA_MAX_DISTANCE
	app.SetCameraMaxDistance(CAMERA_MAX_DISTANCE)

def SET_CAMERA_MAX_DISTANCE_INDEX(index):
	global CAMERA_MAX_DISTANCE
	global CAMERA_MAX_DISTANCE_LIST
	try:
		CAMERA_MAX_DISTANCE=CAMERA_MAX_DISTANCE_LIST[index]
	except:
		CAMERA_MAX_DISTANCE=CAMERA_MAX_DISTANCE_LIST[0]
	cfg.Set(cfg.SAVE_OPTION, "CameraMaxDistance", str(CAMERA_MAX_DISTANCE))

	app.SetCameraMaxDistance(CAMERA_MAX_DISTANCE)

def GET_CAMERA_MAX_DISTANCE_INDEX():
	global CAMERA_MAX_DISTANCE
	global CAMERA_MAX_DISTANCE_LIST
	if CAMERA_MAX_DISTANCE in CAMERA_MAX_DISTANCE_LIST:
		return CAMERA_MAX_DISTANCE_LIST.index(CAMERA_MAX_DISTANCE)
	else:
		return CAMERA_MAX_DISTANCE_LONG

########################

import chrmgr
import player
import app

def SET_DEFAULT_CHRNAME_COLOR():
	global CHRNAME_COLOR_INDEX
	chrmgr.SetEmpireNameMode(CHRNAME_COLOR_INDEX)

def SET_CHRNAME_COLOR_INDEX(index):
	global CHRNAME_COLOR_INDEX
	CHRNAME_COLOR_INDEX=index
	chrmgr.SetEmpireNameMode(index)

def GET_CHRNAME_COLOR_INDEX():
	global CHRNAME_COLOR_INDEX
	return CHRNAME_COLOR_INDEX

def SET_VIEW_OTHER_EMPIRE_PLAYER_TARGET_BOARD(index):
	global VIEW_OTHER_EMPIRE_PLAYER_TARGET_BOARD
	VIEW_OTHER_EMPIRE_PLAYER_TARGET_BOARD = index

def GET_VIEW_OTHER_EMPIRE_PLAYER_TARGET_BOARD():
	global VIEW_OTHER_EMPIRE_PLAYER_TARGET_BOARD
	return VIEW_OTHER_EMPIRE_PLAYER_TARGET_BOARD

def SET_DEFAULT_CONVERT_EMPIRE_LANGUAGE_ENABLE():
	global CONVERT_EMPIRE_LANGUAGE_ENABLE
	net.SetEmpireLanguageMode(CONVERT_EMPIRE_LANGUAGE_ENABLE)

def SET_DEFAULT_USE_ITEM_WEAPON_TABLE_ATTACK_BONUS():
	global USE_ITEM_WEAPON_TABLE_ATTACK_BONUS
	player.SetWeaponAttackBonusFlag(USE_ITEM_WEAPON_TABLE_ATTACK_BONUS)

def SET_DEFAULT_USE_SKILL_EFFECT_ENABLE():
	global USE_SKILL_EFFECT_UPGRADE_ENABLE
	app.SetSkillEffectUpgradeEnable(USE_SKILL_EFFECT_UPGRADE_ENABLE)

def SET_TWO_HANDED_WEAPON_ATT_SPEED_DECREASE_VALUE():
	global TWO_HANDED_WEAPON_ATT_SPEED_DECREASE_VALUE
	app.SetTwoHandedWeaponAttSpeedDecreaseValue(TWO_HANDED_WEAPON_ATT_SPEED_DECREASE_VALUE)

########################
import item

ACCESSORY_MATERIAL_LIST = [50623, 50624, 50625, 50626, 50627, 50628, 50629, 50630, 50631, 50632, 50633, 50634]
#ACCESSORY_MATERIAL_LIST = [50623, 50623, 50624, 50624, 50625, 50625, 50626, 50627, 50628, 50629, 50630, 50631, 50632, 50633, 
#			    50623, 50623, 50624, 50624, ]
JewelAccessoryInfos = [
		# jewel		wrist	neck	ear		wrist2	neck2	ear2
		[50639, 14570, 16570, 17570, 15520, 16660, 17660],	
		[50633, 19180, 19170, 19160, 0, 0, 0],
		[50634, 19240, 19230, 19220, 0, 0, 0],
	]
NEW_ACCESSORY_MATERIAL_LIST = [50635, 50636, 50637, 50638, 50639]

NEW_PERMA_ACCESSORY_ORE_LIST = [
	[ 93042, 14020, 16020, 17020 ],
	[ 93043, 14040, 16040, 17040 ],
	[ 93044, 14060, 16060, 17060 ],
	[ 93045, 14080, 16080, 17080 ],
	[ 93046, 14100, 16100, 17100 ],
	[ 93047, 14120, 16120, 17120 ],
	[ 93048, 14140, 16140, 17140 ],
	[ 93049, 14160, 16160, 17160 ],
	[ 93050, 14180, 16180, 17180 ],
	[ 93051, 14200, 16200, 17200 ],
	[ 93052, 14220, 16220, 17220 ],
	[ 93053, 14500, 16500, 17500 ],
	[ 93054, 14520, 16520, 17520 ],
	[ 93055, 14540, 16540, 17540 ],
	[ 93056, 14560, 16560, 17560 ],
	[ 93057, 14570, 16570, 17570 ],
	[ 93051, 19180, 19170, 19160 ],
	[ 93052, 19240, 19230, 19220 ],
]

def GET_ACCESSORY_MATERIAL_VNUM_BY_TYPE(vnum, jewType, itemType = -1):
	permaVnum = 0
	normalVnum = 0

	item_base = (vnum / 10) * 10
	if item_base == 17580 or item_base == 14580 or item_base == 16580:
		if jewType == 1:
			permaVnum = 93056
			normalVnum = 50638
		elif jewType == 2:
			permaVnum = 93054
			normalVnum = 50636
		elif jewType == 3:
			permaVnum = 93055
			normalVnum = 50637
		elif jewType == 4:
			permaVnum = 93053
			normalVnum = 50635
		elif jewType == 0:
			return (93056, 50638, 93054, 50636, 93055, 50637, 93053, 50635)
			
	if itemType == 33:
		normalVnum = 18900
		if jewType == 1:
			permaVnum = 94340
		elif jewType == 2:
			permaVnum = 94341
		elif jewType == 0:
			return (18900, 94340, 94341)

	return (normalVnum, permaVnum)
	
def GET_ACCESSORY_MATERIAL_VNUM(vnum, subType):
	ret = vnum

	item_base = (vnum / 10) * 10
	permaVnum = 0
	for i in NEW_PERMA_ACCESSORY_ORE_LIST:
		for j in xrange(1, 4):
			if item_base == i[j]:
				permaVnum = i[0]

	for info in JewelAccessoryInfos:
		if item.ARMOR_WRIST == subType:	
			if info[1] == item_base or (info[1+3] != 0 and info[1+3] == item_base):
				return (info[0], permaVnum)
		elif item.ARMOR_NECK == subType:	
			if info[2] == item_base or (info[2+3] != 0 and info[2+3] == item_base):
				return (info[0], permaVnum)
		elif item.ARMOR_EAR == subType:	
			if info[3] == item_base or (info[3+3] != 0 and info[3+3] == item_base):
				return (info[0], permaVnum)

	if (vnum >= 14500 and vnum <= 14619) or (vnum >= 16500 and vnum <= 16619) or (vnum >= 17500 and vnum <= 17619):
		if vnum <= 14619:
			ITEM_VNUM_BASE = 14500
		elif vnum <= 16619:
			ITEM_VNUM_BASE = 16500
		else:
			ITEM_VNUM_BASE = 17500
		ret -= ITEM_VNUM_BASE

		if (vnum >= 14589 and vnum <= 14619) or (vnum >= 16589 and vnum <= 16619) or (vnum >= 17589 and vnum <= 17619):
			type = (ret - 80) / 10
		else:
			type = ret / 20

		return (NEW_ACCESSORY_MATERIAL_LIST[type], permaVnum)

	if vnum >= 16210 and vnum <= 16219:
		return (50625, permaVnum)

	if item.ARMOR_WRIST == subType:	
		WRIST_ITEM_VNUM_BASE = 14000
		ret -= WRIST_ITEM_VNUM_BASE
	elif item.ARMOR_NECK == subType:
		NECK_ITEM_VNUM_BASE = 16000
		ret -= NECK_ITEM_VNUM_BASE
	elif item.ARMOR_EAR == subType:
		EAR_ITEM_VNUM_BASE = 17000
		ret -= EAR_ITEM_VNUM_BASE

	type = ret/20

	if type<0 or type>=len(ACCESSORY_MATERIAL_LIST):
		type = (ret-170) / 20
		if type<0 or type>=len(ACCESSORY_MATERIAL_LIST):
			return (0, permaVnum)

	return (ACCESSORY_MATERIAL_LIST[type], permaVnum)


def IS_AUTO_POTION(itemVnum):
	return IS_AUTO_POTION_HP(itemVnum) or IS_AUTO_POTION_SP(itemVnum)
	
def IS_AUTO_POTION_HP(itemVnum):
	if 72723 <= itemVnum and 72726 >= itemVnum:
		return 1
	elif itemVnum >= 76021 and itemVnum <= 76022:
		return 1
	elif itemVnum == 79012:
		return 1

	if ENABLE_PERMANENT_POTIONS:
		if itemVnum == 93274:
			return 1

	return 0

def IS_AUTO_POTION_SP(itemVnum):
	if 72727 <= itemVnum and 72730 >= itemVnum:
		return 1
	elif itemVnum >= 76004 and itemVnum <= 76005:
		return 1
	elif itemVnum == 79013:
		return 1

	if ENABLE_PERMANENT_POTIONS:
		if itemVnum == 93275:
			return 1

	return 0

if INFINITY_ITEMS:
	def IS_INFINITY_ITEMS(itemVnum):
		list = [ 93366, 93367, 93368, 93369, 93370, 93371, 93360, 93361, 93362, 93363, 93364, 93365, 93273, 50828, 95219, 95220, 95381 ]
		return itemVnum in list

def GET_URL_TYPE(url):
	startIgnore = "http://"
	startIgnore2 = "https://"
	for key in URL_NAME_TYPES:
		curIgnore = startIgnore
		if url.startswith(startIgnore2):
			curIgnore = startIgnore2

		if url[len(curIgnore):].startswith(key):
			return URL_NAME_TYPES[key]

	return ""

WHEEL_TO_SCROLL_MIN = 5
WHEEL_TO_SCROLL_MAX = 40
WHEEL_TO_SCROLL_DEFAULT = 13

WHEEL_VALUE = 0
WHEEL_LOADED = False

def WHEEL_LOAD():
	global WHEEL_VALUE, WHEEL_LOADED
	WHEEL_VALUE = int(cfg.Get(cfg.SAVE_OPTION, "wheel_scroll", str(WHEEL_TO_SCROLL_DEFAULT)))
	WHEEL_LOADED = True

def WHEEL_SET_VALUE(value):
	if int(value) < WHEEL_TO_SCROLL_MIN:
		value = WHEEL_TO_SCROLL_MIN
	elif int(value) > WHEEL_TO_SCROLL_MAX:
		value = WHEEL_TO_SCROLL_MAX

	cfg.Set(cfg.SAVE_OPTION, "wheel_scroll", str(value))
	WHEEL_VALUE = int(value)

def WHEEL_TO_SCROLL(wheel):
	if False == WHEEL_LOADED:
		WHEEL_LOAD()
	return -wheel * (WHEEL_VALUE / WHEEL_TO_SCROLL_MIN)

def WHEEL_TO_SCROLL_SLOW(wheel):
	if False == WHEEL_LOADED:
		WHEEL_LOAD()
	return -wheel * max(1, WHEEL_VALUE / WHEEL_TO_SCROLL_DEFAULT)

def WHEEL_TO_SCROLL_PX(wheel):
	if False == WHEEL_LOADED:
		WHEEL_LOAD()
	return -wheel * WHEEL_VALUE

POINT_TYPE_TO_APPLY_TYPE = {
	player.MAX_HP : item.APPLY_MAX_HP,
	player.MAX_SP : item.APPLY_MAX_SP,
	player.HT : item.APPLY_CON,
	player.IQ : item.APPLY_INT,
	player.ST : item.APPLY_STR,
	player.DX : item.APPLY_DEX,
	player.ATT_SPEED : item.APPLY_ATT_SPEED,
	player.MOVING_SPEED : item.APPLY_MOV_SPEED,
	player.CASTING_SPEED : item.APPLY_CAST_SPEED,
	player.POINT_HP_REGEN : item.APPLY_HP_REGEN,
	player.POINT_SP_REGEN : item.APPLY_SP_REGEN,
	player.POINT_POISON_PCT : item.APPLY_POISON_PCT,
	player.POINT_STUN_PCT : item.APPLY_STUN_PCT,
	player.POINT_SLOW_PCT : item.APPLY_SLOW_PCT,
	player.POINT_CRITICAL_PCT : item.APPLY_CRITICAL_PCT,
	player.POINT_PENETRATE_PCT : item.APPLY_PENETRATE_PCT,
	player.POINT_ATTBONUS_WARRIOR : item.APPLY_ATTBONUS_WARRIOR,
	player.POINT_ATTBONUS_ASSASSIN : item.APPLY_ATTBONUS_ASSASSIN,
	player.POINT_ATTBONUS_SURA : item.APPLY_ATTBONUS_SURA,
	player.POINT_ATTBONUS_SHAMAN : item.APPLY_ATTBONUS_SHAMAN,
	player.POINT_ATTBONUS_MONSTER : item.APPLY_ATTBONUS_MONSTER,
	player.POINT_ATTBONUS_HUMAN : item.APPLY_ATTBONUS_HUMAN,
	player.POINT_ATTBONUS_ANIMAL : item.APPLY_ATTBONUS_ANIMAL,
	player.POINT_ATTBONUS_ORC : item.APPLY_ATTBONUS_ORC,
	player.POINT_ATTBONUS_MILGYO : item.APPLY_ATTBONUS_MILGYO,
	player.POINT_ATTBONUS_UNDEAD : item.APPLY_ATTBONUS_UNDEAD,
	player.POINT_ATTBONUS_DEVIL : item.APPLY_ATTBONUS_DEVIL,
	player.POINT_STEAL_HP : item.APPLY_STEAL_HP,
	player.POINT_STEAL_SP : item.APPLY_STEAL_SP,
	player.POINT_MANA_BURN_PCT : item.APPLY_MANA_BURN_PCT,
	player.POINT_DAMAGE_SP_RECOVER : item.APPLY_DAMAGE_SP_RECOVER,
	player.POINT_BLOCK : item.APPLY_BLOCK,
	player.POINT_DODGE : item.APPLY_DODGE,
	player.POINT_RESIST_SWORD : item.APPLY_RESIST_SWORD,
	player.POINT_RESIST_TWOHAND : item.APPLY_RESIST_TWOHAND,
	player.POINT_RESIST_DAGGER : item.APPLY_RESIST_DAGGER,
	player.POINT_RESIST_BELL : item.APPLY_RESIST_BELL,
	player.POINT_RESIST_FAN : item.APPLY_RESIST_FAN,
	player.POINT_RESIST_BOW : item.APPLY_RESIST_BOW,
	player.POINT_RESIST_FIRE : item.APPLY_RESIST_FIRE,
	player.POINT_RESIST_ICE : item.APPLY_RESIST_ICE,
	player.POINT_RESIST_EARTH : item.APPLY_RESIST_EARTH,
	player.POINT_RESIST_DARK : item.APPLY_RESIST_DARK,
	player.POINT_RESIST_ELEC : item.APPLY_RESIST_ELEC,
	player.POINT_RESIST_MAGIC : item.APPLY_RESIST_MAGIC,
	player.POINT_RESIST_WIND : item.APPLY_RESIST_WIND,
	player.POINT_REFLECT_MELEE : item.APPLY_REFLECT_MELEE,
	player.POINT_POISON_REDUCE : item.APPLY_POISON_REDUCE,
	player.POINT_KILL_SP_RECOVER : item.APPLY_KILL_SP_RECOVER,
	player.POINT_EXP_DOUBLE_BONUS : item.APPLY_EXP_DOUBLE_BONUS,
	player.POINT_EXP_REAL_BONUS : item.APPLY_EXP_REAL_BONUS,
	player.POINT_GOLD_DOUBLE_BONUS : item.APPLY_GOLD_DOUBLE_BONUS,
	player.POINT_ITEM_DROP_BONUS : item.APPLY_ITEM_DROP_BONUS,
	player.POINT_POTION_BONUS : item.APPLY_POTION_BONUS,
	player.POINT_KILL_HP_RECOVER : item.APPLY_KILL_HP_RECOVER,
	player.POINT_DEF_GRADE_BONUS : item.APPLY_DEF_GRADE_BONUS,
	player.POINT_ATT_GRADE_BONUS : item.APPLY_ATT_GRADE_BONUS,
	player.POINT_MAGIC_ATT_GRADE_BONUS : item.APPLY_MAGIC_ATT_GRADE,
	player.POINT_MAGIC_DEF_GRADE_BONUS : item.APPLY_MAGIC_DEF_GRADE,
	player.POINT_NORMAL_HIT_DAMAGE_BONUS : item.APPLY_NORMAL_HIT_DAMAGE_BONUS,
	player.POINT_SKILL_DAMAGE_BONUS : item.APPLY_SKILL_DAMAGE_BONUS,
	player.POINT_NORMAL_HIT_DEFEND_BONUS : item.APPLY_NORMAL_HIT_DEFEND_BONUS,
	player.POINT_SKILL_DEFEND_BONUS : item.APPLY_SKILL_DEFEND_BONUS,
	player.POINT_RESIST_WARRIOR : item.APPLY_RESIST_WARRIOR,
	player.POINT_RESIST_ASSASSIN : item.APPLY_RESIST_ASSASSIN,
	player.POINT_RESIST_SURA : item.APPLY_RESIST_SURA,
	player.POINT_RESIST_SHAMAN : item.APPLY_RESIST_SHAMAN,
	player.POINT_MAX_HP_PCT : item.APPLY_MAX_HP_PCT,
	player.POINT_MAX_SP_PCT : item.APPLY_MAX_SP_PCT,
	player.POINT_RESIST_CRITICAL : item.APPLY_ANTI_CRITICAL_PCT,
	player.POINT_RESIST_PENETRATE : item.APPLY_ANTI_PENETRATE_PCT,
	player.POINT_MALL_EXPBONUS : item.APPLY_MALL_EXPBONUS,
	player.POINT_MALL_ITEMBONUS : item.APPLY_MALL_EXPBONUS,
	
	player.POINT_RESIST_SWORD_PEN : item.APPLY_RESIST_SWORD_PEN,
	player.POINT_RESIST_TWOHAND_PEN : item.APPLY_RESIST_TWOHAND_PEN,
	player.POINT_RESIST_DAGGER_PEN : item.APPLY_RESIST_DAGGER_PEN,
	player.POINT_RESIST_BELL_PEN : item.APPLY_RESIST_BELL_PEN,
	player.POINT_RESIST_FAN_PEN : item.APPLY_RESIST_FAN_PEN,
	player.POINT_RESIST_BOW_PEN : item.APPLY_RESIST_BOW_PEN,
	player.POINT_RESIST_ATTBONUS_HUMAN : item.APPLY_RESIST_ATTBONUS_HUMAN,
	player.POINT_DEF_BONUS : item.APPLY_DEFENSE_BONUS,
	
	player.POINT_ATTBONUS_ZODIAC : item.APPLY_ATTBONUS_ZODIAC
}
