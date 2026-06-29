# `x0_i0_spawncond.nss`

Source: `NSS/x0_/x0_i0_spawncond.nss`  
8 functions · 28 constants

## Constants

| Constant | Type | Value | Note |
|---|---|---|---|
| `sSpawnCondVarname` | string | `"NW_GENERIC_MASTER"` |  |
| `NW_FLAG_SPECIAL_CONVERSATION` | int | `0x00000001` |  |
| `NW_FLAG_SHOUT_ATTACK_MY_TARGET` | int | `0x00000002` |  |
| `NW_FLAG_STEALTH` | int | `0x00000004` |  |
| `NW_FLAG_SEARCH` | int | `0x00000008` |  |
| `NW_FLAG_SET_WARNINGS` | int | `0x00000010` |  |
| `NW_FLAG_ESCAPE_RETURN` | int | `0x00000020` | Failed |
| `NW_FLAG_ESCAPE_LEAVE` | int | `0x00000040` |  |
| `NW_FLAG_TELEPORT_RETURN` | int | `0x00000080` | Failed |
| `NW_FLAG_TELEPORT_LEAVE` | int | `0x00000100` |  |
| `NW_FLAG_PERCIEVE_EVENT` | int | `0x00000200` |  |
| `NW_FLAG_ATTACK_EVENT` | int | `0x00000400` |  |
| `NW_FLAG_DAMAGED_EVENT` | int | `0x00000800` |  |
| `NW_FLAG_SPELL_CAST_AT_EVENT` | int | `0x00001000` |  |
| `NW_FLAG_DISTURBED_EVENT` | int | `0x00002000` |  |
| `NW_FLAG_END_COMBAT_ROUND_EVENT` | int | `0x00004000` |  |
| `NW_FLAG_ON_DIALOGUE_EVENT` | int | `0x00008000` |  |
| `NW_FLAG_RESTED_EVENT` | int | `0x00010000` |  |
| `NW_FLAG_DEATH_EVENT` | int | `0x00020000` |  |
| `NW_FLAG_SPECIAL_COMBAT_CONVERSATION` | int | `0x00040000` |  |
| `NW_FLAG_AMBIENT_ANIMATIONS` | int | `0x00080000` |  |
| `NW_FLAG_HEARTBEAT_EVENT` | int | `0x00100000` |  |
| `NW_FLAG_IMMOBILE_AMBIENT_ANIMATIONS` | int | `0x00200000` |  |
| `NW_FLAG_DAY_NIGHT_POSTING` | int | `0x00400000` |  |
| `NW_FLAG_AMBIENT_ANIMATIONS_AVIAN` | int | `0x00800000` |  |
| `NW_FLAG_APPEAR_SPAWN_IN_ANIMATION` | int | `0x01000000` |  |
| `NW_FLAG_SLEEPING_AT_NIGHT` | int | `0x02000000` |  |
| `NW_FLAG_FAST_BUFF_ENEMY` | int | `0x04000000` |  |

## Functions

#### `void SetSpawnInCondition(int nCondition, int bValid = TRUE)`
> Sets the specified spawn-in condition on the caller as directed.

#### `int GetSpawnInCondition(int nCondition)`
> Returns TRUE if the specified condition has been set on the
> caller, otherwise FALSE.

#### `void SetSpawnInLocals(int nCondition)`
> Sets the listening patterns and local variables needed
> for the given spawn-in condition on the caller.

#### `void SetListeningPatterns()`
> Sets the correct listen checks on the NPC by
> determining what talents they possess or what
> class they use.

#### `void SetSpawnInCondition(int nCondition, int bValid = TRUE)`
> Sets the specified spawn-in condition on the caller as directed.

#### `int GetSpawnInCondition(int nCondition)`
> Returns TRUE if the specified condition has been set on the
> caller, otherwise FALSE.

#### `void SetSpawnInLocals(int nCondition)`
> Sets the listening patterns and local variables needed
> for the given spawn-in condition on the caller.

#### `void SetListeningPatterns()`
