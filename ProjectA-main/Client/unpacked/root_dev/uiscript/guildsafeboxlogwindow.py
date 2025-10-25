import uiScriptLocale
import ui

BOARD_WIDTH = 450
BOARD_HEIGHT = 359

LEFT_SPACE = 3
RIGHT_SPACE = 3
TOP_SPACE = 3
BOTTOM_SPACE = 3

TEXT_BOX_WIDTH = BOARD_WIDTH - LEFT_SPACE - RIGHT_SPACE - ui.ScrollBar.SCROLLBAR_WIDTH - 5
TEXT_BOX_HEIGHT = BOARD_HEIGHT - TOP_SPACE - BOTTOM_SPACE

window = {
	"name" : "GuildSafeboxLogWindow",

	"x" : 100,
	"y" : 20,

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

			"title" : uiScriptLocale.GUILD_SAFE_LOG_TITLE,

			"children" :
			(
				{
					"name" : "text_field",
					"type" : "field",

					"x" : LEFT_SPACE,
					"y" : TOP_SPACE,

					"width" : TEXT_BOX_WIDTH,
					"height" : TEXT_BOX_HEIGHT,

					"children" :
					(
						{
							"name" : "text_box",
							"type" : "listboxex",

							"x" : 7,
							"y" : 3,

							"width" : TEXT_BOX_WIDTH - 7 * 2,
							"height" : TEXT_BOX_HEIGHT - 3 * 2,

							"itemsize_x" : TEXT_BOX_WIDTH - 7 * 2,
							"itemsize_y" : 18,

							"itemstep" : 18,

							"viewcount" : (TEXT_BOX_HEIGHT - 3 * 2) / 18,
						},
					),
				},
				{
					"name" : "scrollbar",
					"type" : "scrollbar",

					"x" : RIGHT_SPACE + ui.ScrollBar.SCROLLBAR_WIDTH,
					"y" : TOP_SPACE,

					"size" : TEXT_BOX_HEIGHT,

					"horizontal_align" : "right",
				},
			),
		},
	),
}
