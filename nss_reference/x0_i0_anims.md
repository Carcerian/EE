# `x0_i0_anims.nss`

Source: `NSS/x0_/x0_i0_anims.nss`  
105 functions · 16 constants

## Constants

| Constant | Type | Value | Note |
|---|---|---|---|
| `ANIM_LOOPING_LENGTH` | float | `4.0` |  |
| `ANIM_LOOPING_SPEED` | float | `1.0` |  |
| `ANIM_CONVERSATION` | string | `"x0_npc_homeconv"` |  |
| `sAnimCondVarname` | string | `"NW_ANIM_CONDITION"` |  |
| `NW_ANIM_FLAG_INITIALIZED` | int | `0x00000001` |  |
| `NW_ANIM_FLAG_CONSTANT` | int | `0x00000002` |  |
| `NW_ANIM_FLAG_CHATTER` | int | `0x00000004` |  |
| `NW_ANIM_FLAG_IS_ACTIVE` | int | `0x00000008` |  |
| `NW_ANIM_FLAG_IS_INTERACTING` | int | `0x00000010` |  |
| `NW_ANIM_FLAG_IS_INSIDE` | int | `0x00000020` |  |
| `NW_ANIM_FLAG_HAS_HOME` | int | `0x00000040` |  |
| `NW_ANIM_FLAG_IS_TALKING` | int | `0x00000080` |  |
| `NW_ANIM_FLAG_IS_MOBILE` | int | `0x00000100` |  |
| `NW_ANIM_FLAG_IS_MOBILE_CLOSE_RANGE` | int | `0x00000200` |  |
| `NW_ANIM_FLAG_IS_CIVILIZED` | int | `0x00000400` |  |
| `NW_ANIM_FLAG_CLOSE_DOORS` | int | `0x00001000` |  |

## Functions

#### `void AnimDebug(string sMsg)`
> Debugging function. Will be commented out for final.

#### `int GetAnimationCondition(int nCondition, object oCreature = OBJECT_SELF)`
> TRUE if the given creature has the given condition set

#### `void SetAnimationCondition(int nCondition, int bValid = TRUE, object oCreature = OBJECT_SELF)`
> Mark that the given creature has the given condition set

#### `int GetIsBusyWithAnimation(object oCreature)`
> Returns TRUE if the creature is busy talking or interacting
> with a placeable.

#### `object GetRandomFriend(float fMaxDistance)`
> Get a random nearby friend.
> OBJECT_INVALID will be returned if the friend is a PC,
> is busy with another animation, is in conversation or combat,
> or is further away than the distance limit.

#### `object GetRandomObjectByTag(string sTag, float fMaxDistance)`
> Get a random nearby object within the specified distance with
> the specified tag.

#### `object GetRandomObjectByType(int nObjType, float fMaxDistance)`
> Get a random nearby object within the specified distance with
> the specified type.
> nObjType: Any of the OBJECT_TYPE_* constants

#### `object GetRandomStop(float fMaxDistance)`
> Get a random "NW_STOP" object in the area.
> If fMaxDistance is non-zero, will return OBJECT_INVALID
> if the stop is too far away.
> The first time this is called in a given area, it cycles
> through all the stops in the area and stores them.

#### `void SetCreatureHomeWaypoint()`
> Check for a waypoint marked NW_HOME in the area; if it
> exists, mark it as the caller's home waypoint.

#### `object GetCreatureHomeWaypoint()`
> Get a creature's home waypoint; returns OBJECT_INVALID if none set.

#### `void SetCurrentFriend(object oFriend)`
> Set a specific creature (or OBJECT_INVALID to clear) as the caller's "friend"

#### `object GetCurrentFriend()`
> Get the caller's current friend, if set; OBJECT_INVALID otherwise

#### `void SetCurrentInteractionTarget(object oTarget)`
> Set an object (or OBJECT_INVALID to clear) as the caller's interactive
> target.

#### `object GetCurrentInteractionTarget()`
> Get the caller's current interaction target, if set; OBJECT_INVALID otherwise

#### `void CheckIsCivilized()`
> Mark the caller as civilized based on its racialtype.
> This will not unset the NW_ANIM_FLAG_IS_CIVILIZED flag
> if it was set outside.

#### `void CheckCurrentModes()`
> Check to see if we should switch on detect/stealth mode

#### `int CheckIsAnimActive(object oCreature)`
> Check if the creature should be active and turn off if not,
> returning FALSE. This respects the NW_ANIM_FLAG_CONSTANT
> setting.

#### `int CheckCurrentAction()`
> Check to see if we're in the middle of some action
> so we don't interrupt or pile actions onto the queue.
> Returns TRUE if in the middle of an action, FALSE otherwise.

