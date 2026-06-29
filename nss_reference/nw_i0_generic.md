# `nw_i0_generic.nss`

Source: `NSS/nw_/nw_i0_generic.nss`  
31 functions · 12 constants

## Constants

| Constant | Type | Value | Note |
|---|---|---|---|
| `NW_GENERIC_FLEE_EXIT_FLEE` | int | `0` |  |
| `NW_GENERIC_FLEE_EXIT_RETURN` | int | `1` |  |
| `NW_GENERIC_FLEE_TELEPORT_FLEE` | int | `2` |  |
| `NW_GENERIC_FLEE_TELEPORT_RETURN` | int | `3` |  |
| `NW_GENERIC_SHOUT_I_WAS_ATTACKED` | int | `1` |  |
| `NW_GENERIC_SHOUT_I_AM_DEAD` | int | `12` |  |
| `NW_GENERIC_SHOUT_BACK_UP_NEEDED` | int | `13` |  |
| `NW_GENERIC_SHOUT_BLOCKER` | int | `2` |  |
| `chooseTactics_MEMORY_OFFENSE_MELEE` | int | `0` |  |
| `chooseTactics_MEMORY_DEFENSE_OTHERS` | int | `1` |  |
| `chooseTactics_MEMORY_DEFENSE_SELF` | int | `2` |  |
| `chooseTactics_MEMORY_OFFENSE_SPELL` | int | `3` |  |

## Functions

#### `int chooseTactics(object oIntruder)`
> The class-specific tactics have been broken out from DetermineCombatRound
> for readability. This function determines the actual tactics each class
> will use.

#### `int GetCharacterLevel(object oTarget)`
> Adds all three of the class levels together.  Used before
> GetHitDice became available

#### `void RemoveAmbientSleep()`
> If using ambient sleep this will remove the effect

#### `object GetLockedObject(object oMaster)`
> Searches for the nearest locked object to the master

#### `int BashDoorCheck(object oIntruder = OBJECT_INVALID)`
> Used in DetermineCombatRound to keep a
> henchmen bashing doors.

#### `int DetermineClassToUse()`
> Determines which of a NPCs three classes to
> use in DetermineCombatRound

#### `void DetermineCombatRound(object oIntruder = OBJECT_INVALID, int nAI_Difficulty = 10)`
> Created By: Preston Watamaniuk
> Created On: Oct 16, 2001

#### `void RespondToShout(object oShouter, int nShoutIndex, object oIntruder = OBJECT_INVALID)`
> Respond To Shouts
> Copyright (c) 2001 Bioware Corp.
> Allows the listener to react in a manner
> consistant with the given shout but only to one
> combat shout per round
> Created By: Preston Watamaniuk
> Created On: Oct 25, 2001
> NOTE ABOUT COMMONERS
> Commoners are universal cowards.  If you attack anyone
> they will flee for 4 seconds away from the attacker.
> However to make the commoners into a mob, make a single
> commoner at least 10th level of the same faction.
> If that higher level commoner is attacked or killed then
> the commoners will attack the attacker.  They will disperse again
> after some of them are killed.  Should NOT make multi-class
> creatures using commoners.
> NOTE ABOUT BLOCKERS
> It should be noted that the Generic Script for On Dialogue
> attempts to get a local set on the shouter by itself.
> This object represents the LastOpenedBy object.  It is this
> object that becomes the oIntruder within this function.
> NOTE ABOUT INTRUDERS
> The intruder object is for cases where a placable needs to
> pass a LastOpenedBy Object or a AttackMyAttacker
> needs to make his attacker the enemy of everyone.

#### `int AdjustBehaviorVariable(int nVar, string sVarName)`

#### `int InvisibleBecome(object oSelf = OBJECT_SELF)`
> Created By:  Brent
> Created On:  June 14, 2003

#### `int InvisibleTrue(object oSelf = OBJECT_SELF)`

#### `int GetShouldNotCastSpellsBecauseofArmor(object oTarget, int nClass)`
> Returns true if a wizard or sorcerer and wearing armor

#### `int chooseTactics(object oIntruder)`

#### `int __InCombatRound()`
> Created By:   Brent
> Created On:   July 11 2003

#### `void __TurnCombatRoundOn(int bBool)`

#### `void DetermineCombatRound(object oIntruder = OBJECT_INVALID, int nAI_Difficulty = 10)`

#### `void RespondToShout(object oShouter, int nShoutIndex, object oIntruder = OBJECT_INVALID)`

#### `void SetNPCWarningStatus(int nStatus = TRUE)`
> NPCs who have warning status set to TRUE will allow
> one 'free' attack by PCs from a non-hostile faction.

#### `int GetNPCWarningStatus()`
> NPCs who have warning status set to TRUE will allow
> one 'free' attack by PCs from a non-hostile faction.

#### `void SetSummonHelpIfAttacked()`
> Presently Does not work with the current implementation of encounter trigger

#### `void CreateSignPostNPC(string sTag, location lLocal)`
> This function is used only because ActionDoCommand can only accept void functions

#### `void ActivateFleeToExit()`

#### `int GetFleeToExit()`

#### `int GetCharacterLevel(object oTarget)`

#### `void RemoveAmbientSleep()`

#### `object GetLockedObject(object oMaster)`

#### `void CheckIsUnlocked(object oLastObject)`

#### `void PlayMobileAmbientAnimations()`
> Play Mobile Ambient Animations
> This function is now just a wrapper around
> code from x0_i0_anims.

#### `void DetermineSpecialBehavior(object oIntruder = OBJECT_INVALID)`

#### `int BashDoorCheck(object oIntruder = OBJECT_INVALID)`

#### `int DetermineClassToUse()`
