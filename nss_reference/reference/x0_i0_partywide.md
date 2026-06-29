# `x0_i0_partywide.nss`

Source: `NSS/x0_/x0_i0_partywide.nss`  
52 functions · 0 constants

## Functions

#### `int GetNumberPartyMembers(object oPC)`
> Return the number of other players in the PC's party.
> Does NOT include associates.

#### `void SetLocalStringOnAll(object oPC, string sVarname, string value)`
> Given a varname, value, and PC, sets the variable on
> all members of the PC's party.
> For strings.

#### `void SetLocalIntOnAll(object oPC, string sVarname, int value)`
> Given a varname, value, and PC, sets the variable on
> all members of the PC's party.
> For ints.

#### `void SetLocalFloatOnAll(object oPC, string sVarname, float value)`
> Given a varname, value, and PC, sets the variable on
> all members of the PC's party.
> For floats.

#### `void SetLocalLocationOnAll(object oPC, string sVarname, location value)`
> Given a varname, value, and PC, sets the variable on
> all members of the PC's party.
> For locations.

#### `void SetLocalObjectOnAll(object oPC, string sVarname, object value)`
> Given a varname, value, and PC, sets the variable on
> all members of the PC's party.
> For objects.

#### `void SetCampaignDBStringOnAll(object oPC, string sVarname, string value)`
> Given a varname, value, and PC, sets the variable on
> all PC members of the PC's party.
> For strings.

#### `void SetCampaignDBIntOnAll(object oPC, string sVarname, int value)`
> Given a varname, value, and PC, sets the variable on
> all PC members of the PC's party.
> For ints.

#### `void SetCampaignDBFloatOnAll(object oPC, string sVarname, float value)`
> Given a varname, value, and PC, sets the variable on
> all PC members of the PC's party.
> For floats.

#### `void SetCampaignDBVectorOnAll(object oPC, string sVarname, vector value)`
> Given a varname, value, and PC, sets the variable on
> all PC members of the PC's party.
> For vectors.

#### `void SetCampaignDBLocationOnAll(object oPC, string sVarname, location value)`
> Given a varname, value, and PC, sets the variable on
> all PC members of the PC's party.
> For locations.

#### `void StoreCampaignDBObjectOnAll(object oPC, string sVarname, object value)`
> NOTE: this does not store a reference, it stores the entire actual object,
> including all of its inventory. Storing many objects can be highly resource-
> intensive! It should NOT be used like Set/GetLocalObject.
> Given a varname, value, and PC, stores the variable on
> all PC members of the PC's party.
> For objects.

#### `void DeleteCampaignDBVariableOnAll(object oPC, string sVarname)`
> Delete a campaign variable from all members of the PC's party.

#### `void GiveGoldToAllEqually(object oPC, int nGoldToDivide)`
> Given a gold amount, divides it equally among the party members
> of the given PC's party.
> None given to associates.

#### `void GiveGoldToAll(object oPC, int nGold)`
> Given a gold amount, gives that amount to all party members
> of the given PC's party.
> None given to associates.

#### `void GiveXPToAllEqually(object oPC, int nXPToDivide)`
> Given an XP amount, divides it equally among party members
> of the given PC's party.
> None given to associates.
> Tip: use with GetJournalQuestExperience(<journal tag>) to
> get the amount of XP assigned to that quest in the
> journal.

#### `void GiveXPToAll(object oPC, int nXP)`
> Given an XP amount, gives that amount to all party members
> of the given PC's party.
> None given to associates.
> Tip: use with GetJournalQuestExperience(<journal tag>)
> get the amount of XP assigned to that quest in the
> journal.

#### `void AdjustReputationWithFaction(object oPC, object oNPC, int nAdjustment)`
> This adjusts the reputation of all members of the PC's
> faction with all members of the NPC's faction by the
> specified amount.

#### `void ClearPersonalReputationWithFaction(object oPC, object oNPC)`
> This clears the personal reputation of all members of the
> PC's faction with all members of the NPC's faction.

#### `void ClearAssociateActions(object oPC, int bClearCombat = FALSE)`
> Clear the actions of all the PC's associates

#### `void ClearNearbyFriendActions(object oTarget = OBJECT_SELF, int bClearCombat = FALSE)`
> This clears the actions of all nearby friends,
> useful for stopping a battle in progress.

#### `void SurrenderAllToEnemies(object oSurrendering = OBJECT_SELF)`
> Cause all members of the faction of the given surrendering
> object to issue a SurrenderToEnemies call. Does not work
> on PCs, but DOES work on their associates.

#### `int GetIsItemPossessedByParty(object oPC, string sItemTag)`
> TRUE if any member of the PC's party has an item with the given tag

#### `object GetItemPossessedByParty(object oPC, string sItemTag)`
> Check for an item possessed by anyone in the PC's
> party. If not found, returns OBJECT_INVALID.

#### `void RemoveItemFromParty(object oPC, string sItemTag)`
> Remove an item from any party member who has it.
> Note: this assumes that the item is unique.

