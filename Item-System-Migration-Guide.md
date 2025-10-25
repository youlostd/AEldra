# 📦 ITEM System Migration Guide

## 📋 Overview

This guide provides detailed instructions for migrating ProjectA's ITEM system to NoahGameFrame. The ITEM system manages all in-game items, including equipment, consumables, quest items, and special items with complex attributes and socket systems.

## 🎯 Migration Goals

- **Preserve Item Logic**: Maintain all existing item mechanics and balance
- **Modernize Interface**: Use NoahGameFrame's object-oriented design
- **Improve Performance**: Leverage NoahGameFrame's optimized data structures
- **Enhance Maintainability**: Clean separation of item types and behaviors

## 🔍 Current ProjectA Structure

### **CItem Class Analysis**

```cpp
// ProjectA CItem class (item.h)
class CItem : public CEntity
{
    // Basic properties
    DWORD m_dwVnum;                    // Item number
    DWORD m_dwID;                      // Unique ID
    DWORD m_dwCount;                   // Quantity
    DWORD m_dwVID;                     // Virtual ID
    
    // Item properties
    long m_lFlag;                      // Item flags
    BYTE m_bWindow;                    // Window type (inventory, shop, etc.)
    
    // Socket system
    TPlayerItemAttribute m_aAttr[ITEM_ATTRIBUTE_MAX_NUM];
    TPlayerItemAttributeEx m_aAttrEx[ITEM_ATTRIBUTE_MAX_NUM];
    
    // Refine system
    BYTE m_bRefineLevel;               // Refine level
    DWORD m_dwRefineExp;               // Refine experience
    
    // Crystal system
    #ifdef CRYSTAL_SYSTEM
    DWORD m_dwCrystalTime;             // Crystal time
    BYTE m_bCrystalClarityType;        // Crystal clarity type
    BYTE m_bCrystalClarityLevel;       // Crystal clarity level
    #endif
    
    // Item prototype
    network::TItemTable* m_pProto;     // Item prototype data
    
    // Durability
    int m_iDurability;                 // Current durability
    int m_iMaxDurability;              // Maximum durability
    
    // Special properties
    DWORD m_dwMaskVnum;                // Masked vnum for display
    DWORD m_dwData;                    // Item data
    DWORD m_dwTransmutationVnum;       // Transmutation vnum
    
    // Timestamps
    DWORD m_dwCreateTime;              // Creation time
    DWORD m_dwLastUpdateTime;          // Last update time
};
```

### **Key Methods Analysis**

```cpp
// Core item methods
class CItem
{
public:
    // Lifecycle
    void Initialize();
    void Destroy();
    void Save();
    
    // Basic properties
    DWORD GetVnum() const;
    void SetVnum(DWORD vnum);
    DWORD GetID() const;
    void SetID(DWORD id);
    DWORD GetCount() const;
    bool SetCount(DWORD count);
    
    // Item type
    BYTE GetType() const;
    BYTE GetSubType() const;
    BYTE GetSize() const;
    
    // Item properties
    long GetFlag() const;
    void SetFlag(long flag);
    void AddFlag(long bit);
    void RemoveFlag(long bit);
    
    // Wear system
    DWORD GetWearFlag() const;
    DWORD GetAntiFlag() const;
    DWORD GetImmuneFlag() const;
    
    // Socket system
    int GetSocket(int index) const;
    void SetSocket(int index, int value);
    int GetAttribute(int index) const;
    void SetAttribute(int index, int value);
    
    // Refine system
    BYTE GetRefineLevel() const;
    void SetRefineLevel(BYTE level);
    DWORD GetRefineExp() const;
    void SetRefineExp(DWORD exp);
    
    // Durability
    int GetDurability() const;
    void SetDurability(int durability);
    int GetMaxDurability() const;
    void SetMaxDurability(int maxDurability);
    
    // Usage
    bool Use(LPCHARACTER user);
    bool CanUse(LPCHARACTER user) const;
    bool IsStackable() const;
    bool IsEquipable() const;
    
    // Display
    const char* GetName(BYTE languageId = LANGUAGE_DEFAULT) const;
    const char* GetBaseName() const;
    
    // Serialization
    void EncodeInsertPacket(LPENTITY entity);
    void EncodeRemovePacket(LPENTITY entity);
};
```

## 🚀 NoahGameFrame Migration

### **NFItem Class Design**

