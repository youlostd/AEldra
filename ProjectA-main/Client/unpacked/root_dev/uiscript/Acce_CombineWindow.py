import uiScriptLocale
import item
import app

COSTUME_START_INDEX = item.COSTUME_SLOT_START
    
window = {
	"name" : "Acce_CombineWindow",

	"x" : 0,
	"y" : 0,

	"style" : ("movable", "float",),

	"width" : 215,
	"height" : 270,

	"children" :
	(
		{
			"name" : "board",
			"type" : "board_with_titlebar",
			"style" : ("attach",),

			"x" : 0,
			"y" : 0,

			"width" : 215,
			"height" : 270,

			"title" : uiScriptLocale.ACCE_COMBINE,
		
			"children" :
			(
				## Slot
				{
					"name" : "Acce_Combine",
					"type" : "image",
					
					"x" : 9,
					"y" : 35,
					
					"image" : "d:/ymir work/ui/acce/acce_combine.tga",
					
					"children" :
					(
						{
							"name" : "AcceSlot",
							"type" : "slot",
					
							"x" : 3,
							"y" : 3,
					
							"width" : 200,
							"height" : 150,
					
							"slot" : (
								{"index":0, "x":78, "y":7, "width":32, "height":32},  # 메인
								{"index":1, "x":78, "y":60, "width":32, "height":32},  # 서브
								{"index":2, "x":78, "y":115, "width":32, "height":32}, # 결과
							),
						},
						## Help Text
						{
							"name" : "Main", "type" : "text", "text" : uiScriptLocale.ACCE_MAIN, "text_horizontal_align":"center", "x" : 85+12, "y" : 7+36,
						},
						{
							"name" : "serve", "type" : "text", "text" : uiScriptLocale.ACCE_SERVE, "text_horizontal_align":"center", "x" : 85+12, "y" : 60+38,
						},
						{
							"name" : "Result", "type" : "text", "text" : uiScriptLocale.ACCE_RESULT, "text_horizontal_align":"center", "x" : 85+12, "y" : 115+40
						},

					),
				},
				## 비용
				{
					"name" : "Cost",
					"type" : "text",
					"text" : "",
					"text_horizontal_align" : "center",
					"x" : 105,
					"y" : 215,
				},
				## Button
				{
					"name" : "AcceptButton",
					"type" : "button",

					"x" : 40,
					"y" : 235,

					"text" : uiScriptLocale.OK,

					"default_image" : "d:/ymir work/ui/public/middle_button_01.sub",
					"over_image" : "d:/ymir work/ui/public/middle_button_02.sub",
					"down_image" : "d:/ymir work/ui/public/middle_button_03.sub",
				},
				{
					"name" : "CancelButton",
					"type" : "button",

					"x" : 114,
					"y" : 235,

					"text" : uiScriptLocale.CANCEL,

					"default_image" : "d:/ymir work/ui/public/middle_button_01.sub",
					"over_image" : "d:/ymir work/ui/public/middle_button_02.sub",
					"down_image" : "d:/ymir work/ui/public/middle_button_03.sub",
				},				
			),
		},
	),
}