#### `void AnimInitialization()`
> General initialization for animations.
> Called from all the Play_* functions.

#### `void PlayMobileAmbientAnimations_NonAvian()`
> This function should be used for mobile NPCs and monsters
> other than avian ones. It should be called by the creature
> that you want to perform the animations.
> Creatures will move randomly between objects in their
> area that have the tag "NW_STOP". Injured creatures will
> go to the nearest "NW_SAFE" waypoint and rest there.
> If at any point a creature gets to an "NW_DETECT" or
> "NW_STEALTH" waypoint, they will toggle on/off detect or
> stealth mode as appropriate.
> Humanoid creatures will also perform the following actions
> (you can set the NW_ANIM_FLAG_IS_CIVILIZED flag in script
> on non-humanoid creatures to make them use these behaviors):
> Creatures who are spawned in an area with the "NW_HOME" tag
> will mark that area as their home, leave during the day,
> and return at night.
> Creatures who are spawned in an outdoor area (for instance,
> in city streets) will go inside areas that have one of the
> interior waypoints (NW_TAVERN, NW_SHOP), if those areas
> are connected by an unlocked door. They will come back out
> as well.
> Mobile creatures will also have all the behaviors of immobile
> creatures, just tending to move around more.

#### `void PlayMobileAmbientAnimations_Avian()`
> Avian creatures will fly around randomly.

#### `void PlayImmobileAmbientAnimations()`
> This function should be used for any NPCs that should
> not move around. It should be called by the creature
> that you want to perform the animations.
> Creatures who call this function will never leave the
> area they spawned in.
> Injured creatures will rest at their starting location.
> Creatures who have the NW_ANIM_FLAG_IS_MOBILE_CLOSE_RANGE
> flag set will move around slightly within the area.
> Creatures in an area with an "interior" waypoint (NW_HOME,
> NW_SHOP, NW_TAVERN) will be set to have this flag automatically.
> Close-range creatures will move around the area, frequently
> returning to their starting point, interacting with other
> creatures and placeables. They will visit NW_STOP waypoints
> in their immediate vicinity, and they will close opened doors.
> In all other cases, the creature will not move from its starting
> position. They will turn around randomly, turn to and 'talk' to
> other NPCs in their immediate vicinity, and interact with
> placeables in their immediate vicinity.

#### `void AnimActionPlayRandomImmobile()`
> Perform a strictly immobile action.
> Includes:
> - play a random animation
> - turn towards a nearby unoccupied friend and 'talk'
> - turn towards a nearby placeable and interact
> - turn around randomly

#### `void AnimActionPlayRandomCloseRange()`
> Perform a random close-range action.
> This will include:
> - go to a nearby placeable and interact with it
> - go to a nearby friend and interact with them
> - play a random animation
> - walk to a nearby 'NW_STOP' waypoint
> - close an open door and return
> - go back to starting position
> - fall through to ActionPlayRandomImmobile

#### `void AnimActionPlayRandomMobile()`
> Perform a mobile action.
> Includes:
> - walk to an 'NW_STOP' waypoint in the area
> - walk to an area door and possibly go inside
> - go outside if previously went inside
> - fall through to ActionPlayRandomCloseRange

#### `void AnimActionPlayRandomUncivilized()`
> Perform a mobile action for an uncivilized creature.
> Includes:
> - perform random limited animations
> - walk to an 'NW_STOP' waypoint in the area
> - random walk if none available

#### `void AnimActionStartInteracting(object oPlaceable)`
> Start interacting with a placeable object

#### `void AnimActionStopInteracting()`
> Stop interacting with a placeable object

#### `void AnimActionStartTalking(object oFriend, int nHDiff = 0)`
> Start talking with a friend

#### `void AnimActionStopTalking(object oFriend, int nHDiff = 0)`
> Stop talking to the given friend

#### `void AnimActionPlayRandomGreeting(int nHDiff)`
> Play a greeting animation and possibly voicechat.
> If a negative difference is passed in, caller will bow.

#### `void AnimActionPlayRandomGoodbye(int nHDiff)`
> Play a random farewell animation and possibly voicechat.
> If a negative difference is passed in, caller will bow.

#### `void AnimActionRandomMoveAway(object oSource, float fDistance)`
> Randomly move away from an object the specified distance.
> This is mainly because ActionMoveAwayFromLocation isn't working.

#### `void AnimActionShakeHead()`
> Play animation of shaking head "no" to left and right

#### `void AnimActionLookAround()`
> Play animation of looking around to left and right

#### `void AnimActionTurnAround()`
> Turn around to face a random direction

