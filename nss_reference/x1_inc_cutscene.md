# `x1_inc_cutscene.nss`

Source: `NSS/x1_/x1_inc_cutscene.nss`  
64 functions · 0 constants

## Functions

#### `float GetShift(object oObject, int iShift)`
> Used to shift the entire cutscene a length of time. Used internally here,
> but very handy for cutscenes that are complete, but need to be changed
> after the fact. From the point it is called, it just shifts the cutscene
> accordingly. Can be used (and should be) for non-cutscene delays in a
> script (ie - commands that aren't here or regular DelayCommands in a script.)

#### `void RemoveCommandable(object oPC)`
> Used to clear commandable state FALSE in the event there are too many
> Used in this include only.

#### `void CutRemoveEffects(int nCutscene, float fDelay, object oObject, int iShift = TRUE)`
> Used to remove all effects from an object.
> Example: CutRemoveEffects(10.5, GetObjectByTag("guard1")); would
> remove all effects from guard1 after a 10.5 second delay.

#### `void CutActionStartConversation(int nCutscene, float fDelay, object oNPC, object oPC, string szConversationFile, int iShift = TRUE)`
> Used for a conversation file when you need to have an NPC speak
> via a conversation instead of bubble text. The fDelay is used
> when timing is important.
> Example: CutActionStartConversation(5.0, oNPC, oPC, "my_conv"); would start the
> conversation file "my_conv" of the NPC, after a 5 sec delay, and
> the conversation subject would be the PC.

#### `void CutSpeakString(int nCutscene, float fDelay, object oSpeaker, string szString, int iShift = TRUE)`
> Used for bubble text type speaking.
> Example: CutSpeakString(0.0, GetObjectByTag("drow_priest"), "I like
> green eggs and ham."); would have the object drow_priest speak the
> line "I like green eggs and ham." after no delay.

#### `void CutPlayAnimation(int nCutscene, float fDelay, object oObject, int nAnimation, float fLength, int iShift = TRUE)`
> Used if you need a cutscene participant to do an animation.
> Example: CutPlayAnimation(<cutscene>, 26.0, oPC, ANIMATION_FIREFORGET_BOW, 3.0);
> would have the PC bow for 3 seconds after a 26 second delay.

#### `void CutJumpToLocation(int nCutscene, float fDelay, object oPC, location lLoc, int iShift = TRUE)`
> Used to jump the PC to a location.
> Example: CutJumpToLocation(20.0, oPC, GetLocation(GetWaypointByTag
> ("wp_jump")); would jump the PC to the wp_jump waypoint after a 20
> second delay.

#### `void CutJumpToObject(int nCutscene, float fDelay, object oPC, object oObject, int iShift = TRUE)`
> Used to jump the PC or NPC to an object.
> Example: CutJumpToObject(20.0, oPC, GetObject(GetObjectByTag
> ("invis_object")); would jump the PC to the invis_object after a 20
> second delay.

#### `void CutActionMoveToObject(int nCutscene, float fDelay, object oPC, object oTarget, int iRun, int iShift = TRUE)`
> Used to move the PC or NPC to an object.
> Example: CutActionMoveToObject(2.0, oPC, oTable, TRUE); would have the
> PC run to oTable after a 2 second delay. TRUE = run, FALSE = walk.

#### `void CutActionMoveToLocation(int nCutscene, float fDelay, object oPC, location lLoc, int iRun, int iShift = TRUE)`
> Used to move the PC or NPC to a location.
> Example: CutActionMoveToLocation(2.0, oPC, lTable, FALSE); would have the
> PC walk to lTable after a 2 second delay. TRUE = run, FALSE = walk.

#### `void CutCreateObject(int nCutscene, float fDelay, object oPC, int iType, string sName, location lLoc, int iEffect, int iShift = TRUE)`
> Used to delay object create. Pass the type, the sTemplate, the location,
> and the effect you wish to have appear when the object is created
> (0 for no effect).  The PC is also passed to check cutscene abort.
> EXAMPLE: CutCreateObject(2.3, oPC, OBJECT_TYPE_PLACEABLE, "resref", lLoc, VFX_FNF_HOLY_STRIKE);
> would create a placeable with the resref of "resref" at the location
> lLoc after 2.3 seconds, with the VFX_FNF_HOLY_STRIKE effect.

#### `void CutSetFacingPoint(int nCutscene, float fDelay, object oPC, string szTag, int iShift = TRUE)`
> Used to set the facing of a creature.
> EXAMPLE CutSetFacingPoint(22.5, oPC, "creature_tag"); would
> have the PC face "creature_tag" object after a 22.5 second delay.

#### `void CutFadeOutAndIn(int nCutscene, float fDelay, object oObject, int iShift = TRUE)`
> Used to fade out and back in, with a black screen section of
> 2 seconds in between.
> EXAMPLE: CallFadeOutAndIn(35.0, oPC); would Fade the screen
> out and back in on the PC, after a delay of 35 seconds.

#### `void CutFadeToBlack(int nCutscene, float fDelay, object oObject, int iShift = TRUE)`
> Used to fade out.
> EXAMPLE: CallFadeToBlack(35.0, oPC); would Fade the screen
> out on the PC, after a delay of 35 seconds.

#### `void CutFadeFromBlack(int nCutscene, float fDelay, object oObject, int iShift = TRUE)`
> Used to fade in.
> EXAMPLE: CallFadeFromBlack(35.0, oPC); would Fade the screen
> in on the PC, after a delay of 35 seconds.

#### `void CutSetCamera(int nCutscene, float fDelay, object oObject, int iCameraType, float fFacing, float fZoom, float fPitch, int nSpeed, int iShift = TRUE)`
> Used to set the camera for cutscene dramatics.
> EXAMPLE: To set a camera with the following settings on the PC,
> after a 30.0 second delay:
> CAMERA_MODE_TOP_DOWN
> Facing = 170.0
> Zoom = 5.0
> Pitch = 50.0
> CAMERA_TRANSITION_TYPE_MEDIUM
> CutSetCamera(30.0, oPC, CAMERA_MODE_TOP_DOWN, 170.0, 5.0, 50.0,
> CAMERA_TRANSITION_TYPE_MEDIUM);

#### `void CutClearAllActions(int nCutscene, float fDelay, object oObject, int iShift = TRUE)`
> Used to clear the actions of the subject.
> EXAMPLE: CutClearAllActions(3.2, GetObjectByTag("guard"));
> would clear the actions of "guard" after a 3.2 second delay.

#### `void CutApplyEffectAtLocation(int nCutscene, float fDelay, object oObject, int iDur, int iEffect, location lLoc, float fDur, int iShift = TRUE)`
> Used to apply a visual effect at a location. The PC is passed to
> determine if the cutscene has been aborted or not.
> EXAMPLE: CutApplyEffectAtLocation(98.3, oPC, DURATION_TYPE_INSTANT,
> VXF_FNF_HOLY_STRIKE, lLoc, 0.0);
> would have a holy strike visual appear at lLoc after a 98.3 second delay.
> The duration is instant, lasting the default time.

#### `void CutApplyEffectToObject(int nCutscene, float fDelay, int iDur, int iEffect, object oObject, float fDur, int iShift = TRUE)`
> Used to apply a visual effect to an object.
> EXAMPLE: CutApplyEffectToObject(98.3, oPC, DURATION_TYPE_TEMPORARY,
> VXF_DUR_PETRIFY, oPC, 4.0);
> would have a PETRIFY visual appear to the PC after a 98.3 second delay.
> The duration is temporary, lasting 4 seconds.

#### `void CutApplyEffectToObject2(int nCutscene, float fDelay, int iDur, effect eEffect, object oObject, float fDur, int iShift = TRUE)`
> For all other effects (NOT VISUAL EFFECTS)
> Used to apply a NON visual effect to an object.

#### `void CutKnockdown(int nCutscene, float fDelay, object oObject, float fDur, int iShift = TRUE)`
> Used to apply a knockdown effect to an object.
> EXAMPLE: CutKnockdown(98.3, oPC, 4.0);
> would have a knockdown appear on the PC after a 98.3 second delay.
> The duration is always temporary, this one lasting 4 seconds.

#### `void CutDeath(int nCutscene, float fDelay, object oObject, int iSpec, int iShift = TRUE)`
> Used to apply a death effect to an object.
> EXAMPLE: CutDeath(98.3, oPC, TRUE);
> would have a death appear on the PC after a 98.3 second delay.
> The duration is always instant. TRUE is used if you want a
> spectacular death. Set FALSE otherwise.

#### `void CutActionCastFakeSpellAtObject(int nCutscene, float fDelay, int iSpell, object oObject, object oTarget, int iPath, int iShift = TRUE)`
> Used to cast a fake spell at an object.
> EXAMPLE: CutActionCastFakeSpellAtObject(23.0, oPC, SPELL_SUNBEAM, oTarget,
> PROJECTILE_PATH_TYPE_DEFAULT); would have the
> PC cast a sunbeam at the oTarget, with a default
> projectile path. This would happen after a 23
> second delay.

#### `void CutActionCastFakeSpellAtLocation(int nCutscene, float fDelay, int iSpell, object oObject, location lLoc, int iPath, int iShift = TRUE)`
> Used to cast a fake spell at a location.
> EXAMPLE: CutActionCastFakeSpellAtLocation(23.0, oPC, SPELL_SUNBEAM, lLoc,
> PROJECTILE_PATH_TYPE_DEFAULT); would have the
> PC cast a sunbeam at lLoc, with a default
> projectile path. This would happen after a 23
> second delay.

#### `void CutSetLocation(int nCutscene, float fDelay, object oPC, int iShift = TRUE)`
> Used to set the PC's location so they can be jumped around as though
> they are the camera.
> EXAMPLE: CutSetLocation(23.0, oPC); would set the location
> on the PC, as a variable, as a location to be returned to later. This
> would happen after a 23 second delay.

#### `void CutRestoreLocation(int nCutscene, float fDelay, object oPC, int iShift = TRUE)`
> Used to recall the PC's location so they can be jumped back to their
> original location, stored by CutGetLocation.
> EXAMPLE: CutRestoreLocation(23.0, oPC); would return the PC
> to their original spot. This would happen after a 23 second delay.

#### `void CutSetCutsceneMode(int nCutscene, float fDelay, object oPC, int iValue, int iShift = TRUE)`
> Used to turn cutscene mode on or off.
> EXAMPLE: CutSetCutsceneMode(10.0, oPC, TRUE); would turn cutscene mode
> on after 10 seconds for the PC.

#### `void CutSetPlotFlag(int nCutscene, float fDelay, object oObject, int iValue, int iShift = TRUE)`
> Used to turn plot flags on or off.
> EXAMPLE: CutSetPlotFlag(10.0, oObject, 1); would turn plot flag to
> on after 10 seconds for the object.

#### `void CutDestroyObject(int nCutscene, float fDelay, object oObject, int iShift = TRUE)`
> Used to destroy objects. Make sure they are destroyable first with the
> CutSetPlotFlag function.
> EXAMPLE: CutDestroyObject(10.0, oObject); would destroy the object
> after 10 seconds.

#### `void CutStoreCameraFacing(int nCutscene, float fDelay, object oPC, int iShift = TRUE)`
> Used to store the camera position.
> EXAMPLE: CutStoreCameraFacing(10.0, oPC); would set the current
> camera settings at the 10.0 mark.

#### `void CutRestoreCameraFacing(int nCutscene, float fDelay, object oPC, int iShift = TRUE)`
> Used to restore the camera position.
> EXAMPLE: CutRestoreCameraFacing(10.0, oPC); would set the old
> camera settings back at the 10.0 mark.

#### `void CutBlackScreen(int nCutscene, float fDelay, object oPC, int iShift = TRUE)`
> Used to set the screen to black.  This is very useful in covering up
> and cutscene jumps that happen in the same area as the play area.
> EXAMPLE: CutBlackScreen(10.0, oPC); would set the screen to black
> at the 10.0 mark.

#### `void CutStopFade(int nCutscene, float fDelay, object oPC, int iShift = TRUE)`
> Used to remove the screen to black.
> EXAMPLE: CutStopFade(10.0, oPC); would set the screen back from black
> at the 10.0 mark.

#### `void CallRemoveEffects(int nCutscene, object oObject)`
> Private function used to implement the same function with the "Cut" prefix in
> place of the "Call" prefix.

#### `void CallActionStartConversation(int nCutscene, object oNPC, object oPC, string szConversationFile)`
> Private function used to implement the same function with the "Cut" prefix in
> place of the "Call" prefix.

#### `void CallSpeakString(int nCutscene, object oSpeaker, string szString)`
> Private function used to implement CutSpeakString

#### `void CallPlayAnimation(int nCutscene, object oObject, int nAnimation, float fLength)`
> Private function used to implement CutPlayAnimation.

#### `void CallJumpToLocation(int nCutscene, object oPC, location lLoc)`
> Private function used to implement CutJumpToLocation

#### `void CallJumpToObject(int nCutscene, object oPC, object oObject)`
> Private function used to implement CutJumpToObject

#### `void CallActionMoveToObject(int nCutscene, object oPC, object oTarget, int iRun)`
> Private function used to implement the same function with the "Cut" prefix in
> place of the "Call" prefix.

#### `void CallActionMoveToLocation(int nCutscene, object oPC, location lLoc, int iRun)`
> Private function used to implement the same function with the "Cut" prefix in
> place of the "Call" prefix.

#### `void CallCreateObject(int nCutscene, int iType, object oPC, string sName, location lLoc, int iEffect)`
> Private function used to implement the same function with the "Cut" prefix in
> place of the "Call" prefix.

#### `void CallSetFacingPoint(int nCutscene, object oPC, string szTag)`
> Private function used to implement the same function with the "Cut" prefix in
> place of the "Call" prefix.

#### `void CallFadeOutAndIn(int nCutscene, object oObject)`
> Private function used to implement the same function with the "Cut" prefix in
> place of the "Call" prefix.

#### `void CallFadeToBlack(int nCutscene, object oObject)`
> Private function used to implement the same function with the "Cut" prefix in
> place of the "Call" prefix.

#### `void CallFadeFromBlack(int nCutscene, object oObject)`
> Private function used to implement the same function with the "Cut" prefix in
> place of the "Call" prefix.

#### `void CallSetCamera(int nCutscene, object oObject, int iCameraType, float fFacing, float fZoom, float fPitch, int nSpeed)`
> Private function used to implement the same function with the "Cut" prefix in
> place of the "Call" prefix.

#### `void CallClearAllActions(int nCutscene, object oObject)`
> Private function used to implement the same function with the "Cut" prefix in
> place of the "Call" prefix.

#### `void CallApplyEffectAtLocation(int nCutscene, object oObject, int iDur, int iEffect, location lLoc, float fDur)`
> Private function used to implement the same function with the "Cut" prefix in
> place of the "Call" prefix.

#### `void CallApplyEffectToObject(int nCutscene, int iDur, int iEffect, object oObject, float fDur)`
> Private function used to implement the same function with the "Cut" prefix in
> place of the "Call" prefix.

#### `void CallApplyEffectToObject2(int nCutscene, int iDur, effect eEffect, object oObject, float fDur)`
> Private function used to implement the same function with the "Cut" prefix in
> place of the "Call" prefix.

#### `void CallKnockdown(int nCutscene, object oObject, float fDur)`
> Private function used to implement the same function with the "Cut" prefix in
> place of the "Call" prefix.

#### `void CallDeath(int nCutscene, object oObject, int iSpec)`
> Private function used to implement the same function with the "Cut" prefix in
> place of the "Call" prefix.

#### `void CallActionCastFakeSpellAtObject(int nCutscene, int iSpell, object oObject, object oTarget, int iPath)`
> Private function used to implement the same function with the "Cut" prefix in
> place of the "Call" prefix.

#### `void CallActionCastFakeSpellAtLocation(int nCutscene, int iSpell, object oObject, location lLoc, int iPath)`
> Private function used to implement the same function with the "Cut" prefix in
> place of the "Call" prefix.

#### `void CallSetLocation(int nCutscene, object oPC)`
> Private function used to implement the same function with the "Cut" prefix in
> place of the "Call" prefix.

#### `void CallRestoreLocation(int nCutscene, object oPC)`
> Private function used to implement the same function with the "Cut" prefix in
> place of the "Call" prefix.

#### `void CallSetCutsceneMode(int nCutscene, object oPC, int iValue)`
> Private function used to implement the same function with the "Cut" prefix in
> place of the "Call" prefix.

#### `void CallSetPlotFlag(int nCutscene, object oObject, int iValue)`
> Private function used to implement the same function with the "Cut" prefix in
> place of the "Call" prefix.

#### `void CallDestroyObject(int nCutscene, object oObject)`
> Private function used to implement the same function with the "Cut" prefix in
> place of the "Call" prefix.

#### `void CallStoreCameraFacing(int nCutscene, object oPC)`
> Private function used to implement the same function with the "Cut" prefix in
> place of the "Call" prefix.

#### `void CallRestoreCameraFacing(int nCutscene, object oPC)`
> Private function used to implement the same function with the "Cut" prefix in
> place of the "Call" prefix.

#### `void CallBlackScreen(int nCutscene, object oPC)`
> Private function used to implement the same function with the "Cut" prefix in
> place of the "Call" prefix.

#### `void CallStopFade(int nCutscene, object oPC)`
> Private function used to implement the same function with the "Cut" prefix in
> place of the "Call" prefix.
