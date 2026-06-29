# `x0_i0_common.nss`

Source: `NSS/x0_/x0_i0_common.nss`  
37 functions · 21 constants

## Constants

| Constant | Type | Value | Note |
|---|---|---|---|
| `X0_DEBUG_SETTING` | int | `0` |  |
| `DIFFICULTY_EASY` | int | `1` |  |
| `DIFFICULTY_MODERATE` | int | `2` |  |
| `DIFFICULTY_HARD` | int | `3` |  |
| `DIFFICULTY_IMPOSSIBLE` | int | `4` |  |
| `sHasMetSuffix` | string | `"_MET"` |  |
| `sHasHiredSuffix` | string | `"_HIRED"` |  |
| `sDidQuitSuffix` | string | `"_QUIT"` |  |
| `sFriendSuffix` | string | `"_FR"` |  |
| `sHasInterjectionSuffix` | string | `"_INTJ"` |  |
| `sInterjectionSetSuffix` | string | `"_INTJ_SET"` |  |
| `sAdviceSuffix` | string | `"_ADV"` |  |
| `sPersuadeAttemptSuffix` | string | `"_PERSUADE"` |  |
| `sPersuadeSuccessSuffix` | string | `"_PERSUADE_SUCC"` |  |
| `sThreatenSuffix` | string | `"_THREAT"` |  |
| `sOneLinerVarname` | string | `"X0_CURRENT_ONE_LINER"` |  |
| `sOneShotVarname` | string | `"X0_ONE_SHOT_EVENT"` |  |
| `sRouterTag` | string | `"X0_EVT_ROUTER_M"` |  |
| `sStartLocationVarname` | string | `"X0_START_LOC"` |  |
| `sRespawnLocationVarname` | string | `"X0_RESPAWN_LOC"` |  |
| `CONVERSATION_ATTEMPT_DELAY` | float | `3.0` |  |

## Functions

#### `void DBG_msg(string sMsg)`
> Print out a short message to the log files.

#### `int GetChapter()`
> THIS WILL ONLY WORK CORRECTLY IN EXPANSION PACK 0.
> NOT VALID FOR USER MODULES!
> Returns the number of the current chapter of the game.
> Module 1: 1
> Module 2: 2
> Module 3: 3

#### `int EndModule()`
> Returns true if this is an end module
> ONLY VALID IN EXPANSION PACK 0!
> NOT VALID FOR USER MODULES!
> Note -- this is actually never true since there are
> no end modules for XP1 now.

#### `string GetMyArea(object oTarget = OBJECT_SELF)`
> Returns the tag of the current area oTarget is in

#### `int HasItemByTag(object oTarget, string sTag)`
> Determine if the target is carrying the specified object.

#### `void SetRespawnLocation(object oTarget = OBJECT_SELF)`
> Set the respawn point to the current location of the
> caller

#### `void SetRespawnLocationSpecific(object oTarget, location lRespawn)`
> Set the respawn point for the target to a specific location

#### `location GetRespawnLocation(object oTarget = OBJECT_SELF)`
> Get the current respawn point for the caller

#### `string GetTagNoPrefix(object oTarget = OBJECT_SELF)`
> Returns the tag of the target with the 3-letter prefix (x0_)
> stripped. Useful since these are stripped from blueprint
> resrefs when editing copies.

#### `void SetBooleanValue(object oTarget, string sVarname, int bVal = TRUE)`
> Set a true/false value on oTarget.

#### `int GetBooleanValue(object oTarget, string sVarname)`
> Get the value of a true/false variable on oTarget

#### `void SetCampaignBooleanValue(object oTarget, string sVarname, int bVal = TRUE)`
> Set a true/false persistent value on oTarget

#### `int GetCampaignBooleanValue(object oTarget, string sVarname)`
> Get the value of a persistent true/false variable on oTarget

#### `void ClearAllDialogue(object oPC, object oNPC = OBJECT_SELF)`
> Call to clear all dialogue events

#### `void SetHasInterjection(object oPC, int bHasInter = TRUE, int nInter = 0, object oNPC = OBJECT_SELF)`
> Call to indicate this NPC has an interjection to
> make to this PC and which one if so.

#### `void SetInterjection(object oPC, int nInter = 0, object oNPC = OBJECT_SELF)`
> Call to set the interjection value

