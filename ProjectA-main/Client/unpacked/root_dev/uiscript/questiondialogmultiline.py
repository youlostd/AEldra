import uiScriptLocale

window = {
	"name" : "QuestionDialogMultiLine",
	"style" : ("movable", "float",),

	"x" : SCREEN_WIDTH/2 - 125,
	"y" : SCREEN_HEIGHT/2 - 52,

	"width" : 340,
	"height" : 105,

	"children" :
	(
		{
			"name" : "board",
			"type" : "board",

			"x" : 0,
			"y" : 0,

			"padding" : 0,

			"width" : 340,
			"height" : 105,

			"children" :
			(
				{
					"name" : "message",
					"type" : "multi_text",

					"x" : 20,
					"y" : 30,

					"width" : 340 - 20 - 27,

					"text_horizontal_align" : "center",
				},
				{
					"name" : "accept",
					"type" : "button",

					"x" : -40,
					"y" : 63,

					"width" : 61,
					"height" : 21,

					"horizontal_align" : "center",
					"text" : uiScriptLocale.YES,

					"default_image" : "d:/ymir work/ui/public/middle_button_01.sub",
					"over_image" : "d:/ymir work/ui/public/middle_button_02.sub",
					"down_image" : "d:/ymir work/ui/public/middle_button_03.sub",
				},
				{
					"name" : "cancel",
					"type" : "button",

					"x" : 40,
					"y" : 63,

					"width" : 61,
					"height" : 21,

					"horizontal_align" : "center",
					"text" : uiScriptLocale.NO,

					"default_image" : "d:/ymir work/ui/public/middle_button_01.sub",
					"over_image" : "d:/ymir work/ui/public/middle_button_02.sub",
					"down_image" : "d:/ymir work/ui/public/middle_button_03.sub",
				},
			),
		},
	),
}