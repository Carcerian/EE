# `x0_i0_assoc.nss`

Source: `NSS/x0_/x0_i0_assoc.nss`  
20 functions · 96 constants

## Constants

| Constant | Type | Value | Note |
|---|---|---|---|
| `CLEAR_DEBUG` | int | `FALSE` |  |
| `sAssociateMasterConditionVarname` | string | `"NW_ASSOCIATE_MASTER"` |  |
| `NW_ASC_DISTANCE_2_METERS` | int | `0x00000001` |  |
| `NW_ASC_DISTANCE_4_METERS` | int | `0x00000002` |  |
| `NW_ASC_DISTANCE_6_METERS` | int | `0x00000004` |  |
| `NW_ASC_HEAL_AT_75` | int | `0x00000008` |  |
| `NW_ASC_HEAL_AT_50` | int | `0x00000010` |  |
| `NW_ASC_HEAL_AT_25` | int | `0x00000020` |  |
| `NW_ASC_AGGRESSIVE_BUFF` | int | `0x00000040` |  |
| `NW_ASC_AGGRESSIVE_SEARCH` | int | `0x00000080` |  |
| `NW_ASC_AGGRESSIVE_STEALTH` | int | `0x00000100` |  |
| `NW_ASC_RETRY_OPEN_LOCKS` | int | `0x00000200` |  |
| `NW_ASC_OVERKIll_CASTING` | int | `0x00000400` | GetMax Spell |
| `NW_ASC_POWER_CASTING` | int | `0x00000800` | Get Double CR or max 4 casting |
| `NW_ASC_SCALED_CASTING` | int | `0x00001000` | CR + 4; |
| `NW_ASC_USE_CUSTOM_DIALOGUE` | int | `0x00002000` |  |
| `NW_ASC_DISARM_TRAPS` | int | `0x00004000` |  |
| `NW_ASC_USE_RANGED_WEAPON` | int | `0x00008000` |  |
| `NW_ASC_MODE_DYING` | int | `0x00010000` |  |
| `NW_ASC_MODE_DEFEND_MASTER` | int | `0x04000000` |  |
| `NW_ASC_MODE_STAND_GROUND` | int | `0x08000000` |  |
| `NW_ASC_MASTER_GONE` | int | `0x10000000` |  |
| `NW_ASC_MASTER_REVOKED` | int | `0x20000000` |  |
| `NW_ASC_IS_BUSY` | int | `0x40000000` |  |
| `NW_ASC_HAVE_MASTER` | int | `0x80000000` |  |
| `CLEAR_X0_INC_HENAI_BKATTEMPTTODISARMTRAP_ThrowSelfOnTrap` | int | `1` |  |
| `CLEAR_X0_I0_ASSOC_RESETHENCHMENSTATE` | int | `2` |  |
| `CLEAR_NW_C2_DEFAULT4_29` | int | `3` |  |
| `CLEAR_NW_C2_DEFAULTB_GUSTWIND` | int | `4` |  |
| `CLEAR_NW_CH_AC1_49` | int | `5` |  |
| `CLEAR_NW_CH_AC1_81` | int | `6` |  |
| `CLEAR_NW_CH_AC4_28` | int | `7` |  |
| `CLEAR_NW_I0_GENERIC_658` | int | `8` |  |
| `CLEAR_NW_I0_GENERIC_834` | int | `9` |  |
| `CLEAR_NW_I0_GENERIC_ExitAOESpellArea` | int | `10` |  |
| `CLEAR_NW_I0_GENERIC_DetermineSpecialBehavior1` | int | `11` |  |
| `CLEAR_NW_I0_GENERIC_DetermineSpecialBehavior2` | int | `12` |  |
| `CLEAR_X0_CH_HEN_CONV_26` | int | `13` |  |
| `CLEAR_X0_CH_HEN_USRDEF_91` | int | `14` |  |
| `CLEAR_X0_CH_HEN_USRDEF_92` | int | `15` |  |
| `CLEAR_X0_I0_ANIMS_PlayMobile` | int | `16` |  |
| `CLEAR_X0_I0_ANIMS_PlayRandomMobile` | int | `17` |  |
| `CLEAR_X0_I0_ANIMS_PlayRandomCloseRange1` | int | `18` |  |
| `CLEAR_X0_I0_ANIMS_PlayRandomCloseRange2` | int | `19` |  |
| `CLEAR_X0_I0_ANIMS_AnimActionPlayRandomMobile1` | int | `20` |  |
| `CLEAR_X0_I0_ANIMS_AnimActionPlayRandomMobile2` | int | `21` |  |
| `CLEAR_X0_I0_ANIMS_AnimActionPlayRandomUncivilized` | int | `22` |  |
| `CLEAR_X0_I0_ANIMS_AnimActionGetUpFromChair` | int | `23` |  |
| `CLEAR_X0_I0_ANIMS_AnimActionGoToStop` | int | `24` |  |
| `CLEAR_X0_I0_ANIMS_AnimActionRest1` | int | `25` |  |
| `CLEAR_X0_I0_ANIMS_AnimActionRest2` | int | `26` |  |
| `CLEAR_X0_I0_ANIMS_GoHome` | int | `27` |  |
| `CLEAR_X0_I0_ANIMS_AnimActionLeaveHome` | int | `28` |  |
| `CLEAR_X0_I0_ANIMS_AnimActionChallengeIntruder` | int | `29` |  |
| `CLEAR_X0_I0_COMBAT_SpecialTacticsRanged1` | int | `30` |  |
| `CLEAR_X0_I0_COMBAT_SpecialTacticsRanged2` | int | `31` |  |
| `CLEAR_X0_I0_COMBAT_SpecialTacticsRanged3` | int | `32` |  |
| `CLEAR_X0_I0_COMBAT_SpecialTacticsAmbusher` | int | `33` |  |
| `CLEAR_X0_I0_COMBAT_SpecialTacticsCowardly1` | int | `34` |  |
| `CLEAR_X0_I0_COMBAT_SpecialTacticsCowardly2` | int | `35` |  |
| `CLEAR_X0_I0_EQUIP_EquipAppropriateWeapons1` | int | `36` |  |
| `CLEAR_X0_I0_EQUIP_EquipAppropriateWeapons2` | int | `37` |  |
| `CLEAR_X0_I0_EQUIP_EquipMelee1` | int | `38` |  |
| `CLEAR_X0_I0_EQUIP_EquipMelee2` | int | `39` |  |
| `CLEAR_X0_I0_EQUIP_EquipMelee3` | int | `40` |  |
| `CLEAR_X0_I0_HENCHMAN_Fire` | int | `41` |  |
| `CLEAR_X0_I0_HENCHMAN_LevelUp` | int | `42` |  |
| `CLEAR_X0_I0_HENCHMAN_PreRespawn` | int | `71` |  |
| `CLEAR_X0_INC_GENERIC_TalentFilter` | int | `43` |  |
| `CLEAR_X0_I0_TALENT_RangedAttackers` | int | `44` |  |
| `CLEAR_X0_I0_TALENT_RangedEnemies` | int | `68` |  |
| `CLEAR_X0_I0_TALENT_TalentFlee` | int | `69` |  |
| `CLEAR_X0_I0_TALENT_UseTurning` | int | `70` |  |
| `CLEAR_X0_I0_TALENT_SummonAllies` | int | `45` |  |
| `CLEAR_X0_I0_TALENT_MeleeAttack1` | int | `46` |  |
| `CLEAR_X0_I0_TALENT_MeleeAttack2` | int | `47` |  |
| `CLEAR_X0_I0_TALENT_TalentFlee2` | int | `48` |  |
| `CLEAR_X0_I0_TALENT_AdvancedBuff` | int | `49` |  |
| `CLEAR_X0_I0_TALENT_SeeInvisible` | int | `50` |  |
| `CLEAR_X0_I0_TALENT_BardSong` | int | `51` |  |
| `CLEAR_X0_I0_WALKWAY_WalkWayPoints` | int | `52` |  |
| `CLEAR_X0_INC_HENAI_HCR` | int | `53` |  |
| `CLEAR_X0_INC_HENAI_AttemptToDisarmTrap` | int | `54` |  |
| `CLEAR_X0_INC_HENAI_AttemptToOpenLock1` | int | `55` |  |
| `CLEAR_X0_INC_HENAI_AttemptToOpenLock2` | int | `56` |  |
| `CLEAR_X0_INC_HENAI_AttemptToOpenLock3` | int | `57` |  |
| `CLEAR_X0_INC_HENAI_RespondToShout1` | int | `58` |  |
| `CLEAR_X0_INC_HENAI_RespondToShout2` | int | `59` |  |
| `CLEAR_X0_INC_HENAI_RespondToShout3` | int | `60` |  |
| `CLEAR_X0_INC_HENAI_RespondToShout4` | int | `61` |  |
| `CLEAR_X0_INC_HENAI_CombatAttemptHeal1` | int | `62` |  |
| `CLEAR_X0_INC_HENAI_CombatAttemptHeal2` | int | `63` |  |
| `CLEAR_X0_INC_HENAI_Combat` | int | `64` |  |
| `CLEAR_X0_INC_HENAI_CombatAttemptHeal` | int | `65` |  |
| `CLEAR_X0_INC_HENAI_CombatFollowMaster1` | int | `66` |  |
| `CLEAR_X0_INC_HENAI_CombatFollowMaster2` | int | `67` |  |