#### `void AdjustAlignmentOnAll(object oPC, int nAlignment, int nShift)`
> This adjusts the alignment of all members of the PC's
> faction

#### `int GetNumberPartyMembers(object oPC)`
> Return the number of players in the PC's party
> Does NOT include associates.

#### `void SetLocalStringOnAll(object oPC, string sVarname, string value)`
> Given a varname, value, and PC, sets the variable on
> all members of the PC's party, including associates.
> For strings.

#### `void SetLocalIntOnAll(object oPC, string sVarname, int value)`
> Given a varname, value, and PC, sets the variable on
> all members of the PC's party, including associates.
> For ints.

#### `void SetLocalFloatOnAll(object oPC, string sVarname, float value)`
> Given a varname, value, and PC, sets the variable on
> all members of the PC's party.
> For floats.

#### `void SetLocalLocationOnAll(object oPC, string sVarname, location value)`
> Given a varname, value, and PC, sets the variable on
> all members of the PC's party.
> For locations.

#### `void SetLocalObjectOnAll(object oPC, string sVarname, object value)`
> Given a varname, value, and PC, sets the variable on
> all members of the PC's party.
> For objects.

#### `void SetCampaignDBStringOnAll(object oPC, string sVarname, string value)`
> Given a varname, value, and PC, sets the variable on
> all members of the PC's party, including associates.
> For strings.

#### `void SetCampaignDBIntOnAll(object oPC, string sVarname, int value)`
> Given a varname, value, and PC, sets the variable on
> all members of the PC's party, including associates.
> For ints.

#### `void SetCampaignDBFloatOnAll(object oPC, string sVarname, float value)`
> Given a varname, value, and PC, sets the variable on
> all members of the PC's party.
> For floats.

#### `void SetCampaignDBVectorOnAll(object oPC, string sVarname, vector value)`
> Given a varname, value, and PC, sets the variable on
> all members of the PC's party.
> For vectors.

#### `void SetCampaignDBLocationOnAll(object oPC, string sVarname, location value)`
> Given a varname, value, and PC, sets the variable on
> all members of the PC's party.
> For locations.

#### `void StoreCampaignDBObjectOnAll(object oPC, string sVarname, object value)`
> Given a varname, value, and PC, stores the variable on
> all members of the PC's party.
> For objects.

#### `void DeleteCampaignDBVariableOnAll(object oPC, string sVarname)`
> Delete a campaign variable from all members of the PC's party.

#### `void GiveGoldToAllEqually(object oPC, int nGoldToDivide)`
> Given a gold value, divides it equally among the party members
> None given to associates.

#### `void GiveGoldToAll(object oPC, int nGold)`
> Given a gold value, gives that amount to all party members
> None given to associates.

#### `void GiveXPToAllEqually(object oPC, int nXPToDivide)`
> Given an XP value, divides it equally among party members
> None given to associates.
> Tip: use with GetJournalQuestExperience(<journal tag>) to
> get the amount of XP assigned to that quest in the
> journal.

#### `void GiveXPToAll(object oPC, int nXP)`
> Given an XP value, gives that amount to all party members.
> None given to associates.
> Tip: use with GetJournalQuestExperience(<journal tag>)
> get the amount of XP assigned to that quest in the
> journal.

#### `void AdjustReputationWithFaction(object oPC, object oNPC, int nAdjustment)`
> This adjusts the reputation of all members of the PC's
> faction with all members of the NPC's faction by the
> specified amount.

#### `void ClearPersonalReputationWithFaction(object oPC, object oNPC)`
> This clears the personal reputation of all members of the
> PC's faction with all members of the NPC's faction.

#### `void ClearAssociateActions(object oPC, int bClearCombat = FALSE)`
> Clear the actions of all the PC's associates

#### `void ClearNearbyFriendActions(object oTarget = OBJECT_SELF, int bClearCombat = FALSE)`
> This clears the actions of all nearby friends,
> useful for stopping a battle in progress.

#### `void SurrenderAllToEnemies(object oSurrendering = OBJECT_SELF)`
> Cause all members of the faction of the given surrendering
> object to issue a SurrenderToEnemies call. Does not work
> on PCs, but DOES work on their associates.

#### `int GetIsItemPossessedByParty(object oPC, string sItemTag)`
> TRUE if any member of the PC's party has an item with the given tag

#### `object GetItemPossessedByParty(object oPC, string sItemTag)`
> Check for an item possessed by anyone in the PC's
> party. If not found, returns OBJECT_INVALID.
> This only checks actual PCs, not associates.

#### `void RemoveItemFromParty(object oPC, string sItemTag)`
> Remove an item from any party member who has it.
> Note: this assumes that the item is unique.
> This only checks actual PCs, not associates.
> Note that this WILL destroy plot-flagged items!

#### `void AdjustAlignmentOnAll(object oPC, int nAlignment, int nShift)`
> This adjusts the alignment of all members of the PC's
> faction
