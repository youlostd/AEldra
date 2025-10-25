import uiScriptLocale
import rune
import grp
import localeInfo

BASE_PATH = "d:/ymir work/ui/game/runes/"
TEXT_COLOR = grp.GenerateColor(160.0 / 255.0, 155.0 / 255.0, 140.0 / 255.0, 1.0)

INNER_WIDTH 	= 666
INNER_HEIGHT 	= 470

BOARD_WIDTH 	= 709
BOARD_HEIGHT 	= 531

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

			"image" :  BASE_PATH + "bg2.tga",

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
					"name" : "background",
					"type" : "image",

					"image" : BASE_PATH + "sub_group_circle_below.tga", # need a random image to make it work

					"x" : 10,
					"y" : 32,

					"children" :
					(
						## buttons
						{
							"name" : "save_button",
							"type" : "button",

							"x" : 20 + 36,
							"y" : 16,
							"horizontal_align" : "right",

							"default_image" : BASE_PATH + "btn_save_01.tga",
							"over_image" : BASE_PATH + "btn_save_02.tga",
							"down_image" : BASE_PATH + "btn_save_03.tga",
							"disable_image" : BASE_PATH + "btn_save_04.tga",

							"tooltip_text" : localeInfo.RUNE_TOOLTIP_SAVE,
						},
						{
							"name" : "reset_button",
							"type" : "button",

							"x" : 20 + 36 + 10 + 32,
							"y" : 16,
							"horizontal_align" : "right",

							"default_image" : BASE_PATH + "btn_reset_01.tga",
							"over_image" : BASE_PATH + "btn_reset_02.tga",
							"down_image" : BASE_PATH + "btn_reset_03.tga",
							"disable_image" : BASE_PATH + "btn_reset_04.tga",

							"tooltip_text" : localeInfo.RUNE_TOOLTIP_RESET,
						},

						{
							"name" : "addpoint_button",
							"type" : "button",

							"x" : 20 + 36,
							"y" : 57,
							"horizontal_align" : "right",

							"default_image" : BASE_PATH + "btn_add_01.tga",
							"over_image" : BASE_PATH + "btn_add_02.tga",
							"down_image" : BASE_PATH + "btn_add_03.tga",
							"disable_image" : BASE_PATH + "btn_add_04.tga",

							"tooltip_text" : localeInfo.BUY_POINTS,
						},

						{
							"name" : "resetpoint_button",
							"type" : "button",

							"x" : 20 + 36 + 10 + 32,
							"y" : 57,
							"horizontal_align" : "right",

							"default_image" : BASE_PATH + "btn_resetpoints_01.tga",
							"over_image" : BASE_PATH + "btn_resetpoints_02.tga",
							"down_image" : BASE_PATH + "btn_resetpoints_03.tga",
							"disable_image" : BASE_PATH + "btn_resetpoints_04.tga",

							"tooltip_text" : localeInfo.RUNE_TOOLTIP_RESETPOINTS,
						},

						{
							"name" : "info_button",
							"type" : "button",

							"x" : 46 + 10,
							"y" : 50,

							"horizontal_align" : "right",
							"vertical_align": "bottom",

							"default_image" : BASE_PATH + "rune_info_normal.tga",
							"over_image" : BASE_PATH + "rune_info_hover.tga",
							"down_image" : BASE_PATH + "rune_info_down.tga",

							"tooltip_text" : localeInfo.RUNE_TOOLTIP_INFO,
						},

						## PAGE BUTTONS
						{
							"name" : "page_5",
							"type" : "radio_button",

							"x" : 46 + 25 * 0,
							"y" : 40,

							"default_image" : BASE_PATH + "btn_page.tga",
							"over_image" : BASE_PATH + "btn_page_hover.tga",
							"down_image" : BASE_PATH + "btn_page_active.tga",

							"horizontal_align" : "right",
							"vertical_align": "bottom",

							"children" :
							(
								{
									"name" : "page_5_text",
									"type" : "text",

									"x" : 11,
									"y" : 3,

									"text_horizontal_align": "center",
									"text" : "5",
								},
							),
						},

						{
							"name" : "page_4",
							"type" : "radio_button",

							"x" : 46 + 25 * 1,
							"y" : 40,

							"default_image" : BASE_PATH + "btn_page.tga",
							"over_image" : BASE_PATH + "btn_page_hover.tga",
							"down_image" : BASE_PATH + "btn_page_active.tga",

							"horizontal_align" : "right",
							"vertical_align": "bottom",

							"children" :
							(
								{
									"name" : "page_5_text",
									"type" : "text",

									"x" : 11,
									"y" : 3,

									"text_horizontal_align": "center",
									"text" : "4",
								},
							),
						},

						{
							"name" : "page_3",
							"type" : "radio_button",

							"x" : 46 + 25 * 2,
							"y" : 40,

							"default_image" : BASE_PATH + "btn_page.tga",
							"over_image" : BASE_PATH + "btn_page_hover.tga",
							"down_image" : BASE_PATH + "btn_page_active.tga",

							"horizontal_align" : "right",
							"vertical_align": "bottom",

							"children" :
							(
								{
									"name" : "page_5_text",
									"type" : "text",

									"x" : 11,
									"y" : 3,

									"text_horizontal_align": "center",
									"text" : "3",
								},
							),
						},

						{
							"name" : "page_2",
							"type" : "radio_button",

							"x" : 46 + 25 * 3,
							"y" : 40,

							"default_image" : BASE_PATH + "btn_page.tga",
							"over_image" : BASE_PATH + "btn_page_hover.tga",
							"down_image" : BASE_PATH + "btn_page_active.tga",

							"horizontal_align" : "right",
							"vertical_align": "bottom",

							"children" :
							(
								{
									"name" : "page_5_text",
									"type" : "text",

									"x" : 11,
									"y" : 3,

									"text_horizontal_align": "center",
									"text" : "2",
								},
							),
						},

						{
							"name" : "page_1",
							"type" : "radio_button",

							"x" : 46 + 25 * 4,
							"y" : 40,

							"default_image" : BASE_PATH + "btn_page.tga",
							"over_image" : BASE_PATH + "btn_page_hover.tga",
							"down_image" : BASE_PATH + "btn_page_active.tga",

							"horizontal_align" : "right",
							"vertical_align": "bottom",

							"children" :
							(
								{
									"name" : "page_5_text",
									"type" : "text",

									"x" : 11,
									"y" : 3,

									"text_horizontal_align": "center",
									"text" : "1",
								},
							),
						},

						## POINTS
						{
							"name" : "points_bg",
							"type" : "image",
							"style" : ("not_pick",),

							"x" : 20 + 36 + 10 + 32 + 98,
							"y" : 18,
							"horizontal_align" : "right",

							"image" : BASE_PATH + "points_bg.tga",

							"children" :
							(
								{
									"name" : "points_available",
									"type" : "text",

									"x" : 8,
									"y" : 3,

									"fontsize" : "BOLD",
									"horizontal_align" : "left",
									"text_horizontal_align": "left",

									"text" : localeInfo.BOSS_HUNT_POINTS,
								},

								{
									"name" : "points_amount",
									"type" : "text",

									"x" : 8,
									"y" : 3,

									"fontsize" : "BOLD",
									"horizontal_align" : "right",
									"text_horizontal_align": "right",

									"text" : "0",
								},
							),
						},

						{
							"name" : "group_line_long",
							"type" : "image",
							"style" : ("not_pick",),

							"x" : 47,
							"y" : 30 + 46,

							"image" : BASE_PATH + "sub_line_long.tga",
						},
						
						## rest
						{
							"name" : "group_circle",
							"type" : "button",

							"x" : 30,
							"y" : 30,

							"default_image" : BASE_PATH + "sub_group_circle.tga",
							"over_image" : BASE_PATH + "sub_group_circle.tga",
							"down_image" : BASE_PATH + "sub_group_circle.tga",

							"children" :
							(
								{
									"name" : "group_image",
									"type" : "image",
									"style" : ("not_pick",),

									"x" : 0,
									"y" : 0,

									"image" : BASE_PATH + "sub_group_circle_below.tga", # need a random image to make it work

									"horizontal_align" : "center",
									"vertical_align" : "center",
								},
								{
									"name" : "group_name",
									"type" : "text",

									"x" : 60 + 20,
									"y" : 5,

									"fontsize" : "LARGE_BOLD",
									"letter_spacing" : 2,
								},
								{
									"name" : "group_desc",
									"type" : "multi_text",

									"x" : 60 + 20,
									"y" : 5 + 23,

									"width" : 190,

									"color" : TEXT_COLOR,
								},
							),
						},
						{
							"name" : "group_circle_below",
							"type" : "image",
							"style" : ("not_pick",),

							"x" : 31,
							"y" : 30 + 52,

							"image" : BASE_PATH + "sub_group_circle_below.tga",
						},
					#	{
						#	"name" : "type_seperator1",
						#	"type" : "image",
						#	"style" : ("not_pick",),
#
						#	"x" : 28,
						#	"y" : 191,
#
						#	"image" : BASE_PATH + "sub_type_seperator.tga",
						#},
						{
							"name" : "rune_circle_main",
							"type" : "button",

							"x" : 29,
							"y" : 30 + 52 + 46,

							"default_image" : BASE_PATH + "sub_rune_circle_main.tga",
							"over_image" : BASE_PATH + "sub_rune_circle_main.tga",
							"down_image" : BASE_PATH + "sub_rune_circle_main.tga",

							"over_underlay" : BASE_PATH + "sub_rune_circle_main_hover.tga",
							"down_underlay" : BASE_PATH + "sub_rune_circle_main_hover.tga",
							"underlay_alpha" : 0.6,

							"children" :
							(
								{
									"name" : "rune_main_name",
									"type" : "text",

									"x" : 7 + 60 + 20,
									"y" : 5,

									"fontsize" : "BOLD",
									"letter_spacing" : 1,
								},
								{
									"name" : "rune_main_noname",
									"type" : "text",

									"x" : 7 + 60 + 20,
									"y" : 5,

									"fontsize" : "BOLD",
									"color" : TEXT_COLOR,

									"text" : uiScriptLocale.RUNE_SUB_MAIN_SELECT1,
								},
								{
									"name" : "rune_main_desc",
									"type" : "multi_text",

									"x" : 7 + 60 + 20,
									"y" : 5 + 20,

									"width" : 190,

									"color" : TEXT_COLOR,
								},
								{
									"name" : "rune_main_desc_2",
									"type" : "multi_text",

									"x" : 7 + 60 + 20,
									"y" : 5 + 20 + 16,

									"width" : 190,

									"color" : TEXT_COLOR,
								},
							),
						},
						{
							"name" : "rune_select_main",
							"style" : ("not_pick",),

							"x" : 36 + 80,
							"y" : 30 + 52 + 46,

							"width" : 48 * 3 + 13 * 2,
							"height" : 48,

							"children" :
							(
								{
									"name" : "subtitle_image",
									"type" : "image",
									"style" : ("not_pick",),

									"x" : -2,
									"y" : -26,

									"image" : BASE_PATH + "sub_title.tga",
								},

								{
									"name" : "subtitle_text",
									"type" : "text",

									"x" : 3,
									"y" : -25,

									"fontsize" : "BOLD",
									"text" : uiScriptLocale.RUNE_SUB_SUBTITLE_TEXT,
								},

								{
									"name" : "arrow",
									"type" : "image",
									"style" : ("not_pick",),

									"x" : -27,
									"y" : 11,

									"image" : BASE_PATH + "sub_rune_circle_arrow.tga",
								},

								{
									"name" : "rune_select_main_1",
									"type" : "button",

									"x" : (48 + 13) * 0,
									"y" : 0,

									"default_image" : BASE_PATH + "empty.tga",
									"over_image" : BASE_PATH + "empty.tga",
									"down_image" : BASE_PATH + "empty.tga",

									"underlay_alpha" : 0.6,
								},
								{
									"name" : "rune_select_main_2",
									"type" : "button",

									"x" : (48 + 13) * 1,
									"y" : 0,

									"default_image" : BASE_PATH + "empty.tga",
									"over_image" : BASE_PATH + "empty.tga",
									"down_image" : BASE_PATH + "empty.tga",
									"underlay_alpha" : 0.6,
								},
								{
									"name" : "rune_select_main_3",
									"type" : "button",

									"x" : (48 + 13) * 2,
									"y" : 0,

									"default_image" : BASE_PATH + "empty.tga",
									"over_image" : BASE_PATH + "empty.tga",
									"down_image" : BASE_PATH + "empty.tga",
									"underlay_alpha" : 0.6,
								},
							),
						},
						#{
						#	"name" : "type_seperator2",
						#	"type" : "image",
						#	"style" : ("not_pick",),
#
						#	"x" : 28,
						#	"y" : 286,
#
						#	"image" : BASE_PATH + "sub_type_seperator_mirror.tga",
						#},
						{
							"name" : "rune_circle_1",
							"type" : "button",

							"x" : 30,
							"y" : 30 + 52 + 130,

							"default_image" : BASE_PATH + "sub_rune_circle2.tga",
							"over_image" : BASE_PATH + "sub_rune_circle2.tga",
							"down_image" : BASE_PATH + "sub_rune_circle2.tga",

							"over_underlay" : BASE_PATH + "sub_rune_circle_hover.tga",
							"down_underlay" : BASE_PATH + "sub_rune_circle_hover.tga",
							"underlay_alpha" : 0.6,

							"children" :
							(
								{
									"name" : "rune_1_name",
									"type" : "text",

									"x" : 60 + 20,
									"y" : 5,

									"fontsize" : "BOLD",
									"letter_spacing" : 1,
								},
								{
									"name" : "rune_1_noname",
									"type" : "text",

									"x" : 60 + 20,
									"y" : 5,

									"fontsize" : "BOLD",
									"color" : TEXT_COLOR,

									"text" : uiScriptLocale.RUNE_SUB_MAIN_SELECT2,
								},
								{
									"name" : "rune_1_desc",
									"type" : "multi_text",

									"x" : 60 + 20,
									"y" : 5 + 20,

									"width" : 190,

									"color" : TEXT_COLOR,
								},
							),
						},
						{
							"name" : "rune_select_1",
							"style" : ("not_pick",),

							"x" : 36 + 80,
							"y" : 30 + 52 + 130,

							"width" : 48 * 3 + 13 * 2,
							"height" : 48,

							"children" :
							(
								{
									"name" : "arrow",
									"type" : "image",
									"style" : ("not_pick",),

									"x" : -28,
									"y" : 14,

									"image" : BASE_PATH + "sub_rune_circle_arrow2.tga",
								},

								{
									"name" : "rune_select_1_1",
									"type" : "button",

									"x" : (48 + 13) * 0,
									"y" : 0,

									"default_image" : BASE_PATH + "empty.tga",
									"over_image" : BASE_PATH + "empty.tga",
									"down_image" : BASE_PATH + "empty.tga",
									"underlay_alpha" : 0.6,
								},
								{
									"name" : "rune_select_1_2",
									"type" : "button",

									"x" : (48 + 13) * 1,
									"y" : 0,

									"default_image" : BASE_PATH + "empty.tga",
									"over_image" : BASE_PATH + "empty.tga",
									"down_image" : BASE_PATH + "empty.tga",
									"underlay_alpha" : 0.6,
								},
								{
									"name" : "rune_select_1_3",
									"type" : "button",

									"x" : (48 + 13) * 2,
									"y" : 0,

									"default_image" : BASE_PATH + "empty.tga",
									"over_image" : BASE_PATH + "empty.tga",
									"down_image" : BASE_PATH + "empty.tga",
									"underlay_alpha" : 0.6,
								},
							),
						},
						{
							"name" : "rune_circle_2",
							"type" : "button",

							"x" : 30,
							"y" : 30 + 52 + 130 + 46 + 30 * 1, # 30 = pad

							"default_image" : BASE_PATH + "sub_rune_circle2.tga",
							"over_image" : BASE_PATH + "sub_rune_circle2.tga",
							"down_image" : BASE_PATH + "sub_rune_circle2.tga",

							"over_underlay" : BASE_PATH + "sub_rune_circle_hover.tga",
							"down_underlay" : BASE_PATH + "sub_rune_circle_hover.tga",
							"underlay_alpha" : 0.6,

							"children" :
							(
								{
									"name" : "rune_2_name",
									"type" : "text",

									"x" : 60 + 20,
									"y" : 5,

									"fontsize" : "BOLD",
									"letter_spacing" : 1,
								},
								{
									"name" : "rune_2_noname",
									"type" : "text",

									"x" : 60 + 20,
									"y" : 5,

									"fontsize" : "BOLD",
									"color" : TEXT_COLOR,

									"text" : uiScriptLocale.RUNE_SUB_MAIN_SELECT2,
								},
								{
									"name" : "rune_2_desc",
									"type" : "multi_text",

									"x" : 60 + 20,
									"y" : 5 + 20,

									"width" : 190,

									"color" : TEXT_COLOR,
								},
							),
						},
						{
							"name" : "rune_select_2",
							"style" : ("not_pick",),

							"x" : 36 + 80,
							"y" : 30 + 52 + 130 + 46 + 30 * 1,

							"width" : 48 * 3 + 13 * 2,
							"height" : 48,

							"children" :
							(
								{
									"name" : "arrow",
									"type" : "image",
									"style" : ("not_pick",),

									"x" : -28,
									"y" : 14,

									"image" : BASE_PATH + "sub_rune_circle_arrow2.tga",
								},

								{
									"name" : "rune_select_2_1",
									"type" : "button",

									"x" : (48 + 13) * 0,
									"y" : 0,

									"default_image" : BASE_PATH + "empty.tga",
									"over_image" : BASE_PATH + "empty.tga",
									"down_image" : BASE_PATH + "empty.tga",
									"underlay_alpha" : 0.6,
								},
								{
									"name" : "rune_select_2_2",
									"type" : "button",

									"x" : (48 + 13) * 1,
									"y" : 0,

									"default_image" : BASE_PATH + "empty.tga",
									"over_image" : BASE_PATH + "empty.tga",
									"down_image" : BASE_PATH + "empty.tga",
									"underlay_alpha" : 0.6,
								},
								{
									"name" : "rune_select_2_3",
									"type" : "button",

									"x" : (48 + 13) * 2,
									"y" : 0,

									"default_image" : BASE_PATH + "empty.tga",
									"over_image" : BASE_PATH + "empty.tga",
									"down_image" : BASE_PATH + "empty.tga",
									"underlay_alpha" : 0.6,
								},
							),
						},
						{
							"name" : "rune_circle_3",
							"type" : "button",

							"x" : 30,
							"y" : 30 + 52 + 130 + 46 * 2 + 30 * 2,

							"default_image" : BASE_PATH + "sub_rune_circle2.tga",
							"over_image" : BASE_PATH + "sub_rune_circle2.tga",
							"down_image" : BASE_PATH + "sub_rune_circle2.tga",

							"over_underlay" : BASE_PATH + "sub_rune_circle_hover.tga",
							"down_underlay" : BASE_PATH + "sub_rune_circle_hover.tga",
							"underlay_alpha" : 0.6,

							"children" :
							(
								{
									"name" : "rune_3_name",
									"type" : "text",

									"x" : 60 + 20,
									"y" : 5,

									"fontsize" : "BOLD",
									"letter_spacing" : 1,
								},
								{
									"name" : "rune_3_noname",
									"type" : "text",

									"x" : 60 + 20,
									"y" : 5,

									"fontsize" : "BOLD",
									"color" : TEXT_COLOR,

									"text" : uiScriptLocale.RUNE_SUB_MAIN_SELECT2,
								},
								{
									"name" : "rune_3_desc",
									"type" : "multi_text",

									"x" : 60 + 20,
									"y" : 5 + 20,

									"width" : 190,

									"color" : TEXT_COLOR,
								},
							),
						},
						{
							"name" : "rune_select_3",
							"style" : ("not_pick",),

							"x" : 36 + 80,
							"y" : 30 + 52 + 130 + 46 * 2 + 30 * 2,

							"width" : 48 * 3 + 13 * 2,
							"height" : 48,

							"children" :
							(
								{
									"name" : "arrow",
									"type" : "image",
									"style" : ("not_pick",),

									"x" : -28,
									"y" : 14,

									"image" : BASE_PATH + "sub_rune_circle_arrow2.tga",
								},

								{
									"name" : "rune_select_3_1",
									"type" : "button",

									"x" : (48 + 13) * 0,
									"y" : 0,

									"default_image" : BASE_PATH + "empty.tga",
									"over_image" : BASE_PATH + "empty.tga",
									"down_image" : BASE_PATH + "empty.tga",
									"underlay_alpha" : 0.6,
								},
								{
									"name" : "rune_select_3_2",
									"type" : "button",

									"x" : (48 + 13) * 1,
									"y" : 0,

									"default_image" : BASE_PATH + "empty.tga",
									"over_image" : BASE_PATH + "empty.tga",
									"down_image" : BASE_PATH + "empty.tga",
									"underlay_alpha" : 0.6,
								},
								{
									"name" : "rune_select_3_3",
									"type" : "button",

									"x" : (48 + 13) * 2,
									"y" : 0,

									"default_image" : BASE_PATH + "empty.tga",
									"over_image" : BASE_PATH + "empty.tga",
									"down_image" : BASE_PATH + "empty.tga",
									"underlay_alpha" : 0.6,
								},
							),
						},
						
						### SUB GROUP
						{
							"name" : "group_line_short",
							"type" : "image",
							"style" : ("not_pick",),

							"x" : 30 + 306 + 16,
							"y" : 113 + 46,

							"image" : BASE_PATH + "sub_line_short.tga",
						},

						{
							"name" : "sub_group_circle",
							"type" : "button",

							"x" : 30 + 306,
							"y" : 113,

							"default_image" : BASE_PATH + "sub_group_circle.tga",
							"over_image" : BASE_PATH + "sub_group_circle.tga",
							"down_image" : BASE_PATH + "sub_group_circle.tga",

							"children" :
							(
								{
									"name" : "sub_group_name",
									"type" : "text",

									"x" : 60 + 20,
									"y" : 5,

									"fontsize" : "BOLD",
									"letter_spacing" : 1,
								},
								{
									"name" : "sub_group_noname",
									"type" : "text",

									"x" : 60 + 20,
									"y" : 5,

									"fontsize" : "BOLD",
									"letter_spacing" : 1,

									"text" : uiScriptLocale.RUNE_SUB_SUB_SELECT_GROUP,
								},
								{
									"name" : "sub_group_desc",
									"type" : "multi_text",

									"x" : 60 + 20,
									"y" : 5 + 23,

									"width" : 190,

									"color" : TEXT_COLOR,
								},
							),
						},
						{
							"name" : "sub_group_below",
							"type" : "image",
							"style" : ("not_pick",),

							"x" : 31 + 306,
							"y" : 113 + 52,

							"image" : BASE_PATH + "sub_group_circle_below.tga",
						},
						{
							"name" : "sub_group_select",
							"style" : ("not_pick",),

							"x" : 36 + 306 + 80,
							"y" : 117 + 4,

							"width" : 48 * 4 + 13 * 3,
							"height" : 48,

							"children" :
							(
								{
									"name" : "sub_group_select_1",
									"type" : "button",

									"x" : (48 + 13) * 0,
									"y" : 0,

									"default_image" : BASE_PATH + "sub_rune_circle.tga",
									"over_image" : BASE_PATH + "sub_rune_circle.tga",
									"down_image" : BASE_PATH + "sub_rune_circle.tga",

									"over_underlay" : BASE_PATH + "sub_rune_circle_hover.tga",
									"down_underlay" : BASE_PATH + "sub_rune_circle_hover.tga",
									"underlay_alpha" : 0.6,
								},
								{
									"name" : "sub_group_select_2",
									"type" : "button",

									"x" : (48 + 13) * 1,
									"y" : 0,

									"default_image" : BASE_PATH + "sub_rune_circle.tga",
									"over_image" : BASE_PATH + "sub_rune_circle.tga",
									"down_image" : BASE_PATH + "sub_rune_circle.tga",

									"over_underlay" : BASE_PATH + "sub_rune_circle_hover.tga",
									"down_underlay" : BASE_PATH + "sub_rune_circle_hover.tga",
									"underlay_alpha" : 0.6,
								},
								{
									"name" : "sub_group_select_3",
									"type" : "button",

									"x" : (48 + 13) * 2,
									"y" : 0,

									"default_image" : BASE_PATH + "sub_rune_circle.tga",
									"over_image" : BASE_PATH + "sub_rune_circle.tga",
									"down_image" : BASE_PATH + "sub_rune_circle.tga",

									"over_underlay" : BASE_PATH + "sub_rune_circle_hover.tga",
									"down_underlay" : BASE_PATH + "sub_rune_circle_hover.tga",
									"underlay_alpha" : 0.6,
								},
								{
									"name" : "sub_group_select_4",
									"type" : "button",

									"x" : (48 + 13) * 3,
									"y" : 0,

									"default_image" : BASE_PATH + "sub_rune_circle.tga",
									"over_image" : BASE_PATH + "sub_rune_circle.tga",
									"down_image" : BASE_PATH + "sub_rune_circle.tga",

									"over_underlay" : BASE_PATH + "sub_rune_circle_hover.tga",
									"down_underlay" : BASE_PATH + "sub_rune_circle_hover.tga",
									"underlay_alpha" : 0.6,
								},
							),
						},
						{
							"name" : "sub_rune_circle_1",
							"type" : "button",

							"x" : 29 + 306,
							"y" : 200,

							"default_image" : BASE_PATH + "sub_rune_circle2.tga",
							"over_image" : BASE_PATH + "sub_rune_circle2.tga",
							"down_image" : BASE_PATH + "sub_rune_circle2.tga",
							"disable_image" : BASE_PATH + "sub_rune_circle2.tga",

							"over_underlay" : BASE_PATH + "sub_rune_circle_hover.tga",
							"down_underlay" : BASE_PATH + "sub_rune_circle_hover.tga",
							"underlay_alpha" : 0.6,

							"children" :
							(
								{
									"name" : "sub_rune_name_1",
									"type" : "text",

									"x" : 60 + 20,
									"y" : 5,

									"fontsize" : "BOLD",
									"letter_spacing" : 1,
								},
								{
									"name" : "sub_rune_noname_1",
									"type" : "text",

									"x" : 60 + 20,
									"y" : 5,

									"fontsize" : "BOLD",
									"letter_spacing" : 1,

									"text" : uiScriptLocale.RUNE_SUB_SUB_SELECT_RUNE,
								},
								{
									"name" : "sub_rune_nogroup_1",
									"type" : "text",

									"x" : 60 + 20,
									"y" : 5,

									"fontsize" : "BOLD",
									"letter_spacing" : 1,

									"text" : uiScriptLocale.RUNE_SUB_SUB_SELECT_RUNE_NOGROUP,
								},
								{
									"name" : "sub_rune_desc_1",
									"type" : "multi_text",

									"x" : 60 + 20,
									"y" : 5 + 23,

									"width" : 190,

									"color" : TEXT_COLOR,
								},
							),
						},
						{
							"name" : "sub_rune_circle_2",
							"type" : "button",

							"x" : 29 + 306,
							"y" : 296,

							"default_image" : BASE_PATH + "sub_rune_circle2.tga",
							"over_image" : BASE_PATH + "sub_rune_circle2.tga",
							"down_image" : BASE_PATH + "sub_rune_circle2.tga",
							"disable_image" : BASE_PATH + "sub_rune_circle2.tga",

							"over_underlay" : BASE_PATH + "sub_rune_circle_hover.tga",
							"down_underlay" : BASE_PATH + "sub_rune_circle_hover.tga",
							"underlay_alpha" : 0.6,

							"children" :
							(
								{
									"name" : "sub_rune_name_2",
									"type" : "text",

									"x" : 60 + 20,
									"y" : 5,

									"fontsize" : "BOLD",
									"letter_spacing" : 1,
								},
								{
									"name" : "sub_rune_noname_2",
									"type" : "text",

									"x" : 60 + 20,
									"y" : 5,

									"fontsize" : "BOLD",
									"letter_spacing" : 1,

									"text" : uiScriptLocale.RUNE_SUB_SUB_SELECT_RUNE,
								},
								{
									"name" : "sub_rune_nogroup_2",
									"type" : "text",

									"x" : 60 + 20,
									"y" : 5,

									"fontsize" : "BOLD",
									"letter_spacing" : 1,

									"text" : uiScriptLocale.RUNE_SUB_SUB_SELECT_RUNE_NOGROUP,
								},
								{
									"name" : "sub_rune_desc_2",
									"type" : "multi_text",

									"x" : 60 + 20,
									"y" : 5 + 23,

									"width" : 190,

									"color" : TEXT_COLOR,
								},
							),
						},
						{
							"name" : "sub_rune_select",

							"x" : 36 + 306 + 80,
							"y" : ( 291 - (48 * 3 + 13 * 2) / 2 ) - 10,

							"width" : 48 * 3 + 13 * 2,
							"height" : 48 * 3 + 13 * 2,

							"children" :
							(
								{
									"name" : "sub_rune_select_1_1",
									"type" : "button",

									"x" : (48 + 13) * 0,
									"y" : (48 + 13) * 0,

									"default_image" : BASE_PATH + "sub_rune_circle.tga",
									"over_image" : BASE_PATH + "sub_rune_circle.tga",
									"down_image" : BASE_PATH + "sub_rune_circle.tga",

									"over_underlay" : BASE_PATH + "sub_rune_circle_hover.tga",
									"down_underlay" : BASE_PATH + "sub_rune_circle_hover.tga",
									"underlay_alpha" : 0.6,
								},
								{
									"name" : "sub_rune_select_1_2",
									"type" : "button",

									"x" : (48 + 13) * 1,
									"y" : (48 + 13) * 0,

									"default_image" : BASE_PATH + "sub_rune_circle.tga",
									"over_image" : BASE_PATH + "sub_rune_circle.tga",
									"down_image" : BASE_PATH + "sub_rune_circle.tga",

									"over_underlay" : BASE_PATH + "sub_rune_circle_hover.tga",
									"down_underlay" : BASE_PATH + "sub_rune_circle_hover.tga",
									"underlay_alpha" : 0.6,
								},
								{
									"name" : "sub_rune_select_1_3",
									"type" : "button",

									"x" : (48 + 13) * 2,
									"y" : (48 + 13) * 0,

									"default_image" : BASE_PATH + "sub_rune_circle.tga",
									"over_image" : BASE_PATH + "sub_rune_circle.tga",
									"down_image" : BASE_PATH + "sub_rune_circle.tga",

									"over_underlay" : BASE_PATH + "sub_rune_circle_hover.tga",
									"down_underlay" : BASE_PATH + "sub_rune_circle_hover.tga",
									"underlay_alpha" : 0.6,
								},
								{
									"name" : "sub_rune_select_2_1",
									"type" : "button",

									"x" : (48 + 13) * 0,
									"y" : (48 + 13) * 1,

									"default_image" : BASE_PATH + "sub_rune_circle.tga",
									"over_image" : BASE_PATH + "sub_rune_circle.tga",
									"down_image" : BASE_PATH + "sub_rune_circle.tga",

									"over_underlay" : BASE_PATH + "sub_rune_circle_hover.tga",
									"down_underlay" : BASE_PATH + "sub_rune_circle_hover.tga",
									"underlay_alpha" : 0.6,
								},
								{
									"name" : "sub_rune_select_2_2",
									"type" : "button",

									"x" : (48 + 13) * 1,
									"y" : (48 + 13) * 1,

									"default_image" : BASE_PATH + "sub_rune_circle.tga",
									"over_image" : BASE_PATH + "sub_rune_circle.tga",
									"down_image" : BASE_PATH + "sub_rune_circle.tga",

									"over_underlay" : BASE_PATH + "sub_rune_circle_hover.tga",
									"down_underlay" : BASE_PATH + "sub_rune_circle_hover.tga",
									"underlay_alpha" : 0.6,
								},
								{
									"name" : "sub_rune_select_2_3",
									"type" : "button",

									"x" : (48 + 13) * 2,
									"y" : (48 + 13) * 1,

									"default_image" : BASE_PATH + "sub_rune_circle.tga",
									"over_image" : BASE_PATH + "sub_rune_circle.tga",
									"down_image" : BASE_PATH + "sub_rune_circle.tga",

									"over_underlay" : BASE_PATH + "sub_rune_circle_hover.tga",
									"down_underlay" : BASE_PATH + "sub_rune_circle_hover.tga",
									"underlay_alpha" : 0.6,
								},
								{
									"name" : "sub_rune_select_3_1",
									"type" : "button",

									"x" : (48 + 13) * 0,
									"y" : (48 + 13) * 2,

									"default_image" : BASE_PATH + "sub_rune_circle.tga",
									"over_image" : BASE_PATH + "sub_rune_circle.tga",
									"down_image" : BASE_PATH + "sub_rune_circle.tga",

									"over_underlay" : BASE_PATH + "sub_rune_circle_hover.tga",
									"down_underlay" : BASE_PATH + "sub_rune_circle_hover.tga",
									"underlay_alpha" : 0.6,
								},
								{
									"name" : "sub_rune_select_3_2",
									"type" : "button",

									"x" : (48 + 13) * 1,
									"y" : (48 + 13) * 2,

									"default_image" : BASE_PATH + "sub_rune_circle.tga",
									"over_image" : BASE_PATH + "sub_rune_circle.tga",
									"down_image" : BASE_PATH + "sub_rune_circle.tga",

									"over_underlay" : BASE_PATH + "sub_rune_circle_hover.tga",
									"down_underlay" : BASE_PATH + "sub_rune_circle_hover.tga",
									"underlay_alpha" : 0.6,
								},
								{
									"name" : "sub_rune_select_3_3",
									"type" : "button",

									"x" : (48 + 13) * 2,
									"y" : (48 + 13) * 2,

									"default_image" : BASE_PATH + "sub_rune_circle.tga",
									"over_image" : BASE_PATH + "sub_rune_circle.tga",
									"down_image" : BASE_PATH + "sub_rune_circle.tga",

									"over_underlay" : BASE_PATH + "sub_rune_circle_hover.tga",
									"down_underlay" : BASE_PATH + "sub_rune_circle_hover.tga",
									"underlay_alpha" : 0.6,
								},
							),
						},
					),
				},
			),
		},
	),
}


