import uiScriptLocale

BOARD_WIDTH = 200
BOARD_HEIGHT = 308

PATH = "d:/ymir work/ui/game/attrtree/"

window = {
	"name" : "AttrTreeRefineWindow",

	"x" : (SCREEN_WIDTH - BOARD_WIDTH) / 2,
	"y" : (SCREEN_HEIGHT - BOARD_HEIGHT) / 2,

	"style" : ("movable", "float",),

	"width" : BOARD_WIDTH,
	"height" : BOARD_HEIGHT,

	"children" :
	(
		{
			"name" : "board",
			"type" : "board_with_titlebar",
			"style" : ("attach",),

			"x" : 0,
			"y" : 0,

			"width" : BOARD_WIDTH,
			"height" : BOARD_HEIGHT,

			"title" : uiScriptLocale.ATTRTREE_REFINE_TITLE,

			"children" :
			(
				{
					"name" : "from_bonus",
					"type" : "text",

					"x" : 0,
					"y" : 0,

					"horizontal_align" : "center",
					"text_horizontal_align" : "center",

					"text" : "",
				},
				{
					"name" : "bonus_arrow",
					"type" : "image",

					"x" : 0,
					"y" : 20,

					"horizontal_align" : "center",
					"text_horizontal_align" : "center",

					"image" : PATH + "arrow_down.tga",
				},
				{
					"name" : "to_bonus",
					"type" : "text",

					"x" : 0,
					"y" : 20 + 20 + 5,

					"horizontal_align" : "center",
					"text_horizontal_align" : "center",

					"text" : "",
				},
				{
					"name" : "price",
					"type" : "text",

					"x" : 0,
					"y" : 24 + 5 + 18,

					"horizontal_align" : "center",
					"text_horizontal_align" : "center",
					"vertical_align" : "bottom",

					"text" : "",
				},
				{
					"name" : "upgrade_button",
					"type" : "button",

					"x" : -61/2 - 5,
					"y" : 24,

					"horizontal_align" : "center",
					"vertical_align" : "bottom",

					"default_image" : "d:/ymir work/ui/public/Middle_Button_01.sub",
					"over_image" : "d:/ymir work/ui/public/Middle_Button_02.sub",
					"down_image" : "d:/ymir work/ui/public/Middle_Button_03.sub",

					"text" : uiScriptLocale.ATTRTREE_REFINE_UPGRADE,
				},
				{
					"name" : "cancel_button",
					"type" : "button",

					"x" : 61/2 + 5,
					"y" : 24,

					"horizontal_align" : "center",
					"vertical_align" : "bottom",

					"default_image" : "d:/ymir work/ui/public/Middle_Button_01.sub",
					"over_image" : "d:/ymir work/ui/public/Middle_Button_02.sub",
					"down_image" : "d:/ymir work/ui/public/Middle_Button_03.sub",

					"text" : uiScriptLocale.ATTRTREE_REFINE_CANCEL,
				},
			),
		},
	),
}
