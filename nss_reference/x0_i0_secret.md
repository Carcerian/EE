# `x0_i0_secret.nss`

Source: `NSS/x0_/x0_i0_secret.nss`  
10 functions · 8 constants

## Constants

| Constant | Type | Value | Note |
|---|---|---|---|
| `sRevealedVarname` | string | `"IS_REVEALED"` |  |
| `sOpenVarname` | string | `"IS_OPEN"` |  |
| `sSecretItemVarname` | string | `"SECRET_ITEM"` |  |
| `sDetectTriggerVarname` | string | `"SECRET_TRIGGER"` |  |
| `sFoundPrefix` | string | `"FOUND_"` |  |
| `sDestinationPrefix` | string | `"DST_"` |  |
| `sLocationPrefix` | string | `"LOC_"` |  |
| `EVENT_SECRET_REVEALED` | int | `2801` |  |

## Functions

#### `int GetIsSecretItemRevealed(object oDetectTrigger = OBJECT_SELF)`
> Returns whether the associated secret item is currently revealed;
> should be called from the detect trigger, not the item itself.
> (If you have the item itself, it is definitely revealed!)

#### `object GetSecretItemRevealed(object oDetectTrigger = OBJECT_SELF)`
> Returns the associated secret item

#### `int GetIsSecretItemOpen(object oSecretItem = OBJECT_SELF)`
> Returns whether the secret item is currently open --
> should be called from the secret item itself after
> being revealed.

#### `void SetIsSecretItemOpen(object oSecretItem = OBJECT_SELF, int bValue = TRUE)`
> Set whether the secret item is open or not

#### `int DetectSecretItem(object oPC, object oDetectTrigger = OBJECT_SELF, int nSkillType = SKILL_SEARCH)`
> Detection function for a secret item.
> Uses the specified skill (defaults to SKILL_SEARCH; use any of the
> SKILL_ constants here) and uses the key tag of the trigger as the DC
> of the detection check.
> Returns TRUE if player detects, FALSE otherwise.

#### `int DetectSecretItemByClass(object oPC, object oDetectTrigger = OBJECT_SELF, int nClassType = CLASS_TYPE_RANGER)`
> Detection function that reveals an item only to members of the specified
> class. Compares the PC's level in the class plus a small modifier against
> the value of the key tag of the trigger.

#### `void RevealSecretItem(string sResRef, object oDetectTrigger = OBJECT_SELF)`
> Reveal function for a secret item. When called, this item
> creates the secret item from blueprint in the location of the
> item waypoint. Any item blueprint resref can be used here.
> Some common items are the ones in the placeables palette listed
> under "Secret Items".

#### `void ResetSecretItem(object oDetectTrigger = OBJECT_SELF)`
> Reset function for a secret item. When called, this destroys the
> item and resets the invisible detection object going again. This WILL
> cause any treasure and locks/traps on the door to regenerate.

#### `void UseSecretTransport(object oPC, object oSecretItem = OBJECT_SELF)`
> Use a secret transport to transport a PC and associates

#### `int QuickDetectSecret(object oPC, object oDetectTrigger)`
> Private function (not prototyped to keep invisible in comments section)
> just to avoid a bit of duplicate code in the Detect... functions.