```cpp
// NoahGameFrame ITEM class
class NFItem : public NFIObject
{
private:
    // ProjectA item wrapper
    std::unique_ptr<CItem> m_pOldItem;
    
    // NoahGameFrame specific data
    NFGUID m_itemGUID;
    int m_vnum;
    int m_id;
    int m_count;
    int m_vid;
    
    // Item properties
    int m_flags;
    int m_windowType;
    int m_type;
    int m_subType;
    int m_size;
    
    // Socket system
    std::vector<int> m_sockets;
    std::vector<int> m_attributes;
    
    // Refine system
    int m_refineLevel;
    int m_refineExp;
    
    // Crystal system
    #ifdef CRYSTAL_SYSTEM
    int m_crystalTime;
    int m_crystalClarityType;
    int m_crystalClarityLevel;
    #endif
    
    // Durability
    int m_durability;
    int m_maxDurability;
    
    // Special properties
    int m_maskVnum;
    int m_data;
    int m_transmutationVnum;
    
    // Timestamps
    DWORD m_createTime;
    DWORD m_lastUpdateTime;
    
    // Item prototype
    ItemProto* m_pProto;
    
public:
    // Constructor/Destructor
    NFItem();
    virtual ~NFItem();
    
    // NFIObject interface
    bool Initialize() override;
    void Shut() override;
    void Update() override;
    
    // GUID management
    NFGUID GetGUID() const override;
    void SetGUID(const NFGUID& guid) override;
    
    // Basic properties
    int GetVnum() const;
    void SetVnum(int vnum);
    int GetID() const;
    void SetID(int id);
    int GetCount() const;
    bool SetCount(int count);
    int GetVID() const;
    void SetVID(int vid);
    
    // Item type
    int GetType() const;
    int GetSubType() const;
    int GetSize() const;
    
    // Item properties
    int GetFlags() const;
    void SetFlags(int flags);
    void AddFlag(int flag);
    void RemoveFlag(int flag);
    bool HasFlag(int flag) const;
    
    // Window type
    int GetWindowType() const;
    void SetWindowType(int windowType);
    
    // Wear system
    int GetWearFlag() const;
    int GetAntiFlag() const;
    int GetImmuneFlag() const;
    
    // Socket system
    int GetSocket(int index) const;
    void SetSocket(int index, int value);
    int GetSocketCount() const;
    void SetSocketCount(int count);
    
    // Attribute system
    int GetAttribute(int index) const;
    void SetAttribute(int index, int value);
    int GetAttributeCount() const;
    void SetAttributeCount(int count);
    
    // Refine system
    int GetRefineLevel() const;
    void SetRefineLevel(int level);
    int GetRefineExp() const;
    void SetRefineExp(int exp);
    bool CanRefine() const;
    bool Refine();
    
    // Crystal system
    #ifdef CRYSTAL_SYSTEM
    int GetCrystalTime() const;
    void SetCrystalTime(int time);
    int GetCrystalClarityType() const;
    void SetCrystalClarityType(int type);
    int GetCrystalClarityLevel() const;
    void SetCrystalClarityLevel(int level);
    bool IsCrystalActive() const;
    #endif
    
    // Durability
    int GetDurability() const;
    void SetDurability(int durability);
    int GetMaxDurability() const;
    void SetMaxDurability(int maxDurability);
    float GetDurabilityPercent() const;
    bool IsBroken() const;
    void Repair();
    
    // Special properties
    int GetMaskVnum() const;
    void SetMaskVnum(int vnum);
    int GetData() const;
    void SetData(int data);
    int GetTransmutationVnum() const;
    void SetTransmutationVnum(int vnum);
    
    // Display
    std::string GetName(int languageId = 0) const;
    std::string GetBaseName() const;
    std::string GetDescription(int languageId = 0) const;
    
    // Usage
    bool Use(NFCharacter* user);
    bool CanUse(NFCharacter* user) const;
    bool IsStackable() const;
    bool IsEquipable() const;
    bool IsConsumable() const;
    bool IsQuestItem() const;
    
    // Item prototype
    ItemProto* GetProto() const;
    void SetProto(ItemProto* proto);
    
    // Timestamps
    DWORD GetCreateTime() const;
    void SetCreateTime(DWORD time);
    DWORD GetLastUpdateTime() const;
    void SetLastUpdateTime(DWORD time);
    
    // Serialization
    void Serialize(NFDataList& dataList) const override;
    void Deserialize(const NFDataList& dataList) override;
    
    // ProjectA integration
    CItem* GetProjectAItem() const;
    void SyncFromProjectA();
    void SyncToProjectA();
    
private:
    // Internal methods
    void InitializeProjectA();
    void CleanupProjectA();
    void UpdateProjectA();
    void UpdateNoahGameFrame();
    
    // Helper methods
    bool ValidateUser(NFCharacter* user) const;
    bool ValidateCount(int count) const;
    void ProcessItemUse(NFCharacter* user);
    void ProcessItemEquip(NFCharacter* user);
    void ProcessItemConsume(NFCharacter* user);
    void ProcessItemQuest(NFCharacter* user);
    void UpdateDurability();
    void UpdateCrystal();
    void UpdateRefine();
};
```

### **NFItemManager Class**

