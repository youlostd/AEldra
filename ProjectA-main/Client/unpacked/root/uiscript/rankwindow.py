import uiScriptLocale

window = {
	"name" : "RankWindow",

	"x" : 100,
	"y" : 20,

	"style" : ("movable", "float",),

	"width" : 445,
	"height" : 382,

	"children" :
	(
		{
			"name" : "board",
			"type" : "board",

			"x" : 0,
			"y" : 0,

			"width" : 445,
			"height" : 382,

			"children" :
			(
				## Title
				{
					"name" : "TitleBar",
					"type" : "titlebar",
					"style" : ("attach",),

					"x" : 0,
					"y" : 0,

					"width" : 445,
					# "color" : "yellow",

					"children" :
					(
						{ 
							"name":"TitleName", 
							"type":"text", 
							"x":0, 
							"y":-1, 
							"text": uiScriptLocale.DUNGEON_RANKING_WINDOW, 
							"all_align":"center" 
						},
					),
				},
			),
		},
	),
}
