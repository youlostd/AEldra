import uiScriptLocale

ROOT_PATH = "d:/ymir work/ui/public/"

TEMPORARY_X = +13
BUTTON_TEMPORARY_X = 5
PVP_X = -10

LINE_LABEL_X 	= 22
LINE_DATA_X 	= 90+10
LINE_STEP	= 0
SMALL_BUTTON_WIDTH 	= 45
MIDDLE_BUTTON_WIDTH 	= 65

window = {
	"name" : "GameOptionDialog",
	"style" : ("movable", "float",),

	"x" : 0,
	"y" : 0,

	"width" : 284+10,
	"height" : 25*19-6 + 53,

	"children" :
	(
		{
			"name" : "board",
			"type" : "board",

			"x" : 0,
			"y" : 0,

			"width" : 284+10,
			"height" : 25*18-6,

			"children" :
			(
				## Title
				{
					"name" : "titlebar",
					"type" : "titlebar",
					"style" : ("attach",),

					"x" : 0,
					"y" : 0,

					"width" : 284+10,
					"color" : "gray",

					"children" :
					(
						{ "name":"titlename", "type":"text", "x":0, "y":3, 
						"text" : uiScriptLocale.GAMEOPTION_TITLE, 
						"horizontal_align":"center", "text_horizontal_align":"center" },
					),
				},

				## �̸���
				{
					"name" : "name_color",
					"type" : "text",

					"x" : LINE_LABEL_X,
					"y" : 33+2,

					"text" : uiScriptLocale.OPTION_NAME_COLOR,
				},
				{
					"name" : "name_color_normal",
					"type" : "radio_button",

					"x" : LINE_DATA_X+MIDDLE_BUTTON_WIDTH*0,
					"y" : 33,

					"text" : uiScriptLocale.OPTION_NAME_COLOR_NORMAL,

					"default_image" : ROOT_PATH + "Middle_Button_01.sub",
					"over_image" : ROOT_PATH + "Middle_Button_02.sub",
					"down_image" : ROOT_PATH + "Middle_Button_03.sub",
				},
				{
					"name" : "name_color_empire",
					"type" : "radio_button",

					"x" : LINE_DATA_X+MIDDLE_BUTTON_WIDTH*1,
					"y" : 33,

					"text" : uiScriptLocale.OPTION_NAME_COLOR_EMPIRE,

					"default_image" : ROOT_PATH + "Middle_Button_01.sub",
					"over_image" : ROOT_PATH + "Middle_Button_02.sub",
					"down_image" : ROOT_PATH + "Middle_Button_03.sub",
				},

				## Ÿ��â
				{
					"name" : "target_board",
					"type" : "text",

					"x" : LINE_LABEL_X,
					"y" : 58+2,

					"text" : uiScriptLocale.OPTION_TARGET_BOARD,
				},
				{
					"name" : "target_board_no_view",
					"type" : "radio_button",

					"x" : LINE_DATA_X+MIDDLE_BUTTON_WIDTH*0,
					"y" : 58,

					"text" : uiScriptLocale.OPTION_TARGET_BOARD_NO_VIEW,

					"default_image" : ROOT_PATH + "Middle_Button_01.sub",
					"over_image" : ROOT_PATH + "Middle_Button_02.sub",
					"down_image" : ROOT_PATH + "Middle_Button_03.sub",
				},
				{
					"name" : "target_board_view",
					"type" : "radio_button",

					"x" : LINE_DATA_X+MIDDLE_BUTTON_WIDTH*1,
					"y" : 58,

					"text" : uiScriptLocale.OPTION_TARGET_BOARD_VIEW,

					"default_image" : ROOT_PATH + "Middle_Button_01.sub",
					"over_image" : ROOT_PATH + "Middle_Button_02.sub",
					"down_image" : ROOT_PATH + "Middle_Button_03.sub",
				},

				
				## PvP Mode
				{
					"name" : "pvp_mode",
					"type" : "text",

					"x" : LINE_LABEL_X,
					"y" : 83+2,

					"text" : uiScriptLocale.OPTION_PVPMODE,
				},
				{
					"name" : "pvp_peace",
					"type" : "radio_button",

					"x" : LINE_DATA_X+SMALL_BUTTON_WIDTH*0,
					"y" : 83,

					"text" : uiScriptLocale.OPTION_PVPMODE_PEACE,
					"tooltip_text" : uiScriptLocale.OPTION_PVPMODE_PEACE_TOOLTIP,

					"default_image" : ROOT_PATH + "small_Button_01.sub",
					"over_image" : ROOT_PATH + "small_Button_02.sub",
					"down_image" : ROOT_PATH + "small_Button_03.sub",
				},
				{
					"name" : "pvp_revenge",
					"type" : "radio_button",

					"x" : LINE_DATA_X+SMALL_BUTTON_WIDTH*1,
					"y" : 83,

					"text" : uiScriptLocale.OPTION_PVPMODE_REVENGE,
					"tooltip_text" : uiScriptLocale.OPTION_PVPMODE_REVENGE_TOOLTIP,

					"default_image" : ROOT_PATH + "small_Button_01.sub",
					"over_image" : ROOT_PATH + "small_Button_02.sub",
					"down_image" : ROOT_PATH + "small_Button_03.sub",
				},
				{
					"name" : "pvp_guild",
					"type" : "radio_button",

					"x" : LINE_DATA_X+SMALL_BUTTON_WIDTH*2,
					"y" : 83,

					"text" : uiScriptLocale.OPTION_PVPMODE_GUILD,
					"tooltip_text" : uiScriptLocale.OPTION_PVPMODE_GUILD_TOOLTIP,

					"default_image" : ROOT_PATH + "small_Button_01.sub",
					"over_image" : ROOT_PATH + "small_Button_02.sub",
					"down_image" : ROOT_PATH + "small_Button_03.sub",
				},
				{
					"name" : "pvp_free",
					"type" : "radio_button",

					"x" : LINE_DATA_X+SMALL_BUTTON_WIDTH*3,
					"y" : 83,

					"text" : uiScriptLocale.OPTION_PVPMODE_FREE,
					"tooltip_text" : uiScriptLocale.OPTION_PVPMODE_FREE_TOOLTIP,

					"default_image" : ROOT_PATH + "small_Button_01.sub",
					"over_image" : ROOT_PATH + "small_Button_02.sub",
					"down_image" : ROOT_PATH + "small_Button_03.sub",
				},

				## Block
				{
					"name" : "block",
					"type" : "text",

					"x" : LINE_LABEL_X,
					"y" : 108+2,

					"text" : uiScriptLocale.OPTION_BLOCK,
				},
				{
					"name" : "block_exchange_button",
					"type" : "toggle_button",

					"x" : LINE_DATA_X+MIDDLE_BUTTON_WIDTH*0,
					"y" : 108,

					"text" : uiScriptLocale.OPTION_BLOCK_EXCHANGE,

					"default_image" : ROOT_PATH + "middle_button_01.sub",
					"over_image" : ROOT_PATH + "middle_button_02.sub",
					"down_image" : ROOT_PATH + "middle_button_03.sub",
				},
				{
					"name" : "block_party_button",
					"type" : "toggle_button",

					"x" : LINE_DATA_X+MIDDLE_BUTTON_WIDTH*1,
					"y" : 108,

					"text" : uiScriptLocale.OPTION_BLOCK_PARTY,

					"default_image" : ROOT_PATH + "middle_button_01.sub",
					"over_image" : ROOT_PATH + "middle_button_02.sub",
					"down_image" : ROOT_PATH + "middle_button_03.sub",
				},
				{
					"name" : "block_guild_button",
					"type" : "toggle_button",

					"x" : LINE_DATA_X+MIDDLE_BUTTON_WIDTH*2,
					"y" : 108,

					"text" : uiScriptLocale.OPTION_BLOCK_GUILD,

					"default_image" : ROOT_PATH + "middle_button_01.sub",
					"over_image" : ROOT_PATH + "middle_button_02.sub",
					"down_image" : ROOT_PATH + "middle_button_03.sub",
				},
				{
					"name" : "block_whisper_button",
					"type" : "toggle_button",

					"x" : LINE_DATA_X+MIDDLE_BUTTON_WIDTH*0,
					"y" : 133,

					"text" : uiScriptLocale.OPTION_BLOCK_WHISPER,

					"default_image" : ROOT_PATH + "middle_button_01.sub",
					"over_image" : ROOT_PATH + "middle_button_02.sub",
					"down_image" : ROOT_PATH + "middle_button_03.sub",
				},
				{
					"name" : "block_friend_button",
					"type" : "toggle_button",

					"x" : LINE_DATA_X+MIDDLE_BUTTON_WIDTH*1,
					"y" : 133,

					"text" : uiScriptLocale.OPTION_BLOCK_FRIEND,

					"default_image" : ROOT_PATH + "middle_button_01.sub",
					"over_image" : ROOT_PATH + "middle_button_02.sub",
					"down_image" : ROOT_PATH + "middle_button_03.sub",
				},
				{
					"name" : "block_party_request_button",
					"type" : "toggle_button",

					"x" : LINE_DATA_X+MIDDLE_BUTTON_WIDTH*2,
					"y" : 133,

					"text" : uiScriptLocale.OPTION_BLOCK_PARTY_REQUEST,

					"default_image" : ROOT_PATH + "middle_button_01.sub",
					"over_image" : ROOT_PATH + "middle_button_02.sub",
					"down_image" : ROOT_PATH + "middle_button_03.sub",
				},

				## Chat
				{
					"name" : "chat",
					"type" : "text",

					"x" : LINE_LABEL_X,
					"y" : 158+2,

					"text" : uiScriptLocale.OPTION_VIEW_CHAT,
				},
				{
					"name" : "view_chat_on_button",
					"type" : "radio_button",

					"x" : LINE_DATA_X,
					"y" : 158,

					"text" : uiScriptLocale.OPTION_VIEW_CHAT_ON,

					"default_image" : ROOT_PATH + "middle_button_01.sub",
					"over_image" : ROOT_PATH + "middle_button_02.sub",
					"down_image" : ROOT_PATH + "middle_button_03.sub",
				},
				{
					"name" : "view_chat_off_button",
					"type" : "radio_button",

					"x" : LINE_DATA_X+MIDDLE_BUTTON_WIDTH,
					"y" : 158,

					"text" : uiScriptLocale.OPTION_VIEW_CHAT_OFF,

					"default_image" : ROOT_PATH + "middle_button_01.sub",
					"over_image" : ROOT_PATH + "middle_button_02.sub",
					"down_image" : ROOT_PATH + "middle_button_03.sub",
				},

				## Always Show Name
				{
					"name" : "always_show_name",
					"type" : "text",

					"x" : LINE_LABEL_X,
					"y" : 183+2,

					"text" : uiScriptLocale.OPTION_ALWAYS_SHOW_NAME,
				},
				{
					"name" : "always_show_name_on_button",
					"type" : "radio_button",

					"x" : LINE_DATA_X,
					"y" : 183,

					"text" : uiScriptLocale.OPTION_ALWAYS_SHOW_NAME_ON,

					"default_image" : ROOT_PATH + "middle_button_01.sub",
					"over_image" : ROOT_PATH + "middle_button_02.sub",
					"down_image" : ROOT_PATH + "middle_button_03.sub",
				},
				{
					"name" : "always_show_name_off_button",
					"type" : "radio_button",

					"x" : LINE_DATA_X+MIDDLE_BUTTON_WIDTH,
					"y" : 183,

					"text" : uiScriptLocale.OPTION_ALWAYS_SHOW_NAME_OFF,

					"default_image" : ROOT_PATH + "middle_button_01.sub",
					"over_image" : ROOT_PATH + "middle_button_02.sub",
					"down_image" : ROOT_PATH + "middle_button_03.sub",
				},

				## Effect On/Off
				{
					"name" : "effect_on_off",
					"type" : "text",

					"x" : LINE_LABEL_X,
					"y" : 208+2,

					"text" : uiScriptLocale.OPTION_EFFECT,
				},
				{
					"name" : "show_damage_on_button",
					"type" : "radio_button",

					"x" : LINE_DATA_X,
					"y" : 208,

					"text" : uiScriptLocale.OPTION_VIEW_CHAT_ON,

					"default_image" : ROOT_PATH + "middle_button_01.sub",
					"over_image" : ROOT_PATH + "middle_button_02.sub",
					"down_image" : ROOT_PATH + "middle_button_03.sub",
				},
				{
					"name" : "show_damage_off_button",
					"type" : "radio_button",

					"x" : LINE_DATA_X+MIDDLE_BUTTON_WIDTH,
					"y" : 208,

					"text" : uiScriptLocale.OPTION_VIEW_CHAT_OFF,

					"default_image" : ROOT_PATH + "middle_button_01.sub",
					"over_image" : ROOT_PATH + "middle_button_02.sub",
					"down_image" : ROOT_PATH + "middle_button_03.sub",
				},





				## Item Highlight
				{
					"name" : "item_highlight_option",
					"type" : "text",

					"x" : LINE_LABEL_X,
					"y" : 205+25 + 24 / 2,

					"text" : uiScriptLocale.OPTION_ITEM_HIGHLIGHT,

					"text_vertical_align" : "center",
				},
				{
					"name" : "item_highlight_option_on",
					"type" : "toggle_button",

					"x" : LINE_DATA_X,
					"y" : 208+25,

					"text" : uiScriptLocale.OPTION_ITEM_HIGHLIGHT_ON,

					"default_image" : ROOT_PATH + "middle_button_01.sub",
					"over_image" : ROOT_PATH + "middle_button_02.sub",
					"down_image" : ROOT_PATH + "middle_button_03.sub",
				},
				{
					"name" : "item_highlight_option_off",
					"type" : "toggle_button",

					"x" : LINE_DATA_X + MIDDLE_BUTTON_WIDTH,
					"y" : 208+25,

					"text" : uiScriptLocale.OPTION_ITEM_HIGHLIGHT_OFF,

					"default_image" : ROOT_PATH + "middle_button_01.sub",
					"over_image" : ROOT_PATH + "middle_button_02.sub",
					"down_image" : ROOT_PATH + "middle_button_03.sub",
				},

				## Gold chat
				{
					"name" : "gold_pickup_chat_option",
					"type" : "text",

					"x" : LINE_LABEL_X,
					"y" : 205+25+25 + 24 / 2,

					"text" : uiScriptLocale.OPTION_GOLD_PICKUP,

					"text_vertical_align" : "center",
				},
				{
					"name" : "gold_pickup_chat_option_on",
					"type" : "toggle_button",

					"x" : LINE_DATA_X,
					"y" : 208+25+25,

					"text" : uiScriptLocale.OPTION_GOLD_PICKUP_ON,

					"default_image" : ROOT_PATH + "middle_button_01.sub",
					"over_image" : ROOT_PATH + "middle_button_02.sub",
					"down_image" : ROOT_PATH + "middle_button_03.sub",
				},
				{
					"name" : "gold_pickup_chat_option_off",
					"type" : "toggle_button",

					"x" : LINE_DATA_X + MIDDLE_BUTTON_WIDTH,
					"y" : 208+25+25,

					"text" : uiScriptLocale.OPTION_GOLD_PICKUP_OFF,

					"default_image" : ROOT_PATH + "middle_button_01.sub",
					"over_image" : ROOT_PATH + "middle_button_02.sub",
					"down_image" : ROOT_PATH + "middle_button_03.sub",
				},


				## Pickup filter
				{
					"name" : "pickup",
					"type" : "text",

					"x" : LINE_LABEL_X,
					"y" : 205+25+25 + 25 + 24 / 2,

					"text" : uiScriptLocale.OPTION_DISABLE_PICKUP,
					"text_vertical_align" : "center",
				},
				{
					"name" : "disable_pickup_weapon",
					"type" : "toggle_button",

					"x" : LINE_DATA_X+MIDDLE_BUTTON_WIDTH*0,
					"y" :  208+25+25 + 25,

					"text" : uiScriptLocale.OPTION_DISABLE_PICKUP_WEAPON,

					"default_image" : ROOT_PATH + "middle_button_01.sub",
					"over_image" : ROOT_PATH + "middle_button_02.sub",
					"down_image" : ROOT_PATH + "middle_button_03.sub",
				},
				{
					"name" : "disable_pickup_armor",
					"type" : "toggle_button",

					"x" : LINE_DATA_X+MIDDLE_BUTTON_WIDTH*1,
					"y" :  208+25+25 + 25,

					"text" : uiScriptLocale.OPTION_DISABLE_PICKUP_ARMOR,

					"default_image" : ROOT_PATH + "middle_button_01.sub",
					"over_image" : ROOT_PATH + "middle_button_02.sub",
					"down_image" : ROOT_PATH + "middle_button_03.sub",
				},
				{
					"name" : "disable_pickup_etc",
					"type" : "toggle_button",

					"x" : LINE_DATA_X+MIDDLE_BUTTON_WIDTH*2,
					"y" :  208+25+25 + 25,

					"text" : uiScriptLocale.OPTION_DISABLE_PICKUP_ETC,

					"default_image" : ROOT_PATH + "middle_button_01.sub",
					"over_image" : ROOT_PATH + "middle_button_02.sub",
					"down_image" : ROOT_PATH + "middle_button_03.sub",
				},



				## Pickup all
				{
					"name" : "pickup_all",
					"type" : "text",

					"x" : LINE_LABEL_X,
					"y" : 205+25+25 + 25*2 + 24 / 2,

					"text" : uiScriptLocale.OPTION_PICKUP_ALL,
					"text_vertical_align" : "center",
				},
				{
					"name" : "pickup_all_fast",
					"type" : "toggle_button",

					"x" : LINE_DATA_X+MIDDLE_BUTTON_WIDTH*0,
					"y" :  208+25+25 + 25*2,

					"text" : uiScriptLocale.OPTION_PICKUP_FAST,

					"default_image" : ROOT_PATH + "middle_button_01.sub",
					"over_image" : ROOT_PATH + "middle_button_02.sub",
					"down_image" : ROOT_PATH + "middle_button_03.sub",
				},
				{
					"name" : "pickup_all_slow",
					"type" : "toggle_button",

					"x" : LINE_DATA_X+MIDDLE_BUTTON_WIDTH*1,
					"y" :  208+25+25 + 25*2,

					"text" : uiScriptLocale.OPTION_PICKUP_SLOW,

					"default_image" : ROOT_PATH + "middle_button_01.sub",
					"over_image" : ROOT_PATH + "middle_button_02.sub",
					"down_image" : ROOT_PATH + "middle_button_03.sub",
				},

				
				## Quest letter
				{
					"name" : "quest_letter",
					"type" : "text",

					"x" : LINE_LABEL_X,
					"y" : 205+25+25 + 25*3 + 24 / 2,

					"text" : uiScriptLocale.OPTION_QUEST_LETTER,
					"text_vertical_align" : "center",
				},
				{
					"name" : "quest_letter_show",
					"type" : "toggle_button",

					"x" : LINE_DATA_X+MIDDLE_BUTTON_WIDTH*0,
					"y" :  208+25+25 + 25*3,

					"text" : uiScriptLocale.OPTION_QUEST_LETTER_SHOW,

					"default_image" : ROOT_PATH + "middle_button_01.sub",
					"over_image" : ROOT_PATH + "middle_button_02.sub",
					"down_image" : ROOT_PATH + "middle_button_03.sub",
				},
				{
					"name" : "quest_letter_hide",
					"type" : "toggle_button",

					"x" : LINE_DATA_X+MIDDLE_BUTTON_WIDTH*1,
					"y" :  208+25+25 + 25*3,

					"text" : uiScriptLocale.OPTION_QUEST_LETTER_HIDE,

					"default_image" : ROOT_PATH + "middle_button_01.sub",
					"over_image" : ROOT_PATH + "middle_button_02.sub",
					"down_image" : ROOT_PATH + "middle_button_03.sub",
				},
				
				## Night Modus
				{
					"name" : "usenight_on_off",
					"type" : "text",

					"x" : LINE_LABEL_X,
					"y" : 205+25+25 + 25*4 + 24 / 2,

					"text" : uiScriptLocale.OPTION_USENIGHT,
					"text_vertical_align" : "center",
				},
				{
					"name" : "usenight_on_button",
					"type" : "toggle_button",

					"x" : LINE_DATA_X+MIDDLE_BUTTON_WIDTH*0,
					"y" :  208+25+25 + 25*4,

					"text" : uiScriptLocale.OPTION_GOLD_PICKUP_ON,

					"default_image" : ROOT_PATH + "middle_button_01.sub",
					"over_image" : ROOT_PATH + "middle_button_02.sub",
					"down_image" : ROOT_PATH + "middle_button_03.sub",
				},
				{
					"name" : "usenight_off_button",
					"type" : "toggle_button",

					"x" : LINE_DATA_X+MIDDLE_BUTTON_WIDTH*1,
					"y" :  208+25+25 + 25*4,

					"text" : uiScriptLocale.OPTION_GOLD_PICKUP_OFF,

					"default_image" : ROOT_PATH + "middle_button_01.sub",
					"over_image" : ROOT_PATH + "middle_button_02.sub",
					"down_image" : ROOT_PATH + "middle_button_03.sub",
				},

				
				## Hide Shop Ads
				{
					"name" : "hidehsopads_label",
					"type" : "text",

					"x" : LINE_LABEL_X,
					"y" : 205+25+25 + 25*5 + 24 / 2,

					"text" : uiScriptLocale.OPTION_SHOP_TITLE,
					"text_vertical_align" : "center",
				},
				{
					"name" : "hide_shop_ad_on_button",
					"type" : "toggle_button",

					"x" : LINE_DATA_X+MIDDLE_BUTTON_WIDTH*0,
					"y" :  208+25+25 + 25*5,

					"text" : uiScriptLocale.OPTION_QUEST_LETTER_HIDE,

					"default_image" : ROOT_PATH + "middle_button_01.sub",
					"over_image" : ROOT_PATH + "middle_button_02.sub",
					"down_image" : ROOT_PATH + "middle_button_03.sub",
				},
				{
					"name" : "hide_shop_ad_off_button",
					"type" : "toggle_button",

					"x" : LINE_DATA_X+MIDDLE_BUTTON_WIDTH*1,
					"y" :  208+25+25 + 25*5,

					"text" : uiScriptLocale.OPTION_QUEST_LETTER_SHOW,

					"default_image" : ROOT_PATH + "middle_button_01.sub",
					"over_image" : ROOT_PATH + "middle_button_02.sub",
					"down_image" : ROOT_PATH + "middle_button_03.sub",
				},

				## Render option
				{
					"name" : "render_text",
					"type" : "text",

					"x" : LINE_LABEL_X,
					"y" : 205+25+25 + 25*6 + 24 / 2,

					"text" : uiScriptLocale.RENDER_OPT,
					"text_vertical_align" : "center",
				},
				{
					"name" : "render_low",
					"type" : "toggle_button",

					"x" : LINE_DATA_X+MIDDLE_BUTTON_WIDTH*0,
					"y" : 208+25+25 + 25*6,

					"text" : uiScriptLocale.RENDER_OPT_LOW,

					"default_image" : ROOT_PATH + "Middle_Button_01.sub",
					"over_image" : ROOT_PATH + "Middle_Button_02.sub",
					"down_image" : ROOT_PATH + "Middle_Button_03.sub",
				},
				{
					"name" : "render_medium",
					"type" : "toggle_button",

					"x" : LINE_DATA_X+MIDDLE_BUTTON_WIDTH*1,
					"y" : 208+25+25 + 25*6,

					"text" : uiScriptLocale.RENDER_OPT_MEDIUM,

					"default_image" : ROOT_PATH + "Middle_Button_01.sub",
					"over_image" : ROOT_PATH + "Middle_Button_02.sub",
					"down_image" : ROOT_PATH + "Middle_Button_03.sub",
				},
				{
					"name" : "render_high",
					"type" : "toggle_button",

					"x" : LINE_DATA_X+MIDDLE_BUTTON_WIDTH*2,
					"y" : 208+25+25 + 25*6,

					"text" : uiScriptLocale.RENDER_OPT_HIGH,

					"default_image" : ROOT_PATH + "Middle_Button_01.sub",
					"over_image" : ROOT_PATH + "Middle_Button_02.sub",
					"down_image" : ROOT_PATH + "Middle_Button_03.sub",
				},
			),
		},

		{
			"name" : "board",
			"type" : "board",

			"x" : 0,
			"y" : 25*18,

			"width" : 284+10,
			"height" : 53 + 22,

			"children" :
			(
				## Title
				{
					"name" : "titlebar2",
					"type" : "titlebar",
					"style" : ("attach",),

					"x" : 0,
					"y" : 0,

					"width" : 284+10,
					"color" : "gray",

					"children" :
					(
						{ "name":"titlename", "type":"text", "x":0, "y":3, 
						"text" : uiScriptLocale.GAMEOPTION_TITLE_EXTRA, 
						"horizontal_align":"center", "text_horizontal_align":"center" },
					),
				},

				## Hide costumes
				{
					"name" : "hide_costume_text",
					"type" : "text",

					"x" : LINE_LABEL_X,
					"y" : 33-5+2,

					"text" : uiScriptLocale.HIDE_COSTUMES,
				},
				{
					"name" : "hide_costume_weapon",
					"type" : "toggle_button",

					"x" : 20+MIDDLE_BUTTON_WIDTH*0,
					"y" : 33-5 + 20,

					"text" : uiScriptLocale.SHOP_SEARCH_CAT_WEAPON,

					"default_image" : ROOT_PATH + "Middle_Button_01.sub",
					"over_image" : ROOT_PATH + "Middle_Button_02.sub",
					"down_image" : ROOT_PATH + "Middle_Button_03.sub",
				},
				{
					"name" : "hide_costume_armor",
					"type" : "toggle_button",

					"x" : 20+MIDDLE_BUTTON_WIDTH*1,
					"y" : 33-5 + 20,

					"text" : uiScriptLocale.SHOP_SEARCH_CAT_ARMOR,

					"default_image" : ROOT_PATH + "Middle_Button_01.sub",
					"over_image" : ROOT_PATH + "Middle_Button_02.sub",
					"down_image" : ROOT_PATH + "Middle_Button_03.sub",
				},
				{
					"name" : "hide_costume_hair",
					"type" : "toggle_button",

					"x" : 20+MIDDLE_BUTTON_WIDTH*2,
					"y" : 33-5 + 20,

					"text" : uiScriptLocale.GAMEOPTION_HAIR,

					"default_image" : ROOT_PATH + "Middle_Button_01.sub",
					"over_image" : ROOT_PATH + "Middle_Button_02.sub",
					"down_image" : ROOT_PATH + "Middle_Button_03.sub",
				},
				{
					"name" : "hide_costume_acce",
					"type" : "toggle_button",

					"x" : 20+MIDDLE_BUTTON_WIDTH*3,
					"y" : 33-5 + 20,

					"text" : uiScriptLocale.GAMEOPTION_ACCE,

					"default_image" : ROOT_PATH + "Middle_Button_01.sub",
					"over_image" : ROOT_PATH + "Middle_Button_02.sub",
					"down_image" : ROOT_PATH + "Middle_Button_03.sub",
				},
			),
		},
	),
}

