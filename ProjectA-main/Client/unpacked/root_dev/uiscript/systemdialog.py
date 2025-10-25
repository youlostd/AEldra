import uiScriptLocale
import constInfo
import localeInfo

ROOT = "d:/ymir work/ui/public/"

ADDITION_Y = 0
if constInfo.NEW_PICKUP_FILTER:
	ADDITION_Y += 30

WIKI_ADDITION = 0
if constInfo.ENABLE_INGAME_WIKI:
	WIKI_ADDITION += 30

ADDITION_Y += WIKI_ADDITION

window = {
	"name" : "SystemDialog",
	"style" : ("float",),

	"x" : (SCREEN_WIDTH  - 200) /2,
	"y" : (SCREEN_HEIGHT - 288) /2,

	"width" : 200,
	"height" : 318 - 17 - 17,

	"children" :
	(
		{
			"name" : "board",
			"type" : "thinboard",

			"x" : 0,
			"y" : 0,

			"width" : 200,
			"height" : 318 - 17 - 17,

			"children" :
			(
				{
					"name" : "mall_button",
					"type" : "button",

					"x" : 10,
					"y" : 57 - 17 - 17,

					"text" : uiScriptLocale.SYSTEM_MALL,
					"text_color" : 0xffF8BF24,

					"default_image" : ROOT + "XLarge_Button_02.sub",
					"over_image" : ROOT + "XLarge_Button_02.sub",
					"down_image" : ROOT + "XLarge_Button_02.sub",
				},

				{
					"name" : "system_option_button",
					"type" : "button",

					"x" : 10,
					"y" : 87 - 17 - 17 + WIKI_ADDITION,

					"text" : uiScriptLocale.SYSTEMOPTION_TITLE,

					"default_image" : ROOT + "XLarge_Button_01.sub",
					"over_image" : ROOT + "XLarge_Button_02.sub",
					"down_image" : ROOT + "XLarge_Button_03.sub",
				},
				{
					"name" : "game_option_button",
					"type" : "button",

					"x" : 10,
					"y" : 117 - 17 - 17 + WIKI_ADDITION,

					"text" : uiScriptLocale.GAMEOPTION_TITLE,

					"default_image" : ROOT + "XLarge_Button_01.sub",
					"over_image" : ROOT + "XLarge_Button_02.sub",
					"down_image" : ROOT + "XLarge_Button_03.sub",
				},
				{
					"name" : "change_button",
					"type" : "button",

					"x" : 10,
					"y" : 147 - 17 - 17 + ADDITION_Y,

					"text" : uiScriptLocale.SYSTEM_CHANGE,

					"default_image" : ROOT + "XLarge_Button_01.sub",
					"over_image" : ROOT + "XLarge_Button_02.sub",
					"down_image" : ROOT + "XLarge_Button_03.sub",
				},
				{
					"name" : "channel_button",
					"type" : "button",

					"x" : 10,
					"y" : 177 - 17 - 17 + ADDITION_Y,

					"text" : uiScriptLocale.SYSTEM_CHANNEL,
					"text_color" : 0xffF8BF24,

					"default_image" : ROOT + "XLarge_Button_01.sub",
					"over_image" : ROOT + "XLarge_Button_02.sub",
					"down_image" : ROOT + "XLarge_Button_03.sub",
					"disable_image" : ROOT + "XLarge_Button_04.sub",
				},
				{
					"name" : "logout_button",
					"type" : "button",

					"x" : 10,
					"y" : 207 - 17 - 17 + ADDITION_Y,

					"text" : uiScriptLocale.SYSTEM_LOGOUT,

					"default_image" : ROOT + "XLarge_Button_01.sub",
					"over_image" : ROOT + "XLarge_Button_02.sub",
					"down_image" : ROOT + "XLarge_Button_03.sub",
				},
				{
					"name" : "exit_button",
					"type" : "button",

					"x" : 10,
					"y" : 247 - 17 - 17 + ADDITION_Y,

					"text" : uiScriptLocale.SYSTEM_EXIT,

					"default_image" : ROOT + "XLarge_Button_01.sub",
					"over_image" : ROOT + "XLarge_Button_02.sub",
					"down_image" : ROOT + "XLarge_Button_03.sub",
				},
				{
					"name" : "cancel_button",
					"type" : "button",

					"x" : 10,
					"y" : 277 - 17 - 17 + ADDITION_Y,

					"text" : uiScriptLocale.CANCEL,

					"default_image" : ROOT + "XLarge_Button_01.sub",
					"over_image" : ROOT + "XLarge_Button_02.sub",
					"down_image" : ROOT + "XLarge_Button_03.sub",
				},
			),
		},
	),
}

if constInfo.NEW_PICKUP_FILTER:
	window["height"] += ADDITION_Y
	window["children"][0]["height"] += ADDITION_Y
	window["children"][0]["children"] += (
			{
				"name" : "pickup_option_button",
				"type" : "button",

				"x" : 10,
				"y" : 147 - 17 - 17 + WIKI_ADDITION,

				"text" : uiScriptLocale.SYSTEM_PICK_OPTION,

				"default_image" : ROOT + "XLarge_Button_01.sub",
				"over_image" : ROOT + "XLarge_Button_02.sub",
				"down_image" : ROOT + "XLarge_Button_03.sub",
			},
		)

if constInfo.ENABLE_INGAME_WIKI:
	window["children"][0]["children"] += (
			{
				"name" : "wiki_button",
				"type" : "button",

				"x" : 10,
				"y" : 87 - 17 - 17,

				"text" : localeInfo.WIKI_TITLENAME,

				"default_image" : ROOT + "XLarge_Button_01.sub",
				"over_image" : ROOT + "XLarge_Button_02.sub",
				"down_image" : ROOT + "XLarge_Button_03.sub",
			},
		)
