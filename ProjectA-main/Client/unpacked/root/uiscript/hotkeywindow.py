import uiScriptLocale

BOARD_WIDTH = 250
BOARD_HEIGHT = 146

window = {
	"name" : "HotkeyWindow",

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

			"title" : uiScriptLocale.HOTKEY_TITLE_TEXT,

			"children" :
			(
				{
					"name" : "text",
					"type" : "extended_text",
					"style" : ("attach",),

					"x" : 0,
					"y" : 73,

					"horizontal_align" : "center",
				},
			
				{
					"name" : "hotkey_button",
					"type" : "button",

					"x" : 0,
					"y" : 102,

					"default_image" : "d:/ymir work/ui/public/XLarge_Button_01.sub",
					"over_image" : "d:/ymir work/ui/public/XLarge_Button_02.sub",
					"down_image" : "d:/ymir work/ui/public/XLarge_Button_03.sub",
					"disable_image" : "d:/ymir work/ui/public/XLarge_Button_04.sub",

					"horizontal_align" : "center",
				},
			),
		},
	),
}
