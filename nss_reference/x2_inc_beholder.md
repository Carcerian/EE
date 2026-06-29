# `x2_inc_beholder.nss`

Source: `NSS/x2_/x2_inc_beholder.nss`  
7 functions · 7 constants

## Constants

| Constant | Type | Value | Note |
|---|---|---|---|
| `BEHOLDER_RAY_DEATH` | int | `1` |  |
| `BEHOLDER_RAY_TK` | int | `2` |  |
| `BEHOLDER_RAY_PETRI` | int | `3` |  |
| `BEHOLDER_RAY_CHARM` | int | `4` |  |
| `BEHOLDER_RAY_SLOW` | int | `5` |  |
| `BEHOLDER_RAY_WOUND` | int | `6` |  |
| `BEHOLDER_RAY_FEAR` | int | `7` |  |

## Functions

#### `int GetAntiMagicRayMakesSense(object oTarget)`

#### `void OpenAntiMagicEye(object oTarget)`

#### `void CloseAntiMagicEye(object oTarget)`
> being a badass beholder, we close our antimagic eye only to attack with our eye rays
> and then reopen it...

#### `int BehGetTargetThreatRating(object oTarget)`

#### `int BehDetermineHasEffect(int nRay, object oCreature)`
> stacking protection

#### `void BehDoFireBeam(int nRay, object oTarget)`

#### `struct beholder_target_struct GetRayTargets(object oTarget)`
