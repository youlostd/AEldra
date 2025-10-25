#include <string>
#include <map>
#include <set>
#include <algorithm>

#include "lzo.h"

#pragma comment(lib, "lzo.lib")
#pragma comment(lib, "libprotobuf.lib")

#define MAKEFOURCC(ch0, ch1, ch2, ch3)                              \
                ((DWORD)(BYTE)(ch0) | ((DWORD)(BYTE)(ch1) << 8) |   \
                ((DWORD)(BYTE)(ch2) << 16) | ((DWORD)(BYTE)(ch3) << 24 ))

typedef unsigned char BYTE;
typedef unsigned short WORD;
typedef unsigned long DWORD;
typedef int INT;

using namespace std;

#define __ADDON_TYPE__


#define LOWER(c)	(((c)>='A'  && (c) <= 'Z') ? ((c)+('a'-'A')) : (c))
size_t str_lower(const char * src, char * dest, size_t dest_size)
{
	size_t len = 0;

	if (!dest || dest_size == 0)
		return len;

	if (!src)
	{
		*dest = '\0';
		return len;
	}

	--dest_size;

	while (*src && len < dest_size)
	{
		*dest = LOWER(*src);

		++src;
		++dest;
		++len;
	}

	*dest = '\0';
	return len;
}

const char* strlower(const char* string)
{
	static char s_szLowerString[1024 + 1];
	str_lower(string, s_szLowerString, sizeof(s_szLowerString));
	return s_szLowerString;
}

enum ELanguages
{
	LANGUAGE_ENGLISH,
	LANGUAGE_GERMAN,
	LANGUAGE_TURKISH,
	LANGUAGE_ROMANIA,
	LANGUAGE_POLISH,
	LANGUAGE_ITALIAN,
	LANGUAGE_SPANISH,
	LANGUAGE_HUNGARIAN,
	LANGUAGE_CZECH,
	LANGUAGE_PORTUGUESE,
	LANGUAGE_FRENCH,
	LANGUAGE_ARABIC,
	LANGUAGE_GREEK,
	LANGUAGE_MAX_NUM,

	LANGUAGE_DEFAULT = LANGUAGE_GERMAN,
};

std::string astLocaleStringNames[LANGUAGE_MAX_NUM];
enum EMisc
{
	CHARACTER_NAME_MAX_LEN	= 35,
	MOB_SKILL_MAX_NUM		= 5,
};

enum EMobEnchants
{
	MOB_ENCHANT_CURSE,
	MOB_ENCHANT_SLOW,
	MOB_ENCHANT_POISON,
	MOB_ENCHANT_STUN,
	MOB_ENCHANT_CRITICAL,
	MOB_ENCHANT_PENETRATE,
	MOB_ENCHANT_IGNORE_BLOCK,
	MOB_ENCHANTS_MAX_NUM
};

enum EMobResists
{
	MOB_RESIST_SWORD,
	MOB_RESIST_TWOHAND,
	MOB_RESIST_DAGGER,
	MOB_RESIST_BELL,
	MOB_RESIST_FAN,
	MOB_RESIST_BOW,
	MOB_RESIST_CLAW,
	MOB_RESIST_FIRE,
	MOB_RESIST_ELECT,
	MOB_RESIST_MAGIC,
	MOB_RESIST_WIND,
	MOB_RESIST_POISON,
	MOB_RESIST_BLEEDING,
	MOB_RESIST_EARTH,
	MOB_RESIST_ICE,
	MOB_RESIST_DARK,
	MOB_RESISTS_MAX_NUM
};

enum EItemMisc
{
	ITEM_NAME_MAX_LEN = 100,
	ITEM_VALUES_MAX_NUM = 6,
	ITEM_SMALL_DESCR_MAX_LEN = 256,
	ITEM_LIMIT_MAX_NUM = 2,
	ITEM_APPLY_MAX_NUM = 4,
	ITEM_SOCKET_MAX_NUM = 3,
	ITEM_MAX_COUNT = 200,
	ITEM_ATTRIBUTE_MAX_NUM = 7,
	ITEM_ATTRIBUTE_MAX_LEVEL = 5,
	ITEM_AWARD_WHY_MAX_LEN = 50,
	ITEM_STRING_DATA_MAX_LEN = 50,

	REFINE_MATERIAL_MAX_NUM = 5,

	ITEM_ELK_VNUM = 50026,

#ifdef __ACCE_COSTUME__
	ITEM_MAX_ACCEDRAIN = 25,
	ITEM_MIN_ACCEDRAIN = 20,
#endif
};

//typedef struct TItemTable;

#include <google/protobuf/message.h>

#include "..\..\..\Source\Server\db\src\CsvReader.h"
#include "..\..\..\Source\Server\db\src\ProtoReader.h"
#include "..\..\..\Source\Server\db\src\protobuf_data.h"

network::TRepeatedMobTable m_MobData;
network::TRepeatedItemTable m_ItemData;

#ifndef __DUMP_PROTO__
#define __DUMP_PROTO__
#endif
#ifdef __DUMP_PROTO__

