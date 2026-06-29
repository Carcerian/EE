# `x0_i0_treasure.nss`

Source: `NSS/x0_/x0_i0_treasure.nss`  
49 functions · 30 constants

## Constants

| Constant | Type | Value | Note |
|---|---|---|---|
| `BK_CHANCE_OF_N0_MONSTERTREASURE` | int | `80` |  |
| `sModContLow` | string | `"X0_MOD_TREASURE_LOW"` |  |
| `sModContMed` | string | `"X0_MOD_TREASURE_MED"` |  |
| `sModContHigh` | string | `"X0_MOD_TREASURE_HIGH"` |  |
| `sModContUniq` | string | `"X0_MOD_TREASURE_UNIQ"` |  |
| `sContLow` | string | `"X0_TREASURE_LOW"` |  |
| `sContMed` | string | `"X0_TREASURE_MED"` |  |
| `sContHigh` | string | `"X0_TREASURE_HIGH"` |  |
| `sContUniq` | string | `"X0_TREASURE_UNIQ"` |  |
| `sContMonster` | string | `"X0_TREASURE_MONSTER"` |  |
| `sGoldResRef` | string | `"NW_IT_GOLD001"` |  |
| `sNumTreasureItemsVarname` | string | `"X0_NUM_TREASURE_ITEMS"` |  |
| `sBaseTypeVarname` | string | `"X0_BASE_TYPE_TREASURE"` |  |
| `sTreasureItemVarname` | string | `"X0_TREASURE_ITEM"` |  |
| `sTreasureGeneratedVarname` | string | `"X0_TREASURE_HAS_BEEN_GENERATED"` |  |
| `TREASURE_TYPE_LOW` | int | `1` |  |
| `TREASURE_TYPE_MED` | int | `2` |  |
| `TREASURE_TYPE_HIGH` | int | `3` |  |
| `TREASURE_TYPE_UNIQUE` | int | `4` |  |
| `TREASURE_TYPE_MONSTER` | int | `5` |  |
| `TREASURE_BASE_TYPE_WEAPON` | int | `13000` |  |
| `TREASURE_BASE_TYPE_WEAPON_NOAMMO` | int | `13001` |  |
| `TREASURE_BASE_TYPE_WEAPON_RANGED` | int | `13002` |  |
| `TREASURE_BASE_TYPE_WEAPON_MELEE` | int | `13003` |  |
| `TREASURE_BASE_TYPE_ARMOR` | int | `13004` |  |
| `TREASURE_BASE_TYPE_CLOTHING` | int | `13005` |  |
| `TREASURE_PROBABILITY_1` | int | `70` |  |
| `TREASURE_PROBABILITY_2` | int | `20` |  |
| `TREASURE_GOLD_PROBABILITY` | int | `35` |  |
| `X0_GOLD_MODIFIER` | float | `0.50` |  |

## Functions

#### `int CTG_GetNumItems()`
> Get the number of items to generate
> Returns an integer from 1-3, probabilities
> determined by the values of the constants
> TREASURE_PROBABILITY_1 & _2.

#### `int CTG_GetNumItemsInBaseContainer(object oBaseCont)`
> Get the number of items in a base container.

#### `int CTG_IsItemGold()`
> Determine whether an item should actually just be gold.
> Returns TRUE or FALSE.
> Probability controlled by constant TREASURE_GOLD_PROBABILITY

#### `object CTG_GetMonsterBaseContainer(object oSource = OBJECT_SELF)`
> Find and return the right monster container, if
> available.

#### `object CTG_GetNearestBaseContainer(int nTreasureType, object oSource = OBJECT_SELF)`
> Locate the base container of the appropriate type closest to
> oSource.
> Possible values for nTreasureType:
> TREASURE_TYPE_LOW
> TREASURE_TYPE_MED
> TREASURE_TYPE_HIGH
> TREASURE_TYPE_UNIQUE

#### `object CTG_GetModuleBaseContainer(int nTreasureType)`
> Get the module-wide base container of the appropriate type.
> Possible values for nTreasureType:
> TREASURE_TYPE_LOW
> TREASURE_TYPE_MED
> TREASURE_TYPE_HIGH
> TREASURE_TYPE_UNIQUE

