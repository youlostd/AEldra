import uiScriptLocale
import auction

BOARD_WIDTH = 32 * auction.SHOP_SLOT_COUNT_X + 5 * 2
BOARD_HEIGHT = 7 + 32 * auction.SHOP_SLOT_COUNT_Y + 5 + 25

window = {
	"name" : "AuctionGuestShopWindow",

	"x" : (SCREEN_WIDTH / 2) - (BOARD_WIDTH / 2),
	"y" : (SCREEN_HEIGHT / 2) - (BOARD_HEIGHT / 2),

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

			"title" : "AuctionShop",

			"children" :
			(
				## Item Slot
				{
					"name" : "ItemSlot",
					"type" : "grid_table",

					"x" : 5,
					"y" : 7,

					"start_index" : 0,
					"x_count" : auction.SHOP_SLOT_COUNT_X,
					"y_count" : auction.SHOP_SLOT_COUNT_Y,
					"x_step" : 32,
					"y_step" : 32,

					"image" : "d:/ymir work/ui/public/Slot_Base.sub",
				},
				## Buy
				{
					"name" : "BuyButton",
					"type" : "toggle_button",

					"x" : 5,
					"y" : 7 + 32 * auction.SHOP_SLOT_COUNT_Y + 5,

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
					"y" : 7 + 32 * auction.SHOP_SLOT_COUNT_Y + 5,

					"width" : 61,
					"height" : 21,

					"horizontal_align" : "right",

					"text" : uiScriptLocale.SHOP_SELL,

					"default_image" : "d:/ymir work/ui/public/middle_button_01.sub",
					"over_image" : "d:/ymir work/ui/public/middle_button_02.sub",
					"down_image" : "d:/ymir work/ui/public/middle_button_03.sub",
				},
			),
		},
	),
}