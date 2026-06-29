# `x0_i0_enemy.nss`

Source: `NSS/x0_/x0_i0_enemy.nss`  
17 functions · 1 constants

## Constants

| Constant | Type | Value | Note |
|---|---|---|---|
| `MELEE_DISTANCE` | float | `3.0` |  |

## Functions

#### `object GetNearestEnemy(object oSource = OBJECT_SELF, int nNth = 1)`
> Gets the nearest enemy.

#### `object GetNearestPerceivedEnemy(object oSource = OBJECT_SELF, int nNth = 1, int nCriteriaType = 1000, int nCriteriaValue = 1000)`
> Returns the nearest object that can be seen, then checks for
> the nearest heard target.
> You may pass in any of the CREATURE_TYPE_* constants
> used in GetNearestCreature as nCriteriaType, with
> corresponding values for nCriteriaValue, to get a more
> specific result.
> KLUDGE: Huge default values used here for nCriteriaType/Value
> because -1 cannot be passed in at the moment due to a
> compiler bug. Should be changed to -1 once that's fixed.

#### `object GetNearestSeenEnemy(object oSource = OBJECT_SELF, int nNth = 1)`
> Get the nearest seen enemy. This will NOT return an enemy that is
> heard but not seen; for that, use GetNearestPerceivedEnemy instead.

#### `object GetNearestSeenOrHeardEnemy(object oSource = OBJECT_SELF, int nNth = 1)`
> Returns the nearest object that can be seen, then checks for
> the nearest heard target.
> Now just a wrapper around GetNearestPerceivedEnemy.

#### `object GetNearestSeenFriend(object oSource = OBJECT_SELF, int nNth = 1)`
> Get the nearest seen friend.

#### `struct sSituation CountEnemiesAndAllies(float fRadius = 20.0, object oSource = OBJECT_SELF)`
> Count the number of enemies and allies in a given radius
> and their respective total CRs (slightly rounded, since
> we use integers instead of floats).
> This returns a "struct sSituation" type value. To use, do
> something like the following:
> struct sSituation sitCurr = CountEnemiesAndAllies(20.0);
> int nNumEnemies = sitCurr.ENEMY_NUM;
> int nNumAllies = sitCurr.ALLY_NUM;
> int nAllyCR = sitCurr.ALLY_CR;
> int nEnemyCR = sitCurr.ENEMY_CR;

#### `struct sEnemies DetermineEnemies()`
> Categorizes the enemies the creature is facing
> into four types: fighters, clerics, mages, monsters.
> Determines the number of HD of each type as well
> as total number of enemies and total enemy HD.

#### `string GetMostDangerousClass(struct sEnemies sCount)`
> Use the four archetypes to determine the
> most dangerous group type facing the NPC

#### `int GetIsMeleeAttacker(object oAttacker)`
> Returns TRUE if the given opponent is a melee
> attacker, meaning they are in melee range and
> equipped with a melee weapon.

#### `int GetIsRangedAttacker(object oAttacker)`
> Returns TRUE if the given opponent is a ranged
> attacker, meaning they are outside melee range.

#### `int GetIsWieldingRanged(object oAttacker)`
> Returns TRUE if the given opponent is wielding a
> ranged weapon.

#### `int GetNumberOfMeleeAttackers()`
> Calculate the number of people currently attacking self.

#### `int GetNumberOfRangedAttackers()`
> Calculate the number of people attacking self from beyond 5m

#### `int GetRacialTypeCount(int nRacial_Type)`
> Determine the number of targets within 20m that are of the
> specified racial-type

#### `int CheckFriendlyFireOnTarget(object oTarget, float fDistance = 5.0)`
> Returns the number of persons who are considered friendly to the target.

#### `int CheckEnemyGroupingOnTarget(object oTarget, float fDistance = 5.0)`
> Returns the number of enemies on a target.

#### `object FindSingleRangedTarget()`
> Find a single target who is an enemy with 30m of self
