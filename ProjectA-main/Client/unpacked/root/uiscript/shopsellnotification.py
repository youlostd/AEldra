import uiScriptLocale

window = {
	"name" : "ShopSellNotification",
	"style" : ("movable", "float",),

	"x" : SCREEN_WIDTH/2 - 250,
	"y" : SCREEN_HEIGHT/2 - 40,

	"width" : 225,
	"height" : 200,

	"children" :
	(
		{
			"name" : "board",
			"type" : "board",

			"x" : 0,
			"y" : 0,

			"width" : 225,
			"height" : 200,
			
			"text" : uiScriptLocale.SHOP_SELL_NOTIFICATION,

			"children" :
			(
				## Title
				{
					"name" : "titlebar",
					"type" : "titlebar",
					"style" : ("attach",),

					"x" : 0,
					"y" : 0,

					"width" : 161,
					"color" : "yellow",

					"children" :
					(
						{ "name":"TitleName", "type":"text", "x":0, "horizontal_align":"center","text_horizontal_align":"center", "y":3, "text":uiScriptLocale.SHOP_SELL_NOTIFICATION_TITLE, "text_horizontal_align":"center" },
					),
				

				},

				{
					"name" : "message",
					"type" : "multi_text",

					"x" : 0,
					"y" : 40,

					"text" : uiScriptLocale.SHOP_SELL_NOTIFICATION,

					"width" : 275 - 35 * 2,
					"horizontal_align" : "center",
					"text_horizontal_align" : "center",
					"text_vertical_align" : "center",
				},
				{
					"name" : "accept",
					"type" : "button",

					"x" : 0,
					"y" : 25,

					"horizontal_align" : "center",
					"vertical_align" : "bottom",
					"text" : uiScriptLocale.OK,

					"default_image" : "d:/ymir work/ui/public/large_button_01.sub",
					"over_image" : "d:/ymir work/ui/public/large_button_02.sub",
					"down_image" : "d:/ymir work/ui/public/large_button_03.sub",
				},
			),
		},
	),
}