import uiScriptLocale

UI_WIDTH = 420
UI_HEIGHT = 364

UI_X = 0
UI_Y = 0

window = {
	"name" : "SwitchWindow",
	"x" : (SCREEN_WIDTH/4)-70,
	"y" : (SCREEN_HEIGHT/2)-(UI_HEIGHT/2),
	"style" : ("movable", "float",),
	"width" : UI_WIDTH,
	"height" : UI_HEIGHT,
	"children" :
	(
		{
			"name" : "board",
			"type" : "board",
			"x" : 0,
			"y" : 0,
			"width" : UI_WIDTH,
			"height" : UI_HEIGHT,
			# "title": "",
			"children" :
			(
				{
					"name" : "background",
					"type" : "image",
					"x" : 0,
					"y" : 0,
					"width" : UI_WIDTH,
					"height" : UI_HEIGHT,
					"image" : "d:/ymir work/ui/game/blackjack/bg3.tga",
					"horizontal_align": "center",
				},
				{
					"name" : "stopButton",
					"type" : "button",
					"x" : -(88/2),
					"y" : 60,
					"default_image" : "d:/ymir work/ui/game/blackjack/btn_stop_normal.tga",
					"over_image" : "d:/ymir work/ui/game/blackjack/btn_stop_hover.tga",
					"down_image" : "d:/ymir work/ui/game/blackjack/btn_stop_down.tga",
					"text": uiScriptLocale.BLACKJACK_STAY,

					"horizontal_align":"center",
					"vertical_align": "bottom",
				},
				{
					"name" : "confirmButton",
					"type" : "button",
					"x" : (88/2),
					"y" : 60,
					"default_image" : "d:/ymir work/ui/game/blackjack/btn_confirm_normal.tga",
					"over_image" : "d:/ymir work/ui/game/blackjack/btn_confirm_hover.tga",
					"down_image" : "d:/ymir work/ui/game/blackjack/btn_confirm_down.tga",
					"text": uiScriptLocale.BLACKJACK_HIT,

					"horizontal_align": "center",
					"vertical_align": "bottom",
				},
				{
					"name" : "startButton",
					"type" : "button",
					"x" : 0,
					"y" : 90,
					"default_image" : "d:/ymir work/ui/game/blackjack/btn_confirm_normal.tga",
					"over_image" : "d:/ymir work/ui/game/blackjack/btn_confirm_hover.tga",
					"down_image" : "d:/ymir work/ui/game/blackjack/btn_confirm_down.tga",
					"text": uiScriptLocale.BLACKJACK_START_GAME,

					"horizontal_align": "center",
					"vertical_align": "bottom",
				},
			),
		},
	),
}