```cpp
// Item manager for NoahGameFrame
class NFItemManager : public NFIModule
{
private:
    // Item storage
    std::map<NFGUID, NFItem*> m_mapItems;
    std::map<int, std::vector<NFItem*>> m_mapItemsByVnum;
    
    // Item prototypes
    std::map<int, ItemProto*> m_mapItemProtos;
    
    // Update management
    std::vector<NFItem*> m_updateQueue;
    int m_updateIndex;
    DWORD m_lastUpdateTime;
    
    // ProjectA integration
    ITEM_MANAGER* m_pProjectAManager;
    
public:
    // NFIModule interface
    bool Initialize() override;
    void Shut() override;
    void Update() override;
    
    // Item management
    NFItem* CreateItem(int vnum, int count = 1);
    void DestroyItem(NFItem* item);
    NFItem* GetItem(const NFGUID& guid) const;
    std::vector<NFItem*> GetItemsByVnum(int vnum) const;
    
    // Item prototype management
    bool LoadItemProtos();
    ItemProto* GetItemProto(int vnum) const;
    bool AddItemProto(ItemProto* proto);
    void RemoveItemProto(int vnum);
    
    // Item queries
    std::vector<NFItem*> GetItemsInWindow(int windowType) const;
    std::vector<NFItem*> GetEquippedItems(NFCharacter* character) const;
    std::vector<NFItem*> GetInventoryItems(NFCharacter* character) const;
    
    // Item operations
    bool MoveItem(NFItem* item, int fromWindow, int toWindow, int fromSlot, int toSlot);
    bool SplitItem(NFItem* item, int count);
    bool MergeItems(NFItem* item1, NFItem* item2);
    bool StackItems(NFItem* item1, NFItem* item2);
    
    // Item creation
    NFItem* CreateRandomItem(int vnum, int count = 1);
    NFItem* CreateRefinedItem(int vnum, int refineLevel, int count = 1);
    NFItem* CreateSocketedItem(int vnum, const std::vector<int>& sockets, int count = 1);
    
    // Item validation
    bool ValidateItem(NFItem* item) const;
    bool ValidateItemUse(NFItem* item, NFCharacter* user) const;
    bool ValidateItemEquip(NFItem* item, NFCharacter* user, int slot) const;
    
    // Update management
    void AddToUpdateQueue(NFItem* item);
    void RemoveFromUpdateQueue(NFItem* item);
    void ProcessUpdateQueue();
    
    // ProjectA integration
    void SyncFromProjectA();
    void SyncToProjectA();
    ITEM_MANAGER* GetProjectAManager() const;
    
    // Statistics
    int GetItemCount() const;
    int GetItemCountByVnum(int vnum) const;
    int GetItemCountInWindow(int windowType) const;
    
private:
    // Internal methods
    void InitializeProjectA();
    void CleanupProjectA();
    void UpdateProjectA();
    void UpdateNoahGameFrame();
    
    // Helper methods
    bool ValidateItemData(NFItem* item) const;
    void ProcessItemUpdates();
    void ProcessItemDurability();
    void ProcessItemCrystal();
    void ProcessItemRefine();
    void ProcessItemTimers();
};
```

## 🔧 Implementation Steps

### **Step 1: Create ItemProto Class**

```cpp
// Item prototype class
class ItemProto
{
public:
    int vnum;
    std::string name;
    std::string description;
    int type;
    int subType;
    int size;
    int flags;
    int wearFlag;
    int antiFlag;
    int immuneFlag;
    int level;
    int minLevel;
    int maxLevel;
    int price;
    int sellPrice;
    int durability;
    int maxDurability;
    int socketCount;
    int attributeCount;
    int refineLevel;
    int refineExp;
    int crystalTime;
    int crystalClarityType;
    int crystalClarityLevel;
    int transmutationVnum;
    int data;
    
    // Constructor
    ItemProto()
        : vnum(0)
        , type(0)
        , subType(0)
        , size(0)
        , flags(0)
        , wearFlag(0)
        , antiFlag(0)
        , immuneFlag(0)
        , level(0)
        , minLevel(0)
        , maxLevel(0)
        , price(0)
        , sellPrice(0)
        , durability(0)
        , maxDurability(0)
        , socketCount(0)
        , attributeCount(0)
        , refineLevel(0)
        , refineExp(0)
        , crystalTime(0)
        , crystalClarityType(0)
        , crystalClarityLevel(0)
        , transmutationVnum(0)
        , data(0)
    {
    }
    
    // Validation
    bool IsValid() const
    {
        return vnum > 0 && !name.empty();
    }
    
    // Serialization
    void Serialize(NFDataList& dataList) const;
    void Deserialize(const NFDataList& dataList);
};
```

### **Step 2: Implement NFItem Class**

