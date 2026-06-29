# `x0_i0_talent.nss`

Source: `NSS/x0_/x0_i0_talent.nss`  
66 functions · 8 constants

## Constants

| Constant | Type | Value | Note |
|---|---|---|---|
| `TALENT_ANY` | int | `20` |  |
| `COND_CURSE` | int | `0x00000001` |  |
| `COND_POISON` | int | `0x00000002` |  |
| `COND_DISEASE` | int | `0x00000004` |  |
| `COND_ABILITY` | int | `0x00000008` |  |
| `COND_DRAINED` | int | `0x00000010` |  |
| `COND_BLINDDEAF` | int | `0x00000020` |  |
| `WHIRL_DISTANCE` | float | `3.0` | * Shortened distance so its more effective (went from 5.0 to 2.0 and up to 3.0) |

## Functions

#### `int TryKiDamage(object oTarget)`
> Tries to do the Ki Damage ability

#### `int TrySpell(int nSpell, object oTarget = OBJECT_SELF, object oCaster = OBJECT_SELF)`
> Try a spell to produce a particular spell effect.
> This will only cast the spell if the target DOES NOT already have the
> given spell effect, and the caster possesses the spell.
> Returns TRUE on success, FALSE on failure.

#### `int TrySpellForEffect(int nSpell, int nEffect, object oTarget = OBJECT_SELF, object oCaster = OBJECT_SELF)`
> Try a spell corresponding to a particular effect.
> This will only cast the spell if the target DOES have the
> given effect, and the caster possesses the spell.
> Returns TRUE on success, FALSE on failure.

#### `int TryTalent(talent tUse, object oTarget = OBJECT_SELF, object oCaster = OBJECT_SELF)`
> Try a given talent.
> This will only cast spells and feats if the targets do not already
> have the effects of those feats, and will funnel all talents
> through bkTalentFilter for a final check.

#### `int TalentUseProtectionOnSelf()`
> PROTECT SELF
> Returns TRUE on successful use of such a talent, FALSE otherwise.

#### `int TalentUseProtectionOthers(object oDefault = OBJECT_INVALID)`
> PROTECT PARTY
> Returns TRUE on successful use of such a talent, FALSE otherwise.

#### `int TalentEnhanceOthers()`
> ENHANCE OTHERS
> Returns TRUE on successful use of such a talent, FALSE otherwise.

#### `int TalentUseEnhancementOnSelf()`
> ENHANCE SELF
> Returns TRUE on successful use of such a talent, FALSE otherwise.

#### `int genericDoHarmfulRangedAttack(talent tUse, object oTarget)`
> SPELL CASTER MELEE ATTACKED
> Wrote this function so I could do further
> checks such as making them not cast
> Dispel Magic.
> Possible Issue (brent): It may get stuck on
> dispel magics...trying to cast them
> and not proceed down Area Of Effect Discriminants...
> SOLUTION: If this function returns true the TalentMeleeAttacked routine
> will exit, however if it returns false, it will try and find some
> other ability to use.

#### `int genericAttemptHarmfulRanged(talent tUse, object oTarget)`
> Will return true if it succesfully
> used a harmful ranged talent.

#### `int TalentMeleeAttacked(object oIntruder = OBJECT_INVALID)`
> MELEE ATTACKED
> Returns TRUE on successful use of such a talent, FALSE otherwise.

#### `int TalentRangedAttackers(object oIntruder = OBJECT_INVALID)`
> SPELL CASTER RANGED ATTACKED
> Returns TRUE on successful use of such a talent, FALSE otherwise.

#### `int TalentRangedEnemies(object oIntruder = OBJECT_INVALID)`
> SPELL CASTER WITH RANGED ENEMIES
> Returns TRUE on successful use of such a talent, FALSE otherwise.

#### `int TalentSummonAllies()`
> SUMMON ALLIES
> Returns TRUE on successful use of such a talent, FALSE otherwise.

#### `int TalentHealingSelf(int bForce = FALSE)`
> HEAL SELF WITH POTIONS AND SPELLS
> Returns TRUE on successful use of such a talent, FALSE otherwise.

#### `int TalentHeal(int nForce = FALSE, object oTarget = OBJECT_SELF)`
> Use spells only on others and self
> Returns TRUE on successful use of such a talent, FALSE otherwise.

