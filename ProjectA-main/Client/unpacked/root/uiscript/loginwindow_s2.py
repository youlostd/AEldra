import uiScriptLocale
ROOT_PATH = "d:/ymir work/ui/game/intro/login_s2/"
ACCSLOT_HEIGHT = 38
ACCSLOT_SPACE = 13
ACCSLOT_COUNT = 8

TOP = 212

SCALE_X = float(SCREEN_WIDTH) / 1920.0
SCALE_Y = float(SCREEN_HEIGHT) / 1080.0

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

			"default_image" : ROOT_PATH + "button_normal.tga",
			"over_image" : ROOT_PATH + "button_hover.tga",
			"down_image" : ROOT_PATH + "button_down.tga",
			
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


		## LOGIN_WINDOW
		{
			"name" : "LoginBoard",
			"type" : "image",


			"horizontal_align" : "center",
			"vertical_align" : "center",
			
			
			"x" : 0,
			"y" : 0,
			"image" : ROOT_PATH + "login_bg.tga",

			"children" :
			(
				{
					"name" : "LabelRegisterClick",
					"type" : "text",

					"x" : 244-75,
					"y" : 613+26+30-TOP,

					"text" : uiScriptLocale.ACCOUNT_REGISTER,
					"fontname" : "Tahoma:15",
					"color" : 0xFFd8910a,
					# "text_horizontal_align" : "right",
				},
				
				{
					"name" : "LabelPasswordForgot",
					"type" : "text",

					"x" : 480-70,
					"y" : 613+26+30-TOP,

					"text" : uiScriptLocale.ACCOUNT_PASSWORD_Q,
					"fontname" : "Tahoma:15",
					"color" : 0xFF00ff3f,
				},
				# Normal Login
				{

					"name" : "normal_login",
					"x" : 227-70,
					"y" : 440-TOP,
					"width" : 234 + 50,
					"height" : 65 + 24 + 38,
					"children" : (
						{
							"name" : "LabelAccountID",
							"type" : "text",

							"x" : 12,
							"y" : 0 + 38+10,

							"fontname" : "Tahoma:16",
							"text" : uiScriptLocale.ACCOUNT_USERNAME_LABEL,
						},


						{
							"name" : "EditAccountID_Image",
							"type" : "image",

							"x" : 0,
							"y" : 24 + 38,

							"image" : ROOT_PATH + "textbox.tga",

							"children" :
							(
								{
									"name" : "EditAccountID",
									"type" : "editline",

									"vertical_align":"center",
									"x" : 20,
									"y" : 2,

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

							"x" : 12,
							"y" : 65 + 38+10,

							"fontname" : "Tahoma:16",
							"text" : uiScriptLocale.ACCOUNT_PASSWORD_LABEL,
						},
						{
							"name" : "EditPasswordID_Image",
							"type" : "image",

							"x" : 0,
							"y" : 65 + 24 + 38,

							"image" : ROOT_PATH + "textbox.tga",

							"children" :
							(
								{
									"name" : "EditPasswordID",
									"type" : "editline",

									"vertical_align":"center",
									"x" : 20,
									"y" : 2,

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
					"x" : 222-50,
					"y" : 747-TOP,
					"width" : 400,
					"height" : 29,
					"children" :
					(

						{
							"name" : "ShadowFix1",
							"type" : "window",

							"x" : 0,
							"y" : 0,

							"width" : 100,
							"height" : 29,

							"children" :
							(
								{
									"name" : "Channel1",
									"type" : "radio_button",

									"x" :0,
									"y" :0,

									"default_image" : ROOT_PATH + "channel_inactive.tga",
									"over_image" : ROOT_PATH + "channel_inactive.tga",
									"down_image" : ROOT_PATH + "channel_active.tga",

								},
								{
									"name" : "Channel1Text",
									"type" : "text",

									"x" : 55,
									"y" : 0,

									"vertical_align" : "center",
									"text_vertical_align" : "center",
									"text_horizontal_align" : "center",

									"text" : uiScriptLocale.ACCOUNT_CHANNEL % 1,
									"fontname" : "Tahoma:14",
								},
							),
						},
						{
							"name" : "ShadowFix2",
							"type" : "window",

							"x" : 100,
							"y" : 0,

							"width" : 100,
							"height" : 29,

							"children" :
							(
								{
									"name" : "Channel2",
									"type" : "radio_button",

									"x" :0,
									"y" :0,

									"default_image" : ROOT_PATH + "channel_inactive.tga",
									"over_image" : ROOT_PATH + "channel_inactive.tga",
									"down_image" : ROOT_PATH + "channel_active.tga",

								},
								{
									"name" : "Channel2Text",
									"type" : "text",

									"x" : 55,
									"y" : 0,

									"vertical_align" : "center",
									"text_vertical_align" : "center",
									"text_horizontal_align" : "center",

									"text" : uiScriptLocale.ACCOUNT_CHANNEL % 2,
									"fontname" : "Tahoma:14",
								},
							),
						},
						{
							"name" : "ShadowFix3",
							"type" : "window",

							"x" : 100*2,
							"y" : 0,

							"width" : 100,
							"height" : 29,

							"children" :
							(
								{
									"name" : "Channel3",
									"type" : "radio_button",

									"x" :0,
									"y" :0,

									"default_image" : ROOT_PATH + "channel_inactive.tga",
									"over_image" : ROOT_PATH + "channel_inactive.tga",
									"down_image" : ROOT_PATH + "channel_active.tga",

								},
								{
									"name" : "Channel3Text",
									"type" : "text",

									"x" : 55,
									"y" : 0,

									"vertical_align" : "center",
									"text_vertical_align" : "center",
									"text_horizontal_align" : "center",

									"text" : uiScriptLocale.ACCOUNT_CHANNEL % 3,
									"fontname" : "Tahoma:14",
								},
							),
						},
						{
							"name" : "ShadowFix4",
							"type" : "window",

							"x" : 100*3,
							"y" : 0,

							"width" : 100,
							"height" : 29,

							"children" :
							(
								{
									"name" : "Channel4",
									"type" : "radio_button",

									"x" :0,
									"y" :0,

									"default_image" : ROOT_PATH + "channel_inactive.tga",
									"over_image" : ROOT_PATH + "channel_inactive.tga",
									"down_image" : ROOT_PATH + "channel_active.tga",

								},
								{
									"name" : "Channel4Text",
									"type" : "text",

									"x" : 55,
									"y" : 0,

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


				## ACC BOARD
				{
					"name" : "slot_window",
					"x" : 610-100,
					"y" : 400 + 85 - TOP,

					"width": 175 * 4,
					"height":ACCSLOT_HEIGHT*(ACCSLOT_COUNT - 2)+ACCSLOT_SPACE*(ACCSLOT_COUNT-3) + 30  + 76,
					
					"children" : 
					(
						##### COL 1
						{
							"name" : "acc1",
							"x" : 0,
							"y" : (ACCSLOT_HEIGHT+ACCSLOT_SPACE)*0,
							"width" : 155,
							"height" : ACCSLOT_HEIGHT-4,
							"children" : (
								{
									"name" : "account_slot",
									"type" : "image",
									"style" : ["not_pick"],
									"x" : 6, "y" : 6,
									"image" : ROOT_PATH + "account_slot.tga",
									"children" : 
									(
										{
											"name" : "CircleFKey1",
											"type" : "image",
											"style" : ["not_pick"],
											"vertical_align" : "center",
											"x" : 4,
											"y" : 0,
											"image" : ROOT_PATH + "account_f1.tga",
										},
										{
											"name" : "AccountName1",
											"type" : "text",
											"style" : ["not_pick"],

											"x" : 42,
											"y" : -1,
											
											"vertical_align" : "center",
											"text_vertical_align" : "center",
											"fontname" : "Tahoma:12",

											"text" : "AccountName",
										},
									),
								},
								{
									"name" : "DeleteButton1",
									"type" : "button",
									"vertical_align" : "center",
									"x" : 133+5,
									"y" : 7,

									"default_image" : ROOT_PATH + "account_minus_normal.tga",
									"over_image" : ROOT_PATH + "account_minus_hover.tga",
									"down_image" : ROOT_PATH + "account_minus_down.tga",
								},
								{
									"name" : "AddButton1",
									"type" : "button",
									"vertical_align" : "center",
									"x" : 133+5,
									"y" : 7,

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
							"width" : 155,
							"height" : ACCSLOT_HEIGHT-4,
							"children" : (
								{
									"name" : "account_slot",
									"type" : "image",
									"style" : ["not_pick"],
									"x" : 6, "y" : 6,
									"image" : ROOT_PATH + "account_slot.tga",
									"children" : 
									(
										{
											"name" : "CircleFKey2",
											"type" : "image",
											"style" : ["not_pick"],
											"vertical_align" : "center",
											"x" : 4,
											"y" : 0,
											"image" : ROOT_PATH + "account_f2.tga",
										},
										{
											"name" : "AccountName2",
											"type" : "text",
											"style" : ["not_pick"],

											"x" : 42,
											"y" : -1,
											
											"vertical_align" : "center",
											"text_vertical_align" : "center",
											"fontname" : "Tahoma:12",

											"text" : "AccountName",
										},
									),
								},
								{
									"name" : "DeleteButton2",
									"type" : "button",
									"vertical_align" : "center",
									"x" : 133+5,
									"y" : 7,

									"default_image" : ROOT_PATH + "account_minus_normal.tga",
									"over_image" : ROOT_PATH + "account_minus_hover.tga",
									"down_image" : ROOT_PATH + "account_minus_down.tga",
								},
								{
									"name" : "AddButton2",
									"type" : "button",
									"vertical_align" : "center",
									"x" : 133+5,
									"y" : 7,

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
							"width" : 155,
							"height" : ACCSLOT_HEIGHT-4,
							"children" : (
								{
									"name" : "account_slot",
									"type" : "image",
									"style" : ["not_pick"],
									"x" : 6, "y" : 6,
									"image" : ROOT_PATH + "account_slot.tga",
									"children" : 
									(
										{
											"name" : "CircleFKey3",
											"type" : "image",
											"style" : ["not_pick"],
											"vertical_align" : "center",
											"x" : 4,
											"y" : 0,
											"image" : ROOT_PATH + "account_f3.tga",
										},
										{
											"name" : "AccountName3",
											"type" : "text",
											"style" : ["not_pick"],

											"x" : 42,
											"y" : -1,
											
											"vertical_align" : "center",
											"text_vertical_align" : "center",
											"fontname" : "Tahoma:12",

											"text" : "AccountName",
										},
									),
								},
								{
									"name" : "DeleteButton3",
									"type" : "button",
									"vertical_align" : "center",
									"x" : 133+5,
									"y" : 7,

									"default_image" : ROOT_PATH + "account_minus_normal.tga",
									"over_image" : ROOT_PATH + "account_minus_hover.tga",
									"down_image" : ROOT_PATH + "account_minus_down.tga",
								},
								{
									"name" : "AddButton3",
									"type" : "button",
									"vertical_align" : "center",
									"x" : 133+5,
									"y" : 7,

									"default_image" : ROOT_PATH + "account_plus_normal.tga",
									"over_image" : ROOT_PATH + "account_plus_hover.tga",
									"down_image" : ROOT_PATH + "account_plus_down.tga",
								},
							),
						},
						{
							"name" : "acc4",
							"x" : 0,
							"y" : (ACCSLOT_HEIGHT+ACCSLOT_SPACE)*3,
							"width" : 155,
							"height" : ACCSLOT_HEIGHT-4,
							"children" : (
								{
									"name" : "account_slot",
									"type" : "image",
									"style" : ["not_pick"],
									"x" : 6, "y" : 6,
									"image" : ROOT_PATH + "account_slot.tga",
									"children" : 
									(
										{
											"name" : "CircleFKey4",
											"type" : "image",
											"style" : ["not_pick"],
											"vertical_align" : "center",
											"x" : 4,
											"y" : 0,
											"image" : ROOT_PATH + "account_f4.tga",
										},
										{
											"name" : "AccountName4",
											"type" : "text",
											"style" : ["not_pick"],

											"x" : 42,
											"y" : -1,
											
											"vertical_align" : "center",
											"text_vertical_align" : "center",
											"fontname" : "Tahoma:12",

											"text" : "AccountName",
										},
									),
								},
								{
									"name" : "DeleteButton4",
									"type" : "button",
									"vertical_align" : "center",
									"x" : 133+5,
									"y" : 7,

									"default_image" : ROOT_PATH + "account_minus_normal.tga",
									"over_image" : ROOT_PATH + "account_minus_hover.tga",
									"down_image" : ROOT_PATH + "account_minus_down.tga",
								},
								{
									"name" : "AddButton4",
									"type" : "button",
									"vertical_align" : "center",
									"x" : 133+5,
									"y" : 7,

									"default_image" : ROOT_PATH + "account_plus_normal.tga",
									"over_image" : ROOT_PATH + "account_plus_hover.tga",
									"down_image" : ROOT_PATH + "account_plus_down.tga",
								},
							),
						},
						##### COL 1 END
						###################
						##### COL 2
						{
							"name" : "acc5",
							"x" : 160,
							"y" : (ACCSLOT_HEIGHT+ACCSLOT_SPACE)*0,
							"width" : 155,
							"height" : ACCSLOT_HEIGHT-4,
							"children" : (
								{
									"name" : "account_slot",
									"type" : "image",
									"style" : ["not_pick"],
									"x" : 6, "y" : 6,
									"image" : ROOT_PATH + "account_slot.tga",
									"children" : 
									(
										{
											"name" : "CircleFKey5",
											"type" : "image",
											"style" : ["not_pick"],
											"vertical_align" : "center",
											"x" : 4,
											"y" : 0,
											"image" : ROOT_PATH + "account_f5.tga",
										},
										{
											"name" : "AccountName5",
											"type" : "text",
											"style" : ["not_pick"],

											"x" : 42,
											"y" : -1,
											
											"vertical_align" : "center",
											"text_vertical_align" : "center",
											"fontname" : "Tahoma:12",

											"text" : "AccountName",
										},
									),
								},
								{
									"name" : "DeleteButton5",
									"type" : "button",
									"vertical_align" : "center",
									"x" : 133+5,
									"y" : 7,

									"default_image" : ROOT_PATH + "account_minus_normal.tga",
									"over_image" : ROOT_PATH + "account_minus_hover.tga",
									"down_image" : ROOT_PATH + "account_minus_down.tga",
								},
								{
									"name" : "AddButton5",
									"type" : "button",
									"vertical_align" : "center",
									"x" : 133+5,
									"y" : 7,

									"default_image" : ROOT_PATH + "account_plus_normal.tga",
									"over_image" : ROOT_PATH + "account_plus_hover.tga",
									"down_image" : ROOT_PATH + "account_plus_down.tga",
								},
							),
						},
						{
							"name" : "acc6",
							"x" : 160,
							"y" : (ACCSLOT_HEIGHT+ACCSLOT_SPACE)*1,
							"width" : 155,
							"height" : ACCSLOT_HEIGHT-4,
							"children" : (
								{
									"name" : "account_slot",
									"type" : "image",
									"style" : ["not_pick"],
									"x" : 6, "y" : 6,
									"image" : ROOT_PATH + "account_slot.tga",
									"children" : 
									(
										{
											"name" : "CircleFKey6",
											"type" : "image",
											"style" : ["not_pick"],
											"vertical_align" : "center",
											"x" : 4,
											"y" : 0,
											"image" : ROOT_PATH + "account_f6.tga",
										},
										{
											"name" : "AccountName6",
											"type" : "text",
											"style" : ["not_pick"],

											"x" : 42,
											"y" : -1,
											
											"vertical_align" : "center",
											"text_vertical_align" : "center",
											"fontname" : "Tahoma:12",

											"text" : "AccountName",
										},
									),
								},
								{
									"name" : "DeleteButton6",
									"type" : "button",
									"vertical_align" : "center",
									"x" : 133+5,
									"y" : 7,

									"default_image" : ROOT_PATH + "account_minus_normal.tga",
									"over_image" : ROOT_PATH + "account_minus_hover.tga",
									"down_image" : ROOT_PATH + "account_minus_down.tga",
								},
								{
									"name" : "AddButton6",
									"type" : "button",
									"vertical_align" : "center",
									"x" : 133+5,
									"y" : 7,

									"default_image" : ROOT_PATH + "account_plus_normal.tga",
									"over_image" : ROOT_PATH + "account_plus_hover.tga",
									"down_image" : ROOT_PATH + "account_plus_down.tga",
								},
							),
						},
						{
							"name" : "acc7",
							"x" : 160,
							"y" : (ACCSLOT_HEIGHT+ACCSLOT_SPACE)*2,
							"width" : 155,
							"height" : ACCSLOT_HEIGHT-4,
							"children" : (
								{
									"name" : "account_slot",
									"type" : "image",
									"style" : ["not_pick"],
									"x" : 6, "y" : 6,
									"image" : ROOT_PATH + "account_slot.tga",
									"children" : 
									(
										{
											"name" : "CircleFKey7",
											"type" : "image",
											"style" : ["not_pick"],
											"vertical_align" : "center",
											"x" : 4,
											"y" : 0,
											"image" : ROOT_PATH + "account_f7.tga",
										},
										{
											"name" : "AccountName7",
											"type" : "text",
											"style" : ["not_pick"],

											"x" : 42,
											"y" : -1,
											
											"vertical_align" : "center",
											"text_vertical_align" : "center",
											"fontname" : "Tahoma:12",

											"text" : "AccountName",
										},
									),
								},
								{
									"name" : "DeleteButton7",
									"type" : "button",
									"vertical_align" : "center",
									"x" : 133+5,
									"y" : 7,

									"default_image" : ROOT_PATH + "account_minus_normal.tga",
									"over_image" : ROOT_PATH + "account_minus_hover.tga",
									"down_image" : ROOT_PATH + "account_minus_down.tga",
								},
								{
									"name" : "AddButton7",
									"type" : "button",
									"vertical_align" : "center",
									"x" : 133+5,
									"y" : 7,

									"default_image" : ROOT_PATH + "account_plus_normal.tga",
									"over_image" : ROOT_PATH + "account_plus_hover.tga",
									"down_image" : ROOT_PATH + "account_plus_down.tga",
								},
							),
						},
						{
							"name" : "acc8",
							"x" : 160,
							"y" : (ACCSLOT_HEIGHT+ACCSLOT_SPACE)*3,
							"width" : 155,
							"height" : ACCSLOT_HEIGHT-4,
							"children" : (
								{
									"name" : "account_slot",
									"type" : "image",
									"style" : ["not_pick"],
									"x" : 6, "y" : 6,
									"image" : ROOT_PATH + "account_slot.tga",
									"children" : 
									(
										{
											"name" : "CircleFKey8",
											"type" : "image",
											"style" : ["not_pick"],
											"vertical_align" : "center",
											"x" : 4,
											"y" : 0,
											"image" : ROOT_PATH + "account_f8.tga",
										},
										{
											"name" : "AccountName8",
											"type" : "text",
											"style" : ["not_pick"],

											"x" : 42,
											"y" : -1,
											
											"vertical_align" : "center",
											"text_vertical_align" : "center",
											"fontname" : "Tahoma:12",

											"text" : "AccountName",
										},
									),
								},
								{
									"name" : "DeleteButton8",
									"type" : "button",
									"vertical_align" : "center",
									"x" : 133+5,
									"y" : 7,

									"default_image" : ROOT_PATH + "account_minus_normal.tga",
									"over_image" : ROOT_PATH + "account_minus_hover.tga",
									"down_image" : ROOT_PATH + "account_minus_normal.tga",
								},
								{
									"name" : "AddButton8",
									"type" : "button",
									"vertical_align" : "center",
									"x" : 133+5,
									"y" : 7,

									"default_image" : ROOT_PATH + "account_plus_normal.tga",
									"over_image" : ROOT_PATH + "account_plus_hover.tga",
									"down_image" : ROOT_PATH + "account_plus_down.tga",
								},
							),
						},


						### COL 2 END

					),
				},

				# login btn
				{
					"name" : "ButtonLogin",
					"type" : "button",

					"x" : 244-86,
					"y" : 613-TOP,

					"default_image" : ROOT_PATH + "login_normal.tga",
					"over_image" : ROOT_PATH + "login_hover.tga",
					"down_image" : ROOT_PATH + "login_normal.tga",

					#"text" : uiScriptLocale.ACCOUNT_LOGIN,
				},

			),
		},
	),
}