#### `void AnimActionPlayRandomInteractAnimation(object oPlaceable)`
> Interact with a placeable object.
> This will activate/deactivate the placeable object if a valid
> one is passed in.
> KLUDGE: If a placeable object without an inventory should
> still be opened/shut instead of de/activated, set
> its Will Save to 1.

#### `void AnimActionPlayRandomTalkAnimation(int nHDiff)`
> Play a random talk gesture animation.
> If a hit dice difference (should be the hit dice of the talker
> minus the hit dice of the person being talked to) is passed in,
> slightly different animations will play based on this.

#### `void AnimActionPlayRandomBasicAnimation()`
> Play a random animation that all creatures should have.
> This is a very small set.
> Currently only has: get mid, taunt

#### `void AnimActionPlayRandomAnimation()`
> Play a random animation.
> This animation will be chosen from a different set
> based on whether a special waypoint or placeable
> is in the vicinity.

#### `int AnimActionCloseRandomDoor()`
> If there's an open door nearby, possibly go close it,
> then come back to our current spot.
> Returns TRUE on success, FALSE on failure.

#### `int AnimActionSitInChair(float fMaxDistance)`
> Sit in a random nearby chair if available.
> Looks for items with tag: NW_SEAT
> Returns TRUE on success, FALSE on failure.

#### `int AnimActionGetUpFromChair()`
> Get up from a chair if we're sitting.
> Returns TRUE on success, FALSE on failure.

#### `int AnimActionGoInside()`
> Go through a nearby door if appropriate.
> This will be done if the door is unlocked and
> the area the door leads to contains a waypoint
> with one of these tags:
> NW_TAVERN, NW_SHOP
> Returns TRUE on success, FALSE on failure.

#### `int AnimActionGoOutside()`
> Leave area if appropriate.
> This only works for NPCs that entered an area that
> has a waypoint with one of these tags:
> NW_TAVERN, NW_SHOP
> If the NPC entered through a door, they will exit through
> that door.
> Returns TRUE on success, FALSE on failure.

#### `int AnimActionGoToStop(float fMaxDistance = 20.0)`
> Go to a nearby waypoint or placeable marked with the
> tag "NW_STOP".
> Returns TRUE on success, FALSE on failure.

#### `int AnimActionFindFriend(float fMaxDistance)`
> Find a friend within the given distance and talk to them.
> Returns TRUE on success, FALSE on failure.

#### `int AnimActionFindPlaceable(float fMaxDistance)`
> Find a placeable within the given distance and interact
> with it.
> Returns TRUE on success, FALSE on failure.

#### `int AnimActionRest()`
> If injured and mobile, find the nearest NW_SAFE waypoint,
> go to it, and rest. If injured and immobile, go to starting
> location if not already there, and rest.
> Returns TRUE on success, FALSE on failure.

#### `int AnimActionGoHome()`
> If it is night, go back to our home waypoint, if we have one.
> This is only meaningful for mobile NPCs who would have left
> their homes during the day.
> Returns TRUE on success, FALSE on failure.

#### `int AnimActionLeaveHome()`
> If it is day, leave our home area, if we have one.
> This is only meaningful for mobile NPCs.
> Returns TRUE on success, FALSE on failure.

#### `int AnimActionChallengeIntruder()`
> If a PC is in the NPC's home and has not been challenged before,
> challenge them.
> This involves speaking a one-liner conversation from the
> conversation file ANIM_CONVERSATION, set above.

#### `void AnimDebug(string sMsg)`
> Debugging function. Will be commented out for final.

#### `int GetAnimationCondition(int nCondition, object oCreature = OBJECT_SELF)`
> TRUE if the given creature has the given condition set

#### `void SetAnimationCondition(int nCondition, int bValid = TRUE, object oCreature = OBJECT_SELF)`
> Mark that the given creature has the given condition set

#### `int GetIsBusyWithAnimation(object oCreature)`
> Returns TRUE if the creature is busy talking or interacting
> with a placeable.

#### `object GetRandomFriend(float fMaxDistance)`
> Get a random nearby friend within the specified distance limit,
> that isn't busy doing something else.

#### `object GetRandomObjectByTag(string sTag, float fMaxDistance)`
> Get a random nearby object within the specified distance with
> the specified tag.

#### `object GetRandomObjectByType(int nObjType, float fMaxDistance)`
> Get a random nearby object within the specified distance with
> the specified type.
> nObjType: Any of the OBJECT_TYPE_* constants

#### `object GetRandomStop(float fMaxDistance)`
> Get a random "NW_STOP" object in the area.
> If fMaxDistance is non-zero, will return OBJECT_INVALID
> if the stop is too far away.
> The first time this is called in a given area, it cycles
> through all the stops in the area and stores them.

