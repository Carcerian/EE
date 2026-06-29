# `x0_inc_skills.nss`

Source: `NSS/x0_/x0_inc_skills.nss`  
15 functions · 63 constants

## Constants

| Constant | Type | Value | Note |
|---|---|---|---|
| `mySKILL_CRAFT_TRAP` | int | `22` |  |
| `SKILL_TRAP_DCMINOR` | int | `2001` |  |
| `SKILL_TRAP_DCAVERAGE` | int | `2002` |  |
| `SKILL_TRAP_DCSTRONG` | int | `2003` |  |
| `SKILL_TRAP_DCDEADLY` | int | `2004` |  |
| `SKILL_CTRAP_FIRECOMPONENT` | string | `"X1_WMGRENADE002"` | alchemists fire |
| `SKILL_CTRAP_ELECTRICALCOMPONENT` | string | `"NW_IT_MSMLMISC11"` | quartz crystal |
| `SKILL_CTRAP_TANGLECOMPONENT` | string | `"X1_WMGRENADE006"` | tanglefoot bag |
| `SKILL_CTRAP_SPIKECOMPONENT` | string | `"X1_WMGRENADE003"` | caltrops |
| `SKILL_CTRAP_HOLYCOMPONENT` | string | `"X1_WMGRENADE005"` | holy water |
| `SKILL_CTRAP_GASCOMPONENT` | string | `"X1_WMGRENADE004"` | choking powder |
| `SKILL_CTRAP_FROSTCOMPONENT` | string | `"X1_IT_MSMLMISC01"` | coldstone |
| `SKILL_CTRAP_NEGATIVECOMPONENT` | string | `"NW_IT_MSMLMISC13"` | skeleton knuckles |
| `SKILL_CTRAP_SONICCOMPONENT` | string | `"X1_WMGRENADE007"` | thunderstone |
| `SKILL_CTRAP_ACIDCOMPONENT` | string | `"X1_WMGRENADE001"` | acid flask |
| `SKILL_TRAP_MINOR` | int | `1` |  |
| `SKILL_TRAP_AVERAGE` | int | `3` |  |
| `SKILL_TRAP_STRONG` | int | `5` |  |
| `SKILL_TRAP_DEADLY` | int | `7` |  |
| `SKILLDC_TRAP_BASE_TYPE_MINOR_SPIKE` | int | `5` |  |
| `SKILLDC_TRAP_BASE_TYPE_AVERAGE_SPIKE` | int | `20` |  |
| `SKILLDC_TRAP_BASE_TYPE_STRONG_SPIKE` | int | `25` |  |
| `SKILLDC_TRAP_BASE_TYPE_DEADLY_SPIKE` | int | `35` |  |
| `SKILLDC_TRAP_BASE_TYPE_MINOR_HOLY` | int | `15` |  |
| `SKILLDC_TRAP_BASE_TYPE_AVERAGE_HOLY` | int | `20` |  |
| `SKILLDC_TRAP_BASE_TYPE_STRONG_HOLY` | int | `25` |  |
| `SKILLDC_TRAP_BASE_TYPE_DEADLY_HOLY` | int | `30` |  |
| `SKILLDC_TRAP_BASE_TYPE_MINOR_TANGLE` | int | `15` |  |
| `SKILLDC_TRAP_BASE_TYPE_AVERAGE_TANGLE` | int | `20` |  |
| `SKILLDC_TRAP_BASE_TYPE_STRONG_TANGLE` | int | `25` |  |
| `SKILLDC_TRAP_BASE_TYPE_DEADLY_TANGLE` | int | `30` |  |
| `SKILLDC_TRAP_BASE_TYPE_MINOR_ACID` | int | `15` |  |
| `SKILLDC_TRAP_BASE_TYPE_AVERAGE_ACID` | int | `25` |  |
| `SKILLDC_TRAP_BASE_TYPE_STRONG_ACID` | int | `30` |  |
| `SKILLDC_TRAP_BASE_TYPE_DEADLY_ACID` | int | `35` |  |
| `SKILLDC_TRAP_BASE_TYPE_MINOR_FIRE` | int | `20` |  |
| `SKILLDC_TRAP_BASE_TYPE_AVERAGE_FIRE` | int | `25` |  |
| `SKILLDC_TRAP_BASE_TYPE_STRONG_FIRE` | int | `30` |  |
| `SKILLDC_TRAP_BASE_TYPE_DEADLY_FIRE` | int | `35` |  |
| `SKILLDC_TRAP_BASE_TYPE_MINOR_ELECTRICAL` | int | `20` |  |
| `SKILLDC_TRAP_BASE_TYPE_AVERAGE_ELECTRICAL` | int | `25` |  |
| `SKILLDC_TRAP_BASE_TYPE_STRONG_ELECTRICAL` | int | `30` |  |
| `SKILLDC_TRAP_BASE_TYPE_DEADLY_ELECTRICAL` | int | `35` |  |
| `SKILLDC_TRAP_BASE_TYPE_MINOR_GAS` | int | `30` |  |
| `SKILLDC_TRAP_BASE_TYPE_AVERAGE_GAS` | int | `35` |  |
| `SKILLDC_TRAP_BASE_TYPE_STRONG_GAS` | int | `40` |  |
| `SKILLDC_TRAP_BASE_TYPE_DEADLY_GAS` | int | `45` |  |
| `SKILLDC_TRAP_BASE_TYPE_MINOR_FROST` | int | `15` |  |
| `SKILLDC_TRAP_BASE_TYPE_AVERAGE_FROST` | int | `20` |  |
| `SKILLDC_TRAP_BASE_TYPE_STRONG_FROST` | int | `25` |  |
| `SKILLDC_TRAP_BASE_TYPE_DEADLY_FROST` | int | `30` |  |
| `SKILLDC_TRAP_BASE_TYPE_MINOR_NEGATIVE` | int | `15` |  |
| `SKILLDC_TRAP_BASE_TYPE_AVERAGE_NEGATIVE` | int | `20` |  |
| `SKILLDC_TRAP_BASE_TYPE_STRONG_NEGATIVE` | int | `25` |  |
| `SKILLDC_TRAP_BASE_TYPE_DEADLY_NEGATIVE` | int | `30` |  |
| `SKILLDC_TRAP_BASE_TYPE_MINOR_SONIC` | int | `15` |  |
| `SKILLDC_TRAP_BASE_TYPE_AVERAGE_SONIC` | int | `20` |  |
| `SKILLDC_TRAP_BASE_TYPE_STRONG_SONIC` | int | `25` |  |
| `SKILLDC_TRAP_BASE_TYPE_DEADLY_SONIC` | int | `30` |  |
| `SKILLDC_TRAP_BASE_TYPE_MINOR_ACID_SPLASH` | int | `15` |  |
| `SKILLDC_TRAP_BASE_TYPE_AVERAGE_ACID_SPLASH` | int | `20` |  |
| `SKILLDC_TRAP_BASE_TYPE_STRONG_ACID_SPLASH` | int | `25` |  |
| `SKILLDC_TRAP_BASE_TYPE_DEADLY_ACID_SPLASH` | int | `30` |  |

