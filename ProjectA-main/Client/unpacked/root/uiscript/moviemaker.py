ROOT_PATH = "d:/ymir work/ui/public/"
BOARD_WIDTH=180
BOARD_HEIGHT=270
window = {
	"name" : "MovieMakerDialog",

	"x" : SCREEN_WIDTH - BOARD_WIDTH + 23,
	"y" : SCREEN_HEIGHT - BOARD_HEIGHT - 43,

	"style" : ("movable", "float",),

	"width" : BOARD_WIDTH,
	"height" : BOARD_HEIGHT,

	"children" :
	(
		{
			"name" : "board",
			"type" : "board_with_titlebar",
			"style" : ("attach",),

			"x" : 0,
			"y" : 0,

			"width" : BOARD_WIDTH,
			"height" : BOARD_HEIGHT,
			
			"title" : "MovieMaker",
			
			"children" :
			(
				# Camera Positions
				{
					"name" : "pos",
					"type" : "window",
					"x" : 0,
					"y" : 30+30,
					"height" : 50,
					"width": BOARD_WIDTH,
					"children" : 
					(
						{
							"name" : "topic",
							"type" : "extended_text",
							"x" : 0,
							"y" : 0,
							"text" : "Camera Positions",
							"horizontal_align" : "center",
						},
						{
							"name" : "objects_lbl",
							"type" : "extended_text",
							"x" : 0,
							"y" : 20,
							"text" : "12/100",
							"horizontal_align" : "center",
						},
						{
							"name" : "pos_left_btn",
							"type" : "button",
							"x" : 25,
							"y" : 20,
							"text" : "<",
							"default_image" : ROOT_PATH + "Small_Button_01.sub",
							"over_image" : ROOT_PATH + "Small_Button_02.sub",
							"down_image" : ROOT_PATH + "Small_Button_03.sub",
						},
						{
							"name" : "pos_right_btn",
							"type" : "button",
							"x" : BOARD_WIDTH - 24 - 25,
							"y" : 20,
							"text" : ">",
							"default_image" : ROOT_PATH + "Small_Button_01.sub",
							"over_image" : ROOT_PATH + "Small_Button_02.sub",
							"down_image" : ROOT_PATH + "Small_Button_03.sub",
						},
					),
				},

				# Edit 
				{
					"name" : "editWnd",
					"type" : "window",
					"x" : 0,
					"y" : 80+30,
					"height" : 50,
					"width": BOARD_WIDTH,
					"children" : 
					(
						{
							"name" : "topic",
							"type" : "extended_text",
							"x" : 0,
							"y" : 0,
							"text" : "Edit / Remove cur Pos",
							"horizontal_align" : "center",
						},

						## Input Slot
						{
							"name" : "InputSlot",
							"type" : "slotbar",

							"x" : 19,
							"y" : 22,
							"width" : 50,
							"height" : 18,

							"children" :
							(
								{
									"name" : "edit_input",
									"type" : "editline",
									"x" : 3,
									"y" : 3,
									"width" : 50,
									"height" : 18,
									"input_limit" : 6,
									"text":"14.0",
								},
							),
						},
						{
							"name" : "edit_save_btn",
							"type" : "button",
							"x" : BOARD_WIDTH - 24 - 25 - 25 - 2,
							"y" : 20,
							"text" : "E",
							"default_image" : ROOT_PATH + "Small_Button_01.sub",
							"over_image" : ROOT_PATH + "Small_Button_02.sub",
							"down_image" : ROOT_PATH + "Small_Button_03.sub",
						},
						{
							"name" : "remove_btn",
							"type" : "button",
							"x" : BOARD_WIDTH - 24 - 25,
							"y" : 20,
							"text" : "X",
							"default_image" : ROOT_PATH + "Small_Button_01.sub",
							"over_image" : ROOT_PATH + "Small_Button_02.sub",
							"down_image" : ROOT_PATH + "Small_Button_03.sub",
						},
					),
				},

				# Add
				{
					"name" : "pos",
					"type" : "window",
					"x" : 0,
					"y" : 130+30,
					"height" : 50,
					"width": BOARD_WIDTH,
					"children" : 
					(
						{
							"name" : "topic",
							"type" : "extended_text",
							"x" : 0,
							"y" : 0,
							"text" : "Add Position",
							"horizontal_align" : "center",
						},

						## Input Slot
						{
							"name" : "InputSlot",
							"type" : "slotbar",

							"x" : 19,
							"y" : 22,
							"width" : 50,
							"height" : 18,

							"children" :
							(
								{
									"name" : "add_input",
									"type" : "editline",
									"x" : 3,
									"y" : 3,
									"width" : 50,
									"height" : 18,
									"input_limit" : 6,
									"text":"4.0",
								},
							),
						},

						{
							"name" : "add_btn",
							"type" : "button",
							"x" : BOARD_WIDTH - 24 - 25,
							"y" : 20,
							"text" : "Add",
							"default_image" : ROOT_PATH + "Small_Button_01.sub",
							"over_image" : ROOT_PATH + "Small_Button_02.sub",
							"down_image" : ROOT_PATH + "Small_Button_03.sub",
						},
					),
				},

				# Others
				{
					"name" : "play_sel_btn",
					"type" : "button",
					"x" : ((BOARD_WIDTH - 50)  / 2) - 32 - 5,
					"y" : BOARD_HEIGHT - 25 - 25,
					"text" : "Play",
					"default_image" : ROOT_PATH + "Middle_Button_01.sub",
					"over_image" : ROOT_PATH + "Middle_Button_02.sub",
					"down_image" : ROOT_PATH + "Middle_Button_03.sub",
				},

				{
					"name" : "play_all_btn",
					"type" : "button",
					"x" : ((BOARD_WIDTH - 50)  / 2) + 32 - 5,
					"y" : BOARD_HEIGHT - 25 - 25,
					"text" : "Movie",
					"default_image" : ROOT_PATH + "Middle_Button_01.sub",
					"over_image" : ROOT_PATH + "Middle_Button_02.sub",
					"down_image" : ROOT_PATH + "Middle_Button_03.sub",
				},

	
			),
		},
	),
}