import constInfo

if constInfo.NEW_MINIMAP_UI:
	ROOT = "d:/ymir work/ui/minimap_new/"

	window = {
		"name" : "MiniMap",

		"x" : SCREEN_WIDTH - 136 - 5,
		"y" : 0 + 5,

		"width" : 146,
		"height" : 137,

		"children" :
		(
			## OpenWindow
			{
				"name" : "OpenWindow",
				"type" : "window",

				"x" : 0,
				"y" : 0,

				"width" : 136,
				"height" : 137,

				"children" :
				(
					{
						"name" : "OpenWindowBGI",
						"type" : "image",
						"x" : -26,
						"y" : -16,
						"image" : ROOT + "circle.tga",
					},
					## MiniMapWindow
					{
						"name" : "MiniMapWindow",
						"type" : "window",

						"x" : 4,
						"y" : 5,

						"width" : 128,
						"height" : 128,
					},
					## ScaleUpButton
					{
						"name" : "ScaleUpButton",
						"type" : "button",

						"x" : 105,
						"y" : 104,

						"default_image" : ROOT + "plus_normal.tga",
						"over_image" : ROOT + "plus_hover.tga",
						"down_image" : ROOT + "plus_down.tga",
					},
					## ScaleDownButton
					{
						"name" : "ScaleDownButton",
						"type" : "button",

						"x" : 117,
						"y" : 90,

						"default_image" : ROOT + "minus_normal.tga",
						"over_image" : ROOT + "minus_hover.tga",
						"down_image" : ROOT + "minus_down.tga",
					},
					## MiniMapHideButton
					{
						"name" : "MiniMapHideButton",
						"type" : "button",

						"x" : 105,
						"y" : 15,

						"default_image" : ROOT + "btn_cl_normal.tga",
						"over_image" : ROOT + "btn_cl_hover.tga",
						"down_image" : ROOT + "btn_cl_down.tga",
					},
					## NewBattlepassUI
					# {
					# 	"name" : "BattlepassButton",
					# 	"type" : "button",

					# 	"x" : -5,
					# 	"y" : 98-67,

					# 	"default_image" : ROOT + "btn_q_normal.tga",
					# 	"over_image" : ROOT + "btn_q_hover.tga",
					# 	"down_image" : ROOT + "btn_q_down.tga",
					# },
					## EQ Changer
					{
						"name" : "EQChangerButton",
						"type" : "button",

						"x" : -5,
						"y" : 98-67,

						"default_image" : ROOT + "btn_eq_normal.tga",
						"over_image" : ROOT + "btn_eq_hover.tga",
						"down_image" : ROOT + "btn_eq_down.tga",
					},
					## RuneSystem
					{
						"name" : "RuneSystemButton",
						"type" : "button",

						"x" : -10,
						"y" : 98-42,

						"default_image" : ROOT + "btn_1_normal.tga",
						"over_image" : ROOT + "btn_1_hover.tga",
						"down_image" : ROOT + "btn_1_down.tga",
					},
					## QuestTimer
					{
						"name" : "QuestTimerButton",
						"type" : "button",

						"x" : -5,
						"y" : 98-17,

						"default_image" : ROOT + "btn_t_normal.tga",
						"over_image" : ROOT + "btn_t_hover.tga",
						"down_image" : ROOT + "btn_t_down.tga",
					},
					## AtlasShowButton
					{
						"name" : "AtlasShowButton",
						"type" : "button",

						"x" : 9,
						"y" : 98 + 5,

						"default_image" : ROOT + "btn_m_normal.tga",
						"over_image" : ROOT + "btn_m_hover.tga",
						"down_image" : ROOT + "btn_m_down.tga",
					},
					## ServerInfo
					{
						"name" : "ServerInfo",
						"type" : "text",
					
						"text_horizontal_align" : "center",

						"outline" : 1,

						"x" : 70,
						"y" : 140,

						"text" : "",
					},
					{
						"name" : "TimeBG",
						"type" : "image",
						"x" : 70 - 28,
						"y" : 124,
						"image" : ROOT + "time.tga",
						"children" :
						(
							{
								"name" : "Clock",
								"type" : "text",

								"text_horizontal_align" : "center",

								"outline" : 1,

								"x" : 28,
								"y" : 2,

								"text" : "",
							},
						),
					},
					## PositionInfo
					{
						"name" : "PositionInfo",
						"type" : "text",
					
						"text_horizontal_align" : "center",

						"outline" : 1,

						"x" : 70,
						"y" : 167,

						"text" : "",
					},
					## ObserverCount
					{
						"name" : "ObserverCount",
						"type" : "text",
					
						"text_horizontal_align" : "center",

						"outline" : 1,

						"x" : 70,
						"y" : 180,

						"text" : "",
					},
				),
			},
			{
				"name" : "fpsBox",
				"type" : "window",
				"width" : 40,
				"height" : 20,
				"x" : -100,
				"y" : -8,
				"horizontal_align" : "right",
				"horizontal_align" : "top",
				"children" :
				(
					{
						"name" : "fps",
						"type" : "text",
						"x" : 0,
						"y" : 0,
						"all_align" : "center",
						"text" : "",
						"color" : 0xffffffff,
						"outline" : 1,
					},
				),
			},
			{
				"name" : "CloseWindow",
				"type" : "window",

				"x" : 0,
				"y" : 0,

				"width" : 132,
				"height" : 48,

				"children" :
				(
					## ShowButton
					{
						"name" : "MiniMapShowButton",
						"type" : "button",

						"x" : 100,
						"y" : 4,

						"default_image" : "d:/ymir work/ui/minimap/minimap_open_default.sub",
						"over_image" : "d:/ymir work/ui/minimap/minimap_open_default.sub",
						"down_image" : "d:/ymir work/ui/minimap/minimap_open_default.sub",
					},
				),
			},
		),
	}