import constInfo
if constInfo.ENABLE_CHANGE_TEXTURE_SNOW:
	window["height"] += 25
	window["children"][1]["y"] += 25
	window["children"][0]["height"] += 25
	window["children"][0]["children"] += (
					{
						"name" : "nighttitle",
						"type" : "text",
						"x" : LINE_LABEL_X,
						"y" : 208+25+25 + 25*7,
						"text" : "Snow",
					},
					{
						"name" : "snow_on",
						"type" : "radio_button",
						"x" : LINE_DATA_X+SMALL_BUTTON_WIDTH*0,
						"y" : 208+25+25 + 25*7,
						"text" : "On",
						"default_image" : ROOT_PATH + "small_Button_01.sub",
						"over_image" : ROOT_PATH + "small_Button_02.sub",
						"down_image" : ROOT_PATH + "small_Button_03.sub",
					},
					{
						"name" : "snow_off",
						"type" : "radio_button",
						"x" : LINE_DATA_X+SMALL_BUTTON_WIDTH*1,
						"y" : 208+25+25 + 25*7,
						"text" : "Off",
						"default_image" : ROOT_PATH + "small_Button_01.sub",
						"over_image" : ROOT_PATH + "small_Button_02.sub",
						"down_image" : ROOT_PATH + "small_Button_03.sub",
					},
					)
