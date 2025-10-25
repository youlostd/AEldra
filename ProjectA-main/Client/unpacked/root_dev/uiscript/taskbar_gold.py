import uiScriptLocale

ROOT = "d:/ymir work/ui/game/"

GAYA_SLOT_X = 18 + 8
MONEY_SLOT_X = GAYA_SLOT_X + 61 + 18 + 4

BOARD_WIDTH = MONEY_SLOT_X + 130 + 7
BOARD_HEIGHT = 30

window = {
	"name" : "TaskBar",

	"x" : 0,
	"y" : 0,

	"width" : BOARD_WIDTH,
	"height" : BOARD_HEIGHT,

	"children" :
	(
		## Board
		{
			"name" : "board",
			"type" : "board",

			"x" : 0,
			"y" : 0,

			"width" : BOARD_WIDTH,
			"height" : BOARD_HEIGHT,

			"children" :
			(
				{
					"name":"Gaya_Slot",
					"type":"button",

					"x":GAYA_SLOT_X,
					"y":5,

					"default_image" : "d:/ymir work/ui/public/parameter_slot_02.sub",
					"over_image" : "d:/ymir work/ui/public/parameter_slot_02.sub",
					"down_image" : "d:/ymir work/ui/public/parameter_slot_02.sub",
					"children" :

					(
						{
							"name":"Gaya_Icon",
							"type":"image",

							"x":-18,
							"y":3,

							"image":"d:/ymir work/ui/gemshop/gemshop_gemicon.sub",
						},
						{
							"name" : "Gaya",
							"type" : "text",

							"x" : 3,
							"y" : 3,

							"horizontal_align" : "right",
							"text_horizontal_align" : "right",

							"text" : "123456",
						},
					),
				},
				## MoneySlot
				{
					"name":"Money_Slot",
					"type":"button",

					"x":MONEY_SLOT_X,
					"y":5,

					"default_image" : "d:/ymir work/ui/public/parameter_slot_05.sub",
					"over_image" : "d:/ymir work/ui/public/parameter_slot_05.sub",
					"down_image" : "d:/ymir work/ui/public/parameter_slot_05.sub",

					"children" :
					(
						{
							"name":"Money_Icon",
							"type":"image",

							"x":-18,
							"y":2,

							"image":"d:/ymir work/ui/game/windows/money_icon.sub",
						},

						{
							"name" : "Money",
							"type" : "text",

							"x" : 3,
							"y" : 3,

							"horizontal_align" : "right",
							"text_horizontal_align" : "right",

							"text" : "123456789",
						},
					),
				},
			),
		},
	),
}
