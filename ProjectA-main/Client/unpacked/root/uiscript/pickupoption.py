import uiScriptLocale

WINDOW_WIDTH = 294
WINDOW_HIGHT = 145

ROOT_PATH = "d:/ymir work/ui/public/"

LINE_LABEL_X		= 22
LINE_DATA_X			= 100
MIDDLE_BUTTON_WIDTH	= 65

window = {
	"name" : "PickupOption",

	"x" : 0,
	"y" : 0,

	"style" : ("movable", "float",),

	"width" : WINDOW_WIDTH,
	"height" : WINDOW_HIGHT,

	"children" :
	(
		{
			"name" : "board",
			"type" : "board",
			"style" : ("attach",),

			"x" : 0,
			"y" : 0,

			"width" : WINDOW_WIDTH,
			"height" : WINDOW_HIGHT,

			"children" :
			(
				## Title
				{
					"name" : "TitleBar",
					"type" : "titlebar",
					"style" : ("attach",),

					"x" : 0,
					"y" : 0,

					"width" : WINDOW_WIDTH,

					"children" :
					(
						{ "name" : "TitleName", "type" : "text", "x" : 0, "y" : -1, "text" : uiScriptLocale.SYSTEM_PICK_OPTION, "all_align" : "center" },
					),
				},

				## Pickup filter
				{
					"name" : "pickup",
					"type" : "text",

					"x" : LINE_LABEL_X - 10,
					"y" : 10 + 25 + 9,

					"text" : uiScriptLocale.OPTION_DISABLE_PICKUP,
					"text_vertical_align" : "center",
				},
				{
					"name" : "disable_pickup_weapon",
					"type" : "toggle_button",

					"x" : LINE_DATA_X+MIDDLE_BUTTON_WIDTH*0,
					"y" : 10 + 25,

					"text" : uiScriptLocale.OPTION_DISABLE_PICKUP_WEAPON,

					"default_image" : ROOT_PATH + "middle_button_01.sub",
					"over_image" : ROOT_PATH + "middle_button_02.sub",
					"down_image" : ROOT_PATH + "middle_button_03.sub",
				},
				{
					"name" : "disable_pickup_armor",
					"type" : "toggle_button",

					"x" : LINE_DATA_X+MIDDLE_BUTTON_WIDTH*1,
					"y" : 10 + 25,

					"text" : uiScriptLocale.OPTION_DISABLE_PICKUP_ARMOR,

					"default_image" : ROOT_PATH + "middle_button_01.sub",
					"over_image" : ROOT_PATH + "middle_button_02.sub",
					"down_image" : ROOT_PATH + "middle_button_03.sub",
				},
				{
					"name" : "disable_pickup_etc",
					"type" : "toggle_button",

					"x" : LINE_DATA_X+MIDDLE_BUTTON_WIDTH*2,
					"y" : 10 + 25,

					"text" : uiScriptLocale.OPTION_DISABLE_PICKUP_ETC,

					"default_image" : ROOT_PATH + "middle_button_01.sub",
					"over_image" : ROOT_PATH + "middle_button_02.sub",
					"down_image" : ROOT_PATH + "middle_button_03.sub",
				},
				{
					"name" : "disable_pickup_potion",
					"type" : "toggle_button",

					"x" : LINE_DATA_X+MIDDLE_BUTTON_WIDTH*0,
					"y" : 10 + 25*2,

					"text" : uiScriptLocale.PICKUP_CATEGORY_POTION,

					"default_image" : ROOT_PATH + "middle_button_01.sub",
					"over_image" : ROOT_PATH + "middle_button_02.sub",
					"down_image" : ROOT_PATH + "middle_button_03.sub",
				},
				{
					"name" : "disable_pickup_book",
					"type" : "toggle_button",

					"x" : LINE_DATA_X+MIDDLE_BUTTON_WIDTH*1,
					"y" : 10 + 25*2,

					"text" : uiScriptLocale.PICKUP_CATEGORY_BOOK,

					"default_image" : ROOT_PATH + "middle_button_01.sub",
					"over_image" : ROOT_PATH + "middle_button_02.sub",
					"down_image" : ROOT_PATH + "middle_button_03.sub",
				},


				## Pickup all
				{
					"name" : "pickup_all",
					"type" : "text",

					"x" : LINE_LABEL_X - 10,
					"y" : 10 + 25*3 + 9,

					"text" : uiScriptLocale.OPTION_PICKUP_ALL,
					"text_vertical_align" : "center",
				},
				{
					"name" : "pickup_all_fast",
					"type" : "toggle_button",

					"x" : LINE_DATA_X+MIDDLE_BUTTON_WIDTH*0,
					"y" : 10 + 25*3,

					"text" : uiScriptLocale.OPTION_PICKUP_FAST,

					"default_image" : ROOT_PATH + "middle_button_01.sub",
					"over_image" : ROOT_PATH + "middle_button_02.sub",
					"down_image" : ROOT_PATH + "middle_button_03.sub",
				},
				{
					"name" : "pickup_all_slow",
					"type" : "toggle_button",

					"x" : LINE_DATA_X+MIDDLE_BUTTON_WIDTH*1,
					"y" : 10 + 25*3,

					"text" : uiScriptLocale.OPTION_PICKUP_SLOW,

					"default_image" : ROOT_PATH + "middle_button_01.sub",
					"over_image" : ROOT_PATH + "middle_button_02.sub",
					"down_image" : ROOT_PATH + "middle_button_03.sub",
				},


				# Pickup Item Size
				{
					"name" : "pickup_size",
					"type" : "text",

					"x" : LINE_LABEL_X - 10,
					"y" : 10 + 25*4 + 9,

					"text" : uiScriptLocale.PICKUP_CATEGORY_SIZE_TITLE,
					"text_vertical_align" : "center",
				},
				{
					"name" : "pickup_size_1",
					"type" : "toggle_button",

					"x" : LINE_DATA_X+MIDDLE_BUTTON_WIDTH*0,
					"y" : 10 + 25*4,

					"text" : uiScriptLocale.PICKUP_CATEGORY_SIZE_1,

					"default_image" : ROOT_PATH + "middle_button_01.sub",
					"over_image" : ROOT_PATH + "middle_button_02.sub",
					"down_image" : ROOT_PATH + "middle_button_03.sub",
				},
				{
					"name" : "pickup_size_2",
					"type" : "toggle_button",

					"x" : LINE_DATA_X+MIDDLE_BUTTON_WIDTH*1,
					"y" : 10 + 25*4,

					"text" : uiScriptLocale.PICKUP_CATEGORY_SIZE_2,

					"default_image" : ROOT_PATH + "middle_button_01.sub",
					"over_image" : ROOT_PATH + "middle_button_02.sub",
					"down_image" : ROOT_PATH + "middle_button_03.sub",
				},
				{
					"name" : "pickup_size_3",
					"type" : "toggle_button",

					"x" : LINE_DATA_X+MIDDLE_BUTTON_WIDTH*2,
					"y" : 10 + 25*4,

					"text" : uiScriptLocale.PICKUP_CATEGORY_SIZE_3,

					"default_image" : ROOT_PATH + "middle_button_01.sub",
					"over_image" : ROOT_PATH + "middle_button_02.sub",
					"down_image" : ROOT_PATH + "middle_button_03.sub",
				},
			),
		},
	),
}
