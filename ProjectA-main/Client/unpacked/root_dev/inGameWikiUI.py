from __future__ import division
import ui
import wndMgr
import grp
import math
import item
from _weakref import proxy
import wiki
import app
import uiToolTip
import player
import nonplayer
import types
import constInfo
import localeInfo
import uiScriptLocale
import timer

enableDebugThings = test_server

#############################################################################

if __SERVER__ == 1:
	ORIGIN_MAP = {
		94146 : "random test text",
		94147 : "random test text2",
	}

	MOB_ORIGIN_MAP = {
		2598 : "random test text",
		2599 : "random test text2",
	}

	BOSS_CHEST_VNUMS = [50070,50081,50073,50074,50076,50077,50078,50079,50082,54700,54702,54703,50266,50186,95237,95238,33028,93254,92394,92395,93036,50270,50271,94339]
	EVENT_CHEST_VNUMS = [38056,50011,50037,50267,50268,50269,25311,25312,25313,93238,93239,93240,93241,93276,93277,93278,93279,94093,94094,94095,94096,94202,30714,94249,94250,94251,94252,94389,94390,50096,50265,94529,95221,95222,95223]
	ALT_CHEST_VNUMS = [50128,50130,94173,93234,93235,93110,93058,93059,93060,92863,92864,92957,95216]

	COSTUME_WEAPON_VNUMS = [range(93144, 93150), range(92400, 92405), range(92905, 92910), range(92920, 92930), range(92937, 92942), range(93072, 93074), range(93067, 93064), range(93061, 93063), range(92971, 92977), range(93069, 93071), range(93021, 93026), 93068, 93087, range(93176, 93182), range(93197, 93210), range(93218, 93224), range(40108, 40113), range(93247, 93253), range(93335, 93340), range(93406, 93436), range(94105, 94111), range(94138, 94143), range(94162, 94168), range(94190, 94195), range(94196, 94201), range(94254, 94260), range(94303, 94309), range(94345, 94354), range(94273, 94309), range(94371, 94376),94562,94563,94564,94565,94566,94567,94568,94546,94547,94548,94549,94550,94551, range(95289, 95295), range(95345, 95351)]
	COSTUME_ARMOR_VNUMS = [11971,11972,11973,11974,92536,92537,92538,92539,92540,92541,92542,92543,92544,92546,92547,92549,92568,92569,92570,92571,92578,92579,92580,92582,92583,92593,92594,92601,92602,92604,92605,92606,92607,92608,92617,92618,92619,92625,92626,92628,92633,92634,92635,92636,92597,92598,92406,92407,92408,92409,92411,92412,92413,92414,92415,92416,92417,92418,92419,92420,92421,92641,92642,92643,92644,92645,92646,92911,92912,92915,92916,92944,92945,92946,92947,92990,92991,92992,92993,92994,92995,92996,92997,93102,93103,93104,93105,25329,25330,25331,25332,93245,93246,41686,41687,41688,41689,93280,93281,93282,93283,93284,93285,93286,93287,93288,93289,93290,93291,93292,93293,93294,93295,93296,93297,93329,93330,93372,93373,93451,93452,93453,93454,94135,94169,93151,93152,94233,94234,94237,94237,94241,94242,94245,94246, range(41291, 41298), 94398,94399,94402,94403, range(94261, 94270), range(94356, 94365),94377,94554,94555,94556,94557,95296,95340,95341,95336,95337,95330,95331]
	COSTUME_HAIR_VNUMS = [92552,92553,92554,92555,92557,92559,92560,92561,92576,92577,92584,92585,92586,92587,92588,92589,92590,92591,92592,92595,92596,92600,92609,92610,92613,92614,92615,92616,92621,92622,92623,92624,92629,92630,92631,92632,92637,92638,92639,92640,92599,92647,92648,92649,92650,92651,92652,92653,92654,92655,92913,92914,92917,92918,92948,92949,92951,92950,93107,93108,93109,25333,25334,25335,25336,45364,45365,45366,45367,93310,93311,93312,93313,93314,93315,93316,93317,93318,93319,93320,93321,93322,93323,93324,93325,93457,93458,93459,93460,94174,94235,94236,94239,94240,94243,94244,94247,94248, range(45119, 45126),94400,94401,94404,94405,range(94310, 94319),94378,94558,94559,94560,94561,]
	COSTUME_PET_VNUMS = [93156,93157,53005,25316,25317,53274,53275,93304,93305,93306,93328,94100,94101,94157]
	COSTUME_MOUNT_VNUMS = [25314,25315,25322,25323,71243,93298,93299,93300,93302,93303,94391,94392,71124,]

	ITEM_BLACKLIST = [20760,20770,20780,20790,20800,20810,20820,20830,20840,20850,20860,20870,20880,20890,20900,20910,20920,20930,20940,21970,21960,21950,21940,21930,21920,21910,21900,7200,3200,3180,260,230,220,210,2190,8000,4030,1160,1150,1140,5150,5140,5130,7180,7170,11700,11030,11020,11010,11000,11300,11500,13020
    , range(14590, 14599), range(16590, 16599), range(17590, 17599), range(15460, 15469), range(19260, 19269), range(12820, 12829), range(18100, 18109)]
	MOB_BLACKLIST = [60004,35035, range(6443, 6470),6394,6393,6392,6391,6322,6321,6193,6207,6151,5163,3964,3963,3962,3961,3960,3959,3958,3957,3956,3913,3912,3911,3910,3906,3905,3903,3901,3891,3890,3596,3595,3591,3590,949,948,765,3902,8615,8613,8611,8603,8607,8605,8601,7124,2495,2307,2306,2192,2093,1906,1903,1310,1307,1095,1094,796,795,60010,60009,8614,8612,8610,8606,8604,8602,8600,5002,5001,2207,2095,1905,1904,1902,1309,1308,993,794,793,692,20500,20432,20422,20399,8062,8061,8058,8057,6529,6209,8429,8428,8050,8049,8048,8038,8036,7112,7111,7110,7109,7108,7107,6118,20482,20481,20480,20479,20478,20477,20476,20475,20474,20473,20472,20471,8204,8203,8201,8200,8116,8115,8114,8113,8112,8111,8110,8109,8108,8107,8106,8105,8104,8103,8102,8101,8060,8047,8046,8045,8044,8043,8042,8041,8040,8039,8037,8035,8033,8034,8032,8031,8023,8022,8021,8020,8019,8018,8017,8016,8015,60005,12022,12018,11111,11110,11109,11108,11107,11106,11105,11104,11103,11102,11101,11100,8619,8618,8616,8617,7122,7121,7120,7116,7115,7114,7113,60007,11117,11116,11115,11114,11113,11112,8622,8621,7119,7118,60008,11510,11509,11508,11507,11506,11505,8623,7106,7105,7104,7103,7102,7101]
	#no drops filter
	MOB_BLACKLIST.extend([[8508,8509,8510,8511,8505,8506,8507,8504,8503,7092,7093,8501,8502,7090,7091,7088,7089,7086,7087,7080,7079,7077,7078,7075,7076,7074,7073,7072,7071,7062,7063,7061,7060,7057,7058,7059,7052,7053,7054,7055,7051,7042,7050,7041,7036,7037,7038,7039,7040,7033,7034,7035,7032,7029,7030,7031,7028,7027,7026,7024,7025,7023,7022,7021,7020,7018,7019,7017,7015,7016,7014,7012,7013,7009,7010,7004,7005,7006,7007,7008,5207,5208,5209,7001,7002,5206,5205,5204,5202,5203,5201,5146,5145,5144,5142,5143,5141,5133,5134,5132,5127,5131,5116,2311,5003,2302,2301,2234,2235,2233,2231,2232,2157,2158,2154,2155,2156,2153,2151,2152,2101,2054,2055,2053,2052,2051,2032,2031,2001,2002,1335,1174,1175,1176,1177,1067,1066,1061,1062,1031,1032,1033,1034,1035,1001,991,992,933,934,935,936,937,931,903,775,776,777,773,774,755,756,757,771,772,753,754,735,751,731,732,733,705,698,697,695,696,655,656,657,652,653,654,651,635,595,554,552,553,551,501,454,455,456,451,452,453,402,403,397,398,354,391,392,393,394,180,181,182,183,178,179,177,171,172,173,174,175,144,140,141,142,143,138,139,137,135,136,132,133,134,115,131,114,113,111,112,110,109,108,107,105,106,104,102,103,101,176,184,185,301,302,303,304,331,332,333,334,351,352,353,395,396,752,932,1036,1037,1038,1039,1040,1151,1152,1153,1154,1155,1156,1157,1171,1172,1173,1331,7003,7056,7085,7094,7095,7096,7083,7084,7082,7081,7070,7069,7068,7067,7066,7065,7064,7049,7048,7047,7046,7045,7044,7043,6519,6518,6517,6516,6514,6515,6513,6499,6497,6496,6495,6494,6492,6493,6491,6490,6487,6488,6489,6486,6484,6485,6481,6482,6483,6480,6479,6478,6477,6476,6475,6474,6473,6471,6472,6470,6302,6203,6301,6117,6201,6202,4022,6001,6002,6101,4016,4017,4018,4019,4020,3704,3705,3801,3802,3803,3305,3401,3304,3202,3204,3205,3301,3005,3101,2510,2511,2512,2513,2514,2312,767,761,762,763,764,2415,2491,2494,2501,2541,2542,2543,2544,3104,3405,3501,3804,3805,3904,3907,3908,3909,4012,4013,4014,4015,4021,6102,3604,3605,3001,9480,9481,9710,9711,9479,9478,9476,9477,9474,9475,9473,9467,9468,9465,9466,9464,9463,9461,9462,6511,6512,9460,6503,6504,6505,6506,6507,6436,6437,6438,6439,6440,6419,6420,6421,6422,6304,6305,6306,6307,6206,6303,6112,6113,6114,6115,6204,6110,6111,6109,5153,5154,5155,5156,5152,3955,5151,1601,1602,1603,3950,3951,1403,1501,1502,1503,972,973,974,975,966,967,968,969,941,942,943,944,670,671,672,673,674,675,6205,6405,6406,6409,6410,6510,6435,6434,6433,6427,6428,6429,6430,6431,6108,5157,6003,6004,3952,3953,3954,1401,1402,970,971,946,947,965,940,945,976,977,978,979,6005,6006,6007,6008,6308,6309,6310,6401,6402,6403,6404,6411,6412,6413,6414,6423,6424,6425,6426,6432,6441,6442,6501,6502,6508,6106,6107,6009,983,984,36079,36096,9705,9702,9703,9704,9141,9142,9700,9701,4023,4024,988,985,986,987,676,9139,9140,8416,8417,8418,8421,8441,35071,36097,35074,35073,35072,8443,8442]])

	#############################################################################
	 
	USE_CATEG_ANIMATION = True
	WIKI_CATEGORIES = [
		[
			localeInfo.WIKI_CATEGORY_EQUIPEMENT,
			[
				[localeInfo.WIKI_SUBCATEGORY_WEAPONS, (0,), "d:/ymir work/ui/wiki/banners/banner_weapons.tga"],
				[localeInfo.WIKI_SUBCATEGORY_ARMOR, (1,), "d:/ymir work/ui/wiki/banners/armor.tga"],
				[localeInfo.WIKI_SUBCATEGORY_HELMET, (4,), "d:/ymir work/ui/wiki/banners/helmets.tga"],
				[localeInfo.WIKI_SUBCATEGORY_SHIELD, (6,), "d:/ymir work/ui/wiki/banners/shield.tga"],
				[localeInfo.WIKI_SUBCATEGORY_EARRINGS, (2,), "d:/ymir work/ui/wiki/banners/earrings.tga"],
				[localeInfo.WIKI_SUBCATEGORY_BRACELET, (7,), "d:/ymir work/ui/wiki/banners/bracelests.tga"],
				[localeInfo.WIKI_SUBCATEGORY_NECKLACE, (5,), "d:/ymir work/ui/wiki/banners/neck.tga"],
				[localeInfo.WIKI_SUBCATEGORY_SHOES, (3,), "d:/ymir work/ui/wiki/banners/shoes.tga"],
				[localeInfo.WIKI_SUBCATEGORY_BELTS, (9,), "d:/ymir work/ui/wiki/banners/belts.tga"],
				[localeInfo.WIKI_SUBCATEGORY_TALISMANS, (10,), "d:/ymir work/ui/wiki/banners/talisman.tga"],
				#["Talisman", ()],
			]
		],
		[
			localeInfo.WIKI_CATEGORY_CHESTS,
			[
				[localeInfo.WIKI_SUBCATEGORY_CHESTS, (BOSS_CHEST_VNUMS,), "d:/ymir work/ui/wiki/banners/bosschests.tga"],
				[localeInfo.WIKI_SUBCATEGORY_EVENT_CHESTS, (EVENT_CHEST_VNUMS,), "d:/ymir work/ui/wiki/banners/eventchests.tga"],
				[localeInfo.WIKI_SUBCATEGORY_ALTERNATIVE_CHESTS, (ALT_CHEST_VNUMS,), "d:/ymir work/ui/wiki/banners/altchests.tga"]
			]
		],
		[
			localeInfo.WIKI_CATEGORY_BOSSES,
			[
				[localeInfo.WIKI_SUBCATEGORY_LV1_75, (0, 1, 75), "d:/ymir work/ui/wiki/banners/bosses.tga"],
				[localeInfo.WIKI_SUBCATEGORY_LV76_100, (0, 76, 100), "d:/ymir work/ui/wiki/banners/bosses.tga"],
				[localeInfo.WIKI_SUBCATEGORY_LV100, (0, 100, 255), "d:/ymir work/ui/wiki/banners/bosses.tga"]
			]
		],
		[
			localeInfo.WIKI_CATEGORY_MONSTERS,
			[
				[localeInfo.WIKI_SUBCATEGORY_LV1_75, (1, 1, 75), "d:/ymir work/ui/wiki/banners/monster.tga"],
				[localeInfo.WIKI_SUBCATEGORY_LV76_100, (1, 76, 100), "d:/ymir work/ui/wiki/banners/monster.tga"],
				[localeInfo.WIKI_SUBCATEGORY_LV100, (1, 100, 255), "d:/ymir work/ui/wiki/banners/monster.tga"]
			]
		],
		[
			localeInfo.WIKI_CATEGORY_METINSTONES,
			[
				[localeInfo.WIKI_SUBCATEGORY_LV1_75, (2, 1, 75), "d:/ymir work/ui/wiki/banners/metin.tga"],
				[localeInfo.WIKI_SUBCATEGORY_LV76_100, (2, 76, 100), "d:/ymir work/ui/wiki/banners/metin.tga"],
				[localeInfo.WIKI_SUBCATEGORY_LV100, (2, 100, 255), "d:/ymir work/ui/wiki/banners/metin.tga"]
			]
		],
		[
			localeInfo.WIKI_CATEGORY_SYSTEMS,
			[
				[localeInfo.WIKI_SUBCATEGORY_RUNES, ("systems/runes.txt",)],
				[localeInfo.WIKI_SUBCATEGORY_DRAGONALCHEMY, ("systems/dragon_alchemy.txt",)],
				[localeInfo.WIKI_SUBCATEGORY_SHOULDER_SASH, ("systems/shoulder_sash.txt",)],
				[localeInfo.WIKI_SUBCATEGORY_COSTUME_SASH, ("systems/costume_sash.txt",)],
				[localeInfo.WIKI_SUBCATEGORY_BATTLEPASS, ("systems/battlepass.txt",)],
				[localeInfo.WIKI_SUBCATEGORY_COSTUMES, ("systems/costumes.txt",)],
				[localeInfo.WIKI_SUBCATEGORY_GAYA, ("systems/gaya.txt",)],
				[localeInfo.WIKI_SUBCATEGORY_SKILL_COLOR, ("systems/skill_color.txt",)],
				[localeInfo.WIKI_SUBCATEGORY_CONTER_BOOST, ("systems/conter_boost.txt",)]
			]
		],
		[
			localeInfo.WIKI_CATEGORY_DUNGEONS,
			[
				[localeInfo.WIKI_SUBCATEGORY_ORCMAZE, ("dungeons/orc_maze.txt",)],
				[localeInfo.WIKI_SUBCATEGORY_SPIDER_BARONESS, ("dungeons/spider_baroness.txt",)],
				[localeInfo.WIKI_SUBCATEGORY_AZRAEL, ("dungeons/azrael.txt",)],
				[localeInfo.WIKI_SUBCATEGORY_BERAN_SETAOU, ("dungeons/beran_setaou.txt",)],
				[localeInfo.QUEST_TIMER_SLIME, ("dungeons/slime.txt",)],
				[localeInfo.WIKI_SUBCATEGORY_NEMERE, ("dungeons/nemere.txt",)],
				[localeInfo.WIKI_SUBCATEGORY_RAZADOR, ("dungeons/razador.txt",)],
				[localeInfo.WIKI_SUBCATEGORY_SHIPDEFENSE, ("dungeons/ship_defense.txt",)],
				[localeInfo.WIKI_SUBCATEGORY_JOTUN_THRYM, ("dungeons/jotun_thrym.txt",)],
				[localeInfo.WIKI_SUBCATEGORY_CRYSTAL_DRAGON, ("dungeons/crystal_dragon.txt",)],
				[localeInfo.WIKI_SUBCATEGORY_MELEY, ("dungeons/meley.txt",)],
				[localeInfo.WIKI_SUBCATEGORY_THRANDUILS_LAIR, ("dungeons/thranduil.txt",)],
				[localeInfo.WIKI_SUBCATEGORY_ZODIAC, ("dungeons/zodiac.txt",)],
				[localeInfo.QUEST_TIMER_INFECTED, ("dungeons/infected.txt",)]
			]
		],
		[
			localeInfo.WIKI_CATEGORY_COSTUMES,
			[
				[localeInfo.WIKI_SUBCATEGORY_WEAPONS, (COSTUME_WEAPON_VNUMS,), "d:/ymir work/ui/wiki/banners/costume_weapon.tga"],
				[localeInfo.WIKI_SUBCATEGORY_ARMOR, (COSTUME_ARMOR_VNUMS,), "d:/ymir work/ui/wiki/banners/costume_armor.tga"],
				[localeInfo.WIKI_SUBCATEGORY_HAIRSTYLES, (COSTUME_HAIR_VNUMS,), "d:/ymir work/ui/wiki/banners/costume_hairstyle.tga"],
				[localeInfo.WIKI_SUBCATEGORY_PET, (COSTUME_PET_VNUMS,), "d:/ymir work/ui/wiki/banners/costume_pet.tga"],
				[localeInfo.WIKI_SUBCATEGORY_MOUNT, (COSTUME_MOUNT_VNUMS,), "d:/ymir work/ui/wiki/banners/costume_mount.tga"],
				#"Shining"
			]
		],
		[
			localeInfo.WIKI_CATEGORY_EVENTS,
			[
				[localeInfo.WIKI_SUBCATEGORY_OKAY_CARD, ("events/okey_card.txt",)],
				[localeInfo.WIKI_SUBCATEGORY_FISHPUZZLE, ("events/fishpuzzle.txt",)],
				[localeInfo.WIKI_SUBCATEGORY_BOSS_HUNT, ("events/boss_hunt.txt",)],
				#["Reaction Event", ("events/reaction_event.txt",)],
				[localeInfo.WIKI_SUBCATEGORY_MOONLIGHT_CHESTS, ("events/moonlight_chests.txt",)],
				[localeInfo.WIKI_SUBCATEGORY_HEXAGONAL_CHESTS, ("events/hexagonal_chests.txt",)],
				[localeInfo.WIKI_SUBCATEGORY_TAG_TEAM, ("events/tag_team.txt",)],
				[localeInfo.WIKI_SUBCATEGORY_EMPIRE_WAR, ("events/empire_war.txt",)],
				[localeInfo.WIKI_SUBCATEGORY_PVP_TOURNAMENT, ("events/pvp_tournament.txt",)]
			]
		],
		[
			localeInfo.WIKI_CATEGORY_GUIDES,
			[
				[localeInfo.WIKI_SUBCATEGORY_THE_START, ("guides/the_start.txt",)],
				[localeInfo.WIKI_SUBCATEGORY_RUNES, ("guides/runes.txt",)],
				[localeInfo.WIKI_SUBCATEGORY_105_AND_NOW, ("guides/105_and_now.txt",)]
			]
		],
	]
