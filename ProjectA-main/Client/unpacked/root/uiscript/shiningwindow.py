import uiScriptLocale
import player

SHINING_START_INDEX = player.SHINING_EQUIP_SLOT_START

window = {
	"name" : "ShiningWindow",

	"x" : SCREEN_WIDTH - 185 - 114,
	"y" : SCREEN_HEIGHT - 37 - 565,

	"style" : ("movable", "float",),

	"width" : 113,
	"height" : 129,

	"children" :
	(
		{
			"name" : "board",
			"type" : "board_with_titlebar",
			"style" : ("attach",),

			"x" : 0,
			"y" : 0,

			"width" : 113,
			"height" : 129,
			
			"title" : uiScriptLocale.SHINING_WINDOW_TITLE,
			"children" :
			(
				## Equipment Slot
				{
					"name" : "Shining_Base",
					"type" : "image",

					"x" : 0,
					"y" : 0,
					
					"image" : "d:/ymir work/ui/shining_slot_bg.tga",

					"children" :
					(
						{
							"name" : "ShiningSlotArmor",
							"type" : "grid_table",

							"x" : 61,
							"y" : 33,

							"start_index" : SHINING_START_INDEX,
							"x_count" : 1,
							"y_count" : 2,
							"x_step" : 32,
							"y_step" : 32,

							#"image" : "d:/ymir work/ui/public/Slot_Base.sub",
						},

						{
							"name" : "ShiningSlotWeapon",
							"type" : "grid_table",

							"x" : 15,
							"y" : 33,

							"start_index" : SHINING_START_INDEX + 2,
							"x_count" : 1,
							"y_count" : 2,
							"x_step" : 32,
							"y_step" : 32,

							#"image" : "d:/ymir work/ui/public/Slot_Base.sub",
						},
					),
				},
			),
		},
	),
}