import constInfo
if constInfo.ENABLE_RUNE_PAGES:
	window["children"][0]["children"] += (
					{
						"name" : "page_button_0",
						"type" : "radio_button",

						"x" : 170,
						"y" : 477,
						"horizontal_align" : "right",

						"default_image" : BASE_PATH + "btn_page.tga",
						"over_image" : BASE_PATH + "btn_page_hover.tga",
						"down_image" : BASE_PATH + "btn_page_active.tga",

						"text" : "1",
					},
					{
						"name" : "page_button_1",
						"type" : "radio_button",

						"x" : 170 - 25,
						"y" : 477,
						"horizontal_align" : "right",

						"default_image" : BASE_PATH + "btn_page.tga",
						"over_image" : BASE_PATH + "btn_page_hover.tga",
						"down_image" : BASE_PATH + "btn_page_active.tga",

						"text" : "2",
					},
					{
						"name" : "page_button_2",
						"type" : "radio_button",

						"x" : 170 - 50,
						"y" : 477,
						"horizontal_align" : "right",

						"default_image" : BASE_PATH + "btn_page.tga",
						"over_image" : BASE_PATH + "btn_page_hover.tga",
						"down_image" : BASE_PATH + "btn_page_active.tga",

						"text" : "3",
					},
					{
						"name" : "page_button_3",
						"type" : "radio_button",

						"x" : 170 - 75,
						"y" : 477,
						"horizontal_align" : "right",

						"default_image" : BASE_PATH + "btn_page.tga",
						"over_image" : BASE_PATH + "btn_page_hover.tga",
						"down_image" : BASE_PATH + "btn_page_active.tga",

						"text" : "4",
					},
					)
