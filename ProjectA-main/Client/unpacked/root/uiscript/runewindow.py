import uiScriptLocale
import rune
import grp

BASE_PATH = "d:/ymir work/ui/game/runes/"
MAIN_TITLE_COLOR = grp.GenerateColor(114.0 / 255.0, 114.0 / 255.0, 113.0 / 255.0, 1.0)
MAIN_TEXT_COLOR_DEFAULT = grp.GenerateColor(221.0 / 255.0, 221.0 / 255.0, 221.0 / 255.0, 0.2)
MAIN_TEXT_COLOR_OVER = grp.GenerateColor(221.0 / 255.0, 221.0 / 255.0, 221.0 / 255.0, 1.0)

MAIN_GROUP_SPACE = 0
MAIN_GROUP_WIDTH = 180
MAIN_GROUP_HEIGHT = 370

#894
#376

BOARD_WIDTH = 930 #MAIN_GROUP_WIDTH * rune.GROUP_MAX_NUM + MAIN_GROUP_SPACE * (rune.GROUP_MAX_NUM - 1) + 17 + 23
BOARD_HEIGHT = 441 #MAIN_GROUP_HEIGHT + 56 + 15

####### UI HELPER
Main_RuneGroupCounter = 0
def Main_GetRuneGroup(inc = False):
	global Main_RuneGroupCounter

	if inc:
		Main_RuneGroupCounter += 1
	return Main_RuneGroupCounter
#######

