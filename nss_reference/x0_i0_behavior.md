# `x0_i0_behavior.nss`

Source: `NSS/x0_/x0_i0_behavior.nss`  
2 functions · 4 constants

## Constants

| Constant | Type | Value | Note |
|---|---|---|---|
| `NW_FLAG_BEHAVIOR_SPECIAL` | int | `0x00000001` |  |
| `NW_FLAG_BEHAVIOR_CARNIVORE` | int | `0x00000002` |  |
| `NW_FLAG_BEHAVIOR_OMNIVORE` | int | `0x00000004` |  |
| `NW_FLAG_BEHAVIOR_HERBIVORE` | int | `0x00000008` |  |

## Functions

#### `void SetBehaviorState(int nCondition, int bValid = TRUE)`
> Add the specified condition flag to the behavior state of the caller

#### `int GetBehaviorState(int nCondition)`
> Returns TRUE if the specified behavior flag is set on the caller
