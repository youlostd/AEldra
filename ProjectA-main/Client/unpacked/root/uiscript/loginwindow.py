import uiScriptLocale
ROOT_PATH = "d:/ymir work/ui/intro/login/new/"
ACCSLOT_HEIGHT = 35
ACCSLOT_SPACE = 13
ACCSLOT_COUNT = 8

SCALE_X = float(SCREEN_WIDTH) / 1882.0
SCALE_Y = float(SCREEN_HEIGHT) / 927.0

LOGIN_BOX_WIDTH = 240 - 15
LOGIN_BOX_X = SCREEN_WIDTH - LOGIN_BOX_WIDTH - 12 

ACCOUNT_BOX_X = int(1440 * SCALE_X) - 10
ACCOUNT_BOX_Y = int(265 * SCALE_Y)

window = {
	"name" : "LoginWindow",
	"sytle" : ("movable",),

	"x" : 0,
	"y" : 0,

	"width" : SCREEN_WIDTH,
	"height" : SCREEN_HEIGHT- 10,

	"children" :
	(
		## BG
		{
			"name" : "bg1", "type" : "expanded_image", 
			"x" : 0, 
			"y" : 0,
			"x_scale" : SCALE_X, 
			"y_scale" : SCALE_Y,
			"image" : ROOT_PATH + "background.jpg",
		},
		#exit btn
		{
			"name" : "close_btn",
			"type" : "button",

			"x" : SCREEN_WIDTH - 132,
			"y" : 34,

			"horizontal_align" : "left",
			"vertical_align": "bottom",

			"default_image" : ROOT_PATH + "channel_active_normal.tga",
			"over_image" : ROOT_PATH + "channel_active_normal.tga",
			"down_image" : ROOT_PATH + "channel_active_normal.tga",
			
			"text" : uiScriptLocale.LOGIN_EXIT,
		},
		#pvp server btn
		{
			"name" : "pvp_server_btn",
			"type" : "button",

			"x" : 0,
			"y" : 33,

			"horizontal_align" : "center",
			"vertical_align": "bottom",

			"default_image" : ROOT_PATH + "channel_active_normal.tga",
			"over_image" : ROOT_PATH + "channel_active_normal.tga",
			"down_image" : ROOT_PATH + "channel_active_normal.tga",
			
			"text" : "",
		},
		#lang btn
		{
			"name" : "lang_title",
			"type" : "text",
			"fontname" : "Tahoma:18",
			"x": SCREEN_WIDTH - 195,
			"y": 13,
			"text" : uiScriptLocale.SELECT_LANGUAGE_TITLE,
		},

		## LOGIN_WINDOW
		{
			"name" : "LoginBoard",
			"type" : "image",

			"x" : SCREEN_WIDTH / 2 - 590 / 2,
			"y" : (SCREEN_HEIGHT - 10) / 2 - 672 / 2,

			"image" : ROOT_PATH + "login_bg.tga",

			"children" :
			(

				# Normal Login
				{

					"name" : "normal_login",
					"x" : 110,
					"y" : 160 + 100 + 5,
					"width" : 234 + 50,
					"height" : 65 + 24 + 38,
					"children" : (
						{
							"name" : "LabelAccountID",
							"type" : "text",

							"x" : 0,
							"y" : 0 + 38,

							"fontname" : "Tahoma:16",
							"text" : uiScriptLocale.ACCOUNT_USERNAME_LABEL,
						},
						{
							"name" : "LabelRegisterClick",
							"type" : "text",

							"x" : 0 + 158,
							"y" : 0 + 38,

							"text" : uiScriptLocale.ACCOUNT_REGISTER,
							"fontname" : "Tahoma:15",
							"color" : 0xFF85A6CA,
							# "text_horizontal_align" : "right",
						},

						{
							"name" : "EditAccountID_Image",
							"type" : "image",

							"x" : 0,
							"y" : 24 + 38,

							"image" : ROOT_PATH + "login_input.tga",

							"children" :
							(
								{
									"name" : "EditAccountID",
									"type" : "editline",

									"x" : 5,
									"y" : 5,

									"width" : 234-10,
									"height" : 20,

									"fontname" : "Tahoma:16",
									"input_limit" : 16,
								},
							),
						},
						{
							"name" : "LabelPasswordID",
							"type" : "text",

							"x" : 0,
							"y" : 65 + 38,

							"fontname" : "Tahoma:16",
							"text" : uiScriptLocale.ACCOUNT_PASSWORD_LABEL,
						},
						{
							"name" : "LabelPasswordForgot",
							"type" : "text",

							"x" : 166,
							"y" : 65 + 38,

							"text" : uiScriptLocale.ACCOUNT_PASSWORD_Q,
							"fontname" : "Tahoma:15",
							"color" : 0xFF85A6CA,
						},

						{
							"name" : "EditPasswordID_Image",
							"type" : "image",

							"x" : 0,
							"y" : 65 + 24 + 38,

							"image" : ROOT_PATH + "login_input.tga",

							"children" :
							(
								{
									"name" : "EditPasswordID",
									"type" : "editline",

									"x" : 5,
									"y" : 5,

									"width" : 234-10,
									"height" : 20,

									"fontname" : "Tahoma:16",
									"input_limit" : 16,
									"secret_flag" : 1,
								},
							),
						},
					),
				},

				# Channel Window,
				{
					"name" : "channel_window",
					# "type" : "thinboard_circle",
					"x" : 380,
					"y" : 130 + 100 + 73,
					"width" : 114,
					"height" : 35*4 + 26,
					"children" :
					(

						{
							"name" : "ShadowFix1",
							"type" : "window",

							"x" : 0,
							"y" : 35 * 0,

							"width" : 114,
							"height" : 26,

							"children" :
							(
								{
									"name" : "Channel1",
									"type" : "radio_button",

									"x" : -12,
									"y" : -12,

									"default_image" : ROOT_PATH + "channel_inactive_normal.tga",
									"over_image" : ROOT_PATH + "channel_inactive_normal.tga",
									"down_image" : ROOT_PATH + "channel_active_normal.tga",

									"children" :
									(
										{
											"name" : "Channel1Text",
											"type" : "text",

											"x" : 138 / 2,
											"y" : -1,

											"vertical_align" : "center",
											"text_vertical_align" : "center",
											"text_horizontal_align" : "center",

											"text" : uiScriptLocale.ACCOUNT_CHANNEL % 1,
											"fontname" : "Tahoma:14",
										},
									),
								},
							),
						},
						{
							"name" : "ShadowFix2",
							"type" : "window",

							"x" : 0,
							"y" : 35 * 1,

							"width" : 114,
							"height" : 26,

							"children" :
							(
								{
									"name" : "Channel2",
									"type" : "radio_button",

									"x" : -12,
									"y" : -12,

									"default_image" : ROOT_PATH + "channel_inactive_normal.tga",
									"over_image" : ROOT_PATH + "channel_inactive_normal.tga",
									"down_image" : ROOT_PATH + "channel_active_normal.tga",

									"children" :
									(
										{
											"name" : "Channel2Text",
											"type" : "text",

											"x" : 138 / 2,
											"y" : -1,

											"vertical_align" : "center",
											"text_vertical_align" : "center",
											"text_horizontal_align" : "center",

											"text" : uiScriptLocale.ACCOUNT_CHANNEL % 2,
											"fontname" : "Tahoma:14",
										},
									),
								},
							),
						},
						{
							"name" : "ShadowFix3",
							"type" : "window",

							"x" : 0,
							"y" : 35 * 2,

							"width" : 114,
							"height" : 26,

							"children" :
							(
								{
									"name" : "Channel3",
									"type" : "radio_button",

									"x" : -12,
									"y" : -12,

									"default_image" : ROOT_PATH + "channel_inactive_normal.tga",
									"over_image" : ROOT_PATH + "channel_inactive_normal.tga",
									"down_image" : ROOT_PATH + "channel_active_normal.tga",

									"children" :
									(
										{
											"name" : "Channel3Text",
											"type" : "text",

											"x" : 138 / 2,
											"y" : -1,

											"vertical_align" : "center",
											"text_vertical_align" : "center",
											"text_horizontal_align" : "center",

											"text" : uiScriptLocale.ACCOUNT_CHANNEL % 3,
											"fontname" : "Tahoma:14",
										},
									),
								},
							),
						},
						{
							"name" : "ShadowFix4",
							"type" : "window",

							"x" : 0,
							"y" : 35 * 3,

							"width" : 114,
							"height" : 26,

							"children" :
							(
								{
									"name" : "Channel4",
									"type" : "radio_button",

									"x" : -12,
									"y" : -12,

									"default_image" : ROOT_PATH + "channel_inactive_normal.tga",
									"over_image" : ROOT_PATH + "channel_inactive_normal.tga",
									"down_image" : ROOT_PATH + "channel_active_normal.tga",

									"children" :
									(
										{
											"name" : "Channel4Text",
											"type" : "text",

											"x" : 138 / 2,
											"y" : -1,

											"vertical_align" : "center",
											"text_vertical_align" : "center",
											"text_horizontal_align" : "center",

											"text" : uiScriptLocale.ACCOUNT_CHANNEL % 4,
											"fontname" : "Tahoma:14",
										},
									),
								},
							),
						},
						{
							"name" : "ShadowFix5",
							"type" : "window",

							"x" : 0,
							"y" : 35 * 4,

							"width" : 114,
							"height" : 26,

							"children" :
							(
								{
									"name" : "Channel5",
									"type" : "radio_button",

									"x" : -12,
									"y" : -12,

									"default_image" : ROOT_PATH + "channel_inactive_normal.tga",
									"over_image" : ROOT_PATH + "channel_inactive_normal.tga",
									"down_image" : ROOT_PATH + "channel_active_normal.tga",

									"children" :
									(
										{
											"name" : "Channel5Text",
											"type" : "text",

											"x" : 138 / 2,
											"y" : -1,

											"vertical_align" : "center",
											"text_vertical_align" : "center",
											"text_horizontal_align" : "center",

											"text" : uiScriptLocale.ACCOUNT_CHANNEL % 5,
											"fontname" : "Tahoma:14",
										},
									),
								},
							),
						},
					),
				},


				## ACC BOARD
				{
					"name" : "slot_window",
					"x" : 40,
					"y" : 400 + 100,

					"width": 175 * 4,
					"height":ACCSLOT_HEIGHT*(ACCSLOT_COUNT - 2)+ACCSLOT_SPACE*(ACCSLOT_COUNT-3) + 30  + 76,
					
					"children" : 
					(

						{
							"name" : "acc1",
							"x" : 0,
							"y" : (ACCSLOT_HEIGHT+ACCSLOT_SPACE)*0,
							"width" : 143 + 11,
							"height" : ACCSLOT_HEIGHT,
							"children" : (
								{
									"name" : "CircleFKey1",
									"type" : "image",
									"style" : ["not_pick"],
									"x" : 0,
									"y" : 0,
									"image" : ROOT_PATH + "account_f1.tga",
								},
								{
									"name" : "AccountName1",
									"type" : "text",

									"x" : 45,
									"y" : -1,
									
									"vertical_align" : "center",
									"text_vertical_align" : "center",
									"fontname" : "Tahoma:12",

									"text" : "AccountName",
								},
								{
									"name" : "DeleteButton1",
									"type" : "button",

									"x" : 133,
									"y" : 0,

									"vertical_align" : "center",

									"default_image" : ROOT_PATH + "account_minus_normal.tga",
									"over_image" : ROOT_PATH + "account_minus_hover.tga",
									"down_image" : ROOT_PATH + "account_minus_down.tga",
								},
								{
									"name" : "AddButton1",
									"type" : "button",

									"x" : 133,
									"y" : 0,

									"vertical_align" : "center",

									"default_image" : ROOT_PATH + "account_plus_normal.tga",
									"over_image" : ROOT_PATH + "account_plus_hover.tga",
									"down_image" : ROOT_PATH + "account_plus_down.tga",
								},
							),
						},
						{
							"name" : "acc2",
							"x" : 0,
							"y" : (ACCSLOT_HEIGHT+ACCSLOT_SPACE)*1,
							"width" : 143 + 11,
							"height" : ACCSLOT_HEIGHT,
							"children" : (
								{
									"name" : "CircleFKey2",
									"type" : "image",
									"style" : ["not_pick"],
									"x" : 0,
									"y" : 0,
									"image" : ROOT_PATH + "account_f2.tga",
								},
								{
									"name" : "AccountName2",
									"type" : "text",

									"x" : 45,
									"y" : -1,
									
									"vertical_align" : "center",
									"text_vertical_align" : "center",
									"fontname" : "Tahoma:12",

									"text" : "AccountName",
								},
								{
									"name" : "DeleteButton2",
									"type" : "button",

									"x" : 133,
									"y" : 0,

									"vertical_align" : "center",

									"default_image" : ROOT_PATH + "account_minus_normal.tga",
									"over_image" : ROOT_PATH + "account_minus_hover.tga",
									"down_image" : ROOT_PATH + "account_minus_down.tga",
								},
								{
									"name" : "AddButton2",
									"type" : "button",

									"x" : 133,
									"y" : 0,

									"vertical_align" : "center",

									"default_image" : ROOT_PATH + "account_plus_normal.tga",
									"over_image" : ROOT_PATH + "account_plus_hover.tga",
									"down_image" : ROOT_PATH + "account_plus_down.tga",
								},
							),
						},
						{
							"name" : "acc3",
							"x" : 0,
							"y" : (ACCSLOT_HEIGHT+ACCSLOT_SPACE)*2,
							"width" : 143 + 11,
							"height" : ACCSLOT_HEIGHT,
							"children" : (
								{
									"name" : "CircleFKey3",
									"type" : "image",
									"style" : ["not_pick"],
									"x" : 0,
									"y" : 0,
									"image" : ROOT_PATH + "account_f3.tga",
								},
								{
									"name" : "AccountName3",
									"type" : "text",

									"x" : 45,
									"y" : -1,
									
									"vertical_align" : "center",
									"text_vertical_align" : "center",
									"fontname" : "Tahoma:12",

									"text" : "AccountName",
								},
								{
									"name" : "DeleteButton3",
									"type" : "button",

									"x" : 133,
									"y" : 0,

									"vertical_align" : "center",

									"default_image" : ROOT_PATH + "account_minus_normal.tga",
									"over_image" : ROOT_PATH + "account_minus_hover.tga",
									"down_image" : ROOT_PATH + "account_minus_down.tga",
								},
								{
									"name" : "AddButton3",
									"type" : "button",

									"x" : 133,
									"y" : 0,

									"vertical_align" : "center",

									"default_image" : ROOT_PATH + "account_plus_normal.tga",
									"over_image" : ROOT_PATH + "account_plus_hover.tga",
									"down_image" : ROOT_PATH + "account_plus_down.tga",
								},
							),
						},
						{
							"name" : "acc4",
							"x" : 175,
							"y" : (ACCSLOT_HEIGHT+ACCSLOT_SPACE)*0,
							"width" : 143 + 11,
							"height" : ACCSLOT_HEIGHT,
							"children" : (
								{
									"name" : "CircleFKey4",
									"type" : "image",
									"style" : ["not_pick"],
									"x" : 0,
									"y" : 0,
									"image" : ROOT_PATH + "account_f4.tga",
								},
								{
									"name" : "AccountName4",
									"type" : "text",

									"x" : 45,
									"y" : -1,
									
									"vertical_align" : "center",
									"text_vertical_align" : "center",
									"fontname" : "Tahoma:12",

									"text" : "AccountName",
								},
								{
									"name" : "DeleteButton4",
									"type" : "button",

									"x" : 133,
									"y" : 0,

									"vertical_align" : "center",

									"default_image" : ROOT_PATH + "account_minus_normal.tga",
									"over_image" : ROOT_PATH + "account_minus_hover.tga",
									"down_image" : ROOT_PATH + "account_minus_down.tga",
								},
								{
									"name" : "AddButton4",
									"type" : "button",

									"x" : 133,
									"y" : 0,

									"vertical_align" : "center",

									"default_image" : ROOT_PATH + "account_plus_normal.tga",
									"over_image" : ROOT_PATH + "account_plus_hover.tga",
									"down_image" : ROOT_PATH + "account_plus_down.tga",
								},
							),
						},
						{
							"name" : "acc5",
							"x" : 175,
							"y" : (ACCSLOT_HEIGHT+ACCSLOT_SPACE)*1,
							"width" : 143 + 11,
							"height" : ACCSLOT_HEIGHT,
							"children" : (
								{
									"name" : "CircleFKey5",
									"type" : "image",
									"style" : ["not_pick"],
									"x" : 0,
									"y" : 0,
									"image" : ROOT_PATH + "account_f5.tga",
								},
								{
									"name" : "AccountName5",
									"type" : "text",

									"x" : 45,
									"y" : -1,
									
									"vertical_align" : "center",
									"text_vertical_align" : "center",
									"fontname" : "Tahoma:12",

									"text" : "AccountName",
								},
								{
									"name" : "DeleteButton5",
									"type" : "button",

									"x" : 133,
									"y" : 0,

									"vertical_align" : "center",

									"default_image" : ROOT_PATH + "account_minus_normal.tga",
									"over_image" : ROOT_PATH + "account_minus_hover.tga",
									"down_image" : ROOT_PATH + "account_minus_down.tga",
								},
								{
									"name" : "AddButton5",
									"type" : "button",

									"x" : 133,
									"y" : 0,

									"vertical_align" : "center",

									"default_image" : ROOT_PATH + "account_plus_normal.tga",
									"over_image" : ROOT_PATH + "account_plus_hover.tga",
									"down_image" : ROOT_PATH + "account_plus_down.tga",
								},
							),
						},
						{
							"name" : "acc6",
							"x" : 175,
							"y" : (ACCSLOT_HEIGHT+ACCSLOT_SPACE)*2,
							"width" : 143 + 11,
							"height" : ACCSLOT_HEIGHT,
							"children" : (
								{
									"name" : "CircleFKey6",
									"type" : "image",
									"style" : ["not_pick"],
									"x" : 0,
									"y" : 0,
									"image" : ROOT_PATH + "account_f6.tga",
								},
								{
									"name" : "AccountName6",
									"type" : "text",

									"x" : 45,
									"y" : -1,
									
									"vertical_align" : "center",
									"text_vertical_align" : "center",
									"fontname" : "Tahoma:12",

									"text" : "AccountName",
								},
								{
									"name" : "DeleteButton6",
									"type" : "button",

									"x" : 133,
									"y" : 0,

									"vertical_align" : "center",

									"default_image" : ROOT_PATH + "account_minus_normal.tga",
									"over_image" : ROOT_PATH + "account_minus_hover.tga",
									"down_image" : ROOT_PATH + "account_minus_down.tga",
								},
								{
									"name" : "AddButton6",
									"type" : "button",

									"x" : 133,
									"y" : 0,

									"vertical_align" : "center",

									"default_image" : ROOT_PATH + "account_plus_normal.tga",
									"over_image" : ROOT_PATH + "account_plus_hover.tga",
									"down_image" : ROOT_PATH + "account_plus_down.tga",
								},
							),
						},
						{
							"name" : "acc7",
							"x" : 175 * 2,
							"y" : (ACCSLOT_HEIGHT+ACCSLOT_SPACE)*0,
							"width" : 143 + 11,
							"height" : ACCSLOT_HEIGHT,
							"children" : (
								{
									"name" : "CircleFKey7",
									"type" : "image",
									"style" : ["not_pick"],
									"x" : 0,
									"y" : 0,
									"image" : ROOT_PATH + "account_f7.tga",
								},
								{
									"name" : "AccountName7",
									"type" : "text",

									"x" : 45,
									"y" : -1,
									
									"vertical_align" : "center",
									"text_vertical_align" : "center",
									"fontname" : "Tahoma:12",

									"text" : "AccountName",
								},
								{
									"name" : "DeleteButton7",
									"type" : "button",

									"x" : 133,
									"y" : 0,

									"vertical_align" : "center",

									"default_image" : ROOT_PATH + "account_minus_normal.tga",
									"over_image" : ROOT_PATH + "account_minus_hover.tga",
									"down_image" : ROOT_PATH + "account_minus_down.tga",
								},
								{
									"name" : "AddButton7",
									"type" : "button",

									"x" : 133,
									"y" : 0,

									"vertical_align" : "center",

									"default_image" : ROOT_PATH + "account_plus_normal.tga",
									"over_image" : ROOT_PATH + "account_plus_hover.tga",
									"down_image" : ROOT_PATH + "account_plus_down.tga",
								},
							),
						},
						{
							"name" : "acc8",
							"x" : 175 * 2,
							"y" : (ACCSLOT_HEIGHT+ACCSLOT_SPACE)*1,
							"width" : 143 + 11,
							"height" : ACCSLOT_HEIGHT,
							"children" : (
								{
									"name" : "CircleFKey8",
									"type" : "image",
									"style" : ["not_pick"],
									"x" : 0,
									"y" : 0,
									"image" : ROOT_PATH + "account_f8.tga",
								},
								{
									"name" : "AccountName8",
									"type" : "text",

									"x" : 45,
									"y" : -1,
									
									"vertical_align" : "center",
									"text_vertical_align" : "center",
									"fontname" : "Tahoma:12",

									"text" : "AccountName",
								},
								{
									"name" : "DeleteButton8",
									"type" : "button",

									"x" : 133,
									"y" : 0,

									"vertical_align" : "center",

									"default_image" : ROOT_PATH + "account_minus_normal.tga",
									"over_image" : ROOT_PATH + "account_minus_hover.tga",
									"down_image" : ROOT_PATH + "account_minus_down.tga",
								},
								{
									"name" : "AddButton8",
									"type" : "button",

									"x" : 133,
									"y" : 0,

									"vertical_align" : "center",

									"default_image" : ROOT_PATH + "account_plus_normal.tga",
									"over_image" : ROOT_PATH + "account_plus_hover.tga",
									"down_image" : ROOT_PATH + "account_plus_down.tga",
								},
							),
						},
						{
							"name" : "acc9",
							"x" : 175 * 2,
							"y" : (ACCSLOT_HEIGHT+ACCSLOT_SPACE)*2,
							"width" : 143 + 11,
							"height" : ACCSLOT_HEIGHT,
							"children" : (
								{
									"name" : "CircleFKey9",
									"type" : "image",
									"style" : ["not_pick"],
									"x" : 0,
									"y" : 0,
									"image" : ROOT_PATH + "account_f9.tga",
								},
								{
									"name" : "AccountName9",
									"type" : "text",

									"x" : 45,
									"y" : -1,
									
									"vertical_align" : "center",
									"text_vertical_align" : "center",
									"fontname" : "Tahoma:12",

									"text" : "AccountName",
								},
								{
									"name" : "DeleteButton9",
									"type" : "button",

									"x" : 133,
									"y" : 0,

									"vertical_align" : "center",

									"default_image" : ROOT_PATH + "account_minus_normal.tga",
									"over_image" : ROOT_PATH + "account_minus_hover.tga",
									"down_image" : ROOT_PATH + "account_minus_down.tga",
								},
								{
									"name" : "AddButton9",
									"type" : "button",

									"x" : 133,
									"y" : 0,

									"vertical_align" : "center",

									"default_image" : ROOT_PATH + "account_plus_normal.tga",
									"over_image" : ROOT_PATH + "account_plus_hover.tga",
									"down_image" : ROOT_PATH + "account_plus_down.tga",
								},
							),
						},
					),
				},

				# login btn
				{
					"name" : "ButtonLogin",
					"type" : "button",

					"x" : 100 - 3,
					"y" : 310 - 12 + 85 + 41,

					"default_image" : ROOT_PATH + "login_button_normal.tga",
					"over_image" : ROOT_PATH + "login_button_hover.tga",
					"down_image" : ROOT_PATH + "login_button_down.tga",

					"text" : uiScriptLocale.ACCOUNT_LOGIN,
				},

			),
		},
	),
}