# `x0_i0_infinite.nss`

Source: `NSS/x0_/x0_i0_infinite.nss`  
40 functions · 14 constants

## Constants

| Constant | Type | Value | Note |
|---|---|---|---|
| `INF_AREA` | string | `INF_BASE + "_AREA"` |  |
| `INF_REWARD` | string | `INF_BASE + "_REWARD"` |  |
| `INF_REWARD_KEY` | string | `INF_BASE + "_REWARD_KEY"` |  |
| `INF_TRANS` | string | `INF_BASE + "_TRANS"` |  |
| `INF_WARN` | string | `INF_BASE + "_WARN"` |  |
| `INF_START` | string | `INF_BASE + "_START"` |  |
| `INF_OUT_OF_POOL` | string | `INF_BASE + "_OUT_OF_POOL"` |  |
| `INF_FIXED_LOC` | string | `INF_BASE + "_FIXED_LOC"` |  |
| `INF_ENTERED` | string | `INF_BASE + "_ENTERED"` |  |
| `INF_COMPLETED` | string | `INF_BASE + "_COMPLETED"` |  |
| `INF_CURRENT` | string | `INF_BASE + "_CURRENT"` |  |
| `INF_NTRANS` | string | `INF_BASE + "_NTRANS"` |  |
| `INF_RUNLEN` | string | `INF_BASE + "_RUNLEN"` |  |
| `INF_MSG_DELAY` | float | `4.0` |  |

## Functions

#### `object INF_GetCurrentStartingPoint(object oObj)`
> Get the starting point for this run

#### `void INF_SetCurrentStartingPoint(object oObj, object oStart)`
> Set the starting point for this run
> If OBJECT_INVALID is passed in for oStart, it will
> clear the variable.

#### `int INF_GetIsInInfiniteSpace(object oPC)`
> Determine whether the player is currently inside an infinite
> area.

#### `int INF_GetHasEntered(object oPC, object oStart)`
> Get whether the PC has entered this starting point's run before

#### `void INF_SetHasEntered(object oPC, object oStart)`
> Set whether the PC has entered this starting point's run before

#### `int INF_GetHasCompleted(object oPC, object oStart)`
> Get whether the PC has completed this run before

#### `void INF_SetHasCompleted(object oPC, object oStart)`
> Set whether the PC has completed this run before

#### `int INF_GetNumberTransitionsPassed(object oPC)`
> Get the number of transitions passed var on PC

#### `void INF_SetNumberTransitionsPassed(object oPC, int nTrans = 0)`
> Set the number of transitions passed var (default is 0)

#### `void INF_IncrNumberTransitionsPassed(object oPC)`
> Increment the number of transitions passed var

#### `int INF_GetRunLength(object oPC)`
> Get the run length var on the PC

#### `void INF_SetRunLength(object oPC, int nLen)`
> Set the run length on the PC

#### `int INF_GetIsInPool(object oArea)`
> Returns TRUE if the area is not currently taken.

#### `void INF_SetIsInPool(object oArea, int bInPool = TRUE)`
> Mark the area as taken or not

#### `object INF_GetFixedLocation(object oTrans)`
> Get the fixed location of the transition, OBJECT_INVALID if not set

#### `void INF_SetFixedLocation(object oTrans, object oLocation)`
> Set the fixed location of a transition

#### `int INF_GetHasFinishedRunLength(object oPC)`
> Returns TRUE if the player has reached the end of the run length

#### `object INF_GetRewardArea(object oPC)`
> Get the reward area, or OBJECT_INVALID if it doesn't exist

#### `object INF_GetRewardKey(object oPC)`
> Get the reward area key item or OBJECT_INVALID if it doesn't exist

#### `int INF_GetPartyHasRewardKey(object oPC)`
> TRUE if the player or a party member has the reward key

#### `object INF_GetAreaFromPool(object oPC)`
> Retrieve an area from the pool. If no area is available in the pool,
> return OBJECT_INVALID.

#### `void INF_AreaSetup(object oArea, object oPC)`
> Set up a generic area, possibly specific to the PC triggering

#### `void INF_ItemCleanup(object oItem, object oStart)`
> Handle item cleanup

#### `void INF_AreaCleanup(object oArea)`
> Clean up a generic area

#### `void INF_SetupPC(object oPC, object oStart)`
> Set up the PC on infinite run entry for the specified
> starting point.

#### `void INF_CleanupPC(object oPC)`
> Clean up the PC on infinite run exit

#### `void INF_CleanupTransition(object oTrans)`
> Clean up a transition

#### `void INF_TransportToStartingPoint(object oPC)`
> Send the PC back to the starting point

#### `int INF_GetIsPartyLeaderInRange(object oPC)`
> TRUE if the PC's party leader is in the same desert area but
> not in the same room.

#### `void INF_TransportToPartyLeader(object oPC)`
> Send the PC to join the party leader, if in range.

#### `object INF_GetReturnTransition(object oTrans, object oDestArea)`
> Get the return transition in the destination area

#### `void INF_SendMessage(object oPC, string sMessage)`
> Send a message to the PC after a delay.
> Replaces <CUSTOM0> with the name of the area the PC is in,
> if the message contains that.

#### `void INF_TransportToNewArea(object oPC, object oTrans, object oArea = OBJECT_INVALID)`
> Set up a new area and transport the PC through it.
> Can also do this with a specified reward area
> as an argument.

#### `void INF_DoFirstTransition(object oPC, object oTrans)`
> Handle the first transition into an area

#### `void INF_DoTransition(object oPC, object oTrans)`
> Master transition function
> This is what actually handles most of the work.
> See internal comments to the function for details.

#### `int INF_GetNumGenericAreas()`
> Get the number of generic areas that exist (not necessarily the
> number that are currently available).

#### `void INF_TransportToTransition(object oPC, object oTrans)`
> Send the PC to a good position inside the given transition

#### `int INF_GetIsTransition(object oTrig)`
> TRUE if the object is an infinite transition trigger

#### `object INF_GetNearestTransition(object oSource)`
> Get the nearest transition to the object

#### `void INF_ReallySendMessage(object oPC, string sMessage)`
> Deliberately not prototyped! Do not use outside this
> library. Use INF_SendMessage instead.
> This is the function that actually sends the message.
