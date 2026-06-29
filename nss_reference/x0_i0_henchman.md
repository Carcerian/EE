# `x0_i0_henchman.nss`

Source: `NSS/x0_/x0_i0_henchman.nss`  
100 functions · 16 constants

## Constants

| Constant | Type | Value | Note |
|---|---|---|---|
| `X0_NUMBER_HENCHMEN` | int | `3` |  |
| `X2_NUMBER_HENCHMEN` | int | `2` | This won't be the same as the GetMaxHenchmen() function due to followers |
| `sDeekin` | string | `"X0_HEN_DEE"` |  |
| `sDorna` | string | `"X0_HEN_DOR"` |  |
| `sXandos` | string | `"X0_HEN_XAN"` |  |
| `sHenchmanDeathVarname` | string | `"NW_L_HEN_I_DIED"` |  |
| `sIsHiredVarname` | string | `"X0_IS_CURRENTLY_HIRED"` |  |
| `sLastMasterVarname` | string | `"X0_LAST_MASTER_TAG"` |  |
| `sHenchmanKilledSuffix` | string | `"_GOTKILLED"` |  |
| `sHenchmanResurrectedSuffix` | string | `"_RESURRECTED"` |  |
| `sHenchmanDyingVarname` | string | `"X0_HEN_IS_DYING"` |  |
| `sStoredHenchmanVarname` | string | `"X0_HEN_STORED"` |  |
| `DELAY_BETWEEN_RESPAWN_CHECKS` | float | `3.0f` |  |
| `HENCHMEN_DIE_ANIM_DURATION` | float | `6500000000.0f` |  |
| `MAX_RESPAWN_WAIT` | float | `60.0f` |  |
| `sGoHomeScript` | string | `"x0_ch_hen_gohome"` |  |

## Functions

#### `void CopyHenchmanLocals(object oSource, object oTarget)`
> Copy all henchman-related local variables from source to target.
> Used when henchmen level up to keep variables consistent between
> the two copies of the henchman.
> This is a good function to look at to see what the local variables
> used on henchmen are.

#### `void SetHasMet(object oPC, object oHench = OBJECT_SELF)`
> Use when the player first meets the henchman/NPC
> This uses local variables, not campaign variables.

#### `int GetHasMet(object oPC, object oHench = OBJECT_SELF)`
> Returns TRUE if the player has met this henchman
> This uses local variables, not campaign variables.

#### `void HireHenchman(object oPC, object oHench = OBJECT_SELF, int bAdd = TRUE)`
> Can be used for both initial hiring and rejoining.

#### `void FireHenchman(object oPC, object oHench = OBJECT_SELF)`
> Use to fire the henchman

#### `void QuitHenchman(object oPC, object oHench = OBJECT_SELF)`
> Used when the henchman quits

#### `int GetIsHired(object oHench = OBJECT_SELF)`
> Returns TRUE if the henchman is currently hired

#### `void SetLastMaster(object oPC, object oHench = OBJECT_SELF)`
> Set the last master

#### `object GetLastMaster(object oHench = OBJECT_SELF)`
> Returns the last master of this henchman (useful for death situations)

#### `void SetPlayerHasHired(object oPC, object oHench = OBJECT_SELF, int bHired = TRUE)`
> Indicate whether the player has ever hired this henchman

#### `int GetPlayerHasHired(object oPC, object oHench = OBJECT_SELF)`
> Determine whether the player has ever hired this henchman

#### `void SetPlayerHasHiredInCampaign(object oPC, object oHench = OBJECT_SELF, int bHired = TRUE)`
> Indicate whether the player has ever hired this henchman in this
> campaign.

#### `int GetPlayerHasHiredInCampaign(object oPC, object oHench = OBJECT_SELF)`
> Indicate whether the player has ever hired this henchman in this
> campaign.

#### `int GetWorkingForPlayer(object oPC, object oHench = OBJECT_SELF)`
> Determine whether the henchman is currently working
> for this PC.

#### `void SetDidQuit(object oPC, object oHench = OBJECT_SELF, int bQuit = TRUE)`
> Set whether the henchman quit this player's employ

#### `int GetDidQuit(object oPC, object oHench = OBJECT_SELF)`
> Determine if the henchman quit

#### `int GetCanLevelUp(object oPC, object oHench = OBJECT_SELF)`
> Checks to see if the henchman can level up.
> Can only level up if player is 2 or more levels
> higher than henchman.
> MAX = Level 14

