import uiScriptLocale
import localeInfo

window = {
	"name" : "GameWindow",
	"style" : ("not_pick",),

	"x" : 0,
	"y" : 0,

	"width" : SCREEN_WIDTH,
	"height" : SCREEN_HEIGHT,

	"children" :
	(
		{ 
			"name":"HelpButton", 
			"type":"button", 
			"x" : 50,
			"y" : SCREEN_HEIGHT-170,
			"default_image" : "d:/ymir work/ui/game/windows/btn_bigplus_up.sub",
			"over_image" : "d:/ymir work/ui/game/windows/btn_bigplus_over.sub",
			"down_image" : "d:/ymir work/ui/game/windows/btn_bigplus_down.sub",

			"children" : 
			(
				{ 
					"name":"HelpButtonLabel", 
					"type":"text", 
					"x": 16, 
					"y": 40, 
					"text":uiScriptLocale.GAME_HELP, 
					"r":1.0, "g":1.0, "b":1.0, "a":1.0, 
					"text_horizontal_align":"center" 
				},
			),
		},
		{ 
			"name":"QuestButton", 
			"type":"button", 
			"x" : SCREEN_WIDTH-50-32,
			"y" : SCREEN_HEIGHT-170,
			"default_image" : "d:/ymir work/ui/game/windows/btn_bigplus_up.sub",
			"over_image" : "d:/ymir work/ui/game/windows/btn_bigplus_over.sub",
			"down_image" : "d:/ymir work/ui/game/windows/btn_bigplus_down.sub",

			"children" : 
			(
				{ 
					"name":"QuestButtonLabel", 
					"type":"text", 
					"x": 16, 
					"y": 40, 
					"text":uiScriptLocale.GAME_QUEST, 
					"r":1.0, "g":1.0, "b":1.0, "a":1.0, 
					"text_horizontal_align":"center" 
				},
			),
		},
		{ 
			"name":"StatusPlusButton", 
			"type" : "button", 
			"x" : 50, 
			"y" : SCREEN_HEIGHT-150, 
			"default_image" : "d:/ymir work/ui/game/windows/btn_bigplus_up.sub",
			"over_image" : "d:/ymir work/ui/game/windows/btn_bigplus_over.sub",
			"down_image" : "d:/ymir work/ui/game/windows/btn_bigplus_down.sub",

			"children" :
			(
				{ 
					"name":"StatusPlusLabel", 
					"type":"text", 
					"x": 16, 
					"y": 40, 
					"text":uiScriptLocale.GAME_STAT_UP, 
					"r":1.0, "g":1.0, "b":1.0, "a":1.0, 
					"text_horizontal_align":"center" 
				},		
			),
		},
		{ 
			"name":"SoldItemButton", 
			"type" : "button", 
			"x" : SCREEN_WIDTH-180, 
			"y" : 25, 
			"default_image" : "icon/item/50200.tga",
			"over_image" : "icon/item/50200.tga",
			"down_image" : "icon/item/50200.tga"
		},
		#{ 
		#	"name":"ChatColorButton", 
		#	"type":"button", 
		#	"x" : SCREEN_WIDTH/2 + 302,
		#	"y" : SCREEN_HEIGHT - 23 - 37,
		#	"default_image" : "d:/ymir work/ui/chat/color_icon.tga",
		#	"over_image" : "d:/ymir work/ui/chat/color_icon.tga",
		#	"down_image" : "d:/ymir work/ui/chat/color_icon.tga",
		#	"disable_image" : "d:/ymir work/ui/chat/color_icon_disabled.tga",
		#	"tooltip_text": localeInfo.CHAT_COLOR_PALETTE,
		#},
		{ 
			"name":"SkillPlusButton", 
			"type" : "button", 
			"x" : SCREEN_WIDTH-50-32,
			"y" : SCREEN_HEIGHT-150,
			"default_image" : "d:/ymir work/ui/game/windows/btn_bigplus_up.sub",
			"over_image" : "d:/ymir work/ui/game/windows/btn_bigplus_over.sub",
			"down_image" : "d:/ymir work/ui/game/windows/btn_bigplus_down.sub",

			"children" : 
			(
				{ 
					"name":"SkillPlusLabel", 
					"type":"text", 
					"x": 16, 
					"y": 40, 
					"text":uiScriptLocale.GAME_SKILL_UP, 
					"r":1.0, "g":1.0, "b":1.0, "a":1.0, 
					"text_horizontal_align":"center" 
				},	
			),
		},			
		{ 
			"name":"ExitObserver", 
			"type" : "button", 
			"x" : SCREEN_WIDTH-50-32,
			"y" : SCREEN_HEIGHT-170,
			"default_image" : "d:/ymir work/ui/game/windows/btn_bigplus_up.sub",
			"over_image" : "d:/ymir work/ui/game/windows/btn_bigplus_over.sub",
			"down_image" : "d:/ymir work/ui/game/windows/btn_bigplus_down.sub",

			"children" : 
			(
				{ 
					"name":"ExitObserverButtonName", 
					"type":"text", 
					"x": 16, 
					"y": 40, 
					"text": uiScriptLocale.GAME_EXIT_OBSERVER, 
					"r":1.0, "g":1.0, "b":1.0, "a":1.0, 
					"text_horizontal_align":"center" 
				},	
			),
		},
		{ 
			"name":"BuildGuildBuilding",
			"type" : "button",
			"x" : SCREEN_WIDTH-50-32,
			"y" : SCREEN_HEIGHT-170,
			"default_image" : "d:/ymir work/ui/game/windows/btn_bigplus_up.sub",
			"over_image" : "d:/ymir work/ui/game/windows/btn_bigplus_over.sub",
			"down_image" : "d:/ymir work/ui/game/windows/btn_bigplus_down.sub",

			"children" : 
			(
				{ 
					"name":"BuildGuildBuildingButtonName",
					"type":"text",
					"x": 16,
					"y": 40,
					"text": uiScriptLocale.GUILD_BUILDING_TITLE,
					"r":1.0, "g":1.0, "b":1.0, "a":1.0,
					"text_horizontal_align":"center"
				},	
			),
		},
	),
}