elif __SERVER__ == 2:
	ORIGIN_MAP = {
		94146 : ".",
	}

	MOB_ORIGIN_MAP = {
		2598 : ".",
	}

	BOSS_CHEST_VNUMS = [50070,50081,50073,50076,50077,50078,50079,50082,54700,50186,54702,54703]
	EVENT_CHEST_VNUMS = [50011,71144,38053,95471,95472,95473,95474,50267,50268,50269]
	ALT_CHEST_VNUMS = [50130,54028,92203,92204,50120,50121,50122]

	COSTUME_WEAPON_VNUMS = [range(92905, 92911), range(93011, 93017),93335,93336,93337,93338,93339,93340,92925,92926,92927,92928,92929,92930]
	COSTUME_ARMOR_VNUMS = [range(92578, 92584), range(92605, 92609),25329,25330,25331,25332,93294,93295,93296,93297,93286,93287,93288,93289,41686,41687,41688,41689,93290,93291,93292, 93293,95487,95488, 92597,92598]
	COSTUME_HAIR_VNUMS = [range(92584, 92593), range(92613, 92617),25333,25334,25335,25336,93322,93323,93324,93325,93310,93312,93313,45364,45365,45366,45367,93318,93319,93320,93321,95489,95490,92599,92600]
	COSTUME_PET_VNUMS = [53274,53275,95463,95464,95465,95466,95485,95486]
	COSTUME_MOUNT_VNUMS = [71243,71242,95483,95484,93298,93299,93302,93303]

	ITEM_BLACKLIST = [20760,20770,20780,20790,20800,20810,20820,20830,20840,20850,20860,20870,20880,20890,20900,20910,20920,20930,20940,21970,21960,21950,21940,21930,21920,21910,21900,7200,3200,3180,260,230,220,210,2190,8000,4030,1160,1150,1140,5150,5140,5130,7180,7170,11700,11030,11020,11010,11000,11300,11500,13020,3500,3220,500,310,2500,2200,1500,1180,7500,7300,5500,5160,510,19690,12070,19890,12080,19490,12060,19290,12050,19000,12730,12690,19010,12740,12700,19030,12760,12720,19020,12750,12710,19140,19130,19120,19110,19040,19250,13200,19190,17580,17570,19220,19160,14580,14570,19240,19180,16580,16570,19230,19170,15440,15450,19210,19150,19160,15240, range(19050, 19160),19200,13020,18010,18011,18012,18013,18014,18015,18016,18017,18018,18019,18030,18031,18032,18033,18034,18035,18036,18037,18038,18039,18040,18041,18042,18043,18044,18045,18046,18047,18048,18049,18060,18061,18062,18063,18064,18065,18066,18067,18068,18069,18070,18071,18072,18073,18074,18075,18076,18077,18078,18079]
	MOB_BLACKLIST = [5004,7123,2291,1334,1306,1096,693,35070,8085,5162,5161,2597,694,60004,35035, range(6443, 6470),792,2094,791,6394,6393,6392,6391,6322,6321,6193,6207,6151,3964,3963,3962,3961,3960,3959,3958,3957,3956,3913,3912,3911,3910,3906,3905,3903,3901,3891,3890,3596,3595,3591,3590,949,948,765,3902,8615,8613,8611,8603,8607,8605,8601,7124,2495,2307,2306,2192,2093,1906,1903,1310,1307,1095,1094,796,795,60010,60009,8614,8612,8610,8606,8604,8602,8600,5002,5001,2207,2095,1905,1904,1902,1309,1308,993,794,793,692,20500,20432,20422,20399,8062,8061,8058,8057,6529,6209,8429,8428,8050,8049,8048,8038,8036,7112,7111,7110,7109,7108,7107,6118,20482,20481,20480,20479,20478,20477,20476,20475,20474,20473,20472,20471,8204,8203,8201,8200,8116,8115,8114,8113,8112,8111,8110,8109,8108,8107,8106,8105,8104,8103,8102,8101,8060,8047,8046,8045,8044,8043,8042,8041,8040,8039,8037,8035,8033,8034,8032,8031,8023,8022,8021,8020,8019,8018,8017,8016,8015,60005,12022,12018,11111,11110,11109,11108,11107,11106,11105,11104,11103,11102,11101,11100,8619,8618,8616,8617,7122,7121,7120,7116,7115,7114,7113,60007,11117,11116,11115,11114,11113,11112,8622,8621,7119,7118,60008,11510,11509,11508,11507,11506,11505,8623,7106,7105,7104,7103,7102,7101,9140,9139,768,36079,35102,35101,9705,9704,9703,9702,9701,9700,9472,9471,9470,9469,9142,9141,6543,6542,6541,6540,6539,6538,6537,6536,6535,6534,6533,6532,6408,6407,6320,6192,6116,1191,950,6192,6320,767,764,763,762,761,6117,6201,6202,6203, range(6470, 6520), range(9710, 9713), range(9460, 9482), range(6400, 6443), range(940, 948), range(3950, 3956), range(6110, 6116),6204,6205,6206,35071,8430,35202,35201,35200,35103,35074,35073,35072,35036,8414,8413,8412,8411,8059,6528,6527,6526,6525,6524,6523,6522,6521,6520]
	#no drops filter
	MOB_BLACKLIST.extend([[2431,2432,2433,2434,2451,2452,2453,2454,8510,8511,8620,60006,7085,7094,7095,7096,6307,6308,6309,6310,8509,8505,8506,8507,8508,8502,8503,8504,7117,8501,7093,7089,7090,7091,7092,7088,7087,7086,7080,7079,7078,7073,7074,7075,7076,7072,7059,7060,7061,7062,7052,7053,7054,7055,7056,7051,7037,7038,7039,7040,7041,7034,7035,7036,7031,7032,7033,7029,7030,7027,7028,7025,7026,7024,7017,7018,7019,7020,7021,7016,7014,7015,7010,7012,7013,7009,7004,7005,7006,7007,7008,7002,7003,5209,7001,5207,5208,5206,5205,5202,5203,5204,5201,5157,5155,5156,5153,5154,5151,5152,5145,5146,5144,5143,5142,5141,5134,5132,5133,5131,5127,5116,5003,2301,2235,2234,2233,2232,2231,2158,2157,2156,2154,2155,2153,2151,2152,2101,2055,2032,2031,1335,1331,1333,1176,1177,1175,1174,1173,1172,1157,1171,1156,1155,1153,1154,1152,1151,1066,1037,1038,1039,1040,1041,1036,1034,1032,1033,1031,992,937,991,934,935,936,777,776,760,766,771,772,755,753,754,733,732,731,698,697,696,695,653,654,595,552,453,403,396,352,353,303,177,178,179,174,175,173,171,144,142,143,140,139,137,136,135,132,133,108,102,101,8085,35070,2291,7123,1306,1334,1096,693,7084,7083,7081,7082,7070,7069,7067,7068,7065,7066,7064,7049,7046,7047,7048,7044,7045,7043,6302,6001,6002,6101,6102,6301,3908,3909,3804,3805,3904,3907,3703,3704,3705,3801,3602,3603,3604,3605,3555,3601,3551,3552,3553,3554,3505,3503,3405,3501,3502,3403,3404,3305,3401,3203,3204,3205,3301,3202,3004,3101,3103,2594,2595,2596,3001,3002,2544,2545,2546,2547,2591,2512,2513,2514,2542,2511,2509,2510,2508,2505,2501,2502,2503,2415,6306,6305,6303,6304,6108,6109,6107,6106,6009,6051,6103,6104,6007,6008,6003,6004,6005,6006,3802,3803,3701,3304,3201,3303,7058,7063,7071,7077,3105,3104,3003,2593,2592,2504,7057,7050,7042,7023,7022,1067,554,451,452,6105]])

	#############################################################################
	 
	USE_CATEG_ANIMATION = True
	WIKI_CATEGORIES = [
		[
			localeInfo.WIKI_CATEGORY_EQUIPEMENT,
			[
				[localeInfo.WIKI_SUBCATEGORY_WEAPONS, (0,), "d:/ymir work/ui/wiki/banners/banner_weapons.tga"],
				[localeInfo.WIKI_SUBCATEGORY_ARMOR, (1,), "d:/ymir work/ui/wiki/banners/armor.tga"],
				[localeInfo.WIKI_SUBCATEGORY_HELMET, (4,), "d:/ymir work/ui/wiki/banners/helmets.tga"],
				[localeInfo.WIKI_SUBCATEGORY_SHIELD, (6,), "d:/ymir work/ui/wiki/banners/shield.tga"],
				[localeInfo.WIKI_SUBCATEGORY_EARRINGS, (2,), "d:/ymir work/ui/wiki/banners/earrings.tga"],
				[localeInfo.WIKI_SUBCATEGORY_BRACELET, (7,), "d:/ymir work/ui/wiki/banners/bracelests.tga"],
				[localeInfo.WIKI_SUBCATEGORY_NECKLACE, (5,), "d:/ymir work/ui/wiki/banners/neck.tga"],
				[localeInfo.WIKI_SUBCATEGORY_SHOES, (3,), "d:/ymir work/ui/wiki/banners/shoes.tga"],
				[localeInfo.WIKI_SUBCATEGORY_BELTS, (9,), "d:/ymir work/ui/wiki/banners/belts.tga"],
				#[localeInfo.WIKI_SUBCATEGORY_TALISMANS, (10,), "d:/ymir work/ui/wiki/banners/talisman.tga"],
				#["Talisman", ()],
			]
		],
		[
			localeInfo.WIKI_CATEGORY_CHESTS,
			[
				[localeInfo.WIKI_SUBCATEGORY_CHESTS, (BOSS_CHEST_VNUMS,), "d:/ymir work/ui/wiki/banners/bosschests.tga"],
				[localeInfo.WIKI_SUBCATEGORY_EVENT_CHESTS, (EVENT_CHEST_VNUMS,), "d:/ymir work/ui/wiki/banners/eventchests.tga"],
				[localeInfo.WIKI_SUBCATEGORY_ALTERNATIVE_CHESTS, (ALT_CHEST_VNUMS,), "d:/ymir work/ui/wiki/banners/altchests.tga"]
			]
		],
		[
			localeInfo.WIKI_CATEGORY_BOSSES,
			[
				[localeInfo.WIKI_SUBCATEGORY_LV1_75, (0, 1, 76), "d:/ymir work/ui/wiki/banners/bosses.tga"],
				[localeInfo.WIKI_SUBCATEGORY_LV76_100, (0, 76, 100), "d:/ymir work/ui/wiki/banners/bosses.tga"],
				[localeInfo.WIKI_SUBCATEGORY_LV100, (0, 100, 255), "d:/ymir work/ui/wiki/banners/bosses.tga"]
			]
		],
		[
			localeInfo.WIKI_CATEGORY_MONSTERS,
			[
				[localeInfo.WIKI_SUBCATEGORY_LV1_75, (1, 1, 76), "d:/ymir work/ui/wiki/banners/monster.tga"],
				[localeInfo.WIKI_SUBCATEGORY_LV76_100, (1, 76, 100), "d:/ymir work/ui/wiki/banners/monster.tga"],
				#[localeInfo.WIKI_SUBCATEGORY_LV100, (1, 100, 255), "d:/ymir work/ui/wiki/banners/monster.tga"]
			]
		],
		[
			localeInfo.WIKI_CATEGORY_METINSTONES,
			[
				[localeInfo.WIKI_SUBCATEGORY_LV1_75, (2, 1, 76), "d:/ymir work/ui/wiki/banners/metin.tga"],
				[localeInfo.WIKI_SUBCATEGORY_LV76_105, (2, 76, 105), "d:/ymir work/ui/wiki/banners/metin.tga"],
				#[localeInfo.WIKI_SUBCATEGORY_LV100, (2, 100, 255), "d:/ymir work/ui/wiki/banners/metin.tga"]
			]
		],
		[
			localeInfo.WIKI_CATEGORY_SYSTEMS,
			[
				#[localeInfo.WIKI_SUBCATEGORY_RUNES, ("systems/runes.txt",)],
				[localeInfo.WIKI_SUBCATEGORY_DRAGONALCHEMY, ("systems/dragon_alchemy_s2.txt",)],
				[localeInfo.WIKI_SUBCATEGORY_SHOULDER_SASH, ("systems/shoulder_sash_s2.txt",)],
				#[localeInfo.WIKI_SUBCATEGORY_COSTUME_SASH, ("systems/costume_sash.txt",)],
				#[localeInfo.WIKI_SUBCATEGORY_BATTLEPASS, ("systems/battlepass.txt",)],
				[localeInfo.WIKI_SUBCATEGORY_COSTUMES, ("systems/costumes_s2.txt",)],
				[localeInfo.WIKI_SUBCATEGORY_GAYA, ("systems/gaya_s2.txt",)],
				#[localeInfo.WIKI_SUBCATEGORY_SKILL_COLOR, ("systems/skill_color.txt",)],
				#[localeInfo.WIKI_SUBCATEGORY_CONTER_BOOST, ("systems/conter_boost.txt",)]
			]
		],
		[
			localeInfo.WIKI_CATEGORY_DUNGEONS,
			[
				#[localeInfo.WIKI_SUBCATEGORY_ORCMAZE, ("dungeons/orc_maze.txt",)],
                [localeInfo.WIKI_SUBCATEGORY_APE_DUNGEON, ("dungeons/apedungeon.txt",)],
                [localeInfo.WIKI_SUBCATEGORY_DEMONTOWER, ("dungeons/demontower.txt",)],
				[localeInfo.WIKI_SUBCATEGORY_SPIDER_BARONESS, ("dungeons/spider_baroness_s2.txt",)],
				[localeInfo.WIKI_SUBCATEGORY_AZRAEL, ("dungeons/azrael_s2.txt",)],
				[localeInfo.WIKI_SUBCATEGORY_BERAN_SETAOU, ("dungeons/beran_setaou_s2.txt",)],
				#[localeInfo.QUEST_TIMER_SLIME, ("dungeons/slime.txt",)],
				[localeInfo.WIKI_SUBCATEGORY_NEMERE, ("dungeons/nemere_s2.txt",)],
				[localeInfo.WIKI_SUBCATEGORY_RAZADOR, ("dungeons/razador_s2.txt",)],
				#[localeInfo.WIKI_SUBCATEGORY_SHIPDEFENSE, ("dungeons/ship_defense.txt",)],
				#[localeInfo.WIKI_SUBCATEGORY_JOTUN_THRYM, ("dungeons/jotun_thrym.txt",)],
				#[localeInfo.WIKI_SUBCATEGORY_CRYSTAL_DRAGON, ("dungeons/crystal_dragon.txt",)],
				#[localeInfo.WIKI_SUBCATEGORY_MELEY, ("dungeons/meley.txt",)],
				#[localeInfo.WIKI_SUBCATEGORY_THRANDUILS_LAIR, ("dungeons/thranduil.txt",)],
				#[localeInfo.WIKI_SUBCATEGORY_ZODIAC, ("dungeons/zodiac.txt",)],
				#[localeInfo.QUEST_TIMER_INFECTED, ("dungeons/infected.txt",)]
			]
		],
		[
			localeInfo.WIKI_CATEGORY_COSTUMES,
			[
				[localeInfo.WIKI_SUBCATEGORY_WEAPONS, (COSTUME_WEAPON_VNUMS,), "d:/ymir work/ui/wiki/banners/costume_weapon.tga"],
				[localeInfo.WIKI_SUBCATEGORY_ARMOR, (COSTUME_ARMOR_VNUMS,), "d:/ymir work/ui/wiki/banners/costume_armor.tga"],
				[localeInfo.WIKI_SUBCATEGORY_HAIRSTYLES, (COSTUME_HAIR_VNUMS,), "d:/ymir work/ui/wiki/banners/costume_hairstyle.tga"],
				[localeInfo.WIKI_SUBCATEGORY_PET, (COSTUME_PET_VNUMS,), "d:/ymir work/ui/wiki/banners/costume_pet.tga"],
				[localeInfo.WIKI_SUBCATEGORY_MOUNT, (COSTUME_MOUNT_VNUMS,), "d:/ymir work/ui/wiki/banners/costume_mount.tga"],
				#"Shining"
			]
		],
		[
			localeInfo.WIKI_CATEGORY_EVENTS,
			[
				[localeInfo.WIKI_SUBCATEGORY_OKAY_CARD, ("events/okey_card.txt",)],
				[localeInfo.WIKI_SUBCATEGORY_FISHPUZZLE, ("events/fishpuzzle.txt",)],
				[localeInfo.WIKI_SUBCATEGORY_BOSS_HUNT, ("events/boss_hunt.txt",)],
				#["Reaction Event", ("events/reaction_event.txt",)],
				[localeInfo.WIKI_SUBCATEGORY_MOONLIGHT_CHESTS, ("events/moonlight_chests.txt",)],
				#[localeInfo.WIKI_SUBCATEGORY_HEXAGONAL_CHESTS, ("events/hexagonal_chests.txt",)],
				#[localeInfo.WIKI_SUBCATEGORY_TAG_TEAM, ("events/tag_team.txt",)],
				[localeInfo.WIKI_SUBCATEGORY_EMPIRE_WAR, ("events/empire_war.txt",)],
				[localeInfo.WIKI_SUBCATEGORY_PVP_TOURNAMENT, ("events/pvp_tournament.txt",)]
			]
		],
		#[
		#	localeInfo.WIKI_CATEGORY_GUIDES,
		#	[
		#		[localeInfo.WIKI_SUBCATEGORY_THE_START, ("guides/the_start.txt",)],
		#		[localeInfo.WIKI_SUBCATEGORY_RUNES, ("guides/runes.txt",)],
		#		[localeInfo.WIKI_SUBCATEGORY_105_AND_NOW, ("guides/105_and_now.txt",)]
		#	]
		#],
	]


#if enableDebugThings:
#	WIKI_CATEGORIES[1][1].append(["DEV allchests", ([],)])

categoryPeakWindowSize = [109, 391 - 30]
mainBoardPos = [148, 106]
mainBoardSize = [555, 361]

def MakeMoneyText(money):
	money = str(money)
	original = money
	sLen = len(original)
	while sLen > 3 and original[sLen-3:] == "000":
		money = money[::-1].replace("000"[::-1], "k"[::-1], 1)[::-1]
		original = original[:sLen - 3]
		sLen -= 3

	return money

def HAS_FLAG(value, flag):
	return (value & flag) == flag

class WikiRenderTarget(ui.RenderTarget):
	def __init__(self, width, height):
		self.moduleID = -1
		super(WikiRenderTarget, self).__init__()
		self.SetSize(width, height)
		self.moduleID = wiki.GetFreeModelViewID()
		wndMgr.SetWikiRenderTarget(self.hWnd, self.moduleID)
		wiki.AddModelView(self.moduleID)
		wiki.RegisterModelViewWindow(self.moduleID, self.hWnd)

	def __del__(self):
		wiki.RegisterModelViewWindow(self.moduleID, 0)
		super(WikiRenderTarget, self).__del__()
		wiki.RemoveModelView(self.moduleID)

	def SetModel(self, vnum):
		if self.moduleID >= 0:
			wiki.SetModelViewModel(self.moduleID, vnum)

	def SetWeaponModel(self, vnum):
		if self.moduleID >= 0:
			wiki.SetModelViewWeapon(self.moduleID, vnum)

	def SetModelHair(self, vnum):
		if self.moduleID >= 0:
			wiki.SetModelViewHair(self.moduleID, vnum)

	def SetModelForm(self, vnum):
		if self.moduleID >= 0:
			wiki.SetModelViewForm(self.moduleID, vnum)

	def Show(self):
		super(WikiRenderTarget, self).Show()
		if self.moduleID >= 0:
			wiki.ShowModelView(self.moduleID, True)

	def Hide(self):
		super(WikiRenderTarget, self).Hide()
		if self.moduleID >= 0:
			wiki.ShowModelView(self.moduleID, False)

class WikiScrollBar(ui.Window):
	class MiddleBar(ui.DragButton):
		def __init__(self):
			ui.DragButton.__init__(self)
			self.AddFlag("movable")

			self.middle = ui.Bar()
			self.middle.SetParent(self)
			self.middle.AddFlag("attach")
			self.middle.AddFlag("not_pick")
			self.middle.SetColor(grp.GenerateColor(165/255, 165/255, 165/255, 1.0))
			self.middle.SetSize(1, 1)
			self.middle.Show()

		def SetSize(self, height):
			height = max(2, height)
			ui.DragButton.SetSize(self, self.middle.GetWidth(), height)
			self.middle.SetSize(self.middle.GetWidth(), height)

		def SetWidth(self, width):
			width = max(2, width)
			ui.DragButton.SetSize(self, width, self.middle.GetHeight())
			self.middle.SetSize(width, self.middle.GetHeight())

	def __init__(self):
		super(WikiScrollBar, self).__init__()

		self.scrollEvent = None
		self.scrollSpeed = 1
		self.sizeScale = 1.0
		self.bars = []
		for i in xrange(9):
			br = ui.Bar()
			br.SetParent(self)
			br.AddFlag("attach")
			br.AddFlag("not_pick")
			br.Show()
			self.bars.append(br)

		self.middleBar = self.MiddleBar()
		self.middleBar.SetParent(self)
		self.middleBar.Show()

		self.middleBar.SetMoveEvent(ui.__mem_func__(self.OnScrollMove))

		#corners
		self.bars[1].SetColor(grp.GenerateColor(87/255, 87/255, 87/255, 1.0))
		self.bars[1].SetSize(1, 1)
		self.bars[3].SetColor(grp.GenerateColor(87/255, 87/255, 87/255, 1.0))
		self.bars[3].SetSize(1, 1)
		self.bars[5].SetColor(grp.GenerateColor(87/255, 87/255, 87/255, 1.0))
		self.bars[5].SetSize(1, 1)
		self.bars[7].SetColor(grp.GenerateColor(87/255, 87/255, 87/255, 1.0))
		self.bars[7].SetSize(1, 1)

		#lines
		self.bars[0].SetColor(grp.GenerateColor(87/255, 87/255, 87/255, 1.0))
		self.bars[2].SetColor(grp.GenerateColor(87/255, 87/255, 87/255, 1.0))
		self.bars[4].SetColor(grp.GenerateColor(87/255, 87/255, 87/255, 1.0))
		self.bars[6].SetColor(grp.GenerateColor(87/255, 87/255, 87/255, 1.0))

		#base
		self.bars[8].SetColor(grp.GenerateColor(0.0, 0.0, 0.0, 1.0))

	def OnScrollMove(self):
		if self.scrollEvent:
			self.scrollEvent(float(self.middleBar.GetLocalPosition()[1] - 1) / float(self.GetHeight() - 2 - self.middleBar.GetHeight()))

	def SetScrollEvent(self, func):
		self.scrollEvent = ui.__mem_func__(func)

	def SetScrollSpeed(self, speed):
		self.scrollSpeed = speed

	def OnMouseWheel(self, length):
		if self.IsInPosition():
			val = min(max(1, self.middleBar.GetLocalPosition()[1] - length * self.scrollSpeed * self.sizeScale), self.GetHeight() - self.middleBar.GetHeight() - 1)
			self.middleBar.SetPosition(1, val)
			self.OnScrollMove()
			return True
		return False

	def OnMouseLeftButtonDown(self):
		(xMouseLocalPosition, yMouseLocalPosition) = self.GetMouseLocalPosition()
		if xMouseLocalPosition == 0 or xMouseLocalPosition == self.GetWidth():
			return
		pickedPos = yMouseLocalPosition
		self.middleBar.SetPosition(1, yMouseLocalPosition - self.middleBar.GetHeight() / 2)
		self.OnScrollMove()

	def SetSize(self, w, h):
		w = max(3, w)
		h = max(3, h)
		ui.Window.SetSize(self, w, h)

		self.bars[0].SetSize(1, h - 2)
		self.bars[4].SetSize(1, h - 2)
		self.bars[2].SetSize(w - 2, 1)
		self.bars[6].SetSize(w - 2, 1)

		self.bars[0].SetPosition(0, 1)
		self.bars[2].SetPosition(1, 0)
		self.bars[4].SetPosition(w - 1, 1)
		self.bars[6].SetPosition(1, h - 1)

		self.bars[1].SetPosition(0, 0)
		self.bars[3].SetPosition(w - 1, 0)
		self.bars[5].SetPosition(w - 1, h - 1)
		self.bars[7].SetPosition(0, h - 1)

		self.bars[8].SetPosition(1, 1)
		self.bars[8].SetSize(w - 2, h - 2)

		self.middleBar.SetWidth(w - 2)
		self.middleBar.SetSize(12)
		#self.middleBar.SetPosition(1, 1)

		self.middleBar.SetRestrictMovementArea(1, 1, w - 2, h - 2)

	def SetScale(self, fScale):
		self.sizeScale = fScale
		self.middleBar.SetSize(math.floor((self.GetHeight() - 2) * fScale))

	def SetPosScale(self, fScale):
		self.middleBar.SetPosition(1, math.ceil((self.GetHeight() - 2 - self.middleBar.GetHeight()) * fScale) + 1)

