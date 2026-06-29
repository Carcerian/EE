# `x0_i0_match.nss`

Source: `NSS/x0_/x0_i0_match.nss`  
20 functions · 2 constants

## Constants

| Constant | Type | Value | Note |
|---|---|---|---|
| `NW_TALENT_PROTECT` | int | `1` |  |
| `NW_TALENT_ENHANCE` | int | `2` |  |

## Functions

#### `int GetMatchCompatibility(talent tUse, string sClass, int nType)`
> Used to break protections into 3 categories:
> COMBAT, SPELL and ELEMENTAL.
> sClass should be one of: FIGHTER, CLERIC, MAGE, MONSTER
> nType should always be:  NW_TALENT_PROTECT

#### `int MatchDoIHaveAMindAffectingSpellOnMe(object oTarget)`
> Do I have any effect on me that came from a mind affecting spell?

#### `int MatchAreaOfEffectSpell(int nSpell)`
> if the passed in spell is an area of effect spell of any kind

#### `int MatchCombatProtections(talent tUse)`
> Is this spell a combat protection spells?

#### `int MatchSpellProtections(talent tUse)`
> Is this talent a protection against spells?

#### `int MatchElementalProtections(talent tUse)`
> Is this talent a protection against elemental damage?

#### `int MatchSingleHandedWeapon(object oItem)`
> Is this item a single-handed weapon?

#### `int MatchDoubleHandedWeapon(object oItem)`
> TRUE if the item is a double-handed weapon

#### `int MatchMeleeWeapon(object oItem)`
> TRUE if the item is a melee weapon

#### `int MatchShield(object oItem)`
> TRUE if the item is a shield

#### `int MatchCrossbow(object oItem)`
> True if the item is a crossbow

#### `int MatchNormalBow(object oItem)`
> True if the item is a longbow or shortbow

#### `int MatchMindAffectingSpells(int iSpell)`
> is this a mind affecting spell?

#### `int MatchPersonSpells(int iSpell)`
> is this a charm type spell?

#### `int MatchInflictTouchAttack(int nSpell)`
> True if this spell is one of the Reverse Healing touch Attacks

#### `int MatchNonliving(int nRacialType)`
> True if the creature is an elemental, undead, or golem

#### `int VerifyDisarm(talent tUse, object oTarget)`
> Checks that the melee talent being used
> is Disarm and if so then if the target has a
> weapon.
> This should return TRUE if:
> - we are not trying to use disarm
> - we are using disarm appropriately
> This should return FALSE if:
> - we are trying to use disarm on an inappropriate target
> - we are using disarm too frequently
> If this returns FALSE, we will fall back to a standard
> melee attack instead.

#### `int VerifyCombatMeleeTalent(talent tUse, object oTarget)`
> Makes sure that certain talents are not used
> on Elementals, Undead or Constructs

#### `int GetHasEffect(int nEffectType, object oTarget = OBJECT_SELF)`
> Checks the target for a specific EFFECT_TYPE constant value

#### `int GetRemovalSpell()`
> Returns a potential removal spell that might be useful in this situation
