import uiScriptLocale
import item

COSTUME_START_INDEX = item.COSTUME_SLOT_START

window = {
	"name" : "CostumeWindow",

	"x" : SCREEN_WIDTH - 185 - 146,
	"y" : SCREEN_HEIGHT - 37 - 565,

	"style" : ("movable", "float",),

	"width" : 147,
	"height" : 129,

	"children" :
	(
		{
			"name" : "board",
			"type" : "board_with_titlebar",
			"style" : ("attach",),

			"x" : 0,
			"y" : 0,

			"width" : 147,
			"height" : 129,
			
			"title" : uiScriptLocale.COSTUME_WINDOW_TITLE,
			"children" :
			(
				## Equipment Slot
				{
					"name" : "Costume_Base",
					"type" : "image",

					"x" : 0,
					"y" : 0,
					
					"image" : uiScriptLocale.LOCALE_UISCRIPT_PATH + "costume/costume_bg_n_new.tga",

					"children" :
					(

						{
							"name" : "CostumeSlot",
							"type" : "slot",

							"x" : 0,
							"y" : 0,

							"width" : 147,
							"height" : 129,

							"slot" : (
										{"index":COSTUME_START_INDEX+0, "x":65, "y":48, "width":32, "height":64},
										{"index":COSTUME_START_INDEX+1, "x":65, "y":12, "width":32, "height":32},
										{"index":COSTUME_START_INDEX+2, "x":16, "y":16, "width":32, "height":96},
										{"index":item.COSTUME_SLOT_ACCE_CUSTOME, "x":109, "y":12, "width":32, "height":32}
									),
						},
					),
				},

			),
		},
	),
}
