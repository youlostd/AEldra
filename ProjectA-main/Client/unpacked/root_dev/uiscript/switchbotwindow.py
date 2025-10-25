import uiScriptLocale
from ui import GenerateColor
from colorInfo import CHAT_RGB_INFO

WIDTH = 611
HEIGHT = 531

window = {

	"name" : "SwitchbotWindow",

	"x" : SCREEN_WIDTH/2 - WIDTH/2,
	"y" : SCREEN_HEIGHT/2 - HEIGHT/2,

	"width" : WIDTH,
	"height" : HEIGHT,

	"style" : ("movable", "float",),

	"children" : (
		{
			"name" : "bg",
			"type" : "image",

			"x" : 0,
			"y" : 0,

			"style" : ("attach",),
			"image" : "d:/ymir work/ui/switchbot/bg.tga",

			"children" : (
				{
					"name" : "icon",
					"type" : "image",

					"x" : 49,
					"y" : 85,

					"style" : ("attach",),
				},
				{
					"name" : "info_window",
					"type" : "window",

					"x" : 113,
					"y" : 79,

					"width" : 246,
					"height" : 113,

					"style" : ("attach",),

					"children" : (
						{
							"name" : "title_starttime",
							"type" : "text",

							"x" : 18,
							"y" : 10,

							"text" : uiScriptLocale.SWITCHBOT_START_TIME,
							
							"children" : (
								{
									"name" : "starttime",
									"type" : "text",

									"x" : 216,
									"y" : 0,

									"text_horizontal_align": "right",
									"text" : "00:00",
								},
							),
						},
						{
							"name" : "title_alltime",
							"type" : "text",

							"x" : 18,
							"y" : 10 + 25,

							"text" : uiScriptLocale.SWITCHBOT_TIME_PASSED,
							
							"children" : (
								{
									"name" : "alltime",
									"type" : "text",

									"x" : 216,
									"y" : 0,

									"text_horizontal_align": "right",
									"text" : "00:00:00:00",
								},
							),
						},
						{
							"name" : "title_consumption",
							"type" : "text",

							"x" : 18,
							"y" : 10 + 25 + 25,

							"text" : uiScriptLocale.SWITCHBOT_SWITCHERS_USED,
							
							"children" : (
								{
									"name" : "consumption",
									"type" : "text",

									"x" : 216,
									"y" : 0,

									"text_horizontal_align": "right",
									"text" : "0",
								},
							),
						},
						{
							"name" : "title_speed",
							"type" : "text",

							"x" : 18,
							"y" : 10 + 25 + 25 + 25,

							"text" : uiScriptLocale.SWITCHBOT_CURRENT_SPEED,
							
							"children" : (
								{
									"name" : "speed",
									"type" : "text",

									"x" : 216,
									"y" : 0,

									"text_horizontal_align": "right",
									"text" : "0",
								},
							),
						},
					),
				},
				{
					"name" : "start_button",
					"type" : "button",

					"x" : 0,
					"y" : 88,

					"horizontal_align": "center",
					"vertical_align": "bottom",

					"default_image" : "d:/ymir work/ui/switchbot/start_button_01.tga",
					"over_image" : "d:/ymir work/ui/switchbot/start_button_02.tga",
					"down_image" : "d:/ymir work/ui/switchbot/start_button_03.tga",

					"text": uiScriptLocale.SWITCHBOT_BUTTON_START,
				},
				{
					"name" : "reset_button",
					"type" : "button",

					"x" : 504,
					"y" : 205,

					"default_image" : "d:/ymir work/ui/switchbot/reset_button_01.tga",
					"over_image" : "d:/ymir work/ui/switchbot/reset_button_02.tga",
					"down_image" : "d:/ymir work/ui/switchbot/reset_button_03.tga",

					"text": uiScriptLocale.SWITCHBOT_BUTTON_RESET,
				},
				{
					"name" : "delete_button",
					"type" : "button",

					"x" : 504 - 25,
					"y" : 205,

					"default_image" : "d:/ymir work/ui/switchbot/delete_01.tga",
					"over_image" : "d:/ymir work/ui/switchbot/delete_02.tga",
					"down_image" : "d:/ymir work/ui/switchbot/delete_03.tga",

					"tooltip_text": uiScriptLocale.SWITCHBOT_BUTTON_DELETE,
				},
				{
					"name" : "dropdown_05",
					"type" : "text_dropdown",

					"style" : ("float",),

					"x" : 27,
					"y" : 241 + 39 + 39 + 39 + 39,
					
					"width" : 201,
					"height" : 27,

					"item_height" : 15,
					"viewcount" : 6,

					"default" : uiScriptLocale.SWITCHBOT_SELECT_DEFAULT,
				},
				{
					"name" : "dropdown_04",
					"type" : "text_dropdown",

					"style" : ("float",),

					"x" : 27,
					"y" : 241 + 39 + 39 + 39,
					
					"width" : 201,
					"height" : 27,

					"item_height" : 15,
					"viewcount" : 6,

					"default" : uiScriptLocale.SWITCHBOT_SELECT_DEFAULT,
				},
				{
					"name" : "dropdown_03",
					"type" : "text_dropdown",

					"x" : 27,
					"y" : 241 + 39 + 39,

					"style" : ("float",),
					
					"width" : 201,
					"height" : 27,

					"item_height" : 15,
					"viewcount" : 6,

					"default" : uiScriptLocale.SWITCHBOT_SELECT_DEFAULT,
				},
				{
					"name" : "dropdown_02",
					"type" : "text_dropdown",

					"x" : 27,
					"y" : 241 + 39,

					"style" : ("float",),
					
					"width" : 201,
					"height" : 27,

					"item_height" : 15,
					"viewcount" : 6,

					"default" : uiScriptLocale.SWITCHBOT_SELECT_DEFAULT,
				},
				{
					"name" : "dropdown_01",
					"type" : "text_dropdown",

					"x" : 27,
					"y" : 241,

					"style" : ("float",),
					
					"width" : 201,
					"height" : 27,

					"item_height" : 15,
					"viewcount" : 6,

					"default" : uiScriptLocale.SWITCHBOT_SELECT_DEFAULT,
				},
				{
					"name" : "input_01",
					"type" : "editline",

					"x" : 237 + 4,
					"y" : 242 + 4,

					"width" : 37,
					"height" : 15,

					"input_limit" : 4,
					"only_number" : 1,
				},
				{
					"name" : "input_02",
					"type" : "editline",

					"x" : 237 + 4,
					"y" : 242 + 4 + 39,

					"width" : 37,
					"height" : 15,

					"input_limit" : 4,
					"only_number" : 1,
				},
				{
					"name" : "input_03",
					"type" : "editline",

					"x" : 237 + 4,
					"y" : 242 + 4 + 39 + 39,

					"width" : 37,
					"height" : 15,

					"input_limit" : 4,
					"only_number" : 1,
				},
				{
					"name" : "input_04",
					"type" : "editline",

					"x" : 237 + 4,
					"y" : 242 + 4 + 39 + 39 + 39,

					"width" : 37,
					"height" : 15,

					"input_limit" : 4,
					"only_number" : 1,
				},
				{
					"name" : "input_05",
					"type" : "editline",

					"x" : 237 + 4,
					"y" : 242 + 4 + 39 + 39 + 39 + 39,

					"width" : 37,
					"height" : 15,

					"input_limit" : 4,
					"only_number" : 1,
				},

				# PREMIUM SECTION
				{
					"name" : "premium_section_bg",
					"type" : "image",

					"x" : 332,
					"y" : 241,
					
					"style" : ("attach",),
					"image" : "d:/ymir work/ui/switchbot/premium_active.tga",
				},

				{
					"name" : "premium_info",
					"type" : "button",

					"x" : 332,
					"y" : 207,

					"default_image" : "d:/ymir work/ui/info.tga",
					"over_image" : "d:/ymir work/ui/info.tga",
					"down_image" : "d:/ymir work/ui/info.tga",

					"children" : (
						{
							"name" : "speed_premium_text",
							"type" : "text",

							"x" : 26,
							"y" : 3,

							"text" : uiScriptLocale.SWITCHBOT_PREMIUM_INACTIVE,
							"color" : GenerateColor(*CHAT_RGB_INFO),
						},
					),
				},
				# PREMIUM SECTION END

				# PREMIUM DROPDOWN
				{
					"name" : "prem_dropdown_05",
					"type" : "text_dropdown",

					"style" : ("float",),

					"x" : 27 + 201 + 51,
					"y" : 241 + 39 + 39 + 39 + 39,
					
					"width" : 201,
					"height" : 27,

					"item_height" : 15,
					"viewcount" : 6,

					"default" : uiScriptLocale.SWITCHBOT_SELECT_DEFAULT,

					"horizontal_align" : "right",
				},
				{
					"name" : "prem_dropdown_04",
					"type" : "text_dropdown",

					"style" : ("float",),

					"x" : 27 + 201 + 51,
					"y" : 241 + 39 + 39 + 39,
					
					"width" : 201,
					"height" : 27,

					"item_height" : 15,
					"viewcount" : 6,

					"default" : uiScriptLocale.SWITCHBOT_SELECT_DEFAULT,
					"horizontal_align" : "right",
				},
				{
					"name" : "prem_dropdown_03",
					"type" : "text_dropdown",

					"x" : 27 + 201 + 51,
					"y" : 241 + 39 + 39,

					"style" : ("float",),
					
					"width" : 201,
					"height" : 27,

					"item_height" : 15,
					"viewcount" : 6,

					"default" : uiScriptLocale.SWITCHBOT_SELECT_DEFAULT,
					"horizontal_align" : "right",
				},
				{
					"name" : "prem_dropdown_02",
					"type" : "text_dropdown",

					"x" : 27 + 201 + 51,
					"y" : 241 + 39,

					"style" : ("float",),
					
					"width" : 201,
					"height" : 27,

					"item_height" : 15,
					"viewcount" : 6,

					"default" : uiScriptLocale.SWITCHBOT_SELECT_DEFAULT,
					"horizontal_align" : "right",
				},
				{
					"name" : "prem_dropdown_01",
					"type" : "text_dropdown",

					"x" : 27 + 201 + 51,
					"y" : 241,

					"style" : ("float",),
					
					"width" : 201,
					"height" : 27,

					"item_height" : 15,
					"viewcount" : 6,

					"default" : uiScriptLocale.SWITCHBOT_SELECT_DEFAULT,
					"horizontal_align" : "right",
				},
				{
					"name" : "prem_input_01",
					"type" : "editline",

					"x" : 65,
					"y" : 242 + 4,

					"width" : 37,
					"height" : 15,

					"input_limit" : 4,
					"only_number" : 1,
					"horizontal_align" : "right",
				},
				{
					"name" : "prem_input_02",
					"type" : "editline",

					"x" : 65,
					"y" : 242 + 4 + 39,

					"width" : 37,
					"height" : 15,

					"input_limit" : 4,
					"only_number" : 1,
					"horizontal_align" : "right",
				},
				{
					"name" : "prem_input_03",
					"type" : "editline",

					"x" : 65,
					"y" : 242 + 4 + 39 + 39,

					"width" : 37,
					"height" : 15,

					"input_limit" : 4,
					"only_number" : 1,
					"horizontal_align" : "right",
				},
				{
					"name" : "prem_input_04",
					"type" : "editline",

					"x" : 65,
					"y" : 242 + 4 + 39 + 39 + 39,

					"width" : 37,
					"height" : 15,

					"input_limit" : 4,
					"only_number" : 1,
					"horizontal_align" : "right",
				},
				{
					"name" : "prem_input_05",
					"type" : "editline",

					"x" :65,
					"y" : 242 + 4 + 39 + 39 + 39 + 39,

					"width" : 37,
					"height" : 15,

					"input_limit" : 4,
					"only_number" : 1,
					"horizontal_align" : "right",
				},

				# SPEED SELECTOR
				{
					"name" : "speed_slow_button",
					"type" : "radio_button",

					"x" : 384,
					"y" : 93,

					"default_image" : "d:/ymir work/ui/switchbot/speed_button_01.tga",
					"over_image" : "d:/ymir work/ui/switchbot/speed_button_02.tga",
					"down_image" : "d:/ymir work/ui/switchbot/speed_button_03.tga",
					"disable_image" : "d:/ymir work/ui/switchbot/speed_button_04.tga",

					"children" : (
						{
							"name" : "speed_slow_text",
							"type" : "text",

							"x" : 24,
							"y" : 1,

							"text" : uiScriptLocale.SWITCHBOT_SPEED_SLOW,
						},
					),
				},
				{
					"name" : "speed_medium_button",
					"type" : "radio_button",

					"x" : 384,
					"y" : 93 + 22,

					"default_image" : "d:/ymir work/ui/switchbot/speed_button_01.tga",
					"over_image" : "d:/ymir work/ui/switchbot/speed_button_02.tga",
					"down_image" : "d:/ymir work/ui/switchbot/speed_button_03.tga",
					"disable_image" : "d:/ymir work/ui/switchbot/speed_button_04.tga",

					"children" : (
						{
							"name" : "speed_medium_text",
							"type" : "text",

							"x" : 24,
							"y" : 1,

							"text" : uiScriptLocale.SWITCHBOT_SPEED_MEDIUM,
						},
					),
				},
				{
					"name" : "speed_normal_button",
					"type" : "radio_button",

					"x" : 384,
					"y" : 93 + 22 + 22,

					"default_image" : "d:/ymir work/ui/switchbot/speed_button_01.tga",
					"over_image" : "d:/ymir work/ui/switchbot/speed_button_02.tga",
					"down_image" : "d:/ymir work/ui/switchbot/speed_button_03.tga",
					"disable_image" : "d:/ymir work/ui/switchbot/speed_button_04.tga",

					"children" : (
						{
							"name" : "speed_normal_text",
							"type" : "text",

							"x" : 24,
							"y" : 1,

							"text" : uiScriptLocale.SWITCHBOT_SPEED_NORMAL,
						},
					),
				},
				{
					"name" : "speed_premium_button",
					"type" : "radio_button",

					"x" : 384,
					"y" : 93 + 22 + 22 + 22,

					"default_image" : "d:/ymir work/ui/switchbot/speed_button_01.tga",
					"over_image" : "d:/ymir work/ui/switchbot/speed_button_02.tga",
					"down_image" : "d:/ymir work/ui/switchbot/speed_button_03.tga",
					"disable_image" : "d:/ymir work/ui/switchbot/speed_button_04.tga",

					"children" : (
						{
							"name" : "speed_premium_select_text",
							"type" : "text",

							"x" : 24,
							"y" : 1,

							"text" : uiScriptLocale.SWITCHBOT_SPEED_PREMIUM,
						},
					),
				},
				# SPEED SELECTOR END
			),
		},
		{
			"name" : "bg_default",
			"type" : "image",

			"x" : 0,
			"y" : 0,

			"style" : ("attach",),
			"image" : "d:/ymir work/ui/switchbot/bg_default2.tga",
			"children" : (
				{
					"name" : "drop_label",
					"type" : "text",

					"x" : 0,
					"y" : -50,

					"horizontal_align" : "center",
					"vertical_align" : "center",
					"text_horizontal_align": "center",

					"fontname" : "Tahoma:24",
					"text" : uiScriptLocale.SWITCHBOT_DROP,
					"color" : 0xFFFFFFFF,
				},
			)
		},
		{
			"name" : "titlebar",
			"type" : "titlebar",

			"x" : 6,
			"y" : 5,

			"width": WIDTH - 10,
			"style" : ("attach",),

			"children" : (
				{
					"name" : "title",
					"type" : "text",

					"x" : 0,
					"y" : -2,

					"text" : uiScriptLocale.SWITCHBOT_TITLE,
					"all_align" : 1,
				},
				{
					"name" : "minimize_button",
					"type" : "button",

					"x" : 45,
					"y" : -1,

					"horizontal_align" : "right",
					"vertical_align" : "center",

					"default_image" : "d:/ymir work/ui/public/minimize_button_01.sub",
					"over_image" : "d:/ymir work/ui/public/minimize_button_02.sub",
					"down_image" : "d:/ymir work/ui/public/minimize_button_03.sub",
				},
			),
		},
	),
}