```cpp
// NFItem implementation
class NFItem : public NFProjectAWrapper
{
public:
    NFItem()
        : m_pOldItem(nullptr)
        , m_vnum(0)
        , m_id(0)
        , m_count(1)
        , m_vid(0)
        , m_flags(0)
        , m_windowType(0)
        , m_type(0)
        , m_subType(0)
        , m_size(0)
        , m_refineLevel(0)
        , m_refineExp(0)
        , m_durability(0)
        , m_maxDurability(0)
        , m_maskVnum(0)
        , m_data(0)
        , m_transmutationVnum(0)
        , m_createTime(0)
        , m_lastUpdateTime(0)
        , m_pProto(nullptr)
    {
    }
    
    virtual ~NFItem()
    {
        CleanupProjectA();
    }
    
    bool Initialize() override
    {
        // Initialize NoahGameFrame specific data
        m_itemGUID = NFGUID::CreateGUID();
        m_createTime = GetTickCount();
        m_lastUpdateTime = m_createTime;
        
        // Initialize ProjectA item
        InitializeProjectA();
        
        return true;
    }
    
    void Shut() override
    {
        // Cleanup NoahGameFrame specific data
        m_itemGUID = NFGUID::NULL_OBJECT;
        m_sockets.clear();
        m_attributes.clear();
        
        // Cleanup ProjectA item
        CleanupProjectA();
    }
    
    void Update() override
    {
        // Update ProjectA item
        UpdateProjectA();
        
        // Update NoahGameFrame specific logic
        UpdateNoahGameFrame();
    }
    
    // Basic properties
    int GetVnum() const
    {
        return m_vnum;
    }
    
    void SetVnum(int vnum)
    {
        m_vnum = vnum;
        if (m_pOldItem)
        {
            m_pOldItem->SetVnum(vnum);
        }
    }
    
    int GetID() const
    {
        return m_id;
    }
    
    void SetID(int id)
    {
        m_id = id;
        if (m_pOldItem)
        {
            m_pOldItem->SetID(id);
        }
    }
    
    int GetCount() const
    {
        return m_count;
    }
    
    bool SetCount(int count)
    {
        if (count < 0 || count > GetMaxCount())
        {
            return false;
        }
        
        m_count = count;
        if (m_pOldItem)
        {
            return m_pOldItem->SetCount(count);
        }
        return true;
    }
    
    // Item type
    int GetType() const
    {
        return m_type;
    }
    
    int GetSubType() const
    {
        return m_subType;
    }
    
    int GetSize() const
    {
        return m_size;
    }
    
    // Item properties
    int GetFlags() const
    {
        return m_flags;
    }
    
    void SetFlags(int flags)
    {
        m_flags = flags;
        if (m_pOldItem)
        {
            m_pOldItem->SetFlag(flags);
        }
    }
    
    void AddFlag(int flag)
    {
        m_flags |= flag;
        if (m_pOldItem)
        {
            m_pOldItem->AddFlag(flag);
        }
    }
    
    void RemoveFlag(int flag)
    {
        m_flags &= ~flag;
        if (m_pOldItem)
        {
            m_pOldItem->RemoveFlag(flag);
        }
    }
    
    bool HasFlag(int flag) const
    {
        return (m_flags & flag) != 0;
    }
    
    // Socket system
    int GetSocket(int index) const
    {
        if (index < 0 || index >= (int)m_sockets.size())
        {
            return 0;
        }
        return m_sockets[index];
    }
    
    void SetSocket(int index, int value)
    {
        if (index < 0 || index >= (int)m_sockets.size())
        {
            return;
        }
        m_sockets[index] = value;
        if (m_pOldItem)
        {
            m_pOldItem->SetSocket(index, value);
        }
    }
    
    int GetSocketCount() const
    {
        return (int)m_sockets.size();
    }
    
    void SetSocketCount(int count)
    {
        m_sockets.resize(count, 0);
        if (m_pOldItem)
        {
            // Update ProjectA socket count
            for (int i = 0; i < count; ++i)
            {
                m_pOldItem->SetSocket(i, m_sockets[i]);
            }
        }
    }
    
    // Attribute system
    int GetAttribute(int index) const
    {
        if (index < 0 || index >= (int)m_attributes.size())
        {
            return 0;
        }
        return m_attributes[index];
    }
    
    void SetAttribute(int index, int value)
    {
        if (index < 0 || index >= (int)m_attributes.size())
        {
            return;
        }
        m_attributes[index] = value;
        if (m_pOldItem)
        {
            m_pOldItem->SetAttribute(index, value);
        }
    }
    
    int GetAttributeCount() const
    {
        return (int)m_attributes.size();
    }
    
    void SetAttributeCount(int count)
    {
        m_attributes.resize(count, 0);
        if (m_pOldItem)
        {
            // Update ProjectA attribute count
            for (int i = 0; i < count; ++i)
            {
                m_pOldItem->SetAttribute(i, m_attributes[i]);
            }
        }
    }
    
    // Refine system
    int GetRefineLevel() const
    {
        return m_refineLevel;
    }
    
    void SetRefineLevel(int level)
    {
        m_refineLevel = level;
        if (m_pOldItem)
        {
            m_pOldItem->SetRefineLevel(level);
        }
    }
    
    int GetRefineExp() const
    {
        return m_refineExp;
    }
    
    void SetRefineExp(int exp)
    {
        m_refineExp = exp;
        if (m_pOldItem)
        {
            m_pOldItem->SetRefineExp(exp);
        }
    }
    
    bool CanRefine() const
    {
        if (!m_pProto)
        {
            return false;
        }
        return m_refineLevel < m_pProto->refineLevel && m_refineExp >= GetRequiredRefineExp();
    }
    
    bool Refine()
    {
        if (!CanRefine())
        {
            return false;
        }
        
        // Refine logic here
        m_refineLevel++;
        m_refineExp -= GetRequiredRefineExp();
        
        if (m_pOldItem)
        {
            m_pOldItem->SetRefineLevel(m_refineLevel);
            m_pOldItem->SetRefineExp(m_refineExp);
        }
        
        return true;
    }
    
    // Durability
    int GetDurability() const
    {
        return m_durability;
    }
    
    void SetDurability(int durability)
    {
        m_durability = std::max(0, std::min(durability, m_maxDurability));
        if (m_pOldItem)
        {
            m_pOldItem->SetDurability(m_durability);
        }
    }
    
    int GetMaxDurability() const
    {
        return m_maxDurability;
    }
    
    void SetMaxDurability(int maxDurability)
    {
        m_maxDurability = maxDurability;
        if (m_pOldItem)
        {
            m_pOldItem->SetMaxDurability(maxDurability);
        }
    }
    
    float GetDurabilityPercent() const
    {
        if (m_maxDurability <= 0)
        {
            return 1.0f;
        }
        return (float)m_durability / (float)m_maxDurability;
    }
    
    bool IsBroken() const
    {
        return m_durability <= 0;
    }
    
    void Repair()
    {
        m_durability = m_maxDurability;
        if (m_pOldItem)
        {
            m_pOldItem->SetDurability(m_durability);
        }
    }
    
    // Usage
    bool Use(NFCharacter* user)
    {
        if (!CanUse(user))
        {
            return false;
        }
        
        ProcessItemUse(user);
        return true;
    }
    
    bool CanUse(NFCharacter* user) const
    {
        if (!user || !ValidateUser(user))
        {
            return false;
        }
        
        // Check level requirements
        if (m_pProto && user->GetLevel() < m_pProto->minLevel)
        {
            return false;
        }
        
        // Check item type specific requirements
        if (IsEquipable())
        {
            return ValidateItemEquip(user);
        }
        else if (IsConsumable())
        {
            return ValidateItemConsume(user);
        }
        else if (IsQuestItem())
        {
            return ValidateItemQuest(user);
        }
        
        return true;
    }
    
    bool IsStackable() const
    {
        return HasFlag(ITEM_FLAG_STACKABLE);
    }
    
    bool IsEquipable() const
    {
        return m_pProto && m_pProto->wearFlag != 0;
    }
    
    bool IsConsumable() const
    {
        return m_pProto && m_pProto->type == ITEM_TYPE_USE;
    }
    
    bool IsQuestItem() const
    {
        return m_pProto && m_pProto->type == ITEM_TYPE_QUEST;
    }
    
    // Display
    std::string GetName(int languageId = 0) const
    {
        if (m_pProto)
        {
            return m_pProto->name;
        }
        return "Unknown Item";
    }
    
    std::string GetBaseName() const
    {
        if (m_pProto)
        {
            return m_pProto->name;
        }
        return "Unknown Item";
    }
    
    std::string GetDescription(int languageId = 0) const
    {
        if (m_pProto)
        {
            return m_pProto->description;
        }
        return "";
    }
    
    // Serialization
    void Serialize(NFDataList& dataList) const override
    {
        dataList.AddInt(m_vnum);
        dataList.AddInt(m_id);
        dataList.AddInt(m_count);
        dataList.AddInt(m_vid);
        dataList.AddInt(m_flags);
        dataList.AddInt(m_windowType);
        dataList.AddInt(m_type);
        dataList.AddInt(m_subType);
        dataList.AddInt(m_size);
        dataList.AddInt(m_refineLevel);
        dataList.AddInt(m_refineExp);
        dataList.AddInt(m_durability);
        dataList.AddInt(m_maxDurability);
        dataList.AddInt(m_maskVnum);
        dataList.AddInt(m_data);
        dataList.AddInt(m_transmutationVnum);
        dataList.AddInt(m_createTime);
        dataList.AddInt(m_lastUpdateTime);
        
        // Serialize sockets
        dataList.AddInt((int)m_sockets.size());
        for (int socket : m_sockets)
        {
            dataList.AddInt(socket);
        }
        
        // Serialize attributes
        dataList.AddInt((int)m_attributes.size());
        for (int attribute : m_attributes)
        {
            dataList.AddInt(attribute);
        }
    }
    
    void Deserialize(const NFDataList& dataList) override
    {
        m_vnum = dataList.Int(0);
        m_id = dataList.Int(1);
        m_count = dataList.Int(2);
        m_vid = dataList.Int(3);
        m_flags = dataList.Int(4);
        m_windowType = dataList.Int(5);
        m_type = dataList.Int(6);
        m_subType = dataList.Int(7);
        m_size = dataList.Int(8);
        m_refineLevel = dataList.Int(9);
        m_refineExp = dataList.Int(10);
        m_durability = dataList.Int(11);
        m_maxDurability = dataList.Int(12);
        m_maskVnum = dataList.Int(13);
        m_data = dataList.Int(14);
        m_transmutationVnum = dataList.Int(15);
        m_createTime = dataList.Int(16);
        m_lastUpdateTime = dataList.Int(17);
        
        // Deserialize sockets
        int socketCount = dataList.Int(18);
        m_sockets.clear();
        for (int i = 0; i < socketCount; ++i)
        {
            m_sockets.push_back(dataList.Int(19 + i));
        }
        
        // Deserialize attributes
        int attributeCount = dataList.Int(19 + socketCount);
        m_attributes.clear();
        for (int i = 0; i < attributeCount; ++i)
        {
            m_attributes.push_back(dataList.Int(20 + socketCount + i));
        }
    }
    
    // ProjectA integration
    CItem* GetProjectAItem() const
    {
        return m_pOldItem.get();
    }
    
    void SyncFromProjectA()
    {
        if (!m_pOldItem)
        {
            return;
        }
        
        m_vnum = m_pOldItem->GetVnum();
        m_id = m_pOldItem->GetID();
        m_count = m_pOldItem->GetCount();
        m_vid = m_pOldItem->GetVID();
        m_flags = m_pOldItem->GetFlag();
        m_windowType = m_pOldItem->GetWindow();
        m_type = m_pOldItem->GetType();
        m_subType = m_pOldItem->GetSubType();
        m_size = m_pOldItem->GetSize();
        m_refineLevel = m_pOldItem->GetRefineLevel();
        m_refineExp = m_pOldItem->GetRefineExp();
        m_durability = m_pOldItem->GetDurability();
        m_maxDurability = m_pOldItem->GetMaxDurability();
        
        // Sync sockets
        for (int i = 0; i < ITEM_ATTRIBUTE_MAX_NUM; ++i)
        {
            if (i < (int)m_sockets.size())
            {
                m_sockets[i] = m_pOldItem->GetSocket(i);
            }
        }
        
        // Sync attributes
        for (int i = 0; i < ITEM_ATTRIBUTE_MAX_NUM; ++i)
        {
            if (i < (int)m_attributes.size())
            {
                m_attributes[i] = m_pOldItem->GetAttribute(i);
            }
        }
    }
    
    void SyncToProjectA()
    {
        if (!m_pOldItem)
        {
            return;
        }
        
        m_pOldItem->SetVnum(m_vnum);
        m_pOldItem->SetID(m_id);
        m_pOldItem->SetCount(m_count);
        m_pOldItem->SetVID(m_vid);
        m_pOldItem->SetFlag(m_flags);
        m_pOldItem->SetWindow(m_windowType);
        m_pOldItem->SetRefineLevel(m_refineLevel);
        m_pOldItem->SetRefineExp(m_refineExp);
        m_pOldItem->SetDurability(m_durability);
        m_pOldItem->SetMaxDurability(m_maxDurability);
        
        // Sync sockets
        for (int i = 0; i < (int)m_sockets.size() && i < ITEM_ATTRIBUTE_MAX_NUM; ++i)
        {
            m_pOldItem->SetSocket(i, m_sockets[i]);
        }
        
        // Sync attributes
        for (int i = 0; i < (int)m_attributes.size() && i < ITEM_ATTRIBUTE_MAX_NUM; ++i)
        {
            m_pOldItem->SetAttribute(i, m_attributes[i]);
        }
    }
    
private:
    // Internal methods
    void InitializeProjectA()
    {
        // Create ProjectA item
        m_pOldItem = std::make_unique<CItem>(m_vnum);
        if (m_pOldItem)
        {
            m_pOldItem->Initialize();
            m_bProjectAInitialized = true;
        }
    }
    
    void CleanupProjectA()
    {
        if (m_pOldItem)
        {
            m_pOldItem->Destroy();
            m_pOldItem.reset();
            m_bProjectAInitialized = false;
        }
    }
    
    void UpdateProjectA()
    {
        if (m_pOldItem && m_bProjectAInitialized)
        {
            m_pOldItem->Update();
        }
    }
    
    void UpdateNoahGameFrame()
    {
        // Update NoahGameFrame specific logic
        UpdateDurability();
        UpdateCrystal();
        UpdateRefine();
    }
    
    // Helper methods
    bool ValidateUser(NFCharacter* user) const
    {
        return user != nullptr && user->IsAlive();
    }
    
    bool ValidateCount(int count) const
    {
        return count > 0 && count <= GetMaxCount();
    }
    
    int GetMaxCount() const
    {
        if (m_pProto)
        {
            return m_pProto->maxCount;
        }
        return 1;
    }
    
    int GetRequiredRefineExp() const
    {
        if (m_pProto)
        {
            return m_pProto->refineExp;
        }
        return 0;
    }
    
    bool ValidateItemEquip(NFCharacter* user) const
    {
        // Check level requirements
        if (m_pProto && user->GetLevel() < m_pProto->minLevel)
        {
            return false;
        }
        
        // Check class requirements
        if (m_pProto && !CheckClassRequirement(user))
        {
            return false;
        }
        
        return true;
    }
    
    bool ValidateItemConsume(NFCharacter* user) const
    {
        // Check if item can be consumed
        if (!IsConsumable())
        {
            return false;
        }
        
        // Check cooldown
        if (IsOnCooldown())
        {
            return false;
        }
        
        return true;
    }
    
    bool ValidateItemQuest(NFCharacter* user) const
    {
        // Check if user has the quest
        if (!user->HasQuest(m_vnum))
        {
            return false;
        }
        
        return true;
    }
    
    bool CheckClassRequirement(NFCharacter* user) const
    {
        if (!m_pProto)
        {
            return true;
        }
        
        // Check class requirements here
        // This would need to be implemented based on ProjectA's class system
        return true;
    }
    
    bool IsOnCooldown() const
    {
        DWORD currentTime = GetTickCount();
        return (currentTime - m_lastUpdateTime) < ITEM_USE_COOLDOWN;
    }
    
    void ProcessItemUse(NFCharacter* user)
    {
        if (IsEquipable())
        {
            ProcessItemEquip(user);
        }
        else if (IsConsumable())
        {
            ProcessItemConsume(user);
        }
        else if (IsQuestItem())
        {
            ProcessItemQuest(user);
        }
        
        m_lastUpdateTime = GetTickCount();
    }
    
    void ProcessItemEquip(NFCharacter* user)
    {
        // Equip item logic
        user->EquipItem(this, GetEquipSlot());
    }
    
    void ProcessItemConsume(NFCharacter* user)
    {
        // Consume item logic
        if (m_count > 1)
        {
            SetCount(m_count - 1);
        }
        else
        {
            // Item is consumed, remove it
            user->RemoveItem(this);
        }
    }
    
    void ProcessItemQuest(NFCharacter* user)
    {
        // Quest item logic
        user->UseQuestItem(this);
    }
    
    int GetEquipSlot() const
    {
        if (!m_pProto)
        {
            return -1;
        }
        
        // Determine equip slot based on wear flag
        // This would need to be implemented based on ProjectA's equip system
        return 0;
    }
    
    void UpdateDurability()
    {
        // Update durability based on usage
        // This would need to be implemented based on ProjectA's durability system
    }
    
    void UpdateCrystal()
    {
        #ifdef CRYSTAL_SYSTEM
        // Update crystal system
        // This would need to be implemented based on ProjectA's crystal system
        #endif
    }
    
    void UpdateRefine()
    {
        // Update refine system
        // This would need to be implemented based on ProjectA's refine system
    }
};
```

