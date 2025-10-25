import uiScriptLocale
import safebox

BUTTON_WIDTH = 38
BUTTON_HEIGHT = 39
BUTTON_X_SPACE = 2
BUTTON_Y_SPACE = 2

BUTTON_X_COUNT = 4
BUTTON_Y_COUNT = 2

BUTTON_WND_WIDTH = (BUTTON_WIDTH + BUTTON_X_SPACE) * BUTTON_X_COUNT - BUTTON_X_SPACE
BUTTON_WND_HEIGHT = (BUTTON_HEIGHT + BUTTON_Y_SPACE) * BUTTON_Y_COUNT - BUTTON_Y_SPACE

SLOT_WND_WIDTH = 32 * safebox.SAFEBOX_SLOT_X_COUNT
SLOT_WND_HEIGHT = 32 * safebox.SAFEBOX_SLOT_Y_COUNT

PAGE_BTN_HEIGHT = 20 * 2
PAGE_BTN_SPACE = 6

BOARD_WIDTH = 3 + SLOT_WND_WIDTH + 3
BOARD_HEIGHT = 3 + SLOT_WND_HEIGHT + PAGE_BTN_SPACE + PAGE_BTN_HEIGHT + PAGE_BTN_SPACE + BUTTON_WND_HEIGHT