#### `object CTG_GetTreasureItem(object oBaseCont, int nItemNum)`
> Get the specified item out of the given base container's inventory

#### `int CTG_GetIsTreasureGenerated(object oCont)`
> Test if treasure has been generated in the given object

#### `void CTG_SetIsTreasureGenerated(object oCont, int bGenerated = TRUE)`
> Set whether treasure has been generated

#### `void CTG_CreateTreasure(int nTreasureType, object oAdventurer, object oCont = OBJECT_SELF)`
> Create random treasure items of the appropriate type
> in the specified container. Will typically be called
> by a script on a treasure container.
> Possible values for nTreasureType:
> TREASURE_TYPE_LOW
> TREASURE_TYPE_MED
> TREASURE_TYPE_HIGH
> TREASURE_TYPE_UNIQUE

#### `object CTG_GetSpecificBaseTypeTreasureItem(object oBaseCont, int nItemNum, int nBaseType1 = BASE_ITEM_INVALID, int nBaseType2 = BASE_ITEM_INVALID, int nBaseType3 = BASE_ITEM_INVALID)`
> Starting from the specified item position, return the first
> item that matches one of the three base types.
> nBaseType1 may also be passed in as a special custom type,
> which will OVERRIDE any other specified base types:
> TREASURE_BASE_TYPE_WEAPON (for any weapon type)
> TREASURE_BASE_TYPE_WEAPON_NOAMMO (for any weapon but ammunition)
> TREASURE_BASE_TYPE_WEAPON_RANGED (for any ranged weapon)
> TREASURE_BASE_TYPE_WEAPON_MELEE (for any melee weapon)
> TREASURE_BASE_TYPE_ARMOR (for armor, shields)
> TREASURE_BASE_TYPE_CLOTHING (for belts, boots, bracers,
> cloaks, helms, gloves)

#### `void CTG_CreateSpecificBaseTypeTreasure(int nTreasureType, object oAdventurer, object oCont, int nBaseType1 = BASE_ITEM_INVALID, int nBaseType2 = BASE_ITEM_INVALID, int nBaseType3 = BASE_ITEM_INVALID)`
> Create treasure of the appropriate treasure level and matching one
> of up to three different base types in the specified container.
> Possible values for nTreasureType:
> TREASURE_TYPE_LOW
> TREASURE_TYPE_MED
> TREASURE_TYPE_HIGH
> TREASURE_TYPE_UNIQUE
> Possible values for nBaseType1/2/3: any BASE_ITEM_* constant.
> If nBaseType1 is passed in as invalid, NO TYPE CHECKING WILL BE DONE.
> nBaseType1 may also be passed in as a special custom type,
> which will OVERRIDE any other specified base types:
> TREASURE_BASE_TYPE_WEAPON (for any weapon type)
> TREASURE_BASE_TYPE_WEAPON_NOAMMO (for any weapon but ammunition)
> TREASURE_BASE_TYPE_WEAPON_RANGED (for any ranged weapon)
> TREASURE_BASE_TYPE_WEAPON_MELEE (for any melee weapon)
> TREASURE_BASE_TYPE_ARMOR (for armor, shields)
> TREASURE_BASE_TYPE_CLOTHING (for belts, boots, bracers,
> cloaks, helms, gloves)

#### `void CTG_CreateGoldTreasure(int nTreasureType, object oAdventurer, object oCont = OBJECT_SELF)`
> Create gold treasure in the specified container.

#### `void CTG_GenerateNPCTreasure(int nTreasureType = 5, object oNPC = OBJECT_SELF)`
> Create treasure on an NPC.
> This function will typically be called from within the
> NPC's OnSpawn handler.
> Note that this defaults to TREASURE_TYPE_MONSTER, which uses
> the monster-specific treasure chests and falls back to low-
> level treasure if none exist.

