# `x0_i0_equip.nss`

Source: `NSS/x0_/x0_i0_equip.nss`  
9 functions · 0 constants

## Functions

#### `int WiseToDualWield(object oUser)`
> checks to see if oUser has ambidexteriy and two weapon fighting

#### `void EquipAppropriateWeapons(object oTarget)`
> Equip the weapon appropriate to enemy and position.
> This is now just a wrapper around bkEquipAppropriateWeapons.

#### `int IsOutOfAmmo(int bIAmAHenc)`
> returns true if out of ammo of currently equipped weapons

#### `void bkEquipMelee(object oTarget = OBJECT_INVALID, int nClearActions = TRUE)`
> Equip melee weapon(s) and a shield.

#### `void bkEquipRanged(object oTarget = OBJECT_INVALID, int bIAmAHenc = FALSE, int bForceEquip = FALSE)`
> New function February 28 2003. Need a wrapper for ranged
> so I have quick access to exiting from it for OC henchmen
> equipping

#### `void bkEquipAppropriateWeapons(object oTarget, int nPrefersRanged = FALSE, int nClearActions = TRUE)`
> Equip the appropriate weapons to face the target.

#### `void WrapperActionAttack(object oTarget)`
> this is just a wrapper around ActionAttack
> to make sure the creature equips weapons

#### `void StoreLastRanged()`
> stores the last Ranged weapons used for when the
> henchmen switches from Ranged to melee in XP1

#### `int GetIsWeaponLarge(object oItem)`
