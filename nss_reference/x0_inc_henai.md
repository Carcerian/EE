# `x0_inc_henai.nss`

Source: `NSS/x0_/x0_inc_henai.nss`  
17 functions · 7 constants

## Constants

| Constant | Type | Value | Note |
|---|---|---|---|
| `BK_HEALINMELEE` | int | `10` |  |
| `BK_CURRENT_AI_MODE` | int | `20` | Can only be in one AI mode at a time |
| `BK_AI_MODE_FOLLOW` | int | `9` | default mode, moving after the player |
| `BK_AI_MODE_RUN_AWAY` | int | `19` | something is causing AI to retreat |
| `BK_NEVERFIGHT` | int | `30` |  |
| `BK_HEALTHRESHOLD` | float | `5.0` |  |
| `BK_FOLLOW_THRESHOLD` | float | `15.0` |  |

## Functions

#### `void bkSetListeningPatterns()`
> Sets up special additional listening patterns
> for associates.

#### `void HenchmenCombatRound(object oIntruder = OBJECT_INVALID)`
> Henchman/associate combat round wrapper
> passing in OBJECT_INVALID is okay
> Does special stuff for henchmen and familiars, then
> falls back to default generic combat code.

#### `int bkAttemptToDisarmTrap(object oTrap, int bWasShout = FALSE)`
> Attempt to disarm given trap
> (called from RespondToShout and heartbeat)

#### `int bkAttemptToOpenLock(object oLocked)`
> Attempt to open a given locked object.

#### `int bkManualPickNearestLock()`
> Manually pick the nearest locked object

#### `void bkRespondToHenchmenShout(object oShouter, int nShoutIndex, object oIntruder = OBJECT_INVALID, int nBanInventory = FALSE)`
> Handles responses to henchmen commands, including both radial
> menu and voice commands.

#### `int bkCombatAttemptHeal()`
> Attempt to heal self then master

#### `int bkCombatFollowMaster()`
> Attempts to follow master if outside range

#### `void bkSetBehavior(int nBehavior, int nValue)`
> set behavior used by AI

#### `int bkGetBehavior(int nBehavior)`
> get behavior used by AI

#### `int bkGetIsDoorInLineOfSight(object oTarget)`
> TRUE if the target door is in line of sight.

#### `float bkGetCosAngleBetween(object Loc1, object Loc2)`
> Get the cosine of the angle between two objects.

#### `int bkGetIsInLineOfSight(object oTarget, object oSeer = OBJECT_SELF)`
> TRUE if target in the line of sight of the seer.

#### `void SendForHelp()`
> called from state scripts (nw_g0_charm) to signal
> to other party members to help me out

#### `void SendForHelp()`
> called from state scripts (nw_g0_charm) to signal
> to other party members to help me out

#### `void bkSetListeningPatterns()`
> Sets up any special listening patterns in addition to the default
> associate ones that are used

#### `void HenchmenCombatRound(object oIntruder)`
> Special combat round precursor for associates
