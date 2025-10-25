import app
import uiScriptLocale

ROOT_PATH = "d:/ymir work/ui/zodiac/12zi/reward/"
MISSION_COUNT = "50"
JACHUC_START_X = 32
JACHUC_Y = -8
GAP_X = 40
GAP_START_Y = 140

window = {
	"name" : "zi_Reward_Window",

	"x" : (SCREEN_WIDTH -500) / 2,
	"y" : (SCREEN_HEIGHT - 467) / 2,

	"style" : ("movable", "float",),

	"width" : 500,
	"height" : 467,

	"children" :
	(
		{
			"name" : "board",
			"type" : "board",

			"x" : 0,
			"y" : 0,

			"width" : 500,
			"height" :467,
		
			"children" :
			(
				## Title
				{
					"name" : "TitleBar",
					"type" : "titlebar",

					"x" : 6,
					"y" : 6,

					"width" : 487,
					"color" : "yellow",

					"children" :
					(
						{ "name":"TitleName", "type":"text", "x":250, "y":3, "text" : uiScriptLocale.ZODIAC_CALENDAR, "text_horizontal_align":"center" },
					),
				},
				## Background Window
				{
					"name" : "BgWindow",

					"x" : 10,
					"y" : 32,

					"width" : 490,
					"height" : 437,
					
					"children" :
					(				
						{
							"name":"BgImage",
							"type":"image",
							
							"x":0,
							"y":0,

							"image" : ROOT_PATH + "bg_12zi_reward.sub",

						},
				
						{"name":"bg_weekly_row_0", "type":"button", "x":114, "y":0, "default_image" : ROOT_PATH + "bg_weekly_row.sub", "over_image" : ROOT_PATH + "bg_weekly_row.sub", "down_image" : ROOT_PATH + "bg_weekly_row.sub"},
						{"name":"bg_weekly_row_1", "type":"button", "x":142, "y":0, "default_image" : ROOT_PATH + "bg_weekly_row_1.sub", "over_image" : ROOT_PATH + "bg_weekly_row_1.sub", "down_image" : ROOT_PATH + "bg_weekly_row_1.sub"},
						{"name":"bg_weekly_row_2", "type":"button", "x":198, "y":0, "default_image" : ROOT_PATH + "bg_weekly_row_2.sub", "over_image" : ROOT_PATH + "bg_weekly_row_2.sub", "down_image" : ROOT_PATH + "bg_weekly_row_2.sub"},
						{"name":"bg_weekly_row_3", "type":"button", "x":254, "y":0, "default_image" : ROOT_PATH + "bg_weekly_row_3.sub", "over_image" : ROOT_PATH + "bg_weekly_row_3.sub", "down_image" : ROOT_PATH + "bg_weekly_row_3.sub"},
						{"name":"bg_weekly_row_4", "type":"button", "x":310, "y":0, "default_image" : ROOT_PATH + "bg_weekly_row_4.sub", "over_image" : ROOT_PATH + "bg_weekly_row_4.sub", "down_image" : ROOT_PATH + "bg_weekly_row_4.sub"},
						{"name":"bg_weekly_row_5", "type":"button", "x":366, "y":0, "default_image" : ROOT_PATH + "bg_weekly_row_5.sub", "over_image" : ROOT_PATH + "bg_weekly_row_5.sub", "down_image" : ROOT_PATH + "bg_weekly_row_5.sub"},
						{"name":"bg_weekly_row_6", "type":"button", "x":422, "y":0, "default_image" : ROOT_PATH + "bg_weekly_row_6.sub", "over_image" : ROOT_PATH + "bg_weekly_row_6.sub", "down_image" : ROOT_PATH + "bg_weekly_row_6.sub"},
						{"name":"bg_weekly_row_7", "type":"button", "x":114, "y":30, "default_image" : ROOT_PATH + "bg_charm_12zi.sub", "over_image" : ROOT_PATH + "bg_charm_12zi.sub", "down_image" : ROOT_PATH + "bg_charm_12zi.sub"},
						{"name":"bg_weekly_row_8", "type":"button", "x":142, "y":30, "default_image" : ROOT_PATH + "bg_charm_12zi_1.sub", "over_image" : ROOT_PATH + "bg_charm_12zi_1.sub", "down_image" : ROOT_PATH + "bg_charm_12zi_1.sub"},
						{"name":"bg_weekly_row_9", "type":"button", "x":170, "y":30, "default_image" : ROOT_PATH + "bg_charm_12zi_2.sub", "over_image" : ROOT_PATH + "bg_charm_12zi_2.sub", "down_image" : ROOT_PATH + "bg_charm_12zi_2.sub"},
						{"name":"bg_weekly_row_10", "type":"button", "x":198, "y":30, "default_image" : ROOT_PATH + "bg_charm_12zi_3.sub", "over_image" : ROOT_PATH + "bg_charm_12zi_3.sub", "down_image" : ROOT_PATH + "bg_charm_12zi_3.sub"},
						{"name":"bg_weekly_row_11", "type":"button", "x":226, "y":30, "default_image" : ROOT_PATH + "bg_charm_12zi_4.sub", "over_image" : ROOT_PATH + "bg_charm_12zi_4.sub", "down_image" : ROOT_PATH + "bg_charm_12zi_4.sub"},
						{"name":"bg_weekly_row_12", "type":"button", "x":254, "y":30, "default_image" : ROOT_PATH + "bg_charm_12zi_5.sub", "over_image" : ROOT_PATH + "bg_charm_12zi_5.sub", "down_image" : ROOT_PATH + "bg_charm_12zi_5.sub"},
						{"name":"bg_weekly_row_13", "type":"button", "x":282, "y":30, "default_image" : ROOT_PATH + "bg_charm_12zi_6.sub", "over_image" : ROOT_PATH + "bg_charm_12zi_6.sub", "down_image" : ROOT_PATH + "bg_charm_12zi_6.sub"},
						{"name":"bg_weekly_row_14", "type":"button", "x":310, "y":30, "default_image" : ROOT_PATH + "bg_charm_12zi_7.sub", "over_image" : ROOT_PATH + "bg_charm_12zi_7.sub", "down_image" : ROOT_PATH + "bg_charm_12zi_7.sub"},
						{"name":"bg_weekly_row_15", "type":"button", "x":338, "y":30, "default_image" : ROOT_PATH + "bg_charm_12zi_8.sub", "over_image" : ROOT_PATH + "bg_charm_12zi_8.sub", "down_image" : ROOT_PATH + "bg_charm_12zi_8.sub"},
						{"name":"bg_weekly_row_16", "type":"button", "x":366, "y":30, "default_image" : ROOT_PATH + "bg_charm_12zi_9.sub", "over_image" : ROOT_PATH + "bg_charm_12zi_9.sub", "down_image" : ROOT_PATH + "bg_charm_12zi_9.sub"},
						{"name":"bg_weekly_row_17", "type":"button", "x":394, "y":30, "default_image" : ROOT_PATH + "bg_charm_12zi_10.sub", "over_image" : ROOT_PATH + "bg_charm_12zi_10.sub", "down_image" : ROOT_PATH + "bg_charm_12zi_10.sub"},
						{"name":"bg_weekly_row_18", "type":"button", "x":422, "y":30, "default_image" : ROOT_PATH + "bg_charm_12zi_11.sub", "over_image" : ROOT_PATH + "bg_charm_12zi_11.sub", "down_image" : ROOT_PATH + "bg_charm_12zi_11.sub"},
						{"name":"bg_weekly_row_19", "type":"button", "x":450, "y":30, "default_image" : ROOT_PATH + "bg_charm_12zi_12.sub", "over_image" : ROOT_PATH + "bg_charm_12zi_12.sub", "down_image" : ROOT_PATH + "bg_charm_12zi_12.sub"},
						{"name":"bg_weekly_row_20", "type":"button", "x":114, "y":58, "default_image" : ROOT_PATH + "bg_count_slot_row.sub", "over_image" : ROOT_PATH + "bg_count_slot_row.sub", "down_image" : ROOT_PATH + "bg_count_slot_row.sub"},
						{"name":"bg_weekly_row_21", "type":"button", "x":114, "y":86, "default_image" : ROOT_PATH + "bg_need_count_slot_row.sub", "over_image" : ROOT_PATH + "bg_need_count_slot_row.sub", "down_image" : ROOT_PATH + "bg_need_count_slot_row.sub"},
						{"name":"bg_weekly_row_22", "type":"button", "x":0, "y":86, "default_image" : ROOT_PATH + "bg_weekly_column.sub", "over_image" : ROOT_PATH + "bg_weekly_column.sub", "down_image" : ROOT_PATH + "bg_weekly_column.sub"},
						{"name":"bg_weekly_row_23", "type":"button", "x":0, "y":114, "default_image" : ROOT_PATH + "bg_weekly_column_1.sub", "over_image" : ROOT_PATH + "bg_weekly_column_1.sub", "down_image" : ROOT_PATH + "bg_weekly_column_1.sub"},
						{"name":"bg_weekly_row_24", "type":"button", "x":0, "y":170, "default_image" : ROOT_PATH + "bg_weekly_column_2.sub", "over_image" : ROOT_PATH + "bg_weekly_column_2.sub", "down_image" : ROOT_PATH + "bg_weekly_column_2.sub"},
						{"name":"bg_weekly_row_25", "type":"button", "x":0, "y":226, "default_image" : ROOT_PATH + "bg_weekly_column_3.sub", "over_image" : ROOT_PATH + "bg_weekly_column_3.sub", "down_image" : ROOT_PATH + "bg_weekly_column_3.sub"},
						{"name":"bg_weekly_row_26", "type":"button", "x":0, "y":282, "default_image" : ROOT_PATH + "bg_weekly_column_4.sub", "over_image" : ROOT_PATH + "bg_weekly_column_4.sub", "down_image" : ROOT_PATH + "bg_weekly_column_4.sub"},
						{"name":"bg_weekly_row_27", "type":"button", "x":0, "y":338, "default_image" : ROOT_PATH + "bg_weekly_column_5.sub", "over_image" : ROOT_PATH + "bg_weekly_column_5.sub", "down_image" : ROOT_PATH + "bg_weekly_column_5.sub"},
						{"name":"bg_weekly_row_28", "type":"button", "x":30, "y":114, "default_image" : ROOT_PATH + "bg_weekly_column_6.sub", "over_image" : ROOT_PATH + "bg_weekly_column_6.sub", "down_image" : ROOT_PATH + "bg_weekly_column_6.sub"},
						{"name":"bg_weekly_row_29", "type":"button", "x":58, "y":86, "default_image" : ROOT_PATH + "bg_charm_10gan.sub", "over_image" : ROOT_PATH + "bg_charm_10gan.sub", "down_image" : ROOT_PATH + "bg_charm_10gan.sub"},
						{"name":"bg_weekly_row_30", "type":"button", "x":58, "y":114, "default_image" : ROOT_PATH + "bg_charm_10gan_1.sub", "over_image" : ROOT_PATH + "bg_charm_10gan_1.sub", "down_image" : ROOT_PATH + "bg_charm_10gan_1.sub"},
						{"name":"bg_weekly_row_31", "type":"button", "x":58, "y":142, "default_image" : ROOT_PATH + "bg_charm_10gan_2.sub", "over_image" : ROOT_PATH + "bg_charm_10gan_2.sub", "down_image" : ROOT_PATH + "bg_charm_10gan_2.sub"},
						{"name":"bg_weekly_row_32", "type":"button", "x":58, "y":170, "default_image" : ROOT_PATH + "bg_charm_10gan_3.sub", "over_image" : ROOT_PATH + "bg_charm_10gan_3.sub", "down_image" : ROOT_PATH + "bg_charm_10gan_3.sub"},
						{"name":"bg_weekly_row_33", "type":"button", "x":58, "y":198, "default_image" : ROOT_PATH + "bg_charm_10gan_4.sub", "over_image" : ROOT_PATH + "bg_charm_10gan_4.sub", "down_image" : ROOT_PATH + "bg_charm_10gan_4.sub"},
						{"name":"bg_weekly_row_34", "type":"button", "x":58, "y":226, "default_image" : ROOT_PATH + "bg_charm_10gan_5.sub", "over_image" : ROOT_PATH + "bg_charm_10gan_5.sub", "down_image" : ROOT_PATH + "bg_charm_10gan_5.sub"},
						{"name":"bg_weekly_row_35", "type":"button", "x":58, "y":254, "default_image" : ROOT_PATH + "bg_charm_10gan_6.sub", "over_image" : ROOT_PATH + "bg_charm_10gan_6.sub", "down_image" : ROOT_PATH + "bg_charm_10gan_6.sub"},
						{"name":"bg_weekly_row_36", "type":"button", "x":58, "y":282, "default_image" : ROOT_PATH + "bg_charm_10gan_7.sub", "over_image" : ROOT_PATH + "bg_charm_10gan_7.sub", "down_image" : ROOT_PATH + "bg_charm_10gan_7.sub"},
						{"name":"bg_weekly_row_37", "type":"button", "x":58, "y":310, "default_image" : ROOT_PATH + "bg_charm_10gan_8.sub", "over_image" : ROOT_PATH + "bg_charm_10gan_8.sub", "down_image" : ROOT_PATH + "bg_charm_10gan_8.sub"},
						{"name":"bg_weekly_row_38", "type":"button", "x":58, "y":338, "default_image" : ROOT_PATH + "bg_charm_10gan_9.sub", "over_image" : ROOT_PATH + "bg_charm_10gan_9.sub", "down_image" : ROOT_PATH + "bg_charm_10gan_9.sub"},
						{"name":"bg_weekly_row_39", "type":"button", "x":58, "y":366, "default_image" : ROOT_PATH + "bg_charm_10gan_10.sub", "over_image" : ROOT_PATH + "bg_charm_10gan_10.sub", "down_image" : ROOT_PATH + "bg_charm_10gan_10.sub"},
						{"name":"bg_weekly_row_40", "type":"button", "x":86, "y":86, "default_image" : ROOT_PATH + "bg_count_slot_column.sub", "over_image" : ROOT_PATH + "bg_count_slot_column.sub", "down_image" : ROOT_PATH + "bg_count_slot_column.sub"},
						{"name":"bg_weekly_row_41", "type":"button", "x":114, "y":86, "default_image" : ROOT_PATH + "bg_need_count_slot_column.sub", "over_image" : ROOT_PATH + "bg_need_count_slot_column.sub", "down_image" : ROOT_PATH + "bg_need_count_slot_column.sub"},
						{"name":"bg_check", "type":"image", "x":142, "y":114, "image" : ROOT_PATH + "bg_check.sub"},
	
	
						{ "name":"12zi1", "type":"text", "x":155, "y":125-32, "text" : MISSION_COUNT, "text_horizontal_align":"center" },
						{ "name":"12zi2", "type":"text", "x":155+28*1, "y":125-32, "text" : MISSION_COUNT, "text_horizontal_align":"center" },
						{ "name":"12zi3", "type":"text", "x":155+28*2, "y":125-32, "text" : MISSION_COUNT, "text_horizontal_align":"center" },
						{ "name":"12zi4", "type":"text", "x":155+28*3, "y":125-32, "text" : MISSION_COUNT, "text_horizontal_align":"center" },
						{ "name":"12zi5", "type":"text", "x":155+28*4, "y":125-32, "text" : MISSION_COUNT, "text_horizontal_align":"center" },
						{ "name":"12zi6", "type":"text", "x":155+28*5, "y":125-32, "text" : MISSION_COUNT, "text_horizontal_align":"center" },
						{ "name":"12zi7", "type":"text", "x":155+28*6, "y":125-32, "text" : MISSION_COUNT, "text_horizontal_align":"center" },
						{ "name":"12zi8", "type":"text", "x":155+28*7, "y":125-32, "text" : MISSION_COUNT, "text_horizontal_align":"center" },
						{ "name":"12zi9", "type":"text", "x":155+28*8, "y":125-32, "text" : MISSION_COUNT, "text_horizontal_align":"center" },
						{ "name":"12zi10", "type":"text", "x":155+28*9, "y":125-32, "text" : MISSION_COUNT, "text_horizontal_align":"center" },
						{ "name":"12zi11", "type":"text", "x":155+28*10, "y":125-32, "text" : MISSION_COUNT, "text_horizontal_align":"center" },
						{ "name":"12zi12", "type":"text", "x":155+28*11, "y":125-32, "text" : MISSION_COUNT, "text_horizontal_align":"center" },

						{ "name":"10gan1", "type":"text", "x":127, "y":153-32+28*0, "text" : MISSION_COUNT, "text_horizontal_align":"center" },
						{ "name":"10gan2", "type":"text", "x":127, "y":153-32+28*1, "text" : MISSION_COUNT, "text_horizontal_align":"center" },
						{ "name":"10gan3", "type":"text", "x":127, "y":153-32+28*2, "text" : MISSION_COUNT, "text_horizontal_align":"center" },
						{ "name":"10gan4", "type":"text", "x":127, "y":153-32+28*3, "text" : MISSION_COUNT, "text_horizontal_align":"center" },
						{ "name":"10gan5", "type":"text", "x":127, "y":153-32+28*4, "text" : MISSION_COUNT, "text_horizontal_align":"center" },
						{ "name":"10gan6", "type":"text", "x":127, "y":153-32+28*5, "text" : MISSION_COUNT, "text_horizontal_align":"center" },
						{ "name":"10gan7", "type":"text", "x":127, "y":153-32+28*6, "text" : MISSION_COUNT, "text_horizontal_align":"center" },
						{ "name":"10gan8", "type":"text", "x":127, "y":153-32+28*7, "text" : MISSION_COUNT, "text_horizontal_align":"center" },
						{ "name":"10gan9", "type":"text", "x":127, "y":153-32+28*8, "text" : MISSION_COUNT, "text_horizontal_align":"center" },
						{ "name":"10gan10", "type":"text", "x":127, "y":153-32+28*9, "text" : MISSION_COUNT, "text_horizontal_align":"center" },
						
						
						#Gods required
						{ "name":"muiezenu0", "type":"text", "x":155, "y":125-32-28, "text" : MISSION_COUNT, "text_horizontal_align":"center" },
						{ "name":"muiezenu1", "type":"text", "x":155+28*1, "y":125-32-28, "text" : MISSION_COUNT, "text_horizontal_align":"center" },
						{ "name":"muiezenu2", "type":"text", "x":155+28*2, "y":125-32-28, "text" : MISSION_COUNT, "text_horizontal_align":"center" },
						{ "name":"muiezenu3", "type":"text", "x":155+28*3, "y":125-32-28, "text" : MISSION_COUNT, "text_horizontal_align":"center" },
						{ "name":"muiezenu4", "type":"text", "x":155+28*4, "y":125-32-28, "text" : MISSION_COUNT, "text_horizontal_align":"center" },
						{ "name":"muiezenu5", "type":"text", "x":155+28*5, "y":125-32-28, "text" : MISSION_COUNT, "text_horizontal_align":"center" },
						{ "name":"muiezenu6", "type":"text", "x":155+28*6, "y":125-32-28, "text" : MISSION_COUNT, "text_horizontal_align":"center" },
						{ "name":"muiezenu7", "type":"text", "x":155+28*7, "y":125-32-28, "text" : MISSION_COUNT, "text_horizontal_align":"center" },
						{ "name":"muiezenu8", "type":"text", "x":155+28*8, "y":125-32-28, "text" : MISSION_COUNT, "text_horizontal_align":"center" },
						{ "name":"muiezenu9", "type":"text", "x":155+28*9, "y":125-32-28, "text" : MISSION_COUNT, "text_horizontal_align":"center" },
						{ "name":"muiezenu10", "type":"text", "x":155+28*10, "y":125-32-28, "text" : MISSION_COUNT, "text_horizontal_align":"center" },
						{ "name":"muiezenu11", "type":"text", "x":155+28*11, "y":125-32-28, "text" : MISSION_COUNT, "text_horizontal_align":"center" },
						
						#Insignia required
						{ "name":"muiezenu12", "type":"text", "x":127-28, "y":153-32+28*0, "text" : MISSION_COUNT, "text_horizontal_align":"center" },
						{ "name":"muiezenu13", "type":"text", "x":127-28, "y":153-32+28*1, "text" : MISSION_COUNT, "text_horizontal_align":"center" },
						{ "name":"muiezenu14", "type":"text", "x":127-28, "y":153-32+28*2, "text" : MISSION_COUNT, "text_horizontal_align":"center" },
						{ "name":"muiezenu15", "type":"text", "x":127-28, "y":153-32+28*3, "text" : MISSION_COUNT, "text_horizontal_align":"center" },
						{ "name":"muiezenu16", "type":"text", "x":127-28, "y":153-32+28*4, "text" : MISSION_COUNT, "text_horizontal_align":"center" },
						{ "name":"muiezenu17", "type":"text", "x":127-28, "y":153-32+28*5, "text" : MISSION_COUNT, "text_horizontal_align":"center" },
						{ "name":"muiezenu18", "type":"text", "x":127-28, "y":153-32+28*6, "text" : MISSION_COUNT, "text_horizontal_align":"center" },
						{ "name":"muiezenu19", "type":"text", "x":127-28, "y":153-32+28*7, "text" : MISSION_COUNT, "text_horizontal_align":"center" },
						{ "name":"muiezenu20", "type":"text", "x":127-28, "y":153-32+28*8, "text" : MISSION_COUNT, "text_horizontal_align":"center" },
						{ "name":"muiezenu21", "type":"text", "x":127-28, "y":153-32+28*9, "text" : MISSION_COUNT, "text_horizontal_align":"center" },
						
					),
				},

				## Check				
				{
					"name" : "CheckButtonWindow",
					"type" : "window",

					"x" : 153,
					"y" : 147,
					"width" : 336,
					"height" :280,
				},
				
				## Button
				{
					"name" : "YellowInactive",
					"type" : "image",

					"x" : 11,
					"y" : 430,

					"image" : ROOT_PATH + "btn_yellow_inactive.sub",
				},
				#AICI SE LUCREAZA
				{ 
					"name":"muietiger0", 
					"type":"text", 
					"x" : 11 + 52,
					"y" : 430 + 3,
					"text" : "0", 
					"text_horizontal_align":"center" 
				},

				
				{
					"name" : "GreenBTN_30",
					"type" : "button",

					"x" : 11,
					"y" : 430,

					"default_image" : ROOT_PATH + "btn_yellow_default.sub",
					"over_image" : ROOT_PATH + "btn_yellow_over.sub",
					"down_image" : ROOT_PATH + "btn_yellow_down.sub",
				},
				{
					"name" : "YellowRewardCount",
					"type" : "numberline",
					
					"x" : 11+60,
					"y" : 430+12,
				},
				{
					"name" : "GreenInactive",
					"type" : "image",

					"x" : 99,
					"y" : 430,

					"image" : ROOT_PATH + "btn_green_inactive.sub",
				},
				# AICI SE LUCREAZA
				{ 
					"name":"muietiger1", 
					"type":"text", 
					"x" : 99 + 53,
					"y" : 430 + 3,
					"text" : "0", 
					"text_horizontal_align":"center" 
				},
				{
					"name" : "GreenBTN_31",
					"type" : "button",

					"x" : 99,
					"y" : 430,

					"default_image" : ROOT_PATH + "btn_green_default.sub",
					"over_image" : ROOT_PATH + "btn_green_over.sub",
					"down_image" : ROOT_PATH + "btn_green_down.sub",
				},				
				{
					"name" : "GreenRewardCount",
					"type" : "numberline",
					
					"x" : 99+60,
					"y" : 430+12,
				},
				{
					"name" : "AllClearButtonInactive",
					"type" : "image",

					"x" : 391,
					"y" : 430,

					"image" : ROOT_PATH + "btn_gold_down.sub",
				},
				{
					"name" : "GreenBTN_32",
					"type" : "button",

					"x" : 391,
					"y" : 430,

					"default_image" : ROOT_PATH + "btn_gold_default.sub",
					"over_image" : ROOT_PATH + "btn_gold_over.sub",
					"down_image" : ROOT_PATH + "btn_gold_down.sub",
				},
				##YELLOW FIRST ROW
				{
					"name" : "YellowBTN_0",
					"type" : "button",

					"x" : 153,
					"y" : 148,
					

					"default_image" : ROOT_PATH + "clear_yellow.sub",
					"over_image" : ROOT_PATH + "check_yellow.sub",
					"down_image" : ROOT_PATH + "down_new_yellow.sub",
				},
				{
					"name" : "YellowBTN_1",
					"type" : "button",

					"x" : 153 + 56,
					"y" : 148,
					

					"default_image" : ROOT_PATH + "clear_yellow.sub",
					"over_image" : ROOT_PATH + "check_yellow.sub",
					"down_image" : ROOT_PATH + "down_new_yellow.sub",
				},
				{
					"name" : "YellowBTN_2",
					"type" : "button",

					"x" : 153 + 56 * 2,
					"y" : 148,
					

					"default_image" : ROOT_PATH + "clear_yellow.sub",
					"over_image" : ROOT_PATH + "check_yellow.sub",
					"down_image" : ROOT_PATH + "down_new_yellow.sub",
				},
				{
					"name" : "YellowBTN_3",
					"type" : "button",

					"x" : 153 + 56 * 3,
					"y" : 148,
					

					"default_image" : ROOT_PATH + "clear_yellow.sub",
					"over_image" : ROOT_PATH + "check_yellow.sub",
					"down_image" : ROOT_PATH + "down_new_yellow.sub",
				},
				{
					"name" : "YellowBTN_4",
					"type" : "button",

					"x" : 153 + 56 * 4,
					"y" : 148,
					

					"default_image" : ROOT_PATH + "clear_yellow.sub",
					"over_image" : ROOT_PATH + "check_yellow.sub",
					"down_image" : ROOT_PATH + "down_new_yellow.sub",
				},
				{
					"name" : "YellowBTN_5",
					"type" : "button",

					"x" : 153 + 56 * 5,
					"y" : 148,
					

					"default_image" : ROOT_PATH + "clear_yellow.sub",
					"over_image" : ROOT_PATH + "check_yellow.sub",
					"down_image" : ROOT_PATH + "down_new_yellow.sub",
				},
				##YELLOW SECOND ROW
				{
					"name" : "YellowBTN_6",
					"type" : "button",

					"x" : 153,
					"y" : 148 + 56,
					

					"default_image" : ROOT_PATH + "clear_yellow.sub",
					"over_image" : ROOT_PATH + "check_yellow.sub",
					"down_image" : ROOT_PATH + "down_new_yellow.sub",
				},
				{
					"name" : "YellowBTN_7",
					"type" : "button",

					"x" : 153 + 56,
					"y" : 148 + 56,
					

					"default_image" : ROOT_PATH + "clear_yellow.sub",
					"over_image" : ROOT_PATH + "check_yellow.sub",
					"down_image" : ROOT_PATH + "down_new_yellow.sub",
				},
				{
					"name" : "YellowBTN_8",
					"type" : "button",

					"x" : 153 + 56 * 2,
					"y" : 148 + 56,
					

					"default_image" : ROOT_PATH + "clear_yellow.sub",
					"over_image" : ROOT_PATH + "check_yellow.sub",
					"down_image" : ROOT_PATH + "down_new_yellow.sub",
				},
				{
					"name" : "YellowBTN_9",
					"type" : "button",

					"x" : 153 + 56 * 3,
					"y" : 148 + 56,
					

					"default_image" : ROOT_PATH + "clear_yellow.sub",
					"over_image" : ROOT_PATH + "check_yellow.sub",
					"down_image" : ROOT_PATH + "down_new_yellow.sub",
				},
				{
					"name" : "YellowBTN_10",
					"type" : "button",

					"x" : 153 + 56 * 4,
					"y" : 148 + 56,
					

					"default_image" : ROOT_PATH + "clear_yellow.sub",
					"over_image" : ROOT_PATH + "check_yellow.sub",
					"down_image" : ROOT_PATH + "down_new_yellow.sub",
				},
				{
					"name" : "YellowBTN_11",
					"type" : "button",

					"x" : 153 + 56 * 5,
					"y" : 148 + 56,
					

					"default_image" : ROOT_PATH + "clear_yellow.sub",
					"over_image" : ROOT_PATH + "check_yellow.sub",
					"down_image" : ROOT_PATH + "down_new_yellow.sub",
				},
				##YELLOW THIRD ROW
				{
					"name" : "YellowBTN_12",
					"type" : "button",

					"x" : 153,
					"y" : 148 + 56 + 56,
					

					"default_image" : ROOT_PATH + "clear_yellow.sub",
					"over_image" : ROOT_PATH + "check_yellow.sub",
					"down_image" : ROOT_PATH + "down_new_yellow.sub",
				},
				{
					"name" : "YellowBTN_13",
					"type" : "button",

					"x" : 153 + 56,
					"y" : 148 + 56 + 56,
					

					"default_image" : ROOT_PATH + "clear_yellow.sub",
					"over_image" : ROOT_PATH + "check_yellow.sub",
					"down_image" : ROOT_PATH + "down_new_yellow.sub",
				},
				{
					"name" : "YellowBTN_14",
					"type" : "button",

					"x" : 153 + 56 * 2,
					"y" : 148 + 56 + 56,
					

					"default_image" : ROOT_PATH + "clear_yellow.sub",
					"over_image" : ROOT_PATH + "check_yellow.sub",
					"down_image" : ROOT_PATH + "down_new_yellow.sub",
				},
				{
					"name" : "YellowBTN_15",
					"type" : "button",

					"x" : 153 + 56 * 3,
					"y" : 148 + 56 + 56,
					

					"default_image" : ROOT_PATH + "clear_yellow.sub",
					"over_image" : ROOT_PATH + "check_yellow.sub",
					"down_image" : ROOT_PATH + "down_new_yellow.sub",
				},
				{
					"name" : "YellowBTN_16",
					"type" : "button",

					"x" : 153 + 56 * 4,
					"y" : 148 + 56 + 56,
					

					"default_image" : ROOT_PATH + "clear_yellow.sub",
					"over_image" : ROOT_PATH + "check_yellow.sub",
					"down_image" : ROOT_PATH + "down_new_yellow.sub",
				},
				{
					"name" : "YellowBTN_17",
					"type" : "button",

					"x" : 153 + 56 * 5,
					"y" : 148 + 56 + 56,
					

					"default_image" : ROOT_PATH + "clear_yellow.sub",
					"over_image" : ROOT_PATH + "check_yellow.sub",
					"down_image" : ROOT_PATH + "down_new_yellow.sub",
				},
				##YELLOW FORTH ROW
				{
					"name" : "YellowBTN_18",
					"type" : "button",

					"x" : 153,
					"y" : 148 + 56 + 56 + 56,
					

					"default_image" : ROOT_PATH + "clear_yellow.sub",
					"over_image" : ROOT_PATH + "check_yellow.sub",
					"down_image" : ROOT_PATH + "down_new_yellow.sub",
				},
				{
					"name" : "YellowBTN_19",
					"type" : "button",

					"x" : 153 + 56,
					"y" : 148 + 56 + 56 + 56,
					

					"default_image" : ROOT_PATH + "clear_yellow.sub",
					"over_image" : ROOT_PATH + "check_yellow.sub",
					"down_image" : ROOT_PATH + "down_new_yellow.sub",
				},
				{
					"name" : "YellowBTN_20",
					"type" : "button",

					"x" : 153 + 56 * 2,
					"y" : 148 + 56 + 56 + 56,
					

					"default_image" : ROOT_PATH + "clear_yellow.sub",
					"over_image" : ROOT_PATH + "check_yellow.sub",
					"down_image" : ROOT_PATH + "down_new_yellow.sub",
				},
				{
					"name" : "YellowBTN_21",
					"type" : "button",

					"x" : 153 + 56 * 3,
					"y" : 148 + 56 + 56 + 56,
					

					"default_image" : ROOT_PATH + "clear_yellow.sub",
					"over_image" : ROOT_PATH + "check_yellow.sub",
					"down_image" : ROOT_PATH + "down_new_yellow.sub",
				},
				{
					"name" : "YellowBTN_22",
					"type" : "button",

					"x" : 153 + 56 * 4,
					"y" : 148 + 56 + 56 + 56,
					

					"default_image" : ROOT_PATH + "clear_yellow.sub",
					"over_image" : ROOT_PATH + "check_yellow.sub",
					"down_image" : ROOT_PATH + "down_new_yellow.sub",
				},
				{
					"name" : "YellowBTN_23",
					"type" : "button",

					"x" : 153 + 56 * 5,
					"y" : 148 + 56 + 56 + 56,
					

					"default_image" : ROOT_PATH + "clear_yellow.sub",
					"over_image" : ROOT_PATH + "check_yellow.sub",
					"down_image" : ROOT_PATH + "down_new_yellow.sub",
				},
				##YELLOW FIFTH ROW
				{
					"name" : "YellowBTN_24",
					"type" : "button",

					"x" : 153,
					"y" : 148 + 56 + 56 + 56 + 56,
					

					"default_image" : ROOT_PATH + "clear_yellow.sub",
					"over_image" : ROOT_PATH + "check_yellow.sub",
					"down_image" : ROOT_PATH + "down_new_yellow.sub",
				},
				{
					"name" : "YellowBTN_25",
					"type" : "button",

					"x" : 153 + 56,
					"y" : 148 + 56 + 56 + 56 + 56,
					

					"default_image" : ROOT_PATH + "clear_yellow.sub",
					"over_image" : ROOT_PATH + "check_yellow.sub",
					"down_image" : ROOT_PATH + "down_new_yellow.sub",
				},
				{
					"name" : "YellowBTN_26",
					"type" : "button",

					"x" : 153 + 56 * 2,
					"y" : 148 + 56 + 56 + 56 + 56,
					

					"default_image" : ROOT_PATH + "clear_yellow.sub",
					"over_image" : ROOT_PATH + "check_yellow.sub",
					"down_image" : ROOT_PATH + "down_new_yellow.sub",
				},
				{
					"name" : "YellowBTN_27",
					"type" : "button",

					"x" : 153 + 56 * 3,
					"y" : 148 + 56 + 56 + 56 + 56,
					

					"default_image" : ROOT_PATH + "clear_yellow.sub",
					"over_image" : ROOT_PATH + "check_yellow.sub",
					"down_image" : ROOT_PATH + "down_new_yellow.sub",
				},
				{
					"name" : "YellowBTN_28",
					"type" : "button",

					"x" : 153 + 56 * 4,
					"y" : 148 + 56 + 56 + 56 + 56,
					

					"default_image" : ROOT_PATH + "clear_yellow.sub",
					"over_image" : ROOT_PATH + "check_yellow.sub",
					"down_image" : ROOT_PATH + "down_new_yellow.sub",
				},
				{
					"name" : "YellowBTN_29",
					"type" : "button",

					"x" : 153 + 56 * 5,
					"y" : 148 + 56 + 56 + 56 + 56,
					

					"default_image" : ROOT_PATH + "clear_yellow.sub",
					"over_image" : ROOT_PATH + "check_yellow.sub",
					"down_image" : ROOT_PATH + "down_new_yellow.sub",
				},
				##### START OF YELLOW CHECKBOXES#####
				##GREEN FIRST ROW
				{
					"name" : "GreenBTN_0",
					"type" : "button",

					"x" : 181,
					"y" : 176,
					

					"default_image" : ROOT_PATH + "clear_green.sub",
					"over_image" : ROOT_PATH + "check_green.sub",
					"down_image" : ROOT_PATH + "down_new_green.sub",
				},
				{
					"name" : "GreenBTN_1",
					"type" : "button",

					"x" : 181 + 56,
					"y" : 176,
					

					"default_image" : ROOT_PATH + "clear_green.sub",
					"over_image" : ROOT_PATH + "check_green.sub",
					"down_image" : ROOT_PATH + "down_new_green.sub",
				},
				{
					"name" : "GreenBTN_2",
					"type" : "button",

					"x" : 181 + 56 * 2,
					"y" : 176,
					

					"default_image" : ROOT_PATH + "clear_green.sub",
					"over_image" : ROOT_PATH + "check_green.sub",
					"down_image" : ROOT_PATH + "down_new_green.sub",
				},
				{
					"name" : "GreenBTN_3",
					"type" : "button",

					"x" : 181 + 56 * 3,
					"y" : 176,
					

					"default_image" : ROOT_PATH + "clear_green.sub",
					"over_image" : ROOT_PATH + "check_green.sub",
					"down_image" : ROOT_PATH + "down_new_green.sub",
				},
				{
					"name" : "GreenBTN_4",
					"type" : "button",

					"x" : 181 + 56 * 4,
					"y" : 176,
					

					"default_image" : ROOT_PATH + "clear_green.sub",
					"over_image" : ROOT_PATH + "check_green.sub",
					"down_image" : ROOT_PATH + "down_new_green.sub",
				},
				{
					"name" : "GreenBTN_5",
					"type" : "button",

					"x" : 181 + 56 * 5,
					"y" : 176,
					

					"default_image" : ROOT_PATH + "clear_green.sub",
					"over_image" : ROOT_PATH + "check_green.sub",
					"down_image" : ROOT_PATH + "down_new_green.sub",
				},
				##GREEN SECOND ROW
				{
					"name" : "GreenBTN_6",
					"type" : "button",

					"x" : 181,
					"y" : 176 + 56,
					

					"default_image" : ROOT_PATH + "clear_green.sub",
					"over_image" : ROOT_PATH + "check_green.sub",
					"down_image" : ROOT_PATH + "down_new_green.sub",
				},
				{
					"name" : "GreenBTN_7",
					"type" : "button",

					"x" : 181 + 56,
					"y" : 176 + 56,
					

					"default_image" : ROOT_PATH + "clear_green.sub",
					"over_image" : ROOT_PATH + "check_green.sub",
					"down_image" : ROOT_PATH + "down_new_green.sub",
				},
				{
					"name" : "GreenBTN_8",
					"type" : "button",

					"x" : 181 + 56 * 2,
					"y" : 176 + 56,
					

					"default_image" : ROOT_PATH + "clear_green.sub",
					"over_image" : ROOT_PATH + "check_green.sub",
					"down_image" : ROOT_PATH + "down_new_green.sub",
				},
				{
					"name" : "GreenBTN_9",
					"type" : "button",

					"x" : 181 + 56 * 3,
					"y" : 176 + 56,
					

					"default_image" : ROOT_PATH + "clear_green.sub",
					"over_image" : ROOT_PATH + "check_green.sub",
					"down_image" : ROOT_PATH + "down_new_green.sub",
				},
				{
					"name" : "GreenBTN_10",
					"type" : "button",

					"x" : 181 + 56 * 4,
					"y" : 176 + 56,
					

					"default_image" : ROOT_PATH + "clear_green.sub",
					"over_image" : ROOT_PATH + "check_green.sub",
					"down_image" : ROOT_PATH + "down_new_green.sub",
				},
				{
					"name" : "GreenBTN_11",
					"type" : "button",

					"x" : 181 + 56 * 5,
					"y" : 176 + 56,
					

					"default_image" : ROOT_PATH + "clear_green.sub",
					"over_image" : ROOT_PATH + "check_green.sub",
					"down_image" : ROOT_PATH + "down_new_green.sub",
				},
				##GREEN THIRD ROW
				{
					"name" : "GreenBTN_12",
					"type" : "button",

					"x" : 181,
					"y" : 176 + 56 + 56,
					

					"default_image" : ROOT_PATH + "clear_green.sub",
					"over_image" : ROOT_PATH + "check_green.sub",
					"down_image" : ROOT_PATH + "down_new_green.sub",
				},
				{
					"name" : "GreenBTN_13",
					"type" : "button",

					"x" : 181 + 56,
					"y" : 176 + 56 + 56,
					

					"default_image" : ROOT_PATH + "clear_green.sub",
					"over_image" : ROOT_PATH + "check_green.sub",
					"down_image" : ROOT_PATH + "down_new_green.sub",
				},
				{
					"name" : "GreenBTN_14",
					"type" : "button",

					"x" : 181 + 56 * 2,
					"y" : 176 + 56 + 56,
					

					"default_image" : ROOT_PATH + "clear_green.sub",
					"over_image" : ROOT_PATH + "check_green.sub",
					"down_image" : ROOT_PATH + "down_new_green.sub",
				},
				{
					"name" : "GreenBTN_15",
					"type" : "button",

					"x" : 181 + 56 * 3,
					"y" : 176 + 56 + 56,
					

					"default_image" : ROOT_PATH + "clear_green.sub",
					"over_image" : ROOT_PATH + "check_green.sub",
					"down_image" : ROOT_PATH + "down_new_green.sub",
				},
				{
					"name" : "GreenBTN_16",
					"type" : "button",

					"x" : 181 + 56 * 4,
					"y" : 176 + 56 + 56,
					

					"default_image" : ROOT_PATH + "clear_green.sub",
					"over_image" : ROOT_PATH + "check_green.sub",
					"down_image" : ROOT_PATH + "down_new_green.sub",
				},
				{
					"name" : "GreenBTN_17",
					"type" : "button",

					"x" : 181 + 56 * 5,
					"y" : 176 + 56 + 56,
					

					"default_image" : ROOT_PATH + "clear_green.sub",
					"over_image" : ROOT_PATH + "check_green.sub",
					"down_image" : ROOT_PATH + "down_new_green.sub",
				},
				##GREEN FORTH ROW
				{
					"name" : "GreenBTN_18",
					"type" : "button",

					"x" : 181,
					"y" : 176 + 56 + 56 + 56,
					

					"default_image" : ROOT_PATH + "clear_green.sub",
					"over_image" : ROOT_PATH + "check_green.sub",
					"down_image" : ROOT_PATH + "down_new_green.sub",
				},
				{
					"name" : "GreenBTN_19",
					"type" : "button",

					"x" : 181 + 56,
					"y" : 176 + 56 + 56 + 56,
					

					"default_image" : ROOT_PATH + "clear_green.sub",
					"over_image" : ROOT_PATH + "check_green.sub",
					"down_image" : ROOT_PATH + "down_new_green.sub",
				},
				{
					"name" : "GreenBTN_20",
					"type" : "button",

					"x" : 181 + 56 * 2,
					"y" : 176 + 56 + 56 + 56,
					

					"default_image" : ROOT_PATH + "clear_green.sub",
					"over_image" : ROOT_PATH + "check_green.sub",
					"down_image" : ROOT_PATH + "down_new_green.sub",
				},
				{
					"name" : "GreenBTN_21",
					"type" : "button",

					"x" : 181 + 56 * 3,
					"y" : 176 + 56 + 56 + 56,
					

					"default_image" : ROOT_PATH + "clear_green.sub",
					"over_image" : ROOT_PATH + "check_green.sub",
					"down_image" : ROOT_PATH + "down_new_green.sub",
				},
				{
					"name" : "GreenBTN_22",
					"type" : "button",

					"x" : 181 + 56 * 4,
					"y" : 176 + 56 + 56 + 56,
					

					"default_image" : ROOT_PATH + "clear_green.sub",
					"over_image" : ROOT_PATH + "check_green.sub",
					"down_image" : ROOT_PATH + "down_new_green.sub",
				},
				{
					"name" : "GreenBTN_23",
					"type" : "button",

					"x" : 181 + 56 * 5,
					"y" : 176 + 56 + 56 + 56,
					

					"default_image" : ROOT_PATH + "clear_green.sub",
					"over_image" : ROOT_PATH + "check_green.sub",
					"down_image" : ROOT_PATH + "down_new_green.sub",
				},
				##GREEN FIFTH ROW
				{
					"name" : "GreenBTN_24",
					"type" : "button",

					"x" : 181,
					"y" : 176 + 56 + 56 + 56 + 56,
					

					"default_image" : ROOT_PATH + "clear_green.sub",
					"over_image" : ROOT_PATH + "check_green.sub",
					"down_image" : ROOT_PATH + "down_new_green.sub",
				},
				{
					"name" : "GreenBTN_25",
					"type" : "button",

					"x" : 181 + 56,
					"y" : 176 + 56 + 56 + 56 + 56,
					

					"default_image" : ROOT_PATH + "clear_green.sub",
					"over_image" : ROOT_PATH + "check_green.sub",
					"down_image" : ROOT_PATH + "down_new_green.sub",
				},
				{
					"name" : "GreenBTN_26",
					"type" : "button",

					"x" : 181 + 56 * 2,
					"y" : 176 + 56 + 56 + 56 + 56,
					

					"default_image" : ROOT_PATH + "clear_green.sub",
					"over_image" : ROOT_PATH + "check_green.sub",
					"down_image" : ROOT_PATH + "down_new_green.sub",
				},
				{
					"name" : "GreenBTN_27",
					"type" : "button",

					"x" : 181 + 56 * 3,
					"y" : 176 + 56 + 56 + 56 + 56,
					

					"default_image" : ROOT_PATH + "clear_green.sub",
					"over_image" : ROOT_PATH + "check_green.sub",
					"down_image" : ROOT_PATH + "down_new_green.sub",
				},
				{
					"name" : "GreenBTN_28",
					"type" : "button",

					"x" : 181 + 56 * 4,
					"y" : 176 + 56 + 56 + 56 + 56,
					

					"default_image" : ROOT_PATH + "clear_green.sub",
					"over_image" : ROOT_PATH + "check_green.sub",
					"down_image" : ROOT_PATH + "down_new_green.sub",
				},
				{
					"name" : "GreenBTN_29",
					"type" : "button",

					"x" : 181 + 56 * 5,
					"y" : 176 + 56 + 56 + 56 + 56,
					

					"default_image" : ROOT_PATH + "clear_green.sub",
					"over_image" : ROOT_PATH + "check_green.sub",
					"down_image" : ROOT_PATH + "down_new_green.sub",
				},
			),
		},
	),
}

