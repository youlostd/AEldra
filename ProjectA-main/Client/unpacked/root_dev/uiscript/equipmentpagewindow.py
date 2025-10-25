import uiScriptLocale

BOARD_WIDTH = 215
BOARD_HEIGHT = 209

window = {
	"name" : "EquipmentPageWindow",

	"x" : SCREEN_WIDTH - 175 - BOARD_WIDTH,
	"y" : SCREEN_HEIGHT - 37 - 480,

	"style" : ("movable", "float",),

	"width" : BOARD_WIDTH,
	"height" : BOARD_HEIGHT,

	"children" :
	(
		{
			"name" : "board",
			"type" : "board",
			"style" : ("attach",),

			"x" : 0,
			"y" : 0,

			"width" : BOARD_WIDTH,
			"height" : BOARD_HEIGHT,
			
			"children" :
			(
				## Title
				{
					"name" : "TitleBar",
					"type" : "titlebar",
					"style" : ("attach",),

					"x" : 6,
					"y" : 6,

					"width" : BOARD_WIDTH - 10,
					"color" : "yellow",

					"children" :
					(
						{ "name":"TitleName", "type":"text", "x":60, "y":3, "text":uiScriptLocale.EQUIPMENT_PAGE_TITLE, "text_horizontal_align":"center" },
					),
				},
				
				## Scrollbar
				{
					"name" : "PageScroll",
					"type" : "scrollbar",
					
					"x" : 15,
					"y" : 34,
					
					"size" : BOARD_HEIGHT - 34 - 15,
				},
				
				## Page list
				{
					"name" : "PageList",
					"type" : "listboxex",
					
					"x" : 35,
					"y" : 37,
					
					"width" : BOARD_WIDTH - 35 - 10 - 10,
					"height" : BOARD_HEIGHT - 34 - 15,
					
					"itemsize_x" : BOARD_WIDTH - 35 - 10 - 10,
					"itemsize_y" : 32,
					
					"itemstep" : 32,
					
					"viewcount" : (BOARD_HEIGHT - 34 - 15) / 32,
				},
				
				# Disable Window
				{
					"name" : "TimeoutWindow",
					
					"x" : 35,
					"y" : 34,
					
					"width" : BOARD_WIDTH - 35 - 10,
					"height" : BOARD_HEIGHT - 34 - 15,
					
					"children" :
					(
						{
							"name" : "TimeoutAnimation",
							"type" : "ani_image",
							
							"x" : (BOARD_WIDTH - 35 - 10) / 2 - 16 / 2,
							"y" : (BOARD_HEIGHT - 34 - 15) / 2 - 16 / 2,
							
							"delay" : 6,
							
							"images" : (
								"locale/de/ui/select/loading/00.tga",
								"locale/de/ui/select/loading/01.tga",
								"locale/de/ui/select/loading/02.tga",
								"locale/de/ui/select/loading/03.tga",
								"locale/de/ui/select/loading/04.tga",
								"locale/de/ui/select/loading/05.tga",
								"locale/de/ui/select/loading/06.tga",
								"locale/de/ui/select/loading/07.tga",
							),
						},
					),
				},
			),
		},
	),
}
