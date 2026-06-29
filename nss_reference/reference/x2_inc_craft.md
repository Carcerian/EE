# `x2_inc_craft.nss`

Source: `NSS/x2_/x2_inc_craft.nss`  
44 functions · 32 constants

## Constants

| Constant | Type | Value | Note |
|---|---|---|---|
| `X2_CI_CRAFTSKILL_CONV` | string | `"x2_p_craftskills"` |  |
| `X2_CI_BREWPOTION_FEAT_ID` | int | `944` | Brew Potion feat simulation |
| `X2_CI_BREWPOTION_MAXLEVEL` | int | `3` | Max Level for potions |
| `X2_CI_BREWPOTION_COSTMODIFIER` | int | `50` | gp Brew Potion XPCost Modifier |
| `X2_CI_BREWPOTION_NEWITEM_RESREF` | string | `"x2_it_pcpotion"` | ResRef for new potion item |
| `X2_CI_SCRIBESCROLL_FEAT_ID` | int | `945` |  |
| `X2_CI_SCRIBESCROLL_COSTMODIFIER` | int | `25` | Scribescroll Cost Modifier |
| `X2_CI_SCRIBESCROLL_NEWITEM_RESREF` | string | `"x2_it_pcscroll"` | ResRef for new scroll item |
| `X2_CI_CRAFTWAND_FEAT_ID` | int | `946` |  |
| `X2_CI_CRAFTWAND_MAXLEVEL` | int | `4` |  |
| `X2_CI_CRAFTWAND_COSTMODIFIER` | int | `750` |  |
| `X2_CI_CRAFTWAND_NEWITEM_RESREF` | string | `"x2_it_pcwand"` |  |
| `X2_CI_CRAFTING_WP_2DA` | string | `"des_crft_weapon"` |  |
| `X2_CI_CRAFTING_AR_2DA` | string | `"des_crft_armor"` |  |
| `X2_CI_CRAFTING_MAT_2DA` | string | `"des_crft_mat"` |  |
| `X2_CI_CRAFTING_SP_2DA` | string | `"des_crft_spells"` |  |
| `X2_CI_CRAFTINGSKILL_CTOKENBASE` | int | `13220` |  |
| `X2_CI_CRAFTINGSKILL_DC_CTOKENBASE` | int | `14220` |  |
| `X2_CI_CRAFTINGSKILL_GP_CTOKENBASE` | int | `14320` |  |
| `X2_CI_MODIFYARMOR_GP_CTOKENBASE` | int | `14420` |  |
| `X2_CI_CRAFTING_ITEMS_PER_ROW` | int | `5` |  |
| `X2_CI_2DA_SCROLLS` | string | `"des_crft_scroll"` |  |
| `X2_CI_CRAFTMODE_INVALID` | int | `0` |  |
| `X2_CI_CRAFTMODE_CONTAINER` | int | `1` | no longer used, but left in for the community to reactivate |
| `X2_CI_CRAFTMODE_BASE_ITEM` | int | `2` |  |
| `X2_CI_CRAFTMODE_ASSEMBLE` | int | `3` |  |
| `X2_CI_MAGICTYPE_INVALID` | int | `0` |  |
| `X2_CI_MAGICTYPE_ARCANE` | int | `1` |  |
| `X2_CI_MAGICTYPE_DIVINE` | int | `2` |  |
| `X2_CI_MODMODE_INVALID` | int | `0` |  |
| `X2_CI_MODMODE_ARMOR` | int | `1` |  |
| `X2_CI_MODMODE_WEAPON` | int | `2` |  |

## Functions

#### `int CIGetIsCraftFeatBaseItem(object oItem)`
> Returns TRUE if an item is a Craft Base Item
> to be used in spellscript that can be cast on items - i.e light

#### `int CICraftCheckBrewPotion(object oSpellTarget, object oCaster)`
> Checks if the last spell cast was used to brew potion and will do the brewing process.
> Returns TRUE if the spell was indeed used to brew a potion (regardless of the actual outcome of the brewing process)
> Meant to be used in spellscripts only

#### `int CICraftCheckScribeScroll(object oSpellTarget, object oCaster)`
> Checks if the last spell cast was used to scribe a scroll and handles the scribe scroll process
> Returns TRUE if the spell was indeed used to scribe a scroll (regardless of the actual outcome)
> Meant to be used in spellscripts only

#### `object CICraftBrewPotion(object oCreator, int nSpellID)`
> Create a new potion item based on the spell nSpellID  on the creator

#### `object CICraftScribeScroll(object oCreator, int nSpellID)`
> Create a new scroll item based on the spell nSpellID on the creator

#### `int CIGetSpellWasUsedForItemCreation(object oSpellTarget)`
> Checks if the caster intends to use his item creation feats and
> calls appropriate item creation subroutine if conditions are met (spell cast on correct item, etc).
> Returns TRUE if the spell was used for an item creation feat

#### `int CIGetSpellInnateLevel(int nSpellID, int bDefaultZeroToOne = FALSE)`
> Returns the innate level of a spell. If bDefaultZeroToOne is given
> Level 0 spell will be returned as level 1 spells

#### `object CIUseCraftItemSkill(object oPC, int nSkill, string sResRef, int nDC, object oContainer = OBJECT_INVALID)`
> Makes oPC do a Craft check using nSkill to create the item supplied in sResRe
> If oContainer is specified, the item will be created there.
> Throwing weapons are created with stack sizes of 10, ammo with 20
> oPC       - The player crafting
> nSkill    - SKILL_CRAFT_WEAPON or SKILL_CRAFT_ARMOR,
> sResRef   - ResRef of the item to be crafted
> nDC       - DC to beat to succeed
> oContainer - if a container is specified, create item inside