## Functions

#### `int skillCTRAPGetHasComponent(string sComponent, object oPC, int nTrapDifficulty)`

#### `void skillCTRAPTakeComponent(string sComponent, object oPC, int nTrapDifficulty)`

#### `int skillCTRAPSetCurrentTrapView(string sComponent)`

#### `int skillCTRAPGetCurrentTrapViewEquals(string sComponent)`

#### `string skillCTRAPGetCurrentTrapView()`

#### `void DestroyNumItems(object oTarget, string sItem, int nNumItems)`
> destroys the indicated number of items

#### `void skillCTRAPCreateTrapKit(string sComponent, object oPC, int nTrapDifficulty)`

#### `int skillCTRAPGetHasComponent(string sComponent, object oPC, int nTrapDifficulty)`

#### `void skillCTRAPTakeComponent(string sComponent, object oPC, int nTrapDifficulty)`

#### `void ClearTrapMaking()`
> Created By:
> Created On:

#### `void skillCTRAPCreateTrapKit(string sComponent, object oPC, int nTrapDifficulty)`

#### `void skillCTRAPSetCurrentTrapView(string sComponent)`
> Created By:
> Created On:

#### `int skillCTRAPGetCurrentTrapViewEquals(string sComponent)`
> returns true if sComponent is equal to the current trap view

#### `string skillCTRAPGetCurrentTrapView()`
> returns the string of the current trap view

#### `void DestroyNumItems(object oTarget, string sItem, int nNumItems)`
> destroys the indicated number of items
