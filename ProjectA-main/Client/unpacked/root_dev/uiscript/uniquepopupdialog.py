import uiScriptLocale
import localeInfo

window = {
	"name" : "PopupDialog",
	"style" : ("float",),

	"x" : SCREEN_WIDTH/2 - 250,
	"y" : SCREEN_HEIGHT/2 - 40,

	"width" : 280,
	"height" : 105,

	"children" :
	(
		{
			"name" : "board",
			"type" : "board",

			"x" : 0,
			"y" : 0,

			"width" : 280,
			"height" : 65,

			"children" :
			(
				{
					"name" : "message",
					"type" : "multi_text",

					"x" : 0,
					"y" : 38,

					"text" : uiScriptLocale.MESSAGE,

					"width" : 280 - 25 * 2,

					"horizontal_align" : "center",
					"text_horizontal_align" : "center",
					"text_vertical_align" : "center",
				},
				{
					"name" : "never_again",
					"type" : "checkbox",

					"x" : 0,
					"y" : 63,

					"checked" : True,

					"horizontal_align" : "center",
					"vertical_align" : "bottom",

					"text" : localeInfo.UNIQUE_POPUP_DIALOG_NEVER_SHOW_AGAIN,
				},
				{
					"name" : "accept",
					"type" : "button",

					"x" : 0,
					"y" : 40,

					"width" : 61,
					"height" : 21,

					"horizontal_align" : "center",
					"vertical_align" : "bottom",
					"text" : uiScriptLocale.OK,

					"default_image" : "d:/ymir work/ui/public/middle_button_01.sub",
					"over_image" : "d:/ymir work/ui/public/middle_button_02.sub",
					"down_image" : "d:/ymir work/ui/public/middle_button_03.sub",
				},
			),
		},
	),
}