bool Set_Mob_Proto_Table(network::TMobTable *mobTable, cCsvTable &csvTable, std::map<int,const char*> *nameMap)
{
	int col = 0;

	mobTable->set_vnum(atoi(csvTable.AsStringByIndex(col++)));
	mobTable->set_name(csvTable.AsStringByIndex(col++));

	map<int, const char*>::iterator it;
	for (int i = 0; i < LANGUAGE_MAX_NUM; ++i)
	{
		it = nameMap[i].find(mobTable->vnum());
		if (it != nameMap[i].end()) {
			mobTable->add_locale_name(it->second);
		}
		else {
			mobTable->add_locale_name();
		}
	}
	//4. RANK
	mobTable->set_rank(get_Mob_Rank_Value(csvTable.AsStringByIndex(col++)));
	//5. TYPE
	mobTable->set_type(get_Mob_Type_Value(csvTable.AsStringByIndex(col++)));
	//6. BATTLE_TYPE
	mobTable->set_battle_type(get_Mob_BattleType_Value(csvTable.AsStringByIndex(col++)));

	mobTable->set_level(atoi(csvTable.AsStringByIndex(col++)));
	//8. SIZE
	mobTable->set_size(get_Mob_Size_Value(csvTable.AsStringByIndex(col++)));
	//8. SCALING_SIZE
	mobTable->set_scaling_size(atof(csvTable.AsStringByIndex(col++)));
	//9. AI_FLAG
	mobTable->set_ai_flag(get_Mob_AIFlag_Value(csvTable.AsStringByIndex(col++)));
	col++; //mount_capacity;
	//10. RACE_FLAG
	mobTable->set_race_flag(get_Mob_RaceFlag_Value(csvTable.AsStringByIndex(col++)));
	//11. IMMUNE_FLAG
	mobTable->set_immune_flag(get_Mob_ImmuneFlag_Value(csvTable.AsStringByIndex(col++)));

	mobTable->set_empire(atoi(csvTable.AsStringByIndex(col++)));

	//folder
	mobTable->set_folder(csvTable.AsStringByIndex(col++));

	mobTable->set_on_click_type(atoi(csvTable.AsStringByIndex(col++)));

	mobTable->set_str(atoi(csvTable.AsStringByIndex(col++)));
	mobTable->set_dex(atoi(csvTable.AsStringByIndex(col++)));
	mobTable->set_con(atoi(csvTable.AsStringByIndex(col++)));
	mobTable->set_int_(atoi(csvTable.AsStringByIndex(col++)));
	mobTable->set_damage_min(atoi(csvTable.AsStringByIndex(col++)));
	mobTable->set_damage_max(atoi(csvTable.AsStringByIndex(col++)));
	mobTable->set_max_hp(atoi(csvTable.AsStringByIndex(col++)));
	mobTable->set_regen_cycle(atoi(csvTable.AsStringByIndex(col++)));
	mobTable->set_regen_percent(atoi(csvTable.AsStringByIndex(col++)));

	mobTable->set_gold_min(atoi(csvTable.AsStringByIndex(col++)));
	mobTable->set_gold_max(atoi(csvTable.AsStringByIndex(col++)));
	mobTable->set_exp(atoi(csvTable.AsStringByIndex(col++)));
	mobTable->set_def(atoi(csvTable.AsStringByIndex(col++)));
	mobTable->set_attack_speed(atoi(csvTable.AsStringByIndex(col++)));
	mobTable->set_moving_speed(atoi(csvTable.AsStringByIndex(col++)));
	mobTable->set_aggressive_hp_pct(atoi(csvTable.AsStringByIndex(col++)));
	mobTable->set_aggressive_sight(atoi(csvTable.AsStringByIndex(col++)));
	mobTable->set_attack_range(atoi(csvTable.AsStringByIndex(col++)));

	mobTable->set_drop_item_vnum(atoi(csvTable.AsStringByIndex(col++)));
	col++;	//resurrectionVnum


	for (int i = 0; i < MOB_ENCHANTS_MAX_NUM; ++i)
		mobTable->add_enchants(atoi(csvTable.AsStringByIndex(col++)));

	for (int i = 0; i < MOB_RESISTS_MAX_NUM; ++i)
		mobTable->add_resists(atoi(csvTable.AsStringByIndex(col++)));

	mobTable->set_dam_multiply(atof(csvTable.AsStringByIndex(col++)));
	mobTable->set_summon_vnum(atoi(csvTable.AsStringByIndex(col++)));
	mobTable->set_drain_sp(atoi(csvTable.AsStringByIndex(col++)));
	mobTable->set_mob_color(atoi(csvTable.AsStringByIndex(col++)));
	
	return true;
}

#else
#define Set_Mob_Proto_Table Set_Proto_Mob_Table
#endif

