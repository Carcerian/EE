# `x0_i0_deckmany.nss`

Source: `NSS/x0_/x0_i0_deckmany.nss`  
31 functions · 3 constants

## Constants

| Constant | Type | Value | Note |
|---|---|---|---|
| `TOKEN_NAME` | int | `9323` |  |
| `TOKEN_CARD_NAME` | int | `9324` |  |
| `DECK_DELAY` | float | `8.0` |  |

## Functions

#### `int GetHasUsedDeck(object oCaster)`
> Check if the deck has been used before by this creature

#### `void SetHasUsedDeck(object oCaster)`
> Mark that the deck has been used by this creature

#### `int GetNumberDeckDraws(object oCaster)`
> Get the number of draws remaining

#### `void SetNumberDeckDraws(object oCaster, int nDraws)`
> Set the number of draws remaining

#### `void DoDeckDrawPositive(object oCaster, int nTurn = 0)`
> Do a positive card draw

#### `void DoDeckDrawNegative(object oCaster, int nTurn = 0)`
> Do a negative card draw

#### `object GetSpecialAreaForDeckCard(string sAreaTag)`
> Get a special deck-specific area if it exists and is available.
> This will start by checking for an area with just the given area
> tag. If that doesn't exist or is taken, it will start looking
> for areas tagged sAreaTag + number, until it finds one that is available.
> X0_DECK_DONJON1, X0_DECK_DONJON2, etc
> Returns OBJECT_INVALID if no area found.

#### `int DoSpecialAreaDeckCard(object oCaster, string sAreaTag, int nTurn = 0)`
> Get a special area and transport the caster (with
> associates but without party members) to the
> X0_DECK_START waypoint inside it.
> Returns TRUE on success, FALSE otherwise.

#### `int DoFoolDeckCard(object oCaster, int nTurn = 0)`
> The Fool card (negative)
> Lose 10,000 XP and get 2 extra cards.

#### `int DoDonjonDeckCard(object oCaster, int nTurn = 0)`
> The Donjon card (negative)
> If a donjon area is available, the caster and associates are transported
> there.
> The area should be tagged X0_DECK_DONJON1.
> The starting location should be tagged X0_DECK_START.
> See the Gauntlet area in module 3 of XP1 as an example.
> (This is a good model to use if you want to create a "Keep" or
> "Void" type card for your own module.)

#### `int DoTraitorDeckCard(object oCaster, int nTurn = 0)`
> The Traitor card (negative)
> Change to diametrically-opposed alignment instantly.

#### `int DoKnaveDeckCard(object oCaster, int nTurn = 0)`
> The Knave card (negative)
> All non-plot possessions not currently equipped are destroyed.

#### `int DoPlagueDeckCard(object oCaster, int nTurn = 0)`
> The Plague card (negative)
> Permanent disease effect applied for duration of the module.

#### `int DoLookingGlassDeckCard(object oCaster, int nTurn = 0)`
> The Looking Glass card (negative)
> Caster's henchman is replaced with an evil doppelganger.

#### `int DoWyrmDeckCard(object oCaster, int nTurn = 0)`
> The Wyrm card (negative)
> A hostile ancient dragon is lured to the caster.

#### `int DoJokerDeckCard(object oCaster, int nTurn = 0)`
> The Joker card (positive)
> Gain 10,000 XP and get 2 extra cards.

#### `int DoHoardDeckCard(object oCaster, int nTurn = 0)`
> The Hoard card (positive)
> Gain 50-100,000 gold instantly

#### `int DoOracleDeckCard(object oCaster, int nTurn = 0)`
> The Oracle card (positive)
> Gain permanent premonition effect for duration of the module

#### `int DoAvatarDeckCard(object oCaster, int nTurn = 0)`
> The Avatar card (positive)
> Caster is transformed into an avatar of their alignment.

#### `int DoFountainDeckCard(object oCaster, int nTurn = 0)`
> The Fountain card (positive)
> All of caster's items are recharged and all stacked items are
> filled up to the maximum possible number.

#### `int DoHatchlingDeckCard(object oCaster, int nTurn = 0)`
> The Hatchling card (positive)
> A wyrmling of alignment-appropriate color appears and follows
> the caster as a summoned creature until damaged, at which point
> it transforms into an adult dragon and fights on the caster's behalf
> until all enemies are slain, then vanishes.

#### `int DoBequestDeckCard(object oCaster, int nTurn = 0)`
> The Bequest card (positive)
> Gain a major unique magical item (this will respect the
> XP1 treasure system if it is used in the module, otherwise
> random boss-level treasure will be generated).

#### `object GetSpecialAreaForDeck(string sAreaTag)`
> Get a special deck-specific area if it exists and is available.
> This will start by checking for an area with just the given area
> tag. If that doesn't exist or is taken, it will start looking
> for areas tagged sAreaTag + number, until it finds one that is available.
> X0_DECK_DONJON1, X0_DECK_DONJON2, etc
> Returns OBJECT_INVALID if no area found.

#### `void DoPlagueDeckCardEffect(object oCaster)`
> Private function used to apply the initial plague effect

#### `void DoLookingGlassDeckCardEffect(object oCaster, object oHench)`
> Private function to run the actual henchman change after a delay

#### `void DoWyrmDeckCardEffect(object oCaster, string sResRef)`
> Private function to run the actual wyrm summon after a delay

#### `void DoAvatarDeckCardEffect(object oCaster)`
> Private function to create the avatar item on the caster

#### `void DoAvatarDeckCardTransform(object oCaster)`
> Private function to do the avatar transformation effect

#### `void DoHatchlingDeckCardEffect(object oCaster)`
> Private function used to create the hatchling-summoning object

#### `void DoHatchlingDeckCardRecord(string sTag)`
> Private function used to record the hatchling object

#### `void DoHatchlingDeckCardSummon()`
> Private function -- this is assigned to the caster as an action
> to cause them to summon the hatchling.