window = {
	"name" : "SafeboxWindow",

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
			"style" : ("attach",),

			"x" : 0,
			"y" : 0,

			"width" : BOARD_WIDTH,
			"height" : BOARD_HEIGHT,

			"title" : uiScriptLocale.SAFE_TITLE,

			"children" :
			(
				{
					"name" : "slot",
					"type" : "grid_table",

					"x" : 3,
					"y" : 3,

					"start_index" : 0,
					"x_count" : safebox.SAFEBOX_SLOT_X_COUNT,
					"y_count" : safebox.SAFEBOX_SLOT_Y_COUNT,
					"x_step" : 32,
					"y_step" : 32,

					"image" : "d:/ymir work/ui/public/Slot_Base.sub",
				},
				{
					"name" : "slot_loading",
					"type" : "ani_image",

					"x" : (BOARD_WIDTH - 16) / 2,
					"y" : 3 + (SLOT_WND_HEIGHT - 16) / 2,

					"delay" : 6,

					"images" : (
						"d:/ymir work/ui/loading_ani/00.tga",
						"d:/ymir work/ui/loading_ani/01.tga",
						"d:/ymir work/ui/loading_ani/02.tga",
						"d:/ymir work/ui/loading_ani/03.tga",
						"d:/ymir work/ui/loading_ani/04.tga",
						"d:/ymir work/ui/loading_ani/05.tga",
						"d:/ymir work/ui/loading_ani/06.tga",
						"d:/ymir work/ui/loading_ani/07.tga",
					),
				},
				{
					"name" : "page_btn_window",

					"x" : 3,
					"y" : 3 + BUTTON_WND_HEIGHT + PAGE_BTN_SPACE + PAGE_BTN_HEIGHT,

					"width" : BOARD_WIDTH - 3 * 2,
					"height" : PAGE_BTN_HEIGHT,

					"vertical_align" : "bottom",
				},
				{
					"name" : "btn_window",

					"x" : 0,
					"y" : 3 + BUTTON_WND_HEIGHT,

					"width" : BUTTON_WIDTH * BUTTON_X_COUNT + BUTTON_X_SPACE * (BUTTON_X_COUNT - 1),
					"height" : BUTTON_HEIGHT * BUTTON_Y_COUNT + BUTTON_Y_SPACE * (BUTTON_Y_COUNT - 1),

					"horizontal_align" : "center",
					"vertical_align" : "bottom",

					"children" :
					(
						# NORMAL BUTTON
						{
							"name" : "btn_normal",
							"type" : "radio_button",

							"x" : (BUTTON_WIDTH + BUTTON_X_SPACE) * 0,
							"y" : (BUTTON_HEIGHT + BUTTON_Y_SPACE) * 0,
							"tooltip_text" : uiScriptLocale.SAFEBOX_INVENTORY_NORMAL,
							"default_image" : "d:/ymir work/ui/game/safebox/etc_normal.tga",
							"over_image" : "d:/ymir work/ui/game/safebox/etc_hover.tga",
							"down_image" : "d:/ymir work/ui/game/safebox/etc_down.tga",
						},
						# MALL BUTTON
						{
							"name" : "btn_mall",
							"type" : "radio_button",

							"x" : (BUTTON_WIDTH + BUTTON_X_SPACE) * 1,
							"y" : (BUTTON_HEIGHT + BUTTON_Y_SPACE) * 0,
							"tooltip_text" : uiScriptLocale.SAFEBOX_INVENTORY_ITEMSHOP,
							"default_image" : "d:/ymir work/ui/game/safebox/itemshop_normal.tga",
							"over_image" : "d:/ymir work/ui/game/safebox/itemshop_hover.tga",
							"down_image" : "d:/ymir work/ui/game/safebox/itemshop_down.tga",
						},
						# UPP-ITEM BUTTON
						{
							"name" : "btn_upp",
							"type" : "radio_button",

							"x" : (BUTTON_WIDTH + BUTTON_X_SPACE) * 2,
							"y" : (BUTTON_HEIGHT + BUTTON_Y_SPACE) * 0,
							"tooltip_text" : uiScriptLocale.SAFEBOX_INVENTORY_UPP,
							"default_image" : "d:/ymir work/ui/game/safebox/upp_normal.tga",
							"over_image" : "d:/ymir work/ui/game/safebox/upp_hover.tga",
							"down_image" : "d:/ymir work/ui/game/safebox/upp_down.tga",
						},
						# SKILLBOOK BUTTON
						{
							"name" : "btn_skillbook",
							"type" : "radio_button",

							"x" : (BUTTON_WIDTH + BUTTON_X_SPACE) * 3,
							"y" : (BUTTON_HEIGHT + BUTTON_Y_SPACE) * 0,
							"tooltip_text" : uiScriptLocale.SAFEBOX_INVENTORY_SKILL,
							"default_image" : "d:/ymir work/ui/game/safebox/skillbook_normal.tga",
							"over_image" : "d:/ymir work/ui/game/safebox/skillbook_hover.tga",
							"down_image" : "d:/ymir work/ui/game/safebox/skillbook_down.tga",
						},
						# STONE BUTTON
						{
							"name" : "btn_stone",
							"type" : "radio_button",

							#"x" : int((BUTTON_WIDTH + BUTTON_X_SPACE) * 1.5),
							"x" : (BUTTON_WIDTH + BUTTON_X_SPACE) * 0,
							"y" : (BUTTON_HEIGHT + BUTTON_Y_SPACE) * 1,
							"tooltip_text" : uiScriptLocale.SAFEBOX_INVENTORY_STONE,
							"default_image" : "d:/ymir work/ui/game/safebox/stone_normal.tga",
							"over_image" : "d:/ymir work/ui/game/safebox/stone_hover.tga",
							"down_image" : "d:/ymir work/ui/game/safebox/stone_down.tga",
						},
						# ENCHANT BUTTON
						{
							"name" : "btn_enchant",
							"type" : "radio_button",

							#"x" : int((BUTTON_WIDTH + BUTTON_X_SPACE) * 1.5),
							"x" : (BUTTON_WIDTH + BUTTON_X_SPACE) * 1,
							"y" : (BUTTON_HEIGHT + BUTTON_Y_SPACE) * 1,
							"tooltip_text" : uiScriptLocale.SAFEBOX_INVENTORY_ENCHANT,
							"default_image" : "d:/ymir work/ui/game/safebox/enchant_normal.tga",
							"over_image" : "d:/ymir work/ui/game/safebox/enchant_hover.tga",
							"down_image" : "d:/ymir work/ui/game/safebox/enchant_down.tga",
						},
						# COSTUME BUTTON
						{
							"name" : "btn_costume",
							"type" : "radio_button",

							#"x" : int((BUTTON_WIDTH + BUTTON_X_SPACE) * 1.5),
							"x" : (BUTTON_WIDTH + BUTTON_X_SPACE) * 2,
							"y" : (BUTTON_HEIGHT + BUTTON_Y_SPACE) * 1,
							"tooltip_text" : uiScriptLocale.SAFEBOX_INVENTORY_COSTUME,
							"default_image" : "d:/ymir work/ui/game/safebox/costume_normal.tga",
							"over_image" : "d:/ymir work/ui/game/safebox/costume_hover.tga",
							"down_image" : "d:/ymir work/ui/game/safebox/costume_down.tga",
						},
						# GUILD BUTTON
						{
							"name" : "btn_guild",
							"type" : "button",

							#"x" : int((BUTTON_WIDTH + BUTTON_X_SPACE) * 1.5),
							"x" : (BUTTON_WIDTH + BUTTON_X_SPACE) * 3,
							"y" : (BUTTON_HEIGHT + BUTTON_Y_SPACE) * 1,
							"tooltip_text" : uiScriptLocale.SAFEBOX_INVENTORY_GUILD,
							"default_image" : "d:/ymir work/ui/game/safebox/gildenlager_normal.tga",
							"over_image" : "d:/ymir work/ui/game/safebox/gildenlager_hover.tga",
							"down_image" : "d:/ymir work/ui/game/safebox/gildenlager_down.tga",
						},
					),
				},
			),
		},
	),
}


import constInfo
if constInfo.SORT_AND_STACK_ITEMS_SAFEBOX:
	window["children"] += (
					{
						"name" : "SeparateBaseImage",
						"type" : "image",
						"style" : ("attach",),

						"x" : 8,
						"y" : 7,

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