bool BuildMobTableFromTXT()
{

	//%%% <ÇÔ¼ö ¼³¸í> %%%//
	//1. ¿ä¾à : 'mob_proto.txt', 'mob_proto_test.txt', 'mob_names.txt' ÆÄÀÏÀ» ÀÐ°í,
	//		m_pMobTable ¸¦ ±¸¼ºÇÑ´Ù.
	//2. ¼ø¼­
	//	1)'mob_names.txt' ÆÄÀÏÀ» ÀÐ¾î¼­ vnum:name ¸ÊÀ» ¸¸µç´Ù.
	//	2)'mob_proto_test.txt' ÆÄÀÏÀ» ÀÐ¾î¼­,
	//		test_mob_table ¸¦ ¸¸µé°í,
	//		vnum:TMobTable ¸ÊÀ» ¸¸µç´Ù.
	//	3)'mob_proto.txt' ÆÄÀÏÀ» ÀÐ°í, m_pMobTable¸¦ ±¸¼ºÇÑ´Ù.
	//		test_mob_table¿¡ ÀÖ´Â vnumÀº Å×½ºÆ® µ¥ÀÌÅÍ¸¦ ³Ö´Â´Ù.
	//	4)test_mob_table µ¥ÀÌÅÍÁß¿¡, m_pMobTable ¿¡ ¾ø´Â µ¥ÀÌÅÍ¸¦ Ãß°¡ÇÑ´Ù.
	//3. Å×½ºÆ®
	//	1)'mob_proto.txt' Á¤º¸°¡ m_pMobTable¿¡ Àß µé¾î°¬´ÂÁö. -> ¿Ï·á
	//	2)'mob_names.txt' Á¤º¸°¡ m_pMobTable¿¡ Àß µé¾î°¬´ÂÁö. -> ¿Ï·á
	//	3)'mob_proto_test.txt' ¿¡¼­ [°ãÄ¡´Â] Á¤º¸°¡ m_pMobTable ¿¡ Àß µé¾î°¬´ÂÁö. -> ¿Ï·á
	//	4)'mob_proto_test.txt' ¿¡¼­ [»õ·Î¿î] Á¤º¸°¡ m_pMobTable ¿¡ Àß µé¾î°¬´ÂÁö. -> ¿Ï·á
	//^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^//

	::fprintf(stderr, "[BuildItemTableFromTXT]\n");

	//==============================================================//
	//======localº° ¸ó½ºÅÍ ÀÌ¸§À» ÀúÀåÇÏ°í ÀÖ´Â [¸Ê] vnum:name======//
	//==============================================================//
	map<int, const char*> localMap[LANGUAGE_MAX_NUM];
	bool isNameFile[LANGUAGE_MAX_NUM];
	//<¨ˇAAI A¨˘ˇľa>
	cCsvTable nameData[LANGUAGE_MAX_NUM];
	for (int i = 0; i < LANGUAGE_MAX_NUM; ++i)
	{
		isNameFile[i] = true;

		char szFileName[FILENAME_MAX];
		sprintf_s(szFileName, sizeof(szFileName), "locale/%s/mob_names.txt", strlower(astLocaleStringNames[i].c_str()));

		if (!nameData[i].Load(szFileName, '\t'))
		{
			::fprintf(stderr, "mob_names.txt ¨ˇAAIAˇí A¨˘¨úi˘ŻAAo ˘¬©ŞC©¬¨öA˘ĄI˘ĄU\n");
			isNameFile[i] = false;
		}
		else {
			nameData[i].Next();	//¨ů©ř˘¬irow ˇíyˇ¤ˇě.
			while (nameData[i].Next()) {
				localMap[i][atoi(nameData[i].AsStringByIndex(0))] = nameData[i].AsStringByIndex(1);
			}
		}
	}
	//______________________________________________________________//

	//=========================================//
	//======¸ó½ºÅÍµéÀÇ vnumÀ» ÀúÀåÇÒ [¼Â]======//
	//  *Å×½ºÆ®¿ë ÆÄÀÏÀ» »õ·Î ÀÐ¾î¿Ã¶§,        //
	//  1. ±âÁ¸¿¡ ÀÖ´ø µ¥ÀÌÅÍÀÎÁö È®ÀÏÇÒ¶§ »ç¿ë//
	//=========================================//
	set<int> vnumSet;
	//_________________________________________//

	//==================================================//
	//	2)'mob_proto_test.txt' ÆÄÀÏÀ» ÀÐ¾î¼­,
	//		test_mob_table ¸¦ ¸¸µé°í,
	//		vnum:TMobTable ¸ÊÀ» ¸¸µç´Ù.
	//==================================================//
	map<DWORD, network::TMobTable*> test_map_mobTableByVnum;

	//1. ÆÄÀÏ ÀÐ¾î¿À±â.
	cCsvTable test_data;
	if (!test_data.Load("mob_proto_test.txt", '\t'))
	{
		::fprintf(stderr, "mob_proto_test.txt ÆÄÀÏÀ» ÀÐ¾î¿ÀÁö ¸øÇß½À´Ï´Ù\n");
		//return false;
	}
	else {
		test_data.Next();	//¼³¸í ·Î¿ì ³Ñ¾î°¡±â.

		//2. Å×½ºÆ® ¸ó½ºÅÍ Å×ÀÌºí »ý¼º.
		google::protobuf::RepeatedPtrField<network::TMobTable> test_mob_table;
		int test_MobTableSize = test_data.m_File.GetRowCount() - 1;
		test_mob_table.Reserve(test_MobTableSize);

		//3. Å×½ºÆ® ¸ó½ºÅÍ Å×ÀÌºí¿¡ °ªÀ» ³Ö°í, ¸Ê¿¡±îÁö ³Ö±â.
		while (test_data.Next()) {
			auto tab = test_mob_table.Add();
			if (!Set_Mob_Proto_Table(tab, test_data, localMap))
			{
				::fprintf(stderr, "¸÷ ÇÁ·ÎÅä Å×ÀÌºí ¼ÂÆÃ ½ÇÆÐ.\n");
			}


			test_map_mobTableByVnum.insert(std::map<DWORD, network::TMobTable *>::value_type(tab->vnum(), tab));
		}
	}

	//^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^//


	//ÆÄÀÏ ÀÐ¾î¿À±â.
	cCsvTable data;
	if (!data.Load("mob_proto.txt", '\t'))
	{
		::fprintf(stderr, "mob_proto.txt ÆÄÀÏÀ» ÀÐ¾î¿ÀÁö ¸øÇß½À´Ï´Ù\n");
		return false;
	}
	data.Next(); //¸Ç À­ÁÙ Á¦¿Ü (¾ÆÀÌÅÛ Ä®·³À» ¼³¸íÇÏ´Â ºÎºÐ)



	//===== ¸÷ Å×ÀÌºí »ý¼º=====//
	if (m_MobData.data_size() > 0)
		m_MobData.clear_data();

	//»õ·Î Ãß°¡µÇ´Â °¹¼ö¸¦ ÆÄ¾ÇÇÑ´Ù.
	int addNumber = 0;
	while (data.Next()) {
		int vnum = atoi(data.AsStringByIndex(0));
		auto it_map_mobTable = test_map_mobTableByVnum.find(vnum);
		if (it_map_mobTable != test_map_mobTableByVnum.end()) {
			addNumber++;
		}
	}

	auto mobTables = m_MobData.mutable_data();
	mobTables->Reserve(data.m_File.GetRowCount() - 1 + addNumber);

	//data¸¦ ´Ù½Ã Ã¹ÁÙ·Î ¿Å±ä´Ù.(´Ù½Ã ÀÐ¾î¿Â´Ù;;)
	data.Destroy();
	if (!data.Load("mob_proto.txt", '\t'))
	{
		::fprintf(stderr, "mob_proto.txt ÆÄÀÏÀ» ÀÐ¾î¿ÀÁö ¸øÇß½À´Ï´Ù\n");
		return false;
	}
	data.Next(); //¸Ç À­ÁÙ Á¦¿Ü (¾ÆÀÌÅÛ Ä®·³À» ¼³¸íÇÏ´Â ºÎºÐ)

	while (data.Next())
	{
		int col = 0;

		auto mob_table = mobTables->Add();

		auto it_map_mobTable = test_map_mobTableByVnum.find(atoi(data.AsStringByIndex(col)));
		if (it_map_mobTable == test_map_mobTableByVnum.end()) {

			if (!Set_Mob_Proto_Table(mob_table, data, localMap))
			{
				::fprintf(stderr, "¸÷ ÇÁ·ÎÅä Å×ÀÌºí ¼ÂÆÃ ½ÇÆÐ.\n");
			}

		}
		else
		{
			*mob_table = *it_map_mobTable->second;
		}

		::fprintf(stdout, "MOB #%-5d %-16s %-16s sight: %u color %u exp %u[%s]\n",
			mob_table->vnum(),
			mob_table->name().c_str(),
			mob_table->locale_name(0).c_str(),
			mob_table->aggressive_sight(),
			mob_table->mob_color(),
			mob_table->exp(),
			0);

		vnumSet.insert(mob_table->vnum());

		++mob_table;
	}



	//============================//
	//===== Å×½ºÆ® Á¤º¸ Ãß°¡ =====//
	//%%ÁÖÀÇ%%
	//%% -> »õ·Î¿î Á¤º¸¸¸ Ãß°¡µÊ  //
	//Áßº¹µÇ´Â Á¤º¸´Â À§¿¡¼­ Ãß°¡ //
	//============================//
	test_data.Destroy();
	if (!test_data.Load("mob_proto_test.txt", '\t'))
	{
		::fprintf(stderr, "mob_proto_test.txt ÆÄÀÏÀ» ÀÐ¾î¿ÀÁö ¸øÇß½À´Ï´Ù\n");
		//return false;
	}
	else {
		test_data.Next();	//¼³¸í ·Î¿ì ³Ñ¾î°¡±â.

		while (test_data.Next())	//Å×½ºÆ® µ¥ÀÌÅÍ °¢°¢À» ÈÈ¾î³ª°¡¸ç,»õ·Î¿î °ÍÀ» Ãß°¡ÇÑ´Ù.
		{
			//Áßº¹µÇ´Â ºÎºÐÀÌ¸é ³Ñ¾î°£´Ù.
			set<int>::iterator itVnum;
			itVnum = vnumSet.find(atoi(test_data.AsStringByIndex(0)));
			if (itVnum != vnumSet.end()) {
				continue;
			}


			auto mob_table = mobTables->Add();
			if (!Set_Mob_Proto_Table(mob_table, test_data, localMap))
			{
				::fprintf(stderr, "¸÷ ÇÁ·ÎÅä Å×ÀÌºí ¼ÂÆÃ ½ÇÆÐ.\n");
			}

			::fprintf(stdout, "[New]MOB #%-5d %-16s sight: %u color %u[%s]\n",
				mob_table->vnum(),
				mob_table->locale_name(0).c_str(),
				mob_table->aggressive_sight(),
				mob_table->mob_color(),
				test_data.AsStringByIndex(54));

			//¼Â¿¡ vnum Ãß°¡
			vnumSet.insert(mob_table->vnum());

			++mob_table;
		}
	}
	//^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^//

	return true;
}