class SubCategObject(ui.Window):
	def __init__(self, text):
		super(SubCategObject, self).__init__()
		self.SetWindowName("SubCategObject_ListBoxEx_Item")

		self.mArgs = ()
		self.bannerFileName = None
		if type(text) == types.ListType:
			self.mArgs = text[1]
			if len(text) > 2:
				self.bannerFileName = text[2]

			text = text[0]
		self.needAnim = False
		self.originText = text
		self.isMoving = False

		self.textWindow = ui.Window()
		self.textWindow.SetParent(self)
		self.textWindow.AddFlag("attach")
		self.textWindow.AddFlag("not_pick")
		self.textWindow.SetPosition(2, 3)
		self.textWindow.Show()

		self.textLine = ui.TextLine()
		self.textLine.AddFlag("attach")
		self.textLine.AddFlag("not_pick")
		self.textLine.SetParent(self.textWindow)
		self.textLine.SetText(text)
		self.textLine.Show()

		self.testText = ui.TextLine()
		self.testText.SetParent(self.textWindow)
		self.testText.Hide()

	def SetSize(self, w, h):
		ui.Window.SetSize(self, w, h)
		self.textWindow.SetSize(w - 2, h - 3)
		self.CheckText()

	def CheckText(self):
		self.testText.SetText(self.originText)
		(wL, wT, wR, wB) = self.testText.GetRenderBox()
		if wR > 0:
			self.needAnim = True

			i = len(self.originText) - 1
			while wR > 0:
				self.testText.SetText(self.originText[:i])
				(wL, wT, wR, wB) = self.testText.GetRenderBox()
				i -= 1

			self.testText.SetText(self.originText[:i].strip() + "..")
			(wL, wT, wR, wB) = self.testText.GetRenderBox()
			if wR > 0:
				i -= 1
			self.textLine.SetText(self.originText[:i].strip() + "..")

	def SetParent(self, parent):
		ui.Window.SetParent(self, parent)
		self.parent=proxy(parent)

	def OnMouseLeftButtonDown(self):
		self.parent.SelectItem(self)

	def OnUpdate(self):
		if self.needAnim:
			currX = self.textLine.GetLocalPosition()[0]
			if self.IsIn():
				self.textLine.SetText(self.originText)
				(wL, wT, wR, wB) = self.textLine.GetRenderBox()
				if wR > 0:
					self.textLine.SetPosition(currX - 1, 0)

			elif currX < 0:
				self.textLine.SetPosition(currX + 1, 0)				
				if currX + 1 == 0:
					self.CheckText()

	def OnRender(self):
		if self.parent.GetSelectedItem()==self:
			grp.SetColor(ui.SELECT_COLOR)
			self.OnSelectedRender()
		elif self.IsIn():
			grp.SetColor(ui.HALF_WHITE_COLOR)
			self.OnSelectedRender()

	def OnSelectedRender(self):
		(rLeft, rTop, rRight, rBottom) = self.GetRenderBox()
		x, y = self.GetGlobalPosition()
		grp.RenderBar(x + rLeft, y + rTop, self.GetWidth() - rLeft - rRight, self.GetHeight() - rBottom - rTop)

class WikiCategory(ui.Window):
	TICK_COUNT = 6
	MIN_HEIGHT = 20
	ARROW_IMG = ["d:/ymir work/ui/wiki/arrow.tga", "d:/ymir work/ui/wiki/arrow_up.tga"]
	def __init__(self, owner = None):
		super(WikiCategory, self).__init__()
		if owner:
			self.owner = proxy(owner)
		else:
			self.owner = None

		self.clickEvent = None

		self.expectedSize = 0
		self.isAnimating = False
		self.isOpening = False
		self.currHeight = self.MIN_HEIGHT

		self.titleImg = ui.ExpandedImageBox()
		self.titleImg.SetParent(self)
		#self.titleImg.AddFlag("attach")
		self.titleImg.LoadImage("d:/ymir work/ui/wiki/category.tga")
		self.titleImg.SetStringEvent("MOUSE_LEFT_DOWN",ui.__mem_func__( self.ClickExpand))
		self.titleImg.Show()

		self.titleText = ui.TextLine()
		self.titleText.SetParent(self.titleImg)
		self.titleText.AddFlag("attach")
		self.titleText.AddFlag("not_pick")
		#self.titleText.SetVerticalAlignCenter()
		self.titleText.SetPosition(5, self.titleImg.GetHeight() / 2)
		self.titleText.Show()

		self.arrow = ui.ExpandedImageBox()
		self.arrow.SetParent(self.titleImg)
		self.arrow.AddFlag("attach")
		self.arrow.AddFlag("not_pick")
		self.arrow.LoadImage(self.ARROW_IMG[0])
		self.arrow.SetPosition(self.titleImg.GetWidth() - self.arrow.GetWidth() - 5, self.titleImg.GetHeight() / 2 - self.arrow.GetHeight() / 2)
		self.arrow.Show()

		self.expandWnd = ui.Window()
		self.expandWnd.SetParent(self)
		self.expandWnd.AddFlag("attach")
		self.expandWnd.AddFlag("not_pick")
		self.expandWnd.SetPosition(0, self.titleImg.GetHeight())
		if USE_CATEG_ANIMATION:
			self.expandWnd.SetSize(self.titleImg.GetWidth(), 0)
			self.expandWnd.Show()
		else:
			self.expandWnd.SetSize(self.titleImg.GetWidth(), self.MIN_HEIGHT)

		self.bars = []
		for i in xrange(6):
			br = ui.Bar()
			br.SetParent(self.expandWnd)
			br.AddFlag("attach")
			br.AddFlag("not_pick")
			br.Show()
			self.bars.append(br)

		self.categList = ui.ListBoxEx()
		self.categList.SetParent(self.expandWnd)
		self.categList.SetItemSize(self.titleImg.GetWidth() - 3 - 3, 17)
		self.categList.SetItemStep(17)
		self.categList.SetSize(self.titleImg.GetWidth() - 3 - 3, self.MIN_HEIGHT - 1)
		self.categList.SetPosition(3, 1)
		self.categList.SetSelectEvent(ui.__mem_func__(self.OnSelectSubCategory))
		self.categList.Show()

		self.bars[1].SetColor(grp.GenerateColor(75/255, 75/255, 75/255, 150/255))
		self.bars[3].SetColor(grp.GenerateColor(75/255, 75/255, 75/255, 150/255))

		self.bars[0].SetColor(grp.GenerateColor(54/255, 54/255, 54/255, 1.0))
		self.bars[2].SetColor(grp.GenerateColor(54/255, 54/255, 54/255, 1.0))
		self.bars[4].SetColor(grp.GenerateColor(54/255, 54/255, 54/255, 1.0))

		self.bars[5].SetColor(grp.GenerateColor(0.0, 0.0, 0.0, 1.0))

		ui.Window.SetSize(self, self.titleImg.GetWidth(), self.titleImg.GetHeight())
		self.ArrangeBars(self.MIN_HEIGHT)

	def OnSelectSubCategory(self, elem):
		self.owner.NotifyCategorySelect(self)

		wikiClass = wiki.GetBaseClass()
		if elem.bannerFileName and wikiClass:
			wikiClass.header.LoadImage(elem.bannerFileName)
			wikiClass.header.Show()
		elif wikiClass:
			wikiClass.header.Hide()

		if self.clickEvent:
			apply(self.clickEvent, elem.mArgs)

	def UnselectSubCategory(self):
		self.categList.SelectIndex(-1)

	def AddSubCategory(self, key, text):
		self.currHeight = 17 * (self.categList.GetItemCount() + 1) + 3
		if not USE_CATEG_ANIMATION:
			self.ArrangeBars(self.currHeight)
			self.expandWnd.SetSize(self.titleImg.GetWidth(), self.currHeight)
			if self.expandWnd.IsShow():
				oldS = self.GetHeight()
				ui.Window.SetSize(self, self.titleImg.GetWidth(), self.titleImg.GetHeight() + self.currHeight)
				self.owner.NotifySizeChange(self, self.GetHeight() - oldS)
		elif self.expandWnd.GetHeight() > 0:
			self.ArrangeBars(self.currHeight)
			self.isAnimating = True

		self.categList.SetViewItemCount(self.categList.GetItemCount() + 1)
		self.categList.AppendItem(SubCategObject(text))
		self.categList.SetSize(self.categList.GetWidth(), self.currHeight - 1)

	def ClickExpand(self):
		if not USE_CATEG_ANIMATION:
			change = 0
			if self.expandWnd.IsShow():
				ui.Window.SetSize(self, self.titleImg.GetWidth(), self.titleImg.GetHeight())
				self.expandWnd.Hide()
				self.arrow.LoadImage(self.ARROW_IMG[0])
				change = -self.expandWnd.GetHeight()
			else:
				ui.Window.SetSize(self, self.titleImg.GetWidth(), self.titleImg.GetHeight() + self.expandWnd.GetHeight())
				self.expandWnd.Show()
				self.arrow.LoadImage(self.ARROW_IMG[1])
				change = self.expandWnd.GetHeight()

			self.owner.NotifySizeChange(self, change)
		else:
			if self.isOpening:
				self.arrow.LoadImage(self.ARROW_IMG[0])
			else:
				self.arrow.LoadImage(self.ARROW_IMG[1])

			self.isOpening = not self.isOpening
			self.isAnimating = True
			self.expandWnd.Show()
			if self.isOpening:
				self.ArrangeBars(self.currHeight)
			else:
				self.ArrangeBars(0)

	if USE_CATEG_ANIMATION:
		def OnUpdate(self):
			if self.isAnimating:
				h = self.expandWnd.GetHeight()
				if h == self.expectedSize:
					self.isAnimating = False
					if h == 0:
						self.expandWnd.Hide()
					return

				isOpening = True
				if h > self.expectedSize:
					isOpening = False

				newSize = 0
				step = self.currHeight / self.TICK_COUNT
				if isOpening:
					newSize = min(self.currHeight, self.expandWnd.GetHeight() + step)
				else:
					newSize = max(0, self.expandWnd.GetHeight() - step)

				change = newSize - self.expandWnd.GetHeight()

				self.expandWnd.SetSize(self.titleImg.GetWidth(), newSize)
				ui.Window.SetSize(self, self.titleImg.GetWidth(), self.titleImg.GetHeight() + newSize)
				self.owner.NotifySizeChange(self, change)

	def SetSize(self, width, height):
		import dbg
		dbg.LogBox("WikiCategory -> SetSize - unsupported function")

	def ArrangeBars(self, currHeight):
		self.expectedSize = currHeight
		if currHeight < self.MIN_HEIGHT:
			return

		currWidth = self.expandWnd.GetWidth()
		self.bars[0].SetSize(1, currHeight - 1)
		self.bars[1].SetSize(1, 1)
		self.bars[2].SetSize(currWidth - 2, 1)
		self.bars[3].SetSize(1, 1)
		self.bars[4].SetSize(1, currHeight - 1)
		self.bars[5].SetSize(currWidth - 2, currHeight - 1)

		self.bars[1].SetPosition(0, currHeight - 1)
		self.bars[2].SetPosition(1, currHeight - 1)
		self.bars[3].SetPosition(currWidth - 1, currHeight - 1)
		self.bars[4].SetPosition(currWidth - 1, 0)
		self.bars[5].SetPosition(1, 0)

	def SetTitleName(self, text):
		self.titleText.SetText(text)
		self.titleText.SetPosition(5, self.titleImg.GetHeight() / 2 - self.titleText.GetTextSize()[1] / 2 - 1)

class WikiCategories(ui.Window):
	CATEGORY_PADDING = 5
	SCROLL_SPEED = 17
	def __init__(self):
		super(WikiCategories, self).__init__()
		self.elements = []

		self.scrollBoard = ui.Window()
		self.scrollBoard.SetParent(self)
		self.scrollBoard.AddFlag("attach")
		self.scrollBoard.AddFlag("not_pick")
		self.scrollBoard.Show()

		self.scrollBar = None
		self.hideWindowsEvent = None

		self.SetSize(categoryPeakWindowSize[0], categoryPeakWindowSize[1])
		self.SetInsideRender(True)

	def AddCategory(self, text):
		tmp = WikiCategory(self)
		tmp.SetParent(self.scrollBoard)
		tmp.SetTitleName(text)
		tmp.Show()

		addPadding = 0
		if len(self.elements) > 0:
			tmp.SetPosition(0, self.elements[-1].GetLocalPosition()[1] + self.elements[-1].GetHeight() + self.CATEGORY_PADDING)
			addPadding = self.CATEGORY_PADDING

		self.scrollBoard.SetSize(tmp.GetWidth(), self.scrollBoard.GetHeight() + addPadding + tmp.GetHeight())
		self.elements.append(tmp)
		return tmp

	def NotifySizeChange(self, obj, amount):
		ind = len(self.elements)
		if obj in self.elements:
			ind = self.elements.index(obj) + 1

		if ind < len(self.elements):
			for i in xrange(ind, len(self.elements)):
				self.elements[i].SetPosition(0, self.elements[i - 1].GetLocalPosition()[1] + self.elements[i - 1].GetHeight() + self.CATEGORY_PADDING)

		self.scrollBoard.SetSize(self.scrollBoard.GetWidth(), self.scrollBoard.GetHeight() + amount)
		self.UpdateScrollbar()

	def NotifyCategorySelect(self, obj):
		if self.hideWindowsEvent:
			self.hideWindowsEvent()
		for i in self.elements:
			if obj != proxy(i) and obj != i:
				i.UnselectSubCategory()

	def OnMouseWheel(self, length):
		if self.IsInPosition():
			self.UpdateScrollbar(length * self.SCROLL_SPEED)
			return True
		return False

	def OnScrollBar(self, fScale):
		curr = min(0, max(math.ceil((self.scrollBoard.GetHeight() - categoryPeakWindowSize[1]) * fScale * -1.0), -self.scrollBoard.GetHeight() + categoryPeakWindowSize[1]))
		self.scrollBoard.SetPosition(0, curr)

	def ChangeScrollbar(self):
		if self.scrollBar:
			if self.scrollBoard.GetHeight() <= self.GetHeight():
				self.scrollBar.Hide()
			else:
				self.scrollBar.SetScale(self.GetHeight() / self.scrollBoard.GetHeight())
				self.scrollBar.SetPosScale(abs(self.scrollBoard.GetLocalPosition()[1]) / (self.scrollBoard.GetHeight() - self.GetHeight()))
				self.scrollBar.Show()

	def UpdateScrollbar(self, val = 0):
		curr = min(0, max(self.scrollBoard.GetLocalPosition()[1] + val, -self.scrollBoard.GetHeight() + categoryPeakWindowSize[1]))
		self.scrollBoard.SetPosition(0, curr)
		self.ChangeScrollbar()

	def RegisterScrollBar(self, scroll):
		self.scrollBar = proxy(scroll)
		self.scrollBar.SetScrollEvent(self.OnScrollBar)
		self.scrollBar.SetScrollSpeed(self.SCROLL_SPEED)
		self.ChangeScrollbar()

