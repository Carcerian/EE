# `x0_i0_npckilled.nss`

Source: `NSS/x0_/x0_i0_npckilled.nss`  
14 functions · 3 constants

## Constants

| Constant | Type | Value | Note |
|---|---|---|---|
| `sKilledPrefix` | string | `"X0_KILLED_"` |  |
| `sResurrectedPrefix` | string | `"X0_RESURRECTED_"` |  |
| `sJustResurrectedVarname` | string | `"X0_I_WAS_JUST_RESURRECTED"` |  |

## Functions

#### `void SetNPCKilled(object oPC, string sNPCTag, int bDidKill = TRUE)`
> Mark all members of the party as having killed the NPC

#### `int GetNPCKilled(object oPC, string sNPCTag)`
> Determine if the player killed this NPC

#### `object CreateReplacementNPC(object oPC, string sNPCResRef, location lNPC)`
> Create a replacement for the NPC
> General system:
> - Create an NPC *BLUEPRINT*
> - Put it in a non-hostile faction and set it PLOT
> - Use the script 'x0_d1_go_hostile' in conversation to cause the
> NPC to become hostile and to unset its PLOT flag.
> - Put the script 'x0_death_npc' in the OnDeath handler function
> of the NPC.
> - Create a conversation node for after the NPC's death using the
> script 'x0_d2_npckilled'.
> - Paint the NPC in the appropriate location.

#### `void SetNPCJustResurrected(object oNPC = OBJECT_SELF, int bRaised = TRUE)`
> Mark the NPC as just having been resurrected

#### `int GetNPCJustResurrected(object oNPC = OBJECT_SELF)`
> Check if the NPC was just resurrected

#### `void SetNPCResurrected(object oPC, object oNPC = OBJECT_SELF, int bRaised = TRUE)`
> Mark the PC & friends as having resurrected this NPC
> and clear the 'just resurrected' var.

#### `int GetNPCResurrected(object oPC, object oNPC = OBJECT_SELF)`
> Check if this PC resurrected this NPC

#### `void SetNPCKilled(object oPC, string sNPCTag, int bDidKill = TRUE)`
> Mark all members of the party as having killed the NPC

#### `int GetNPCKilled(object oPC, string sNPCTag)`
> Determine if the player killed this NPC

#### `object CreateReplacementNPC(object oPC, string sNPCResRef, location lNPC)`
> Create a replacement for the NPC

#### `void SetNPCJustResurrected(object oNPC = OBJECT_SELF, int bRaised = TRUE)`
> Mark the NPC as just having been resurrected

#### `int GetNPCJustResurrected(object oNPC = OBJECT_SELF)`
> Check if the NPC was just resurrected

#### `void SetNPCResurrected(object oPC, object oNPC = OBJECT_SELF, int bRaised = TRUE)`
> Mark the PC & friends as having resurrected this NPC
> and clear the 'just resurrected' var.

#### `int GetNPCResurrected(object oPC, object oNPC = OBJECT_SELF)`
> Check if this PC resurrected this NPC
> Check if the NPC was just resurrected
