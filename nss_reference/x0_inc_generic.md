# `x0_inc_generic.nss`

Source: `NSS/x0_/x0_inc_generic.nss`  
17 functions · 1 constants

## Constants

| Constant | Type | Value | Note |
|---|---|---|---|
| `NO_SMART` | int | `FALSE` |  |

## Functions

#### `void bkSetupBehavior(int nBehaviour)`
> Set up our hated class

#### `int GetCombatDifficulty(object oRelativeTo = OBJECT_SELF, int bEnable = FALSE)`
> Return the combat difficulty.
> This is only used for henchmen and its only function currently
> is to keep henchmen from casting spells in an easy fight.
> This determines the difficulty by counting the number of allies
> and enemies and their respective CRs, then converting the value
> into a "spell CR" rating.
> A value of 20 means use whatever you have, a negative value
> means a very easy fight.

#### `object bkAcquireTarget()`
> Determine our target for the next combat round.
> Normally, this will be the same target as the last round.
> The only time this changes is if the target is gone/killed
> or they are in dying mode.

#### `object ChooseNewTarget()`
> Choose a new nearby target. Target must be an enemy, perceived,
> and not in dying mode. If possible, we first target members of
> a class we "hate" -- this is generally random, to keep everyone
> from attacking the same target.

#### `int GetCRMax()`
> Determines the Spell CR to be used in the
> given situation
> BK: changed this. It returns the the max CR for
> this particular scenario.
> NOTE: Will apply to all creatures though it may
> be necessary to limit it just for associates.
> Created By: Preston Watamaniuk
> Created On: Nov 18, 2001

#### `int bkEvaluationSanityCheck(object oIntruder, float fFollow)`
> Returns true if something that shouldn't
> have happened, happens. Will abort this combat
> round.

#### `int bkTalentFilter(talent tUse, object oTarget, int bJustTest = FALSE)`
> This function is the last minute filter to prevent
> any inappropriate effects from being applied
> to inapproprite creatures.
> Returns TRUE if the talent was valid, FALSE otherwise.
> If an invalid talent is attempted, we instead perform
> a standard melee attack to avoid AI stopping.
> Based on Pausanias's Final Talent Filter.
> Parameters
> bJustTest = If this is true the function only does a test
> the action stack is NOT modified at all

#### `void SetLastGenericSpellCast(int nSpell)`
> Sets a local variable for the last spell used

#### `int GetLastGenericSpellCast()`
> Returns a SPELL_ constant for the last spell used

#### `int CompareLastSpellCast(int nSpell)`
> Compares the current spell with the last one cast

#### `int GetIsFighting(object oFighting)`
> Does a check to determine if the NPC has an attempted
> spell or attack target

#### `void bkSetupBehavior(int nBehaviour)`

#### `int GetCombatDifficulty(object oRelativeTo = OBJECT_SELF, int bEnable = FALSE)`
> Return the combat difficulty.
> This is only used for henchmen and its only function currently
> is to keep henchmen from casting spells in an easy fight.
> This determines the difficulty by counting the number of allies
> and enemies and their respective CRs, then converting the value
> into a "spell CR" rating.
> A value of 20 means use whatever you have, a negative value
> means a very easy fight.
> Only does something if Enable is turned on, since I originally turned this function off

#### `object bkAcquireTarget()`
> This function returns the target for this combat round.
> Normally, this will be the same target as the last round.
> The only time this changes is if the target is gone/killed
> or they are in dying mode.

#### `object ChooseNewTarget()`
> Choose a new nearby target. Target must be an enemy, perceived,
> and not in dying mode. If possible, we first target members of
> a class we hate.

#### `int GetCRMax()`
> Created By: Preston Watamaniuk
> Created On: Nov 18, 2001

#### `int bkEvaluationSanityCheck(object oIntruder, float fFollow)`
