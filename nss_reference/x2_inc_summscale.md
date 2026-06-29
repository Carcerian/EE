# `x2_inc_summscale.nss`

Source: `NSS/x2_/x2_inc_summscale.nss`  
12 functions · 0 constants

## Functions

#### `int SSMLevelUpCreature(object oCreature, int nLevelUpTo, int nClass = CLASS_TYPE_INVALID, int bReadySpells = TRUE)`
> Level up a creature to a specific level.
> See x2_inc_summscale for more information

#### `int SSMScaleEpicShadowLord(object oLord)`
> Scale up a summoned shadowlord into epic leves
> See x2_inc_summscale for more information

#### `int SSMScaleEpicFiendishServant(object oServant)`
> Scale up a summoned fiendish servant into epic leves
> See x2_inc_summscale for more information

#### `int SSMGetSummonFailedLevelUp(object oCreature)`

#### `void SSMSetSummonLevelUpOK(object oCreature)`

#### `void SSMSetSummonFailedLevelUp(object oCreature, int nLevel)`

#### `int SSMLevelUpCreature(object oCreature, int nLevelUpTo, int nClass = CLASS_TYPE_INVALID, int bReadySpells = TRUE)`

#### `int SSMScaleEpicShadowLord(object oLord)`
> Created By: Georg Zoeller
> Created On: 2003-07-25

#### `int SSMScaleEpicFiendishServant(object oServant)`
> Created By: Georg Zoeller
> Created On: 2003-07-25

#### `void SSMSetSummonFailedLevelUp(object oCreature, int nLevel)`
> SSMSetSummonFailedLevelUp()
> Georg, 2003-07-25
> Sets a flag on the summoned creature, indicating that it failed
> to level up to the level it was required to level up to.
> setting the level to a negative number will indicate that one
> of the special functions in this include will be called to level up the creature:
> - 1 : SSMScaleEpicShadowLord(object oLord)

#### `int SSMGetSummonFailedLevelUp(object oCreature)`

#### `void SSMSetSummonLevelUpOK(object oCreature)`
