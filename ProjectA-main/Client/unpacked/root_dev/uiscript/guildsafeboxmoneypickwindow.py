import ui
import uiScriptLocale

BOARD_WIDTH = 300
BOARD_HEIGHT = 78

window = {
	"name" : "GuildSafeboxMoney",
	"style" : ("movable", "float",),

	"x" : SCREEN_WIDTH / 2 - BOARD_WIDTH / 2,
	"y" : SCREEN_HEIGHT / 2 - BOARD_HEIGHT / 2,

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

			"title" : uiScriptLocale.GUILD_SAFEBOX_MONEY_TITLE,

			"children" :
			(
				{
					"name" : "info",
					"type" : "text",

					"x" : 0,
					"y" : 7,

					"horizontal_align" : "center",
					"text_horizontal_align" : "center",

					"text" : uiScriptLocale.GUILD_SAFEBOX_MONEY_INFO_TEXT,
				},
				{
					"name" : "input_field",
					"type" : "field",

					"x" : 0,
					"y" : 25,

					"width" : 100,
					"height" : 18,

					"horizontal_align" : "center",

					"children" :
					(
						{
							"name" : "input",
							"type" : "editline",

							"x" : 3,
							"y" : 3,

							"width" : 100 - 4,
							"height" : 18 - 4,

							"only_number" : True,
							"input_limit" : 9,
							"overlay" : "0",
						},
					),
				},
				{
					"name" : "give_button",
					"type" : "button",

					"x" : 35,
					"y" : 5 + 24,

					"vertical_align" : "bottom",

					"default_image" : "d:/ymir work/ui/public/Large_Button_01.sub",
					"over_image" : "d:/ymir work/ui/public/Large_Button_02.sub",
					"down_image" : "d:/ymir work/ui/public/Large_Button_03.sub",

					"text" : uiScriptLocale.GUILD_SAFEBOX_MONEY_GIVE_BUTTON,
				},
				{
					"name" : "take_button",
					"type" : "button",

					"x" : 40 + 88,
					"y" : 5 + 24,

					"horizontal_align" : "right",
					"vertical_align" : "bottom",

					"default_image" : "d:/ymir work/ui/public/Large_Button_01.sub",
					"over_image" : "d:/ymir work/ui/public/Large_Button_02.sub",
					"down_image" : "d:/ymir work/ui/public/Large_Button_03.sub",

					"text" : uiScriptLocale.GUILD_SAFEBOX_MONEY_TAKE_BUTTON,
				},
			),
		},
	),
}
