import uiScriptLocale


WINDOW_WIDTH = 253
WINDOW_HEIGHT = 265


window = {
	"name" : "SkillColorWindow",

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

			"style" : ("attach",),

			"x" : 0,
			"y" : 0,

			"image" : "d:/ymir work/ui/game/skillcolor/bg.tga",

			"children" :
			(
				## Title
				{
					"name" : "TitleBar",
					"type" : "titlebar",
					"style" : ("attach",),

					"x" : 6,
					"y" : 6,

					"width" : WINDOW_WIDTH - 11,

					"children" :
					(
						{ "name" : "TitleName", "type" : "text", "x" : 0, "y" : -1, "text" : uiScriptLocale.SKILL_COLOR, "all_align" : "center" },
					),
				},
				{
					"name" : "ColorBar0",
					"type" : "image",

					"x" : 26,
					"y" : 51,

					"image" : "d:/ymir work/ui/game/skillcolor/color_red.tga",
				},
				{
					"name" : "ColorBar1",
					"type" : "image",

					"x" : 26,
					"y" : 51 + 21,

					"image" : "d:/ymir work/ui/game/skillcolor/color_green.tga",
				},
				{
					"name" : "ColorBar2",
					"type" : "image",

					"x" : 26,
					"y" : 51 + 21 * 2,

					"image" : "d:/ymir work/ui/game/skillcolor/color_blue.tga",
				},
				{
					"name" : "LayerBtn0",
					"type" : "radio_button",

					"x" : 26,
					"y" : 152,

					"default_image" : "d:/ymir work/ui/game/skillcolor/btn_small.tga",
					"over_image" : "d:/ymir work/ui/game/skillcolor/btn_small_hover.tga",
					"down_image" : "d:/ymir work/ui/game/skillcolor/btn_small_down.tga",

					"text" : "I",
				},
				{
					"name" : "LayerBtn1",
					"type" : "radio_button",

					"x" : 26 + 42,
					"y" : 152,

					"default_image" : "d:/ymir work/ui/game/skillcolor/btn_small.tga",
					"over_image" : "d:/ymir work/ui/game/skillcolor/btn_small_hover.tga",
					"down_image" : "d:/ymir work/ui/game/skillcolor/btn_small_down.tga",

					"text" : "II",
				},
				{
					"name" : "LayerBtn2",
					"type" : "radio_button",

					"x" : 26 + 42 * 2,
					"y" : 152,

					"default_image" : "d:/ymir work/ui/game/skillcolor/btn_small.tga",
					"over_image" : "d:/ymir work/ui/game/skillcolor/btn_small_hover.tga",
					"down_image" : "d:/ymir work/ui/game/skillcolor/btn_small_down.tga",

					"text" : "III",
				},
				{
					"name" : "LayerBtn3",
					"type" : "radio_button",

					"x" : 26 + 42 * 3,
					"y" : 152,

					"default_image" : "d:/ymir work/ui/game/skillcolor/btn_small.tga",
					"over_image" : "d:/ymir work/ui/game/skillcolor/btn_small_hover.tga",
					"down_image" : "d:/ymir work/ui/game/skillcolor/btn_small_down.tga",

					"text" : "IV",
				},
				{
					"name" : "LayerBtn4",
					"type" : "radio_button",

					"x" : 26 + 42 * 4,
					"y" : 152,

					"default_image" : "d:/ymir work/ui/game/skillcolor/btn_small.tga",
					"over_image" : "d:/ymir work/ui/game/skillcolor/btn_small_hover.tga",
					"down_image" : "d:/ymir work/ui/game/skillcolor/btn_small_down.tga",

					"text" : "V",
				},
				{
					"name" : "SaveButton",
					"type" : "button",
					"x" : 32,
					"y" : 198,
					"text" : uiScriptLocale.SAVE,
					"default_image" : "d:/ymir work/ui/game/skillcolor/btn_normal.tga",
					"over_image" : "d:/ymir work/ui/game/skillcolor/btn_hover.tga",
					"down_image" : "d:/ymir work/ui/game/skillcolor/btn_down.tga",
				},
				{
					"name" : "StandardButton",
					"type" : "button",
					"x" : 137,
					"y" : 198,
					"text" : uiScriptLocale.STANDARD,
					"default_image" : "d:/ymir work/ui/game/skillcolor/btn_normal.tga",
					"over_image" : "d:/ymir work/ui/game/skillcolor/btn_hover.tga",
					"down_image" : "d:/ymir work/ui/game/skillcolor/btn_down.tga",
				},
				{
					"name" : "ColorBoxImg",
					"type" : "image",

					"style" : ("movable", "attach",),

					"x" : 132,
					"y" : 115,

					"image" : "d:/ymir work/ui/game/skillcolor/color_box.tga",

					"children" :
					(
						{
							"name" : "Text",
							"type" : "text",
							"x" : -80,
							"y" : -1,
							"text" : uiScriptLocale.SKILL_COLOR_CURRENT,
							"all_align" : "center"
						},

						{
							"name" : "ColorBar",
							"type" : "bar",

							"x" : 1,
							"y" : 1,

							"width" : 69,
							"height" : 14,
						},
					),
				},

			),
		},
	),
}
