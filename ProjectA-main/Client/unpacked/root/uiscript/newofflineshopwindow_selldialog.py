import uiScriptLocale

WIDTH = 241
HEIGHT = 427

window = {

	"name" : "NewOfflineShopWindowSellItemDialog",

	# CENTER
	"x" : (SCREEN_WIDTH / 2) - (WIDTH / 2),
	"y" : (SCREEN_HEIGHT / 2) - (HEIGHT / 2),

	"style" : ("movable", "float",),

	"width" : WIDTH,
	"height" : HEIGHT,

	"children" :
	(
		{
			"name" : "background",
			"type" : "image",
			"style" : ("attach",),

			"x" : 0,
			"y" : 0,

			"image" : "d:/ymir work/ui/game/offlineshop/tab_sell/bg.tga",

			"children" :
			(
				## BUTTONS
				{
					"name" : "button_sell",
					"type" : "button",

					"x" : -48,
					"y" : 55,

					"text" : uiScriptLocale.SHOP_SELL,

					"horizontal_align" : "center",
					"vertical_align" : "bottom",

					"default_image" : "d:/ymir work/ui/game/offlineshop/tab_sell/btn_normal.tga",
					"over_image" : "d:/ymir work/ui/game/offlineshop/tab_sell/btn_hover.tga",
					"down_image" : "d:/ymir work/ui/game/offlineshop/tab_sell/btn_down.tga",
				},

				{
					"name" : "button_close",
					"type" : "button",

					"x" : 48,
					"y" : 55,

					"text" : uiScriptLocale.CLOSE,

					"horizontal_align" : "center",
					"vertical_align" : "bottom",

					"default_image" : "d:/ymir work/ui/game/offlineshop/tab_sell/btn_normal.tga",
					"over_image" : "d:/ymir work/ui/game/offlineshop/tab_sell/btn_hover.tga",
					"down_image" : "d:/ymir work/ui/game/offlineshop/tab_sell/btn_down.tga",
				},

				{
					"name" : "average_price_label",
					"type" : "text",

					"x" : 0,
					"y" : 97,

					"vertical_align" : "bottom",
					"horizontal_align" : "center",
					"text_horizontal_align" : "center",

					"fontsize" : "LARGE",

					"text" : uiScriptLocale.OFFLINE_SHOP_AVERAGE_PRICE,
				},

				{
					"name" : "average_price_text",
					"type" : "text",

					"x" : 0,
					"y" : 80,

					"vertical_align" : "bottom",
					"horizontal_align" : "center",
					"text_horizontal_align" : "center",

					"fontsize" : "LARGE",

					"text" : "0 Yang",
				},

				# {
				# 	"name" : "colorbar",
				# 	"type" : "image",

				# 	"x" : 21,
				# 	"y" : 61,

				# 	"image" : "d:/ymir work/ui/game/offlineshop/tab_sell/colorbar2.tga",

				# 	# "children" : 
				# 	# (
				# 		# {
				# 			# "name" : "price_arrow",
				# 			# "type" : "image",

				# 			# "x" : -5,
				# 			# "y" : 1,

				# 			# "image" : "d:/ymir work/ui/game/offlineshop/tab_sell/arrow.tga",
				# 		# },
				# 	# ),
				# },

				{
					"name" : "price_ask_label",
					"type" : "multi_text",

					"x" : 0,
					"y" : 21,

					"vertical_align" : "top",
					"horizontal_align" : "center",
					"text_horizontal_align" : "center",

					#"fontsize" : "LARGE",

					"text" : uiScriptLocale.OFFLINE_SHOP_SELL_DIALOG_QUESTION,
				},

				{
					"name" : "item_name",
					"type" : "text",

					"x" : 0,
					"y" : 196,

					"horizontal_align" : "center",
					"text_horizontal_align" : "center",

					"fontsize" : "LARGE",

					"text" : "",
				},

				{
					"name" : "you_get_text",
					"type" : "text",

					"x" : 0,
					"y" : 144,

					"horizontal_align" : "center",
					"text_horizontal_align" : "center",

					"text" : uiScriptLocale.OFFLINE_SHOP_YOU_GET,
				},

				{
					"name" : "item_background",
					"type" : "image",

					"x" : 0,
					"y" : 215,

					"horizontal_align" : "center",

					"image" : "d:/ymir work/ui/game/offlineshop/tab_sell/item_bg.tga",

					"children" :
					(
						{
							"name" : "item_icon",
							"type" : "image",

							"x" : 0,
							"y" : 0,

							"image" : "d:/ymir work/ui/game/offlineshop/tab_sell/yang.tga",

							"horizontal_align" : "center",
							"vertical_align" : "center",
						},
					),
				},

				{
					"name" : "price_field",
					"type" : "image",

					"x" : 24,
					"y" : 82,

					"image" : "d:/ymir work/ui/game/offlineshop/tab_sell/yang_bg.tga",

					"children" : 
					(
						{
							"name" : "price_editline",
							"type" : "editline",

							"x" : 27,
							"y" : 1,

							"vertical_align" : "center",
							"horizontal_align" : "left",

							"width" : 120,
							"height" : 16,

							"input_limit" : 10,
						},

						{
							"name" : "yang_icon",
							"type" : "image",

							"x" : 7,
							"y" : 7,

							"image" : "d:/ymir work/ui/game/offlineshop/tab_sell/yang.tga",
						}
					),
				},

				{
					"name" : "real_price_field",
					"type" : "image",

					"x" : 24,
					"y" : 164,

					"image" : "d:/ymir work/ui/game/offlineshop/tab_sell/yang_bg.tga",

					"children" : 
					(
						{
							"name" : "real_price_text",
							"type" : "text",

							"x" : 27,
							"y" : -8,

							"vertical_align" : "center",
							"horizontal_align" : "left",
							"text_horizontal_align" : "left",

							"fontsize" : "LARGE",

							"text" : "",
						},

						{
							"name" : "yang_icon",
							"type" : "image",

							"x" : 7,
							"y" : 7,

							"image" : "d:/ymir work/ui/game/offlineshop/tab_sell/yang.tga",
						}
					),
				},
				
				{
					"name" : "button_set_avg_price",
					"type" : "toggle_button",

					"x" : 25,
					"y" : 118,

					"horizontal_align" : "left",

					"default_image" : "d:/ymir work/ui/game/offlineshop/tab_sell/checkbox_new_unselected.tga",
					"over_image" : "d:/ymir work/ui/game/offlineshop/tab_sell/checkbox_new_unselected.tga",
					"down_image" : "d:/ymir work/ui/game/offlineshop/tab_sell/checkbox_new_selected.tga",
				},

				{
					"name" : "sell_for_average_text",
					"type" : "text",

					"x" : 25 + 14 + 5,
					"y" : 118,

					"horizontal_align" : "left",
					"text_horizontal_align" : "left",

					"text" : uiScriptLocale.OFFLINE_SHOP_SELL_AVERAGE_PRICE,
				},

			),
		},
	),
}
