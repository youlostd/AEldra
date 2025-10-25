import uiScriptLocale

BOARD_WIDTH = 176
BOARD_HEIGHT = 7 + 25 + 8 * 32 + 5 + 25

window = {
	"name" : "PrivateShopBuilder",

	"x" : 0,
	"y" : 0,

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

			"children" :
			(
				## Name
				{
					"name" : "NameSlot",
					"type" : "slotbar",
					"x" : 8,
					"y" : 7,
					"width" : BOARD_WIDTH - 8 * 2,
					"height" : 18,

					"children" :
					(
						{
							"name" : "NameLine",
							"type" : "text",
							"x" : 3,
							"y" : 3,
							"text" : "1234567890123456789012345",
						},
					),
				},

				## Item Slot
				{
					"name" : "ItemSlot",
					"type" : "grid_table",

					"x" : 8,
					"y" : 7 + 25,

					"start_index" : 0,
					"x_count" : 5,
					"y_count" : 8,
					"x_step" : 32,
					"y_step" : 32,

					"image" : "d:/ymir work/ui/public/Slot_Base.sub",
				},

				{
					"name" : "ColorWindow",

					"x" : 0,
					"y" : 7 + 25 + 8 * 32 + 5,

					"width" : 175,
					"height" : 160 + 5 + 12,

					"horizontal_align" : "center",

					"children" :
					(
						{
							"name" : "ColorImage",
							"type" : "image",

							"x" : 0,
							"y" : 0,

							"image" : "d:/ymir work/ui/colorcircle.tga",
							"horizontal_align" : "center",
						},
						{
							"name" : "ColorBrightnessScroll",
							"type" : "sliderbar",

							"x" : 0,
							"y" : 160 + 5,
						},
					),
				},

				## Ok
				{
					"name" : "OkButton",
					"type" : "button",

					"x" : 8,
					"y" : 7 + 25 + 8 * 32 + 5,

					"width" : 61,
					"height" : 21,

					"text" : uiScriptLocale.OK,

					"default_image" : "d:/ymir work/ui/public/middle_button_01.sub",
					"over_image" : "d:/ymir work/ui/public/middle_button_02.sub",
					"down_image" : "d:/ymir work/ui/public/middle_button_03.sub",
				},

				## Close
				{
					"name" : "CloseButton",
					"type" : "button",

					"x" : 8 + 61,
					"y" : 7 + 25 + 8 * 32 + 5,

					"width" : 61,
					"height" : 21,

					"horizontal_align" : "right",

					"text" : uiScriptLocale.CLOSE,

					"default_image" : "d:/ymir work/ui/public/middle_button_01.sub",
					"over_image" : "d:/ymir work/ui/public/middle_button_02.sub",
					"down_image" : "d:/ymir work/ui/public/middle_button_03.sub",
				},
			),
		},
	),
}