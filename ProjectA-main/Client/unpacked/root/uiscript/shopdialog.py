import uiScriptLocale
import app

BOARD_WIDTH = 32 * 5 + 5 * 2
BOARD_HEIGHT = 7 + 32 * 8 + 5 + 25

window = {
	"name" : "ShopDialog",

	"x" : SCREEN_WIDTH - 400,
	"y" : 10,

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

			"title" : uiScriptLocale.SHOP_TITLE,

			"children" :
			(
				## Item Slot
				{
					"name" : "ItemSlot",
					"type" : "grid_table",

					"x" : 5,
					"y" : 7,

					"start_index" : 0,
					"x_count" : 5,
					"y_count" : 8,
					"x_step" : 32,
					"y_step" : 32,

					"image" : "d:/ymir work/ui/public/Slot_Base.sub",
				},

				## Buy
				{
					"name" : "BuyButton",
					"type" : "toggle_button",

					"x" : 5,
					"y" : 7 + 32 * 8 + 5,

					"width" : 61,
					"height" : 21,

					"text" : uiScriptLocale.SHOP_BUY,

					"default_image" : "d:/ymir work/ui/public/middle_button_01.sub",
					"over_image" : "d:/ymir work/ui/public/middle_button_02.sub",
					"down_image" : "d:/ymir work/ui/public/middle_button_03.sub",
				},

				## Sell
				{
					"name" : "SellButton",
					"type" : "toggle_button",

					"x" : 5 + 61,
					"y" : 7 + 32 * 8 + 5,

					"width" : 61,
					"height" : 21,

					"horizontal_align" : "right",

					"text" : uiScriptLocale.SHOP_SELL,

					"default_image" : "d:/ymir work/ui/public/middle_button_01.sub",
					"over_image" : "d:/ymir work/ui/public/middle_button_02.sub",
					"down_image" : "d:/ymir work/ui/public/middle_button_03.sub",
				},

				## Close
				{
					"name" : "CloseButton",
					"type" : "button",

					"x" : 0,
					"y" : 7 + 32 * 8 + 5,

					"horizontal_align" : "center",

					"text" : uiScriptLocale.PRIVATE_SHOP_CLOSE_BUTTON,

					"default_image" : "d:/ymir work/ui/public/large_button_01.sub",
					"over_image" : "d:/ymir work/ui/public/large_button_02.sub",
					"down_image" : "d:/ymir work/ui/public/large_button_03.sub",
				},

				## OfflineShop Money
				{
					"name" : "OfflineMoney_Slot",
					"type" : "button",

					"x" : 0,
					"y" : 7 + 32 * 8 + 5,

					"horizontal_align" : "center",

					"default_image" : "d:/ymir work/ui/public/parameter_slot_05.sub",
					"over_image" : "d:/ymir work/ui/public/parameter_slot_05.sub",
					"down_image" : "d:/ymir work/ui/public/parameter_slot_05.sub",

					"children" :
					(
						{
							"name" : "OfflineMoney",
							"type" : "text",

							"x" : 3,
							"y" : 3,

							"horizontal_align" : "right",
							"text_horizontal_align" : "right",

							"text" : "0",
						},
					),
				},

			),
		},
	),
}

if app.COMBAT_ZONE:
	window["children"] += (
		{
			"name" : "BattleShopSubBoard",
			"type" : "board",
			"style" : ("attach",),

			"x" : 0,
			"y" : 354-5,

			"width" : 184,
			"height" : 40,
			
			"children" :
			(
			{ "name":"BattleShopSubInfoImage", "type":"image", "x":20, "y":13, "image":"d:/ymir work/ui/public/battle/icon_my_point.sub", },
			{ "name":"BattleShopSubInfo1", "type":"text", "x":40, "y":15, "text":"My Point : 0"},
			{ "name":"BattleShopSubInfo2", "type":"text", "x":20, "y":35, "text":"Limit : 0/100"},
			)
		},
	)