#### `int GetHasInterjection(object oPC, object oNPC = OBJECT_SELF)`
> Call to determine if the NPC has an interjection
> to make to this PC. Returns FALSE or the number
> of the interjection otherwise.

#### `void SetHasAdvice(object oPC, int bHasAdvice = TRUE, int nAdvice = 0, object oNPC = OBJECT_SELF)`
> Call to indicate this NPC has some advice to
> give to this PC and which advice set if so.

#### `int GetHasAdvice(object oPC, object oNPC = OBJECT_SELF)`
> Call to determine if the NPC has advice to give
> to this PC. Returns FALSE or the number of the
> advice set otherwise.

#### `void SetOneLiner(int bHasOneLiner = TRUE, int nLine = 0, object oNPC = OBJECT_SELF)`
> Set whether an NPC has a one-liner available to make

#### `int GetOneLiner(object oNPC = OBJECT_SELF)`
> Determine whether and which one-liner an NPC has available

#### `int GetPersuadeAttempt(object oPC, int nCheck = 1, object oNPC = OBJECT_SELF)`
> Determine whether the PC has attempted to persuade an NPC.
> nCheck is used for NPCs with multiple persuade checks in their
> conversation tree.

#### `void SetPersuadeAttempt(object oPC, int nCheck = 1, object oNPC = OBJECT_SELF)`
> Indicate that the PC attempted to persuade the NPC

#### `int GetDidPersuade(object oPC, int nCheck = 1, object oNPC = OBJECT_SELF)`
> Determine whether the PC has successfully persuaded the NPC

#### `void SetDidPersuade(object oPC, int nCheck = 1, object oNPC = OBJECT_SELF)`
> Indicate that the PC persuaded the NPC

#### `void SetThreaten(object oPC, object oNPC = OBJECT_SELF)`
> Indicate that the PC attempted to threaten the NPC

#### `int GetThreaten(object oPC, object oNPC = OBJECT_SELF)`
> Determine if the PC attempted to threaten the NPC

#### `void SetFriendly(object oPC, int bFriendly = TRUE, object oNPC = OBJECT_SELF)`
> Indicate that the PC did something friendly
> use FALSE if the PC was nasty
> This increments/decrements a variable on the PC and
> can be looked up to see how many friendly or nasty acts
> a player has committed to this NPC.

#### `int GetFriendly(object oPC, object oNPC = OBJECT_SELF)`
> Check how friendly/nasty the PC has been to this NPC

#### `object GetEventRouter()`
> Return the appropriate event router for this chapter.
> This function will create the event router if it doesn't
> already exist.

#### `string GetEventRouterTag()`
> Return the appropriate event router tag for this chapter

#### `object CreateEventRouter()`
> Create the appropriate event router for this chapter
> in the starting location. The event router should be an
> invisible object.

#### `int ThreatenCheck(int nDifficulty, object oPC, object oNPC = OBJECT_SELF)`
> Threaten check
> Formula: (PC level + cha mod + d20) - (NPC level + wis mod + d20)
> DIFFICULTY_EASY: > -2
> DIFFICULTY_MODERATE: > 0
> DIFFICULTY_HARD: > 4
> DIFFICULTY_IMPOSSIBLE: > 8

#### `int FriendCheck(int nDifficulty, object oPC, object oNPC = OBJECT_SELF)`
> Friendly check
> DIFFICULTY_EASY: has done at least one friendly thing
> DIFFICULTY_MODERATE: at least two
> DIFFICULTY_HARD: at least four
> DIFFICULTY_IMPOSSIBLE: at least six

#### `int MeanCheck(int nDifficulty, object oPC, object oNPC = OBJECT_SELF)`
> Unfriendly check
> DIFFICULTY_EASY: has done at least one unfriendly thing
> DIFFICULTY_MODERATE: at least two
> DIFFICULTY_HARD: at least four
> DIFFICULTY_IMPOSSIBLE: at least six

#### `void PersistentConversationAttempt(object oPC, string sConvo = "", int bPrivate = FALSE)`
> This causes the caller to try to start a conversation with the
> PC repeatedly with progressively longer delays.

#### `int GetInterjectionSet(object oPC, object oNPC = OBJECT_SELF)`
> Call to determine the current interjection set.
