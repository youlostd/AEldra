root = "d:/ymir work/ui/fraction_wnd/"

window = {
	"name" : "ChooseFractionWindow",

	"x" : 100,
	"y" : 20,

	"style" : ("movable", "float",),

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