#### `int CIGetIsSpellRestrictedFromCraftFeat(int nSpellID, int nFeatID)`
> Returns TRUE if a spell is prevented from being used with one of the crafting feats

#### `struct craft_struct CIGetCraftItemStructFrom2DA(string s2DA, int nRow, int nItemNo)`
> Return craftitemstructdata

#### `int CI_GetClassMagicType(int nClass)`
> Return the type of magic as one of the following constants
> const int X2_CI_MAGICTYPE_INVALID = 0;
> const int X2_CI_MAGICTYPE_ARCANE  = 1;
> const int X2_CI_MAGICTYPE_DIVINE  = 2;
> Parameters:
> nClass - CLASS_TYPE_* constant

#### `string GetMaterialComponentTag(int nPropID)`

#### `int CIGetIsCraftFeatBaseItem(object oItem)`
> Return true if oItem is a crafting target item

#### `object CICraftBrewPotion(object oCreator, int nSpellID)`
> Georg, 2003-06-12
> Create a new playermade potion object with properties matching nSpellID and return it

#### `int CIGetCraftGPCost(int nLevel, int nMod)`
> Wrapper for the crafting cost calculation, returns GP required

#### `object CICraftCraftWand(object oCreator, int nSpellID)`
> Georg, 2003-06-12
> Create a new playermade wand object with properties matching nSpellID
> and return it

#### `object CICraftScribeScroll(object oCreator, int nSpellID)`
> Georg, 2003-06-12
> Create and Return a magic wand with an item property
> matching nSpellID. Charges are set to d20 + casterlevel
> capped at 50 max

#### `int CICraftCheckBrewPotion(object oSpellTarget, object oCaster)`
> Returns TRUE if the player used the last spell to brew a potion

#### `int CICraftCheckScribeScroll(object oSpellTarget, object oCaster)`
> Returns TRUE if the player used the last spell to create a scroll

#### `int CICraftCheckCraftWand(object oSpellTarget, object oCaster)`
> Returns TRUE if the player used the last spell to craft a wand

#### `int CIGetSpellWasUsedForItemCreation(object oSpellTarget)`
> Georg, July 2003
> Checks if the caster intends to use his item creation feats and
> calls appropriate item creation subroutine if conditions are met
> (spell cast on correct item, etc).
> Returns TRUE if the spell was used for an item creation feat

#### `object CIUseCraftItemSkill(object oPC, int nSkill, string sResRef, int nDC, object oContainer = OBJECT_INVALID)`
> Makes oPC do a Craft check using nSkill to create the item supplied in sResRe
> If oContainer is specified, the item will be created there.
> Throwing weapons are created with stack sizes of 10, ammo with 20

#### `int CIDoCraftItemFromConversation(int nNumber)`
> georg, 2003-06-13 (
> Craft an item. This is only to be called from the crafting conversation
> spawned by x2_s2_crafting!!!

#### `struct craft_struct CIGetCraftItemStructFrom2DA(string s2DA, int nRow, int nItemNo)`
> Retrieve craft information on a certain item

#### `int CIGetItemPartModificationCost(object oOldItem, int nPart)`
> Return the cost

#### `int CIGetItemPartModificationDC(object oOldItem, int nPart)`
> Return the DC for modifying a certain armor part on oOldItem

#### `int CIGetArmorModificationCost(object oOldItem, object oNewItem)`
> returns the dc
> dc to modify oOlditem to look like oNewItem

#### `int CIGetArmorModificationDC(object oOldItem, object oNewItem)`
> returns the cost in gold piece that it would
> cost to modify oOlditem to look like oNewItem

#### `int CIGetIsSpellRestrictedFromCraftFeat(int nSpellID, int nFeatID)`
> returns TRUE if the spell matching nSpellID is prevented from being used
> with the CraftFeat matching nFeatID
> This is controlled in des_crft_spells.2da

#### `int CIGetCraftingReceipeRow(int nMode, object oMajor, object oMinor, int nSkill)`
> Retrieve the row in des_crft_bmat too look up receipe

#### `void CISetupCraftingConversation(object oPC, int nNumber, int nSkill, int nReceipe, object oMajor, object oMinor, int nMode)`
> used to set all variable required for the crafting conversation
> (Used materials, number of choises, 2da row, skill and mode)

#### `struct craft_receipe_struct CIGetCraftingModeFromTarget(object oPC, object oTarget, object oItem = OBJECT_INVALID)`
> oItem - The item used for crafting

#### `int CIGetInModWeaponOrArmorConv(object oPC)`
> Crafting Conversation Functions ***

#### `void CISetCurrentModMode(object oPC, int nMode)`

#### `int CIGetCurrentModMode(object oPC)`

#### `object CIGetCurrentModBackup(object oPC)`

#### `object CIGetCurrentModItem(object oPC)`

#### `void CISetCurrentModBackup(object oPC, object oBackup)`

#### `void CISetCurrentModItem(object oPC, object oItem)`

#### `void CISetCurrentModPart(object oPC, int nPart, int nStrRef)`
> This does multiple things:
> -  store the part currently modified
> -  setup the custom token for the conversation
> -  zoom the camera to that part

#### `int CIGetCurrentModPart(object oPC)`

#### `void CISetDefaultModItemCamera(object oPC)`

#### `void CIUpdateModItemCostDC(object oPC, int nDC, int nCost)`

#### `int CIGetWeaponModificationCost(object oOldItem, object oNewItem)`
> dc to modify oOlditem to look like oNewItem
