# `x2_inc_itemprop.nss`

Source: `NSS/x2_/x2_inc_itemprop.nss`  
40 functions · 18 constants

## Constants

| Constant | Type | Value | Note |
|---|---|---|---|
| `X2_IP_WORK_CONTAINER_TAG` | string | `"x2_plc_ipbox"` |  |
| `X2_IP_ADDRPOP_2DA` | string | `"des_crft_props"` |  |
| `X2_IP_POISONWEAPON_2DA` | string | `"des_crft_poison"` |  |
| `X2_IP_ARMORPARTS_2DA` | string | `"des_crft_aparts"` |  |
| `X2_IP_ARMORAPPEARANCE_2DA` | string | `"des_crft_appear"` |  |
| `XP_IP_ITEMMODCONVERSATION_CTOKENBASE` | int | `12220` |  |
| `X2_IP_ITEMMODCONVERSATION_MODE_TAILOR` | int | `0` |  |
| `X2_IP_ITEMMODCONVERSATION_MODE_CRAFT` | int | `1` |  |
| `X2_IP_MAX_ITEM_PROPERTIES` | int | `8` |  |
| `X2_IP_ARMORTYPE_NEXT` | int | `0` |  |
| `X2_IP_ARMORTYPE_PREV` | int | `1` |  |
| `X2_IP_ARMORTYPE_RANDOM` | int | `2` |  |
| `X2_IP_WEAPONTYPE_NEXT` | int | `0` |  |
| `X2_IP_WEAPONTYPE_PREV` | int | `1` |  |
| `X2_IP_WEAPONTYPE_RANDOM` | int | `2` |  |
| `X2_IP_ADDPROP_POLICY_REPLACE_EXISTING` | int | `0` |  |
| `X2_IP_ADDPROP_POLICY_KEEP_EXISTING` | int | `1` |  |
| `X2_IP_ADDPROP_POLICY_IGNORE_EXISTING` | int | `2` |  |

## Functions

#### `void IPRemoveMatchingItemProperties(object oItem, int nItemPropertyType, int nItemPropertyDuration = DURATION_TYPE_TEMPORARY, int nItemPropertySubType = -1)`
> removes all itemproperties with matching nItemPropertyType and nItemPropertyDuration

#### `void IPRemoveAllItemProperties(object oItem, int nItemPropertyDuration = DURATION_TYPE_TEMPORARY)`
> Removes ALL item properties from oItem matching nItemPropertyDuration

#### `int IPGetIsItemEquipable(object oItem)`
> returns TRUE if item can be equipped.
> Uses Get2DAString, so do not use in a loop!

#### `object IPDyeArmor(object oItem, int nColorType, int nColor)`
> Changes the color of an item armor
> oItem        - The armor
> nColorType   - ITEM_APPR_ARMOR_COLOR_* constant
> nColor       - color from 0 to 63
> Since oItem is destroyed in the process, the function returns
> the item created with the color changed

#### `object IPGetIPWorkContainer(object oCaller = OBJECT_SELF)`
> Returns the container used for item property and appearance modifications in the
> module. If it does not exist, create it.

#### `itemproperty IPGetItemPropertyByID(int nPropID, int nParam1 = 0, int nParam2 = 0, int nParam3 = 0, int nParam4 = 0)`
> This function needs to be rather extensive and needs to be updated if there are new
> ip types we want to use, but it goes into the item property include anyway

#### `int IPGetIsRangedWeapon(object oItem)`
> returns TRUE if oItem is a ranged weapon

#### `int IPGetIsMeleeWeapon(object oItem)`
> return TRUE if oItem is a melee weapon

#### `int IPGetIsProjectile(object oItem)`
> return TRUE if oItem is a projectile (bolt, arrow, etc)

#### `int IPGetIsBludgeoningWeapon(object oItem)`
> returns true if weapon is blugeoning (used for poison)
> This uses Get2DAstring, so it is slow. Avoid using in loops!

#### `int IPGetIPConstCastSpellFromSpellID(int nSpellID)`
> Return the IP_CONST_CASTSPELL_* ID matching to the SPELL_* constant given in nSPELL_ID
> This uses Get2DAstring, so it is slow. Avoid using in loops!
> returns -1 if there is no matching property for a spell

