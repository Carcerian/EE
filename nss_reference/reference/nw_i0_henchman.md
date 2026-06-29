# `nw_i0_henchman.nss`

Source: `NSS/nw_/nw_i0_henchman.nss`  
30 functions · 8 constants

## Constants

| Constant | Type | Value | Note |
|---|---|---|---|
| `sDaelinTag` | string | `"NW_HEN_DAE"` |  |
| `sSharwynTag` | string | `"NW_HEN_SHA"` |  |
| `sLinuTag` | string | `"NW_HEN_LIN"` |  |
| `sGallowTag` | string | `"NW_HEN_GAL"` |  |
| `sGrimTag` | string | `"NW_HEN_GRI"` |  |
| `sBoddyTag` | string | `"NW_HEN_BOD"` |  |
| `INT_NUM_HENCHMEN` | int | `6` |  |
| `INT_FUDGE` | int | `3` | * used to help with figuring |

## Functions

#### `object PC()`
> debug function for displaying strings. Returns the first pc in the area

#### `void SetDidDie(int bDie)`
> Created By: Brent
> Created On:
> this is turned off again when the player talks to
> his henchman after finding him again.

#### `int GetDidDie()`

#### `void SetBeenHired(int bHired = TRUE, object oTarget = OBJECT_SELF)`
> Created By: Brent
> Created On:

#### `int GetBeenHired(object oTarget = OBJECT_SELF)`

#### `void SetWorkingForPlayer(object oPC)`
> This local is on the player
> it is true if this particular henchman
> is working for the player

#### `int GetWorkingForPlayer(object oPC)`

#### `object GetFormerMaster(object oHench = OBJECT_SELF)`

#### `void SetFormerMaster(object oPC, object oHench)`

#### `void SetStoryVar(int nChapter, int nVal, object oTarget = OBJECT_SELF)`
> Created By:  Brent
> Created On:

#### `int GetStoryVar(int nChapter, object oTarget = OBJECT_SELF)`

#### `void SetGreetingVar(int nChapter, object oPC)`
> Created By:  Brent
> Created On:

#### `int GetGreetingVar(int nChapter, object oPC)`

#### `string STR_PersonalItem(object oThing = OBJECT_SELF)`
> Created By: Brent
> Created On:

#### `string STR_QuestItem(int nChapter, object oThing = OBJECT_SELF)`

#### `string STR_RewardItem(int nChapter, object oThing = OBJECT_SELF)`

#### `void DestroyAllPersonalItems(object oPC)`
> Created By: Brent
> Created On:

#### `void GivePersonalItem(object oPC, object oHench = OBJECT_SELF)`
> Created By: Brent
> Created On:

#### `int HasPersonalItem(object oPC)`

#### `void StripAllPersonalItemsFromEveryone()`
> Created By: Brent
> Created On: April 9 2002

#### `int GetCanLevelUp(object oPC, object meLevel = OBJECT_SELF)`
> Created By: Brent
> Created On:

#### `void CopyLocals(object oSource, object oTarget)`
> Created By:   Brent
> Created On:

#### `object DoLevelUp(object oPC, object MeLevel = OBJECT_SELF)`
> assumes that a succesful GetCanLevelUp has already
> been tested.    Will level up character to one level
> less than player.
> meLevel defaults to object self unless another object is passed in
> returns the new creature

#### `int HasChapterQuestItem(int nChapter, object oPC)`
> Created By:  Brent
> Created On:

#### `void DestroyChapterQuestItem(int nChapter, object oPC)`

#### `void DestroyChapterRewardItem(int nChapter, object oPC)`

#### `int GetChapter()`
> Created By:   Brent
> Created On:

#### `string GetMyArea(object oThing = OBJECT_SELF)`

#### `int EndModule()`
> returns true if this is an end module

#### `void SpawnHenchman()`
> Spawns appropriate henchman into C1e, C2e, or C4
