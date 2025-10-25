import uiScriptLocale
import grp

TEXT_COLOR = grp.GenerateColor(255.0 / 255.0, 255.0 / 255.0, 130.0 / 255.0, 1.0)

BOARD_WIDTH = 300
BOARD_HEIGHT = 40

window = {
	"name" : "HorseUpgradeWindow",

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

			"title" : "",
		},
	),
}
