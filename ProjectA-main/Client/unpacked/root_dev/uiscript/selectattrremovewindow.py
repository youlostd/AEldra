import uiScriptLocale

BOARD_WIDTH = 300 - 32

window = {
	"name" : "SelectAttrRemoveWindow",
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

			"title" : uiScriptLocale.SELECT_ATTR_DETACH_TITLE,

			"children" :
			(
				{
					"name" : "description",
					"type" : "text",

					"x" : 0,
					"y" : 5,

					"horizontal_align" : "center",
					"text_horizontal_align" : "center",

					"text" : uiScriptLocale.SELECT_ATTR_DETACH_INFO,
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
					"name" : "attr_list_box_bg",
					"type" : "thinboard",

					"x" : 0,
					"y" : 0,

					"width" : 0,
					"height" : 0,

					"horizontal_align" : "center",

					"children" :
					(
						{
							"name" : "attr_list_box",
							"type" : "listboxex",

							"x" : 0,
							"y" : 0,

							"width" : 0,
							"height" : 0,

							#"horizontal_align" : "center",
							#"vertical_align" : "center",
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

					"text" : uiScriptLocale.SELECT_ATTR_DETACH_BUTTON,
				},
			),
		},
	),
}
