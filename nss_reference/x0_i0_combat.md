# `x0_i0_combat.nss`

Source: `NSS/x0_/x0_i0_combat.nss`  
7 functions · 5 constants

## Constants

| Constant | Type | Value | Note |
|---|---|---|---|
| `sCombatCondVarname` | string | `"X0_COMBAT_CONDITION"` |  |
| `X0_COMBAT_FLAG_RANGED` | int | `0x00000001` |  |
| `X0_COMBAT_FLAG_DEFENSIVE` | int | `0x00000002` |  |
| `X0_COMBAT_FLAG_COWARDLY` | int | `0x00000004` |  |
| `X0_COMBAT_FLAG_AMBUSHER` | int | `0x00000008` |  |

## Functions

#### `int GetCombatCondition(int nCond, object oTarget = OBJECT_SELF)`
> Determine whether the specified X0_COMBAT_FLAG_* is set on the target

#### `void SetCombatCondition(int nCond, int bValid = TRUE, object oTarget = OBJECT_SELF)`
> Set one of the X0_COMBAT_FLAG_* values on the target

#### `int SpecialTactics(object oTarget)`
> This function checks for the special tactics flags and
> chooses tactics appropriately for each.
> Currently available:
> X0_COMBAT_FLAG_{RANGED,DEFENSIVE,COWARDLY,AMBUSHER}
> Note that only one special tactics flag should be applied
> to a single creature for the most part!
> Returns TRUE on success, FALSE on failure.

#### `int SpecialTacticsRanged(object oTarget)`
> Special tactics for ranged fighters.
> The caller will attempt to stay in ranged distance and
> will make use of active ranged combat feats (Rapid Shot
> and Called Shot).
> If the target is too close and is not currently attacking
> the caller, the caller will instead try to find a ranged
> enemy to attack. If that fails, the caller will try to run
> away from the target to a ranged distance.
> This will fall through and return FALSE after three
> consecutive attempts to get away from an opponent within
> melee distance, at which point the caller will use normal
> tactics until they are again at a ranged distance from
> their target.
> Returns TRUE on success, FALSE on failure.

#### `int SpecialTacticsAmbusher(object oTarget)`
> Special tactics for ambushers.
> Ambushers will first attempt to get out of sight
> of their target if currently visible to that target.
> If not visible to the target, they will use any invisibility/
> hide powers they have.
> Once hidden, they will then attempt to attack the target using
> standard AI.
> Returns TRUE on success, FALSE on failure.

#### `int SpecialTacticsCowardly(object oTarget)`
> Special tactics for cowardly creatures
> Cowards act as follows:
> - if you and your friends outnumber the enemy by 6:1 or
> by more than 10, fall through to normal combat.
> - if you are currently being attacked by a melee attacker,
> fight defensively (see SpecialTacticsDefensive).
> - if there is a "NW_SAFE" waypoint in your area that is
> out of sight of the target, run to it.
> - otherwise, run away randomly from the target.
> Returns TRUE on success, FALSE on failure.

#### `int SpecialTacticsDefensive(object oTarget)`
> Special tactics for defensive fighters
> This will attempt to use the active defensive feats such as
> Knockdown and Expertise, and also use Parry mode, when these
> are appropriate. Falls through to standard combat on failure.
> Returns TRUE on success, FALSE on failure.