#### `int CTG_GetIsBaseType(int nItemBaseType, int nBaseType1 = BASE_ITEM_INVALID, int nBaseType2 = BASE_ITEM_INVALID, int nBaseType3 = BASE_ITEM_INVALID)`
> Check if the item's base type is of the given base type

#### `int CTG_GetIsWeapon(int nItemBaseType)`
> Check if the item's base type is a weapon

#### `int CTG_GetIsWeaponNoammo(int nItemBaseType)`
> Check if the item's base type is a weapon but not ammunition

#### `int CTG_GetIsRangedWeapon(int nItemBaseType)`
> Check if the item's base type is a ranged weapon

#### `int CTG_GetIsMeleeWeapon(int nItemBaseType)`
> Check if the item's base type is a melee weapon

#### `int CTG_GetIsArmor(int nItemBaseType)`
> Check if the item's base type is armor

#### `int CTG_GetIsClothing(int nItemBaseType)`
> Check if the item's base type is clothing

#### `string CTG_GetRacialtypeChestTag(string sBaseTag, object oSource)`
> Tack on the appropriate racialtype suffix

#### `int CTG_GetIsContainerInitialized(object oBaseCont)`
> This function deliberately not prototyped. Should not be used
> outside this library.
> Test whether a treasure container has been initialized for
> specific base treasure type use.

#### `void CTG_SetIsContainerInitialized(object oBaseCont, int bInit = TRUE)`
> This function deliberately not prototyped. Should not be used
> outside this library.
> Set whether a treasure container has been initialized for
> specific base treasure type use.

#### `void CTG_InitContainer(object oBaseCont)`
> This function deliberately not prototyped. Should not be used
> outside this library.
> Initialize a treasure container to store the items contained
> inside as local variables on the container.

#### `int CTG_GetNumItems()`
> Get the number of items to generate
> Returns an integer from 1-3, probabilities
> determined by the values of the constants
> TREASURE_PROBABILITY_1 & _2.

#### `int CTG_GetNumItemsInBaseContainer(object oBaseCont)`
> Get the number of items in a base container

#### `int CTG_IsItemGold()`
> Determine whether an item should actually just be gold.
> Returns TRUE or FALSE.
> Probability controlled by constant TREASURE_GOLD_PROBABILITY

#### `int GetIsInteger(string sChar)`

#### `object CTG_GetMonsterBaseContainer(object oSource = OBJECT_SELF)`
> Find and return the right monster container, if
> available.

#### `object CTG_GetNearestBaseContainer(int nTreasureType, object oSource = OBJECT_SELF)`
> Locate the nearest base container of the appropriate type.
> Possible values for nTreasureType:
> TREASURE_TYPE_MONSTER
> TREASURE_TYPE_LOW
> TREASURE_TYPE_MED
> TREASURE_TYPE_HIGH
> TREASURE_TYPE_UNIQUE

#### `object CTG_GetModuleBaseContainer(int nTreasureType)`
> Get the module-wide base container of the appropriate type.
> Possible values for nTreasureType:
> TREASURE_TYPE_LOW
> TREASURE_TYPE_MED
> TREASURE_TYPE_HIGH
> TREASURE_TYPE_UNIQUE

#### `void CTG_CreateDefaultTreasure(int nTreasureType, object oAdventurer, object oCont)`
> Generate treasure using default method.
> Not prototyped -- this function should not be used outside
> this library.

#### `object CTG_GetTreasureItem(object oBaseCont, int nItemNum)`
> Get the specified item out of the given base container's inventory

#### `object CTG_GetSpecificBaseTypeTreasureItem(object oBaseCont, int nItemNum, int nBaseType1 = BASE_ITEM_INVALID, int nBaseType2 = BASE_ITEM_INVALID, int nBaseType3 = BASE_ITEM_INVALID)`
> Starting from the specified item position, return the first
> item that matches one of the three base types.
> If nBaseType1 is passed in as invalid, NO TYPE CHECKING WILL BE DONE.
> nBaseType1 may also be passed in as a special custom type:
> TREASURE_BASE_TYPE_WEAPON (for any weapon type)
> TREASURE_BASE_TYPE_WEAPON_NOAMMO (for any weapon but ammunition)
> TREASURE_BASE_TYPE_WEAPON_RANGED (for any ranged weapon)
> TREASURE_BASE_TYPE_WEAPON_MELEE (for any melee weapon)
> TREASURE_BASE_TYPE_ARMOR (for armor, shields)
> TREASURE_BASE_TYPE_CLOTHING (for belts, boots, bracers,
> cloaks, helms, gloves)

