# `x0_i0_corpses.nss`

Source: `NSS/x0_/x0_i0_corpses.nss`  
31 functions · 4 constants

## Constants

| Constant | Type | Value | Note |
|---|---|---|---|
| `sCorpseResRef` | string | `"x0_plc_corpse"` |  |
| `sBombResRef` | string | `"x0_plc_bomb"` |  |
| `CORPSE_DECAY_TIME` | float | `120.0f` |  |
| `CORPSE_EXPLODE_TIME` | float | `2.0f` |  |

## Functions

#### `void SetObjectIsDestroyable(object oVictim, int bCanDestroy, int bCanRaise = TRUE, int bCanSelect = FALSE)`
> Convenience function to set another object destroyable

#### `void LootInventorySlots(object oVictim, object oCorpse, int bDecay = TRUE, int bDropWielded = TRUE)`
> Loot all the droppable items from the inventory slots of the
> victim into the inventory of the corpse object.
> If bDropWielded is TRUE, the items the victim is wielding in
> its right and left hands will be dropped to either side
> of it, otherwise they will simply be placed into inventory.

#### `void LootInventory(object oVictim, object oCorpse)`
> Strip everything droppable in the regular inventory.
> Use LootInventorySlots to strip equipped items.

#### `void KillAndReplaceLootable(object oVictim, int bDecay = TRUE, int bDropWielded = TRUE)`
> Die young, leave a lootable corpse. (ha ha ha... okay, been working too long)
> Despite the name, can be used in an OnDeath script;
> it won't kill the victim twice.
> If bDecay is TRUE, the corpse will decay to a bag after a brief delay.
> If bDropWielded is TRUE, the corpse will drop its right/left hand items
> to either side (making the body more decorative, but the items harder
> to see).

#### `void KillAndReplaceDecay(object oVictim)`
> Kill and leave a decorative corpse that will decay
> after a short while.
> Despite the name, can be used in an OnDeath script;
> it won't kill the victim twice.

#### `void KillAndReplaceRaiseable(object oVictim)`
> Kill and leave a raiseable & selectable corpse
> Despite the name, can be used in an OnDeath script;
> it won't kill the victim twice.

#### `void KillAndReplaceSelectable(object oVictim)`
> Kill and leave a corpse with the corpse's name
> Despite the name, can be used in an OnDeath script;
> it won't kill the victim twice.

#### `void KillAndReplaceDecorative(object oVictim)`
> Kill and leave a purely decorative corpse (no name,
> not raiseable).
> Despite the name, can be used in an OnDeath script;
> it won't kill the victim twice.

#### `void KillAndExplode(object oVictim, int nSpell = SPELL_FIREBALL)`
> Kill and leave an exploding corpse
> Despite the name, can be used in an OnDeath script;
> it won't kill the victim twice.
> Any spell can be used.

#### `void ExplodeObject(object oOrigin, int nSpell = SPELL_FIREBALL)`
> Blow up an object with the given spell (actually
> casts the spell, injuring those around the object)

#### `void TriggerExplodeObject(int nSpell = SPELL_FIREBALL)`
> Blow up the nearest object with a matching tag with the specified
> spell.
> This should be called by the trigger object! It ASSUMES
> that GetEnteringObject() will work for OBJECT_SELF here.
> This destroys the trigger after it is successfully invoked
> by the PC.

#### `void RaiseCorpse(object oVictim, int nVisualEffect = VFX_IMP_RAISE_DEAD, int bDestroyable = TRUE)`
> Raise a given corpse from the dead with given visual effect.
> Unless bDestroyable is set to FALSE, the newly-raised corpse will
> be changed so it will be destroyed on its next death.

#### `object GetNearestCorpse(object oSource = OBJECT_SELF)`
> Return the nearest corpse object

#### `void TriggerRaiseCorpse(int nVisualEffect = VFX_IMP_RAISE_DEAD)`
> Raise the nearest corpse from the dead.
> This should be called by the trigger object! It ASSUMES
> that GetEnteringObject() will work for OBJECT_SELF here.

#### `void DoActualKilling(object oVictim)`
> Actually kill off a victim, regardless of plot flag.

#### `int GetIsVictimDressed(object oVictim)`
> This function is used to determine if the victim is the type
> of creature that "wears" its clothing, so we don't strip them
> naked.

#### `void CopyItem2(object oSource, object oInventory)`
> convenience function for copying objects properly

#### `void SetObjectIsDestroyable(object oVictim, int bCanDestroy, int bCanRaise = TRUE, int bCanSelect = FALSE)`
> Convenience function to set another object destroyable

#### `void LootInventorySlots(object oVictim, object oCorpse, int bDecay = TRUE, int bDropWielded = TRUE)`
> If bDropWielded is TRUE, the items the victim is wielding in
> its right and left hands will be dropped to either side
> of it, otherwise they will simply be placed into inventory.

#### `void LootInventory(object oVictim, object oCorpse)`
> Strip everything droppable in the regular inventory, too.

#### `void KillAndReplaceLootable(object oVictim, int bDecay = TRUE, int bDropWielded = TRUE)`
> If bDecay is TRUE, the corpse will decay to a bag after a brief delay.
> If bDropWielded is TRUE, the corpse will drop its right/left hand items
> to either side (making the body more decorative, but the items harder
> to see).

#### `void KillAndReplaceDecay(object oVictim)`
> Kill and leave a decorative corpse that will decay
> after a short while.

#### `void KillAndReplaceRaiseable(object oVictim)`
> Kill and leave a raiseable & selectable corpse

#### `void KillAndReplaceSelectable(object oVictim)`
> Kill and leave a corpse with the corpse's name

#### `void KillAndReplaceDecorative(object oVictim)`
> Kill and leave a purely decorative corpse (no name,
> not raiseable).

#### `void KillAndExplode(object oVictim, int nSpell = SPELL_FIREBALL)`
> Kill and leave an exploding corpse
> Despite the name, can be used in an OnDeath script;
> it won't kill the victim twice.
> Any spell can be used.

#### `void ExplodeObject(object oOrigin, int nSpell = SPELL_FIREBALL)`
> Blow up an object with the given spell (actually
> casts the spell, injuring those around the object)

#### `void TriggerExplodeObject(int nSpell = SPELL_FIREBALL)`
> Blow up the nearest object with a matching tag,
> using the specified spell.

#### `void RaiseCorpse(object oVictim, int nVisualEffect = VFX_IMP_RAISE_DEAD, int bDestroyable = TRUE)`
> Raise a given corpse from the dead with given visual effect.
> Unless bDestroyable is set to FALSE, the newly-raised corpse will
> be changed so it will be destroyed on its next death.

#### `object GetNearestCorpse(object oSource = OBJECT_SELF)`
> Return the nearest corpse object

#### `void TriggerRaiseCorpse(int nVisualEffect = VFX_IMP_RAISE_DEAD)`
> Raise the nearest corpse from the dead.
> This should be called by the trigger object! It ASSUMES
> that GetEnteringObject() will work for OBJECT_SELF here.
