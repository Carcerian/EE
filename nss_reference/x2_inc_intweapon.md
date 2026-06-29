# `x2_inc_intweapon.nss`

Source: `NSS/x2_/x2_inc_intweapon.nss`  
52 functions · 13 constants

## Constants

| Constant | Type | Value | Note |
|---|---|---|---|
| `X2_IW_INTERJECTION_CHANCE_EQUIP` | int | `25` |  |
| `X2_IW_INTERJECTION_TYPE_EQUIP` | int | `1` |  |
| `X2_IW_INTERJECTION_EQUIP_COUNT` | int | `5` |  |
| `X2_IW_INTERJECTION_CHANCE_UNEQUIP` | int | `25` |  |
| `X2_IW_INTERJECTION_TYPE_UNEQUIP` | int | `2` |  |
| `X2_IW_INTERJECTION_UNEQUIP_COUNT` | int | `5` |  |
| `X2_IW_INTERJECTION_CHANCE_BATTLECRY` | int | `8` |  |
| `X2_IW_INTERJECTION_TYPE_BATTLECRY` | int | `3` |  |
| `X2_IW_INTERJECTION_BATTLECRY_COUNT` | int | `20` |  |
| `X2_IW_INTERJECTION_CHANCE_ONHIT_CRE` | int | `20` |  |
| `X2_IW_INTERJECTION_TYPE_ONHIT_CRE` | int | `4` |  |
| `X2_IW_INTERJECTION_TYPE_TRIGGER` | int | `5` |  |
| `X2_IW_CURSE_ENHANCEMENT_DURATION` | int | `10` |  |

## Functions

#### `string IWGetWeaponDialogName(object oWeapon)`
> Return the Dialog ResRef Name of the intelligent weapon passed in.

#### `void IWSWrapper(object oPlayer, object oWeapon)`
> Wrapper to use IWSpawnInWeaponCreature with Delaycommand

#### `object IWSpawnInWeaponCreature(object oPlayer, object oWeapon, int bEquip = TRUE)`
> Spawns in a null human creature for oWeapon worn by oPlayer.

#### `void IWStartIntelligentWeaponConversation(object oPlayer, object oWeapon)`
> Start a conversation with the intelligent weapon. This will make the
> weapon jump out of the players hands onto a null human and start the conv.

#### `void IWEndIntelligentWeaponConversation(object oWeaponCreature, object oPlayer)`
> End an intelligent weapon conversation, despawning the null human that wields
> the weapon and moving the weapon back into the players hands. This should be
> called on the OnEnd and OnAbort scripts of the weapon dialog

#### `int IWGetIsInIntelligentWeaponConversation(object oPlayer)`
> Returns TRUE if oPlayer is currently engaged in a conversation with his
> intelligent weapon

#### `void IWSetConversationCondition(object oPlayer, int nType, int nValue)`
> Sets the starting conditions for the next intelligent weapon conversation

#### `int IWGetConversationCondition(object oPlayer, int nType)`
> Gets the starting conditions for current intelligent weapon conversation

#### `void IWClearConversationConditions(object oPlayer)`
> Clear current intelligent weapon starting conditions

#### `void IWSetCreatureHadOneLiner(object oCreature, int bValue)`

#### `void IWPlayRandomEquipComment(object oPlayer, object oWeapon)`

#### `void IWPlayRandomUnequipComment(object oPlayer, object oWeapon)`

#### `void IWPlayRandomHitQuote(object oPlayer, object oWeapon, object oTarget)`

#### `object IWGetIntelligentWeaponEquipped(object oPlayer)`

#### `void IWCreateIntelligentWeapon(object oWeapon, int nLevel = 1)`
> Transforms the weapon passed in oWeapon into an intelligent weapon, preserving
> all item properties stored on the weapon.
> nLevel - The power level of the weapon - unused at the moment (1 = default)

#### `void IWSetEnhancementAndDrainLevel(object oWeapon, int nAddition, int bRemove = FALSE)`

#### `int IWGetStaticEnhancementBonus(object oWeapon)`

#### `void IWSetTalkedTo(object oPlayer, string sWeaponTag, int nNumTimes = 1)`
> Sets the number of times a player has talked to the intelligent weapon
> This information is stored on the player

#### `int IWGetTalkedTo(object oPlayer, string sWeaponTag)`
> Gets the number of times a player has talked to the intelligent weapon
> This information is stored on the player

#### `void IWSetQuestionAsked(object oPlayer, string sWeaponTag, int nQuestion)`
> Sets the asked flag for question no. nQuestion, in sWeaponTag's conversation
> on the Player

#### `int IWGetQuestionAsked(object oPlayer, string sWeaponTag, int nQuestion)`
> Returns the asked flag for question no. nQuestion, in sWeaponTag's conversation
> on the Player