class WikiMainWeaponWindow(ui.Window):
	class WikiItem(ui.Window):
		#this item is fucking dooomed (since I got the image in one piece)
		TABLE_COLS = [
			[
				131,
				21,
				40,
				134,
			],
			[
				172,
				21,
				40,
				134,
			],
			[
				213,
				21,
				41,
				134,
			],
			[
				255,
				21,
				40,
				134,
			],
			[
				296,
				21,
				40,
				134,
			],
			[
				337,
				21,
				41,
				134,
			],
			[
				379,
				21,
				40,
				134,
			],
			[
				420,
				21,
				40,
				134,
			],
			[
				461,
				21,
				41,
				134,
			],
			[
				503,
				21,
				36,
				134,
			],
		]
		ROW_HEIGHTS = [21, 44, 51, 17]
		ROW_START_Y = [0, 21 + 1, 21 + 1 + 44 + 1, 21 + 1 + 44 + 1 + 51 + 1]
		ROW_HEIGHTS3 = [21, 44, 47, 42, 22]
		ROW_START_Y3 = [0, 21 + 1, 21 + 1 + 44 + 1, 21 + 1 + 44 + 1 + 47 + 1, 21 + 1 + 44 + 1 + 47 + 1 + 42 + 1]
		def __init__(self, vnum, parent, enable3Row = False):
			ui.Window.__init__(self)

			wikiBase = wiki.GetBaseClass()
			if id(self) not in wikiBase.objList:
				wikiBase.objList[long(id(self))] = proxy(self)

			self.additionalLoaded = False
			self.vnum = vnum
			self.levelLimit = 0
			self.parent = proxy(parent)

			self.base = ui.ExpandedImageBox()
			self.base.SetParent(self)
			self.base.AddFlag("attach")
			self.base.AddFlag("not_pick")
			self.base.LoadImage("d:/ymir work/ui/wiki/detail_item.tga")
			self.base.Show()
			self.enable3Row = enable3Row

			self.cols = []
			cnt = 0
			for i in self.TABLE_COLS:
				tmp = ui.Window()
				tmp.SetParent(self.base)
				tmp.AddFlag("attach")
				tmp.AddFlag("not_pick")
				tmp.SetPosition(i[0], i[1])
				tmp.SetSize(i[2], i[3])
				tmp.Show()

				titleWnd = ui.Window()
				titleWnd.SetParent(tmp)
				titleWnd.SetPosition(0, self.ROW_START_Y[0])
				titleWnd.SetSize(tmp.GetWidth(), self.ROW_HEIGHTS[0])
				titleWnd.SAFE_SetOverInEvent(self.parent.OnOverIn, self.vnum + cnt)
				titleWnd.SAFE_SetOverOutEvent(self.parent.OnOverOut)
				if wiki.GetBaseClass():
					titleWnd.SetMouseLeftButtonDownEvent(ui.__mem_func__(wiki.GetBaseClass().OpenSpecialPage), self.parent, self.vnum, False)
				titleWnd.Show()
				tmp.titleWnd = titleWnd

				tx = ui.TextLine()
				tx.SetParent(titleWnd)
				tx.SetText("+" + str(cnt))
				tx.SetPosition(titleWnd.GetWidth() / 2 - tx.GetTextSize()[0] / 2, titleWnd.GetHeight() / 2 - tx.GetTextSize()[1] / 2 - 1)
				tx.Show()

				tmp.refineText = tx

				tmp.refineMat = []
				for j in xrange(2):
					img = ui.ExpandedImageBox()
					img.SetParent(tmp)
					img.Show()
					tmp.refineMat.append(img)

				tx = ui.TextLine()
				tx.SetParent(tmp)
				tx.SetText("-")
				tx.SetPosition(tmp.GetWidth() / 2 - tx.GetTextSize()[0] / 2, self.ROW_START_Y[1] + self.ROW_HEIGHTS[1] / 2 - tx.GetTextSize()[1] / 2 - 1)
				tx.Show()

				tmp.refineMatText = [tx]

				tx = ui.TextLine()
				tx.SetParent(tmp)
				tx.SetText("-")
				tx.SetPosition(tmp.GetWidth() / 2 - tx.GetTextSize()[0] / 2, self.ROW_START_Y[2] + self.ROW_HEIGHTS[2] / 2 - tx.GetTextSize()[1] / 2 - 1)
				tx.Show()

				tmp.refineMatText.append(tx)

				tx = ui.TextLine()
				tx.SetParent(tmp)
				tx.SetText("-")
				tx.SetPosition(tmp.GetWidth() / 2 - tx.GetTextSize()[0] / 2, self.ROW_START_Y[3] + self.ROW_HEIGHTS[3] / 2 - tx.GetTextSize()[1] / 2 - 1)
				tx.Show()

				tmp.moneyText = tx
				self.cols.append(tmp)
				cnt += 1

			self.goldText = ui.TextLine()
			self.goldText.SetParent(self.base)
			self.goldText.SetText(localeInfo.WIKI_REFINEINFO_YANG_COSTS)
			self.goldText.SetPosition(49 + 81 / 2 - self.goldText.GetTextSize()[0] / 2, 21 + self.ROW_START_Y[3] + self.ROW_HEIGHTS[3] / 2 - self.goldText.GetTextSize()[1] / 2 - 1)
			self.goldText.Show()

			self.upgradeText = ui.TextLine()
			self.upgradeText.SetParent(self.base)
			self.upgradeText.SetText(localeInfo.WIKI_REFINEINFO_UPGRADE_COSTS)
			self.upgradeText.SetPosition(49 + 81 / 2 - self.upgradeText.GetTextSize()[0] / 2, 21 + self.ROW_START_Y[0] + self.ROW_HEIGHTS[0] / 2 - self.upgradeText.GetTextSize()[1] / 2 - 1)
			self.upgradeText.Show()

			self.levelText = ui.TextLine()
			self.levelText.SetParent(self.base)

			for i in xrange(item.LIMIT_MAX_NUM):
				(limitType, limitValue) = item.GetLimit(i)
				if item.LIMIT_LEVEL == limitType:
					self.levelLimit = limitValue
					break

			self.levelText.SetText(localeInfo.WIKI_REFINEINFO_ITEM_LEVEL % self.levelLimit)
			self.levelText.SetPosition(self.base.GetWidth() - self.levelText.GetTextSize()[0] - 8, 1 + 19 / 2 - self.levelText.GetTextSize()[1] / 2)
			self.levelText.Show()

			self.itemNameText = ui.TextLine()
			self.itemNameText.SetParent(self.base)
			itemName = item.GetItemName()
			fnd = itemName.find("+")
			if fnd >= 0:
				itemName = itemName[:fnd].strip()
			if enableDebugThings:
				self.itemNameText.SetText(itemName + " (%i)" % self.vnum)
			else:
				self.itemNameText.SetText(itemName)
			self.itemNameText.SetPosition(5, 1 + 19 / 2 - self.itemNameText.GetTextSize()[1] / 2)
			self.itemNameText.Show()

			self.itemImage = ui.ExpandedImageBox()
			self.itemImage.SetParent(self.base)
			self.itemImage.LoadImage(item.GetIconImageFileName())
			self.itemImage.SetPosition(1 + 47 / 2 - self.itemImage.GetWidth() / 2, 21 + 134 / 2 - self.itemImage.GetHeight() / 2)
			self.itemImage.Show()
			self.itemImage.SetStringEvent("MOUSE_OVER_IN",ui.__mem_func__( self.parent.OnOverIn), self.vnum + 9)
			self.itemImage.SetStringEvent("MOUSE_OVER_OUT",ui.__mem_func__( self.parent.OnOverOut))
			if wiki.GetBaseClass():
				self.itemImage.SetStringEvent("MOUSE_LEFT_DOWN", ui.__mem_func__(wiki.GetBaseClass().OpenSpecialPage), self.parent, self.vnum, False)

			self.SetSize(self.base.GetWidth(), self.base.GetHeight())

		def __del__(self):
			if wiki.GetBaseClass():
				wiki.GetBaseClass().objList.pop(long(id(self)))
			ui.Window.__del__(self)

		def NoticeMe(self):
			retInfo = wiki.GetRefineInfo(self.vnum)
			if not retInfo:
				return

			maxMat = 2
			moneyRow = 3
			useHeight = self.ROW_HEIGHTS
			useStart = self.ROW_START_Y
			for i in xrange(0, 9):
				curr = 0
				for j in retInfo[i][1]:
					if j[0] == 0:
						continue
					if curr >= 3:
						break
					curr += 1
				maxMat = max(maxMat, curr)

			if maxMat > 2:
				self.Set3Row()
				moneyRow = 4
				useHeight = self.ROW_HEIGHTS3
				useStart = self.ROW_START_Y3

			for i in xrange(0, 9):
				currWindow = self.cols[i+1]
				money = MakeMoneyText(retInfo[i][0])
				currWindow.moneyText.SetText(money)
				currWindow.moneyText.SetPosition(currWindow.GetWidth() / 2 - currWindow.moneyText.GetTextSize()[0] / 2, useStart[moneyRow] + useHeight[moneyRow] / 2 - currWindow.moneyText.GetTextSize()[1] / 2 - 1)

				curr = 0
				for j in retInfo[i][1]:
					if j[0] == 0:
						continue
					if curr >= maxMat:
						break

					item.SelectItem(1, 2, j[0])
					currImage = currWindow.refineMat[curr]
					currImage.LoadImage(item.GetIconImageFileName())
					currImage.SetPosition(currWindow.GetWidth() / 2 - currImage.GetWidth() / 2, useStart[curr + 1] + useHeight[curr + 1] / 2 - currImage.GetHeight() / 2)
					currImage.SetStringEvent("MOUSE_OVER_IN",ui.__mem_func__( self.parent.OnOverIn), j[0])
					currImage.SetStringEvent("MOUSE_OVER_OUT",ui.__mem_func__( self.parent.OnOverOut))

					currText = currWindow.refineMatText[curr]
					currText.SetFontColor(1.0, 1.0, 1.0)
					currText.SetText(j[1])
					currText.SetPosition(currImage.GetLocalPosition()[0] + currImage.GetWidth() - currText.GetTextSize()[0], currImage.GetLocalPosition()[1] + currImage.GetHeight() - currText.GetTextSize()[1])

					curr += 1

		def Set3Row(self):
			oldSize = self.base.GetHeight()
			self.base.LoadImage("d:/ymir work/ui/wiki/detail_item_2.tga") 
			self.SetSize(self.base.GetWidth(), self.base.GetHeight())

			for tmp in self.cols:
				tmp.SetSize(tmp.GetWidth(), 178)
				tmp.refineMat = []
				for j in xrange(3):
					img = ui.ExpandedImageBox()
					img.SetParent(tmp)
					img.Show()
					tmp.refineMat.append(img)

				tx = ui.TextLine()
				tx.SetParent(tmp)
				tx.SetText("-")
				tx.SetPosition(tmp.GetWidth() / 2 - tx.GetTextSize()[0] / 2, self.ROW_START_Y3[1] + self.ROW_HEIGHTS3[1] / 2 - tx.GetTextSize()[1] / 2 - 1)
				tx.Show()

				tmp.refineMatText = [tx]

				tx = ui.TextLine()
				tx.SetParent(tmp)
				tx.SetText("-")
				tx.SetPosition(tmp.GetWidth() / 2 - tx.GetTextSize()[0] / 2, self.ROW_START_Y3[2] + self.ROW_HEIGHTS3[2] / 2 - tx.GetTextSize()[1] / 2 - 1)
				tx.Show()

				tmp.refineMatText.append(tx)

				tx = ui.TextLine()
				tx.SetParent(tmp)
				tx.SetText("-")
				tx.SetPosition(tmp.GetWidth() / 2 - tx.GetTextSize()[0] / 2, self.ROW_START_Y3[3] + self.ROW_HEIGHTS3[3] / 2 - tx.GetTextSize()[1] / 2 - 1)
				tx.Show()

				tmp.refineMatText.append(tx)

				tx = ui.TextLine()
				tx.SetParent(tmp)
				tx.SetText("-")
				tx.SetPosition(tmp.GetWidth() / 2 - tx.GetTextSize()[0] / 2, self.ROW_START_Y3[4] + self.ROW_HEIGHTS3[4] / 2 - tx.GetTextSize()[1] / 2 - 1)
				tx.Show()

				tmp.moneyText = tx

			self.goldText.SetPosition(49 + 81 / 2 - self.goldText.GetTextSize()[0] / 2, 21 + self.ROW_START_Y3[4] + self.ROW_HEIGHTS3[4] / 2 - self.goldText.GetTextSize()[1] / 2 - 1)
			self.itemImage.SetPosition(1 + 47 / 2 - self.itemImage.GetWidth() / 2, 21 + 178 / 2 - self.itemImage.GetHeight() / 2)

			if self.parent:
				self.parent.ChangeElementSize(self, self.base.GetHeight() - oldSize)

		def OnRender(self):
			if not self.additionalLoaded:
				if wiki.IsSet(self.vnum) or not hasattr(self.parent, "loadFrom") or self.parent.loadFrom == self.parent.loadTo:
					self.additionalLoaded = True
					wiki.LoadInfo(long(id(self)), self.vnum)
		
	ELEM_PADDING = 5
	SCROLL_SPEED = 50
	ITEM_LOAD_PER_UPDATE = 1
	CLASS_BUTTONS = [
		[
			item.ITEM_ANTIFLAG_WARRIOR,
			"d:/ymir work/ui/wiki/class_w_normal.tga",
			"d:/ymir work/ui/wiki/class_w_hover.tga",
			"d:/ymir work/ui/wiki/class_w_selected.tga"
		],
		[
			item.ITEM_ANTIFLAG_ASSASSIN,
			"d:/ymir work/ui/wiki/class_n_normal.tga",
			"d:/ymir work/ui/wiki/class_n_hover.tga",
			"d:/ymir work/ui/wiki/class_n_selected.tga"
		],
		[
			item.ITEM_ANTIFLAG_SHAMAN,
			"d:/ymir work/ui/wiki/class_s_normal.tga",
			"d:/ymir work/ui/wiki/class_s_hover.tga",
			"d:/ymir work/ui/wiki/class_s_selected.tga"
		],
		[
			item.ITEM_ANTIFLAG_SURA,
			"d:/ymir work/ui/wiki/class_su_normal.tga",
			"d:/ymir work/ui/wiki/class_su_hover.tga",
			"d:/ymir work/ui/wiki/class_su_selected.tga"
		]
	]
	def __init__(self):
		super(WikiMainWeaponWindow, self).__init__()

		self.SetSize(mainBoardSize[0], mainBoardSize[1])

		self.elements = []
		self.isOpened = False
		self.scrollBar = None
		self.loadFrom = 0
		self.loadTo = 0
		self.currFlag = 0
		self.currCateg = 0
		self.toolTip = uiToolTip.ItemToolTip()

		self.peekWindow = ui.Window()
		self.peekWindow.SetParent(self)
		self.peekWindow.AddFlag("attach")
		self.peekWindow.AddFlag("not_pick")
		self.peekWindow.SetSize(541, self.GetHeight() - 50 - 10)
		self.peekWindow.SetPosition(5, 50)
		self.peekWindow.Show()
		self.peekWindow.SetInsideRender(True)

		self.categWindow = ui.Window()
		self.categWindow.SetParent(self)
		self.categWindow.AddFlag("attach")
		self.categWindow.AddFlag("not_pick")
		self.categWindow.Show()

		self.classBtns = []
		for i in self.CLASS_BUTTONS:
			tmp = ui.RadioButton()
			tmp.SetParent(self.categWindow)
			tmp.SetUpVisual(i[1])
			tmp.SetOverVisual(i[2])
			tmp.SetDownVisual(i[3])
			tmp.SetEvent(ui.__mem_func__(self.OnSelectCateg), proxy(tmp), i[0])
			tmp.Show()

			tmp.SetPosition(self.categWindow.GetWidth() + 5 * self.CLASS_BUTTONS.index(i), 0)
			self.categWindow.SetSize(self.categWindow.GetWidth() + tmp.GetWidth(), tmp.GetHeight())
			self.classBtns.append(tmp)

		self.categWindow.SetSize(self.categWindow.GetWidth() + 5 * (len(self.CLASS_BUTTONS) - 1), self.categWindow.GetHeight())
		self.categWindow.SetPosition(self.GetWidth() / 2 - self.categWindow.GetWidth() / 2, 10)

		self.scrollBoard = ui.Window()
		self.scrollBoard.SetParent(self.peekWindow)
		self.scrollBoard.AddFlag("attach")
		self.scrollBoard.AddFlag("not_pick")
		self.scrollBoard.Show()

		self.RegisterScrollBar()

	def OpenWindow(self):
		super(WikiMainWeaponWindow, self).Show()

	def Show(self, categID):
		super(WikiMainWeaponWindow, self).Show()
		isChanged = not categID == self.currCateg
		self.currCateg = categID
		if not self.isOpened:
			self.isOpened = True
			if len(self.classBtns):
				self.OnSelectCateg(proxy(self.classBtns[0]), self.CLASS_BUTTONS[0][0])
		else:
			self.loadTo = wiki.LoadClassItems(self.currCateg, self.currFlag)
			if self.loadFrom > self.loadTo or isChanged:
				del self.elements[:]
				self.scrollBoard.SetSize(0, 0)
				self.UpdateScrollbar()
				self.loadFrom = 0

	def OnOverIn(self, vnum):
		self.toolTip.ClearToolTip()
		self.toolTip.AddItemData(vnum, [0 for i in xrange(player.METIN_SOCKET_MAX_NUM)], 0)

	def OnOverOut(self):
		self.toolTip.Hide()

	def OnSelectCateg(self, btn, flag):
		self.currFlag = flag
		for i in self.classBtns:
			if proxy(i) != btn:
				i.SetUp()
			else:
				i.SetDown()

		del self.elements[:]
		self.scrollBoard.SetSize(0, 0)
		self.UpdateScrollbar()

		self.loadTo = wiki.LoadClassItems(self.currCateg, self.currFlag)
		self.loadFrom = 0

	def OnUpdate(self):
		if self.loadFrom < self.loadTo:
			for i in wiki.ChangePage(self.loadFrom, min(self.loadTo, self.loadFrom + self.ITEM_LOAD_PER_UPDATE)):
				self.AddItem(i)
				self.loadFrom += 1

	def ChangeElementSize(self, elem, sizeDiff):
		foundItem = False
		for i in self.elements:
			if elem != i and not foundItem:
				continue
			elif elem == i:
				foundItem = True
				continue

			i.SetPosition(i.GetLocalPosition()[0], i.GetLocalPosition()[1] + sizeDiff)

		if foundItem:
			self.scrollBoard.SetSize(elem.GetWidth(), self.scrollBoard.GetHeight() + sizeDiff)
			self.UpdateScrollbar()

	def AddItem(self, vnum):
		if vnum != 94326:
			vnum = int(vnum / 10) * 10
		for i in self.elements:
			if vnum == i.vnum:
				return None
		if not item.SelectItem(1, 2, vnum):
			return None

		tmp = self.WikiItem(vnum, self, True)
		tmp.SetParent(self.scrollBoard)
		tmp.AddFlag("attach")

		totalElem = len(self.elements)
		addPadding = 0
		if totalElem > 0:
			lastIndex = 0
			for i in xrange(totalElem):
				if self.elements[i].levelLimit < tmp.levelLimit or self.elements[i].levelLimit == tmp.levelLimit and self.elements[i].vnum < tmp.vnum:
					break
				lastIndex += 1

			self.elements.insert(lastIndex, tmp)
			totalElem += 1

			for i in xrange(lastIndex, totalElem):
				if i == 0:
					self.elements[i].SetPosition(0, 0)
				else:
					self.elements[i].SetPosition(0, self.elements[i - 1].GetLocalPosition()[1] + self.elements[i - 1].GetHeight() + self.ELEM_PADDING)					

			#tmp.SetPosition(0, self.elements[-1].GetLocalPosition()[1] + self.elements[-1].GetHeight() + self.ELEM_PADDING)
			addPadding = self.ELEM_PADDING

		else:
			self.elements.append(tmp)

		tmp.Show()
		self.scrollBoard.SetSize(tmp.GetWidth(), self.scrollBoard.GetHeight() + addPadding + tmp.GetHeight())
		self.UpdateScrollbar()
		return tmp

	def OnMouseWheel(self, length):
		if self.peekWindow.IsInPosition():
			self.UpdateScrollbar(length * self.SCROLL_SPEED)
			return True
		return False

	def OnScrollBar(self, fScale):
		curr = min(0, max(math.ceil((self.scrollBoard.GetHeight() - self.peekWindow.GetHeight()) * fScale * -1.0), -self.scrollBoard.GetHeight() + self.peekWindow.GetHeight()))
		self.scrollBoard.SetPosition(0, curr)

	def ChangeScrollbar(self):
		if self.scrollBar:
			if self.scrollBoard.GetHeight() <= self.GetHeight():
				self.scrollBar.Hide()
			else:
				self.scrollBar.SetScale(self.GetHeight() / self.scrollBoard.GetHeight())
				self.scrollBar.SetPosScale(abs(self.scrollBoard.GetLocalPosition()[1]) / (self.scrollBoard.GetHeight() - self.peekWindow.GetHeight()))
				self.scrollBar.Show()

	def UpdateScrollbar(self, val = 0):
		curr = min(0, max(self.scrollBoard.GetLocalPosition()[1] + val, -self.scrollBoard.GetHeight() + self.peekWindow.GetHeight()))
		self.scrollBoard.SetPosition(0, curr)
		self.ChangeScrollbar()

	def RegisterScrollBar(self):
		self.scrollBar = WikiScrollBar()
		self.scrollBar.SetParent(self)
		self.scrollBar.SetPosition(self.peekWindow.GetLocalPosition()[0] + self.peekWindow.GetWidth() + 1, self.peekWindow.GetLocalPosition()[1])
		self.scrollBar.SetSize(7, self.peekWindow.GetHeight())
		self.scrollBar.Show()

		self.scrollBar.SetScrollEvent(self.OnScrollBar)
		self.scrollBar.SetScrollSpeed(self.SCROLL_SPEED)
		self.ChangeScrollbar()

class ChestPeekWindow(ui.Window):
	ELEM_X_PADDING = 0
	ELEM_PADDING = 0
	SCROLL_SPEED = 25
	ELEM_PER_LINE = 11
	def __init__(self, parent, w, h, sendParent = True):
		ui.Window.__init__(self)

		self.SetSize(w, h)

		self.parent = proxy(parent)
		self.posMap = {}
		self.elements = []
		self.scrollBar = None
		self.mOverInEvent = None
		self.mOverOutEvent = None
		self.sendParent = sendParent

		self.peekWindow = ui.Window()
		self.peekWindow.SetParent(self)
		self.peekWindow.AddFlag("attach")
		self.peekWindow.AddFlag("not_pick")
		self.peekWindow.SetSize(w-6, self.GetHeight())
		self.peekWindow.SetPosition(0, 0)
		self.peekWindow.Show()

		self.scrollBoard = ui.Window()
		self.scrollBoard.SetParent(self.peekWindow)
		self.scrollBoard.AddFlag("attach")
		self.scrollBoard.AddFlag("not_pick")
		self.scrollBoard.Show()

	def AddItem(self, vnumFrom, vnumTo):
		if not self.scrollBar:
			self.RegisterScrollBar()
		metinSlot = [0 for i in xrange(player.METIN_SOCKET_MAX_NUM)]
		if vnumFrom == 8:
			vnumFrom = 70104
			metinSlot[0] = vnumTo
		if not item.SelectItem(1, 2, vnumFrom):
			return None

		tmp = ui.ExpandedImageBox()
		tmp.SetParent(self.scrollBoard)
		tmp.LoadImage(item.GetIconImageFileName())
		tmp.itemSize = item.GetItemSize()[1]
		tmp.SetStringEvent("MOUSE_OVER_IN", self.mOverInEvent, vnumFrom, metinSlot)
		tmp.SetStringEvent("MOUSE_OVER_OUT", self.mOverOutEvent)
		if (item.GetItemType() == item.ITEM_TYPE_WEAPON or item.GetItemType() == item.ITEM_TYPE_ARMOR) and wiki.GetBaseClass():
			if not self.sendParent:
				tmp.SetStringEvent("MOUSE_LEFT_DOWN", ui.__mem_func__(wiki.GetBaseClass().OpenSpecialPage), None, int(vnumFrom / 10) * 10, False)
			else:
				if hasattr(self.parent, "parent"):
					tmp.SetStringEvent("MOUSE_LEFT_DOWN", ui.__mem_func__(wiki.GetBaseClass().OpenSpecialPage), self.parent.parent, int(vnumFrom / 10) * 10, False)
				else:
					tmp.SetStringEvent("MOUSE_LEFT_DOWN", ui.__mem_func__(wiki.GetBaseClass().OpenSpecialPage), self.parent, int(vnumFrom / 10) * 10, False)
		tmp.vnum = vnumFrom

		totalElem = len(self.elements)
		if totalElem > 0:				
			#tmp.SetPosition(0, self.elements[-1].GetLocalPosition()[1] + self.elements[-1].GetHeight() + self.ELEM_PADDING)
			currAdd = 0
			while True:
				if currAdd in self.posMap:
					currAdd += 1
					continue
				break

			totalLine = currAdd % self.ELEM_PER_LINE
			currH = math.floor(currAdd / self.ELEM_PER_LINE) * (32 + self.ELEM_PADDING)

			for i in xrange(tmp.itemSize):
				self.posMap[currAdd + i * self.ELEM_PER_LINE] = True

			tmp.SetPosition(1 + totalLine * (36 + self.ELEM_X_PADDING), 0 + currH)

		else:
			for i in xrange(tmp.itemSize):
				self.posMap[i * self.ELEM_PER_LINE] = True

			tmp.SetPosition(1, 0)
		
		self.elements.append(tmp)

		tmp.Show()
		self.scrollBoard.SetSize(self.peekWindow.GetWidth(), max(self.scrollBoard.GetHeight(), tmp.GetLocalPosition()[1] + tmp.GetHeight()))
		self.UpdateScrollbar()
		return tmp

	def OnMouseWheel(self, length):
		if self.peekWindow.IsInPosition():
			if self.scrollBar and self.scrollBar.IsShow():
				self.UpdateScrollbar(length * self.SCROLL_SPEED)
				return True
		return False

	def OnScrollBar(self, fScale):
		curr = min(0, max(math.ceil((self.scrollBoard.GetHeight() - self.peekWindow.GetHeight()) * fScale * -1.0), -self.scrollBoard.GetHeight() + self.peekWindow.GetHeight()))
		self.scrollBoard.SetPosition(0, curr)

	def ChangeScrollbar(self):
		if self.scrollBar:
			if self.scrollBoard.GetHeight() <= self.GetHeight():
				self.scrollBar.Hide()
			else:
				self.scrollBar.SetScale(self.GetHeight() / self.scrollBoard.GetHeight())
				self.scrollBar.SetPosScale(abs(self.scrollBoard.GetLocalPosition()[1]) / (self.scrollBoard.GetHeight() - self.peekWindow.GetHeight()))
				self.scrollBar.Show()

	def UpdateScrollbar(self, val = 0):
		curr = min(0, max(self.scrollBoard.GetLocalPosition()[1] + val, -self.scrollBoard.GetHeight() + self.peekWindow.GetHeight()))
		self.scrollBoard.SetPosition(0, curr)
		self.ChangeScrollbar()

	def RegisterScrollBar(self):
		self.scrollBar = WikiScrollBar()
		self.scrollBar.SetParent(self)
		self.scrollBar.SetPosition(self.peekWindow.GetLocalPosition()[0] + self.peekWindow.GetWidth() + 1, self.peekWindow.GetLocalPosition()[1])
		self.scrollBar.SetSize(5, self.peekWindow.GetHeight())

		self.scrollBar.SetScrollEvent(self.OnScrollBar)
		self.scrollBar.SetScrollSpeed(self.SCROLL_SPEED)
		self.ChangeScrollbar()