#### `int TalentMeleeAttack(object oIntruder = OBJECT_INVALID)`
> MELEE ATTACK OTHERS
> ISSUE 1: Talent Melee Attack should set the Last Spell Used
> to 0 so that melee casters can use a single special ability.
> Returns TRUE on successful use of such a talent, FALSE otherwise.

#### `int TalentSneakAttack()`
> SNEAK ATTACK OTHERS
> Returns TRUE on successful use of such a talent, FALSE otherwise.

#### `int TalentFlee(object oIntruder = OBJECT_INVALID)`
> FLEE COMBAT AND HOSTILES
> Returns TRUE on successful use of such a talent, FALSE otherwise.

#### `int TalentUseTurning()`
> TURN UNDEAD
> Returns TRUE on successful use of such a talent, FALSE otherwise.

#### `int TalentPersistentAbilities()`
> ACTIVATE AURAS
> Returns TRUE on successful use of such a talent, FALSE otherwise.

#### `int TalentAdvancedBuff(float fDistance, int bInstant = TRUE)`
> FAST BUFF SELF
> Returns TRUE on successful use of such a talent, FALSE otherwise.

#### `int TalentBuffSelf()`
> USE POTIONS
> Used for Potions of Enhancement and Protection
> Returns TRUE on successful use of such a talent, FALSE otherwise.

#### `int TalentSeeInvisible()`
> USE SPELLS TO DEFEAT INVISIBLE CREATURES
> THIS TALENT IS NOT USED
> Returns TRUE on successful use of such a talent, FALSE otherwise.

#### `int GetHasNegativeCondition(int nCondition, int nCurrentConditions)`
> Utility function for TalentCureCondition
> Checks to see if the creature has the given condition in the
> given condition value.
> To use, you must first calculate the nCurrentConditions value
> with GetCurrentNegativeConditions.
> The value of nCondition can be any of the COND_* constants
> declared in x0_i0_talent.

#### `int GetCurrentNegativeConditions(object oCreature)`
> Utility function for TalentCureCondition
> Returns an integer with bitwise flags set that represent the
> current negative conditions on the creature.
> To be used with GetHasNegativeCondition.

#### `int TalentCureCondition()`
> CURE DISEASE, POISON ETC
> Returns TRUE on successful use of such a talent, FALSE otherwise.

#### `int TalentDragonCombat(object oIntruder = OBJECT_INVALID)`
> DRAGON COMBAT
> Returns TRUE on successful use of such a talent, FALSE otherwise.

#### `int TalentBardSong()`
> BARD SONG
> Returns TRUE on successful use of such a talent, FALSE otherwise.

#### `int TalentAdvancedProtectSelf()`
> ADVANCED PROTECT SELF Talent 2.0
> This will use the class specific defensive spells first and
> leave the rest for the normal defensive AI
> Returns TRUE on successful use of such a talent, FALSE otherwise.

#### `int TalentSelfProtectionMantleOrGlobe()`
> Cast a spell mantle or globe of invulnerability protection on
> yourself.

#### `int TalentSpellAttack(object oIntruder)`
> Returns TRUE on successful use of such a talent, FALSE otherwise.

#### `talent StartProtectionLoop()`
> This function simply attempts to get the best protective
> talent that the caller has, the protective talents as
> follows:
> TALENT_CATEGORY_BENEFICIAL_PROTECTION_SELF
> TALENT_CATEGORY_BENEFICIAL_PROTECTION_SINGLE
> TALENT_CATEGORY_BENEFICIAL_PROTECTION_AREAEFFECT

