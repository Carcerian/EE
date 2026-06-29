# `x2_inc_treasure.nss`

Source: `NSS/x2_/x2_inc_treasure.nss`  
25 functions · 16 constants

## Constants

| Constant | Type | Value | Note |
|---|---|---|---|
| `X2_DTS_CLASS_LOW` | int | `0` | Treasure Class Low |
| `X2_DTS_CLASS_MEDIUM` | int | `1` | Treasure Clas Medium |
| `X2_DTS_CLASS_HIGH` | int | `2` | Treasure Class High |
| `X2_DTS_TYPE_DISP` | int | `1` |  |
| `X2_DTS_TYPE_AMMO` | int | `2` |  |
| `X2_DTS_TYPE_GOLD` | int | `4` | actually gold and gems |
| `X2_DTS_TYPE_ITEM` | int | `8` | char specific Item |
| `X2_DTS_BASECHANCE_TREAS` | int | `50` | Basic chance for treasure |
| `X2_DTS_MAXITEMS` | int | `2` |  |
| `X2_DTS_STACKVAR` | int | `50` | Stack variation is 50-100 percent of the number listed in the 2da |
| `X2_DTS_2DA_DISP` | string | `"des_treas_disp"` | 2da for disposeable class treasure |
| `X2_DTS_2DA_AMMO` | string | `"des_treas_ammo"` | 2da for ammo class treasure |
| `X2_DTS_2DA_GOLD` | string | `"des_treas_gold"` | 2da for gold n gems |
| `X2_DTS_2DA_ITEM` | string | `"des_treas_items"` | 2da for specific items |
| `X2_DTS_2DA_ENHANCEMENTS` | string | `"des_treas_enh"` |  |
| `X2_DTS_2DA_CONF` | string | `"des_conf_treas"` | 2da with configuration |

## Functions

#### `void DTSGenerateTreasureOnContainer(object oContainer, object oOpener, int nClass, int nType = 5)`
> Generate random, disposeable treasure on the container
> oContainer - Valid object with inventory
> oOpener    - The one who opened the container
> nClass - Treasure Class (X2_DTS_CLASS_*)
> nType  - Treasure Type  (X2_DTS_TYPE_*), default = X2_DTS_TYPE_DISPOSEABLE | X2_DTS_TYPE_GOLD
> Values: X2_DTS_TYPE_DISPOSEABLE - Potions, Kits, etc
> X2_DTS_TYPE_AMMO        - Ammunition
> X2_DTS_TYPE_GOLD        - Gold and Gems
> X2_DTS_TYPE_ITEM    - Character Optimized treasure (ignores treasure class)
> Example:
> Generate Low Class Ammo and Gold+Gems
> DTSGenerateTreasureOnContainer (oChest, X2_DTS_CLASS_LOW, X2_DTS_TYPE_AMMO | X2_DTS_TYPE_GOLD);

#### `object DTSGenerateCharSpecificTreasure(object oContainer, object oAdventurer, int bIgnoreFeats = FALSE)`
> Generates one random, character specific item on container
> Treasure is optimized to suit a characters needs
> if bIgnoreFeats is set TRUE, the system will not use Feats (i.e. Weapon Focus)
> to determine a baseitem to spawn

#### `void DTSInitialize(int nConfigIndex = 0)`
> Initializes the treasure system by loading x2_conf_tras.2da
> nConfigIndex - RowIndex of the configuration to load

#### `void DTSSetAreaTreasureProbability(object oArea, int nBaseChance, int bDisabled = FALSE)`
> Sets the area wide chance for treasure Generation ...
> if bDisable = TRUE, then no random treasure is generated at all

#### `int DTSGrantCharSpecificWeaponEnhancement(int nLevel, object oItem)`
> Enchantes the weapon passed in oItem with a scaled enhancement bonus
> nLevel should be the level of the player who is going to receive
> the item. Lookup is done via  des_treas_enh.2da.
> returns TRUE on success

#### `void DTSDebug(string s)`

#### `string DTSGet2DAStringOrDefault(string s2DA, string sColumn, int nRow, string sDefault)`
> Get a 2da String or the supplied default if string is empty

#### `string DTSGet2DANameByType(int nType)`
> Maps the X2_DTS_TYPE_* value given in nType to a 2da name

#### `string DTSGet2DAColNameByClass(int nClass)`
> Maps the X2_DTS_CLASS_* value given in nType to row name in the 2da

#### `int DTSGetNoOfRowsInTreasureTable(int nType, int nClass = 1, string sCol = "")`
> Returns the number of entries available for random treasure of a given type and class
> nType   - X2_DTS_TYPE_*
> nClass  - X2_DTS_CLASS_* (default = X2_DTS_CLASS_LOW)
> sCol    - used when X2_DTS_TYPE_ITEM is specified

#### `int DTSGetBaseChance(object oArea)`

#### `int DTSGetMaxItems()`
> Returns the maximum number of items to generate according to the configuration
> If no configuration is used, default is X2_DTS_MAXITEMS (2)

#### `float DTSGetStackVariation()`
> Returns the stack variation to use when generation stacked items
> If no configuration is used, default is X2_DTS_STACKVAR (0.5)
> Stacks are calculated (Stack* X2_DTS_STACKVAR) + Random (Stack *X2_DTS_STACKVAR)

#### `int DTSGrantCharSpecificWeaponEnhancement(int nLevel, object oItem)`
> Enchantes the weapon passed in oItem with a scaled enhancement bonus
> nLevel should be the level of the player who is going to receive
> the item. Lookup is done via  des_treas_enh.2da.
> returns TRUE on success

#### `object DTSCreateItemOnObject(string sItemTemplate, object oTarget)`
> This is a wrapper for CreateItemOnObject which can handle the stack number
> given on

#### `string DTSGetRandomItemResRef(int nType, int nClass)`
> Returns a single random item resref from the approriate 2da
> nType   - X2_DTS_TYPE_*  - Type of Treasure (i.e. disposeable, ammo)
> nClass  - X2_DTS_CLASS_* - Class of Treasure (i.e. high, medium, low)

#### `string DTSGetFeatSpecificItemResRef(int nFeatID)`

#### `int DTSGetHighestClass(object oCreature)`
> Returns the Highest class of a creature

#### `int DTSDetermineFeatToUse(object oAdventurer, int bDontUseFeats = FALSE)`

#### `void DTSGenerateTreasureItems(object oContainer, object oOpener, int nClass, int nType)`

#### `int DTSGetNumberofPartyMembers(object oPC)`

#### `void DTSGenerateTreasureOnContainer(object oContainer, object oOpener, int nClass, int nType = 5)`
> Created By: Georg Zoeller
> Created On: 2003-06-03

#### `object DTSGenerateCharSpecificTreasure(object oContainer, object oAdventurer, int bIgnoreFeats = FALSE)`
> Created By: Georg Zoeller
> Created On: 2003-06-04

#### `void DTSInitialize(int nConfigIndex = 0)`

#### `void DTSSetAreaTreasureProbability(object oArea, int nBaseChance, int bDisabled = FALSE)`
> Sets the area wide chance for treasure Generation ...
> if bDisable = TRUE, then no random treasure is generated at all
