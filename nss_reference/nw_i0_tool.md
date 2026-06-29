# `nw_i0_tool.nss`

Source: `NSS/nw_/nw_i0_tool.nss`  
8 functions · 4 constants

## Constants

| Constant | Type | Value | Note |
|---|---|---|---|
| `DC_EASY` | int | `0` |  |
| `DC_MEDIUM` | int | `1` |  |
| `DC_HARD` | int | `2` |  |
| `G_CLASSCHANCE` | int | `70` |  |

## Functions

#### `int HasItem(object oCreature, string s)`

#### `void TakeGold(int nAmount, object oGoldHolder, int bDestroy = TRUE)`
> Created By: Brent
> Created On: November 2001

#### `int HasGold(int nAmount, object oGoldHolder)`
> Created By:
> Created On:

#### `int AutoDC(int DC, int nSkill, object oTarget)`
> AutoDC
> Returns a pass value based on the object's level and the suggested DC
> December 20 2001: Changed so that the difficulty is determined by the
> NPC's Hit Dice
> Created By: Brent, September 13 2001

#### `void DoGiveXP(string sJournalTag, int nPercentage, object oTarget, int QuestAlignment = ALIGNMENT_NEUTRAL)`

#### `void RewardPartyGP(int GP, object oTarget, int bAllParty = TRUE)`

#### `void RewardPartyXP(int XP, object oTarget, int bAllParty = TRUE)`

#### `int CheckPartyForItem(object oMember, string sItem)`
