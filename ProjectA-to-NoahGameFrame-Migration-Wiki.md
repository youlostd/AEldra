# 🎮 ProjectA to NoahGameFrame Migration Wiki

## 📋 Table of Contents

1. [Overview](#overview)
2. [Architecture Analysis](#architecture-analysis)
3. [Core Systems Migration](#core-systems-migration)
4. [Implementation Guide](#implementation-guide)
5. [Troubleshooting](#troubleshooting)
6. [Contributing](#contributing)

---

## 🎯 Overview

This wiki provides a comprehensive guide for migrating ProjectA's game logic and mechanics to the NoahGameFrame framework. ProjectA is a Korean MMORPG server implementation, and NoahGameFrame is a modern C++ game server framework with plugin architecture.

### 🎯 Migration Goals

- **Preserve Core Game Logic**: Maintain all existing game mechanics and balance
- **Modernize Architecture**: Leverage NoahGameFrame's plugin system and modern C++ features
- **Improve Performance**: Utilize NoahGameFrame's optimized networking and database layers
- **Enhance Maintainability**: Clean separation of concerns and modular design
- **Cross-Platform Support**: Benefit from NoahGameFrame's cross-platform capabilities

### 📊 ProjectA Analysis Summary

| System | Files | Lines | Complexity | Priority |
|--------|-------|-------|------------|----------|
| CHARACTER | char.h/cpp | 3200+ | High | Tier 1 |
| ITEM | item.h/cpp | 500+ | Medium | Tier 1 |
| SKILL | skill.h/cpp | 300+ | High | Tier 1 |
| BATTLE | battle.h/cpp | 200+ | High | Tier 1 |
| PARTY | party.h/cpp | 400+ | Medium | Tier 1 |
| GUILD | guild.h/cpp | 500+ | High | Tier 1 |
| QUEST | quest*.h/cpp | 800+ | Medium | Tier 2 |
| DUNGEON | dungeon*.h/cpp | 600+ | Medium | Tier 2 |

---

## 🏗️ Architecture Analysis

### 🔍 ProjectA Current Architecture

```
ProjectA Server Structure:
├── Source/Server/
│   ├── game/src/           # Core game logic
│   │   ├── char.h/cpp      # Character system
│   │   ├── item.h/cpp      # Item system
│   │   ├── skill.h/cpp     # Skill system
│   │   ├── battle.h/cpp    # Battle system
│   │   ├── party.h/cpp     # Party system
│   │   ├── guild.h/cpp     # Guild system
│   │   └── ...             # Other systems
│   ├── db/src/             # Database server
│   └── libthecore/         # Core utilities
```

### 🚀 NoahGameFrame Target Architecture

```
NoahGameFrame Plugin Structure:
├── NFGameLogicModule/      # Main game logic plugin
│   ├── NFCharacter/        # Character system
│   ├── NFItem/             # Item system
│   ├── NFSkill/            # Skill system
│   ├── NFBattle/           # Battle system
│   ├── NFParty/            # Party system
│   └── NFGuild/            # Guild system
├── NFCombatModule/         # Combat-specific features
├── NFQuestModule/          # Quest system
└── NFGuildModule/          # Guild-specific features
```

### 🔄 Migration Strategy

#### **Wrapper Pattern Approach**
```cpp
// ProjectA classes wrapped in NoahGameFrame interfaces
class NFCharacter : public NFIObject
{
private:
    std::unique_ptr<CHARACTER> m_pOldCharacter;  // ProjectA character
public:
    // NoahGameFrame interface methods
    NFGUID GetGUID() const override;
    void SetGUID(const NFGUID& guid) override;
    // ... other interface methods
};
```

#### **Gradual Migration**
1. **Phase 1**: Core systems (Character, Item, Skill, Battle)
2. **Phase 2**: Social systems (Party, Guild)
3. **Phase 3**: Advanced systems (Quest, Dungeon, Events)
4. **Phase 4**: Polish and optimization

---

## 🎮 Core Systems Migration

### 1. 🧙‍♂️ CHARACTER System

#### **Current ProjectA Structure**
```cpp
class CHARACTER : public CEntity, public CFSM
{
    // Core attributes
    CHARACTER_POINT m_points;           // HP, SP, ST, ATK, DEF
    CHARACTER_POINT_INSTANT m_pointsInstant;
    
    // Combat system
    DWORD m_dwLastAttackTime;
    LPCHARACTER m_pkChrTarget;
    
    // Item system
    std::vector<LPITEM> m_pItems;
    LPITEM m_pWear[WEAR_MAX_NUM];
    
    // Skill system
    BYTE m_abSkill[CHARACTER_SKILL_COUNT];
    DWORD m_dwSkillGroup;
    
    // Social systems
    LPPARTY m_pkParty;
    LPGUILD m_pkGuild;
};
```

#### **NoahGameFrame Migration**
```cpp
class NFCharacter : public NFIObject
{
private:
    std::unique_ptr<CHARACTER> m_pOldCharacter;
    
public:
    // Core attributes
    int GetHP() const;
    void SetHP(int hp);
    int GetMaxHP() const;
    
    int GetSP() const;
    void SetSP(int sp);
    int GetMaxSP() const;
    
    int GetLevel() const;
    void SetLevel(int level);
    
    // Combat system
    bool Attack(NFCharacter* target);
    int CalculateDamage(NFCharacter* target);
    bool IsAlive() const;
    
    // Item system
    bool EquipItem(NFItem* item, int slot);
    bool UnequipItem(int slot);
    NFItem* GetEquippedItem(int slot) const;
    
    // Skill system
    bool UseSkill(int skillId, NFCharacter* target);
    int GetSkillLevel(int skillId) const;
    void SetSkillLevel(int skillId, int level);
    
    // Social systems
    void JoinParty(NFParty* party);
    void LeaveParty();
    NFParty* GetParty() const;
    
    void JoinGuild(NFGuild* guild);
    void LeaveGuild();
    NFGuild* GetGuild() const;
    
    // Update loop
    void Update() override;
};
```

### 2. 📦 ITEM System

#### **Current ProjectA Structure**
```cpp
class CItem : public CEntity
{
    DWORD m_dwVnum;                    // Item number
    DWORD m_dwID;                      // Unique ID
    DWORD m_dwCount;                   // Quantity
    DWORD m_dwVID;                     // Virtual ID
    
    long m_lFlag;                      // Item flags
    BYTE m_bWindow;                    // Window type
    
    // Socket system
    TPlayerItemAttribute m_aAttr[ITEM_ATTRIBUTE_MAX_NUM];
    TPlayerItemAttributeEx m_aAttrEx[ITEM_ATTRIBUTE_MAX_NUM];
    
    // Refine system
    BYTE m_bRefineLevel;
    DWORD m_dwRefineExp;
};
```

#### **NoahGameFrame Migration**
```cpp
class NFItem : public NFIObject
{
private:
    std::unique_ptr<CItem> m_pOldItem;
    
public:
    // Basic properties
    int GetVnum() const;
    void SetVnum(int vnum);
    
    int GetCount() const;
    void SetCount(int count);
    
    int GetID() const;
    void SetID(int id);
    
    // Item type
    int GetType() const;
    int GetSubType() const;
    
    // Item properties
    bool IsStackable() const;
    bool IsEquipable() const;
    int GetWearFlag() const;
    
    // Socket system
    int GetSocket(int index) const;
    void SetSocket(int index, int value);
    
    // Attribute system
    int GetAttribute(int index) const;
    void SetAttribute(int index, int value);
    
    // Refine system
    int GetRefineLevel() const;
    void SetRefineLevel(int level);
    
    // Usage
    bool Use(NFCharacter* user);
    bool CanUse(NFCharacter* user) const;
    
    // Serialization
    void Serialize(NFDataList& dataList) const override;
    void Deserialize(const NFDataList& dataList) override;
};
```

### 3. ⚔️ SKILL System

#### **Current ProjectA Structure**
```cpp
struct CSkillProto
{
    DWORD dwVnum;                      // Skill number
    std::string strName;               // Skill name
    BYTE bType;                        // Skill type
    BYTE bMaxLevel;                    // Max level
    
    int iSplashAround;                 // Splash radius
    int iSplashCount;                  // Splash count
    
    int iNeedSP;                       // SP cost
    int iNeedHP;                       // HP cost
    int iNeedItem;                     // Item cost
    
    int iCooltime;                     // Cooldown time
    DWORD dwFlag;                      // Skill flags
    
    CExpression m_meleeDamage;         // Melee damage formula
    CExpression m_magicDamage;         // Magic damage formula
    CExpression m_needSP;              // SP requirement formula
};
```

#### **NoahGameFrame Migration**
```cpp
class NFSkill : public NFIObject
{
private:
    CSkillProto* m_pSkillProto;
    int m_iLevel;
    DWORD m_dwLastUseTime;
    
public:
    // Basic properties
    int GetVnum() const;
    std::string GetName() const;
    int GetType() const;
    int GetLevel() const;
    void SetLevel(int level);
    
    // Usage
    bool CanUse(NFCharacter* user) const;
    bool Use(NFCharacter* user, NFCharacter* target);
    
    // Damage calculation
    int CalculateDamage(NFCharacter* user, NFCharacter* target) const;
    int CalculateMagicDamage(NFCharacter* user, NFCharacter* target) const;
    
    // Costs
    int GetNeedSP() const;
    int GetNeedHP() const;
    int GetNeedItem() const;
    
    // Cooldown
    int GetCooltime() const;
    bool IsOnCooldown() const;
    void SetLastUseTime(DWORD time);
    
    // Flags
    bool HasFlag(int flag) const;
    bool IsAttackSkill() const;
    bool IsMagicSkill() const;
    bool IsSplashSkill() const;
};
```

### 4. ⚔️ BATTLE System

#### **Current ProjectA Structure**
```cpp
// Battle calculation functions
extern int CalcMeleeDamage(LPCHARACTER pAttacker, LPCHARACTER pVictim, 
                          bool bIgnoreDefense = false, 
                          bool bIgnoreTargetRating = false);

extern int CalcMagicDamage(LPCHARACTER pAttacker, LPCHARACTER pVictim);

extern int CalcArrowDamage(LPCHARACTER pkAttacker, LPCHARACTER pkVictim, 
                          LPITEM pkBow, LPITEM pkArrow, 
                          bool bIgnoreDefense = false);

extern float CalcAttackRating(LPCHARACTER pkAttacker, LPCHARACTER pkVictim, 
                             bool bIgnoreTargetRating = false);
```

#### **NoahGameFrame Migration**
```cpp
class NFBattleSystem : public NFIModule
{
public:
    // Damage calculation
    int CalculateMeleeDamage(NFCharacter* attacker, NFCharacter* victim, 
                            bool ignoreDefense = false, 
                            bool ignoreTargetRating = false);
    
    int CalculateMagicDamage(NFCharacter* attacker, NFCharacter* victim);
    
    int CalculateArrowDamage(NFCharacter* attacker, NFCharacter* victim, 
                            NFItem* bow, NFItem* arrow, 
                            bool ignoreDefense = false);
    
    // Attack rating calculation
    float CalculateAttackRating(NFCharacter* attacker, NFCharacter* victim, 
                               bool ignoreTargetRating = false);
    
    // Combat controls
    bool CanAttack(NFCharacter* attacker, NFCharacter* victim);
    bool IsAttackable(NFCharacter* attacker, NFCharacter* victim);
    
    // Combat operations
    int MeleeAttack(NFCharacter* attacker, NFCharacter* victim);
    int MagicAttack(NFCharacter* attacker, NFCharacter* victim);
    int ArrowAttack(NFCharacter* attacker, NFCharacter* victim, NFItem* bow, NFItem* arrow);
    
    // Combat end
    void EndBattle(NFCharacter* attacker);
    void OnCharacterDeath(NFCharacter* character);
    
    // Critical hit and penetration
    bool IsCriticalHit(NFCharacter* attacker, NFCharacter* victim);
    bool IsPenetration(NFCharacter* attacker, NFCharacter* victim);
    
    // Elemental damage
    int CalculateElementalDamage(NFCharacter* attacker, NFCharacter* victim, int elementType);
    
    // Buff/Debuff effects
    void ApplyAttackEffects(NFCharacter* attacker, NFCharacter* victim, int damage);
    void ApplySkillEffects(NFCharacter* attacker, NFCharacter* victim, int skillId);
};
```

### 5. 👥 PARTY System

#### **Current ProjectA Structure**
```cpp
class CParty
{
    typedef struct SMember
    {
        LPCHARACTER pCharacter;        // Character pointer
        bool bNear;                    // Is near?
        bool bLeader;                  // Is leader?
        BYTE bRole;                    // Role (tanker, healer, etc.)
        BYTE bLevel;                   // Level
        std::string strName;           // Name
    } TMember;
    
    TMemberMap m_memberMap;            // Member map
    DWORD m_dwLeaderPID;               // Leader PID
    LPCHARACTER m_pkChrLeader;         // Leader character
    
    int m_iExpBonus;                   // EXP bonus
    int m_iAttBonus;                   // Attack bonus
    int m_iDefBonus;                   // Defense bonus
};
```

#### **NoahGameFrame Migration**
```cpp
class NFParty : public NFIObject
{
public:
    struct Member
    {
        NFGUID characterGUID;
        bool isNear;
        bool isLeader;
        int role;
        int level;
        std::string name;
    };
    
private:
    std::map<NFGUID, Member> m_mapMembers;
    NFGUID m_leaderGUID;
    
    int m_iExpBonus;
    int m_iAttBonus;
    int m_iDefBonus;
    
public:
    // Member management
    bool AddMember(NFCharacter* character);
    bool RemoveMember(NFCharacter* character);
    bool IsMember(NFCharacter* character) const;
    
    // Leader management
    NFCharacter* GetLeader() const;
    bool SetLeader(NFCharacter* character);
    
    // Member count
    int GetMemberCount() const;
    int GetNearMemberCount() const;
    
    // Bonus calculations
    int GetExpBonus() const;
    int GetAttackBonus() const;
    int GetDefenseBonus() const;
    void CalculateBonuses();
    
    // EXP distribution
    void SetExpDistributionMode(int mode);
    int GetExpDistributionMode() const;
    void DistributeExp(int exp, NFCharacter* source);
    
    // Messaging
    void SendMessageToAll(const std::string& message);
    void SendMessageToNear(const std::string& message);
    
    // Role system
    bool SetMemberRole(NFCharacter* character, int role);
    int GetMemberRole(NFCharacter* character) const;
    
    // Party healing
    void HealParty();
    void SummonToLeader(NFCharacter* character);
    
    // Update
    void Update() override;
};
```

### 6. 🏰 GUILD System

#### **Current ProjectA Structure**
```cpp
class CGuild
{
    TGuildData m_data;
    TGuildMemberContainer m_member;
    TGuildMemberOnlineContainer m_memberOnline;
    
    int m_general_count;
    int m_iMemberCountBonus;
    
    TEnemyGuildContainer m_EnemyGuild;
    std::map<DWORD, DWORD> m_mapGuildWarEndTime;
    
    bool m_abSkillUsable[GUILD_SKILL_COUNT];
};
```

#### **NoahGameFrame Migration**
```cpp
class NFGuild : public NFIObject
{
public:
    struct GuildMember
    {
        NFGUID characterGUID;
        int grade;                    // Rank (1-15)
        bool isGeneral;               // Is general?
        int job;                      // Job
        int level;                    // Level
        int offerExp;                 // Donated EXP
        std::string name;
    };
    
    struct GuildData
    {
        int guildId;
        NFGUID masterGUID;
        int exp;
        int level;
        std::string name;
        int gold;
        int power;
        int maxPower;
        int ladderPoint;
        int win[GUILD_WAR_TYPE_MAX_NUM];
        int draw[GUILD_WAR_TYPE_MAX_NUM];
        int loss[GUILD_WAR_TYPE_MAX_NUM];
    };
    
private:
    GuildData m_data;
    std::map<NFGUID, GuildMember> m_mapMembers;
    std::set<NFGUID> m_setOnlineMembers;
    
    int m_generalCount;
    int m_memberCountBonus;
    
    std::map<int, GuildWar> m_mapEnemyGuilds;
    std::map<int, DWORD> m_mapWarEndTimes;
    
    bool m_skillUsable[GUILD_SKILL_COUNT];
    
public:
    // Basic properties
    int GetGuildId() const;
    std::string GetName() const;
    NFGUID GetMasterGUID() const;
    int GetLevel() const;
    int GetExp() const;
    int GetGold() const;
    
    // Member management
    bool AddMember(NFCharacter* character, int grade = 15);
    bool RemoveMember(NFCharacter* character);
    bool IsMember(NFCharacter* character) const;
    GuildMember* GetMember(NFCharacter* character);
    
    // Master management
    NFCharacter* GetMaster() const;
    bool ChangeMaster(NFCharacter* newMaster);
    
    // Member count
    int GetMemberCount() const;
    int GetMaxMemberCount() const;
    int GetOnlineMemberCount() const;
    
    // Rank system
    bool ChangeMemberGrade(NFCharacter* character, int grade);
    bool ChangeMemberGeneral(NFCharacter* character, bool isGeneral);
    
    // EXP system
    bool OfferExp(NFCharacter* character, int amount);
    void LevelChange(NFCharacter* character, int level);
    
    // Guild skills
    int GetSkillLevel(int skillId) const;
    void SkillLevelUp(int skillId);
    bool UseSkill(int skillId, NFCharacter* user, NFCharacter* target);
    
    // Money system
    bool DepositMoney(NFCharacter* character, int amount);
    bool WithdrawMoney(NFCharacter* character, int amount);
    
    // War system
    bool CanStartWar(int guildId, int warType);
    bool DeclareWar(int guildId, int warType);
    bool IsAtWar(int guildId) const;
    void EndWar(int guildId);
    
    // Messaging
    void SendMessageToAll(const std::string& message);
    void SendMessageToOnline(const std::string& message);
    
    // Update
    void Update() override;
};
```

---

## 🛠️ Implementation Guide

### 📋 Phase 1: Foundation Setup (Week 1-2)

#### **1.1 Environment Setup**
```bash
# Clone NoahGameFrame
git clone https://github.com/youlostd/NoahGameFrame.git
cd NoahGameFrame

# Create plugin directory structure
mkdir -p plugins/NFGameLogicModule
mkdir -p plugins/NFCombatModule
mkdir -p plugins/NFQuestModule
mkdir -p plugins/NFGuildModule
```

#### **1.2 Core Wrapper Classes**
```cpp
// Create base wrapper class
class NFProjectAWrapper : public NFIObject
{
protected:
    // Common ProjectA integration methods
    virtual void InitializeProjectA() = 0;
    virtual void CleanupProjectA() = 0;
    virtual void UpdateProjectA() = 0;
};
```

#### **1.3 Character System Migration**
```cpp
// Implement NFCharacter class
class NFCharacter : public NFProjectAWrapper
{
private:
    std::unique_ptr<CHARACTER> m_pOldCharacter;
    
public:
    bool Initialize() override;
    void Shut() override;
    void Update() override;
    
    // Character-specific methods
    // ... (as shown in previous sections)
};
```

### 📋 Phase 2: Core Systems (Week 3-6)

#### **2.1 Item System Implementation**
```cpp
// Implement NFItem class
class NFItem : public NFProjectAWrapper
{
private:
    std::unique_ptr<CItem> m_pOldItem;
    
public:
    bool Initialize() override;
    void Shut() override;
    void Update() override;
    
    // Item-specific methods
    // ... (as shown in previous sections)
};
```

#### **2.2 Skill System Implementation**
```cpp
// Implement NFSkill class
class NFSkill : public NFProjectAWrapper
{
private:
    CSkillProto* m_pSkillProto;
    int m_iLevel;
    DWORD m_dwLastUseTime;
    
public:
    bool Initialize() override;
    void Shut() override;
    void Update() override;
    
    // Skill-specific methods
    // ... (as shown in previous sections)
};
```

#### **2.3 Battle System Implementation**
```cpp
// Implement NFBattleSystem module
class NFBattleSystem : public NFIModule
{
public:
    bool Initialize() override;
    void Shut() override;
    void Update() override;
    
    // Battle-specific methods
    // ... (as shown in previous sections)
};
```

### 📋 Phase 3: Social Systems (Week 7-10)

#### **3.1 Party System Implementation**
```cpp
// Implement NFParty and NFPartyManager
class NFParty : public NFProjectAWrapper
{
    // ... (as shown in previous sections)
};

class NFPartyManager : public NFIModule
{
    // ... (as shown in previous sections)
};
```

#### **3.2 Guild System Implementation**
```cpp
// Implement NFGuild and NFGuildManager
class NFGuild : public NFProjectAWrapper
{
    // ... (as shown in previous sections)
};

class NFGuildManager : public NFIModule
{
    // ... (as shown in previous sections)
};
```

### 📋 Phase 4: Advanced Systems (Week 11-14)

#### **4.1 Quest System Migration**
```cpp
// Implement NFQuest system
class NFQuest : public NFProjectAWrapper
{
private:
    std::unique_ptr<CQuest> m_pOldQuest;
    
public:
    // Quest-specific methods
    bool AcceptQuest(NFCharacter* character);
    bool CompleteQuest(NFCharacter* character);
    bool AbandonQuest(NFCharacter* character);
    // ... other quest methods
};
```

#### **4.2 Dungeon System Migration**
```cpp
// Implement NFDungeon system
class NFDungeon : public NFProjectAWrapper
{
private:
    std::unique_ptr<CDungeon> m_pOldDungeon;
    
public:
    // Dungeon-specific methods
    bool EnterDungeon(NFCharacter* character);
    bool ExitDungeon(NFCharacter* character);
    bool IsDungeonActive() const;
    // ... other dungeon methods
};
```

### 📋 Phase 5: Polish & Testing (Week 15-16)

#### **5.1 Performance Optimization**
```cpp
// Optimize update loops
void NFCharacter::Update()
{
    // Only update if character is active
    if (!IsActive()) return;
    
    // Update ProjectA character
    if (m_pOldCharacter)
    {
        m_pOldCharacter->Update();
    }
    
    // Update NoahGameFrame specific logic
    UpdateNoahGameFrame();
}
```

#### **5.2 Memory Management**
```cpp
// Proper cleanup in destructors
NFCharacter::~NFCharacter()
{
    if (m_pOldCharacter)
    {
        m_pOldCharacter->Destroy();
        m_pOldCharacter.reset();
    }
}
```

#### **5.3 Testing Framework**
```cpp
// Create test cases
class NFCharacterTest : public NFITest
{
public:
    void TestCharacterCreation();
    void TestCharacterCombat();
    void TestCharacterSkills();
    void TestCharacterItems();
    // ... other test methods
};
```

---

## 🔧 Troubleshooting

### ❌ Common Issues

#### **1. Memory Leaks**
```cpp
// Problem: ProjectA objects not properly cleaned up
// Solution: Use RAII and smart pointers
class NFCharacter
{
private:
    std::unique_ptr<CHARACTER> m_pOldCharacter;  // Automatic cleanup
public:
    ~NFCharacter()
    {
        if (m_pOldCharacter)
        {
            m_pOldCharacter->Destroy();
            m_pOldCharacter.reset();
        }
    }
};
```

#### **2. Circular Dependencies**
```cpp
// Problem: Circular includes between ProjectA and NoahGameFrame
// Solution: Use forward declarations and interfaces
class NFCharacter;  // Forward declaration
class NFItem;       // Forward declaration

class NFCharacter
{
    // Use pointers to avoid circular dependencies
    NFItem* GetEquippedItem(int slot) const;
};
```

#### **3. Thread Safety**
```cpp
// Problem: ProjectA code not thread-safe
// Solution: Add proper synchronization
class NFCharacter
{
private:
    std::mutex m_mutex;
    
public:
    void Update()
    {
        std::lock_guard<std::mutex> lock(m_mutex);
        if (m_pOldCharacter)
        {
            m_pOldCharacter->Update();
        }
    }
};
```

#### **4. Performance Issues**
```cpp
// Problem: Too many updates per frame
// Solution: Implement update batching
class NFCharacterManager
{
private:
    std::vector<NFCharacter*> m_updateQueue;
    int m_updateIndex = 0;
    
public:
    void Update()
    {
        // Update only a subset of characters per frame
        int batchSize = 100;
        int startIndex = m_updateIndex;
        int endIndex = std::min(startIndex + batchSize, (int)m_updateQueue.size());
        
        for (int i = startIndex; i < endIndex; ++i)
        {
            m_updateQueue[i]->Update();
        }
        
        m_updateIndex = endIndex % m_updateQueue.size();
    }
};
```

### 🐛 Debugging Tips

#### **1. Enable Debug Logging**
```cpp
// Add debug logging to track issues
void NFCharacter::Update()
{
    if (test_server)
    {
        sys_log(0, "NFCharacter::Update() - Character: %s", GetName().c_str());
    }
    
    if (m_pOldCharacter)
    {
        m_pOldCharacter->Update();
    }
}
```

#### **2. Use Assertions**
```cpp
// Add assertions to catch bugs early
void NFCharacter::SetHP(int hp)
{
    assert(hp >= 0 && hp <= GetMaxHP());
    if (m_pOldCharacter)
    {
        m_pOldCharacter->SetHP(hp);
    }
}
```

#### **3. Memory Debugging**
```cpp
// Use memory debugging tools
#ifdef _DEBUG
    // Enable memory leak detection
    _CrtSetDbgFlag(_CRTDBG_ALLOC_MEM_DF | _CRTDBG_LEAK_CHECK_DF);
#endif
```

---

## 🤝 Contributing

### 📝 How to Contribute

1. **Fork the repository**
2. **Create a feature branch**
3. **Make your changes**
4. **Add tests**
5. **Submit a pull request**

### 📋 Contribution Guidelines

- Follow the existing code style
- Add comprehensive comments
- Include unit tests for new features
- Update documentation
- Test on multiple platforms

### 🐛 Reporting Issues

When reporting issues, please include:
- NoahGameFrame version
- ProjectA version
- Operating system
- Compiler version
- Steps to reproduce
- Expected vs actual behavior
- Log files

---

## 📚 Additional Resources

### 🔗 Links

- [NoahGameFrame GitHub](https://github.com/youlostd/NoahGameFrame)
- [ProjectA Repository](https://github.com/AEldra/ProjectA-main)
- [C++ Documentation](https://en.cppreference.com/)
- [Game Development Resources](https://www.gamedev.net/)

### 📖 Documentation

- [NoahGameFrame Documentation](https://github.com/youlostd/NoahGameFrame/wiki)
- [ProjectA Documentation](https://github.com/AEldra/ProjectA-main/wiki)
- [Migration Examples](examples/)
- [API Reference](api/)

### 💬 Community

- [Discord Server](https://discord.gg/noahgameframe)
- [GitHub Discussions](https://github.com/youlostd/NoahGameFrame/discussions)
- [Reddit Community](https://reddit.com/r/NoahGameFrame)

---

## 📄 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

---

## 🙏 Acknowledgments

- **NoahGameFrame Team** - For creating an excellent game server framework
- **ProjectA Contributors** - For the comprehensive MMORPG server implementation
- **Community Contributors** - For their valuable feedback and contributions

---

*Last updated: December 2024*
*Version: 1.0.0*