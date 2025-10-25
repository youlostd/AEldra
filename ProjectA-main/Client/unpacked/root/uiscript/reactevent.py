import uiScriptLocale

IMAGE_PATH = "d:/ymir work/ui/react_event/"
WINDOW_WIDTH = 253
WINDOW_HEIGHT = 344

window = {
	"name" : "ReactEventWindow",

	"x" : (SCREEN_WIDTH - WINDOW_WIDTH) / 2,
	"y" : (SCREEN_HEIGHT - WINDOW_HEIGHT) / 2,

	"style" : ("movable", "float",),

	"width" : WINDOW_WIDTH,
	"height" : WINDOW_HEIGHT,

	"children" :
	(
		{
			"name" : "background",
			"type" : "image",

			"style" : ("movable", "attach",),

			"x" : 0,
			"y" : 0,

			"image" : IMAGE_PATH + "bg.tga",

			"children" :
			(
				{
					"name" : "TitleBar",
					"type" : "titlebar",
					"style" : ("attach",),

					"x" : 6,
					"y" : 5,

					"width" : 243,
					"color" : "red",

					"children" :
					(
						{
							"name" : "TitleName",
							"type" : "text",
							"text" : "Reaction Event",
							"horizontal_align" : "center",
							"text_horizontal_align" : "center",
							"x" : 0,
							"y" : 3,
						},
					),
				},

				{
					"name" : "Field1",
					"type" : "image",

					"x" : 36,
					"y" : 100,

					"image" : IMAGE_PATH + "field_1.tga",

					"children" :
					(
						{
							"name" : "InputNumber",
							"type" : "text",

							"x" : 0,
							"y" : 4,

							# "width" : 179,
							# "height" : 23,

							"horizontal_align" : "center",
							"text_horizontal_align" : "center",
						},
					),
				},

				# {
				# 	"name" : "Field2",
				# 	"type" : "image",

				# 	"x" : 36,
				# 	"y" : 299,

				# 	"image" : IMAGE_PATH + "field_2.tga",

				# 	"children" :
				# 	(
						# {
							# "name" : "InputWord",
							# "type" : "editline",

							# "x" : 2,
							# "y" : 6,

							# "width" : 177,
							# "height" : 21,

							# "text_horizontal_align" : "left",

							# "input_limit" : 25,
						# },
					# ),
				# },

				{
					"name" : "ClearButton",
					"type" : "button",

					"x" : 40,
					"y" : 252,

					"default_image" : IMAGE_PATH + "button_l_normal.tga",
					"over_image" : IMAGE_PATH + "button_l_hover.tga",
					"down_image" : IMAGE_PATH + "button_l_down.tga",

					"text" : "Clear",
				},

				{
					"name" : "EnterButton",
					"type" : "button",

					"x" : 131,
					"y" : 252,

					"default_image" : IMAGE_PATH + "button_l_normal.tga",
					"over_image" : IMAGE_PATH + "button_l_hover.tga",
					"down_image" : IMAGE_PATH + "button_l_down.tga",

					"text" : "Enter",
				},
			),
		},
	),
}