bool BuildMobTableFromDB()
{
	::fprintf(stderr, "[BuildMobTableFromDB]");

	cCsvTable data;
	if (!data.Load("mob_proto.txt", '\t'))
	{
		::fprintf(stderr, "mob_proto.txt ÆÄÀÏÀ» ÀÐ¾î¿ÀÁö ¸øÇß½À´Ï´Ù\n");
		return false;
	}

	if (m_MobData.data_size() > 0)
		m_MobData.clear_data();

	auto mobTables = m_MobData.mutable_data();
	mobTables->Reserve(data.m_File.GetRowCount());

	while (data.Next())
	{
		int col = 0;

		auto mobTable = mobTables->Add();

		mobTable->set_vnum(atoi(data.AsStringByIndex(col++)));
		mobTable->set_name(data.AsStringByIndex(col++));
		for (int i = 0; i < LANGUAGE_MAX_NUM; ++i)
			mobTable->add_locale_name(data.AsStringByIndex(col++));
		//4. RANK
		mobTable->set_rank(get_Mob_Rank_Value(data.AsStringByIndex(col++)));
		//5. TYPE
		mobTable->set_type(get_Mob_Type_Value(data.AsStringByIndex(col++)));
		//6. BATTLE_TYPE
		mobTable->set_battle_type(get_Mob_BattleType_Value(data.AsStringByIndex(col++)));

		mobTable->set_level(atoi(data.AsStringByIndex(col++)));
		//8. SIZE
		mobTable->set_size(get_Mob_Size_Value(data.AsStringByIndex(col++)));
		//9. AI_FLAG
		mobTable->set_ai_flag(get_Mob_AIFlag_Value(data.AsStringByIndex(col++)));
		col++; //mount_capacity;
		//10. RACE_FLAG
		mobTable->set_race_flag(get_Mob_RaceFlag_Value(data.AsStringByIndex(col++)));
		//11. IMMUNE_FLAG
		mobTable->set_immune_flag(get_Mob_ImmuneFlag_Value(data.AsStringByIndex(col++)));

		mobTable->set_empire(atoi(data.AsStringByIndex(col++)));

		//folder
		mobTable->set_folder(data.AsStringByIndex(col++));

		mobTable->set_on_click_type(atoi(data.AsStringByIndex(col++)));

		mobTable->set_str(atoi(data.AsStringByIndex(col++)));
		mobTable->set_dex(atoi(data.AsStringByIndex(col++)));
		mobTable->set_con(atoi(data.AsStringByIndex(col++)));
		mobTable->set_int_(atoi(data.AsStringByIndex(col++)));
		mobTable->set_damage_min(atoi(data.AsStringByIndex(col++)));
		mobTable->set_damage_max(atoi(data.AsStringByIndex(col++)));
		mobTable->set_max_hp(atoi(data.AsStringByIndex(col++)));
		mobTable->set_regen_cycle(atoi(data.AsStringByIndex(col++)));
		mobTable->set_regen_percent(atoi(data.AsStringByIndex(col++)));

		mobTable->set_gold_min(atoi(data.AsStringByIndex(col++)));
		mobTable->set_gold_max(atoi(data.AsStringByIndex(col++)));
		mobTable->set_exp(atoi(data.AsStringByIndex(col++)));
		mobTable->set_def(atoi(data.AsStringByIndex(col++)));
		mobTable->set_attack_speed(atoi(data.AsStringByIndex(col++)));
		mobTable->set_moving_speed(atoi(data.AsStringByIndex(col++)));
		mobTable->set_aggressive_hp_pct(atoi(data.AsStringByIndex(col++)));
		mobTable->set_aggressive_sight(atoi(data.AsStringByIndex(col++)));
		mobTable->set_attack_range(atoi(data.AsStringByIndex(col++)));

		mobTable->set_drop_item_vnum(atoi(data.AsStringByIndex(col++)));
		col++;	//resurrectionVnum


		for (int i = 0; i < MOB_ENCHANTS_MAX_NUM; ++i)
			mobTable->add_enchants(atoi(data.AsStringByIndex(col++)));

		for (int i = 0; i < MOB_RESISTS_MAX_NUM; ++i)
			mobTable->add_resists(atoi(data.AsStringByIndex(col++)));

		mobTable->set_dam_multiply(atof(data.AsStringByIndex(col++)));
		mobTable->set_summon_vnum(atoi(data.AsStringByIndex(col++)));
		mobTable->set_drain_sp(atoi(data.AsStringByIndex(col++)));
		mobTable->set_mob_color(atoi(data.AsStringByIndex(col++)));

		::fprintf(stdout, "MOB #%-5d %-16s %-16s sight: %u color %u[%s]\n",
			mobTable->vnum(), mobTable->name().c_str(), mobTable->locale_name(0).c_str(), mobTable->aggressive_sight(), mobTable->mob_color(), 0);
	}

	return true;
}

bool BuildMobTable()
{
	/*fprintf(stderr, "Soll die Mob-Tabelle von einem Datenbank-Export[1] oder 2 Textdateien des DB-Cores[2] erstellt werden: ");
	char arg;
	do {
		cin.clear();
		cin >> arg;
	} while (arg != '1' && arg != '2');

	if (arg == '1')
		return BuildMobTableFromDB();
	else*/
		return BuildMobTableFromTXT();
}




DWORD g_adwMobProtoKey[4] =
{   
	4813894,
	18955,
	552631,             
	6822045
};


void SaveMobProto()
{   
	FILE * fp;          

	fp = fopen("mob_proto", "wb");

	if (!fp)
	{ 
		printf("cannot open %s for writing\n", "mob_proto");
		return;
	}

	DWORD fourcc = MAKEFOURCC('M', 'M', 'P', 'T');
	fwrite(&fourcc, sizeof(DWORD), 1, fp);      

	CLZObject zObj;     

	std::vector<uint8_t> serializedData;
	serializedData.resize(m_MobData.ByteSize());
	m_MobData.SerializeToArray(&serializedData[0], serializedData.size());

	if (!CLZO::instance().CompressEncryptedMemory(zObj, &serializedData[0], serializedData.size(), g_adwMobProtoKey))
	{
		printf("cannot compress\n");
		fclose(fp);
		return;
	}

	const CLZObject::THeader & r = zObj.GetHeader();

	printf("MobProto count %u\n%u --Compress--> %u --Encrypt--> %u, GetSize %u\n",
			m_MobData.data_size(), r.dwRealSize, r.dwCompressedSize, r.dwEncryptSize, zObj.GetSize());

	DWORD dwDataSize = zObj.GetSize();
	fwrite(&dwDataSize, sizeof(DWORD), 1, fp);
	fwrite(zObj.GetBuffer(), dwDataSize, 1, fp);

	fclose(fp);
}

