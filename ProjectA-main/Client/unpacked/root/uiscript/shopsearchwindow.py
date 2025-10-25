import ui
import uiScriptLocale
import uiShopSearch
import grp

ROOT = "d:/ymir work/ui/game/shopsearch/"

BOARD_WIDTH = 611
BOARD_HEIGHT = 682

CAT_SPACE = 3

window = {
	"name" : "AuctionWindow",
	"style" : ("movable", "float",),

	"x" : 0,
	"y" : 0,

	"width" : BOARD_WIDTH,
	"height" : BOARD_HEIGHT,

	"children" :
	(
		{
			"name" : "board",
			"type" : "image",
			"style" : ("attach",),

			"x" : 0,
			"y" : 0,

			"image" : ROOT + "bg_full.tga",

			"title" : uiScriptLocale.AUCTION_WINDOW_TITLE,

			"children" :
			(
				{
					"name" : "titlebar",
					"type" : "titlebar",

					"x" : 7,
					"y" : 6,

					"width" : BOARD_WIDTH - 7 - 5,

					"children" :
					(
						{
							"name" : "title",
							"type" : "text",

							"x" : 0,
							"y" : 0,

							"all_align" : 1,

							"text" : uiScriptLocale.AUCTION_WINDOW_TITLE,
						},
					),
				},
				{
					"name" : "search_window",
					"style" : ("not_pick",),

					"x" : 21,
					"y" : 47,

					"width" : 193,
					"height" : 613,

					"children" :
					(
						{
							"name" : "premium_info_icon",
							"type" : "image",

							"x" : 32 - 21,
							"y" : 5,

							#"vertical_align" : "bottom",

							"image" : "d:/ymir work/ui/info.tga",

							"children" :
							(
								{
									"name" : "premium_info",
									"type" : "text",

									"x" : 20 + 7,
									"y" : 0,

									"vertical_align" : "center",
									"text_vertical_align" : "center",

									"text" : "Premium aktiv",
								},
							),
						},
						# search
						{
							"name" : "search_text_edit_text",
							"type" : "editline",

							"x" : 32 - 21 + 4,
							"y" : 78 - 47 + 4,

							"width" : 159 - 4 * 2,
							"height" : 24 - 4 * 2,

							"input_limit" : 40,
							"overlay" : uiScriptLocale.AUCTION_SEARCH_EDIT_OVERLAY_TEXT,

							"children" :
							(
								{
									"name" : "search_text_edit_text_hint",
									"type" : "text",

									"x" : 0,
									"y" : 0,

									"color" : grp.GenerateColor(1.0, 1.0, 1.0, 0.5),
								},
							),
						},
						{
							"name" : "search_text_button",
							"type" : "button",

							"x" : 167 - 21,
							"y" : 80 - 47,

							"default_image" : ROOT + "button_search_normal.tga",
							"over_image" : ROOT + "button_search_hover.tga",
							"down_image" : ROOT + "button_search_down.tga",
							"disable_image" : ROOT + "button_search_down.tga",
						},

						{
							"name" : "strict_search_checkbox",
							"type" : "checkbox",

							"x" : 35 - 15,
							"y" : 165 - 47 - 57,

							"checked" : False,

							"text" : uiScriptLocale.AUCTION_STRICT_SEARCH,
						},

						# {
						# 	"name" : "search_sort_desc",
						# 	"type" : "text",

						# 	"x" : 35 - 21,
						# 	"y" : 113 - 47,

						# 	"text" : uiScriptLocale.SHOP_SEARCH_SORT_DESC,
						# },
						# {
						# "name" : "sort_info_icon",
						# 	"type" : "image",

						# 	"x" : 35 - 21,
						# 	"y" : 133 - 47,

						# 	#"vertical_align" : "bottom",

						# 	"image" : "d:/ymir work/ui/info.tga",
						# },
						# {
						# 	"name" : "search_sort_dropdown",
						# 	"type" : "combobox",

						# 	"x" : 35 - 21,
						# 	"y" : 133 - 47,

						# 	"width" : 157,
						# 	"height" : 18,

						# 	"text_align" : "left",
						# 	"text_pos" : 16,

						# 	"items" : (
						# 		(0, uiScriptLocale.SHOP_SEARCH_SORT_ALPHA_AZ),
						# 		(1, uiScriptLocale.SHOP_SEARCH_SORT_ALPHA_ZA),
						# 		(2, uiScriptLocale.SHOP_SEARCH_SORT_PRICE_ASC),
						# 		(3, uiScriptLocale.SHOP_SEARCH_SORT_PRICE_DESC),
						# 	),

						# 	"select_item" : 0,

						# 	"children" :
						# 	(
						# 		{
						# 			"name" : "search_sort_dropdown_arrow",
						# 			"type" : "image",
						# 			"style" : ("not_pick",),

						# 			"x" : 4,
						# 			"y" : (18 - 4) / 2 + 1,

						# 			"image" : ROOT + "arrow_down.tga",
						# 		},
						# 	),
						# },
						{
							"name" : "search_cat_desc",
							"type" : "text",

							"x" : 35 - 21,
							"y" : 165 - 47,

							"text" : uiScriptLocale.SHOP_SEARCH_CAT_DESC,
						},
						{
							"name" : "search_cat_btn_all",
							"type" : "state_button",

							"x" : 33 - 21,
							"y" : 185 - 47 + (23 + CAT_SPACE) * 0,

							"default_image_1" : ROOT + "category_inactive_normal.tga",
							"over_image_1" : ROOT + "category_inactive_hover.tga",
							"down_image_1" : ROOT + "category_inactive_down.tga",
							"default_image_2" : ROOT + "category_active.tga",
							"over_image_2" : ROOT + "category_active.tga",
							"down_image_2" : ROOT + "category_active.tga",

							"children" :
							(
								{
									"name" : "search_cat_btn_all_icon",
									"type" : "image",
									"style" : ("not_pick",),

									"x" : 4,
									"y" : 4,

									"image" : ROOT + "category_icon_all.tga",
								},
								{
									"name" : "search_cat_btn_all_text",
									"type" : "text",

									"x" : 30,
									"y" : 11,

									"text_vertical_align" : "center",

									"text" : uiScriptLocale.SHOP_SEARCH_CAT_ALL,
								},
							),
						},
						{
							"name" : "search_cat_btn_weapon",
							"type" : "state_button",

							"x" : 33 - 21,
							"y" : 185 - 47 + (23 + CAT_SPACE) * 1,

							"default_image_1" : ROOT + "category_inactive_normal.tga",
							"over_image_1" : ROOT + "category_inactive_hover.tga",
							"down_image_1" : ROOT + "category_inactive_down.tga",
							"default_image_2" : ROOT + "category_active.tga",
							"over_image_2" : ROOT + "category_active.tga",
							"down_image_2" : ROOT + "category_active.tga",

							"children" :
							(
								{
									"name" : "search_cat_btn_weapon_icon",
									"type" : "image",
									"style" : ("not_pick",),

									"x" : 4,
									"y" : 4,

									"image" : ROOT + "category_icon_waffen.tga",
								},
								{
									"name" : "search_cat_btn_weapon_text",
									"type" : "text",

									"x" : 30,
									"y" : 11,

									"text_vertical_align" : "center",

									"text" : uiScriptLocale.SHOP_SEARCH_CAT_WEAPON,
								},
							),
						},
						{
							"name" : "search_cat_btn_armor",
							"type" : "state_button",

							"x" : 33 - 21,
							"y" : 185 - 47 + (23 + CAT_SPACE) * 2,

							"default_image_1" : ROOT + "category_inactive_normal.tga",
							"over_image_1" : ROOT + "category_inactive_hover.tga",
							"down_image_1" : ROOT + "category_inactive_down.tga",
							"default_image_2" : ROOT + "category_active.tga",
							"over_image_2" : ROOT + "category_active.tga",
							"down_image_2" : ROOT + "category_active.tga",

							"children" :
							(
								{
									"name" : "search_cat_btn_armor_icon",
									"type" : "image",
									"style" : ("not_pick",),

									"x" : 4,
									"y" : 4,

									"image" : ROOT + "category_icon_ruestung.tga",
								},
								{
									"name" : "search_cat_btn_armor_text",
									"type" : "text",

									"x" : 30,
									"y" : 11,

									"text_vertical_align" : "center",

									"text" : uiScriptLocale.SHOP_SEARCH_CAT_ARMOR,
								},
							),
						},
						{
							"name" : "search_cat_btn_jewellery",
							"type" : "state_button",

							"x" : 33 - 21,
							"y" : 185 - 47 + (23 + CAT_SPACE) * 3,

							"default_image_1" : ROOT + "category_inactive_normal.tga",
							"over_image_1" : ROOT + "category_inactive_hover.tga",
							"down_image_1" : ROOT + "category_inactive_down.tga",
							"default_image_2" : ROOT + "category_active.tga",
							"over_image_2" : ROOT + "category_active.tga",
							"down_image_2" : ROOT + "category_active.tga",

							"children" :
							(
								{
									"name" : "search_cat_btn_jewellery_icon",
									"type" : "image",
									"style" : ("not_pick",),

									"x" : 4,
									"y" : 4,

									"image" : ROOT + "category_icon_schmuck.tga",
								},
								{
									"name" : "search_cat_btn_jewellery_text",
									"type" : "text",

									"x" : 30,
									"y" : 11,

									"text_vertical_align" : "center",

									"text" : uiScriptLocale.SHOP_SEARCH_CAT_JEWELLERY,
								},
							),
						},
						{
							"name" : "search_cat_btn_talisman",
							"type" : "state_button",

							"x" : 33 - 21,
							"y" : 185 - 47 + (23 + CAT_SPACE) * 4,

							"default_image_1" : ROOT + "category_inactive_normal.tga",
							"over_image_1" : ROOT + "category_inactive_hover.tga",
							"down_image_1" : ROOT + "category_inactive_down.tga",
							"default_image_2" : ROOT + "category_active.tga",
							"over_image_2" : ROOT + "category_active.tga",
							"down_image_2" : ROOT + "category_active.tga",

							"children" :
							(
								{
									"name" : "search_cat_btn_talisman_icon",
									"type" : "image",
									"style" : ("not_pick",),

									"x" : 4,
									"y" : 4,

									"image" : ROOT + "category_icon_talismane.tga",
								},
								{
									"name" : "search_cat_btn_talisman_text",
									"type" : "text",

									"x" : 30,
									"y" : 11,

									"text_vertical_align" : "center",

									"text" : uiScriptLocale.SHOP_SEARCH_CAT_TALISMAN,
								},
							),
						},
						{
							"name" : "search_cat_btn_dragonsoul",
							"type" : "state_button",

							"x" : 33 - 21,
							"y" : 185 - 47 + (23 + CAT_SPACE) * 5,

							"default_image_1" : ROOT + "category_inactive_normal.tga",
							"over_image_1" : ROOT + "category_inactive_hover.tga",
							"down_image_1" : ROOT + "category_inactive_down.tga",
							"default_image_2" : ROOT + "category_active.tga",
							"over_image_2" : ROOT + "category_active.tga",
							"down_image_2" : ROOT + "category_active.tga",

							"children" :
							(
								{
									"name" : "search_cat_btn_dragonsoul_icon",
									"type" : "image",
									"style" : ("not_pick",),

									"x" : 4,
									"y" : 4,

									"image" : ROOT + "category_icon_drachenst.tga",
								},
								{
									"name" : "search_cat_btn_dragonsoul_text",
									"type" : "text",

									"x" : 30,
									"y" : 11,

									"text_vertical_align" : "center",

									"text" : uiScriptLocale.SHOP_SEARCH_CAT_DRAGONSOUL,
								},
							),
						},
						{
							"name" : "search_cat_btn_costume",
							"type" : "state_button",

							"x" : 33 - 21,
							"y" : 185 - 47 + (23 + CAT_SPACE) * 6,

							"default_image_1" : ROOT + "category_inactive_normal.tga",
							"over_image_1" : ROOT + "category_inactive_hover.tga",
							"down_image_1" : ROOT + "category_inactive_down.tga",
							"default_image_2" : ROOT + "category_active.tga",
							"over_image_2" : ROOT + "category_active.tga",
							"down_image_2" : ROOT + "category_active.tga",

							"children" :
							(
								{
									"name" : "search_cat_btn_costume_icon",
									"type" : "image",
									"style" : ("not_pick",),

									"x" : 4,
									"y" : 4,

									"image" : ROOT + "category_icon_kostuem.tga",
								},
								{
									"name" : "search_cat_btn_costume_text",
									"type" : "text",

									"x" : 30,
									"y" : 11,

									"text_vertical_align" : "center",

									"text" : uiScriptLocale.SHOP_SEARCH_CAT_COSTUME,
								},
							),
						},
						{
							"name" : "search_cat_btn_costume_boni",
							"type" : "state_button",

							"x" : 33 - 21,
							"y" : 185 - 47 + (23 + CAT_SPACE) * 7,

							"default_image_1" : ROOT + "category_inactive_normal.tga",
							"over_image_1" : ROOT + "category_inactive_hover.tga",
							"down_image_1" : ROOT + "category_inactive_down.tga",
							"default_image_2" : ROOT + "category_active.tga",
							"over_image_2" : ROOT + "category_active.tga",
							"down_image_2" : ROOT + "category_active.tga",

							"children" :
							(
								{
									"name" : "search_cat_btn_costume_boni_icon",
									"type" : "image",
									"style" : ("not_pick",),

									"x" : 4,
									"y" : 4,

									"image" : ROOT + "category_icon_kostuembonus.tga",
								},
								{
									"name" : "search_cat_btn_costume_boni_text",
									"type" : "text",

									"x" : 30,
									"y" : 11,

									"text_vertical_align" : "center",

									"text" : uiScriptLocale.SHOP_SEARCH_CAT_COSTUME_BONI,
								},
							),
						},
						{
							"name" : "search_cat_btn_skills",
							"type" : "state_button",

							"x" : 33 - 21,
							"y" : 185 - 47 + (23 + CAT_SPACE) * 8,

							"default_image_1" : ROOT + "category_inactive_normal.tga",
							"over_image_1" : ROOT + "category_inactive_hover.tga",
							"down_image_1" : ROOT + "category_inactive_down.tga",
							"default_image_2" : ROOT + "category_active.tga",
							"over_image_2" : ROOT + "category_active.tga",
							"down_image_2" : ROOT + "category_active.tga",

							"children" :
							(
								{
									"name" : "search_cat_btn_skills_icon",
									"type" : "image",
									"style" : ("not_pick",),

									"x" : 4,
									"y" : 4,

									"image" : ROOT + "category_icon_fertigkeiten.tga",
								},
								{
									"name" : "search_cat_btn_skills_text",
									"type" : "text",

									"x" : 30,
									"y" : 11,

									"text_vertical_align" : "center",

									"text" : uiScriptLocale.SHOP_SEARCH_CAT_SKILLS,
								},
							),
						},
						{
							"name" : "search_cat_btn_potions",
							"type" : "state_button",

							"x" : 33 - 21,
							"y" : 185 - 47 + (23 + CAT_SPACE) * 9,

							"default_image_1" : ROOT + "category_inactive_normal.tga",
							"over_image_1" : ROOT + "category_inactive_hover.tga",
							"down_image_1" : ROOT + "category_inactive_down.tga",
							"default_image_2" : ROOT + "category_active.tga",
							"over_image_2" : ROOT + "category_active.tga",
							"down_image_2" : ROOT + "category_active.tga",

							"children" :
							(
								{
									"name" : "search_cat_btn_potions_icon",
									"type" : "image",
									"style" : ("not_pick",),

									"x" : 4,
									"y" : 4,

									"image" : ROOT + "category_icon_traenke.tga",
								},
								{
									"name" : "search_cat_btn_potions_text",
									"type" : "text",

									"x" : 30,
									"y" : 11,

									"text_vertical_align" : "center",

									"text" : uiScriptLocale.SHOP_SEARCH_CAT_POTIONS,
								},
							),
						},
						{
							"name" : "search_cat_btn_usable",
							"type" : "state_button",

							"x" : 33 - 21,
							"y" : 185 - 47 + (23 + CAT_SPACE) * 10,

							"default_image_1" : ROOT + "category_inactive_normal.tga",
							"over_image_1" : ROOT + "category_inactive_hover.tga",
							"down_image_1" : ROOT + "category_inactive_down.tga",
							"default_image_2" : ROOT + "category_active.tga",
							"over_image_2" : ROOT + "category_active.tga",
							"down_image_2" : ROOT + "category_active.tga",

							"children" :
							(
								{
									"name" : "search_cat_btn_usable_icon",
									"type" : "image",
									"style" : ("not_pick",),

									"x" : 4,
									"y" : 4,

									"image" : ROOT + "category_icon_verbrauchs.tga",
								},
								{
									"name" : "search_cat_btn_usable_text",
									"type" : "text",

									"x" : 30,
									"y" : 11,

									"text_vertical_align" : "center",

									"text" : uiScriptLocale.SHOP_SEARCH_CAT_USABLE,
								},
							),
						},
						{
							"name" : "search_cat_btn_fishs",
							"type" : "state_button",

							"x" : 33 - 21,
							"y" : 185 - 47 + (23 + CAT_SPACE) * 11,

							"default_image_1" : ROOT + "category_inactive_normal.tga",
							"over_image_1" : ROOT + "category_inactive_hover.tga",
							"down_image_1" : ROOT + "category_inactive_down.tga",
							"default_image_2" : ROOT + "category_active.tga",
							"over_image_2" : ROOT + "category_active.tga",
							"down_image_2" : ROOT + "category_active.tga",

							"children" :
							(
								{
									"name" : "search_cat_btn_fishs_icon",
									"type" : "image",
									"style" : ("not_pick",),

									"x" : 4,
									"y" : 4,

									"image" : ROOT + "category_icon_fische.tga",
								},
								{
									"name" : "search_cat_btn_fishs_text",
									"type" : "text",

									"x" : 30,
									"y" : 11,

									"text_vertical_align" : "center",

									"text" : uiScriptLocale.SHOP_SEARCH_CAT_FISHS,
								},
							),
						},
						{
							"name" : "search_cat_btn_mounts",
							"type" : "state_button",

							"x" : 33 - 21,
							"y" : 185 - 47 + (23 + CAT_SPACE) * 12,

							"default_image_1" : ROOT + "category_inactive_normal.tga",
							"over_image_1" : ROOT + "category_inactive_hover.tga",
							"down_image_1" : ROOT + "category_inactive_down.tga",
							"default_image_2" : ROOT + "category_active.tga",
							"over_image_2" : ROOT + "category_active.tga",
							"down_image_2" : ROOT + "category_active.tga",

							"children" :
							(
								{
									"name" : "search_cat_btn_mounts_icon",
									"type" : "image",
									"style" : ("not_pick",),

									"x" : 4,
									"y" : 4,

									"image" : ROOT + "category_icon_reittiere.tga",
								},
								{
									"name" : "search_cat_btn_mounts_text",
									"type" : "text",

									"x" : 30,
									"y" : 11,

									"text_vertical_align" : "center",

									"text" : uiScriptLocale.SHOP_SEARCH_CAT_MOUNTS,
								},
							),
						},
						{
							"name" : "search_cat_btn_pets",
							"type" : "state_button",

							"x" : 33 - 21,
							"y" : 185 - 47 + (23 + CAT_SPACE) * 11,

							"default_image_1" : ROOT + "category_inactive_normal.tga",
							"over_image_1" : ROOT + "category_inactive_hover.tga",
							"down_image_1" : ROOT + "category_inactive_down.tga",
							"default_image_2" : ROOT + "category_active.tga",
							"over_image_2" : ROOT + "category_active.tga",
							"down_image_2" : ROOT + "category_active.tga",

							"children" :
							(
								{
									"name" : "search_cat_btn_pets_icon",
									"type" : "image",
									"style" : ("not_pick",),

									"x" : 4,
									"y" : 4,

									"image" : ROOT + "category_icon_begleiter.tga",
								},
								{
									"name" : "search_cat_btn_pets_text",
									"type" : "text",

									"x" : 30,
									"y" : 11,

									"text_vertical_align" : "center",

									"text" : uiScriptLocale.SHOP_SEARCH_CAT_PETS,
								},
							),
						},
						{
							"name" : "search_cat_btn_owned",
							"type" : "state_button",

							"x" : 33 - 21,
							"y" : 185 - 47 + (23 + CAT_SPACE) * 14,

							"default_image_1" : ROOT + "category_inactive_normal.tga",
							"over_image_1" : ROOT + "category_inactive_hover.tga",
							"down_image_1" : ROOT + "category_inactive_down.tga",
							"default_image_2" : ROOT + "category_active.tga",
							"over_image_2" : ROOT + "category_active.tga",
							"down_image_2" : ROOT + "category_active.tga",

							"children" :
							(
								{
									"name" : "search_cat_btn_owned_icon",
									"type" : "image",
									"style" : ("not_pick",),

									"x" : 4,
									"y" : 4,

									"image" : ROOT + "category_icon_meineitems.tga",
								},
								{
									"name" : "search_cat_btn_owned_text",
									"type" : "text",

									"x" : 30,
									"y" : 11,

									"text_vertical_align" : "center",

									"text" : uiScriptLocale.SHOP_SEARCH_CAT_OWNED,
								},
							),
						},
					),
				},
				{
					"name" : "item_window",
					"style" : ("not_pick",),

					"x" : 224,
					"y" : 47,

					"width" : 375,
					"height" : 613,

					"children" :
					(
						{
							"name" : "item_list",
							"type" : "listboxex",

							"x" : 5,
							"y" : 5,

							"width" : 375 - (9 + 2) - 5 * 2,
							"height" : uiShopSearch.ShopSearchWindow.Item.ITEM_HEIGHT * 14,
							"viewcount" : 14,

							"itemsize_x" : 0,
							"itemsize_y" : uiShopSearch.ShopSearchWindow.Item.ITEM_HEIGHT,

							"itemstep" : uiShopSearch.ShopSearchWindow.Item.ITEM_HEIGHT,
						},
						{
							"name" : "item_scrollbar",
							"type" : "scrollbar_template",

							"x" : 9 + 2,
							"y" : 5,

							"horizontal_align" : "right",

							"bg_top_image" : ROOT + "scroll_top.tga",
							"bg_center_image" : ROOT + "scroll_center.tga",
							"bg_bottom_image" : ROOT + "scroll_bottom.tga",
							"middle_image" : ROOT + "scrollbar.tga",

							"size" : uiShopSearch.ShopSearchWindow.Item.ITEM_HEIGHT * 14,
						},
						{
							"name" : "item_loading",
							"type" : "ani_image",

							"x" : (375 - 16) / 2,
							"y" : (613 - 16) / 2,

							"delay" : 6,

							"images" : (
								"d:/ymir work/ui/loading_ani/00.tga",
								"d:/ymir work/ui/loading_ani/01.tga",
								"d:/ymir work/ui/loading_ani/02.tga",
								"d:/ymir work/ui/loading_ani/03.tga",
								"d:/ymir work/ui/loading_ani/04.tga",
								"d:/ymir work/ui/loading_ani/05.tga",
								"d:/ymir work/ui/loading_ani/06.tga",
								"d:/ymir work/ui/loading_ani/07.tga",
							),
						},
					),
				},
			),
		},
	),
}

