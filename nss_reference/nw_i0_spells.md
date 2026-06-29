# `nw_i0_spells.nss`

Source: `NSS/nw_/nw_i0_spells.nss`  
34 functions · 1 constants

## Constants

| Constant | Type | Value | Note |
|---|---|---|---|
| `NW_I0_SPELLS_MAX_BREACH` | int | `33` |  |

## Functions

#### `void TrapDoElectricalDamage(int ngDamageMaster, int nSaveDC, int nSecondary)`
> Function for doing electrical traps

#### `int MyResistSpell(object oCaster, object oTarget, float fDelay = 0.0)`
> Used to route the resist magic checks into this function to check for spell countering by SR, Globes or Mantles.
> Return value if oCaster or oTarget is an invalid object: FALSE
> Return value if spell cast is not a player spell: - 1
> Return value if spell resisted: 1
> Return value if spell resisted via magic immunity: 2
> Return value if spell resisted via spell absorption: 3

#### `int MySavingThrow(int nSavingThrow, object oTarget, int nDC, int nSaveType = SAVING_THROW_TYPE_NONE, object oSaveVersus = OBJECT_SELF, float fDelay = 0.0)`
> Used to route the saving throws through this function to check for spell countering by a saving throw.
> Returns: 0 if the saving throw roll failed
> Returns: 1 if the saving throw roll succeeded
> Returns: 2 if the target was immune to the save type specified
> Note: If used within an Area of Effect Object Script (On Enter, OnExit, OnHeartbeat), you MUST pass
> GetAreaOfEffectCreator() into oSaveVersus!!    \

#### `effect CreateProtectionFromAlignmentLink(int nAlignment, int nPower = 1)`
> Will pass back a linked effect for all the protection from alignment spells.  The power represents the multiplier of strength.
> That is instead of +3 AC and +2 Saves a  power of 2 will yield +6 AC and +4 Saves.

#### `effect CreateDoomEffectsLink()`
> Will pass back a linked effect for all of the doom effects.

#### `void RemoveSpellEffects(int nSpell_ID, object oCaster, object oTarget)`
> Searchs through a persons effects and removes those from a particular spell by a particular caster.

#### `void RemoveSpecificEffect(int nEffectTypeID, object oTarget)`
> Searchs through a persons effects and removes all those of a specific type.

#### `float GetSpellEffectDelay(location SpellTargetLocation, object oTarget)`
> Returns the time in seconds that the effect should be delayed before application.

#### `float GetRandomDelay(float fMinimumTime = 0.4, float MaximumTime = 1.1)`
> This allows the application of a random delay to effects based on time parameters passed in.  Min default = 0.4, Max default = 1.1

#### `int GetScaledDuration(int nActualDuration, object oTarget)`
> Get Difficulty Duration

#### `effect GetScaledEffect(effect eStandard, object oTarget)`
> Get Scaled Effect

#### `int RemoveProtections(int nSpell_ID, object oTarget, int nCount)`
> Remove all spell protections of a specific type

#### `int GetSpellBreachProtection(int nLastChecked)`
> Performs a spell breach up to nTotal spells are removed and nSR spell
> resistance is lowered.

#### `void spellsCure(int nDamage, int nMaxExtraDamage, int nMaximized, int vfx_impactHurt, int vfx_impactHeal, int nSpellID)`

#### `void DoSpellBreach(object oTarget, int nTotal, int nSR, int nSpellId = -1)`
> Created By: Brent
> Created On: September 2002
> Modified  : Georg, Oct 31, 2003

#### `int GetDragonFearDC(int nAge)`
> Created By: Brent
> Created On: Sep 13, 2002

#### `int CalcNumberOfAttacks()`
> Kovi function: calculates the appropriate base number of attacks
> for spells that increase this (tensers, divine power)

#### `void RemoveTempHitPoints()`
> GZ: gets rids of temporary hit points so that they will not stack

#### `void RemoveEffectsFromSpell(object oTarget, int SpellID)`
> Kovi. removes any effects from this type of spell
> i.e., used in Mage Armor to remove any previous
> mage armors

#### `int MyResistSpell(object oCaster, object oTarget, float fDelay = 0.0)`

#### `int MySavingThrow(int nSavingThrow, object oTarget, int nDC, int nSaveType = SAVING_THROW_TYPE_NONE, object oSaveVersus = OBJECT_SELF, float fDelay = 0.0)`

#### `effect CreateProtectionFromAlignmentLink(int nAlignment, int nPower = 1)`

#### `effect CreateDoomEffectsLink()`

#### `void RemoveSpellEffects(int nSpell_ID, object oCaster, object oTarget)`

#### `void RemoveSpecificEffect(int nEffectTypeID, object oTarget)`

#### `float GetSpellEffectDelay(location SpellTargetLocation, object oTarget)`

#### `float GetRandomDelay(float fMinimumTime = 0.4, float MaximumTime = 1.1)`

#### `int GetScaledDuration(int nActualDuration, object oTarget)`

#### `effect GetScaledEffect(effect eStandard, object oTarget)`

#### `int RemoveProtections(int nSpell_ID, object oTarget, int nCount)`

#### `int GetSpellBreachProtection(int nLastChecked)`
> Returns the nLastChecked-nth highest spell on the creature for use in
> the spell breach routines
> Please modify the constatn NW_I0_SPELLS_MAX_BREACH at the top of this file
> if you change the number of spells.

#### `void AssignAOEDebugString(string sString)`

#### `void PlayDragonBattleCry()`

#### `void TrapDoElectricalDamage(int ngDamageMaster, int nSaveDC, int nSecondary)`