## 🧪 Testing

### **Unit Tests**

```cpp
// Item system unit tests
class NFItemTest : public NFITest
{
public:
    void TestItemCreation()
    {
        NFItemManager* manager = new NFItemManager();
        manager->Initialize();
        
        NFItem* item = manager->CreateItem(1001, 1); // Create a test item
        ASSERT_TRUE(item != nullptr);
        ASSERT_EQ(item->GetVnum(), 1001);
        ASSERT_EQ(item->GetCount(), 1);
        ASSERT_EQ(item->GetType(), ITEM_TYPE_WEAPON);
        
        manager->DestroyItem(item);
        manager->Shut();
        delete manager;
    }
    
    void TestItemProperties()
    {
        NFItemManager* manager = new NFItemManager();
        manager->Initialize();
        
        NFItem* item = manager->CreateItem(1001, 1);
        ASSERT_TRUE(item != nullptr);
        
        // Test basic properties
        item->SetCount(5);
        ASSERT_EQ(item->GetCount(), 5);
        
        item->SetRefineLevel(3);
        ASSERT_EQ(item->GetRefineLevel(), 3);
        
        item->SetDurability(80);
        ASSERT_EQ(item->GetDurability(), 80);
        
        manager->DestroyItem(item);
        manager->Shut();
        delete manager;
    }
    
    void TestItemSockets()
    {
        NFItemManager* manager = new NFItemManager();
        manager->Initialize();
        
        NFItem* item = manager->CreateItem(1001, 1);
        ASSERT_TRUE(item != nullptr);
        
        // Test socket system
        item->SetSocketCount(3);
        ASSERT_EQ(item->GetSocketCount(), 3);
        
        item->SetSocket(0, 1001);
        item->SetSocket(1, 1002);
        item->SetSocket(2, 1003);
        
        ASSERT_EQ(item->GetSocket(0), 1001);
        ASSERT_EQ(item->GetSocket(1), 1002);
        ASSERT_EQ(item->GetSocket(2), 1003);
        
        manager->DestroyItem(item);
        manager->Shut();
        delete manager;
    }
    
    void TestItemAttributes()
    {
        NFItemManager* manager = new NFItemManager();
        manager->Initialize();
        
        NFItem* item = manager->CreateItem(1001, 1);
        ASSERT_TRUE(item != nullptr);
        
        // Test attribute system
        item->SetAttributeCount(5);
        ASSERT_EQ(item->GetAttributeCount(), 5);
        
        item->SetAttribute(0, 10);
        item->SetAttribute(1, 20);
        item->SetAttribute(2, 30);
        
        ASSERT_EQ(item->GetAttribute(0), 10);
        ASSERT_EQ(item->GetAttribute(1), 20);
        ASSERT_EQ(item->GetAttribute(2), 30);
        
        manager->DestroyItem(item);
        manager->Shut();
        delete manager;
    }
    
    void TestItemUsage()
    {
        NFItemManager* manager = new NFItemManager();
        manager->Initialize();
        
        NFItem* item = manager->CreateItem(1001, 1);
        ASSERT_TRUE(item != nullptr);
        
        // Test item usage
        NFCharacter* character = CreateTestCharacter();
        ASSERT_TRUE(character != nullptr);
        
        bool useResult = item->Use(character);
        ASSERT_TRUE(useResult);
        
        manager->DestroyItem(item);
        manager->Shut();
        delete manager;
    }
};
```

