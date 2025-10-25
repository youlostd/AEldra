import uiScriptLocale
import player
import app

EQUIPMENT_START_INDEX = player.EQUIPMENT_SLOT_START

if app.GetSelectedDesignName() == "pro":
	SMIDDLE_NAME = "tab_button_small_%s.sub"
else:
	SMIDDLE_NAME = "tab_button_smiddle_%s.sub"

SMALL_NAME = "tab_button_small_%s.sub" if __SERVER__ == 1 else "tab_button_smiddle_%s.sub"

window = {
	"name" : "InventoryWindow",

	## 600 - (width + ���������� ���� ���� 24 px)
	"x" : SCREEN_WIDTH - (162 + BOARD_PADDING_LEFT + BOARD_PADDING_RIGHT) - 20,
	"y" : SCREEN_HEIGHT - 37 - (30 + BOARD_PADDING_TOP + BOARD_PADDING_BOTTOM) + 10 - (530 + BOARD_PADDING_TOP + BOARD_PADDING_BOTTOM) + 5,

	"style" : ("movable", "float",),

	"width" : 162,
	"height" : 530,

	"children" :
	(
		{
			"name" : "board",
			"type" : "board",
			"style" : ("attach",),

			"x" : 0,
			"y" : 0,

			"width" : 162,
			"height" : 530,

			"children" :
			(
				## Title
				{
					"name" : "TitleBar",
					"type" : "titlebar",
					"style" : ("attach",),

					"x" : 0,
					"y" : 0,

					"width" : 161,
					"color" : "yellow",

					"children" :
					(
						{ "name":"TitleName", "type":"text", "x":0, "horizontal_align":"center","text_horizontal_align":"center", "y":3, "text":uiScriptLocale.INVENTORY_TITLE, "text_horizontal_align":"center" },
					),
				},

				## Equipment Slot
				{
					"name" : "Equipment_Base",
					"type" : "image",

					"x" : 2,
					"y" : 26,

					"image" : "d:/ymir work/ui/%s.tga" % ("equipment_bg_new" if __SERVER__ == 1 else "equipment_bg_new2"),

					"children" :
					(

						{
							"name" : "EquipmentSlot",
							"type" : "slot",

							"x" : 0,
							"y" : 0,

							"width" : 155,
							"height" : 187,

							"slot" : (
										{"index":EQUIPMENT_START_INDEX+0, "x":41, "y":36, "width":32, "height":64},
										{"index":EQUIPMENT_START_INDEX+1, "x":41, "y":4, "width":32, "height":32},
										{"index":EQUIPMENT_START_INDEX+2, "x":41, "y":147, "width":32, "height":32},
										{"index":EQUIPMENT_START_INDEX+3, "x":77, "y":68, "width":32, "height":32},
										{"index":EQUIPMENT_START_INDEX+4, "x":5, "y":4, "width":32, "height":96},
										{"index":EQUIPMENT_START_INDEX+5, "x":117, "y":68, "width":32, "height":32},
										{"index":EQUIPMENT_START_INDEX+6, "x":117, "y":36, "width":32, "height":32},
										{"index":EQUIPMENT_START_INDEX+7, "x":5, "y":147, "width":32, "height":32},
										{"index":EQUIPMENT_START_INDEX+8, "x":77, "y":147, "width":32, "height":32},
										{"index":EQUIPMENT_START_INDEX+9, "x":117, "y":4, "width":32, "height":32},
										{"index":EQUIPMENT_START_INDEX+10, "x":77, "y":36, "width":32, "height":32},
										{"index":EQUIPMENT_START_INDEX+24, "x":78, "y":4, "width":32, "height":32},
										{"index":EQUIPMENT_START_INDEX+25, "x":41, "y":108, "width":32, "height":32},
										{"index":EQUIPMENT_START_INDEX+28, "x":5, "y":108, "width":32, "height":32},
									) 
									if __SERVER__ == 1 else
									(
										{"index":EQUIPMENT_START_INDEX+0, "x":41, "y":36, "width":32, "height":64},
										{"index":EQUIPMENT_START_INDEX+1, "x":41, "y":4, "width":32, "height":32},
										{"index":EQUIPMENT_START_INDEX+2, "x":41, "y":147, "width":32, "height":32},
										{"index":EQUIPMENT_START_INDEX+3, "x":77, "y":68, "width":32, "height":32},
										{"index":EQUIPMENT_START_INDEX+4, "x":5, "y":4, "width":32, "height":96},
										{"index":EQUIPMENT_START_INDEX+5, "x":117, "y":68, "width":32, "height":32},
										{"index":EQUIPMENT_START_INDEX+6, "x":117, "y":36, "width":32, "height":32},
										{"index":EQUIPMENT_START_INDEX+7, "x":5, "y":147, "width":32, "height":32},
										{"index":EQUIPMENT_START_INDEX+8, "x":77, "y":147, "width":32, "height":32},
										{"index":EQUIPMENT_START_INDEX+9, "x":117, "y":4, "width":32, "height":32},
										{"index":EQUIPMENT_START_INDEX+10, "x":77, "y":36, "width":32, "height":32},
										{"index":EQUIPMENT_START_INDEX+24, "x":78, "y":4, "width":32, "height":32},
										{"index":EQUIPMENT_START_INDEX+25, "x":41, "y":108, "width":32, "height":32},
										# {"index":EQUIPMENT_START_INDEX+28, "x":5, "y":108, "width":32, "height":32},
									) 
									,
						},
						## ShopButton
						{
							"name" : "ShopButton",
							"type" : "button",
							
							"x" : 117,
							"y" : 109,
							
							"tooltip_text" : uiScriptLocale.SHOP_TITLE,
							
							"default_image" : "d:/ymir work/ui/shop_button_01.tga",
							"over_image" : "d:/ymir work/ui/shop_button_02.tga",
							"down_image" : "d:/ymir work/ui/shop_button_03.tga",
						},
						## CostumeButton
						{
							"name" : "CostumeButton",
							"type" : "button",
							
							"x" : 117,
							"y" : 148,
							
							"tooltip_text" : uiScriptLocale.COSTUME_TITLE,
							
							"default_image" : "d:/ymir work/ui/game/taskbar/costume_Button_01.tga",
							"over_image" : "d:/ymir work/ui/game/taskbar/costume_Button_02.tga",
							"down_image" : "d:/ymir work/ui/game/taskbar/costume_Button_03.tga",
						},

						## DSS Button
						{
							"name" : "DragonSoulButton",
							"type" : "button",

							"x" : 74,
							"y" : 107,

							"tooltip_text" : uiScriptLocale.DRAGONSOUL_TITLE,
							
							"default_image" : "d:/ymir work/ui/dragonsoul/dss_inventory_button_01.tga",
							"over_image" : "d:/ymir work/ui/dragonsoul/dss_inventory_button_02.tga",
							"down_image" : "d:/ymir work/ui/dragonsoul/dss_inventory_button_03.tga",
						},

						{
							"name" : "Equipment_Tab_01",
							"type" : "radio_button",

							"x" : 86,
							"y" : 161,

							"default_image" : "d:/ymir work/ui/game/windows/" + (SMIDDLE_NAME % "01"),
							"over_image" : "d:/ymir work/ui/game/windows/" + (SMIDDLE_NAME % "02"),
							"down_image" : "d:/ymir work/ui/game/windows/" + (SMIDDLE_NAME % "03"),

							"children" :
							(
								{
									"name" : "Equipment_Tab_01_Print",
									"type" : "text",

									"x" : 0,
									"y" : 0,

									"all_align" : "center",

									"text" : "I",
								},
							),
						},
						{
							"name" : "Equipment_Tab_02",
							"type" : "radio_button",

							"x" : 86 + 32,
							"y" : 161,

							"default_image" : "d:/ymir work/ui/game/windows/" + (SMIDDLE_NAME % "01"),
							"over_image" : "d:/ymir work/ui/game/windows/" + (SMIDDLE_NAME % "02"),
							"down_image" : "d:/ymir work/ui/game/windows/" + (SMIDDLE_NAME % "03"),

							"children" :
							(
								{
									"name" : "Equipment_Tab_02_Print",
									"type" : "text",

									"x" : 0,
									"y" : 0,

									"all_align" : "center",

									"text" : "II",
								},
							),
						},

					),
				},

				{
					"name" : "Inventory_Tab_01",
					"type" : "radio_button",

					"x" : 0,
					"y" : 26 + 191,

					"default_image" : "d:/ymir work/ui/game/windows/" + (SMALL_NAME % "01"),
					"over_image" : "d:/ymir work/ui/game/windows/" + (SMALL_NAME % "02"),
					"down_image" : "d:/ymir work/ui/game/windows/" + (SMALL_NAME % "03"),
					"tooltip_text" : uiScriptLocale.INVENTORY_PAGE_BUTTON_TOOLTIP % 1,

					"children" :
					(
						{
							"name" : "Inventory_Tab_01_Print",
							"type" : "text",

							"x" : 0,
							"y" : 0,

							"all_align" : "center",

							"text" : "I",
						},
					),
				},
				{
					"name" : "Inventory_Tab_02",
					"type" : "radio_button",

					"x" : 0 + 32,
					"y" : 26 + 191,

					"default_image" : "d:/ymir work/ui/game/windows/" + (SMALL_NAME % "01"),
					"over_image" : "d:/ymir work/ui/game/windows/" + (SMALL_NAME % "02"),
					"down_image" : "d:/ymir work/ui/game/windows/" + (SMALL_NAME % "03"),
					"tooltip_text" : uiScriptLocale.INVENTORY_PAGE_BUTTON_TOOLTIP % 2,

					"children" :
					(
						{
							"name" : "Inventory_Tab_02_Print",
							"type" : "text",

							"x" : 0,
							"y" : 0,

							"all_align" : "center",

							"text" : "II",
						},
					),
				},
				{
					"name" : "Inventory_Tab_03",
					"type" : "radio_button",

					"x" : 0 + 32 * 2,
					"y" : 26 + 191,

					"default_image" : "d:/ymir work/ui/game/windows/" + (SMALL_NAME % "01"),
					"over_image" : "d:/ymir work/ui/game/windows/" + (SMALL_NAME % "02"),
					"down_image" : "d:/ymir work/ui/game/windows/" + (SMALL_NAME % "03"),
					"tooltip_text" : uiScriptLocale.INVENTORY_PAGE_BUTTON_TOOLTIP % 3,

					"children" :
					(
						{
							"name" : "Inventory_Tab_03_Print",
							"type" : "text",

							"x" : 0,
							"y" : 0,

							"all_align" : "center",

							"text" : "III",
						},
					),
				},
				{
					"name" : "Inventory_Tab_04",
					"type" : "radio_button",

					"x" : 0 + 32 * 3,
					"y" : 26 + 191,

					"default_image" : "d:/ymir work/ui/game/windows/" + (SMALL_NAME % "01"),
					"over_image" : "d:/ymir work/ui/game/windows/" + (SMALL_NAME % "02"),
					"down_image" : "d:/ymir work/ui/game/windows/" + (SMALL_NAME % "03"),
					"tooltip_text" : uiScriptLocale.INVENTORY_PAGE_BUTTON_TOOLTIP % 4,

					"children" :
					(
						{
							"name" : "Inventory_Tab_04_Print",
							"type" : "text",

							"x" : 0,
							"y" : 0,

							"all_align" : "center",

							"text" : "IV",
						},
					),
				},
				{
					"name" : "Inventory_Tab_05",
					"type" : "radio_button",

					"x" : 0 + 32 * 4,
					"y" : 26 + 191,

					"default_image" : "d:/ymir work/ui/game/windows/" + (SMALL_NAME % "01"),
					"over_image" : "d:/ymir work/ui/game/windows/" + (SMALL_NAME % "02"),
					"down_image" : "d:/ymir work/ui/game/windows/" + (SMALL_NAME % "03"),
					"tooltip_text" : uiScriptLocale.INVENTORY_PAGE_BUTTON_TOOLTIP % 5,

					"children" :
					(
						{
							"name" : "Inventory_Tab_05_Print",
							"type" : "text",

							"x" : 0,
							"y" : 0,

							"all_align" : "center",

							"text" : "V",
						},
					),
				},

				## Item Slot
				{
					"name" : "ItemSlot",
					"type" : "grid_table",

					"x" : 0,
					"y" : 239,

					"start_index" : 0,
					"x_count" : 5,
					"y_count" : 9,
					"x_step" : 32,
					"y_step" : 32,

					"image" : "d:/ymir work/ui/public/Slot_Base.sub",

					"children" :
					(
						{
							"name" : "ItemSlotDisable1",
							"type" : "image",

							"x" : 0,
							"y" : 32 * 0,

							"image" : "d:/ymir work/ui/game/inventory/row_disabled.tga",
						},
						{
							"name" : "ItemSlotDisable2",
							"type" : "image",

							"x" : 0,
							"y" : 32 * 1,

							"image" : "d:/ymir work/ui/game/inventory/row_disabled.tga",
						},
						{
							"name" : "ItemSlotDisable3",
							"type" : "image",

							"x" : 0,
							"y" : 32 * 2,

							"image" : "d:/ymir work/ui/game/inventory/row_disabled.tga",
						},
						{
							"name" : "ItemSlotDisable4",
							"type" : "image",

							"x" : 0,
							"y" : 32 * 3,

							"image" : "d:/ymir work/ui/game/inventory/row_disabled.tga",
						},
						{
							"name" : "ItemSlotDisable5",
							"type" : "image",

							"x" : 0,
							"y" : 32 * 4,

							"image" : "d:/ymir work/ui/game/inventory/row_disabled.tga",
						},
						{
							"name" : "ItemSlotDisable6",
							"type" : "image",

							"x" : 0,
							"y" : 32 * 5,

							"image" : "d:/ymir work/ui/game/inventory/row_disabled.tga",
						},
						{
							"name" : "ItemSlotDisable7",
							"type" : "image",

							"x" : 0,
							"y" : 32 * 6,

							"image" : "d:/ymir work/ui/game/inventory/row_disabled.tga",
						},
						{
							"name" : "ItemSlotDisable8",
							"type" : "image",

							"x" : 0,
							"y" : 32 * 7,

							"image" : "d:/ymir work/ui/game/inventory/row_disabled.tga",
						},
						{
							"name" : "ItemSlotDisable9",
							"type" : "image",

							"x" : 0,
							"y" : 32 * 8,

							"image" : "d:/ymir work/ui/game/inventory/row_disabled.tga",
						},
					),
				},
			),
		},
	),
}


import constInfo
if constInfo.SORT_AND_STACK_ITEMS:
	window["children"][0]["children"][0]["width"] -= 38
	window["children"][0]["children"][0]["x"] += 38
	window["children"][0]["children"] += (
					{
						"name" : "SeparateBaseImage",
						"type" : "image",
						"style" : ("attach",),

						"x" : 0,
						"y" : 0,

						"image" : "d:/ymir work/ui/pattern/titlebar_inv_refresh_baseframe.tga",

						"children" :
						(
							{
								"name" : "SeparateButton",
								"type" : "button",

								"x" : 11,
								"y" : 3,

								# "tooltip_text" : uiScriptLocale.INVENTORY_SEPARATE,

								"default_image" : "d:/ymir work/ui/game/inventory/refresh_small_button_01.sub",
								"over_image" : "d:/ymir work/ui/game/inventory/refresh_small_button_02.sub",
								"down_image" : "d:/ymir work/ui/game/inventory/refresh_small_button_03.sub",
								"disable_image" : "d:/ymir work/ui/game/inventory/refresh_small_button_04.sub",
							},
						),
					},
					)