void LoadMobProto()
{
	FILE * fp;
	DWORD fourcc, dataSize;

	fp = fopen("mob_proto", "rb");

	fread(&fourcc, sizeof(DWORD), 1, fp);
	fread(&dataSize, sizeof(DWORD), 1, fp);
	BYTE * data = (BYTE *) malloc(dataSize);

	if (data)
	{
		fread(data, dataSize, 1, fp);

		CLZObject zObj;

		if (CLZO::instance().Decompress(zObj, data, g_adwMobProtoKey))
		{
			printf("real_size %u\n", zObj.GetSize());

			network::TRepeatedMobTable tables;
			tables.ParseFromArray(zObj.GetBuffer(), zObj.GetSize());

			for (auto& tab : tables.data())
				::printf("%u %s\n", tab.vnum(), tab.name().c_str());
		}

		free(data);
	}

	fclose(fp);
}


#ifdef __DUMP_PROTO__

bool Set_Item_Proto_Table(network::TItemTable *itemTable, cCsvTable &csvTable, std::map<int, const char*> *nameMap)
{
	itemTable->Clear();

	// vnum ¹× vnum range ÀÐ±â.
	{
		std::string s(csvTable.AsStringByIndex(0));
		int pos = s.find("~");
		// vnum ÇÊµå¿¡ '~'°¡ ¾ø´Ù¸é ÆÐ½º
		if (std::string::npos == pos)
		{
			itemTable->set_vnum(atoi(s.c_str()));
			if (0 == itemTable->vnum())
			{
				printf ("INVALID VNUM %s\n", s.c_str());
				return false;
			}
		}
		else
		{
			std::string s_start_vnum (s.substr(0, pos));
			std::string s_end_vnum (s.substr(pos +1 ));

			int start_vnum = atoi(s_start_vnum.c_str());
			int end_vnum = atoi(s_end_vnum.c_str());

			if (0 == start_vnum || (0 != end_vnum && end_vnum < start_vnum))
			{
				printf ("INVALID VNUM RANGE%s\n", s.c_str());
				return false;
			}
			itemTable->set_vnum(start_vnum);
			itemTable->set_vnum_range(end_vnum - start_vnum);
		}
	}

	int col = 1;

	itemTable->set_name(csvTable.AsStringByIndex(col++));
	//³×ÀÓ ÆÄÀÏÀÌ Á¸ÀçÇÏ¸é Á¤º¸¸¦ ÀÐ¾î¿È.
	map<int, const char*>::iterator it;
	for (int i = 0; i < LANGUAGE_MAX_NUM; ++i)
	{
		it = nameMap[i].find(itemTable->vnum());
		if (it != nameMap[i].end()) {
			itemTable->add_locale_name(it->second);
		}
		else {
			itemTable->add_locale_name(itemTable->name());
		}
	}
	itemTable->set_type(get_Item_Type_Value(csvTable.AsStringByIndex(col++)));
	itemTable->set_sub_type(get_Item_SubType_Value(itemTable->type(), csvTable.AsStringByIndex(col++)));
	itemTable->set_size(atoi(csvTable.AsStringByIndex(col++)));
	itemTable->set_anti_flags(get_Item_AntiFlag_Value(csvTable.AsStringByIndex(col++)));
	itemTable->set_flags(get_Item_Flag_Value(csvTable.AsStringByIndex(col++)));
	itemTable->set_wear_flags(get_Item_WearFlag_Value(csvTable.AsStringByIndex(col++)));
	itemTable->set_immune_flags(get_Item_Immune_Value(csvTable.AsStringByIndex(col++)));
	itemTable->set_gold(atoi(csvTable.AsStringByIndex(col++)));
	itemTable->set_shop_buy_price(atoi(csvTable.AsStringByIndex(col++)));
	itemTable->set_refined_vnum(atoi(csvTable.AsStringByIndex(col++)));
	itemTable->set_refine_set(atoi(csvTable.AsStringByIndex(col++)));
	itemTable->set_alter_to_magic_item_pct(atoi(csvTable.AsStringByIndex(col++)));

	int i;

	for (i = 0; i < ITEM_LIMIT_MAX_NUM; ++i)
	{
		auto limit = itemTable->add_limits();
		limit->set_type(get_Item_LimitType_Value(csvTable.AsStringByIndex(col++)));
		limit->set_value(atoi(csvTable.AsStringByIndex(col++)));
	}

	for (i = 0; i < ITEM_APPLY_MAX_NUM; ++i)
	{
		auto apply = itemTable->add_applies();
		apply->set_type(get_Item_ApplyType_Value(csvTable.AsStringByIndex(col++)));
		apply->set_value(atoi(csvTable.AsStringByIndex(col++)));
	}

	for (i = 0; i < ITEM_VALUES_MAX_NUM; ++i)
		itemTable->add_values(atoi(csvTable.AsStringByIndex(col++)));

	itemTable->set_specular(atoi(csvTable.AsStringByIndex(col++)));
	itemTable->set_gain_socket_pct(atoi(csvTable.AsStringByIndex(col++)));
#ifdef __ADDON_TYPE__
	itemTable->set_addon_type(atoi(csvTable.AsStringByIndex(col++))); //AddonType
#else
	col++;
#endif

	return true;
}

#else
#define Set_Item_Proto_Table Set_Proto_Item_Table
#endif