#### `talent GetCreatureTalent(int nCategory, int nCRMax, int bRandom = FALSE, object oCreature = OBJECT_SELF)`
> Wrapper function so that I could add a variable to allow randomization
> to the AI.
> WARNING: This will make the AI cast spells badly if they have a bad
> spell selection (i.e., only turn randomization on if you know what you are doing
> nCRMax only applies if bRandom is FALSE
> oCreature is the creature checking to see if it has the talent

#### `int TrySpell(int nSpell, object oTarget = OBJECT_SELF, object oCaster = OBJECT_SELF)`
> Try a spell to produce a particular spell effect.
> This will only cast the spell if the target DOES NOT already have the
> given spell effect, and the caster possesses the spell.
> Returns TRUE on success, FALSE on failure.

#### `int TrySpellForEffect(int nSpell, int nEffect, object oTarget = OBJECT_SELF, object oCaster = OBJECT_SELF)`
> Try a spell corresponding to a particular effect.
> This will only cast the spell if the target DOES have the
> given effect, and the caster possesses the spell.
> Returns TRUE on success, FALSE on failure.

#### `int TryTalent(talent tUse, object oTarget = OBJECT_SELF, object oCaster = OBJECT_SELF)`
> Try a given talent.
> This will only cast spells and feats if the targets do not already
> have the effects of those feats, and will funnel all talents
> through bkTalentFilter for a final check.

#### `int TalentUseProtectionOnSelf()`
> PROTECT SELF

#### `int TalentUseProtectionOthers(object oDefault = OBJECT_INVALID)`
> PROTECT PARTY

#### `int TalentEnhanceOthers()`
> ENHANCE OTHERS

#### `int TalentUseEnhancementOnSelf()`
> ENHANCE SELF

#### `int genericDoHarmfulRangedAttack(talent tUse, object oTarget)`

#### `int genericAttemptHarmfulRanged(talent tUse, object oTarget)`

#### `int TalentMeleeAttacked(object oIntruder = OBJECT_INVALID)`

#### `int TalentRangedAttackers(object oIntruder = OBJECT_INVALID)`
> SPELL CASTER RANGED ATTACKED

#### `int TalentRangedEnemies(object oIntruder = OBJECT_INVALID)`
> SPELL CASTER WITH RANGED ENEMIES

#### `talent GetCreatureTalent(int nCategory, int nCRMax, int bRandom = FALSE, object oCreature = OBJECT_SELF)`
> Wrapper function so that I could add a variable to allow randomization
> to the AI.
> WARNING: This will make the AI cast spells badly if they have a bad
> spell selection (i.e., only turn randomization on if you know what you are doing
> nCRMax only applies if bRandom is FALSE
> oCreature is the creature checking to see if it has the talent

#### `int TalentSpellAttack(object oIntruder)`

#### `int TalentSummonAllies()`
> SUMMON ALLIES

#### `int TalentHealingSelf(int bForce = FALSE)`
> HEAL SELF WITH POTIONS AND SPELLS
> July 14 2003: If bForce=TRUE then force a heal

#### `int TalentHeal(int nForce = FALSE, object oTarget = OBJECT_SELF)`
> HEAL ALL ALLIES
> BK: Added an optional parameter for object.

#### `int WhirlwindGetNumberOfMeleeAttackers(float fDist = 5.0)`

#### `int GetOKToWhirl(object oCreature)`
> Returns true if the creature's variable
> set on it rolled against a d100
> says it is okay to whirlwind.
> Added this because it got silly to see creatures
> constantly whirlwinded

#### `int TalentMeleeAttack(object oIntruder = OBJECT_INVALID)`

#### `int TalentSneakAttack()`
> SNEAK ATTACK OTHERS

#### `int TalentFlee(object oIntruder = OBJECT_INVALID)`
> FLEE COMBAT AND HOSTILES

#### `int TalentUseTurning()`
> TURN UNDEAD

#### `int TalentPersistentAbilities()`
> ACTIVATE AURAS

#### `int TalentAdvancedBuff(float fDistance, int bInstant = TRUE)`
> FAST BUFF SELF
> Dec 19 2002: Added the instant parameter so this could be used for 'legal' spellcasting as well

#### `int TalentBuffSelf()`
> USE POTIONS

#### `int TalentSeeInvisible()`
> USE SPELLS TO DEFEAT INVISIBLE CREATURES
> THIS TALENT IS NOT USED

#### `int GetHasNegativeCondition(int nCondition, int nCurrentConditions)`
> Utility function for TalentCureCondition
> Checks to see if the creature has the given condition in the
> given condition value.
> To use, you must first calculate the nCurrentConditions value
> with GetCurrentNegativeConditions.
> The value of nCondition can be any of the COND_* constants
> declared in x0_i0_talent.

#### `int GetCurrentNegativeConditions(object oCreature)`
> Utility function for TalentCureCondition
> Returns an integer with bitwise flags set that represent the
> current negative conditions on the creature.
> To be used with GetHasNegativeCondition.

#### `int TalentCureCondition()`
> CURE DISEASE, POISON ETC

#### `int TalentDragonCombat(object oIntruder = OBJECT_INVALID)`
> DRAGON COMBAT
> February 2003: Cut the melee interaction (BK)

#### `int TalentBardSong()`
> BARD SONG
> July 15 2003: Improving so its more likely
> to work with non creature wizard designed creatures
> GZ: Capped bardsong at level 20 so we don't overflow into
> other feats
