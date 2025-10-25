import uiScriptLocale

BOARD_WIDTH = 368
BOARD_HEIGHT = 443

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
			"type" : "image",
			"style" : ("attach",),

			"x" : 0,
			"y" : 0,

			"image" : "d:/ymir work/ui/game/offlineshop/tab_main/bg_2.tga",

			"children" :
			(
				## TITLE BAR
				{
					"name" : "title_bar",
					"type" : "titlebar",
					"style" : ("attach",),

					"x" : 8,
					"y" : 8,

					"width" : BOARD_WIDTH - 16,
					"color" : "red",

					"children" :
					(
						{
							"name" : "title_name",
							"type" : "text",
							"text" : uiScriptLocale.OFFLINE_SHOP_CREATE_TITLE,
							"horizontal_align" : "center",
							"text_horizontal_align" : "center",
							"x" : 0,
							"y" : 3,
						},
					),
				},
				## SHOP NAME
				{
					"name" : "shop_name_bg",
					"type" : "image",

					"x" : 16,
					"y" : 35,

					"image" : "d:/ymir work/ui/game/offlineshop/tab_main/namefield2.tga",

					"children" :
					(
						{
							"name" : "NameLine",
							"type" : "text",
							"text" : "",
							"horizontal_align" : "left",
							"text_horizontal_align" : "left",
							"x" : 9,
							"y" : 6,
						},
					),
				},
				## Button Visuals
				{
					"name" : "button_visuals",
					"type" : "button",

					"x" : 277,
					"y" : 35,

					"default_image" : "d:/ymir work/ui/game/offlineshop/tab_main/btn_4_normal.tga",
					"over_image" : "d:/ymir work/ui/game/offlineshop/tab_main/btn_4_hover.tga",
					"down_image" : "d:/ymir work/ui/game/offlineshop/tab_main/btn_4_down.tga",

					"tooltip_text" : uiScriptLocale.OFFLINE_SHOP_CHANGE_APPEARANCE,
				},
				## Item Slot
				{
					"name" : "ItemSlot",
					"type" : "grid_table",

					"x" : 23,
					"y" : 81,

					"start_index" : 0,
					"x_count" : 5,
					"y_count" : 8,
					"x_step" : 32,
					"y_step" : 32,
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

					"x" : 8 + 20,
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

					"x" : 8 + 61 + 20,
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
