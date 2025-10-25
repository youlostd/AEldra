import uiScriptLocale

window = {
	"name" : "PickMoneyDialog",

	"x" : 100,
	"y" : 100,

	"style" : ("movable", "float",),

	"width" : 140,
	"height" : 60,

	"children" :
	(
		{
			"name" : "board",
			"type" : "board_with_titlebar",
			"style" : ("attach",),

			"x" : 0,
			"y" : 0,

			"width" : 140,
			"height" : 60,
			"title" : uiScriptLocale.PICK_MONEY_TITLE,

			"children" :
			(

				## Money Slot
				{
					"name" : "money_window",

					"x" : 0,
					"y" : 5,

					"width" : 61,
					"height" : 18,

					"horizontal_align" : "center",

					"children" :
					(
						{
							"name" : "money_slot",
							"type" : "field",

							"x" : 0,
							"y" : 0,

							"width" : 61,
							"height" : 18,

							"children" :
							(
								{
									"name" : "money_value",
									"type" : "editline",

									"x" : 3,
									"y" : 2,

									"width" : 60,
									"height" : 18,

									"input_limit" : 10,
									# "only_number" : 1, # "k"..

									"text" : "1",
								},
								{
									"name" : "max_value",
									"type" : "text",

									"x" : 63,
									"y" : 0,

									"text" : "/ 999999",

									"vertical_align" : "center",
									"text_vertical_align" : "center",
								},
							),
						},
					),
				},

				## Button
				{
					"name" : "accept_button",
					"type" : "button",

					"x" : -6 - 61 / 2,
					"y" : 25,

					"text" : uiScriptLocale.OK,

					"default_image" : "d:/ymir work/ui/public/middle_button_01.sub",
					"over_image" : "d:/ymir work/ui/public/middle_button_02.sub",
					"down_image" : "d:/ymir work/ui/public/middle_button_03.sub",

					"horizontal_align" : "center",
					"vertical_align" : "bottom",
				},
				{
					"name" : "cancel_button",
					"type" : "button",

					"x" : 6 + 61 / 2,
					"y" : 25,

					"text" : uiScriptLocale.CANCEL,

					"default_image" : "d:/ymir work/ui/public/middle_button_01.sub",
					"over_image" : "d:/ymir work/ui/public/middle_button_02.sub",
					"down_image" : "d:/ymir work/ui/public/middle_button_03.sub",

					"horizontal_align" : "center",
					"vertical_align" : "bottom",
				},
			),
		},
	),
}