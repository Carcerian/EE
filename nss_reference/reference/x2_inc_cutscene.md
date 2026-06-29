# `x2_inc_cutscene.nss`

Source: `NSS/x2_/x2_inc_cutscene.nss`  
227 functions · 11 constants

## Constants

| Constant | Type | Value | Note |
|---|---|---|---|
| `CUT_DELAY_TYPE_CUMULATIVE` | int | `0` |  |
| `CUT_DELAY_TYPE_CONSTANT` | int | `1` |  |
| `VANISH` | int | `2` |  |
| `CUT_CAMERA_HEIGHT_VERY_LOW` | int | `2` |  |
| `CUT_CAMERA_HEIGHT_LOW` | int | `3` |  |
| `CUT_CAMERA_HEIGHT_MEDIUM` | int | `4` |  |
| `CUT_CAMERA_HEIGHT_HIGH` | int | `5` |  |
| `CUT_CAMERA_HEIGHT_VERY_HIGH` | int | `6` |  |
| `RESTORE_TYPE_NONE` | int | `0` |  |
| `RESTORE_TYPE_NORMAL` | int | `1` |  |
| `RESTORE_TYPE_COPY` | int | `2` |  |

## Functions

#### `int CutSetActiveCutsceneForObject(object oObject, int nCutNum, int bMainPC = FALSE)`
> Use this function at the begining of a cutscene for each object involved in the cutscene.
> Notice that this function would fail if oObject already has another cutscene value (any
> number greater than 0). The function returns 0 on success, -1 otherwise.

#### `float GetShift(object oObject, int iShift)`