### **Integration Tests**

```cpp
// Item system integration tests
class NFItemIntegrationTest : public NFITest
{
public:
    void TestItemManagerIntegration()
    {
        NFItemManager* manager = new NFItemManager();
        manager->Initialize();
        
        // Create multiple items
        std::vector<NFItem*> items;
        for (int i = 0; i < 100; ++i)
        {
            NFItem* item = manager->CreateItem(1001 + i, 1);
            ASSERT_TRUE(item != nullptr);
            items.push_back(item);
        }
        
        // Test item queries
        ASSERT_EQ(manager->GetItemCount(), 100);
        
        // Test item updates
        for (int i = 0; i < 1000; ++i)
        {
            manager->Update();
        }
        
        // Cleanup
        for (NFItem* item : items)
        {
            manager->DestroyItem(item);
        }
        manager->Shut();
        delete manager;
    }
    
    void TestItemPrototypeIntegration()
    {
        NFItemManager* manager = new NFItemManager();
        manager->Initialize();
        
        // Load item prototypes
        bool loadResult = manager->LoadItemProtos();
        ASSERT_TRUE(loadResult);
        
        // Test item prototype queries
        ItemProto* proto = manager->GetItemProto(1001);
        ASSERT_TRUE(proto != nullptr);
        ASSERT_EQ(proto->vnum, 1001);
        
        manager->Shut();
        delete manager;
    }
};
```