window["height"] += 25
window["children"][1]["y"] += 25
window["children"][0]["height"] += 25
window["children"][0]["children"] += (
				{
					"name" : "hide_fps",
					"type" : "text",
					"x" : LINE_LABEL_X,
					"y" : 208+25+25 + 25*8,
					"text" : "FPS",
				},
				{
					"name" : "hide_fps",
					"type" : "toggle_button",
					"x" : LINE_DATA_X+MIDDLE_BUTTON_WIDTH*0,
					"y" : 208+25+25 + 25*8,
					"text" : uiScriptLocale.OPTION_HIDE_FPS,
					"default_image" : ROOT_PATH + "Middle_Button_01.sub",
					"over_image" : ROOT_PATH + "Middle_Button_02.sub",
					"down_image" : ROOT_PATH + "Middle_Button_03.sub",
				},
				{
					"name" : "show_fps",
					"type" : "toggle_button",
					"x" : LINE_DATA_X+MIDDLE_BUTTON_WIDTH*1,
					"y" : 208+25+25 + 25*8,
					"text" : uiScriptLocale.OPTION_SHOW_FPS,
					"default_image" : ROOT_PATH + "Middle_Button_01.sub",
					"over_image" : ROOT_PATH + "Middle_Button_02.sub",
					"down_image" : ROOT_PATH + "Middle_Button_03.sub",
				},
				)