#### `void CutSetActiveCutscene(int nCutsceneNumber, int nDelayType, int bSetCutsceneObject = TRUE)`
> Set the current active cutscene. Any following delayed Cut* functions would run only if the
> initiating object has the same cutscene number as the global active one. A value of -1
> means that no cutscene is active (possible values for bDelayType: CUT_DELAY_TYPE_CUMULATIVE, CUT_DELAY_TYPE_CONSTANT.
> bSetCutsceneObject should be set to FALSE whenever calling this function more than once for the
> same cutscene but in another file. This would keep the original cutscene object that created
> all the cutscene effect so it would be possible to remove them when the cutscene ends.

#### `int GetActiveCutsceneNum()`
> Returns current global cutscene number.

#### `void RemoveCommandable(object oPC)`
> Used to clear commandable state FALSE in the event there are too many
> Used in this include only.

#### `void CutPlayVoiceChat(float fDelay, object oObject, int nChatID, int iShift = TRUE)`
> Plays voice chat nChatID for oObject.

#### `void CutRemoveEffects(float fDelay, object oObject, int iShift = TRUE)`
> Used to remove all effects from an object.
> Example: CutRemoveEffects(10.5, GetObjectByTag("guard1")) would remove all effects from guard1 after a 10.5 second delay.
> Notice that only effects created for the cutscene would be removed.

#### `void CutJumpAssociateToLocation(float fDelay, object oPC, location lLoc, int iShift = TRUE)`
> Jumps all associates of oPC to lLoc

#### `void CutActionStartConversation(float fDelay, object oNPC, object oPC, string szConversationFile, int iShift = TRUE)`
> Used for a conversation file when you need to have an NPC speak
> via a conversation instead of bubble text. The fDelay is used
> when timing is important.
> Example: CutActionStartConversation(5.0, oNPC, oPC, "my_conv"); would start the
> conversation file "my_conv" of the NPC, after a 5 sec delay, and
> the conversation subject would be the PC.

#### `void CutBeginConversation(float fDelay, object oTalker, object oTalkTo, string sConvFile, int iShift = TRUE)`
> Use this instead of CutActionStartConversation() to start a dialog
> without one object running to the other.

#### `void CutActionAttack(float fDelay, object oAttacker, object oAttackee, int bPassive = FALSE, int iShift = TRUE)`
> oAttacker would attack oAttackee.

#### `void CutActionCloseDoor(float fDelay, object oCloser, object oDoor, int iShift = TRUE)`

#### `void CutActionEquipItem(float fDelay, object oObject, object oItem, int InvSlot, int iShift = TRUE)`

#### `void CutActionUnequipItem(float fDelay, object oObject, object oItem, int iShift = TRUE)`

#### `void CutActionForceFollowObject(float fDelay, object oObject, object oFollow, float fFollowDistance = 0.0, int iShift = TRUE)`

#### `void CutActionLockObject(float fDelay, object oObject, object oTarget, int iShift = TRUE)`

#### `void CutActionUnLockObject(float fDelay, object oObject, object oTarget, int iShift = TRUE)`

#### `void CutActionMoveAwayFromLocation(float fDelay, object oObject, location lLoc, int bRun = FALSE, float fRange = 40.0, int iShift = TRUE)`

#### `void CutActionMoveAwayFromObject(float fDelay, object oObject, object oTarget, int bRun = FALSE, float fRange = 40.0, int iShift = TRUE)`

#### `void CutActionOpenDoor(float fDelay, object oObject, object oDoor, int iShift = TRUE)`

#### `void CutActionSit(float fDelay, object oObject, object oChair, int iShift = TRUE)`

#### `void CutSpeakString(float fDelay, object oSpeaker, string szString, int iShift = TRUE)`

#### `void CutSpeakStringByStrRef(float fDelay, object oSpeaker, int nStrRef, int iShift = TRUE)`

#### `void CutPlayAnimation(float fDelay, object oObject, int nAnimation, float fLength, int iShift = TRUE)`

#### `void CutJumpToLocation(float fDelay, object oPC, location lLoc, int iShift = TRUE)`

#### `void CutJumpToObject(float fDelay, object oPC, object oObject, int iShift = TRUE)`

#### `void CutActionMoveToObject(float fDelay, object oPC, object oTarget, int iRun, int iShift = TRUE)`

#### `void CutActionMoveToLocation(float fDelay, object oPC, location lLoc, int iRun, int iShift = TRUE)`

#### `void CutActionForceMoveToObject(float fDelay, object oPC, object oTarget, int iRun = FALSE, float fRange = 1.0, float fTimeout = 30.0, int iShift = TRUE)`

#### `void CutActionForceMoveToLocation(float fDelay, object oPC, location lLoc, int iRun = FALSE, float fTimeout = 30.0, int iShift = TRUE)`

#### `void CutCreateObject(float fDelay, object oPC, int iType, string sName, location lLoc, int iEffect, int nSetActive = TRUE, int iShift = TRUE)`
> Would create an object after the delay. Please avoid using this function as it is currently impossible
> to cancel action of objects created by it after aborting the cutscene.

#### `void CutSetFacingPoint(float fDelay, object oPC, string szTag, int iShift = TRUE)`

#### `void CutFadeOutAndIn(float fDelay, object oObject, float fFadeLen = 4.3, float nFadeSpeed = FADE_SPEED_FASTEST, int iShift = TRUE)`
> Combines fade-out and fade-in into one function.

#### `void CutFadeToBlack(float fDelay, object oObject, float nFadeSpeed = FADE_SPEED_FASTEST, int iShift = TRUE)`

#### `void CutFadeFromBlack(float fDelay, object oObject, float nFadeSpeed = FADE_SPEED_FASTEST, int iShift = TRUE)`

#### `void CutSetCamera(float fDelay, object oObject, int iCameraType, float fFacing, float fZoom, float fPitch, int nSpeed, int iShift = TRUE)`

#### `void CutClearAllActions(float fDelay, object oObject, int nClearCombatState, int iShift = TRUE)`

#### `void CutApplyEffectAtLocation(float fDelay, object oObject, int iDur, int iEffect, location lLoc, float fDur = 0.0, int iShift = TRUE)`

#### `void CutApplyEffectToObject(float fDelay, int iDur, int iEffect, object oObject, float fDur = 0.0, int iShift = TRUE)`
> Applies visual effect iEffect to oObject.
> If you want to apply non-visual effect use CutApplyEffectToObject2

#### `void CutApplyEffectToObject2(float fDelay, int iDur, effect eEffect, object oObject, float fDur = 0.0, int iShift = TRUE)`
> Applies eEffect to Object.

#### `void CutKnockdown(float fDelay, object oObject, float fDur, int iShift = TRUE)`

#### `void CutDeath(float fDelay, object oObject, int iSpec, int iShift = TRUE)`

#### `void CutActionCastFakeSpellAtObject(float fDelay, int iSpell, object oObject, object oTarget, int iPath = PROJECTILE_PATH_TYPE_DEFAULT, int iShift = TRUE)`

#### `void CutActionCastFakeSpellAtLocation(float fDelay, int iSpell, object oObject, location lLoc, int iPath = PROJECTILE_PATH_TYPE_DEFAULT, int iShift = TRUE)`

#### `void CutActionCastSpellAtObject(float fDelay, int iSpell, object oObject, object oTarget, int nMetaMagic = METAMAGIC_ANY, int bCheat = FALSE, int nDomainLevel = 0, int iPath = PROJECTILE_PATH_TYPE_DEFAULT, int bInstantSpell = FALSE, int iShift = TRUE)`

#### `void CutActionCastSpellAtLocation(float fDelay, int iSpell, object oObject, location lLoc, int METAMAGIC = METAMAGIC_ANY, int nCheat = FALSE, int nDomainLevel = 0, int iPath = PROJECTILE_PATH_TYPE_DEFAULT, int iShift = TRUE)`

#### `void CutSetLocation(float fDelay, object oPC, int iShift = TRUE)`
> Stores the current location of oPC to be restored later with CutRestoreLocation.

#### `void CutRestoreLocation(float fDelay, object oPC, int iShift = TRUE)`
> Restores the location that had been stored by CutSetLocation.

#### `void CutSetCutsceneMode(float fDelay, object oPC, int iValue, int bInv, int bKeepAssociates = TRUE, int bFreezeAssociates = TRUE, int iShift = TRUE)`
> Used to turn cutscene mode on or off.
> iValue: TRUE to start cutscene, and FALSE to exit cutscene mode.
> bInv: TRUE -  to make the player invisible.
> FASLE - would leave the player visible.
> CUT_CAMERA_HEIGHT_VERY_LOW - would turn the playe invisible and put the camera at a very low position.
> CUT_CAMERA_HEIGHT_LOW - would turn the playe invisible and put the camera at a low position.
> CUT_CAMERA_HEIGHT_MEDIUM - would turn the playe invisible and put the camera at a low position.
> CUT_CAMERA_HEIGHT_HIGH would turn the playe invisible and put the camera at a high position.
> CUT_CAMERA_HEIGHT_VERY_HIGH would turn the playe invisible and put the camera at a very high position.
> bKeepAssociates: would destroy all associate when set to FALSE.
> bFreezeAssociates would freeze all associates when set to TRUE, and turn them invisible when set to VANISH = 2.

#### `void CutSetPlotFlag(float fDelay, object oObject, int iValue, int iShift = TRUE)`

#### `void CutDestroyObject(float fDelay, object oObject, int iShift = TRUE)`

#### `void CutStoreCameraFacing(float fDelay, object oPC, int iShift = TRUE)`
> Stores camera facing for oPC to be restored by CutRestoreCameraFacing.

#### `void CutRestoreCameraFacing(float fDelay, object oPC, int iShift = TRUE)`
> Restored camera facing that has been stored by CutStoreCameraFacing.

#### `void CutBlackScreen(float fDelay, object oPC, int iShift = TRUE)`

#### `void CutStopFade(float fDelay, object oPC, int iShift = TRUE)`

#### `void CutPlaySound(float fDelay, object oPC, string szSound, int iShift = TRUE)`

#### `void CutSetMusic(float fDelay, object oPC, int nTrack, int iShift = TRUE)`
> Sets the track nTrack as the music for the current area of oPC and plays it.

#### `void CutStoreMusic(float fDelay, object oPC, int iShift = TRUE)`
> Stores the current music track for the area where oPC is. Use CutRestoreMusic to reset the music for the area

#### `void CutRestoreMusic(float fDelay, object oPC, int iShift = TRUE)`
> Restores the music track for the area where oPC is which was stores by CutStoreMusic.

#### `void CutSetAmbient(float fDelay, object oPC, int nTrack, int iShift = TRUE)`
> Sets the track nTrack as the music for the current area of oPC and plays it.

#### `void CutSetTileMainColor(float fDelay, object oPC, location lLoc, int nMainColor1, int nMainColor2, int iShift = TRUE)`
> Sets the main tile color for the tile at lLoc.

#### `void CutSetTileSourceColor(float fDelay, object oPC, location lLoc, int nSourceColor1, int nSourceColor2, int iShift = TRUE)`
> Sets the source tile color for the tile at lLoc.

#### `void CutSetWeather(float fDelay, object oPC, int nWeather, int iShift = TRUE)`

#### `void CutSetAbortDelay(int nCutscene, float fDelay)`
> Sets the delay between pressing the ESC key to actually doing the cutscene cleanup.
> This function should be used at the beginning of a cutscene only if such delay is required.
> Otherwise, there would be no cleanup delay.

#### `float CutGetAbortDelay(int nCutscene)`
> Retrieves the current abort delay for nCutscene after aborting.

#### `void CutSetDestroyCopyDelay(int nCutscene, float fDelay)`
> Sets the delay between pressing the ESC key to actually destroying the PC copy.
> This function should be used at the beginning of a cutscene only if such delay is required.
> Otherwise, there would be no delay.

#### `float CutGetDestroyCopyDelay(int nCutscene)`
> Retrieves the current destroy PC delay after aborting a cutscene.

#### `object CutCreatePCCopy(object oPC, location lLoc, string sTag)`
> Creates a copy of oPC at lLoc with tag sTag. Older copies of oPC would be destroyed if any.

#### `object CutCreateObjectCopy(float fDelay, object oObject, location lLoc, string sTag = "", int iShift = TRUE)`
> Creates a copy of oPC at lLoc with tag sTag. Older copies of oPC would be destroyed if any.

#### `void CutDestroyPCCopy(float fDelay, object oPC, int bRestorePCLocation = TRUE, int iShift = TRUE)`
> Destroys the copy of oPC and restores the PC's original location if bRestorePCLocation is TRUE.

#### `void CutDisableCutscene(int nCutscene, float fCleanupDelay, float fDestPCCopyDelay, int nRestoreType = RESTORE_TYPE_NORMAL)`
> Disables a cutscene. All generic disable functions would be called after a delay of fCleanupDelay,
> and any PC copy object would be destroyed after a delay of fDestPCCopyDelay).
> If using the CUT_DELAY_TYPE_CUMULATIVE delay type, then each delay should be in relation to
> the previous delay (independent delays). nRestoreType should have one of the following values:
> - RESTORE_TYPE_NONE: Do not jump the player.
> - RESTORE_TYPE_NORMAL: Jump the player to the last place that he used CutSetLocation() at.
> - RESTORE_TYPE_COPY: Jupm the player to the place where the copy was created.

