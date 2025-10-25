import uiScriptLocale

SLOTS = 3 if __SERVER__ == 1 else 2
BOARD_WIDTH = 95/2*SLOTS
BOARD_HEIGHT = 42

window = {
	"name" : "FakeBuffSkillWindow",

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

			"title" : uiScriptLocale.FAKEBUFF_SKILL_TITLE,

			"children" :
			(
				{
					"name" : "slot",
					"type" : "slot",

					"x" : (BOARD_WIDTH - (41 * SLOTS)) / 3 + 4,
					"y" : 4,

					"width" : 41 * SLOTS,
					"height" : 38,

					"slot" : (
						{"index":94, "x":41*0, "y":0, "width":38, "height":38,},
						{"index":96, "x":41*1, "y":0, "width":38, "height":38,},
						{"index":111, "x":41*2, "y":0, "width":38, "height":38,},
					) if __SERVER__ == 1 else (
						{"index":94, "x":41*0, "y":0, "width":38, "height":38,},
						{"index":96, "x":41*1, "y":0, "width":38, "height":38,},
						# {"index":111, "x":41*2, "y":0, "width":38, "height":38,},
					),
				},
			),
		},
		{
			"name" : "InfoImage",
			"type" : "image",

			"x" : 20,
			"y" : 10,

			"scaled_load" : 0.6,

			"image" : "d:/ymir work/ui/game/eqchanger/info_normal.tga"

			# "width" : 41 * 3,
			# "height" : 38,
		},
	),
}