## 📊 Performance Considerations

### **Memory Management**

```cpp
// Optimized item memory management
class NFItem
{
private:
    // Use object pooling for frequently created/destroyed items
    static std::queue<NFItem*> s_itemPool;
    static std::mutex s_poolMutex;
    
public:
    static NFItem* CreateFromPool()
    {
        std::lock_guard<std::mutex> lock(s_poolMutex);
        if (s_itemPool.empty())
        {
            return new NFItem();
        }
        
        NFItem* item = s_itemPool.front();
        s_itemPool.pop();
        return item;
    }
    
    static void ReturnToPool(NFItem* item)
    {
        if (!item) return;
        
        std::lock_guard<std::mutex> lock(s_poolMutex);
        item->Reset();
        s_itemPool.push(item);
    }
    
private:
    void Reset()
    {
        // Reset all item data
        m_vnum = 0;
        m_id = 0;
        m_count = 1;
        m_vid = 0;
        m_flags = 0;
        m_windowType = 0;
        m_type = 0;
        m_subType = 0;
        m_size = 0;
        m_refineLevel = 0;
        m_refineExp = 0;
        m_durability = 0;
        m_maxDurability = 0;
        m_maskVnum = 0;
        m_data = 0;
        m_transmutationVnum = 0;
        m_createTime = 0;
        m_lastUpdateTime = 0;
        m_pProto = nullptr;
        
        m_sockets.clear();
        m_attributes.clear();
    }
};
```