#### `int IPGetItemHasItemOnHitPropertySubType(object oTarget, int nSubType)`
> Returns TRUE if an item has ITEM_PROPERTY_ON_HIT and the specified nSubType
> possible values for nSubType can be taken from IPRP_ONHIT.2da
> popular ones:
> 5 - Daze   19 - ItemPoison   24 - Vorpal

#### `int IPGetNumberOfAppearances(int nPart)`
> Returns the number of possible armor part variations for the specified part
> nPart - ITEM_APPR_ARMOR_MODEL_* constant
> Uses Get2DAstring, so do not use in loops

#### `int IPGetNextArmorAppearanceType(object oArmor, int nPart)`
> Returns the next valid appearance type for oArmor
> nPart - ITEM_APPR_ARMOR_MODEL_* constant
> Uses Get2DAstring, so do not use in loops

#### `int IPGetPrevArmorAppearanceType(object oArmor, int nPart)`
> Returns the previous valid appearance type for oArmor
> nPart - ITEM_APPR_ARMOR_MODEL_* constant
> Uses Get2DAstring, so do not use in loops

#### `int IPGetRandomArmorAppearanceType(object oArmor, int nPart)`
> Returns a random valid appearance type for oArmor
> nPart - ITEM_APPR_ARMOR_MODEL_* constant
> Uses Get2DAstring, so do not use in loops

#### `object IPGetModifiedArmor(object oArmor, int nPart, int nMode, int bDestroyOldOnSuccess)`
> Returns a new armor based of oArmor with nPartModified
> nPart - ITEM_APPR_ARMOR_MODEL_* constant of the part to be changed
> nMode -
> X2_IP_ARMORTYPE_NEXT    - next valid appearance
> X2_IP_ARMORTYPE_PREV    - previous valid apperance;
> X2_IP_ARMORTYPE_RANDOM  - random valid appearance;
> bDestroyOldOnSuccess - Destroy oArmor in process?
> Uses Get2DAstring, so do not use in loops

#### `void IPSafeAddItemProperty(object oItem, itemproperty ip, float fDuration = 0.0f, int nAddItemPropertyPolicy = X2_IP_ADDPROP_POLICY_REPLACE_EXISTING, int bIgnoreDurationType = FALSE, int bIgnoreSubType = FALSE)`
> Add an item property in a safe fashion, preventing unwanted stacking
> Parameters:
> oItem     - the item to add the property to
> ip        - the itemproperty to add
> fDuration - set 0.0f to add the property permanent, anything else is temporary
> nAddItemPropertyPolicy - How to handle existing properties. Valid values are:
> X2_IP_ADDPROP_POLICY_REPLACE_EXISTING - remove any property of the same type, subtype, durationtype before adding;
> X2_IP_ADDPROP_POLICY_KEEP_EXISTING - do not add if any property with same type, subtype and durationtype already exists;
> X2_IP_ADDPROP_POLICY_IGNORE_EXISTING - add itemproperty in any case - Do not Use with OnHit or OnHitSpellCast props!
> bIgnoreDurationType - If set to TRUE, an item property will be considered identical even if the DurationType is different. Be careful when using this
> with X2_IP_ADDPROP_POLICY_REPLACE_EXISTING, as this could lead to a temporary item property removing a permanent one
> bIgnoreSubType      - If set to TRUE an item property will be considered identical even if the SubType is different.

#### `int IPGetItemHasProperty(object oItem, itemproperty ipCompareTo, int nDurationType, int bIgnoreSubType = FALSE)`
> Wrapper for GetItemHasItemProperty that returns true if
> oItem has an itemproperty that matches ipCompareTo by Type AND DurationType AND SubType
> nDurationType = Valid DURATION_TYPE_* or -1 to ignore
> bIgnoreSubType - If set to TRUE an item property will be considered identical even if the SubType is different.

#### `int IPGetItemSequencerProperty(object oItem)`
> returns FALSE it the item has no sequencer property
> returns number of spells that can be stored in any other case

#### `int IPGetIsIntelligentWeapon(object oItem)`
> returns TRUE if the item has the OnHit:IntelligentWeapon property.

#### `int IPGetDamagePowerConstantFromNumber(int nNumber)`
> Mapping between numbers and power constants for ITEM_PROPERTY_DAMAGE_BONUS
> returns the appropriate ITEM_PROPERTY_DAMAGE_POWER_* constant for nNumber

