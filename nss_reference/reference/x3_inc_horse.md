# `x3_inc_horse.nss`

Source: `NSS/x3_/x3_inc_horse.nss`  
112 functions · 43 constants

## Constants

| Constant | Type | Value | Note |
|---|---|---|---|
| `X3_HORSE_DATABASE` | string | `"X3HORSE"` |  |
| `HORSE_APPEARANCE_OFFSET` | int | `496` |  |
| `HORSE_TAIL_OFFSET` | int | `15` |  |
| `HORSE_NUMBER_OF_HORSES` | int | `65` |  |
| `HORSE_PALADIN_PREFIX` | string | `"x3_palhrs"` |  |
| `HORSE_NULL_RACE_DWARF` | int | `562` |  |
| `HORSE_NULL_RACE_ELF` | int | `563` |  |
| `HORSE_NULL_RACE_HALFLING` | int | `565` |  |
| `HORSE_NULL_RACE_HUMAN` | int | `568` |  |
| `HORSE_NULL_RACE_HALFELF` | int | `566` |  |
| `HORSE_NULL_RACE_HALFORC` | int | `567` |  |
| `HORSE_NULL_RACE_GNOME` | int | `564` |  |
| `HORSE_RACE_MOUNTED_DWARFM` | int | `483` |  |
| `HORSE_RACE_MOUNTED_DWARFF` | int | `482` |  |
| `HORSE_RACE_MOUNTED_ELFM` | int | `485` |  |
| `HORSE_RACE_MOUNTED_ELFF` | int | `484` |  |
| `HORSE_RACE_MOUNTED_GNOMEM` | int | `487` |  |
| `HORSE_RACE_MOUNTED_GNOMEF` | int | `486` |  |
| `HORSE_RACE_MOUNTED_HALFLINGM` | int | `489` |  |
| `HORSE_RACE_MOUNTED_HALFLINGF` | int | `488` |  |
| `HORSE_RACE_MOUNTED_HALFELFM` | int | `491` |  |
| `HORSE_RACE_MOUNTED_HALFELFF` | int | `490` |  |
| `HORSE_RACE_MOUNTED_HALFORCM` | int | `493` |  |
| `HORSE_RACE_MOUNTED_HALFORCF` | int | `492` |  |
| `HORSE_RACE_MOUNTED_HUMANM` | int | `495` |  |
| `HORSE_RACE_MOUNTED_HUMANF` | int | `494` |  |
| `HORSE_PHENOTYPE_MOUNTED_N` | int | `3` |  |
| `HORSE_PHENOTYPE_MOUNTED_L` | int | `5` |  |
| `HORSE_PHENOTYPE_JOUSTING_N` | int | `6` |  |
| `HORSE_PHENOTYPE_JOUSTING_L` | int | `8` |  |
| `HORSE_ANIMATION_MOUNT` | int | `41` |  |
| `HORSE_ANIMATION_DISMOUNT` | int | `42` |  |
| `HORSE_ANIMATION_LOOPING_JOUST_VIOLENT_FALL` | int | `ANIMATION_LOOPING_CUSTOM3` |  |
| `HORSE_ANIMATION_LOOPING_JOUST_GLANCE` | int | `ANIMATION_LOOPING_CUSTOM4` |  |
| `HORSE_ANIMATION_LOOPING_JOUST_FALL` | int | `ANIMATION_LOOPING_CUSTOM5` |  |
| `HORSE_ANIMATION_LOOPING_JOUST_STAB` | int | `ANIMATION_LOOPING_CUSTOM10` |  |
| `HORSE_ANIMATION_LOOPING_JOUST_HELMOFF` | int | `ANIMATION_LOOPING_CUSTOM4` |  |
| `HORSE_FOOTSTEP_SOUND` | int | `17` |  |
| `HORSE_MOUNT_DURATION` | float | `2.0f` |  |
| `HORSE_DISMOUNT_DURATION` | float | `3.0f` |  |
| `IP_CONST_HORSE_MENU` | int | `40` |  |
| `HORSE_DEFAULT_SPEED_INCREASE` | int | `99` |  |
| `X3_ACTION_DELAY` | float | `0.8f` |  |

