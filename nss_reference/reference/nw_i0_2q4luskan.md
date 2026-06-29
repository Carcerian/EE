# `nw_i0_2q4luskan.nss`

Source: `NSS/nw_/nw_i0_2q4luskan.nss`  
26 functions · 22 constants

## Constants

| Constant | Type | Value | Note |
|---|---|---|---|
| `PLOT_2Q4_ITEM_KURTH_BASE_KEY` | int | `1` |  |
| `PLOT_2Q4_ITEM_BARAM_BASE_KEY` | int | `2` |  |
| `PLOT_2Q4_ITEM_ERBS_RING` | int | `3` |  |
| `NW_2Q4_COLMARR_FIRE_LEVER` | int | `0x00000001` |  |
| `NW_2Q4_COLMARR_AIR_LEVER` | int | `0x00000002` |  |
| `NW_2Q4_COLMARR_WATER_LEVER` | int | `0x00000004` |  |
| `NW_2Q4_COLMARR_STONE_LEVER` | int | `0x00000008` |  |
| `NW_2Q4_ENGINE_STATE_OFF` | int | `0x00000000` | Levers all off |
| `NW_2Q4_ENGINE_IDENTIFY` | int | `0x00000001` | Fire |
| `NW_2Q4_ENGINE_AID` | int | `0x00000002` | Air |
| `NW_2Q4_ENGINE_CURE_LIGHT` | int | `0x00000004` | Water |
| `NW_2Q4_ENGINE_BARKSKIN` | int | `0x00000008` | Earth |
| `NW_2Q4_FOXS_CUNNING` | int | `0x00000005` | Fire and Water |
| `NW_2Q4_INVISIBILITY` | int | `0x0000000A` | Air and Earth |
| `NW_2Q4_ENDURANCE` | int | `0x0000000C` | Water and Earth |
| `NW_2Q4_BULLS_STRENGTH` | int | `0x00000009` | Fire and Earth |
| `NW_2Q4_CATS_GRACE` | int | `0x00000003` | Fire and Air |
| `NW_2Q4_CURE_MODERATE` | int | `0x00000006` | Water and Air |
| `NW_2Q4_SPEED` | int | `0x00000007` | Fire, Air and Water |
| `NW_2Q4_CURE_SERIOUS` | int | `0x0000000B` | Fire, Air and Earth |
| `NW_2Q4_CLARITY` | int | `0x0000000E` | Air, Water and Earth |
| `NW_2Q4_ENGINE_STATE_ON` | int | `0x0000000F` | Levers all on gives sewage |

## Functions

#### `void Give2Q4PlotItem(int nPlotItemConstant)`
> Function to determine what plot item to hand to the character

#### `int GetHas2Q4PlotItem(object oItemPossesser, int nPlotItemConstant)`
> Test if the object has the specified plot item

#### `void MoveTo2Q4PlotPoint(int nPlotPointIndex)`
> Pass in one of nine predetermined way points to move the character to.

#### `void SetLocalPlotIntOnCharacter(object oNPC, int nPlotStateIndex)`
> Set a generic plot flag on a specific character

#### `int GetLocalPlotIntFromCharacter(object oNPC)`
> Get the generic plot flag off of a character

#### `int GetCanSeePC(object oObject = OBJECT_SELF)`
> Returns true if a PC can be seen

#### `void PlayConversationAnimation(int nAnimationConstant, object oTarget = OBJECT_INVALID)`
> Sets the animation on the creature and makes them face the PC if object left invalid.

#### `void CreateColmarrPotion()`
> This is a plot specific function used to generate potions for Colmarr's Machine.

#### `void SetMachineState(int nCondition, int bValid)`
> Set the new state of the machine after the lever is pressed.

#### `int GetMachineState(int nCondition)`
> Get the state of one lever

#### `void FaceNearestPC()`
> Makes the NPC face the nearest PC

#### `void AssignPCDebugString(string sString)`
> Make the nearest PC say the stated string

#### `void CreateObjectVoid(int nObjectType, string sTemplate, location lLoc, int bUseAppearAnimation = FALSE)`
> Creates a creature with a specific string at a specified location

#### `void Give2Q4PlotItem(int nPlotItemConstant)`

#### `int GetHas2Q4PlotItem(object oItemPossesser, int nPlotItemConstant)`

#### `void MoveTo2Q4PlotPoint(int nPlotPointIndex)`

#### `void SetLocalPlotIntOnCharacter(object oNPC, int nPlotStateIndex)`

#### `int GetLocalPlotIntFromCharacter(object oNPC)`

#### `int GetCanSeePC(object oObject = OBJECT_SELF)`

#### `void PlayConversationAnimation(int nAnimationConstant, object oTarget)`
> Created By: Preston Watamaniuk
> Created On: Jan 28, 2002

#### `void CreateColmarrPotion()`

#### `void SetMachineState(int nCondition, int bValid)`

#### `int GetMachineState(int nCondition)`

#### `void FaceNearestPC()`

#### `void AssignPCDebugString(string sString)`

#### `void CreateObjectVoid(int nObjectType, string sTemplate, location lLoc, int bUseAppearAnimation = FALSE)`