class WikiMainChestWindow(ui.Window):
	class WikiItem(ui.Window):
		#this item is fucking dooomed (since I got the image in one piece)
		def __init__(self, vnum, parent):
			ui.Window.__init__(self)

			wikiBase = wiki.GetBaseClass()
			if id(self) not in wikiBase.objList:
				wikiBase.objList[long(id(self))] = proxy(self)

			self.additionalLoaded = False
			self.vnum = vnum
			self.parent = proxy(parent)

			self.base = ui.ExpandedImageBox()
			self.base.SetParent(self)
			self.base.AddFlag("attach")
			self.base.AddFlag("not_pick")
			self.base.LoadImage("d:/ymir work/ui/wiki/detail_chest.tga")
			self.base.Show()

			self.chestImage = ui.ExpandedImageBox()
			self.chestImage.SetParent(self.base)
			self.chestImage.LoadImage(item.GetIconImageFileName())
			self.chestImage.SetPosition(1 + 47 / 2 - self.chestImage.GetWidth() / 2, 1 + 87 / 2 - self.chestImage.GetHeight() / 2)
			self.chestImage.Show()

			self.chestImage.SetStringEvent("MOUSE_OVER_IN",ui.__mem_func__( self.parent.OnOverIn), self.vnum)
			self.chestImage.SetStringEvent("MOUSE_OVER_OUT",ui.__mem_func__( self.parent.OnOverOut))

			self.dropList = ChestPeekWindow(self, 401, 66)
			self.dropList.AddFlag("attach")
			self.dropList.SetParent(self.base)
			self.dropList.SetPosition(49, 22)
			self.dropList.Show()
			self.dropList.mOverInEvent = ui.__mem_func__(self.parent.OnOverIn)
			self.dropList.mOverOutEvent = ui.__mem_func__(self.parent.OnOverOut)

			self.originTextHead = ui.TextLine()
			self.originTextHead.SetParent(self.base)
			self.originTextHead.AddFlag("attach")
			self.originTextHead.AddFlag("not_pick")
			self.originTextHead.SetText(localeInfo.WIKI_CHESTINFO_ORIGIN)
			self.originTextHead.SetPosition(451 + 89 / 2 - self.originTextHead.GetTextSize()[0] / 2, 1 + 20 / 2 - self.originTextHead.GetTextSize()[1] / 2 - 1)
			self.originTextHead.Show()

			self.contentText = ui.TextLine()
			self.contentText.SetParent(self.base)
			self.contentText.AddFlag("attach")
			self.contentText.AddFlag("not_pick")
			if enableDebugThings:
				self.contentText.SetText("Content of %s (%i)" % (item.GetItemName(), self.vnum))
			else:
				self.contentText.SetText(localeInfo.WIKI_CHESTINFO_CONTENTOF % item.GetItemName())
			self.contentText.SetPosition(49 + 401 / 2 - self.contentText.GetTextSize()[0] / 2, 1 + 20 / 2 - self.contentText.GetTextSize()[1] / 2 - 1)
			self.contentText.Show()

			self.originText = ui.TextLine()
			self.originText.SetParent(self.base)
			self.originText.AddFlag("attach")
			self.originText.AddFlag("not_pick")
			self.originText.SetText("-")
			self.originText.SetPosition(451 + 89 / 2 - self.originText.GetTextSize()[0] / 2, 22 + 66 / 2 - self.originText.GetTextSize()[1] / 2 - 1)
			self.originText.Show()

			self.SetSize(self.base.GetWidth(), self.base.GetHeight())

		def __del__(self):
			if wiki.GetBaseClass():
				wiki.GetBaseClass().objList.pop(long(id(self)))
			ui.Window.__del__(self)

		def __GenerateMultiLine(self, text, maxWidth):
			currText = self.__GenerateSingleLine()
			textHolder = []

			tempText = ui.TextLine()
			tempText.Hide()
			
			splt = text.split(" ")
			currText.SetText(splt[0])
			splt = splt[1:]
			for i in splt:
				tempText.SetText(" " + i)
				if tempText.GetTextWidth() + currText.GetTextWidth() > maxWidth:
					currText.AdjustSize()
					textHolder.append(currText)
					currText = self.__GenerateSingleLine()
					currText.SetText(i)
				else:
					currText.SetText(currText.GetText() + " " + i)

			textHolder.append(currText)
			return textHolder

		def __GenerateSingleLine(self):
			text = ui.TextLine()
			text.SetParent(self.base)
			text.Show()
			return text

		def NoticeMe(self):
			ret = wiki.GetChestInfo(self.vnum)
			if len(ret) == 2:
				(dwOrigin, isCommon) = ret
			else:
				(dwOrigin, isCommon, lst) = ret

			self.originText.Hide()
			self.multiHolder = []
			if self.vnum in ORIGIN_MAP:
				self.multiHolder = self.__GenerateMultiLine(ORIGIN_MAP[self.vnum], 66)
			elif isCommon:
				self.multiHolder = self.__GenerateMultiLine(localeInfo.WIKI_CHESTINFO_COMMON_DROP, 66)
			elif dwOrigin:
				self.multiHolder = self.__GenerateMultiLine(nonplayer.GetMonsterName(dwOrigin), 66)
			else:
				self.originText.SetPosition(451 + 89 / 2 - self.originText.GetTextSize()[0] / 2, 22 + 66 / 2 - self.originText.GetTextSize()[1] / 2 - 1)
				self.originText.Show()

			for i in self.multiHolder:
				totalH = self.multiHolder[0].GetTextSize()[1] * len(self.multiHolder) + 3 * (len(self.multiHolder) - 1)
				i.SetPosition(451 + 89 / 2 - i.GetTextSize()[0] / 2, 22 + 66 / 2 - totalH / 2 + 3 * self.multiHolder.index(i) + i.GetTextSize()[1] * self.multiHolder.index(i))

			if len(ret) < 3:
				return

			sizeLst = []
			orderedLst = []
			otherStuff = []
			for i in lst:
				if i[0] < 10:
					otherStuff.append(i[:])
					continue

				for j in xrange(i[0], i[1] + 1):
					lastPos = 0
					size = 0
					if item.SelectItem(1, 2, j):
						size = item.GetItemSize()[1]

					for k in xrange(len(sizeLst)):
						if sizeLst[k] < size:
							break
						lastPos += 1

					sizeLst.insert(lastPos, size)
					orderedLst.insert(lastPos, j)


			for i in orderedLst:
				self.dropList.AddItem(i, 0)

			for i in otherStuff:
				self.dropList.AddItem(i[0], i[1])

		def OnRender(self):
			if not self.additionalLoaded:
				if wiki.IsSet(self.vnum) or self.parent.loadFrom == self.parent.loadTo:
					self.additionalLoaded = True
					wiki.LoadInfo(long(id(self)), self.vnum)
		
	ELEM_PADDING = 5
	SCROLL_SPEED = 50
	ITEM_LOAD_PER_UPDATE = 1
	def __init__(self):
		super(WikiMainChestWindow, self).__init__()

		self.SetSize(mainBoardSize[0], mainBoardSize[1])

		self.elements = []
		self.isOpened = False
		self.scrollBar = None
		self.loadFrom = 0
		self.loadTo = 0
		self.chestVnums = []
		self.toolTip = uiToolTip.ItemToolTip()

		self.peekWindow = ui.Window()
		self.peekWindow.SetParent(self)
		self.peekWindow.AddFlag("attach")
		self.peekWindow.AddFlag("not_pick")
		self.peekWindow.SetSize(541, self.GetHeight() - 15)
		self.peekWindow.SetPosition(5, 5)
		self.peekWindow.Show()
		self.peekWindow.SetInsideRender(True)

		self.scrollBoard = ui.Window()
		self.scrollBoard.SetParent(self.peekWindow)
		self.scrollBoard.AddFlag("attach")
		self.scrollBoard.AddFlag("not_pick")
		self.scrollBoard.Show()

		self.RegisterScrollBar()

	def OpenWindow(self):
		super(WikiMainChestWindow, self).Show()

	def Show(self, vnums):
		super(WikiMainChestWindow, self).Show()

		isChanged = not len(vnums) == len(self.chestVnums)
		if not isChanged:
			for i in vnums:
				if i not in self.chestVnums:
					isChanged = True
					break

		if not isChanged:
			for i in self.chestVnums:
				if i not in vnums:
					isChanged = True
					break

		if not len(vnums) and enableDebugThings:
			self.loadTo = wiki.LoadClassItems(8, 0)
			del self.chestVnums[:]
		else:
			self.chestVnums = vnums[:]
			self.loadTo = len(self.chestVnums)

		if not self.isOpened:
			self.isOpened = True
			self.loadFrom = 0

		if self.loadFrom > self.loadTo or isChanged:
			del self.elements[:]
			self.loadFrom = 0
			self.scrollBoard.SetSize(0, 0)
			self.UpdateScrollbar()

	def OnOverIn(self, vnum, metinSlot = [0 for i in xrange(player.METIN_SOCKET_MAX_NUM)]):
		self.toolTip.ClearToolTip()
		self.toolTip.AddItemData(vnum, metinSlot, 0)

	def OnOverOut(self):
		self.toolTip.Hide()

	def OnUpdate(self):
		if self.loadFrom < self.loadTo:
			if not len(self.chestVnums) and enableDebugThings:
				for i in wiki.ChangePage(self.loadFrom, min(self.loadTo, self.loadFrom + self.ITEM_LOAD_PER_UPDATE)):
					self.AddItem(i)
					self.loadFrom += 1
			else:
				for i in xrange(self.loadFrom, min(self.loadTo, self.loadFrom + self.ITEM_LOAD_PER_UPDATE)):
					self.AddItem(self.chestVnums[i])
					self.loadFrom += 1

	def AddItem(self, vnum):
		for i in self.elements:
			if vnum == i.vnum:
				return None
		if not item.SelectItem(1, 2, vnum):
			return None

		tmp = self.WikiItem(vnum, self)
		tmp.SetParent(self.scrollBoard)
		tmp.AddFlag("attach")

		totalElem = len(self.elements)
		addPadding = 0
		if totalElem > 0:
			lastIndex = totalElem
			"""for i in xrange(totalElem):
				if self.elements[i].vnum < tmp.vnum:
					break
				lastIndex += 1"""

			self.elements.insert(lastIndex, tmp)
			totalElem += 1

			for i in xrange(lastIndex, totalElem):
				if i == 0:
					self.elements[i].SetPosition(0, 0)
				else:
					self.elements[i].SetPosition(0, self.elements[i - 1].GetLocalPosition()[1] + self.elements[i - 1].GetHeight() + self.ELEM_PADDING)					

			#tmp.SetPosition(0, self.elements[-1].GetLocalPosition()[1] + self.elements[-1].GetHeight() + self.ELEM_PADDING)
			addPadding = self.ELEM_PADDING

		else:
			self.elements.append(tmp)

		tmp.Show()
		self.scrollBoard.SetSize(tmp.GetWidth(), self.scrollBoard.GetHeight() + addPadding + tmp.GetHeight())
		self.UpdateScrollbar()
		return tmp

	def OnMouseWheel(self, length):
		if self.peekWindow.IsInPosition():
			self.UpdateScrollbar(length * self.SCROLL_SPEED)
			return True
		return False

	def OnScrollBar(self, fScale):
		curr = min(0, max(math.ceil((self.scrollBoard.GetHeight() - self.peekWindow.GetHeight()) * fScale * -1.0), -self.scrollBoard.GetHeight() + self.peekWindow.GetHeight()))
		self.scrollBoard.SetPosition(0, curr)

	def ChangeScrollbar(self):
		if self.scrollBar:
			if self.scrollBoard.GetHeight() <= self.GetHeight():
				self.scrollBar.Hide()
			else:
				self.scrollBar.SetScale(self.GetHeight() / self.scrollBoard.GetHeight())
				self.scrollBar.SetPosScale(abs(self.scrollBoard.GetLocalPosition()[1]) / (self.scrollBoard.GetHeight() - self.peekWindow.GetHeight()))
				self.scrollBar.Show()

	def UpdateScrollbar(self, val = 0):
		curr = min(0, max(self.scrollBoard.GetLocalPosition()[1] + val, -self.scrollBoard.GetHeight() + self.peekWindow.GetHeight()))
		self.scrollBoard.SetPosition(0, curr)
		self.ChangeScrollbar()

	def RegisterScrollBar(self):
		self.scrollBar = WikiScrollBar()
		self.scrollBar.SetParent(self)
		self.scrollBar.SetPosition(self.peekWindow.GetLocalPosition()[0] + self.peekWindow.GetWidth() + 1, self.peekWindow.GetLocalPosition()[1])
		self.scrollBar.SetSize(7, self.peekWindow.GetHeight())
		self.scrollBar.Show()

		self.scrollBar.SetScrollEvent(self.OnScrollBar)
		self.scrollBar.SetScrollSpeed(self.SCROLL_SPEED)
		self.ChangeScrollbar()

class WikiMainBossWindow(ui.Window):
	class WikiItem(ui.Window):
		#this item is fucking dooomed (since I got the image in one piece)
		def __init__(self, vnum, parent):
			ui.Window.__init__(self)

			wikiBase = wiki.GetBaseClass()
			if id(self) not in wikiBase.objList:
				wikiBase.objList[long(id(self))] = proxy(self)

			self.additionalLoaded = False
			self.vnum = vnum
			self.parent = proxy(parent)

			self.base = ui.ExpandedImageBox()
			self.base.SetParent(self)
			self.base.AddFlag("attach")
			self.base.AddFlag("not_pick")
			self.base.LoadImage("d:/ymir work/ui/wiki/detail_chest.tga")
			self.base.Show()

			self.modelView = WikiRenderTarget(47, 87)
			self.modelView.SetParent(self.base)
			self.modelView.SetPosition(1 + 47 / 2 - self.modelView.GetWidth() / 2, 1 + 87 / 2 - self.modelView.GetHeight() / 2)
			if wiki.GetBaseClass():
				self.modelView.SetMouseLeftButtonDownEvent(ui.__mem_func__(wiki.GetBaseClass().OpenSpecialPage), self.parent, self.vnum, True)

			self.dropList = ChestPeekWindow(self, 401, 66)
			self.dropList.AddFlag("attach")
			self.dropList.SetParent(self.base)
			self.dropList.SetPosition(49, 22)
			self.dropList.Show()
			self.dropList.mOverInEvent = ui.__mem_func__(self.parent.OnOverIn)
			self.dropList.mOverOutEvent = ui.__mem_func__(self.parent.OnOverOut)

			self.originTextHead = ui.TextLine()
			self.originTextHead.SetParent(self.base)
			self.originTextHead.AddFlag("attach")
			self.originTextHead.AddFlag("not_pick")
			self.originTextHead.SetText(localeInfo.WIKI_CHESTINFO_ORIGIN)
			self.originTextHead.SetPosition(451 + 89 / 2 - self.originTextHead.GetTextSize()[0] / 2, 1 + 20 / 2 - self.originTextHead.GetTextSize()[1] / 2 - 1)
			self.originTextHead.Show()

			self.contentText = ui.TextLine()
			self.contentText.SetParent(self.base)
			self.contentText.AddFlag("attach")
			self.contentText.AddFlag("not_pick")
			if enableDebugThings:
				self.contentText.SetText("Droplist of %s (%i)" % (nonplayer.GetMonsterName(self.vnum), self.vnum))
			else:
				self.contentText.SetText(localeInfo.WIKI_MONSTERINFO_DROPLISTOF % nonplayer.GetMonsterName(self.vnum))
			self.contentText.SetPosition(49 + 401 / 2 - self.contentText.GetTextSize()[0] / 2, 1 + 20 / 2 - self.contentText.GetTextSize()[1] / 2 - 1)
			self.contentText.Show()

			self.originText = ui.TextLine()
			self.originText.SetParent(self.base)
			self.originText.AddFlag("attach")
			self.originText.AddFlag("not_pick")
			self.originText.SetText("-")
			self.originText.SetPosition(451 + 89 / 2 - self.originText.GetTextSize()[0] / 2, 22 + 66 / 2 - self.originText.GetTextSize()[1] / 2 - 1)
			self.originText.Show()

			self.SetSize(self.base.GetWidth(), self.base.GetHeight())

		def __del__(self):
			if wiki.GetBaseClass():
				wiki.GetBaseClass().objList.pop(long(id(self)))
			ui.Window.__del__(self)

		def __GenerateMultiLine(self, text, maxWidth):
			currText = self.__GenerateSingleLine()
			textHolder = []

			tempText = ui.TextLine()
			tempText.Hide()
			
			splt = text.split(" ")
			currText.SetText(splt[0])
			splt = splt[1:]
			for i in splt:
				tempText.SetText(" " + i)
				if tempText.GetTextWidth() + currText.GetTextWidth() > maxWidth:
					currText.AdjustSize()
					textHolder.append(currText)
					currText = self.__GenerateSingleLine()
					currText.SetText(i)
				else:
					currText.SetText(currText.GetText() + " " + i)

			textHolder.append(currText)
			return textHolder

		def __GenerateSingleLine(self):
			text = ui.TextLine()
			text.SetParent(self.base)
			text.Show()
			return text

		def NoticeMe(self):
			lst = wiki.GetMobInfo(self.vnum)

			self.originText.Hide()
			self.multiHolder = []
			if self.vnum in MOB_ORIGIN_MAP:
				self.multiHolder = self.__GenerateMultiLine(MOB_ORIGIN_MAP[self.vnum], 66)
			else:
				self.originText.SetPosition(451 + 89 / 2 - self.originText.GetTextSize()[0] / 2, 22 + 66 / 2 - self.originText.GetTextSize()[1] / 2 - 1)
				self.originText.Show()

			for i in self.multiHolder:
				totalH = self.multiHolder[0].GetTextSize()[1] * len(self.multiHolder) + 3 * (len(self.multiHolder) - 1)
				i.SetPosition(451 + 89 / 2 - i.GetTextSize()[0] / 2, 22 + 66 / 2 - totalH / 2 + 3 * self.multiHolder.index(i) + i.GetTextSize()[1] * self.multiHolder.index(i))

			if not lst:
				return

			sizeLst = []
			orderedLst = []
			for i in lst:
				if i < 10:
					continue

				for j in xrange(i, i + 1):
					if j in orderedLst:
						continue
					lastPos = 0
					size = 0
					if item.SelectItem(1, 2, j):
						size = item.GetItemSize()[1]

					for k in xrange(len(sizeLst)):
						if sizeLst[k] < size:
							break
						lastPos += 1

					sizeLst.insert(lastPos, size)
					orderedLst.insert(lastPos, j)


			for i in orderedLst:
				self.dropList.AddItem(i, 0)

		def OnRender(self):
			if not self.additionalLoaded:
				if wiki.IsSet(self.vnum, True) or self.parent.loadFrom == self.parent.loadTo:
					self.additionalLoaded = True
					self.modelView.SetModel(self.vnum)
					self.modelView.Show()
					wiki.LoadInfo(long(id(self)), self.vnum, True)
		
	ELEM_PADDING = 5
	SCROLL_SPEED = 50
	ITEM_LOAD_PER_UPDATE = 2
	def __init__(self):
		super(WikiMainBossWindow, self).__init__()

		self.SetSize(mainBoardSize[0], mainBoardSize[1])

		self.elements = []
		self.isOpened = False
		self.scrollBar = None
		self.loadFrom = 0
		self.loadTo = 0
		self.mobtypes = 0
		self.fromlvl = 0
		self.tolvl = 0
		self.toolTip = uiToolTip.ItemToolTip()

		self.peekWindow = ui.Window()
		self.peekWindow.SetParent(self)
		self.peekWindow.AddFlag("attach")
		self.peekWindow.AddFlag("not_pick")
		self.peekWindow.SetSize(541, self.GetHeight() - 15)
		self.peekWindow.SetPosition(5, 5)
		self.peekWindow.Show()
		self.peekWindow.SetInsideRender(True)

		self.scrollBoard = ui.Window()
		self.scrollBoard.SetParent(self.peekWindow)
		self.scrollBoard.AddFlag("attach")
		self.scrollBoard.AddFlag("not_pick")
		self.scrollBoard.Show()

		self.RegisterScrollBar()

	def OpenWindow(self):
		super(WikiMainBossWindow, self).Show()

	def Show(self, mobtypes, fromlvl, tolvl):
		super(WikiMainBossWindow, self).Show()
		isChanged = False
		if not (mobtypes == self.mobtypes and fromlvl == self.fromlvl and tolvl == self.tolvl):
			isChanged = True
		self.mobtypes = mobtypes
		self.fromlvl = fromlvl
		self.tolvl = tolvl

		self.loadTo = wiki.LoadClassMobs(mobtypes, fromlvl, tolvl)
		if not self.isOpened:
			self.isOpened = True
			self.loadFrom = 0

		if self.loadFrom > self.loadTo or isChanged:
			del self.elements[:]
			self.loadFrom = 0
			self.scrollBoard.SetSize(0, 0)
			self.UpdateScrollbar()

	def Hide(self):
		super(WikiMainBossWindow, self).Hide()

	def OnOverIn(self, vnum, metinSlot = [0 for i in xrange(player.METIN_SOCKET_MAX_NUM)]):
		self.toolTip.ClearToolTip()
		self.toolTip.AddItemData(vnum, metinSlot, 0)

	def OnOverOut(self):
		self.toolTip.Hide()

	def OnUpdate(self):
		if self.loadFrom < self.loadTo:
			for i in wiki.ChangePage(self.loadFrom, min(self.loadTo, self.loadFrom + self.ITEM_LOAD_PER_UPDATE), True):
				self.AddItem(i)
				self.loadFrom += 1

	def AddItem(self, vnum):
		for i in self.elements:
			if vnum == i.vnum:
				return None

		tmp = self.WikiItem(vnum, self)
		tmp.SetParent(self.scrollBoard)
		tmp.AddFlag("attach")

		totalElem = len(self.elements)
		addPadding = 0
		if totalElem > 0:
			lastIndex = 0
			for i in xrange(totalElem):
				if self.elements[i].vnum < tmp.vnum:
					break
				lastIndex += 1

			self.elements.insert(lastIndex, tmp)
			totalElem += 1

			for i in xrange(lastIndex, totalElem):
				if i == 0:
					self.elements[i].SetPosition(0, 0)
				else:
					self.elements[i].SetPosition(0, self.elements[i - 1].GetLocalPosition()[1] + self.elements[i - 1].GetHeight() + self.ELEM_PADDING)					

			#tmp.SetPosition(0, self.elements[-1].GetLocalPosition()[1] + self.elements[-1].GetHeight() + self.ELEM_PADDING)
			addPadding = self.ELEM_PADDING

		else:
			self.elements.append(tmp)

		tmp.Show()
		self.scrollBoard.SetSize(tmp.GetWidth(), self.scrollBoard.GetHeight() + addPadding + tmp.GetHeight())
		self.UpdateScrollbar()
		return tmp

	def OnMouseWheel(self, length):
		if self.peekWindow.IsInPosition():
			self.UpdateScrollbar(length * self.SCROLL_SPEED)
			return True
		return False

	def OnScrollBar(self, fScale):
		curr = min(0, max(math.ceil((self.scrollBoard.GetHeight() - self.peekWindow.GetHeight()) * fScale * -1.0), -self.scrollBoard.GetHeight() + self.peekWindow.GetHeight()))
		self.scrollBoard.SetPosition(0, curr)

	def ChangeScrollbar(self):
		if self.scrollBar:
			if self.scrollBoard.GetHeight() <= self.GetHeight():
				self.scrollBar.Hide()
			else:
				self.scrollBar.SetScale(self.GetHeight() / self.scrollBoard.GetHeight())
				self.scrollBar.SetPosScale(abs(self.scrollBoard.GetLocalPosition()[1]) / (self.scrollBoard.GetHeight() - self.peekWindow.GetHeight()))
				self.scrollBar.Show()

	def UpdateScrollbar(self, val = 0):
		curr = min(0, max(self.scrollBoard.GetLocalPosition()[1] + val, -self.scrollBoard.GetHeight() + self.peekWindow.GetHeight()))
		self.scrollBoard.SetPosition(0, curr)
		self.ChangeScrollbar()

	def RegisterScrollBar(self):
		self.scrollBar = WikiScrollBar()
		self.scrollBar.SetParent(self)
		self.scrollBar.SetPosition(self.peekWindow.GetLocalPosition()[0] + self.peekWindow.GetWidth() + 1, self.peekWindow.GetLocalPosition()[1])
		self.scrollBar.SetSize(7, self.peekWindow.GetHeight())
		self.scrollBar.Show()

		self.scrollBar.SetScrollEvent(self.OnScrollBar)
		self.scrollBar.SetScrollSpeed(self.SCROLL_SPEED)
		self.ChangeScrollbar()

