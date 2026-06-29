# `x2_i0_spells.nss`

Source: `NSS/x2_/x2_i0_spells.nss`  
17 functions · 8 constants

## Constants

| Constant | Type | Value | Note |
|---|---|---|---|
| `X2_SPELL_AOEBEHAVIOR_FLEE` | int | `0` |  |
| `X2_SPELL_AOEBEHAVIOR_IGNORE` | int | `1` |  |
| `X2_SPELL_AOEBEHAVIOR_GUST` | int | `2` |  |
| `X2_SPELL_AOEBEHAVIOR_DISPEL_L` | int | `SPELL_LESSER_DISPEL` |  |
| `X2_SPELL_AOEBEHAVIOR_DISPEL_N` | int | `SPELL_DISPEL_MAGIC` |  |
| `X2_SPELL_AOEBEHAVIOR_DISPEL_G` | int | `SPELL_GREATER_DISPELLING` |  |
| `X2_SPELL_AOEBEHAVIOR_DISPEL_M` | int | `SPELL_MORDENKAINENS_DISJUNCTION` |  |
| `X2_SPELL_AOEBEHAVIOR_DISPEL_C` | int | `727` |  |

## Functions

#### `effect CreateBadTideEffectsLink()`
> Will pass back a linked effect for all of the bad tide of battle effects.

#### `effect CreateGoodTideEffectsLink()`
> Will pass back a linked effect for all of the good tide of battle effects.

#### `int GetSlashingWeapon(object oItem)`
> Passes in the slashing weapon type

#### `int GetMeleeWeapon(object oItem)`
> Passes in the melee weapon type

#### `int GetIsMagicalItem(object oItem)`
> Passes in if the item is magical or not.

#### `int GetIsMagicStatBonus(object oCaster)`
> Passes back the stat bonus of the characters magical stat, if any.

#### `int GetEpicSpellSaveDC(object oCaster)`
> Save DC against Epic Spells is the relevant ability score of the caster
> + 20. The hightest ability score of the casting relevants is 99.99% identical
> with the one that is used for casting, so we just take it.
> if used by a placeable, it is equal to the placeables WILL save field.

#### `void CheckAndApplyEpicRageFeats(int nRounds)`
> Hub function for the epic barbarian feats that upgrade rage. Call from
> the end of the barbarian rage spellscript

#### `void CheckAndApplyThunderingRage(int nRounds)`
> Checks the character for the thundering rage feat and will apply temporary massive critical
> to the worn weapons
> called by CheckAndApplyEpicRageFeats(

#### `void CheckAndApplyTerrifyingRage(int nRounds)`
> Checks and runs Rerrifying Rage feat
> called by CheckAndApplyEpicRageFeats(

#### `void DoMindBlast(int nDC, int nDuration, float fRange)`
> Do a mind blast
> nDC      - DC of the Save to resist
> nRounds  - Rounds the stun effect holds
> fRange   - Range of the EffectCone

#### `int GetIsRangedWeapon(object oItem)`
> AN, 2003
> Returns TRUE if oItem is a ranged weapon

#### `int DoCubeParalyze(object oTarget, object oSource, int nSaveDC = 16)`
> Gelatinous Cube Paralyze attack

#### `void EngulfAndDamage(object oTarget, object oSource)`
> GZ: Gel. Cube special abilities

#### `int GetBestAOEBehavior(int nSpellID)`
> GZ: Sept 2003
> Determines the optimal behavior against AoESpell nSpellId for a NPC
> use in OnSpellCastAt

#### `void GZRemoveSpellEffects(int nID, object oTarget, int bMagicalEffectsOnly = TRUE)`
> GZ: 2003-Oct-15
> Removes all effects from nID without paying attention to the caster as
> the spell can from only one caster anyway
> By default, it will only cancel magical effects

#### `int GZGetDelayedSpellEffectsExpired(int nSpell_ID, object oTarget, object oCaster)`
> GZ: 2003-Oct-15
> A different approach for timing these spells that has the positive side
> effects of making the spell dispellable as well.
> I am using the VFX applied by the spell to track the remaining duration
> instead of adding the remaining runtime on the stack
> This function returns FALSE if a delayed Spell effect from nSpell_ID has
> expired. See x2_s0_bigby4.nss for details
