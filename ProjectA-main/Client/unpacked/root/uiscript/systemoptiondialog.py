import uiScriptLocale

ROOT_PATH = "d:/ymir work/ui/public/"

TEMPORARY_X = +13
TEXT_TEMPORARY_X = -10
BUTTON_TEMPORARY_X = 5
PVP_X = -10

window = {
	"name" : "SystemOptionDialog",
	"style" : ("movable", "float",),

	"x" : 0,
	"y" : 0,

	"width" : 284+25,
	"height" : 241,

	"children" :
	(
		{
			"name" : "board",
			"type" : "board",

			"x" : 0,
			"y" : 0,

			"width" : 284+25,
			"height" : 241,

			"children" :
			(
				## Title
				{
					"name" : "titlebar",
					"type" : "titlebar",
					"style" : ("attach",),

					"x" : 0,
					"y" : 0,

					"width" : 284+25,
					"color" : "gray",

					"children" :
					(
						{ 
						"name":"titlename", "type":"text", "x":0, "y":3, 
						"horizontal_align":"center", "text_horizontal_align":"center",
						"text": uiScriptLocale.SYSTEMOPTION_TITLE, 
						 },
					),
				},

				
				## Music
				{
					"name" : "music_name",
					"type" : "text",

					"x" : 22,
					"y" : 68,

					"text" : uiScriptLocale.OPTION_MUSIC,
				},
				
				{
					"name" : "music_volume_controller",
					"type" : "sliderbar",

					"x" : 103,
					"y" : 68,
				},
				
				{
					"name" : "bgm_button",
					"type" : "button",

					"x" : 12,
					"y" : 93,

					"text" : uiScriptLocale.OPTION_MUSIC_CHANGE,

					"default_image" : ROOT_PATH + "Middle_Button_01.sub",
					"over_image" : ROOT_PATH + "Middle_Button_02.sub",
					"down_image" : ROOT_PATH + "Middle_Button_03.sub",
				},
				
				{
					"name" : "bgm_file",
					"type" : "text",

					"x" : 92,
					"y" : 95,

					"text" : uiScriptLocale.OPTION_MUSIC_DEFAULT_THEMA,
				},
				
				## Sound
				{
					"name" : "sound_name",
					"type" : "text",

					"x" : 22,
					"y" : 43,

					"text" : uiScriptLocale.OPTION_SOUND,
				},
				
				{
					"name" : "sound_volume_controller",
					"type" : "sliderbar",

					"x" : 103,
					"y" : 43,
				},	

				## ī�޶�
				{
					"name" : "camera_mode",
					"type" : "text",

					"x" : 32 + TEXT_TEMPORARY_X,
					"y" : 128+2,

					"text" : uiScriptLocale.OPTION_CAMERA_DISTANCE,
				},
				
				{
					"name" : "camera_short",
					"type" : "radio_button",

					"x" : 102,
					"y" : 128,

					"text" : uiScriptLocale.OPTION_CAMERA_DISTANCE_SHORT,

					"default_image" : ROOT_PATH + "Middle_Button_01.sub",
					"over_image" : ROOT_PATH + "Middle_Button_02.sub",
					"down_image" : ROOT_PATH + "Middle_Button_03.sub",
				},
				
				{
					"name" : "camera_long",
					"type" : "radio_button",

					"x" : 102+70,
					"y" : 128,

					"text" : uiScriptLocale.OPTION_CAMERA_DISTANCE_LONG,

					"default_image" : ROOT_PATH + "Middle_Button_01.sub",
					"over_image" : ROOT_PATH + "Middle_Button_02.sub",
					"down_image" : ROOT_PATH + "Middle_Button_03.sub",
				},

				{
					"name" : "camera_huge",
					"type" : "radio_button",

					"x" : 102+70+70,
					"y" : 128,

					"text" : uiScriptLocale.OPTION_CAMERA_DISTANCE_HUGE,

					"default_image" : ROOT_PATH + "Middle_Button_01.sub",
					"over_image" : ROOT_PATH + "Middle_Button_02.sub",
					"down_image" : ROOT_PATH + "Middle_Button_03.sub",
				},

				## �Ȱ�
				{
					"name" : "fog_mode",
					"type" : "text",

					"x" : 22,
					"y" : 153+2,

					"text" : uiScriptLocale.OPTION_FOG,
				},
				
				{
					"name" : "fog_level0",
					"type" : "radio_button",

					"x" : 102,
					"y" : 153,

					"text" : uiScriptLocale.OPTION_FOG_DENSE,

					"default_image" : ROOT_PATH + "small_Button_01.sub",
					"over_image" : ROOT_PATH + "small_Button_02.sub",
					"down_image" : ROOT_PATH + "small_Button_03.sub",
				},
				
				{
					"name" : "fog_level1",
					"type" : "radio_button",

					"x" : 102+50,
					"y" : 153,

					"text" : uiScriptLocale.OPTION_FOG_MIDDLE,
					
					"default_image" : ROOT_PATH + "small_Button_01.sub",
					"over_image" : ROOT_PATH + "small_Button_02.sub",
					"down_image" : ROOT_PATH + "small_Button_03.sub",
				},
				
				{
					"name" : "fog_level2",
					"type" : "radio_button",

					"x" : 102 + 100,
					"y" : 153,

					"text" : uiScriptLocale.OPTION_FOG_LIGHT,
					
					"default_image" : ROOT_PATH + "small_Button_01.sub",
					"over_image" : ROOT_PATH + "small_Button_02.sub",
					"down_image" : ROOT_PATH + "small_Button_03.sub",
				},

				## Ÿ�� ����
				{
					"name" : "tiling_mode",
					"type" : "text",

					"x" : 32 + TEXT_TEMPORARY_X,
					"y" : 178+2,

					"text" : uiScriptLocale.OPTION_TILING,
				},
				
				{
					"name" : "tiling_cpu",
					"type" : "radio_button",

					"x" : 102,
					"y" : 178,

					"text" : uiScriptLocale.OPTION_TILING_CPU,

					"default_image" : ROOT_PATH + "small_Button_01.sub",
					"over_image" : ROOT_PATH + "small_Button_02.sub",
					"down_image" : ROOT_PATH + "small_Button_03.sub",
				},
				
				{
					"name" : "tiling_gpu",
					"type" : "radio_button",

					"x" : 102+50,
					"y" : 178,

					"text" : uiScriptLocale.OPTION_TILING_GPU,

					"default_image" : ROOT_PATH + "small_Button_01.sub",
					"over_image" : ROOT_PATH + "small_Button_02.sub",
					"down_image" : ROOT_PATH + "small_Button_03.sub",
				},
				
				{
					"name" : "tiling_apply",
					"type" : "button",

					"x" : 102+100,
					"y" : 178,

					"text" : uiScriptLocale.OPTION_TILING_APPLY,

					"default_image" : ROOT_PATH + "middle_Button_01.sub",
					"over_image" : ROOT_PATH + "middle_Button_02.sub",
					"down_image" : ROOT_PATH + "middle_Button_03.sub",
				},

				{
					"name" : "font_mode",
					"type" : "text",

					"x" : 32 + TEXT_TEMPORARY_X,
					"y" : 203 + 2, # + 24 / 2,

					"text" : uiScriptLocale.FONT,
				},
				
				{
					"name" : "font_default",
					"type" : "radio_button",

					"x" : 102,
					"y" : 203,

					"text" : uiScriptLocale.FONT_DEFAULT,

					"default_image" : ROOT_PATH + "Middle_Button_01.sub",
					"over_image" : ROOT_PATH + "Middle_Button_02.sub",
					"down_image" : ROOT_PATH + "Middle_Button_03.sub",
				},

				{
					"name" : "font_new",
					"type" : "radio_button",

					"x" : 102 + 70,
					"y" : 203,

					"text" : "1",

					"default_image" : ROOT_PATH + "Middle_Button_01.sub",
					"over_image" : ROOT_PATH + "Middle_Button_02.sub",
					"down_image" : ROOT_PATH + "Middle_Button_03.sub",
				},

				{
					"name" : "font_new_2",
					"type" : "radio_button",

					"x" : 102 + 70 + 70,
					"y" : 203,

					"text" : "2",

					"default_image" : ROOT_PATH + "Middle_Button_01.sub",
					"over_image" : ROOT_PATH + "Middle_Button_02.sub",
					"down_image" : ROOT_PATH + "Middle_Button_03.sub",
				},


				## �׸���
#				{
#					"name" : "shadow_mode",
#					"type" : "text",

#					"x" : 30,
#					"y" : 210,

#					"text" : uiScriptLocale.OPTION_SHADOW,
#				},
				
#				{
#					"name" : "shadow_bar",
#					"type" : "sliderbar",

#					"x" : 110,
#					"y" : 210,
#				},
			),
		},
	),
}
