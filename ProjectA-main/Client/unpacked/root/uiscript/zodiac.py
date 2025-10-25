ZODIAC = "d:/ymir work/ui/zodiac/12zi/"
window = {
	"name" : "ZodiacMap",

	"x" : SCREEN_WIDTH - 136,
	"y" : 0,

	"width" : 136,
	"height" : 137,

	"children" :
	(
		{
			"name" : "ZodiacWindow",
			"type" : "window",

			"x" : 0,
			"y" : 0,

			"width" : 136,
			"height" : 137,

			"children" :
			(
				{
					"name" : "ZodiacBG",
					"type" : "image",
					"x" : 0,
					"y" : 0,
					"image" : ZODIAC + "timer/bg_12zi_timer.sub",
				},

				# 
				{ "name":"JumpStep", "type":"text", "x":68, "y":40, "text" : "5", "text_horizontal_align":"center", "r" : 1.0, "g" : 0.0, "b" : 0.0, "a" : 1.0, "fontsize":"LARGE"},
				{ "name":"LeftTime", "type":"text", "x":68, "y":61, "text" : "11:11", "text_horizontal_align":"center" },
				{ "name":"CurrentFloor", "type":"text", "x":68, "y":78, "text" : "5", "text_horizontal_align":"center", "r" : 1.0, "g" : 0.831, "b" : 0.043, "a" : 1.0, "fontsize":"LARGE"},
				#ZODIAC ANIMASPHERE
				# {
					# "name" : "AnimasphereDesign",
					# "type" : "radio_button",

					# "x" : 2,
					# "y" : 2,

					# "default_image" : ZODIAC + "bead/bead_default.sub",
					# "over_image" : ZODIAC + "bead/bead_over.sub",
					# "down_image" : ZODIAC + "bead/bead_default.sub",
					# "children" :
					# (
						# {
							# "name" : "Animasphere",
							# "type" : "text",

							# "x" : 0,
							# "y" : 0,

							# "outline" : 1,

							# "all_align" : "center",

							# "text" : "0",
						# },

					# ),
				# },
			),
		},
	),
}