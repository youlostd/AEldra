import app

ROOT_PATH = "d:/ymir work/ui/ziranking/"
SLOT_DISTANCE = 25
BAR_DEFAULT_Y = 6
BAR_SPACE_1 = 50

window = {
	"name" : "zi_Reward_Window",

	"x" : (SCREEN_WIDTH -510) / 2,
	"y" : (SCREEN_HEIGHT - 340) / 2,

	"style" : ("movable", "float",),

	"width" : 510,
	"height" : 340,

	"children" :
	(
		{
			"name" : "zirankingboard",
			"type" : "board",

			"x" : 0,
			"y" : 0,

			"width" : 510,
			"height" : 340,
		
			"children" :
			(
				## Title
				{
					"name" : "TitleBar",
					"type" : "titlebar",

					"x" : 6,
					"y" : 6,

					"width" : 487 + 9,
					"color" : "yellow",

					"children" :
					(
						{ "name":"TitleName", "type":"text", "x":250, "y":3, "text" : "Zodiac Ranking Table", "text_horizontal_align":"center" },
					),
				},
				## Background Window
				{
					"name" : "BgWindow",

					"x" : 10,
					"y" : 32,

					"width" : 510,
					"height" : 340,
					
					"children" :
					(	
						## INTERFACE BG
						{
							"name":"BackgroundInterfaceRanking",
							"type":"image",
							
							"x":10,
							"y":9,

							"image" : ROOT_PATH + "zenumuie.tga",
							
							"children" :
							(
								#Rank text
								{ 
									"name":"TOPBARTEXT_1", 
									"type":"text", 
									"x":12, 
									"y":BAR_DEFAULT_Y, 
									"text" : "Rank", 
									"text_horizontal_align":"left" 
								},
								#Leader text
								{ 
									"name":"TOPBARTEXT_2", 
									"type":"text", 
									"x":BAR_SPACE_1 + 26, 
									"y":BAR_DEFAULT_Y, 
									"text" : "Leader's Name", 
									"text_horizontal_align":"left" 
								},
								#Level text
								{ 
									"name":"TOPBARTEXT_3", 
									"type":"text", 
									"x":BAR_SPACE_1*3 + 60, 
									"y":BAR_DEFAULT_Y, 
									"text" : "Level", 
									"text_horizontal_align":"left" 
								},
								#Time text
								{ 
									"name":"TOPBARTEXT_4", 
									"type":"text", 
									"x":BAR_SPACE_1*6, 
									"y":BAR_DEFAULT_Y, 
									"text" : "Time", 
									"text_horizontal_align":"left" 
								},
								#Date text
								{ 
									"name":"TOPBARTEXT_4", 
									"type":"text", 
									"x":BAR_SPACE_1*8, 
									"y":BAR_DEFAULT_Y, 
									"text" : "Date", 
									"text_horizontal_align":"left" 
								},
								## Hover Stuff
								{
									"name" : "MuieZenu_1",
									"type" : "button",

									"x" : 3,
									"y" : 28,
									

									"default_image" : ROOT_PATH + "muietiger.tga",
									"over_image" : ROOT_PATH + "muiezenu.tga",
									"down_image" : ROOT_PATH + "muiezenu.tga",
								},
								## Hover Stuff
								{
									"name" : "MuieZenu_2",
									"type" : "button",

									"x" : 3,
									"y" : 28 + SLOT_DISTANCE,
									

									"default_image" : ROOT_PATH + "muietiger.tga",
									"over_image" : ROOT_PATH + "muiezenu.tga",
									"down_image" : ROOT_PATH + "muiezenu.tga",
								},
								## Hover Stuff
								{
									"name" : "MuieZenu_3",
									"type" : "button",

									"x" : 3,
									"y" : 28 + SLOT_DISTANCE*2,
									

									"default_image" : ROOT_PATH + "muietiger.tga",
									"over_image" : ROOT_PATH + "muiezenu.tga",
									"down_image" : ROOT_PATH + "muiezenu.tga",
								},
								## Hover Stuff
								{
									"name" : "MuieZenu_4",
									"type" : "button",

									"x" : 3,
									"y" : 28 + SLOT_DISTANCE*3,
									

									"default_image" : ROOT_PATH + "muietiger.tga",
									"over_image" : ROOT_PATH + "muiezenu.tga",
									"down_image" : ROOT_PATH + "muiezenu.tga",
								},
								## Hover Stuff
								{
									"name" : "MuieZenu_5",
									"type" : "button",

									"x" : 3,
									"y" : 28 + SLOT_DISTANCE*4,
									

									"default_image" : ROOT_PATH + "muietiger.tga",
									"over_image" : ROOT_PATH + "muiezenu.tga",
									"down_image" : ROOT_PATH + "muiezenu.tga",
								},
								## Hover Stuff
								{
									"name" : "MuieZenu_6",
									"type" : "button",

									"x" : 3,
									"y" : 28 + SLOT_DISTANCE*5,
									

									"default_image" : ROOT_PATH + "muietiger.tga",
									"over_image" : ROOT_PATH + "muiezenu.tga",
									"down_image" : ROOT_PATH + "muiezenu.tga",
								},
								## Hover Stuff
								{
									"name" : "MuieZenu_7",
									"type" : "button",

									"x" : 3,
									"y" : 28 + SLOT_DISTANCE*6,
									

									"default_image" : ROOT_PATH + "muietiger.tga",
									"over_image" : ROOT_PATH + "muiezenu.tga",
									"down_image" : ROOT_PATH + "muiezenu.tga",
								},
								## Hover Stuff
								{
									"name" : "MuieZenu_8",
									"type" : "button",

									"x" : 3,
									"y" : 28 + SLOT_DISTANCE*7,
									

									"default_image" : ROOT_PATH + "muietiger.tga",
									"over_image" : ROOT_PATH + "muiezenu.tga",
									"down_image" : ROOT_PATH + "muiezenu.tga",
								},
								## Hover Stuff
								{
									"name" : "MuieZenu_9",
									"type" : "button",

									"x" : 3,
									"y" : 28 + SLOT_DISTANCE*8,
									

									"default_image" : ROOT_PATH + "muietiger.tga",
									"over_image" : ROOT_PATH + "muiezenu.tga",
									"down_image" : ROOT_PATH + "muiezenu.tga",
								},
								## Hover Stuff
								{
									"name" : "MuieZenu_10",
									"type" : "button",

									"x" : 3,
									"y" : 28 + SLOT_DISTANCE*9,
									

									"default_image" : ROOT_PATH + "muietiger.tga",
									"over_image" : ROOT_PATH + "muiezenu.tga",
									"down_image" : ROOT_PATH + "muiezenu.tga",
								},
								
								#################### --------------- REAL DEAL ------------ ########################

								#Rank text
								{ 
									"name":"Rank_1", 
									"type":"text", 
									"x":12 + 7, 
									"y":BAR_DEFAULT_Y + 24, 
									"text" : "#1", 
									"text_horizontal_align":"left" 
								},
								#Leader text
								{ 
									"name":"Zi_Rank_Name_1", 
									"type":"text", 
									"x":BAR_SPACE_1 + 36, 
									"y":BAR_DEFAULT_Y + 24, 
									"text" : "- none -", 
									"text_horizontal_align":"left" 
								},
								#Level text
								{ 
									"name":"Zi_Rank_Level_1", 
									"type":"text", 
									"x":BAR_SPACE_1*3 + 60, 
									"y":BAR_DEFAULT_Y + 24, 
									"text" : "- none -", 
									"text_horizontal_align":"center" 
								},
								#Time text
								{ 
									"name":"Zi_Rank_Time_1", 
									"type":"text", 
									"x":BAR_SPACE_1*6 + 10, 
									"y":BAR_DEFAULT_Y + 24, 
									"text" : "- none -", 
									"text_horizontal_align":"center" 
								},
								#Date text
								{ 
									"name":"Zi_Rank_Date_1", 
									"type":"text", 
									"x":BAR_SPACE_1*8 + 10, 
									"y":BAR_DEFAULT_Y + 24, 
									"text" : "- none -", 
									"text_horizontal_align":"center" 
								},
								#RANK 2
								#Rank text
								{ 
									"name":"Rank_2", 
									"type":"text", 
									"x":12 + 7, 
									# "y":BAR_DEFAULT_Y + 24, 
									"y" : 28 + SLOT_DISTANCE,
									"text" : "#2", 
									"text_horizontal_align":"left" 
								},
								#Leader text
								{ 
									"name":"Zi_Rank_Name_2", 
									"type":"text", 
									"x":BAR_SPACE_1 + 36, 
									# "y":BAR_DEFAULT_Y + 24, 
									"y" : 28 + SLOT_DISTANCE,
									"text" : "- none -", 
									"text_horizontal_align":"left" 
								},
								#Level text
								{ 
									"name":"Zi_Rank_Level_2", 
									"type":"text", 
									"x":BAR_SPACE_1*3 + 60, 
									# "y":BAR_DEFAULT_Y + 24, 
									"y" : 28 + SLOT_DISTANCE,
									"text" : "- none -", 
									"text_horizontal_align":"center" 
								},
								#Time text
								{ 
									"name":"Zi_Rank_Time_2", 
									"type":"text", 
									"x":BAR_SPACE_1*6 + 10, 
									# "y":BAR_DEFAULT_Y + 24, 
									"y" : 28 + SLOT_DISTANCE,
									"text" : "- none -", 
									"text_horizontal_align":"center" 
								},
								#Date text
								{ 
									"name":"Zi_Rank_Date_2", 
									"type":"text", 
									"x":BAR_SPACE_1*8 + 10, 
									# "y":BAR_DEFAULT_Y + 24, 
									"y" : 28 + SLOT_DISTANCE,
									"text" : "- none -", 
									"text_horizontal_align":"center" 
								},
								
								#RANK 3
								#Rank text
								{ 
									"name":"Rank_3", 
									"type":"text", 
									"x":12 + 7, 
									# "y":BAR_DEFAULT_Y + 24, 
									"y" : 28 + SLOT_DISTANCE*2,
									"text" : "#3", 
									"text_horizontal_align":"left" 
								},
								#Leader text
								{ 
									"name":"Zi_Rank_Name_3", 
									"type":"text", 
									"x":BAR_SPACE_1 + 36, 
									# "y":BAR_DEFAULT_Y + 24, 
									"y" : 28 + SLOT_DISTANCE*2,
									"text" : "- none -", 
									"text_horizontal_align":"left" 
								},
								#Level text
								{ 
									"name":"Zi_Rank_Level_3", 
									"type":"text", 
									"x":BAR_SPACE_1*3 + 60, 
									# "y":BAR_DEFAULT_Y + 24, 
									"y" : 28 + SLOT_DISTANCE*2,
									"text" : "- none -", 
									"text_horizontal_align":"center" 
								},
								#Time text
								{ 
									"name":"Zi_Rank_Time_3", 
									"type":"text", 
									"x":BAR_SPACE_1*6 + 10, 
									# "y":BAR_DEFAULT_Y + 24, 
									"y" : 28 + SLOT_DISTANCE*2,
									"text" : "- none -", 
									"text_horizontal_align":"center" 
								},
								#Date text
								{ 
									"name":"Zi_Rank_Date_3", 
									"type":"text", 
									"x":BAR_SPACE_1*8 + 10, 
									# "y":BAR_DEFAULT_Y + 24, 
									"y" : 28 + SLOT_DISTANCE*2,
									"text" : "- none -", 
									"text_horizontal_align":"center" 
								},
								
								#RANK 4
								#Rank text
								{ 
									"name":"Rank_4", 
									"type":"text", 
									"x":12 + 11,
									# "y":BAR_DEFAULT_Y + 24, 
									"y" : 28 + SLOT_DISTANCE*3,
									"text" : "4", 
									"text_horizontal_align":"left" 
								},
								#Leader text
								{ 
									"name":"Zi_Rank_Name_4", 
									"type":"text", 
									"x":BAR_SPACE_1 + 36, 
									# "y":BAR_DEFAULT_Y + 24, 
									"y" : 28 + SLOT_DISTANCE*3,
									"text" : "- none -", 
									"text_horizontal_align":"left" 
								},
								#Level text
								{ 
									"name":"Zi_Rank_Level_4", 
									"type":"text", 
									"x":BAR_SPACE_1*3 + 60, 
									# "y":BAR_DEFAULT_Y + 24, 
									"y" : 28 + SLOT_DISTANCE*3,
									"text" : "- none -", 
									"text_horizontal_align":"center" 
								},
								#Time text
								{ 
									"name":"Zi_Rank_Time_4", 
									"type":"text", 
									"x":BAR_SPACE_1*6 + 10, 
									# "y":BAR_DEFAULT_Y + 24, 
									"y" : 28 + SLOT_DISTANCE*3,
									"text" : "- none -", 
									"text_horizontal_align":"center" 
								},
								#Date text
								{ 
									"name":"Zi_Rank_Date_4", 
									"type":"text", 
									"x":BAR_SPACE_1*8 + 10, 
									# "y":BAR_DEFAULT_Y + 24, 
									"y" : 28 + SLOT_DISTANCE*3,
									"text" : "- none -", 
									"text_horizontal_align":"center" 
								},
								#RANK 5
								#Rank text
								{ 
									"name":"Rank_5", 
									"type":"text", 
									"x":12 + 11, 
									# "y":BAR_DEFAULT_Y + 24, 
									"y" : 28 + SLOT_DISTANCE*4,
									"text" : "5", 
									"text_horizontal_align":"left" 
								},
								#Leader text
								{ 
									"name":"Zi_Rank_Name_5", 
									"type":"text", 
									"x":BAR_SPACE_1 + 36, 
									# "y":BAR_DEFAULT_Y + 24, 
									"y" : 28 + SLOT_DISTANCE*4,
									"text" : "- none -", 
									"text_horizontal_align":"left" 
								},
								#Level text
								{ 
									"name":"Zi_Rank_Level_5", 
									"type":"text", 
									"x":BAR_SPACE_1*3 + 60, 
									# "y":BAR_DEFAULT_Y + 24, 
									"y" : 28 + SLOT_DISTANCE*4,
									"text" : "- none -", 
									"text_horizontal_align":"center" 
								},
								#Time text
								{ 
									"name":"Zi_Rank_Time_5", 
									"type":"text", 
									"x":BAR_SPACE_1*6 + 10, 
									# "y":BAR_DEFAULT_Y + 24, 
									"y" : 28 + SLOT_DISTANCE*4,
									"text" : "- none -", 
									"text_horizontal_align":"center" 
								},
								#Date text
								{ 
									"name":"Zi_Rank_Date_5", 
									"type":"text", 
									"x":BAR_SPACE_1*8 + 10, 
									# "y":BAR_DEFAULT_Y + 24, 
									"y" : 28 + SLOT_DISTANCE*4,
									"text" : "- none -", 
									"text_horizontal_align":"center" 
								},
								#RANK 6
								#Rank text
								{ 
									"name":"Rank_6", 
									"type":"text", 
									"x":12 + 11,
									# "y":BAR_DEFAULT_Y + 24, 
									"y" : 28 + SLOT_DISTANCE*5,
									"text" : "6", 
									"text_horizontal_align":"left" 
								},
								#Leader text
								{ 
									"name":"Zi_Rank_Name_6", 
									"type":"text", 
									"x":BAR_SPACE_1 + 36, 
									# "y":BAR_DEFAULT_Y + 24, 
									"y" : 28 + SLOT_DISTANCE*5,
									"text" : "- none -", 
									"text_horizontal_align":"left" 
								},
								#Level text
								{ 
									"name":"Zi_Rank_Level_6", 
									"type":"text", 
									"x":BAR_SPACE_1*3 + 60, 
									# "y":BAR_DEFAULT_Y + 24, 
									"y" : 28 + SLOT_DISTANCE*5,
									"text" : "- none -", 
									"text_horizontal_align":"center" 
								},
								#Time text
								{ 
									"name":"Zi_Rank_Time_6", 
									"type":"text", 
									"x":BAR_SPACE_1*6 + 10, 
									# "y":BAR_DEFAULT_Y + 24, 
									"y" : 28 + SLOT_DISTANCE*5,
									"text" : "- none -", 
									"text_horizontal_align":"center" 
								},
								#Date text
								{ 
									"name":"Zi_Rank_Date_6", 
									"type":"text", 
									"x":BAR_SPACE_1*8 + 10, 
									# "y":BAR_DEFAULT_Y + 24, 
									"y" : 28 + SLOT_DISTANCE*5,
									"text" : "- none -", 
									"text_horizontal_align":"center" 
								},
								#RANK 7
								#Rank text
								{ 
									"name":"Rank_7", 
									"type":"text", 
									"x":12 + 11,
									# "y":BAR_DEFAULT_Y + 24, 
									"y" : 28 + SLOT_DISTANCE*6,
									"text" : "7", 
									"text_horizontal_align":"left" 
								},
								#Leader text
								{ 
									"name":"Zi_Rank_Name_7", 
									"type":"text", 
									"x":BAR_SPACE_1 + 36, 
									# "y":BAR_DEFAULT_Y + 24, 
									"y" : 28 + SLOT_DISTANCE*6,
									"text" : "- none -", 
									"text_horizontal_align":"left" 
								},
								#Level text
								{ 
									"name":"Zi_Rank_Level_7", 
									"type":"text", 
									"x":BAR_SPACE_1*3 + 60, 
									# "y":BAR_DEFAULT_Y + 24, 
									"y" : 28 + SLOT_DISTANCE*6,
									"text" : "- none -", 
									"text_horizontal_align":"center" 
								},
								#Time text
								{ 
									"name":"Zi_Rank_Time_7", 
									"type":"text", 
									"x":BAR_SPACE_1*6 + 10, 
									# "y":BAR_DEFAULT_Y + 24, 
									"y" : 28 + SLOT_DISTANCE*6,
									"text" : "- none -", 
									"text_horizontal_align":"center" 
								},
								#Date text
								{ 
									"name":"Zi_Rank_Date_7", 
									"type":"text", 
									"x":BAR_SPACE_1*8 + 10, 
									# "y":BAR_DEFAULT_Y + 24, 
									"y" : 28 + SLOT_DISTANCE*6,
									"text" : "- none -", 
									"text_horizontal_align":"center" 
								},
								#RANK 8
								#Rank text
								{ 
									"name":"Rank_8", 
									"type":"text", 
									"x":12 + 11,
									# "y":BAR_DEFAULT_Y + 24, 
									"y" : 28 + SLOT_DISTANCE*7,
									"text" : "8", 
									"text_horizontal_align":"left" 
								},
								#Leader text
								{ 
									"name":"Zi_Rank_Name_8", 
									"type":"text", 
									"x":BAR_SPACE_1 + 36, 
									# "y":BAR_DEFAULT_Y + 24, 
									"y" : 28 + SLOT_DISTANCE*7,
									"text" : "- none -", 
									"text_horizontal_align":"left" 
								},
								#Level text
								{ 
									"name":"Zi_Rank_Level_8", 
									"type":"text", 
									"x":BAR_SPACE_1*3 + 60, 
									# "y":BAR_DEFAULT_Y + 24, 
									"y" : 28 + SLOT_DISTANCE*7,
									"text" : "- none -", 
									"text_horizontal_align":"center" 
								},
								#Time text
								{ 
									"name":"Zi_Rank_Time_8", 
									"type":"text", 
									"x":BAR_SPACE_1*6 + 10, 
									# "y":BAR_DEFAULT_Y + 24, 
									"y" : 28 + SLOT_DISTANCE*7,
									"text" : "- none -", 
									"text_horizontal_align":"center" 
								},
								#Date text
								{ 
									"name":"Zi_Rank_Date_8", 
									"type":"text", 
									"x":BAR_SPACE_1*8 + 10, 
									# "y":BAR_DEFAULT_Y + 24, 
									"y" : 28 + SLOT_DISTANCE*7,
									"text" : "- none -", 
									"text_horizontal_align":"center" 
								},	
								#RANK 9
								#Rank text
								{ 
									"name":"Rank_9", 
									"type":"text", 
									"x":12 + 11,
									# "y":BAR_DEFAULT_Y + 24, 
									"y" : 28 + SLOT_DISTANCE*8,
									"text" : "9", 
									"text_horizontal_align":"left" 
								},
								#Leader text
								{ 
									"name":"Zi_Rank_Name_9", 
									"type":"text", 
									"x":BAR_SPACE_1 + 36, 
									# "y":BAR_DEFAULT_Y + 24, 
									"y" : 28 + SLOT_DISTANCE*8,
									"text" : "- none -", 
									"text_horizontal_align":"left" 
								},
								#Level text
								{ 
									"name":"Zi_Rank_Level_9", 
									"type":"text", 
									"x":BAR_SPACE_1*3 + 60, 
									# "y":BAR_DEFAULT_Y + 24, 
									"y" : 28 + SLOT_DISTANCE*8,
									"text" : "- none -", 
									"text_horizontal_align":"center" 
								},
								#Time text
								{ 
									"name":"Zi_Rank_Time_9", 
									"type":"text", 
									"x":BAR_SPACE_1*6 + 10, 
									# "y":BAR_DEFAULT_Y + 24, 
									"y" : 28 + SLOT_DISTANCE*8,
									"text" : "- none -", 
									"text_horizontal_align":"center" 
								},
								#Date text
								{ 
									"name":"Zi_Rank_Date_9", 
									"type":"text", 
									"x":BAR_SPACE_1*8 + 10, 
									# "y":BAR_DEFAULT_Y + 24, 
									"y" : 28 + SLOT_DISTANCE*8,
									"text" : "- none -", 
									"text_horizontal_align":"center" 
								},	
								#RANK 10
								#Rank text
								{ 
									"name":"Rank_10", 
									"type":"text", 
									"x":12 + 11,
									# "y":BAR_DEFAULT_Y + 24, 
									"y" : 28 + SLOT_DISTANCE*9,
									"text" : "10", 
									"text_horizontal_align":"left" 
								},
								#Leader text
								{ 
									"name":"Zi_Rank_Name_10", 
									"type":"text", 
									"x":BAR_SPACE_1 + 36, 
									# "y":BAR_DEFAULT_Y + 24, 
									"y" : 28 + SLOT_DISTANCE*9,
									"text" : "- none -", 
									"text_horizontal_align":"left" 
								},
								#Level text
								{ 
									"name":"Zi_Rank_Level_10", 
									"type":"text", 
									"x":BAR_SPACE_1*3 + 60, 
									# "y":BAR_DEFAULT_Y + 24, 
									"y" : 28 + SLOT_DISTANCE*9,
									"text" : "- none -", 
									"text_horizontal_align":"center" 
								},
								#Time text
								{ 
									"name":"Zi_Rank_Time_10", 
									"type":"text", 
									"x":BAR_SPACE_1*6 + 10, 
									# "y":BAR_DEFAULT_Y + 24, 
									"y" : 28 + SLOT_DISTANCE*9,
									"text" : "- none -", 
									"text_horizontal_align":"center" 
								},
								#Date text
								{ 
									"name":"Zi_Rank_Date_10",
									"type":"text", 
									"x":BAR_SPACE_1*8 + 10, 
									# "y":BAR_DEFAULT_Y + 24, 
									"y" : 28 + SLOT_DISTANCE*9,
									"text" : "- none -", 
									"text_horizontal_align":"center" 
								},	
							),
						},

					),
				},
			),
		},
	),
}

