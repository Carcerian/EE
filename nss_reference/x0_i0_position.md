# `x0_i0_position.nss`

Source: `NSS/x0_/x0_i0_position.nss`  
64 functions · 5 constants

## Constants

| Constant | Type | Value | Note |
|---|---|---|---|
| `DISTANCE_TINY` | float | `1.0` |  |
| `DISTANCE_SHORT` | float | `3.0` |  |
| `DISTANCE_MEDIUM` | float | `5.0` |  |
| `DISTANCE_LARGE` | float | `10.0` |  |
| `DISTANCE_HUGE` | float | `20.0` |  |

## Functions

#### `string LocationToString(location loc)`
> Turn a location into a string. Useful for debugging.

#### `string VectorToString(vector vec)`
> Turn a vector into a string. Useful for debugging.

#### `void MoveToNewLocation(location lNewLocation, object oTarget = OBJECT_SELF)`
> This actually moves the target to the given new location,
> and makes them face the correct way once they get there.

#### `float GetChangeInX(float fDistance, float fAngle)`
> This returns the change in X coordinate that should be made to
> cause an object to be fDistance away at fAngle.

#### `float GetChangeInY(float fDistance, float fAngle)`
> This returns the change in Y coordinate that should be made to
> cause an object to be fDistance away at fAngle.

#### `vector GetChangedPosition(vector vOriginal, float fDistance, float fAngle)`
> This returns a new vector representing a position that is fDistance
> meters away at fAngle from the original position.
> If a negative coordinate is generated, the absolute value will
> be used instead.

#### `float GetAngleBetweenLocations(location lOne, location lTwo)`
> This returns the angle between two locations

