import uiScriptLocale

WINDOW_WIDTH = 611
WINDOW_HEIGHT = 509

window = {
	"name" : "XmasEvent",

	"x" : (SCREEN_WIDTH - WINDOW_WIDTH) / 2,
	"y" : (SCREEN_HEIGHT - WINDOW_HEIGHT) / 2,

	"style" : ("movable", "float",),

	"width" : WINDOW_WIDTH,
	"height" : WINDOW_HEIGHT,

	"children" :
	(
		{
			"name" : "background",
			"type" : "image",
			"style" : ("movable", "attach",),

			"x" : 0,
			"y" : 0,

			"image" : "d:/ymir work/ui/xmas/bg.tga",

			"children" :
			(
				{
					"name" : "TitleBar",
					"type" : "titlebar",
					"style" : ("attach",),

					"x" : 6,
					"y" : 5,

					"width" : WINDOW_WIDTH - 10,

					"children" :
					(
						{ "name" : "TitleName", "type" : "text", "x" : 0, "y" : -1, "text" : uiScriptLocale.XMAS_EVENT_TITLE, "all_align" : "center" },
					),
				},
			),
		},
	),
}
