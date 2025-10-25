import uiScriptLocale

window = {
	"name" : "CubeWindow",

	"x" : 430,
	"y" : 230,

	"style" : ("movable", "float",),

	"width" : 176,
	"height" : 175,

	"children" :
	(
		{
			"name" : "board",
			"type" : "board_with_titlebar",
			"style" : ("attach",),

			"x" : 0,
			"y" : 0,

			"width" : 176,
			"height" : 175,

			"title" : "Cube",

			"children" :
			(
				## Cube Slot
				{
					"name" : "CubeSlot",
					"type" : "grid_table",

					"x" : 176/2 - 32,
					"y" : 40 - 2,

					"start_index" : 0,
					"x_count" : 2,
					"y_count" : 2,
					"x_step" : 32,
					"y_step" : 32,

					"image" : "d:/ymir work/ui/public/Slot_Base.sub"
				},

				## Text
				{
					"name":"label",
					"type":"text",

					"x":0,
					"y":60,

					"vertical_align" : "bottom",
					"horizontal_align" : "center",

					"text":"합성에 성공 했습니다",
					"text_horizontal_align":"center",
				},

				## Button
				{
					"name" : "CloseButton",
					"type" : "button",

					"x" : 0,
					"y" : 35,
					"horizontal_align" : "center",
					"vertical_align" : "bottom",

					"text" : uiScriptLocale.OK,

					"default_image" : "d:/ymir work/ui/public/middle_button_01.sub",
					"over_image" : "d:/ymir work/ui/public/middle_button_02.sub",
					"down_image" : "d:/ymir work/ui/public/middle_button_03.sub",
				},
			),
		},
	),
}