## Functions

#### `int GetPercentageHPLoss(object oWounded)`
> Determine the percentage of hit points the object has left.
> Used to determine whether the assoc should heal their master.
> Returns an integer between 0 - 100.

#### `void SetAssociateState(int nCondition, int bValid = TRUE, object oAssoc = OBJECT_SELF)`
> Set/unset the specified condition flag in the caller's associate state

#### `int GetAssociateState(int nCondition, object oAssoc = OBJECT_SELF)`
> Returns TRUE if the specified condition flag is set on
> the associate.

#### `void ResetHenchmenState()`
> Returns the henchmen to a commandable state of grace

#### `int AssociateCheck(object oCheck)`
> TRUE if the object to check is NOT the caller's henchman

#### `int GetAssociateHealMaster()`
> Returns TRUE if the associate should attempt to heal the master

#### `float GetFollowDistance()`
> Returns the distance in meters at which the associate should begin
> to run after the master.

#### `void SetAssociateStartLocation()`
> Sets the associate's current location as their
> start location.

#### `location GetAssociateStartLocation()`
> Gets the associate's current start location.

#### `void ClearActions(int nClearConstant = 0, int bClearCombat = FALSE)`
> This is a wrapper for ClearAllActions.
> Added to try and track down some bugs in
> the AI.

#### `int GetPercentageHPLoss(object oWounded)`

#### `void ResetHenchmenState()`
> Created By: Preston Watamaniuk
> Created On: April 4, 2002

#### `int AssociateCheck(object oCheck)`
> True if the object is NOT the caller's henchman

#### `void SetAssociateState(int nCondition, int bValid = TRUE, object oAssoc = OBJECT_SELF)`

#### `int GetAssociateState(int nCondition, object oAssoc = OBJECT_SELF)`

#### `int GetAssociateHealMaster()`
> Created By: Preston Watamaniuk
> Created On: Nov 18, 2001

#### `float GetFollowDistance()`
> Determine the distance we should follow at

#### `void SetAssociateStartLocation()`
> Set Associate Start Location
> Copyright (c) 2001 Bioware Corp.
> Created By: Preston Watmaniuk
> Created On: Nov 21, 2001

#### `location GetAssociateStartLocation()`
> Get Associate Start Location
> Copyright (c) 2001 Bioware Corp.
> Created By: Preston Watmaniuk
> Created On: Nov 21, 2001

#### `void ClearActions(int nClearConstant = 0, int bClearCombat = FALSE)`
> Created By: Brent
> Created On: February 6, 2003
