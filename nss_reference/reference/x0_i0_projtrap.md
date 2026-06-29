# `x0_i0_projtrap.nss`

Source: `NSS/x0_/x0_i0_projtrap.nss`  
5 functions · 0 constants

## Functions

#### `object GetProjectileTrapOrigin(object oTarget, object oTrigger = OBJECT_SELF)`
> Get the origin for a projectile trap. This simply returns the nearest
> object to the target that has a tag matching the tag of the trigger.

#### `void TriggerProjectileTrap(int nSpell, object oTarget, int nCasterLevel = 20, object oOrigin = OBJECT_INVALID, object oTrigger = OBJECT_SELF, int nProjectilePath = PROJECTILE_PATH_TYPE_DEFAULT)`
> Causes oOrigin to fire a specified spell (SPELL_*) at oTarget,
> using the specified caster level (SEE *** COMMENTS).
> The specified level doesn't work yet.
> As a kludge, we are using the reflex save of the origin as
> the caster level. This kludge only works for a few spells
> at the moment. Other spells will fire typically at the
> highest caster level allowed for that spell.
> If the origin is invalid, the function will attempt to find the
> object nearest the target that has the same tag as the trigger.
> If no such object exists, we assume that the origin of the trap
> has been destroyed, and don't fire the trap.
> Only creatures, placeables, and items can be used as trap origins.
> Note that a few spells (notably the arrow/bolt/dart/shuriken) require
> PROJECTILE_PATH_TYPE_HOMING to work correctly.
> See the projectile trap trigger blueprints for usage.

#### `int GetIsTrapOriginValid(object oOrigin)`
> Small private function -- this just checks to see if the item
> is a valid origin object.

#### `object GetProjectileTrapOrigin(object oTarget, object oTrigger = OBJECT_SELF)`
> Get the origin for a projectile trap. This simply returns the nearest
> object to the target that has a tag matching the tag of the trigger.

#### `void TriggerProjectileTrap(int nSpell, object oTarget, int nCasterLevel = 20, object oOrigin = OBJECT_INVALID, object oTrigger = OBJECT_SELF, int nProjectilePath = PROJECTILE_PATH_TYPE_DEFAULT)`
> See detailed comments above
