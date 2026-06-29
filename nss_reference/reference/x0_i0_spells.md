# `x0_i0_spells.nss`

Source: `NSS/x0_/x0_i0_spells.nss`  
25 functions · 4 constants

## Constants

| Constant | Type | Value | Note |
|---|---|---|---|
| `SPELL_TARGET_ALLALLIES` | int | `1` |  |
| `SPELL_TARGET_STANDARDHOSTILE` | int | `2` |  |
| `SPELL_TARGET_SELECTIVEHOSTILE` | int | `3` |  |
| `SAVING_THROW_NONE` | int | `4` |  |

## Functions

#### `void DoTrapSpike(int nDamage)`
> Created By:
> Created On:
> apply effects of spike trap on entering object

#### `int MaximizeOrEmpower(int nDice, int nNumberOfDice, int nMeta, int nBonus = 0)`

#### `void DoGrenade(int nDirectDamage, int nSplashDamage, int vSmallHit, int vRingHit, int nDamageType, float fExplosionRadius, int nObjectFilter, int nRacialType = RACIAL_TYPE_ALL)`
> Created By:
> Created On:

#### `int GetCasterAbilityModifier(object oCaster)`
> Created By:
> Created On:

#### `int GetSizeModifier(object oCreature)`
> Created By:
> Created On:

#### `void DoDirgeEffect(object oTarget)`

#### `void DoCamoflage(object oTarget)`

#### `void DoSpikeGrowthEffect(object oTarget)`

#### `void spellsInflictTouchAttack(int nDamage, int nMaxExtraDamage, int nMaximized, int vfx_impactHurt, int vfx_impactHeal, int nSpellID)`

#### `void DoMissileStorm(int nD6Dice, int nCap, int nSpell, int nMIRV = VFX_IMP_MIRV, int nVIS = VFX_IMP_MAGBLUE, int nDAMAGETYPE = DAMAGE_TYPE_MAGICAL, int nONEHIT = FALSE, int nReflexSave = FALSE)`
> Created By: Brent
> Created On: July 31, 2002
> Modified March 14 2003: Removed the option to hurt chests/doors
> was potentially causing bugs when no creature targets available.

#### `void DoMagicFang(int nPower, int nDamagePower)`

#### `void DoCaltropEffect(object oTarget)`

#### `int CanCreatureBeDestroyed(object oTarget)`

#### `int spellsIsTarget(object oTarget, int nTargetType, object oSource)`

#### `void spellsGenericAreaOfEffect(object oCaster, location lTargetLoc, int nShape, float fRadiusSize, int nSpellID, effect eImpact, effect eLink, effect eVis, int nDurationType = DURATION_TYPE_INSTANT, float fDuration = 0.0, int nTargetType = SPELL_TARGET_ALLALLIES, int bHarmful = FALSE, int nRemoveEffectSpell = FALSE, int nRemoveEffect1 = 0, int nRemoveEffect2 = 0, int nRemoveEffect3 = 0, int bLineOfSight = FALSE, int nObjectFilter = OBJECT_TYPE_CREATURE, int bPersistentObject = FALSE, int bResistCheck = FALSE, int nSavingThrowType = SAVING_THROW_NONE, int nSavingThrowSubType = SAVING_THROW_TYPE_ALL)`
> generic area of effect constructor

#### `void spellApplyMindBlank(object oTarget, int nSpellId, float fDelay = 0.0)`
> Created By:
> Created On:

#### `void doAura(int nAlign, int nVis1, int nVis2, int nDamageType)`

#### `void spellsStinkingCloud(object oTarget = OBJECT_INVALID)`
> Does a stinking cloud. If oTarget is Invalid, then does area effect, otherwise
> just attempts on otarget

#### `void RemoveSpellEffects2(int nSpell_ID, object oCaster, object oTarget, int nSpell_ID2, int nSpell_ID3)`
> Created By:
> Created On:

#### `int spellsIsImmuneToPetrification(object oCreature)`
> returns true if the creature has flesh

#### `int spellsIsFlying(object oCreature)`
> Returns true or false depending on whether the creature is flying
> or not

#### `int spellsIsMindless(object oCreature)`
> returns true if oCreature does not have a mind

#### `void RemoveAnySpellEffects(int nSpell_ID, object oTarget)`
> Doesn't care who the caster was removes the effects of the spell nSpell_ID.
> will ignore the subtype as well...
> GZ: Removed the check that made it remove only one effect.

#### `void spellsDispelMagic(object oTarget, int nCasterLevel, effect eVis, effect eImpac, int bAll = TRUE, int bBreachSpells = FALSE)`
> Attempts a dispel on one target, with all safety checks put in.

#### `int GZGetHighestSpellcastingClassLevel(object oCreature)`
> GZ: Aug 27 2003
> Return the hightest spellcasting class of oCreature, used for dispel magic
> workaround
