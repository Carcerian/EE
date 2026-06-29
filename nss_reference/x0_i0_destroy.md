# `x0_i0_destroy.nss`

Source: `NSS/x0_/x0_i0_destroy.nss`  
3 functions · 1 constants

## Constants

| Constant | Type | Value | Note |
|---|---|---|---|
| `INVISIBLE_OBJECT_RESREF` | string | `"plc_invisobj"` |  |

## Functions

#### `int CountAllObjectsInAreaByTag(string sTag, object oSource = OBJECT_SELF)`
> Count all objects in the area with a matching tag

#### `void DestroyNearestObjectByTag(string sTag, object oSource = OBJECT_SELF, float fDelay = 0.1)`
> Destroy the nearest object in the source's area by tag

#### `void DestroyObjectsInAreaByTag(string sTag, object oCenter = OBJECT_SELF, int nLimit = 0)`
> Destroy all the objects in the area with a given tag.
> If nLimit is > 0, this will be the maximum number of things
> destroyed with the given tag.
