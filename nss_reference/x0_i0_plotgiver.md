# `x0_i0_plotgiver.nss`

Source: `NSS/x0_/x0_i0_plotgiver.nss`  
15 functions · 9 constants

## Constants

| Constant | Type | Value | Note |
|---|---|---|---|
| `QUEST_NOT_TAKEN` | int | `0` |  |
| `QUEST_IN_PROGRESS` | int | `1` |  |
| `QUEST_COMPLETE` | int | `2` |  |
| `QUEST_COMPLETE_OTHER` | int | `3` |  |
| `sQuestVarname` | string | `"QUEST_STATUS"` |  |
| `sQuestSuffix` | string | `"_Q"` |  |
| `sQuestItemSuffix` | string | `"_QI"` |  |
| `sPlotItemSuffix` | string | `"_PI"` |  |
| `sRewardItemSuffix` | string | `"_RI"` |  |

## Functions

#### `string GetQuestTag(object oTarget = OBJECT_SELF, int nQuest = 1)`
> Get the tag for the given quest

#### `string GetQuestVarname(int nQuest = 1)`
> Get the NPC's local varname for the given quest

#### `string GetPlotItemTag(object oTarget = OBJECT_SELF, int nQuest = 1)`
> Return the tag used for the given NPC's plot item
> for the specified quest.

#### `string GetQuestItemTag(object oTarget = OBJECT_SELF, int nQuest = 1)`
> Return the tag used for the given NPC's quest item
> for the specified quest.

#### `string GetRewardItemTag(object oTarget = OBJECT_SELF, int nQuest = 1)`
> Return the tag used for the given NPC's reward item
> for the specified quest.

#### `void SetOnQuest(object oPC, int nQuest = 1, object oNPC = OBJECT_SELF)`
> Call when a PC takes the quest

#### `void SetQuestDone(object oPC, int nQuest = 1, object oNPC = OBJECT_SELF)`
> Call when a PC completes a quest

#### `int GetQuestStatus(object oPC, int nQuest = 1, object oNPC = OBJECT_SELF)`
> Call to determine the status of the quest relative to this PC
> returns one of:
> QUEST_NOT_TAKEN
> QUEST_IN_PROGRESS
> QUEST_COMPLETE
> QUEST_COMPLETE_OTHER -- quest is complete, but by someone else

#### `void GiveQuestItem(object oPC, int nQuest = 1, object oNPC = OBJECT_SELF)`
> Give a PC the quest item

#### `void GiveRewardItem(object oPC, int nQuest = 1, object oNPC = OBJECT_SELF)`
> Give a PC the reward item

#### `int HasQuestItem(object oPC, int nQuest = 1, object oNPC = OBJECT_SELF)`
> See if a PC is carrying the quest item

#### `int HasPlotItem(object oPC, int nQuest = 1, object oNPC = OBJECT_SELF)`
> See if a PC is carrying the plot item

#### `int HasRewardItem(object oPC, int nQuest = 1, object oNPC = OBJECT_SELF)`
> See if a PC is carrying the reward item

#### `void TakePlotItem(object oPC, int nQuest = 1, object oNPC = OBJECT_SELF)`
> Remove a plot item from a PC

#### `void TakeQuestItem(object oPC, int nQuest = 1, object oNPC = OBJECT_SELF)`
> Remove a quest item from a PC