#### `object DoLevelUp(object oPC, object oHench = OBJECT_SELF)`
> Levels the henchman up to be one level less than player.
> Returns the new creature.

#### `void StoreHenchmanItems(object oPC, object oHench)`
> Store all items in the henchman's inventory in the campaign DB,
> skipping those items which have the henchman's tag in their
> name.
> This is paired with RetrieveHenchmanItems for the leveling-up
> process.

#### `void RetrieveHenchmanItems(object oPC, object oHench)`
> Retrieve (and then delete) all henchman inventory items out of
> the campaign DB, putting them in the inventory of the henchman.
> This is paired with StoreHenchmanItems for the leveling-up
> process.

#### `void SetHenchmanDying(object oHench = OBJECT_SELF, int bIsDying = TRUE)`
> Wrapper function added to fix bugs in the dying-state
> process. Need to figure out whenever his value changes.

#### `void SetDidDie(int bDie = TRUE, object oHench = OBJECT_SELF)`
> Set on the henchman to indicate s/he died; can also be used to
> unset this variable.

#### `int GetDidDie(object oHench = OBJECT_SELF)`
> Returns TRUE if the henchman died.
> UNLIKE original, does NOT reset the value -- use
> SetDidDie(FALSE) to do that.

#### `void SetKilled(object oPC, object oHench = OBJECT_SELF, int bKilled = TRUE)`
> Set got killed

#### `int GetKilled(object oPC, object oHench = OBJECT_SELF)`
> Determine if this PC got the henchman killed

#### `void SetResurrected(object oPC, object oHench = OBJECT_SELF, int bResurrected = TRUE)`
> Set that this PC resurrected the henchman

#### `int GetResurrected(object oPC, object oHench = OBJECT_SELF)`
> Determine if this PC resurrected the henchman

#### `void RespawnHenchman(object oHench = OBJECT_SELF)`
> Respawn the henchman, by preference at the master's current
> respawn point, or at the henchman's starting location otherwise.

#### `void KeepDead(object oHench = OBJECT_SELF)`
> Keep dead by playing the appropriate death animation for the
> maximum wait until respawn.

#### `void StopKeepingDead(object oHench = OBJECT_SELF)`
> Stop keeping dead by playing the 'woozy' standing animation.

#### `void RaiseForRespawn(object oPC, object oHench = OBJECT_SELF)`
> Raise and freeze henchman to 1 hp so s/he can be stabilized

#### `int GetHasMaxWaitPassed(int nChecks)`
> See if our maximum wait time has passed

#### `void RespawnCheck(object oPC, int nChecks = 0, object oHench = OBJECT_SELF)`
> Do the checking to see if we respawn -- this function works
> in a circle with DoRespawnCheck.

#### `void DoRespawnCheck(object oPC, int nChecks, object oHench = OBJECT_SELF)`
> Perform a single respawn check -- this function works
> in a circle with RespawnCheck.

#### `void DoRespawn(object oPC, object oHench = OBJECT_SELF)`
> This function actually invokes the respawn.

#### `void PreRespawnSetup(object oHench = OBJECT_SELF)`
> Set up before the respawn

#### `void PostRespawnCleanup(object oHench = OBJECT_SELF)`
> Clean up after the respawn.

#### `int GetIsHenchmanDying(object oHench = OBJECT_SELF)`
> Determine if this henchman is currently dying

#### `void LevelUpXP1Henchman(object oPC)`
> levels up the henchman assigned to oPC

#### `void StoreCampaignHenchman(object oPC)`
> Call this function when the PC is about to leave a module
> to enable restoration of the henchman on re-entry into the
> sequel module. Both modules must use the same campaign db
> for this to work.

#### `void RetrieveCampaignHenchman(object oPC)`
> Call this function when a PC enters a sequel module to restore
> the henchman (complete with inventory). The function
> StoreCampaignHenchman must have been called first, and both
> modules must use the same campaign db. (See notes in x0_i0_campaign.)
> The restored henchman will automatically be re-hired and will be
> created next to the PC.

#### `void LevelHenchmanUpTo(object oHenchman, int nLevel, int nClass2 = CLASS_TYPE_INVALID, int nMaxLevelInSecondClass = 0, int nPackageClass1 = PACKAGE_INVALID, int nPackageClass2 = PACKAGE_INVALID)`
> Levels a henchman up to the given level, alternating
> between the first and second classes if they are multiclassed.