## Functions

#### `void HorseMount(object oHorse, int bAnimate = TRUE, int bInstant = FALSE, int nState = 0)`
> FILE: x3_inc_horse       FUNCTION: HorseMount()
> This function will cause the calling object to attempt to mount oHorse.
> If bAnimate is set to TRUE this will cause the calling object and oHorse
> to be involved in the complete animating process.  If you bAnimate is false
> and bInstant is false the caller will still walk to the horse before mounting.
> If bAnimate is false and bInstant is TRUE then the script will immediately
> mount oHorse without any moving (this is the quickest method if needed for
> situations like cutscenes).  nState is a variable used by the function itself
> and need not be adjusted when this function is called.

#### `object HorseDismount(int bAnimate = TRUE, int bSetOwner = TRUE)`
> FILE: x3_inc_horse       FUNCTION: HorseDismount()
> This function will cause the calling object to dismount if it is mounted. If
> bAnimate is TRUE then it will animate the dismount.   If bOwner is set to
> TRUE then it will set the object that dismounted as the owner.  This function
> will return the object that is the dismounted horse.

#### `void HorseSetOwner(object oHorse, object oOwner, int bAssign = FALSE)`
> FILE: x3_inc_horse       FUNCTION: HorseSetOwner()
> This function will set oOwner as the owner of oHorse. If bAssign is set to
> TRUE it will also set this horse to be oOwners assigned mount.   This is not
> done by default so more than one mount can be assigned to a single target if
> need be.

#### `void HorseRemoveOwner(object oHorse)`
> FILE: x3_inc_horse       FUNCTION: HorseRemoveOwner()
> This function will remove the owner from oHorse.  This will not work on
> Paladin mounts.

#### `int HorseGetCanBeMounted(object oTarget, object oRider = OBJECT_INVALID, int bAssignMount = FALSE)`
> FILE: x3_inc_horse       FUNCTION: HorseGetCanBeMounted()
> This function will return TRUE if oTarget can be mounted.  If oRider is
> specified it will also make sure that oTarget can be ridden by oRider.
> The bAssignMount field should be set to TRUE if the call of this function
> should ignore whether someone can mount a horse in the area or not.

#### `object HorseSummonPaladinMount(int bPHBDuration = FALSE)`
> FILE: x3_inc_horse       FUNCTION: HorseSummonPaladinMount()
> This function can be used to cause the calling object to summon the paladin
> mount.   If bPHBDuration is set to TRUE then the mount will use the Players
> Handbook 3.0 edition rules for the duration that the mount will stay around.

#### `void HorseUnsummonPaladinMount()`
> FILE: x3_inc_horse       FUNCTION: HorseUnsummonPaladinMount()
> This function can be used to cause the calling object to unsummon its paladin
> mount.

#### `int HorseGetIsMounted(object oTarget)`
> FILE: x3_inc_horse       FUNCTION: HorseGetIsMounted()
> This function will return TRUE if oTarget is mounted.

#### `object HorseCreateHorse(string sResRef, location lLoc, object oOwner = OBJECT_INVALID, string sTag = "", int nAppearance = -1, int nTail = -1, int nFootstep = -1, string sScript = "")`
> FILE: x3_inc_horse       FUNCTION: HorseCreateHorse()
> This function will create a horse based on the blueprint sResRef at location
> lLoc and will set the owner of the horse to oOwner.  If sTag is set to
> something other than "" it will set the horse to that tag.  If nAppearance,
> nTail, and nFootstep are set to something other than -1 then it will set the
> horse to that appearance, tail, or footstep.  The function will return the
> horse that is spawned.   This function is setup the way it is so, that you
> could potentially use a single blueprint to store multiple appearance horses.
> sScript is a specific script that should be executed on the horse after it is
> spawned.  This is again supplied to further support multiple horses with a
> single blueprint.