bool BuildItemTableFromTXT()
{
	//%%% <ÇÔ¼ö ¼³¸í> %%%//
	//1. ¿ä¾à : 'item_proto.txt', 'item_proto_test.txt', 'item_names.txt' ÆÄÀÏÀ» ÀÐ°í,
	//		m_pItemTable ¸¦ ±¸¼ºÇÑ´Ù.
	//2. ¼ø¼­
	//	1)'item_names.txt' ÆÄÀÏÀ» ÀÐ¾î¼­ vnum:name ¸ÊÀ» ¸¸µç´Ù.
	//	2)'item_proto_test.txt' ÆÄÀÏÀ» ÀÐ¾î¼­,
	//		test_item_table ¸¦ ¸¸µé°í,
	//		vnum:TClientItemTable ¸ÊÀ» ¸¸µç´Ù.
	//	3)'item_proto.txt' ÆÄÀÏÀ» ÀÐ°í, m_pItemTable¸¦ ±¸¼ºÇÑ´Ù.
	//		test_item_table¿¡ ÀÖ´Â vnumÀº Å×½ºÆ® µ¥ÀÌÅÍ¸¦ ³Ö´Â´Ù.
	//	4)test_item_table µ¥ÀÌÅÍÁß¿¡, m_pItemTable ¿¡ ¾ø´Â µ¥ÀÌÅÍ¸¦ Ãß°¡ÇÑ´Ù.
	//3. Å×½ºÆ®
	//	1)'item_proto.txt' Á¤º¸°¡ m_pItemTable¿¡ Àß µé¾î°¬´ÂÁö.
	//	2)'item_names.txt' Á¤º¸°¡ m_pItemTable¿¡ Àß µé¾î°¬´ÂÁö.
	//	3)'item_proto_test.txt' ¿¡¼­ [°ãÄ¡´Â] Á¤º¸°¡ m_pItemTable ¿¡ Àß µé¾î°¬´ÂÁö.
	//	4)'item_proto_test.txt' ¿¡¼­ [»õ·Î¿î] Á¤º¸°¡ m_pItemTable ¿¡ Àß µé¾î°¬´ÂÁö.
	//^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^//

	fprintf(stderr, "[BuildItemTableFromTXT]");

	//=================================================================//
	//	1)'item_names.txt' ÆÄÀÏÀ» ÀÐ¾î¼­ vnum:name ¸ÊÀ» ¸¸µç´Ù.
	//=================================================================//
	map<int, const char*> localMap[LANGUAGE_MAX_NUM];
	bool isNameFile[LANGUAGE_MAX_NUM];
	cCsvTable nameData[LANGUAGE_MAX_NUM];
	for (int i = 0; i < LANGUAGE_MAX_NUM; ++i)
	{
		isNameFile[i] = true;

		char szFileName[FILENAME_MAX];
		sprintf_s(szFileName, sizeof(szFileName), "locale/%s/item_names.txt", strlower(astLocaleStringNames[i].c_str()));

		if (!nameData[i].Load(szFileName, '\t'))
		{
			fprintf(stderr, "item_names.txt ¨ˇAAIAˇí A¨˘¨úi˘ŻAAo ˘¬©ŞC©¬¨öA˘ĄI˘ĄU\n");
			isNameFile[i] = false;
		}
		else {
			nameData[i].Next();	//¨ů©ř˘¬irow ˇíyˇ¤ˇě.
			while (nameData[i].Next()) {
				localMap[i][atoi(nameData[i].AsStringByIndex(0))] = nameData[i].AsStringByIndex(1);
			}
		}
	}
	//_________________________________________________________________//

	//===================== =======================//
	//	2)'item_proto_test.txt' ÆÄÀÏÀ» ÀÐ¾î¼­,
	//		test_item_table ¸¦ ¸¸µé°í,
	//		vnum:TClientItemTable ¸ÊÀ» ¸¸µç´Ù.
	//=============================================//
	map<DWORD, network::TItemTable *> test_map_itemTableByVnum;

	//1. ÆÄÀÏ ÀÐ¾î¿À±â.
	cCsvTable test_data;
	if (!test_data.Load("item_proto_test.txt", '\t'))
	{
		fprintf(stderr, "item_proto_test.txt ÆÄÀÏÀ» ÀÐ¾î¿ÀÁö ¸øÇß½À´Ï´Ù\n");
		//return false;
	}
	else {
		test_data.Next();	//¼³¸í ·Î¿ì ³Ñ¾î°¡±â.

		//2. Å×½ºÆ® ¾ÆÀÌÅÛ Å×ÀÌºí »ý¼º.
		google::protobuf::RepeatedPtrField<network::TItemTable> test_item_table;
		int test_itemTableSize = test_data.m_File.GetRowCount() - 1;
		test_item_table.Reserve(test_itemTableSize);

		//3. Å×½ºÆ® ¸ó½ºÅÍ Å×ÀÌºí¿¡ °ªÀ» ³Ö°í, ¸Ê¿¡±îÁö ³Ö±â.
		while (test_data.Next()) {
			auto table = TItemTable();
			if (!Set_Item_Proto_Table(&table, test_data, localMap))
			{
				fprintf(stderr, "¸÷ ÇÁ·ÎÅä Å×ÀÌºí ¼ÂÆÃ ½ÇÆÐ.\n");
				continue;
			}

			auto ptr_table = test_item_table.Add();
			*ptr_table = table;
			test_map_itemTableByVnum.insert(std::map<DWORD, network::TItemTable *>::value_type(ptr_table->vnum(), ptr_table));
		}
	}

	//^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^//


	//================================================================//
	//	3)'item_proto.txt' ÆÄÀÏÀ» ÀÐ°í, m_pItemTable¸¦ ±¸¼ºÇÑ´Ù.
	//		test_item_table¿¡ ÀÖ´Â vnumÀº Å×½ºÆ® µ¥ÀÌÅÍ¸¦ ³Ö´Â´Ù.
	//================================================================//

	//vnumµéÀ» ÀúÀåÇÒ ¼Â. »õ·Î¿î Å×½ºÆ® ¾ÆÀÌÅÛÀ» ÆÇº°ÇÒ¶§ »ç¿ëµÈ´Ù.
	set<int> vnumSet;

	//ÆÄÀÏ ÀÐ¾î¿À±â.
	cCsvTable data;
	if (!data.Load("item_proto.txt", '\t'))
	{
		fprintf(stderr, "item_proto.txt ÆÄÀÏÀ» ÀÐ¾î¿ÀÁö ¸øÇß½À´Ï´Ù\n");
		return false;
	}
	data.Next(); //¸Ç À­ÁÙ Á¦¿Ü (¾ÆÀÌÅÛ Ä®·³À» ¼³¸íÇÏ´Â ºÎºÐ)

	if (m_ItemData.data_size() > 0)
		m_ItemData.clear_data();

	//===== ¾ÆÀÌÅÛ Å×ÀÌºí »ý¼º =====//
	//»õ·Î Ãß°¡µÇ´Â °¹¼ö¸¦ ÆÄ¾ÇÇÑ´Ù.
	int addNumber = 0;
	while (data.Next()) {
		int vnum = atoi(data.AsStringByIndex(0));
		auto it_map_itemTable = test_map_itemTableByVnum.find(vnum);
		if (it_map_itemTable != test_map_itemTableByVnum.end()) {
			addNumber++;
		}
	}
	//data¸¦ ´Ù½Ã Ã¹ÁÙ·Î ¿Å±ä´Ù.(´Ù½Ã ÀÐ¾î¿Â´Ù;;)
	data.Destroy();
	if (!data.Load("item_proto.txt", '\t'))
	{
		fprintf(stderr, "item_proto.txt ÆÄÀÏÀ» ÀÐ¾î¿ÀÁö ¸øÇß½À´Ï´Ù\n");
		return false;
	}
	data.Next(); //¸Ç À­ÁÙ Á¦¿Ü (¾ÆÀÌÅÛ Ä®·³À» ¼³¸íÇÏ´Â ºÎºÐ)

	auto itemTables = m_ItemData.mutable_data();
	itemTables->Reserve(data.m_File.GetRowCount() - 1 + addNumber);

	while (data.Next())
	{
		int col = 0;

		auto tmp_item_table = TItemTable();

		auto it_map_itemTable = test_map_itemTableByVnum.find(atoi(data.AsStringByIndex(col)));
		if (it_map_itemTable == test_map_itemTableByVnum.end()) {


			if (!Set_Item_Proto_Table(&tmp_item_table, data, localMap))
			{
				fprintf(stderr, "¸÷ ÇÁ·ÎÅä Å×ÀÌºí ¼ÂÆÃ ½ÇÆÐ.\n");
				continue;
			}
		}
		else {	//$$$$$$$$$$$$$$$$$$$$$$$ Å×½ºÆ® ¾ÆÀÌÅÛ Á¤º¸°¡ ÀÖ´Ù!	
			tmp_item_table = *it_map_itemTable->second;
		}

		auto item_table = itemTables->Add();
		*item_table = std::move(tmp_item_table);

		fprintf(stdout, "ITEM #%-5u %-24s %-24s TYPE: %d SUBTYPE: %d VAL: %ld %ld %ld %ld %ld %ld WEAR %u ANTI %u IMMUNE %u REFINE %u\n",
			item_table->vnum(),
			item_table->name().c_str(),
			item_table->locale_name(0).c_str(),
			item_table->type(),
			item_table->sub_type(),
			item_table->values(0),
			item_table->values(1),
			item_table->values(2),
			item_table->values(3),
			item_table->values(4),
			item_table->values(5),
			item_table->wear_flags(),
			item_table->anti_flags(),
			item_table->immune_flags(),
			item_table->refined_vnum());

		//vnum ÀúÀå.
		vnumSet.insert(item_table->vnum());
		++item_table;
	}

	//==========================================================================//
	//	4)test_item_table µ¥ÀÌÅÍÁß¿¡, m_pItemTable ¿¡ ¾ø´Â µ¥ÀÌÅÍ¸¦ Ãß°¡ÇÑ´Ù.
	//==========================================================================//
	test_data.Destroy();
	if (!test_data.Load("item_proto_test.txt", '\t'))
	{
		fprintf(stderr, "item_proto_test.txt ÆÄÀÏÀ» ÀÐ¾î¿ÀÁö ¸øÇß½À´Ï´Ù\n");
		//return false;
	}
	else {
		test_data.Next();	//¼³¸í ·Î¿ì ³Ñ¾î°¡±â.

		while (test_data.Next())	//Å×½ºÆ® µ¥ÀÌÅÍ °¢°¢À» ÈÈ¾î³ª°¡¸ç,»õ·Î¿î °ÍÀ» Ãß°¡ÇÑ´Ù.
		{
			//Áßº¹µÇ´Â ºÎºÐÀÌ¸é ³Ñ¾î°£´Ù.
			set<int>::iterator itVnum;
			itVnum = vnumSet.find(atoi(test_data.AsStringByIndex(0)));
			if (itVnum != vnumSet.end()) {
				continue;
			}

			auto tmp_item_table = TItemTable();
			if (!Set_Item_Proto_Table(&tmp_item_table, test_data, localMap))
			{
				fprintf(stderr, "¸÷ ÇÁ·ÎÅä Å×ÀÌºí ¼ÂÆÃ ½ÇÆÐ.\n");
				continue;
			}

			auto item_table = itemTables->Add();
			*item_table = std::move(tmp_item_table);

			fprintf(stdout, "[NEW]ITEM #%-5u %-24s %-24s TYPE: %d SUBTYPE: %d VAL: %ld %ld %ld %ld %ld %ld WEAR %u ANTI %u IMMUNE %u REFINE %u\n",
				item_table->vnum(),
				item_table->name().c_str(),
				item_table->locale_name(0).c_str(),
				item_table->type(),
				item_table->sub_type(),
				item_table->values(0),
				item_table->values(1),
				item_table->values(2),
				item_table->values(3),
				item_table->values(4),
				item_table->values(5),
				item_table->wear_flags(),
				item_table->anti_flags(),
				item_table->immune_flags(),
				item_table->refined_vnum());


			//¼Â¿¡ vnum Ãß°¡
			vnumSet.insert(item_table->vnum());

			++item_table;
		}
	}

	return true;
}

