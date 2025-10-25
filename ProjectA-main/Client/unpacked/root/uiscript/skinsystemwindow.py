import uiScriptLocale
import item

window = {
	"name" : "CostumeWindow",

	"x" : SCREEN_WIDTH - 185 - 146 - 113,
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
			
			"title" : uiScriptLocale.SKINSYSTEM_TITLE,
			
			"children" :
			(
				## Equipment Slot
				{
					"name" : "Costume_Base",
					"type" : "image",

					"x" : 0,
					"y" : 0,
					
					"image" : "d:/ymir work/ui/game/skinsystem/costume_bg_s.tga",

					"children" :
					(
						{
							"name" : "SlotBuffiWeapon",
							"type" : "grid_table",

							"x" : 15,
							"y" : 21,

							"start_index" : item.SKINSYSTEM_SLOT_BUFFI_WEAPON,
							"x_count" : 1,
							"y_count" : 2,
							"x_step" : 32,
							"y_step" : 32,
						},

						{
							"name" : "SlotPet",
							"type" : "grid_table",

							"x" : 15,
							"y" : 91,

							"start_index" : item.SKINSYSTEM_SLOT_PET,
							"x_count" : 1,
							"y_count" : 1,
							"x_step" : 32,
							"y_step" : 32,
						},

						{
							"name" : "SlotMount",
							"type" : "grid_table",

							"x" : 61,
							"y" : 91,

							"start_index" : item.SKINSYSTEM_SLOT_MOUNT,
							"x_count" : 1,
							"y_count" : 1,
							"x_step" : 32,
							"y_step" : 32,
						},

						{
							"name" : "SlotBuffiBody",
							"type" : "grid_table",

							"x" : 61,
							"y" : 21,

							"start_index" : item.SKINSYSTEM_SLOT_BUFFI_BODY,
							"x_count" : 1,
							"y_count" : 2,
							"x_step" : 32,
							"y_step" : 32,
						},

					),
				},

			),
		},
	),
}