#### `float GetOppositeDirection(float fDirection)`
> This returns the opposite direction (ie, this is the direction you
> would use to set something facing exactly opposite the way of
> something else that's facing in direction fDirection).

#### `float GetRightDirection(float fDirection)`
> This returns the direction directly to the right. (IE, what
> you would use to make an object turn to the right.)

#### `float GetHalfRightDirection(float fDirection)`
> This returns a direction that's a half-turn to the right

#### `float GetFarRightDirection(float fDirection)`
> This returns a direction one and a half turns to the right

#### `float GetCustomRightDirection(float fDirection, float fAngle)`
> This returns a direction a specified angle to the right

#### `float GetLeftDirection(float fDirection)`
> This returns the direction directly to the left. (IE, what
> you would use to make an object turn to the left.)

#### `float GetHalfLeftDirection(float fDirection)`
> This returns a direction that's a half-turn to the left

#### `float GetFarLeftDirection(float fDirection)`
> This returns a direction one and a half turns to the left

#### `float GetCustomLeftDirection(float fDirection, float fAngle)`
> This returns a direction a specified angle to the left

#### `void TurnToFaceObject(object oObjectToFace, object oTarget = OBJECT_SELF)`
> Turns the target object to face the specified object

#### `location GetFlankingRightLocation(object oTarget)`
> Returns the location flanking the target to the right
> (slightly behind) and facing same direction as the target
> (useful for backup)

#### `location GetFlankingLeftLocation(object oTarget)`
> Returns the location flanking the target to the left
> (slightly behind) and facing same direction as the target.
> (useful for backup)

#### `location GetOppositeLocation(object oTarget)`
> Returns a location directly opposite the target and
> facing the target

#### `location GetAheadLocation(object oTarget)`
> Returns location directly ahead of the target and facing
> same direction as the target

#### `location GetBehindLocation(object oTarget)`
> Returns location directly behind the target and facing same
> direction as the target (useful for backstabbing attacks)

#### `location GetForwardFlankingRightLocation(object oTarget)`
> Returns location to the forward right flank of the target
> and facing the same way as the target
> (useful for guarding)

#### `location GetForwardFlankingLeftLocation(object oTarget)`
> Returns location to the forward left flank of the target
> and facing the same way as the target
> (useful for guarding)

#### `location GetAheadRightLocation(object oTarget)`
> Returns location to the forward right and facing the target.
> (useful for one of two people facing off against the target)

#### `location GetAheadLeftLocation(object oTarget)`
> Returns location to the forward left and facing the target.
> (useful for one of two people facing off against the target)

#### `location GetStepLeftLocation(object oTarget)`
> Returns location just a step to the left
> (Let's do the time warp...)

#### `location GetStepRightLocation(object oTarget)`
> Returns location just a step to the right

#### `location GetRandomLocation(object oArea, object oSource = OBJECT_INVALID, float fDist = 0.0)`
> Get a random location in a given area based on a given object,
> the specified distance away.
> If no object is given, will use a random object in the area.
> If that is not available, will use the roughly-center point
> of the area.
> If distance is set to 0.0, a random distance will be used.

#### `void SpeakLocation(location lLoc)`
> Speak location -- private function for debugging

#### `void PrintLocation(location lLoc)`
> Print location --- private function for debugging

#### `string LocationToString(location loc)`
> Turn a location into a string. Useful for debugging.

#### `string VectorToString(vector vec)`
> Turn a vector into a string. Useful for debugging.

#### `void MoveToNewLocation(location lNewLocation, object oTarget = OBJECT_SELF)`
> This actually moves the target to the given new location,
> and makes them face the correct way once they get there.

#### `float GetChangeInX(float fDistance, float fAngle)`
> This returns the change in X coordinate that should be made to
> cause an object to be fDistance away at fAngle.

#### `float GetChangeInY(float fDistance, float fAngle)`
> This returns the change in Y coordinate that should be made to
> cause an object to be fDistance away at fAngle.

#### `vector GetChangedPosition(vector vOriginal, float fDistance, float fAngle)`
> This returns a new vector representing a position that is fDistance
> meters away in the direction fAngle from the original position.
> If a negative coordinate is generated, the absolute value will
> be used instead.

#### `float GetAngleBetweenLocations(location lOne, location lTwo)`
> This returns the angle between two locations

#### `float GetNormalizedDirection(float fDirection)`
> This returns a direction normalized to the range 0.0 - 360.0

#### `float GetOppositeDirection(float fDirection)`
> This returns the opposite direction (ie, this is the direction you
> would use to set something facing exactly opposite the way of
> something else that's facing in direction fDirection).

#### `float GetRightDirection(float fDirection)`
> This returns the direction directly to the right. (IE, what
> you would use to make an object turn to the right.)

#### `float GetHalfRightDirection(float fDirection)`
> This returns a direction that's a half-turn to the right

#### `float GetFarRightDirection(float fDirection)`
> This returns a direction one and a half turns to the right

#### `float GetCustomRightDirection(float fDirection, float fAngle)`
> This returns a direction a specified angle to the right

#### `float GetLeftDirection(float fDirection)`
> This returns the direction directly to the left. (IE, what
> you would use to make an object turn to the left.)

#### `float GetHalfLeftDirection(float fDirection)`
> This returns a direction that's a half-turn to the left

#### `float GetFarLeftDirection(float fDirection)`
> This returns a direction one and a half turns to the left

#### `float GetCustomLeftDirection(float fDirection, float fAngle)`
> This returns a direction a specified angle to the left

#### `void TurnToFaceObject(object oObjectToFace, object oTarget = OBJECT_SELF)`
> Turns the object to face the specified object

#### `location GenerateNewLocation(object oTarget, float fDistance, float fAngle, float fOrientation)`
> Private function -- we use this to get the new location

#### `location GenerateNewLocationFromLocation(location lTarget, float fDistance, float fAngle, float fOrientation)`
> Private function -- we use this to get the new location
> from a source location.

#### `location GetFlankingRightLocation(object oTarget)`
> This returns the location flanking the target to the right

#### `location GetFlankingLeftLocation(object oTarget)`
> Returns the location flanking the target to the left
> (slightly behind) and facing same direction as the target.
> (useful for backup)

#### `location GetOppositeLocation(object oTarget)`
> Returns a location directly ahead of the target and
> facing the target

#### `location GetAheadLocation(object oTarget)`
> Returns location directly ahead of the target and facing
> same direction as the target

#### `location GetBehindLocation(object oTarget)`
> Returns location directly behind the target and facing same
> direction as the target (useful for backstabbing attacks)

#### `location GetForwardFlankingRightLocation(object oTarget)`
> Returns location to the forward right flank of the target
> and facing the same way as the target
> (useful for guarding)

#### `location GetForwardFlankingLeftLocation(object oTarget)`
> Returns location to the forward left flank of the target
> and facing the same way as the target
> (useful for guarding)

#### `location GetAheadRightLocation(object oTarget)`
> Returns location to the forward right and facing the target.
> (useful for one of two people facing off against the target)

#### `location GetAheadLeftLocation(object oTarget)`
> Returns location to the forward left and facing the target.
> (useful for one of two people facing off against the target)

#### `location GetStepLeftLocation(object oTarget)`
> Returns location just a step to the left
> (Let's do the time warp...)

#### `location GetStepRightLocation(object oTarget)`
> Returns location just a step to the right

#### `location GetCenterPointOfArea(object oArea)`
> Get the (roughly) center point of an area.
> This works by going through all the objects in an area and
> getting their positions, so it is resource-intensive.

#### `location GetRandomLocation(object oArea, object oSource = OBJECT_INVALID, float fDist = 0.0)`
> Get a random location in a given area based on a given object,
> the specified distance away.
> If no object is given, will use a random object in the area.
> If that is not available, will use the roughly-center point
> of the area.
> If distance is set to 0.0, a random distance will be used.