bool BuildItemTableFromDB()
{
	fprintf(stderr, "[BuildItemTableFromDB]");

	//================================================================//
	//	3)'item_proto.txt' ÆÄÀÏÀ» ÀÐ°í, m_pItemTable¸¦ ±¸¼ºÇÑ´Ù.
	//		test_item_table¿¡ ÀÖ´Â vnumÀº Å×½ºÆ® µ¥ÀÌÅÍ¸¦ ³Ö´Â´Ù.
	//================================================================//

	//vnumµéÀ» ÀúÀåÇÒ ¼Â. »õ·Î¿î Å×½ºÆ® ¾ÆÀÌÅÛÀ» ÆÇº°ÇÒ¶§ »ç¿ëµÈ´Ù.
	set<int> vnumSet;

	//ÆÄÀÏ ÀÐ¾î¿À±â.

	if (m_ItemData.data_size() > 0)
		m_ItemData.clear_data();

	cCsvTable data;
	if (!data.Load("item_proto.txt", '\t'))
	{
		fprintf(stderr, "item_proto.txt ÆÄÀÏÀ» ÀÐ¾î¿ÀÁö ¸øÇß½À´Ï´Ù\n");
		return false;
	}

	auto itemTables = m_ItemData.mutable_data();
	itemTables->Reserve(data.m_File.GetRowCount());

	while (data.Next())
	{
		auto item_table = itemTables->Add();

		{
			std::string s(data.AsStringByIndex(0));
			int pos = s.find("~");
			// vnum ÇÊµå¿¡ '~'°¡ ¾ø´Ù¸é ÆÐ½º
			if (std::string::npos == pos)
			{
				item_table->set_vnum(atoi(s.c_str()));
				if (0 == item_table->vnum())
				{
					printf("INVALID VNUM %s\n", s.c_str());
					return false;
				}
			}
			else
			{
				std::string s_start_vnum(s.substr(0, pos));
				std::string s_end_vnum(s.substr(pos + 1));

				int start_vnum = atoi(s_start_vnum.c_str());
				int end_vnum = atoi(s_end_vnum.c_str());

				if (0 == start_vnum || (0 != end_vnum && end_vnum < start_vnum))
				{
					printf("INVALID VNUM RANGE%s\n", s.c_str());
					return false;
				}
				item_table->set_vnum(start_vnum);
				item_table->set_vnum_range(end_vnum - start_vnum);
			}
		}

		int col = 1;

		item_table->set_name(data.AsStringByIndex(col++));
		for (int i = 0; i < LANGUAGE_MAX_NUM; ++i)
			item_table->add_locale_name(data.AsStringByIndex(col++));

		item_table->set_type(get_Item_Type_Value(data.AsStringByIndex(col++)));
		item_table->set_sub_type(get_Item_SubType_Value(item_table->type(), data.AsStringByIndex(col++)));
		item_table->set_weight(atoi(data.AsStringByIndex(col++)));
		item_table->set_size(atoi(data.AsStringByIndex(col++)));
		item_table->set_anti_flags(get_Item_AntiFlag_Value(data.AsStringByIndex(col++)));
		item_table->set_flags(get_Item_Flag_Value(data.AsStringByIndex(col++)));
		item_table->set_wear_flags(get_Item_WearFlag_Value(data.AsStringByIndex(col++)));
		item_table->set_immune_flags(get_Item_Immune_Value(data.AsStringByIndex(col++)));
		item_table->set_gold(atoi(data.AsStringByIndex(col++)));
		item_table->set_shop_buy_price(atoi(data.AsStringByIndex(col++)));
		item_table->set_refined_vnum(atoi(data.AsStringByIndex(col++)));
		item_table->set_refine_set(atoi(data.AsStringByIndex(col++)));
		col++; // refineSet2
		item_table->set_alter_to_magic_item_pct(atoi(data.AsStringByIndex(col++)));

		int i;

		for (i = 0; i < ITEM_LIMIT_MAX_NUM; ++i)
		{
			auto limit = item_table->add_limits();
			limit->set_type(get_Item_LimitType_Value(data.AsStringByIndex(col++)));
			limit->set_value(atoi(data.AsStringByIndex(col++)));
		}

		for (i = 0; i < ITEM_APPLY_MAX_NUM; ++i)
		{
			auto apply = item_table->add_applies();
			apply->set_type(get_Item_ApplyType_Value(data.AsStringByIndex(col++)));
			apply->set_value(atoi(data.AsStringByIndex(col++)));
		}

		for (i = 0; i < ITEM_VALUES_MAX_NUM; ++i)
			item_table->add_values(atoi(data.AsStringByIndex(col++)));

		for (i = 0; i < 5 + 1; ++i)
		{
			long lSocket = atoi(data.AsStringByIndex(col++));
			if (i < ITEM_SOCKET_MAX_NUM)
				item_table->add_sockets(lSocket);
		}

		item_table->set_specular(atoi(data.AsStringByIndex(col++)));
		item_table->set_gain_socket_pct(atoi(data.AsStringByIndex(col++)));
#ifdef __ADDON_TYPE__
		item_table->set_addon_type(atoi(data.AsStringByIndex(col++))); //AddonType
#else
		col++;
#endif

		fprintf(stdout, "ITEM #%-5u %-24s %-24s TYPE: %d SUBTYPE: %d VAL: %ld %ld %ld %ld %ld %ld WEAR %u ANTI %u IMMUNE %u REFINE %u\n",
			item_table->vnum(),
			item_table->name().c_str(),
			item_table->locale_name(0).c_str(),
			item_table->type(),
			item_table->sub_type(),
			item_table->values(0),
			item_table->values(1),
			item_table->values(2),
			item_table->values(3),
			item_table->values(4),
			item_table->values(5),
			item_table->wear_flags(),
			item_table->anti_flags(),
			item_table->immune_flags(),
			item_table->refined_vnum());

		//vnum ÀúÀå.
		vnumSet.insert(item_table->vnum());
		++item_table;
	}

	return true;
}