### **Update Optimization**

```cpp
// Optimized item update
void NFItem::Update()
{
    // Only update if item needs updating
    if (!NeedsUpdate())
    {
        return;
    }
    
    // Update ProjectA item
    UpdateProjectA();
    
    // Update NoahGameFrame specific logic
    UpdateNoahGameFrame();
    
    // Mark as updated
    m_lastUpdateTime = GetTickCount();
}

bool NFItem::NeedsUpdate() const
{
    DWORD currentTime = GetTickCount();
    return (currentTime - m_lastUpdateTime) >= ITEM_UPDATE_INTERVAL;
}
```

### **Serialization Optimization**

```cpp
// Optimized item serialization
void NFItem::Serialize(NFDataList& dataList) const
{
    // Use bit packing for flags
    dataList.AddInt(m_vnum);
    dataList.AddInt(m_id);
    dataList.AddInt(m_count);
    dataList.AddInt(m_vid);
    dataList.AddInt(m_flags);
    dataList.AddInt(m_windowType);
    dataList.AddInt(m_type);
    dataList.AddInt(m_subType);
    dataList.AddInt(m_size);
    dataList.AddInt(m_refineLevel);
    dataList.AddInt(m_refineExp);
    dataList.AddInt(m_durability);
    dataList.AddInt(m_maxDurability);
    dataList.AddInt(m_maskVnum);
    dataList.AddInt(m_data);
    dataList.AddInt(m_transmutationVnum);
    dataList.AddInt(m_createTime);
    dataList.AddInt(m_lastUpdateTime);
    
    // Pack sockets and attributes efficiently
    int socketCount = (int)m_sockets.size();
    int attributeCount = (int)m_attributes.size();
    
    dataList.AddInt(socketCount);
    for (int i = 0; i < socketCount; ++i)
    {
        dataList.AddInt(m_sockets[i]);
    }
    
    dataList.AddInt(attributeCount);
    for (int i = 0; i < attributeCount; ++i)
    {
        dataList.AddInt(m_attributes[i]);
    }
}
```

## 🔧 Troubleshooting

### **Common Issues**

1. **Memory Leaks**: Ensure proper cleanup in destructors and use object pooling
2. **Performance Issues**: Implement update batching and optimization
3. **Serialization Errors**: Validate data before serialization
4. **Socket/Attribute Mismatches**: Ensure consistent indexing

### **Debug Tips**

1. **Enable Logging**: Add debug logging to track item operations
2. **Use Assertions**: Add assertions to catch bugs early
3. **Memory Debugging**: Use memory debugging tools
4. **Profile Performance**: Use profiling tools to identify bottlenecks

---

*This guide provides a comprehensive approach to migrating ProjectA's ITEM system to NoahGameFrame while maintaining all existing functionality and improving performance.*