import constInfo
if constInfo.ENABLE_RACE_CATEGORY:
	window["children"][0]["children"] += (
		{
			"name" : "CategoryButton0",
			"type" : "toggle_button",

			"x" : 30,
			"y" : 120,

			"text" : "",

			"default_image" : ROOT + "warrior_grey.tga",
			"over_image" : ROOT + "warrior_color.tga",
			"down_image" : ROOT + "warrior_color.tga",
		},
		{
			"name" : "CategoryButton1",
			"type" : "toggle_button",

			"x" : 30 + 35,
			"y" : 120,

			"text" : "",

			"default_image" : ROOT + "ninja_grey.tga",
			"over_image" : ROOT + "ninja_color.tga",
			"down_image" : ROOT + "ninja_color.tga",
		},
		{
			"name" : "CategoryButton2",
			"type" : "toggle_button",

			"x" : 30 + 70,
			"y" : 120 + 2,

			"text" : "",

			"default_image" : ROOT + "sura_grey.tga",
			"over_image" : ROOT + "sura_color.tga",
			"down_image" : ROOT + "sura_color.tga",
		},
		{
			"name" : "CategoryButton3",
			"type" : "toggle_button",

			"x" : 30 + 105,
			"y" : 120,

			"text" : "",

			"default_image" : ROOT + "shaman_grey.tga",
			"over_image" : ROOT + "shaman_color.tga",
			"down_image" : ROOT + "shaman_color.tga",
		},
	)

