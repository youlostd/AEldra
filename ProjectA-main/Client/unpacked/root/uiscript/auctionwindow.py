import ui
import uiScriptLocale
import playerSettingModule
import uiAuction
import constInfo
import grp

MARGIN_LEFT = 15
MARGIN_TOP = 15
MARGIN_RIGHT = 15
MARGIN_BOTTOM = 15

BOARD_WIDTH = 600
BOARD_HEIGHT = 546
BOARD_USABLE_HEIGHT = BOARD_HEIGHT - MARGIN_TOP - MARGIN_BOTTOM

LEFT_WND_WIDTH = 220
INPUT_HEIGHT = 19

ITEM_WIDTH = BOARD_WIDTH - MARGIN_LEFT - MARGIN_RIGHT - LEFT_WND_WIDTH - 10

if constInfo.AUCTION_INSERT_ITEM_ENABLED:
	sellNoItemText = uiScriptLocale.AUCTION_SELL_NO_ITEM_TEXT
else:
	sellNoItemText = uiScriptLocale.AUCTION_SELL_NO_ITEM_DISABLE_TEXT

window = {
	"name" : "AuctionWindow",
	"style" : ("movable", "float",),

	"x" : 0,
	"y" : 0,

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

			"title" : uiScriptLocale.AUCTION_WINDOW_TITLE,

			"children" :
			(

				{
					"name" : "premium_info_icon",
					"type" : "image",

					"x" : MARGIN_LEFT,
					"y" : 5,

					#"vertical_align" : "bottom",

					"image" : "d:/ymir work/ui/info.tga",

					"children" :
					(
						{
							"name" : "premium_info",
							"type" : "text",

							"x" : 20 + 7,
							"y" : 0,

							"vertical_align" : "center",
							"text_vertical_align" : "center",

							"text" : "Premium aktiv",
						},
					),
				},
				{
					"name" : "search_window",
					"type" : "thinboard",

					"x" : MARGIN_LEFT,
					"y" : MARGIN_TOP + 15,

					"width" : LEFT_WND_WIDTH,
					"height" : BOARD_USABLE_HEIGHT - 215,

					"children" :
					(
						{
							"name" : "search_text_edit_field",
							"type" : "slotbar",

							"x" : 10,
							"y" : 10,

							"width" : LEFT_WND_WIDTH - 10 * 2,
							"height" : INPUT_HEIGHT,

							"children" :
							(
								{
									"name" : "search_text_edit_text",
									"type" : "editline",

									"x" : 4,
									"y" : 4,

									"width" : LEFT_WND_WIDTH - (15 + 25) - 15 - 4 * 2,
									"height" : INPUT_HEIGHT - 4 * 2,

									"input_limit" : 90,

									"overlay" : uiScriptLocale.AUCTION_SEARCH_EDIT_OVERLAY_TEXT,
								},
							),
						},
						{
							"name" : "search_race_title",
							"type" : "text",

							"x" : 15,
							"y" : 10 + INPUT_HEIGHT + 10,

							"text" : uiScriptLocale.AUCTION_RACE_TEXT,
						},
						{
							"name" : "search_race_checkbox1",
							"type" : "checkbox",

							"x" : 25,
							"y" : 10 + INPUT_HEIGHT + 10 + 20,

							"text" : uiScriptLocale.AUCTION_RACE_TEXT_1,
							"checked" : True,
						},
						{
							"name" : "search_race_checkbox2",
							"type" : "checkbox",

							"x" : 25,
							"y" : 10 + INPUT_HEIGHT + 10 + 20 + 20,

							"text" : uiScriptLocale.AUCTION_RACE_TEXT_2,
							"checked" : True,
						},
						{
							"name" : "search_race_checkbox3",
							"type" : "checkbox",

							"x" : 25,
							"y" : 10 + INPUT_HEIGHT + 10 + 20 + 20 + 20,

							"text" : uiScriptLocale.AUCTION_RACE_TEXT_3,
							"checked" : True,
						},
						{
							"name" : "search_race_checkbox4",
							"type" : "checkbox",

							"x" : 25,
							"y" : 10 + INPUT_HEIGHT + 10 + 20 + 20 + 20 + 20,

							"text" : uiScriptLocale.AUCTION_RACE_TEXT_4,
							"checked" : True,
						},
						{
							"name" : "search_level_text1",
							"type" : "text",

							"x" : 15,
							"y" : 10 + INPUT_HEIGHT + 10 + 20 + 20 + 20 + 20 + 20 + 8,

							"text" : uiScriptLocale.AUCTION_LV_TEXT_1,
						},
						{
							"name" : "search_level_field1",
							"type" : "slotbar",

							"x" : 15,
							"y" : 10 + INPUT_HEIGHT + 10 + 20 + 20 + 20 + 20 + 20 + 8 + 20,

							"width" : 81,
							"height" : INPUT_HEIGHT,

							"children" :
							(
								{
									"name" : "search_level_edit1",
									"type" : "editline",

									"x" : 4,
									"y" : 4,

									"width" : 81 - 4 * 2,
									"height" : INPUT_HEIGHT - 4 * 2,

									"input_limit" : 3,
									"only_number" : True,

									"overlay" : "0",
								},
							),
						},
						{
							"name" : "search_level_text2",
							"type" : "text",

							"x" : 15 + 81 + 7,
							"y" : 10 + INPUT_HEIGHT + 10 + 20 + 20 + 20 + 20 + 20 + 8 + 20 + 3,

							"text" : uiScriptLocale.AUCTION_LV_TEXT_2,
						},
						{
							"name" : "search_level_field2",
							"type" : "slotbar",

							"x" : 15 + 81 + 7 + 20,
							"y" : 10 + INPUT_HEIGHT + 10 + 20 + 20 + 20 + 20 + 20 + 8 + 20,

							"width" : 82,
							"height" : INPUT_HEIGHT,

							"children" :
							(
								{
									"name" : "search_level_edit2",
									"type" : "editline",

									"x" : 4,
									"y" : 4,

									"width" : 82 - 4 * 2,
									"height" : INPUT_HEIGHT - 4 * 2,

									"input_limit" : 3,
									"only_number" : True,

									"overlay" : "105",
								},
							),
						},
						{
							"name" : "search_price_text1",
							"type" : "text",

							"x" : 15,
							"y" : 10 + INPUT_HEIGHT + 10 + 20 + 20 + 20 + 20 + 20 + 8 + 20 + INPUT_HEIGHT + 10,

							"text" : uiScriptLocale.AUCTION_PRICE_TEXT_1,
						},
						{
							"name" : "search_price_field1",
							"type" : "slotbar",

							"x" : 15,
							"y" : 10 + INPUT_HEIGHT + 10 + 20 + 20 + 20 + 20 + 20 + 8 + 20 + INPUT_HEIGHT + 10 + 20,

							"width" : 76,
							"height" : INPUT_HEIGHT,

							"children" :
							(
								{
									"name" : "search_price_edit1",
									"type" : "editline",

									"x" : 4,
									"y" : 4,

									"width" : 76 - 4 * 2,
									"height" : INPUT_HEIGHT - 4 * 2,

									"input_limit" : 12,
									"only_number" : True,

									"overlay" : "1",
								},
							),
						},
						{
							"name" : "search_price_text2",
							"type" : "text",

							"x" : 15 + 76 + 7,
							"y" : 10 + INPUT_HEIGHT + 10 + 20 + 20 + 20 + 20 + 20 + 8 + 20 + INPUT_HEIGHT + 10 + 20 + 3,

							"text" : uiScriptLocale.AUCTION_PRICE_TEXT_2,
						},
						{
							"name" : "search_price_field2",
							"type" : "slotbar",

							"x" : 15 + 76 + 7 + 20,
							"y" : 10 + INPUT_HEIGHT + 10 + 20 + 20 + 20 + 20 + 20 + 8 + 20 + INPUT_HEIGHT + 10 + 20,

							"width" : 87,
							"height" : INPUT_HEIGHT,

							"children" :
							(
								{
									"name" : "search_price_edit2",
									"type" : "editline",

									"x" : 4,
									"y" : 4,

									"width" : 87 - 4 * 2,
									"height" : INPUT_HEIGHT - 4 * 2,

									"input_limit" : 12,
									"only_number" : True,

									"overlay" : uiScriptLocale.AUCTION_PRICE_OVERLAY_2,
								},
							),
						},
						
						{
							"name" : "search_button",
							"type" : "button",

							"x" : 15,
							"y" : 10 + 24 + 3,

							"vertical_align" : "bottom",

							"default_image" : "d:/ymir work/ui/public/Large_Button_01.sub",
							"over_image" : "d:/ymir work/ui/public/Large_Button_02.sub",
							"down_image" : "d:/ymir work/ui/public/Large_Button_03.sub",
							"disable_image" : "d:/ymir work/ui/public/Large_Button_04.sub",

							"text" : uiScriptLocale.AUCTION_SEARCH_BUTTON_TEXT,
						},
						{
							"name" : "search_reset_button",
							"type" : "button",

							"x" : 15 + 88,
							"y" : 10 + 24 + 3,

							"horizontal_align" : "right",
							"vertical_align" : "bottom",

							"default_image" : "d:/ymir work/ui/public/Large_Button_01.sub",
							"over_image" : "d:/ymir work/ui/public/Large_Button_02.sub",
							"down_image" : "d:/ymir work/ui/public/Large_Button_03.sub",
							"disable_image" : "d:/ymir work/ui/public/Large_Button_04.sub",

							"text" : uiScriptLocale.AUCTION_SEARCH_RESET_BUTTON_TEXT,
						},
					),
				},
				{
					"name" : "item_window",
					"type" : "thinboard",

					"x" : MARGIN_LEFT + LEFT_WND_WIDTH + 10,
					"y" : MARGIN_TOP,

					"width" : ITEM_WIDTH,
					"height" : BOARD_USABLE_HEIGHT,

					"children" :
					(
						{
							"name" : "item_list",
							"type" : "listboxex",

							"x" : 6,
							"y" : 6,

							"width" : ITEM_WIDTH - 6 * 2,
							"height" : (uiAuction.AuctionWindow.AuctionItem.ITEM_HEIGHT + 2) * 10 - 2,

							"itemsize_x" : ITEM_WIDTH - 6 * 2,
							"itemsize_y" : uiAuction.AuctionWindow.AuctionItem.ITEM_HEIGHT,

							"itemstep" : uiAuction.AuctionWindow.AuctionItem.ITEM_HEIGHT + 2,
						},
						{
							"name" : "item_scroll",
							"type" : "scrollbar",

							"x" : 6 + ITEM_WIDTH - 6 * 2 - ui.ScrollBar.SCROLLBAR_WIDTH,
							"y" : 6,

							"size" : (uiAuction.AuctionWindow.AuctionItem.ITEM_HEIGHT + 2) * 10 - 2,
						},
						{
							"name" : "item_loading_image",
							"type" : "ani_image",

							"x" : (ITEM_WIDTH - 16) / 2,
							"y" : (BOARD_USABLE_HEIGHT - 16) / 2,

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
					),
				},
				{
					"name" : "item_page_button_left",
					"type" : "button",

					"x" : MARGIN_LEFT + LEFT_WND_WIDTH + 10,
					"y" : MARGIN_TOP + BOARD_USABLE_HEIGHT + 4,

					"default_image" : "d:/ymir work/ui/button_skip_left.tga",
					"over_image" : "d:/ymir work/ui/button_skip_left_over.tga",
					"down_image" : "d:/ymir work/ui/button_skip_left_down.tga",

					"tooltip_text" : uiScriptLocale.AUCTION_ITEM_PAGE_BUTTON_LEFT_TOOLTIP,
				},
				{
					"name" : "item_page_button_right",
					"type" : "button",

					"x" : MARGIN_LEFT + LEFT_WND_WIDTH + 10 + ITEM_WIDTH - 17,
					"y" : MARGIN_TOP + BOARD_USABLE_HEIGHT + 4,

					"default_image" : "d:/ymir work/ui/button_skip_right.tga",
					"over_image" : "d:/ymir work/ui/button_skip_right_over.tga",
					"down_image" : "d:/ymir work/ui/button_skip_right_down.tga",

					"tooltip_text" : uiScriptLocale.AUCTION_ITEM_PAGE_BUTTON_RIGHT_TOOLTIP,
				},
			),
		},
	),
}