#### `int IPGetDamageBonusConstantFromNumber(int nNumber)`
> returns the appropriate ITEM_PROPERTY_DAMAGE_BONUS_= constant for nNumber
> Do not pass in any number <1 ! Will return -1 on error

#### `void IPWildShapeCopyItemProperties(object oOld, object oNew, int bWeapon = FALSE)`
> Special Version of Copy Item Properties for use with greater wild shape
> oOld - Item equipped before polymorphing (source for item props)
> oNew - Item equipped after polymorphing  (target for item props)
> bWeapon - Must be set TRUE when oOld is a weapon.

#### `int IPGetWeaponEnhancementBonus(object oWeapon, int nEnhancementBonusType = ITEM_PROPERTY_ENHANCEMENT_BONUS)`
> Returns the current enhancement bonus of a weapon (+1 to +20), 0 if there is
> no enhancement bonus. You can test for a specific type of enhancement bonus
> by passing the appropritate ITEM_PROPERTY_ENHANCEMENT_BONUS* constant into
> nEnhancementBonusType

#### `void IPSetWeaponEnhancementBonus(object oWeapon, int nBonus, int bOnlyIfHigher = TRUE)`
> Shortcut function to set the enhancement bonus of a weapon to a certain bonus
> Specifying bOnlyIfHigher as TRUE will prevent a bonus lower than the requested
> bonus from being applied. Valid values for nBonus are 1 to 20.

#### `void IPUpgradeWeaponEnhancementBonus(object oWeapon, int nUpgradeBy)`
> Shortcut function to upgrade the enhancement bonus of a weapon by the
> number specified in nUpgradeBy. If the resulting new enhancement bonus
> would be out of bounds (>+20), it will be set to +20

#### `int IPGetHasItemPropertyOnCharacter(object oPC, int nItemPropertyConst)`
> Returns TRUE if a character has any item equipped that has the itemproperty
> defined in nItemPropertyConst in it (ITEM_PROPERTY_* constant)

#### `int IPGetNumberOfItemProperties(object oItem)`
> Returns an integer with the number of properties present oItem

#### `int IPGetNumberOfArmorAppearances(int nPart)`
> Returns the number of possible armor part variations for the specified part
> nPart - ITEM_APPR_ARMOR_MODEL_* constant
> Uses Get2DAstring, so do not use in loops

#### `int IPGetArmorAppearanceType(object oArmor, int nPart, int nMode)`
> (private)
> Returns the previous or next armor appearance type, depending on the specified
> mode (X2_IP_ARMORTYPE_NEXT || X2_IP_ARMORTYPE_PREV)

#### `object IPCreateProficiencyFeatItemOnCreature(object oCreature)`
> Creates a special ring on oCreature that gives
> all weapon and armor proficiencies to the wearer
> Item is set non dropable

#### `object IPGetTargetedOrEquippedMeleeWeapon()`

#### `object IPGetTargetedOrEquippedArmor(int bAllowShields = FALSE)`

#### `void IPCopyItemProperties(object oSource, object oTarget, int bIgnoreCraftProps = TRUE)`

#### `int IPGetWeaponAppearanceType(object oWeapon, int nPart, int nMode)`
> (private)

#### `object IPGetModifiedWeapon(object oWeapon, int nPart, int nMode, int bDestroyOldOnSuccess)`
> Returns a new armor based of oArmor with nPartModified
> nPart - ITEM_APPR_WEAPON_MODEL_* constant of the part to be changed
> nMode -
> X2_IP_WEAPONTYPE_NEXT    - next valid appearance
> X2_IP_WEAPONTYPE_PREV    - previous valid apperance;
> X2_IP_WEAPONTYPE_RANDOM  - random valid appearance (torso is never changed);
> bDestroyOldOnSuccess - Destroy oArmor in process?
> Uses Get2DAstring, so do not use in loops

#### `object IPCreateAndModifyArmorRobe(object oArmor, int nRobeType)`

#### `int IPGetHasItemPropertyByConst(int nItemProp, object oItem)`

#### `int IPGetHasUseLimitation(object oItem)`
> Returns TRUE if a use limitation of any kind is present on oItem
