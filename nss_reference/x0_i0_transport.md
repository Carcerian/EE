# `x0_i0_transport.nss`

Source: `NSS/x0_/x0_i0_transport.nss`  
17 functions · 0 constants

## Functions

#### `void TravelToObject(object oDest, object oTarget = OBJECT_SELF, int bRun = FALSE, float fDelay = 10.0)`
> Target goes to specified destination object intelligently.
> If location is in same area, walk (or run) there.
> If location is in different area, walk (or run) to
> most appropriate door, area transition, or waypoint,
> then jump.
> If either of these fail, jump after fDelay seconds.

#### `void TravelToLocation(location lDest, object oTarget = OBJECT_SELF, int bRun = FALSE, float fDelay = 10.0)`
> Target goes to specified location intelligently. See
> TravelToObject for description.

#### `object GetNearestExit(object oTarget = OBJECT_SELF)`
> Find nearest exit to target (either door or waypoint).

#### `object GetBestExit(object oTarget = OBJECT_SELF, object oTargetArea = OBJECT_INVALID)`
> Find best exit based on desired target area

#### `void TransportToWaypoint(object oPC, object oWaypoint)`
> Transport a player and his/her associates to a waypoint.
> This does NOT transport the rest of the player's party,
> only their henchman, summoned, dominated, etc.

#### `void TransportToLocation(object oPC, location oLoc)`
> Transport a player and his/her associates to a location.
> This does NOT transport the rest of the player's party,
> only their henchman, summoned, dominated, etc.

#### `void TransportAllToWaypoint(object oPC, object oWay)`
> Transport an entire party to a waypoint

#### `void TransportAllToLocation(object oPC, location lLoc)`
> Transport an entire party to a location

#### `void TravelToObject(object oDest, object oTarget = OBJECT_SELF, int bRun = FALSE, float fDelay = 10.0)`
> Target goes to specified destination object intelligently.
> If location is in same area, walk (or run) there.
> If location is in different area, walk (or run) to
> nearest waypoint or door, then jump.
> If either of these fail, jump after a timeout.

#### `void TravelToLocation(location lDest, object oTarget = OBJECT_SELF, int bRun = FALSE, float fDelay = 10.0)`
> Target goes to specified location intelligently. See
> TravelToObject for description.

#### `object GetNearestExit(object oTarget = OBJECT_SELF)`
> Find nearest exit to target (either door or trigger or
> (failing those) waypoint).

#### `object GetBestExitByType(object oTarget = OBJECT_SELF, object oTargetArea = OBJECT_INVALID, int nObjType = OBJECT_TYPE_DOOR)`
> Private function: find the best exit of the desired type.

#### `object GetBestExit(object oTarget = OBJECT_SELF, object oTargetArea = OBJECT_INVALID)`
> Find best exit based on desired target area

#### `void TransportToWaypoint(object oPC, object oWaypoint)`
> Transport a player and his/her associates to a waypoint.
> This does NOT transport the rest of the player's party,
> only their henchman, summoned, dominated, etc.

#### `void TransportToLocation(object oPC, location oLoc)`
> Transport a player and his/her associates to a location.
> This does NOT transport the rest of the player's party,
> only their henchman, summoned, dominated, etc.

#### `void TransportAllToWaypoint(object oPC, object oWaypoint)`
> Transport an entire party with all associates to a waypoint.

#### `void TransportAllToLocation(object oPC, location oLoc)`
> Transport an entire party with all associates to a location.
