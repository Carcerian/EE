# `x0_i0_infdesert.nss`

Source: `NSS/x0_/x0_i0_infdesert.nss`  
13 functions · 25 constants

## Constants

| Constant | Type | Value | Note |
|---|---|---|---|
| `INF_BASE` | string | `"INF_DESERT"` |  |
| `INF_ENCOUNTER` | string | `INF_BASE + "_ENCOUNTER"` |  |
| `INF_MAX_RUN_LENGTH` | int | `3` |  |
| `INF_MIN_RUN_LENGTH` | int | `2` |  |
| `MIN_HD_FOR_BOSS` | int | `6` |  |
| `ENCOUNTER_WOLF` | string | `"nw_wolf\|nw_dog\|nw_direwolf\|nw_wolfdireboss+2+5"` |  |
| `ENCOUNTER_CAT` | string | `"nw_cougar\|nw_cragcat\|nw_beastmalar001\|nw_panther\|nw_cougar+2+5"` |  |
| `ENCOUNTER_EARTH_ELEM` | string | `"nw_earth\|NOBOSS+1+3"` |  |
| `ENCOUNTER_HUMANOID` | string | `"nw_goblina\|nw_goblinb\|nw_gobchiefb\|nw_orca\|nw_orcchiefa\|nw_gobwiza+3+6"` |  |
| `ENCOUNTER_ASABI1` | string | `"x0_asabi_warrior\|x0_asabi_chief+2+3"` |  |
| `ENCOUNTER_ASABI2` | string | `"x0_asabi_warrior\|x0_asabi_shaman+2+3"` |  |
| `ENCOUNTER_BEETLE` | string | `"nw_btlfire\|nw_btlfire02\|nw_btlbomb\|NOBOSS+4+6"` |  |
| `ENCOUNTER_BASILISK` | string | `"x0_basilisk\|NOBOSS+1+1"` |  |
| `ENCOUNTER_COCKATRICE` | string | `"x0_cockatrice\|NOBOSS+1+1"` |  |
| `ENCOUNTER_GORGON` | string | `"x0_gorgon\|NOBOSS+1+1"` |  |
| `ENCOUNTER_STINGER` | string | `"x0_stinger\|x0_stinger_war\|x0_stinger_mage\|x0_stinger_chief+2+4"` |  |
| `ENCOUNTER_WILLOWISP` | string | `"nw_willowisp\|NOBOSS+1+1"` |  |
| `ENCOUNTER_FORMIAN` | string | `"x0_form_warrior\|x0_form_worker\|x0_form_taskmast+2+5"` |  |
| `ENCOUNTER_WERECAT` | string | `"nw_werecat001\|NOBOSS+2+4"` |  |
| `ENCOUNTER_MUMMY` | string | `"nw_mummy\|nw_mumcleric\|nw_mumfight\|NOBOSS+1+3"` |  |
| `ENCOUNTER_UNDEAD` | string | `"nw_shadow\|nw_shfiend\|nw_skeleton\|nw_skelwarr01\|nw_ghast\|nw_ghoul\|NOBOSS+3+5"` |  |
| `ENCOUNTER_BANDIT` | string | `"nw_bandit001\|nw_bandit002\|nw_bandit003\|NOBOSS+3+5"` |  |
| `ENCOUNTER_MERC` | string | `"nw_halfmerc001\|nw_dwarfmerc001\|nw_humanmerc002\|nw_elfmerc001\|NOBOSS+3+6"` |  |
| `ENCOUNTER_ZHENT` | string | `"zhentarimcleric\|zhentarimclrf2\|zhentarimguard\|zhentarimguar007\|zhentarimmage003\|zhentarimmage\|zhentarimguar001\|zhentarimguar008+4+6"` |  |
| `ENCOUNTER_HUMANOID2` | string | `"nw_goblina\|nw_goblinb\|nw_gobchiefb\|nw_gobwiza+6+8"` |  |

## Functions

#### `void INF_CreateRandomEncounter(object oArea, object oPC)`
> Create a random encounter in the specified area, possibly based
> on the PC's characteristics.

#### `void INF_CreateRandomPlaceables(object oArea, object oPC)`
> Create random decorative placeables in the specified area.

#### `string INF_GetEntryMessage()`
> Message sent to the player the first time they enter an
> infinite area.

#### `string INF_GetReentryMessage()`
> The message sent to the player when they re-enter an
> infinite area that they've been to before.

#### `string INF_GetReachStartMessage()`
> Message sent to PC when they get dropped back to the starting
> point from within the desert for the first time.

#### `string INF_GetReturnToStartMessage()`
> Message sent to PC when they get dropped back to the starting
> point after the first time.

#### `string INF_GetReachRewardMessage()`
> Message sent to PC when they reach the reward area of the infinite
> run for the first time.

#### `string INF_GetReturnToRewardMessage()`
> Message sent to PC when they reach the reward area of the infinite
> run on a subsequent re-entry.

#### `string INF_GetPoolEmptyMessage()`
> Message sent to PC in the case where the pool of generic areas
> is empty and no new area can be allocated. This should happen
> very rarely, and the result will be that the PC is returned to
> the starting point.

#### `string INF_GetNeedKeyMessage()`
> Message sent to PC when they would reach the reward area but don't
> have the key.

#### `string INF_GetNoStartMessage()`
> Message sent to PC when no starting marker is available, which
> means they can't enter the desert. This should only happen if
> the modmaker has forgotten to put down a starting marker!

#### `string PickRandomEncounter()`
> Randomly selects one of the encounter lists above

#### `void CreateEncounterGroup(location locEnc, object oPC)`
> This takes a string for an encounter type (eg, ENCOUNTER_WOLF)
> that is a pipe-delimited list of creature blueprints. It will
> randomly generate the specified number of creatures out of the
> list and create them in the given location.
> The last two entries in the list after the + symbol are the
> min/max number of creatures to generate.
> The last blueprint in a list is the boss. (To make a list
> with no boss, simply repeat one creature at the end.) Bosses will
> be unique and will show up randomly, if the given PC has HD lower
> than the minimum hit dice required.
> Each creature in the list will have an equal chance of showing up.
> Each creature will have the ambient animations spawn-in condition
> set to make them wander about.