#### `void CutDisableAbort(int nCutscene)`
> Disables the possibility to disable nCutscene. Pressing ESC would do nothing after calling this function.

#### `int CutGetIsAbortDisabled(int nCutscene)`
> returns TRUE if it is not possible to abort nCutscene, FALSE otherwise.

#### `float CutGetConvDuration(string sConvName)`
> Get the duration of dialog sConvName from a 2da. A value of 0.0 is returned on error.
> The value in the 2da should be set when first knowing the english length of the dialog.

#### `void CutAdjustReputation(float fDelay, object oTarget, object oSource, int nAdjustment, int iShift = TRUE)`
> This adjusts Faction Reputation, how the entire faction that
> oSourceFactionMember is in, feels about oTarget.

#### `void CutSetCameraSpeed(float fDelay, object oPC, float fMovementRateFactor, int iShift = TRUE)`
> Sets the current movement rate factor of
> the cutscene camera-man (oPC)
> fMovementRateFactor: Factor ranging between 0.1 and 2.0

#### `void UnFreezeAssociate(object oPlayers)`

#### `float CutGetConvDuration(string sConvName)`

#### `void CutSetActiveCutscene(int nCutsceneNumber, int nDelayType, int bSetCutsceneObject = TRUE)`

#### `int GetActiveCutsceneNum()`

