# `x2_inc_restsys.nss`

Source: `NSS/x2_/x2_inc_restsys.nss`  
26 functions · 7 constants

## Constants

| Constant | Type | Value | Note |
|---|---|---|---|
| `X2_WM_2DA_NAME` | string | `"des_restsystem"` |  |
| `X2_WM_SPAWNSPOT_TAG` | string | `"x2_restsys_spawn"` |  |
| `X2_WM_SPAWNSPOT_EVENTID` | int | `2011` |  |
| `X2_WM_FLOOD_PROTECTION_PERIOD` | float | `10.0f` |  |
| `X2_WMT_INVALID_TABLE` | int | `0` | Row number of NO_TABLE_SETTable |
| `X2_WMT_DEFAULT_FEEDBACK_FAIL` | int | `83306` | Default StrRef when failing listen check check |
| `X2_WMT_DEFAULT_FEEDBACK_SUCCESS` | int | `83307` | Default StrRef when succeeding listen check |

## Functions

#### `void WMSetAreaProbability(object oArea, int nDayPercent, int nNightPercent)`
> Change the probability of encountering a wandering monster for an area
> oArea - the Area
> sTableName - The name of the encounter table (TableName Column in 2da)
> NOTE: You can call WMSetAreaProbability later to change the probability
> of having an encounter

#### `void WMSetAreaTable(object oArea, string sTableName, int bUseDoors = FALSE, int nListenCheckDC = -1)`
> Call this to define the encounter table to use with the wandering monster
> system.
> oArea - the Area
> sTableName - The name of the encounter table (TableName Column in 2da)
> bUseDoors -  Monsters will spawn behind the next not-locked door, open them
> and move onto the pc (default = TRUE )
> nListenCheckDC - The DC to beat in an listen check in order to wake up early.
> (default = -1, use value in 2da)
> NOTE: You can call WMSetAreaProbability later to change the probability
> of having an encounter

#### `int WMGetAreaHasTable(object oArea)`
> Returns TRUE if oArea has a wandering monster table set. Use WMSetAreaTable to
> set a wandering monster table on an area

#### `int WMGetUseAppearAnimation(object oArea)`
> Returns TRUE if a X2_L_WM_USE_APPEAR_ANIMATIONS has been set to TRUE on the area
> making all creatures appearing within use their appear animations

#### `int WMGetWanderingMonstersDisabled(object oArea)`
> Returns TRUE if oArea has the Wandering Monster System disabled

#### `void WMSetWanderingMonstersDisabled(object oArea, int bDisabled = FALSE)`
> Sets if oArea has the Wandering Monster System disabled

#### `int WMCheckForWanderingMonster(object oPC)`
> Wandering Monster System, Check for wandering
> monster
> oPC - the player who triggered the check
> This will check if the player has triggered a wandering monster
> and return TRUE if yes.
> To be used in the OnRest event handler.  It will also setup the
> encounter so if ExecuteScript (DoWanderingMonster) is called on
> a PC, the encounter will start.

#### `void WMBuild2DACache()`
> Reads all encounter tables from 2da
> specified in X2_WM_2DA_NAME and caches them
> to LocalVariables to speed up access to them.
> This function is intended to be used
> in an OnModuleLoad event script

#### `void WMSetupAmbush(object oPC, string sMonsters)`
> Setup the necessary variables for the x2_restsys_ambus script
> You probably won't ever need this function as it is used internally by the system, but you could
> use it to build your own monster ambush (just call WMRunAmbush() to execute)
> oPC - The player to be ambushed
> sMonsters - one or more monster ResRefs, comma seperated with no whitespaces in between
> Examples:
> WMSetupAmbush(GetEnteringObject(), "nw_dog,nw_dog") for multiple enemies
> WMSetupAmbush(GetEnteringObject(), "nw_badger") for a single enemy

#### `void WMRunAmbush(object oPC)`
> This command runs the actual wandering monster ambush on the pc, using the data stored
> by WMSetupAmbush. It is called by x2_restsys_ambus.nss.

#### `int WMStartPlayerRest(object oPC)`
> Placeholder at the moment - handles sleep and multiplayer code
> If an ambush is in progress it will return FALSE so resting can be disabled
> Fades Screen to Black for PC

#### `void WMFinishPlayerRest(object oPC, int bRestCanceled = FALSE)`
> Removes the cutscene blackness, etc
> Called after a rest is done from OnPlayerRest Event

#### `int WMGetAreaListenCheck(object oArea)`
> Returns the DC to beat in a listen check to wake up. Its defined in the 2da
> but can be overwritten in WMSetAreaTable)

#### `int WMDoListenCheck(object oPC)`
> Do a listen check against the designer defined DC for waking up in that area
> See WMSetAreaTable() on how to set the DC.
> Returns TRUE if check was successful

#### `string Get2DAStringOrDefault(string s2DA, string sColumn, int nRow, string sDefault)`
> Get a 2da String or the supplied default if string is empty

#### `void WMDebug(string sWrite)`
> Debug Output, remove all calls to this for version

#### `string WMGet2DAToUse()`
> Retrieve the 2da to use for the system

#### `struct wm_struct GetNextWMTableEntry(int bAllData = FALSE)`
> This function returns a wm_struct of the row number currently set in LocalInt
> X2_WM_ROWSCANPTR
> on the Module. if bAllData is true, it will read all columns of the 2da, if not,
> it will just return the RowNumber and Probability columns.
> This is the place where data gets read from the 2da... the only place
> Use after GetFirstWMTableEntry until wm_struct.nRowNumber = -1

#### `struct wm_struct GetFirstWMTableEntry(int bAllData = FALSE)`

#### `struct wm_struct GetWMTableEntryByIndex(int nNo)`
> returns a FULL Data wm_struct of row nNo from the wandering monster 2da file

#### `struct wm_struct GetWMStructByName(string sName, int bAllData = FALSE)`
> return a wm_struct of the data in the row with TableName sName in the 2da

#### `struct wm_struct WMGetAreaMonsterTable(object oArea)`
> Returns a wm_struct containing the full wandering monster table
> for the selected area.

#### `string WMGetWanderingMonsterFrom2DA(object oPC)`
> Returns a string containing or more wandering monsters
> from the encounter table currently active for oPC's area

#### `location WMGetAmbushSpot(object oPC)`
> Calulates the best ambush spot for the monster's using the area preset values
> If a placeable/waypoint is found, it will be stored as object in
> X2_WM_AMBUSH_SPOT for later retrival
> If a door is used as spawnspot, it will be stored in X2_WM_AMBUSH_DOOR
> for later retrieval

#### `void WMSpawnAmbushMonsters(object oPC, location lSpot)`
> I had to make this a seperate function in order to delay it
> It is just called from inside WMRunAmbush

#### `void WMMakePartyRest(object oPC)`
> Will make the party of the character rest as long as everyone is in the
> same area currently not useds
