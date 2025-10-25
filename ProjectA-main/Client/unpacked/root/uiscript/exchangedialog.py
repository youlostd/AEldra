import uiScriptLocale

ROOT = "d:/ymir work/ui/game/exchange/"

window = {
	"name" : "ExchangeDialog",

	"x" : 0,
	"y" : 0,

	"style" : ("movable", "float",),

	"width" : 291,
	"height" : 291,

	"children" :
	(
		{
			"name" : "board",
			"type" : "image",
			"style" : ("attach",),

			"x" : 0,
			"y" : 0,

			"image" : ROOT + "bg_all.tga",

			"width" : 291,
			"height" : 291,

			"padding" : 0,

			"children" :
			(
				## Title
				{
					"name" : "TitleBar",
					"type" : "titlebar",
					"style" : ("attach",),

					"x" : 8,
					"y" : 8,
 
					"width" : 291-16,
					"color" : "gray",

					"children" :
					(
						{ "name":"TitleName", "type":"text", "x":133, "y":3, "text":uiScriptLocale.EXCHANGE_TITLE, "text_horizontal_align":"center" },
					),
				},


				{
					"name" : "Target_Name",
					"type" : "text",

					"x" : 70,
					"y" : 37,

					"text" : "Target",

					"text_horizontal_align" : "center",
				},


				{
					"name" : "Owner_Name",
					"type" : "text",

					"x" : 214,
					"y" : 37,

					"text" : "You",

					"text_horizontal_align" : "center",
				},

				## Owner
				{
					"name" : "Owner",
					"type" : "window",

					"x" : 144+9,
					"y" : 33+25,

					"width" : 130,
					"height" : 130+96,

					"children" :
					(
						{
							"name" : "Owner_Slot",
							"type" : "grid_table",

							"start_index" : 0,

							"x" : 0,
							"y" : 0,

							"x_count" : 4,
							"y_count" : 6,
							"x_step" : 32,
							"y_step" : 32,
							"x_blank" : 0,
							"y_blank" : 0,

							"image" : "d:/ymir work/ui/public/slot_base.sub",
						},
						{
							"name" : "Owner_Money",
							"type" : "button",

							"x" : 0,
							"y" : 102+100,

							#"image" : "d:/ymir work/ui/public/parameter_slot_02.sub",

							"default_image" : "d:/ymir work/ui/public/parameter_slot_02.sub",
							"over_image" : "d:/ymir work/ui/public/parameter_slot_02.sub",
							"down_image" : "d:/ymir work/ui/public/parameter_slot_02.sub",

							"children" :
							(
								{
									"name" : "Owner_Money_Value",
									"type" : "text",

									"x" : 59,
									"y" : 2,

									"text" : "1234567",

									"text_horizontal_align" : "right",
								},
							),
						},
						{
							"name" : "Owner_Accept_Light",
							"type" : "button",

							"x" : 62+2,
							"y" : 101+100+2,

							"default_image" : ROOT + "kugel_gray.tga",
							"over_image" : ROOT + "kugel_gray.tga",
							"down_image" : ROOT + "kugel_green.tga",
						},
						{
							"name" : "Owner_Accept_Button",
							"type" : "toggle_button",

							"x" : 85,
							"y" : 101+100,

							"text" : uiScriptLocale.EXCHANGE_ACCEPT,

							"default_image" : "d:/ymir work/ui/public/small_button_01.sub",
							"over_image" : "d:/ymir work/ui/public/small_button_02.sub",
							"down_image" : "d:/ymir work/ui/public/small_button_03.sub",
						},
					),
				},

				## Target
				{
					"name" : "Target",
					"type" : "window",

					"x" : 10,
					"y" : 33+25,

					"width" : 130,
					"height" : 130+96,

					"children" :
					(
						{
							"name" : "Target_Slot",
							"type" : "grid_table",

							"start_index" : 0,

							"x" : 0,
							"y" : 0,

							"x_count" : 4,
							"y_count" : 6,
							"x_step" : 32,
							"y_step" : 32,
							"x_blank" : 0,
							"y_blank" : 0,

							"image" : "d:/ymir work/ui/public/slot_base.sub",
						},
						{
							"name" : "Target_Money",
							"type" : "image",

							"x" : 0,
							"y" : 102+100,

							"image" : "d:/ymir work/ui/public/parameter_slot_02.sub",

							"children" :
							(
								{
									"name" : "Target_Money_Value",
									"type" : "text",

									"x" : 59,
									"y" : 2,

									"text" : "1234567",

									"text_horizontal_align" : "right",
								},
							),
						},
						{
							"name" : "Target_Accept_Light",
							"type" : "button",

							"x" : 62+2,
							"y" : 101+100+2,

							"default_image" : ROOT + "kugel_gray.tga",
							"over_image" : ROOT + "kugel_gray.tga",
							"down_image" : ROOT + "kugel_green.tga",
						},
					),
				},
			),
		},
	),
}