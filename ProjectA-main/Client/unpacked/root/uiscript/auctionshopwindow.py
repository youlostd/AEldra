import uiScriptLocale

WIDTH = 368
HEIGHT = 443

window = {
	"name" : "AuctionShopWindow",

	"x" : (SCREEN_WIDTH / 2) - (WIDTH / 2),
	"y" : (SCREEN_HEIGHT / 2) - (HEIGHT / 2),

	"style" : ("movable", "float",),

	"width" : WIDTH,
	"height" : HEIGHT,

	"children" :
	(
		{
			"name" : "board",
			"type" : "image",
			"style" : ("attach",),

			"x" : 0,
			"y" : 0,

			"image" : "d:/ymir work/ui/game/offlineshop/tab_main/bg_2.tga",

			"children" :
			(
				## TITLE BAR
				{
					"name" : "title_bar",
					"type" : "titlebar",
					"style" : ("attach",),

					"x" : 8,
					"y" : 8,

					"width" : WIDTH - 16,
					"color" : "red",

					"children" :
					(
						{
							"name" : "title_name",
							"type" : "text",
							"text" : uiScriptLocale.OFFLINE_SHOP_TITLE,
							"horizontal_align" : "center",
							"text_horizontal_align" : "center",
							"x" : 0,
							"y" : 3,
						},
					),
				},
				## SHOP NAME
				{
					"name" : "shop_name_bg",
					"type" : "image",

					"x" : 16,
					"y" : 35,

					"image" : "d:/ymir work/ui/game/offlineshop/tab_main/namefield2.tga",

					"children" :
					(
						{
							"name" : "shop_name_text",
							"type" : "text",
							"text" : "",
							"horizontal_align" : "left",
							"text_horizontal_align" : "left",
							"x" : 9,
							"y" : 6,
						},
					),
				},
				## Button Close
				{
					"name" : "CloseButton",
					"type" : "button",

					"x" : 277,
					"y" : 35,

					"default_image" : "d:/ymir work/ui/game/offlineshop/tab_main/btn_2_normal.tga",
					"over_image" : "d:/ymir work/ui/game/offlineshop/tab_main/btn_2_hover.tga",
					"down_image" : "d:/ymir work/ui/game/offlineshop/tab_main/btn_2_down.tga",

					"tooltip_text" : uiScriptLocale.PRIVATE_SHOP_CLOSE_BUTTON,
				},
				# Button History
				{
					"name" : "button_history",
					"type" : "button",

					"x" : 318,
					"y" : 35,

					"default_image" : "d:/ymir work/ui/game/offlineshop/tab_main/btn_3_normal.tga",
					"over_image" : "d:/ymir work/ui/game/offlineshop/tab_main/btn_3_hover.tga",
					"down_image" : "d:/ymir work/ui/game/offlineshop/tab_main/btn_3_down.tga",

					"tooltip_text" : uiScriptLocale.OFFLINE_SHOP_SALES_HISTORY,
				},
				## Item Slot
				{
					"name" : "ItemSlot",
					"type" : "grid_table",

					"x" : 23,
					"y" : 81,

					"start_index" : 0,
					"x_count" : 10,
					"y_count" : 8,
					"x_step" : 32,
					"y_step" : 32,
				},

				{
					"name" : "bottom_bar",

					"x" : 17,
					"y" : 344,

					"width" : 332,
					"height" : 79,

					"children" :
					(
						{
							"name" : "time_left_bg",
							"type" : "image",

							"x" : 22 - 17,
							"y" : 360 - 344,

							"image" : "d:/ymir work/ui/game/offlineshop/tab_main/time_bg.tga",

							"children" :
							(
								{
									"name" : "time_left_label_text",
									"type" : "text",
									"text" : uiScriptLocale.OFFLINE_SHOP_TIME_REMAINING,
									"horizontal_align" : "center",
									"text_horizontal_align" : "center",
									"x" : -10,
									"y" : 6,
								},

								{
									"name" : "TimeLeftText",
									"type" : "text",
									"text" : "",
									"horizontal_align" : "center",
									"text_horizontal_align" : "center",
									"x" : -10,
									"y" : 20,
									"color" : 0xff00ff00,
								},
							),
						},

						{
							"name" : "RenewButton",
							"type" : "button",

							"x" : 131 - 17,
							"y" : 355 - 344 + 2,

							"default_image" : "d:/ymir work/ui/game/offlineshop/tab_main/btn_time_normal.tga",
							"over_image" : "d:/ymir work/ui/game/offlineshop/tab_main/btn_time_hover.tga",
							"down_image" : "d:/ymir work/ui/game/offlineshop/tab_main/btn_time_down.tga",
						},

						{
							"name" : "yang_withdraw_bg",
							"type" : "image",

							"x" : 195 - 17,
							"y" : 354 - 344,

							"image" : "d:/ymir work/ui/game/offlineshop/tab_main/yang_bg.tga",

							"children" :
							(
								{
									"name" : "yang_withdraw_yangicon",
									"type" : "image",

									"x" : 7,
									"y" : 7,

									"image" : "d:/ymir work/ui/game/offlineshop/tab_main/yang.tga",
								},

								{
									"name" : "Money",
									"type" : "text",
									"text" : "0",
									"horizontal_align" : "right",
									"text_horizontal_align" : "right",
									"x" : 10,
									"y" : 6,
								},
							),
						},

						{
							"name" : "Money_Slot",
							"type" : "button",

							"x" : 195 - 17 + 1,
							"y" : 388 - 344 + 1,

							"default_image" : "d:/ymir work/ui/game/offlineshop/tab_main/btn_yang_normal.tga",
							"over_image" : "d:/ymir work/ui/game/offlineshop/tab_main/btn_yang_hover.tga",
							"down_image" : "d:/ymir work/ui/game/offlineshop/tab_main/btn_yang_down.tga",

							"text" : uiScriptLocale.OFFLINE_SHOP_WITHDRAW_GOLD,
						},
					),
				},
				# History
				{
					"name" : "history",

					"x" : 17,
					"y" : 76,

					"width" : 348,
					"height" : 331,

					"children" : 
					(
						{
							"name" : "label_item",
							"type" : "text",

							"text" : uiScriptLocale.OFFLINE_SHOP_HISTORY_COLUMN1,

							"text_horizontal_align" : "left",

							"x" : 56 - 30,
							"y" : 6,
						},

						{
							"name" : "label_price",
							"type" : "text",

							"text" : uiScriptLocale.OFFLINE_SHOP_HISTORY_COLUMN2,

							"text_horizontal_align" : "left",

							"x" : 141 - 20,
							"y" : 6,
						},

						{
							"name" : "label_buyer",
							"type" : "text",

							"text" : uiScriptLocale.OFFLINE_SHOP_HISTORY_COLUMN3,

							"text_horizontal_align" : "left",

							"x" : 217 - 15,
							"y" : 6,
						},

						{
							"name" : "label_date",
							"type" : "text",

							"text" : uiScriptLocale.OFFLINE_SHOP_HISTORY_COLUMN4,

							"text_horizontal_align" : "left",

							"x" : 296 - 17,
							"y" : 6,
						},

						{
							"name" : "history_listbox",
							"type" : "listboxex",

							"x" : 21 - 17,
							"y" : 103 - 76,

							"width" : 314,
							"height" : 310,

							"itemsize_x" : 314,
							"itemsize_y" : 44,

							"viewcount" : 7,
							"itemstep" : 44,
						},

						{
							"name" : "history_scrollbar",
							"type" : "scrollbar_template",

							"x" : 339 - 17,
							"y" : 103 - 76,

							"size" : 44 * 7,

							"bg_top_image" : "d:/ymir work/ui/game/offlineshop/tab_main/scroll/top.tga",
							"bg_center_image" : "d:/ymir work/ui/game/offlineshop/tab_main/scroll/middle_2.tga",
							"bg_bottom_image" : "d:/ymir work/ui/game/offlineshop/tab_main/scroll/bottom.tga",

							"middle_image" : "d:/ymir work/ui/game/offlineshop/tab_main/scroll/middle.tga",
						},
					),
				},
			),
		},
	),
}