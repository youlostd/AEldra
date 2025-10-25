import uiScriptLocale
import player
import constInfo

IMAGE_PATH = "d:/ymir work/ui/game/eqchanger/"
RUNE_BASE_PATH = "d:/ymir work/ui/game/runes/"
WINDOW_WIDTH = 513
WINDOW_HEIGHT = 263

EQUIPMENT_START_INDEX = player.EQUIPMENT_SLOT_START
LOCALE_PATH = constInfo.GetCharacterWindowPath()

window = {
	"name" : "EquipmentChangerWindow",

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
				## Title
				{
					"name" : "titlebar",
					"type" : "titlebar",
					"style" : ("attach",),

					"x" : 3,
					"y" : 6,

					"width" : WINDOW_WIDTH - 9,
					"children" :
					(
						{ "name":"TitleName", "type":"text", "x":0, "horizontal_align":"center","text_horizontal_align":"center", "y":3, "text":uiScriptLocale.EQUIPMENT_PAGE_TITLE, "text_horizontal_align":"center" },
					),
				},

				# {
				# 	"name" : "SaveButton",
				# 	"type" : "button",

				# 	"x" : -50,
				# 	"y" : 55,

				# 	"horizontal_align" : "center",
				# 	"vertical_align" : "bottom",

				# 	"text" : "Save",

				# 	"default_image" : IMAGE_PATH + "btn_normal.tga",
				# 	"over_image" : IMAGE_PATH + "btn_hover.tga",
				# 	"down_image" : IMAGE_PATH + "btn_down.tga",
				# },
				# {
				# 	"name" : "LoadButton",
				# 	"type" : "button",

				# 	"x" : 50,
				# 	"y" : 55,

				# 	"horizontal_align" : "center",
				# 	"vertical_align" : "bottom",

				# 	"text" : "Load",

				# 	"default_image" : IMAGE_PATH + "btn_normal.tga",
				# 	"over_image" : IMAGE_PATH + "btn_hover.tga",
				# 	"down_image" : IMAGE_PATH + "btn_down.tga",
				# },
				{
					"name" : "rune_page_circle",
					"type" : "radio_button",

					"x" : 150-40-5,
					"y" : 55+44+5,

					"vertical_align" : "bottom",

					"default_image" : RUNE_BASE_PATH + "btn_page.tga",
					"disable_image" : RUNE_BASE_PATH + "btn_page.tga",

					"text" : "",

					"tooltip_text" : uiScriptLocale.RUNE_MAIN_TITLE,
				},
				{
					"name" : "InfoButton",
					"type" : "button",

					"x" : 60,
					"y" : 55,

					"horizontal_align" : "right",
					"vertical_align" : "bottom",

					"default_image" : IMAGE_PATH + "info_normal.tga",
					"over_image" : IMAGE_PATH + "info_hover.tga",
					"down_image" : IMAGE_PATH + "info_hover.tga",
				},
				{
					"name" : "EquipmentSlot",
					"type" : "slot",

					"x" : 24,
					"y" : 47,

					"width" : 155,
					"height" : 187,

					"slot" : (
								{"index":0, "x":41, "y":36, "width":32, "height":64},
								{"index":1, "x":41, "y":4, "width":32, "height":32},
								{"index":2, "x":41, "y":147, "width":32, "height":32},
								{"index":3, "x":77, "y":68, "width":32, "height":32},
								{"index":4, "x":5, "y":4, "width":32, "height":96},
								{"index":5, "x":117, "y":68, "width":32, "height":32},
								{"index":6, "x":117, "y":36, "width":32, "height":32},
								{"index":7, "x":117, "y":4, "width":32, "height":32},
								{"index":8, "x":77, "y":36, "width":32, "height":32},
								{"index":12, "x":78, "y":4, "width":32, "height":32},
								{"index":13, "x":41, "y":108, "width":32, "height":32},
								{"index":14, "x":5, "y":108, "width":32, "height":32},
							),
				},
				{
					"name" : "EquipmentCostumesSlot",
					"type" : "slot",

					"x" : 24+358,
					"y" : 47+8,

					"width" : 96,
					"height" : 100,

					"slot" : (
								{"index":9, "x":41+13, "y":36-1, "width":32, "height":64},
								{"index":11, "x":5, "y":4+4, "width":32, "height":96},
								{"index":10, "x":41+13, "y":4-1, "width":32, "height":32},
							),
				},
				{
					"name" : "hotkey_button",
					"type" : "button",

					"x" : 150-40-5,
					"y" : 55+8,

					"vertical_align" : "bottom",

					"default_image" : "d:/ymir work/ui/public/Middle_Button_01.sub",
					"over_image" : "d:/ymir work/ui/public/Middle_Button_02.sub",
					"down_image" : "d:/ymir work/ui/public/Middle_Button_03.sub",

					"text" : "None",
				},
			),
		},
	),
}
