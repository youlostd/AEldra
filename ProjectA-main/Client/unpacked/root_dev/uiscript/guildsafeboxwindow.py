import uiScriptLocale

window = {
	"name" : "GuildSafeboxWindow",

	"x" : 100,
	"y" : 20,

	"style" : ("movable", "float",),

	"width" : 210,
	"height" : 314,

	"children" :
	(
		{
			"name" : "board",
			"type" : "board_with_titlebar",
			"style" : ("attach",),

			"x" : 0,
			"y" : 0,

			"width" : 210,
			"height" : 314,

			"title" : uiScriptLocale.GUILD_SAFE_TITLE,

			"children" :
			(
				## Button
				{
					"name":"Money_Slot",
					"type":"field",

					"x":0,
					"y":24 + 5 + 18 + 4,

					"width" : 130,
					"height" : 18,

					"horizontal_align":"center",
					"vertical_align":"bottom",

					"default_image" : "d:/ymir work/ui/public/parameter_slot_05.sub",
					"over_image" : "d:/ymir work/ui/public/parameter_slot_05.sub",
					"down_image" : "d:/ymir work/ui/public/parameter_slot_05.sub",

					"button_style" : True,

					"children" :
					(
						{
							"name":"Money_Icon",
							"type":"image",

							"x":-18,
							"y":2,

							"image":"d:/ymir work/ui/game/inventory/money_icon.tga",
						},

						{
							"name" : "Money",
							"type" : "text",

							"x" : 3,
							"y" : 3,

							"horizontal_align" : "right",
							"text_horizontal_align" : "right",

							"text" : "123456789",
						},
					),
				},
				{
					"name" : "ExitButton",
					"type" : "button",

					"x" : 0,
					"y" : 24 + 5 - 2,

					"text" : uiScriptLocale.CLOSE,
					"horizontal_align" : "center",
					"vertical_align" : "bottom",

					"default_image" : "d:/ymir work/ui/public/large_button_01.sub",
					"over_image" : "d:/ymir work/ui/public/large_button_02.sub",
					"down_image" : "d:/ymir work/ui/public/large_button_03.sub",
				},
				{
					"name" : "LogButton",
					"type" : "button",

					"x" : (88 + 5 + 24) / 2,
					"y" : 24 + 5,

					"horizontal_align" : "center",
					"vertical_align" : "bottom",

					"default_image" : "d:/ymir work/ui/game/guild/guild_log_1.tga",
					"over_image" : "d:/ymir work/ui/game/guild/guild_log_2.tga",
					"down_image" : "d:/ymir work/ui/game/guild/guild_log_3.tga",

					"tooltip_text" : uiScriptLocale.GUILD_SAFE_LOG_BUTTON,
				},

			),
		},
	),
}
