import uiScriptLocale

WEB_WIDTH = 1020
WEB_HEIGHT = 720
if SCREEN_WIDTH < WEB_WIDTH:
	WEB_WIDTH = 780
	WEB_HEIGHT = 623

window = {
	"name" : "MallWindow",

	"x" : 0,
	"y" : 0,

	"style" : ("movable", "float",),

	"width"  : WEB_WIDTH  ,
	"height" : WEB_HEIGHT ,

	"children" :
	(
		{
			"name" : "board",
			"type" : "board_with_titlebar",
			"style" : ("attach",),

			"x" : 0,
			"y" : 0,

			"padding" : 0,

			"width"	 : WEB_WIDTH  ,
			"height" : WEB_HEIGHT ,

			"title" : uiScriptLocale.SYSTEM_MALL,

			"children" :
			(
				{
					"name" : "webrender",

					"x" : 10,
					"y" : 33,

					"width" : WEB_WIDTH - 10 - 23 + 13,
					"height" : WEB_HEIGHT - 33 - 13,
				},
			),
		},
	),
}
