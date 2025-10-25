import localeInfo

WIDTH 	= 368
HEIGHT 	= 328
root = "d:/ymir work/ui/fraction_wnd/"

window = {
	"name" : "ChooseFractionWindow",

	"x" : ( SCREEN_WIDTH - WIDTH ) / 2,
	"y" : ( SCREEN_HEIGHT - HEIGHT ) / 2,

	"style" : ( "movable", "float", ),

	"width" : WIDTH,
	"height" : HEIGHT,

	"children" :
	(
		{
			"name" : "background",
			"type" : "image",
			"style" : ("attach",),

			"x" : 0,
			"y" : 0,

			"image" : root+"angel_selection_2.tga",

			"children" :
			(
				## TITLE BAR
				{
					"name" : "title_bar",
					"type" : "titlebar",
					"style" : ("attach",),

					"x" : 8,
					"y" : 8,

					"width" : WIDTH - 16,
					"color" : "red",

					"children" :
					(
						{
							"name" : "title_name",
							"type" : "text",
							"text" : localeInfo.ANGELSDEMONS_TITLE,
							"horizontal_align" : "center",
							"text_horizontal_align" : "center",
							"x" : 0,
							"y" : 3,
						},
					),
				},

				## FRACTION DESCRIPTIONS
				{
					"name" : "description_angels",
					"type" : "multi_text",

					"x" : 36,
					"y" : 56+80,

					"text_horizontal_align" : "center",

					"vertical_align" : "top",
					"horizontal_align" : "left",
					"outline" : 1,
					"color" : "blue",

					"text" : localeInfo.ANGELSDEMONS_DESC_ANGELS,
				},

				{
					"name" : "description_demons",
					"type" : "multi_text",

					"x" : 36 + 130,
					"y" : 56+80,

					"text_horizontal_align" : "center",

					"vertical_align" : "top",
					"horizontal_align" : "right",
					"outline" : 1,
					"color" : "blue",

					"text" : localeInfo.ANGELSDEMONS_DESC_DEMONS,
				},

				## BUTTONS TEAM CHOOSE
				{
					"name" : "button_join_angels",
					"type" : "button",

					"x" : 55,
					"y" : 40+225,

					"vertical_align" : "bottom",
					"horizontal_align" : "left",

					"default_image" : "d:/ymir work/ui/game/angels_demons/btn_normal.tga",
					"over_image" : "d:/ymir work/ui/game/angels_demons/btn_hover.tga",
					"down_image" : "d:/ymir work/ui/game/angels_demons/btn_down.tga",

					"text" : localeInfo.JOIN,
				},

				{
					"name" : "button_join_demons",
					"type" : "button",

					"x" : 55 + 82,
					"y" : 40+225,

					"vertical_align" : "bottom",
					"horizontal_align" : "right",

					"default_image" : "d:/ymir work/ui/game/angels_demons/btn_normal.tga",
					"over_image" : "d:/ymir work/ui/game/angels_demons/btn_hover.tga",
					"down_image" : "d:/ymir work/ui/game/angels_demons/btn_down.tga",

					"text" : localeInfo.JOIN,
				},
			),
		},
	),
}