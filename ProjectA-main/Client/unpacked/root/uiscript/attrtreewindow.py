import uiScriptLocale

LEVEL_X_POS = 24
LEVEL_Y_POS = 50 + (252 - 240) / 2 # figureStartY + (figureHeight - levelDisplayHeight) / 2

ROW_WIDTH = 163
ROW_SKIP_WIDTH = 164

BOARD_WIDTH = 983
BOARD_HEIGHT = 308

PATH = "d:/ymir work/ui/game/attrtree/"

window = {
	"name" : "AttrTreeWindow",

	"x" : (SCREEN_WIDTH - BOARD_WIDTH) / 2,
	"y" : (SCREEN_HEIGHT - BOARD_HEIGHT) / 2,

	"style" : ("movable", "float",),

	"width" : BOARD_WIDTH,
	"height" : BOARD_HEIGHT,

	"children" :
	(
		{
			"name" : "board",
			"type" : "board",
			"style" : ("attach",),

			"x" : 0,
			"y" : 0,

			"width" : BOARD_WIDTH,
			"height" : BOARD_HEIGHT,

			"children" :
			(
				{
					"name" : "bg",
					"type" : "image",
					"style" : ("not_pick",),

					"x" : 0,
					"y" : 0,

					"image" : PATH + "bg_all.tga",
				},
				{
					"name" : "close_btn",
					"type" : "button",

					"x" : 15,
					"y" : 0,

					"horizontal_align" : "right",

					"default_image" : "d:/ymir work/ui/public/close_button_01.sub",
					"over_image" : "d:/ymir work/ui/public/close_button_02.sub",
					"down_image" : "d:/ymir work/ui/public/close_button_03.sub",
				},
				{
					"name" : "row_1",
					"style" : ("not_pick",),

					"x" : ROW_SKIP_WIDTH * 0,
					"y" : 0,

					"width" : ROW_WIDTH,
					"height" : BOARD_HEIGHT,

					"children" :
					(
						{
							"name" : "title_1",
							"type" : "text",

							"x" : 13 + 136 / 2,
							"y" : 10 + 17 / 2,

							"text_horizontal_align" : "center",
							"text_vertical_align" : "center",

							"text" : uiScriptLocale.ATTRTREE_TITLE_1,
						},
						{
							"name" : "connect_1_5",
							"type" : "image",

							"x" : LEVEL_X_POS + 10,
							"y" : LEVEL_Y_POS + 0 * 51 + 17,

							"image" : PATH + "connect_0.tga",
						},
						{
							"name" : "ball_1_5",
							"type" : "button",

							"x" : LEVEL_X_POS,
							"y" : LEVEL_Y_POS + 0 * 51,

							"default_image" : PATH + "ball_0_1.tga",
							"over_image" : PATH + "ball_0_2.tga",
							"down_image" : PATH + "ball_0_3.tga",
							"disable_image" : PATH + "ball_0_1.tga",
						},
						{
							"name" : "connect_1_4",
							"type" : "image",

							"x" : LEVEL_X_POS + 10,
							"y" : LEVEL_Y_POS + 1 * 51 + 17,

							"image" : PATH + "connect_0.tga",
						},
						{
							"name" : "ball_1_4",
							"type" : "button",

							"x" : LEVEL_X_POS,
							"y" : LEVEL_Y_POS + 1 * 51,

							"default_image" : PATH + "ball_0_1.tga",
							"over_image" : PATH + "ball_0_2.tga",
							"down_image" : PATH + "ball_0_3.tga",
							"disable_image" : PATH + "ball_0_1.tga",
						},
						{
							"name" : "connect_1_3",
							"type" : "image",

							"x" : LEVEL_X_POS + 10,
							"y" : LEVEL_Y_POS + 2 * 51 + 17,

							"image" : PATH + "connect_0.tga",
						},
						{
							"name" : "ball_1_3",
							"type" : "button",

							"x" : LEVEL_X_POS,
							"y" : LEVEL_Y_POS + 2 * 51,

							"default_image" : PATH + "ball_0_1.tga",
							"over_image" : PATH + "ball_0_2.tga",
							"down_image" : PATH + "ball_0_3.tga",
							"disable_image" : PATH + "ball_0_1.tga",
						},
						{
							"name" : "connect_1_2",
							"type" : "image",

							"x" : LEVEL_X_POS + 10,
							"y" : LEVEL_Y_POS + 3 * 51 + 17,

							"image" : PATH + "connect_0.tga",
						},
						{
							"name" : "ball_1_2",
							"type" : "button",

							"x" : LEVEL_X_POS,
							"y" : LEVEL_Y_POS + 3 * 51,

							"default_image" : PATH + "ball_0_1.tga",
							"over_image" : PATH + "ball_0_2.tga",
							"down_image" : PATH + "ball_0_3.tga",
							"disable_image" : PATH + "ball_0_1.tga",
						},
						{
							"name" : "ball_1_1",
							"type" : "button",

							"x" : LEVEL_X_POS,
							"y" : LEVEL_Y_POS + 4 * 51,

							"default_image" : PATH + "ball_0_1.tga",
							"over_image" : PATH + "ball_0_2.tga",
							"down_image" : PATH + "ball_0_3.tga",
							"disable_image" : PATH + "ball_0_1.tga",
						},
					),
				},
				{
					"name" : "row_2",
					"style" : ("not_pick",),

					"x" : ROW_SKIP_WIDTH * 1,
					"y" : 0,

					"width" : ROW_WIDTH,
					"height" : BOARD_HEIGHT,

					"children" :
					(
						{
							"name" : "title_2",
							"type" : "text",

							"x" : 13 + 136 / 2,
							"y" : 10 + 17 / 2,

							"text_horizontal_align" : "center",
							"text_vertical_align" : "center",

							"text" : uiScriptLocale.ATTRTREE_TITLE_2,
						},
						{
							"name" : "connect_2_5",
							"type" : "image",

							"x" : LEVEL_X_POS + 10,
							"y" : LEVEL_Y_POS + 0 * 51 + 17,

							"image" : PATH + "connect_0.tga",
						},
						{
							"name" : "ball_2_5",
							"type" : "button",

							"x" : LEVEL_X_POS,
							"y" : LEVEL_Y_POS + 0 * 51,

							"default_image" : PATH + "ball_0_1.tga",
							"over_image" : PATH + "ball_0_2.tga",
							"down_image" : PATH + "ball_0_3.tga",
							"disable_image" : PATH + "ball_0_1.tga",
						},
						{
							"name" : "connect_2_4",
							"type" : "image",

							"x" : LEVEL_X_POS + 10,
							"y" : LEVEL_Y_POS + 1 * 51 + 17,

							"image" : PATH + "connect_0.tga",
						},
						{
							"name" : "ball_2_4",
							"type" : "button",

							"x" : LEVEL_X_POS,
							"y" : LEVEL_Y_POS + 1 * 51,

							"default_image" : PATH + "ball_0_1.tga",
							"over_image" : PATH + "ball_0_2.tga",
							"down_image" : PATH + "ball_0_3.tga",
							"disable_image" : PATH + "ball_0_1.tga",
						},
						{
							"name" : "connect_2_3",
							"type" : "image",

							"x" : LEVEL_X_POS + 10,
							"y" : LEVEL_Y_POS + 2 * 51 + 17,

							"image" : PATH + "connect_0.tga",
						},
						{
							"name" : "ball_2_3",
							"type" : "button",

							"x" : LEVEL_X_POS,
							"y" : LEVEL_Y_POS + 2 * 51,

							"default_image" : PATH + "ball_0_1.tga",
							"over_image" : PATH + "ball_0_2.tga",
							"down_image" : PATH + "ball_0_3.tga",
							"disable_image" : PATH + "ball_0_1.tga",
						},
						{
							"name" : "connect_2_2",
							"type" : "image",

							"x" : LEVEL_X_POS + 10,
							"y" : LEVEL_Y_POS + 3 * 51 + 17,

							"image" : PATH + "connect_0.tga",
						},
						{
							"name" : "ball_2_2",
							"type" : "button",

							"x" : LEVEL_X_POS,
							"y" : LEVEL_Y_POS + 3 * 51,

							"default_image" : PATH + "ball_0_1.tga",
							"over_image" : PATH + "ball_0_2.tga",
							"down_image" : PATH + "ball_0_3.tga",
							"disable_image" : PATH + "ball_0_1.tga",
						},
						{
							"name" : "ball_2_1",
							"type" : "button",

							"x" : LEVEL_X_POS,
							"y" : LEVEL_Y_POS + 4 * 51,

							"default_image" : PATH + "ball_0_1.tga",
							"over_image" : PATH + "ball_0_2.tga",
							"down_image" : PATH + "ball_0_3.tga",
							"disable_image" : PATH + "ball_0_1.tga",
						},
					),
				},
				{
					"name" : "row_3",
					"style" : ("not_pick",),

					"x" : ROW_SKIP_WIDTH * 2,
					"y" : 0,

					"width" : ROW_WIDTH,
					"height" : BOARD_HEIGHT,

					"children" :
					(
						{
							"name" : "title_3",
							"type" : "text",

							"x" : 13 + 136 / 2,
							"y" : 10 + 17 / 2,

							"text_horizontal_align" : "center",
							"text_vertical_align" : "center",

							"text" : uiScriptLocale.ATTRTREE_TITLE_3,
						},
						{
							"name" : "connect_3_5",
							"type" : "image",

							"x" : LEVEL_X_POS + 10,
							"y" : LEVEL_Y_POS + 0 * 51 + 17,

							"image" : PATH + "connect_0.tga",
						},
						{
							"name" : "ball_3_5",
							"type" : "button",

							"x" : LEVEL_X_POS,
							"y" : LEVEL_Y_POS + 0 * 51,

							"default_image" : PATH + "ball_0_1.tga",
							"over_image" : PATH + "ball_0_2.tga",
							"down_image" : PATH + "ball_0_3.tga",
							"disable_image" : PATH + "ball_0_1.tga",
						},
						{
							"name" : "connect_3_4",
							"type" : "image",

							"x" : LEVEL_X_POS + 10,
							"y" : LEVEL_Y_POS + 1 * 51 + 17,

							"image" : PATH + "connect_0.tga",
						},
						{
							"name" : "ball_3_4",
							"type" : "button",

							"x" : LEVEL_X_POS,
							"y" : LEVEL_Y_POS + 1 * 51,

							"default_image" : PATH + "ball_0_1.tga",
							"over_image" : PATH + "ball_0_2.tga",
							"down_image" : PATH + "ball_0_3.tga",
							"disable_image" : PATH + "ball_0_1.tga",
						},
						{
							"name" : "connect_3_3",
							"type" : "image",

							"x" : LEVEL_X_POS + 10,
							"y" : LEVEL_Y_POS + 2 * 51 + 17,

							"image" : PATH + "connect_0.tga",
						},
						{
							"name" : "ball_3_3",
							"type" : "button",

							"x" : LEVEL_X_POS,
							"y" : LEVEL_Y_POS + 2 * 51,

							"default_image" : PATH + "ball_0_1.tga",
							"over_image" : PATH + "ball_0_2.tga",
							"down_image" : PATH + "ball_0_3.tga",
							"disable_image" : PATH + "ball_0_1.tga",
						},
						{
							"name" : "connect_3_2",
							"type" : "image",

							"x" : LEVEL_X_POS + 10,
							"y" : LEVEL_Y_POS + 3 * 51 + 17,

							"image" : PATH + "connect_0.tga",
						},
						{
							"name" : "ball_3_2",
							"type" : "button",

							"x" : LEVEL_X_POS,
							"y" : LEVEL_Y_POS + 3 * 51,

							"default_image" : PATH + "ball_0_1.tga",
							"over_image" : PATH + "ball_0_2.tga",
							"down_image" : PATH + "ball_0_3.tga",
							"disable_image" : PATH + "ball_0_1.tga",
						},
						{
							"name" : "ball_3_1",
							"type" : "button",

							"x" : LEVEL_X_POS,
							"y" : LEVEL_Y_POS + 4 * 51,

							"default_image" : PATH + "ball_0_1.tga",
							"over_image" : PATH + "ball_0_2.tga",
							"down_image" : PATH + "ball_0_3.tga",
							"disable_image" : PATH + "ball_0_1.tga",
						},
					),
				},
				{
					"name" : "row_4",
					"style" : ("not_pick",),

					"x" : ROW_SKIP_WIDTH * 3,
					"y" : 0,

					"width" : ROW_WIDTH,
					"height" : BOARD_HEIGHT,

					"children" :
					(
						{
							"name" : "title_4",
							"type" : "text",

							"x" : 13 + 136 / 2,
							"y" : 10 + 17 / 2,

							"text_horizontal_align" : "center",
							"text_vertical_align" : "center",

							"text" : uiScriptLocale.ATTRTREE_TITLE_4,
						},
						{
							"name" : "connect_4_5",
							"type" : "image",

							"x" : LEVEL_X_POS + 10,
							"y" : LEVEL_Y_POS + 0 * 51 + 17,

							"image" : PATH + "connect_0.tga",
						},
						{
							"name" : "ball_4_5",
							"type" : "button",

							"x" : LEVEL_X_POS,
							"y" : LEVEL_Y_POS + 0 * 51,

							"default_image" : PATH + "ball_0_1.tga",
							"over_image" : PATH + "ball_0_2.tga",
							"down_image" : PATH + "ball_0_3.tga",
							"disable_image" : PATH + "ball_0_1.tga",
						},
						{
							"name" : "connect_4_4",
							"type" : "image",

							"x" : LEVEL_X_POS + 10,
							"y" : LEVEL_Y_POS + 1 * 51 + 17,

							"image" : PATH + "connect_0.tga",
						},
						{
							"name" : "ball_4_4",
							"type" : "button",

							"x" : LEVEL_X_POS,
							"y" : LEVEL_Y_POS + 1 * 51,

							"default_image" : PATH + "ball_0_1.tga",
							"over_image" : PATH + "ball_0_2.tga",
							"down_image" : PATH + "ball_0_3.tga",
							"disable_image" : PATH + "ball_0_1.tga",
						},
						{
							"name" : "connect_4_3",
							"type" : "image",

							"x" : LEVEL_X_POS + 10,
							"y" : LEVEL_Y_POS + 2 * 51 + 17,

							"image" : PATH + "connect_0.tga",
						},
						{
							"name" : "ball_4_3",
							"type" : "button",

							"x" : LEVEL_X_POS,
							"y" : LEVEL_Y_POS + 2 * 51,

							"default_image" : PATH + "ball_0_1.tga",
							"over_image" : PATH + "ball_0_2.tga",
							"down_image" : PATH + "ball_0_3.tga",
							"disable_image" : PATH + "ball_0_1.tga",
						},
						{
							"name" : "connect_4_2",
							"type" : "image",

							"x" : LEVEL_X_POS + 10,
							"y" : LEVEL_Y_POS + 3 * 51 + 17,

							"image" : PATH + "connect_0.tga",
						},
						{
							"name" : "ball_4_2",
							"type" : "button",

							"x" : LEVEL_X_POS,
							"y" : LEVEL_Y_POS + 3 * 51,

							"default_image" : PATH + "ball_0_1.tga",
							"over_image" : PATH + "ball_0_2.tga",
							"down_image" : PATH + "ball_0_3.tga",
							"disable_image" : PATH + "ball_0_1.tga",
						},
						{
							"name" : "ball_4_1",
							"type" : "button",

							"x" : LEVEL_X_POS,
							"y" : LEVEL_Y_POS + 4 * 51,

							"default_image" : PATH + "ball_0_1.tga",
							"over_image" : PATH + "ball_0_2.tga",
							"down_image" : PATH + "ball_0_3.tga",
							"disable_image" : PATH + "ball_0_1.tga",
						},
					),
				},
				{
					"name" : "row_5",
					"style" : ("not_pick",),

					"x" : ROW_SKIP_WIDTH * 4,
					"y" : 0,

					"width" : ROW_WIDTH,
					"height" : BOARD_HEIGHT,

					"children" :
					(
						{
							"name" : "title_5",
							"type" : "text",

							"x" : 13 + 136 / 2,
							"y" : 10 + 17 / 2,

							"text_horizontal_align" : "center",
							"text_vertical_align" : "center",

							"text" : uiScriptLocale.ATTRTREE_TITLE_5,
						},
						{
							"name" : "connect_5_5",
							"type" : "image",

							"x" : LEVEL_X_POS + 10,
							"y" : LEVEL_Y_POS + 0 * 51 + 17,

							"image" : PATH + "connect_0.tga",
						},
						{
							"name" : "ball_5_5",
							"type" : "button",

							"x" : LEVEL_X_POS,
							"y" : LEVEL_Y_POS + 0 * 51,

							"default_image" : PATH + "ball_0_1.tga",
							"over_image" : PATH + "ball_0_2.tga",
							"down_image" : PATH + "ball_0_3.tga",
							"disable_image" : PATH + "ball_0_1.tga",
						},
						{
							"name" : "connect_5_4",
							"type" : "image",

							"x" : LEVEL_X_POS + 10,
							"y" : LEVEL_Y_POS + 1 * 51 + 17,

							"image" : PATH + "connect_0.tga",
						},
						{
							"name" : "ball_5_4",
							"type" : "button",

							"x" : LEVEL_X_POS,
							"y" : LEVEL_Y_POS + 1 * 51,

							"default_image" : PATH + "ball_0_1.tga",
							"over_image" : PATH + "ball_0_2.tga",
							"down_image" : PATH + "ball_0_3.tga",
							"disable_image" : PATH + "ball_0_1.tga",
						},
						{
							"name" : "connect_5_3",
							"type" : "image",

							"x" : LEVEL_X_POS + 10,
							"y" : LEVEL_Y_POS + 2 * 51 + 17,

							"image" : PATH + "connect_0.tga",
						},
						{
							"name" : "ball_5_3",
							"type" : "button",

							"x" : LEVEL_X_POS,
							"y" : LEVEL_Y_POS + 2 * 51,

							"default_image" : PATH + "ball_0_1.tga",
							"over_image" : PATH + "ball_0_2.tga",
							"down_image" : PATH + "ball_0_3.tga",
							"disable_image" : PATH + "ball_0_1.tga",
						},
						{
							"name" : "connect_5_2",
							"type" : "image",

							"x" : LEVEL_X_POS + 10,
							"y" : LEVEL_Y_POS + 3 * 51 + 17,

							"image" : PATH + "connect_0.tga",
						},
						{
							"name" : "ball_5_2",
							"type" : "button",

							"x" : LEVEL_X_POS,
							"y" : LEVEL_Y_POS + 3 * 51,

							"default_image" : PATH + "ball_0_1.tga",
							"over_image" : PATH + "ball_0_2.tga",
							"down_image" : PATH + "ball_0_3.tga",
							"disable_image" : PATH + "ball_0_1.tga",
						},
						{
							"name" : "ball_5_1",
							"type" : "button",

							"x" : LEVEL_X_POS,
							"y" : LEVEL_Y_POS + 4 * 51,

							"default_image" : PATH + "ball_0_1.tga",
							"over_image" : PATH + "ball_0_2.tga",
							"down_image" : PATH + "ball_0_3.tga",
							"disable_image" : PATH + "ball_0_1.tga",
						},
					),
				},
				{
					"name" : "row_6",
					"style" : ("not_pick",),

					"x" : ROW_SKIP_WIDTH * 5,
					"y" : 0,

					"width" : ROW_WIDTH,
					"height" : BOARD_HEIGHT,

					"children" :
					(
						{
							"name" : "title_6",
							"type" : "text",

							"x" : 13 + 136 / 2,
							"y" : 10 + 17 / 2,

							"text_horizontal_align" : "center",
							"text_vertical_align" : "center",

							"text" : uiScriptLocale.ATTRTREE_TITLE_6,
						},
						{
							"name" : "connect_6_5",
							"type" : "image",

							"x" : LEVEL_X_POS + 10,
							"y" : LEVEL_Y_POS + 0 * 51 + 17,

							"image" : PATH + "connect_0.tga",
						},
						{
							"name" : "ball_6_5",
							"type" : "button",

							"x" : LEVEL_X_POS,
							"y" : LEVEL_Y_POS + 0 * 51,

							"default_image" : PATH + "ball_0_1.tga",
							"over_image" : PATH + "ball_0_2.tga",
							"down_image" : PATH + "ball_0_3.tga",
							"disable_image" : PATH + "ball_0_1.tga",
						},
						{
							"name" : "connect_6_4",
							"type" : "image",

							"x" : LEVEL_X_POS + 10,
							"y" : LEVEL_Y_POS + 1 * 51 + 17,

							"image" : PATH + "connect_0.tga",
						},
						{
							"name" : "ball_6_4",
							"type" : "button",

							"x" : LEVEL_X_POS,
							"y" : LEVEL_Y_POS + 1 * 51,

							"default_image" : PATH + "ball_0_1.tga",
							"over_image" : PATH + "ball_0_2.tga",
							"down_image" : PATH + "ball_0_3.tga",
							"disable_image" : PATH + "ball_0_1.tga",
						},
						{
							"name" : "connect_6_3",
							"type" : "image",

							"x" : LEVEL_X_POS + 10,
							"y" : LEVEL_Y_POS + 2 * 51 + 17,

							"image" : PATH + "connect_0.tga",
						},
						{
							"name" : "ball_6_3",
							"type" : "button",

							"x" : LEVEL_X_POS,
							"y" : LEVEL_Y_POS + 2 * 51,

							"default_image" : PATH + "ball_0_1.tga",
							"over_image" : PATH + "ball_0_2.tga",
							"down_image" : PATH + "ball_0_3.tga",
							"disable_image" : PATH + "ball_0_1.tga",
						},
						{
							"name" : "connect_6_2",
							"type" : "image",

							"x" : LEVEL_X_POS + 10,
							"y" : LEVEL_Y_POS + 3 * 51 + 17,

							"image" : PATH + "connect_0.tga",
						},
						{
							"name" : "ball_6_2",
							"type" : "button",

							"x" : LEVEL_X_POS,
							"y" : LEVEL_Y_POS + 3 * 51,

							"default_image" : PATH + "ball_0_1.tga",
							"over_image" : PATH + "ball_0_2.tga",
							"down_image" : PATH + "ball_0_3.tga",
							"disable_image" : PATH + "ball_0_1.tga",
						},
						{
							"name" : "ball_6_1",
							"type" : "button",

							"x" : LEVEL_X_POS,
							"y" : LEVEL_Y_POS + 4 * 51,

							"default_image" : PATH + "ball_0_1.tga",
							"over_image" : PATH + "ball_0_2.tga",
							"down_image" : PATH + "ball_0_3.tga",
							"disable_image" : PATH + "ball_0_1.tga",
						},
					),
				},
			),
		},
	),
}
