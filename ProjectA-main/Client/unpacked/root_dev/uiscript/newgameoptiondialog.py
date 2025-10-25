import uiScriptLocale
 
LINE_LABEL_X 	= 22
ROOT_PATH = "d:/ymir work/ui/public/"
MIDDLE_BUTTON_WIDTH 	= 65


window = {
	"name" : "GameOptionDialog",
	"style" : ("movable", "float",),

	"x" : 0,
	"y" : 0,

	"width" : 284+10+25,
	"height" : 25*18+53 + 22,

	"children" :
	(
		{
			"name" : "board",
			"type" : "board",

			"x" : 0,
			"y" : 0,

			"width" : 284+10+25,
			"height" : 25*18,

			"children" :
			(
				## Title
				{
					"name" : "TitleBar",
					"type" : "titlebar",
					"style" : ("attach",),

					"x" : 0,
					"y" : 0,

					"width" : 284+10+25,
					"color" : "gray",

					"children" :
					(
						{ "name":"titlename", "type":"text", "x":0, "y":3, 
						"text" : uiScriptLocale.GAMEOPTION_TITLE, 
						"horizontal_align":"center", "text_horizontal_align":"center" },
					),
				},
				{
					"name" : "ScrollBar",
					"type" : "scrollbar",

					"x" : 20,
					"y" : 40,
					"size" : 400,
					"horizontal_align" : "right",
				},
			),
		},
		{
			"name" : "board2",
			"type" : "board",

			"x" : 0,
			"y" : (25*18)+5,

			"width" : 284+10+25,
			"height" : 53 + 22,

			"children" :
			(
				## Title
				{
					"name" : "titlebar2",
					"type" : "titlebar",
					"style" : ("attach",),

					"x" : 0,
					"y" : 0,

					"width" : 284+10+22,
					"color" : "gray",

					"children" :
					(
						{ "name":"titlename", "type":"text", "x":0, "y":3, 
						"text" : uiScriptLocale.GAMEOPTION_TITLE_EXTRA, 
						"horizontal_align":"center", "text_horizontal_align":"center" },
					),
				},

				## Hide costumes
				{
					"name" : "hide_costume_text",
					"type" : "text",

					"x" : LINE_LABEL_X,
					"y" : 33-5+2,

					"text" : uiScriptLocale.HIDE_COSTUMES,
				},
				{
					"name" : "hide_costume_weapon",
					"type" : "toggle_button",

					"x" : 20+MIDDLE_BUTTON_WIDTH*0,
					"y" : 33-5 + 20,

					"text" : uiScriptLocale.SHOP_SEARCH_CAT_WEAPON,

					"default_image" : ROOT_PATH + "Middle_Button_01.sub",
					"over_image" : ROOT_PATH + "Middle_Button_02.sub",
					"down_image" : ROOT_PATH + "Middle_Button_03.sub",
				},
				{
					"name" : "hide_costume_armor",
					"type" : "toggle_button",

					"x" : 20+MIDDLE_BUTTON_WIDTH*1,
					"y" : 33-5 + 20,

					"text" : uiScriptLocale.SHOP_SEARCH_CAT_ARMOR,

					"default_image" : ROOT_PATH + "Middle_Button_01.sub",
					"over_image" : ROOT_PATH + "Middle_Button_02.sub",
					"down_image" : ROOT_PATH + "Middle_Button_03.sub",
				},
				{
					"name" : "hide_costume_hair",
					"type" : "toggle_button",

					"x" : 20+MIDDLE_BUTTON_WIDTH*2,
					"y" : 33-5 + 20,

					"text" : uiScriptLocale.GAMEOPTION_HAIR,

					"default_image" : ROOT_PATH + "Middle_Button_01.sub",
					"over_image" : ROOT_PATH + "Middle_Button_02.sub",
					"down_image" : ROOT_PATH + "Middle_Button_03.sub",
				},
				{
					"name" : "hide_costume_acce",
					"type" : "toggle_button",

					"x" : 20+MIDDLE_BUTTON_WIDTH*3,
					"y" : 33-5 + 20,

					"text" : uiScriptLocale.GAMEOPTION_ACCE,

					"default_image" : ROOT_PATH + "Middle_Button_01.sub",
					"over_image" : ROOT_PATH + "Middle_Button_02.sub",
					"down_image" : ROOT_PATH + "Middle_Button_03.sub",
				},
			),
		},
	),
}

