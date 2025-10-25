import uiScriptLocale

BOARD_WIDTH = 270
BOARD_HEIGHT = 115

window = {
	"name" : "WebLoadingWindow",

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
		
			"padding" : 0,

			"width" : BOARD_WIDTH,
			"height" : BOARD_HEIGHT,

			"title" : uiScriptLocale.WEB_LOADING_TITLE,

			"children" :
			(
				{
					"name" : "desc",
					"type" : "text",

					"x" : 0,
					"y" : 60,

					"r" : 1.0,
					"g" : 1.0,
					"b" : 130.0 / 255.0,

					"horizontal_align" : "center",
					"text_horizontal_align" : "center",

					"text" : uiScriptLocale.WEB_LOADING_DESC,
				},
				{
					"name" : "img",
					"type" : "ani_image",

					"x" : (BOARD_WIDTH - 16) / 2,
					"y" : 80,

					"delay" : 6,

					"images" : (
						"d:/ymir work/ui/loading_ani/00.tga",
						"d:/ymir work/ui/loading_ani/01.tga",
						"d:/ymir work/ui/loading_ani/02.tga",
						"d:/ymir work/ui/loading_ani/03.tga",
						"d:/ymir work/ui/loading_ani/04.tga",
						"d:/ymir work/ui/loading_ani/05.tga",
						"d:/ymir work/ui/loading_ani/06.tga",
						"d:/ymir work/ui/loading_ani/07.tga",
					),
				},
			),
		},
	),
}