if constInfo.HIDE_NPC_OPTION:
	window["height"] += 25
	window["children"][1]["y"] += 25
	window["children"][0]["height"] += 25
	window["children"][0]["children"] += (
					{
						"name" : "HideNPC",
						"type" : "text",
						"x" : LINE_LABEL_X,
						"y" : 208+25+25 + 25*9,
						"text" : uiScriptLocale.OPTION_HIDE_NPC_TITLE,
					},
					{
						"name" : "HideBuffi",
						"type" : "toggle_button",
						"x" : LINE_DATA_X+MIDDLE_BUTTON_WIDTH*0,
						"y" : 208+25+25 + 25*9,
						"text" : uiScriptLocale.OPTION_HIDE_NPC_CAT1,
						"default_image" : ROOT_PATH + "Middle_Button_01.sub",
						"over_image" : ROOT_PATH + "Middle_Button_02.sub",
						"down_image" : ROOT_PATH + "Middle_Button_03.sub",
					},
					{
						"name" : "HideMount",
						"type" : "toggle_button",
						"x" : LINE_DATA_X+MIDDLE_BUTTON_WIDTH*1,
						"y" : 208+25+25 + 25*9,
						"text" : uiScriptLocale.OPTION_HIDE_NPC_CAT2,
						"default_image" : ROOT_PATH + "Middle_Button_01.sub",
						"over_image" : ROOT_PATH + "Middle_Button_02.sub",
						"down_image" : ROOT_PATH + "Middle_Button_03.sub",
					},
					{
						"name" : "HidePet",
						"type" : "toggle_button",
						"x" : LINE_DATA_X+MIDDLE_BUTTON_WIDTH*2,
						"y" : 208+25+25 + 25*9,
						"text" : uiScriptLocale.OPTION_HIDE_NPC_CAT3,
						"default_image" : ROOT_PATH + "Middle_Button_01.sub",
						"over_image" : ROOT_PATH + "Middle_Button_02.sub",
						"down_image" : ROOT_PATH + "Middle_Button_03.sub",
					},
					)

