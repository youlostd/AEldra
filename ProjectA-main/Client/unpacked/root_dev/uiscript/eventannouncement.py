import localeInfo

BASE_PATH 	= "d:/ymir work/ui/game/announcement/"
SIZE 		= ( 184, 54 )

window = {

	"name" : "EventAnnouncementWindow",

	"x" : SCREEN_WIDTH - 180 - SIZE[ 0 ],
	"y" : 38,

	"width" : SIZE[ 0 ],
	"height" : SIZE[ 1 ],

	"children" :
	(
		{
			"name" : "background",
			"type" : "image",
			"style" : ("attach",),

			"x" : 0,
			"y" : 0,

			"image" :  BASE_PATH + "announce_battlepass.tga",

			"children" :
			(
				## OPEN THREAD BUTTON
				{
					"name" : "open_thread_btn",
					"type" : "button",

					"x" : 34,
					"y" : 18,

					"horizontal_align" : "right",

					"tooltip_text" : localeInfo.CHAT_INFORMATION,

					"default_image" : BASE_PATH + "a_info_normal.tga",
					"over_image" : BASE_PATH + "a_info_hover.tga",
					"down_image" : BASE_PATH + "a_info_down.tga",
				},

				## TIME LEFT TEXT
				{
					"name" : "time_left_text",
					"type" : "text",

					"x" : 32,
					"y" : 35,

					"horizontal_align" : "left",
					"text_horizontal_align" : "left",

					"text" : "99:99:99",
				},
			),
		},
	),
}