#### `int CTG_GetIsTreasureGenerated(object oCont)`
> Test if treasure has been generated in the given object

#### `void CTG_SetIsTreasureGenerated(object oCont, int bGenerated = TRUE)`
> Set whether treasure has been generated

#### `void CTG_CreateTreasure(int nTreasureType, object oAdventurer, object oCont = OBJECT_SELF)`
> Create random treasure items of the appropriate type
> in the specified container. Should be called
> by a script on a treasure container.
> Possible values for nTreasureType:
> TREASURE_TYPE_LOW
> TREASURE_TYPE_MED
> TREASURE_TYPE_HIGH
> TREASURE_TYPE_UNIQUE

#### `void CTG_CreateSpecificBaseTypeTreasure(int nTreasureType, object oAdventurer, object oCont, int nBaseType1 = BASE_ITEM_INVALID, int nBaseType2 = BASE_ITEM_INVALID, int nBaseType3 = BASE_ITEM_INVALID)`
> Create treasure of the appropriate treasure level and matching one
> of up to three different base types in the specified container.
> Possible values for nTreasureType:
> TREASURE_TYPE_LOW
> TREASURE_TYPE_MED
> TREASURE_TYPE_HIGH
> TREASURE_TYPE_UNIQUE
> Possible values for nBaseType1/2/3: any BASE_ITEM_* constant.
> Can also use these special values:
> TREASURE_BASE_TYPE_WEAPON (for any weapon type)
> TREASURE_BASE_TYPE_WEAPON_NOAMMO (for any weapon but ammunition)
> TREASURE_BASE_TYPE_WEAPON_RANGED (for any ranged weapon)
> TREASURE_BASE_TYPE_WEAPON_MELEE (for any melee weapon)
> TREASURE_BASE_TYPE_ARMOR (for armor, shields)
> TREASURE_BASE_TYPE_CLOTHING (for belts, boots, bracers,
> cloaks, helms, gloves)

#### `void CTG_CreateGoldTreasure(int nTreasureType, object oAdventurer, object oCont = OBJECT_SELF)`
> Create gold treasure in the specified container.

#### `void CTG_GenerateNPCTreasure(int nTreasureType = 5, object oNPC = OBJECT_SELF)`
> Create treasure on an NPC.
> This function will typically be called from within the
> NPC's OnSpawn handler.
> Note that this defaults to TREASURE_TYPE_MONSTER, which uses
> the monster-specific treasure chests and falls back to low-
> level treasure if none exist.

#### `int CTG_GetIsBaseType(int nItemBaseType, int nBaseType1 = BASE_ITEM_INVALID, int nBaseType2 = BASE_ITEM_INVALID, int nBaseType3 = BASE_ITEM_INVALID)`
> Check if the item's base type is of the given base type

#### `int CTG_GetIsWeapon(int nItemBaseType)`
> Check if the item's base type is a weapon

#### `int CTG_GetIsWeaponNoammo(int nItemBaseType)`
> Check if the item's base type is a weapon but not ammunition

#### `int CTG_GetIsRangedWeapon(int nItemBaseType)`
> Check if the item's base type is a ranged weapon

#### `int CTG_GetIsMeleeWeapon(int nItemBaseType)`
> Check if the item's base type is a melee weapon

#### `int CTG_GetIsArmor(int nItemBaseType)`
> Check if the item's base type is armor

#### `int CTG_GetIsClothing(int nItemBaseType)`
> Check if the item's base type is clothing

#### `string CTG_GetRacialtypeChestTag(string sBaseTag, object oSource)`
> Tack on the appropriate racialtype suffix
