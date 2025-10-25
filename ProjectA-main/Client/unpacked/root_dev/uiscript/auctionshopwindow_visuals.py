import uiScriptLocale

WIDTH = 554
HEIGHT = 334

window = {

	"name" : "AuctionShopWindowVisuals",

	# CENTER
	"x" : (SCREEN_WIDTH / 2) - (WIDTH / 2),
	"y" : (SCREEN_HEIGHT / 2) - (HEIGHT / 2),

	"style" : ("movable", "float",),

	"width" : WIDTH,
	"height" : HEIGHT,

	"children" :
	(
		{
			"name" : "background",
			"type" : "image",
			"style" : ("attach",),

			"x" : 0,
			"y" : 0,

			"image" : "d:/ymir work/ui/game/offlineshop/tab_visuals/bg.tga",

			"children" :
			(
				## BUTTONS
				{
					"name" : "button_save",
					"type" : "button",

					"x" : -50,
					"y" : 55,

					"text" : uiScriptLocale.SAVE,

					"horizontal_align" : "center",
					"vertical_align" : "bottom",

					"default_image" : "d:/ymir work/ui/game/offlineshop/tab_visuals/btn_normal.tga",
					"over_image" : "d:/ymir work/ui/game/offlineshop/tab_visuals/btn_hover.tga",
					"down_image" : "d:/ymir work/ui/game/offlineshop/tab_visuals/btn_down.tga",
				},

				{
					"name" : "button_close",
					"type" : "button",

					"x" : 50,
					"y" : 55,

					"text" : uiScriptLocale.CLOSE,

					"horizontal_align" : "center",
					"vertical_align" : "bottom",

					"default_image" : "d:/ymir work/ui/game/offlineshop/tab_visuals/btn_normal.tga",
					"over_image" : "d:/ymir work/ui/game/offlineshop/tab_visuals/btn_hover.tga",
					"down_image" : "d:/ymir work/ui/game/offlineshop/tab_visuals/btn_down.tga",
				},

				## SLOTS
				{
					"name" : "slot_left_1",
					"type" : "radio_button",

					"x" : 28,
					"y" : 46 + 33 * 0,

					"text" : "",

					"horizontal_align" : "left",

					"default_image" : "d:/ymir work/ui/game/offlineshop/tab_visuals/slot_locked_normal.tga",
					"over_image" : "d:/ymir work/ui/game/offlineshop/tab_visuals/slot_locked_hover.tga",
					"down_image" : "d:/ymir work/ui/game/offlineshop/tab_visuals/slot_locked_selected.tga",
				},

				{
					"name" : "slot_left_2",
					"type" : "radio_button",

					"x" : 28,
					"y" : 46 + 33 * 1,

					"text" : "",

					"horizontal_align" : "left",

					"default_image" : "d:/ymir work/ui/game/offlineshop/tab_visuals/slot_locked_normal.tga",
					"over_image" : "d:/ymir work/ui/game/offlineshop/tab_visuals/slot_locked_hover.tga",
					"down_image" : "d:/ymir work/ui/game/offlineshop/tab_visuals/slot_locked_selected.tga",
				},

				{
					"name" : "slot_left_3",
					"type" : "radio_button",

					"x" : 28,
					"y" : 46 + 33 * 2,

					"text" : "",

					"horizontal_align" : "left",

					"default_image" : "d:/ymir work/ui/game/offlineshop/tab_visuals/slot_locked_normal.tga",
					"over_image" : "d:/ymir work/ui/game/offlineshop/tab_visuals/slot_locked_hover.tga",
					"down_image" : "d:/ymir work/ui/game/offlineshop/tab_visuals/slot_locked_selected.tga",
				},

				{
					"name" : "slot_left_4",
					"type" : "radio_button",

					"x" : 28,
					"y" : 46 + 33 * 3,

					"text" : "",

					"horizontal_align" : "left",

					"default_image" : "d:/ymir work/ui/game/offlineshop/tab_visuals/slot_locked_normal.tga",
					"over_image" : "d:/ymir work/ui/game/offlineshop/tab_visuals/slot_locked_hover.tga",
					"down_image" : "d:/ymir work/ui/game/offlineshop/tab_visuals/slot_locked_selected.tga",
				},

				{
					"name" : "slot_left_5",
					"type" : "radio_button",

					"x" : 28,
					"y" : 46 + 33 * 4,

					"text" : "",

					"horizontal_align" : "left",

					"default_image" : "d:/ymir work/ui/game/offlineshop/tab_visuals/slot_locked_normal.tga",
					"over_image" : "d:/ymir work/ui/game/offlineshop/tab_visuals/slot_locked_hover.tga",
					"down_image" : "d:/ymir work/ui/game/offlineshop/tab_visuals/slot_locked_selected.tga",
				},

				{
					"name" : "slot_left_6",
					"type" : "radio_button",

					"x" : 28,
					"y" : 46 + 33 * 5,

					"text" : "",

					"horizontal_align" : "left",

					"default_image" : "d:/ymir work/ui/game/offlineshop/tab_visuals/slot_locked_normal.tga",
					"over_image" : "d:/ymir work/ui/game/offlineshop/tab_visuals/slot_locked_hover.tga",
					"down_image" : "d:/ymir work/ui/game/offlineshop/tab_visuals/slot_locked_selected.tga",
				},

				{
					"name" : "slot_left_7",
					"type" : "radio_button",

					"x" : 28,
					"y" : 46 + 33 * 6,

					"text" : "",

					"horizontal_align" : "left",

					"default_image" : "d:/ymir work/ui/game/offlineshop/tab_visuals/slot_locked_normal.tga",
					"over_image" : "d:/ymir work/ui/game/offlineshop/tab_visuals/slot_locked_hover.tga",
					"down_image" : "d:/ymir work/ui/game/offlineshop/tab_visuals/slot_locked_selected.tga",
				},

				{
					"name" : "slot_right_1",
					"type" : "radio_button",

					"x" : 28 + 158,
					"y" : 46 + 33 * 0,

					"text" : "",

					"horizontal_align" : "right",

					"default_image" : "d:/ymir work/ui/game/offlineshop/tab_visuals/slot_locked_normal.tga",
					"over_image" : "d:/ymir work/ui/game/offlineshop/tab_visuals/slot_locked_hover.tga",
					"down_image" : "d:/ymir work/ui/game/offlineshop/tab_visuals/slot_locked_selected.tga",
				},

				{
					"name" : "slot_right_2",
					"type" : "radio_button",

					"x" : 28 + 158,
					"y" : 46 + 33 * 1,

					"text" : "",

					"horizontal_align" : "right",

					"default_image" : "d:/ymir work/ui/game/offlineshop/tab_visuals/slot_locked_normal.tga",
					"over_image" : "d:/ymir work/ui/game/offlineshop/tab_visuals/slot_locked_hover.tga",
					"down_image" : "d:/ymir work/ui/game/offlineshop/tab_visuals/slot_locked_selected.tga",
				},

				{
					"name" : "slot_right_3",
					"type" : "radio_button",

					"x" : 28 + 158,
					"y" : 46 + 33 * 2,

					"text" : "",

					"horizontal_align" : "right",

					"default_image" : "d:/ymir work/ui/game/offlineshop/tab_visuals/slot_locked_normal.tga",
					"over_image" : "d:/ymir work/ui/game/offlineshop/tab_visuals/slot_locked_hover.tga",
					"down_image" : "d:/ymir work/ui/game/offlineshop/tab_visuals/slot_locked_selected.tga",
				},

				{
					"name" : "slot_right_4",
					"type" : "radio_button",

					"x" : 28 + 158,
					"y" : 46 + 33 * 3,

					"text" : "",

					"horizontal_align" : "right",

					"default_image" : "d:/ymir work/ui/game/offlineshop/tab_visuals/slot_locked_normal.tga",
					"over_image" : "d:/ymir work/ui/game/offlineshop/tab_visuals/slot_locked_hover.tga",
					"down_image" : "d:/ymir work/ui/game/offlineshop/tab_visuals/slot_locked_selected.tga",
				},

				{
					"name" : "slot_right_5",
					"type" : "radio_button",

					"x" : 28 + 158,
					"y" : 46 + 33 * 4,

					"text" : "",

					"horizontal_align" : "right",

					"default_image" : "d:/ymir work/ui/game/offlineshop/tab_visuals/slot_locked_normal.tga",
					"over_image" : "d:/ymir work/ui/game/offlineshop/tab_visuals/slot_locked_hover.tga",
					"down_image" : "d:/ymir work/ui/game/offlineshop/tab_visuals/slot_locked_selected.tga",
				},

				{
					"name" : "slot_right_6",
					"type" : "radio_button",

					"x" : 28 + 158,
					"y" : 46 + 33 * 5,

					"text" : "",

					"horizontal_align" : "right",

					"default_image" : "d:/ymir work/ui/game/offlineshop/tab_visuals/slot_locked_normal.tga",
					"over_image" : "d:/ymir work/ui/game/offlineshop/tab_visuals/slot_locked_hover.tga",
					"down_image" : "d:/ymir work/ui/game/offlineshop/tab_visuals/slot_locked_selected.tga",
				},

				{
					"name" : "slot_right_7",
					"type" : "radio_button",

					"x" : 28 + 158,
					"y" : 46 + 33 * 6,

					"text" : "",

					"horizontal_align" : "right",

					"default_image" : "d:/ymir work/ui/game/offlineshop/tab_visuals/slot_locked_normal.tga",
					"over_image" : "d:/ymir work/ui/game/offlineshop/tab_visuals/slot_locked_hover.tga",
					"down_image" : "d:/ymir work/ui/game/offlineshop/tab_visuals/slot_locked_selected.tga",
				},
			),
		},
	),
}