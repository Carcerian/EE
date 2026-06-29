# `x2_inc_shifter.nss`

Source: `NSS/x2_/x2_inc_shifter.nss`  
12 functions · 7 constants

## Constants

| Constant | Type | Value | Note |
|---|---|---|---|
| `SHIFTER_DC_VERY_EASY` | int | `0` |  |
| `SHIFTER_DC_EASY` | int | `1` |  |
| `SHIFTER_DC_EASY_MEDIUM` | int | `2` |  |
| `SHIFTER_DC_NORMAL` | int | `3` |  |
| `SHIFTER_DC_HARD` | int | `4` |  |
| `X2_GW2_EPIC_THRESHOLD` | int | `11` |  |
| `X2_GW3_EPIC_THRESHOLD` | int | `15` |  |

## Functions

#### `int ShifterDecrementGWildShapeSpellUsesLeft()`
> Returns and decrements the number of times this ability can be used
> while in this shape. See x2_s2_gwildshp for more information
> Do not place this on any spellscript that is not called
> exclusively from Greater Wildshape

#### `void ShifterSetGWildshapeSpellLimits(int nSpellId)`
> Introduces an artifical limit on the special abilities of the Greater
> Wildshape forms,in order to work around the engine limitation
> of being able to cast any assigned spell an unlimited number of times
> Current settings:
> Darkness (Drow/Drider) : 1+ 1 use per 5 levels
> Stonegaze(Medusa) :      1+ 1 use per 5 levels
> Stonegaze(Basilisk) :    1+ 1 use per 5 levels
> Stonegaze(Basilisk) :    1+ 1 use per 5 levels
> MindBlast(Illithid) :    1+ 1 use per 3 levels
> Domination(Vampire) :    1+ 1 use per 5 levels

#### `int ShifterGetSaveDC(object oPC, int nShifterDCConst = SHIFTER_DC_NORMAL, int bAddDruidLevels = FALSE)`
> Used for the scaling DC of various shifter abilities.
> Parameters:
> oPC              - The Shifter
> nShifterDCConst  - SHIFTER_DC_EASY, SHIFTER_DC_NORMAL, SHIFTER_DC_HARD
> bAddDruidLevels  - Take druid levels into account

#### `int ShifterMergeWeapon(int nPolymorphConstant)`
> Returns TRUE if the shifter's current weapon should be merged onto his
> newly equipped melee weapon

#### `int ShifterMergeArmor(int nPolymorphConstant)`
> Returns TRUE if the shifter's current armor should be merged onto his
> creature hide after shifting.

#### `int ShifterMergeItems(int nPolymorphConstant)`
> Returns TRUE if the shifter's current items (gloves, belt, etc) should
> be merged onto his creature hide after shiftng.

#### `void ShifterSetGWildshapeSpellLimits(int nSpellId)`
> GZ, 2003-07-09
> Introduces an artifical limit on the special abilities of the Greater
> Wildshape forms,in order to work around the engine limitation
> of being able to cast any assigned spell an unlimited number of times

#### `int ShifterDecrementGWildShapeSpellUsesLeft()`
> GZ, 2003-07-09
> Returns and decrements the number of times this ability can be used
> while in this shape. See x2_s2_gwildshp for more information
> Do not place this on any spellscript that is not called
> exclusively from Greater Wildshape

#### `int ShifterGetSaveDC(object oPC, int nShifterDCConst = SHIFTER_DC_NORMAL, int bAddDruidLevels = FALSE)`
> GZ, Oct 19, 2003
> Used for the scaling DC of various shifter abilities.
> Parameters:
> oPC              - The Shifter
> nShifterDCConst  - SHIFTER_DC_VERY_EASY, SHIFTER_DC_EASY,
> SHIFTER_DC_NORMAL, SHIFTER_DC_HARD, SHIFTER_DC_EASY_MEDIUM
> bAddDruidLevels  - Take druid levels into account

#### `int ShifterMergeWeapon(int nPolymorphConstant)`
> GZ, Oct 19, 2003
> Returns TRUE if the shifter's current weapon should be merged onto his
> newly equipped melee weapon

#### `int ShifterMergeArmor(int nPolymorphConstant)`
> GZ, Oct 19, 2003
> Returns TRUE if the shifter's current armor should be merged onto his
> creature hide after shifting.

#### `int ShifterMergeItems(int nPolymorphConstant)`
> GZ, Oct 19, 2003
> Returns TRUE if the shifter's current items (gloves, belt, etc) should
> be merged onto his creature hide after shifting.
