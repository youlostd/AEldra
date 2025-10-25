import uiScriptLocale

IMAGE_PATH = "d:/ymir work/ui/battlepass/"
WINDOW_WIDTH = 471
WINDOW_HEIGHT = 338

window = {
	"name" : "BattlePassWindow",

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
				{
					"name" : "TitleBar",
					"type" : "titlebar",
					"style" : ("attach",),

					"x" : 6,
					"y" : 5,

					"width" : WINDOW_WIDTH - 10,
					"color" : "red",

					"children" :
					(
						{
							"name" : "TitleName",
							"type" : "text",
							"text" : "BattlePass",
							"horizontal_align" : "center",
							"text_horizontal_align" : "center",
							"x" : 0,
							"y" : 3,
						},
					),
				},
				{
					"name" : "QuestButton",
					"type" : "button",

					"x" : 12,
					"y" : 140,

					"default_image" : IMAGE_PATH + "btn_quests_normal.tga",
					"over_image" : IMAGE_PATH + "btn_quests_hover.tga",
					"down_image" : IMAGE_PATH + "btn_quests_down.tga",
				},
				{
					"name" : "ShopButton",
					"type" : "button",

					"x" : 12,
					"y" : 174,

					"default_image" : IMAGE_PATH + "btn_shop_normal.tga",
					"over_image" : IMAGE_PATH + "btn_shop_hover.tga",
					"down_image" : IMAGE_PATH + "btn_shop_down.tga",
				},
				{
					"name" : "ItemGrid",
					"type" : "grid_table",

					"x" : 114,
					"y" : 134,

					"start_index" : 0,
					"x_count" : 11,
					"y_count" : 6,
					"x_step" : 32,
					"y_step" : 32,

					"image" : "d:/ymir work/ui/public/Slot_Base.sub",
				},
				# {
					# "name" : "ItemGrid2",
					# "type" : "grid_table",

					# "x" : 114 + (5*32),
					# "y" : 134,

					# "start_index" : 30,
					# "x_count" : 5,
					# "y_count" : 6,
					# "x_step" : 32,
					# "y_step" : 32,

					# "image" : "d:/ymir work/ui/public/Slot_Base.sub",
				# },
				# {
				# 	"name" : "ItemGrid",
				# 	"type" : "grid_table",

				# 	"x" : 114 + (5*32),
				# 	"y" : 134,

				# 	"start_index" : 0,
				# 	"x_count" : 11,
				# 	"y_count" : 6,
				# 	"x_step" : 32,
				# 	"y_step" : 32,

				# 	"image" : "d:/ymir work/ui/public/Slot_Base.sub",
				# },
			),
		},
	),
}