if constInfo.NEW_SEARCH_CATEGORY:
	window["children"][0]["children"][1]["children"][18]["y"] = 185 - 47 + (23 + CAT_SPACE) * 14
	window["children"][0]["children"][1]["children"] += (
			{
				"name" : "search_cat_btn_ores",
				"type" : "state_button",

				"x" : 33 - 21,
				"y" : 185 - 47 + (23 + CAT_SPACE) * 13,

				"default_image_1" : ROOT + "category_inactive_normal.tga",
				"over_image_1" : ROOT + "category_inactive_hover.tga",
				"down_image_1" : ROOT + "category_inactive_down.tga",
				"default_image_2" : ROOT + "category_active.tga",
				"over_image_2" : ROOT + "category_active.tga",
				"down_image_2" : ROOT + "category_active.tga",

				"children" :
				(
					{
						"name" : "search_cat_btn_ores_icon",
						"type" : "image",
						"style" : ("not_pick",),

						"x" : 4,
						"y" : 4,

						"image" : ROOT + "category_icon_erze.tga",
					},
					{
						"name" : "search_cat_btn_ores_text",
						"type" : "text",

						"x" : 30,
						"y" : 11,

						"text_vertical_align" : "center",

						"text" : uiScriptLocale.SHOP_SEARCH_CAT_ORES,
					},
				),
			},
		)
