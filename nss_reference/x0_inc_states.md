# `x0_inc_states.nss`

Source: `NSS/x0_/x0_inc_states.nss`  
2 functions · 22 constants

## Constants

| Constant | Type | Value | Note |
|---|---|---|---|
| `NW_ASC_DISTANCE_2_METERS` | int | `0x00000001` |  |
| `NW_ASC_DISTANCE_4_METERS` | int | `0x00000002` |  |
| `NW_ASC_DISTANCE_6_METERS` | int | `0x00000004` |  |
| `NW_ASC_HEAL_AT_75` | int | `0x00000008` |  |
| `NW_ASC_HEAL_AT_50` | int | `0x00000010` |  |
| `NW_ASC_HEAL_AT_25` | int | `0x00000020` |  |
| `NW_ASC_AGGRESSIVE_BUFF` | int | `0x00000040` |  |
| `NW_ASC_AGGRESSIVE_SEARCH` | int | `0x00000080` |  |
| `NW_ASC_AGGRESSIVE_STEALTH` | int | `0x00000100` |  |
| `NW_ASC_RETRY_OPEN_LOCKS` | int | `0x00000200` |  |
| `NW_ASC_OVERKIll_CASTING` | int | `0x00000400` | GetMax Spell |
| `NW_ASC_POWER_CASTING` | int | `0x00000800` | Get Double CR or max 4 casting |
| `NW_ASC_SCALED_CASTING` | int | `0x00001000` | CR + 4; |
| `NW_ASC_USE_CUSTOM_DIALOGUE` | int | `0x00002000` |  |
| `NW_ASC_DISARM_TRAPS` | int | `0x00004000` |  |
| `NW_ASC_USE_RANGED_WEAPON` | int | `0x00008000` |  |
| `NW_ASC_MODE_DEFEND_MASTER` | int | `0x04000000` | Guard Me Mode, Attack Nearest sets this to FALSE. |
| `NW_ASC_MODE_STAND_GROUND` | int | `0x08000000` | The Henchman will ignore move to object in the heartbeat |
| `NW_ASC_MASTER_GONE` | int | `0x10000000` |  |
| `NW_ASC_MASTER_REVOKED` | int | `0x20000000` |  |
| `NW_ASC_IS_BUSY` | int | `0x40000000` | Only busy if attempting to bash or pick a lock |
| `NW_ASC_HAVE_MASTER` | int | `0x80000000` | Not actually used, here for system continuity |

## Functions

#### `void SetAssociateState(int nCondition, int bValid = TRUE)`

#### `int GetAssociateState(int nCondition)`
