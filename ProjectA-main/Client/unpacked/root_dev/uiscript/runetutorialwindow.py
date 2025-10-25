import uiScriptLocale
import localeInfo

TUTWINDOW_PATH 		= "d:/ymir work/ui/game/runes_tut/"
TUTWINDOW_WIDTH 	= 575
TUTWINDOW_HEIGHT 	= 535

window = {
	"name" : "RuneTutorialWindow",

	"x" : ( SCREEN_WIDTH - TUTWINDOW_WIDTH ) / 2,
	"y" : ( SCREEN_HEIGHT - TUTWINDOW_WIDTH ) / 2,

	"style" : ( "movable", "float", ),

	"width" : TUTWINDOW_WIDTH,
	"height" : TUTWINDOW_HEIGHT,

	"children" :
	(
		{
			"name" : "background",
			"type" : "image",
			"style" : ("attach",),

			"x" : 0,
			"y" : 0,

			"image" :  TUTWINDOW_PATH + "bg_1.tga",

			"children" :
			(
				## TITLE BAR
				{
					"name" : "title_bar",
					"type" : "titlebar",
					"style" : ("attach",),

					"x" : 8,
					"y" : 8,

					"width" : TUTWINDOW_WIDTH - 16,
					"color" : "red",

					"children" :
					(
						{
							"name" : "title_name",
							"type" : "text",
							"text" : uiScriptLocale.RUNE_WINDOW_TUTORIAL,
							"horizontal_align" : "center",
							"text_horizontal_align" : "center",
							"x" : 0,
							"y" : 3,
						},
					),
				},

				## LEFT BUTTON
				{
					"name" : "button_left",
					"type" : "button",

					"x" : 68,
					"y" : 58,

					"horizontal_align" : "left",
					"vertical_align" : "bottom",

					"default_image" : TUTWINDOW_PATH + "btn_left_normal.tga",
					"over_image" : TUTWINDOW_PATH + "btn_left_hover.tga",
					"down_image" : TUTWINDOW_PATH + "btn_left_down.tga",
				},

				## RIGHT BUTTON
				{
					"name" : "button_right",
					"type" : "button",

					# 88 = width of button

					"x" : 68 + 88,
					"y" : 58,

					"horizontal_align" : "right",
					"vertical_align" : "bottom",

					"default_image" : TUTWINDOW_PATH + "btn_right_normal.tga",
					"over_image" : TUTWINDOW_PATH + "btn_right_hover.tga",
					"down_image" : TUTWINDOW_PATH + "btn_right_down.tga",
				},

				## TEXT DESCRIPTION
				{
					"name" : "description",
					"type" : "multi_text",

					"x" : 40,
					"y" : 66,

					"text_horizontal_align" : "center",
					"text_vertical_align" : "center",

					"width" : 180,
					"text" : localeInfo.RUNE_TUTORIAL_DESC_1,
				},
			),
		},
	),
}