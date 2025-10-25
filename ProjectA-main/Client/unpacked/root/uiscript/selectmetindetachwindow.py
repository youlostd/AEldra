import uiScriptLocale

BOARD_WIDTH = 300 - 32

window = {
	"name" : "SelectMetinDetachWindow",
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

			"title" : uiScriptLocale.SELECT_METIN_DETACH_TITLE,

			"children" :
			(
				{
					"name" : "description",
					"type" : "text",

					"x" : 0,
					"y" : 5,

					"horizontal_align" : "center",
					"text_horizontal_align" : "center",

					"text" : uiScriptLocale.SELECT_METIN_DETACH_INFO,
				},
				{
					"name" : "item",
					"type" : "image",

					"x" : 0,
					"y" : 23,

					"horizontal_align" : "center",

					"image" : "d:/ymir work/ui/public/Slot_Base.sub",
				},
				{
					"name" : "metin_slot_background",
					"type" : "window", #"slot_background",

					"x" : 0,
					"y" : 0,

					"width" : 0,
					"height" : 32,

					"horizontal_align" : "center",

					"children" :
					(
						{
							"name" : "metin_slot",
							"type" : "slot",

							"x" : 0,
							"y" : 0,

							"width" : 96 + 32 + 10,
							"height" : 32,

							"image" : "d:/ymir work/ui/public/Slot_Base.sub",

							"slot" :
							(
								{"index":0, "x":0, "y":0, "width":32, "height":32},
								{"index":1, "x":32 + 5, "y":0, "width":32, "height":32},
								{"index":2, "x":64 + 10, "y":0, "width":32, "height":32},
								#{"index":3, "x":64 + 32 + 15, "y":0, "width":32, "height":32},
							),
						},
					),
				},
				{
					"name" : "remove_button",
					"type" : "button",

					"x" : 0,
					"y" : 10 + 24,

					"default_image" : "d:/ymir work/ui/public/XLarge_Button_01.sub",
					"over_image" : "d:/ymir work/ui/public/XLarge_Button_02.sub",
					"down_image" : "d:/ymir work/ui/public/XLarge_Button_03.sub",

					"horizontal_align" : "center",
					"vertical_align" : "bottom",

					"text" : uiScriptLocale.SELECT_METIN_DETACH_BUTTON,
				},
			),
		},
	),
}