#### `int GetIsFollower(object oHench)`
> returns true if oHench is a follower

#### `void SetIsFollower(object oHench, int bValue = TRUE)`
> sets whether oHench is a follower or not

#### `void RemoveAllFollowers(object oPC, int bRemoveAll = FALSE)`
> removes all followers
> if bRemoveAll=TRUe then remove normal hencies too

#### `void WrapCommandable(int bCommand, object oHench)`
> had to add this commandable wrapper to track down a bug in the henchmen

#### `void brentDebug(string s)`

#### `void CopyHenchmanLocals(object oSource, object oTarget)`
> Copy all henchman-related local variables from source to target.
> Used when henchmen level up to keep variables consistent between
> the two copies of the henchman.
> This is a good function to look at to see what the local variables
> used on henchmen are.

#### `void SetHasMet(object oPC, object oHench = OBJECT_SELF)`
> Use when the player first meets the henchman

#### `int GetHasMet(object oPC, object oHench = OBJECT_SELF)`
> Returns TRUE if the player has met this henchman

#### `int GetIsFollower(object oHench)`
> returns true if oHench is a follower

#### `void SetIsFollower(object oHench, int bValue = TRUE)`
> sets whether oHench is a follower or not

#### `void RemoveAllFollowers(object oPC, int bRemoveAll = FALSE)`
> removes all followers
> if bRemoveAll=true, it removes
> all henchmen.

#### `int X2_GetNumberOfHenchmen(object oPC, int bFollowersInstead = FALSE)`
> count number of henchman
> if nFollowersInstead = TRUE then count the # of

#### `void X2_FireFirstHenchman(object oPC)`
> Fires the first henchman who is not
> a follower

#### `void HireHenchman(object oPC, object oHench = OBJECT_SELF, int bAdd = TRUE)`
> Can be used for both initial hiring and rejoining.

#### `void FireHenchman(object oPC, object oHench = OBJECT_SELF)`
> Use to fire the PC's current henchman

#### `void QuitHenchman(object oPC, object oHench = OBJECT_SELF)`
> Used when the henchman quits

#### `int GetIsHired(object oHench = OBJECT_SELF)`
> Returns TRUE if the henchman is currently hired

#### `void SetLastMaster(object oPC, object oHench = OBJECT_SELF)`
> Set the last master

#### `object GetLastMaster(object oHench = OBJECT_SELF)`
> Returns the last master of this henchman (useful for death situations)

#### `void SetPlayerHasHired(object oPC, object oHench = OBJECT_SELF, int bHired = TRUE)`
> Indicate whether the player has ever hired this henchman

#### `int GetPlayerHasHired(object oPC, object oHench = OBJECT_SELF)`
> Determine whether the player has ever hired this henchman

#### `void SetPlayerHasHiredInCampaign(object oPC, object oHench = OBJECT_SELF, int bHired = TRUE)`
> Indicate whether the player has ever hired this henchman in this
> campaign.

#### `int GetPlayerHasHiredInCampaign(object oPC, object oHench = OBJECT_SELF)`
> Indicate whether the player has ever hired this henchman in this
> campaign.

#### `int GetWorkingForPlayer(object oPC, object oHench = OBJECT_SELF)`
> Determine whether the henchman is currently working
> for this PC.

#### `void SetDidQuit(object oPC, object oHench = OBJECT_SELF, int bQuit = TRUE)`
> Set whether the henchman quit this player's employ

#### `int GetDidQuit(object oPC, object oHench = OBJECT_SELF)`
> Determine if the henchman quit

#### `int GetCanLevelUp(object oPC, object oHench = OBJECT_SELF)`
> Checks to see if the henchman can level up.
> Can only level up if player is 2 or more levels
> higher than henchman.
> MIN = Level 4
> MAX = Level 14

#### `object DoLevelUp(object oPC, object oHench = OBJECT_SELF)`
> Levels the henchman up to be one level less than player.
> Returns the new creature.

#### `void StoreHenchmanItems(object oPC, object oHench)`
> Store all items in the henchman's inventory in the campaign DB.

#### `void RetrieveHenchmanItems(object oPC, object oHench)`
> Retrieve (and then delete) all henchman inventory items out of
> the campaign DB, putting them in the inventory of the henchman.

#### `void SetDidDie(int bDie = TRUE, object oHench = OBJECT_SELF)`
> Set on the henchman to indicate s/he died; can also be used to
> unset this variable.

