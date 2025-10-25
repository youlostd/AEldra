import uiScriptLocale
import player

window = {
	"name" : "SkillbookInventoryWindow",

	"x" : 100,
	"y" : 20,

	"style" : ("movable", "float",),

	"width" : 176,
	"height" : 421,

	"children" :
	(
		{
			"name" : "board",
			"type" : "board_with_titlebar",
			"style" : ("attach",),

			"x" : 0,
			"y" : 0,

			"width" : 176,
			"height" : 421,

			"title" : uiScriptLocale.SAFE_TITLE,

			"children" :
			(
				{
					"name" : "SkillbookSlot",
					"type" : "grid_table",

					"x" : 8,
					"y" : 35,

					"start_index" : player.SKILLBOOK_INV_SLOT_START,
					"x_count" : 5,
					"y_count" : 10,
					"x_step" : 32,
					"y_step" : 32,

					"image" : "d:/ymir work/ui/public/Slot_Base.sub"
				},
				{
					"name" : "PageButton1",
					"type" : "radio_button",

					"x" : 176 / 2 - 52 - 3,
					"y" : 35 + 32 * 10 + 8,

					"text" : "I",

					"default_image" : "d:/ymir work/ui/game/windows/tab_button_middle_01.sub",
					"over_image" : "d:/ymir work/ui/game/windows/tab_button_middle_02.sub",
					"down_image" : "d:/ymir work/ui/game/windows/tab_button_middle_03.sub",
				},
				{
					"name" : "PageButton2",
					"type" : "radio_button",

					"x" : 176 / 2 + 3,
					"y" : 35 + 32 * 10 + 8,

					"text" : "II",

					"default_image" : "d:/ymir work/ui/game/windows/tab_button_middle_01.sub",
					"over_image" : "d:/ymir work/ui/game/windows/tab_button_middle_02.sub",
					"down_image" : "d:/ymir work/ui/game/windows/tab_button_middle_03.sub",
				},
				{
					"name" : "ExitButton",
					"type" : "button",

					"x" : 0,
					"y" : 35 + 32 * 10 + 8 + 19 + 5,

					"text" : uiScriptLocale.CLOSE,
					"horizontal_align" : "center",

					"default_image" : "d:/ymir work/ui/public/large_button_01.sub",
					"over_image" : "d:/ymir work/ui/public/large_button_02.sub",
					"down_image" : "d:/ymir work/ui/public/large_button_03.sub",
				},
			),
		},
	),
}