if constInfo.SAVE_WINDOW_POSITION:
	window["height"] += 25
	window["children"][1]["y"] += 25
	window["children"][0]["height"] += 25
	window["children"][0]["children"] += (
					{
						"name" : "wnd_pos_txt",
						"type" : "text",

						"x" : LINE_LABEL_X,
						"y" : 208+25+25 + 25*10,

						"text" : uiScriptLocale.SAVE_WINDOW_POS,
					},
					{
						"name" : "wnd_pos_btn0",
						"type" : "radio_button",

						"x" : LINE_DATA_X+MIDDLE_BUTTON_WIDTH*1,
						"y" : 208+25+25 + 25*10,

						"text" : uiScriptLocale.NO,

						"default_image" : ROOT_PATH + "Middle_Button_01.sub",
						"over_image" : ROOT_PATH + "Middle_Button_02.sub",
						"down_image" : ROOT_PATH + "Middle_Button_03.sub",
					},
					{
						"name" : "wnd_pos_btn1",
						"type" : "radio_button",

						"x" : LINE_DATA_X+MIDDLE_BUTTON_WIDTH*2,
						"y" : 208+25+25 + 25*10,

						"text" : uiScriptLocale.YES,

						"default_image" : ROOT_PATH + "Middle_Button_01.sub",
						"over_image" : ROOT_PATH + "Middle_Button_02.sub",
						"down_image" : ROOT_PATH + "Middle_Button_03.sub",
					},
					)
