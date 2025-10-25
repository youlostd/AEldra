import uiScriptLocale

JIGSAW_ROOT = "d:/ymir work/ui/game/event_icons/"

window = {
    "name" : "JigsawIconWindow",
 
    "x" : SCREEN_WIDTH - 136 - 100,
    "y" : 15 + 30,
 
    "width" : 100,
    "height" : 58,
 
    "children" :
    (
        {
            "name" : "jigsaw_window",
            "type" : "window",
            "style" : ("attach",),

            "x" : 0,
            "y" : 0,

            "width" : 205,
            "height" : 270,
         
            "children" :
            (
                {
                    "name" : "jigsaw_button",
                    "type" : "button",
                 
                    "x" : 0,
                    "y" : 0,
                 
                    "default_image" : JIGSAW_ROOT + "fishpuzzle.tga",
                    "over_image" : JIGSAW_ROOT + "fishpuzzle.tga",
                    "down_image" : JIGSAW_ROOT + "fishpuzzle.tga",
                },
            ),
        },
    ), 
}
 