class WikiMonsterBonusInfoWindow(ui.Window):
	ELEM_PADDING = 5
	SCROLL_SPEED = 50
	ITEM_LOAD_PER_UPDATE = 2

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
	IMMUNE_FLAG_TO_NAME = {
		nonplayer.IMMUNE_STUN : localeInfo.WIKI_MONSTERINFO_IMMUNE_STUN,
		nonplayer.IMMUNE_SLOW : localeInfo.WIKI_MONSTERINFO_IMMUNE_SLOW,
		nonplayer.IMMUNE_FALL : localeInfo.WIKI_MONSTERINFO_IMMUNE_FALL,
		nonplayer.IMMUNE_CURSE : localeInfo.WIKI_MONSTERINFO_IMMUNE_CURSE,
		nonplayer.IMMUNE_POISON : localeInfo.WIKI_MONSTERINFO_IMMUNE_POISON,
		nonplayer.IMMUNE_TERROR : localeInfo.WIKI_MONSTERINFO_IMMUNE_TERROR,
		nonplayer.IMMUNE_REFLECT : localeInfo.WIKI_MONSTERINFO_IMMUNE_REFLECT,
	}
	def __init__(self, vnum):
		super(WikiMonsterBonusInfoWindow, self).__init__()

		self.SetSize(539, 157)
		self.vnum = vnum

		self.elements = []
		self.scrollBar = None

		self.peekWindow = ui.Window()
		self.peekWindow.SetParent(self)
		self.peekWindow.AddFlag("attach")
		self.peekWindow.AddFlag("not_pick")
		self.peekWindow.SetSize(self.GetWidth() - 8 - 6, self.GetHeight() - 6)
		self.peekWindow.SetPosition(3, 3)
		self.peekWindow.Show()
		self.peekWindow.SetInsideRender(True)

		self.scrollBoard = ui.Window()
		self.scrollBoard.SetParent(self.peekWindow)
		self.scrollBoard.AddFlag("attach")
		self.scrollBoard.AddFlag("not_pick")
		self.scrollBoard.Show()

		self.AddItem(localeInfo.WIKI_MONSTERINFO_LEVEL % nonplayer.GetMonsterLevel(self.vnum))
		(mainrace, subrace) = self.GetRaceStrings()
		self.AddItem(localeInfo.TARGET_INFO_MAINRACE % mainrace + " | " + localeInfo.TARGET_INFO_SUBRACE % subrace)
		self.AddItem(localeInfo.WIKI_MONSTERINFO_IMMUNE_TO % self.GetImmuneString())
		(damageMin, damageMax) = nonplayer.GetMonsterDamage(self.vnum)
		damageMin = localeInfo.NumberToMoneyString(damageMin, False)
		damageMax = localeInfo.NumberToMoneyString(damageMax, False)
		self.AddItem(localeInfo.WIKI_MONSTERINFO_DMG_HP % (damageMin, damageMax, localeInfo.NumberToMoneyString(nonplayer.GetMonsterMaxHP(self.vnum), False)))
		(goldMin, goldMax) = nonplayer.GetMonsterGold(self.vnum)
		goldMin = localeInfo.NumberToMoneyString(goldMin, False)
		goldMax = localeInfo.NumberToMoneyString(goldMax, False)
		self.AddItem(localeInfo.WIKI_MONSTERINFO_GOLD_EXP % (goldMin, goldMax, localeInfo.NumberToMoneyString(nonplayer.GetMonsterExp(self.vnum), False)))
		self.AddItem(localeInfo.WIKI_MONSTERINFO_RESISTANCES)
		self.AddItem(uiToolTip.GET_AFFECT_STRING(item.APPLY_RESIST_SWORD, nonplayer.GetMonsterResistValue(self.vnum, nonplayer.MOB_RESIST_SWORD)), 10)
		self.AddItem(uiToolTip.GET_AFFECT_STRING(item.APPLY_RESIST_TWOHAND, nonplayer.GetMonsterResistValue(self.vnum, nonplayer.MOB_RESIST_TWOHAND)), 10)
		self.AddItem(uiToolTip.GET_AFFECT_STRING(item.APPLY_RESIST_DAGGER, nonplayer.GetMonsterResistValue(self.vnum, nonplayer.MOB_RESIST_DAGGER)), 10)
		self.AddItem(uiToolTip.GET_AFFECT_STRING(item.APPLY_RESIST_BELL, nonplayer.GetMonsterResistValue(self.vnum, nonplayer.MOB_RESIST_BELL)), 10)
		self.AddItem(uiToolTip.GET_AFFECT_STRING(item.APPLY_RESIST_FAN, nonplayer.GetMonsterResistValue(self.vnum, nonplayer.MOB_RESIST_FAN)), 10)
		self.AddItem(uiToolTip.GET_AFFECT_STRING(item.APPLY_RESIST_BOW, nonplayer.GetMonsterResistValue(self.vnum, nonplayer.MOB_RESIST_BOW)), 10)

		self.RegisterScrollBar()

	def GetImmuneString(self):
		dwImmuneFlag = nonplayer.GetMonsterImmuneFlag(self.vnum)
		immuneflags = ""

		for i in xrange(nonplayer.IMMUNE_FLAG_MAX_NUM):
			curFlag = 1 << i
			if HAS_FLAG(dwImmuneFlag, curFlag):
				if self.IMMUNE_FLAG_TO_NAME.has_key(curFlag):
					immuneflags += self.IMMUNE_FLAG_TO_NAME[curFlag] + ", "

		if immuneflags == "":
			immuneflags = localeInfo.WIKI_MONSTERINFO_IMMUNE_NOTHING
		else:
			immuneflags = immuneflags[:-2]

		return immuneflags

	def GetRaceStrings(self):
		dwRaceFlag = nonplayer.GetMonsterRaceFlag(self.vnum)
		mainrace = ""
		subrace = ""
		for i in xrange(nonplayer.RACE_FLAG_MAX_NUM):
			curFlag = 1 << i
			if HAS_FLAG(dwRaceFlag, curFlag):
				if self.RACE_FLAG_TO_NAME.has_key(curFlag):
					mainrace += self.RACE_FLAG_TO_NAME[curFlag] + ", "
				elif self.SUB_RACE_FLAG_TO_NAME.has_key(curFlag):
					subrace += self.SUB_RACE_FLAG_TO_NAME[curFlag] + ", "
		if nonplayer.IsMonsterStone(self.vnum):
			mainrace += localeInfo.TARGET_INFO_RACE_METIN + ", "
		if mainrace == "":
			mainrace = localeInfo.TARGET_INFO_NO_RACE
		else:
			mainrace = mainrace[:-2]
		if subrace == "":
			subrace = localeInfo.TARGET_INFO_NO_RACE
		else:
			subrace = subrace[:-2]

		return (mainrace, subrace)

	def AddItem(self, text, padding = 0):
		tmp = ui.Window()
		tmp.SetParent(self.scrollBoard)
		tmp.AddFlag("attach")
		tmp.SetSize(self.GetWidth() - 8, 15)

		img = ui.ExpandedImageBox()
		img.SetParent(tmp)
		img.AddFlag("attach")
		img.AddFlag("not_pick")
		img.LoadImage("d:/ymir work/ui/wiki/arrow_2.tga")
		img.SetPosition(padding, tmp.GetHeight() / 2 - img.GetHeight() / 2)
		img.Show()
		tmp.img = img

		txt = ui.TextLine()
		txt.SetParent(tmp)
		txt.AddFlag("attach")
		txt.AddFlag("not_pick")
		fnt = constInfo.GetChoosenFontName().split(":")
		txt.SetFontName(fnt[0] +":"+ str(int(fnt[1]) + 2))
		txt.SetText(text)
		txt.SetPosition(img.GetLocalPosition()[0] + img.GetWidth() + 5, tmp.GetHeight() / 2 - txt.GetTextSize()[1] / 2 - 1)
		txt.Show()
		tmp.txt = txt

		totalElem = len(self.elements)
		addPadding = 0
		if totalElem > 0:
			lastIndex = totalElem

			self.elements.insert(lastIndex, tmp)
			totalElem += 1

			for i in xrange(lastIndex, totalElem):
				if i == 0:
					self.elements[i].SetPosition(0, 0)
				else:
					self.elements[i].SetPosition(0, self.elements[i - 1].GetLocalPosition()[1] + self.elements[i - 1].GetHeight() + self.ELEM_PADDING)					

			#tmp.SetPosition(0, self.elements[-1].GetLocalPosition()[1] + self.elements[-1].GetHeight() + self.ELEM_PADDING)
			addPadding = self.ELEM_PADDING

		else:
			self.elements.append(tmp)

		tmp.Show()
		self.scrollBoard.SetSize(tmp.GetWidth(), self.scrollBoard.GetHeight() + addPadding + tmp.GetHeight())
		self.UpdateScrollbar()
		return tmp

	def OnMouseWheel(self, length):
		if self.peekWindow.IsInPosition():
			self.UpdateScrollbar(length * self.SCROLL_SPEED)
			return True
		return False

	def OnScrollBar(self, fScale):
		curr = min(0, max(math.ceil((self.scrollBoard.GetHeight() - self.peekWindow.GetHeight()) * fScale * -1.0), -self.scrollBoard.GetHeight() + self.peekWindow.GetHeight()))
		self.scrollBoard.SetPosition(0, curr)

	def ChangeScrollbar(self):
		if self.scrollBar:
			if self.scrollBoard.GetHeight() <= self.GetHeight():
				self.scrollBar.Hide()
			else:
				self.scrollBar.SetScale(self.GetHeight() / self.scrollBoard.GetHeight())
				self.scrollBar.SetPosScale(abs(self.scrollBoard.GetLocalPosition()[1]) / (self.scrollBoard.GetHeight() - self.peekWindow.GetHeight()))
				self.scrollBar.Show()

	def UpdateScrollbar(self, val = 0):
		curr = min(0, max(self.scrollBoard.GetLocalPosition()[1] + val, -self.scrollBoard.GetHeight() + self.peekWindow.GetHeight()))
		self.scrollBoard.SetPosition(0, curr)
		self.ChangeScrollbar()

	def RegisterScrollBar(self):
		self.scrollBar = WikiScrollBar()
		self.scrollBar.SetParent(self)
		self.scrollBar.SetPosition(self.peekWindow.GetLocalPosition()[0] + self.peekWindow.GetWidth() + 1, self.peekWindow.GetLocalPosition()[1])
		self.scrollBar.SetSize(7, self.peekWindow.GetHeight())
		self.scrollBar.Show()

		self.scrollBar.SetScrollEvent(self.OnScrollBar)
		self.scrollBar.SetScrollSpeed(self.SCROLL_SPEED)
		self.ChangeScrollbar()

class WikiItemOriginInfo(ui.Window):
	ELEM_PADDING = 5
	SCROLL_SPEED = 50
	ITEM_LOAD_PER_UPDATE = 2

	def __init__(self, vnum):
		super(WikiItemOriginInfo, self).__init__()

		self.SetSize(351, 142)
		self.vnum = vnum

		self.elements = []
		self.scrollBar = None

		self.peekWindow = ui.Window()
		self.peekWindow.SetParent(self)
		self.peekWindow.AddFlag("attach")
		self.peekWindow.AddFlag("not_pick")
		self.peekWindow.SetSize(self.GetWidth() - 8 - 6, self.GetHeight() - 6)
		self.peekWindow.SetPosition(3, 3)
		self.peekWindow.Show()
		self.peekWindow.SetInsideRender(True)

		self.scrollBoard = ui.Window()
		self.scrollBoard.SetParent(self.peekWindow)
		self.scrollBoard.AddFlag("attach")
		self.scrollBoard.AddFlag("not_pick")
		self.scrollBoard.Show()

		self.RegisterScrollBar()

	def ParseTextlines(self):
		lst = wiki.GetOriginInfo(self.vnum)
		if not lst:
			return

		alreadyParsed = []

		for (vnum, isMonster) in lst:
			bAlready = False
			for i in alreadyParsed:
				if i[0] == vnum and i[1] == isMonster:
					bAlready = True
					break
			if bAlready:
				continue
			if isMonster:
				currName = nonplayer.GetMonsterName(vnum)
			else:
				item.SelectItem(1, 2, vnum)
				currName = item.GetItemName()

			alreadyParsed.append([vnum, isMonster])
			self.AddItem(currName)


	def AddItem(self, text, padding = 0):
		tmp = ui.Window()
		tmp.SetParent(self.scrollBoard)
		tmp.AddFlag("attach")
		tmp.SetSize(self.GetWidth() - 8, 15)

		img = ui.ExpandedImageBox()
		img.SetParent(tmp)
		img.AddFlag("attach")
		img.AddFlag("not_pick")
		img.LoadImage("d:/ymir work/ui/wiki/arrow_2.tga")
		img.SetPosition(padding, tmp.GetHeight() / 2 - img.GetHeight() / 2)
		img.Show()
		tmp.img = img

		txt = ui.TextLine()
		txt.SetParent(tmp)
		txt.AddFlag("attach")
		txt.AddFlag("not_pick")
		fnt = constInfo.GetChoosenFontName().split(":")
		txt.SetFontName(fnt[0] +":"+ str(int(fnt[1]) + 2))
		txt.SetText(text)
		txt.SetPosition(img.GetLocalPosition()[0] + img.GetWidth() + 5, tmp.GetHeight() / 2 - txt.GetTextSize()[1] / 2 - 1)
		txt.Show()
		tmp.txt = txt

		totalElem = len(self.elements)
		addPadding = 0
		if totalElem > 0:
			lastIndex = totalElem

			self.elements.insert(lastIndex, tmp)
			totalElem += 1

			for i in xrange(lastIndex, totalElem):
				if i == 0:
					self.elements[i].SetPosition(0, 0)
				else:
					self.elements[i].SetPosition(0, self.elements[i - 1].GetLocalPosition()[1] + self.elements[i - 1].GetHeight() + self.ELEM_PADDING)					

			#tmp.SetPosition(0, self.elements[-1].GetLocalPosition()[1] + self.elements[-1].GetHeight() + self.ELEM_PADDING)
			addPadding = self.ELEM_PADDING

		else:
			self.elements.append(tmp)

		tmp.Show()
		self.scrollBoard.SetSize(tmp.GetWidth(), self.scrollBoard.GetHeight() + addPadding + tmp.GetHeight())
		self.UpdateScrollbar()
		return tmp

	def OnMouseWheel(self, length):
		if self.peekWindow.IsInPosition():
			self.UpdateScrollbar(length * self.SCROLL_SPEED)
			return True
		return False

	def OnScrollBar(self, fScale):
		curr = min(0, max(math.ceil((self.scrollBoard.GetHeight() - self.peekWindow.GetHeight()) * fScale * -1.0), -self.scrollBoard.GetHeight() + self.peekWindow.GetHeight()))
		self.scrollBoard.SetPosition(0, curr)

	def ChangeScrollbar(self):
		if self.scrollBar:
			if self.scrollBoard.GetHeight() <= self.GetHeight():
				self.scrollBar.Hide()
			else:
				self.scrollBar.SetScale(self.GetHeight() / self.scrollBoard.GetHeight())
				self.scrollBar.SetPosScale(abs(self.scrollBoard.GetLocalPosition()[1]) / (self.scrollBoard.GetHeight() - self.peekWindow.GetHeight()))
				self.scrollBar.Show()

	def UpdateScrollbar(self, val = 0):
		curr = min(0, max(self.scrollBoard.GetLocalPosition()[1] + val, -self.scrollBoard.GetHeight() + self.peekWindow.GetHeight()))
		self.scrollBoard.SetPosition(0, curr)
		self.ChangeScrollbar()

	def RegisterScrollBar(self):
		self.scrollBar = WikiScrollBar()
		self.scrollBar.SetParent(self)
		self.scrollBar.SetPosition(self.peekWindow.GetLocalPosition()[0] + self.peekWindow.GetWidth() + 1, self.peekWindow.GetLocalPosition()[1])
		self.scrollBar.SetSize(7, self.peekWindow.GetHeight())
		self.scrollBar.Show()

		self.scrollBar.SetScrollEvent(self.OnScrollBar)
		self.scrollBar.SetScrollSpeed(self.SCROLL_SPEED)
		self.ChangeScrollbar()