#### `void SetCreatureHomeWaypoint()`
> Check for a waypoint marked NW_HOME in the area; if it
> exists, mark it as the caller's home waypoint.

#### `object GetCreatureHomeWaypoint()`
> Get a creature's home waypoint; returns OBJECT_INVALID if none set.

#### `void SetCurrentFriend(object oFriend)`
> Set a specific creature (or OBJECT_INVALID to clear) as the caller's "friend"

#### `object GetCurrentFriend()`
> Get the caller's current friend, if set; OBJECT_INVALID otherwise

#### `void SetCurrentInteractionTarget(object oTarget)`
> Set an object (or OBJECT_INVALID to clear) as the caller's interactive
> target.

#### `object GetCurrentInteractionTarget()`
> Get the caller's current interaction target, if set; OBJECT_INVALID otherwise

#### `void CheckIsCivilized()`
> Mark the caller as civilized based on its racialtype.
> This will not unset the NW_ANIM_FLAG_IS_CIVILIZED flag
> if it was set outside.

#### `void CheckCurrentModes()`
> Check to see if we should switch on detect/stealth mode

#### `int CheckIsAnimActive(object oCreature)`
> Check if the creature should be active and turn off if not,
> returning FALSE. This respects the NW_ANIM_FLAG_CONSTANT
> setting.

#### `int CheckCurrentAction()`
> Check to see if we're in the middle of some action
> so we don't interrupt or pile actions onto the queue.
> Returns TRUE if in the middle of an action, FALSE otherwise.

#### `void AnimInitialization()`
> General initialization for animations.
> Called from all the Play_* functions.

#### `void PlayMobileAmbientAnimations_NonAvian()`
> This function should be used for mobile NPCs and monsters
> other than avian ones. It should be called by the creature
> that you want to perform the animations.
> Creatures will interact with each other and move around,
> possibly even moving between areas.
> Creatures who are spawned in an area with the "NW_HOME" tag
> will mark that area as their home, leave from the nearest
> door during the day, and return at night.
> Injured creatures will go to the nearest "NW_SAFE" waypoint
> in their immediate area and rest there.
> If at any point the nearest waypoint is "NW_DETECT" or
> "NW_STEALTH", the creature will toggle search/stealth mode
> respectively.
> Creatures who are spawned in an outdoor area (for instance,
> in city streets) will go inside areas that have one of the
> interior waypoints (NW_TAVERN, NW_SHOP), if those areas
> are connected by an unlocked door. They will come back out
> as well.
> Creatures will also move randomly between objects in their
> area that have the tag "NW_STOP".
> Mobile creatures will have all the same behaviors as immobile
> creatures, just tending to move around more.

#### `void PlayMobileAmbientAnimations_Avian()`
> Avian creatures will fly around randomly.

#### `void PlayImmobileAmbientAnimations()`
> This function should be used for any NPCs that should
> not move around. It should be called by the creature
> that you want to perform the animations.
> Creatures who call this function will never leave the
> area they spawned in.
> Injured creatures will rest at their starting location.
> Creatures who have the NW_ANIM_FLAG_IS_MOBILE_CLOSE_RANGE
> flag set will move around slightly within the area.
> Creatures in an area with an "interior" waypoint (NW_HOME,
> NW_SHOP, NW_TAVERN) will be set to have this flag automatically.
> Close-range creatures will move around the area, frequently
> returning to their starting point, interacting with other
> creatures and placeables. They will visit NW_STOP waypoints
> in their immediate vicinity, and they will close opened doors.
> In all other cases, the creature will not move from its starting
> position. They will turn around randomly, turn to and 'talk' to
> other NPCs in their immediate vicinity, and interact with
> placeables in their immediate vicinity.

#### `void AnimActionPlayRandomImmobile()`
> Perform a strictly immobile action.
> Includes:
> - turn towards a nearby unoccupied friend and 'talk'
> - turn towards a nearby placeable and interact
> - turn around randomly
> - play a random animation

#### `void AnimActionPlayRandomCloseRange()`
> Perform a random close-range action.
> This will include:
> - any of the immobile actions
> - close any nearby doors, then return to current position
> - go to a nearby placeable and interact with it
> - go to a nearby friend and interact with them
> - walk to a nearby 'NW_STOP' waypoint
> - going back to starting point

#### `void AnimActionPlayRandomMobile()`
> Perform a mobile action.
> Includes:
> - walk to an 'NW_STOP' waypoint in the area
> - walk to an area door and possibly go inside
> - go outside if previously went inside
> - fall through to AnimActionPlayRandomCloseRange

