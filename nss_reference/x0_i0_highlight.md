# `x0_i0_highlight.nss`

Source: `NSS/x0_/x0_i0_highlight.nss`  
5 functions · 0 constants

## Functions

#### `void AddHighlight(object oTarget, int nVisualEffect = VFX_DUR_ETHEREAL_VISAGE)`
> Apply a highlight effect to an object. Lasts permanently until
> removed.
> A few good ones, although any VFX_DUR_ effect can be used:
> VFX_DUR_ETHEREAL_VISAGE: glowing, purple, transparent
> VFX_DUR_GHOSTLY_VISAGE: glowing, blue, transparent
> VFX_DUR_BLUR: alternating blue/white pulsing glow
> VFX_DUR_PARALYZED: alternating red/white pulsing glow
> VFX_DUR_PROT_SHADOW_ARMOR: shimmery opaque black glow
> VFX_DUR_MIND_AFFECTING_DOMINATED: spinning crown of lights
> VFX_DUR_MIND_AFFECTING_DISABLED: crown of sparkling lights

#### `void AddTemporaryHighlight(object oTarget, int nVisualEffect = VFX_DUR_ETHEREAL_VISAGE, float fDuration = 10.0f)`
> Adds a temporary highlight to an object.
> See comments to AddHighlight for suggested highlight effects.

#### `void RemoveHighlight(object oTarget, int nVisualEffect = VFX_NONE)`
> Remove the highlight from an object.
> If not specified, removes the last-added highlight, although
> this default behavior will NOT work twice in a row to remove
> multiple highlights.

#### `void TriggerAddHighlight(int nVisualEffect = VFX_DUR_ETHEREAL_VISAGE, int nDurationType = DURATION_TYPE_TEMPORARY, float fDuration = 10.0f)`
> THIS FUNCTION INTENDED FOR USE IN OnEntered SCRIPT FOR A TRIGGER.
> Add a highlight to the nearest object with the same tag
> as the trigger when a PC enters the trigger area.
> See comments to AddHighlight for suggested highlight effects.

#### `void TriggerRemoveHighlight(int nVisualEffect = VFX_DUR_ETHEREAL_VISAGE)`
> THIS FUNCTION INTENDED FOR USE IN OnExited SCRIPT FOR A TRIGGER.
> Remove the highlight from the nearest object with the same tag
> as the trigger when a PC exits the trigger area.