class SpecialPageWindow(ui.Window):
	def __init__(self, vnum, isMonster):
		super(SpecialPageWindow, self).__init__()
		wikiBase = wiki.GetBaseClass()
		if id(self) not in wikiBase.objList:
			wikiBase.objList[long(id(self))] = proxy(self)

		self.vnum = vnum
		self.isMonster = isMonster
		self.toolTip = uiToolTip.ItemToolTip()

		self.bg = ui.ExpandedImageBox()
		self.bg.SetParent(self)
		self.bg.AddFlag("attach")
		self.bg.AddFlag("not_pick")
		self.bg.LoadImage("d:/ymir work/ui/wiki/detail_monster.tga")
		self.bg.Show()

		self.SetSize(self.bg.GetWidth(), self.bg.GetHeight())

		self.subTitleText1 = ui.TextLine()
		self.subTitleText1.SetParent(self.bg)
		self.subTitleText1.AddFlag("attach")
		self.subTitleText1.AddFlag("not_pick")
		self.subTitleText1.Show()

		self.subTitleText2 = ui.TextLine()
		self.subTitleText2.SetParent(self.bg)
		self.subTitleText2.AddFlag("attach")
		self.subTitleText2.AddFlag("not_pick")
		self.subTitleText2.Show()

		if isMonster:
			if enableDebugThings:
				self.subTitleText1.SetText("Droplist of %s (%i)" % (nonplayer.GetMonsterName(self.vnum), self.vnum))
				self.subTitleText2.SetText("Statistics of %s (%i)" % (nonplayer.GetMonsterName(self.vnum), self.vnum))
			else:
				self.subTitleText1.SetText(localeInfo.WIKI_MONSTERINFO_DROPLISTOF % nonplayer.GetMonsterName(self.vnum))
				self.subTitleText2.SetText(localeInfo.WIKI_MONSTERINFO_STATISTICSOF % nonplayer.GetMonsterName(self.vnum))

			self.modelView = WikiRenderTarget(163, 163)
			self.modelView.SetParent(self.bg)
			self.modelView.AddFlag("attach")
			self.modelView.SetPosition(1 + 187 / 2 - 163 / 2, 1)
			self.modelView.SetModel(vnum)
			self.modelView.Show()

			self.itemContainer = ChestPeekWindow(self, 351, 142, False)
			self.itemContainer.ELEM_PER_LINE = 10
			self.itemContainer.ELEM_X_PADDING = -2
			self.itemContainer.AddFlag("attach")
			self.itemContainer.SetParent(self.bg)
			self.itemContainer.SetPosition(189, 22)
			self.itemContainer.Show()
			self.itemContainer.mOverInEvent = ui.__mem_func__(self.OnOverIn)
			self.itemContainer.mOverOutEvent = ui.__mem_func__(self.OnOverOut)
			self.LoadDropData()

			self.bonusInfo = WikiMonsterBonusInfoWindow(self.vnum)
			self.bonusInfo.SetParent(self.bg)
			self.bonusInfo.AddFlag("attach")
			self.bonusInfo.SetPosition(1, 188)
			self.bonusInfo.Show()

		else:
			if self.vnum != 94326:
				self.vnum = int(self.vnum / 10) * 10
			item.SelectItem(1, 2, self.vnum)
			self.subTitleText1.SetText(localeInfo.WIKI_ITEMINFO_OPTAINEDFROM)
			if enableDebugThings:
				self.subTitleText2.SetText("Refine info of %s (%i)" % (item.GetItemName()[:-2], self.vnum))
			else:
				self.subTitleText2.SetText(localeInfo.WIKI_ITEMINFO_REFINEINFO % item.GetItemName()[:-2])

			self.modelView = ui.ExpandedImageBox()
			self.modelView.SetParent(self.bg)
			self.modelView.AddFlag("attach")
			self.modelView.LoadImage(item.GetIconImageFileName())
			self.modelView.SetPosition(1 + 187 / 2 - self.modelView.GetWidth() / 2, 1 + 163 / 2 - self.modelView.GetHeight() / 2)
			self.modelView.SetStringEvent("MOUSE_OVER_IN", ui.__mem_func__(self.OnOverIn), self.vnum + 9)
			self.modelView.SetStringEvent("MOUSE_OVER_OUT", ui.__mem_func__(self.OnOverOut))
			self.modelView.Show()

			self.bonusPeekWindow = ui.Window()
			self.bonusPeekWindow.SetParent(self.bg)
			self.bonusPeekWindow.AddFlag("attach")
			self.bonusPeekWindow.AddFlag("not_pick")
			self.bonusPeekWindow.SetPosition(0, 187)
			self.bonusPeekWindow.Show()
			self.bonusPeekWindow.SetInsideRender(True)

			self.bonusScrollBoard = ui.Window()
			self.bonusScrollBoard.SetParent(self.bonusPeekWindow)
			self.bonusScrollBoard.AddFlag("attach")
			self.bonusScrollBoard.AddFlag("not_pick")
			self.bonusScrollBoard.Show()

			self.bonusInfo = WikiMainWeaponWindow.WikiItem(self.vnum, self)
			self.bonusInfo.SetParent(self.bonusScrollBoard)
			#self.bonusInfo.SetPosition(0, 187)
			self.bonusInfo.Show()
			self.additionalLoaded = False

			self.bonusPeekWindow.SetSize(self.bonusInfo.GetWidth(), self.bonusInfo.GetHeight())
			self.bonusScrollBoard.SetSize(self.bonusInfo.GetWidth(), self.bonusInfo.GetHeight())


			self.originInfo = WikiItemOriginInfo(self.vnum)
			self.originInfo.SetParent(self.bg)
			self.originInfo.AddFlag("attach")
			self.originInfo.SetPosition(189, 22)
			self.originInfo.Show()

		self.subTitleText1.SetPosition(189 + 351 / 2 - self.subTitleText1.GetTextSize()[0] / 2, 1 + 10 - self.subTitleText1.GetTextSize()[1] / 2)
		self.subTitleText2.SetPosition(1 + 539 / 2 - self.subTitleText2.GetTextSize()[0] / 2, 165 + 11 - self.subTitleText2.GetTextSize()[1] / 2)


	def __del__(self):
		if wiki.GetBaseClass():
			wiki.GetBaseClass().objList.pop(long(id(self)))
		super(SpecialPageWindow, self).__del__()

	def OnMouseWheel(self, length):
		if self.bonusScrollBoard.GetHeight() == self.bonusPeekWindow.GetHeight():
			return

		if self.bonusPeekWindow.IsInPosition():
			self.UpdateScrollbar(-constInfo.WHEEL_TO_SCROLL(length))
			return True
		return False

	def ChangeElementSize(self, elem, sizeDiff):
		self.bonusScrollBoard.SetSize(self.bonusScrollBoard.GetWidth(), self.bonusScrollBoard.GetHeight() + sizeDiff)

	def UpdateScrollbar(self, val = 0):
		curr = min(0, max(self.bonusScrollBoard.GetLocalPosition()[1] + val, -self.bonusScrollBoard.GetHeight() + self.bonusPeekWindow.GetHeight()))
		self.bonusScrollBoard.SetPosition(0, curr)
		
	def OnOverIn(self, vnum, metinSlot = [0 for i in xrange(player.METIN_SOCKET_MAX_NUM)]):
		self.toolTip.ClearToolTip()
		self.toolTip.AddItemData(vnum, metinSlot, 0)

	def OnOverOut(self):
		self.toolTip.Hide()

	def OnRender(self):
		if not self.isMonster and not self.additionalLoaded and wiki.IsSet(self.vnum):
			self.additionalLoaded = True
			self.originInfo.ParseTextlines()

	def OpenWindow(self):
		super(SpecialPageWindow, self).Show()

	def NoticeMe(self):
		self.LoadDropData()

	def LoadDropData(self):
		if not self.isMonster:
			return

		if not wiki.IsSet(self.vnum, True):
			wiki.LoadInfo(long(id(self)), self.vnum, True)
			return

		lst = wiki.GetMobInfo(self.vnum)
		if not lst:
			return

		sizeLst = []
		orderedLst = []
		for i in lst:
			if i < 10:
				continue

			for j in xrange(i, i + 1):
				if j in orderedLst:
					continue
				lastPos = 0
				size = 0
				if item.SelectItem(1, 2, j):
					size = item.GetItemSize()[1]

				for k in xrange(len(sizeLst)):
					if sizeLst[k] < size:
						break
					lastPos += 1

				sizeLst.insert(lastPos, size)
				orderedLst.insert(lastPos, j)


		for i in orderedLst:
			self.itemContainer.AddItem(i, 0)

	def Show(self):
		super(SpecialPageWindow, self).Show()

	def Hide(self):
		super(SpecialPageWindow, self).Hide()

class SimpleTextLoader(ui.Window):
	ELEM_PADDING = 0
	SCROLL_SPEED = 50
	def __init__(self):
		super(SimpleTextLoader, self).__init__()

		self.SetSize(mainBoardSize[0], mainBoardSize[1])

		self.elements = []
		self.images = []
		self.scrollBar = None

		self.peekWindow = ui.Window()
		self.peekWindow.SetParent(self)
		self.peekWindow.AddFlag("attach")
		self.peekWindow.AddFlag("not_pick")
		self.peekWindow.SetSize(self.GetWidth() - 8 - 5, self.GetHeight() - 5)
		self.peekWindow.SetPosition(5, 5)
		self.peekWindow.Show()
		self.peekWindow.SetInsideRender(True)

		self.scrollBoard = ui.Window()
		self.scrollBoard.SetParent(self.peekWindow)
		self.scrollBoard.AddFlag("attach")
		self.scrollBoard.AddFlag("not_pick")
		self.scrollBoard.Show()

		self.RegisterScrollBar()

	def ParseToken(self, data):
		data = data.replace(chr(10), "").replace(chr(13), "")
		if not (len(data) and data[0] == "["):
			return (False, {}, data)

		fnd = data.find("]")
		if fnd <= 0:
			return (False, {}, data)

		content = data[1:fnd]
		data = data[fnd+1:]
		
		content = content.split(";")
		container = {}
		for i in content:
			i = i.strip()
			splt = i.split("=")
			if len(splt) == 1:
				container[splt[0].lower().strip()] = True
			else:
				container[splt[0].lower().strip()] = splt[1].lower().strip()

		return (True, container, data)

	def GetColorFromString(self, strCol):
		hCol = long(strCol, 16)
		retData = []
		dNum = 4
		if hCol <= 0xFFFFFF:
			retData.append(1.0)
			dNum = 3

		for i in xrange(dNum):
			retData.append(float((hCol >> (8 * i)) & 0xFF) / 255.0)

		retData.reverse()
		return retData

	def LoadFile(self, filename):
		del self.elements[:]
		del self.images[:]
		self.scrollBoard.SetSize(0, 0)
		self.UpdateScrollbar()

		open_filename = app.GetLocalePath() + "/wiki/" + filename
		if not timer.Exists(open_filename):
			open_filename = "locale/en/wiki/" + filename

		if enableDebugThings and not timer.Exists(open_filename):
			open_filename = "wiki\\\\" + filename
			loadF = open(open_filename)
		else:
			loadF = pack_open(open_filename)

		for i in loadF.readlines()[1:]:
			(ret, tokenMap, i) = self.ParseToken(i)
			if ret:
				if tokenMap.has_key("banner_img"):
					if wiki.GetBaseClass():
						wiki.GetBaseClass().header.LoadImage(tokenMap["banner_img"])
						wiki.GetBaseClass().header.Show()

					tokenMap.pop("banner_img")

				if tokenMap.has_key("img"):
					cimg = ui.ExpandedImageBox()
					cimg.SetParent(self.scrollBoard)
					cimg.AddFlag("attach")
					cimg.AddFlag("not_pick")
					cimg.LoadImage(tokenMap["img"])
					cimg.Show()
					tokenMap.pop("img")

					x = 0
					if tokenMap.has_key("x"):
						x = int(tokenMap["x"])
						tokenMap.pop("x")

					y = 0
					if tokenMap.has_key("y"):
						y = int(tokenMap["y"])
						tokenMap.pop("y")

					if tokenMap.has_key("center_align"):
						cimg.SetPosition(self.peekWindow.GetWidth() / 2 - cimg.GetWidth() / 2, y)
						tokenMap.pop("center_align")
					elif tokenMap.has_key("right_align"):
						cimg.SetPosition(self.peekWindow.GetWidth() - cimg.GetWidth(), y)
						tokenMap.pop("right_align")
					else:
						cimg.SetPosition(x, y)

					self.images.append(cimg)

			if ret and not len(i):
				continue

			tmp = ui.Window()
			tmp.SetParent(self.scrollBoard)
			tmp.AddFlag("attach")
			tmp.AddFlag("not_pick")

			tx = ui.TextLine()
			tx.SetParent(tmp)
			if tokenMap.has_key("font_size"):
				splt = localeInfo.UI_DEF_FONT.split(":")
				tx.SetFontName(splt[0]+":"+tokenMap["font_size"])
				tokenMap.pop("font_size")
			else:
				tx.SetFontName(localeInfo.UI_DEF_FONT)
			tx.SetText(i)
			tx.Show()
			tmp.SetSize(tx.GetTextSize()[0], tx.GetTextSize()[1])
			tmp.txt = tx

			if len(i) > 0 and i[0] == "*":
				tx.SetText(i[1:])

				img = ui.ExpandedImageBox()
				img.SetParent(tmp)
				img.AddFlag("attach")
				img.AddFlag("not_pick")
				img.LoadImage("d:/ymir work/ui/wiki/arrow_2.tga")
				img.Show()
				tmp.img = img

				tmp.SetSize(img.GetWidth() + 5 + tx.GetTextSize()[0], max(img.GetHeight(), tx.GetTextSize()[1]))
				img.SetPosition(0, abs(tmp.GetHeight() / 2 - img.GetHeight() / 2))

				tx.SetPosition(img.GetWidth() + 5, abs(tmp.GetHeight() / 2 - tx.GetTextSize()[1] / 2) - 1)

			if tokenMap.has_key("color"):
				fontColor = self.GetColorFromString(tokenMap["color"])
				tx.SetPackedFontColor(grp.GenerateColor(fontColor[0], fontColor[1], fontColor[2], fontColor[3]))
				tokenMap.pop("color")

			totalElem = len(self.elements)
			addPadding = 0
			if tokenMap.has_key("y_padding"):
				addPadding = int(tokenMap["y_padding"])
				tokenMap.pop("y_padding")

			if totalElem > 0:
				lastIndex = totalElem

				self.elements.insert(lastIndex, tmp)
				totalElem += 1

				for i in xrange(lastIndex, totalElem):
					if i == 0:
						self.elements[i].SetPosition(0, 0)
					else:
						self.elements[i].SetPosition(0, self.elements[i - 1].GetLocalPosition()[1] + self.elements[i - 1].GetHeight() + addPadding)					

			else:
				self.elements.append(tmp)
				tmp.SetPosition(0, addPadding)

			if tokenMap.has_key("center_align"):
				tmp.SetPosition(self.peekWindow.GetWidth() / 2 - tmp.GetWidth() / 2, tmp.GetLocalPosition()[1])
				tokenMap.pop("center_align")
			elif tokenMap.has_key("right_align"):
				tmp.SetPosition(self.peekWindow.GetWidth() - tmp.GetWidth(), tmp.GetLocalPosition()[1])
				tokenMap.pop("right_align")
			elif tokenMap.has_key("x_padding"):
				tmp.SetPosition(int(tokenMap["x_padding"]), tmp.GetLocalPosition()[1])
				tokenMap.pop("x_padding")

			tmp.Show()
			self.scrollBoard.SetSize(self.peekWindow.GetWidth(), self.scrollBoard.GetHeight() + addPadding + tmp.GetHeight())

		for i in self.images:
			mxSize = i.GetLocalPosition()[1] + i.GetHeight()
			if mxSize > self.scrollBoard.GetHeight():
				self.scrollBoard.SetSize(self.peekWindow.GetWidth(), mxSize)

		self.UpdateScrollbar()
		self.Show()

	def OnMouseWheel(self, length):
		if self.peekWindow.IsInPosition():
			self.UpdateScrollbar(length * self.SCROLL_SPEED)
			return True
		return False

	def OnScrollBar(self, fScale):
		curr = min(0, max(math.ceil((self.scrollBoard.GetHeight() - self.peekWindow.GetHeight()) * fScale * -1.0), -self.scrollBoard.GetHeight() + self.peekWindow.GetHeight()))
		self.scrollBoard.SetPosition(0, curr)

	def ChangeScrollbar(self):
		if self.scrollBar:
			if self.scrollBoard.GetHeight() <= self.GetHeight():
				self.scrollBar.Hide()
			else:
				self.scrollBar.SetScale(self.GetHeight() / self.scrollBoard.GetHeight())
				self.scrollBar.SetPosScale(abs(self.scrollBoard.GetLocalPosition()[1]) / (self.scrollBoard.GetHeight() - self.peekWindow.GetHeight()))
				self.scrollBar.Show()

	def UpdateScrollbar(self, val = 0):
		curr = min(0, max(self.scrollBoard.GetLocalPosition()[1] + val, -self.scrollBoard.GetHeight() + self.peekWindow.GetHeight()))
		self.scrollBoard.SetPosition(0, curr)
		self.ChangeScrollbar()

	def RegisterScrollBar(self):
		self.scrollBar = WikiScrollBar()
		self.scrollBar.SetParent(self)
		self.scrollBar.SetPosition(self.peekWindow.GetLocalPosition()[0] + self.peekWindow.GetWidth() + 1, self.peekWindow.GetLocalPosition()[1])
		self.scrollBar.SetSize(7, self.peekWindow.GetHeight())
		self.scrollBar.Show()

		self.scrollBar.SetScrollEvent(self.OnScrollBar)
		self.scrollBar.SetScrollSpeed(self.SCROLL_SPEED)
		self.ChangeScrollbar()