window = {
	"name" : "SphaeraWindow",

	"x" : (SCREEN_WIDTH - BOARD_WIDTH) / 2,
	"y" : (SCREEN_HEIGHT - BOARD_HEIGHT) / 2,

	"style" : ("movable", "float",),

	"width" : BOARD_WIDTH,
	"height" : BOARD_HEIGHT,

	"children" :
	(
		{
			"name" : "background_image",
			"type" : "image",
			"style" : ("attach",),

			"x" : 0,
			"y" : 0,

			"image" :  BASE_PATH + "bg.tga",

			"children" :
			(
				{
					"name" : "title_bar",
					"type" : "titlebar",
					"style" : ("attach",),

					"x" : 8,
					"y" : 8,

					"width" : BOARD_WIDTH - 16,
					"color" : "red",

					"children" :
					(
						{
							"name" : "title_name",
							"type" : "text",
							"text" : uiScriptLocale.RUNE_MAIN_TITLE,
							"horizontal_align" : "center",
							"text_horizontal_align" : "center",
							"x" : 0,
							"y" : 3,
						},
					),
				},

				{
					"name" : "main_%d" % Main_GetRuneGroup(True),

					"x" : 17 + (MAIN_GROUP_WIDTH + MAIN_GROUP_SPACE) * (Main_GetRuneGroup() - 1),
					"y" : 35,

					"width" : MAIN_GROUP_WIDTH,
					"height" : MAIN_GROUP_HEIGHT,

					"children" :
					(
						## background lines
						{
							"name" : "main_%d_lines" % Main_GetRuneGroup(),
							"type" : "image",
							"style" : ("not_pick",),

							"x" : 31,
							"y" : 120,

							"image" : BASE_PATH + "main_lines.tga",
						},

						## text background
						{
							"name" : "main_%d_textbg" % Main_GetRuneGroup(),
							"type" : "image",
							"style" : ("not_pick",),

							"x" : 21,
							"y" : 164,

							"image" : BASE_PATH + "text_box.tga",
						},

						## top circle
						{
							"name" : "main_%d_circle" % Main_GetRuneGroup(),
							"type" : "image",
							"style" : ("not_pick",),

							"x" : 0,
							"y" : 18,

							"horizontal_align" : "center",

							"image" : BASE_PATH + "main_circles/main_circle_%d.tga" % Main_GetRuneGroup( ),

							"children" :
							(
								## inner image
								{
									"name" : "main_%d_circle_inner" % Main_GetRuneGroup(),
									"type" : "image",
									"style" : ("not_pick",),

									"x" : -33,
									"y" : -43,

									"image" : BASE_PATH + "rune%d/main_circle_inner.tga" % Main_GetRuneGroup(),
								},
								## glow for the circle while hovering
								{
									"name" : "main_%d_circle_glow" % Main_GetRuneGroup(),
									"type" : "image",
									"style" : ("not_pick",),

									"x" : -32,
									"y" : -40,

									"image" : BASE_PATH + "rune%d/main_circle_glow.tga" % Main_GetRuneGroup(),
								},
							),
						},

						## group title name
						{
							"name" : "main_%d_title" % Main_GetRuneGroup(),
							"type" : "text",
							"style" : ("not_pick",),

							"x" : 0,
							"y" : 178,

							"horizontal_align" : "center",
							"text_horizontal_align" : "center",

							"fontname": "Tahoma:16",
							"letter_spacing" : 2,
							"text" : uiScriptLocale.GetLocals()["RUNE_MAIN_GROUP_TITLE%d" % Main_GetRuneGroup()],
						},

						## group desc
						{
							"name" : "main_%d_description" % Main_GetRuneGroup(),
							"type" : "multi_text",
							"style" : ("not_pick",),

							"x" : 0,
							"y" : 30,

							"width" : MAIN_GROUP_WIDTH - 15 * 2,

							"horizontal_align" : "center",
							"text_horizontal_align" : "center",
							"vertical_align" : "bottom",

							"register_color" : (
								(False, MAIN_TEXT_COLOR_DEFAULT, True), # not over, default
								(True, MAIN_TEXT_COLOR_OVER), # over
							),
							"text" : uiScriptLocale.GetLocals()["RUNE_MAIN_GROUP_DESC%d" % Main_GetRuneGroup()],
						},

						## main runes
						{
							"name" : "main_%d_runes" % Main_GetRuneGroup(),
							"style" : ("not_pick",),

							"x" : 0,
							"y" : 32 + 200, #+ 105,

							"width" : int(62 * 2.6),
							"height" : 62 * 2 + 15,

							"horizontal_align" : "center",

							"children" :
							(
								{
									"name" : "main_%d_rune1" % Main_GetRuneGroup(),
									"type" : "image",
									"style" : ("not_pick",),

									"x" : -3,
									"y" : -10,

									"image" : BASE_PATH + "rune%d/main_rune1.tga" % Main_GetRuneGroup(),
								},
								{
									"name" : "main_%d_rune2" % Main_GetRuneGroup(),
									"type" : "image",
									"style" : ("not_pick",),

									"x" : 67,
									"y" : -10,

									"horizontal_align" : "right",

									"image" : BASE_PATH + "rune%d/main_rune2.tga" % Main_GetRuneGroup(),
								},
								{
									"name" : "main_%d_rune3" % Main_GetRuneGroup(),
									"type" : "image",
									"style" : ("not_pick",),

									"x" : 0,
									"y" : 54,

									"horizontal_align" : "center",

									"image" : BASE_PATH + "rune%d/main_rune3.tga" % Main_GetRuneGroup(),
								},
							),
						},

						# main glow
						{
							"name" : "main_%d_glow" % Main_GetRuneGroup(),
							"type" : "image",
						
							"x" : 0,
							"y" : 0,
						
							"image" : BASE_PATH + "main_glow.tga", # % Main_GetRuneGroup(),
						},
					),
				},
				{
					"name" : "main_%d" % Main_GetRuneGroup(True),

					"x" : 19 + (MAIN_GROUP_WIDTH + MAIN_GROUP_SPACE) * (Main_GetRuneGroup() - 1),
					"y" : 35,

					"width" : MAIN_GROUP_WIDTH,
					"height" : MAIN_GROUP_HEIGHT,

					"children" :
					(
						## background lines
						{
							"name" : "main_%d_lines" % Main_GetRuneGroup(),
							"type" : "image",
							"style" : ("not_pick",),

							"x" : 31,
							"y" : 120,

							"image" : BASE_PATH + "main_lines.tga",
						},

						## text background
						{
							"name" : "main_%d_textbg" % Main_GetRuneGroup(),
							"type" : "image",
							"style" : ("not_pick",),

							"x" : 21,
							"y" : 164,

							"image" : BASE_PATH + "text_box.tga",
						},

						## top circle
						{
							"name" : "main_%d_circle" % Main_GetRuneGroup(),
							"type" : "image",
							"style" : ("not_pick",),

							"x" : 0,
							"y" : 18,

							"horizontal_align" : "center",

							"image" : BASE_PATH + "main_circles/main_circle_%d.tga" % Main_GetRuneGroup( ),

							"children" :
							(
								## inner image
								{
									"name" : "main_%d_circle_inner" % Main_GetRuneGroup(),
									"type" : "image",
									"style" : ("not_pick",),

									"x" : -33,
									"y" : -43,

									"image" : BASE_PATH + "rune%d/main_circle_inner.tga" % Main_GetRuneGroup(),
								},
								## glow for the circle while hovering
								{
									"name" : "main_%d_circle_glow" % Main_GetRuneGroup(),
									"type" : "image",
									"style" : ("not_pick",),

									"x" : -32,
									"y" : -40,

									"image" : BASE_PATH + "rune%d/main_circle_glow.tga" % Main_GetRuneGroup(),
								},
							),
						},

						## group title name
						{
							"name" : "main_%d_title" % Main_GetRuneGroup(),
							"type" : "text",
							"style" : ("not_pick",),

							"x" : 0,
							"y" : 178,

							"horizontal_align" : "center",
							"text_horizontal_align" : "center",

							"fontname": "Tahoma:16",
							"letter_spacing" : 2,
							"text" : uiScriptLocale.GetLocals()["RUNE_MAIN_GROUP_TITLE%d" % Main_GetRuneGroup()],
						},

						## group desc
						{
							"name" : "main_%d_description" % Main_GetRuneGroup(),
							"type" : "multi_text",
							"style" : ("not_pick",),

							"x" : 0,
							"y" : 30,

							"width" : MAIN_GROUP_WIDTH - 15 * 2,

							"horizontal_align" : "center",
							"text_horizontal_align" : "center",
							"vertical_align" : "bottom",

							"register_color" : (
								(False, MAIN_TEXT_COLOR_DEFAULT, True), # not over, default
								(True, MAIN_TEXT_COLOR_OVER), # over
							),
							"text" : uiScriptLocale.GetLocals()["RUNE_MAIN_GROUP_DESC%d" % Main_GetRuneGroup()],
						},

						## main runes
						{
							"name" : "main_%d_runes" % Main_GetRuneGroup(),
							"style" : ("not_pick",),

							"x" : 0,
							"y" : 32 + 200,# + 105,

							"width" : int(62 * 2.6),
							"height" : 62 * 2 + 15,

							"horizontal_align" : "center",

							"children" :
							(
								{
									"name" : "main_%d_rune1" % Main_GetRuneGroup(),
									"type" : "image",
									"style" : ("not_pick",),

									"x" : -3,
									"y" : -10,

									"image" : BASE_PATH + "rune%d/main_rune1.tga" % Main_GetRuneGroup(),
								},
								{
									"name" : "main_%d_rune2" % Main_GetRuneGroup(),
									"type" : "image",
									"style" : ("not_pick",),

									"x" : 67,
									"y" : -10,

									"horizontal_align" : "right",

									"image" : BASE_PATH + "rune%d/main_rune2.tga" % Main_GetRuneGroup(),
								},
								{
									"name" : "main_%d_rune3" % Main_GetRuneGroup(),
									"type" : "image",
									"style" : ("not_pick",),

									"x" : 0,
									"y" : 54,

									"horizontal_align" : "center",

									"image" : BASE_PATH + "rune%d/main_rune3.tga" % Main_GetRuneGroup(),
								},
							),
						},

						# main glow
						{
							"name" : "main_%d_glow" % Main_GetRuneGroup(),
							"type" : "image",

							"x" : 0,
							"y" : 0,

							"image" : BASE_PATH + "main_glow.tga", # % Main_GetRuneGroup(),
						},
					),
				},
				{
					"name" : "main_%d" % Main_GetRuneGroup(True),

					"x" : 19 + (MAIN_GROUP_WIDTH + MAIN_GROUP_SPACE) * (Main_GetRuneGroup() - 1),
					"y" : 35,

					"width" : MAIN_GROUP_WIDTH,
					"height" : MAIN_GROUP_HEIGHT,

					"children" :
					(
						## background lines
						{
							"name" : "main_%d_lines" % Main_GetRuneGroup(),
							"type" : "image",
							"style" : ("not_pick",),

							"x" : 31,
							"y" : 120,

							"image" : BASE_PATH + "main_lines.tga",
						},

						## text background
						{
							"name" : "main_%d_textbg" % Main_GetRuneGroup(),
							"type" : "image",
							"style" : ("not_pick",),

							"x" : 21,
							"y" : 164,

							"image" : BASE_PATH + "text_box.tga",
						},

						## top circle
						{
							"name" : "main_%d_circle" % Main_GetRuneGroup(),
							"type" : "image",
							"style" : ("not_pick",),

							"x" : 0,
							"y" : 18,

							"horizontal_align" : "center",

							"image" : BASE_PATH + "main_circles/main_circle_%d.tga" % Main_GetRuneGroup( ),

							"children" :
							(
								## inner image
								{
									"name" : "main_%d_circle_inner" % Main_GetRuneGroup(),
									"type" : "image",
									"style" : ("not_pick",),

									"x" : -33,
									"y" : -43,

									"image" : BASE_PATH + "rune%d/main_circle_inner.tga" % Main_GetRuneGroup(),
								},
								## glow for the circle while hovering
								{
									"name" : "main_%d_circle_glow" % Main_GetRuneGroup(),
									"type" : "image",
									"style" : ("not_pick",),

									"x" : -32,
									"y" : -40,

									"image" : BASE_PATH + "rune%d/main_circle_glow.tga" % Main_GetRuneGroup(),
								},
							),
						},

						## group title name
						{
							"name" : "main_%d_title" % Main_GetRuneGroup(),
							"type" : "text",
							"style" : ("not_pick",),

							"x" : 0,
							"y" : 178,

							"horizontal_align" : "center",
							"text_horizontal_align" : "center",

							"fontname": "Tahoma:16",
							"letter_spacing" : 2,
							"text" : uiScriptLocale.GetLocals()["RUNE_MAIN_GROUP_TITLE%d" % Main_GetRuneGroup()],
						},

						## group desc
						{
							"name" : "main_%d_description" % Main_GetRuneGroup(),
							"type" : "multi_text",
							"style" : ("not_pick",),

							"x" : 0,
							"y" : 30,

							"width" : MAIN_GROUP_WIDTH - 15 * 2,

							"horizontal_align" : "center",
							"text_horizontal_align" : "center",
							"vertical_align" : "bottom",

							"register_color" : (
								(False, MAIN_TEXT_COLOR_DEFAULT, True), # not over, default
								(True, MAIN_TEXT_COLOR_OVER), # over
							),
							"text" : uiScriptLocale.GetLocals()["RUNE_MAIN_GROUP_DESC%d" % Main_GetRuneGroup()],
						},

						## main runes
						{
							"name" : "main_%d_runes" % Main_GetRuneGroup(),
							"style" : ("not_pick",),

							"x" : 0,
							"y" : 32 + 200, #+ 105,

							"width" : int(62 * 2.6),
							"height" : 62 * 2 + 15,

							"horizontal_align" : "center",

							"children" :
							(
								{
									"name" : "main_%d_rune1" % Main_GetRuneGroup(),
									"type" : "image",
									"style" : ("not_pick",),

									"x" : -3,
									"y" : -10,

									"image" : BASE_PATH + "rune%d/main_rune1.tga" % Main_GetRuneGroup(),
								},
								{
									"name" : "main_%d_rune2" % Main_GetRuneGroup(),
									"type" : "image",
									"style" : ("not_pick",),

									"x" : 67,
									"y" : -10,

									"horizontal_align" : "right",

									"image" : BASE_PATH + "rune%d/main_rune2.tga" % Main_GetRuneGroup(),
								},
								{
									"name" : "main_%d_rune3" % Main_GetRuneGroup(),
									"type" : "image",
									"style" : ("not_pick",),

									"x" : 0,
									"y" : 54,

									"horizontal_align" : "center",

									"image" : BASE_PATH + "rune%d/main_rune3.tga" % Main_GetRuneGroup(),
								},
							),
						},

						# main glow
						{
							"name" : "main_%d_glow" % Main_GetRuneGroup(),
							"type" : "image",

							"x" : 0,
							"y" : 0,

							"image" : BASE_PATH + "main_glow.tga", # % Main_GetRuneGroup(),
						},
					),
				},
				{
					"name" : "main_%d" % Main_GetRuneGroup(True),

					"x" : 19 + (MAIN_GROUP_WIDTH + MAIN_GROUP_SPACE) * (Main_GetRuneGroup() - 1),
					"y" : 35,

					"width" : MAIN_GROUP_WIDTH,
					"height" : MAIN_GROUP_HEIGHT,

					"children" :
					(
						## background lines
						{
							"name" : "main_%d_lines" % Main_GetRuneGroup(),
							"type" : "image",
							"style" : ("not_pick",),

							"x" : 31,
							"y" : 120,

							"image" : BASE_PATH + "main_lines.tga",
						},

						## text background
						{
							"name" : "main_%d_textbg" % Main_GetRuneGroup(),
							"type" : "image",
							"style" : ("not_pick",),

							"x" : 21,
							"y" : 164,

							"image" : BASE_PATH + "text_box.tga",
						},

						## top circle
						{
							"name" : "main_%d_circle" % Main_GetRuneGroup(),
							"type" : "image",
							"style" : ("not_pick",),

							"x" : 0,
							"y" : 18,

							"horizontal_align" : "center",

							"image" : BASE_PATH + "main_circles/main_circle_%d.tga" % Main_GetRuneGroup( ),

							"children" :
							(
								## inner image
								{
									"name" : "main_%d_circle_inner" % Main_GetRuneGroup(),
									"type" : "image",
									"style" : ("not_pick",),

									"x" : -33,
									"y" : -43,

									"image" : BASE_PATH + "rune%d/main_circle_inner.tga" % Main_GetRuneGroup(),
								},
								## glow for the circle while hovering
								{
									"name" : "main_%d_circle_glow" % Main_GetRuneGroup(),
									"type" : "image",
									"style" : ("not_pick",),

									"x" : -32,
									"y" : -40,

									"image" : BASE_PATH + "rune%d/main_circle_glow.tga" % Main_GetRuneGroup(),
								},
							),
						},

						## group title name
						{
							"name" : "main_%d_title" % Main_GetRuneGroup(),
							"type" : "text",
							"style" : ("not_pick",),

							"x" : 0,
							"y" : 178,

							"horizontal_align" : "center",
							"text_horizontal_align" : "center",

							"fontname": "Tahoma:16",
							"letter_spacing" : 2,
							"text" : uiScriptLocale.GetLocals()["RUNE_MAIN_GROUP_TITLE%d" % Main_GetRuneGroup()],
						},

						## group desc
						{
							"name" : "main_%d_description" % Main_GetRuneGroup(),
							"type" : "multi_text",
							"style" : ("not_pick",),

							"x" : 0,
							"y" : 30,

							"width" : MAIN_GROUP_WIDTH - 15 * 2,

							"horizontal_align" : "center",
							"text_horizontal_align" : "center",
							"vertical_align" : "bottom",

							"register_color" : (
								(False, MAIN_TEXT_COLOR_DEFAULT, True), # not over, default
								(True, MAIN_TEXT_COLOR_OVER), # over
							),
							"text" : uiScriptLocale.GetLocals()["RUNE_MAIN_GROUP_DESC%d" % Main_GetRuneGroup()],
						},

						## main runes
						{
							"name" : "main_%d_runes" % Main_GetRuneGroup(),
							"style" : ("not_pick",),

							"x" : 0,
							"y" : 32 + 200,# + 105,

							"width" : int(62 * 2.6),
							"height" : 62 * 2 + 15,

							"horizontal_align" : "center",

							"children" :
							(
								{
									"name" : "main_%d_rune1" % Main_GetRuneGroup(),
									"type" : "image",
									"style" : ("not_pick",),

									"x" : -3,
									"y" : -10,

									"image" : BASE_PATH + "rune%d/main_rune1.tga" % Main_GetRuneGroup(),
								},
								{
									"name" : "main_%d_rune2" % Main_GetRuneGroup(),
									"type" : "image",
									"style" : ("not_pick",),

									"x" : 67,
									"y" : -10,

									"horizontal_align" : "right",

									"image" : BASE_PATH + "rune%d/main_rune2.tga" % Main_GetRuneGroup(),
								},
								{
									"name" : "main_%d_rune3" % Main_GetRuneGroup(),
									"type" : "image",
									"style" : ("not_pick",),

									"x" : 0,
									"y" : 54,

									"horizontal_align" : "center",

									"image" : BASE_PATH + "rune%d/main_rune3.tga" % Main_GetRuneGroup(),
								},
							),
						},

						# main glow
						{
							"name" : "main_%d_glow" % Main_GetRuneGroup(),
							"type" : "image",

							"x" : 0,
							"y" : 0,

							"image" : BASE_PATH + "main_glow.tga", # % Main_GetRuneGroup(),
						},
					),
				},
				{
					"name" : "main_%d" % Main_GetRuneGroup(True),

					"x" : 19 + (MAIN_GROUP_WIDTH + MAIN_GROUP_SPACE) * (Main_GetRuneGroup() - 1),
					"y" : 35,

					"width" : MAIN_GROUP_WIDTH,
					"height" : MAIN_GROUP_HEIGHT,

					"children" :
					(
						## background lines
						{
							"name" : "main_%d_lines" % Main_GetRuneGroup(),
							"type" : "image",
							"style" : ("not_pick",),

							"x" : 31,
							"y" : 120,

							"image" : BASE_PATH + "main_lines.tga",
						},

						## text background
						{
							"name" : "main_%d_textbg" % Main_GetRuneGroup(),
							"type" : "image",
							"style" : ("not_pick",),

							"x" : 21,
							"y" : 164,

							"image" : BASE_PATH + "text_box.tga",
						},

						## top circle
						{
							"name" : "main_%d_circle" % Main_GetRuneGroup(),
							"type" : "image",
							"style" : ("not_pick",),

							"x" : 0,
							"y" : 18,

							"horizontal_align" : "center",

							"image" : BASE_PATH + "main_circles/main_circle_%d.tga" % Main_GetRuneGroup( ),

							"children" :
							(
								## inner image
								{
									"name" : "main_%d_circle_inner" % Main_GetRuneGroup(),
									"type" : "image",
									"style" : ("not_pick",),

									"x" : -33,
									"y" : -43,

									"image" : BASE_PATH + "rune%d/main_circle_inner.tga" % Main_GetRuneGroup(),
								},
								## glow for the circle while hovering
								{
									"name" : "main_%d_circle_glow" % Main_GetRuneGroup(),
									"type" : "image",
									"style" : ("not_pick",),

									"x" : -32,
									"y" : -40,

									"image" : BASE_PATH + "rune%d/main_circle_glow.tga" % Main_GetRuneGroup(),
								},
							),
						},

						## group title name
						{
							"name" : "main_%d_title" % Main_GetRuneGroup(),
							"type" : "text",
							"style" : ("not_pick",),

							"x" : 0,
							"y" : 178,

							"horizontal_align" : "center",
							"text_horizontal_align" : "center",

							"fontname": "Tahoma:16",
							"letter_spacing" : 2,
							"text" : uiScriptLocale.GetLocals()["RUNE_MAIN_GROUP_TITLE%d" % Main_GetRuneGroup()],
						},

						## group desc
						{
							"name" : "main_%d_description" % Main_GetRuneGroup(),
							"type" : "multi_text",
							"style" : ("not_pick",),

							"x" : 0,
							"y" : 30,

							"width" : MAIN_GROUP_WIDTH - 15 * 2,

							"horizontal_align" : "center",
							"text_horizontal_align" : "center",
							"vertical_align" : "bottom",

							"register_color" : (
								(False, MAIN_TEXT_COLOR_DEFAULT, True), # not over, default
								(True, MAIN_TEXT_COLOR_OVER), # over
							),
							"text" : uiScriptLocale.GetLocals()["RUNE_MAIN_GROUP_DESC%d" % Main_GetRuneGroup()],
						},

						## main runes
						{
							"name" : "main_%d_runes" % Main_GetRuneGroup(),
							"style" : ("not_pick",),

							"x" : 0,
							"y" : 32 + 200,# + 105,

							"width" : int(62 * 2.6),
							"height" : 62 * 2 + 15,

							"horizontal_align" : "center",

							"children" :
							(
								{
									"name" : "main_%d_rune1" % Main_GetRuneGroup(),
									"type" : "image",
									"style" : ("not_pick",),

									"x" : -3,
									"y" : -10,

									"image" : BASE_PATH + "rune%d/main_rune1.tga" % Main_GetRuneGroup(),
								},
								{
									"name" : "main_%d_rune2" % Main_GetRuneGroup(),
									"type" : "image",
									"style" : ("not_pick",),

									"x" : 67,
									"y" : -10,

									"horizontal_align" : "right",

									"image" : BASE_PATH + "rune%d/main_rune2.tga" % Main_GetRuneGroup(),
								},
								{
									"name" : "main_%d_rune3" % Main_GetRuneGroup(),
									"type" : "image",
									"style" : ("not_pick",),

									"x" : 0,
									"y" : 54,

									"horizontal_align" : "center",

									"image" : BASE_PATH + "rune%d/main_rune3.tga" % Main_GetRuneGroup(),
								},
							),
						},

						# main glow
						{
							"name" : "main_%d_glow" % Main_GetRuneGroup(),
							"type" : "image",

							"x" : 0,
							"y" : 0,

							"image" : BASE_PATH + "main_glow.tga", # % Main_GetRuneGroup(),
						},
					),
				},
			),
		},
	),
}