else:
	ROOT = "d:/ymir work/ui/minimap/"

	window = {
		"name" : "MiniMap",

		"x" : SCREEN_WIDTH - 136,
		"y" : 0,

		"width" : 146,
		"height" : 137,

		"children" :
		(
			## OpenWindow
			{
				"name" : "OpenWindow",
				"type" : "window",

				"x" : 0,
				"y" : 0,

				"width" : 136,
				"height" : 137,

				"children" :
				(
					{
						"name" : "OpenWindowBGI",
						"type" : "image",
						"x" : 0,
						"y" : 0,
						"image" : ROOT + "minimap.sub",
					},
					## MiniMapWindow
					{
						"name" : "MiniMapWindow",
						"type" : "window",

						"x" : 4,
						"y" : 5,

						"width" : 128,
						"height" : 128,
					},
					## ScaleUpButton
					{
						"name" : "ScaleUpButton",
						"type" : "button",

						"x" : 101,
						"y" : 116,

						"default_image" : ROOT + "minimap_scaleup_default.sub",
						"over_image" : ROOT + "minimap_scaleup_over.sub",
						"down_image" : ROOT + "minimap_scaleup_down.sub",
					},
					## ScaleDownButton
					{
						"name" : "ScaleDownButton",
						"type" : "button",

						"x" : 115,
						"y" : 103,

						"default_image" : ROOT + "minimap_scaledown_default.sub",
						"over_image" : ROOT + "minimap_scaledown_over.sub",
						"down_image" : ROOT + "minimap_scaledown_down.sub",
					},
					## MiniMapHideButton
					{
						"name" : "MiniMapHideButton",
						"type" : "button",

						"x" : 111,
						"y" : 6,

						"default_image" : ROOT + "minimap_close_default.sub",
						"over_image" : ROOT + "minimap_close_over.sub",
						"down_image" : ROOT + "minimap_close_down.sub",
					},
					## AtlasShowButton
					{
						"name" : "AtlasShowButton",
						"type" : "button",

						"x" : -7,
						"y" : 60,

						"default_image" : ROOT + "atlas_open_default.sub",
						"over_image" : ROOT + "atlas_open_over.sub",
						"down_image" : ROOT + "atlas_open_down.sub",
					},
					## ServerInfo
					{
						"name" : "ServerInfo",
						"type" : "text",
					
						"text_horizontal_align" : "center",

						"outline" : 1,

						"x" : 70,
						"y" : 140,

						"text" : "",
					},
					{
						"name" : "Clock",
						"type" : "text",
					
						"text_horizontal_align" : "center",

						"outline" : 1,

						"x" : 70,
						"y" : 153,

						"text" : "",
					},
					## PositionInfo
					{
						"name" : "PositionInfo",
						"type" : "text",
					
						"text_horizontal_align" : "center",

						"outline" : 1,

						"x" : 70,
						"y" : 160,

						"text" : "",
					},
					## ObserverCount
					{
						"name" : "ObserverCount",
						"type" : "text",
					
						"text_horizontal_align" : "center",

						"outline" : 1,

						"x" : 70,
						"y" : 180,

						"text" : "",
					},
				),
			},
			{
				"name" : "fpsBox",
				"type" : "window",
				"width" : 40,
				"height" : 20,
				"x" : -40,
				"y" : 3,
				"horizontal_align" : "right",
				"horizontal_align" : "top",
				"children" :
				(
					{
						"name" : "fps",
						"type" : "text",
						"x" : 0,
						"y" : 0,
						"all_align" : "center",
						"text" : "",
						"color" : 0xffffffff,
						"outline" : 1,
					},
				),
			},
			{
				"name" : "CloseWindow",
				"type" : "window",

				"x" : 0,
				"y" : 0,

				"width" : 132,
				"height" : 48,

				"children" :
				(
					## ShowButton
					{
						"name" : "MiniMapShowButton",
						"type" : "button",

						"x" : 100,
						"y" : 4,

						"default_image" : ROOT + "minimap_open_default.sub",
						"over_image" : ROOT + "minimap_open_default.sub",
						"down_image" : ROOT + "minimap_open_default.sub",
					},
				),
			},
		),
	}

import app
if app.COMBAT_ZONE:
	window["children"][0]["children"] += ({
					"name" : "BattleButton",
					"type" : "button",

					"x" : 119,
					"y" : 40,

					"default_image" : ROOT + "btn_B1_normal.tga",
					"over_image" : ROOT + "btn_B_hover.tga",
					"down_image" : ROOT + "btn_B1_down.tga",
				},)
