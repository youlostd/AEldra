import uiScriptLocale
import item
import app

BOARD_WIDTH = 368 - 7
BACK_IMG_PATH = "d:/ymir work/ui/public/public_board_back/"
ROOT_PATH = "d:/ymir work/ui/game/guild/dragonlairranking/"

window = {
	"name" : "GuildDragonLairWindow",

	"x" : 0,
	"y" : 0,

	"style" : ("movable", "float",),

	"width" : BOARD_WIDTH,
	"height" : 200,

	"children" :
	(
		{
			"name" : "board",
			"type" : "board_with_titlebar",
			"style" : ("attach",),

			"x" : 0,
			"y" : 0,

			"width" : BOARD_WIDTH,
			"height" : 200,

			"title" : uiScriptLocale.GUILD_DRAGONLAIR_RANKING,
		
			"children" :
			(
				{
					"name" : "BaseWindow",
					"type" : "window",

					"x" : 10,
					"y" : 10,

					"width" : 317 + 17,
					"height" : 173 + 17,

					"children" : 
					(
						## 센터 백그라운드 시작
						## LeftTop
						{
							"name" : "LeftTop",
							"type" : "image",
							"x" : 0,
							"y" : 0,
							"image" : BACK_IMG_PATH+"boardback_mainboxlefttop.sub",
						},
						## RightTop
						{
							"name" : "RightTop",
							"type" : "image",
							"x" : 318 - 17,
							"y" : 0,
							"image" : BACK_IMG_PATH+"boardback_mainboxrighttop.sub",
						},
						## LeftBottom
						{
							"name" : "LeftBottom",
							"type" : "image",
							"x" : 0,
							"y" : 173 - 38,
							"image" : BACK_IMG_PATH+"boardback_mainboxleftbottom.sub",
						},
						## RightBottom
						{
							"name" : "RightBottom",
							"type" : "image",
							"x" : 318 - 17,
							"y" : 173 - 38,
							"image" : BACK_IMG_PATH+"boardback_mainboxrightbottom.sub",
						},
						## leftcenterImg
						{
							"name" : "leftcenterImg",
							"type" : "expanded_image",
							"x" : 0,
							"y" : 16,
							"image" : BACK_IMG_PATH+"boardback_leftcenterImg.tga",
							"rect" : (0.0, 0.0, 0, 6),
						},
						## rightcenterImg
						{
							"name" : "rightcenterImg",
							"type" : "expanded_image",
							"x" : 317 - 17,
							"y" : 16,
							"image" : BACK_IMG_PATH+"boardback_rightcenterImg.tga",
							"rect" : (0.0, 0.0, 0, 6),
						},
						## topcenterImg
						{
							"name" : "topcenterImg",
							"type" : "expanded_image",
							"x" : 15,
							"y" :  0,
							"image" : BACK_IMG_PATH+"boardback_topcenterImg.tga",
							"rect" : (0.0, 0.0, 16, 0),
						},
						## bottomcenterImg
						{
							"name" : "bottomcenterImg",
							"type" : "expanded_image",
							"x" : 15,
							"y" : 173 - 38,
							"image" : BACK_IMG_PATH+"boardback_bottomcenterImg.tga",
							"rect" : (0.0, 0.0, 16, 0),
						},
						## centerImg
						{
							"name" : "centerImg",
							"type" : "expanded_image",
							"x" : 15,
							"y" : 15,
							"image" : BACK_IMG_PATH+"boardback_centerImg.tga",
							"rect" : (0.0, 0.0, 16, 6),
						},

						## 센터 백그라운드 끝
						## GuildTiTleImg
						{
							"name" : "GuildTiTleImg",
							"type" : "image",
							"x" : 20 - 17,
							"y" : 41 - 38,
							"image" : ROOT_PATH+"ranking_list_menu.sub",
							"children" :
							(
								## Text
								{ "name" : "ResultNameRanking", "type" : "text", "x" : 10, "y" : 4,  "text" : uiScriptLocale.GUILD_DRAGONLAIR_RANKING_COUNT, },
								{ "name" : "ResultNameGuild", "type" : "text", "x" : 95, "y" : 4, "text" : uiScriptLocale.GUILD_DRAGONLAIR_RANKING_NAME, },
								{ "name" : "ResultMemberCount", "type" : "text", "x" : 180, "y" : 4, "text" : uiScriptLocale.GUILD_DRAGONLAIR_RANKING_MEMBER, },
								{ "name" : "ResultClearTime", "type" : "text", "x" : 240, "y" : 4, "text" : uiScriptLocale.GUILD_DRAGONLAIR_RANKING_TIME, },
							),
						},
					),
				},
				
				## 스크롤 바.
				{
					"name" : "GuildDragonLairScrollBar",
					"type" : "scrollbar",
					"x" : 340 - 7,
					"y" : 10,
					"size" : 180,
				},

				{
					"name" : "MyRankingWindow",
					"type" : "window",

					"x" : 10,
					"y" : 190 - 38 + 10,

					"width" : 317 + 17,
					"height" : 15 + 17,

					"children" : 
					(
						## 센터 백그라운드 시작 (자신길드)
						## LeftTop
						{
							"name" : "LeftTopSelf",
							"type" : "image",
							"x" : 0,
							"y" : 0,
							"image" : BACK_IMG_PATH+"boardback_mainboxlefttop.sub",
						},
						## RightTop
						{
							"name" : "RightTopSelf",
							"type" : "image",
							"x" : 318 - 17,
							"y" : 0,
							"image" : BACK_IMG_PATH+"boardback_mainboxrighttop.sub",
						},
						## LeftBottom
						{
							"name" : "LeftBottomSelf",
							"type" : "image",
							"x" : 0,
							"y" : 15,
							"image" : BACK_IMG_PATH+"boardback_mainboxleftbottom.sub",
						},
						## RightBottom
						{
							"name" : "RightBottomSelf",
							"type" : "image",
							"x" : 318 - 17,
							"y" : 15,
							"image" : BACK_IMG_PATH+"boardback_mainboxrightbottom.sub",
						},
						## topcenterImg
						{
							"name" : "topcenterImgSelf",
							"type" : "expanded_image",
							"x" : 15,
							"y" : 0,
							"image" : BACK_IMG_PATH+"boardback_topcenterImg.tga",
							"rect" : (0.0, 0.0, 16, 0),
						},
						## bottomcenterImg
						{
							"name" : "bottomcenterImgSelf",
							"type" : "expanded_image",
							"x" : 15,
							"y" : 15,
							"image" : BACK_IMG_PATH+"boardback_bottomcenterImg.tga",
							"rect" : (0.0, 0.0, 16, 0),
						},
					),
				},	
			),
		},
	),
}

