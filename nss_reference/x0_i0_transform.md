# `x0_i0_transform.nss`

Source: `NSS/x0_/x0_i0_transform.nss`  
7 functions · 2 constants

## Constants

| Constant | Type | Value | Note |
|---|---|---|---|
| `sItemResrefSuffix` | string | `"_i"` |  |
| `sItemPickupSoundResref` | string | `"it_genericsmall"` |  |

## Functions

#### `void ActionCreateObject(string sResRef, location lLoc, float fDir = 361.0, int nObjType = OBJECT_TYPE_CREATURE)`
> Wrapper around CreateObject.
> This also optionally takes a direction to face.

#### `void TransformObject(object oOrigin, string sNewObjResRef, int nVisualEffect = VFX_NONE, int nNewObjType = OBJECT_TYPE_CREATURE)`
> Transform one object into another, using the specified visual effect
> (if any) at the original object's location.

#### `void TransformObjectToCreature(object oOrigin, string sCreature, int nVisualEffect = VFX_NONE)`
> See comments at the top of x0_i0_transform for usage advice. **
> Transform the given object into the creature of the specified type,
> using the specified visual effect (if any) at the object location.
> Some nice effects that work well:
> VFX_IMP_RAISE_DEAD, VFX_IMP_DISPEL, VFX_FNF_SUMMON_MONSTER_2
> Any VFX_IMP or VFX_FNF constant should work.

#### `void TransformObjectToPlaceable(object oOrigin, string sPlaceable, int nVisualEffect = VFX_NONE)`
> Transform the given object into the placeable of the specified type,
> using the specified visual effect (if any) at the object location.
> Works largely like TransformObjectToCreature, see comments for that.

#### `void TriggerObjectTransform(string sCreature, int nVisualEffect = VFX_NONE)`
> Trigger the nearest object with matching tag to convert.
> This should be called by the trigger object! It ASSUMES
> that GetEnteringObject() will work for OBJECT_SELF here.
> This destroys the trigger after it is successfully invoked
> by the PC.

#### `void TransformObjectToItem(object oOrigin, string sItem, object oInventory = OBJECT_INVALID)`
> This causes an object to be transformed into an item.
> This is useful for special placeables,
> where you want to be able to leave an "item" lying around
> on the ground that doesn't look like a bag but still can be
> picked up (without creating a new base item type).

#### `object GetNearestSeenEnemyForTransform(object oSource)`
> Private convenience function --