#### `float CutCalculateCurrentDelay(float fDelayModifier, int nCutsceneNumber)`
> Calculates the "real" delay to execute a cut* action (can be a comulative delay or a constant one)

#### `float GetShift(object oObject, int iShift)`

#### `void CutDisableAbort(int nCutscene)`
> flagging a cutscene as non-abortable. This function should be used at the begining of
> a cutscene (probably for short cutscenes).

#### `int CutGetIsAbortDisabled(int nCutscene)`

#### `int CutSetActiveCutsceneForObject(object oObject, int nCutNum, int bMainPC = FALSE)`

#### `int CutGetActiveCutsceneForObject(object oObject)`

#### `void CutResetActiveObjectsForCutscene(int nCutscene)`
> This function is used internally by the generic abort script.
> It finds all active objects for this cutscene and resets them so they won't execute any
> more actions.

#### `void CallRestorePCCopyLocation(int nCutscene, object oPC)`

#### `void CallRemoveEffects(int nCutscene, object oObject)`

#### `void CutRemoveEffects(float fDelay, object oObject, int iShift = TRUE)`

#### `void CallRemoveAssociatesEffects(int nCutscene, object oPC)`

#### `void CallJumpAssociateToLocation(int nCutscene, object oPC, location lLoc)`

#### `void CutJumpAssociateToLocation(float fDelay, object oPC, location lLoc, int iShift = TRUE)`