#### `object HorseGetOwner(object oHorse)`
> FILE: x3_inc_horse       FUNCTION: HorseGetOwner()
> This function will return an object pointer to whom the owner of oHorse is
> if there is a valid horse.   If there is no owner it will return
> OBJECT_INVALID.

#### `void HorseSetPhenotype(object oRider, int bJoust = FALSE)`
> FILE: x3_inc_horse       FUNCTION: HorseSetPhenotype()
> This function will set oRider to the correct mounted phenotype for riding
> a horse.  If bJoust is set to TRUE it will set oRider to the mounted jousting
> phenotype.  This is a special phenotype with differing animation sets and
> designed to hold the lance in a very specific way.

#### `void HorseInstantMount(object oRider, int nTail, int bJoust = FALSE, string sResRef = "")`
> FILE: x3_inc_horse       FUNCTION: HorseInstantMount()
> This function is primarily supplied for cutscenes and other instances where
> you simply need oRider to be switched to mounted mode as quickly as possible
> without preserving any variables or anything.  However, you can store a
> resref for the horse to dismount by setting sResRef.  If bJoust is set to
> TRUE then it will use the Joust Phenotypes.
> WARNING: This does not care whether someone meets the criteria to mount,
> or even if they are already mounted.   It will simply set them to the
> proper appearance and mode.   The ResRef is provided only in case someone
> uses HorseDismount() instead of using HorseInstantDismount() with this
> rider.   It is recommended this function only be used in conjunction with
> HorseInstantDismount().

#### `void HorseInstantDismount(object oRider)`
> FILE: x3_inc_horse       FUNCTION: HorseInstantDismount()
> This function is used to rapidly dismount oRider and does not produce a horse
> object.   It's intended usage is with cutscenes or other instances where
> having oRider dismounted as quickly as possible are required.  This will not
> produce horse/mount as it is primarily intende for cutscene work and not
> intended to replace the HorseDismount() function in other cases.
> WARNING: This does not protect Saddlebags so, it is recommended this only
> be used in conjunction with HorseInstantMount.   If you need to protect
> saddlebag contents use HorseDismount().

#### `int HorseGetMountTail(object oHorse)`
> FILE: x3_inc_horse       FUNCTION: HorseGetMountTail()
> This function will return the tail that should be used with the specified
> horse.

#### `string HorseGetMountFailureMessage(object oHorse, object oRider = OBJECT_INVALID)`
> FILE: x3_inc_horse       FUNCTION: HorseGetMountFailureMessage()
> This is a companion function to HorseGetCanBeMounted.  If you need a text
> message that explains why the horse cannot be mounted.

#### `void HorseAddHorseMenu(object oPC)`
> FILE: x3_inc_horse       FUNCTION: HorseAddHorseMenu()
> This function will add horse menus to the respective PC.  This is only
> needed for PCs that were not created new using patch 1.69.

#### `object HorseGetPaladinMount(object oRider)`
> FILE: x3_inc_horse       FUNCTION: HorseGetPaladinMount()
> If this rider has a paladin mount then it will be returned as the object.
> If the rider is currently riding their paladin mount then it will return
> oRider as the object.   If no paladin mount currently exists for oRider it
> will return OBJECT_INVALID.

#### `int HorseGetIsAMount(object oTarget)`
> FILE: x3_inc_horse       FUNCTION: HorseGetIsAMount()
> This will return TRUE if oTarget is a mountable creature.

