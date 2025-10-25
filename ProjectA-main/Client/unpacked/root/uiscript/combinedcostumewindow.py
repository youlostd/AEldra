import uiScriptLocale
import item
import player

COSTUME_START_INDEX = item.COSTUME_SLOT_START

window = {
	"name" : "CostumeWindow",

	"x" : SCREEN_WIDTH - 185 - 237,
	"y" : SCREEN_HEIGHT - 37 - 565,

	"style" : ("movable", "float",),

	"width" : 236,
	"height" : 338,

	"children" :
	(
		{
			"name" : "board",
			"type" : "expanded_image",
			"style" : ("attach",),

			"x" : 0,
			"y" : 0,
			
			"image" : "D:/Ymir Work/ui/game/costume_window/combine_ui_bg.tga",
			"children" :
			(
				{
					"name" : "CostumeWindowText",
					"type" : "text",

					"text_horizontal_align": "center",
					"text_vertical_align" : "center",
					"x" : 54 + 64,
					"y" : 41 + 5,

					"text" : uiScriptLocale.COSTUME_WINDOW_TITLE,
				},
				{
					"name" : "ShiningWindowText",
					"type" : "text",

					"text_horizontal_align": "center",
					"text_vertical_align" : "center",
					"x" : 136 + 44,
					"y" : 171 + 6,

					"text" : uiScriptLocale.SHINING_WINDOW_TITLE,
				},
				{
					"name" : "SkinWindowText",
					"type" : "text",

					"text_horizontal_align": "center",
					"text_vertical_align" : "center",
					"x" : 15 + 44,
					"y" : 171 + 6,

					"text" : uiScriptLocale.SKINSYSTEM_TITLE,
				},
				{
					"name" : "CostumeSlot",
					"type" : "slot",

					"x" : 0,
					"y" : 0,
					"width" : 236,
					"height" : 338,

					"slot" : (
							{"index":COSTUME_START_INDEX+0, "x":107, "y":96, "width":32, "height":64},
							{"index":COSTUME_START_INDEX+1, "x":107, "y":60, "width":32, "height":32},
							{"index":COSTUME_START_INDEX+2, "x":58, "y":64, "width":32, "height":96},
							{"index":item.COSTUME_SLOT_ACCE_CUSTOME, "x":149, "y":60, "width":32, "height":32},
							{"index":item.SKINSYSTEM_SLOT_BUFFI_WEAPON, "x":15, "y":208, "width":32, "height":32*2},
							{"index":item.SKINSYSTEM_SLOT_PET, "x":15, "y":278, "width":32, "height":32},
							{"index":item.SKINSYSTEM_SLOT_MOUNT, "x":61, "y":282, "width":32, "height":32},
							{"index":item.SKINSYSTEM_SLOT_BUFFI_BODY, "x":61, "y":220, "width":32, "height":32*2},
							{"index":item.SKINSYSTEM_SLOT_BUFFI_HAIR, "x":61, "y":189, "width":32, "height":32},
							{"index":player.SHINING_EQUIP_SLOT_START, "x":175, "y":221, "width":32, "height":32},
							{"index":player.SHINING_EQUIP_SLOT_START+1, "x":175, "y":221+32, "width":32, "height":32},
							{"index":player.SHINING_EQUIP_SLOT_START+2, "x":129, "y":221, "width":32, "height":32},
							{"index":player.SHINING_EQUIP_SLOT_START+3, "x":129, "y":221+32, "width":32, "height":32},
					),
				},
			),
		},
	),
}
