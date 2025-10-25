import uiScriptLocale

BOARD_WIDTH = 237
BOARD_HEIGHT = 33+42+5+20+(18+7)*3+18+3

SLOT_WIDTH = 40

window = {
	"name" : "PetWindow",

	"x" : 0,
	"y" : 0,

	"style" : ("movable", "float",),

	"width" : BOARD_WIDTH,
	"height" : BOARD_HEIGHT,

	"children" :
	(
		{
			"name" : "board",
			"type" : "board_with_titlebar",

			"x" : 0,
			"y" : 0,

			"width" : BOARD_WIDTH,
			"height" : BOARD_HEIGHT,

			"title" : uiScriptLocale.MOUNT_TITLE,

			"children" :
			(
				{
					"name" : "name_slot",
					"type" : "slotbar",

					"x" : 0,
					"y" : 7,

					"width" : 150,
					"height" : 18,

					"horizontal_align" : "center",

					"children" :
					(
						{
							"name" : "name_text",
							"type" : "text",

							"x" : 0,
							"y" : 0,

							"all_align" : 1,
							"text" : "unknown name",
						},
					),
				},

				## Header
				{ 
					"name":"Status_Header", "type":"window", "x":4, "y":33, "width":0, "height":0, 
					"children" :
					(
						## Lv
						{
							"name":"Status_Lv", "type":"window", "x":0, "y":0, "width":37, "height":42, 
							"children" :
							(
								{ "name":"Level_Header", "type":"image", "x":0, "y":0, "image":uiScriptLocale.WINDOWS_PATH+"label_level.sub" },
								{ "name":"Level_Value", "type":"text", "x":19, "y":19, "fontsize":"LARGE", "text":"999", "r":1.0, "g":1.0, "b":1.0, "a":1.0, "text_horizontal_align":"center" },
							),
						},

						## EXP
						{
							"name":"Status_CurExp", "type":"window", "x":44, "y":0, "width":87, "height":42,
							"children" :
							(
								{ "name":"Exp_Slot", "type":"image", "x":0, "y":0, "image":uiScriptLocale.WINDOWS_PATH+"label_cur_exp.sub" },
								{ "name":"Exp_Value", "type":"text", "x":46, "y":19, "fontsize":"LARGE", "text":"12345678901", "r":1.0, "g":1.0, "b":1.0, "a":1.0, "text_horizontal_align":"center" },									),
						},

						## REXP
						{
							"name":"Status_RestExp", "type":"window", "x":141, "y":0, "width":50, "height":42, 
							"children" :
							(
								{ "name":"RestExp_Slot", "type":"image", "x":0, "y":0, "image":uiScriptLocale.WINDOWS_PATH+"label_last_exp.sub" },
								{ "name":"RestExp_Value", "type":"text", "x":46, "y":19, "fontsize":"LARGE", "text":"12345678901", "r":1.0, "g":1.0, "b":1.0, "a":1.0, "text_horizontal_align":"center" },
							),
						},
					),
				},

			#	{
			#		"name" : "StatMain",
			#		"type" : "text",

			#		"x" : 5,
			#		"y" : 33 + 42 + 5,

			#		"text" : "",
			#	},

				{
					"name" : "StatPoints",
					"type" : "extended_text",

					"x" : 5,
					"y" : 33 + 42 + 5,

					"text" : "",

					"horizontal_align" : "right",
				},
				
				{
					"name" : "Stat1",

					"x" : 5,
					"y" : 33+42+5+20,

					"width" : BOARD_WIDTH - 5 * 2,
					"height" : 18,

					"children" :
					(
						{
							"name" : "Stat1_Text",
							"type" : "text",

							"x" : 0,
							"y" : 0,

							"vertical_align" : "center",
							"text_vertical_align" : "center",

							"text" : uiScriptLocale.MOUNT_STAT1_NAME,
						},
						{
							"name" : "Stat1_Slot",
							"type" : "slotbar",

							"x" : SLOT_WIDTH,
							"y" : 0,

							"width" : SLOT_WIDTH,
							"height" : 18,

							"horizontal_align" : "right",

							"children" :
							(
								{
									"name" : "Stat1_Value",
									"type" : "text",

									"x" : 0,
									"y" : 0,

									"all_align" : 1,
									"text" : "99",
								},
							),
						},
						{
							"name" : "Stat1_PlusBtn",
							"type" : "button",

							"x" : SLOT_WIDTH + 5 + 13,
							"y" : 0,

							"horizontal_align" : "right",
							"vertical_align" : "center",

							"default_image" : "d:/ymir work/ui/game/windows/btn_plus_up.sub",
							"over_image" : "d:/ymir work/ui/game/windows/btn_plus_over.sub",
							"down_image" : "d:/ymir work/ui/game/windows/btn_plus_down.sub",
						},
					),
				},
				{
					"name" : "Stat2",

					"x" : 5,
					"y" : 33+42+5+20+(18+7)*1,

					"width" : BOARD_WIDTH - 5 * 2,
					"height" : 18,

					"children" :
					(
						{
							"name" : "Stat2_Text",
							"type" : "text",

							"x" : 0,
							"y" : 0,

							"vertical_align" : "center",
							"text_vertical_align" : "center",

							"text" : uiScriptLocale.MOUNT_STAT2_NAME,
						},
						{
							"name" : "Stat2_Slot",
							"type" : "slotbar",

							"x" : SLOT_WIDTH,
							"y" : 0,

							"width" : SLOT_WIDTH,
							"height" : 18,

							"horizontal_align" : "right",

							"children" :
							(
								{
									"name" : "Stat2_Value",
									"type" : "text",

									"x" : 0,
									"y" : 0,

									"all_align" : 1,
									"text" : "99",
								},
							),
						},
						{
							"name" : "Stat2_PlusBtn",
							"type" : "button",

							"x" : SLOT_WIDTH + 5 + 13,
							"y" : 0,

							"horizontal_align" : "right",
							"vertical_align" : "center",

							"default_image" : "d:/ymir work/ui/game/windows/btn_plus_up.sub",
							"over_image" : "d:/ymir work/ui/game/windows/btn_plus_over.sub",
							"down_image" : "d:/ymir work/ui/game/windows/btn_plus_down.sub",
						},
					),
				},
				{
					"name" : "Stat3",

					"x" : 5,
					"y" : 33+42+5+20+(18+7)*2,

					"width" : BOARD_WIDTH - 5 * 2,
					"height" : 18,

					"children" :
					(
						{
							"name" : "Stat3_Text",
							"type" : "text",

							"x" : 0,
							"y" : 0,

							"vertical_align" : "center",
							"text_vertical_align" : "center",

							"text" : uiScriptLocale.MOUNT_STAT3_NAME,
						},
						{
							"name" : "Stat3_Slot",
							"type" : "slotbar",

							"x" : SLOT_WIDTH,
							"y" : 0,

							"width" : SLOT_WIDTH,
							"height" : 18,

							"horizontal_align" : "right",

							"children" :
							(
								{
									"name" : "Stat3_Value",
									"type" : "text",

									"x" : 0,
									"y" : 0,

									"all_align" : 1,
									"text" : "99",
								},
							),
						},
						{
							"name" : "Stat3_PlusBtn",
							"type" : "button",

							"x" : SLOT_WIDTH + 5 + 13,
							"y" : 0,

							"horizontal_align" : "right",
							"vertical_align" : "center",

							"default_image" : "d:/ymir work/ui/game/windows/btn_plus_up.sub",
							"over_image" : "d:/ymir work/ui/game/windows/btn_plus_over.sub",
							"down_image" : "d:/ymir work/ui/game/windows/btn_plus_down.sub",
						},
					),
				},
				{
					"name" : "Stat4",

					"x" : 5,
					"y" : 33+42+5+20+(18+7)*3,

					"width" : BOARD_WIDTH - 5 * 2,
					"height" : 18,

					"children" :
					(
						{
							"name" : "Stat4_Text",
							"type" : "text",

							"x" : 0,
							"y" : 0,

							"vertical_align" : "center",
							"text_vertical_align" : "center",

							"text" : uiScriptLocale.MOUNT_STAT4_NAME,
						},
						{
							"name" : "Stat4_Slot",
							"type" : "slotbar",

							"x" : SLOT_WIDTH,
							"y" : 0,

							"width" : SLOT_WIDTH,
							"height" : 18,

							"horizontal_align" : "right",

							"children" :
							(
								{
									"name" : "Stat4_Value",
									"type" : "text",

									"x" : 0,
									"y" : 0,

									"all_align" : 1,
									"text" : "99",
								},
							),
						},
						{
							"name" : "Stat4_PlusBtn",
							"type" : "button",

							"x" : SLOT_WIDTH + 5 + 13,
							"y" : 0,

							"horizontal_align" : "right",
							"vertical_align" : "center",

							"default_image" : "d:/ymir work/ui/game/windows/btn_plus_up.sub",
							"over_image" : "d:/ymir work/ui/game/windows/btn_plus_over.sub",
							"down_image" : "d:/ymir work/ui/game/windows/btn_plus_down.sub",
						},
					),
				},
			),
		},
	),
}