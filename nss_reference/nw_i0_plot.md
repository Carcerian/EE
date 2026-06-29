# `nw_i0_plot.nss`

Source: `NSS/nw_/nw_i0_plot.nss`  
45 functions · 16 constants

## Constants

| Constant | Type | Value | Note |
|---|---|---|---|
| `DC_EASY` | int | `0` |  |
| `DC_MEDIUM` | int | `1` |  |
| `DC_HARD` | int | `2` |  |
| `DC_SUPERIOR` | int | `3` |  |
| `DC_MASTER` | int | `4` |  |
| `DC_LEGENDARY` | int | `5` |  |
| `DC_EPIC` | int | `6` |  |
| `G_CLASSCHANCE` | int | `70` |  |
| `XP_VERY_LOW` | int | `1` | 50 xp |
| `XP_LOW` | int | `2` | 100 xp |
| `XP_MEDIUM_LOW` | int | `3` | 150 xp |
| `XP_MEDIUM` | int | `4` | 250 xp |
| `XP_MEDIUM_HIGH` | int | `5` | 500 xp |
| `XP_HIGH` | int | `6` | 1000 xp |
| `XP_VERY_HIGH` | int | `7` | 2000 xp |
| `XP_EPIC` | int | `8` | 5000 xp |

## Functions

#### `int plotCanRemoveXP(object oPC, int nPenalty)`
> returns true if the player can afford to lose the indicated amount of XP without losing  a level

#### `int GetCanCastHealingSpells(object oPC)`

#### `int DoOnce()`

#### `void DebugSpeak(string s)`

#### `object GetMyMaster()`

#### `int IsRecall()`

#### `void DimensionHop(object oTarget)`

#### `int CanSeePlayer()`

#### `void EscapeArea(int bRun = TRUE, string sTag = "NW_EXIT")`

#### `int HasItem(object oCreature, string s)`

#### `void TakeGold(int nAmount, object oGoldHolder, int bDestroy = TRUE)`

#### `object GetNearestPC()`

#### `void SetIsEnemy(object oTarget)`

#### `int AutoDC(int DC, int nSkill, object oTarget)`
> Provide a scaled skill check DC based on the DC_* constant passed in
> DC      -  DC_EASY  DC_MEDIUM  DC_HARD  DC_SUPERIOR  DC_MASTER  DC_LEGENDARY  DC_EPIC
> nSkill  - SKILL_* constant
> oTarget - creature that is going to perform the check;

#### `void AutoAlignG(int DC, object oTarget)`

#### `void AutoAlignE(int DC, object oTarget)`

#### `void DoGiveXP(string sJournalTag, int nPercentage, object oTarget, int QuestAlignment = ALIGNMENT_NEUTRAL)`

#### `void RewardXP(string sJournalTag, int nPercentage, object oTarget, int QuestAlignment = ALIGNMENT_NEUTRAL, int bAllParty = TRUE)`

#### `void RewardGP(int GP, object oTarget, int bAllParty = TRUE)`

#### `int CheckCharismaMiddle()`

#### `int CheckCharismaNormal()`

#### `int CheckCharismaLow()`

#### `int CheckCharismaHigh()`

#### `int CheckIntelligenceLow()`

#### `int CheckIntelligenceNormal()`

#### `int CheckIntelligenceHigh()`

#### `int CheckWisdomHigh()`

#### `int GetWisdom(object oTarget)`
> Return the wisdom of oTarget

#### `int GetIntelligence(object oTarget)`
> Return the Intelligence of the Target

#### `int GetCharisma(object oTarget)`
> Return the Charisma of the Target

#### `int GetNumItems(object oTarget, string sItem)`
> Return the numer of items oTarget possesses from type sItem (Tag)

#### `void GiveNumItems(object oTarget, string sItem, int nNumItems)`
> Gives the item with the ResRef sItem to creature oTarget nNumItems times

#### `void TakeNumItems(object oTarget, string sItem, int nNumItems)`
> Remove nNumItems Items of Type sItem (Tag) from oTarget

#### `void PlayCharacterTheme(int nTheme)`
> plays the correct character theme
> assumes OBJECT_SELF is in the area

#### `void PlayOldTheme()`
> plays the old theme for the area
> assumes OBJECT_SELF is in the area

#### `int GetPLocalInt(object oPC, string sLocalName)`

#### `void SetPLocalInt(object oPC, string sLocalName, int nValue)`

#### `void RemoveEffects(object oDead)`
> removes all negative effects

#### `void gplotAppraiseOpenStore(object oStore, object oPC, int nBonusMarkUp = 0, int nBonusMarkDown = 0)`
> starts store using appraise skill

#### `void gplotAppraiseFavOpenStore(object oStore, object oPC, int nBonusMarkUp = 0, int nBonusMarkDown = 0)`
> starts store with favorable appraise check

#### `int CheckDCStr(int DC, int nSkill, object oTarget)`
> Do a DC check and modify the skill by the Target's Strength modifier

#### `int GetIsPlayerCharacter(object oTarget)`
> Check to see if target is PC and not DM

#### `void Reward_2daXP(object oPC, int nRow, int bAllParty = TRUE, int nPercentage = 100)`
> Reward Experience based on an entry in the des_xp_rewards 2da file

#### `void PlaySpeakSoundByStrRef(int nStrRef)`
> Both speak a string ref as well as play the associate sound file

#### `int GetNPCEasyMark(object oTarget)`
> returns a value that will be subtracted from the
> oTarget's DC to resist APpraise or Persuasion
