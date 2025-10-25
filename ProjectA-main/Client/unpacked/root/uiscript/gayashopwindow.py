import uiScriptLocale

LEFT_MARGIN = 7
RIGHT_MARGIN = 7
TOP_MARGIN = 7
BOT_MARGIN = 7

BOARD_WIDTH = LEFT_MARGIN + 138 + RIGHT_MARGIN
BOARD_HEIGHT = TOP_MARGIN + 177 + BOT_MARGIN

window = {
	"name" : "GayaShopWindow",
	"style" : ("movable", "float"),

	"x" : 0,
	"y" : 0,

	"width" : BOARD_WIDTH,
	"height" : BOARD_HEIGHT,

	"children" :
	(
		## Board
		{
			"name" : "board",
			"type" : "board_with_titlebar",
			"style" : ("attach",),

			"x" : 0,
			"y" : 0,

			"width" : BOARD_WIDTH,
			"height" : BOARD_HEIGHT,

			"title" : uiScriptLocale.GAYA_SHOP_TITLE,

			"children" :
			(
				{
					"name" : "background",
					"type" : "image",

					"x" : LEFT_MARGIN,
					"y" : TOP_MARGIN,

					"image" : "d:/ymir work/ui/gemshop/gemshop_backimg.sub",

					"children" :
					(
						{
							"name" : "slot",
							"type" : "slot",

							"x" : 0,
							"y" : 0,

							"width" : 138,
							"height" : 177,

							"slot" : (
								{"index":0, "x": 8, "y":  7, "width":32, "height":32},
								{"index":1, "x":53, "y":  7, "width":32, "height":32},
								{"index":2, "x":98, "y":  7, "width":32, "height":32},
								{"index":3, "x": 8, "y": 65, "width":32, "height":32},
								{"index":4, "x":53, "y": 65, "width":32, "height":32},
								{"index":5, "x":98, "y": 65, "width":32, "height":32},
								{"index":6, "x": 8, "y":123, "width":32, "height":32},
								{"index":7, "x":53, "y":123, "width":32, "height":32},
								{"index":8, "x":98, "y":123, "width":32, "height":32},
							),
						},

						{
							"name" : "slot2",
							"type" : "slot",

							"x" : 0,
							"y" : 0,

							"width" : 138,
							"height" : 235,

							"slot" : (
								{"index":0, "x": 8, "y":  7, "width":32, "height":32},
								{"index":1, "x":53, "y":  7, "width":32, "height":32},
								{"index":2, "x":98, "y":  7, "width":32, "height":32},
								{"index":3, "x": 8, "y": 65, "width":32, "height":32},
								{"index":4, "x":53, "y": 65, "width":32, "height":32},
								{"index":5, "x":98, "y": 65, "width":32, "height":32},
								{"index":6, "x": 8, "y":123, "width":32, "height":32},
								{"index":7, "x":53, "y":123, "width":32, "height":32},
								{"index":8, "x":98, "y":123, "width":32, "height":32},
								{"index":9, "x": 8, "y":181, "width":32, "height":32},
								{"index":10, "x":53, "y":181, "width":32, "height":32},
								{"index":11, "x":98, "y":181, "width":32, "height":32},
							),
						},
						{
							"name" : "gaya_icon1",
							"type" : "image",

							"x" : 8 -3,
							"y" : 7 +39,

							"image" : "d:/ymir work/ui/gemshop/gemshop_gemicon.sub",

							"children" :
							(
								{
									"name" : "gaya_text_wnd1",

									"x" : 13,
									"y" : 0,

									"width" : 27,
									"height" : 11,

									"children" :
									(
										{
											"name" : "price1",
											"type" : "text",

											"x" : 0,
											"y" : 0,

											"all_align" : 1,

											"text" : "999",
										},
									),
								},
							),
						},
						{
							"name" : "gaya_icon2",
							"type" : "image",

							"x" : 53-3,
							"y" : 7 +39,

							"image" : "d:/ymir work/ui/gemshop/gemshop_gemicon.sub",

							"children" :
							(
								{
									"name" : "gaya_text_wnd2",

									"x" : 13,
									"y" : 0,

									"width" : 27,
									"height" : 11,

									"children" :
									(
										{
											"name" : "price2",
											"type" : "text",

											"x" : 0,
											"y" : 0,

											"all_align" : 1,

											"text" : "999",
										},
									),
								},
							),
						},
						{
							"name" : "gaya_icon3",
							"type" : "image",

							"x" : 98-3,
							"y" : 7 +39,

							"image" : "d:/ymir work/ui/gemshop/gemshop_gemicon.sub",

							"children" :
							(
								{
									"name" : "gaya_text_wnd3",

									"x" : 13,
									"y" : 0,

									"width" : 27,
									"height" : 11,

									"children" :
									(
										{
											"name" : "price3",
											"type" : "text",

											"x" : 0,
											"y" : 0,

											"all_align" : 1,

											"text" : "999",
										},
									),
								},
							),
						},
						{
							"name" : "gaya_icon4",
							"type" : "image",

							"x" : 8 -3,
							"y" : 65+39,

							"image" : "d:/ymir work/ui/gemshop/gemshop_gemicon.sub",

							"children" :
							(
								{
									"name" : "gaya_text_wnd4",

									"x" : 13,
									"y" : 0,

									"width" : 27,
									"height" : 11,

									"children" :
									(
										{
											"name" : "price4",
											"type" : "text",

											"x" : 0,
											"y" : 0,

											"all_align" : 1,

											"text" : "999",
										},
									),
								},
							),
						},
						{
							"name" : "gaya_icon5",
							"type" : "image",

							"x" : 53-3,
							"y" : 65+39,

							"image" : "d:/ymir work/ui/gemshop/gemshop_gemicon.sub",

							"children" :
							(
								{
									"name" : "gaya_text_wnd5",

									"x" : 13,
									"y" : 0,

									"width" : 27,
									"height" : 11,

									"children" :
									(
										{
											"name" : "price5",
											"type" : "text",

											"x" : 0,
											"y" : 0,

											"all_align" : 1,

											"text" : "999",
										},
									),
								},
							),
						},
						{
							"name" : "gaya_icon6",
							"type" : "image",

							"x" : 98-3,
							"y" : 65+39,

							"image" : "d:/ymir work/ui/gemshop/gemshop_gemicon.sub",

							"children" :
							(
								{
									"name" : "gaya_text_wnd6",

									"x" : 13,
									"y" : 0,

									"width" : 27,
									"height" : 11,

									"children" :
									(
										{
											"name" : "price6",
											"type" : "text",

											"x" : 0,
											"y" : 0,

											"all_align" : 1,

											"text" : "999",
										},
									),
								},
							),
						},
						{
							"name" : "gaya_icon7",
							"type" : "image",

							"x" : 8 -3,
							"y" : 123+39,

							"image" : "d:/ymir work/ui/gemshop/gemshop_gemicon.sub",

							"children" :
							(
								{
									"name" : "gaya_text_wnd7",

									"x" : 13,
									"y" : 0,

									"width" : 27,
									"height" : 11,

									"children" :
									(
										{
											"name" : "price7",
											"type" : "text",

											"x" : 0,
											"y" : 0,

											"all_align" : 1,

											"text" : "999",
										},
									),
								},
							),
						},
						{
							"name" : "gaya_icon8",
							"type" : "image",

							"x" : 53-3,
							"y" : 123+39,

							"image" : "d:/ymir work/ui/gemshop/gemshop_gemicon.sub",

							"children" :
							(
								{
									"name" : "gaya_text_wnd8",

									"x" : 13,
									"y" : 0,

									"width" : 27,
									"height" : 11,

									"children" :
									(
										{
											"name" : "price8",
											"type" : "text",

											"x" : 0,
											"y" : 0,

											"all_align" : 1,

											"text" : "999",
										},
									),
								},
							),
						},
						{
							"name" : "gaya_icon9",
							"type" : "image",

							"x" : 98-3,
							"y" : 123+39,

							"image" : "d:/ymir work/ui/gemshop/gemshop_gemicon.sub",

							"children" :
							(
								{
									"name" : "gaya_text_wnd9",

									"x" : 13,
									"y" : 0,

									"width" : 27,
									"height" : 11,

									"children" :
									(
										{
											"name" : "price9",
											"type" : "text",

											"x" : 0,
											"y" : 0,

											"all_align" : 1,

											"text" : "999",
										},
									),
								},
							),
						},

						{
							"name" : "gaya_icon10",
							"type" : "image",

							"x" : 8 -3,
							"y" : 123+39 + 58,

							"image" : "d:/ymir work/ui/gemshop/gemshop_gemicon.sub",

							"children" :
							(
								{
									"name" : "gaya_text_wnd10",

									"x" : 13,
									"y" : 0,

									"width" : 27,
									"height" : 11,

									"children" :
									(
										{
											"name" : "price10",
											"type" : "text",

											"x" : 0,
											"y" : 0,

											"all_align" : 1,

											"text" : "999",
										},
									),
								},
							),
						},
						{
							"name" : "gaya_icon11",
							"type" : "image",

							"x" : 53-3,
							"y" : 123+39 + 59,

							"image" : "d:/ymir work/ui/gemshop/gemshop_gemicon.sub",

							"children" :
							(
								{
									"name" : "gaya_text_wnd11",

									"x" : 13,
									"y" : 0,

									"width" : 27,
									"height" : 11,

									"children" :
									(
										{
											"name" : "price11",
											"type" : "text",

											"x" : 0,
											"y" : 0,

											"all_align" : 1,

											"text" : "999",
										},
									),
								},
							),
						},
						{
							"name" : "gaya_icon12",
							"type" : "image",

							"x" : 98-3,
							"y" : 123+39 + 59,

							"image" : "d:/ymir work/ui/gemshop/gemshop_gemicon.sub",

							"children" :
							(
								{
									"name" : "gaya_text_wnd12",

									"x" : 13,
									"y" : 0,

									"width" : 27,
									"height" : 11,

									"children" :
									(
										{
											"name" : "price12",
											"type" : "text",

											"x" : 0,
											"y" : 0,

											"all_align" : 1,

											"text" : "999",
										},
									),
								},
							),
						},

					),
				},
			),
		},
	),
}
