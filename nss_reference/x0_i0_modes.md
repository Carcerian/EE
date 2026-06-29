# `x0_i0_modes.nss`

Source: `NSS/x0_/x0_i0_modes.nss`  
8 functions · 3 constants

## Constants

| Constant | Type | Value | Note |
|---|---|---|---|
| `sModeVarname` | string | `"NW_MODES_CONDITION"` |  |
| `NW_MODE_STEALTH` | int | `0x00000001` |  |
| `NW_MODE_DETECT` | int | `0x00000002` |  |

## Functions

#### `int GetModeActive(int nMode, object oCreature = OBJECT_SELF)`
> TRUE if the given creature has the given mode active

#### `void SetModeActive(int nMode, int bActive = TRUE, object oCreature = OBJECT_SELF)`
> Mark that the given creature has the given mode active or not

#### `void UseStealthMode()`
> If stealth mode is active, turn on the appropriate skills.

#### `void UseDetectMode()`
> If detect mode is active, turn on the appropriate skills.

#### `int GetModeActive(int nMode, object oCreature = OBJECT_SELF)`
> TRUE if the given creature has the given mode active

#### `void SetModeActive(int nMode, int bActive = TRUE, object oCreature = OBJECT_SELF)`
> Mark that the given creature has the given mode active or not

#### `void UseStealthMode()`
> If stealth mode is active, turn on the appropriate skills.

#### `void UseDetectMode()`
> If detect mode is active, turn on the appropriate skills.
