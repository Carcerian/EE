# `x2_inc_globals.nss`

Source: `NSS/x2_/x2_inc_globals.nss`  
30 functions · 1 constants

## Constants

| Constant | Type | Value | Note |
|---|---|---|---|
| `DB_NAME` | string | `"XP2"` |  |

## Functions

#### `void SetGlobalInt(string sVarName, int nValue)`
> Wrapper function for setting important variables in Chapter 2
> This will eventually be modified to set the variables on the
> database.

#### `int GetGlobalInt(string sVarName)`
> Wrapper function for setting important variables in Chapter 2
> This will eventually be modified to set the variables on the
> database.

#### `void SetGlobalString(string sVarName, string sValue)`
> Wrapper function for setting important variables in Chapter 2
> This will eventually be modified to set the variables on the
> database.

#### `string GetGlobalString(string sVarName)`
> Wrapper function for setting important variables in Chapter 2
> This will eventually be modified to set the variables on the
> database.

#### `void ClearDatabase()`
> Only needed while things are being implemented
> Should be called ????;

#### `void CopyVariableIntToDatabase(string sVar)`
> Copies the specified variable from the Module to the database

#### `void CopyAllHenchmen(object oPlayer)`
> Copies all henchmen over

#### `void RestoreAllHenchmen(location lLoc, object oPlayer)`
> Restore henchmen. THis function should be called after all other
> database fetches because it destroys the database.

#### `void CallForthHenchman(string sTag, string sMemory)`
> Call this function as a wrapper for retrieving a henchman from hell
> the henchmen should have been loaded in

#### `void RestoreHenchmenVariables(object oHench)`
> ReStores all important variables that the
> the henchmen may have on them  from db

#### `void ReturnToChapter2()`

#### `int PCBetrayedNathyrra()`
> Returns whether player betrayed nathyrra

#### `int PCBetrayedValen()`
> Returns whether player betrayed nathyrra

#### `void StoreInt(string sVarName)`
> Store/Restore used as a quick short-cut to save and the load the GetModule() globals

#### `void RestoreInt(string sVarName)`

#### `void StoreIntFromObject(string sVarName, object oSelf)`
> gets an int from an object other than the module

#### `void RestoreIntFromObject(string sVarName, object oSelf)`
> gets an int from an object other than the module

#### `void StoreString(string sVarName)`

#### `void RestoreString(string sVarName)`

#### `void StoreHenchmenVariables(object oHench)`
> Stores all important variables that the
> the henchmen may have on them  into the database
> Must be careful in this function to avoid strings that are too long...

#### `object WrapCopyItem(object oItem, object oTarget, int bIgnoreCursedAndNoDrop = FALSE)`

#### `void CopyInventory(object oSource, object oTarget, int bIgnoreCursedAndNoDrop = FALSE)`
> copies everything from oSource's inventory into oTarget
> can be used with either Creatures or Stores
> does not destroy original
> bIgnoreCursedAndNoDrop - set this flag to true if you don't want things like henchmen items copied

#### `void RemoveInventory(object oStore)`
> used at start of c2 and c3 to "blank" the genie store.

#### `void CopyOriginalFourInventory()`
> Copies the original 4 henchmen inventories into the Pool of Lost Souls

#### `void StorePoolOfLostSouls(object oPC)`
> Copies the Pool of Lost Souls

#### `object RestorePoolOfLostSouls(object oPC)`
> Copies the Pool of Lost Souls  into the place of the existing one in the module

#### `void StoreWeaponInt(object oPC, string sVarName)`

#### `void RestoreWeaponInt(object oPC, string sVarName)`

#### `void StoreWeaponVars(object oPC)`
> stores the variables for the intelligent weapon

#### `void RestoreWeaponVars(object oPC)`
> restores weapon variables