class WikiMainCostumeWindow(ui.Window):
	class WikiItem(ui.Window):
		def __init__(self, vnum, parent):
			ui.Window.__init__(self)

			self.vnum = vnum
			self.parent = proxy(parent)

			self.base = ui.ExpandedImageBox()
			self.base.SetParent(self)
			self.base.AddFlag("attach")
			self.base.AddFlag("not_pick")
			self.base.LoadImage("d:/ymir work/ui/wiki/detail_item_small.tga")
			self.base.Show()

			self.costumeImage = ui.ExpandedImageBox()
			self.costumeImage.SetParent(self.base)
			self.costumeImage.LoadImage(item.GetIconImageFileName())
			self.costumeImage.SetPosition(1 + 125 / 2 - self.costumeImage.GetWidth() / 2, 1 + 120 / 2 - self.costumeImage.GetHeight() / 2)
			self.costumeImage.Show()

			self.costumeImage.SetStringEvent("MOUSE_OVER_IN",ui.__mem_func__( self.parent.OnOverIn), self.vnum)
			self.costumeImage.SetStringEvent("MOUSE_OVER_OUT",ui.__mem_func__( self.parent.OnOverOut))

			self.contentText = ui.TextLine()
			self.contentText.SetParent(self.base)
			self.contentText.AddFlag("attach")
			self.contentText.AddFlag("not_pick")
			if enableDebugThings:
				self.contentText.SetText("%s (%i)" % (item.GetItemName(), self.vnum))
			else:
				self.contentText.SetText(item.GetItemName())
			self.contentText.SetPosition(1 + 125 / 2 - self.contentText.GetTextSize()[0] / 2, 122 + 18 / 2 - self.contentText.GetTextSize()[1] / 2 - 1)
			self.contentText.Show()

			self.SetSize(self.base.GetWidth(), self.base.GetHeight())
		
	ELEM_X_PADDING = 10
	ELEM_PADDING = 10
	SCROLL_SPEED = 25
	ELEM_PER_LINE = 4
	ITEM_LOAD_PER_UPDATE = 1
	def __init__(self):
		super(WikiMainCostumeWindow, self).__init__()

		self.SetSize(mainBoardSize[0], mainBoardSize[1])

		self.elements = []
		self.posMap = {}
		self.isOpened = False
		self.scrollBar = None
		self.loadFrom = 0
		self.loadTo = 0
		self.costumeVnums = []
		self.toolTip = uiToolTip.ItemToolTip()
		self.toolTip.AddFlag("not_pick")
		self.wikiRenderTarget = WikiRenderTarget(150, 200)
		self.wikiRenderTarget.SetParent(self.toolTip)
		self.wikiRenderTarget.AddFlag("not_pick")
		self.wikiRenderTarget.SetPosition(5, self.toolTip.toolTipHeight)
		self.wikiRenderTarget.Show()

		self.peekWindow = ui.Window()
		self.peekWindow.SetParent(self)
		self.peekWindow.AddFlag("attach")
		self.peekWindow.AddFlag("not_pick")
		self.peekWindow.SetSize(541, self.GetHeight() - 15)
		self.peekWindow.SetPosition(5, 5)
		self.peekWindow.Show()
		self.peekWindow.SetInsideRender(True)

		self.scrollBoard = ui.Window()
		self.scrollBoard.SetParent(self.peekWindow)
		self.scrollBoard.AddFlag("attach")
		self.scrollBoard.AddFlag("not_pick")
		self.scrollBoard.Show()

		self.RegisterScrollBar()

	def OpenWindow(self):
		super(WikiMainCostumeWindow, self).Show()

	def Hide(self):
		super(WikiMainCostumeWindow, self).Hide()

	def Show(self, vnums):
		super(WikiMainCostumeWindow, self).Show()

		extractedLists = []
		for i in vnums:
			if type(i) == types.ListType:
				extractedLists.append(i)

		for i in extractedLists:
			pos = vnums.index(i)
			vnums.remove(i)
			for j in xrange(len(i)):
				vnums.insert(pos + j, i[j])

		isChanged = not len(vnums) == len(self.costumeVnums)
		if not isChanged:
			for i in vnums:
				if i not in self.costumeVnums:
					isChanged = True
					break

		if not isChanged:
			for i in self.costumeVnums:
				if i not in vnums:
					isChanged = True
					break

		self.costumeVnums = vnums[:]
		self.loadTo = len(self.costumeVnums)

		if not self.isOpened:
			self.isOpened = True
			self.loadFrom = 0

		if self.loadFrom > self.loadTo or isChanged:
			del self.elements[:]
			self.posMap = {}
			self.loadFrom = 0
			self.scrollBoard.SetSize(0, 0)
			self.UpdateScrollbar()

	def GetRandomChar(self):
		WARRIOR_M 	= 0
		ASSASSIN_W 	= 1
		SURA_M 		= 2
		SHAMAN_W 	= 3
		WARRIOR_W 	= 4
		ASSASSIN_M 	= 5
		SURA_W 		= 6
		SHAMAN_M 	= 7

		SEX_FEMALE 	= 0
		SEX_MALE 	= 1
	
		ASSASSINS 	= [ ASSASSIN_W, ASSASSIN_M ]
		WARRIORS 	= [ WARRIOR_W, WARRIOR_M ]
		SURAS 		= [ SURA_W, SURA_M ]
		SHAMANS 	= [ SHAMAN_W, SHAMAN_M ]
		# what characters can wear it
		ITEM_CHARACTERS = [ ASSASSINS, WARRIORS, SURAS, SHAMANS ]
		# what sex can wear it
		ITEM_SEX = [ SEX_FEMALE, SEX_MALE ]

		# anti flag male -> remove male from ITEM_SEX
		if item.IsAntiFlag( item.ITEM_ANTIFLAG_MALE ):
			ITEM_SEX.remove( SEX_MALE )

		# anti flag female -> remove female from ITEM_SEX
		if item.IsAntiFlag( item.ITEM_ANTIFLAG_FEMALE ):
			ITEM_SEX.remove( SEX_FEMALE )

		# get characters that can use it, bit ghetto code
		if item.IsAntiFlag( item.ITEM_ANTIFLAG_WARRIOR ):
			ITEM_CHARACTERS.remove( WARRIORS )

		if item.IsAntiFlag( item.ITEM_ANTIFLAG_SURA ):
			ITEM_CHARACTERS.remove( SURAS )

		if item.IsAntiFlag( item.ITEM_ANTIFLAG_ASSASSIN ):
			ITEM_CHARACTERS.remove( ASSASSINS )

		if item.IsAntiFlag( item.ITEM_ANTIFLAG_SHAMAN ):
			ITEM_CHARACTERS.remove( SHAMANS )

		return ITEM_CHARACTERS[app.GetRandom(0, len(ITEM_CHARACTERS) - 1)][ITEM_SEX[app.GetRandom(0, len(ITEM_SEX) - 1)]]

	def OnOverIn(self, vnum, metinSlot = [0 for i in xrange(player.METIN_SOCKET_MAX_NUM)]):
		self.toolTip.ClearToolTip()
		self.toolTip.SetThinBoardSize(self.wikiRenderTarget.GetWidth() + 10, self.wikiRenderTarget.GetHeight() + self.toolTip.toolTipHeight)
		self.toolTip.childrenList.append(self.wikiRenderTarget)
		self.toolTip.ResizeToolTip()

		item.SelectItem(1, 2, vnum)
		itemType = item.GetItemType()
		subType = item.GetItemSubType()
		if itemType == item.ITEM_TYPE_WEAPON or itemType == item.ITEM_TYPE_COSTUME and subType == item.COSTUME_TYPE_WEAPON:
			self.wikiRenderTarget.SetWeaponModel(vnum)

		elif itemType == item.ITEM_TYPE_COSTUME and subType == item.COSTUME_TYPE_BODY:
			self.wikiRenderTarget.SetModel(self.GetRandomChar())
			self.wikiRenderTarget.SetModelForm(vnum)

		elif itemType == item.ITEM_TYPE_COSTUME and subType == item.COSTUME_TYPE_HAIR:
			chartype = self.GetRandomChar()
			self.wikiRenderTarget.SetModel(chartype)
			self.wikiRenderTarget.SetModelHair(vnum)
			if chartype == 0:
				wiki.SetModelV3Eye(self.wikiRenderTarget.moduleID, 311.4753, -16.3934, -32.7869)
				wiki.SetModelV3Target(self.wikiRenderTarget.moduleID, -1000.0, 49.1803, -16.3934)
			elif chartype == 1:
				wiki.SetModelV3Eye(self.wikiRenderTarget.moduleID, 344.2622, -16.3934, -32.7869)
				wiki.SetModelV3Target(self.wikiRenderTarget.moduleID, -1000.0, 49.1803, -16.3934)
			elif chartype == 2:
				wiki.SetModelV3Eye(self.wikiRenderTarget.moduleID, 311.4753, -16.3934, -32.7869)
				wiki.SetModelV3Target(self.wikiRenderTarget.moduleID, -1000.0, 49.1803, -49.1804)
			elif chartype == 3 or chartype == 4:
				wiki.SetModelV3Eye(self.wikiRenderTarget.moduleID, 344.2622, -16.3934, -32.7869)
				wiki.SetModelV3Target(self.wikiRenderTarget.moduleID, -1000.0, 49.1803, -16.3934)
			elif chartype == 5:
				wiki.SetModelV3Eye(self.wikiRenderTarget.moduleID, 344.2622, -16.3934, -32.7869)
				wiki.SetModelV3Target(self.wikiRenderTarget.moduleID, -1000.0, 49.1803, -32.7869)
			elif chartype == 6:
				wiki.SetModelV3Eye(self.wikiRenderTarget.moduleID, 311.4753, -16.3934, -32.7869)
				wiki.SetModelV3Target(self.wikiRenderTarget.moduleID, -1000.0, 49.1803, -25.7869)
			elif chartype == 7:
				wiki.SetModelV3Eye(self.wikiRenderTarget.moduleID, 377.0492, -16.3934, -32.7869)
				wiki.SetModelV3Target(self.wikiRenderTarget.moduleID, -1000.0, 49.1803, -32.7869)

		elif itemType == item.ITEM_TYPE_COSTUME and subType == item.COSTUME_TYPE_PET:
			self.wikiRenderTarget.SetModel(item.GetValue(0))

		elif itemType == item.ITEM_TYPE_COSTUME and subType == item.COSTUME_TYPE_MOUNT:
			self.wikiRenderTarget.SetModel(item.GetValue(0))

		#self.toolTip.ViewModel(vnum)
		self.toolTip.AddItemData(vnum, metinSlot, 0)
		self.wikiRenderTarget.SetPosition(self.toolTip.GetWidth() / 2 - self.wikiRenderTarget.GetWidth() / 2, self.wikiRenderTarget.GetLocalPosition()[1])

	def OnOverOut(self):
		self.toolTip.Hide()

	def OnUpdate(self):
		if self.loadFrom < self.loadTo:
			for i in xrange(self.loadFrom, min(self.loadTo, self.loadFrom + self.ITEM_LOAD_PER_UPDATE)):
				self.AddItem(self.costumeVnums[i])
				self.loadFrom += 1
				
	def AddItem(self, vnum):
		for i in self.elements:
			if vnum == i.vnum:
				return None
		if not item.SelectItem(1, 2, vnum):
			return None

		tmp = self.WikiItem(vnum, self)
		tmp.SetParent(self.scrollBoard)
		tmp.AddFlag("attach")

		totalElem = len(self.elements)
		if totalElem > 0:				
			#tmp.SetPosition(0, self.elements[-1].GetLocalPosition()[1] + self.elements[-1].GetHeight() + self.ELEM_PADDING)
			currAdd = 0
			while currAdd in self.posMap:
				currAdd += 1

			totalLine = currAdd % self.ELEM_PER_LINE
			currH = math.floor(currAdd / self.ELEM_PER_LINE) * (tmp.GetHeight() + self.ELEM_PADDING)

			self.posMap[currAdd] = True
			tmp.SetPosition(1 + totalLine * (tmp.GetWidth() + self.ELEM_X_PADDING), 0 + currH)

		else:
			self.posMap[0] = True
			tmp.SetPosition(1, 0)
		
		self.elements.append(tmp)

		tmp.Show()
		self.scrollBoard.SetSize(self.peekWindow.GetWidth(), max(self.scrollBoard.GetHeight(), tmp.GetLocalPosition()[1] + tmp.GetHeight()))
		self.UpdateScrollbar()

	def OnMouseWheel(self, length):
		if self.peekWindow.IsInPosition():
			self.UpdateScrollbar(length * self.SCROLL_SPEED)
			return True
		return False

	def OnScrollBar(self, fScale):
		curr = min(0, max(math.ceil((self.scrollBoard.GetHeight() - self.peekWindow.GetHeight()) * fScale * -1.0), -self.scrollBoard.GetHeight() + self.peekWindow.GetHeight()))
		self.scrollBoard.SetPosition(0, curr)

	def ChangeScrollbar(self):
		if self.scrollBar:
			if self.scrollBoard.GetHeight() <= self.GetHeight():
				self.scrollBar.Hide()
			else:
				self.scrollBar.SetScale(self.GetHeight() / self.scrollBoard.GetHeight())
				self.scrollBar.SetPosScale(abs(self.scrollBoard.GetLocalPosition()[1]) / (self.scrollBoard.GetHeight() - self.peekWindow.GetHeight()))
				self.scrollBar.Show()

	def UpdateScrollbar(self, val = 0):
		curr = min(0, max(self.scrollBoard.GetLocalPosition()[1] + val, -self.scrollBoard.GetHeight() + self.peekWindow.GetHeight()))
		self.scrollBoard.SetPosition(0, curr)
		self.ChangeScrollbar()

	def RegisterScrollBar(self):
		self.scrollBar = WikiScrollBar()
		self.scrollBar.SetParent(self)
		self.scrollBar.SetPosition(self.peekWindow.GetLocalPosition()[0] + self.peekWindow.GetWidth() + 1, self.peekWindow.GetLocalPosition()[1])
		self.scrollBar.SetSize(7, self.peekWindow.GetHeight())
		self.scrollBar.Show()

		self.scrollBar.SetScrollEvent(self.OnScrollBar)
		self.scrollBar.SetScrollSpeed(self.SCROLL_SPEED)
		self.ChangeScrollbar()

def InitMainWindow(self):
	self.AddFlag('movable')
	self.AddFlag('float')

	for i in ITEM_BLACKLIST:
		if type(i) == types.ListType:
			for k in i:
				wiki.RegisterItemBlacklist(k)
		else:		
			wiki.RegisterItemBlacklist(i)

	for i in MOB_BLACKLIST:
		if type(i) == types.ListType:
			for k in i:
				wiki.RegisterMonsterBlacklist(k)
		else:
			wiki.RegisterMonsterBlacklist(i)

	nonplayer.BuildWikiSearchList()

def InitMainWeaponWindow(self):
	self.mainWeaponWindow = WikiMainWeaponWindow()
	self.mainWeaponWindow.SetParent(self.baseBoard)
	self.mainWeaponWindow.AddFlag("attach")
	self.mainWeaponWindow.SetPosition(mainBoardPos[0], mainBoardPos[1])

def InitMainChestWindow(self):
	self.mainChestWindow = WikiMainChestWindow()
	self.mainChestWindow.SetParent(self.baseBoard)
	self.mainChestWindow.AddFlag("attach")
	self.mainChestWindow.SetPosition(mainBoardPos[0], mainBoardPos[1])
	#self.mainChestWindow.Show()

def InitMainBossWindow(self):
	self.mainBossWindow = WikiMainBossWindow()
	self.mainBossWindow.SetParent(self.baseBoard)
	self.mainBossWindow.AddFlag("attach")
	self.mainBossWindow.SetPosition(mainBoardPos[0], mainBoardPos[1])
	#self.mainBossWindow.Show()

def InitCustomPageWindow(self):
	self.customPageWindow = SimpleTextLoader()
	self.customPageWindow.SetParent(self.baseBoard)
	self.customPageWindow.AddFlag("attach")
	self.customPageWindow.SetPosition(mainBoardPos[0], mainBoardPos[1])
	#self.customPageWindow.Show()

def InitCostumePageWindow(self):
	self.costumePageWindow = WikiMainCostumeWindow()
	self.costumePageWindow.SetParent(self.baseBoard)
	self.costumePageWindow.AddFlag("attach")
	self.costumePageWindow.SetPosition(mainBoardPos[0], mainBoardPos[1])

def InitTitleBar(self):
	titleBar = ui.TitleBar()
	titleBar.SetParent(self.baseBoard)
	titleBar.MakeTitleBar(0, "red")
	titleBar.SetWidth(self.GetWidth() - 15)
	if app.GetSelectedDesignName() != "illumina":
		titleBar.SetPosition(8, 7)
	else:
		titleBar.SetPosition(8, 11)
	titleBar.Show()

	titleName = ui.TextLine()
	titleName.SetParent(titleBar)
	titleName.SetPosition(0, 4)
	if app.GetSelectedDesignName() != "illumina":
		titleName.SetPosition(0, 4)
	else:
		titleName.SetPosition(0, 7)
	titleName.SetWindowHorizontalAlignCenter()
	titleName.SetHorizontalAlignCenter()
	titleName.SetText(localeInfo.WIKI_TITLENAME)
	titleName.Show()

	self.titleBar = titleBar
	self.titleName = titleName
	self.titleBar.SetCloseEvent(self.Close)

def BuildSearchWindow(self):
	self.searchBG = ui.ExpandedImageBox()
	self.searchBG.SetParent(self.baseBoard)
	self.searchBG.LoadImage("d:/ymir work/ui/wiki/searchfield.tga")
	self.searchBG.SetPosition(13, 33)
	self.searchBG.Show()

	self.searchButton = ui.Button()
	self.searchButton.SetParent(self.searchBG)
	self.searchButton.SetUpVisual("d:/ymir work/ui/game/shopsearch/button_search_normal.tga")
	self.searchButton.SetOverVisual("d:/ymir work/ui/game/shopsearch/button_search_hover.tga")
	self.searchButton.SetDownVisual("d:/ymir work/ui/game/shopsearch/button_search_down.tga")
	self.searchButton.SetPosition(self.searchBG.GetWidth() - self.searchButton.GetWidth() - 2, self.searchBG.GetHeight() / 2 - self.searchButton.GetHeight() / 2 + 1)
	self.searchButton.SAFE_SetEvent(self.StartSearch)
	self.searchButton.Show()

	self.searchEditHint = ui.TextLine()

	self.searchEdit = ui.EditLine()
	self.searchEdit.SetParent(self.searchBG)
	self.searchEdit.SetMax(50)
	self.searchEdit.SetSize(111 - self.searchButton.GetWidth() - 2, 15)
	self.searchEdit.SetPosition(5, self.searchBG.GetHeight() / 2 - 15 / 2)
	self.searchEdit.SetOverlayText(uiScriptLocale.AUCTION_SEARCH_EDIT_OVERLAY_TEXT)
	self.searchEdit.SetLimitWidth(self.searchEdit.GetWidth())
	self.searchEdit.SetOutline()
	self.searchEdit.Show()

	self.searchEdit.SetEscapeEvent(ui.__mem_func__(self.OnPressNameEscapeKey))
	self.searchEdit.SetReturnEvent(ui.__mem_func__(self.StartSearch))
	self.searchEdit.SetUpdateEvent(ui.__mem_func__(self.Search_RefreshTextHint))
	self.searchEdit.SetTabEvent(ui.__mem_func__(self.Search_CompleteTextSearch))

	self.searchEditHint.SetParent(self.searchEdit)
	self.searchEditHint.SetPackedFontColor(grp.GenerateColor(1.0, 1.0, 1.0, 0.5))
	#self.searchEditHint.SetOutline()
	self.searchEditHint.Show()

def BuildBaseMain(self):
	self.baseBoard = ui.ExpandedImageBox()
	self.baseBoard.AddFlag("attach")
	self.baseBoard.SetParent(self)
	self.baseBoard.LoadImage("D:/Ymir Work/ui/wiki/bg.tga")
	self.baseBoard.SetWindowName("InGameWikiBoard")
	self.baseBoard.Show()

	self.SetSize(self.baseBoard.GetWidth(), self.baseBoard.GetHeight())

	self.header = ui.ExpandedImageBox()
	#self.header.AddFlag("attach")
	#self.header.AddFlag("not_pick")
	self.header.SetParent(self.baseBoard)
	self.header.SetPosition(149, 37)

	BuildSearchWindow(self)

	self.categText = ui.TextLine()
	self.categText.SetParent(self.baseBoard)
	self.categText.SetPosition(13, self.searchBG.GetLocalPosition()[1] + self.searchBG.GetHeight() + 10)
	self.categText.SetText(localeInfo.WIKI_CATEGORIES_TITLE)
	self.categText.Show()

	self.categ = WikiCategories()
	self.categ.hideWindowsEvent = ui.__mem_func__(self.CloseBaseWindows)
	self.categ.SetParent(self.baseBoard)
	self.categ.AddFlag("attach")
	self.categ.SetPosition(13, 77 + 15)
	self.categ.Show()

	self.prevButt = ui.Button()
	self.prevButt.SetParent(self.baseBoard)
	self.prevButt.SetUpVisual("d:/ymir work/ui/wiki/btn_arrow_left_normal.tga")
	self.prevButt.SetOverVisual("d:/ymir work/ui/wiki/btn_arrow_left_hover.tga")
	self.prevButt.SetDownVisual("d:/ymir work/ui/wiki/btn_arrow_left_down.tga")
	self.prevButt.SetDisableVisual("d:/ymir work/ui/wiki/btn_arrow_left_down.tga")
	self.prevButt.SetPosition(self.categ.GetLocalPosition()[0], self.categ.GetLocalPosition()[1] + self.categ.GetHeight() + 5)
	self.prevButt.SAFE_SetEvent(self.OnPressPrevButton)
	self.prevButt.Show()
	self.prevButt.Disable()

	self.nextButt = ui.Button()
	self.nextButt.SetParent(self.baseBoard)
	self.nextButt.SetUpVisual("d:/ymir work/ui/wiki/btn_arrow_right_normal.tga")
	self.nextButt.SetOverVisual("d:/ymir work/ui/wiki/btn_arrow_right_hover.tga")
	self.nextButt.SetDownVisual("d:/ymir work/ui/wiki/btn_arrow_right_down.tga")
	self.nextButt.SetDisableVisual("d:/ymir work/ui/wiki/btn_arrow_right_down.tga")
	self.nextButt.SetPosition(self.categ.GetLocalPosition()[0] + self.categ.GetWidth() - self.nextButt.GetWidth(), self.categ.GetLocalPosition()[1] + self.categ.GetHeight() + 5)
	self.nextButt.SAFE_SetEvent(self.OnPressNextButton)
	self.nextButt.Show()
	self.nextButt.Disable()

	self.scrollBar = WikiScrollBar()
	self.scrollBar.SetParent(self.baseBoard)
	self.scrollBar.SetPosition(self.categ.GetLocalPosition()[0] + self.categ.GetWidth() + 5, self.categ.GetLocalPosition()[1])
	self.scrollBar.SetSize(7, categoryPeakWindowSize[1])
	self.scrollBar.Show()

	self.categ.RegisterScrollBar(self.scrollBar)

	InitTitleBar(self)
	InitMainWeaponWindow(self)
	InitMainChestWindow(self)
	InitMainBossWindow(self)
	InitCustomPageWindow(self)
	InitCostumePageWindow(self)

	funclist = [
		ui.__mem_func__(self.mainWeaponWindow.Show),
		ui.__mem_func__(self.mainChestWindow.Show),
		ui.__mem_func__(self.mainBossWindow.Show),
		ui.__mem_func__(self.mainBossWindow.Show),
		ui.__mem_func__(self.mainBossWindow.Show),
		ui.__mem_func__(self.customPageWindow.LoadFile),
		ui.__mem_func__(self.customPageWindow.LoadFile),
		ui.__mem_func__(self.costumePageWindow.Show),
		ui.__mem_func__(self.customPageWindow.LoadFile),
		ui.__mem_func__(self.customPageWindow.LoadFile),
	]

	for i in WIKI_CATEGORIES:
		ret = self.categ.AddCategory(i[0])
		for j in xrange(len(i[1])):
			ret.AddSubCategory(j, i[1][j])

		curr = WIKI_CATEGORIES.index(i)
		if curr < len(funclist):
			ret.clickEvent = funclist[curr]

	self.customPageWindow.LoadFile("landingpage.txt")
	self.header.SetStringEvent("MOUSE_LEFT_DOWN", ui.__mem_func__(self.GoToLanding))