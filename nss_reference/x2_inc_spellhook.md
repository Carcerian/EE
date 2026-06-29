# `x2_inc_spellhook.nss`

Source: `NSS/x2_/x2_inc_spellhook.nss`  
9 functions · 1 constants

## Constants

| Constant | Type | Value | Note |
|---|---|---|---|
| `X2_EVENT_CONCENTRATION_BROKEN` | int | `12400` |  |

## Functions

#### `int X2UseMagicDeviceCheck()`
> Use Magic Device Check.
> Returns TRUE if the Spell is allowed to be cast, either because the
> character is allowed to cast it or he has won the required UMD check
> Only active on spell scroll

#### `int X2PreSpellCastCode()`
> This function holds all functions that are supposed to run before the actual
> spellscript gets run. If this functions returns FALSE, the spell is aborted
> and the spellscript will not run

#### `int X2CastOnItemWasAllowed(object oItem)`
> check if the spell is prohibited from being cast on items
> returns FALSE if the spell was cast on an item but is prevented
> from being cast there by its corresponding entry in des_crft_spells
> oItem - pass GetSpellTargetObject in here

#### `int X2GetSpellCastOnSequencerItem(object oItem)`
> Sequencer Item Property Handling
> Returns TRUE (and charges the sequencer item) if the spell
> ... was cast on an item AND
> ... the item has the sequencer property
> ... the spell was non hostile
> ... the spell was not cast from an item
> in any other case, FALSE is returned an the normal spellscript will be run
> oItem - pass GetSpellTargetObject in here

#### `int X2RunUserDefinedSpellScript()`
> Execute a user overridden spell script.

#### `void X2BreakConcentrationSpells()`
> This is our little concentration system for black blade of disaster
> if the mage tries to cast any kind of spell, the blade is signaled an event to die

#### `int X2GetBreakConcentrationCondition(object oPlayer)`
> being hit by any kind of negative effect affecting the caster's ability to concentrate
> will cause a break condition for concentration spells

#### `void X2DoBreakConcentrationCheck()`

#### `int X3ShapeShiftSpell(object oTarget)`
> This function will return TRUE if the spell that is cast is a shape shifting
> spell.
