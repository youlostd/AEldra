import uiScriptLocale

MARGIN_LEFT = 20
MARGIN_TOP = 65
MARGIN_RIGHT = 25
MARGIN_BOTTOM = 20

BOARD_WIDTH = 350

window = {
	"name" : "AuctionInformerWindow",
	"style" : ("movable", "float",),

	"x" : 0,
	"y" : 0,

	"width" : BOARD_WIDTH,
	"height" : 0,

	"children" :
	(
		{
			"name" : "board",
			"type" : "board_with_titlebar",
			"style" : ("attach",),

			"x" : 0,
			"y" : 0,

			"width" : BOARD_WIDTH,
			"height" : 0,

			"title" : uiScriptLocale.AUCTION_INFORMER_WINDOW_TITLE,

			"children" :
			(
				{
					"name" : "info",
					"type" : "text",

					"x" : 0,
					"y" : MARGIN_TOP,

					"horizontal_align" : "center",
					"text_horizontal_align" : "center",
				},
				{
					"name" : "icon",
					"type" : "image",

					"x" : 0,
					"y" : MARGIN_TOP + 18,

					"horizontal_align" : "center",
				},
				{
					"name" : "received_gold",
					"type" : "extended_text",

					"x" : 0,
					"y" : MARGIN_BOTTOM + 24 + 18,

					"horizontal_align" : "center",
					"vertical_align" : "bottom",
				},
				{
					"name" : "close",
					"type" : "button",

					"x" : 0,
					"y" : MARGIN_BOTTOM + 24,

					"horizontal_align" : "center",
					"vertical_align" : "bottom",

					"default_image" : "d:/ymir work/ui/public/XLarge_Button_01.sub",
					"over_image" : "d:/ymir work/ui/public/XLarge_Button_02.sub",
					"down_image" : "d:/ymir work/ui/public/XLarge_Button_03.sub",

					"text" : uiScriptLocale.CLOSE,
				},
			),
		},
	),
}