#### `void CallDestroyPCCopy(int nCutscene, object oPC, int bRestorePCLocation)`

#### `void CutDestroyPCCopy(float fDelay, object oPC, int bRestorePCLocation = TRUE, int iShift = TRUE)`
> Destroys the copy of oPC. This function would work even if there is no valid cutscene for oPC.
> If bRestorePCLocation is TRUE then the PC would be jumped to original location.

#### `object CutCreatePCCopy(object oPC, location lLoc, string sTag)`
> Creates a copy of the pc at lLoc (and destroys an old one, if exists.

#### `void CallCreateObjectCopy(int nCutscene, object oObject, location lLoc, string sTag)`

#### `void CutCreateObjectCopy(float fDelay, object oObject, location lLoc, string sTag = "", int iShift = TRUE)`

#### `int CutGetIsMainPC(object oPC)`
> returns TRUE whether the pc is the main pc for his current cutscene, FALSE otherwise.

#### `void CutSetDestroyCopyDelay(int nCutscene, float fDelay)`
> set delay for removal of pc copy in the generic abort script (should be used
> at the begining of a cutscene)

#### `float CutGetDestroyCopyDelay(int nCutscene)`

#### `void CutSetAbortDelay(int nCutscene, float fDelay)`

#### `float CutGetAbortDelay(int nCutscene)`
> get the delay for cutscene-disable funcions in the generic abort script (used only there)

#### `void RemoveAssociateEffects(object oCreature)`

#### `object FreezeAssociate(object oPlayers, int bVanish)`

#### `void UnFreezeAssociate(object oPlayers)`

#### `void RemoveCommandable(object oPC)`

#### `void Talk(string sConvFile, object oTalkTo)`
> Helper function

#### `void CallBeginConversation(int nCutscene, object oTalker, object oTalkTo, string sConvFile)`

#### `void CutBeginConversation(float fDelay, object oTalker, object oTalkTo, string sConvFile, int iShift = TRUE)`

#### `void CallActionStartConversation(int nCutscene, object oNPC, object oPC, string szConversationFile)`

#### `void CutActionStartConversation(float fDelay, object oNPC, object oPC, string szConversationFile, int iShift = TRUE)`

#### `void CallSpeakString(int nCutscene, object oSpeaker, string szString)`

#### `void CallSpeakStringByStrRef(int nCutscene, object oSpeaker, int nStrRef)`

#### `void CutSpeakString(float fDelay, object oSpeaker, string szString, int iShift = TRUE)`

#### `void CutSpeakStringByStrRef(float fDelay, object oSpeaker, int nStrRef, int iShift = TRUE)`

#### `void CallPlayAnimation(int nCutscene, object oObject, int nAnimation, float fLength)`

#### `void CutPlayAnimation(float fDelay, object oObject, int nAnimation, float fLength, int iShift = TRUE)`

#### `void CallJumpToLocation(int nCutscene, object oPC, location lLoc)`

#### `void CutJumpToLocation(float fDelay, object oPC, location lLoc, int iShift = TRUE)`

#### `void CallJumpToObject(int nCutscene, object oPC, object oObject)`

#### `void CutJumpToObject(float fDelay, object oPC, object oObject, int iShift = TRUE)`

#### `void CallActionForceMoveToObject(int nCutscene, object oPC, object oTarget, int iRun, float fRange, float fTimeout)`
> Used to force move the PC or NPC to an object.

#### `void CutActionForceMoveToObject(float fDelay, object oPC, object oTarget, int iRun = FALSE, float fRange = 1.0, float fTimeout = 30.0, int iShift = TRUE)`

#### `void CallActionMoveToObject(int nCutscene, object oPC, object oTarget, int iRun)`

#### `void CutActionMoveToObject(float fDelay, object oPC, object oTarget, int iRun, int iShift = TRUE)`

#### `void CallActionForceMoveToLocation(int nCutscene, object oPC, location lLoc, int iRun, float fTimeout)`
> Used to force move the PC or NPC to a location.

#### `void CutActionForceMoveToLocation(float fDelay, object oPC, location lLoc, int iRun = FALSE, float fTimeout = 30.0, int iShift = TRUE)`

#### `void CallActionMoveToLocation(int nCutscene, object oPC, location lLoc, int iRun)`

#### `void CutActionMoveToLocation(float fDelay, object oPC, location lLoc, int iRun, int iShift = TRUE)`

#### `void CallCreateObject(int nCutscene, int iType, object oPC, string sName, location lLoc, int iEffect, int nSetActive)`

#### `void CutCreateObject(float fDelay, object oPC, int iType, string sName, location lLoc, int iEffect, int nSetActive = TRUE, int iShift = TRUE)`

#### `void CallSetFacingPoint(int nCutscene, object oPC, string szTag)`

#### `void CutSetFacingPoint(float fDelay, object oPC, string szTag, int iShift = TRUE)`

#### `void CallAdjustReputation(int nCutscene, object oTarget, object oSource, int nAdjustment)`

#### `void CutAdjustReputation(float fDelay, object oTarget, object oSource, int nAdjustment, int iShift = TRUE)`

#### `void CallFadeOutAndIn(int nCutscene, object oObject, float fFadeLen, float fFadeSpeed)`

#### `void CutFadeOutAndIn(float fDelay, object oObject, float fFadeLen = 4.3, float fFadeSpeed = FADE_SPEED_FASTEST, int iShift = TRUE)`

#### `void CallFadeToBlack(int nCutscene, object oObject, float fFadeSpeed)`

#### `void CutFadeToBlack(float fDelay, object oObject, float fFadeSpeed = FADE_SPEED_FASTEST, int iShift = TRUE)`

#### `void CallFadeFromBlack(int nCutscene, object oObject, float fFadeSpeed)`

#### `void CutFadeFromBlack(float fDelay, object oObject, float fFadeSpeed = FADE_SPEED_FASTEST, int iShift = TRUE)`

#### `void CallSetCamera(int nCutscene, object oObject, int iCameraType, float fFacing, float fZoom, float fPitch, int nSpeed)`

#### `void CutSetCamera(float fDelay, object oObject, int iCameraType, float fFacing, float fZoom, float fPitch, int nSpeed, int iShift = TRUE)`

#### `void CallClearAllActions(int nCutscene, object oObject, int nClearCombatState = FALSE)`

#### `void CutClearAllActions(float fDelay, object oObject, int nClearCombatState = FALSE, int iShift = TRUE)`

#### `void CallApplyEffectAtLocation(int nCutscene, object oObject, int iDur, int iEffect, location lLoc, float fDur)`

#### `void CutApplyEffectAtLocation(float fDelay, object oObject, int iDur, int iEffect, location lLoc, float fDur = 0.0, int iShift = TRUE)`

#### `void CallApplyEffectToObject(int nCutscene, int iDur, int iEffect, object oObject, float fDur)`

#### `void CutApplyEffectToObject(float fDelay, int iDur, int iEffect, object oObject, float fDur = 0.0, int iShift = TRUE)`

#### `void CallApplyEffectToObject2(int nCutscene, int iDur, effect eEffect, object oObject, float fDur)`
> For all other effects (NOT VISUAL EFFECTS)
> Used to apply a NON visual effect to an object.

#### `void CutApplyEffectToObject2(float fDelay, int iDur, effect eEffect, object oObject, float fDur = 0.0, int iShift = TRUE)`

#### `void CallKnockdown(int nCutscene, object oObject, float fDur)`

#### `void CutKnockdown(float fDelay, object oObject, float fDur = 3.0, int iShift = TRUE)`

#### `void CallActionAttack(int nCutscene, object oAttacker, object oAttackee, int bPassive = FALSE)`

#### `void CutActionAttack(float fDelay, object oAttacker, object oAttackee, int bPassive = FALSE, int iShift = TRUE)`

#### `void CallDeath(int nCutscene, object oObject, int iSpec)`

#### `void CutDeath(float fDelay, object oObject, int iSpec = FALSE, int iShift = TRUE)`

#### `void CallActionUnlockObject(int nCutscene, object oObject, object oTarget)`
> oObject would unlock oTarget

#### `void CutActionUnlockObject(float fDelay, object oObject, object oTarget, int iShift = TRUE)`

#### `void CallActionLockObject(int nCutscene, object oObject, object oTarget)`
> oObject would lock oTarget

#### `void CutActionLockObject(float fDelay, object oObject, object oTarget, int iShift = TRUE)`

#### `void CallActionMoveAwayFromLocation(int nCutscene, object oObject, location lLoc, int bRun, float fDistance)`
> oObject would flee lLoc

#### `void CutActionMoveAwayFromLocation(float fDelay, object oObject, location lLoc, int bRun = FALSE, float fDistance = 40.0, int iShift = TRUE)`

#### `void CallActionMoveAwayFromObject(int nCutscene, object oObject, object oTarget, int bRun, float fDistance)`
> oObject would flee oTarget

#### `void CutActionMoveAwayFromObject(float fDelay, object oObject, object oTarget, int bRun = FALSE, float fDistance = 40.0, int iShift = TRUE)`

#### `void CallActionForceFollowObject(int nCutscene, object oObject, object oFollow, float fFollowDistance)`
> oObject would follow oFollow

#### `void CutActionForceFollowObject(float fDelay, object oObject, object oFollow, float fFollowDistance = 0.0, int iShift = TRUE)`

#### `void CallActionUnequipItem(int nCutscene, object oObject, object oItem)`
> oObject unequips oItem

#### `void CutActionUnequipItem(float fDelay, object oObject, object oItem, int iShift = TRUE)`

#### `void CallActionEquipItem(int nCutscene, object oObject, object oItem, int nInvSlot)`
> oObject equips oItem in InvSlot

#### `void CutActionEquipItem(float fDelay, object oObject, object oItem, int nInvSlot, int iShift = TRUE)`

#### `void CallActionSit(int nCutscene, object oObject, object oChair)`
> oObject would sit on oChair

#### `void CutActionSit(float fDelay, object oObject, object oChair, int iShift = TRUE)`

#### `void CallActionOpenDoor(int nCutscene, object oObject, object oDoor)`
> oObject would open oDoor

#### `void CutActionOpenDoor(float fDelay, object oObject, object oDoor, int iShift = TRUE)`

#### `void CallActionCloseDoor(int nCutscene, object oCloser, object oDoor)`

#### `void CutActionCloseDoor(float fDelay, object oCloser, object oDoor, int iShift = TRUE)`

#### `void CallActionCastFakeSpellAtObject(int nCutscene, int iSpell, object oObject, object oTarget, int iPath)`

#### `void CutActionCastFakeSpellAtObject(float fDelay, int iSpell, object oObject, object oTarget, int iPath = PROJECTILE_PATH_TYPE_DEFAULT, int iShift = TRUE)`

#### `void CallActionCastSpellAtObject(int nCutscene, int iSpell, object oObject, object oTarget, int nMetaMagic, int bCheat, int nDomainLevel, int iPath, int bInstantSpell)`
> Used to cast a  spell at an object.

#### `void CutActionCastSpellAtObject(float fDelay, int iSpell, object oObject, object oTarget, int nMetaMagic = METAMAGIC_ANY, int bCheat = FALSE, int nDomainLevel = 0, int iPath = PROJECTILE_PATH_TYPE_DEFAULT, int bInstantSpell = FALSE, int iShift = TRUE)`

#### `void CallActionCastFakeSpellAtLocation(int nCutscene, int iSpell, object oObject, location lLoc, int iPath)`

#### `void CutActionCastFakeSpellAtLocation(float fDelay, int iSpell, object oObject, location lLoc, int iPath = PROJECTILE_PATH_TYPE_DEFAULT, int iShift = TRUE)`

#### `void CallActionCastSpellAtLocation(int nCutscene, int iSpell, object oObject, location lLoc, int nMetaMagic, int bCheat, int iPath, int bInstantSpell)`

#### `void CutActionCastSpellAtLocation(float fDelay, int iSpell, object oObject, location lLoc, int nMetaMagic = METAMAGIC_ANY, int bCheat = FALSE, int iPath = PROJECTILE_PATH_TYPE_DEFAULT, int bInstantSpell = FALSE, int iShift = TRUE)`

#### `void CallSetLocation(int nCutscene, object oPC)`

#### `void CutSetLocation(float fDelay, object oPC, int iShift = TRUE)`

#### `void CallRestoreLocation(int nCutscene, object oPC)`

#### `void CutRestoreLocation(float fDelay, object oPC, int iShift = TRUE)`

#### `void CutRestorePCAppearance(int nCutscene, object oPC)`

#### `void CutRemoveHenchmenAssociates(object oPC)`

#### `void CallSetCutsceneMode(int nCutscene, object oPC, int iValue, int bInv, int bKeepAssociate = TRUE, int bFreezeAssociate = TRUE)`

#### `void CutSetCutsceneMode(float fDelay, object oPC, int iValue, int bInv, int bKeepAssociate = TRUE, int bFreezeAssociate = TRUE, int iShift = TRUE)`

#### `void CallSetPlotFlag(int nCutscene, object oObject, int iValue)`

#### `void CutSetPlotFlag(float fDelay, object oObject, int iValue, int iShift = TRUE)`

#### `void CallDestroyObject(int nCutscene, object oObject)`

#### `void CutDestroyObject(float fDelay, object oObject, int iShift = TRUE)`

#### `void CallStoreCameraFacing(int nCutscene, object oPC)`

#### `void CutStoreCameraFacing(float fDelay, object oPC, int iShift = TRUE)`

#### `void CallRestoreCameraFacing(int nCutscene, object oPC)`

#### `void CutRestoreCameraFacing(float fDelay, object oPC, int iShift = TRUE)`

#### `void CallBlackScreen(int nCutscene, object oPC)`

#### `void CutBlackScreen(float fDelay, object oPC, int iShift = TRUE)`

#### `void CallStopFade(int nCutscene, object oPC)`

#### `void CutStopFade(float fDelay, object oPC, int iShift = TRUE)`

#### `void CallPlayVoiceChat(int nCutscene, object oPC, int nChatID)`

#### `void CutPlayVoiceChat(float fDelay, object oPC, int nChatID, int iShift = TRUE)`

#### `void CallPlaySound(int nCutscene, object oPC, string szSound)`

#### `void CutPlaySound(float fDelay, object oPC, string szSound, int iShift = TRUE)`

#### `void CallSetAmbient(int nCutscene, object oPC, int nTrack)`
> Setting a background ambient sounds and playing it for the area where oPC is in.

#### `void CutSetAmbient(float fDelay, object oPC, int nTrack, int iShift = TRUE)`

#### `void CallSetMusic(int nCutscene, object oPC, int nTrack)`
> Setting a background music and playing it for the area where oPC is in.

#### `void CutSetMusic(float fDelay, object oPC, int nTrack, int iShift = TRUE)`

#### `void CallStoreMusic(int nCutscene, object oPC)`
> keep old background music

#### `void CutStoreMusic(float fDelay, object oPC, int iShift = TRUE)`

#### `void CallRestoreMusic(int nCutscene, object oPC)`
> restore old background music. Notice that there is no cutscene number check - so music can
> be restoed after aborting a cutscene

#### `void CutRestoreMusic(float fDelay, object oPC, int iShift = TRUE)`

#### `void CallSetTileMainColor(int nCutscene, object oPC, location lLoc, int nMainColor1, int nMainColor2)`

#### `void CutSetTileMainColor(float fDelay, object oPC, location lLoc, int nMainColor1, int nMainColor2, int iShift = TRUE)`

#### `void CallSetTileSourceColor(int nCutscene, object oPC, location lLoc, int nSourceColor1, int nSourceColor2)`

#### `void CutSetTileSourceColor(float fDelay, object oPC, location lLoc, int nSourceColor1, int nSourceColor2, int iShift = TRUE)`

#### `void CallSetWeather(int nCutscene, object oPC, int nWeather)`

#### `void CutSetWeather(float fDelay, object oPC, int nWeather, int iShift = TRUE)`

#### `void CallSetCameraSpeed(int nCutscene, object oPC, float fMovementRateFactor)`

#### `void CutSetCameraSpeed(float fDelay, object oPC, float fMovementRateFactor, int iShift = TRUE)`

#### `void CutDisableCutscene(int nCutscene, float fCleanupDelay, float fDestPCCopyDelay, int nRestoreType = RESTORE_TYPE_NORMAL)`
