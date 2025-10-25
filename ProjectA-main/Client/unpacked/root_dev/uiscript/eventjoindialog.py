import uiScriptLocale

BOARD_WIDTH = 304

window = {
	"name" : "EventJoinDialog",

	"x" : SCREEN_WIDTH / 2 - BOARD_WIDTH / 2,
	"y" : SCREEN_HEIGHT / 2,

	"style" : ("movable", "float",),

	"width"  : BOARD_WIDTH,
	"height" : 0,

	"children" :
	(
		{
			"name" : "board",
			"type" : "board_with_titlebar",
			"style" : ("attach",),

			"x" : 0,
			"y" : 0,

			"width" : BOARD_WIDTH,
			"height" : 0,

			"title" : uiScriptLocale.EVENT_JOIN_TITLE,

			"children" :
			(
				{
					"name" : "event_name_text",
					"type" : "text",

					"x" : 0,
					"y" : 10,

					"horizontal_align" : "center",
					"text_horizontal_align" : "center",
					"style" : ("movable", "float",),
					"r" : 1.0,
					"g" : 0.7137,
					"b" : 0.0,
				},
				{
					"name" : "event_desc_text",
					"type" : "multi_text",

					"x" : 20,
					"y" : 26,

					"width" : BOARD_WIDTH - 20 * 2,
					"style" : ("movable", "float",),
					"text_horizontal_align" : "center",
				},
				{
					"name" : "accept_button",
					"type" : "button",

					"x" : BOARD_WIDTH / 4 * 1 - 88 / 2,
					"y" : 0,

					"default_image" : "d:/ymir work/ui/public/Large_Button_01.sub",
					"over_image" : "d:/ymir work/ui/public/Large_Button_02.sub",
					"down_image" : "d:/ymir work/ui/public/Large_Button_03.sub",

					"text" : uiScriptLocale.EVENT_JOIN_ACCEPT_BUTTON,
				},
				{
					"name" : "decline_button",
					"type" : "button",

					"x" : BOARD_WIDTH / 4 * 3 - 88 / 2,
					"y" : 0,

					"default_image" : "d:/ymir work/ui/public/Large_Button_01.sub",
					"over_image" : "d:/ymir work/ui/public/Large_Button_02.sub",
					"down_image" : "d:/ymir work/ui/public/Large_Button_03.sub",

					"text" : uiScriptLocale.EVENT_JOIN_DECLINE_BUTTON,
				},
			),
		},
	),
}