#### `int IWGetIsHotUChapter1()`
> Helper Function. Returns TRUE if we currently play Hordes of the Underdark
> Chapter 1

#### `int IWGetIsHotUChapter2()`
> Helper Function. Returns TRUE if we currently play Hordes of the Underdark
> Chapter 2

#### `int IWGetIsHotUChapter3()`
> Helper Function. Returns TRUE if we currently play Hordes of the Underdark
> Chapter 3

#### `string IWGetWeaponDialogName(object oWeapon)`
> Return the Dialog ResRef Name of the intelligent weapon passed in.

#### `object IWSpawnInWeaponCreature(object oPlayer, object oWeapon, int bEquip = TRUE)`
> Spawns in a null human creature for oWeapon worn by oPlayer.

#### `void IWSWrapper(object oPlayer, object oWeapon)`
> Wrapper to use IWSpawnInWeaponCreature with Delaycommand

#### `void IWStartIntelligentWeaponConversation(object oPlayer, object oWeapon)`
> Start a conversation with the intelligent weapon. This will make the
> weapon jump out of the players hands onto a null human and start the conv.

#### `void IWEndIntelligentWeaponConversation(object oWeaponCreature, object oPlayer)`
> End an intelligent weapon conversation,
> This should be called on the OnEnd and OnAbort scripts of the weapon dialog

#### `int IWGetIsInIntelligentWeaponConversation(object oPlayer)`
> Returns TRUE if oPlayer is currently engaged in a conversation with his
> intelligent weapon

#### `void IWSetConversationCondition(object oPlayer, int nType, int nValue)`
> Sets the starting conditions for the next intelligent weapon conversation

#### `void IWClearConversationConditions(object oPlayer)`
> Clear current intelligent weapon starting conditions

#### `int IWGetConversationCondition(object oPlayer, int nType)`
> Gets the starting conditions for current intelligent weapon conversation

#### `void IWPlayRandomEquipComment(object oPlayer, object oWeapon)`

#### `void IWPlayRandomUnequipComment(object oPlayer, object oWeapon)`

#### `void IWSetCreatureHadOneLiner(object oCreature, int bValue)`

#### `int IWGetCreatureHadOneLiner(object oCreature)`

#### `void IWPlayRandomHitQuote(object oPlayer, object oWeapon, object oTarget)`

#### `void IWPlayTriggerQuote(object oPlayer, object oWeapon, int nID)`
> Play a Trigger Quote

#### `void IWSetIntelligentWeaponEquipped(object oPlayer, object oWeapon)`

#### `object IWGetIntelligentWeaponEquipped(object oPlayer)`

#### `void IWCreateIntelligentWeapon(object oWeapon, int nLevel = 1)`
> Transforms the weapon passed in oWeapon into an intelligent weapon, preserving
> all item properties stored on the weapon.
> nLevel - The power level of the weapon - unused at the moment (1 = default)

#### `void IWSetTalkedTo(object oPlayer, string sWeaponTag, int nNumTimes = 1)`
> Sets the number of times a player has talked to the intelligent weapon
> This information is stored on the player.

#### `int IWGetTalkedTo(object oPlayer, string sWeaponTag)`
> gets the number of times a player has talked to the intelligent weapon
> This information is stored on the player

#### `void IWSetQuestionAsked(object oPlayer, string sWeaponTag, int nQuestion)`
> Sets the asked flag for question no. nQuestion, in sWeaponTag's conversation
> on the Player

#### `int IWGetQuestionAsked(object oPlayer, string sWeaponTag, int nQuestion)`
> Returns the asked flag for question no. nQuestion, in sWeaponTag's conversation
> on the Player

#### `int IWGetIsHotUChapter1()`
> Helper Function. Returns TRUE if we currently play Hordes of the Underdark
> Chapter 1

#### `int IWGetIsHotUChapter2()`
> Helper Function. Returns TRUE if we currently play Hordes of the Underdark
> Chapter 2

#### `int IWGetIsHotUChapter3()`
> Helper Function. Returns TRUE if we currently play Hordes of the Underdark
> Chapter 3

#### `void IWClearConversationCondition(object oPlayer)`
> Someone made a typo....

#### `int IWGetStaticEnhancementBonus(object oWeapon)`
> Returns the current permanent part of oWeapon's enhancement bonus

#### `void IWSetEnhancementAndDrainLevel(object oWeapon, int nAddition, int bRemove = FALSE)`
> Function to manage the intelligent sword's drain abilityin the
> official campaign.
> nAddition: The number to increase the enchantment bonus by
> The function will fail whenever any wrong value has been entered
