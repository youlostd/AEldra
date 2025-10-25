root = "d:/ymir work/ui/fraction_wnd/"

window = {
	"name" : "ChooseFractionWindow",

	"x" : (SCREEN_WIDTH  - 335) /2,
	"y" : 50,

	"style" : ("float",),

	"width" : 335,
	"height" : 119,

	"children" :
	(
		{
			"name" : "header",
			"type" : "image",
			"style" : ("attach",),
			"horizontal_align" : "center",
			"x" : 0,
			"y" : 0,

			"image" : root+"wings_bg.tga",
			"children" : 
			(
				{
					"name" : "button",
					"type" : "button",
					
					"horizontal_align" : "center",
					"x" : 8,
					"y" : 85,
					"default_image" : root+"dropdown_btn_normal.tga",
					"over_image" : root+"dropdown_btn_hover.tga",
					"down_image" : root+"dropdown_btn_normal.tga",
				},
				{
					"name" : "first_text",
					"type" : "text",

					"horizontal_align" : "center",
					"x" : -39,
					"y" : 30,
					"text" : "Angel vs Demon",
					"fontname" : "Tahoma:16",
				},
				{
					"name" : "second_text",
					"type" : "text",

					"horizontal_align" : "center",
					"x" : -87,
					"y" : 66,
					"text" : "Defeat the Enemy Fraction Boss",
					"fontname" : "Tahoma:16",
				},
				{
					"name" : "red_bar",
					"type" : "expanded_image",

					"x" : 167-42,
					"y" : 54,
					"image" : root + "bar_red.tga",
				},
				{
					"name" : "blue_bar",
					"type" : "expanded_image",

					"x" : 167-42,
					"y" : 54,
					"image" : root + "bar_blue.tga",
					"children" : 
					(
						{
							"name" : "ball",
							"type" : "expanded_image",

							# "horizontal_align" : "center",
							"x" : 0,
							"y" : -7,
							"image" : root + "ball.tga",
						},
					),
				},
			),
		},
		{
			"name" : "board",
			"type" : "image",
			"style" : ("attach",),
			"x" : 0,
			"y" : 119,

			"image" : root+"slots_bg.tga",
		},
	),
}
