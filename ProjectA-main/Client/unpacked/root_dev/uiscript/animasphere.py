import app
import constInfo

if constInfo.NEW_MINIMAP_UI:
	ZODIAC = "d:/ymir work/ui/minimap_new/"

	window = {
		"name" : "AnimasphereZI",

		"x" : (SCREEN_WIDTH - 135),
		"y" : 9,

		"style" : ("movable", "float",),

		"width" : 28,
		"height" : 28,

		"children" :
		(
			{
				"name" : "LabadeUrs",
				"type" : "window",

				"x" : 0,
				"y" : 0,

				"width" : 28,
				"height" : 28,

				"children" :
				(
			
					# BGAnimasphere
					{
						"name" : "AnimasphereDesign",
						"type" : "radio_button",

						"x" : 2,
						"y" : 2,

						"default_image" : ZODIAC + "btn_dr_normal.tga",
						"over_image" : ZODIAC + "btn_dr_hover.tga",
						"down_image" : ZODIAC + "btn_dr_down.tga",
					},
					# Animasphere Count
					{
						"name" : "Animasphere2",
						"type" : "text",
						"x" : 17,
						"y" : 8 + 5 + 3,
						"outline" : 1,
						"text_horizontal_align" : "center",
						"text" : "0",
					},

				),
			},
		),
	}
else:
	ZODIAC = "d:/ymir work/ui/zodiac/12zi/"

	window = {
		"name" : "AnimasphereZI",

		"x" : (SCREEN_WIDTH - 135),
		"y" : -2,

		"style" : ("movable", "float",),

		"width" : 50,
		"height" : 50,

		"children" :
		(
			{
				"name" : "LabadeUrs",
				"type" : "window",

				"x" : 0,
				"y" : 0,

				"width" : 50,
				"height" : 50,

				"children" :
				(
			
					# BGAnimasphere
					{
						"name" : "AnimasphereDesign",
						"type" : "radio_button",

						"x" : 2,
						"y" : 2,

						"default_image" : ZODIAC + "bead/bead_default.sub",
						"over_image" : ZODIAC + "bead/bead_over.sub",
						"down_image" : ZODIAC + "bead/bead_default.sub",
					},
					# Animasphere Count
					{
						"name" : "Animasphere2",
						"type" : "text",
						"x" : 17,
						"y" : 8 + 5 + 3,
						"outline" : 1,
						"text_horizontal_align" : "center",
						"text" : "0",
					},

				),
			},
		),
	}
