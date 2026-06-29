# `x0_i0_walkway.nss`

Source: `NSS/x0_/x0_i0_walkway.nss`  
9 functions · 5 constants

## Constants

| Constant | Type | Value | Note |
|---|---|---|---|
| `sWalkwayVarname` | string | `"NW_WALK_CONDITION"` |  |
| `NW_WALK_FLAG_INITIALIZED` | int | `0x00000001` |  |
| `NW_WALK_FLAG_CONSTANT` | int | `0x00000002` |  |
| `NW_WALK_FLAG_IS_DAY` | int | `0x00000004` |  |
| `NW_WALK_FLAG_BACKWARDS` | int | `0x00000008` |  |

## Functions

#### `int GetWalkCondition(int nCondition, object oCreature = OBJECT_SELF)`
> Get whether the condition is set

#### `void SetWalkCondition(int nCondition, int bValid = TRUE, object oCreature = OBJECT_SELF)`
> Set a given condition

#### `string GetWaypointSuffix(int i)`
> Get a waypoint number suffix, padded if necessary

#### `void LookUpWalkWayPoints()`
> Look up the caller's waypoints and store them on the creature.
> Waypoint variables:
> WP_NUM     : number of day waypoints
> WN_NUM     : number of night waypoints
> WP_#, WN_# : the waypoint objects
> WP_CUR     : the current waypoint number
> bCrossAreas: if set to TRUE, the creature will travel between areas to reach
> its waypoint

#### `object GetNextWalkWayPoint(object oCreature = OBJECT_SELF)`
> Get the creature's next waypoint.
> If it has just become day/night, or if this is
> the first time we're getting a waypoint, we go
> to the nearest waypoint in our new set.

#### `int GetNearestWalkWayPoint(object oCreature = OBJECT_SELF)`
> Get the number of the nearest of the creature's current
> set of waypoints (respecting day/night).

#### `void WalkWayPoints(int nRun = FALSE, float fPause = 1.0)`
> HEAVILY REVISED!
> The previous version of this function was too little
> bang-for-the-buck, as it set up an infinite loop and
> made creatures walk around even when there was no one
> in the area.
> Now, each time this function is called, the caller
> will move to their next waypoint. The OnHeartbeat and
> OnPerception scripts have been modified to call this
> function as appropriate.
> However, also note that the mobile ambient animations
> have been heavily revised. For most creatures, those
> should now be good enough, especially if you put down
> some "NW_STOP" waypoints for them to wander among.
> Specific waypoints will now be more for creatures that
> you really want to patrol back and forth along a pre-set
> path.

#### `int CheckWayPoints(object oWalker = OBJECT_SELF)`
> Check to make sure that the walker has at least one valid
> waypoint they will walk to at some point (day or night).

#### `int GetIsPostOrWalking(object oWalker = OBJECT_SELF)`
> Check to see if the specified object is currently walking
> waypoints or standing at a post.