#### `int GetDidDie(object oHench = OBJECT_SELF)`
> Returns TRUE if the henchman died

#### `void SetKilled(object oPC, object oHench = OBJECT_SELF, int bKilled = TRUE)`
> Set got killed

#### `int GetKilled(object oPC, object oHench = OBJECT_SELF)`
> Determine if this PC got the henchman killed

#### `void SetResurrected(object oPC, object oHench = OBJECT_SELF, int bResurrected = TRUE)`
> Set that this PC resurrected the henchman

#### `int GetResurrected(object oPC, object oHench = OBJECT_SELF)`
> Determine if this PC resurrected the henchman

#### `void RespawnHenchman(object oHench = OBJECT_SELF)`
> Handle the respawning of the henchman back at either the
> respawn location or the starting location

#### `void KeepDead(object oHench = OBJECT_SELF)`
> Keep dead by playing the appropriate death animation for the
> maximum wait until respawn.

#### `void StopKeepingDead(object oHench = OBJECT_SELF)`
> Stop keeping dead by playing the 'woozy' standing animation.

#### `void PartialRes(object oHench)`
> Does a partial restoration to get rid of negative effects

#### `void RaiseForRespawn(object oPC, object oHench = OBJECT_SELF)`
> Raise and freeze henchman to 1 hp so s/he can be stabilized

#### `int GetHasMaxWaitPassed(int nChecks)`
> See if our maximum wait time has passed

#### `void RespawnCheck(object oPC, int nChecks = 0, object oHench = OBJECT_SELF)`
> Do the checking to see if we respawn -- this function works
> in a circle with DoRespawnCheck.

#### `void DoRespawnCheck(object oPC, int nChecks, object oHench = OBJECT_SELF)`
> Perform a single respawn check -- this function works
> in a circle with RespawnCheck.

#### `void DoRespawn(object oPC, object oHench = OBJECT_SELF)`
> This function actually invokes the respawn.

#### `void PreRespawnSetup(object oHench = OBJECT_SELF)`

#### `void PostRespawnCleanup(object oHench = OBJECT_SELF)`

#### `int GetIsHenchmanDying(object oHench = OBJECT_SELF)`
> Determine if this henchman is currently dying

#### `void SetHenchmanDying(object oHench = OBJECT_SELF, int bIsDying = TRUE)`
> Wrapper function added to fix bugs in the dying-state
> process. Need to figure out whenever his value changes.

#### `void StoreCampaignHenchman(object oPC)`
> Call this function when the PC is about to leave a module
> to enable restoration of the henchman on re-entry into the
> sequel module. Both modules must use the same campaign db
> for this to work.

#### `void RetrieveCampaignHenchman(object oPC)`
> Call this function when a PC enters a sequel module to restore
> the henchman (complete with inventory). The function
> StoreCampaignHenchman must have been called first, and both
> modules must use the same campaign db. (See notes in x0_i0_campaign.)
> The restored henchman will automatically be re-hired and will be
> created next to the PC.
> Any object in the module with the same tag as the henchman will be
> destroyed (to remove duplicates).

#### `void LevelHenchmanUpTo(object oHenchman, int nLevel, int nClass2 = CLASS_TYPE_INVALID, int nMaxLevelInSecondClass = 0, int nPackageClass1 = PACKAGE_INVALID, int nPackageClass2 = PACKAGE_INVALID)`
> Levels a henchman up to the given level, alternating
> between the first and second classes if they are multiclassed.
> 0 as a max level means they will try to keep their levels balanced

#### `int AdjustXP2Levels(int nLevel, int nMin = 13, int nAdjust = 2)`
> Adjusts the levels for the henchmen

#### `void LevelUpXP1Henchman(object oPC)`
> levels up the henchman assigned to oPC
> Modified for XP2 so that it cycles through
> all the available henchmen and levels them all up

#### `void LevelUpAribeth(object oAribeth)`
> Created By: Brent
> Created On:

#### `void SetNumberOfRandom(string sVariableName, object oHench, int nNum)`
> Created By:
> Created On:

#### `string GetDialogFile(object oPC, string sHenchmenDlg, string sPreHenchDlg, object oHench = OBJECT_SELF)`
> Oct 14 - added the oHench parameters

#### `string GetDialogFileToUse(object oPC, object oHench = OBJECT_SELF)`