#### `int HorseGetIsDisabled(object oCreature = OBJECT_SELF)`
> FILE: x3_inc_horse       FUNCTION: HorseGetIsDisabled()
> This function detects if oCreature is in a disabled state. Can be used to
> detect disabling effects such as death, fear, confusion, sleep, paralysis,
> petrify, stun, entangle and knockdown (also applied in a non-hostile way,
> where oCreature doesn't enter a combat state)

#### `void HorseReloadFromDatabase(object oPC, string sDatabase)`
> FILE: x3_inc_horse       FUNCTION: HorseReloadFromDatabase()
> This function is provided for use with an OnClientEnter script when you
> are using a persistent world type environment and need the PC's mounted
> state reloaded.  This will also make sure that henchmen for the PC are also
> restored as they were.

#### `void HorseSaveToDatabase(object oPC, string sDatabase)`
> FILE: x3_inc_horse       FUNCTION: HorseSaveToDatabase()
> This will save all of the current status for the PC and the PCs henchmen.

#### `void HorseStoreInventory(object oCreature, object oRider = OBJECT_INVALID)`
> FILE: x3_inc_horse       FUNCTION: HorseStoreInventory()
> This function is used to store inventory of the horse for later recovery.
> See x3_inc_horse for complete details.

#### `void HorseRestoreInventory(object oCreature, int bDrop = FALSE)`
> FILE: x3_inc_horse       FUNCTION: HorseRestoreInventory()
> This function is used to return stored inventory back onto the horse
> See x3_inc_horse for complete details. If bDrop is set to TRUE then it
> will drop the contents where the horse is rather than putting them on the
> horse.  bDrop was primarily intended for cases where a mounted PC dies.

#### `void HorseChangeToDefault(object oCreature)`
> FILE: x3_inc_horse       FUNCTION: HorseChangeToDefault()
> This function will set oCreature to the default racial appearance and is
> useful for reversing any situations where a creature or PC is stuck in some
> variation of a mounted appearance.   This will also clear ANY information
> stored on the creature relating to mounting. NOTE: If the target had a
> tail when not mounted this function will not restore that.

#### `void HorseIfNotDefaultAppearanceChange(object oCreature)`
> FILE: x3_inc_horse       FUNCTION: HorseIfNotDefaultAppearanceChange()
> This funtion will check the appearance of oCreature,   If it is not set to
> the default racial appearance (see racialtypes.2da) then it will call the
> HorseChangeToDefault() function.

#### `object HorseGetMyHorse(object oRider)`
> FILE: x3_inc_horse       FUNCTION: HorseGetMyHorse()
> When oRider is dismounted, this function returns the horse currently assigned
> to oRider (OBJECT_INVALID if there is none). In certain script hooks
> (pre-mount, post-mount and post-dismount), the function returns the horse
> that is currently being mounted / dismounted. It should not be used when the
> rider is mounted, or in a pre-dismount script hook.

#### `int HorseGetHasAHorse(object oRider)`
> FILE: x3_inc_horse       FUNCTION: HorseGetHasAHorse()
> This function will return TRUE if oRider has a mount or horse.

#### `object HorseGetHorse(object oRider, int nN = 1)`
> FILE: x3_inc_horse       FUNCTION: HorseGetHorse()
> This function will return the nNth horse that is owned by oRider.

#### `void HorseRestoreHenchmenLocations(object oPC)`
> FILE: x3_inc_horse       FUNCTION: HorseRestoreHenchmenLocations()
> This function will check the module variable X3_RESTORE_HENCHMEN_LOCATIONS
> which when set to TRUE on the module will cause this function to jump any
> npc henchmen to the PC and will also make sure their henchmen also jump.
> This function is provided so, that there exists a function which will remain
> true to whether henchmen are mounted in no mount areas and whether mounts are
> prevented from entering no mount areas.   This is not the perfect function
> but, it will address some of the issues with the engine not restoring the
> locations of henchmen belonging to henchmen on a module reload.   This will
> actually NOT jump henchmen to the PC.   It's primary purpose is to make sure
> that henchmen belonging to the henchman are jumped to the proper location.
> It is assumed that the henchman that is their master will already be at the
> proper location due to a reload or due to a respawn from some special script
> for the server.

#### `void HorseHitchHorses(object oHitch, object oClicker, location lPreJump)`
> FILE: x3_inc_horse        FUNCTION: HorseHitchHorses()
> This function is designed to be used in conjunction with a transition script.
> oHitch is an object to hitch horses/mounts near.   If it is OBJECT_INVALID
> then a specific destination to hitch will not be used.  oClicker is who
> clicked the area transistion.  lPreJump is a pre-transition location which
> is used to determine where the horses should stay near (actually walk a
> small distance away) if they do not transition.

#### `void HorseForceJump(object oJumper, object oDestination, float fRange = 2.0, int nTimeOut = 10)`
> FILE: x3_inc_horse       FUNCTION: HorseForceJump()
> This is used to make sure oJumper makes it to withing fRange of oDestination.
> The nTimeOut is used to set a maximum number of attempts that will be made.

#### `void HorseMoveAssociates(object oMaster)`
> FILE: x3_inc_horse       FUNCTION: HorseMoveAssociates()
> This function is intended to be used after a transition has been made and
> oMaster has moved onto the target destination.   This function will cause
> any associates that also transitioned to move away from oMaster a small
> amount to make sure they do not block movement for oMaster.   This can be
> particularly important when you consider horses have a bit more personal
> space requirements than the traditional associate.

#### `void HorsePreloadAnimations(object oPC)`
> FILE: x3_inc_horse       FUNCTION: HorsePreloadAnimations()
> The mount and dismount animations are rather complex and by default the
> aurora engine does not always preload these animations.   This function was
> created to temporarily set the tail and appearance of a PC to that of one of
> the horse models that will thus, force preloading of the animations.   After
> that is done the animations should played properly.   This is a good function
> to call in the OnEnter script of the module or similar location.

#### `int HORSE_SupportGetMountedAppearance(object oRider)`

#### `string HORSE_SupportRaceRestrictString(object oRider)`

#### `string HORSE_SupportMountResRef(object oRider)`

#### `int HORSE_SupportMountAppearance(object oRider)`

#### `int HORSE_SupportMountTail(object oRider)`

#### `int HORSE_SupportMountFootstep(object oRider)`

#### `string HORSE_SupportMountTag(object oRider)`

#### `string HORSE_SupportMountScript(object oRider)`

#### `int HORSE_SupportRiderAppearance(object oRider)`

#### `int HORSE_SupportRiderPhenotype(object oRider)`

#### `void HORSE_SupportCleanVariables(object oTarget)`

#### `void HORSE_SupportMountCleanVariables(object oRider)`

#### `location HORSE_SupportGetMountLocation(object oCreature, object oRider, float fDirection = 90.0)`

#### `int HORSE_SupportNullAppearance(object oHorse, object oRider)`

#### `int Horse_SupportRaceAppearance(int nAppearance)`

#### `void HORSE_SupportIncreaseSpeed(object oRider, object oHorse)`

#### `void HORSE_SupportOriginalSpeed(object oRider)`

#### `void HORSE_SupportAdjustMountedArcheryPenalty(object oRider)`

#### `void HORSE_SupportApplyMountedSkillDecreases(object oRider)`

#### `void HORSE_SupportRemoveMountedSkillDecreases(object oRider)`

#### `void HORSE_SupportResetUnmountedAppearance(object oRider)`

#### `int HORSE_SupportAbsoluteMinute()`

#### `void HORSE_SupportMonitorPaladinUnsummon(object oPaladin)`

#### `void HORSE_SupportApplyACBonus(object oRider, object oHorse)`

#### `void HORSE_SupportRemoveACBonus(object oRider)`

#### `void HORSE_SupportApplyHPBonus(object oRider, object oHorse)`

#### `void HORSE_SupportRemoveHPBonus(object oRider)`

#### `void HORSE_SupportHandleDamage(object oRider, object oHorse)`

#### `void KillTheHorse(object oHorse, int bStart = TRUE)`

#### `void HORSE_SupportTransferInventory(object oFrom, object oTo, location lLoc, int bDestroyFrom = FALSE, int bFirst = TRUE)`

#### `int HORSE_SupportCountHenchmen(object oPC)`

#### `void HORSE_SupportTransferPreservedValues(object oRider, object oHorse)`

#### `void HORSE_SupportDismountWrapper(int bAnimate, int bSetOwner)`

#### `void HORSE_SupportRestoreFromPreload(object oPC, int nApp, int nTail)`

#### `void HORSE_SupportSetMountingSentinel(object oRider, object oHorse, float fTimeout = 6.0, int nCount = 0)`

#### `void HORSE_Support_AssignRemainingMount(object oOwner)`

#### `void HORSE_SupportDeleteFromDatabase(object oPC, string sDatabase, int nN = 1)`

#### `void HORSE_SupportSaveToDatabase(object oPC, object oHenchman, string sDatabase, int nN = 1)`

#### `int HORSE_SupportGetHenchmanExistsInDatabase(object oPC, string sDatabase, int nN = 1)`

#### `void HORSE_SupportRestoreHenchmanFromDatabase(object oPC, string sDatabase, int nN = 1)`

#### `void HORSE_SupportDeleteMountedPCFromDatabase(object oPC, string sDatabase)`

#### `void HORSE_SupportStoreMountedPCInDatabase(object oPC, string sDatabase)`

#### `void HORSE_SupportReloadMountedPCFromDatabase(object oPC, string sDatabase)`

#### `void HorseReloadFromDatabase(object oPC, string sDatabase)`

#### `void HorseSaveToDatabase(object oPC, string sDatabase)`

#### `object HorseCreateHorse(string sResRef, location lLoc, object oOwner = OBJECT_INVALID, string sTag = "", int nAppearance = -1, int nTail = -1, int nFootstep = -1, string sScript = "")`

#### `int HorseGetIsMounted(object oTarget)`

#### `int HorseGetCanBeMounted(object oTarget, object oRider = OBJECT_INVALID, int bAssignMount = FALSE)`

#### `string HorseGetMountFailureMessage(object oTarget, object oRider = OBJECT_INVALID)`

#### `void HorseSetOwner(object oHorse, object oOwner, int bAssign = FALSE)`

#### `void HorseRemoveOwner(object oHorse)`

#### `object HorseGetOwner(object oHorse)`

#### `void HorseAddHorseMenu(object oPC)`

#### `void HorseSetPhenotype(object oRider, int bJoust = FALSE)`

#### `int HorseGetIsDisabled(object oCreature)`

#### `void HorseMount(object oHorse, int bAnimate = TRUE, int bInstant = FALSE, int nState = 0)`

#### `object HorseDismount(int bAnimate = TRUE, int bSetOwner = TRUE)`

#### `int HorseGetMountTail(object oHorse)`

#### `void HorseInstantDismount(object oRider)`

#### `void HorseInstantMount(object oRider, int nTail, int bJoust = FALSE, string sResRef = "")`

#### `object HorseGetPaladinMount(object oRider)`

#### `object HorseSummonPaladinMount(int bPHBDuration = FALSE)`

#### `void HorseUnsummonPaladinMount()`

#### `int HorseGetIsAMount(object oTarget)`

#### `void HorseStoreInventory(object oCreature, object oRider = OBJECT_INVALID)`

#### `void HorseRestoreInventory(object oCreature, int bDrop = FALSE)`

#### `void HorseChangeToDefault(object oCreature)`

#### `void HorseIfNotDefaultAppearanceChange(object oCreature)`

#### `object HorseGetMyHorse(object oRider)`

#### `int HorseGetHasAHorse(object oRider)`

#### `object HorseGetHorse(object oRider, int nN = 1)`

#### `void HorseRestoreHenchmenLocations(object oPC)`

#### `void HorseHitchHorses(object oHitch, object oClicker, location lPreJump)`

#### `void HorseForceJump(object oJumper, object oDestination, float fRange = 2.0, int nTimeOut = 10)`

#### `void HorseMoveAssociates(object oMaster)`

#### `void HorseDismountWrapper()`

#### `void HorseReassign(object oHorse, object oHench, object oMaster)`

#### `int HorseHandleDeath()`

#### `void HorsePreloadAnimations(object oPC)`