#### `void AnimActionPlayRandomUncivilized()`
> Perform a mobile action for an uncivilized creature.
> Includes:
> - perform random limited animations
> - walk to an 'NW_STOP' waypoint in the area
> - random walk if none available

#### `void AnimActionStartInteracting(object oPlaceable)`
> Start interacting with a placeable object

#### `void AnimActionStopInteracting()`
> Stop interacting with a placeable object

#### `void AnimActionStartTalking(object oFriend, int nHDiff = 0)`
> Start talking with a friend

#### `void AnimActionStopTalking(object oFriend, int nHDiff = 0)`
> Stop talking to the given friend

#### `void AnimActionPlayRandomGreeting(int nHDiff = 0)`
> Play a greeting animation and possibly voicechat.
> If a negative hit dice difference (HD caller - HD greeted) is
> passed in, the caller will bow.

#### `void AnimActionPlayRandomGoodbye(int nHDiff)`
> Play a random farewell animation and possibly voicechat.
> If a negative hit dice difference is passed in, the
> caller will bow.

#### `void AnimActionRandomMoveAway(object oSource, float fDistance)`
> Randomly move away from an object the specified distance.
> This is mainly because ActionMoveAwayFromLocation isn't working.

#### `void AnimActionShakeHead()`
> Play animation of shaking head "no" to left & right

#### `void AnimActionLookAround()`
> Play animation of looking to left and right

#### `void AnimActionTurnAround()`
> Turn around to face a random direction

#### `void AnimActionGoThroughDoor(object oDoor)`
> Go through a door and close it behind you,
> then walk a short distance away.
> This assumes the door exists, is unlocked, etc.

#### `int AnimActionCloseRandomDoor()`
> If there's an open door nearby, possibly go close it,
> then come back to our current spot.

#### `int AnimActionSitInChair(float fMaxDistance)`
> Sit in a random nearby chair if available.
> Looks for items with tag: Chair

#### `int AnimActionGetUpFromChair()`
> Get up from a chair if we're sitting

#### `int AnimActionGoInside()`
> Go through a nearby door if appropriate.
> This will be done if the door is unlocked and
> the area the door leads to contains a waypoint
> with one of these tags:
> NW_TAVERN, NW_SHOP

#### `int AnimActionGoOutside()`
> Leave area if appropriate.
> This only works for NPCs that entered an area that
> has a waypoint with one of these tags:
> NW_TAVERN, NW_SHOP
> If the NPC entered through a door, they will exit through
> that door.

#### `int AnimActionGoToStop(float fMaxDistance)`
> Go to a nearby waypoint or placeable marked with the
> tag "NW_STOP".

#### `int AnimActionFindFriend(float fMaxDistance)`
> Find a friend within the given distance and talk to them.
> Returns TRUE on success, FALSE on failure.

#### `int AnimActionFindPlaceable(float fMaxDistance)`
> Find a placeable within the given distance and interact
> with it.
> Returns TRUE on success, FALSE on failure.

#### `int AnimActionRest()`
> If injured, find the nearest "NW_SAFE" object,
> go to it, and rest.
> Returns TRUE on success, FALSE on failure.

#### `int AnimActionGoHome()`
> If it is night, go back to our home waypoint, if we have one.
> This is only meaningful for mobile NPCs who would have left
> their homes during the day.
> Returns TRUE on success, FALSE on failure.

#### `int AnimActionLeaveHome()`
> If it is day, leave our home area, if we have one.
> This is only meaningful for mobile NPCs.
> Returns TRUE on success, FALSE on failure.

#### `int AnimActionChallengeIntruder()`
> If a PC is in the NPC's home and has not been challenged before,
> challenge them.
> This involves speaking a one-liner conversation from the
> conversation file ANIM_CONVERSATION, set above.
> Returns TRUE on success, FALSE on failure.

#### `void AnimActionPlayRandomInteractAnimation(object oPlaceable)`
> Interact with a placeable object.
> This will activate/deactivate the placeable object if a valid
> one is passed in.
> KLUDGE: If a placeable object without an inventory should
> still be opened/shut instead of de/activated, set
> its Will Save to 1.

#### `void AnimActionPlayRandomTalkAnimation(int nHDiff)`
> Play a random talk gesture animation.
> If a hit dice difference (should be the hit dice of the caller
> minus the hit dice of the person being talked to) is passed in,
> the caller will play slightly different animations if they are
> weaker.

#### `void AnimActionPlayRandomBasicAnimation()`
> Play a random animation that all creatures should have.

#### `void AnimActionPlayRandomAnimation()`
> Play a random animation.
