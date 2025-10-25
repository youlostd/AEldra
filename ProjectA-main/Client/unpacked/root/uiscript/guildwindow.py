import uiScriptLocale
import app

ROOT_PATH = "d:/ymir work/ui/game/guild/"
LOCALE_PATH = uiScriptLocale.GUILD_PATH

if app.ENABLE_SECOND_GUILDRENEWAL_SYSTEM:
	PLUS_WITDH = 80
	window = {
		"name" : "GuildWindow",
		"style" : ("movable", "float",),

		"x" : 0,
		"y" : 0,

		"width" : 376 + PLUS_WITDH,
		"height" : 356+9,

		"children" :
		(
			{
				"name" : "Board",
				"type" : "board_with_titlebar",

				"x" : 0,
				"y" : 0,

				"width" : 376 + PLUS_WITDH,
				"height" : 356+9,

				"title" : uiScriptLocale.GUILD_NAME,

				"padding" : 0,

				"children" :
				(
					## Tab Area
					{
						"name" : "TabControl",
						"type" : "window",

						"x" : 0,
						"y" : 328,

						"width" : 376,
						"height" : 37,

						"children" :
						(
							## Tab
							{
								"name" : "Tab_01",
								"type" : "image",

								"x" : 0,
								"y" : 0,

								"width" : 376,
								"height" : 37,

								"image" : ROOT_PATH+"tab_1_noguildbase.sub",
							},
							{
								"name" : "Tab_02",
								"type" : "image",

								"x" : 0,
								"y" : 0,

								"width" : 376,
								"height" : 37,

								"image" : ROOT_PATH+"tab_2_noguildbase.sub",
							},
							{
								"name" : "Tab_03",
								"type" : "image",

								"x" : 0,
								"y" : 0,

								"width" : 376,
								"height" : 37,

								"image" : ROOT_PATH+"tab_3_noguildbase.sub",
							},
							{
								"name" : "Tab_04",
								"type" : "image",

								"x" : 0,
								"y" : 0,

								"width" : 376,
								"height" : 37,

								"image" : ROOT_PATH+"tab_4_noguildbase.sub",
							},
							{
								"name" : "Tab_05",
								"type" : "image",

								"x" : 0,
								"y" : 0,

								"width" : 376,
								"height" : 37,

								"image" : ROOT_PATH+"tab_5_noguildbase.sub",
							},
							{
								"name" : "Tab_06",
								"type" : "image",

								"x" : 0,
								"y" : 0,

								"width" : 376,
								"height" : 37,

								"image" : ROOT_PATH+"tab_6_noguildbase.sub",
							},
							## RadioButton
							{
								"name" : "Tab_Button_01",
								"type" : "radio_button",

								"x" : 6,
								"y" : 5,

								"width" : 53,
								"height" : 27,
							},
							{
								"name" : "Tab_Button_02",
								"type" : "radio_button",

								"x" : 61,
								"y" : 5,

								"width" : 67,
								"height" : 27,
							},
							{
								"name" : "Tab_Button_03",
								"type" : "radio_button",

								"x" : 130,
								"y" : 5,

								"width" : 60,
								"height" : 27,
							},
							#{
							#	"name" : "Tab_Button_04",
							#	"type" : "radio_button",

							#	"x" : 192,
							#	"y" : 5,

							#	"width" : 60,
							#	"height" : 27,
							#},
							{
								"name" : "Tab_Button_05",
								"type" : "radio_button",

								"x" : 254 - 62,
								"y" : 5,

								"width" : 60,
								"height" : 27,
							},
							{
								"name" : "Tab_Button_06",
								"type" : "radio_button",

								"x" : 316 - 62,
								"y" : 5,

								"width" : 55,
								"height" : 27,
							},
						),
					},
				),
			},
		),
	}
else:
	window = {
		"name" : "GuildWindow",
		"style" : ("movable", "float",),

		"x" : 0,
		"y" : 0,

		"width" : 376,
		"height" : 356,

		"children" :
		(
			{
				"name" : "Board",
				"type" : "board_with_titlebar",

				"x" : 0,
				"y" : 0,

				"width" : 376,
				"height" : 356,

				"title" : uiScriptLocale.GUILD_NAME,

				"children" :
				(
					## Tab Area
					{
						"name" : "TabControl",
						"type" : "window",

						"x" : 0,
						"y" : 328,

						"width" : 376,
						"height" : 37,

						"children" :
						(
							## Tab
							{
								"name" : "Tab_01",
								"type" : "image",

								"x" : 0,
								"y" : 0,

								"width" : 376,
								"height" : 37,

								"image" : LOCALE_PATH+"tab_1.sub",
							},
							{
								"name" : "Tab_02",
								"type" : "image",

								"x" : 0,
								"y" : 0,

								"width" : 376,
								"height" : 37,

								"image" : LOCALE_PATH+"tab_2.sub",
							},
							{
								"name" : "Tab_03",
								"type" : "image",

								"x" : 0,
								"y" : 0,

								"width" : 376,
								"height" : 37,

								"image" : LOCALE_PATH+"tab_3.sub",
							},
							{
								"name" : "Tab_04",
								"type" : "image",

								"x" : 0,
								"y" : 0,

								"width" : 376,
								"height" : 37,

								"image" : LOCALE_PATH+"tab_4.sub",
							},
							{
								"name" : "Tab_05",
								"type" : "image",

								"x" : 0,
								"y" : 0,

								"width" : 376,
								"height" : 37,

								"image" : LOCALE_PATH+"tab_5.sub",
							},
							{
								"name" : "Tab_06",
								"type" : "image",

								"x" : 0,
								"y" : 0,

								"width" : 376,
								"height" : 37,

								"image" : LOCALE_PATH+"tab_6.sub",
							},
							## RadioButton
							{
								"name" : "Tab_Button_01",
								"type" : "radio_button",

								"x" : 6,
								"y" : 5,

								"width" : 53,
								"height" : 27,
							},
							{
								"name" : "Tab_Button_02",
								"type" : "radio_button",

								"x" : 61,
								"y" : 5,

								"width" : 67,
								"height" : 27,
							},
							{
								"name" : "Tab_Button_03",
								"type" : "radio_button",

								"x" : 130,
								"y" : 5,

								"width" : 60,
								"height" : 27,
							},
							{
								"name" : "Tab_Button_04",
								"type" : "radio_button",

								"x" : 192,
								"y" : 5,

								"width" : 60,
								"height" : 27,
							},
							{
								"name" : "Tab_Button_05",
								"type" : "radio_button",

								"x" : 254,
								"y" : 5,

								"width" : 60,
								"height" : 27,
							},
							{
								"name" : "Tab_Button_06",
								"type" : "radio_button",

								"x" : 316,
								"y" : 5,

								"width" : 55,
								"height" : 27,
							},
						),
					},
				),
			},
		),
	}