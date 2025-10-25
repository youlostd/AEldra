import ui
import uiScriptLocale
import playerSettingModule
import uiAuction

MARGIN_LEFT = 20
MARGIN_TOP = 65
MARGIN_BOTTOM = 20

BOARD_NO_ITEM_WIDTH = 250
BOARD_NO_ITEM_HEIGHT = 250

INPUT_WIDTH = 135
INPUT_HEIGHT = 19

window = {
	"name" : "AuctionInsertWindow",
	"style" : ("movable", "float",),

	"x" : 0,
	"y" : 0,

	"width" : 0,
	"height" : 0,

	"children" :
	(
		{
			"name" : "board",
			"type" : "board_with_titlebar",
			"style" : ("attach",),

			"x" : 0,
			"y" : 0,

			"width" : 0,
			"height" : 0,

			"title" : uiScriptLocale.AUCTION_INSERT_WINDOW_TITLE,

			"children" :
			(
				{
					"name" : "no_item_window",

					"x" : MARGIN_LEFT,
					"y" : MARGIN_TOP,

					"width" : BOARD_NO_ITEM_WIDTH,
					"height" : BOARD_NO_ITEM_HEIGHT,

					"children" :
					(
						{
							"name" : "no_item_info",
							"type" : "multi_text",

							"x" : 0,
							"y" : 0,

							"width" : 130,

							"horizontal_align" : "center",
							"text_horizontal_align" : "center",
							"vertical_align" : "center",
							"text_vertical_align" : "center",

							"text" : uiScriptLocale.AUCTION_INSERT_NO_ITEM_TEXT,
						},
					),
				},
				{
					"name" : "item_window",

					"x" : MARGIN_LEFT,
					"y" : MARGIN_TOP,

					"width" : 0,
					"height" : 0,

					"children" :
					(
						{
							"name" : "item_slot",
							"type" : "slot",

							"x" : 0,
							"y" : 0,

							"width" : 0,
							"height" : 0,

							"slot" : (),
							"image" : "d:/ymir work/ui/public/Slot_Base.sub",
						},
						{
							"name" : "item_price_field",
							"type" : "field",

							"x" : 0,
							"y" : 24 + 5 + INPUT_HEIGHT,

							"width" : INPUT_WIDTH,
							"height" : INPUT_HEIGHT,

							"vertical_align" : "bottom",

							"children" :
							(
								{
									"name" : "item_price_edit",
									"type" : "editline",

									"x" : 4,
									"y" : 4,

									"width" : INPUT_WIDTH - 4 * 2,
									"height" : INPUT_HEIGHT - 4 * 2,

									"input_limit" : 10,
									"only_number" : True,

									"overlay" : uiScriptLocale.AUCTION_SEARCH_EDIT_OVERLAY_TEXT,
								},
							),
						},
					),
				},
			),
		},
	),
}