bool BuildItemTable()
{
	/*
	fprintf(stderr, "Soll die Item-Tabelle von einem Datenbank-Export[1] oder 2 Textdateien des DB-Cores[2] erstellt werden: ");
	char arg;
	do {
		cin.clear();
		cin >> arg;
	} while (arg != '1' && arg != '2');

	if (arg == '1')
		return BuildItemTableFromDB();
	else*/
		return BuildItemTableFromTXT();
}

DWORD g_adwItemProtoKey[4] =
{
	173217,
	72619434,
	408587239,
	27973291
};  

void SaveItemProto()
{
	FILE * fp;

	fp = fopen("item_proto", "wb");

	if (!fp)
	{
		printf("cannot open %s for writing\n", "item_proto");
		return;
	}  

	DWORD fourcc = MAKEFOURCC('M', 'I', 'P', 'X');
	fwrite(&fourcc, sizeof(DWORD), 1, fp);

	CLZObject zObj;

	std::vector<BYTE> serializedData;
	serializedData.resize(m_ItemData.ByteSize());
	m_ItemData.SerializeToArray(&serializedData[0], serializedData.size());

	if (!CLZO::instance().CompressEncryptedMemory(zObj, &serializedData[0], serializedData.size(), g_adwItemProtoKey))
	{
		printf("cannot compress\n");
		fclose(fp);
		return;
	}

	const CLZObject::THeader & r = zObj.GetHeader();

	printf("Elements %d\n%u --Compress--> %u --Encrypt--> %u, GetSize %u\n",
			m_ItemData.data_size(),
			r.dwRealSize,
			r.dwCompressedSize,
			r.dwEncryptSize,
			zObj.GetSize());

	DWORD dwDataSize = zObj.GetSize();
	fwrite(&dwDataSize, sizeof(DWORD), 1, fp);
	fwrite(zObj.GetBuffer(), dwDataSize, 1, fp);

	fclose(fp);

	fp = fopen("item_proto", "rb");

	if (!fp)
	{
		printf("Error!!\n");
		return;
	}

	fread(&fourcc, sizeof(DWORD), 1, fp);

	printf("Elements Check %u fourcc match %d\n", m_ItemData.data_size(), fourcc == MAKEFOURCC('M', 'I', 'P', 'X'));
	fclose(fp);
}

int main(int argc, char ** argv)
{
	astLocaleStringNames[LANGUAGE_ENGLISH] = "en";
	astLocaleStringNames[LANGUAGE_GERMAN] = "de";
	astLocaleStringNames[LANGUAGE_TURKISH] = "tr";
	astLocaleStringNames[LANGUAGE_ROMANIA] = "ro";
	astLocaleStringNames[LANGUAGE_POLISH] = "pl";
	astLocaleStringNames[LANGUAGE_ITALIAN] = "it";
	astLocaleStringNames[LANGUAGE_SPANISH] = "es";
	astLocaleStringNames[LANGUAGE_HUNGARIAN] = "hu";
	astLocaleStringNames[LANGUAGE_CZECH] = "cz";
	astLocaleStringNames[LANGUAGE_PORTUGUESE] = "pt";
	astLocaleStringNames[LANGUAGE_FRENCH] = "fr";
	astLocaleStringNames[LANGUAGE_ARABIC] = "ae";
	astLocaleStringNames[LANGUAGE_GREEK] = "gr";

	/*astLocaleStringNames[LANGUAGE_DK] = "dk";
	astLocaleStringNames[LANGUAGE_NL] = "nl";
	astLocaleStringNames[LANGUAGE_RU] = "ru";

	if (argc > 1)
		for (BYTE i = 1; i < argc; ++i)
			astLocaleStringNames[i - 1] = argv[i];*/
	
	if (BuildMobTable())
	{
		SaveMobProto();
		cout << "BuildMobTable working normal" << endl;
	}
	

	
	if (BuildItemTable())
	{
		SaveItemProto();
		cout << "BuildItemTable working normal" << endl;
	}
	
	

	return 0;
}
