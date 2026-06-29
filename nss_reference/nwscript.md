# `nwscript.nss`

Source: `NSS/nwscript.nss`  
1187 functions · 6279 constants

## Constants

| Constant | Type | Value | Note |
|---|---|---|---|
| `NUM_INVENTORY_SLOTS` | int | `18` |  |
| `TRUE` | int | `1` |  |
| `FALSE` | int | `0` |  |
| `DIRECTION_EAST` | float | `0.0` |  |
| `DIRECTION_NORTH` | float | `90.0` |  |
| `DIRECTION_WEST` | float | `180.0` |  |
| `DIRECTION_SOUTH` | float | `270.0` |  |
| `PI` | float | `3.141592` |  |
| `ATTITUDE_NEUTRAL` | int | `0` |  |
| `ATTITUDE_AGGRESSIVE` | int | `1` |  |
| `ATTITUDE_DEFENSIVE` | int | `2` |  |
| `ATTITUDE_SPECIAL` | int | `3` |  |
| `TALKVOLUME_TALK` | int | `0` |  |
| `TALKVOLUME_WHISPER` | int | `1` |  |
| `TALKVOLUME_SHOUT` | int | `2` |  |
| `TALKVOLUME_SILENT_TALK` | int | `3` |  |
| `TALKVOLUME_SILENT_SHOUT` | int | `4` |  |
| `TALKVOLUME_PARTY` | int | `5` |  |
| `TALKVOLUME_TELL` | int | `6` |  |
| `INVENTORY_SLOT_HEAD` | int | `0` |  |
| `INVENTORY_SLOT_CHEST` | int | `1` |  |
| `INVENTORY_SLOT_BOOTS` | int | `2` |  |
| `INVENTORY_SLOT_ARMS` | int | `3` |  |
| `INVENTORY_SLOT_RIGHTHAND` | int | `4` |  |
| `INVENTORY_SLOT_LEFTHAND` | int | `5` |  |
| `INVENTORY_SLOT_CLOAK` | int | `6` |  |
| `INVENTORY_SLOT_LEFTRING` | int | `7` |  |
| `INVENTORY_SLOT_RIGHTRING` | int | `8` |  |
| `INVENTORY_SLOT_NECK` | int | `9` |  |
| `INVENTORY_SLOT_BELT` | int | `10` |  |
| `INVENTORY_SLOT_ARROWS` | int | `11` |  |
| `INVENTORY_SLOT_BULLETS` | int | `12` |  |
| `INVENTORY_SLOT_BOLTS` | int | `13` |  |
| `INVENTORY_SLOT_CWEAPON_L` | int | `14` |  |
| `INVENTORY_SLOT_CWEAPON_R` | int | `15` |  |
| `INVENTORY_SLOT_CWEAPON_B` | int | `16` |  |
| `INVENTORY_SLOT_CARMOUR` | int | `17` |  |
| `DURATION_TYPE_INSTANT` | int | `0` |  |
| `DURATION_TYPE_TEMPORARY` | int | `1` |  |
| `DURATION_TYPE_PERMANENT` | int | `2` |  |
| `SUBTYPE_MAGICAL` | int | `8` |  |
| `SUBTYPE_SUPERNATURAL` | int | `16` |  |
| `SUBTYPE_EXTRAORDINARY` | int | `24` |  |
| `SUBTYPE_UNYIELDING` | int | `32` |  |
| `ABILITY_STRENGTH` | int | `0` | should be the same as in nwseffectlist.cpp |
| `ABILITY_DEXTERITY` | int | `1` |  |
| `ABILITY_CONSTITUTION` | int | `2` |  |
| `ABILITY_INTELLIGENCE` | int | `3` |  |
| `ABILITY_WISDOM` | int | `4` |  |
| `ABILITY_CHARISMA` | int | `5` |  |
| `SHAPE_SPELLCYLINDER` | int | `0` |  |
| `SHAPE_CONE` | int | `1` |  |
| `SHAPE_CUBE` | int | `2` |  |
| `SHAPE_SPELLCONE` | int | `3` |  |
| `SHAPE_SPHERE` | int | `4` |  |
| `METAMAGIC_NONE` | int | `0` |  |
| `METAMAGIC_EMPOWER` | int | `1` |  |
| `METAMAGIC_EXTEND` | int | `2` |  |
| `METAMAGIC_MAXIMIZE` | int | `4` |  |
| `METAMAGIC_QUICKEN` | int | `8` |  |
| `METAMAGIC_SILENT` | int | `16` |  |
| `METAMAGIC_STILL` | int | `32` |  |
| `METAMAGIC_ANY` | int | `255` |  |
| `OBJECT_TYPE_CREATURE` | int | `1` |  |
| `OBJECT_TYPE_ITEM` | int | `2` |  |
| `OBJECT_TYPE_TRIGGER` | int | `4` |  |
| `OBJECT_TYPE_DOOR` | int | `8` |  |
| `OBJECT_TYPE_AREA_OF_EFFECT` | int | `16` |  |
| `OBJECT_TYPE_WAYPOINT` | int | `32` |  |
| `OBJECT_TYPE_PLACEABLE` | int | `64` |  |
| `OBJECT_TYPE_STORE` | int | `128` |  |
| `OBJECT_TYPE_ENCOUNTER` | int | `256` |  |
| `OBJECT_TYPE_TILE` | int | `512` |  |
| `OBJECT_TYPE_ALL` | int | `32767` |  |
| `OBJECT_TYPE_INVALID` | int | `32767` |  |
| `GENDER_MALE` | int | `0` |  |
| `GENDER_FEMALE` | int | `1` |  |
| `GENDER_BOTH` | int | `2` |  |
| `GENDER_OTHER` | int | `3` |  |
| `GENDER_NONE` | int | `4` |  |
| `DAMAGE_TYPE_BLUDGEONING` | int | `1` |  |
| `DAMAGE_TYPE_PIERCING` | int | `2` |  |
| `DAMAGE_TYPE_SLASHING` | int | `4` |  |
| `DAMAGE_TYPE_MAGICAL` | int | `8` |  |
| `DAMAGE_TYPE_ACID` | int | `16` |  |
| `DAMAGE_TYPE_COLD` | int | `32` |  |
| `DAMAGE_TYPE_DIVINE` | int | `64` |  |
| `DAMAGE_TYPE_ELECTRICAL` | int | `128` |  |
| `DAMAGE_TYPE_FIRE` | int | `256` |  |
| `DAMAGE_TYPE_NEGATIVE` | int | `512` |  |
| `DAMAGE_TYPE_POSITIVE` | int | `1024` |  |
| `DAMAGE_TYPE_SONIC` | int | `2048` |  |
| `DAMAGE_TYPE_BASE_WEAPON` | int | `4096` |  |
| `DAMAGE_TYPE_CUSTOM1` | int | `8192` |  |
| `DAMAGE_TYPE_CUSTOM2` | int | `16384` |  |
| `DAMAGE_TYPE_CUSTOM3` | int | `32768` |  |
| `DAMAGE_TYPE_CUSTOM4` | int | `65536` |  |
| `DAMAGE_TYPE_CUSTOM5` | int | `131072` |  |
| `DAMAGE_TYPE_CUSTOM6` | int | `262144` |  |
| `DAMAGE_TYPE_CUSTOM7` | int | `524288` |  |
| `DAMAGE_TYPE_CUSTOM8` | int | `1048576` |  |
| `DAMAGE_TYPE_CUSTOM9` | int | `2097152` |  |
| `DAMAGE_TYPE_CUSTOM10` | int | `4194304` |  |
| `DAMAGE_TYPE_CUSTOM11` | int | `8388608` |  |
| `DAMAGE_TYPE_CUSTOM12` | int | `16777216` |  |
| `DAMAGE_TYPE_CUSTOM13` | int | `33554432` |  |
| `DAMAGE_TYPE_CUSTOM14` | int | `67108864` |  |
| `DAMAGE_TYPE_CUSTOM15` | int | `134217728` |  |
| `DAMAGE_TYPE_CUSTOM16` | int | `268435456` |  |
| `DAMAGE_TYPE_CUSTOM17` | int | `536870912` |  |
| `DAMAGE_TYPE_CUSTOM18` | int | `1073741824` |  |
| `DAMAGE_TYPE_CUSTOM19` | int | `2147483648` |  |
| `AC_VS_DAMAGE_TYPE_ALL` | int | `4103` |  |
| `DAMAGE_BONUS_1` | int | `1` |  |
| `DAMAGE_BONUS_2` | int | `2` |  |
| `DAMAGE_BONUS_3` | int | `3` |  |
| `DAMAGE_BONUS_4` | int | `4` |  |
| `DAMAGE_BONUS_5` | int | `5` |  |
| `DAMAGE_BONUS_1d4` | int | `6` |  |
| `DAMAGE_BONUS_1d6` | int | `7` |  |
| `DAMAGE_BONUS_1d8` | int | `8` |  |
| `DAMAGE_BONUS_1d10` | int | `9` |  |
| `DAMAGE_BONUS_2d6` | int | `10` |  |
| `DAMAGE_BONUS_2d8` | int | `11` |  |
| `DAMAGE_BONUS_2d4` | int | `12` |  |
| `DAMAGE_BONUS_2d10` | int | `13` |  |
| `DAMAGE_BONUS_1d12` | int | `14` |  |
| `DAMAGE_BONUS_2d12` | int | `15` |  |
| `DAMAGE_BONUS_6` | int | `16` |  |
| `DAMAGE_BONUS_7` | int | `17` |  |
| `DAMAGE_BONUS_8` | int | `18` |  |
| `DAMAGE_BONUS_9` | int | `19` |  |
| `DAMAGE_BONUS_10` | int | `20` |  |
| `DAMAGE_BONUS_11` | int | `21` |  |
| `DAMAGE_BONUS_12` | int | `22` |  |
| `DAMAGE_BONUS_13` | int | `23` |  |
| `DAMAGE_BONUS_14` | int | `24` |  |
| `DAMAGE_BONUS_15` | int | `25` |  |
| `DAMAGE_BONUS_16` | int | `26` |  |
| `DAMAGE_BONUS_17` | int | `27` |  |
| `DAMAGE_BONUS_18` | int | `28` |  |
| `DAMAGE_BONUS_19` | int | `29` |  |
| `DAMAGE_BONUS_20` | int | `30` |  |
| `DAMAGE_POWER_NORMAL` | int | `0` |  |
| `DAMAGE_POWER_PLUS_ONE` | int | `1` |  |
| `DAMAGE_POWER_PLUS_TWO` | int | `2` |  |
| `DAMAGE_POWER_PLUS_THREE` | int | `3` |  |
| `DAMAGE_POWER_PLUS_FOUR` | int | `4` |  |
| `DAMAGE_POWER_PLUS_FIVE` | int | `5` |  |
| `DAMAGE_POWER_ENERGY` | int | `6` |  |
| `DAMAGE_POWER_PLUS_SIX` | int | `7` |  |
| `DAMAGE_POWER_PLUS_SEVEN` | int | `8` |  |
| `DAMAGE_POWER_PLUS_EIGHT` | int | `9` |  |
| `DAMAGE_POWER_PLUS_NINE` | int | `10` |  |
| `DAMAGE_POWER_PLUS_TEN` | int | `11` |  |
| `DAMAGE_POWER_PLUS_ELEVEN` | int | `12` |  |
| `DAMAGE_POWER_PLUS_TWELVE` | int | `13` |  |
| `DAMAGE_POWER_PLUS_THIRTEEN` | int | `14` |  |
| `DAMAGE_POWER_PLUS_FOURTEEN` | int | `15` |  |
| `DAMAGE_POWER_PLUS_FIFTEEN` | int | `16` |  |
| `DAMAGE_POWER_PLUS_SIXTEEN` | int | `17` |  |
| `DAMAGE_POWER_PLUS_SEVENTEEN` | int | `18` |  |
| `DAMAGE_POWER_PLUS_EIGHTEEN` | int | `19` |  |
| `DAMAGE_POWER_PLUS_NINTEEN` | int | `20` |  |
| `DAMAGE_POWER_PLUS_TWENTY` | int | `21` |  |
| `ATTACK_BONUS_MISC` | int | `0` |  |
| `ATTACK_BONUS_ONHAND` | int | `1` |  |
| `ATTACK_BONUS_OFFHAND` | int | `2` |  |
| `AC_DODGE_BONUS` | int | `0` |  |
| `AC_NATURAL_BONUS` | int | `1` |  |
| `AC_ARMOUR_ENCHANTMENT_BONUS` | int | `2` |  |
| `AC_SHIELD_ENCHANTMENT_BONUS` | int | `3` |  |
| `AC_DEFLECTION_BONUS` | int | `4` |  |
| `MISS_CHANCE_TYPE_NORMAL` | int | `0` |  |
| `MISS_CHANCE_TYPE_VS_RANGED` | int | `1` |  |
| `MISS_CHANCE_TYPE_VS_MELEE` | int | `2` |  |
| `DOOR_ACTION_OPEN` | int | `0` |  |
| `DOOR_ACTION_UNLOCK` | int | `1` |  |
| `DOOR_ACTION_BASH` | int | `2` |  |
| `DOOR_ACTION_IGNORE` | int | `3` |  |
| `DOOR_ACTION_KNOCK` | int | `4` |  |
| `PLACEABLE_ACTION_USE` | int | `0` |  |
| `PLACEABLE_ACTION_UNLOCK` | int | `1` |  |
| `PLACEABLE_ACTION_BASH` | int | `2` |  |
| `PLACEABLE_ACTION_KNOCK` | int | `4` |  |
| `RACIAL_TYPE_DWARF` | int | `0` |  |
| `RACIAL_TYPE_ELF` | int | `1` |  |
| `RACIAL_TYPE_GNOME` | int | `2` |  |
| `RACIAL_TYPE_HALFLING` | int | `3` |  |
| `RACIAL_TYPE_HALFELF` | int | `4` |  |
| `RACIAL_TYPE_HALFORC` | int | `5` |  |
| `RACIAL_TYPE_HUMAN` | int | `6` |  |
| `RACIAL_TYPE_ABERRATION` | int | `7` |  |
| `RACIAL_TYPE_ANIMAL` | int | `8` |  |
| `RACIAL_TYPE_BEAST` | int | `9` |  |
| `RACIAL_TYPE_CONSTRUCT` | int | `10` |  |
| `RACIAL_TYPE_DRAGON` | int | `11` |  |
| `RACIAL_TYPE_HUMANOID_GOBLINOID` | int | `12` |  |
| `RACIAL_TYPE_HUMANOID_MONSTROUS` | int | `13` |  |
| `RACIAL_TYPE_HUMANOID_ORC` | int | `14` |  |
| `RACIAL_TYPE_HUMANOID_REPTILIAN` | int | `15` |  |
| `RACIAL_TYPE_ELEMENTAL` | int | `16` |  |
| `RACIAL_TYPE_FEY` | int | `17` |  |
| `RACIAL_TYPE_GIANT` | int | `18` |  |
| `RACIAL_TYPE_MAGICAL_BEAST` | int | `19` |  |
| `RACIAL_TYPE_OUTSIDER` | int | `20` |  |
| `RACIAL_TYPE_SHAPECHANGER` | int | `23` |  |
| `RACIAL_TYPE_UNDEAD` | int | `24` |  |
| `RACIAL_TYPE_VERMIN` | int | `25` |  |
| `RACIAL_TYPE_ALL` | int | `28` |  |
| `RACIAL_TYPE_INVALID` | int | `28` |  |
| `RACIAL_TYPE_OOZE` | int | `29` |  |
| `ALIGNMENT_ALL` | int | `0` |  |
| `ALIGNMENT_NEUTRAL` | int | `1` |  |
| `ALIGNMENT_LAWFUL` | int | `2` |  |
| `ALIGNMENT_CHAOTIC` | int | `3` |  |
| `ALIGNMENT_GOOD` | int | `4` |  |
| `ALIGNMENT_EVIL` | int | `5` |  |
| `SAVING_THROW_ALL` | int | `0` |  |
| `SAVING_THROW_FORT` | int | `1` |  |
| `SAVING_THROW_REFLEX` | int | `2` |  |
| `SAVING_THROW_WILL` | int | `3` |  |
| `SAVING_THROW_TYPE_ALL` | int | `0` |  |
| `SAVING_THROW_TYPE_NONE` | int | `0` |  |
| `SAVING_THROW_TYPE_MIND_SPELLS` | int | `1` |  |
| `SAVING_THROW_TYPE_POISON` | int | `2` |  |
| `SAVING_THROW_TYPE_DISEASE` | int | `3` |  |
| `SAVING_THROW_TYPE_FEAR` | int | `4` |  |
| `SAVING_THROW_TYPE_SONIC` | int | `5` |  |
| `SAVING_THROW_TYPE_ACID` | int | `6` |  |
| `SAVING_THROW_TYPE_FIRE` | int | `7` |  |
| `SAVING_THROW_TYPE_ELECTRICITY` | int | `8` |  |
| `SAVING_THROW_TYPE_POSITIVE` | int | `9` |  |
| `SAVING_THROW_TYPE_NEGATIVE` | int | `10` |  |
| `SAVING_THROW_TYPE_DEATH` | int | `11` |  |
| `SAVING_THROW_TYPE_COLD` | int | `12` |  |
| `SAVING_THROW_TYPE_DIVINE` | int | `13` |  |
| `SAVING_THROW_TYPE_TRAP` | int | `14` |  |
| `SAVING_THROW_TYPE_SPELL` | int | `15` |  |
| `SAVING_THROW_TYPE_GOOD` | int | `16` |  |
| `SAVING_THROW_TYPE_EVIL` | int | `17` |  |
| `SAVING_THROW_TYPE_LAW` | int | `18` |  |
| `SAVING_THROW_TYPE_CHAOS` | int | `19` |  |
| `SAVING_THROW_TYPE_PARALYSIS` | int | `20` |  |
| `IMMUNITY_TYPE_NONE` | int | `0` |  |
| `IMMUNITY_TYPE_MIND_SPELLS` | int | `1` |  |
| `IMMUNITY_TYPE_POISON` | int | `2` |  |
| `IMMUNITY_TYPE_DISEASE` | int | `3` |  |
| `IMMUNITY_TYPE_FEAR` | int | `4` |  |
| `IMMUNITY_TYPE_TRAP` | int | `5` |  |
| `IMMUNITY_TYPE_PARALYSIS` | int | `6` |  |
| `IMMUNITY_TYPE_BLINDNESS` | int | `7` |  |
| `IMMUNITY_TYPE_DEAFNESS` | int | `8` |  |
| `IMMUNITY_TYPE_SLOW` | int | `9` |  |
| `IMMUNITY_TYPE_ENTANGLE` | int | `10` |  |
| `IMMUNITY_TYPE_SILENCE` | int | `11` |  |
| `IMMUNITY_TYPE_STUN` | int | `12` |  |
| `IMMUNITY_TYPE_SLEEP` | int | `13` |  |
| `IMMUNITY_TYPE_CHARM` | int | `14` |  |
| `IMMUNITY_TYPE_DOMINATE` | int | `15` |  |
| `IMMUNITY_TYPE_CONFUSED` | int | `16` |  |
| `IMMUNITY_TYPE_CURSED` | int | `17` |  |
| `IMMUNITY_TYPE_DAZED` | int | `18` |  |
| `IMMUNITY_TYPE_ABILITY_DECREASE` | int | `19` |  |
| `IMMUNITY_TYPE_ATTACK_DECREASE` | int | `20` |  |
| `IMMUNITY_TYPE_DAMAGE_DECREASE` | int | `21` |  |
| `IMMUNITY_TYPE_DAMAGE_IMMUNITY_DECREASE` | int | `22` |  |
| `IMMUNITY_TYPE_AC_DECREASE` | int | `23` |  |
| `IMMUNITY_TYPE_MOVEMENT_SPEED_DECREASE` | int | `24` |  |
| `IMMUNITY_TYPE_SAVING_THROW_DECREASE` | int | `25` |  |
| `IMMUNITY_TYPE_SPELL_RESISTANCE_DECREASE` | int | `26` |  |
| `IMMUNITY_TYPE_SKILL_DECREASE` | int | `27` |  |
| `IMMUNITY_TYPE_KNOCKDOWN` | int | `28` |  |
| `IMMUNITY_TYPE_NEGATIVE_LEVEL` | int | `29` |  |
| `IMMUNITY_TYPE_SNEAK_ATTACK` | int | `30` |  |
| `IMMUNITY_TYPE_CRITICAL_HIT` | int | `31` |  |
| `IMMUNITY_TYPE_DEATH` | int | `32` |  |
| `AREA_TRANSITION_RANDOM` | int | `0` |  |
| `AREA_TRANSITION_USER_DEFINED` | int | `1` |  |
| `AREA_TRANSITION_CITY_01` | int | `2` |  |
| `AREA_TRANSITION_CITY_02` | int | `3` |  |
| `AREA_TRANSITION_CITY_03` | int | `4` |  |
| `AREA_TRANSITION_CITY_04` | int | `5` |  |
| `AREA_TRANSITION_CITY_05` | int | `6` |  |
| `AREA_TRANSITION_CRYPT_01` | int | `7` |  |
| `AREA_TRANSITION_CRYPT_02` | int | `8` |  |
| `AREA_TRANSITION_CRYPT_03` | int | `9` |  |
| `AREA_TRANSITION_CRYPT_04` | int | `10` |  |
| `AREA_TRANSITION_CRYPT_05` | int | `11` |  |
| `AREA_TRANSITION_DUNGEON_01` | int | `12` |  |
| `AREA_TRANSITION_DUNGEON_02` | int | `13` |  |
| `AREA_TRANSITION_DUNGEON_03` | int | `14` |  |
| `AREA_TRANSITION_DUNGEON_04` | int | `15` |  |
| `AREA_TRANSITION_DUNGEON_05` | int | `16` |  |
| `AREA_TRANSITION_DUNGEON_06` | int | `17` |  |
| `AREA_TRANSITION_DUNGEON_07` | int | `18` |  |
| `AREA_TRANSITION_DUNGEON_08` | int | `19` |  |
| `AREA_TRANSITION_MINES_01` | int | `20` |  |
| `AREA_TRANSITION_MINES_02` | int | `21` |  |
| `AREA_TRANSITION_MINES_03` | int | `22` |  |
| `AREA_TRANSITION_MINES_04` | int | `23` |  |
| `AREA_TRANSITION_MINES_05` | int | `24` |  |
| `AREA_TRANSITION_MINES_06` | int | `25` |  |
| `AREA_TRANSITION_MINES_07` | int | `26` |  |
| `AREA_TRANSITION_MINES_08` | int | `27` |  |
| `AREA_TRANSITION_MINES_09` | int | `28` |  |
| `AREA_TRANSITION_SEWER_01` | int | `29` |  |
| `AREA_TRANSITION_SEWER_02` | int | `30` |  |
| `AREA_TRANSITION_SEWER_03` | int | `31` |  |
| `AREA_TRANSITION_SEWER_04` | int | `32` |  |
| `AREA_TRANSITION_SEWER_05` | int | `33` |  |
| `AREA_TRANSITION_CASTLE_01` | int | `34` |  |
| `AREA_TRANSITION_CASTLE_02` | int | `35` |  |
| `AREA_TRANSITION_CASTLE_03` | int | `36` |  |
| `AREA_TRANSITION_CASTLE_04` | int | `37` |  |
| `AREA_TRANSITION_CASTLE_05` | int | `38` |  |
| `AREA_TRANSITION_CASTLE_06` | int | `39` |  |
| `AREA_TRANSITION_CASTLE_07` | int | `40` |  |
| `AREA_TRANSITION_CASTLE_08` | int | `41` |  |
| `AREA_TRANSITION_INTERIOR_01` | int | `42` |  |
| `AREA_TRANSITION_INTERIOR_02` | int | `43` |  |
| `AREA_TRANSITION_INTERIOR_03` | int | `44` |  |
| `AREA_TRANSITION_INTERIOR_04` | int | `45` |  |
| `AREA_TRANSITION_INTERIOR_05` | int | `46` |  |
| `AREA_TRANSITION_INTERIOR_06` | int | `47` |  |
| `AREA_TRANSITION_INTERIOR_07` | int | `48` |  |
| `AREA_TRANSITION_INTERIOR_08` | int | `49` |  |
| `AREA_TRANSITION_INTERIOR_09` | int | `50` |  |
| `AREA_TRANSITION_INTERIOR_10` | int | `51` |  |
| `AREA_TRANSITION_INTERIOR_11` | int | `52` |  |
| `AREA_TRANSITION_INTERIOR_12` | int | `53` |  |
| `AREA_TRANSITION_INTERIOR_13` | int | `54` |  |
| `AREA_TRANSITION_INTERIOR_14` | int | `55` |  |
| `AREA_TRANSITION_INTERIOR_15` | int | `56` |  |
| `AREA_TRANSITION_INTERIOR_16` | int | `57` |  |
| `AREA_TRANSITION_FOREST_01` | int | `58` |  |
| `AREA_TRANSITION_FOREST_02` | int | `59` |  |
| `AREA_TRANSITION_FOREST_03` | int | `60` |  |
| `AREA_TRANSITION_FOREST_04` | int | `61` |  |
| `AREA_TRANSITION_FOREST_05` | int | `62` |  |
| `AREA_TRANSITION_RURAL_01` | int | `63` |  |
| `AREA_TRANSITION_RURAL_02` | int | `64` |  |
| `AREA_TRANSITION_RURAL_03` | int | `65` |  |
| `AREA_TRANSITION_RURAL_04` | int | `66` |  |
| `AREA_TRANSITION_RURAL_05` | int | `67` |  |
| `AREA_TRANSITION_WRURAL_01` | int | `68` |  |
| `AREA_TRANSITION_WRURAL_02` | int | `69` |  |
| `AREA_TRANSITION_WRURAL_03` | int | `70` |  |
| `AREA_TRANSITION_WRURAL_04` | int | `71` |  |
| `AREA_TRANSITION_WRURAL_05` | int | `72` |  |
| `AREA_TRANSITION_DESERT_01` | int | `73` |  |
| `AREA_TRANSITION_DESERT_02` | int | `74` |  |
| `AREA_TRANSITION_DESERT_03` | int | `75` |  |
| `AREA_TRANSITION_DESERT_04` | int | `76` |  |
| `AREA_TRANSITION_DESERT_05` | int | `77` |  |
| `AREA_TRANSITION_RUINS_01` | int | `78` |  |
| `AREA_TRANSITION_RUINS_02` | int | `79` |  |
| `AREA_TRANSITION_RUINS_03` | int | `80` |  |
| `AREA_TRANSITION_RUINS_04` | int | `81` |  |
| `AREA_TRANSITION_RUINS_05` | int | `82` |  |
| `AREA_TRANSITION_CARAVAN_WINTER` | int | `83` |  |
| `AREA_TRANSITION_CARAVAN_DESERT` | int | `84` |  |
| `AREA_TRANSITION_CARAVAN_RURAL` | int | `85` |  |
| `AREA_TRANSITION_MAGICAL_01` | int | `86` |  |
| `AREA_TRANSITION_MAGICAL_02` | int | `87` |  |
| `AREA_TRANSITION_UNDERDARK_01` | int | `88` |  |
| `AREA_TRANSITION_UNDERDARK_02` | int | `89` |  |
| `AREA_TRANSITION_UNDERDARK_03` | int | `90` |  |
| `AREA_TRANSITION_UNDERDARK_04` | int | `91` |  |
| `AREA_TRANSITION_UNDERDARK_05` | int | `92` |  |
| `AREA_TRANSITION_UNDERDARK_06` | int | `93` |  |
| `AREA_TRANSITION_UNDERDARK_07` | int | `94` |  |
| `AREA_TRANSITION_BEHOLDER_01` | int | `95` |  |
| `AREA_TRANSITION_BEHOLDER_02` | int | `96` |  |
| `AREA_TRANSITION_DROW_01` | int | `97` |  |
| `AREA_TRANSITION_DROW_02` | int | `98` |  |
| `AREA_TRANSITION_ILLITHID_01` | int | `99` |  |
| `AREA_TRANSITION_ILLITHID_02` | int | `100` |  |
| `AREA_TRANSITION_WASTELAND_01` | int | `101` |  |
| `AREA_TRANSITION_WASTELAND_02` | int | `102` |  |
| `AREA_TRANSITION_WASTELAND_03` | int | `103` |  |
| `AREA_TRANSITION_DROW_03` | int | `104` |  |
| `AREA_TRANSITION_DROW_04` | int | `105` |  |
| `AREA_TRANSITION_CITY` | int | `2` |  |
| `AREA_TRANSITION_CRYPT` | int | `7` |  |
| `AREA_TRANSITION_FOREST` | int | `58` |  |
| `AREA_TRANSITION_RURAL` | int | `63` |  |
| `BODY_NODE_HAND` | int | `0` |  |
| `BODY_NODE_CHEST` | int | `1` |  |
| `BODY_NODE_MONSTER_0` | int | `2` |  |
| `BODY_NODE_MONSTER_1` | int | `3` |  |
| `BODY_NODE_MONSTER_2` | int | `4` |  |
| `BODY_NODE_MONSTER_3` | int | `5` |  |
| `BODY_NODE_MONSTER_4` | int | `6` |  |
| `BODY_NODE_MONSTER_5` | int | `7` |  |
| `BODY_NODE_MONSTER_6` | int | `8` |  |
| `BODY_NODE_MONSTER_7` | int | `9` |  |
| `BODY_NODE_MONSTER_8` | int | `10` |  |
| `BODY_NODE_MONSTER_9` | int | `11` |  |
| `RADIUS_SIZE_SMALL` | float | `1.67f` |  |
| `RADIUS_SIZE_MEDIUM` | float | `3.33f` |  |
| `RADIUS_SIZE_LARGE` | float | `5.0f` |  |
| `RADIUS_SIZE_HUGE` | float | `6.67f` |  |
| `RADIUS_SIZE_GARGANTUAN` | float | `8.33f` |  |
| `RADIUS_SIZE_COLOSSAL` | float | `10.0f` |  |
| `EFFECT_TYPE_INVALIDEFFECT` | int | `0` |  |
| `EFFECT_TYPE_DAMAGE_RESISTANCE` | int | `1` |  |
| `EFFECT_TYPE_REGENERATE` | int | `3` |  |
| `EFFECT_TYPE_DAMAGE_REDUCTION` | int | `7` |  |
| `EFFECT_TYPE_TEMPORARY_HITPOINTS` | int | `9` |  |
| `EFFECT_TYPE_ENTANGLE` | int | `11` |  |
| `EFFECT_TYPE_INVULNERABLE` | int | `12` |  |
| `EFFECT_TYPE_DEAF` | int | `13` |  |
| `EFFECT_TYPE_RESURRECTION` | int | `14` |  |
| `EFFECT_TYPE_IMMUNITY` | int | `15` |  |
| `EFFECT_TYPE_ENEMY_ATTACK_BONUS` | int | `17` |  |
| `EFFECT_TYPE_ARCANE_SPELL_FAILURE` | int | `18` |  |
| `EFFECT_TYPE_AREA_OF_EFFECT` | int | `20` |  |
| `EFFECT_TYPE_BEAM` | int | `21` |  |
| `EFFECT_TYPE_CHARMED` | int | `23` |  |
| `EFFECT_TYPE_CONFUSED` | int | `24` |  |
| `EFFECT_TYPE_FRIGHTENED` | int | `25` |  |
| `EFFECT_TYPE_DOMINATED` | int | `26` |  |
| `EFFECT_TYPE_PARALYZE` | int | `27` |  |
| `EFFECT_TYPE_DAZED` | int | `28` |  |
| `EFFECT_TYPE_STUNNED` | int | `29` |  |
| `EFFECT_TYPE_SLEEP` | int | `30` |  |
| `EFFECT_TYPE_POISON` | int | `31` |  |
| `EFFECT_TYPE_DISEASE` | int | `32` |  |
| `EFFECT_TYPE_CURSE` | int | `33` |  |
| `EFFECT_TYPE_SILENCE` | int | `34` |  |
| `EFFECT_TYPE_TURNED` | int | `35` |  |
| `EFFECT_TYPE_HASTE` | int | `36` |  |
| `EFFECT_TYPE_SLOW` | int | `37` |  |
| `EFFECT_TYPE_ABILITY_INCREASE` | int | `38` |  |
| `EFFECT_TYPE_ABILITY_DECREASE` | int | `39` |  |
| `EFFECT_TYPE_ATTACK_INCREASE` | int | `40` |  |
| `EFFECT_TYPE_ATTACK_DECREASE` | int | `41` |  |
| `EFFECT_TYPE_DAMAGE_INCREASE` | int | `42` |  |
| `EFFECT_TYPE_DAMAGE_DECREASE` | int | `43` |  |
| `EFFECT_TYPE_DAMAGE_IMMUNITY_INCREASE` | int | `44` |  |
| `EFFECT_TYPE_DAMAGE_IMMUNITY_DECREASE` | int | `45` |  |
| `EFFECT_TYPE_AC_INCREASE` | int | `46` |  |
| `EFFECT_TYPE_AC_DECREASE` | int | `47` |  |
| `EFFECT_TYPE_MOVEMENT_SPEED_INCREASE` | int | `48` |  |
| `EFFECT_TYPE_MOVEMENT_SPEED_DECREASE` | int | `49` |  |
| `EFFECT_TYPE_SAVING_THROW_INCREASE` | int | `50` |  |
| `EFFECT_TYPE_SAVING_THROW_DECREASE` | int | `51` |  |
| `EFFECT_TYPE_SPELL_RESISTANCE_INCREASE` | int | `52` |  |
| `EFFECT_TYPE_SPELL_RESISTANCE_DECREASE` | int | `53` |  |
| `EFFECT_TYPE_SKILL_INCREASE` | int | `54` |  |
| `EFFECT_TYPE_SKILL_DECREASE` | int | `55` |  |
| `EFFECT_TYPE_INVISIBILITY` | int | `56` |  |
| `EFFECT_TYPE_IMPROVEDINVISIBILITY` | int | `57` |  |
| `EFFECT_TYPE_DARKNESS` | int | `58` |  |
| `EFFECT_TYPE_DISPELMAGICALL` | int | `59` |  |
| `EFFECT_TYPE_ELEMENTALSHIELD` | int | `60` |  |
| `EFFECT_TYPE_NEGATIVELEVEL` | int | `61` |  |
| `EFFECT_TYPE_POLYMORPH` | int | `62` |  |
| `EFFECT_TYPE_SANCTUARY` | int | `63` |  |
| `EFFECT_TYPE_TRUESEEING` | int | `64` |  |
| `EFFECT_TYPE_SEEINVISIBLE` | int | `65` |  |
| `EFFECT_TYPE_TIMESTOP` | int | `66` |  |
| `EFFECT_TYPE_BLINDNESS` | int | `67` |  |
| `EFFECT_TYPE_SPELLLEVELABSORPTION` | int | `68` |  |
| `EFFECT_TYPE_DISPELMAGICBEST` | int | `69` |  |
| `EFFECT_TYPE_ULTRAVISION` | int | `70` |  |
| `EFFECT_TYPE_MISS_CHANCE` | int | `71` |  |
| `EFFECT_TYPE_CONCEALMENT` | int | `72` |  |
| `EFFECT_TYPE_SPELL_IMMUNITY` | int | `73` |  |
| `EFFECT_TYPE_VISUALEFFECT` | int | `74` |  |
| `EFFECT_TYPE_DISAPPEARAPPEAR` | int | `75` |  |
| `EFFECT_TYPE_SWARM` | int | `76` |  |
| `EFFECT_TYPE_TURN_RESISTANCE_DECREASE` | int | `77` |  |
| `EFFECT_TYPE_TURN_RESISTANCE_INCREASE` | int | `78` |  |
| `EFFECT_TYPE_PETRIFY` | int | `79` |  |
| `EFFECT_TYPE_CUTSCENE_PARALYZE` | int | `80` |  |
| `EFFECT_TYPE_ETHEREAL` | int | `81` |  |
| `EFFECT_TYPE_SPELL_FAILURE` | int | `82` |  |
| `EFFECT_TYPE_CUTSCENEGHOST` | int | `83` |  |
| `EFFECT_TYPE_CUTSCENEIMMOBILIZE` | int | `84` |  |
| `EFFECT_TYPE_RUNSCRIPT` | int | `85` |  |
| `EFFECT_TYPE_ICON` | int | `86` |  |
| `EFFECT_TYPE_PACIFY` | int | `87` |  |
| `EFFECT_TYPE_BONUS_FEAT` | int | `88` |  |
| `EFFECT_TYPE_TIMESTOP_IMMUNITY` | int | `89` |  |
| `EFFECT_TYPE_FORCE_WALK` | int | `90` |  |
| `EFFECT_TYPE_APPEAR` | int | `91` |  |
| `EFFECT_TYPE_CUTSCENE_DOMINATED` | int | `92` |  |
| `EFFECT_TYPE_DAMAGE` | int | `93` |  |
| `EFFECT_TYPE_DEATH` | int | `94` |  |
| `EFFECT_TYPE_DISAPPEAR` | int | `95` |  |
| `EFFECT_TYPE_HEAL` | int | `96` |  |
| `EFFECT_TYPE_HITPOINTCHANGEWHENDYING` | int | `97` |  |
| `EFFECT_TYPE_KNOCKDOWN` | int | `98` |  |
| `EFFECT_TYPE_MODIFY_ATTACKS` | int | `99` |  |
| `EFFECT_TYPE_SUMMON_CREATURE` | int | `100` |  |
| `EFFECT_TYPE_TAUNT` | int | `101` |  |
| `EFFECT_TYPE_WOUNDING` | int | `102` |  |
| `ITEM_APPR_TYPE_SIMPLE_MODEL` | int | `0` |  |
| `ITEM_APPR_TYPE_WEAPON_COLOR` | int | `1` |  |
| `ITEM_APPR_TYPE_WEAPON_MODEL` | int | `2` |  |
| `ITEM_APPR_TYPE_ARMOR_MODEL` | int | `3` |  |
| `ITEM_APPR_TYPE_ARMOR_COLOR` | int | `4` |  |
| `ITEM_APPR_NUM_TYPES` | int | `5` |  |
| `ITEM_APPR_ARMOR_COLOR_LEATHER1` | int | `0` |  |
| `ITEM_APPR_ARMOR_COLOR_LEATHER2` | int | `1` |  |
| `ITEM_APPR_ARMOR_COLOR_CLOTH1` | int | `2` |  |
| `ITEM_APPR_ARMOR_COLOR_CLOTH2` | int | `3` |  |
| `ITEM_APPR_ARMOR_COLOR_METAL1` | int | `4` |  |
| `ITEM_APPR_ARMOR_COLOR_METAL2` | int | `5` |  |
| `ITEM_APPR_ARMOR_NUM_COLORS` | int | `6` |  |
| `ITEM_APPR_ARMOR_MODEL_RFOOT` | int | `0` |  |
| `ITEM_APPR_ARMOR_MODEL_LFOOT` | int | `1` |  |
| `ITEM_APPR_ARMOR_MODEL_RSHIN` | int | `2` |  |
| `ITEM_APPR_ARMOR_MODEL_LSHIN` | int | `3` |  |
| `ITEM_APPR_ARMOR_MODEL_LTHIGH` | int | `4` |  |
| `ITEM_APPR_ARMOR_MODEL_RTHIGH` | int | `5` |  |
| `ITEM_APPR_ARMOR_MODEL_PELVIS` | int | `6` |  |
| `ITEM_APPR_ARMOR_MODEL_TORSO` | int | `7` |  |
| `ITEM_APPR_ARMOR_MODEL_BELT` | int | `8` |  |
| `ITEM_APPR_ARMOR_MODEL_NECK` | int | `9` |  |
| `ITEM_APPR_ARMOR_MODEL_RFOREARM` | int | `10` |  |
| `ITEM_APPR_ARMOR_MODEL_LFOREARM` | int | `11` |  |
| `ITEM_APPR_ARMOR_MODEL_RBICEP` | int | `12` |  |
| `ITEM_APPR_ARMOR_MODEL_LBICEP` | int | `13` |  |
| `ITEM_APPR_ARMOR_MODEL_RSHOULDER` | int | `14` |  |
| `ITEM_APPR_ARMOR_MODEL_LSHOULDER` | int | `15` |  |
| `ITEM_APPR_ARMOR_MODEL_RHAND` | int | `16` |  |
| `ITEM_APPR_ARMOR_MODEL_LHAND` | int | `17` |  |
| `ITEM_APPR_ARMOR_MODEL_ROBE` | int | `18` |  |
| `ITEM_APPR_ARMOR_NUM_MODELS` | int | `19` |  |
| `ITEM_APPR_WEAPON_MODEL_BOTTOM` | int | `0` |  |
| `ITEM_APPR_WEAPON_MODEL_MIDDLE` | int | `1` |  |
| `ITEM_APPR_WEAPON_MODEL_TOP` | int | `2` |  |
| `ITEM_APPR_WEAPON_COLOR_BOTTOM` | int | `0` |  |
| `ITEM_APPR_WEAPON_COLOR_MIDDLE` | int | `1` |  |
| `ITEM_APPR_WEAPON_COLOR_TOP` | int | `2` |  |
| `ITEM_PROPERTY_ABILITY_BONUS` | int | `0` |  |
| `ITEM_PROPERTY_AC_BONUS` | int | `1` |  |
| `ITEM_PROPERTY_AC_BONUS_VS_ALIGNMENT_GROUP` | int | `2` |  |
| `ITEM_PROPERTY_AC_BONUS_VS_DAMAGE_TYPE` | int | `3` |  |
| `ITEM_PROPERTY_AC_BONUS_VS_RACIAL_GROUP` | int | `4` |  |
| `ITEM_PROPERTY_AC_BONUS_VS_SPECIFIC_ALIGNMENT` | int | `5` |  |
| `ITEM_PROPERTY_ENHANCEMENT_BONUS` | int | `6` |  |
| `ITEM_PROPERTY_ENHANCEMENT_BONUS_VS_ALIGNMENT_GROUP` | int | `7` |  |
| `ITEM_PROPERTY_ENHANCEMENT_BONUS_VS_RACIAL_GROUP` | int | `8` |  |
| `ITEM_PROPERTY_ENHANCEMENT_BONUS_VS_SPECIFIC_ALIGNEMENT` | int | `9` |  |
| `ITEM_PROPERTY_DECREASED_ENHANCEMENT_MODIFIER` | int | `10` |  |
| `ITEM_PROPERTY_BASE_ITEM_WEIGHT_REDUCTION` | int | `11` |  |
| `ITEM_PROPERTY_BONUS_FEAT` | int | `12` |  |
| `ITEM_PROPERTY_BONUS_SPELL_SLOT_OF_LEVEL_N` | int | `13` |  |
| `ITEM_PROPERTY_CAST_SPELL` | int | `15` |  |
| `ITEM_PROPERTY_DAMAGE_BONUS` | int | `16` |  |
| `ITEM_PROPERTY_DAMAGE_BONUS_VS_ALIGNMENT_GROUP` | int | `17` |  |
| `ITEM_PROPERTY_DAMAGE_BONUS_VS_RACIAL_GROUP` | int | `18` |  |
| `ITEM_PROPERTY_DAMAGE_BONUS_VS_SPECIFIC_ALIGNMENT` | int | `19` |  |
| `ITEM_PROPERTY_IMMUNITY_DAMAGE_TYPE` | int | `20` |  |
| `ITEM_PROPERTY_DECREASED_DAMAGE` | int | `21` |  |
| `ITEM_PROPERTY_DAMAGE_REDUCTION` | int | `22` |  |
| `ITEM_PROPERTY_DAMAGE_RESISTANCE` | int | `23` |  |
| `ITEM_PROPERTY_DAMAGE_VULNERABILITY` | int | `24` |  |
| `ITEM_PROPERTY_DARKVISION` | int | `26` |  |
| `ITEM_PROPERTY_DECREASED_ABILITY_SCORE` | int | `27` |  |
| `ITEM_PROPERTY_DECREASED_AC` | int | `28` |  |
| `ITEM_PROPERTY_DECREASED_SKILL_MODIFIER` | int | `29` |  |
| `ITEM_PROPERTY_ENHANCED_CONTAINER_REDUCED_WEIGHT` | int | `32` |  |
| `ITEM_PROPERTY_EXTRA_MELEE_DAMAGE_TYPE` | int | `33` |  |
| `ITEM_PROPERTY_EXTRA_RANGED_DAMAGE_TYPE` | int | `34` |  |
| `ITEM_PROPERTY_HASTE` | int | `35` |  |
| `ITEM_PROPERTY_HOLY_AVENGER` | int | `36` |  |
| `ITEM_PROPERTY_IMMUNITY_MISCELLANEOUS` | int | `37` |  |
| `ITEM_PROPERTY_IMPROVED_EVASION` | int | `38` |  |
| `ITEM_PROPERTY_SPELL_RESISTANCE` | int | `39` |  |
| `ITEM_PROPERTY_SAVING_THROW_BONUS` | int | `40` |  |
| `ITEM_PROPERTY_SAVING_THROW_BONUS_SPECIFIC` | int | `41` |  |
| `ITEM_PROPERTY_KEEN` | int | `43` |  |
| `ITEM_PROPERTY_LIGHT` | int | `44` |  |
| `ITEM_PROPERTY_MIGHTY` | int | `45` |  |
| `ITEM_PROPERTY_MIND_BLANK` | int | `46` |  |
| `ITEM_PROPERTY_NO_DAMAGE` | int | `47` |  |
| `ITEM_PROPERTY_ON_HIT_PROPERTIES` | int | `48` |  |
| `ITEM_PROPERTY_DECREASED_SAVING_THROWS` | int | `49` |  |
| `ITEM_PROPERTY_DECREASED_SAVING_THROWS_SPECIFIC` | int | `50` |  |
| `ITEM_PROPERTY_REGENERATION` | int | `51` |  |
| `ITEM_PROPERTY_SKILL_BONUS` | int | `52` |  |
| `ITEM_PROPERTY_IMMUNITY_SPECIFIC_SPELL` | int | `53` |  |
| `ITEM_PROPERTY_IMMUNITY_SPELL_SCHOOL` | int | `54` |  |
| `ITEM_PROPERTY_THIEVES_TOOLS` | int | `55` |  |
| `ITEM_PROPERTY_ATTACK_BONUS` | int | `56` |  |
| `ITEM_PROPERTY_ATTACK_BONUS_VS_ALIGNMENT_GROUP` | int | `57` |  |
| `ITEM_PROPERTY_ATTACK_BONUS_VS_RACIAL_GROUP` | int | `58` |  |
| `ITEM_PROPERTY_ATTACK_BONUS_VS_SPECIFIC_ALIGNMENT` | int | `59` |  |
| `ITEM_PROPERTY_DECREASED_ATTACK_MODIFIER` | int | `60` |  |
| `ITEM_PROPERTY_UNLIMITED_AMMUNITION` | int | `61` |  |
| `ITEM_PROPERTY_USE_LIMITATION_ALIGNMENT_GROUP` | int | `62` |  |
| `ITEM_PROPERTY_USE_LIMITATION_CLASS` | int | `63` |  |
| `ITEM_PROPERTY_USE_LIMITATION_RACIAL_TYPE` | int | `64` |  |
| `ITEM_PROPERTY_USE_LIMITATION_SPECIFIC_ALIGNMENT` | int | `65` |  |
| `ITEM_PROPERTY_USE_LIMITATION_TILESET` | int | `66` |  |
| `ITEM_PROPERTY_REGENERATION_VAMPIRIC` | int | `67` |  |
| `ITEM_PROPERTY_TRAP` | int | `70` |  |
| `ITEM_PROPERTY_TRUE_SEEING` | int | `71` |  |
| `ITEM_PROPERTY_ON_MONSTER_HIT` | int | `72` |  |
| `ITEM_PROPERTY_TURN_RESISTANCE` | int | `73` |  |
| `ITEM_PROPERTY_MASSIVE_CRITICALS` | int | `74` |  |
| `ITEM_PROPERTY_FREEDOM_OF_MOVEMENT` | int | `75` |  |
| `ITEM_PROPERTY_POISON` | int | `76` |  |
| `ITEM_PROPERTY_MONSTER_DAMAGE` | int | `77` |  |
| `ITEM_PROPERTY_IMMUNITY_SPELLS_BY_LEVEL` | int | `78` |  |
| `ITEM_PROPERTY_SPECIAL_WALK` | int | `79` |  |
| `ITEM_PROPERTY_HEALERS_KIT` | int | `80` |  |
| `ITEM_PROPERTY_WEIGHT_INCREASE` | int | `81` |  |
| `ITEM_PROPERTY_ONHITCASTSPELL` | int | `82` |  |
| `ITEM_PROPERTY_VISUALEFFECT` | int | `83` |  |
| `ITEM_PROPERTY_ARCANE_SPELL_FAILURE` | int | `84` |  |
| `ITEM_PROPERTY_MATERIAL` | int | `85` |  |
| `ITEM_PROPERTY_QUALITY` | int | `86` |  |
| `ITEM_PROPERTY_ADDITIONAL` | int | `87` |  |
| `BASE_ITEM_SHORTSWORD` | int | `0` |  |
| `BASE_ITEM_LONGSWORD` | int | `1` |  |
| `BASE_ITEM_BATTLEAXE` | int | `2` |  |
| `BASE_ITEM_BASTARDSWORD` | int | `3` |  |
| `BASE_ITEM_LIGHTFLAIL` | int | `4` |  |
| `BASE_ITEM_WARHAMMER` | int | `5` |  |
| `BASE_ITEM_HEAVYCROSSBOW` | int | `6` |  |
| `BASE_ITEM_LIGHTCROSSBOW` | int | `7` |  |
| `BASE_ITEM_LONGBOW` | int | `8` |  |
| `BASE_ITEM_LIGHTMACE` | int | `9` |  |
| `BASE_ITEM_HALBERD` | int | `10` |  |
| `BASE_ITEM_SHORTBOW` | int | `11` |  |
| `BASE_ITEM_TWOBLADEDSWORD` | int | `12` |  |
| `BASE_ITEM_GREATSWORD` | int | `13` |  |
| `BASE_ITEM_SMALLSHIELD` | int | `14` |  |
| `BASE_ITEM_TORCH` | int | `15` |  |
| `BASE_ITEM_ARMOR` | int | `16` |  |
| `BASE_ITEM_HELMET` | int | `17` |  |
| `BASE_ITEM_GREATAXE` | int | `18` |  |
| `BASE_ITEM_AMULET` | int | `19` |  |
| `BASE_ITEM_ARROW` | int | `20` |  |
| `BASE_ITEM_BELT` | int | `21` |  |
| `BASE_ITEM_DAGGER` | int | `22` |  |
| `BASE_ITEM_MISCSMALL` | int | `24` |  |
| `BASE_ITEM_BOLT` | int | `25` |  |
| `BASE_ITEM_BOOTS` | int | `26` |  |
| `BASE_ITEM_BULLET` | int | `27` |  |
| `BASE_ITEM_CLUB` | int | `28` |  |
| `BASE_ITEM_MISCMEDIUM` | int | `29` |  |
| `BASE_ITEM_DART` | int | `31` |  |
| `BASE_ITEM_DIREMACE` | int | `32` |  |
| `BASE_ITEM_DOUBLEAXE` | int | `33` |  |
| `BASE_ITEM_MISCLARGE` | int | `34` |  |
| `BASE_ITEM_HEAVYFLAIL` | int | `35` |  |
| `BASE_ITEM_GLOVES` | int | `36` |  |
| `BASE_ITEM_LIGHTHAMMER` | int | `37` |  |
| `BASE_ITEM_HANDAXE` | int | `38` |  |
| `BASE_ITEM_HEALERSKIT` | int | `39` |  |
| `BASE_ITEM_KAMA` | int | `40` |  |
| `BASE_ITEM_KATANA` | int | `41` |  |
| `BASE_ITEM_KUKRI` | int | `42` |  |
| `BASE_ITEM_MISCTALL` | int | `43` |  |
| `BASE_ITEM_MAGICROD` | int | `44` |  |
| `BASE_ITEM_MAGICSTAFF` | int | `45` |  |
| `BASE_ITEM_MAGICWAND` | int | `46` |  |
| `BASE_ITEM_MORNINGSTAR` | int | `47` |  |
| `BASE_ITEM_POTIONS` | int | `49` |  |
| `BASE_ITEM_QUARTERSTAFF` | int | `50` |  |
| `BASE_ITEM_RAPIER` | int | `51` |  |
| `BASE_ITEM_RING` | int | `52` |  |
| `BASE_ITEM_SCIMITAR` | int | `53` |  |
| `BASE_ITEM_SCROLL` | int | `54` |  |
| `BASE_ITEM_SCYTHE` | int | `55` |  |
| `BASE_ITEM_LARGESHIELD` | int | `56` |  |
| `BASE_ITEM_TOWERSHIELD` | int | `57` |  |
| `BASE_ITEM_SHORTSPEAR` | int | `58` |  |
| `BASE_ITEM_SHURIKEN` | int | `59` |  |
| `BASE_ITEM_SICKLE` | int | `60` |  |
| `BASE_ITEM_SLING` | int | `61` |  |
| `BASE_ITEM_THIEVESTOOLS` | int | `62` |  |
| `BASE_ITEM_THROWINGAXE` | int | `63` |  |
| `BASE_ITEM_TRAPKIT` | int | `64` |  |
| `BASE_ITEM_KEY` | int | `65` |  |
| `BASE_ITEM_LARGEBOX` | int | `66` |  |
| `BASE_ITEM_MISCWIDE` | int | `68` |  |
| `BASE_ITEM_CSLASHWEAPON` | int | `69` |  |
| `BASE_ITEM_CPIERCWEAPON` | int | `70` |  |
| `BASE_ITEM_CBLUDGWEAPON` | int | `71` |  |
| `BASE_ITEM_CSLSHPRCWEAP` | int | `72` |  |
| `BASE_ITEM_CREATUREITEM` | int | `73` |  |
| `BASE_ITEM_BOOK` | int | `74` |  |
| `BASE_ITEM_SPELLSCROLL` | int | `75` |  |
| `BASE_ITEM_GOLD` | int | `76` |  |
| `BASE_ITEM_GEM` | int | `77` |  |
| `BASE_ITEM_BRACER` | int | `78` |  |
| `BASE_ITEM_MISCTHIN` | int | `79` |  |
| `BASE_ITEM_CLOAK` | int | `80` |  |
| `BASE_ITEM_GRENADE` | int | `81` |  |
| `BASE_ITEM_TRIDENT` | int | `95` |  |
| `BASE_ITEM_BLANK_POTION` | int | `101` |  |
| `BASE_ITEM_BLANK_SCROLL` | int | `102` |  |
| `BASE_ITEM_BLANK_WAND` | int | `103` |  |
| `BASE_ITEM_ENCHANTED_POTION` | int | `104` |  |
| `BASE_ITEM_ENCHANTED_SCROLL` | int | `105` |  |
| `BASE_ITEM_ENCHANTED_WAND` | int | `106` |  |
| `BASE_ITEM_DWARVENWARAXE` | int | `108` |  |
| `BASE_ITEM_CRAFTMATERIALMED` | int | `109` |  |
| `BASE_ITEM_CRAFTMATERIALSML` | int | `110` |  |
| `BASE_ITEM_WHIP` | int | `111` |  |
| `BASE_ITEM_INVALID` | int | `256` |  |
| `VFX_NONE` | int | `-1` |  |
| `VFX_DUR_BLUR` | int | `0` |  |
| `VFX_DUR_DARKNESS` | int | `1` |  |
| `VFX_DUR_ENTANGLE` | int | `2` |  |
| `VFX_DUR_FREEDOM_OF_MOVEMENT` | int | `3` |  |
| `VFX_DUR_GLOBE_INVULNERABILITY` | int | `4` |  |
| `VFX_DUR_BLACKOUT` | int | `5` |  |
| `VFX_DUR_INVISIBILITY` | int | `6` |  |
| `VFX_DUR_MIND_AFFECTING_NEGATIVE` | int | `7` |  |
| `VFX_DUR_MIND_AFFECTING_POSITIVE` | int | `8` |  |
| `VFX_DUR_GHOSTLY_VISAGE` | int | `9` |  |
| `VFX_DUR_ETHEREAL_VISAGE` | int | `10` |  |
| `VFX_DUR_PROT_BARKSKIN` | int | `11` |  |
| `VFX_DUR_PROT_GREATER_STONESKIN` | int | `12` |  |
| `VFX_DUR_PROT_PREMONITION` | int | `13` |  |
| `VFX_DUR_PROT_SHADOW_ARMOR` | int | `14` |  |
| `VFX_DUR_PROT_STONESKIN` | int | `15` |  |
| `VFX_DUR_SANCTUARY` | int | `16` |  |
| `VFX_DUR_WEB` | int | `17` |  |
| `VFX_FNF_BLINDDEAF` | int | `18` |  |
| `VFX_FNF_DISPEL` | int | `19` |  |
| `VFX_FNF_DISPEL_DISJUNCTION` | int | `20` |  |
| `VFX_FNF_DISPEL_GREATER` | int | `21` |  |
| `VFX_FNF_FIREBALL` | int | `22` |  |
| `VFX_FNF_FIRESTORM` | int | `23` |  |
| `VFX_FNF_IMPLOSION` | int | `24` |  |
| `VFX_FNF_MASS_HEAL` | int | `26` |  |
| `VFX_FNF_MASS_MIND_AFFECTING` | int | `27` |  |
| `VFX_FNF_METEOR_SWARM` | int | `28` |  |
| `VFX_FNF_NATURES_BALANCE` | int | `29` |  |
| `VFX_FNF_PWKILL` | int | `30` |  |
| `VFX_FNF_PWSTUN` | int | `31` |  |
| `VFX_FNF_SUMMON_GATE` | int | `32` |  |
| `VFX_FNF_SUMMON_MONSTER_1` | int | `33` |  |
| `VFX_FNF_SUMMON_MONSTER_2` | int | `34` |  |
| `VFX_FNF_SUMMON_MONSTER_3` | int | `35` |  |
| `VFX_FNF_SUMMON_UNDEAD` | int | `36` |  |
| `VFX_FNF_SUNBEAM` | int | `37` |  |
| `VFX_FNF_TIME_STOP` | int | `38` |  |
| `VFX_FNF_WAIL_O_BANSHEES` | int | `39` |  |
| `VFX_FNF_WEIRD` | int | `40` |  |
| `VFX_FNF_WORD` | int | `41` |  |
| `VFX_IMP_AC_BONUS` | int | `42` |  |
| `VFX_IMP_ACID_L` | int | `43` |  |
| `VFX_IMP_ACID_S` | int | `44` |  |
| `VFX_IMP_BLIND_DEAF_M` | int | `46` |  |
| `VFX_IMP_BREACH` | int | `47` |  |
| `VFX_IMP_CONFUSION_S` | int | `48` |  |
| `VFX_IMP_DAZED_S` | int | `49` |  |
| `VFX_IMP_DEATH` | int | `50` |  |
| `VFX_IMP_DISEASE_S` | int | `51` |  |
| `VFX_IMP_DISPEL` | int | `52` |  |
| `VFX_IMP_DISPEL_DISJUNCTION` | int | `53` |  |
| `VFX_IMP_DIVINE_STRIKE_FIRE` | int | `54` |  |
| `VFX_IMP_DIVINE_STRIKE_HOLY` | int | `55` |  |
| `VFX_IMP_DOMINATE_S` | int | `56` |  |
| `VFX_IMP_DOOM` | int | `57` |  |
| `VFX_IMP_FEAR_S` | int | `58` |  |
| `VFX_IMP_FLAME_M` | int | `60` |  |
| `VFX_IMP_FLAME_S` | int | `61` |  |
| `VFX_IMP_FROST_L` | int | `62` |  |
| `VFX_IMP_FROST_S` | int | `63` |  |
| `VFX_IMP_GREASE` | int | `64` |  |
| `VFX_IMP_HASTE` | int | `65` |  |
| `VFX_IMP_HEALING_G` | int | `66` |  |
| `VFX_IMP_HEALING_L` | int | `67` |  |
| `VFX_IMP_HEALING_M` | int | `68` |  |
| `VFX_IMP_HEALING_S` | int | `69` |  |
| `VFX_IMP_HEALING_X` | int | `70` |  |
| `VFX_IMP_HOLY_AID` | int | `71` |  |
| `VFX_IMP_KNOCK` | int | `72` |  |
| `VFX_BEAM_LIGHTNING` | int | `73` |  |
| `VFX_IMP_LIGHTNING_M` | int | `74` |  |
| `VFX_IMP_LIGHTNING_S` | int | `75` |  |
| `VFX_IMP_MAGBLUE` | int | `76` |  |
| `VFX_IMP_NEGATIVE_ENERGY` | int | `81` |  |
| `VFX_DUR_PARALYZE_HOLD` | int | `82` |  |
| `VFX_IMP_POISON_L` | int | `83` |  |
| `VFX_IMP_POISON_S` | int | `84` |  |
| `VFX_IMP_POLYMORPH` | int | `85` |  |
| `VFX_IMP_PULSE_COLD` | int | `86` |  |
| `VFX_IMP_PULSE_FIRE` | int | `87` |  |
| `VFX_IMP_PULSE_HOLY` | int | `88` |  |
| `VFX_IMP_PULSE_NEGATIVE` | int | `89` |  |
| `VFX_IMP_RAISE_DEAD` | int | `90` |  |
| `VFX_IMP_REDUCE_ABILITY_SCORE` | int | `91` |  |
| `VFX_IMP_REMOVE_CONDITION` | int | `92` |  |
| `VFX_IMP_SILENCE` | int | `93` |  |
| `VFX_IMP_SLEEP` | int | `94` |  |
| `VFX_IMP_SLOW` | int | `95` |  |
| `VFX_IMP_SONIC` | int | `96` |  |
| `VFX_IMP_STUN` | int | `97` |  |
| `VFX_IMP_SUNSTRIKE` | int | `98` |  |
| `VFX_IMP_UNSUMMON` | int | `99` |  |
| `VFX_COM_SPECIAL_BLUE_RED` | int | `100` |  |
| `VFX_COM_SPECIAL_PINK_ORANGE` | int | `101` |  |
| `VFX_COM_SPECIAL_RED_WHITE` | int | `102` |  |
| `VFX_COM_SPECIAL_RED_ORANGE` | int | `103` |  |
| `VFX_COM_SPECIAL_WHITE_BLUE` | int | `104` |  |
| `VFX_COM_SPECIAL_WHITE_ORANGE` | int | `105` |  |
| `VFX_COM_BLOOD_REG_WIMP` | int | `106` |  |
| `VFX_COM_BLOOD_LRG_WIMP` | int | `107` |  |
| `VFX_COM_BLOOD_CRT_WIMP` | int | `108` |  |
| `VFX_COM_BLOOD_REG_RED` | int | `109` |  |
| `VFX_COM_BLOOD_REG_GREEN` | int | `110` |  |
| `VFX_COM_BLOOD_REG_YELLOW` | int | `111` |  |
| `VFX_COM_BLOOD_LRG_RED` | int | `112` |  |
| `VFX_COM_BLOOD_LRG_GREEN` | int | `113` |  |
| `VFX_COM_BLOOD_LRG_YELLOW` | int | `114` |  |
| `VFX_COM_BLOOD_CRT_RED` | int | `115` |  |
| `VFX_COM_BLOOD_CRT_GREEN` | int | `116` |  |
| `VFX_COM_BLOOD_CRT_YELLOW` | int | `117` |  |
| `VFX_COM_SPARKS_PARRY` | int | `118` |  |
| `VFX_COM_UNLOAD_MODEL` | int | `120` |  |
| `VFX_COM_CHUNK_RED_SMALL` | int | `121` |  |
| `VFX_COM_CHUNK_RED_MEDIUM` | int | `122` |  |
| `VFX_COM_CHUNK_GREEN_SMALL` | int | `123` |  |
| `VFX_COM_CHUNK_GREEN_MEDIUM` | int | `124` |  |
| `VFX_COM_CHUNK_YELLOW_SMALL` | int | `125` |  |
| `VFX_COM_CHUNK_YELLOW_MEDIUM` | int | `126` |  |
| `VFX_DUR_SPELLTURNING` | int | `138` |  |
| `VFX_IMP_IMPROVE_ABILITY_SCORE` | int | `139` |  |
| `VFX_IMP_CHARM` | int | `140` |  |
| `VFX_IMP_MAGICAL_VISION` | int | `141` |  |
| `VFX_IMP_EVIL_HELP` | int | `144` |  |
| `VFX_IMP_GOOD_HELP` | int | `145` |  |
| `VFX_IMP_DEATH_WARD` | int | `146` |  |
| `VFX_DUR_ELEMENTAL_SHIELD` | int | `147` |  |
| `VFX_DUR_LIGHT` | int | `148` |  |
| `VFX_IMP_MAGIC_PROTECTION` | int | `149` |  |
| `VFX_IMP_SUPER_HEROISM` | int | `150` |  |
| `VFX_FNF_STORM` | int | `151` |  |
| `VFX_IMP_ELEMENTAL_PROTECTION` | int | `152` |  |
| `VFX_DUR_LIGHT_BLUE_5` | int | `153` |  |
| `VFX_DUR_LIGHT_BLUE_10` | int | `154` |  |
| `VFX_DUR_LIGHT_BLUE_15` | int | `155` |  |
| `VFX_DUR_LIGHT_BLUE_20` | int | `156` |  |
| `VFX_DUR_LIGHT_YELLOW_5` | int | `157` |  |
| `VFX_DUR_LIGHT_YELLOW_10` | int | `158` |  |
| `VFX_DUR_LIGHT_YELLOW_15` | int | `159` |  |
| `VFX_DUR_LIGHT_YELLOW_20` | int | `160` |  |
| `VFX_DUR_LIGHT_PURPLE_5` | int | `161` |  |
| `VFX_DUR_LIGHT_PURPLE_10` | int | `162` |  |
| `VFX_DUR_LIGHT_PURPLE_15` | int | `163` |  |
| `VFX_DUR_LIGHT_PURPLE_20` | int | `164` |  |
| `VFX_DUR_LIGHT_RED_5` | int | `165` |  |
| `VFX_DUR_LIGHT_RED_10` | int | `166` |  |
| `VFX_DUR_LIGHT_RED_15` | int | `167` |  |
| `VFX_DUR_LIGHT_RED_20` | int | `168` |  |
| `VFX_DUR_LIGHT_ORANGE_5` | int | `169` |  |
| `VFX_DUR_LIGHT_ORANGE_10` | int | `170` |  |
| `VFX_DUR_LIGHT_ORANGE_15` | int | `171` |  |
| `VFX_DUR_LIGHT_ORANGE_20` | int | `172` |  |
| `VFX_DUR_LIGHT_WHITE_5` | int | `173` |  |
| `VFX_DUR_LIGHT_WHITE_10` | int | `174` |  |
| `VFX_DUR_LIGHT_WHITE_15` | int | `175` |  |
| `VFX_DUR_LIGHT_WHITE_20` | int | `176` |  |
| `VFX_DUR_LIGHT_GREY_5` | int | `177` |  |
| `VFX_DUR_LIGHT_GREY_10` | int | `178` |  |
| `VFX_DUR_LIGHT_GREY_15` | int | `179` |  |
| `VFX_DUR_LIGHT_GREY_20` | int | `180` |  |
| `VFX_IMP_MIRV` | int | `181` |  |
| `VFX_DUR_DARKVISION` | int | `182` |  |
| `VFX_FNF_SOUND_BURST` | int | `183` |  |
| `VFX_FNF_STRIKE_HOLY` | int | `184` |  |
| `VFX_FNF_LOS_EVIL_10` | int | `185` |  |
| `VFX_FNF_LOS_EVIL_20` | int | `186` |  |
| `VFX_FNF_LOS_EVIL_30` | int | `187` |  |
| `VFX_FNF_LOS_HOLY_10` | int | `188` |  |
| `VFX_FNF_LOS_HOLY_20` | int | `189` |  |
| `VFX_FNF_LOS_HOLY_30` | int | `190` |  |
| `VFX_FNF_LOS_NORMAL_10` | int | `191` |  |
| `VFX_FNF_LOS_NORMAL_20` | int | `192` |  |
| `VFX_FNF_LOS_NORMAL_30` | int | `193` |  |
| `VFX_IMP_HEAD_ACID` | int | `194` |  |
| `VFX_IMP_HEAD_FIRE` | int | `195` |  |
| `VFX_IMP_HEAD_SONIC` | int | `196` |  |
| `VFX_IMP_HEAD_ELECTRICITY` | int | `197` |  |
| `VFX_IMP_HEAD_COLD` | int | `198` |  |
| `VFX_IMP_HEAD_HOLY` | int | `199` |  |
| `VFX_IMP_HEAD_NATURE` | int | `200` |  |
| `VFX_IMP_HEAD_HEAL` | int | `201` |  |
| `VFX_IMP_HEAD_MIND` | int | `202` |  |
| `VFX_IMP_HEAD_EVIL` | int | `203` |  |
| `VFX_IMP_HEAD_ODD` | int | `204` |  |
| `VFX_DUR_CESSATE_NEUTRAL` | int | `205` |  |
| `VFX_DUR_CESSATE_POSITIVE` | int | `206` |  |
| `VFX_DUR_CESSATE_NEGATIVE` | int | `207` |  |
| `VFX_DUR_MIND_AFFECTING_DISABLED` | int | `208` |  |
| `VFX_DUR_MIND_AFFECTING_DOMINATED` | int | `209` |  |
| `VFX_BEAM_FIRE` | int | `210` |  |
| `VFX_BEAM_COLD` | int | `211` |  |
| `VFX_BEAM_HOLY` | int | `212` |  |
| `VFX_BEAM_MIND` | int | `213` |  |
| `VFX_BEAM_EVIL` | int | `214` |  |
| `VFX_BEAM_ODD` | int | `215` |  |
| `VFX_BEAM_FIRE_LASH` | int | `216` |  |
| `VFX_IMP_DEATH_L` | int | `217` |  |
| `VFX_DUR_MIND_AFFECTING_FEAR` | int | `218` |  |
| `VFX_FNF_SUMMON_CELESTIAL` | int | `219` |  |
| `VFX_DUR_GLOBE_MINOR` | int | `220` |  |
| `VFX_IMP_RESTORATION_LESSER` | int | `221` |  |
| `VFX_IMP_RESTORATION` | int | `222` |  |
| `VFX_IMP_RESTORATION_GREATER` | int | `223` |  |
| `VFX_DUR_PROTECTION_ELEMENTS` | int | `224` |  |
| `VFX_DUR_PROTECTION_GOOD_MINOR` | int | `225` |  |
| `VFX_DUR_PROTECTION_GOOD_MAJOR` | int | `226` |  |
| `VFX_DUR_PROTECTION_EVIL_MINOR` | int | `227` |  |
| `VFX_DUR_PROTECTION_EVIL_MAJOR` | int | `228` |  |
| `VFX_DUR_MAGICAL_SIGHT` | int | `229` |  |
| `VFX_DUR_WEB_MASS` | int | `230` |  |
| `VFX_FNF_ICESTORM` | int | `231` |  |
| `VFX_DUR_PARALYZED` | int | `232` |  |
| `VFX_IMP_MIRV_FLAME` | int | `233` |  |
| `VFX_IMP_DESTRUCTION` | int | `234` |  |
| `VFX_COM_CHUNK_RED_LARGE` | int | `235` |  |
| `VFX_COM_CHUNK_BONE_MEDIUM` | int | `236` |  |
| `VFX_COM_BLOOD_SPARK_SMALL` | int | `237` |  |
| `VFX_COM_BLOOD_SPARK_MEDIUM` | int | `238` |  |
| `VFX_COM_BLOOD_SPARK_LARGE` | int | `239` |  |
| `VFX_DUR_GHOSTLY_PULSE` | int | `240` |  |
| `VFX_FNF_HORRID_WILTING` | int | `241` |  |
| `VFX_DUR_BLINDVISION` | int | `242` |  |
| `VFX_DUR_LOWLIGHTVISION` | int | `243` |  |
| `VFX_DUR_ULTRAVISION` | int | `244` |  |
| `VFX_DUR_MIRV_ACID` | int | `245` |  |
| `VFX_IMP_HARM` | int | `246` |  |
| `VFX_DUR_BLIND` | int | `247` |  |
| `VFX_DUR_ANTI_LIGHT_10` | int | `248` |  |
| `VFX_DUR_MAGIC_RESISTANCE` | int | `249` |  |
| `VFX_IMP_MAGIC_RESISTANCE_USE` | int | `250` |  |
| `VFX_IMP_GLOBE_USE` | int | `251` |  |
| `VFX_IMP_WILL_SAVING_THROW_USE` | int | `252` |  |
| `VFX_IMP_SPIKE_TRAP` | int | `253` |  |
| `VFX_IMP_SPELL_MANTLE_USE` | int | `254` |  |
| `VFX_IMP_FORTITUDE_SAVING_THROW_USE` | int | `255` |  |
| `VFX_IMP_REFLEX_SAVE_THROW_USE` | int | `256` |  |
| `VFX_FNF_GAS_EXPLOSION_ACID` | int | `257` |  |
| `VFX_FNF_GAS_EXPLOSION_EVIL` | int | `258` |  |
| `VFX_FNF_GAS_EXPLOSION_NATURE` | int | `259` |  |
| `VFX_FNF_GAS_EXPLOSION_FIRE` | int | `260` |  |
| `VFX_FNF_GAS_EXPLOSION_GREASE` | int | `261` |  |
| `VFX_FNF_GAS_EXPLOSION_MIND` | int | `262` |  |
| `VFX_FNF_SMOKE_PUFF` | int | `263` |  |
| `VFX_IMP_PULSE_WATER` | int | `264` |  |
| `VFX_IMP_PULSE_WIND` | int | `265` |  |
| `VFX_IMP_PULSE_NATURE` | int | `266` |  |
| `VFX_DUR_AURA_COLD` | int | `267` |  |
| `VFX_DUR_AURA_FIRE` | int | `268` |  |
| `VFX_DUR_AURA_POISON` | int | `269` |  |
| `VFX_DUR_AURA_DISEASE` | int | `270` |  |
| `VFX_DUR_AURA_ODD` | int | `271` |  |
| `VFX_DUR_AURA_SILENCE` | int | `272` |  |
| `VFX_IMP_AURA_HOLY` | int | `273` |  |
| `VFX_IMP_AURA_UNEARTHLY` | int | `274` |  |
| `VFX_IMP_AURA_FEAR` | int | `275` |  |
| `VFX_IMP_AURA_NEGATIVE_ENERGY` | int | `276` |  |
| `VFX_DUR_BARD_SONG` | int | `277` |  |
| `VFX_FNF_HOWL_MIND` | int | `278` |  |
| `VFX_FNF_HOWL_ODD` | int | `279` |  |
| `VFX_COM_HIT_FIRE` | int | `280` |  |
| `VFX_COM_HIT_FROST` | int | `281` |  |
| `VFX_COM_HIT_ELECTRICAL` | int | `282` |  |
| `VFX_COM_HIT_ACID` | int | `283` |  |
| `VFX_COM_HIT_SONIC` | int | `284` |  |
| `VFX_FNF_HOWL_WAR_CRY` | int | `285` |  |
| `VFX_FNF_SCREEN_SHAKE` | int | `286` |  |
| `VFX_FNF_SCREEN_BUMP` | int | `287` |  |
| `VFX_COM_HIT_NEGATIVE` | int | `288` |  |
| `VFX_COM_HIT_DIVINE` | int | `289` |  |
| `VFX_FNF_HOWL_WAR_CRY_FEMALE` | int | `290` |  |
| `VFX_DUR_AURA_DRAGON_FEAR` | int | `291` |  |
| `VFX_DUR_FLAG_RED` | int | `303` |  |
| `VFX_DUR_FLAG_BLUE` | int | `304` |  |
| `VFX_DUR_FLAG_GOLD` | int | `305` |  |
| `VFX_DUR_FLAG_PURPLE` | int | `306` |  |
| `VFX_DUR_FLAG_GOLD_FIXED` | int | `306` |  |
| `VFX_DUR_FLAG_PURPLE_FIXED` | int | `305` |  |
| `VFX_DUR_TENTACLE` | int | `346` |  |
| `VFX_DUR_PETRIFY` | int | `351` |  |
| `VFX_DUR_FREEZE_ANIMATION` | int | `352` |  |
| `VFX_COM_CHUNK_STONE_SMALL` | int | `353` |  |
| `VFX_COM_CHUNK_STONE_MEDIUM` | int | `354` |  |
| `VFX_BEAM_SILENT_LIGHTNING` | int | `307` |  |
| `VFX_BEAM_SILENT_FIRE` | int | `308` |  |
| `VFX_BEAM_SILENT_COLD` | int | `309` |  |
| `VFX_BEAM_SILENT_HOLY` | int | `310` |  |
| `VFX_BEAM_SILENT_MIND` | int | `311` |  |
| `VFX_BEAM_SILENT_EVIL` | int | `312` |  |
| `VFX_BEAM_SILENT_ODD` | int | `313` |  |
| `VFX_DUR_BIGBYS_INTERPOSING_HAND` | int | `314` |  |
| `VFX_IMP_BIGBYS_FORCEFUL_HAND` | int | `315` |  |
| `VFX_DUR_BIGBYS_CLENCHED_FIST` | int | `316` |  |
| `VFX_DUR_BIGBYS_CRUSHING_HAND` | int | `317` |  |
| `VFX_DUR_BIGBYS_GRASPING_HAND` | int | `318` |  |
| `VFX_DUR_CALTROPS` | int | `319` |  |
| `VFX_DUR_SMOKE` | int | `320` |  |
| `VFX_DUR_PIXIEDUST` | int | `321` |  |
| `VFX_FNF_DECK` | int | `322` |  |
| `VFX_DUR_CUTSCENE_INVISIBILITY` | int | `355` |  |
| `VFX_EYES_RED_FLAME_HUMAN_MALE` | int | `360` |  |
| `VFX_EYES_RED_FLAME_HUMAN_FEMALE` | int | `361` |  |
| `VFX_EYES_RED_FLAME_HALFELF_MALE` | int | `360` |  |
| `VFX_EYES_RED_FLAME_HALFELF_FEMALE` | int | `361` |  |
| `VFX_EYES_RED_FLAME_DWARF_MALE` | int | `362` |  |
| `VFX_EYES_RED_FLAME_DWARF_FEMALE` | int | `363` |  |
| `VFX_EYES_RED_FLAME_ELF_MALE` | int | `364` |  |
| `VFX_EYES_RED_FLAME_ELF_FEMALE` | int | `365` |  |
| `VFX_EYES_RED_FLAME_GNOME_MALE` | int | `366` |  |
| `VFX_EYES_RED_FLAME_GNOME_FEMALE` | int | `367` |  |
| `VFX_EYES_RED_FLAME_HALFLING_MALE` | int | `368` |  |
| `VFX_EYES_RED_FLAME_HALFLING_FEMALE` | int | `369` |  |
| `VFX_EYES_RED_FLAME_HALFORC_MALE` | int | `370` |  |
| `VFX_EYES_RED_FLAME_HALFORC_FEMALE` | int | `371` |  |
| `VFX_EYES_RED_FLAME_TROGLODYTE` | int | `372` |  |
| `VFX_EYES_YEL_HUMAN_MALE` | int | `373` |  |
| `VFX_EYES_YEL_HUMAN_FEMALE` | int | `374` |  |
| `VFX_EYES_YEL_DWARF_MALE` | int | `375` |  |
| `VFX_EYES_YEL_DWARF_FEMALE` | int | `376` |  |
| `VFX_EYES_YEL_ELF_MALE` | int | `377` |  |
| `VFX_EYES_YEL_ELF_FEMALE` | int | `378` |  |
| `VFX_EYES_YEL_GNOME_MALE` | int | `379` |  |
| `VFX_EYES_YEL_GNOME_FEMALE` | int | `380` |  |
| `VFX_EYES_YEL_HALFLING_MALE` | int | `381` |  |
| `VFX_EYES_YEL_HALFLING_FEMALE` | int | `382` |  |
| `VFX_EYES_YEL_HALFORC_MALE` | int | `383` |  |
| `VFX_EYES_YEL_HALFORC_FEMALE` | int | `384` |  |
| `VFX_EYES_YEL_TROGLODYTE` | int | `385` |  |
| `VFX_EYES_ORG_HUMAN_MALE` | int | `386` |  |
| `VFX_EYES_ORG_HUMAN_FEMALE` | int | `387` |  |
| `VFX_EYES_ORG_DWARF_MALE` | int | `388` |  |
| `VFX_EYES_ORG_DWARF_FEMALE` | int | `389` |  |
| `VFX_EYES_ORG_ELF_MALE` | int | `390` |  |
| `VFX_EYES_ORG_ELF_FEMALE` | int | `391` |  |
| `VFX_EYES_ORG_GNOME_MALE` | int | `392` |  |
| `VFX_EYES_ORG_GNOME_FEMALE` | int | `393` |  |
| `VFX_EYES_ORG_HALFLING_MALE` | int | `394` |  |
| `VFX_EYES_ORG_HALFLING_FEMALE` | int | `395` |  |
| `VFX_EYES_ORG_HALFORC_MALE` | int | `396` |  |
| `VFX_EYES_ORG_HALFORC_FEMALE` | int | `397` |  |
| `VFX_EYES_ORG_TROGLODYTE` | int | `398` |  |
| `VFX_DUR_IOUNSTONE` | int | `403` |  |
| `VFX_IMP_TORNADO` | int | `407` |  |
| `VFX_DUR_GLOW_LIGHT_BLUE` | int | `408` |  |
| `VFX_DUR_GLOW_PURPLE` | int | `409` |  |
| `VFX_DUR_GLOW_BLUE` | int | `410` |  |
| `VFX_DUR_GLOW_RED` | int | `411` |  |
| `VFX_DUR_GLOW_LIGHT_RED` | int | `412` |  |
| `VFX_DUR_GLOW_YELLOW` | int | `413` |  |
| `VFX_DUR_GLOW_LIGHT_YELLOW` | int | `414` |  |
| `VFX_DUR_GLOW_GREEN` | int | `415` |  |
| `VFX_DUR_GLOW_LIGHT_GREEN` | int | `416` |  |
| `VFX_DUR_GLOW_ORANGE` | int | `417` |  |
| `VFX_DUR_GLOW_LIGHT_ORANGE` | int | `418` |  |
| `VFX_DUR_GLOW_BROWN` | int | `419` |  |
| `VFX_DUR_GLOW_LIGHT_BROWN` | int | `420` |  |
| `VFX_DUR_GLOW_GREY` | int | `421` |  |
| `VFX_DUR_GLOW_WHITE` | int | `422` |  |
| `VFX_DUR_GLOW_LIGHT_PURPLE` | int | `423` |  |
| `VFX_DUR_GHOST_TRANSPARENT` | int | `424` |  |
| `VFX_DUR_GHOST_SMOKE` | int | `425` |  |
| `VFX_DUR_GLYPH_OF_WARDING` | int | `445` |  |
| `VFX_FNF_SOUND_BURST_SILENT` | int | `446` |  |
| `VFX_BEAM_DISINTEGRATE` | int | `447` |  |
| `VFX_FNF_ELECTRIC_EXPLOSION` | int | `459` |  |
| `VFX_IMP_DUST_EXPLOSION` | int | `460` |  |
| `VFX_IMP_PULSE_HOLY_SILENT` | int | `461` |  |
| `VFX_DUR_DEATH_ARMOR` | int | `463` |  |
| `VFX_DUR_ICESKIN` | int | `465` |  |
| `VFX_FNF_SWINGING_BLADE` | int | `473` |  |
| `VFX_DUR_INFERNO` | int | `474` |  |
| `VFX_FNF_DEMON_HAND` | int | `475` |  |
| `VFX_DUR_STONEHOLD` | int | `476` |  |
| `VFX_FNF_MYSTICAL_EXPLOSION` | int | `477` |  |
| `VFX_DUR_GHOSTLY_VISAGE_NO_SOUND` | int | `478` |  |
| `VFX_DUR_GHOST_SMOKE_2` | int | `479` |  |
| `VFX_DUR_FLIES` | int | `480` |  |
| `VFX_FNF_SUMMONDRAGON` | int | `481` |  |
| `VFX_BEAM_FIRE_W` | int | `482` |  |
| `VFX_BEAM_FIRE_W_SILENT` | int | `483` |  |
| `VFX_BEAM_CHAIN` | int | `484` |  |
| `VFX_BEAM_BLACK` | int | `485` |  |
| `VFX_IMP_WALLSPIKE` | int | `486` |  |
| `VFX_FNF_GREATER_RUIN` | int | `487` |  |
| `VFX_FNF_UNDEAD_DRAGON` | int | `488` |  |
| `VFX_DUR_PROT_EPIC_ARMOR` | int | `495` |  |
| `VFX_FNF_SUMMON_EPIC_UNDEAD` | int | `496` |  |
| `VFX_DUR_PROT_EPIC_ARMOR_2` | int | `497` |  |
| `VFX_DUR_INFERNO_CHEST` | int | `498` |  |
| `VFX_DUR_IOUNSTONE_RED` | int | `499` |  |
| `VFX_DUR_IOUNSTONE_BLUE` | int | `500` |  |
| `VFX_DUR_IOUNSTONE_YELLOW` | int | `501` |  |
| `VFX_DUR_IOUNSTONE_GREEN` | int | `502` |  |
| `VFX_IMP_MIRV_ELECTRIC` | int | `503` |  |
| `VFX_COM_CHUNK_RED_BALLISTA` | int | `504` |  |
| `VFX_DUR_INFERNO_NO_SOUND` | int | `505` |  |
| `VFX_DUR_AURA_PULSE_RED_WHITE` | int | `512` |  |
| `VFX_DUR_AURA_PULSE_BLUE_WHITE` | int | `513` |  |
| `VFX_DUR_AURA_PULSE_GREEN_WHITE` | int | `514` |  |
| `VFX_DUR_AURA_PULSE_YELLOW_WHITE` | int | `515` |  |
| `VFX_DUR_AURA_PULSE_MAGENTA_WHITE` | int | `516` |  |
| `VFX_DUR_AURA_PULSE_CYAN_WHITE` | int | `517` |  |
| `VFX_DUR_AURA_PULSE_ORANGE_WHITE` | int | `518` |  |
| `VFX_DUR_AURA_PULSE_BROWN_WHITE` | int | `519` |  |
| `VFX_DUR_AURA_PULSE_PURPLE_WHITE` | int | `520` |  |
| `VFX_DUR_AURA_PULSE_GREY_WHITE` | int | `521` |  |
| `VFX_DUR_AURA_PULSE_GREY_BLACK` | int | `522` |  |
| `VFX_DUR_AURA_PULSE_BLUE_GREEN` | int | `523` |  |
| `VFX_DUR_AURA_PULSE_RED_BLUE` | int | `524` |  |
| `VFX_DUR_AURA_PULSE_RED_YELLOW` | int | `525` |  |
| `VFX_DUR_AURA_PULSE_GREEN_YELLOW` | int | `526` |  |
| `VFX_DUR_AURA_PULSE_RED_GREEN` | int | `527` |  |
| `VFX_DUR_AURA_PULSE_BLUE_YELLOW` | int | `528` |  |
| `VFX_DUR_AURA_PULSE_BLUE_BLACK` | int | `529` |  |
| `VFX_DUR_AURA_PULSE_RED_BLACK` | int | `530` |  |
| `VFX_DUR_AURA_PULSE_GREEN_BLACK` | int | `531` |  |
| `VFX_DUR_AURA_PULSE_YELLOW_BLACK` | int | `532` |  |
| `VFX_DUR_AURA_PULSE_MAGENTA_BLACK` | int | `533` |  |
| `VFX_DUR_AURA_PULSE_CYAN_BLACK` | int | `534` |  |
| `VFX_DUR_AURA_PULSE_ORANGE_BLACK` | int | `535` |  |
| `VFX_DUR_AURA_PULSE_BROWN_BLACK` | int | `536` |  |
| `VFX_DUR_AURA_PULSE_PURPLE_BLACK` | int | `537` |  |
| `VFX_DUR_AURA_PULSE_CYAN_GREEN` | int | `538` |  |
| `VFX_DUR_AURA_PULSE_CYAN_BLUE` | int | `539` |  |
| `VFX_DUR_AURA_PULSE_CYAN_RED` | int | `540` |  |
| `VFX_DUR_AURA_PULSE_CYAN_YELLOW` | int | `541` |  |
| `VFX_DUR_AURA_PULSE_MAGENTA_BLUE` | int | `542` |  |
| `VFX_DUR_AURA_PULSE_MAGENTA_RED` | int | `543` |  |
| `VFX_DUR_AURA_PULSE_MAGENTA_GREEN` | int | `544` |  |
| `VFX_DUR_AURA_PULSE_MAGENTA_YELLOW` | int | `545` |  |
| `VFX_DUR_AURA_PULSE_RED_ORANGE` | int | `546` |  |
| `VFX_DUR_AURA_PULSE_YELLOW_ORANGE` | int | `547` |  |
| `VFX_DUR_AURA_RED` | int | `548` |  |
| `VFX_DUR_AURA_GREEN` | int | `549` |  |
| `VFX_DUR_AURA_BLUE` | int | `550` |  |
| `VFX_DUR_AURA_MAGENTA` | int | `551` |  |
| `VFX_DUR_AURA_YELLOW` | int | `552` |  |
| `VFX_DUR_AURA_WHITE` | int | `553` |  |
| `VFX_DUR_AURA_ORANGE` | int | `554` |  |
| `VFX_DUR_AURA_BROWN` | int | `555` |  |
| `VFX_DUR_AURA_PURPLE` | int | `556` |  |
| `VFX_DUR_AURA_CYAN` | int | `557` |  |
| `VFX_DUR_AURA_GREEN_DARK` | int | `558` |  |
| `VFX_DUR_AURA_GREEN_LIGHT` | int | `559` |  |
| `VFX_DUR_AURA_RED_DARK` | int | `560` |  |
| `VFX_DUR_AURA_RED_LIGHT` | int | `561` |  |
| `VFX_DUR_AURA_BLUE_DARK` | int | `562` |  |
| `VFX_DUR_AURA_BLUE_LIGHT` | int | `563` |  |
| `VFX_DUR_AURA_YELLOW_DARK` | int | `564` |  |
| `VFX_DUR_AURA_YELLOW_LIGHT` | int | `565` |  |
| `VFX_DUR_BUBBLES` | int | `566` |  |
| `VFX_EYES_GREEN_HUMAN_MALE` | int | `567` |  |
| `VFX_EYES_GREEN_HUMAN_FEMALE` | int | `568` |  |
| `VFX_EYES_GREEN_HALFELF_MALE` | int | `567` |  |
| `VFX_EYES_GREEN_HALFELF_FEMALE` | int | `568` |  |
| `VFX_EYES_GREEN_DWARF_MALE` | int | `569` |  |
| `VFX_EYES_GREEN_DWARF_FEMALE` | int | `570` |  |
| `VFX_EYES_GREEN_ELF_MALE` | int | `571` |  |
| `VFX_EYES_GREEN_ELF_FEMALE` | int | `572` |  |
| `VFX_EYES_GREEN_GNOME_MALE` | int | `573` |  |
| `VFX_EYES_GREEN_GNOME_FEMALE` | int | `574` |  |
| `VFX_EYES_GREEN_HALFLING_MALE` | int | `575` |  |
| `VFX_EYES_GREEN_HALFLING_FEMALE` | int | `576` |  |
| `VFX_EYES_GREEN_HALFORC_MALE` | int | `577` |  |
| `VFX_EYES_GREEN_HALFORC_FEMALE` | int | `578` |  |
| `VFX_EYES_GREEN_TROGLODYTE` | int | `579` |  |
| `VFX_EYES_PUR_HUMAN_MALE` | int | `580` |  |
| `VFX_EYES_PUR_HUMAN_FEMALE` | int | `581` |  |
| `VFX_EYES_PUR_DWARF_MALE` | int | `582` |  |
| `VFX_EYES_PUR_DWARF_FEMALE` | int | `583` |  |
| `VFX_EYES_PUR_ELF_MALE` | int | `584` |  |
| `VFX_EYES_PUR_ELF_FEMALE` | int | `585` |  |
| `VFX_EYES_PUR_GNOME_MALE` | int | `586` |  |
| `VFX_EYES_PUR_GNOME_FEMALE` | int | `587` |  |
| `VFX_EYES_PUR_HALFLING_MALE` | int | `588` |  |
| `VFX_EYES_PUR_HALFLING_FEMALE` | int | `589` |  |
| `VFX_EYES_PUR_HALFORC_MALE` | int | `590` |  |
| `VFX_EYES_PUR_HALFORC_FEMALE` | int | `591` |  |
| `VFX_EYES_PUR_TROGLODYTE` | int | `592` |  |
| `VFX_EYES_CYN_HUMAN_MALE` | int | `593` |  |
| `VFX_EYES_CYN_HUMAN_FEMALE` | int | `594` |  |
| `VFX_EYES_CYN_DWARF_MALE` | int | `595` |  |
| `VFX_EYES_CYN_DWARF_FEMALE` | int | `596` |  |
| `VFX_EYES_CYN_ELF_MALE` | int | `597` |  |
| `VFX_EYES_CYN_ELF_FEMALE` | int | `598` |  |
| `VFX_EYES_CYN_GNOME_MALE` | int | `599` |  |
| `VFX_EYES_CYN_GNOME_FEMALE` | int | `600` |  |
| `VFX_EYES_CYN_HALFLING_MALE` | int | `601` |  |
| `VFX_EYES_CYN_HALFLING_FEMALE` | int | `602` |  |
| `VFX_EYES_CYN_HALFORC_MALE` | int | `603` |  |
| `VFX_EYES_CYN_HALFORC_FEMALE` | int | `604` |  |
| `VFX_EYES_CYN_TROGLODYTE` | int | `605` |  |
| `VFX_EYES_WHT_HUMAN_MALE` | int | `606` |  |
| `VFX_EYES_WHT_HUMAN_FEMALE` | int | `607` |  |
| `VFX_EYES_WHT_DWARF_MALE` | int | `608` |  |
| `VFX_EYES_WHT_DWARF_FEMALE` | int | `609` |  |
| `VFX_EYES_WHT_ELF_MALE` | int | `610` |  |
| `VFX_EYES_WHT_ELF_FEMALE` | int | `611` |  |
| `VFX_EYES_WHT_GNOME_MALE` | int | `612` |  |
| `VFX_EYES_WHT_GNOME_FEMALE` | int | `613` |  |
| `VFX_EYES_WHT_HALFLING_MALE` | int | `614` |  |
| `VFX_EYES_WHT_HALFLING_FEMALE` | int | `615` |  |
| `VFX_EYES_WHT_HALFORC_MALE` | int | `616` |  |
| `VFX_EYES_WHT_HALFORC_FEMALE` | int | `617` |  |
| `VFX_EYES_WHT_TROGLODYTE` | int | `618` |  |
| `VFX_IMP_PDK_GENERIC_PULSE` | int | `623` |  |
| `VFX_IMP_PDK_GENERIC_HEAD_HIT` | int | `624` |  |
| `VFX_IMP_PDK_RALLYING_CRY` | int | `625` |  |
| `VFX_IMP_PDK_HEROIC_SHIELD` | int | `626` |  |
| `VFX_IMP_PDK_INSPIRE_COURAGE` | int | `627` |  |
| `VFX_DUR_PDK_FEAR` | int | `628` |  |
| `VFX_IMP_PDK_WRATH` | int | `629` |  |
| `VFX_IMP_PDK_OATH` | int | `630` |  |
| `VFX_IMP_PDK_FINAL_STAND` | int | `631` |  |
| `VFX_DUR_ARROW_IN_STERNUM` | int | `632` |  |
| `VFX_DUR_ARROW_IN_CHEST_LEFT` | int | `633` |  |
| `VFX_DUR_ARROW_IN_CHEST_RIGHT` | int | `634` |  |
| `VFX_DUR_ARROW_IN_BACK` | int | `635` |  |
| `VFX_DUR_ARROW_IN_TEMPLES` | int | `636` |  |
| `VFX_DUR_ARROW_IN_FACE` | int | `637` |  |
| `VFX_DUR_ARROW_IN_HEAD` | int | `638` |  |
| `VFX_DUR_QUILL_IN_CHEST` | int | `639` |  |
| `VFX_IMP_STARBURST_GREEN` | int | `644` |  |
| `VFX_IMP_STARBURST_RED` | int | `645` |  |
| `VFX_IMP_NIGHTMARE_HEAD_HIT` | int | `670` |  |
| `AOE_PER_FOGACID` | int | `0` |  |
| `AOE_PER_FOGFIRE` | int | `1` |  |
| `AOE_PER_FOGSTINK` | int | `2` |  |
| `AOE_PER_FOGKILL` | int | `3` |  |
| `AOE_PER_FOGMIND` | int | `4` |  |
| `AOE_PER_WALLFIRE` | int | `5` |  |
| `AOE_PER_WALLWIND` | int | `6` |  |
| `AOE_PER_WALLBLADE` | int | `7` |  |
| `AOE_PER_WEB` | int | `8` |  |
| `AOE_PER_ENTANGLE` | int | `9` |  |
| `AOE_PER_DARKNESS` | int | `11` |  |
| `AOE_MOB_CIRCEVIL` | int | `12` |  |
| `AOE_MOB_CIRCGOOD` | int | `13` |  |
| `AOE_MOB_CIRCLAW` | int | `14` |  |
| `AOE_MOB_CIRCCHAOS` | int | `15` |  |
| `AOE_MOB_FEAR` | int | `16` |  |
| `AOE_MOB_BLINDING` | int | `17` |  |
| `AOE_MOB_UNEARTHLY` | int | `18` |  |
| `AOE_MOB_MENACE` | int | `19` |  |
| `AOE_MOB_UNNATURAL` | int | `20` |  |
| `AOE_MOB_STUN` | int | `21` |  |
| `AOE_MOB_PROTECTION` | int | `22` |  |
| `AOE_MOB_FIRE` | int | `23` |  |
| `AOE_MOB_FROST` | int | `24` |  |
| `AOE_MOB_ELECTRICAL` | int | `25` |  |
| `AOE_PER_FOGGHOUL` | int | `26` |  |
| `AOE_MOB_TYRANT_FOG` | int | `27` |  |
| `AOE_PER_STORM` | int | `28` |  |
| `AOE_PER_INVIS_SPHERE` | int | `29` |  |
| `AOE_MOB_SILENCE` | int | `30` |  |
| `AOE_PER_DELAY_BLAST_FIREBALL` | int | `31` |  |
| `AOE_PER_GREASE` | int | `32` |  |
| `AOE_PER_CREEPING_DOOM` | int | `33` |  |
| `AOE_PER_EVARDS_BLACK_TENTACLES` | int | `34` |  |
| `AOE_MOB_INVISIBILITY_PURGE` | int | `35` |  |
| `AOE_MOB_DRAGON_FEAR` | int | `36` |  |
| `AOE_PER_CUSTOM_AOE` | int | `37` |  |
| `AOE_PER_GLYPH_OF_WARDING` | int | `38` |  |
| `AOE_PER_FOG_OF_BEWILDERMENT` | int | `39` |  |
| `AOE_PER_VINE_MINE_CAMOUFLAGE` | int | `40` |  |
| `AOE_MOB_TIDE_OF_BATTLE` | int | `41` |  |
| `AOE_PER_STONEHOLD` | int | `42` |  |
| `AOE_PER_OVERMIND` | int | `43` |  |
| `AOE_MOB_HORRIFICAPPEARANCE` | int | `44` |  |
| `AOE_MOB_TROGLODYTE_STENCH` | int | `45` |  |
| `SPELL_ALL_SPELLS` | int | `-1` | used for spell immunity. |
| `SPELL_ACID_FOG` | int | `0` |  |
| `SPELL_AID` | int | `1` |  |
| `SPELL_ANIMATE_DEAD` | int | `2` |  |
| `SPELL_BARKSKIN` | int | `3` |  |
| `SPELL_BESTOW_CURSE` | int | `4` |  |
| `SPELL_BLADE_BARRIER` | int | `5` |  |
| `SPELL_BLESS` | int | `6` |  |
| `SPELL_BLESS_WEAPON` | int | `537` |  |
| `SPELL_BLINDNESS_AND_DEAFNESS` | int | `8` |  |
| `SPELL_BULLS_STRENGTH` | int | `9` |  |
| `SPELL_BURNING_HANDS` | int | `10` |  |
| `SPELL_CALL_LIGHTNING` | int | `11` |  |
| `SPELL_CATS_GRACE` | int | `13` |  |
| `SPELL_CHAIN_LIGHTNING` | int | `14` |  |
| `SPELL_CHARM_MONSTER` | int | `15` |  |
| `SPELL_CHARM_PERSON` | int | `16` |  |
| `SPELL_CHARM_PERSON_OR_ANIMAL` | int | `17` |  |
| `SPELL_CIRCLE_OF_DEATH` | int | `18` |  |
| `SPELL_CIRCLE_OF_DOOM` | int | `19` |  |
| `SPELL_CLAIRAUDIENCE_AND_CLAIRVOYANCE` | int | `20` |  |
| `SPELL_CLARITY` | int | `21` |  |
| `SPELL_CLOAK_OF_CHAOS` | int | `22` |  |
| `SPELL_CLOUDKILL` | int | `23` |  |
| `SPELL_COLOR_SPRAY` | int | `24` |  |
| `SPELL_CONE_OF_COLD` | int | `25` |  |
| `SPELL_CONFUSION` | int | `26` |  |
| `SPELL_CONTAGION` | int | `27` |  |
| `SPELL_CONTROL_UNDEAD` | int | `28` |  |
| `SPELL_CREATE_GREATER_UNDEAD` | int | `29` |  |
| `SPELL_CREATE_UNDEAD` | int | `30` |  |
| `SPELL_CURE_CRITICAL_WOUNDS` | int | `31` |  |
| `SPELL_CURE_LIGHT_WOUNDS` | int | `32` |  |
| `SPELL_CURE_MINOR_WOUNDS` | int | `33` |  |
| `SPELL_CURE_MODERATE_WOUNDS` | int | `34` |  |
| `SPELL_CURE_SERIOUS_WOUNDS` | int | `35` |  |
| `SPELL_DARKNESS` | int | `36` |  |
| `SPELL_DAZE` | int | `37` |  |
| `SPELL_DEATH_WARD` | int | `38` |  |
| `SPELL_DELAYED_BLAST_FIREBALL` | int | `39` |  |
| `SPELL_DISMISSAL` | int | `40` |  |
| `SPELL_DISPEL_MAGIC` | int | `41` |  |
| `SPELL_DIVINE_POWER` | int | `42` |  |
| `SPELL_DOMINATE_ANIMAL` | int | `43` |  |
| `SPELL_DOMINATE_MONSTER` | int | `44` |  |
| `SPELL_DOMINATE_PERSON` | int | `45` |  |
| `SPELL_DOOM` | int | `46` |  |
| `SPELL_ELEMENTAL_SHIELD` | int | `47` |  |
| `SPELL_ELEMENTAL_SWARM` | int | `48` |  |
| `SPELL_ENDURANCE` | int | `49` |  |
| `SPELL_ENDURE_ELEMENTS` | int | `50` |  |
| `SPELL_ENERGY_DRAIN` | int | `51` |  |
| `SPELL_ENERVATION` | int | `52` |  |
| `SPELL_ENTANGLE` | int | `53` |  |
| `SPELL_FEAR` | int | `54` |  |
| `SPELL_FEEBLEMIND` | int | `55` |  |
| `SPELL_FINGER_OF_DEATH` | int | `56` |  |
| `SPELL_FIRE_STORM` | int | `57` |  |
| `SPELL_FIREBALL` | int | `58` |  |
| `SPELL_FLAME_ARROW` | int | `59` |  |
| `SPELL_FLAME_LASH` | int | `60` |  |
| `SPELL_FLAME_STRIKE` | int | `61` |  |
| `SPELL_FREEDOM_OF_MOVEMENT` | int | `62` |  |
| `SPELL_GATE` | int | `63` |  |
| `SPELL_GHOUL_TOUCH` | int | `64` |  |
| `SPELL_GLOBE_OF_INVULNERABILITY` | int | `65` |  |
| `SPELL_GREASE` | int | `66` |  |
| `SPELL_GREATER_DISPELLING` | int | `67` |  |
| `SPELL_GREATER_PLANAR_BINDING` | int | `69` |  |
| `SPELL_GREATER_RESTORATION` | int | `70` |  |
| `SPELL_GREATER_SPELL_BREACH` | int | `72` |  |
| `SPELL_GREATER_SPELL_MANTLE` | int | `73` |  |
| `SPELL_GREATER_STONESKIN` | int | `74` |  |
| `SPELL_GUST_OF_WIND` | int | `75` |  |
| `SPELL_HAMMER_OF_THE_GODS` | int | `76` |  |
| `SPELL_HARM` | int | `77` |  |
| `SPELL_HASTE` | int | `78` |  |
| `SPELL_HEAL` | int | `79` |  |
| `SPELL_HEALING_CIRCLE` | int | `80` |  |
| `SPELL_HOLD_ANIMAL` | int | `81` |  |
| `SPELL_HOLD_MONSTER` | int | `82` |  |
| `SPELL_HOLD_PERSON` | int | `83` |  |
| `SPELL_HOLY_AURA` | int | `84` |  |
| `SPELL_HOLY_SWORD` | int | `538` |  |
| `SPELL_IDENTIFY` | int | `86` |  |
| `SPELL_IMPLOSION` | int | `87` |  |
| `SPELL_IMPROVED_INVISIBILITY` | int | `88` |  |
| `SPELL_INCENDIARY_CLOUD` | int | `89` |  |
| `SPELL_INVISIBILITY` | int | `90` |  |
| `SPELL_INVISIBILITY_PURGE` | int | `91` |  |
| `SPELL_INVISIBILITY_SPHERE` | int | `92` |  |
| `SPELL_KNOCK` | int | `93` |  |
| `SPELL_LESSER_DISPEL` | int | `94` |  |
| `SPELL_LESSER_MIND_BLANK` | int | `95` |  |
| `SPELL_LESSER_PLANAR_BINDING` | int | `96` |  |
| `SPELL_LESSER_RESTORATION` | int | `97` |  |
| `SPELL_LESSER_SPELL_BREACH` | int | `98` |  |
| `SPELL_LESSER_SPELL_MANTLE` | int | `99` |  |
| `SPELL_LIGHT` | int | `100` |  |
| `SPELL_LIGHTNING_BOLT` | int | `101` |  |
| `SPELL_MAGE_ARMOR` | int | `102` |  |
| `SPELL_MAGIC_CIRCLE_AGAINST_CHAOS` | int | `103` |  |
| `SPELL_MAGIC_CIRCLE_AGAINST_EVIL` | int | `104` |  |
| `SPELL_MAGIC_CIRCLE_AGAINST_GOOD` | int | `105` |  |
| `SPELL_MAGIC_CIRCLE_AGAINST_LAW` | int | `106` |  |
| `SPELL_MAGIC_MISSILE` | int | `107` |  |
| `SPELL_MAGIC_VESTMENT` | int | `546` |  |
| `SPELL_MASS_BLINDNESS_AND_DEAFNESS` | int | `110` |  |
| `SPELL_MASS_CHARM` | int | `111` |  |
| `SPELL_MASS_HASTE` | int | `113` |  |
| `SPELL_MASS_HEAL` | int | `114` |  |
| `SPELL_MELFS_ACID_ARROW` | int | `115` |  |
| `SPELL_METEOR_SWARM` | int | `116` |  |
| `SPELL_MIND_BLANK` | int | `117` |  |
| `SPELL_MIND_FOG` | int | `118` |  |
| `SPELL_MINOR_GLOBE_OF_INVULNERABILITY` | int | `119` |  |
| `SPELL_GHOSTLY_VISAGE` | int | `120` |  |
| `SPELL_ETHEREAL_VISAGE` | int | `121` |  |
| `SPELL_MORDENKAINENS_DISJUNCTION` | int | `122` |  |
| `SPELL_MORDENKAINENS_SWORD` | int | `123` |  |
| `SPELL_NATURES_BALANCE` | int | `124` |  |
| `SPELL_NEGATIVE_ENERGY_PROTECTION` | int | `125` |  |
| `SPELL_NEUTRALIZE_POISON` | int | `126` |  |
| `SPELL_PHANTASMAL_KILLER` | int | `127` |  |
| `SPELL_PLANAR_BINDING` | int | `128` |  |
| `SPELL_POISON` | int | `129` |  |
| `SPELL_POLYMORPH_SELF` | int | `130` |  |
| `SPELL_POWER_WORD_KILL` | int | `131` |  |
| `SPELL_POWER_WORD_STUN` | int | `132` |  |
| `SPELL_PRAYER` | int | `133` |  |
| `SPELL_PREMONITION` | int | `134` |  |
| `SPELL_PRISMATIC_SPRAY` | int | `135` |  |
| `SPELL_PROTECTION__FROM_CHAOS` | int | `136` |  |
| `SPELL_PROTECTION_FROM_ELEMENTS` | int | `137` |  |
| `SPELL_PROTECTION_FROM_EVIL` | int | `138` |  |
| `SPELL_PROTECTION_FROM_GOOD` | int | `139` |  |
| `SPELL_PROTECTION_FROM_LAW` | int | `140` |  |
| `SPELL_PROTECTION_FROM_SPELLS` | int | `141` |  |
| `SPELL_RAISE_DEAD` | int | `142` |  |
| `SPELL_RAY_OF_ENFEEBLEMENT` | int | `143` |  |
| `SPELL_RAY_OF_FROST` | int | `144` |  |
| `SPELL_REMOVE_BLINDNESS_AND_DEAFNESS` | int | `145` |  |
| `SPELL_REMOVE_CURSE` | int | `146` |  |
| `SPELL_REMOVE_DISEASE` | int | `147` |  |
| `SPELL_REMOVE_FEAR` | int | `148` |  |
| `SPELL_REMOVE_PARALYSIS` | int | `149` |  |
| `SPELL_RESIST_ELEMENTS` | int | `150` |  |
| `SPELL_RESISTANCE` | int | `151` |  |
| `SPELL_RESTORATION` | int | `152` |  |
| `SPELL_RESURRECTION` | int | `153` |  |
| `SPELL_SANCTUARY` | int | `154` |  |
| `SPELL_SCARE` | int | `155` |  |
| `SPELL_SEARING_LIGHT` | int | `156` |  |
| `SPELL_SEE_INVISIBILITY` | int | `157` |  |
| `SPELL_SHADOW_SHIELD` | int | `160` |  |
| `SPELL_SHAPECHANGE` | int | `161` |  |
| `SPELL_SHIELD_OF_LAW` | int | `162` |  |
| `SPELL_SILENCE` | int | `163` |  |
| `SPELL_SLAY_LIVING` | int | `164` |  |
| `SPELL_SLEEP` | int | `165` |  |
| `SPELL_SLOW` | int | `166` |  |
| `SPELL_SOUND_BURST` | int | `167` |  |
| `SPELL_SPELL_RESISTANCE` | int | `168` |  |
| `SPELL_SPELL_MANTLE` | int | `169` |  |
| `SPELL_SPHERE_OF_CHAOS` | int | `170` |  |
| `SPELL_STINKING_CLOUD` | int | `171` |  |
| `SPELL_STONESKIN` | int | `172` |  |
| `SPELL_STORM_OF_VENGEANCE` | int | `173` |  |
| `SPELL_SUMMON_CREATURE_I` | int | `174` |  |
| `SPELL_SUMMON_CREATURE_II` | int | `175` |  |
| `SPELL_SUMMON_CREATURE_III` | int | `176` |  |
| `SPELL_SUMMON_CREATURE_IV` | int | `177` |  |
| `SPELL_SUMMON_CREATURE_IX` | int | `178` |  |
| `SPELL_SUMMON_CREATURE_V` | int | `179` |  |
| `SPELL_SUMMON_CREATURE_VI` | int | `180` |  |
| `SPELL_SUMMON_CREATURE_VII` | int | `181` |  |
| `SPELL_SUMMON_CREATURE_VIII` | int | `182` |  |
| `SPELL_SUNBEAM` | int | `183` |  |
| `SPELL_TENSERS_TRANSFORMATION` | int | `184` |  |
| `SPELL_TIME_STOP` | int | `185` |  |
| `SPELL_TRUE_SEEING` | int | `186` |  |
| `SPELL_UNHOLY_AURA` | int | `187` |  |
| `SPELL_VAMPIRIC_TOUCH` | int | `188` |  |
| `SPELL_VIRTUE` | int | `189` |  |
| `SPELL_WAIL_OF_THE_BANSHEE` | int | `190` |  |
| `SPELL_WALL_OF_FIRE` | int | `191` |  |
| `SPELL_WEB` | int | `192` |  |
| `SPELL_WEIRD` | int | `193` |  |
| `SPELL_WORD_OF_FAITH` | int | `194` |  |
| `SPELLABILITY_AURA_BLINDING` | int | `195` |  |
| `SPELLABILITY_AURA_COLD` | int | `196` |  |
| `SPELLABILITY_AURA_ELECTRICITY` | int | `197` |  |
| `SPELLABILITY_AURA_FEAR` | int | `198` |  |
| `SPELLABILITY_AURA_FIRE` | int | `199` |  |
| `SPELLABILITY_AURA_MENACE` | int | `200` |  |
| `SPELLABILITY_AURA_PROTECTION` | int | `201` |  |
| `SPELLABILITY_AURA_STUN` | int | `202` |  |
| `SPELLABILITY_AURA_UNEARTHLY_VISAGE` | int | `203` |  |
| `SPELLABILITY_AURA_UNNATURAL` | int | `204` |  |
| `SPELLABILITY_BOLT_ABILITY_DRAIN_CHARISMA` | int | `205` |  |
| `SPELLABILITY_BOLT_ABILITY_DRAIN_CONSTITUTION` | int | `206` |  |
| `SPELLABILITY_BOLT_ABILITY_DRAIN_DEXTERITY` | int | `207` |  |
| `SPELLABILITY_BOLT_ABILITY_DRAIN_INTELLIGENCE` | int | `208` |  |
| `SPELLABILITY_BOLT_ABILITY_DRAIN_STRENGTH` | int | `209` |  |
| `SPELLABILITY_BOLT_ABILITY_DRAIN_WISDOM` | int | `210` |  |
| `SPELLABILITY_BOLT_ACID` | int | `211` |  |
| `SPELLABILITY_BOLT_CHARM` | int | `212` |  |
| `SPELLABILITY_BOLT_COLD` | int | `213` |  |
| `SPELLABILITY_BOLT_CONFUSE` | int | `214` |  |
| `SPELLABILITY_BOLT_DAZE` | int | `215` |  |
| `SPELLABILITY_BOLT_DEATH` | int | `216` |  |
| `SPELLABILITY_BOLT_DISEASE` | int | `217` |  |
| `SPELLABILITY_BOLT_DOMINATE` | int | `218` |  |
| `SPELLABILITY_BOLT_FIRE` | int | `219` |  |
| `SPELLABILITY_BOLT_KNOCKDOWN` | int | `220` |  |
| `SPELLABILITY_BOLT_LEVEL_DRAIN` | int | `221` |  |
| `SPELLABILITY_BOLT_LIGHTNING` | int | `222` |  |
| `SPELLABILITY_BOLT_PARALYZE` | int | `223` |  |
| `SPELLABILITY_BOLT_POISON` | int | `224` |  |
| `SPELLABILITY_BOLT_SHARDS` | int | `225` |  |
| `SPELLABILITY_BOLT_SLOW` | int | `226` |  |
| `SPELLABILITY_BOLT_STUN` | int | `227` |  |
| `SPELLABILITY_BOLT_WEB` | int | `228` |  |
| `SPELLABILITY_CONE_ACID` | int | `229` |  |
| `SPELLABILITY_CONE_COLD` | int | `230` |  |
| `SPELLABILITY_CONE_DISEASE` | int | `231` |  |
| `SPELLABILITY_CONE_FIRE` | int | `232` |  |
| `SPELLABILITY_CONE_LIGHTNING` | int | `233` |  |
| `SPELLABILITY_CONE_POISON` | int | `234` |  |
| `SPELLABILITY_CONE_SONIC` | int | `235` |  |
| `SPELLABILITY_DRAGON_BREATH_ACID` | int | `236` |  |
| `SPELLABILITY_DRAGON_BREATH_COLD` | int | `237` |  |
| `SPELLABILITY_DRAGON_BREATH_FEAR` | int | `238` |  |
| `SPELLABILITY_DRAGON_BREATH_FIRE` | int | `239` |  |
| `SPELLABILITY_DRAGON_BREATH_GAS` | int | `240` |  |
| `SPELLABILITY_DRAGON_BREATH_LIGHTNING` | int | `241` |  |
| `SPELLABILITY_DRAGON_BREATH_PARALYZE` | int | `242` |  |
| `SPELLABILITY_DRAGON_BREATH_SLEEP` | int | `243` |  |
| `SPELLABILITY_DRAGON_BREATH_SLOW` | int | `244` |  |
| `SPELLABILITY_DRAGON_BREATH_WEAKEN` | int | `245` |  |
| `SPELLABILITY_DRAGON_WING_BUFFET` | int | `246` |  |
| `SPELLABILITY_FEROCITY_1` | int | `247` |  |
| `SPELLABILITY_FEROCITY_2` | int | `248` |  |
| `SPELLABILITY_FEROCITY_3` | int | `249` |  |
| `SPELLABILITY_GAZE_CHARM` | int | `250` |  |
| `SPELLABILITY_GAZE_CONFUSION` | int | `251` |  |
| `SPELLABILITY_GAZE_DAZE` | int | `252` |  |
| `SPELLABILITY_GAZE_DEATH` | int | `253` |  |
| `SPELLABILITY_GAZE_DESTROY_CHAOS` | int | `254` |  |
| `SPELLABILITY_GAZE_DESTROY_EVIL` | int | `255` |  |
| `SPELLABILITY_GAZE_DESTROY_GOOD` | int | `256` |  |
| `SPELLABILITY_GAZE_DESTROY_LAW` | int | `257` |  |
| `SPELLABILITY_GAZE_DOMINATE` | int | `258` |  |
| `SPELLABILITY_GAZE_DOOM` | int | `259` |  |
| `SPELLABILITY_GAZE_FEAR` | int | `260` |  |
| `SPELLABILITY_GAZE_PARALYSIS` | int | `261` |  |
| `SPELLABILITY_GAZE_STUNNED` | int | `262` |  |
| `SPELLABILITY_GOLEM_BREATH_GAS` | int | `263` |  |
| `SPELLABILITY_HELL_HOUND_FIREBREATH` | int | `264` |  |
| `SPELLABILITY_HOWL_CONFUSE` | int | `265` |  |
| `SPELLABILITY_HOWL_DAZE` | int | `266` |  |
| `SPELLABILITY_HOWL_DEATH` | int | `267` |  |
| `SPELLABILITY_HOWL_DOOM` | int | `268` |  |
| `SPELLABILITY_HOWL_FEAR` | int | `269` |  |
| `SPELLABILITY_HOWL_PARALYSIS` | int | `270` |  |
| `SPELLABILITY_HOWL_SONIC` | int | `271` |  |
| `SPELLABILITY_HOWL_STUN` | int | `272` |  |
| `SPELLABILITY_INTENSITY_1` | int | `273` |  |
| `SPELLABILITY_INTENSITY_2` | int | `274` |  |
| `SPELLABILITY_INTENSITY_3` | int | `275` |  |
| `SPELLABILITY_KRENSHAR_SCARE` | int | `276` |  |
| `SPELLABILITY_LESSER_BODY_ADJUSTMENT` | int | `277` |  |
| `SPELLABILITY_MEPHIT_SALT_BREATH` | int | `278` |  |
| `SPELLABILITY_MEPHIT_STEAM_BREATH` | int | `279` |  |
| `SPELLABILITY_MUMMY_BOLSTER_UNDEAD` | int | `280` |  |
| `SPELLABILITY_PULSE_DROWN` | int | `281` |  |
| `SPELLABILITY_PULSE_SPORES` | int | `282` |  |
| `SPELLABILITY_PULSE_WHIRLWIND` | int | `283` |  |
| `SPELLABILITY_PULSE_FIRE` | int | `284` |  |
| `SPELLABILITY_PULSE_LIGHTNING` | int | `285` |  |
| `SPELLABILITY_PULSE_COLD` | int | `286` |  |
| `SPELLABILITY_PULSE_NEGATIVE` | int | `287` |  |
| `SPELLABILITY_PULSE_HOLY` | int | `288` |  |
| `SPELLABILITY_PULSE_DEATH` | int | `289` |  |
| `SPELLABILITY_PULSE_LEVEL_DRAIN` | int | `290` |  |
| `SPELLABILITY_PULSE_ABILITY_DRAIN_INTELLIGENCE` | int | `291` |  |
| `SPELLABILITY_PULSE_ABILITY_DRAIN_CHARISMA` | int | `292` |  |
| `SPELLABILITY_PULSE_ABILITY_DRAIN_CONSTITUTION` | int | `293` |  |
| `SPELLABILITY_PULSE_ABILITY_DRAIN_DEXTERITY` | int | `294` |  |
| `SPELLABILITY_PULSE_ABILITY_DRAIN_STRENGTH` | int | `295` |  |
| `SPELLABILITY_PULSE_ABILITY_DRAIN_WISDOM` | int | `296` |  |
| `SPELLABILITY_PULSE_POISON` | int | `297` |  |
| `SPELLABILITY_PULSE_DISEASE` | int | `298` |  |
| `SPELLABILITY_RAGE_3` | int | `299` |  |
| `SPELLABILITY_RAGE_4` | int | `300` |  |
| `SPELLABILITY_RAGE_5` | int | `301` |  |
| `SPELLABILITY_SMOKE_CLAW` | int | `302` |  |
| `SPELLABILITY_SUMMON_SLAAD` | int | `303` |  |
| `SPELLABILITY_SUMMON_TANARRI` | int | `304` |  |
| `SPELLABILITY_TRUMPET_BLAST` | int | `305` |  |
| `SPELLABILITY_TYRANT_FOG_MIST` | int | `306` |  |
| `SPELLABILITY_BARBARIAN_RAGE` | int | `307` |  |
| `SPELLABILITY_TURN_UNDEAD` | int | `308` |  |
| `SPELLABILITY_WHOLENESS_OF_BODY` | int | `309` |  |
| `SPELLABILITY_QUIVERING_PALM` | int | `310` |  |
| `SPELLABILITY_EMPTY_BODY` | int | `311` |  |
| `SPELLABILITY_DETECT_EVIL` | int | `312` |  |
| `SPELLABILITY_LAY_ON_HANDS` | int | `313` |  |
| `SPELLABILITY_AURA_OF_COURAGE` | int | `314` |  |
| `SPELLABILITY_SMITE_EVIL` | int | `315` |  |
| `SPELLABILITY_REMOVE_DISEASE` | int | `316` |  |
| `SPELLABILITY_SUMMON_ANIMAL_COMPANION` | int | `317` |  |
| `SPELLABILITY_SUMMON_FAMILIAR` | int | `318` |  |
| `SPELLABILITY_ELEMENTAL_SHAPE` | int | `319` |  |
| `SPELLABILITY_WILD_SHAPE` | int | `320` |  |
| `SPELL_SHADES_SUMMON_SHADOW` | int | `324` |  |
| `SPELL_SHADES_CONE_OF_COLD` | int | `340` |  |
| `SPELL_SHADES_FIREBALL` | int | `341` |  |
| `SPELL_SHADES_STONESKIN` | int | `342` |  |
| `SPELL_SHADES_WALL_OF_FIRE` | int | `343` |  |
| `SPELL_SHADOW_CONJURATION_SUMMON_SHADOW` | int | `344` |  |
| `SPELL_SHADOW_CONJURATION_DARKNESS` | int | `345` |  |
| `SPELL_SHADOW_CONJURATION_INIVSIBILITY` | int | `346` |  |
| `SPELL_SHADOW_CONJURATION_MAGE_ARMOR` | int | `347` |  |
| `SPELL_SHADOW_CONJURATION_MAGIC_MISSILE` | int | `348` |  |
| `SPELL_GREATER_SHADOW_CONJURATION_SUMMON_SHADOW` | int | `349` |  |
| `SPELL_GREATER_SHADOW_CONJURATION_ACID_ARROW` | int | `350` |  |
| `SPELL_GREATER_SHADOW_CONJURATION_MIRROR_IMAGE` | int | `351` |  |
| `SPELL_GREATER_SHADOW_CONJURATION_WEB` | int | `352` |  |
| `SPELL_GREATER_SHADOW_CONJURATION_MINOR_GLOBE` | int | `353` |  |
| `SPELL_EAGLE_SPLEDOR` | int | `354` |  |
| `SPELL_OWLS_WISDOM` | int | `355` |  |
| `SPELL_FOXS_CUNNING` | int | `356` |  |
| `SPELL_GREATER_EAGLE_SPLENDOR` | int | `357` |  |
| `SPELL_GREATER_OWLS_WISDOM` | int | `358` |  |
| `SPELL_GREATER_FOXS_CUNNING` | int | `359` |  |
| `SPELL_GREATER_BULLS_STRENGTH` | int | `360` |  |
| `SPELL_GREATER_CATS_GRACE` | int | `361` |  |
| `SPELL_GREATER_ENDURANCE` | int | `362` |  |
| `SPELL_AWAKEN` | int | `363` |  |
| `SPELL_CREEPING_DOOM` | int | `364` |  |
| `SPELL_DARKVISION` | int | `365` |  |
| `SPELL_DESTRUCTION` | int | `366` |  |
| `SPELL_HORRID_WILTING` | int | `367` |  |
| `SPELL_ICE_STORM` | int | `368` |  |
| `SPELL_ENERGY_BUFFER` | int | `369` |  |
| `SPELL_NEGATIVE_ENERGY_BURST` | int | `370` |  |
| `SPELL_NEGATIVE_ENERGY_RAY` | int | `371` |  |
| `SPELL_AURA_OF_VITALITY` | int | `372` |  |
| `SPELL_WAR_CRY` | int | `373` |  |
| `SPELL_REGENERATE` | int | `374` |  |
| `SPELL_EVARDS_BLACK_TENTACLES` | int | `375` |  |
| `SPELL_LEGEND_LORE` | int | `376` |  |
| `SPELL_FIND_TRAPS` | int | `377` |  |
| `SPELLABILITY_SUMMON_MEPHIT` | int | `378` |  |
| `SPELLABILITY_SUMMON_CELESTIAL` | int | `379` |  |
| `SPELLABILITY_BATTLE_MASTERY` | int | `380` |  |
| `SPELLABILITY_DIVINE_STRENGTH` | int | `381` |  |
| `SPELLABILITY_DIVINE_PROTECTION` | int | `382` |  |
| `SPELLABILITY_NEGATIVE_PLANE_AVATAR` | int | `383` |  |
| `SPELLABILITY_DIVINE_TRICKERY` | int | `384` |  |
| `SPELLABILITY_ROGUES_CUNNING` | int | `385` |  |
| `SPELLABILITY_ACTIVATE_ITEM` | int | `386` |  |
| `SPELLABILITY_DRAGON_FEAR` | int | `412` |  |
| `SPELL_DIVINE_FAVOR` | int | `414` |  |
| `SPELL_TRUE_STRIKE` | int | `415` |  |
| `SPELL_FLARE` | int | `416` |  |
| `SPELL_SHIELD` | int | `417` |  |
| `SPELL_ENTROPIC_SHIELD` | int | `418` |  |
| `SPELL_CONTINUAL_FLAME` | int | `419` |  |
| `SPELL_ONE_WITH_THE_LAND` | int | `420` |  |
| `SPELL_CAMOFLAGE` | int | `421` |  |
| `SPELL_BLOOD_FRENZY` | int | `422` |  |
| `SPELL_BOMBARDMENT` | int | `423` |  |
| `SPELL_ACID_SPLASH` | int | `424` |  |
| `SPELL_QUILLFIRE` | int | `425` |  |
| `SPELL_EARTHQUAKE` | int | `426` |  |
| `SPELL_SUNBURST` | int | `427` |  |
| `SPELL_ACTIVATE_ITEM_SELF2` | int | `428` |  |
| `SPELL_AURAOFGLORY` | int | `429` |  |
| `SPELL_BANISHMENT` | int | `430` |  |
| `SPELL_INFLICT_MINOR_WOUNDS` | int | `431` |  |
| `SPELL_INFLICT_LIGHT_WOUNDS` | int | `432` |  |
| `SPELL_INFLICT_MODERATE_WOUNDS` | int | `433` |  |
| `SPELL_INFLICT_SERIOUS_WOUNDS` | int | `434` |  |
| `SPELL_INFLICT_CRITICAL_WOUNDS` | int | `435` |  |
| `SPELL_BALAGARNSIRONHORN` | int | `436` |  |
| `SPELL_DROWN` | int | `437` |  |
| `SPELL_OWLS_INSIGHT` | int | `438` |  |
| `SPELL_ELECTRIC_JOLT` | int | `439` |  |
| `SPELL_FIREBRAND` | int | `440` |  |
| `SPELL_WOUNDING_WHISPERS` | int | `441` |  |
| `SPELL_AMPLIFY` | int | `442` |  |
| `SPELL_ETHEREALNESS` | int | `443` |  |
| `SPELL_UNDEATHS_ETERNAL_FOE` | int | `444` |  |
| `SPELL_DIRGE` | int | `445` |  |
| `SPELL_INFERNO` | int | `446` |  |
| `SPELL_ISAACS_LESSER_MISSILE_STORM` | int | `447` |  |
| `SPELL_ISAACS_GREATER_MISSILE_STORM` | int | `448` |  |
| `SPELL_BANE` | int | `449` |  |
| `SPELL_SHIELD_OF_FAITH` | int | `450` |  |
| `SPELL_PLANAR_ALLY` | int | `451` |  |
| `SPELL_MAGIC_FANG` | int | `452` |  |
| `SPELL_GREATER_MAGIC_FANG` | int | `453` |  |
| `SPELL_SPIKE_GROWTH` | int | `454` |  |
| `SPELL_MASS_CAMOFLAGE` | int | `455` |  |
| `SPELL_EXPEDITIOUS_RETREAT` | int | `456` |  |
| `SPELL_TASHAS_HIDEOUS_LAUGHTER` | int | `457` |  |
| `SPELL_DISPLACEMENT` | int | `458` |  |
| `SPELL_BIGBYS_INTERPOSING_HAND` | int | `459` |  |
| `SPELL_BIGBYS_FORCEFUL_HAND` | int | `460` |  |
| `SPELL_BIGBYS_GRASPING_HAND` | int | `461` |  |
| `SPELL_BIGBYS_CLENCHED_FIST` | int | `462` |  |
| `SPELL_BIGBYS_CRUSHING_HAND` | int | `463` |  |
| `SPELL_GRENADE_FIRE` | int | `464` |  |
| `SPELL_GRENADE_TANGLE` | int | `465` |  |
| `SPELL_GRENADE_HOLY` | int | `466` |  |
| `SPELL_GRENADE_CHOKING` | int | `467` |  |
| `SPELL_GRENADE_THUNDERSTONE` | int | `468` |  |
| `SPELL_GRENADE_ACID` | int | `469` |  |
| `SPELL_GRENADE_CHICKEN` | int | `470` |  |
| `SPELL_GRENADE_CALTROPS` | int | `471` |  |
| `SPELL_ACTIVATE_ITEM_PORTAL` | int | `472` |  |
| `SPELL_DIVINE_MIGHT` | int | `473` |  |
| `SPELL_DIVINE_SHIELD` | int | `474` |  |
| `SPELL_SHADOW_DAZE` | int | `475` |  |
| `SPELL_SUMMON_SHADOW` | int | `476` |  |
| `SPELL_SHADOW_EVADE` | int | `477` |  |
| `SPELL_TYMORAS_SMILE` | int | `478` |  |
| `SPELL_CRAFT_HARPER_ITEM` | int | `479` |  |
| `SPELL_FLESH_TO_STONE` | int | `485` |  |
| `SPELL_STONE_TO_FLESH` | int | `486` |  |
| `SPELL_TRAP_ARROW` | int | `487` |  |
| `SPELL_TRAP_BOLT` | int | `488` |  |
| `SPELL_TRAP_DART` | int | `493` |  |
| `SPELL_TRAP_SHURIKEN` | int | `494` |  |
| `SPELLABILITY_BREATH_PETRIFY` | int | `495` |  |
| `SPELLABILITY_TOUCH_PETRIFY` | int | `496` |  |
| `SPELLABILITY_GAZE_PETRIFY` | int | `497` |  |
| `SPELLABILITY_MANTICORE_SPIKES` | int | `498` |  |
| `SPELL_ROD_OF_WONDER` | int | `499` |  |
| `SPELL_DECK_OF_MANY_THINGS` | int | `500` |  |
| `SPELL_ELEMENTAL_SUMMONING_ITEM` | int | `502` |  |
| `SPELL_DECK_AVATAR` | int | `503` |  |
| `SPELL_DECK_GEMSPRAY` | int | `504` |  |
| `SPELL_DECK_BUTTERFLYSPRAY` | int | `505` |  |
| `SPELL_HEALINGKIT` | int | `506` |  |
| `SPELL_POWERSTONE` | int | `507` |  |
| `SPELL_SPELLSTAFF` | int | `508` |  |
| `SPELL_CHARGER` | int | `500` |  |
| `SPELL_DECHARGER` | int | `510` |  |
| `SPELL_KOBOLD_JUMP` | int | `511` |  |
| `SPELL_CRUMBLE` | int | `512` |  |
| `SPELL_INFESTATION_OF_MAGGOTS` | int | `513` |  |
| `SPELL_HEALING_STING` | int | `514` |  |
| `SPELL_GREAT_THUNDERCLAP` | int | `515` |  |
| `SPELL_BALL_LIGHTNING` | int | `516` |  |
| `SPELL_BATTLETIDE` | int | `517` |  |
| `SPELL_COMBUST` | int | `518` |  |
| `SPELL_DEATH_ARMOR` | int | `519` |  |
| `SPELL_GEDLEES_ELECTRIC_LOOP` | int | `520` |  |
| `SPELL_HORIZIKAULS_BOOM` | int | `521` |  |
| `SPELL_IRONGUTS` | int | `522` |  |
| `SPELL_MESTILS_ACID_BREATH` | int | `523` |  |
| `SPELL_MESTILS_ACID_SHEATH` | int | `524` |  |
| `SPELL_MONSTROUS_REGENERATION` | int | `525` |  |
| `SPELL_SCINTILLATING_SPHERE` | int | `526` |  |
| `SPELL_STONE_BONES` | int | `527` |  |
| `SPELL_UNDEATH_TO_DEATH` | int | `528` |  |
| `SPELL_VINE_MINE` | int | `529` |  |
| `SPELL_VINE_MINE_ENTANGLE` | int | `530` |  |
| `SPELL_VINE_MINE_HAMPER_MOVEMENT` | int | `531` |  |
| `SPELL_VINE_MINE_CAMOUFLAGE` | int | `532` |  |
| `SPELL_BLACK_BLADE_OF_DISASTER` | int | `533` |  |
| `SPELL_SHELGARNS_PERSISTENT_BLADE` | int | `534` |  |
| `SPELL_BLADE_THIRST` | int | `535` |  |
| `SPELL_DEAFENING_CLANG` | int | `536` |  |
| `SPELL_CLOUD_OF_BEWILDERMENT` | int | `569` |  |
| `SPELL_KEEN_EDGE` | int | `539` |  |
| `SPELL_BLACKSTAFF` | int | `541` |  |
| `SPELL_FLAME_WEAPON` | int | `542` |  |
| `SPELL_ICE_DAGGER` | int | `543` |  |
| `SPELL_MAGIC_WEAPON` | int | `544` |  |
| `SPELL_GREATER_MAGIC_WEAPON` | int | `545` |  |
| `SPELL_STONEHOLD` | int | `547` |  |
| `SPELL_DARKFIRE` | int | `548` |  |
| `SPELL_GLYPH_OF_WARDING` | int | `549` |  |
| `SPELLABILITY_MINDBLAST` | int | `551` |  |
| `SPELLABILITY_CHARMMONSTER` | int | `552` |  |
| `SPELL_IOUN_STONE_DUSTY_ROSE` | int | `554` |  |
| `SPELL_IOUN_STONE_PALE_BLUE` | int | `555` |  |
| `SPELL_IOUN_STONE_SCARLET_BLUE` | int | `556` |  |
| `SPELL_IOUN_STONE_BLUE` | int | `557` |  |
| `SPELL_IOUN_STONE_DEEP_RED` | int | `558` |  |
| `SPELL_IOUN_STONE_PINK` | int | `559` |  |
| `SPELL_IOUN_STONE_PINK_GREEN` | int | `560` |  |
| `SPELLABILITY_WHIRLWIND` | int | `561` |  |
| `SPELLABILITY_COMMAND_THE_HORDE` | int | `571` |  |
| `SPELLABILITY_AA_IMBUE_ARROW` | int | `600` |  |
| `SPELLABILITY_AA_SEEKER_ARROW_1` | int | `601` |  |
| `SPELLABILITY_AA_SEEKER_ARROW_2` | int | `602` |  |
| `SPELLABILITY_AA_HAIL_OF_ARROWS` | int | `603` |  |
| `SPELLABILITY_AA_ARROW_OF_DEATH` | int | `604` |  |
| `SPELLABILITY_AS_GHOSTLY_VISAGE` | int | `605` |  |
| `SPELLABILITY_AS_DARKNESS` | int | `606` |  |
| `SPELLABILITY_AS_INVISIBILITY` | int | `607` |  |
| `SPELLABILITY_AS_IMPROVED_INVISIBLITY` | int | `608` |  |
| `SPELLABILITY_BG_CREATEDEAD` | int | `609` |  |
| `SPELLABILITY_BG_FIENDISH_SERVANT` | int | `610` |  |
| `SPELLABILITY_BG_INFLICT_SERIOUS_WOUNDS` | int | `611` |  |
| `SPELLABILITY_BG_INFLICT_CRITICAL_WOUNDS` | int | `612` |  |
| `SPELLABILITY_BG_CONTAGION` | int | `613` |  |
| `SPELLABILITY_BG_BULLS_STRENGTH` | int | `614` |  |
| `SPELL_FLYING_DEBRIS` | int | `620` |  |
| `SPELLABILITY_DC_DIVINE_WRATH` | int | `622` |  |
| `SPELLABILITY_PM_ANIMATE_DEAD` | int | `623` |  |
| `SPELLABILITY_PM_SUMMON_UNDEAD` | int | `624` |  |
| `SPELLABILITY_PM_UNDEAD_GRAFT_1` | int | `625` |  |
| `SPELLABILITY_PM_UNDEAD_GRAFT_2` | int | `626` |  |
| `SPELLABILITY_PM_SUMMON_GREATER_UNDEAD` | int | `627` |  |
| `SPELLABILITY_PM_DEATHLESS_MASTER_TOUCH` | int | `628` |  |
| `SPELL_EPIC_HELLBALL` | int | `636` |  |
| `SPELL_EPIC_MUMMY_DUST` | int | `637` |  |
| `SPELL_EPIC_DRAGON_KNIGHT` | int | `638` |  |
| `SPELL_EPIC_MAGE_ARMOR` | int | `639` |  |
| `SPELL_EPIC_RUIN` | int | `640` |  |
| `SPELLABILITY_DW_DEFENSIVE_STANCE` | int | `641` |  |
| `SPELLABILITY_EPIC_MIGHTY_RAGE` | int | `642` |  |
| `SPELLABILITY_EPIC_CURSE_SONG` | int | `644` |  |
| `SPELLABILITY_EPIC_IMPROVED_WHIRLWIND` | int | `645` |  |
| `SPELLABILITY_EPIC_SHAPE_DRAGONKIN` | int | `646` |  |
| `SPELLABILITY_EPIC_SHAPE_DRAGON` | int | `647` |  |
| `SPELL_CRAFT_DYE_CLOTHCOLOR_1` | int | `648` |  |
| `SPELL_CRAFT_DYE_CLOTHCOLOR_2` | int | `649` |  |
| `SPELL_CRAFT_DYE_LEATHERCOLOR_1` | int | `650` |  |
| `SPELL_CRAFT_DYE_LEATHERCOLOR_2` | int | `651` |  |
| `SPELL_CRAFT_DYE_METALCOLOR_1` | int | `652` |  |
| `SPELL_CRAFT_DYE_METALCOLOR_2` | int | `653` |  |
| `SPELL_CRAFT_ADD_ITEM_PROPERTY` | int | `654` |  |
| `SPELL_CRAFT_POISON_WEAPON_OR_AMMO` | int | `655` |  |
| `SPELL_CRAFT_CRAFT_WEAPON_SKILL` | int | `656` |  |
| `SPELL_CRAFT_CRAFT_ARMOR_SKILL` | int | `657` |  |
| `SPELLABILITY_DRAGON_BREATH_NEGATIVE` | int | `698` |  |
| `SPELLABILITY_SEAHAG_EVILEYE` | int | `803` |  |
| `SPELLABILITY_AURA_HORRIFICAPPEARANCE` | int | `804` |  |
| `SPELLABILITY_TROGLODYTE_STENCH` | int | `805` |  |
| `SPELL_HORSE_MENU` | int | `812` |  |
| `SPELL_HORSE_MOUNT` | int | `813` |  |
| `SPELL_HORSE_DISMOUNT` | int | `814` |  |
| `SPELL_HORSE_PARTY_MOUNT` | int | `815` |  |
| `SPELL_HORSE_PARTY_DISMOUNT` | int | `816` |  |
| `SPELL_HORSE_ASSIGN_MOUNT` | int | `817` |  |
| `SPELL_PALADIN_SUMMON_MOUNT` | int | `818` |  |
| `POISON_NIGHTSHADE` | int | `0` |  |
| `POISON_SMALL_CENTIPEDE_POISON` | int | `1` |  |
| `POISON_BLADE_BANE` | int | `2` |  |
| `POISON_GREENBLOOD_OIL` | int | `3` |  |
| `POISON_BLOODROOT` | int | `4` |  |
| `POISON_PURPLE_WORM_POISON` | int | `5` |  |
| `POISON_LARGE_SCORPION_VENOM` | int | `6` |  |
| `POISON_WYVERN_POISON` | int | `7` |  |
| `POISON_BLUE_WHINNIS` | int | `8` |  |
| `POISON_GIANT_WASP_POISON` | int | `9` |  |
| `POISON_SHADOW_ESSENCE` | int | `10` |  |
| `POISON_BLACK_ADDER_VENOM` | int | `11` |  |
| `POISON_DEATHBLADE` | int | `12` |  |
| `POISON_MALYSS_ROOT_PASTE` | int | `13` |  |
| `POISON_NITHARIT` | int | `14` |  |
| `POISON_DRAGON_BILE` | int | `15` |  |
| `POISON_SASSONE_LEAF_RESIDUE` | int | `16` |  |
| `POISON_TERINAV_ROOT` | int | `17` |  |
| `POISON_CARRION_CRAWLER_BRAIN_JUICE` | int | `18` |  |
| `POISON_BLACK_LOTUS_EXTRACT` | int | `19` |  |
| `POISON_OIL_OF_TAGGIT` | int | `20` |  |
| `POISON_ID_MOSS` | int | `21` |  |
| `POISON_STRIPED_TOADSTOOL` | int | `22` |  |
| `POISON_ARSENIC` | int | `23` |  |
| `POISON_LICH_DUST` | int | `24` |  |
| `POISON_DARK_REAVER_POWDER` | int | `25` |  |
| `POISON_UNGOL_DUST` | int | `26` |  |
| `POISON_BURNT_OTHUR_FUMES` | int | `27` |  |
| `POISON_CHAOS_MIST` | int | `28` |  |
| `POISON_BEBILITH_VENOM` | int | `29` |  |
| `POISON_QUASIT_VENOM` | int | `30` |  |
| `POISON_PIT_FIEND_ICHOR` | int | `31` |  |
| `POISON_ETTERCAP_VENOM` | int | `32` |  |
| `POISON_ARANEA_VENOM` | int | `33` |  |
| `POISON_TINY_SPIDER_VENOM` | int | `34` |  |
| `POISON_SMALL_SPIDER_VENOM` | int | `35` |  |
| `POISON_MEDIUM_SPIDER_VENOM` | int | `36` |  |
| `POISON_LARGE_SPIDER_VENOM` | int | `37` |  |
| `POISON_HUGE_SPIDER_VENOM` | int | `38` |  |
| `POISON_GARGANTUAN_SPIDER_VENOM` | int | `39` |  |
| `POISON_COLOSSAL_SPIDER_VENOM` | int | `40` |  |
| `POISON_PHASE_SPIDER_VENOM` | int | `41` |  |
| `POISON_WRAITH_SPIDER_VENOM` | int | `42` |  |
| `POISON_IRON_GOLEM` | int | `43` |  |
| `DISEASE_BLINDING_SICKNESS` | int | `0` |  |
| `DISEASE_CACKLE_FEVER` | int | `1` |  |
| `DISEASE_DEVIL_CHILLS` | int | `2` |  |
| `DISEASE_DEMON_FEVER` | int | `3` |  |
| `DISEASE_FILTH_FEVER` | int | `4` |  |
| `DISEASE_MINDFIRE` | int | `5` |  |
| `DISEASE_MUMMY_ROT` | int | `6` |  |
| `DISEASE_RED_ACHE` | int | `7` |  |
| `DISEASE_SHAKES` | int | `8` |  |
| `DISEASE_SLIMY_DOOM` | int | `9` |  |
| `DISEASE_RED_SLAAD_EGGS` | int | `10` |  |
| `DISEASE_GHOUL_ROT` | int | `11` |  |
| `DISEASE_ZOMBIE_CREEP` | int | `12` |  |
| `DISEASE_DREAD_BLISTERS` | int | `13` |  |
| `DISEASE_BURROW_MAGGOTS` | int | `14` |  |
| `DISEASE_SOLDIER_SHAKES` | int | `15` |  |
| `DISEASE_VERMIN_MADNESS` | int | `16` |  |
| `CREATURE_TYPE_RACIAL_TYPE` | int | `0` |  |
| `CREATURE_TYPE_PLAYER_CHAR` | int | `1` |  |
| `CREATURE_TYPE_CLASS` | int | `2` |  |
| `CREATURE_TYPE_REPUTATION` | int | `3` |  |
| `CREATURE_TYPE_IS_ALIVE` | int | `4` |  |
| `CREATURE_TYPE_HAS_SPELL_EFFECT` | int | `5` |  |
| `CREATURE_TYPE_DOES_NOT_HAVE_SPELL_EFFECT` | int | `6` |  |
| `CREATURE_TYPE_PERCEPTION` | int | `7` |  |
| `REPUTATION_TYPE_FRIEND` | int | `0` |  |
| `REPUTATION_TYPE_ENEMY` | int | `1` |  |
| `REPUTATION_TYPE_NEUTRAL` | int | `2` |  |
| `PERCEPTION_SEEN_AND_HEARD` | int | `0` |  |
| `PERCEPTION_NOT_SEEN_AND_NOT_HEARD` | int | `1` |  |
| `PERCEPTION_HEARD_AND_NOT_SEEN` | int | `2` |  |
| `PERCEPTION_SEEN_AND_NOT_HEARD` | int | `3` |  |
| `PERCEPTION_NOT_HEARD` | int | `4` |  |
| `PERCEPTION_HEARD` | int | `5` |  |
| `PERCEPTION_NOT_SEEN` | int | `6` |  |
| `PERCEPTION_SEEN` | int | `7` |  |
| `PLAYER_CHAR_NOT_PC` | int | `FALSE` |  |
| `PLAYER_CHAR_IS_PC` | int | `TRUE` |  |
| `CLASS_TYPE_BARBARIAN` | int | `0` |  |
| `CLASS_TYPE_BARD` | int | `1` |  |
| `CLASS_TYPE_CLERIC` | int | `2` |  |
| `CLASS_TYPE_DRUID` | int | `3` |  |
| `CLASS_TYPE_FIGHTER` | int | `4` |  |
| `CLASS_TYPE_MONK` | int | `5` |  |
| `CLASS_TYPE_PALADIN` | int | `6` |  |
| `CLASS_TYPE_RANGER` | int | `7` |  |
| `CLASS_TYPE_ROGUE` | int | `8` |  |
| `CLASS_TYPE_SORCERER` | int | `9` |  |
| `CLASS_TYPE_WIZARD` | int | `10` |  |
| `CLASS_TYPE_ABERRATION` | int | `11` |  |
| `CLASS_TYPE_ANIMAL` | int | `12` |  |
| `CLASS_TYPE_CONSTRUCT` | int | `13` |  |
| `CLASS_TYPE_HUMANOID` | int | `14` |  |
| `CLASS_TYPE_MONSTROUS` | int | `15` |  |
| `CLASS_TYPE_ELEMENTAL` | int | `16` |  |
| `CLASS_TYPE_FEY` | int | `17` |  |
| `CLASS_TYPE_DRAGON` | int | `18` |  |
| `CLASS_TYPE_UNDEAD` | int | `19` |  |
| `CLASS_TYPE_COMMONER` | int | `20` |  |
| `CLASS_TYPE_BEAST` | int | `21` |  |
| `CLASS_TYPE_GIANT` | int | `22` |  |
| `CLASS_TYPE_MAGICAL_BEAST` | int | `23` |  |
| `CLASS_TYPE_OUTSIDER` | int | `24` |  |
| `CLASS_TYPE_SHAPECHANGER` | int | `25` |  |
| `CLASS_TYPE_VERMIN` | int | `26` |  |
| `CLASS_TYPE_SHADOWDANCER` | int | `27` |  |
| `CLASS_TYPE_HARPER` | int | `28` |  |
| `CLASS_TYPE_ARCANE_ARCHER` | int | `29` |  |
| `CLASS_TYPE_ASSASSIN` | int | `30` |  |
| `CLASS_TYPE_BLACKGUARD` | int | `31` |  |
| `CLASS_TYPE_DIVINECHAMPION` | int | `32` |  |
| `CLASS_TYPE_DIVINE_CHAMPION` | int | `32` |  |
| `CLASS_TYPE_WEAPON_MASTER` | int | `33` |  |
| `CLASS_TYPE_PALEMASTER` | int | `34` |  |
| `CLASS_TYPE_PALE_MASTER` | int | `34` |  |
| `CLASS_TYPE_SHIFTER` | int | `35` |  |
| `CLASS_TYPE_DWARVENDEFENDER` | int | `36` |  |
| `CLASS_TYPE_DWARVEN_DEFENDER` | int | `36` |  |
| `CLASS_TYPE_DRAGONDISCIPLE` | int | `37` |  |
| `CLASS_TYPE_DRAGON_DISCIPLE` | int | `37` |  |
| `CLASS_TYPE_OOZE` | int | `38` |  |
| `CLASS_TYPE_EYE_OF_GRUUMSH` | int | `39` |  |
| `CLASS_TYPE_SHOU_DISCIPLE` | int | `40` |  |
| `CLASS_TYPE_PURPLE_DRAGON_KNIGHT` | int | `41` |  |
| `CLASS_TYPE_INVALID` | int | `255` |  |
| `PACKAGE_BARBARIAN` | int | `0` |  |
| `PACKAGE_BARD` | int | `1` |  |
| `PACKAGE_CLERIC` | int | `2` |  |
| `PACKAGE_DRUID` | int | `3` |  |
| `PACKAGE_FIGHTER` | int | `4` |  |
| `PACKAGE_MONK` | int | `5` |  |
| `PACKAGE_PALADIN` | int | `6` |  |
| `PACKAGE_RANGER` | int | `7` |  |
| `PACKAGE_ROGUE` | int | `8` |  |
| `PACKAGE_SORCERER` | int | `9` |  |
| `PACKAGE_WIZARDGENERALIST` | int | `10` |  |
| `PACKAGE_DRUID_INTERLOPER` | int | `11` |  |
| `PACKAGE_DRUID_GRAY` | int | `12` |  |
| `PACKAGE_DRUID_DEATH` | int | `13` |  |
| `PACKAGE_DRUID_HAWKMASTER` | int | `14` |  |
| `PACKAGE_BARBARIAN_BRUTE` | int | `15` |  |
| `PACKAGE_BARBARIAN_SLAYER` | int | `16` |  |
| `PACKAGE_BARBARIAN_SAVAGE` | int | `17` |  |
| `PACKAGE_BARBARIAN_ORCBLOOD` | int | `18` |  |
| `PACKAGE_CLERIC_SHAMAN` | int | `19` |  |
| `PACKAGE_CLERIC_DEADWALKER` | int | `20` |  |
| `PACKAGE_CLERIC_ELEMENTALIST` | int | `21` |  |
| `PACKAGE_CLERIC_BATTLE_PRIEST` | int | `22` |  |
| `PACKAGE_FIGHTER_FINESSE` | int | `23` |  |
| `PACKAGE_FIGHTER_PIRATE` | int | `24` |  |
| `PACKAGE_FIGHTER_GLADIATOR` | int | `25` |  |
| `PACKAGE_FIGHTER_COMMANDER` | int | `26` |  |
| `PACKAGE_WIZARD_ABJURATION` | int | `27` |  |
| `PACKAGE_WIZARD_CONJURATION` | int | `28` |  |
| `PACKAGE_WIZARD_DIVINATION` | int | `29` |  |
| `PACKAGE_WIZARD_ENCHANTMENT` | int | `30` |  |
| `PACKAGE_WIZARD_EVOCATION` | int | `31` |  |
| `PACKAGE_WIZARD_ILLUSION` | int | `32` |  |
| `PACKAGE_WIZARD_NECROMANCY` | int | `33` |  |
| `PACKAGE_WIZARD_TRANSMUTATION` | int | `34` |  |
| `PACKAGE_SORCERER_ABJURATION` | int | `35` |  |
| `PACKAGE_SORCERER_CONJURATION` | int | `36` |  |
| `PACKAGE_SORCERER_DIVINATION` | int | `37` |  |
| `PACKAGE_SORCERER_ENCHANTMENT` | int | `38` |  |
| `PACKAGE_SORCERER_EVOCATION` | int | `39` |  |
| `PACKAGE_SORCERER_ILLUSION` | int | `40` |  |
| `PACKAGE_SORCERER_NECROMANCY` | int | `41` |  |
| `PACKAGE_SORCERER_TRANSMUTATION` | int | `42` |  |
| `PACKAGE_BARD_BLADE` | int | `43` |  |
| `PACKAGE_BARD_GALLANT` | int | `44` |  |
| `PACKAGE_BARD_JESTER` | int | `45` |  |
| `PACKAGE_BARD_LOREMASTER` | int | `46` |  |
| `PACKAGE_MONK_SPIRIT` | int | `47` |  |
| `PACKAGE_MONK_GIFTED` | int | `48` |  |
| `PACKAGE_MONK_DEVOUT` | int | `49` |  |
| `PACKAGE_MONK_PEASANT` | int | `50` |  |
| `PACKAGE_PALADIN_ERRANT` | int | `51` |  |
| `PACKAGE_PALADIN_UNDEAD` | int | `52` |  |
| `PACKAGE_PALADIN_INQUISITOR` | int | `53` |  |
| `PACKAGE_PALADIN_CHAMPION` | int | `54` |  |
| `PACKAGE_RANGER_MARKSMAN` | int | `55` |  |
| `PACKAGE_RANGER_WARDEN` | int | `56` |  |
| `PACKAGE_RANGER_STALKER` | int | `57` |  |
| `PACKAGE_RANGER_GIANTKILLER` | int | `58` |  |
| `PACKAGE_ROGUE_GYPSY` | int | `59` |  |
| `PACKAGE_ROGUE_BANDIT` | int | `60` |  |
| `PACKAGE_ROGUE_SCOUT` | int | `61` |  |
| `PACKAGE_ROGUE_SWASHBUCKLER` | int | `62` |  |
| `PACKAGE_SHADOWDANCER` | int | `63` |  |
| `PACKAGE_HARPER` | int | `64` |  |
| `PACKAGE_ARCANE_ARCHER` | int | `65` |  |
| `PACKAGE_ASSASSIN` | int | `66` |  |
| `PACKAGE_BLACKGUARD` | int | `67` |  |
| `PACKAGE_NPC_SORCERER` | int | `70` |  |
| `PACKAGE_NPC_ROGUE` | int | `71` |  |
| `PACKAGE_NPC_BARD` | int | `72` |  |
| `PACKAGE_ABERRATION` | int | `73` |  |
| `PACKAGE_ANIMAL` | int | `74` |  |
| `PACKAGE_CONSTRUCT` | int | `75` |  |
| `PACKAGE_HUMANOID` | int | `76` |  |
| `PACKAGE_MONSTROUS` | int | `77` |  |
| `PACKAGE_ELEMENTAL` | int | `78` |  |
| `PACKAGE_FEY` | int | `79` |  |
| `PACKAGE_DRAGON` | int | `80` |  |
| `PACKAGE_UNDEAD` | int | `81` |  |
| `PACKAGE_COMMONER` | int | `82` |  |
| `PACKAGE_BEAST` | int | `83` |  |
| `PACKAGE_GIANT` | int | `84` |  |
| `PACKAGE_MAGICBEAST` | int | `85` |  |
| `PACKAGE_OUTSIDER` | int | `86` |  |
| `PACKAGE_SHAPECHANGER` | int | `87` |  |
| `PACKAGE_VERMIN` | int | `88` |  |
| `PACKAGE_DWARVEN_DEFENDER` | int | `89` |  |
| `PACKAGE_BARBARIAN_BLACKGUARD` | int | `90` |  |
| `PACKAGE_BARD_HARPER` | int | `91` |  |
| `PACKAGE_CLERIC_DIVINE` | int | `92` |  |
| `PACKAGE_DRUID_SHIFTER` | int | `93` |  |
| `PACKAGE_FIGHTER_WEAPONMASTER` | int | `94` |  |
| `PACKAGE_MONK_ASSASSIN` | int | `95` |  |
| `PACKAGE_PALADIN_DIVINE` | int | `96` |  |
| `PACKAGE_RANGER_ARCANEARCHER` | int | `97` |  |
| `PACKAGE_ROGUE_SHADOWDANCER` | int | `98` |  |
| `PACKAGE_SORCERER_DRAGONDISCIPLE` | int | `99` |  |
| `PACKAGE_WIZARD_PALEMASTER` | int | `100` |  |
| `PACKAGE_NPC_WIZASSASSIN` | int | `101` |  |
| `PACKAGE_NPC_FT_WEAPONMASTER` | int | `102` |  |
| `PACKAGE_NPC_RG_SHADOWDANCER` | int | `103` |  |
| `PACKAGE_NPC_CLERIC_LINU` | int | `104` |  |
| `PACKAGE_NPC_BARBARIAN_DAELAN` | int | `105` |  |
| `PACKAGE_NPC_BARD_FIGHTER` | int | `106` |  |
| `PACKAGE_NPC_PALADIN_FALLING` | int | `107` |  |
| `PACKAGE_SHIFTER` | int | `108` |  |
| `PACKAGE_DIVINE_CHAMPION` | int | `109` |  |
| `PACKAGE_PALE_MASTER` | int | `110` |  |
| `PACKAGE_DRAGON_DISCIPLE` | int | `111` |  |
| `PACKAGE_WEAPONMASTER` | int | `112` |  |
| `PACKAGE_NPC_FT_WEAPONMASTER_VALEN_2` | int | `113` |  |
| `PACKAGE_NPC_BARD_FIGHTER_SHARWYN2` | int | `114` |  |
| `PACKAGE_NPC_WIZASSASSIN_NATHYRRA` | int | `115` |  |
| `PACKAGE_NPC_RG_TOMI_2` | int | `116` |  |
| `PACKAGE_NPC_BARD_DEEKIN_2` | int | `117` |  |
| `PACKAGE_BARBARIAN_BLACKGUARD_2NDCLASS` | int | `118` |  |
| `PACKAGE_BARD_HARPER_2NDCLASS` | int | `119` |  |
| `PACKAGE_CLERIC_DIVINE_2NDCLASS` | int | `120` |  |
| `PACKAGE_DRUID_SHIFTER_2NDCLASS` | int | `121` |  |
| `PACKAGE_FIGHTER_WEAPONMASTER_2NDCLASS` | int | `122` |  |
| `PACKAGE_MONK_ASSASSIN_2NDCLASS` | int | `123` |  |
| `PACKAGE_PALADIN_DIVINE_2NDCLASS` | int | `124` |  |
| `PACKAGE_RANGER_ARCANEARCHER_2NDCLASS` | int | `125` |  |
| `PACKAGE_ROGUE_SHADOWDANCER_2NDCLASS` | int | `126` |  |
| `PACKAGE_SORCERER_DRAGONDISCIPLE_2NDCLASS` | int | `127` |  |
| `PACKAGE_WIZARD_PALEMASTER_2NDCLASS` | int | `128` |  |
| `PACKAGE_NPC_ARIBETH_PALADIN` | int | `129` |  |
| `PACKAGE_NPC_ARIBETH_BLACKGUARD` | int | `130` |  |
| `PACKAGE_INVALID` | int | `255` |  |
| `PERSISTENT_ZONE_ACTIVE` | int | `0` |  |
| `PERSISTENT_ZONE_FOLLOW` | int | `1` |  |
| `STANDARD_FACTION_HOSTILE` | int | `0` |  |
| `STANDARD_FACTION_COMMONER` | int | `1` |  |
| `STANDARD_FACTION_MERCHANT` | int | `2` |  |
| `STANDARD_FACTION_DEFENDER` | int | `3` |  |
| `SKILL_ANIMAL_EMPATHY` | int | `0` |  |
| `SKILL_CONCENTRATION` | int | `1` |  |
| `SKILL_DISABLE_TRAP` | int | `2` |  |
| `SKILL_DISCIPLINE` | int | `3` |  |
| `SKILL_HEAL` | int | `4` |  |
| `SKILL_HIDE` | int | `5` |  |
| `SKILL_LISTEN` | int | `6` |  |
| `SKILL_LORE` | int | `7` |  |
| `SKILL_MOVE_SILENTLY` | int | `8` |  |
| `SKILL_OPEN_LOCK` | int | `9` |  |
| `SKILL_PARRY` | int | `10` |  |
| `SKILL_PERFORM` | int | `11` |  |
| `SKILL_PERSUADE` | int | `12` |  |
| `SKILL_PICK_POCKET` | int | `13` |  |
| `SKILL_SEARCH` | int | `14` |  |
| `SKILL_SET_TRAP` | int | `15` |  |
| `SKILL_SPELLCRAFT` | int | `16` |  |
| `SKILL_SPOT` | int | `17` |  |
| `SKILL_TAUNT` | int | `18` |  |
| `SKILL_USE_MAGIC_DEVICE` | int | `19` |  |
| `SKILL_APPRAISE` | int | `20` |  |
| `SKILL_TUMBLE` | int | `21` |  |
| `SKILL_CRAFT_TRAP` | int | `22` |  |
| `SKILL_BLUFF` | int | `23` |  |
| `SKILL_INTIMIDATE` | int | `24` |  |
| `SKILL_CRAFT_ARMOR` | int | `25` |  |
| `SKILL_CRAFT_WEAPON` | int | `26` |  |
| `SKILL_RIDE` | int | `27` |  |
| `SKILL_ALL_SKILLS` | int | `255` |  |
| `SUBSKILL_FLAGTRAP` | int | `100` |  |
| `SUBSKILL_RECOVERTRAP` | int | `101` |  |
| `SUBSKILL_EXAMINETRAP` | int | `102` |  |
| `FEAT_ALERTNESS` | int | `0` |  |
| `FEAT_AMBIDEXTERITY` | int | `1` |  |
| `FEAT_ARMOR_PROFICIENCY_HEAVY` | int | `2` |  |
| `FEAT_ARMOR_PROFICIENCY_LIGHT` | int | `3` |  |
| `FEAT_ARMOR_PROFICIENCY_MEDIUM` | int | `4` |  |
| `FEAT_CALLED_SHOT` | int | `5` |  |
| `FEAT_CLEAVE` | int | `6` |  |
| `FEAT_COMBAT_CASTING` | int | `7` |  |
| `FEAT_DEFLECT_ARROWS` | int | `8` |  |
| `FEAT_DISARM` | int | `9` |  |
| `FEAT_DODGE` | int | `10` |  |
| `FEAT_EMPOWER_SPELL` | int | `11` |  |
| `FEAT_EXTEND_SPELL` | int | `12` |  |
| `FEAT_EXTRA_TURNING` | int | `13` |  |
| `FEAT_GREAT_FORTITUDE` | int | `14` |  |
| `FEAT_IMPROVED_CRITICAL_CLUB` | int | `15` |  |
| `FEAT_IMPROVED_DISARM` | int | `16` |  |
| `FEAT_IMPROVED_KNOCKDOWN` | int | `17` |  |
| `FEAT_IMPROVED_PARRY` | int | `18` |  |
| `FEAT_IMPROVED_POWER_ATTACK` | int | `19` |  |
| `FEAT_IMPROVED_TWO_WEAPON_FIGHTING` | int | `20` |  |
| `FEAT_IMPROVED_UNARMED_STRIKE` | int | `21` |  |
| `FEAT_IRON_WILL` | int | `22` |  |
| `FEAT_KNOCKDOWN` | int | `23` |  |
| `FEAT_LIGHTNING_REFLEXES` | int | `24` |  |
| `FEAT_MAXIMIZE_SPELL` | int | `25` |  |
| `FEAT_MOBILITY` | int | `26` |  |
| `FEAT_POINT_BLANK_SHOT` | int | `27` |  |
| `FEAT_POWER_ATTACK` | int | `28` |  |
| `FEAT_QUICKEN_SPELL` | int | `29` |  |
| `FEAT_RAPID_SHOT` | int | `30` |  |
| `FEAT_SAP` | int | `31` |  |
| `FEAT_SHIELD_PROFICIENCY` | int | `32` |  |
| `FEAT_SILENCE_SPELL` | int | `33` |  |
| `FEAT_SKILL_FOCUS_ANIMAL_EMPATHY` | int | `34` |  |
| `FEAT_SPELL_FOCUS_ABJURATION` | int | `35` |  |
| `FEAT_SPELL_PENETRATION` | int | `36` |  |
| `FEAT_STILL_SPELL` | int | `37` |  |
| `FEAT_STUNNING_FIST` | int | `39` |  |
| `FEAT_TOUGHNESS` | int | `40` |  |
| `FEAT_TWO_WEAPON_FIGHTING` | int | `41` |  |
| `FEAT_WEAPON_FINESSE` | int | `42` |  |
| `FEAT_WEAPON_FOCUS_CLUB` | int | `43` |  |
| `FEAT_WEAPON_PROFICIENCY_EXOTIC` | int | `44` |  |
| `FEAT_WEAPON_PROFICIENCY_MARTIAL` | int | `45` |  |
| `FEAT_WEAPON_PROFICIENCY_SIMPLE` | int | `46` |  |
| `FEAT_WEAPON_SPECIALIZATION_CLUB` | int | `47` |  |
| `FEAT_WEAPON_PROFICIENCY_DRUID` | int | `48` |  |
| `FEAT_WEAPON_PROFICIENCY_MONK` | int | `49` |  |
| `FEAT_WEAPON_PROFICIENCY_ROGUE` | int | `50` |  |
| `FEAT_WEAPON_PROFICIENCY_WIZARD` | int | `51` |  |
| `FEAT_IMPROVED_CRITICAL_DAGGER` | int | `52` |  |
| `FEAT_IMPROVED_CRITICAL_DART` | int | `53` |  |
| `FEAT_IMPROVED_CRITICAL_HEAVY_CROSSBOW` | int | `54` |  |
| `FEAT_IMPROVED_CRITICAL_LIGHT_CROSSBOW` | int | `55` |  |
| `FEAT_IMPROVED_CRITICAL_LIGHT_MACE` | int | `56` |  |
| `FEAT_IMPROVED_CRITICAL_MORNING_STAR` | int | `57` |  |
| `FEAT_IMPROVED_CRITICAL_STAFF` | int | `58` |  |
| `FEAT_IMPROVED_CRITICAL_SPEAR` | int | `59` |  |
| `FEAT_IMPROVED_CRITICAL_SICKLE` | int | `60` |  |
| `FEAT_IMPROVED_CRITICAL_SLING` | int | `61` |  |
| `FEAT_IMPROVED_CRITICAL_UNARMED_STRIKE` | int | `62` |  |
| `FEAT_IMPROVED_CRITICAL_LONGBOW` | int | `63` |  |
| `FEAT_IMPROVED_CRITICAL_SHORTBOW` | int | `64` |  |
| `FEAT_IMPROVED_CRITICAL_SHORT_SWORD` | int | `65` |  |
| `FEAT_IMPROVED_CRITICAL_RAPIER` | int | `66` |  |
| `FEAT_IMPROVED_CRITICAL_SCIMITAR` | int | `67` |  |
| `FEAT_IMPROVED_CRITICAL_LONG_SWORD` | int | `68` |  |
| `FEAT_IMPROVED_CRITICAL_GREAT_SWORD` | int | `69` |  |
| `FEAT_IMPROVED_CRITICAL_HAND_AXE` | int | `70` |  |
| `FEAT_IMPROVED_CRITICAL_THROWING_AXE` | int | `71` |  |
| `FEAT_IMPROVED_CRITICAL_BATTLE_AXE` | int | `72` |  |
| `FEAT_IMPROVED_CRITICAL_GREAT_AXE` | int | `73` |  |
| `FEAT_IMPROVED_CRITICAL_HALBERD` | int | `74` |  |
| `FEAT_IMPROVED_CRITICAL_LIGHT_HAMMER` | int | `75` |  |
| `FEAT_IMPROVED_CRITICAL_LIGHT_FLAIL` | int | `76` |  |
| `FEAT_IMPROVED_CRITICAL_WAR_HAMMER` | int | `77` |  |
| `FEAT_IMPROVED_CRITICAL_HEAVY_FLAIL` | int | `78` |  |
| `FEAT_IMPROVED_CRITICAL_KAMA` | int | `79` |  |
| `FEAT_IMPROVED_CRITICAL_KUKRI` | int | `80` |  |
| `FEAT_IMPROVED_CRITICAL_SHURIKEN` | int | `82` |  |
| `FEAT_IMPROVED_CRITICAL_SCYTHE` | int | `83` |  |
| `FEAT_IMPROVED_CRITICAL_KATANA` | int | `84` |  |
| `FEAT_IMPROVED_CRITICAL_BASTARD_SWORD` | int | `85` |  |
| `FEAT_IMPROVED_CRITICAL_DIRE_MACE` | int | `87` |  |
| `FEAT_IMPROVED_CRITICAL_DOUBLE_AXE` | int | `88` |  |
| `FEAT_IMPROVED_CRITICAL_TWO_BLADED_SWORD` | int | `89` |  |
| `FEAT_WEAPON_FOCUS_DAGGER` | int | `90` |  |
| `FEAT_WEAPON_FOCUS_DART` | int | `91` |  |
| `FEAT_WEAPON_FOCUS_HEAVY_CROSSBOW` | int | `92` |  |
| `FEAT_WEAPON_FOCUS_LIGHT_CROSSBOW` | int | `93` |  |
| `FEAT_WEAPON_FOCUS_LIGHT_MACE` | int | `94` |  |
| `FEAT_WEAPON_FOCUS_MORNING_STAR` | int | `95` |  |
| `FEAT_WEAPON_FOCUS_STAFF` | int | `96` |  |
| `FEAT_WEAPON_FOCUS_SPEAR` | int | `97` |  |
| `FEAT_WEAPON_FOCUS_SICKLE` | int | `98` |  |
| `FEAT_WEAPON_FOCUS_SLING` | int | `99` |  |
| `FEAT_WEAPON_FOCUS_UNARMED_STRIKE` | int | `100` |  |
| `FEAT_WEAPON_FOCUS_LONGBOW` | int | `101` |  |
| `FEAT_WEAPON_FOCUS_SHORTBOW` | int | `102` |  |
| `FEAT_WEAPON_FOCUS_SHORT_SWORD` | int | `103` |  |
| `FEAT_WEAPON_FOCUS_RAPIER` | int | `104` |  |
| `FEAT_WEAPON_FOCUS_SCIMITAR` | int | `105` |  |
| `FEAT_WEAPON_FOCUS_LONG_SWORD` | int | `106` |  |
| `FEAT_WEAPON_FOCUS_GREAT_SWORD` | int | `107` |  |
| `FEAT_WEAPON_FOCUS_HAND_AXE` | int | `108` |  |
| `FEAT_WEAPON_FOCUS_THROWING_AXE` | int | `109` |  |
| `FEAT_WEAPON_FOCUS_BATTLE_AXE` | int | `110` |  |
| `FEAT_WEAPON_FOCUS_GREAT_AXE` | int | `111` |  |
| `FEAT_WEAPON_FOCUS_HALBERD` | int | `112` |  |
| `FEAT_WEAPON_FOCUS_LIGHT_HAMMER` | int | `113` |  |
| `FEAT_WEAPON_FOCUS_LIGHT_FLAIL` | int | `114` |  |
| `FEAT_WEAPON_FOCUS_WAR_HAMMER` | int | `115` |  |
| `FEAT_WEAPON_FOCUS_HEAVY_FLAIL` | int | `116` |  |
| `FEAT_WEAPON_FOCUS_KAMA` | int | `117` |  |
| `FEAT_WEAPON_FOCUS_KUKRI` | int | `118` |  |
| `FEAT_WEAPON_FOCUS_SHURIKEN` | int | `120` |  |
| `FEAT_WEAPON_FOCUS_SCYTHE` | int | `121` |  |
| `FEAT_WEAPON_FOCUS_KATANA` | int | `122` |  |
| `FEAT_WEAPON_FOCUS_BASTARD_SWORD` | int | `123` |  |
| `FEAT_WEAPON_FOCUS_DIRE_MACE` | int | `125` |  |
| `FEAT_WEAPON_FOCUS_DOUBLE_AXE` | int | `126` |  |
| `FEAT_WEAPON_FOCUS_TWO_BLADED_SWORD` | int | `127` |  |
| `FEAT_WEAPON_SPECIALIZATION_DAGGER` | int | `128` |  |
| `FEAT_WEAPON_SPECIALIZATION_DART` | int | `129` |  |
| `FEAT_WEAPON_SPECIALIZATION_HEAVY_CROSSBOW` | int | `130` |  |
| `FEAT_WEAPON_SPECIALIZATION_LIGHT_CROSSBOW` | int | `131` |  |
| `FEAT_WEAPON_SPECIALIZATION_LIGHT_MACE` | int | `132` |  |
| `FEAT_WEAPON_SPECIALIZATION_MORNING_STAR` | int | `133` |  |
| `FEAT_WEAPON_SPECIALIZATION_STAFF` | int | `134` |  |
| `FEAT_WEAPON_SPECIALIZATION_SPEAR` | int | `135` |  |
| `FEAT_WEAPON_SPECIALIZATION_SICKLE` | int | `136` |  |
| `FEAT_WEAPON_SPECIALIZATION_SLING` | int | `137` |  |
| `FEAT_WEAPON_SPECIALIZATION_UNARMED_STRIKE` | int | `138` |  |
| `FEAT_WEAPON_SPECIALIZATION_LONGBOW` | int | `139` |  |
| `FEAT_WEAPON_SPECIALIZATION_SHORTBOW` | int | `140` |  |
| `FEAT_WEAPON_SPECIALIZATION_SHORT_SWORD` | int | `141` |  |
| `FEAT_WEAPON_SPECIALIZATION_RAPIER` | int | `142` |  |
| `FEAT_WEAPON_SPECIALIZATION_SCIMITAR` | int | `143` |  |
| `FEAT_WEAPON_SPECIALIZATION_LONG_SWORD` | int | `144` |  |
| `FEAT_WEAPON_SPECIALIZATION_GREAT_SWORD` | int | `145` |  |
| `FEAT_WEAPON_SPECIALIZATION_HAND_AXE` | int | `146` |  |
| `FEAT_WEAPON_SPECIALIZATION_THROWING_AXE` | int | `147` |  |
| `FEAT_WEAPON_SPECIALIZATION_BATTLE_AXE` | int | `148` |  |
| `FEAT_WEAPON_SPECIALIZATION_GREAT_AXE` | int | `149` |  |
| `FEAT_WEAPON_SPECIALIZATION_HALBERD` | int | `150` |  |
| `FEAT_WEAPON_SPECIALIZATION_LIGHT_HAMMER` | int | `151` |  |
| `FEAT_WEAPON_SPECIALIZATION_LIGHT_FLAIL` | int | `152` |  |
| `FEAT_WEAPON_SPECIALIZATION_WAR_HAMMER` | int | `153` |  |
| `FEAT_WEAPON_SPECIALIZATION_HEAVY_FLAIL` | int | `154` |  |
| `FEAT_WEAPON_SPECIALIZATION_KAMA` | int | `155` |  |
| `FEAT_WEAPON_SPECIALIZATION_KUKRI` | int | `156` |  |
| `FEAT_WEAPON_SPECIALIZATION_SHURIKEN` | int | `158` |  |
| `FEAT_WEAPON_SPECIALIZATION_SCYTHE` | int | `159` |  |
| `FEAT_WEAPON_SPECIALIZATION_KATANA` | int | `160` |  |
| `FEAT_WEAPON_SPECIALIZATION_BASTARD_SWORD` | int | `161` |  |
| `FEAT_WEAPON_SPECIALIZATION_DIRE_MACE` | int | `163` |  |
| `FEAT_WEAPON_SPECIALIZATION_DOUBLE_AXE` | int | `164` |  |
| `FEAT_WEAPON_SPECIALIZATION_TWO_BLADED_SWORD` | int | `165` |  |
| `FEAT_SPELL_FOCUS_CONJURATION` | int | `166` |  |
| `FEAT_SPELL_FOCUS_DIVINATION` | int | `167` |  |
| `FEAT_SPELL_FOCUS_ENCHANTMENT` | int | `168` |  |
| `FEAT_SPELL_FOCUS_EVOCATION` | int | `169` |  |
| `FEAT_SPELL_FOCUS_ILLUSION` | int | `170` |  |
| `FEAT_SPELL_FOCUS_NECROMANCY` | int | `171` |  |
| `FEAT_SPELL_FOCUS_TRANSMUTATION` | int | `172` |  |
| `FEAT_SKILL_FOCUS_CONCENTRATION` | int | `173` |  |
| `FEAT_SKILL_FOCUS_DISABLE_TRAP` | int | `174` |  |
| `FEAT_SKILL_FOCUS_DISCIPLINE` | int | `175` |  |
| `FEAT_SKILL_FOCUS_HEAL` | int | `177` |  |
| `FEAT_SKILL_FOCUS_HIDE` | int | `178` |  |
| `FEAT_SKILL_FOCUS_LISTEN` | int | `179` |  |
| `FEAT_SKILL_FOCUS_LORE` | int | `180` |  |
| `FEAT_SKILL_FOCUS_MOVE_SILENTLY` | int | `181` |  |
| `FEAT_SKILL_FOCUS_OPEN_LOCK` | int | `182` |  |
| `FEAT_SKILL_FOCUS_PARRY` | int | `183` |  |
| `FEAT_SKILL_FOCUS_PERFORM` | int | `184` |  |
| `FEAT_SKILL_FOCUS_PERSUADE` | int | `185` |  |
| `FEAT_SKILL_FOCUS_PICK_POCKET` | int | `186` |  |
| `FEAT_SKILL_FOCUS_SEARCH` | int | `187` |  |
| `FEAT_SKILL_FOCUS_SET_TRAP` | int | `188` |  |
| `FEAT_SKILL_FOCUS_SPELLCRAFT` | int | `189` |  |
| `FEAT_SKILL_FOCUS_SPOT` | int | `190` |  |
| `FEAT_SKILL_FOCUS_TAUNT` | int | `192` |  |
| `FEAT_SKILL_FOCUS_USE_MAGIC_DEVICE` | int | `193` |  |
| `FEAT_BARBARIAN_ENDURANCE` | int | `194` |  |
| `FEAT_UNCANNY_DODGE_1` | int | `195` |  |
| `FEAT_DAMAGE_REDUCTION` | int | `196` |  |
| `FEAT_BARDIC_KNOWLEDGE` | int | `197` |  |
| `FEAT_NATURE_SENSE` | int | `198` |  |
| `FEAT_ANIMAL_COMPANION` | int | `199` |  |
| `FEAT_WOODLAND_STRIDE` | int | `200` |  |
| `FEAT_TRACKLESS_STEP` | int | `201` |  |
| `FEAT_RESIST_NATURES_LURE` | int | `202` |  |
| `FEAT_VENOM_IMMUNITY` | int | `203` |  |
| `FEAT_FLURRY_OF_BLOWS` | int | `204` |  |
| `FEAT_EVASION` | int | `206` |  |
| `FEAT_MONK_ENDURANCE` | int | `207` |  |
| `FEAT_STILL_MIND` | int | `208` |  |
| `FEAT_PURITY_OF_BODY` | int | `209` |  |
| `FEAT_WHOLENESS_OF_BODY` | int | `211` |  |
| `FEAT_IMPROVED_EVASION` | int | `212` |  |
| `FEAT_KI_STRIKE` | int | `213` |  |
| `FEAT_DIAMOND_BODY` | int | `214` |  |
| `FEAT_DIAMOND_SOUL` | int | `215` |  |
| `FEAT_PERFECT_SELF` | int | `216` |  |
| `FEAT_DIVINE_GRACE` | int | `217` |  |
| `FEAT_DIVINE_HEALTH` | int | `219` |  |
| `FEAT_SNEAK_ATTACK` | int | `221` |  |
| `FEAT_CRIPPLING_STRIKE` | int | `222` |  |
| `FEAT_DEFENSIVE_ROLL` | int | `223` |  |
| `FEAT_OPPORTUNIST` | int | `224` |  |
| `FEAT_SKILL_MASTERY` | int | `225` |  |
| `FEAT_UNCANNY_REFLEX` | int | `226` |  |
| `FEAT_STONECUNNING` | int | `227` |  |
| `FEAT_DARKVISION` | int | `228` |  |
| `FEAT_HARDINESS_VERSUS_POISONS` | int | `229` |  |
| `FEAT_HARDINESS_VERSUS_SPELLS` | int | `230` |  |
| `FEAT_BATTLE_TRAINING_VERSUS_ORCS` | int | `231` |  |
| `FEAT_BATTLE_TRAINING_VERSUS_GOBLINS` | int | `232` |  |
| `FEAT_BATTLE_TRAINING_VERSUS_GIANTS` | int | `233` |  |
| `FEAT_SKILL_AFFINITY_LORE` | int | `234` |  |
| `FEAT_IMMUNITY_TO_SLEEP` | int | `235` |  |
| `FEAT_HARDINESS_VERSUS_ENCHANTMENTS` | int | `236` |  |
| `FEAT_SKILL_AFFINITY_LISTEN` | int | `237` |  |
| `FEAT_SKILL_AFFINITY_SEARCH` | int | `238` |  |
| `FEAT_SKILL_AFFINITY_SPOT` | int | `239` |  |
| `FEAT_KEEN_SENSE` | int | `240` |  |
| `FEAT_HARDINESS_VERSUS_ILLUSIONS` | int | `241` |  |
| `FEAT_BATTLE_TRAINING_VERSUS_REPTILIANS` | int | `242` |  |
| `FEAT_SKILL_AFFINITY_CONCENTRATION` | int | `243` |  |
| `FEAT_PARTIAL_SKILL_AFFINITY_LISTEN` | int | `244` |  |
| `FEAT_PARTIAL_SKILL_AFFINITY_SEARCH` | int | `245` |  |
| `FEAT_PARTIAL_SKILL_AFFINITY_SPOT` | int | `246` |  |
| `FEAT_SKILL_AFFINITY_MOVE_SILENTLY` | int | `247` |  |
| `FEAT_LUCKY` | int | `248` |  |
| `FEAT_FEARLESS` | int | `249` |  |
| `FEAT_GOOD_AIM` | int | `250` |  |
| `FEAT_UNCANNY_DODGE_2` | int | `251` |  |
| `FEAT_UNCANNY_DODGE_3` | int | `252` |  |
| `FEAT_UNCANNY_DODGE_4` | int | `253` |  |
| `FEAT_UNCANNY_DODGE_5` | int | `254` |  |
| `FEAT_UNCANNY_DODGE_6` | int | `255` |  |
| `FEAT_WEAPON_PROFICIENCY_ELF` | int | `256` |  |
| `FEAT_BARD_SONGS` | int | `257` |  |
| `FEAT_QUICK_TO_MASTER` | int | `258` |  |
| `FEAT_SLIPPERY_MIND` | int | `259` |  |
| `FEAT_MONK_AC_BONUS` | int | `260` |  |
| `FEAT_FAVORED_ENEMY_DWARF` | int | `261` |  |
| `FEAT_FAVORED_ENEMY_ELF` | int | `262` |  |
| `FEAT_FAVORED_ENEMY_GNOME` | int | `263` |  |
| `FEAT_FAVORED_ENEMY_HALFLING` | int | `264` |  |
| `FEAT_FAVORED_ENEMY_HALFELF` | int | `265` |  |
| `FEAT_FAVORED_ENEMY_HALFORC` | int | `266` |  |
| `FEAT_FAVORED_ENEMY_HUMAN` | int | `267` |  |
| `FEAT_FAVORED_ENEMY_ABERRATION` | int | `268` |  |
| `FEAT_FAVORED_ENEMY_ANIMAL` | int | `269` |  |
| `FEAT_FAVORED_ENEMY_BEAST` | int | `270` |  |
| `FEAT_FAVORED_ENEMY_CONSTRUCT` | int | `271` |  |
| `FEAT_FAVORED_ENEMY_DRAGON` | int | `272` |  |
| `FEAT_FAVORED_ENEMY_GOBLINOID` | int | `273` |  |
| `FEAT_FAVORED_ENEMY_MONSTROUS` | int | `274` |  |
| `FEAT_FAVORED_ENEMY_ORC` | int | `275` |  |
| `FEAT_FAVORED_ENEMY_REPTILIAN` | int | `276` |  |
| `FEAT_FAVORED_ENEMY_ELEMENTAL` | int | `277` |  |
| `FEAT_FAVORED_ENEMY_FEY` | int | `278` |  |
| `FEAT_FAVORED_ENEMY_GIANT` | int | `279` |  |
| `FEAT_FAVORED_ENEMY_MAGICAL_BEAST` | int | `280` |  |
| `FEAT_FAVORED_ENEMY_OUTSIDER` | int | `281` |  |
| `FEAT_FAVORED_ENEMY_SHAPECHANGER` | int | `284` |  |
| `FEAT_FAVORED_ENEMY_UNDEAD` | int | `285` |  |
| `FEAT_FAVORED_ENEMY_VERMIN` | int | `286` |  |
| `FEAT_WEAPON_PROFICIENCY_CREATURE` | int | `289` |  |
| `FEAT_WEAPON_SPECIALIZATION_CREATURE` | int | `290` |  |
| `FEAT_WEAPON_FOCUS_CREATURE` | int | `291` |  |
| `FEAT_IMPROVED_CRITICAL_CREATURE` | int | `292` |  |
| `FEAT_BARBARIAN_RAGE` | int | `293` |  |
| `FEAT_TURN_UNDEAD` | int | `294` |  |
| `FEAT_QUIVERING_PALM` | int | `296` |  |
| `FEAT_EMPTY_BODY` | int | `297` |  |
| `FEAT_LAY_ON_HANDS` | int | `299` |  |
| `FEAT_AURA_OF_COURAGE` | int | `300` |  |
| `FEAT_SMITE_EVIL` | int | `301` |  |
| `FEAT_REMOVE_DISEASE` | int | `302` |  |
| `FEAT_SUMMON_FAMILIAR` | int | `303` |  |
| `FEAT_ELEMENTAL_SHAPE` | int | `304` |  |
| `FEAT_WILD_SHAPE` | int | `305` |  |
| `FEAT_WAR_DOMAIN_POWER` | int | `306` |  |
| `FEAT_STRENGTH_DOMAIN_POWER` | int | `307` |  |
| `FEAT_PROTECTION_DOMAIN_POWER` | int | `308` |  |
| `FEAT_LUCK_DOMAIN_POWER` | int | `309` |  |
| `FEAT_DEATH_DOMAIN_POWER` | int | `310` |  |
| `FEAT_AIR_DOMAIN_POWER` | int | `311` |  |
| `FEAT_ANIMAL_DOMAIN_POWER` | int | `312` |  |
| `FEAT_DESTRUCTION_DOMAIN_POWER` | int | `313` |  |
| `FEAT_EARTH_DOMAIN_POWER` | int | `314` |  |
| `FEAT_EVIL_DOMAIN_POWER` | int | `315` |  |
| `FEAT_FIRE_DOMAIN_POWER` | int | `316` |  |
| `FEAT_GOOD_DOMAIN_POWER` | int | `317` |  |
| `FEAT_HEALING_DOMAIN_POWER` | int | `318` |  |
| `FEAT_KNOWLEDGE_DOMAIN_POWER` | int | `319` |  |
| `FEAT_MAGIC_DOMAIN_POWER` | int | `320` |  |
| `FEAT_PLANT_DOMAIN_POWER` | int | `321` |  |
| `FEAT_SUN_DOMAIN_POWER` | int | `322` |  |
| `FEAT_TRAVEL_DOMAIN_POWER` | int | `323` |  |
| `FEAT_TRICKERY_DOMAIN_POWER` | int | `324` |  |
| `FEAT_WATER_DOMAIN_POWER` | int | `325` |  |
| `FEAT_LOWLIGHTVISION` | int | `354` |  |
| `FEAT_IMPROVED_INITIATIVE` | int | `377` |  |
| `FEAT_ARTIST` | int | `378` |  |
| `FEAT_BLOODED` | int | `379` |  |
| `FEAT_BULLHEADED` | int | `380` |  |
| `FEAT_COURTLY_MAGOCRACY` | int | `381` |  |
| `FEAT_LUCK_OF_HEROES` | int | `382` |  |
| `FEAT_RESIST_POISON` | int | `383` |  |
| `FEAT_SILVER_PALM` | int | `384` |  |
| `FEAT_SNAKEBLOOD` | int | `386` |  |
| `FEAT_STEALTHY` | int | `387` |  |
| `FEAT_STRONGSOUL` | int | `388` |  |
| `FEAT_EXPERTISE` | int | `389` |  |
| `FEAT_IMPROVED_EXPERTISE` | int | `390` |  |
| `FEAT_GREAT_CLEAVE` | int | `391` |  |
| `FEAT_SPRING_ATTACK` | int | `392` |  |
| `FEAT_GREATER_SPELL_FOCUS_ABJURATION` | int | `393` |  |
| `FEAT_GREATER_SPELL_FOCUS_CONJURATION` | int | `394` |  |
| `FEAT_GREATER_SPELL_FOCUS_DIVINIATION` | int | `395` |  |
| `FEAT_GREATER_SPELL_FOCUS_DIVINATION` | int | `395` |  |
| `FEAT_GREATER_SPELL_FOCUS_ENCHANTMENT` | int | `396` |  |
| `FEAT_GREATER_SPELL_FOCUS_EVOCATION` | int | `397` |  |
| `FEAT_GREATER_SPELL_FOCUS_ILLUSION` | int | `398` |  |
| `FEAT_GREATER_SPELL_FOCUS_NECROMANCY` | int | `399` |  |
| `FEAT_GREATER_SPELL_FOCUS_TRANSMUTATION` | int | `400` |  |
| `FEAT_GREATER_SPELL_PENETRATION` | int | `401` |  |
| `FEAT_THUG` | int | `402` |  |
| `FEAT_SKILLFOCUS_APPRAISE` | int | `404` |  |
| `FEAT_SKILL_FOCUS_TUMBLE` | int | `406` |  |
| `FEAT_SKILL_FOCUS_CRAFT_TRAP` | int | `407` |  |
| `FEAT_BLIND_FIGHT` | int | `408` |  |
| `FEAT_CIRCLE_KICK` | int | `409` |  |
| `FEAT_EXTRA_STUNNING_ATTACK` | int | `410` |  |
| `FEAT_RAPID_RELOAD` | int | `411` |  |
| `FEAT_ZEN_ARCHERY` | int | `412` |  |
| `FEAT_DIVINE_MIGHT` | int | `413` |  |
| `FEAT_DIVINE_SHIELD` | int | `414` |  |
| `FEAT_ARCANE_DEFENSE_ABJURATION` | int | `415` |  |
| `FEAT_ARCANE_DEFENSE_CONJURATION` | int | `416` |  |
| `FEAT_ARCANE_DEFENSE_DIVINATION` | int | `417` |  |
| `FEAT_ARCANE_DEFENSE_ENCHANTMENT` | int | `418` |  |
| `FEAT_ARCANE_DEFENSE_EVOCATION` | int | `419` |  |
| `FEAT_ARCANE_DEFENSE_ILLUSION` | int | `420` |  |
| `FEAT_ARCANE_DEFENSE_NECROMANCY` | int | `421` |  |
| `FEAT_ARCANE_DEFENSE_TRANSMUTATION` | int | `422` |  |
| `FEAT_EXTRA_MUSIC` | int | `423` |  |
| `FEAT_LINGERING_SONG` | int | `424` |  |
| `FEAT_DIRTY_FIGHTING` | int | `425` |  |
| `FEAT_RESIST_DISEASE` | int | `426` |  |
| `FEAT_RESIST_ENERGY_COLD` | int | `427` |  |
| `FEAT_RESIST_ENERGY_ACID` | int | `428` |  |
| `FEAT_RESIST_ENERGY_FIRE` | int | `429` |  |
| `FEAT_RESIST_ENERGY_ELECTRICAL` | int | `430` |  |
| `FEAT_RESIST_ENERGY_SONIC` | int | `431` |  |
| `FEAT_HIDE_IN_PLAIN_SIGHT` | int | `433` |  |
| `FEAT_SHADOW_DAZE` | int | `434` |  |
| `FEAT_SUMMON_SHADOW` | int | `435` |  |
| `FEAT_SHADOW_EVADE` | int | `436` |  |
| `FEAT_DENEIRS_EYE` | int | `437` |  |
| `FEAT_TYMORAS_SMILE` | int | `438` |  |
| `FEAT_LLIIRAS_HEART` | int | `439` |  |
| `FEAT_CRAFT_HARPER_ITEM` | int | `440` |  |
| `FEAT_HARPER_SLEEP` | int | `441` |  |
| `FEAT_HARPER_CATS_GRACE` | int | `442` |  |
| `FEAT_HARPER_EAGLES_SPLENDOR` | int | `443` |  |
| `FEAT_HARPER_INVISIBILITY` | int | `444` |  |
| `FEAT_PRESTIGE_ENCHANT_ARROW_1` | int | `445` |  |
| `FEAT_PRESTIGE_ENCHANT_ARROW_2` | int | `446` |  |
| `FEAT_PRESTIGE_ENCHANT_ARROW_3` | int | `447` |  |
| `FEAT_PRESTIGE_ENCHANT_ARROW_4` | int | `448` |  |
| `FEAT_PRESTIGE_ENCHANT_ARROW_5` | int | `449` |  |
| `FEAT_PRESTIGE_IMBUE_ARROW` | int | `450` |  |
| `FEAT_PRESTIGE_SEEKER_ARROW_1` | int | `451` |  |
| `FEAT_PRESTIGE_SEEKER_ARROW_2` | int | `452` |  |
| `FEAT_PRESTIGE_HAIL_OF_ARROWS` | int | `453` |  |
| `FEAT_PRESTIGE_ARROW_OF_DEATH` | int | `454` |  |
| `FEAT_PRESTIGE_DEATH_ATTACK_1` | int | `455` |  |
| `FEAT_PRESTIGE_DEATH_ATTACK_2` | int | `456` |  |
| `FEAT_PRESTIGE_DEATH_ATTACK_3` | int | `457` |  |
| `FEAT_PRESTIGE_DEATH_ATTACK_4` | int | `458` |  |
| `FEAT_PRESTIGE_DEATH_ATTACK_5` | int | `459` |  |
| `FEAT_BLACKGUARD_SNEAK_ATTACK_1D6` | int | `460` |  |
| `FEAT_BLACKGUARD_SNEAK_ATTACK_2D6` | int | `461` |  |
| `FEAT_BLACKGUARD_SNEAK_ATTACK_3D6` | int | `462` |  |
| `FEAT_PRESTIGE_POISON_SAVE_1` | int | `463` |  |
| `FEAT_PRESTIGE_POISON_SAVE_2` | int | `464` |  |
| `FEAT_PRESTIGE_POISON_SAVE_3` | int | `465` |  |
| `FEAT_PRESTIGE_POISON_SAVE_4` | int | `466` |  |
| `FEAT_PRESTIGE_POISON_SAVE_5` | int | `467` |  |
| `FEAT_PRESTIGE_SPELL_GHOSTLY_VISAGE` | int | `468` |  |
| `FEAT_PRESTIGE_DARKNESS` | int | `469` |  |
| `FEAT_PRESTIGE_INVISIBILITY_1` | int | `470` |  |
| `FEAT_PRESTIGE_INVISIBILITY_2` | int | `471` |  |
| `FEAT_SMITE_GOOD` | int | `472` |  |
| `FEAT_PRESTIGE_DARK_BLESSING` | int | `473` |  |
| `FEAT_INFLICT_LIGHT_WOUNDS` | int | `474` |  |
| `FEAT_INFLICT_MODERATE_WOUNDS` | int | `475` |  |
| `FEAT_INFLICT_SERIOUS_WOUNDS` | int | `476` |  |
| `FEAT_INFLICT_CRITICAL_WOUNDS` | int | `477` |  |
| `FEAT_BULLS_STRENGTH` | int | `478` |  |
| `FEAT_CONTAGION` | int | `479` |  |
| `FEAT_EYE_OF_GRUUMSH_BLINDING_SPITTLE` | int | `480` |  |
| `FEAT_EYE_OF_GRUUMSH_BLINDING_SPITTLE_2` | int | `481` |  |
| `FEAT_EYE_OF_GRUUMSH_COMMAND_THE_HORDE` | int | `482` |  |
| `FEAT_EYE_OF_GRUUMSH_SWING_BLINDLY` | int | `483` |  |
| `FEAT_EYE_OF_GRUUMSH_RITUAL_SCARRING` | int | `484` |  |
| `FEAT_BLINDSIGHT_5_FEET` | int | `485` |  |
| `FEAT_BLINDSIGHT_10_FEET` | int | `486` |  |
| `FEAT_EYE_OF_GRUUMSH_SIGHT_OF_GRUUMSH` | int | `487` |  |
| `FEAT_BLINDSIGHT_60_FEET` | int | `488` |  |
| `FEAT_SHOU_DISCIPLE_DODGE_2` | int | `489` |  |
| `FEAT_EPIC_ARMOR_SKIN` | int | `490` |  |
| `FEAT_EPIC_BLINDING_SPEED` | int | `491` |  |
| `FEAT_EPIC_DAMAGE_REDUCTION_3` | int | `492` |  |
| `FEAT_EPIC_DAMAGE_REDUCTION_6` | int | `493` |  |
| `FEAT_EPIC_DAMAGE_REDUCTION_9` | int | `494` |  |
| `FEAT_EPIC_DEVASTATING_CRITICAL_CLUB` | int | `495` |  |
| `FEAT_EPIC_DEVASTATING_CRITICAL_DAGGER` | int | `496` |  |
| `FEAT_EPIC_DEVASTATING_CRITICAL_DART` | int | `497` |  |
| `FEAT_EPIC_DEVASTATING_CRITICAL_HEAVYCROSSBOW` | int | `498` |  |
| `FEAT_EPIC_DEVASTATING_CRITICAL_LIGHTCROSSBOW` | int | `499` |  |
| `FEAT_EPIC_DEVASTATING_CRITICAL_LIGHTMACE` | int | `500` |  |
| `FEAT_EPIC_DEVASTATING_CRITICAL_MORNINGSTAR` | int | `501` |  |
| `FEAT_EPIC_DEVASTATING_CRITICAL_QUARTERSTAFF` | int | `502` |  |
| `FEAT_EPIC_DEVASTATING_CRITICAL_SHORTSPEAR` | int | `503` |  |
| `FEAT_EPIC_DEVASTATING_CRITICAL_SICKLE` | int | `504` |  |
| `FEAT_EPIC_DEVASTATING_CRITICAL_SLING` | int | `505` |  |
| `FEAT_EPIC_DEVASTATING_CRITICAL_UNARMED` | int | `506` |  |
| `FEAT_EPIC_DEVASTATING_CRITICAL_LONGBOW` | int | `507` |  |
| `FEAT_EPIC_DEVASTATING_CRITICAL_SHORTBOW` | int | `508` |  |
| `FEAT_EPIC_DEVASTATING_CRITICAL_SHORTSWORD` | int | `509` |  |
| `FEAT_EPIC_DEVASTATING_CRITICAL_RAPIER` | int | `510` |  |
| `FEAT_EPIC_DEVASTATING_CRITICAL_SCIMITAR` | int | `511` |  |
| `FEAT_EPIC_DEVASTATING_CRITICAL_LONGSWORD` | int | `512` |  |
| `FEAT_EPIC_DEVASTATING_CRITICAL_GREATSWORD` | int | `513` |  |
| `FEAT_EPIC_DEVASTATING_CRITICAL_HANDAXE` | int | `514` |  |
| `FEAT_EPIC_DEVASTATING_CRITICAL_THROWINGAXE` | int | `515` |  |
| `FEAT_EPIC_DEVASTATING_CRITICAL_BATTLEAXE` | int | `516` |  |
| `FEAT_EPIC_DEVASTATING_CRITICAL_GREATAXE` | int | `517` |  |
| `FEAT_EPIC_DEVASTATING_CRITICAL_HALBERD` | int | `518` |  |
| `FEAT_EPIC_DEVASTATING_CRITICAL_LIGHTHAMMER` | int | `519` |  |
| `FEAT_EPIC_DEVASTATING_CRITICAL_LIGHTFLAIL` | int | `520` |  |
| `FEAT_EPIC_DEVASTATING_CRITICAL_WARHAMMER` | int | `521` |  |
| `FEAT_EPIC_DEVASTATING_CRITICAL_HEAVYFLAIL` | int | `522` |  |
| `FEAT_EPIC_DEVASTATING_CRITICAL_KAMA` | int | `523` |  |
| `FEAT_EPIC_DEVASTATING_CRITICAL_KUKRI` | int | `524` |  |
| `FEAT_EPIC_DEVASTATING_CRITICAL_SHURIKEN` | int | `525` |  |
| `FEAT_EPIC_DEVASTATING_CRITICAL_SCYTHE` | int | `526` |  |
| `FEAT_EPIC_DEVASTATING_CRITICAL_KATANA` | int | `527` |  |
| `FEAT_EPIC_DEVASTATING_CRITICAL_BASTARDSWORD` | int | `528` |  |
| `FEAT_EPIC_DEVASTATING_CRITICAL_DIREMACE` | int | `529` |  |
| `FEAT_EPIC_DEVASTATING_CRITICAL_DOUBLEAXE` | int | `530` |  |
| `FEAT_EPIC_DEVASTATING_CRITICAL_TWOBLADEDSWORD` | int | `531` |  |
| `FEAT_EPIC_DEVASTATING_CRITICAL_CREATURE` | int | `532` |  |
| `FEAT_EPIC_ENERGY_RESISTANCE_COLD_1` | int | `533` |  |
| `FEAT_EPIC_ENERGY_RESISTANCE_COLD_2` | int | `534` |  |
| `FEAT_EPIC_ENERGY_RESISTANCE_COLD_3` | int | `535` |  |
| `FEAT_EPIC_ENERGY_RESISTANCE_COLD_4` | int | `536` |  |
| `FEAT_EPIC_ENERGY_RESISTANCE_COLD_5` | int | `537` |  |
| `FEAT_EPIC_ENERGY_RESISTANCE_COLD_6` | int | `538` |  |
| `FEAT_EPIC_ENERGY_RESISTANCE_COLD_7` | int | `539` |  |
| `FEAT_EPIC_ENERGY_RESISTANCE_COLD_8` | int | `540` |  |
| `FEAT_EPIC_ENERGY_RESISTANCE_COLD_9` | int | `541` |  |
| `FEAT_EPIC_ENERGY_RESISTANCE_COLD_10` | int | `542` |  |
| `FEAT_EPIC_ENERGY_RESISTANCE_ACID_1` | int | `543` |  |
| `FEAT_EPIC_ENERGY_RESISTANCE_ACID_2` | int | `544` |  |
| `FEAT_EPIC_ENERGY_RESISTANCE_ACID_3` | int | `545` |  |
| `FEAT_EPIC_ENERGY_RESISTANCE_ACID_4` | int | `546` |  |
| `FEAT_EPIC_ENERGY_RESISTANCE_ACID_5` | int | `547` |  |
| `FEAT_EPIC_ENERGY_RESISTANCE_ACID_6` | int | `548` |  |
| `FEAT_EPIC_ENERGY_RESISTANCE_ACID_7` | int | `549` |  |
| `FEAT_EPIC_ENERGY_RESISTANCE_ACID_8` | int | `550` |  |
| `FEAT_EPIC_ENERGY_RESISTANCE_ACID_9` | int | `551` |  |
| `FEAT_EPIC_ENERGY_RESISTANCE_ACID_10` | int | `552` |  |
| `FEAT_EPIC_ENERGY_RESISTANCE_FIRE_1` | int | `553` |  |
| `FEAT_EPIC_ENERGY_RESISTANCE_FIRE_2` | int | `554` |  |
| `FEAT_EPIC_ENERGY_RESISTANCE_FIRE_3` | int | `555` |  |
| `FEAT_EPIC_ENERGY_RESISTANCE_FIRE_4` | int | `556` |  |
| `FEAT_EPIC_ENERGY_RESISTANCE_FIRE_5` | int | `557` |  |
| `FEAT_EPIC_ENERGY_RESISTANCE_FIRE_6` | int | `558` |  |
| `FEAT_EPIC_ENERGY_RESISTANCE_FIRE_7` | int | `559` |  |
| `FEAT_EPIC_ENERGY_RESISTANCE_FIRE_8` | int | `560` |  |
| `FEAT_EPIC_ENERGY_RESISTANCE_FIRE_9` | int | `561` |  |
| `FEAT_EPIC_ENERGY_RESISTANCE_FIRE_10` | int | `562` |  |
| `FEAT_EPIC_ENERGY_RESISTANCE_ELECTRICAL_1` | int | `563` |  |
| `FEAT_EPIC_ENERGY_RESISTANCE_ELECTRICAL_2` | int | `564` |  |
| `FEAT_EPIC_ENERGY_RESISTANCE_ELECTRICAL_3` | int | `565` |  |
| `FEAT_EPIC_ENERGY_RESISTANCE_ELECTRICAL_4` | int | `566` |  |
| `FEAT_EPIC_ENERGY_RESISTANCE_ELECTRICAL_5` | int | `567` |  |
| `FEAT_EPIC_ENERGY_RESISTANCE_ELECTRICAL_6` | int | `568` |  |
| `FEAT_EPIC_ENERGY_RESISTANCE_ELECTRICAL_7` | int | `569` |  |
| `FEAT_EPIC_ENERGY_RESISTANCE_ELECTRICAL_8` | int | `570` |  |
| `FEAT_EPIC_ENERGY_RESISTANCE_ELECTRICAL_9` | int | `571` |  |
| `FEAT_EPIC_ENERGY_RESISTANCE_ELECTRICAL_10` | int | `572` |  |
| `FEAT_EPIC_ENERGY_RESISTANCE_SONIC_1` | int | `573` |  |
| `FEAT_EPIC_ENERGY_RESISTANCE_SONIC_2` | int | `574` |  |
| `FEAT_EPIC_ENERGY_RESISTANCE_SONIC_3` | int | `575` |  |
| `FEAT_EPIC_ENERGY_RESISTANCE_SONIC_4` | int | `576` |  |
| `FEAT_EPIC_ENERGY_RESISTANCE_SONIC_5` | int | `577` |  |
| `FEAT_EPIC_ENERGY_RESISTANCE_SONIC_6` | int | `578` |  |
| `FEAT_EPIC_ENERGY_RESISTANCE_SONIC_7` | int | `579` |  |
| `FEAT_EPIC_ENERGY_RESISTANCE_SONIC_8` | int | `580` |  |
| `FEAT_EPIC_ENERGY_RESISTANCE_SONIC_9` | int | `581` |  |
| `FEAT_EPIC_ENERGY_RESISTANCE_SONIC_10` | int | `582` |  |
| `FEAT_EPIC_FORTITUDE` | int | `583` |  |
| `FEAT_EPIC_PROWESS` | int | `584` |  |
| `FEAT_EPIC_REFLEXES` | int | `585` |  |
| `FEAT_EPIC_REPUTATION` | int | `586` |  |
| `FEAT_EPIC_SKILL_FOCUS_ANIMAL_EMPATHY` | int | `587` |  |
| `FEAT_EPIC_SKILL_FOCUS_APPRAISE` | int | `588` |  |
| `FEAT_EPIC_SKILL_FOCUS_CONCENTRATION` | int | `589` |  |
| `FEAT_EPIC_SKILL_FOCUS_CRAFT_TRAP` | int | `590` |  |
| `FEAT_EPIC_SKILL_FOCUS_DISABLETRAP` | int | `591` |  |
| `FEAT_EPIC_SKILL_FOCUS_DISCIPLINE` | int | `592` |  |
| `FEAT_EPIC_SKILL_FOCUS_HEAL` | int | `593` |  |
| `FEAT_EPIC_SKILL_FOCUS_HIDE` | int | `594` |  |
| `FEAT_EPIC_SKILL_FOCUS_LISTEN` | int | `595` |  |
| `FEAT_EPIC_SKILL_FOCUS_LORE` | int | `596` |  |
| `FEAT_EPIC_SKILL_FOCUS_MOVESILENTLY` | int | `597` |  |
| `FEAT_EPIC_SKILL_FOCUS_OPENLOCK` | int | `598` |  |
| `FEAT_EPIC_SKILL_FOCUS_PARRY` | int | `599` |  |
| `FEAT_EPIC_SKILL_FOCUS_PERFORM` | int | `600` |  |
| `FEAT_EPIC_SKILL_FOCUS_PERSUADE` | int | `601` |  |
| `FEAT_EPIC_SKILL_FOCUS_PICKPOCKET` | int | `602` |  |
| `FEAT_EPIC_SKILL_FOCUS_SEARCH` | int | `603` |  |
| `FEAT_EPIC_SKILL_FOCUS_SETTRAP` | int | `604` |  |
| `FEAT_EPIC_SKILL_FOCUS_SPELLCRAFT` | int | `605` |  |
| `FEAT_EPIC_SKILL_FOCUS_SPOT` | int | `606` |  |
| `FEAT_EPIC_SKILL_FOCUS_TAUNT` | int | `607` |  |
| `FEAT_EPIC_SKILL_FOCUS_TUMBLE` | int | `608` |  |
| `FEAT_EPIC_SKILL_FOCUS_USEMAGICDEVICE` | int | `609` |  |
| `FEAT_EPIC_SPELL_FOCUS_ABJURATION` | int | `610` |  |
| `FEAT_EPIC_SPELL_FOCUS_CONJURATION` | int | `611` |  |
| `FEAT_EPIC_SPELL_FOCUS_DIVINATION` | int | `612` |  |
| `FEAT_EPIC_SPELL_FOCUS_ENCHANTMENT` | int | `613` |  |
| `FEAT_EPIC_SPELL_FOCUS_EVOCATION` | int | `614` |  |
| `FEAT_EPIC_SPELL_FOCUS_ILLUSION` | int | `615` |  |
| `FEAT_EPIC_SPELL_FOCUS_NECROMANCY` | int | `616` |  |
| `FEAT_EPIC_SPELL_FOCUS_TRANSMUTATION` | int | `617` |  |
| `FEAT_EPIC_SPELL_PENETRATION` | int | `618` |  |
| `FEAT_EPIC_WEAPON_FOCUS_CLUB` | int | `619` |  |
| `FEAT_EPIC_WEAPON_FOCUS_DAGGER` | int | `620` |  |
| `FEAT_EPIC_WEAPON_FOCUS_DART` | int | `621` |  |
| `FEAT_EPIC_WEAPON_FOCUS_HEAVYCROSSBOW` | int | `622` |  |
| `FEAT_EPIC_WEAPON_FOCUS_LIGHTCROSSBOW` | int | `623` |  |
| `FEAT_EPIC_WEAPON_FOCUS_LIGHTMACE` | int | `624` |  |
| `FEAT_EPIC_WEAPON_FOCUS_MORNINGSTAR` | int | `625` |  |
| `FEAT_EPIC_WEAPON_FOCUS_QUARTERSTAFF` | int | `626` |  |
| `FEAT_EPIC_WEAPON_FOCUS_SHORTSPEAR` | int | `627` |  |
| `FEAT_EPIC_WEAPON_FOCUS_SICKLE` | int | `628` |  |
| `FEAT_EPIC_WEAPON_FOCUS_SLING` | int | `629` |  |
| `FEAT_EPIC_WEAPON_FOCUS_UNARMED` | int | `630` |  |
| `FEAT_EPIC_WEAPON_FOCUS_LONGBOW` | int | `631` |  |
| `FEAT_EPIC_WEAPON_FOCUS_SHORTBOW` | int | `632` |  |
| `FEAT_EPIC_WEAPON_FOCUS_SHORTSWORD` | int | `633` |  |
| `FEAT_EPIC_WEAPON_FOCUS_RAPIER` | int | `634` |  |
| `FEAT_EPIC_WEAPON_FOCUS_SCIMITAR` | int | `635` |  |
| `FEAT_EPIC_WEAPON_FOCUS_LONGSWORD` | int | `636` |  |
| `FEAT_EPIC_WEAPON_FOCUS_GREATSWORD` | int | `637` |  |
| `FEAT_EPIC_WEAPON_FOCUS_HANDAXE` | int | `638` |  |
| `FEAT_EPIC_WEAPON_FOCUS_THROWINGAXE` | int | `639` |  |
| `FEAT_EPIC_WEAPON_FOCUS_BATTLEAXE` | int | `640` |  |
| `FEAT_EPIC_WEAPON_FOCUS_GREATAXE` | int | `641` |  |
| `FEAT_EPIC_WEAPON_FOCUS_HALBERD` | int | `642` |  |
| `FEAT_EPIC_WEAPON_FOCUS_LIGHTHAMMER` | int | `643` |  |
| `FEAT_EPIC_WEAPON_FOCUS_LIGHTFLAIL` | int | `644` |  |
| `FEAT_EPIC_WEAPON_FOCUS_WARHAMMER` | int | `645` |  |
| `FEAT_EPIC_WEAPON_FOCUS_HEAVYFLAIL` | int | `646` |  |
| `FEAT_EPIC_WEAPON_FOCUS_KAMA` | int | `647` |  |
| `FEAT_EPIC_WEAPON_FOCUS_KUKRI` | int | `648` |  |
| `FEAT_EPIC_WEAPON_FOCUS_SHURIKEN` | int | `649` |  |
| `FEAT_EPIC_WEAPON_FOCUS_SCYTHE` | int | `650` |  |
| `FEAT_EPIC_WEAPON_FOCUS_KATANA` | int | `651` |  |
| `FEAT_EPIC_WEAPON_FOCUS_BASTARDSWORD` | int | `652` |  |
| `FEAT_EPIC_WEAPON_FOCUS_DIREMACE` | int | `653` |  |
| `FEAT_EPIC_WEAPON_FOCUS_DOUBLEAXE` | int | `654` |  |
| `FEAT_EPIC_WEAPON_FOCUS_TWOBLADEDSWORD` | int | `655` |  |
| `FEAT_EPIC_WEAPON_FOCUS_CREATURE` | int | `656` |  |
| `FEAT_EPIC_WEAPON_SPECIALIZATION_CLUB` | int | `657` |  |
| `FEAT_EPIC_WEAPON_SPECIALIZATION_DAGGER` | int | `658` |  |
| `FEAT_EPIC_WEAPON_SPECIALIZATION_DART` | int | `659` |  |
| `FEAT_EPIC_WEAPON_SPECIALIZATION_HEAVYCROSSBOW` | int | `660` |  |
| `FEAT_EPIC_WEAPON_SPECIALIZATION_LIGHTCROSSBOW` | int | `661` |  |
| `FEAT_EPIC_WEAPON_SPECIALIZATION_LIGHTMACE` | int | `662` |  |
| `FEAT_EPIC_WEAPON_SPECIALIZATION_MORNINGSTAR` | int | `663` |  |
| `FEAT_EPIC_WEAPON_SPECIALIZATION_QUARTERSTAFF` | int | `664` |  |
| `FEAT_EPIC_WEAPON_SPECIALIZATION_SHORTSPEAR` | int | `665` |  |
| `FEAT_EPIC_WEAPON_SPECIALIZATION_SICKLE` | int | `666` |  |
| `FEAT_EPIC_WEAPON_SPECIALIZATION_SLING` | int | `667` |  |
| `FEAT_EPIC_WEAPON_SPECIALIZATION_UNARMED` | int | `668` |  |
| `FEAT_EPIC_WEAPON_SPECIALIZATION_LONGBOW` | int | `669` |  |
| `FEAT_EPIC_WEAPON_SPECIALIZATION_SHORTBOW` | int | `670` |  |
| `FEAT_EPIC_WEAPON_SPECIALIZATION_SHORTSWORD` | int | `671` |  |
| `FEAT_EPIC_WEAPON_SPECIALIZATION_RAPIER` | int | `672` |  |
| `FEAT_EPIC_WEAPON_SPECIALIZATION_SCIMITAR` | int | `673` |  |
| `FEAT_EPIC_WEAPON_SPECIALIZATION_LONGSWORD` | int | `674` |  |
| `FEAT_EPIC_WEAPON_SPECIALIZATION_GREATSWORD` | int | `675` |  |
| `FEAT_EPIC_WEAPON_SPECIALIZATION_HANDAXE` | int | `676` |  |
| `FEAT_EPIC_WEAPON_SPECIALIZATION_THROWINGAXE` | int | `677` |  |
| `FEAT_EPIC_WEAPON_SPECIALIZATION_BATTLEAXE` | int | `678` |  |
| `FEAT_EPIC_WEAPON_SPECIALIZATION_GREATAXE` | int | `679` |  |
| `FEAT_EPIC_WEAPON_SPECIALIZATION_HALBERD` | int | `680` |  |
| `FEAT_EPIC_WEAPON_SPECIALIZATION_LIGHTHAMMER` | int | `681` |  |
| `FEAT_EPIC_WEAPON_SPECIALIZATION_LIGHTFLAIL` | int | `682` |  |
| `FEAT_EPIC_WEAPON_SPECIALIZATION_WARHAMMER` | int | `683` |  |
| `FEAT_EPIC_WEAPON_SPECIALIZATION_HEAVYFLAIL` | int | `684` |  |
| `FEAT_EPIC_WEAPON_SPECIALIZATION_KAMA` | int | `685` |  |
| `FEAT_EPIC_WEAPON_SPECIALIZATION_KUKRI` | int | `686` |  |
| `FEAT_EPIC_WEAPON_SPECIALIZATION_SHURIKEN` | int | `687` |  |
| `FEAT_EPIC_WEAPON_SPECIALIZATION_SCYTHE` | int | `688` |  |
| `FEAT_EPIC_WEAPON_SPECIALIZATION_KATANA` | int | `689` |  |
| `FEAT_EPIC_WEAPON_SPECIALIZATION_BASTARDSWORD` | int | `690` |  |
| `FEAT_EPIC_WEAPON_SPECIALIZATION_DIREMACE` | int | `691` |  |
| `FEAT_EPIC_WEAPON_SPECIALIZATION_DOUBLEAXE` | int | `692` |  |
| `FEAT_EPIC_WEAPON_SPECIALIZATION_TWOBLADEDSWORD` | int | `693` |  |
| `FEAT_EPIC_WEAPON_SPECIALIZATION_CREATURE` | int | `694` |  |
| `FEAT_EPIC_WILL` | int | `695` |  |
| `FEAT_EPIC_IMPROVED_COMBAT_CASTING` | int | `696` |  |
| `FEAT_EPIC_IMPROVED_KI_STRIKE_4` | int | `697` |  |
| `FEAT_EPIC_IMPROVED_KI_STRIKE_5` | int | `698` |  |
| `FEAT_EPIC_IMPROVED_SPELL_RESISTANCE_1` | int | `699` |  |
| `FEAT_EPIC_IMPROVED_SPELL_RESISTANCE_2` | int | `700` |  |
| `FEAT_EPIC_IMPROVED_SPELL_RESISTANCE_3` | int | `701` |  |
| `FEAT_EPIC_IMPROVED_SPELL_RESISTANCE_4` | int | `702` |  |
| `FEAT_EPIC_IMPROVED_SPELL_RESISTANCE_5` | int | `703` |  |
| `FEAT_EPIC_IMPROVED_SPELL_RESISTANCE_6` | int | `704` |  |
| `FEAT_EPIC_IMPROVED_SPELL_RESISTANCE_7` | int | `705` |  |
| `FEAT_EPIC_IMPROVED_SPELL_RESISTANCE_8` | int | `706` |  |
| `FEAT_EPIC_IMPROVED_SPELL_RESISTANCE_9` | int | `707` |  |
| `FEAT_EPIC_IMPROVED_SPELL_RESISTANCE_10` | int | `708` |  |
| `FEAT_EPIC_OVERWHELMING_CRITICAL_CLUB` | int | `709` |  |
| `FEAT_EPIC_OVERWHELMING_CRITICAL_DAGGER` | int | `710` |  |
| `FEAT_EPIC_OVERWHELMING_CRITICAL_DART` | int | `711` |  |
| `FEAT_EPIC_OVERWHELMING_CRITICAL_HEAVYCROSSBOW` | int | `712` |  |
| `FEAT_EPIC_OVERWHELMING_CRITICAL_LIGHTCROSSBOW` | int | `713` |  |
| `FEAT_EPIC_OVERWHELMING_CRITICAL_LIGHTMACE` | int | `714` |  |
| `FEAT_EPIC_OVERWHELMING_CRITICAL_MORNINGSTAR` | int | `715` |  |
| `FEAT_EPIC_OVERWHELMING_CRITICAL_QUARTERSTAFF` | int | `716` |  |
| `FEAT_EPIC_OVERWHELMING_CRITICAL_SHORTSPEAR` | int | `717` |  |
| `FEAT_EPIC_OVERWHELMING_CRITICAL_SICKLE` | int | `718` |  |
| `FEAT_EPIC_OVERWHELMING_CRITICAL_SLING` | int | `719` |  |
| `FEAT_EPIC_OVERWHELMING_CRITICAL_UNARMED` | int | `720` |  |
| `FEAT_EPIC_OVERWHELMING_CRITICAL_LONGBOW` | int | `721` |  |
| `FEAT_EPIC_OVERWHELMING_CRITICAL_SHORTBOW` | int | `722` |  |
| `FEAT_EPIC_OVERWHELMING_CRITICAL_SHORTSWORD` | int | `723` |  |
| `FEAT_EPIC_OVERWHELMING_CRITICAL_RAPIER` | int | `724` |  |
| `FEAT_EPIC_OVERWHELMING_CRITICAL_SCIMITAR` | int | `725` |  |
| `FEAT_EPIC_OVERWHELMING_CRITICAL_LONGSWORD` | int | `726` |  |
| `FEAT_EPIC_OVERWHELMING_CRITICAL_GREATSWORD` | int | `727` |  |
| `FEAT_EPIC_OVERWHELMING_CRITICAL_HANDAXE` | int | `728` |  |
| `FEAT_EPIC_OVERWHELMING_CRITICAL_THROWINGAXE` | int | `729` |  |
| `FEAT_EPIC_OVERWHELMING_CRITICAL_BATTLEAXE` | int | `730` |  |
| `FEAT_EPIC_OVERWHELMING_CRITICAL_GREATAXE` | int | `731` |  |
| `FEAT_EPIC_OVERWHELMING_CRITICAL_HALBERD` | int | `732` |  |
| `FEAT_EPIC_OVERWHELMING_CRITICAL_LIGHTHAMMER` | int | `733` |  |
| `FEAT_EPIC_OVERWHELMING_CRITICAL_LIGHTFLAIL` | int | `734` |  |
| `FEAT_EPIC_OVERWHELMING_CRITICAL_WARHAMMER` | int | `735` |  |
| `FEAT_EPIC_OVERWHELMING_CRITICAL_HEAVYFLAIL` | int | `736` |  |
| `FEAT_EPIC_OVERWHELMING_CRITICAL_KAMA` | int | `737` |  |
| `FEAT_EPIC_OVERWHELMING_CRITICAL_KUKRI` | int | `738` |  |
| `FEAT_EPIC_OVERWHELMING_CRITICAL_SHURIKEN` | int | `739` |  |
| `FEAT_EPIC_OVERWHELMING_CRITICAL_SCYTHE` | int | `740` |  |
| `FEAT_EPIC_OVERWHELMING_CRITICAL_KATANA` | int | `741` |  |
| `FEAT_EPIC_OVERWHELMING_CRITICAL_BASTARDSWORD` | int | `742` |  |
| `FEAT_EPIC_OVERWHELMING_CRITICAL_DIREMACE` | int | `743` |  |
| `FEAT_EPIC_OVERWHELMING_CRITICAL_DOUBLEAXE` | int | `744` |  |
| `FEAT_EPIC_OVERWHELMING_CRITICAL_TWOBLADEDSWORD` | int | `745` |  |
| `FEAT_EPIC_OVERWHELMING_CRITICAL_CREATURE` | int | `746` |  |
| `FEAT_EPIC_PERFECT_HEALTH` | int | `747` |  |
| `FEAT_EPIC_SELF_CONCEALMENT_10` | int | `748` |  |
| `FEAT_EPIC_SELF_CONCEALMENT_20` | int | `749` |  |
| `FEAT_EPIC_SELF_CONCEALMENT_30` | int | `750` |  |
| `FEAT_EPIC_SELF_CONCEALMENT_40` | int | `751` |  |
| `FEAT_EPIC_SELF_CONCEALMENT_50` | int | `752` |  |
| `FEAT_EPIC_SUPERIOR_INITIATIVE` | int | `753` |  |
| `FEAT_EPIC_TOUGHNESS_1` | int | `754` |  |
| `FEAT_EPIC_TOUGHNESS_2` | int | `755` |  |
| `FEAT_EPIC_TOUGHNESS_3` | int | `756` |  |
| `FEAT_EPIC_TOUGHNESS_4` | int | `757` |  |
| `FEAT_EPIC_TOUGHNESS_5` | int | `758` |  |
| `FEAT_EPIC_TOUGHNESS_6` | int | `759` |  |
| `FEAT_EPIC_TOUGHNESS_7` | int | `760` |  |
| `FEAT_EPIC_TOUGHNESS_8` | int | `761` |  |
| `FEAT_EPIC_TOUGHNESS_9` | int | `762` |  |
| `FEAT_EPIC_TOUGHNESS_10` | int | `763` |  |
| `FEAT_EPIC_GREAT_CHARISMA_1` | int | `764` |  |
| `FEAT_EPIC_GREAT_CHARISMA_2` | int | `765` |  |
| `FEAT_EPIC_GREAT_CHARISMA_3` | int | `766` |  |
| `FEAT_EPIC_GREAT_CHARISMA_4` | int | `767` |  |
| `FEAT_EPIC_GREAT_CHARISMA_5` | int | `768` |  |
| `FEAT_EPIC_GREAT_CHARISMA_6` | int | `769` |  |
| `FEAT_EPIC_GREAT_CHARISMA_7` | int | `770` |  |
| `FEAT_EPIC_GREAT_CHARISMA_8` | int | `771` |  |
| `FEAT_EPIC_GREAT_CHARISMA_9` | int | `772` |  |
| `FEAT_EPIC_GREAT_CHARISMA_10` | int | `773` |  |
| `FEAT_EPIC_GREAT_CONSTITUTION_1` | int | `774` |  |
| `FEAT_EPIC_GREAT_CONSTITUTION_2` | int | `775` |  |
| `FEAT_EPIC_GREAT_CONSTITUTION_3` | int | `776` |  |
| `FEAT_EPIC_GREAT_CONSTITUTION_4` | int | `777` |  |
| `FEAT_EPIC_GREAT_CONSTITUTION_5` | int | `778` |  |
| `FEAT_EPIC_GREAT_CONSTITUTION_6` | int | `779` |  |
| `FEAT_EPIC_GREAT_CONSTITUTION_7` | int | `780` |  |
| `FEAT_EPIC_GREAT_CONSTITUTION_8` | int | `781` |  |
| `FEAT_EPIC_GREAT_CONSTITUTION_9` | int | `782` |  |
| `FEAT_EPIC_GREAT_CONSTITUTION_10` | int | `783` |  |
| `FEAT_EPIC_GREAT_DEXTERITY_1` | int | `784` |  |
| `FEAT_EPIC_GREAT_DEXTERITY_2` | int | `785` |  |
| `FEAT_EPIC_GREAT_DEXTERITY_3` | int | `786` |  |
| `FEAT_EPIC_GREAT_DEXTERITY_4` | int | `787` |  |
| `FEAT_EPIC_GREAT_DEXTERITY_5` | int | `788` |  |
| `FEAT_EPIC_GREAT_DEXTERITY_6` | int | `789` |  |
| `FEAT_EPIC_GREAT_DEXTERITY_7` | int | `790` |  |
| `FEAT_EPIC_GREAT_DEXTERITY_8` | int | `791` |  |
| `FEAT_EPIC_GREAT_DEXTERITY_9` | int | `792` |  |
| `FEAT_EPIC_GREAT_DEXTERITY_10` | int | `793` |  |
| `FEAT_EPIC_GREAT_INTELLIGENCE_1` | int | `794` |  |
| `FEAT_EPIC_GREAT_INTELLIGENCE_2` | int | `795` |  |
| `FEAT_EPIC_GREAT_INTELLIGENCE_3` | int | `796` |  |
| `FEAT_EPIC_GREAT_INTELLIGENCE_4` | int | `797` |  |
| `FEAT_EPIC_GREAT_INTELLIGENCE_5` | int | `798` |  |
| `FEAT_EPIC_GREAT_INTELLIGENCE_6` | int | `799` |  |
| `FEAT_EPIC_GREAT_INTELLIGENCE_7` | int | `800` |  |
| `FEAT_EPIC_GREAT_INTELLIGENCE_8` | int | `801` |  |
| `FEAT_EPIC_GREAT_INTELLIGENCE_9` | int | `802` |  |
| `FEAT_EPIC_GREAT_INTELLIGENCE_10` | int | `803` |  |
| `FEAT_EPIC_GREAT_WISDOM_1` | int | `804` |  |
| `FEAT_EPIC_GREAT_WISDOM_2` | int | `805` |  |
| `FEAT_EPIC_GREAT_WISDOM_3` | int | `806` |  |
| `FEAT_EPIC_GREAT_WISDOM_4` | int | `807` |  |
| `FEAT_EPIC_GREAT_WISDOM_5` | int | `808` |  |
| `FEAT_EPIC_GREAT_WISDOM_6` | int | `809` |  |
| `FEAT_EPIC_GREAT_WISDOM_7` | int | `810` |  |
| `FEAT_EPIC_GREAT_WISDOM_8` | int | `811` |  |
| `FEAT_EPIC_GREAT_WISDOM_9` | int | `812` |  |
| `FEAT_EPIC_GREAT_WISDOM_10` | int | `813` |  |
| `FEAT_EPIC_GREAT_STRENGTH_1` | int | `814` |  |
| `FEAT_EPIC_GREAT_STRENGTH_2` | int | `815` |  |
| `FEAT_EPIC_GREAT_STRENGTH_3` | int | `816` |  |
| `FEAT_EPIC_GREAT_STRENGTH_4` | int | `817` |  |
| `FEAT_EPIC_GREAT_STRENGTH_5` | int | `818` |  |
| `FEAT_EPIC_GREAT_STRENGTH_6` | int | `819` |  |
| `FEAT_EPIC_GREAT_STRENGTH_7` | int | `820` |  |
| `FEAT_EPIC_GREAT_STRENGTH_8` | int | `821` |  |
| `FEAT_EPIC_GREAT_STRENGTH_9` | int | `822` |  |
| `FEAT_EPIC_GREAT_STRENGTH_10` | int | `823` |  |
| `FEAT_EPIC_GREAT_SMITING_1` | int | `824` |  |
| `FEAT_EPIC_GREAT_SMITING_2` | int | `825` |  |
| `FEAT_EPIC_GREAT_SMITING_3` | int | `826` |  |
| `FEAT_EPIC_GREAT_SMITING_4` | int | `827` |  |
| `FEAT_EPIC_GREAT_SMITING_5` | int | `828` |  |
| `FEAT_EPIC_GREAT_SMITING_6` | int | `829` |  |
| `FEAT_EPIC_GREAT_SMITING_7` | int | `830` |  |
| `FEAT_EPIC_GREAT_SMITING_8` | int | `831` |  |
| `FEAT_EPIC_GREAT_SMITING_9` | int | `832` |  |
| `FEAT_EPIC_GREAT_SMITING_10` | int | `833` |  |
| `FEAT_EPIC_IMPROVED_SNEAK_ATTACK_1` | int | `834` |  |
| `FEAT_EPIC_IMPROVED_SNEAK_ATTACK_2` | int | `835` |  |
| `FEAT_EPIC_IMPROVED_SNEAK_ATTACK_3` | int | `836` |  |
| `FEAT_EPIC_IMPROVED_SNEAK_ATTACK_4` | int | `837` |  |
| `FEAT_EPIC_IMPROVED_SNEAK_ATTACK_5` | int | `838` |  |
| `FEAT_EPIC_IMPROVED_SNEAK_ATTACK_6` | int | `839` |  |
| `FEAT_EPIC_IMPROVED_SNEAK_ATTACK_7` | int | `840` |  |
| `FEAT_EPIC_IMPROVED_SNEAK_ATTACK_8` | int | `841` |  |
| `FEAT_EPIC_IMPROVED_SNEAK_ATTACK_9` | int | `842` |  |
| `FEAT_EPIC_IMPROVED_SNEAK_ATTACK_10` | int | `843` |  |
| `FEAT_EPIC_IMPROVED_STUNNING_FIST_1` | int | `844` |  |
| `FEAT_EPIC_IMPROVED_STUNNING_FIST_2` | int | `845` |  |
| `FEAT_EPIC_IMPROVED_STUNNING_FIST_3` | int | `846` |  |
| `FEAT_EPIC_IMPROVED_STUNNING_FIST_4` | int | `847` |  |
| `FEAT_EPIC_IMPROVED_STUNNING_FIST_5` | int | `848` |  |
| `FEAT_EPIC_IMPROVED_STUNNING_FIST_6` | int | `849` |  |
| `FEAT_EPIC_IMPROVED_STUNNING_FIST_7` | int | `850` |  |
| `FEAT_EPIC_IMPROVED_STUNNING_FIST_8` | int | `851` |  |
| `FEAT_EPIC_IMPROVED_STUNNING_FIST_9` | int | `852` |  |
| `FEAT_EPIC_IMPROVED_STUNNING_FIST_10` | int | `853` |  |
| `FEAT_EPIC_BANE_OF_ENEMIES` | int | `855` |  |
| `FEAT_EPIC_DODGE` | int | `856` |  |
| `FEAT_EPIC_AUTOMATIC_QUICKEN_1` | int | `857` |  |
| `FEAT_EPIC_AUTOMATIC_QUICKEN_2` | int | `858` |  |
| `FEAT_EPIC_AUTOMATIC_QUICKEN_3` | int | `859` |  |
| `FEAT_EPIC_AUTOMATIC_SILENT_SPELL_1` | int | `860` |  |
| `FEAT_EPIC_AUTOMATIC_SILENT_SPELL_2` | int | `861` |  |
| `FEAT_EPIC_AUTOMATIC_SILENT_SPELL_3` | int | `862` |  |
| `FEAT_EPIC_AUTOMATIC_STILL_SPELL_1` | int | `863` |  |
| `FEAT_EPIC_AUTOMATIC_STILL_SPELL_2` | int | `864` |  |
| `FEAT_EPIC_AUTOMATIC_STILL_SPELL_3` | int | `865` |  |
| `FEAT_SHOU_DISCIPLE_MARTIAL_FLURRY_LIGHT` | int | `866` |  |
| `FEAT_WHIRLWIND_ATTACK` | int | `867` |  |
| `FEAT_IMPROVED_WHIRLWIND` | int | `868` |  |
| `FEAT_MIGHTY_RAGE` | int | `869` |  |
| `FEAT_EPIC_LASTING_INSPIRATION` | int | `870` |  |
| `FEAT_CURSE_SONG` | int | `871` |  |
| `FEAT_EPIC_WILD_SHAPE_UNDEAD` | int | `872` |  |
| `FEAT_EPIC_WILD_SHAPE_DRAGON` | int | `873` |  |
| `FEAT_EPIC_SPELL_MUMMY_DUST` | int | `874` |  |
| `FEAT_EPIC_SPELL_DRAGON_KNIGHT` | int | `875` |  |
| `FEAT_EPIC_SPELL_HELLBALL` | int | `876` |  |
| `FEAT_EPIC_SPELL_MAGE_ARMOUR` | int | `877` |  |
| `FEAT_EPIC_SPELL_RUIN` | int | `878` |  |
| `FEAT_WEAPON_OF_CHOICE_SICKLE` | int | `879` |  |
| `FEAT_WEAPON_OF_CHOICE_KAMA` | int | `880` |  |
| `FEAT_WEAPON_OF_CHOICE_KUKRI` | int | `881` |  |
| `FEAT_KI_DAMAGE` | int | `882` |  |
| `FEAT_INCREASE_MULTIPLIER` | int | `883` |  |
| `FEAT_SUPERIOR_WEAPON_FOCUS` | int | `884` |  |
| `FEAT_KI_CRITICAL` | int | `885` |  |
| `FEAT_BONE_SKIN_2` | int | `886` |  |
| `FEAT_BONE_SKIN_4` | int | `887` |  |
| `FEAT_BONE_SKIN_6` | int | `888` |  |
| `FEAT_ANIMATE_DEAD` | int | `889` |  |
| `FEAT_SUMMON_UNDEAD` | int | `890` |  |
| `FEAT_DEATHLESS_VIGOR` | int | `891` |  |
| `FEAT_UNDEAD_GRAFT_1` | int | `892` |  |
| `FEAT_UNDEAD_GRAFT_2` | int | `893` |  |
| `FEAT_TOUGH_AS_BONE` | int | `894` |  |
| `FEAT_SUMMON_GREATER_UNDEAD` | int | `895` |  |
| `FEAT_DEATHLESS_MASTERY` | int | `896` |  |
| `FEAT_DEATHLESS_MASTER_TOUCH` | int | `897` |  |
| `FEAT_GREATER_WILDSHAPE_1` | int | `898` |  |
| `FEAT_SHOU_DISCIPLE_MARTIAL_FLURRY_ANY` | int | `899` |  |
| `FEAT_GREATER_WILDSHAPE_2` | int | `900` |  |
| `FEAT_GREATER_WILDSHAPE_3` | int | `901` |  |
| `FEAT_HUMANOID_SHAPE` | int | `902` |  |
| `FEAT_GREATER_WILDSHAPE_4` | int | `903` |  |
| `FEAT_SACRED_DEFENSE_1` | int | `904` |  |
| `FEAT_SACRED_DEFENSE_2` | int | `905` |  |
| `FEAT_SACRED_DEFENSE_3` | int | `906` |  |
| `FEAT_SACRED_DEFENSE_4` | int | `907` |  |
| `FEAT_SACRED_DEFENSE_5` | int | `908` |  |
| `FEAT_DIVINE_WRATH` | int | `909` |  |
| `FEAT_EXTRA_SMITING` | int | `910` |  |
| `FEAT_SKILL_FOCUS_CRAFT_ARMOR` | int | `911` |  |
| `FEAT_SKILL_FOCUS_CRAFT_WEAPON` | int | `912` |  |
| `FEAT_EPIC_SKILL_FOCUS_CRAFT_ARMOR` | int | `913` |  |
| `FEAT_EPIC_SKILL_FOCUS_CRAFT_WEAPON` | int | `914` |  |
| `FEAT_SKILL_FOCUS_BLUFF` | int | `915` |  |
| `FEAT_SKILL_FOCUS_INTIMIDATE` | int | `916` |  |
| `FEAT_EPIC_SKILL_FOCUS_BLUFF` | int | `917` |  |
| `FEAT_EPIC_SKILL_FOCUS_INTIMIDATE` | int | `918` |  |
| `FEAT_WEAPON_OF_CHOICE_CLUB` | int | `919` |  |
| `FEAT_WEAPON_OF_CHOICE_DAGGER` | int | `920` |  |
| `FEAT_WEAPON_OF_CHOICE_LIGHTMACE` | int | `921` |  |
| `FEAT_WEAPON_OF_CHOICE_MORNINGSTAR` | int | `922` |  |
| `FEAT_WEAPON_OF_CHOICE_QUARTERSTAFF` | int | `923` |  |
| `FEAT_WEAPON_OF_CHOICE_SHORTSPEAR` | int | `924` |  |
| `FEAT_WEAPON_OF_CHOICE_SHORTSWORD` | int | `925` |  |
| `FEAT_WEAPON_OF_CHOICE_RAPIER` | int | `926` |  |
| `FEAT_WEAPON_OF_CHOICE_SCIMITAR` | int | `927` |  |
| `FEAT_WEAPON_OF_CHOICE_LONGSWORD` | int | `928` |  |
| `FEAT_WEAPON_OF_CHOICE_GREATSWORD` | int | `929` |  |
| `FEAT_WEAPON_OF_CHOICE_HANDAXE` | int | `930` |  |
| `FEAT_WEAPON_OF_CHOICE_BATTLEAXE` | int | `931` |  |
| `FEAT_WEAPON_OF_CHOICE_GREATAXE` | int | `932` |  |
| `FEAT_WEAPON_OF_CHOICE_HALBERD` | int | `933` |  |
| `FEAT_WEAPON_OF_CHOICE_LIGHTHAMMER` | int | `934` |  |
| `FEAT_WEAPON_OF_CHOICE_LIGHTFLAIL` | int | `935` |  |
| `FEAT_WEAPON_OF_CHOICE_WARHAMMER` | int | `936` |  |
| `FEAT_WEAPON_OF_CHOICE_HEAVYFLAIL` | int | `937` |  |
| `FEAT_WEAPON_OF_CHOICE_SCYTHE` | int | `938` |  |
| `FEAT_WEAPON_OF_CHOICE_KATANA` | int | `939` |  |
| `FEAT_WEAPON_OF_CHOICE_BASTARDSWORD` | int | `940` |  |
| `FEAT_WEAPON_OF_CHOICE_DIREMACE` | int | `941` |  |
| `FEAT_WEAPON_OF_CHOICE_DOUBLEAXE` | int | `942` |  |
| `FEAT_WEAPON_OF_CHOICE_TWOBLADEDSWORD` | int | `943` |  |
| `FEAT_BREW_POTION` | int | `944` |  |
| `FEAT_SCRIBE_SCROLL` | int | `945` |  |
| `FEAT_CRAFT_WAND` | int | `946` |  |
| `FEAT_DWARVEN_DEFENDER_DEFENSIVE_STANCE` | int | `947` |  |
| `FEAT_DAMAGE_REDUCTION_6` | int | `948` |  |
| `FEAT_PRESTIGE_DEFENSIVE_AWARENESS_1` | int | `949` |  |
| `FEAT_PRESTIGE_DEFENSIVE_AWARENESS_2` | int | `950` |  |
| `FEAT_PRESTIGE_DEFENSIVE_AWARENESS_3` | int | `951` |  |
| `FEAT_WEAPON_FOCUS_DWAXE` | int | `952` |  |
| `FEAT_WEAPON_SPECIALIZATION_DWAXE` | int | `953` |  |
| `FEAT_IMPROVED_CRITICAL_DWAXE` | int | `954` |  |
| `FEAT_EPIC_DEVASTATING_CRITICAL_DWAXE` | int | `955` |  |
| `FEAT_EPIC_WEAPON_FOCUS_DWAXE` | int | `956` |  |
| `FEAT_EPIC_WEAPON_SPECIALIZATION_DWAXE` | int | `957` |  |
| `FEAT_EPIC_OVERWHELMING_CRITICAL_DWAXE` | int | `958` |  |
| `FEAT_WEAPON_OF_CHOICE_DWAXE` | int | `959` |  |
| `FEAT_USE_POISON` | int | `960` |  |
| `FEAT_DRAGON_ARMOR` | int | `961` |  |
| `FEAT_DRAGON_ABILITIES` | int | `962` |  |
| `FEAT_DRAGON_IMMUNE_PARALYSIS` | int | `963` |  |
| `FEAT_DRAGON_IMMUNE_FIRE` | int | `964` |  |
| `FEAT_DRAGON_DIS_BREATH` | int | `965` |  |
| `FEAT_EPIC_FIGHTER` | int | `966` |  |
| `FEAT_EPIC_BARBARIAN` | int | `967` |  |
| `FEAT_EPIC_BARD` | int | `968` |  |
| `FEAT_EPIC_CLERIC` | int | `969` |  |
| `FEAT_EPIC_DRUID` | int | `970` |  |
| `FEAT_EPIC_MONK` | int | `971` |  |
| `FEAT_EPIC_PALADIN` | int | `972` |  |
| `FEAT_EPIC_RANGER` | int | `973` |  |
| `FEAT_EPIC_ROGUE` | int | `974` |  |
| `FEAT_EPIC_SORCERER` | int | `975` |  |
| `FEAT_EPIC_WIZARD` | int | `976` |  |
| `FEAT_EPIC_ARCANE_ARCHER` | int | `977` |  |
| `FEAT_EPIC_ASSASSIN` | int | `978` |  |
| `FEAT_EPIC_BLACKGUARD` | int | `979` |  |
| `FEAT_EPIC_SHADOWDANCER` | int | `980` |  |
| `FEAT_EPIC_HARPER_SCOUT` | int | `981` |  |
| `FEAT_EPIC_DIVINE_CHAMPION` | int | `982` |  |
| `FEAT_EPIC_WEAPON_MASTER` | int | `983` |  |
| `FEAT_EPIC_PALE_MASTER` | int | `984` |  |
| `FEAT_EPIC_DWARVEN_DEFENDER` | int | `985` |  |
| `FEAT_EPIC_SHIFTER` | int | `986` |  |
| `FEAT_EPIC_RED_DRAGON_DISC` | int | `987` |  |
| `FEAT_EPIC_THUNDERING_RAGE` | int | `988` |  |
| `FEAT_EPIC_TERRIFYING_RAGE` | int | `989` |  |
| `FEAT_EPIC_SPELL_EPIC_WARDING` | int | `990` |  |
| `FEAT_WEAPON_FOCUS_WHIP` | int | `993` |  |
| `FEAT_WEAPON_SPECIALIZATION_WHIP` | int | `994` |  |
| `FEAT_IMPROVED_CRITICAL_WHIP` | int | `995` |  |
| `FEAT_EPIC_DEVASTATING_CRITICAL_WHIP` | int | `996` |  |
| `FEAT_EPIC_WEAPON_FOCUS_WHIP` | int | `997` |  |
| `FEAT_EPIC_WEAPON_SPECIALIZATION_WHIP` | int | `998` |  |
| `FEAT_EPIC_OVERWHELMING_CRITICAL_WHIP` | int | `999` |  |
| `FEAT_WEAPON_OF_CHOICE_WHIP` | int | `1000` |  |
| `FEAT_EPIC_CHARACTER` | int | `1001` |  |
| `FEAT_EPIC_EPIC_SHADOWLORD` | int | `1002` |  |
| `FEAT_EPIC_EPIC_FIEND` | int | `1003` |  |
| `FEAT_PRESTIGE_DEATH_ATTACK_6` | int | `1004` |  |
| `FEAT_PRESTIGE_DEATH_ATTACK_7` | int | `1005` |  |
| `FEAT_PRESTIGE_DEATH_ATTACK_8` | int | `1006` |  |
| `FEAT_BLACKGUARD_SNEAK_ATTACK_4D6` | int | `1007` |  |
| `FEAT_BLACKGUARD_SNEAK_ATTACK_5D6` | int | `1008` |  |
| `FEAT_BLACKGUARD_SNEAK_ATTACK_6D6` | int | `1009` |  |
| `FEAT_BLACKGUARD_SNEAK_ATTACK_7D6` | int | `1010` |  |
| `FEAT_BLACKGUARD_SNEAK_ATTACK_8D6` | int | `1011` |  |
| `FEAT_BLACKGUARD_SNEAK_ATTACK_9D6` | int | `1012` |  |
| `FEAT_BLACKGUARD_SNEAK_ATTACK_10D6` | int | `1013` |  |
| `FEAT_BLACKGUARD_SNEAK_ATTACK_11D6` | int | `1014` |  |
| `FEAT_BLACKGUARD_SNEAK_ATTACK_12D6` | int | `1015` |  |
| `FEAT_BLACKGUARD_SNEAK_ATTACK_13D6` | int | `1016` |  |
| `FEAT_BLACKGUARD_SNEAK_ATTACK_14D6` | int | `1017` |  |
| `FEAT_BLACKGUARD_SNEAK_ATTACK_15D6` | int | `1018` |  |
| `FEAT_PRESTIGE_DEATH_ATTACK_9` | int | `1019` |  |
| `FEAT_PRESTIGE_DEATH_ATTACK_10` | int | `1020` |  |
| `FEAT_PRESTIGE_DEATH_ATTACK_11` | int | `1021` |  |
| `FEAT_PRESTIGE_DEATH_ATTACK_12` | int | `1022` |  |
| `FEAT_PRESTIGE_DEATH_ATTACK_13` | int | `1023` |  |
| `FEAT_PRESTIGE_DEATH_ATTACK_14` | int | `1024` |  |
| `FEAT_PRESTIGE_DEATH_ATTACK_15` | int | `1025` |  |
| `FEAT_PRESTIGE_DEATH_ATTACK_16` | int | `1026` |  |
| `FEAT_PRESTIGE_DEATH_ATTACK_17` | int | `1027` |  |
| `FEAT_PRESTIGE_DEATH_ATTACK_18` | int | `1028` |  |
| `FEAT_PRESTIGE_DEATH_ATTACK_19` | int | `1029` |  |
| `FEAT_PRESTIGE_DEATH_ATTACK_20` | int | `1030` |  |
| `FEAT_SHOU_DISCIPLE_DODGE_3` | int | `1031` |  |
| `FEAT_DRAGON_HDINCREASE_D6` | int | `1042` |  |
| `FEAT_DRAGON_HDINCREASE_D8` | int | `1043` |  |
| `FEAT_DRAGON_HDINCREASE_D10` | int | `1044` |  |
| `FEAT_PRESTIGE_ENCHANT_ARROW_6` | int | `1045` |  |
| `FEAT_PRESTIGE_ENCHANT_ARROW_7` | int | `1046` |  |
| `FEAT_PRESTIGE_ENCHANT_ARROW_8` | int | `1047` |  |
| `FEAT_PRESTIGE_ENCHANT_ARROW_9` | int | `1048` |  |
| `FEAT_PRESTIGE_ENCHANT_ARROW_10` | int | `1049` |  |
| `FEAT_PRESTIGE_ENCHANT_ARROW_11` | int | `1050` |  |
| `FEAT_PRESTIGE_ENCHANT_ARROW_12` | int | `1051` |  |
| `FEAT_PRESTIGE_ENCHANT_ARROW_13` | int | `1052` |  |
| `FEAT_PRESTIGE_ENCHANT_ARROW_14` | int | `1053` |  |
| `FEAT_PRESTIGE_ENCHANT_ARROW_15` | int | `1054` |  |
| `FEAT_PRESTIGE_ENCHANT_ARROW_16` | int | `1055` |  |
| `FEAT_PRESTIGE_ENCHANT_ARROW_17` | int | `1056` |  |
| `FEAT_PRESTIGE_ENCHANT_ARROW_18` | int | `1057` |  |
| `FEAT_PRESTIGE_ENCHANT_ARROW_19` | int | `1058` |  |
| `FEAT_PRESTIGE_ENCHANT_ARROW_20` | int | `1059` |  |
| `FEAT_EPIC_OUTSIDER_SHAPE` | int | `1060` |  |
| `FEAT_EPIC_CONSTRUCT_SHAPE` | int | `1061` |  |
| `FEAT_EPIC_SHIFTER_INFINITE_WILDSHAPE_1` | int | `1062` |  |
| `FEAT_EPIC_SHIFTER_INFINITE_WILDSHAPE_2` | int | `1063` |  |
| `FEAT_EPIC_SHIFTER_INFINITE_WILDSHAPE_3` | int | `1064` |  |
| `FEAT_EPIC_SHIFTER_INFINITE_WILDSHAPE_4` | int | `1065` |  |
| `FEAT_EPIC_SHIFTER_INFINITE_HUMANOID_SHAPE` | int | `1066` |  |
| `FEAT_EPIC_BARBARIAN_DAMAGE_REDUCTION` | int | `1067` |  |
| `FEAT_EPIC_DRUID_INFINITE_WILDSHAPE` | int | `1068` |  |
| `FEAT_EPIC_DRUID_INFINITE_ELEMENTAL_SHAPE` | int | `1069` |  |
| `FEAT_PRESTIGE_POISON_SAVE_EPIC` | int | `1070` |  |
| `FEAT_EPIC_SUPERIOR_WEAPON_FOCUS` | int | `1071` |  |
| `FEAT_WEAPON_FOCUS_TRIDENT` | int | `1072` |  |
| `FEAT_WEAPON_SPECIALIZATION_TRIDENT` | int | `1073` |  |
| `FEAT_IMPROVED_CRITICAL_TRIDENT` | int | `1074` |  |
| `FEAT_EPIC_DEVASTATING_CRITICAL_TRIDENT` | int | `1075` |  |
| `FEAT_EPIC_WEAPON_FOCUS_TRIDENT` | int | `1076` |  |
| `FEAT_EPIC_WEAPON_SPECIALIZATION_TRIDENT` | int | `1077` |  |
| `FEAT_EPIC_OVERWHELMING_CRITICAL_TRIDENT` | int | `1078` |  |
| `FEAT_WEAPON_OF_CHOICE_TRIDENT` | int | `1079` |  |
| `FEAT_PDK_RALLY` | int | `1080` |  |
| `FEAT_PDK_SHIELD` | int | `1081` |  |
| `FEAT_PDK_FEAR` | int | `1082` |  |
| `FEAT_PDK_WRATH` | int | `1083` |  |
| `FEAT_PDK_STAND` | int | `1084` |  |
| `FEAT_PDK_INSPIRE_1` | int | `1085` |  |
| `FEAT_PDK_INSPIRE_2` | int | `1086` |  |
| `FEAT_MOUNTED_COMBAT` | int | `1087` |  |
| `FEAT_MOUNTED_ARCHERY` | int | `1088` |  |
| `FEAT_HORSE_MENU` | int | `1089` |  |
| `FEAT_HORSE_MOUNT` | int | `1090` |  |
| `FEAT_HORSE_DISMOUNT` | int | `1091` |  |
| `FEAT_HORSE_PARTY_MOUNT` | int | `1092` |  |
| `FEAT_HORSE_PARTY_DISMOUNT` | int | `1093` |  |
| `FEAT_HORSE_ASSIGN_MOUNT` | int | `1094` |  |
| `FEAT_PALADIN_SUMMON_MOUNT` | int | `1095` |  |
| `FEAT_PLAYER_TOOL_01` | int | `1106` |  |
| `FEAT_PLAYER_TOOL_02` | int | `1107` |  |
| `FEAT_PLAYER_TOOL_03` | int | `1108` |  |
| `FEAT_PLAYER_TOOL_04` | int | `1109` |  |
| `FEAT_PLAYER_TOOL_05` | int | `1110` |  |
| `FEAT_PLAYER_TOOL_06` | int | `1111` |  |
| `FEAT_PLAYER_TOOL_07` | int | `1112` |  |
| `FEAT_PLAYER_TOOL_08` | int | `1113` |  |
| `FEAT_PLAYER_TOOL_09` | int | `1114` |  |
| `FEAT_PLAYER_TOOL_10` | int | `1115` |  |
| `SUBFEAT_CALLED_SHOT_LEG` | int | `65000` |  |
| `SUBFEAT_CALLED_SHOT_ARMS` | int | `65001` |  |
| `SUBFEAT_ELEMENTAL_SHAPE_EARTH` | int | `1004` |  |
| `SUBFEAT_ELEMENTAL_SHAPE_WATER` | int | `1005` |  |
| `SUBFEAT_ELEMENTAL_SHAPE_FIRE` | int | `1006` |  |
| `SUBFEAT_ELEMENTAL_SHAPE_AIR` | int | `1007` |  |
| `SUBFEAT_WILD_SHAPE_BROWN_BEAR` | int | `1008` |  |
| `SUBFEAT_WILD_SHAPE_PANTHER` | int | `1009` |  |
| `SUBFEAT_WILD_SHAPE_WOLF` | int | `1010` |  |
| `SUBFEAT_WILD_SHAPE_BOAR` | int | `1011` |  |
| `SUBFEAT_WILD_SHAPE_BADGER` | int | `1012` |  |
| `SPECIAL_ATTACK_INVALID` | int | `0` |  |
| `SPECIAL_ATTACK_CALLED_SHOT_LEG` | int | `1` |  |
| `SPECIAL_ATTACK_CALLED_SHOT_ARM` | int | `2` |  |
| `SPECIAL_ATTACK_SAP` | int | `3` |  |
| `SPECIAL_ATTACK_DISARM` | int | `4` |  |
| `SPECIAL_ATTACK_IMPROVED_DISARM` | int | `5` |  |
| `SPECIAL_ATTACK_KNOCKDOWN` | int | `6` |  |
| `SPECIAL_ATTACK_IMPROVED_KNOCKDOWN` | int | `7` |  |
| `SPECIAL_ATTACK_STUNNING_FIST` | int | `8` |  |
| `SPECIAL_ATTACK_FLURRY_OF_BLOWS` | int | `9` |  |
| `SPECIAL_ATTACK_RAPID_SHOT` | int | `10` |  |
| `COMBAT_MODE_INVALID` | int | `0` |  |
| `COMBAT_MODE_PARRY` | int | `1` |  |
| `COMBAT_MODE_POWER_ATTACK` | int | `2` |  |
| `COMBAT_MODE_IMPROVED_POWER_ATTACK` | int | `3` |  |
| `COMBAT_MODE_FLURRY_OF_BLOWS` | int | `4` |  |
| `COMBAT_MODE_RAPID_SHOT` | int | `5` |  |
| `COMBAT_MODE_EXPERTISE` | int | `6` |  |
| `COMBAT_MODE_IMPROVED_EXPERTISE` | int | `7` |  |
| `COMBAT_MODE_DEFENSIVE_CASTING` | int | `8` |  |
| `COMBAT_MODE_DIRTY_FIGHTING` | int | `9` |  |
| `COMBAT_MODE_DEFENSIVE_STANCE` | int | `10` |  |
| `ENCOUNTER_DIFFICULTY_VERY_EASY` | int | `0` |  |
| `ENCOUNTER_DIFFICULTY_EASY` | int | `1` |  |
| `ENCOUNTER_DIFFICULTY_NORMAL` | int | `2` |  |
| `ENCOUNTER_DIFFICULTY_HARD` | int | `3` |  |
| `ENCOUNTER_DIFFICULTY_IMPOSSIBLE` | int | `4` |  |
| `ANIMATION_LOOPING_PAUSE` | int | `0` |  |
| `ANIMATION_LOOPING_PAUSE2` | int | `1` |  |
| `ANIMATION_LOOPING_LISTEN` | int | `2` |  |
| `ANIMATION_LOOPING_MEDITATE` | int | `3` |  |
| `ANIMATION_LOOPING_WORSHIP` | int | `4` |  |
| `ANIMATION_LOOPING_LOOK_FAR` | int | `5` |  |
| `ANIMATION_LOOPING_SIT_CHAIR` | int | `6` |  |
| `ANIMATION_LOOPING_SIT_CROSS` | int | `7` |  |
| `ANIMATION_LOOPING_TALK_NORMAL` | int | `8` |  |
| `ANIMATION_LOOPING_TALK_PLEADING` | int | `9` |  |
| `ANIMATION_LOOPING_TALK_FORCEFUL` | int | `10` |  |
| `ANIMATION_LOOPING_TALK_LAUGHING` | int | `11` |  |
| `ANIMATION_LOOPING_GET_LOW` | int | `12` |  |
| `ANIMATION_LOOPING_GET_MID` | int | `13` |  |
| `ANIMATION_LOOPING_PAUSE_TIRED` | int | `14` |  |
| `ANIMATION_LOOPING_PAUSE_DRUNK` | int | `15` |  |
| `ANIMATION_LOOPING_DEAD_FRONT` | int | `16` |  |
| `ANIMATION_LOOPING_DEAD_BACK` | int | `17` |  |
| `ANIMATION_LOOPING_CONJURE1` | int | `18` |  |
| `ANIMATION_LOOPING_CONJURE2` | int | `19` |  |
| `ANIMATION_LOOPING_SPASM` | int | `20` |  |
| `ANIMATION_LOOPING_CUSTOM1` | int | `21` |  |
| `ANIMATION_LOOPING_CUSTOM2` | int | `22` |  |
| `ANIMATION_LOOPING_CUSTOM3` | int | `23` |  |
| `ANIMATION_LOOPING_CUSTOM4` | int | `24` |  |
| `ANIMATION_LOOPING_CUSTOM5` | int | `25` |  |
| `ANIMATION_LOOPING_CUSTOM6` | int | `26` |  |
| `ANIMATION_LOOPING_CUSTOM7` | int | `27` |  |
| `ANIMATION_LOOPING_CUSTOM8` | int | `28` |  |
| `ANIMATION_LOOPING_CUSTOM9` | int | `29` |  |
| `ANIMATION_LOOPING_CUSTOM10` | int | `30` |  |
| `ANIMATION_LOOPING_CUSTOM11` | int | `31` |  |
| `ANIMATION_LOOPING_CUSTOM12` | int | `32` |  |
| `ANIMATION_LOOPING_CUSTOM13` | int | `33` |  |
| `ANIMATION_LOOPING_CUSTOM14` | int | `34` |  |
| `ANIMATION_LOOPING_CUSTOM15` | int | `35` |  |
| `ANIMATION_LOOPING_CUSTOM16` | int | `36` |  |
| `ANIMATION_LOOPING_CUSTOM17` | int | `37` |  |
| `ANIMATION_LOOPING_CUSTOM18` | int | `38` |  |
| `ANIMATION_LOOPING_CUSTOM19` | int | `39` |  |
| `ANIMATION_LOOPING_CUSTOM20` | int | `40` |  |
| `ANIMATION_MOUNT1` | int | `41` |  |
| `ANIMATION_DISMOUNT1` | int | `42` |  |
| `ANIMATION_LOOPING_CUSTOM21` | int | `43` |  |
| `ANIMATION_LOOPING_CUSTOM22` | int | `44` |  |
| `ANIMATION_LOOPING_CUSTOM23` | int | `45` |  |
| `ANIMATION_LOOPING_CUSTOM24` | int | `46` |  |
| `ANIMATION_LOOPING_CUSTOM25` | int | `47` |  |
| `ANIMATION_LOOPING_CUSTOM26` | int | `48` |  |
| `ANIMATION_LOOPING_CUSTOM27` | int | `49` |  |
| `ANIMATION_LOOPING_CUSTOM28` | int | `50` |  |
| `ANIMATION_LOOPING_CUSTOM29` | int | `51` |  |
| `ANIMATION_LOOPING_CUSTOM30` | int | `52` |  |
| `ANIMATION_LOOPING_CUSTOM31` | int | `53` |  |
| `ANIMATION_LOOPING_CUSTOM32` | int | `54` |  |
| `ANIMATION_LOOPING_CUSTOM33` | int | `55` |  |
| `ANIMATION_LOOPING_CUSTOM34` | int | `56` |  |
| `ANIMATION_LOOPING_CUSTOM35` | int | `57` |  |
| `ANIMATION_LOOPING_CUSTOM36` | int | `58` |  |
| `ANIMATION_LOOPING_CUSTOM37` | int | `59` |  |
| `ANIMATION_LOOPING_CUSTOM38` | int | `60` |  |
| `ANIMATION_LOOPING_CUSTOM39` | int | `61` |  |
| `ANIMATION_LOOPING_CUSTOM40` | int | `62` |  |
| `ANIMATION_LOOPING_CUSTOM41` | int | `63` |  |
| `ANIMATION_LOOPING_CUSTOM42` | int | `64` |  |
| `ANIMATION_LOOPING_CUSTOM43` | int | `65` |  |
| `ANIMATION_LOOPING_CUSTOM44` | int | `66` |  |
| `ANIMATION_LOOPING_CUSTOM45` | int | `67` |  |
| `ANIMATION_LOOPING_CUSTOM46` | int | `68` |  |
| `ANIMATION_LOOPING_CUSTOM47` | int | `69` |  |
| `ANIMATION_LOOPING_CUSTOM48` | int | `70` |  |
| `ANIMATION_LOOPING_CUSTOM49` | int | `71` |  |
| `ANIMATION_LOOPING_CUSTOM50` | int | `72` |  |
| `ANIMATION_LOOPING_CUSTOM51` | int | `73` |  |
| `ANIMATION_LOOPING_CUSTOM52` | int | `74` |  |
| `ANIMATION_LOOPING_CUSTOM53` | int | `75` |  |
| `ANIMATION_LOOPING_CUSTOM54` | int | `76` |  |
| `ANIMATION_LOOPING_CUSTOM55` | int | `77` |  |
| `ANIMATION_LOOPING_CUSTOM56` | int | `78` |  |
| `ANIMATION_LOOPING_CUSTOM57` | int | `79` |  |
| `ANIMATION_LOOPING_CUSTOM58` | int | `80` |  |
| `ANIMATION_LOOPING_CUSTOM59` | int | `81` |  |
| `ANIMATION_LOOPING_CUSTOM60` | int | `82` |  |
| `ANIMATION_LOOPING_CUSTOM61` | int | `83` |  |
| `ANIMATION_LOOPING_CUSTOM62` | int | `84` |  |
| `ANIMATION_LOOPING_CUSTOM63` | int | `85` |  |
| `ANIMATION_LOOPING_CUSTOM64` | int | `86` |  |
| `ANIMATION_LOOPING_CUSTOM65` | int | `87` |  |
| `ANIMATION_LOOPING_CUSTOM66` | int | `88` |  |
| `ANIMATION_LOOPING_CUSTOM67` | int | `89` |  |
| `ANIMATION_LOOPING_CUSTOM68` | int | `90` |  |
| `ANIMATION_LOOPING_CUSTOM69` | int | `91` |  |
| `ANIMATION_LOOPING_CUSTOM70` | int | `92` |  |
| `ANIMATION_FIREFORGET_HEAD_TURN_LEFT` | int | `100` |  |
| `ANIMATION_FIREFORGET_HEAD_TURN_RIGHT` | int | `101` |  |
| `ANIMATION_FIREFORGET_PAUSE_SCRATCH_HEAD` | int | `102` |  |
| `ANIMATION_FIREFORGET_PAUSE_BORED` | int | `103` |  |
| `ANIMATION_FIREFORGET_SALUTE` | int | `104` |  |
| `ANIMATION_FIREFORGET_BOW` | int | `105` |  |
| `ANIMATION_FIREFORGET_STEAL` | int | `106` |  |
| `ANIMATION_FIREFORGET_GREETING` | int | `107` |  |
| `ANIMATION_FIREFORGET_TAUNT` | int | `108` |  |
| `ANIMATION_FIREFORGET_VICTORY1` | int | `109` |  |
| `ANIMATION_FIREFORGET_VICTORY2` | int | `110` |  |
| `ANIMATION_FIREFORGET_VICTORY3` | int | `111` |  |
| `ANIMATION_FIREFORGET_READ` | int | `112` |  |
| `ANIMATION_FIREFORGET_DRINK` | int | `113` |  |
| `ANIMATION_FIREFORGET_DODGE_SIDE` | int | `114` |  |
| `ANIMATION_FIREFORGET_DODGE_DUCK` | int | `115` |  |
| `ANIMATION_FIREFORGET_SPASM` | int | `116` |  |
| `ANIMATION_PLACEABLE_ACTIVATE` | int | `200` |  |
| `ANIMATION_PLACEABLE_DEACTIVATE` | int | `201` |  |
| `ANIMATION_PLACEABLE_OPEN` | int | `202` |  |
| `ANIMATION_PLACEABLE_CLOSE` | int | `203` |  |
| `ANIMATION_DOOR_CLOSE` | int | `204` |  |
| `ANIMATION_DOOR_OPEN1` | int | `205` |  |
| `ANIMATION_DOOR_OPEN2` | int | `206` |  |
| `ANIMATION_DOOR_DESTROY` | int | `207` |  |
| `TALENT_TYPE_SPELL` | int | `0` |  |
| `TALENT_TYPE_FEAT` | int | `1` |  |
| `TALENT_TYPE_SKILL` | int | `2` |  |
| `ASSOCIATE_COMMAND_STANDGROUND` | int | `-2` |  |
| `ASSOCIATE_COMMAND_ATTACKNEAREST` | int | `-3` |  |
| `ASSOCIATE_COMMAND_HEALMASTER` | int | `-4` |  |
| `ASSOCIATE_COMMAND_FOLLOWMASTER` | int | `-5` |  |
| `ASSOCIATE_COMMAND_MASTERFAILEDLOCKPICK` | int | `-6` |  |
| `ASSOCIATE_COMMAND_GUARDMASTER` | int | `-7` |  |
| `ASSOCIATE_COMMAND_UNSUMMONFAMILIAR` | int | `-8` |  |
| `ASSOCIATE_COMMAND_UNSUMMONANIMALCOMPANION` | int | `-9` |  |
| `ASSOCIATE_COMMAND_UNSUMMONSUMMONED` | int | `-10` |  |
| `ASSOCIATE_COMMAND_MASTERUNDERATTACK` | int | `-11` |  |
| `ASSOCIATE_COMMAND_RELEASEDOMINATION` | int | `-12` |  |
| `ASSOCIATE_COMMAND_UNPOSSESSFAMILIAR` | int | `-13` |  |
| `ASSOCIATE_COMMAND_MASTERSAWTRAP` | int | `-14` |  |
| `ASSOCIATE_COMMAND_MASTERATTACKEDOTHER` | int | `-15` |  |
| `ASSOCIATE_COMMAND_MASTERGOINGTOBEATTACKED` | int | `-16` |  |
| `ASSOCIATE_COMMAND_LEAVEPARTY` | int | `-17` |  |
| `ASSOCIATE_COMMAND_PICKLOCK` | int | `-18` |  |
| `ASSOCIATE_COMMAND_INVENTORY` | int | `-19` |  |
| `ASSOCIATE_COMMAND_DISARMTRAP` | int | `-20` |  |
| `ASSOCIATE_COMMAND_TOGGLECASTING` | int | `-21` |  |
| `ASSOCIATE_COMMAND_TOGGLESTEALTH` | int | `-22` |  |
| `ASSOCIATE_COMMAND_TOGGLESEARCH` | int | `-23` |  |
| `ASSOCIATE_TYPE_NONE` | int | `0` |  |
| `ASSOCIATE_TYPE_HENCHMAN` | int | `1` |  |
| `ASSOCIATE_TYPE_ANIMALCOMPANION` | int | `2` |  |
| `ASSOCIATE_TYPE_FAMILIAR` | int | `3` |  |
| `ASSOCIATE_TYPE_SUMMONED` | int | `4` |  |
| `ASSOCIATE_TYPE_DOMINATED` | int | `5` |  |
| `TALENT_CATEGORY_HARMFUL_AREAEFFECT_DISCRIMINANT` | int | `1` |  |
| `TALENT_CATEGORY_HARMFUL_RANGED` | int | `2` |  |
| `TALENT_CATEGORY_HARMFUL_TOUCH` | int | `3` |  |
| `TALENT_CATEGORY_BENEFICIAL_HEALING_AREAEFFECT` | int | `4` |  |
| `TALENT_CATEGORY_BENEFICIAL_HEALING_TOUCH` | int | `5` |  |
| `TALENT_CATEGORY_BENEFICIAL_CONDITIONAL_AREAEFFECT` | int | `6` |  |
| `TALENT_CATEGORY_BENEFICIAL_CONDITIONAL_SINGLE` | int | `7` |  |
| `TALENT_CATEGORY_BENEFICIAL_ENHANCEMENT_AREAEFFECT` | int | `8` |  |
| `TALENT_CATEGORY_BENEFICIAL_ENHANCEMENT_SINGLE` | int | `9` |  |
| `TALENT_CATEGORY_BENEFICIAL_ENHANCEMENT_SELF` | int | `10` |  |
| `TALENT_CATEGORY_HARMFUL_AREAEFFECT_INDISCRIMINANT` | int | `11` |  |
| `TALENT_CATEGORY_BENEFICIAL_PROTECTION_SELF` | int | `12` |  |
| `TALENT_CATEGORY_BENEFICIAL_PROTECTION_SINGLE` | int | `13` |  |
| `TALENT_CATEGORY_BENEFICIAL_PROTECTION_AREAEFFECT` | int | `14` |  |
| `TALENT_CATEGORY_BENEFICIAL_OBTAIN_ALLIES` | int | `15` |  |
| `TALENT_CATEGORY_PERSISTENT_AREA_OF_EFFECT` | int | `16` |  |
| `TALENT_CATEGORY_BENEFICIAL_HEALING_POTION` | int | `17` |  |
| `TALENT_CATEGORY_BENEFICIAL_CONDITIONAL_POTION` | int | `18` |  |
| `TALENT_CATEGORY_DRAGONS_BREATH` | int | `19` |  |
| `TALENT_CATEGORY_BENEFICIAL_PROTECTION_POTION` | int | `20` |  |
| `TALENT_CATEGORY_BENEFICIAL_ENHANCEMENT_POTION` | int | `21` |  |
| `TALENT_CATEGORY_HARMFUL_MELEE` | int | `22` |  |
| `INVENTORY_DISTURB_TYPE_ADDED` | int | `0` |  |
| `INVENTORY_DISTURB_TYPE_REMOVED` | int | `1` |  |
| `INVENTORY_DISTURB_TYPE_STOLEN` | int | `2` |  |
| `GUI_PANEL_PLAYER_DEATH` | int | `0` |  |
| `GUI_PANEL_MINIMAP` | int | `2` |  |
| `GUI_PANEL_COMPASS` | int | `3` |  |
| `GUI_PANEL_INVENTORY` | int | `4` |  |
| `GUI_PANEL_PLAYERLIST` | int | `5` |  |
| `GUI_PANEL_JOURNAL` | int | `6` |  |
| `GUI_PANEL_SPELLBOOK` | int | `7` |  |
| `GUI_PANEL_CHARACTERSHEET` | int | `8` |  |
| `GUI_PANEL_LEVELUP` | int | `9` |  |
| `GUI_PANEL_GOLD_INVENTORY` | int | `10` |  |
| `GUI_PANEL_GOLD_BARTER` | int | `11` |  |
| `GUI_PANEL_EXAMINE_CREATURE` | int | `12` |  |
| `GUI_PANEL_EXAMINE_ITEM` | int | `13` |  |
| `GUI_PANEL_EXAMINE_PLACEABLE` | int | `14` |  |
| `GUI_PANEL_EXAMINE_DOOR` | int | `15` |  |
| `GUI_PANEL_RADIAL_TILE` | int | `16` |  |
| `GUI_PANEL_RADIAL_TRIGGER` | int | `17` |  |
| `GUI_PANEL_RADIAL_CREATURE` | int | `18` |  |
| `GUI_PANEL_RADIAL_ITEM` | int | `19` |  |
| `GUI_PANEL_RADIAL_PLACEABLE` | int | `20` |  |
| `GUI_PANEL_RADIAL_DOOR` | int | `21` |  |
| `GUI_PANEL_RADIAL_QUICKBAR` | int | `22` |  |
| `VOICE_CHAT_ATTACK` | int | `0` |  |
| `VOICE_CHAT_BATTLECRY1` | int | `1` |  |
| `VOICE_CHAT_BATTLECRY2` | int | `2` |  |
| `VOICE_CHAT_BATTLECRY3` | int | `3` |  |
| `VOICE_CHAT_HEALME` | int | `4` |  |
| `VOICE_CHAT_HELP` | int | `5` |  |
| `VOICE_CHAT_ENEMIES` | int | `6` |  |
| `VOICE_CHAT_FLEE` | int | `7` |  |
| `VOICE_CHAT_TAUNT` | int | `8` |  |
| `VOICE_CHAT_GUARDME` | int | `9` |  |
| `VOICE_CHAT_HOLD` | int | `10` |  |
| `VOICE_CHAT_GATTACK1` | int | `11` |  |
| `VOICE_CHAT_GATTACK2` | int | `12` |  |
| `VOICE_CHAT_GATTACK3` | int | `13` |  |
| `VOICE_CHAT_PAIN1` | int | `14` |  |
| `VOICE_CHAT_PAIN2` | int | `15` |  |
| `VOICE_CHAT_PAIN3` | int | `16` |  |
| `VOICE_CHAT_NEARDEATH` | int | `17` |  |
| `VOICE_CHAT_DEATH` | int | `18` |  |
| `VOICE_CHAT_POISONED` | int | `19` |  |
| `VOICE_CHAT_SPELLFAILED` | int | `20` |  |
| `VOICE_CHAT_WEAPONSUCKS` | int | `21` |  |
| `VOICE_CHAT_FOLLOWME` | int | `22` |  |
| `VOICE_CHAT_LOOKHERE` | int | `23` |  |
| `VOICE_CHAT_GROUP` | int | `24` |  |
| `VOICE_CHAT_MOVEOVER` | int | `25` |  |
| `VOICE_CHAT_PICKLOCK` | int | `26` |  |
| `VOICE_CHAT_SEARCH` | int | `27` |  |
| `VOICE_CHAT_HIDE` | int | `28` |  |
| `VOICE_CHAT_CANDO` | int | `29` |  |
| `VOICE_CHAT_CANTDO` | int | `30` |  |
| `VOICE_CHAT_TASKCOMPLETE` | int | `31` |  |
| `VOICE_CHAT_ENCUMBERED` | int | `32` |  |
| `VOICE_CHAT_SELECTED` | int | `33` |  |
| `VOICE_CHAT_HELLO` | int | `34` |  |
| `VOICE_CHAT_YES` | int | `35` |  |
| `VOICE_CHAT_NO` | int | `36` |  |
| `VOICE_CHAT_STOP` | int | `37` |  |
| `VOICE_CHAT_REST` | int | `38` |  |
| `VOICE_CHAT_BORED` | int | `39` |  |
| `VOICE_CHAT_GOODBYE` | int | `40` |  |
| `VOICE_CHAT_THANKS` | int | `41` |  |
| `VOICE_CHAT_LAUGH` | int | `42` |  |
| `VOICE_CHAT_CUSS` | int | `43` |  |
| `VOICE_CHAT_CHEER` | int | `44` |  |
| `VOICE_CHAT_TALKTOME` | int | `45` |  |
| `VOICE_CHAT_GOODIDEA` | int | `46` |  |
| `VOICE_CHAT_BADIDEA` | int | `47` |  |
| `VOICE_CHAT_THREATEN` | int | `48` |  |
| `POLYMORPH_TYPE_WEREWOLF` | int | `0` |  |
| `POLYMORPH_TYPE_WERERAT` | int | `1` |  |
| `POLYMORPH_TYPE_WERECAT` | int | `2` |  |
| `POLYMORPH_TYPE_GIANT_SPIDER` | int | `3` |  |
| `POLYMORPH_TYPE_TROLL` | int | `4` |  |
| `POLYMORPH_TYPE_UMBER_HULK` | int | `5` |  |
| `POLYMORPH_TYPE_PIXIE` | int | `6` |  |
| `POLYMORPH_TYPE_ZOMBIE` | int | `7` |  |
| `POLYMORPH_TYPE_RED_DRAGON` | int | `8` |  |
| `POLYMORPH_TYPE_FIRE_GIANT` | int | `9` |  |
| `POLYMORPH_TYPE_BALOR` | int | `10` |  |
| `POLYMORPH_TYPE_DEATH_SLAAD` | int | `11` |  |
| `POLYMORPH_TYPE_IRON_GOLEM` | int | `12` |  |
| `POLYMORPH_TYPE_HUGE_FIRE_ELEMENTAL` | int | `13` |  |
| `POLYMORPH_TYPE_HUGE_WATER_ELEMENTAL` | int | `14` |  |
| `POLYMORPH_TYPE_HUGE_EARTH_ELEMENTAL` | int | `15` |  |
| `POLYMORPH_TYPE_HUGE_AIR_ELEMENTAL` | int | `16` |  |
| `POLYMORPH_TYPE_ELDER_FIRE_ELEMENTAL` | int | `17` |  |
| `POLYMORPH_TYPE_ELDER_WATER_ELEMENTAL` | int | `18` |  |
| `POLYMORPH_TYPE_ELDER_EARTH_ELEMENTAL` | int | `19` |  |
| `POLYMORPH_TYPE_ELDER_AIR_ELEMENTAL` | int | `20` |  |
| `POLYMORPH_TYPE_BROWN_BEAR` | int | `21` |  |
| `POLYMORPH_TYPE_PANTHER` | int | `22` |  |
| `POLYMORPH_TYPE_WOLF` | int | `23` |  |
| `POLYMORPH_TYPE_BOAR` | int | `24` |  |
| `POLYMORPH_TYPE_BADGER` | int | `25` |  |
| `POLYMORPH_TYPE_PENGUIN` | int | `26` |  |
| `POLYMORPH_TYPE_COW` | int | `27` |  |
| `POLYMORPH_TYPE_DOOM_KNIGHT` | int | `28` |  |
| `POLYMORPH_TYPE_YUANTI` | int | `29` |  |
| `POLYMORPH_TYPE_IMP` | int | `30` |  |
| `POLYMORPH_TYPE_QUASIT` | int | `31` |  |
| `POLYMORPH_TYPE_SUCCUBUS` | int | `32` |  |
| `POLYMORPH_TYPE_DIRE_BROWN_BEAR` | int | `33` |  |
| `POLYMORPH_TYPE_DIRE_PANTHER` | int | `34` |  |
| `POLYMORPH_TYPE_DIRE_WOLF` | int | `35` |  |
| `POLYMORPH_TYPE_DIRE_BOAR` | int | `36` |  |
| `POLYMORPH_TYPE_DIRE_BADGER` | int | `37` |  |
| `POLYMORPH_TYPE_CELESTIAL_AVENGER` | int | `38` |  |
| `POLYMORPH_TYPE_VROCK` | int | `39` |  |
| `POLYMORPH_TYPE_CHICKEN` | int | `40` |  |
| `POLYMORPH_TYPE_FROST_GIANT_MALE` | int | `41` |  |
| `POLYMORPH_TYPE_FROST_GIANT_FEMALE` | int | `42` |  |
| `POLYMORPH_TYPE_HEURODIS` | int | `43` |  |
| `POLYMORPH_TYPE_JNAH_GIANT_MALE` | int | `44` |  |
| `POLYMORPH_TYPE_JNAH_GIANT_FEMAL` | int | `45` |  |
| `POLYMORPH_TYPE_WYRMLING_WHITE` | int | `52` |  |
| `POLYMORPH_TYPE_WYRMLING_BLUE` | int | `53` |  |
| `POLYMORPH_TYPE_WYRMLING_RED` | int | `54` |  |
| `POLYMORPH_TYPE_WYRMLING_GREEN` | int | `55` |  |
| `POLYMORPH_TYPE_WYRMLING_BLACK` | int | `56` |  |
| `POLYMORPH_TYPE_GOLEM_AUTOMATON` | int | `57` |  |
| `POLYMORPH_TYPE_MANTICORE` | int | `58` |  |
| `POLYMORPH_TYPE_MALE_DROW` | int | `59` |  |
| `POLYMORPH_TYPE_HARPY` | int | `60` |  |
| `POLYMORPH_TYPE_BASILISK` | int | `61` |  |
| `POLYMORPH_TYPE_DRIDER` | int | `62` |  |
| `POLYMORPH_TYPE_BEHOLDER` | int | `63` |  |
| `POLYMORPH_TYPE_MEDUSA` | int | `64` |  |
| `POLYMORPH_TYPE_GARGOYLE` | int | `65` |  |
| `POLYMORPH_TYPE_MINOTAUR` | int | `66` |  |
| `POLYMORPH_TYPE_SUPER_CHICKEN` | int | `67` |  |
| `POLYMORPH_TYPE_MINDFLAYER` | int | `68` |  |
| `POLYMORPH_TYPE_DIRETIGER` | int | `69` |  |
| `POLYMORPH_TYPE_FEMALE_DROW` | int | `70` |  |
| `POLYMORPH_TYPE_ANCIENT_BLUE_DRAGON` | int | `71` |  |
| `POLYMORPH_TYPE_ANCIENT_RED_DRAGON` | int | `72` |  |
| `POLYMORPH_TYPE_ANCIENT_GREEN_DRAGON` | int | `73` |  |
| `POLYMORPH_TYPE_VAMPIRE_MALE` | int | `74` |  |
| `POLYMORPH_TYPE_RISEN_LORD` | int | `75` |  |
| `POLYMORPH_TYPE_SPECTRE` | int | `76` |  |
| `POLYMORPH_TYPE_VAMPIRE_FEMALE` | int | `77` |  |
| `POLYMORPH_TYPE_NULL_HUMAN` | int | `78` |  |
| `INVISIBILITY_TYPE_NORMAL` | int | `1` |  |
| `INVISIBILITY_TYPE_DARKNESS` | int | `2` |  |
| `INVISIBILITY_TYPE_IMPROVED` | int | `4` |  |
| `CREATURE_SIZE_INVALID` | int | `0` |  |
| `CREATURE_SIZE_TINY` | int | `1` |  |
| `CREATURE_SIZE_SMALL` | int | `2` |  |
| `CREATURE_SIZE_MEDIUM` | int | `3` |  |
| `CREATURE_SIZE_LARGE` | int | `4` |  |
| `CREATURE_SIZE_HUGE` | int | `5` |  |
| `SPELL_SCHOOL_GENERAL` | int | `0` |  |
| `SPELL_SCHOOL_ABJURATION` | int | `1` |  |
| `SPELL_SCHOOL_CONJURATION` | int | `2` |  |
| `SPELL_SCHOOL_DIVINATION` | int | `3` |  |
| `SPELL_SCHOOL_ENCHANTMENT` | int | `4` |  |
| `SPELL_SCHOOL_EVOCATION` | int | `5` |  |
| `SPELL_SCHOOL_ILLUSION` | int | `6` |  |
| `SPELL_SCHOOL_NECROMANCY` | int | `7` |  |
| `SPELL_SCHOOL_TRANSMUTATION` | int | `8` |  |
| `ANIMAL_COMPANION_CREATURE_TYPE_BADGER` | int | `0` |  |
| `ANIMAL_COMPANION_CREATURE_TYPE_WOLF` | int | `1` |  |
| `ANIMAL_COMPANION_CREATURE_TYPE_BEAR` | int | `2` |  |
| `ANIMAL_COMPANION_CREATURE_TYPE_BOAR` | int | `3` |  |
| `ANIMAL_COMPANION_CREATURE_TYPE_HAWK` | int | `4` |  |
| `ANIMAL_COMPANION_CREATURE_TYPE_PANTHER` | int | `5` |  |
| `ANIMAL_COMPANION_CREATURE_TYPE_SPIDER` | int | `6` |  |
| `ANIMAL_COMPANION_CREATURE_TYPE_DIREWOLF` | int | `7` |  |
| `ANIMAL_COMPANION_CREATURE_TYPE_DIRERAT` | int | `8` |  |
| `ANIMAL_COMPANION_CREATURE_TYPE_NONE` | int | `255` |  |
| `FAMILIAR_CREATURE_TYPE_BAT` | int | `0` |  |
| `FAMILIAR_CREATURE_TYPE_CRAGCAT` | int | `1` |  |
| `FAMILIAR_CREATURE_TYPE_HELLHOUND` | int | `2` |  |
| `FAMILIAR_CREATURE_TYPE_IMP` | int | `3` |  |
| `FAMILIAR_CREATURE_TYPE_FIREMEPHIT` | int | `4` |  |
| `FAMILIAR_CREATURE_TYPE_ICEMEPHIT` | int | `5` |  |
| `FAMILIAR_CREATURE_TYPE_PIXIE` | int | `6` |  |
| `FAMILIAR_CREATURE_TYPE_RAVEN` | int | `7` |  |
| `FAMILIAR_CREATURE_TYPE_FAIRY_DRAGON` | int | `8` |  |
| `FAMILIAR_CREATURE_TYPE_PSEUDO_DRAGON` | int | `9` |  |
| `FAMILIAR_CREATURE_TYPE_EYEBALL` | int | `10` |  |
| `FAMILIAR_CREATURE_TYPE_NONE` | int | `255` |  |
| `CAMERA_MODE_CHASE_CAMERA` | int | `0` |  |
| `CAMERA_MODE_TOP_DOWN` | int | `1` |  |
| `CAMERA_MODE_STIFF_CHASE_CAMERA` | int | `2` |  |
| `WEATHER_INVALID` | int | `-1` |  |
| `WEATHER_CLEAR` | int | `0` |  |
| `WEATHER_RAIN` | int | `1` |  |
| `WEATHER_SNOW` | int | `2` |  |
| `WEATHER_USE_AREA_SETTINGS` | int | `-1` |  |
| `REST_EVENTTYPE_REST_INVALID` | int | `0` |  |
| `REST_EVENTTYPE_REST_STARTED` | int | `1` |  |
| `REST_EVENTTYPE_REST_FINISHED` | int | `2` |  |
| `REST_EVENTTYPE_REST_CANCELLED` | int | `3` |  |
| `PROJECTILE_PATH_TYPE_DEFAULT` | int | `0` |  |
| `PROJECTILE_PATH_TYPE_HOMING` | int | `1` |  |
| `PROJECTILE_PATH_TYPE_BALLISTIC` | int | `2` |  |
| `PROJECTILE_PATH_TYPE_HIGH_BALLISTIC` | int | `3` |  |
| `PROJECTILE_PATH_TYPE_ACCELERATING` | int | `4` |  |
| `GAME_DIFFICULTY_VERY_EASY` | int | `0` |  |
| `GAME_DIFFICULTY_EASY` | int | `1` |  |
| `GAME_DIFFICULTY_NORMAL` | int | `2` |  |
| `GAME_DIFFICULTY_CORE_RULES` | int | `3` |  |
| `GAME_DIFFICULTY_DIFFICULT` | int | `4` |  |
| `TILE_MAIN_LIGHT_COLOR_BLACK` | int | `0` |  |
| `TILE_MAIN_LIGHT_COLOR_DIM_WHITE` | int | `1` |  |
| `TILE_MAIN_LIGHT_COLOR_WHITE` | int | `2` |  |
| `TILE_MAIN_LIGHT_COLOR_BRIGHT_WHITE` | int | `3` |  |
| `TILE_MAIN_LIGHT_COLOR_PALE_DARK_YELLOW` | int | `4` |  |
| `TILE_MAIN_LIGHT_COLOR_DARK_YELLOW` | int | `5` |  |
| `TILE_MAIN_LIGHT_COLOR_PALE_YELLOW` | int | `6` |  |
| `TILE_MAIN_LIGHT_COLOR_YELLOW` | int | `7` |  |
| `TILE_MAIN_LIGHT_COLOR_PALE_DARK_GREEN` | int | `8` |  |
| `TILE_MAIN_LIGHT_COLOR_DARK_GREEN` | int | `9` |  |
| `TILE_MAIN_LIGHT_COLOR_PALE_GREEN` | int | `10` |  |
| `TILE_MAIN_LIGHT_COLOR_GREEN` | int | `11` |  |
| `TILE_MAIN_LIGHT_COLOR_PALE_DARK_AQUA` | int | `12` |  |
| `TILE_MAIN_LIGHT_COLOR_DARK_AQUA` | int | `13` |  |
| `TILE_MAIN_LIGHT_COLOR_PALE_AQUA` | int | `14` |  |
| `TILE_MAIN_LIGHT_COLOR_AQUA` | int | `15` |  |
| `TILE_MAIN_LIGHT_COLOR_PALE_DARK_BLUE` | int | `16` |  |
| `TILE_MAIN_LIGHT_COLOR_DARK_BLUE` | int | `17` |  |
| `TILE_MAIN_LIGHT_COLOR_PALE_BLUE` | int | `18` |  |
| `TILE_MAIN_LIGHT_COLOR_BLUE` | int | `19` |  |
| `TILE_MAIN_LIGHT_COLOR_PALE_DARK_PURPLE` | int | `20` |  |
| `TILE_MAIN_LIGHT_COLOR_DARK_PURPLE` | int | `21` |  |
| `TILE_MAIN_LIGHT_COLOR_PALE_PURPLE` | int | `22` |  |
| `TILE_MAIN_LIGHT_COLOR_PURPLE` | int | `23` |  |
| `TILE_MAIN_LIGHT_COLOR_PALE_DARK_RED` | int | `24` |  |
| `TILE_MAIN_LIGHT_COLOR_DARK_RED` | int | `25` |  |
| `TILE_MAIN_LIGHT_COLOR_PALE_RED` | int | `26` |  |
| `TILE_MAIN_LIGHT_COLOR_RED` | int | `27` |  |
| `TILE_MAIN_LIGHT_COLOR_PALE_DARK_ORANGE` | int | `28` |  |
| `TILE_MAIN_LIGHT_COLOR_DARK_ORANGE` | int | `29` |  |
| `TILE_MAIN_LIGHT_COLOR_PALE_ORANGE` | int | `30` |  |
| `TILE_MAIN_LIGHT_COLOR_ORANGE` | int | `31` |  |
| `TILE_SOURCE_LIGHT_COLOR_BLACK` | int | `0` |  |
| `TILE_SOURCE_LIGHT_COLOR_WHITE` | int | `1` |  |
| `TILE_SOURCE_LIGHT_COLOR_PALE_DARK_YELLOW` | int | `2` |  |
| `TILE_SOURCE_LIGHT_COLOR_PALE_YELLOW` | int | `3` |  |
| `TILE_SOURCE_LIGHT_COLOR_PALE_DARK_GREEN` | int | `4` |  |
| `TILE_SOURCE_LIGHT_COLOR_PALE_GREEN` | int | `5` |  |
| `TILE_SOURCE_LIGHT_COLOR_PALE_DARK_AQUA` | int | `6` |  |
| `TILE_SOURCE_LIGHT_COLOR_PALE_AQUA` | int | `7` |  |
| `TILE_SOURCE_LIGHT_COLOR_PALE_DARK_BLUE` | int | `8` |  |
| `TILE_SOURCE_LIGHT_COLOR_PALE_BLUE` | int | `9` |  |
| `TILE_SOURCE_LIGHT_COLOR_PALE_DARK_PURPLE` | int | `10` |  |
| `TILE_SOURCE_LIGHT_COLOR_PALE_PURPLE` | int | `11` |  |
| `TILE_SOURCE_LIGHT_COLOR_PALE_DARK_RED` | int | `12` |  |
| `TILE_SOURCE_LIGHT_COLOR_PALE_RED` | int | `13` |  |
| `TILE_SOURCE_LIGHT_COLOR_PALE_DARK_ORANGE` | int | `14` |  |
| `TILE_SOURCE_LIGHT_COLOR_PALE_ORANGE` | int | `15` |  |
| `PANEL_BUTTON_MAP` | int | `0` |  |
| `PANEL_BUTTON_INVENTORY` | int | `1` |  |
| `PANEL_BUTTON_JOURNAL` | int | `2` |  |
| `PANEL_BUTTON_CHARACTER` | int | `3` |  |
| `PANEL_BUTTON_OPTIONS` | int | `4` |  |
| `PANEL_BUTTON_SPELLS` | int | `5` |  |
| `PANEL_BUTTON_REST` | int | `6` |  |
| `PANEL_BUTTON_PLAYER_VERSUS_PLAYER` | int | `7` |  |
| `ACTION_MOVETOPOINT` | int | `0` |  |
| `ACTION_PICKUPITEM` | int | `1` |  |
| `ACTION_DROPITEM` | int | `2` |  |
| `ACTION_ATTACKOBJECT` | int | `3` |  |
| `ACTION_CASTSPELL` | int | `4` |  |
| `ACTION_OPENDOOR` | int | `5` |  |
| `ACTION_CLOSEDOOR` | int | `6` |  |
| `ACTION_DIALOGOBJECT` | int | `7` |  |
| `ACTION_DISABLETRAP` | int | `8` |  |
| `ACTION_RECOVERTRAP` | int | `9` |  |
| `ACTION_FLAGTRAP` | int | `10` |  |
| `ACTION_EXAMINETRAP` | int | `11` |  |
| `ACTION_SETTRAP` | int | `12` |  |
| `ACTION_OPENLOCK` | int | `13` |  |
| `ACTION_LOCK` | int | `14` |  |
| `ACTION_USEOBJECT` | int | `15` |  |
| `ACTION_ANIMALEMPATHY` | int | `16` |  |
| `ACTION_REST` | int | `17` |  |
| `ACTION_TAUNT` | int | `18` |  |
| `ACTION_ITEMCASTSPELL` | int | `19` |  |
| `ACTION_COUNTERSPELL` | int | `31` |  |
| `ACTION_HEAL` | int | `33` |  |
| `ACTION_PICKPOCKET` | int | `34` |  |
| `ACTION_FOLLOW` | int | `35` |  |
| `ACTION_WAIT` | int | `36` |  |
| `ACTION_SIT` | int | `37` |  |
| `ACTION_SMITEGOOD` | int | `40` |  |
| `ACTION_KIDAMAGE` | int | `41` |  |
| `ACTION_RANDOMWALK` | int | `43` |  |
| `ACTION_INVALID` | int | `65535` |  |
| `TRAP_BASE_TYPE_MINOR_SPIKE` | int | `0` |  |
| `TRAP_BASE_TYPE_AVERAGE_SPIKE` | int | `1` |  |
| `TRAP_BASE_TYPE_STRONG_SPIKE` | int | `2` |  |
| `TRAP_BASE_TYPE_DEADLY_SPIKE` | int | `3` |  |
| `TRAP_BASE_TYPE_MINOR_HOLY` | int | `4` |  |
| `TRAP_BASE_TYPE_AVERAGE_HOLY` | int | `5` |  |
| `TRAP_BASE_TYPE_STRONG_HOLY` | int | `6` |  |
| `TRAP_BASE_TYPE_DEADLY_HOLY` | int | `7` |  |
| `TRAP_BASE_TYPE_MINOR_TANGLE` | int | `8` |  |
| `TRAP_BASE_TYPE_AVERAGE_TANGLE` | int | `9` |  |
| `TRAP_BASE_TYPE_STRONG_TANGLE` | int | `10` |  |
| `TRAP_BASE_TYPE_DEADLY_TANGLE` | int | `11` |  |
| `TRAP_BASE_TYPE_MINOR_ACID` | int | `12` |  |
| `TRAP_BASE_TYPE_AVERAGE_ACID` | int | `13` |  |
| `TRAP_BASE_TYPE_STRONG_ACID` | int | `14` |  |
| `TRAP_BASE_TYPE_DEADLY_ACID` | int | `15` |  |
| `TRAP_BASE_TYPE_MINOR_FIRE` | int | `16` |  |
| `TRAP_BASE_TYPE_AVERAGE_FIRE` | int | `17` |  |
| `TRAP_BASE_TYPE_STRONG_FIRE` | int | `18` |  |
| `TRAP_BASE_TYPE_DEADLY_FIRE` | int | `19` |  |
| `TRAP_BASE_TYPE_MINOR_ELECTRICAL` | int | `20` |  |
| `TRAP_BASE_TYPE_AVERAGE_ELECTRICAL` | int | `21` |  |
| `TRAP_BASE_TYPE_STRONG_ELECTRICAL` | int | `22` |  |
| `TRAP_BASE_TYPE_DEADLY_ELECTRICAL` | int | `23` |  |
| `TRAP_BASE_TYPE_MINOR_GAS` | int | `24` |  |
| `TRAP_BASE_TYPE_AVERAGE_GAS` | int | `25` |  |
| `TRAP_BASE_TYPE_STRONG_GAS` | int | `26` |  |
| `TRAP_BASE_TYPE_DEADLY_GAS` | int | `27` |  |
| `TRAP_BASE_TYPE_MINOR_FROST` | int | `28` |  |
| `TRAP_BASE_TYPE_AVERAGE_FROST` | int | `29` |  |
| `TRAP_BASE_TYPE_STRONG_FROST` | int | `30` |  |
| `TRAP_BASE_TYPE_DEADLY_FROST` | int | `31` |  |
| `TRAP_BASE_TYPE_MINOR_NEGATIVE` | int | `32` |  |
| `TRAP_BASE_TYPE_AVERAGE_NEGATIVE` | int | `33` |  |
| `TRAP_BASE_TYPE_STRONG_NEGATIVE` | int | `34` |  |
| `TRAP_BASE_TYPE_DEADLY_NEGATIVE` | int | `35` |  |
| `TRAP_BASE_TYPE_MINOR_SONIC` | int | `36` |  |
| `TRAP_BASE_TYPE_AVERAGE_SONIC` | int | `37` |  |
| `TRAP_BASE_TYPE_STRONG_SONIC` | int | `38` |  |
| `TRAP_BASE_TYPE_DEADLY_SONIC` | int | `39` |  |
| `TRAP_BASE_TYPE_MINOR_ACID_SPLASH` | int | `40` |  |
| `TRAP_BASE_TYPE_AVERAGE_ACID_SPLASH` | int | `41` |  |
| `TRAP_BASE_TYPE_STRONG_ACID_SPLASH` | int | `42` |  |
| `TRAP_BASE_TYPE_DEADLY_ACID_SPLASH` | int | `43` |  |
| `TRAP_BASE_TYPE_EPIC_ELECTRICAL` | int | `44` |  |
| `TRAP_BASE_TYPE_EPIC_FIRE` | int | `45` |  |
| `TRAP_BASE_TYPE_EPIC_FROST` | int | `46` |  |
| `TRAP_BASE_TYPE_EPIC_SONIC` | int | `47` |  |
| `TRACK_RURALDAY1` | int | `1` |  |
| `TRACK_RURALDAY2` | int | `2` |  |
| `TRACK_RURALNIGHT` | int | `3` |  |
| `TRACK_FORESTDAY1` | int | `4` |  |
| `TRACK_FORESTDAY2` | int | `5` |  |
| `TRACK_FORESTNIGHT` | int | `6` |  |
| `TRACK_DUNGEON1` | int | `7` |  |
| `TRACK_SEWER` | int | `8` |  |
| `TRACK_MINES1` | int | `9` |  |
| `TRACK_MINES2` | int | `10` |  |
| `TRACK_CRYPT1` | int | `11` |  |
| `TRACK_CRYPT2` | int | `12` |  |
| `TRACK_DESERT_DAY` | int | `58` |  |
| `TRACK_DESERT_NIGHT` | int | `61` |  |
| `TRACK_WINTER_DAY` | int | `59` |  |
| `TRACK_EVILDUNGEON1` | int | `13` |  |
| `TRACK_EVILDUNGEON2` | int | `14` |  |
| `TRACK_CITYSLUMDAY` | int | `15` |  |
| `TRACK_CITYSLUMNIGHT` | int | `16` |  |
| `TRACK_CITYDOCKDAY` | int | `17` |  |
| `TRACK_CITYDOCKNIGHT` | int | `18` |  |
| `TRACK_CITYWEALTHY` | int | `19` |  |
| `TRACK_CITYMARKET` | int | `20` |  |
| `TRACK_CITYNIGHT` | int | `21` |  |
| `TRACK_TAVERN1` | int | `22` |  |
| `TRACK_TAVERN2` | int | `23` |  |
| `TRACK_TAVERN3` | int | `24` |  |
| `TRACK_TAVERN4` | int | `56` |  |
| `TRACK_RICHHOUSE` | int | `25` |  |
| `TRACK_STORE` | int | `26` |  |
| `TRACK_TEMPLEGOOD` | int | `27` |  |
| `TRACK_TEMPLEGOOD2` | int | `49` |  |
| `TRACK_TEMPLEEVIL` | int | `28` |  |
| `TRACK_THEME_NWN` | int | `29` |  |
| `TRACK_THEME_CHAPTER1` | int | `30` |  |
| `TRACK_THEME_CHAPTER2` | int | `31` |  |
| `TRACK_THEME_CHAPTER3` | int | `32` |  |
| `TRACK_THEME_CHAPTER4` | int | `33` |  |
| `TRACK_BATTLE_RURAL1` | int | `34` |  |
| `TRACK_BATTLE_FOREST1` | int | `35` |  |
| `TRACK_BATTLE_FOREST2` | int | `36` |  |
| `TRACK_BATTLE_DUNGEON1` | int | `37` |  |
| `TRACK_BATTLE_DUNGEON2` | int | `38` |  |
| `TRACK_BATTLE_DUNGEON3` | int | `39` |  |
| `TRACK_BATTLE_CITY1` | int | `40` |  |
| `TRACK_BATTLE_CITY2` | int | `41` |  |
| `TRACK_BATTLE_CITY3` | int | `42` |  |
| `TRACK_BATTLE_CITYBOSS` | int | `43` |  |
| `TRACK_BATTLE_FORESTBOSS` | int | `44` |  |
| `TRACK_BATTLE_LIZARDBOSS` | int | `45` |  |
| `TRACK_BATTLE_DRAGON` | int | `46` |  |
| `TRACK_BATTLE_ARIBETH` | int | `47` |  |
| `TRACK_BATTLE_ENDBOSS` | int | `48` |  |
| `TRACK_BATTLE_DESERT` | int | `57` |  |
| `TRACK_BATTLE_WINTER` | int | `60` |  |
| `TRACK_CASTLE` | int | `50` |  |
| `TRACK_THEME_ARIBETH1` | int | `51` |  |
| `TRACK_THEME_ARIBETH2` | int | `52` |  |
| `TRACK_THEME_GEND` | int | `53` |  |
| `TRACK_THEME_MAUGRIM` | int | `54` |  |
| `TRACK_THEME_MORAG` | int | `55` |  |
| `TRACK_HOTU_THEME` | int | `62` |  |
| `TRACK_HOTU_WATERDEEP` | int | `63` |  |
| `TRACK_HOTU_UNDERMOUNTAIN` | int | `64` |  |
| `TRACK_HOTU_REBELCAMP` | int | `65` |  |
| `TRACK_HOTU_FIREPLANE` | int | `66` |  |
| `TRACK_HOTU_QUEEN` | int | `67` |  |
| `TRACK_HOTU_HELLFROZEOVER` | int | `68` |  |
| `TRACK_HOTU_DRACOLICH` | int | `69` |  |
| `TRACK_HOTU_BATTLE_SMALL` | int | `70` |  |
| `TRACK_HOTU_BATTLE_MED` | int | `71` |  |
| `TRACK_HOTU_BATTLE_LARGE` | int | `72` |  |
| `TRACK_HOTU_BATTLE_HELL` | int | `73` |  |
| `TRACK_HOTU_BATTLE_BOSS1` | int | `74` |  |
| `TRACK_HOTU_BATTLE_BOSS2` | int | `75` |  |
| `STEALTH_MODE_DISABLED` | int | `0` |  |
| `STEALTH_MODE_ACTIVATED` | int | `1` |  |
| `DETECT_MODE_PASSIVE` | int | `0` |  |
| `DETECT_MODE_ACTIVE` | int | `1` |  |
| `DEFENSIVE_CASTING_MODE_DISABLED` | int | `0` |  |
| `DEFENSIVE_CASTING_MODE_ACTIVATED` | int | `1` |  |
| `APPEARANCE_TYPE_INVALID` | int | `-1` |  |
| `APPEARANCE_TYPE_ALLIP` | int | `186` |  |
| `APPEARANCE_TYPE_ARANEA` | int | `157` |  |
| `APPEARANCE_TYPE_ARCH_TARGET` | int | `200` |  |
| `APPEARANCE_TYPE_ARIBETH` | int | `190` |  |
| `APPEARANCE_TYPE_ASABI_CHIEFTAIN` | int | `353` |  |
| `APPEARANCE_TYPE_ASABI_SHAMAN` | int | `354` |  |
| `APPEARANCE_TYPE_ASABI_WARRIOR` | int | `355` |  |
| `APPEARANCE_TYPE_BADGER` | int | `8` |  |
| `APPEARANCE_TYPE_BADGER_DIRE` | int | `9` |  |
| `APPEARANCE_TYPE_BALOR` | int | `38` |  |
| `APPEARANCE_TYPE_BARTENDER` | int | `234` |  |
| `APPEARANCE_TYPE_BASILISK` | int | `369` |  |
| `APPEARANCE_TYPE_BAT` | int | `10` |  |
| `APPEARANCE_TYPE_BAT_HORROR` | int | `11` |  |
| `APPEARANCE_TYPE_BEAR_BLACK` | int | `12` |  |
| `APPEARANCE_TYPE_BEAR_BROWN` | int | `13` |  |
| `APPEARANCE_TYPE_BEAR_DIRE` | int | `15` |  |
| `APPEARANCE_TYPE_BEAR_KODIAK` | int | `204` |  |
| `APPEARANCE_TYPE_BEAR_POLAR` | int | `14` |  |
| `APPEARANCE_TYPE_BEETLE_FIRE` | int | `18` |  |
| `APPEARANCE_TYPE_BEETLE_SLICER` | int | `17` |  |
| `APPEARANCE_TYPE_BEETLE_STAG` | int | `19` |  |
| `APPEARANCE_TYPE_BEETLE_STINK` | int | `20` |  |
| `APPEARANCE_TYPE_BEGGER` | int | `220` |  |
| `APPEARANCE_TYPE_BLOOD_SAILER` | int | `221` |  |
| `APPEARANCE_TYPE_BOAR` | int | `21` |  |
| `APPEARANCE_TYPE_BOAR_DIRE` | int | `22` |  |
| `APPEARANCE_TYPE_BODAK` | int | `23` |  |
| `APPEARANCE_TYPE_BUGBEAR_A` | int | `29` |  |
| `APPEARANCE_TYPE_BUGBEAR_B` | int | `30` |  |
| `APPEARANCE_TYPE_BUGBEAR_CHIEFTAIN_A` | int | `25` |  |
| `APPEARANCE_TYPE_BUGBEAR_CHIEFTAIN_B` | int | `26` |  |
| `APPEARANCE_TYPE_BUGBEAR_SHAMAN_A` | int | `27` |  |
| `APPEARANCE_TYPE_BUGBEAR_SHAMAN_B` | int | `28` |  |
| `APPEARANCE_TYPE_BULETTE` | int | `481` |  |
| `APPEARANCE_TYPE_CAT_CAT_DIRE` | int | `95` |  |
| `APPEARANCE_TYPE_CAT_COUGAR` | int | `203` |  |
| `APPEARANCE_TYPE_CAT_CRAG_CAT` | int | `94` |  |
| `APPEARANCE_TYPE_CAT_JAGUAR` | int | `98` |  |
| `APPEARANCE_TYPE_CAT_KRENSHAR` | int | `96` |  |
| `APPEARANCE_TYPE_CAT_LEOPARD` | int | `93` |  |
| `APPEARANCE_TYPE_CAT_LION` | int | `97` |  |
| `APPEARANCE_TYPE_CAT_MPANTHER` | int | `306` |  |
| `APPEARANCE_TYPE_CAT_PANTHER` | int | `202` |  |
| `APPEARANCE_TYPE_CHICKEN` | int | `31` |  |
| `APPEARANCE_TYPE_COCKATRICE` | int | `368` |  |
| `APPEARANCE_TYPE_COMBAT_DUMMY` | int | `201` |  |
| `APPEARANCE_TYPE_CONVICT` | int | `238` |  |
| `APPEARANCE_TYPE_COW` | int | `34` |  |
| `APPEARANCE_TYPE_CULT_MEMBER` | int | `212` |  |
| `APPEARANCE_TYPE_DEER` | int | `35` |  |
| `APPEARANCE_TYPE_DEER_STAG` | int | `37` |  |
| `APPEARANCE_TYPE_DEVIL` | int | `392` |  |
| `APPEARANCE_TYPE_DOG` | int | `176` |  |
| `APPEARANCE_TYPE_DOG_BLINKDOG` | int | `174` |  |
| `APPEARANCE_TYPE_DOG_DIRE_WOLF` | int | `175` |  |
| `APPEARANCE_TYPE_DOG_FENHOUND` | int | `177` |  |
| `APPEARANCE_TYPE_DOG_HELL_HOUND` | int | `179` |  |
| `APPEARANCE_TYPE_DOG_SHADOW_MASTIF` | int | `180` |  |
| `APPEARANCE_TYPE_DOG_WINTER_WOLF` | int | `184` |  |
| `APPEARANCE_TYPE_DOG_WOLF` | int | `181` |  |
| `APPEARANCE_TYPE_DOG_WORG` | int | `185` |  |
| `APPEARANCE_TYPE_DOOM_KNIGHT` | int | `40` |  |
| `APPEARANCE_TYPE_DRAGON_BLACK` | int | `41` |  |
| `APPEARANCE_TYPE_DRAGON_BLUE` | int | `47` |  |
| `APPEARANCE_TYPE_DRAGON_BRASS` | int | `42` |  |
| `APPEARANCE_TYPE_DRAGON_BRONZE` | int | `45` |  |
| `APPEARANCE_TYPE_DRAGON_COPPER` | int | `43` |  |
| `APPEARANCE_TYPE_DRAGON_GOLD` | int | `46` |  |
| `APPEARANCE_TYPE_DRAGON_GREEN` | int | `48` |  |
| `APPEARANCE_TYPE_DRAGON_RED` | int | `49` |  |
| `APPEARANCE_TYPE_DRAGON_SILVER` | int | `44` |  |
| `APPEARANCE_TYPE_DRAGON_WHITE` | int | `50` |  |
| `APPEARANCE_TYPE_DROW_CLERIC` | int | `215` |  |
| `APPEARANCE_TYPE_DROW_FIGHTER` | int | `216` |  |
| `APPEARANCE_TYPE_DRUEGAR_CLERIC` | int | `218` |  |
| `APPEARANCE_TYPE_DRUEGAR_FIGHTER` | int | `217` |  |
| `APPEARANCE_TYPE_DRYAD` | int | `51` |  |
| `APPEARANCE_TYPE_DWARF` | int | `0` |  |
| `APPEARANCE_TYPE_DWARF_NPC_FEMALE` | int | `248` |  |
| `APPEARANCE_TYPE_DWARF_NPC_MALE` | int | `249` |  |
| `APPEARANCE_TYPE_ELEMENTAL_AIR` | int | `52` |  |
| `APPEARANCE_TYPE_ELEMENTAL_AIR_ELDER` | int | `53` |  |
| `APPEARANCE_TYPE_ELEMENTAL_EARTH` | int | `56` |  |
| `APPEARANCE_TYPE_ELEMENTAL_EARTH_ELDER` | int | `57` |  |
| `APPEARANCE_TYPE_ELEMENTAL_FIRE` | int | `60` |  |
| `APPEARANCE_TYPE_ELEMENTAL_FIRE_ELDER` | int | `61` |  |
| `APPEARANCE_TYPE_ELEMENTAL_WATER` | int | `69` |  |
| `APPEARANCE_TYPE_ELEMENTAL_WATER_ELDER` | int | `68` |  |
| `APPEARANCE_TYPE_ELF` | int | `1` |  |
| `APPEARANCE_TYPE_ELF_NPC_FEMALE` | int | `245` |  |
| `APPEARANCE_TYPE_ELF_NPC_MALE_01` | int | `246` |  |
| `APPEARANCE_TYPE_ELF_NPC_MALE_02` | int | `247` |  |
| `APPEARANCE_TYPE_ETTERCAP` | int | `166` |  |
| `APPEARANCE_TYPE_ETTIN` | int | `72` |  |
| `APPEARANCE_TYPE_FAERIE_DRAGON` | int | `374` |  |
| `APPEARANCE_TYPE_FAIRY` | int | `55` |  |
| `APPEARANCE_TYPE_FALCON` | int | `144` |  |
| `APPEARANCE_TYPE_FEMALE_01` | int | `222` |  |
| `APPEARANCE_TYPE_FEMALE_02` | int | `223` |  |
| `APPEARANCE_TYPE_FEMALE_03` | int | `224` |  |
| `APPEARANCE_TYPE_FEMALE_04` | int | `225` |  |
| `APPEARANCE_TYPE_FORMIAN_MYRMARCH` | int | `362` |  |
| `APPEARANCE_TYPE_FORMIAN_QUEEN` | int | `363` |  |
| `APPEARANCE_TYPE_FORMIAN_WARRIOR` | int | `361` |  |
| `APPEARANCE_TYPE_FORMIAN_WORKER` | int | `360` |  |
| `APPEARANCE_TYPE_GARGOYLE` | int | `73` |  |
| `APPEARANCE_TYPE_GHAST` | int | `74` |  |
| `APPEARANCE_TYPE_GHOUL` | int | `76` |  |
| `APPEARANCE_TYPE_GHOUL_LORD` | int | `77` |  |
| `APPEARANCE_TYPE_GIANT_FIRE` | int | `80` |  |
| `APPEARANCE_TYPE_GIANT_FIRE_FEMALE` | int | `351` |  |
| `APPEARANCE_TYPE_GIANT_FROST` | int | `81` |  |
| `APPEARANCE_TYPE_GIANT_FROST_FEMALE` | int | `350` |  |
| `APPEARANCE_TYPE_GIANT_HILL` | int | `78` |  |
| `APPEARANCE_TYPE_GIANT_MOUNTAIN` | int | `79` |  |
| `APPEARANCE_TYPE_GNOLL_WARRIOR` | int | `388` |  |
| `APPEARANCE_TYPE_GNOLL_WIZ` | int | `389` |  |
| `APPEARANCE_TYPE_GNOME` | int | `2` |  |
| `APPEARANCE_TYPE_GNOME_NPC_FEMALE` | int | `243` |  |
| `APPEARANCE_TYPE_GNOME_NPC_MALE` | int | `244` |  |
| `APPEARANCE_TYPE_GOBLIN_A` | int | `86` |  |
| `APPEARANCE_TYPE_GOBLIN_B` | int | `87` |  |
| `APPEARANCE_TYPE_GOBLIN_CHIEF_A` | int | `82` |  |
| `APPEARANCE_TYPE_GOBLIN_CHIEF_B` | int | `83` |  |
| `APPEARANCE_TYPE_GOBLIN_SHAMAN_A` | int | `84` |  |
| `APPEARANCE_TYPE_GOBLIN_SHAMAN_B` | int | `85` |  |
| `APPEARANCE_TYPE_GOLEM_BONE` | int | `24` |  |
| `APPEARANCE_TYPE_GOLEM_CLAY` | int | `91` |  |
| `APPEARANCE_TYPE_GOLEM_FLESH` | int | `88` |  |
| `APPEARANCE_TYPE_GOLEM_IRON` | int | `89` |  |
| `APPEARANCE_TYPE_GOLEM_STONE` | int | `92` |  |
| `APPEARANCE_TYPE_GORGON` | int | `367` |  |
| `APPEARANCE_TYPE_GRAY_OOZE` | int | `393` |  |
| `APPEARANCE_TYPE_GREY_RENDER` | int | `205` |  |
| `APPEARANCE_TYPE_GYNOSPHINX` | int | `365` |  |
| `APPEARANCE_TYPE_HALFLING` | int | `3` |  |
| `APPEARANCE_TYPE_HALFLING_NPC_FEMALE` | int | `250` |  |
| `APPEARANCE_TYPE_HALFLING_NPC_MALE` | int | `251` |  |
| `APPEARANCE_TYPE_HALF_ELF` | int | `4` |  |
| `APPEARANCE_TYPE_HALF_ORC` | int | `5` |  |
| `APPEARANCE_TYPE_HALF_ORC_NPC_FEMALE` | int | `252` |  |
| `APPEARANCE_TYPE_HALF_ORC_NPC_MALE_01` | int | `253` |  |
| `APPEARANCE_TYPE_HALF_ORC_NPC_MALE_02` | int | `254` |  |
| `APPEARANCE_TYPE_HELMED_HORROR` | int | `100` |  |
| `APPEARANCE_TYPE_HEURODIS_LICH` | int | `370` |  |
| `APPEARANCE_TYPE_HOBGOBLIN_WARRIOR` | int | `390` |  |
| `APPEARANCE_TYPE_HOBGOBLIN_WIZARD` | int | `391` |  |
| `APPEARANCE_TYPE_HOOK_HORROR` | int | `102` |  |
| `APPEARANCE_TYPE_HOUSE_GUARD` | int | `219` |  |
| `APPEARANCE_TYPE_HUMAN` | int | `6` |  |
| `APPEARANCE_TYPE_HUMAN_NPC_FEMALE_01` | int | `255` |  |
| `APPEARANCE_TYPE_HUMAN_NPC_FEMALE_02` | int | `256` |  |
| `APPEARANCE_TYPE_HUMAN_NPC_FEMALE_03` | int | `257` |  |
| `APPEARANCE_TYPE_HUMAN_NPC_FEMALE_04` | int | `258` |  |
| `APPEARANCE_TYPE_HUMAN_NPC_FEMALE_05` | int | `259` |  |
| `APPEARANCE_TYPE_HUMAN_NPC_FEMALE_06` | int | `260` |  |
| `APPEARANCE_TYPE_HUMAN_NPC_FEMALE_07` | int | `261` |  |
| `APPEARANCE_TYPE_HUMAN_NPC_FEMALE_08` | int | `262` |  |
| `APPEARANCE_TYPE_HUMAN_NPC_FEMALE_09` | int | `263` |  |
| `APPEARANCE_TYPE_HUMAN_NPC_FEMALE_10` | int | `264` |  |
| `APPEARANCE_TYPE_HUMAN_NPC_FEMALE_11` | int | `265` |  |
| `APPEARANCE_TYPE_HUMAN_NPC_FEMALE_12` | int | `266` |  |
| `APPEARANCE_TYPE_HUMAN_NPC_MALE_01` | int | `267` |  |
| `APPEARANCE_TYPE_HUMAN_NPC_MALE_02` | int | `268` |  |
| `APPEARANCE_TYPE_HUMAN_NPC_MALE_03` | int | `269` |  |
| `APPEARANCE_TYPE_HUMAN_NPC_MALE_04` | int | `270` |  |
| `APPEARANCE_TYPE_HUMAN_NPC_MALE_05` | int | `271` |  |
| `APPEARANCE_TYPE_HUMAN_NPC_MALE_06` | int | `272` |  |
| `APPEARANCE_TYPE_HUMAN_NPC_MALE_07` | int | `273` |  |
| `APPEARANCE_TYPE_HUMAN_NPC_MALE_08` | int | `274` |  |
| `APPEARANCE_TYPE_HUMAN_NPC_MALE_09` | int | `275` |  |
| `APPEARANCE_TYPE_HUMAN_NPC_MALE_10` | int | `276` |  |
| `APPEARANCE_TYPE_HUMAN_NPC_MALE_11` | int | `277` |  |
| `APPEARANCE_TYPE_HUMAN_NPC_MALE_12` | int | `278` |  |
| `APPEARANCE_TYPE_HUMAN_NPC_MALE_13` | int | `279` |  |
| `APPEARANCE_TYPE_HUMAN_NPC_MALE_14` | int | `280` |  |
| `APPEARANCE_TYPE_HUMAN_NPC_MALE_15` | int | `281` |  |
| `APPEARANCE_TYPE_HUMAN_NPC_MALE_16` | int | `282` |  |
| `APPEARANCE_TYPE_HUMAN_NPC_MALE_17` | int | `283` |  |
| `APPEARANCE_TYPE_HUMAN_NPC_MALE_18` | int | `284` |  |
| `APPEARANCE_TYPE_IMP` | int | `105` |  |
| `APPEARANCE_TYPE_INN_KEEPER` | int | `233` |  |
| `APPEARANCE_TYPE_INTELLECT_DEVOURER` | int | `117` |  |
| `APPEARANCE_TYPE_INVISIBLE_HUMAN_MALE` | int | `298` |  |
| `APPEARANCE_TYPE_INVISIBLE_STALKER` | int | `64` |  |
| `APPEARANCE_TYPE_KID_FEMALE` | int | `242` |  |
| `APPEARANCE_TYPE_KID_MALE` | int | `241` |  |
| `APPEARANCE_TYPE_KOBOLD_A` | int | `302` |  |
| `APPEARANCE_TYPE_KOBOLD_B` | int | `305` |  |
| `APPEARANCE_TYPE_KOBOLD_CHIEF_A` | int | `300` |  |
| `APPEARANCE_TYPE_KOBOLD_CHIEF_B` | int | `303` |  |
| `APPEARANCE_TYPE_KOBOLD_SHAMAN_A` | int | `301` |  |
| `APPEARANCE_TYPE_KOBOLD_SHAMAN_B` | int | `304` |  |
| `APPEARANCE_TYPE_LANTERN_ARCHON` | int | `103` |  |
| `APPEARANCE_TYPE_LICH` | int | `39` |  |
| `APPEARANCE_TYPE_LIZARDFOLK_A` | int | `134` |  |
| `APPEARANCE_TYPE_LIZARDFOLK_B` | int | `135` |  |
| `APPEARANCE_TYPE_LIZARDFOLK_SHAMAN_A` | int | `132` |  |
| `APPEARANCE_TYPE_LIZARDFOLK_SHAMAN_B` | int | `133` |  |
| `APPEARANCE_TYPE_LIZARDFOLK_WARRIOR_A` | int | `130` |  |
| `APPEARANCE_TYPE_LIZARDFOLK_WARRIOR_B` | int | `131` |  |
| `APPEARANCE_TYPE_LUSKAN_GUARD` | int | `211` |  |
| `APPEARANCE_TYPE_MALE_01` | int | `226` |  |
| `APPEARANCE_TYPE_MALE_02` | int | `227` |  |
| `APPEARANCE_TYPE_MALE_03` | int | `228` |  |
| `APPEARANCE_TYPE_MALE_04` | int | `229` |  |
| `APPEARANCE_TYPE_MALE_05` | int | `230` |  |
| `APPEARANCE_TYPE_MANTICORE` | int | `366` |  |
| `APPEARANCE_TYPE_MEDUSA` | int | `352` |  |
| `APPEARANCE_TYPE_MEPHIT_AIR` | int | `106` |  |
| `APPEARANCE_TYPE_MEPHIT_DUST` | int | `107` |  |
| `APPEARANCE_TYPE_MEPHIT_EARTH` | int | `108` |  |
| `APPEARANCE_TYPE_MEPHIT_FIRE` | int | `109` |  |
| `APPEARANCE_TYPE_MEPHIT_ICE` | int | `110` |  |
| `APPEARANCE_TYPE_MEPHIT_MAGMA` | int | `114` |  |
| `APPEARANCE_TYPE_MEPHIT_OOZE` | int | `112` |  |
| `APPEARANCE_TYPE_MEPHIT_SALT` | int | `111` |  |
| `APPEARANCE_TYPE_MEPHIT_STEAM` | int | `113` |  |
| `APPEARANCE_TYPE_MEPHIT_WATER` | int | `115` |  |
| `APPEARANCE_TYPE_MINOGON` | int | `119` |  |
| `APPEARANCE_TYPE_MINOTAUR` | int | `120` |  |
| `APPEARANCE_TYPE_MINOTAUR_CHIEFTAIN` | int | `121` |  |
| `APPEARANCE_TYPE_MINOTAUR_SHAMAN` | int | `122` |  |
| `APPEARANCE_TYPE_MOHRG` | int | `123` |  |
| `APPEARANCE_TYPE_MUMMY_COMMON` | int | `58` |  |
| `APPEARANCE_TYPE_MUMMY_FIGHTER_2` | int | `59` |  |
| `APPEARANCE_TYPE_MUMMY_GREATER` | int | `124` |  |
| `APPEARANCE_TYPE_MUMMY_WARRIOR` | int | `125` |  |
| `APPEARANCE_TYPE_NWN_AARIN` | int | `188` |  |
| `APPEARANCE_TYPE_NWN_ARIBETH_EVIL` | int | `189` |  |
| `APPEARANCE_TYPE_NWN_HAEDRALINE` | int | `191` |  |
| `APPEARANCE_TYPE_NWN_MAUGRIM` | int | `193` |  |
| `APPEARANCE_TYPE_NWN_MORAG` | int | `192` |  |
| `APPEARANCE_TYPE_NWN_NASHER` | int | `296` |  |
| `APPEARANCE_TYPE_NWN_SEDOS` | int | `297` |  |
| `APPEARANCE_TYPE_NW_MILITIA_MEMBER` | int | `210` |  |
| `APPEARANCE_TYPE_NYMPH` | int | `126` |  |
| `APPEARANCE_TYPE_OCHRE_JELLY_LARGE` | int | `394` |  |
| `APPEARANCE_TYPE_OCHRE_JELLY_MEDIUM` | int | `396` |  |
| `APPEARANCE_TYPE_OCHRE_JELLY_SMALL` | int | `398` |  |
| `APPEARANCE_TYPE_OGRE` | int | `127` |  |
| `APPEARANCE_TYPE_OGREB` | int | `207` |  |
| `APPEARANCE_TYPE_OGRE_CHIEFTAIN` | int | `128` |  |
| `APPEARANCE_TYPE_OGRE_CHIEFTAINB` | int | `208` |  |
| `APPEARANCE_TYPE_OGRE_MAGE` | int | `129` |  |
| `APPEARANCE_TYPE_OGRE_MAGEB` | int | `209` |  |
| `APPEARANCE_TYPE_OLD_MAN` | int | `239` |  |
| `APPEARANCE_TYPE_OLD_WOMAN` | int | `240` |  |
| `APPEARANCE_TYPE_ORC_A` | int | `140` |  |
| `APPEARANCE_TYPE_ORC_B` | int | `141` |  |
| `APPEARANCE_TYPE_ORC_CHIEFTAIN_A` | int | `136` |  |
| `APPEARANCE_TYPE_ORC_CHIEFTAIN_B` | int | `137` |  |
| `APPEARANCE_TYPE_ORC_SHAMAN_A` | int | `138` |  |
| `APPEARANCE_TYPE_ORC_SHAMAN_B` | int | `139` |  |
| `APPEARANCE_TYPE_OX` | int | `142` |  |
| `APPEARANCE_TYPE_PARROT` | int | `7` |  |
| `APPEARANCE_TYPE_PENGUIN` | int | `206` |  |
| `APPEARANCE_TYPE_PLAGUE_VICTIM` | int | `231` |  |
| `APPEARANCE_TYPE_PROSTITUTE_01` | int | `236` |  |
| `APPEARANCE_TYPE_PROSTITUTE_02` | int | `237` |  |
| `APPEARANCE_TYPE_PSEUDODRAGON` | int | `375` |  |
| `APPEARANCE_TYPE_QUASIT` | int | `104` |  |
| `APPEARANCE_TYPE_RAKSHASA_BEAR_MALE` | int | `294` |  |
| `APPEARANCE_TYPE_RAKSHASA_TIGER_FEMALE` | int | `290` |  |
| `APPEARANCE_TYPE_RAKSHASA_TIGER_MALE` | int | `293` |  |
| `APPEARANCE_TYPE_RAKSHASA_WOLF_MALE` | int | `295` |  |
| `APPEARANCE_TYPE_RAT` | int | `386` |  |
| `APPEARANCE_TYPE_RAT_DIRE` | int | `387` |  |
| `APPEARANCE_TYPE_RAVEN` | int | `145` |  |
| `APPEARANCE_TYPE_SAHUAGIN` | int | `65` |  |
| `APPEARANCE_TYPE_SAHUAGIN_LEADER` | int | `66` |  |
| `APPEARANCE_TYPE_SAHUAGIN_CLERIC` | int | `67` |  |
| `APPEARANCE_TYPE_SEAGULL_FLYING` | int | `291` |  |
| `APPEARANCE_TYPE_SEAGULL_WALKING` | int | `292` |  |
| `APPEARANCE_TYPE_SHADOW` | int | `146` |  |
| `APPEARANCE_TYPE_SHADOW_FIEND` | int | `147` |  |
| `APPEARANCE_TYPE_SHARK_MAKO` | int | `447` |  |
| `APPEARANCE_TYPE_SHARK_HAMMERHEAD` | int | `448` |  |
| `APPEARANCE_TYPE_SHARK_GOBLIN` | int | `449` |  |
| `APPEARANCE_TYPE_SHIELD_GUARDIAN` | int | `90` |  |
| `APPEARANCE_TYPE_SHOP_KEEPER` | int | `232` |  |
| `APPEARANCE_TYPE_SKELETAL_DEVOURER` | int | `36` |  |
| `APPEARANCE_TYPE_SKELETON_CHIEFTAIN` | int | `182` |  |
| `APPEARANCE_TYPE_SKELETON_COMMON` | int | `63` |  |
| `APPEARANCE_TYPE_SKELETON_MAGE` | int | `148` |  |
| `APPEARANCE_TYPE_SKELETON_PRIEST` | int | `62` |  |
| `APPEARANCE_TYPE_SKELETON_WARRIOR` | int | `150` |  |
| `APPEARANCE_TYPE_SKELETON_WARRIOR_1` | int | `70` |  |
| `APPEARANCE_TYPE_SKELETON_WARRIOR_2` | int | `71` |  |
| `APPEARANCE_TYPE_SLAAD_BLUE` | int | `151` |  |
| `APPEARANCE_TYPE_SLAAD_DEATH` | int | `152` |  |
| `APPEARANCE_TYPE_SLAAD_GRAY` | int | `153` |  |
| `APPEARANCE_TYPE_SLAAD_GREEN` | int | `154` |  |
| `APPEARANCE_TYPE_SLAAD_RED` | int | `155` |  |
| `APPEARANCE_TYPE_SPECTRE` | int | `156` |  |
| `APPEARANCE_TYPE_SPHINX` | int | `364` |  |
| `APPEARANCE_TYPE_SPIDER_DIRE` | int | `158` |  |
| `APPEARANCE_TYPE_SPIDER_GIANT` | int | `159` |  |
| `APPEARANCE_TYPE_SPIDER_PHASE` | int | `160` |  |
| `APPEARANCE_TYPE_SPIDER_SWORD` | int | `161` |  |
| `APPEARANCE_TYPE_SPIDER_WRAITH` | int | `162` |  |
| `APPEARANCE_TYPE_STINGER` | int | `356` |  |
| `APPEARANCE_TYPE_STINGER_CHIEFTAIN` | int | `358` |  |
| `APPEARANCE_TYPE_STINGER_MAGE` | int | `359` |  |
| `APPEARANCE_TYPE_STINGER_WARRIOR` | int | `357` |  |
| `APPEARANCE_TYPE_SUCCUBUS` | int | `163` |  |
| `APPEARANCE_TYPE_TROGLODYTE` | int | `451` |  |
| `APPEARANCE_TYPE_TROGLODYTE_WARRIOR` | int | `452` |  |
| `APPEARANCE_TYPE_TROGLODYTE_CLERIC` | int | `453` |  |
| `APPEARANCE_TYPE_TROLL` | int | `167` |  |
| `APPEARANCE_TYPE_TROLL_CHIEFTAIN` | int | `164` |  |
| `APPEARANCE_TYPE_TROLL_SHAMAN` | int | `165` |  |
| `APPEARANCE_TYPE_UMBERHULK` | int | `168` |  |
| `APPEARANCE_TYPE_UTHGARD_ELK_TRIBE` | int | `213` |  |
| `APPEARANCE_TYPE_UTHGARD_TIGER_TRIBE` | int | `214` |  |
| `APPEARANCE_TYPE_VAMPIRE_FEMALE` | int | `288` |  |
| `APPEARANCE_TYPE_VAMPIRE_MALE` | int | `289` |  |
| `APPEARANCE_TYPE_VROCK` | int | `101` |  |
| `APPEARANCE_TYPE_WAITRESS` | int | `235` |  |
| `APPEARANCE_TYPE_WAR_DEVOURER` | int | `54` |  |
| `APPEARANCE_TYPE_WERECAT` | int | `99` |  |
| `APPEARANCE_TYPE_WERERAT` | int | `170` |  |
| `APPEARANCE_TYPE_WEREWOLF` | int | `171` |  |
| `APPEARANCE_TYPE_WIGHT` | int | `172` |  |
| `APPEARANCE_TYPE_WILL_O_WISP` | int | `116` |  |
| `APPEARANCE_TYPE_WRAITH` | int | `187` |  |
| `APPEARANCE_TYPE_WYRMLING_BLACK` | int | `378` |  |
| `APPEARANCE_TYPE_WYRMLING_BLUE` | int | `377` |  |
| `APPEARANCE_TYPE_WYRMLING_BRASS` | int | `381` |  |
| `APPEARANCE_TYPE_WYRMLING_BRONZE` | int | `383` |  |
| `APPEARANCE_TYPE_WYRMLING_COPPER` | int | `382` |  |
| `APPEARANCE_TYPE_WYRMLING_GOLD` | int | `385` |  |
| `APPEARANCE_TYPE_WYRMLING_GREEN` | int | `379` |  |
| `APPEARANCE_TYPE_WYRMLING_RED` | int | `376` |  |
| `APPEARANCE_TYPE_WYRMLING_SILVER` | int | `384` |  |
| `APPEARANCE_TYPE_WYRMLING_WHITE` | int | `380` |  |
| `APPEARANCE_TYPE_YUAN_TI` | int | `285` |  |
| `APPEARANCE_TYPE_YUAN_TI_CHIEFTEN` | int | `286` |  |
| `APPEARANCE_TYPE_YUAN_TI_WIZARD` | int | `287` |  |
| `APPEARANCE_TYPE_ZOMBIE` | int | `198` |  |
| `APPEARANCE_TYPE_ZOMBIE_ROTTING` | int | `195` |  |
| `APPEARANCE_TYPE_ZOMBIE_TYRANT_FOG` | int | `199` |  |
| `APPEARANCE_TYPE_ZOMBIE_WARRIOR_1` | int | `196` |  |
| `APPEARANCE_TYPE_ZOMBIE_WARRIOR_2` | int | `197` |  |
| `APPEARANCE_TYPE_BEHOLDER` | int | `401` |  |
| `APPEARANCE_TYPE_BEHOLDER_MAGE` | int | `402` |  |
| `APPEARANCE_TYPE_BEHOLDER_EYEBALL` | int | `403` |  |
| `APPEARANCE_TYPE_MEPHISTO_BIG` | int | `404` |  |
| `APPEARANCE_TYPE_DRACOLICH` | int | `405` |  |
| `APPEARANCE_TYPE_DRIDER` | int | `406` |  |
| `APPEARANCE_TYPE_DRIDER_CHIEF` | int | `407` |  |
| `APPEARANCE_TYPE_DROW_SLAVE` | int | `408` |  |
| `APPEARANCE_TYPE_DROW_WIZARD` | int | `409` |  |
| `APPEARANCE_TYPE_DROW_MATRON` | int | `410` |  |
| `APPEARANCE_TYPE_DUERGAR_SLAVE` | int | `411` |  |
| `APPEARANCE_TYPE_DUERGAR_CHIEF` | int | `412` |  |
| `APPEARANCE_TYPE_MINDFLAYER` | int | `413` |  |
| `APPEARANCE_TYPE_MINDFLAYER_2` | int | `414` |  |
| `APPEARANCE_TYPE_MINDFLAYER_ALHOON` | int | `415` |  |
| `APPEARANCE_TYPE_DEEP_ROTHE` | int | `416` |  |
| `APPEARANCE_TYPE_DRAGON_SHADOW` | int | `418` |  |
| `APPEARANCE_TYPE_HARPY` | int | `419` |  |
| `APPEARANCE_TYPE_GOLEM_MITHRAL` | int | `420` |  |
| `APPEARANCE_TYPE_GOLEM_ADAMANTIUM` | int | `421` |  |
| `APPEARANCE_TYPE_SPIDER_DEMON` | int | `422` |  |
| `APPEARANCE_TYPE_SVIRF_MALE` | int | `423` |  |
| `APPEARANCE_TYPE_SVIRF_FEMALE` | int | `424` |  |
| `APPEARANCE_TYPE_DRAGON_PRIS` | int | `425` |  |
| `APPEARANCE_TYPE_SLAAD_BLACK` | int | `426` |  |
| `APPEARANCE_TYPE_SLAAD_WHITE` | int | `427` |  |
| `APPEARANCE_TYPE_AZER_MALE` | int | `428` |  |
| `APPEARANCE_TYPE_AZER_FEMALE` | int | `429` |  |
| `APPEARANCE_TYPE_DEMI_LICH` | int | `430` |  |
| `APPEARANCE_TYPE_OBJECT_CHAIR` | int | `431` |  |
| `APPEARANCE_TYPE_OBJECT_TABLE` | int | `432` |  |
| `APPEARANCE_TYPE_OBJECT_CANDLE` | int | `433` |  |
| `APPEARANCE_TYPE_OBJECT_CHEST` | int | `434` |  |
| `APPEARANCE_TYPE_OBJECT_WHITE` | int | `435` |  |
| `APPEARANCE_TYPE_OBJECT_BLUE` | int | `436` |  |
| `APPEARANCE_TYPE_OBJECT_CYAN` | int | `437` |  |
| `APPEARANCE_TYPE_OBJECT_GREEN` | int | `438` |  |
| `APPEARANCE_TYPE_OBJECT_YELLOW` | int | `439` |  |
| `APPEARANCE_TYPE_OBJECT_ORANGE` | int | `440` |  |
| `APPEARANCE_TYPE_OBJECT_RED` | int | `441` |  |
| `APPEARANCE_TYPE_OBJECT_PURPLE` | int | `442` |  |
| `APPEARANCE_TYPE_OBJECT_FLAME_SMALL` | int | `443` |  |
| `APPEARANCE_TYPE_OBJECT_FLAME_MEDIUM` | int | `444` |  |
| `APPEARANCE_TYPE_OBJECT_FLAME_LARGE` | int | `445` |  |
| `APPEARANCE_TYPE_DRIDER_FEMALE` | int | `446` |  |
| `APPEARANCE_TYPE_SEA_HAG` | int | `454` |  |
| `APPEARANCE_TYPE_GOLEM_DEMONFLESH` | int | `468` |  |
| `APPEARANCE_TYPE_ANIMATED_CHEST` | int | `469` |  |
| `APPEARANCE_TYPE_GELATINOUS_CUBE` | int | `470` |  |
| `APPEARANCE_TYPE_MEPHISTO_NORM` | int | `471` |  |
| `APPEARANCE_TYPE_BEHOLDER_MOTHER` | int | `472` |  |
| `APPEARANCE_TYPE_OBJECT_BOAT` | int | `473` |  |
| `APPEARANCE_TYPE_DWARF_GOLEM` | int | `474` |  |
| `APPEARANCE_TYPE_DWARF_HALFORC` | int | `475` |  |
| `APPEARANCE_TYPE_DROW_WARRIOR_1` | int | `476` |  |
| `APPEARANCE_TYPE_DROW_WARRIOR_2` | int | `477` |  |
| `APPEARANCE_TYPE_DROW_FEMALE_1` | int | `478` |  |
| `APPEARANCE_TYPE_DROW_FEMALE_2` | int | `479` |  |
| `APPEARANCE_TYPE_DROW_WARRIOR_3` | int | `480` |  |
| `PHENOTYPE_NORMAL` | int | `0` |  |
| `PHENOTYPE_BIG` | int | `2` |  |
| `PHENOTYPE_CUSTOM1` | int | `3` |  |
| `PHENOTYPE_CUSTOM2` | int | `4` |  |
| `PHENOTYPE_CUSTOM3` | int | `5` |  |
| `PHENOTYPE_CUSTOM4` | int | `6` |  |
| `PHENOTYPE_CUSTOM5` | int | `7` |  |
| `PHENOTYPE_CUSTOM6` | int | `8` |  |
| `PHENOTYPE_CUSTOM7` | int | `9` |  |
| `PHENOTYPE_CUSTOM8` | int | `10` |  |
| `PHENOTYPE_CUSTOM9` | int | `11` |  |
| `PHENOTYPE_CUSTOM10` | int | `12` |  |
| `PHENOTYPE_CUSTOM11` | int | `13` |  |
| `PHENOTYPE_CUSTOM12` | int | `14` |  |
| `PHENOTYPE_CUSTOM13` | int | `15` |  |
| `PHENOTYPE_CUSTOM14` | int | `16` |  |
| `PHENOTYPE_CUSTOM15` | int | `17` |  |
| `PHENOTYPE_CUSTOM16` | int | `18` |  |
| `PHENOTYPE_CUSTOM17` | int | `19` |  |
| `PHENOTYPE_CUSTOM18` | int | `20` |  |
| `CAMERA_TRANSITION_TYPE_SNAP` | int | `0` |  |
| `CAMERA_TRANSITION_TYPE_CRAWL` | int | `2` |  |
| `CAMERA_TRANSITION_TYPE_VERY_SLOW` | int | `5` |  |
| `CAMERA_TRANSITION_TYPE_SLOW` | int | `20` |  |
| `CAMERA_TRANSITION_TYPE_MEDIUM` | int | `40` |  |
| `CAMERA_TRANSITION_TYPE_FAST` | int | `70` |  |
| `CAMERA_TRANSITION_TYPE_VERY_FAST` | int | `100` |  |
| `FADE_SPEED_SLOWEST` | float | `0.003` |  |
| `FADE_SPEED_SLOW` | float | `0.005` |  |
| `FADE_SPEED_MEDIUM` | float | `0.01` |  |
| `FADE_SPEED_FAST` | float | `0.017` |  |
| `FADE_SPEED_FASTEST` | float | `0.25` |  |
| `EVENT_HEARTBEAT` | int | `1001` |  |
| `EVENT_PERCEIVE` | int | `1002` |  |
| `EVENT_END_COMBAT_ROUND` | int | `1003` |  |
| `EVENT_DIALOGUE` | int | `1004` |  |
| `EVENT_ATTACKED` | int | `1005` |  |
| `EVENT_DAMAGED` | int | `1006` |  |
| `EVENT_DISTURBED` | int | `1008` |  |
| `EVENT_SPELL_CAST_AT` | int | `1011` |  |
| `AI_LEVEL_INVALID` | int | `-1` |  |
| `AI_LEVEL_DEFAULT` | int | `-1` |  |
| `AI_LEVEL_VERY_LOW` | int | `0` |  |
| `AI_LEVEL_LOW` | int | `1` |  |
| `AI_LEVEL_NORMAL` | int | `2` |  |
| `AI_LEVEL_HIGH` | int | `3` |  |
| `AI_LEVEL_VERY_HIGH` | int | `4` |  |
| `AREA_INVALID` | int | `-1` |  |
| `AREA_NATURAL` | int | `1` |  |
| `AREA_ARTIFICIAL` | int | `0` |  |
| `AREA_ABOVEGROUND` | int | `1` |  |
| `AREA_UNDERGROUND` | int | `0` |  |
| `AREA_HEIGHT` | int | `0` |  |
| `AREA_WIDTH` | int | `1` |  |
| `PORTRAIT_INVALID` | int | `65535` |  |
| `USE_CREATURE_LEVEL` | int | `0` |  |
| `IP_CONST_ABILITY_STR` | int | `0` |  |
| `IP_CONST_ABILITY_DEX` | int | `1` |  |
| `IP_CONST_ABILITY_CON` | int | `2` |  |
| `IP_CONST_ABILITY_INT` | int | `3` |  |
| `IP_CONST_ABILITY_WIS` | int | `4` |  |
| `IP_CONST_ABILITY_CHA` | int | `5` |  |
| `IP_CONST_ACMODIFIERTYPE_DODGE` | int | `0` |  |
| `IP_CONST_ACMODIFIERTYPE_NATURAL` | int | `1` |  |
| `IP_CONST_ACMODIFIERTYPE_ARMOR` | int | `2` |  |
| `IP_CONST_ACMODIFIERTYPE_SHIELD` | int | `3` |  |
| `IP_CONST_ACMODIFIERTYPE_DEFLECTION` | int | `4` |  |
| `IP_CONST_ADDITIONAL_UNKNOWN` | int | `0` |  |
| `IP_CONST_ADDITIONAL_CURSED` | int | `1` |  |
| `IP_CONST_ALIGNMENTGROUP_ALL` | int | `0` |  |
| `IP_CONST_ALIGNMENTGROUP_NEUTRAL` | int | `1` |  |
| `IP_CONST_ALIGNMENTGROUP_LAWFUL` | int | `2` |  |
| `IP_CONST_ALIGNMENTGROUP_CHAOTIC` | int | `3` |  |
| `IP_CONST_ALIGNMENTGROUP_GOOD` | int | `4` |  |
| `IP_CONST_ALIGNMENTGROUP_EVIL` | int | `5` |  |
| `IP_CONST_ALIGNMENT_LG` | int | `0` |  |
| `IP_CONST_ALIGNMENT_LN` | int | `1` |  |
| `IP_CONST_ALIGNMENT_LE` | int | `2` |  |
| `IP_CONST_ALIGNMENT_NG` | int | `3` |  |
| `IP_CONST_ALIGNMENT_TN` | int | `4` |  |
| `IP_CONST_ALIGNMENT_NE` | int | `5` |  |
| `IP_CONST_ALIGNMENT_CG` | int | `6` |  |
| `IP_CONST_ALIGNMENT_CN` | int | `7` |  |
| `IP_CONST_ALIGNMENT_CE` | int | `8` |  |
| `IP_CONST_RACIALTYPE_DWARF` | int | `0` |  |
| `IP_CONST_RACIALTYPE_ELF` | int | `1` |  |
| `IP_CONST_RACIALTYPE_GNOME` | int | `2` |  |
| `IP_CONST_RACIALTYPE_HALFLING` | int | `3` |  |
| `IP_CONST_RACIALTYPE_HALFELF` | int | `4` |  |
| `IP_CONST_RACIALTYPE_HALFORC` | int | `5` |  |
| `IP_CONST_RACIALTYPE_HUMAN` | int | `6` |  |
| `IP_CONST_RACIALTYPE_ABERRATION` | int | `7` |  |
| `IP_CONST_RACIALTYPE_ANIMAL` | int | `8` |  |
| `IP_CONST_RACIALTYPE_BEAST` | int | `9` |  |
| `IP_CONST_RACIALTYPE_CONSTRUCT` | int | `10` |  |
| `IP_CONST_RACIALTYPE_DRAGON` | int | `11` |  |
| `IP_CONST_RACIALTYPE_HUMANOID_GOBLINOID` | int | `12` |  |
| `IP_CONST_RACIALTYPE_HUMANOID_MONSTROUS` | int | `13` |  |
| `IP_CONST_RACIALTYPE_HUMANOID_ORC` | int | `14` |  |
| `IP_CONST_RACIALTYPE_HUMANOID_REPTILIAN` | int | `15` |  |
| `IP_CONST_RACIALTYPE_ELEMENTAL` | int | `16` |  |
| `IP_CONST_RACIALTYPE_FEY` | int | `17` |  |
| `IP_CONST_RACIALTYPE_GIANT` | int | `18` |  |
| `IP_CONST_RACIALTYPE_MAGICAL_BEAST` | int | `19` |  |
| `IP_CONST_RACIALTYPE_OUTSIDER` | int | `20` |  |
| `IP_CONST_RACIALTYPE_SHAPECHANGER` | int | `23` |  |
| `IP_CONST_RACIALTYPE_UNDEAD` | int | `24` |  |
| `IP_CONST_RACIALTYPE_VERMIN` | int | `25` |  |
| `IP_CONST_UNLIMITEDAMMO_BASIC` | int | `1` |  |
| `IP_CONST_UNLIMITEDAMMO_1D6FIRE` | int | `2` |  |
| `IP_CONST_UNLIMITEDAMMO_1D6COLD` | int | `3` |  |
| `IP_CONST_UNLIMITEDAMMO_1D6LIGHT` | int | `4` |  |
| `IP_CONST_UNLIMITEDAMMO_PLUS1` | int | `11` |  |
| `IP_CONST_UNLIMITEDAMMO_PLUS2` | int | `12` |  |
| `IP_CONST_UNLIMITEDAMMO_PLUS3` | int | `13` |  |
| `IP_CONST_UNLIMITEDAMMO_PLUS4` | int | `14` |  |
| `IP_CONST_UNLIMITEDAMMO_PLUS5` | int | `15` |  |
| `IP_CONST_AMMOTYPE_ARROW` | int | `0` |  |
| `IP_CONST_AMMOTYPE_BOLT` | int | `1` |  |
| `IP_CONST_AMMOTYPE_BULLET` | int | `2` |  |
| `IP_CONST_CASTSPELL_NUMUSES_SINGLE_USE` | int | `1` |  |
| `IP_CONST_CASTSPELL_NUMUSES_5_CHARGES_PER_USE` | int | `2` |  |
| `IP_CONST_CASTSPELL_NUMUSES_4_CHARGES_PER_USE` | int | `3` |  |
| `IP_CONST_CASTSPELL_NUMUSES_3_CHARGES_PER_USE` | int | `4` |  |
| `IP_CONST_CASTSPELL_NUMUSES_2_CHARGES_PER_USE` | int | `5` |  |
| `IP_CONST_CASTSPELL_NUMUSES_1_CHARGE_PER_USE` | int | `6` |  |
| `IP_CONST_CASTSPELL_NUMUSES_0_CHARGES_PER_USE` | int | `7` |  |
| `IP_CONST_CASTSPELL_NUMUSES_1_USE_PER_DAY` | int | `8` |  |
| `IP_CONST_CASTSPELL_NUMUSES_2_USES_PER_DAY` | int | `9` |  |
| `IP_CONST_CASTSPELL_NUMUSES_3_USES_PER_DAY` | int | `10` |  |
| `IP_CONST_CASTSPELL_NUMUSES_4_USES_PER_DAY` | int | `11` |  |
| `IP_CONST_CASTSPELL_NUMUSES_5_USES_PER_DAY` | int | `12` |  |
| `IP_CONST_CASTSPELL_NUMUSES_UNLIMITED_USE` | int | `13` |  |
| `IP_CONST_DAMAGEBONUS_1` | int | `1` |  |
| `IP_CONST_DAMAGEBONUS_2` | int | `2` |  |
| `IP_CONST_DAMAGEBONUS_3` | int | `3` |  |
| `IP_CONST_DAMAGEBONUS_4` | int | `4` |  |
| `IP_CONST_DAMAGEBONUS_5` | int | `5` |  |
| `IP_CONST_DAMAGEBONUS_1d4` | int | `6` |  |
| `IP_CONST_DAMAGEBONUS_1d6` | int | `7` |  |
| `IP_CONST_DAMAGEBONUS_1d8` | int | `8` |  |
| `IP_CONST_DAMAGEBONUS_1d10` | int | `9` |  |
| `IP_CONST_DAMAGEBONUS_2d6` | int | `10` |  |
| `IP_CONST_DAMAGEBONUS_2d8` | int | `11` |  |
| `IP_CONST_DAMAGEBONUS_2d4` | int | `12` |  |
| `IP_CONST_DAMAGEBONUS_2d10` | int | `13` |  |
| `IP_CONST_DAMAGEBONUS_1d12` | int | `14` |  |
| `IP_CONST_DAMAGEBONUS_2d12` | int | `15` |  |
| `IP_CONST_DAMAGEBONUS_6` | int | `16` |  |
| `IP_CONST_DAMAGEBONUS_7` | int | `17` |  |
| `IP_CONST_DAMAGEBONUS_8` | int | `18` |  |
| `IP_CONST_DAMAGEBONUS_9` | int | `19` |  |
| `IP_CONST_DAMAGEBONUS_10` | int | `20` |  |
| `IP_CONST_DAMAGETYPE_BLUDGEONING` | int | `0` |  |
| `IP_CONST_DAMAGETYPE_PIERCING` | int | `1` |  |
| `IP_CONST_DAMAGETYPE_SLASHING` | int | `2` |  |
| `IP_CONST_DAMAGETYPE_SUBDUAL` | int | `3` |  |
| `IP_CONST_DAMAGETYPE_PHYSICAL` | int | `4` |  |
| `IP_CONST_DAMAGETYPE_MAGICAL` | int | `5` |  |
| `IP_CONST_DAMAGETYPE_ACID` | int | `6` |  |
| `IP_CONST_DAMAGETYPE_COLD` | int | `7` |  |
| `IP_CONST_DAMAGETYPE_DIVINE` | int | `8` |  |
| `IP_CONST_DAMAGETYPE_ELECTRICAL` | int | `9` |  |
| `IP_CONST_DAMAGETYPE_FIRE` | int | `10` |  |
| `IP_CONST_DAMAGETYPE_NEGATIVE` | int | `11` |  |
| `IP_CONST_DAMAGETYPE_POSITIVE` | int | `12` |  |
| `IP_CONST_DAMAGETYPE_SONIC` | int | `13` |  |
| `IP_CONST_DAMAGEIMMUNITY_5_PERCENT` | int | `1` |  |
| `IP_CONST_DAMAGEIMMUNITY_10_PERCENT` | int | `2` |  |
| `IP_CONST_DAMAGEIMMUNITY_25_PERCENT` | int | `3` |  |
| `IP_CONST_DAMAGEIMMUNITY_50_PERCENT` | int | `4` |  |
| `IP_CONST_DAMAGEIMMUNITY_75_PERCENT` | int | `5` |  |
| `IP_CONST_DAMAGEIMMUNITY_90_PERCENT` | int | `6` |  |
| `IP_CONST_DAMAGEIMMUNITY_100_PERCENT` | int | `7` |  |
| `IP_CONST_DAMAGEVULNERABILITY_5_PERCENT` | int | `1` |  |
| `IP_CONST_DAMAGEVULNERABILITY_10_PERCENT` | int | `2` |  |
| `IP_CONST_DAMAGEVULNERABILITY_25_PERCENT` | int | `3` |  |
| `IP_CONST_DAMAGEVULNERABILITY_50_PERCENT` | int | `4` |  |
| `IP_CONST_DAMAGEVULNERABILITY_75_PERCENT` | int | `5` |  |
| `IP_CONST_DAMAGEVULNERABILITY_90_PERCENT` | int | `6` |  |
| `IP_CONST_DAMAGEVULNERABILITY_100_PERCENT` | int | `7` |  |
| `IP_CONST_FEAT_ALERTNESS` | int | `0` |  |
| `IP_CONST_FEAT_AMBIDEXTROUS` | int | `1` |  |
| `IP_CONST_FEAT_CLEAVE` | int | `2` |  |
| `IP_CONST_FEAT_COMBAT_CASTING` | int | `3` |  |
| `IP_CONST_FEAT_DODGE` | int | `4` |  |
| `IP_CONST_FEAT_EXTRA_TURNING` | int | `5` |  |
| `IP_CONST_FEAT_KNOCKDOWN` | int | `6` |  |
| `IP_CONST_FEAT_POINTBLANK` | int | `7` |  |
| `IP_CONST_FEAT_SPELLFOCUSABJ` | int | `8` |  |
| `IP_CONST_FEAT_SPELLFOCUSCON` | int | `9` |  |
| `IP_CONST_FEAT_SPELLFOCUSDIV` | int | `10` |  |
| `IP_CONST_FEAT_SPELLFOCUSENC` | int | `11` |  |
| `IP_CONST_FEAT_SPELLFOCUSEVO` | int | `12` |  |
| `IP_CONST_FEAT_SPELLFOCUSILL` | int | `13` |  |
| `IP_CONST_FEAT_SPELLFOCUSNEC` | int | `14` |  |
| `IP_CONST_FEAT_SPELLPENETRATION` | int | `15` |  |
| `IP_CONST_FEAT_POWERATTACK` | int | `16` |  |
| `IP_CONST_FEAT_TWO_WEAPON_FIGHTING` | int | `17` |  |
| `IP_CONST_FEAT_WEAPSPEUNARM` | int | `18` |  |
| `IP_CONST_FEAT_WEAPFINESSE` | int | `19` |  |
| `IP_CONST_FEAT_IMPCRITUNARM` | int | `20` |  |
| `IP_CONST_FEAT_WEAPON_PROF_EXOTIC` | int | `21` |  |
| `IP_CONST_FEAT_WEAPON_PROF_MARTIAL` | int | `22` |  |
| `IP_CONST_FEAT_WEAPON_PROF_SIMPLE` | int | `23` |  |
| `IP_CONST_FEAT_ARMOR_PROF_HEAVY` | int | `24` |  |
| `IP_CONST_FEAT_ARMOR_PROF_LIGHT` | int | `25` |  |
| `IP_CONST_FEAT_ARMOR_PROF_MEDIUM` | int | `26` |  |
| `IP_CONST_FEAT_MOBILITY` | int | `27` |  |
| `IP_CONST_FEAT_DISARM` | int | `28` |  |
| `IP_CONST_FEAT_WHIRLWIND` | int | `29` |  |
| `IP_CONST_FEAT_RAPID_SHOT` | int | `30` |  |
| `IP_CONST_FEAT_HIDE_IN_PLAIN_SIGHT` | int | `31` |  |
| `IP_CONST_FEAT_SNEAK_ATTACK_1D6` | int | `32` |  |
| `IP_CONST_FEAT_SNEAK_ATTACK_2D6` | int | `33` |  |
| `IP_CONST_FEAT_SNEAK_ATTACK_3D6` | int | `34` |  |
| `IP_CONST_FEAT_SHIELD_PROFICIENCY` | int | `35` |  |
| `IP_CONST_FEAT_USE_POISON` | int | `36` |  |
| `IP_CONST_FEAT_DISARM_WHIP` | int | `37` |  |
| `IP_CONST_FEAT_WEAPON_PROF_CREATURE` | int | `38` |  |
| `IP_CONST_FEAT_SNEAK_ATTACK_5D6` | int | `39` |  |
| `IP_CONST_FEAT_PLAYER_TOOL_01` | int | `53` |  |
| `IP_CONST_FEAT_PLAYER_TOOL_02` | int | `54` |  |
| `IP_CONST_FEAT_PLAYER_TOOL_03` | int | `55` |  |
| `IP_CONST_FEAT_PLAYER_TOOL_04` | int | `56` |  |
| `IP_CONST_FEAT_PLAYER_TOOL_05` | int | `57` |  |
| `IP_CONST_FEAT_PLAYER_TOOL_06` | int | `58` |  |
| `IP_CONST_FEAT_PLAYER_TOOL_07` | int | `59` |  |
| `IP_CONST_FEAT_PLAYER_TOOL_08` | int | `60` |  |
| `IP_CONST_FEAT_PLAYER_TOOL_09` | int | `61` |  |
| `IP_CONST_FEAT_PLAYER_TOOL_10` | int | `62` |  |
| `IP_CONST_IMMUNITYMISC_BACKSTAB` | int | `0` |  |
| `IP_CONST_IMMUNITYMISC_LEVEL_ABIL_DRAIN` | int | `1` |  |
| `IP_CONST_IMMUNITYMISC_MINDSPELLS` | int | `2` |  |
| `IP_CONST_IMMUNITYMISC_POISON` | int | `3` |  |
| `IP_CONST_IMMUNITYMISC_DISEASE` | int | `4` |  |
| `IP_CONST_IMMUNITYMISC_FEAR` | int | `5` |  |
| `IP_CONST_IMMUNITYMISC_KNOCKDOWN` | int | `6` |  |
| `IP_CONST_IMMUNITYMISC_PARALYSIS` | int | `7` |  |
| `IP_CONST_IMMUNITYMISC_CRITICAL_HITS` | int | `8` |  |
| `IP_CONST_IMMUNITYMISC_DEATH_MAGIC` | int | `9` |  |
| `IP_CONST_LIGHTBRIGHTNESS_DIM` | int | `1` |  |
| `IP_CONST_LIGHTBRIGHTNESS_LOW` | int | `2` |  |
| `IP_CONST_LIGHTBRIGHTNESS_NORMAL` | int | `3` |  |
| `IP_CONST_LIGHTBRIGHTNESS_BRIGHT` | int | `4` |  |
| `IP_CONST_LIGHTCOLOR_BLUE` | int | `0` |  |
| `IP_CONST_LIGHTCOLOR_YELLOW` | int | `1` |  |
| `IP_CONST_LIGHTCOLOR_PURPLE` | int | `2` |  |
| `IP_CONST_LIGHTCOLOR_RED` | int | `3` |  |
| `IP_CONST_LIGHTCOLOR_GREEN` | int | `4` |  |
| `IP_CONST_LIGHTCOLOR_ORANGE` | int | `5` |  |
| `IP_CONST_LIGHTCOLOR_WHITE` | int | `6` |  |
| `IP_CONST_MONSTERDAMAGE_1d2` | int | `1` |  |
| `IP_CONST_MONSTERDAMAGE_1d3` | int | `2` |  |
| `IP_CONST_MONSTERDAMAGE_1d4` | int | `3` |  |
| `IP_CONST_MONSTERDAMAGE_2d4` | int | `4` |  |
| `IP_CONST_MONSTERDAMAGE_3d4` | int | `5` |  |
| `IP_CONST_MONSTERDAMAGE_4d4` | int | `6` |  |
| `IP_CONST_MONSTERDAMAGE_5d4` | int | `7` |  |
| `IP_CONST_MONSTERDAMAGE_1d6` | int | `8` |  |
| `IP_CONST_MONSTERDAMAGE_2d6` | int | `9` |  |
| `IP_CONST_MONSTERDAMAGE_3d6` | int | `10` |  |
| `IP_CONST_MONSTERDAMAGE_4d6` | int | `11` |  |
| `IP_CONST_MONSTERDAMAGE_5d6` | int | `12` |  |
| `IP_CONST_MONSTERDAMAGE_6d6` | int | `13` |  |
| `IP_CONST_MONSTERDAMAGE_7d6` | int | `14` |  |
| `IP_CONST_MONSTERDAMAGE_8d6` | int | `15` |  |
| `IP_CONST_MONSTERDAMAGE_9d6` | int | `16` |  |
| `IP_CONST_MONSTERDAMAGE_10d6` | int | `17` |  |
| `IP_CONST_MONSTERDAMAGE_1d8` | int | `18` |  |
| `IP_CONST_MONSTERDAMAGE_2d8` | int | `19` |  |
| `IP_CONST_MONSTERDAMAGE_3d8` | int | `20` |  |
| `IP_CONST_MONSTERDAMAGE_4d8` | int | `21` |  |
| `IP_CONST_MONSTERDAMAGE_5d8` | int | `22` |  |
| `IP_CONST_MONSTERDAMAGE_6d8` | int | `23` |  |
| `IP_CONST_MONSTERDAMAGE_7d8` | int | `24` |  |
| `IP_CONST_MONSTERDAMAGE_8d8` | int | `25` |  |
| `IP_CONST_MONSTERDAMAGE_9d8` | int | `26` |  |
| `IP_CONST_MONSTERDAMAGE_10d8` | int | `27` |  |
| `IP_CONST_MONSTERDAMAGE_1d10` | int | `28` |  |
| `IP_CONST_MONSTERDAMAGE_2d10` | int | `29` |  |
| `IP_CONST_MONSTERDAMAGE_3d10` | int | `30` |  |
| `IP_CONST_MONSTERDAMAGE_4d10` | int | `31` |  |
| `IP_CONST_MONSTERDAMAGE_5d10` | int | `32` |  |
| `IP_CONST_MONSTERDAMAGE_6d10` | int | `33` |  |
| `IP_CONST_MONSTERDAMAGE_7d10` | int | `34` |  |
| `IP_CONST_MONSTERDAMAGE_8d10` | int | `35` |  |
| `IP_CONST_MONSTERDAMAGE_9d10` | int | `36` |  |
| `IP_CONST_MONSTERDAMAGE_10d10` | int | `37` |  |
| `IP_CONST_MONSTERDAMAGE_1d12` | int | `38` |  |
| `IP_CONST_MONSTERDAMAGE_2d12` | int | `39` |  |
| `IP_CONST_MONSTERDAMAGE_3d12` | int | `40` |  |
| `IP_CONST_MONSTERDAMAGE_4d12` | int | `41` |  |
| `IP_CONST_MONSTERDAMAGE_5d12` | int | `42` |  |
| `IP_CONST_MONSTERDAMAGE_6d12` | int | `43` |  |
| `IP_CONST_MONSTERDAMAGE_7d12` | int | `44` |  |
| `IP_CONST_MONSTERDAMAGE_8d12` | int | `45` |  |
| `IP_CONST_MONSTERDAMAGE_9d12` | int | `46` |  |
| `IP_CONST_MONSTERDAMAGE_10d12` | int | `47` |  |
| `IP_CONST_MONSTERDAMAGE_1d20` | int | `48` |  |
| `IP_CONST_MONSTERDAMAGE_2d20` | int | `49` |  |
| `IP_CONST_MONSTERDAMAGE_3d20` | int | `50` |  |
| `IP_CONST_MONSTERDAMAGE_4d20` | int | `51` |  |
| `IP_CONST_MONSTERDAMAGE_5d20` | int | `52` |  |
| `IP_CONST_MONSTERDAMAGE_6d20` | int | `53` |  |
| `IP_CONST_MONSTERDAMAGE_7d20` | int | `54` |  |
| `IP_CONST_MONSTERDAMAGE_8d20` | int | `55` |  |
| `IP_CONST_MONSTERDAMAGE_9d20` | int | `56` |  |
| `IP_CONST_MONSTERDAMAGE_10d20` | int | `57` |  |
| `IP_CONST_ONMONSTERHIT_ABILITYDRAIN` | int | `0` |  |
| `IP_CONST_ONMONSTERHIT_CONFUSION` | int | `1` |  |
| `IP_CONST_ONMONSTERHIT_DISEASE` | int | `2` |  |
| `IP_CONST_ONMONSTERHIT_DOOM` | int | `3` |  |
| `IP_CONST_ONMONSTERHIT_FEAR` | int | `4` |  |
| `IP_CONST_ONMONSTERHIT_LEVELDRAIN` | int | `5` |  |
| `IP_CONST_ONMONSTERHIT_POISON` | int | `6` |  |
| `IP_CONST_ONMONSTERHIT_SLOW` | int | `7` |  |
| `IP_CONST_ONMONSTERHIT_STUN` | int | `8` |  |
| `IP_CONST_ONMONSTERHIT_WOUNDING` | int | `9` |  |
| `IP_CONST_ONHIT_SLEEP` | int | `0` |  |
| `IP_CONST_ONHIT_STUN` | int | `1` |  |
| `IP_CONST_ONHIT_HOLD` | int | `2` |  |
| `IP_CONST_ONHIT_CONFUSION` | int | `3` |  |
| `IP_CONST_ONHIT_DAZE` | int | `5` |  |
| `IP_CONST_ONHIT_DOOM` | int | `6` |  |
| `IP_CONST_ONHIT_FEAR` | int | `7` |  |
| `IP_CONST_ONHIT_KNOCK` | int | `8` |  |
| `IP_CONST_ONHIT_SLOW` | int | `9` |  |
| `IP_CONST_ONHIT_LESSERDISPEL` | int | `10` |  |
| `IP_CONST_ONHIT_DISPELMAGIC` | int | `11` |  |
| `IP_CONST_ONHIT_GREATERDISPEL` | int | `12` |  |
| `IP_CONST_ONHIT_MORDSDISJUNCTION` | int | `13` |  |
| `IP_CONST_ONHIT_SILENCE` | int | `14` |  |
| `IP_CONST_ONHIT_DEAFNESS` | int | `15` |  |
| `IP_CONST_ONHIT_BLINDNESS` | int | `16` |  |
| `IP_CONST_ONHIT_LEVELDRAIN` | int | `17` |  |
| `IP_CONST_ONHIT_ABILITYDRAIN` | int | `18` |  |
| `IP_CONST_ONHIT_ITEMPOISON` | int | `19` |  |
| `IP_CONST_ONHIT_DISEASE` | int | `20` |  |
| `IP_CONST_ONHIT_SLAYRACE` | int | `21` |  |
| `IP_CONST_ONHIT_SLAYALIGNMENTGROUP` | int | `22` |  |
| `IP_CONST_ONHIT_SLAYALIGNMENT` | int | `23` |  |
| `IP_CONST_ONHIT_VORPAL` | int | `24` |  |
| `IP_CONST_ONHIT_WOUNDING` | int | `25` |  |
| `IP_CONST_ONHIT_SAVEDC_14` | int | `0` |  |
| `IP_CONST_ONHIT_SAVEDC_16` | int | `1` |  |
| `IP_CONST_ONHIT_SAVEDC_18` | int | `2` |  |
| `IP_CONST_ONHIT_SAVEDC_20` | int | `3` |  |
| `IP_CONST_ONHIT_SAVEDC_22` | int | `4` |  |
| `IP_CONST_ONHIT_SAVEDC_24` | int | `5` |  |
| `IP_CONST_ONHIT_SAVEDC_26` | int | `6` |  |
| `IP_CONST_ONHIT_DURATION_5_PERCENT_5_ROUNDS` | int | `0` |  |
| `IP_CONST_ONHIT_DURATION_10_PERCENT_4_ROUNDS` | int | `1` |  |
| `IP_CONST_ONHIT_DURATION_25_PERCENT_3_ROUNDS` | int | `2` |  |
| `IP_CONST_ONHIT_DURATION_50_PERCENT_2_ROUNDS` | int | `3` |  |
| `IP_CONST_ONHIT_DURATION_75_PERCENT_1_ROUND` | int | `4` |  |
| `IP_CONST_ONHIT_CASTSPELL_ACID_FOG` | int | `0` |  |
| `IP_CONST_ONHIT_CASTSPELL_BESTOW_CURSE` | int | `1` |  |
| `IP_CONST_ONHIT_CASTSPELL_BLADE_BARRIER` | int | `2` |  |
| `IP_CONST_ONHIT_CASTSPELL_BLINDNESS_AND_DEAFNESS` | int | `3` |  |
| `IP_CONST_ONHIT_CASTSPELL_CALL_LIGHTNING` | int | `4` |  |
| `IP_CONST_ONHIT_CASTSPELL_CHAIN_LIGHTNING` | int | `5` |  |
| `IP_CONST_ONHIT_CASTSPELL_CLOUDKILL` | int | `6` |  |
| `IP_CONST_ONHIT_CASTSPELL_CONFUSION` | int | `7` |  |
| `IP_CONST_ONHIT_CASTSPELL_CONTAGION` | int | `8` |  |
| `IP_CONST_ONHIT_CASTSPELL_DARKNESS` | int | `9` |  |
| `IP_CONST_ONHIT_CASTSPELL_DAZE` | int | `10` |  |
| `IP_CONST_ONHIT_CASTSPELL_DELAYED_BLAST_FIREBALL` | int | `11` |  |
| `IP_CONST_ONHIT_CASTSPELL_DISMISSAL` | int | `12` |  |
| `IP_CONST_ONHIT_CASTSPELL_DISPEL_MAGIC` | int | `13` |  |
| `IP_CONST_ONHIT_CASTSPELL_DOOM` | int | `14` |  |
| `IP_CONST_ONHIT_CASTSPELL_ENERGY_DRAIN` | int | `15` |  |
| `IP_CONST_ONHIT_CASTSPELL_ENERVATION` | int | `16` |  |
| `IP_CONST_ONHIT_CASTSPELL_ENTANGLE` | int | `17` |  |
| `IP_CONST_ONHIT_CASTSPELL_FEAR` | int | `18` |  |
| `IP_CONST_ONHIT_CASTSPELL_FEEBLEMIND` | int | `19` |  |
| `IP_CONST_ONHIT_CASTSPELL_FIRE_STORM` | int | `20` |  |
| `IP_CONST_ONHIT_CASTSPELL_FIREBALL` | int | `21` |  |
| `IP_CONST_ONHIT_CASTSPELL_FLAME_LASH` | int | `22` |  |
| `IP_CONST_ONHIT_CASTSPELL_FLAME_STRIKE` | int | `23` |  |
| `IP_CONST_ONHIT_CASTSPELL_GHOUL_TOUCH` | int | `24` |  |
| `IP_CONST_ONHIT_CASTSPELL_GREASE` | int | `25` |  |
| `IP_CONST_ONHIT_CASTSPELL_GREATER_DISPELLING` | int | `26` |  |
| `IP_CONST_ONHIT_CASTSPELL_GREATER_SPELL_BREACH` | int | `27` |  |
| `IP_CONST_ONHIT_CASTSPELL_GUST_OF_WIND` | int | `28` |  |
| `IP_CONST_ONHIT_CASTSPELL_HAMMER_OF_THE_GODS` | int | `29` |  |
| `IP_CONST_ONHIT_CASTSPELL_HARM` | int | `30` |  |
| `IP_CONST_ONHIT_CASTSPELL_HOLD_ANIMAL` | int | `31` |  |
| `IP_CONST_ONHIT_CASTSPELL_HOLD_MONSTER` | int | `32` |  |
| `IP_CONST_ONHIT_CASTSPELL_HOLD_PERSON` | int | `33` |  |
| `IP_CONST_ONHIT_CASTSPELL_IMPLOSION` | int | `34` |  |
| `IP_CONST_ONHIT_CASTSPELL_INCENDIARY_CLOUD` | int | `35` |  |
| `IP_CONST_ONHIT_CASTSPELL_LESSER_DISPEL` | int | `36` |  |
| `IP_CONST_ONHIT_CASTSPELL_LESSER_SPELL_BREACH` | int | `38` |  |
| `IP_CONST_ONHIT_CASTSPELL_LIGHT` | int | `40` |  |
| `IP_CONST_ONHIT_CASTSPELL_LIGHTNING_BOLT` | int | `41` |  |
| `IP_CONST_ONHIT_CASTSPELL_MAGIC_MISSILE` | int | `42` |  |
| `IP_CONST_ONHIT_CASTSPELL_MASS_BLINDNESS_AND_DEAFNESS` | int | `43` |  |
| `IP_CONST_ONHIT_CASTSPELL_MASS_CHARM` | int | `44` |  |
| `IP_CONST_ONHIT_CASTSPELL_MELFS_ACID_ARROW` | int | `45` |  |
| `IP_CONST_ONHIT_CASTSPELL_METEOR_SWARM` | int | `46` |  |
| `IP_CONST_ONHIT_CASTSPELL_MIND_FOG` | int | `47` |  |
| `IP_CONST_ONHIT_CASTSPELL_PHANTASMAL_KILLER` | int | `49` |  |
| `IP_CONST_ONHIT_CASTSPELL_POISON` | int | `50` |  |
| `IP_CONST_ONHIT_CASTSPELL_POWER_WORD_KILL` | int | `51` |  |
| `IP_CONST_ONHIT_CASTSPELL_POWER_WORD_STUN` | int | `52` |  |
| `IP_CONST_ONHIT_CASTSPELL_SCARE` | int | `54` |  |
| `IP_CONST_ONHIT_CASTSPELL_SEARING_LIGHT` | int | `55` |  |
| `IP_CONST_ONHIT_CASTSPELL_SILENCE` | int | `56` |  |
| `IP_CONST_ONHIT_CASTSPELL_SLAY_LIVING` | int | `57` |  |
| `IP_CONST_ONHIT_CASTSPELL_SLEEP` | int | `58` |  |
| `IP_CONST_ONHIT_CASTSPELL_SLOW` | int | `59` |  |
| `IP_CONST_ONHIT_CASTSPELL_SOUND_BURST` | int | `60` |  |
| `IP_CONST_ONHIT_CASTSPELL_STINKING_CLOUD` | int | `61` |  |
| `IP_CONST_ONHIT_CASTSPELL_STORM_OF_VENGEANCE` | int | `63` |  |
| `IP_CONST_ONHIT_CASTSPELL_SUNBEAM` | int | `64` |  |
| `IP_CONST_ONHIT_CASTSPELL_VAMPIRIC_TOUCH` | int | `65` |  |
| `IP_CONST_ONHIT_CASTSPELL_WAIL_OF_THE_BANSHEE` | int | `66` |  |
| `IP_CONST_ONHIT_CASTSPELL_WALL_OF_FIRE` | int | `67` |  |
| `IP_CONST_ONHIT_CASTSPELL_WEB` | int | `68` |  |
| `IP_CONST_ONHIT_CASTSPELL_WEIRD` | int | `69` |  |
| `IP_CONST_ONHIT_CASTSPELL_WORD_OF_FAITH` | int | `70` |  |
| `IP_CONST_ONHIT_CASTSPELL_CREEPING_DOOM` | int | `72` |  |
| `IP_CONST_ONHIT_CASTSPELL_DESTRUCTION` | int | `73` |  |
| `IP_CONST_ONHIT_CASTSPELL_HORRID_WILTING` | int | `74` |  |
| `IP_CONST_ONHIT_CASTSPELL_ICE_STORM` | int | `75` |  |
| `IP_CONST_ONHIT_CASTSPELL_NEGATIVE_ENERGY_BURST` | int | `76` |  |
| `IP_CONST_ONHIT_CASTSPELL_EVARDS_BLACK_TENTACLES` | int | `77` |  |
| `IP_CONST_ONHIT_CASTSPELL_ACTIVATE_ITEM` | int | `78` |  |
| `IP_CONST_ONHIT_CASTSPELL_FLARE` | int | `79` |  |
| `IP_CONST_ONHIT_CASTSPELL_BOMBARDMENT` | int | `80` |  |
| `IP_CONST_ONHIT_CASTSPELL_ACID_SPLASH` | int | `81` |  |
| `IP_CONST_ONHIT_CASTSPELL_QUILLFIRE` | int | `82` |  |
| `IP_CONST_ONHIT_CASTSPELL_EARTHQUAKE` | int | `83` |  |
| `IP_CONST_ONHIT_CASTSPELL_SUNBURST` | int | `84` |  |
| `IP_CONST_ONHIT_CASTSPELL_BANISHMENT` | int | `85` |  |
| `IP_CONST_ONHIT_CASTSPELL_INFLICT_MINOR_WOUNDS` | int | `86` |  |
| `IP_CONST_ONHIT_CASTSPELL_INFLICT_LIGHT_WOUNDS` | int | `87` |  |
| `IP_CONST_ONHIT_CASTSPELL_INFLICT_MODERATE_WOUNDS` | int | `88` |  |
| `IP_CONST_ONHIT_CASTSPELL_INFLICT_SERIOUS_WOUNDS` | int | `89` |  |
| `IP_CONST_ONHIT_CASTSPELL_INFLICT_CRITICAL_WOUNDS` | int | `90` |  |
| `IP_CONST_ONHIT_CASTSPELL_BALAGARNSIRONHORN` | int | `91` |  |
| `IP_CONST_ONHIT_CASTSPELL_DROWN` | int | `92` |  |
| `IP_CONST_ONHIT_CASTSPELL_ELECTRIC_JOLT` | int | `93` |  |
| `IP_CONST_ONHIT_CASTSPELL_FIREBRAND` | int | `94` |  |
| `IP_CONST_ONHIT_CASTSPELL_WOUNDING_WHISPERS` | int | `95` |  |
| `IP_CONST_ONHIT_CASTSPELL_UNDEATHS_ETERNAL_FOE` | int | `96` |  |
| `IP_CONST_ONHIT_CASTSPELL_INFERNO` | int | `97` |  |
| `IP_CONST_ONHIT_CASTSPELL_ISAACS_LESSER_MISSILE_STORM` | int | `98` |  |
| `IP_CONST_ONHIT_CASTSPELL_ISAACS_GREATER_MISSILE_STORM` | int | `99` |  |
| `IP_CONST_ONHIT_CASTSPELL_BANE` | int | `100` |  |
| `IP_CONST_ONHIT_CASTSPELL_SPIKE_GROWTH` | int | `101` |  |
| `IP_CONST_ONHIT_CASTSPELL_TASHAS_HIDEOUS_LAUGHTER` | int | `102` |  |
| `IP_CONST_ONHIT_CASTSPELL_BIGBYS_INTERPOSING_HAND` | int | `103` |  |
| `IP_CONST_ONHIT_CASTSPELL_BIGBYS_FORCEFUL_HAND` | int | `104` |  |
| `IP_CONST_ONHIT_CASTSPELL_BIGBYS_GRASPING_HAND` | int | `105` |  |
| `IP_CONST_ONHIT_CASTSPELL_BIGBYS_CLENCHED_FIST` | int | `106` |  |
| `IP_CONST_ONHIT_CASTSPELL_BIGBYS_CRUSHING_HAND` | int | `107` |  |
| `IP_CONST_ONHIT_CASTSPELL_FLESH_TO_STONE` | int | `108` |  |
| `IP_CONST_ONHIT_CASTSPELL_STONE_TO_FLESH` | int | `109` |  |
| `IP_CONST_ONHIT_CASTSPELL_CRUMBLE` | int | `110` |  |
| `IP_CONST_ONHIT_CASTSPELL_INFESTATION_OF_MAGGOTS` | int | `111` |  |
| `IP_CONST_ONHIT_CASTSPELL_GREAT_THUNDERCLAP` | int | `112` |  |
| `IP_CONST_ONHIT_CASTSPELL_BALL_LIGHTNING` | int | `113` |  |
| `IP_CONST_ONHIT_CASTSPELL_GEDLEES_ELECTRIC_LOOP` | int | `114` |  |
| `IP_CONST_ONHIT_CASTSPELL_HORIZIKAULS_BOOM` | int | `115` |  |
| `IP_CONST_ONHIT_CASTSPELL_MESTILS_ACID_BREATH` | int | `116` |  |
| `IP_CONST_ONHIT_CASTSPELL_SCINTILLATING_SPHERE` | int | `117` |  |
| `IP_CONST_ONHIT_CASTSPELL_UNDEATH_TO_DEATH` | int | `118` |  |
| `IP_CONST_ONHIT_CASTSPELL_STONEHOLD` | int | `119` |  |
| `IP_CONST_ONHIT_CASTSPELL_EVIL_BLIGHT` | int | `121` |  |
| `IP_CONST_ONHIT_CASTSPELL_ONHIT_TELEPORT` | int | `122` |  |
| `IP_CONST_ONHIT_CASTSPELL_ONHIT_SLAYRAKSHASA` | int | `123` |  |
| `IP_CONST_ONHIT_CASTSPELL_ONHIT_FIREDAMAGE` | int | `124` |  |
| `IP_CONST_ONHIT_CASTSPELL_ONHIT_UNIQUEPOWER` | int | `125` |  |
| `IP_CONST_ONHIT_CASTSPELL_ONHIT_PLANARRIFT` | int | `126` |  |
| `IP_CONST_ONHIT_CASTSPELL_ONHIT_DARKFIRE` | int | `127` |  |
| `IP_CONST_ONHIT_CASTSPELL_ONHIT_EXTRACTBRAIN` | int | `128` |  |
| `IP_CONST_ONHIT_CASTSPELL_ONHITFLAMINGSKIN` | int | `129` |  |
| `IP_CONST_ONHIT_CASTSPELL_ONHIT_CHAOSSHIELD` | int | `130` |  |
| `IP_CONST_ONHIT_CASTSPELL_ONHIT_CONSTRICTWEAPON` | int | `131` |  |
| `IP_CONST_ONHIT_CASTSPELL_ONHITRUINARMORBEBILITH` | int | `132` |  |
| `IP_CONST_ONHIT_CASTSPELL_ONHITDEMILICHTOUCH` | int | `133` |  |
| `IP_CONST_ONHIT_CASTSPELL_ONHITDRACOLICHTOUCH` | int | `134` |  |
| `IP_CONST_ONHIT_CASTSPELL_INTELLIGENT_WEAPON_ONHIT` | int | `135` |  |
| `IP_CONST_ONHIT_CASTSPELL_PARALYZE_2` | int | `136` |  |
| `IP_CONST_ONHIT_CASTSPELL_DEAFENING_CLNG` | int | `137` |  |
| `IP_CONST_ONHIT_CASTSPELL_KNOCKDOWN` | int | `138` |  |
| `IP_CONST_ONHIT_CASTSPELL_FREEZE` | int | `139` |  |
| `IP_CONST_ONHIT_CASTSPELL_COMBUST` | int | `140` |  |
| `IP_CONST_POISON_1D2_STRDAMAGE` | int | `0` |  |
| `IP_CONST_POISON_1D2_DEXDAMAGE` | int | `1` |  |
| `IP_CONST_POISON_1D2_CONDAMAGE` | int | `2` |  |
| `IP_CONST_POISON_1D2_INTDAMAGE` | int | `3` |  |
| `IP_CONST_POISON_1D2_WISDAMAGE` | int | `4` |  |
| `IP_CONST_POISON_1D2_CHADAMAGE` | int | `5` |  |
| `IP_CONST_QUALITY_UNKOWN` | int | `0` |  |
| `IP_CONST_QUALITY_DESTROYED` | int | `1` |  |
| `IP_CONST_QUALITY_RUINED` | int | `2` |  |
| `IP_CONST_QUALITY_VERY_POOR` | int | `3` |  |
| `IP_CONST_QUALITY_POOR` | int | `4` |  |
| `IP_CONST_QUALITY_BELOW_AVERAGE` | int | `5` |  |
| `IP_CONST_QUALITY_AVERAGE` | int | `6` |  |
| `IP_CONST_QUALITY_ABOVE_AVERAGE` | int | `7` |  |
| `IP_CONST_QUALITY_GOOD` | int | `8` |  |
| `IP_CONST_QUALITY_VERY_GOOD` | int | `9` |  |
| `IP_CONST_QUALITY_EXCELLENT` | int | `10` |  |
| `IP_CONST_QUALITY_MASTERWORK` | int | `11` |  |
| `IP_CONST_QUALITY_GOD_LIKE` | int | `12` |  |
| `IP_CONST_QUALITY_RAW` | int | `13` |  |
| `IP_CONST_QUALITY_CUT` | int | `14` |  |
| `IP_CONST_QUALITY_POLISHED` | int | `15` |  |
| `IP_CONST_CONTAINERWEIGHTRED_20_PERCENT` | int | `1` |  |
| `IP_CONST_CONTAINERWEIGHTRED_40_PERCENT` | int | `2` |  |
| `IP_CONST_CONTAINERWEIGHTRED_60_PERCENT` | int | `3` |  |
| `IP_CONST_CONTAINERWEIGHTRED_80_PERCENT` | int | `4` |  |
| `IP_CONST_CONTAINERWEIGHTRED_100_PERCENT` | int | `5` |  |
| `IP_CONST_DAMAGERESIST_5` | int | `1` |  |
| `IP_CONST_DAMAGERESIST_10` | int | `2` |  |
| `IP_CONST_DAMAGERESIST_15` | int | `3` |  |
| `IP_CONST_DAMAGERESIST_20` | int | `4` |  |
| `IP_CONST_DAMAGERESIST_25` | int | `5` |  |
| `IP_CONST_DAMAGERESIST_30` | int | `6` |  |
| `IP_CONST_DAMAGERESIST_35` | int | `7` |  |
| `IP_CONST_DAMAGERESIST_40` | int | `8` |  |
| `IP_CONST_DAMAGERESIST_45` | int | `9` |  |
| `IP_CONST_DAMAGERESIST_50` | int | `10` |  |
| `IP_CONST_SAVEVS_ACID` | int | `1` |  |
| `IP_CONST_SAVEVS_COLD` | int | `3` |  |
| `IP_CONST_SAVEVS_DEATH` | int | `4` |  |
| `IP_CONST_SAVEVS_DISEASE` | int | `5` |  |
| `IP_CONST_SAVEVS_DIVINE` | int | `6` |  |
| `IP_CONST_SAVEVS_ELECTRICAL` | int | `7` |  |
| `IP_CONST_SAVEVS_FEAR` | int | `8` |  |
| `IP_CONST_SAVEVS_FIRE` | int | `9` |  |
| `IP_CONST_SAVEVS_MINDAFFECTING` | int | `11` |  |
| `IP_CONST_SAVEVS_NEGATIVE` | int | `12` |  |
| `IP_CONST_SAVEVS_POISON` | int | `13` |  |
| `IP_CONST_SAVEVS_POSITIVE` | int | `14` |  |
| `IP_CONST_SAVEVS_SONIC` | int | `15` |  |
| `IP_CONST_SAVEVS_UNIVERSAL` | int | `0` |  |
| `IP_CONST_SAVEBASETYPE_FORTITUDE` | int | `1` |  |
| `IP_CONST_SAVEBASETYPE_WILL` | int | `2` |  |
| `IP_CONST_SAVEBASETYPE_REFLEX` | int | `3` |  |
| `IP_CONST_DAMAGESOAK_5_HP` | int | `1` |  |
| `IP_CONST_DAMAGESOAK_10_HP` | int | `2` |  |
| `IP_CONST_DAMAGESOAK_15_HP` | int | `3` |  |
| `IP_CONST_DAMAGESOAK_20_HP` | int | `4` |  |
| `IP_CONST_DAMAGESOAK_25_HP` | int | `5` |  |
| `IP_CONST_DAMAGESOAK_30_HP` | int | `6` |  |
| `IP_CONST_DAMAGESOAK_35_HP` | int | `7` |  |
| `IP_CONST_DAMAGESOAK_40_HP` | int | `8` |  |
| `IP_CONST_DAMAGESOAK_45_HP` | int | `9` |  |
| `IP_CONST_DAMAGESOAK_50_HP` | int | `10` |  |
| `IP_CONST_DAMAGEREDUCTION_1` | int | `0` |  |
| `IP_CONST_DAMAGEREDUCTION_2` | int | `1` |  |
| `IP_CONST_DAMAGEREDUCTION_3` | int | `2` |  |
| `IP_CONST_DAMAGEREDUCTION_4` | int | `3` |  |
| `IP_CONST_DAMAGEREDUCTION_5` | int | `4` |  |
| `IP_CONST_DAMAGEREDUCTION_6` | int | `5` |  |
| `IP_CONST_DAMAGEREDUCTION_7` | int | `6` |  |
| `IP_CONST_DAMAGEREDUCTION_8` | int | `7` |  |
| `IP_CONST_DAMAGEREDUCTION_9` | int | `8` |  |
| `IP_CONST_DAMAGEREDUCTION_10` | int | `9` |  |
| `IP_CONST_DAMAGEREDUCTION_11` | int | `10` |  |
| `IP_CONST_DAMAGEREDUCTION_12` | int | `11` |  |
| `IP_CONST_DAMAGEREDUCTION_13` | int | `12` |  |
| `IP_CONST_DAMAGEREDUCTION_14` | int | `13` |  |
| `IP_CONST_DAMAGEREDUCTION_15` | int | `14` |  |
| `IP_CONST_DAMAGEREDUCTION_16` | int | `15` |  |
| `IP_CONST_DAMAGEREDUCTION_17` | int | `16` |  |
| `IP_CONST_DAMAGEREDUCTION_18` | int | `17` |  |
| `IP_CONST_DAMAGEREDUCTION_19` | int | `18` |  |
| `IP_CONST_DAMAGEREDUCTION_20` | int | `19` |  |
| `IP_CONST_IMMUNITYSPELL_ACID_FOG` | int | `0` |  |
| `IP_CONST_IMMUNITYSPELL_AID` | int | `1` |  |
| `IP_CONST_IMMUNITYSPELL_BARKSKIN` | int | `2` |  |
| `IP_CONST_IMMUNITYSPELL_BESTOW_CURSE` | int | `3` |  |
| `IP_CONST_IMMUNITYSPELL_BLINDNESS_AND_DEAFNESS` | int | `6` |  |
| `IP_CONST_IMMUNITYSPELL_BURNING_HANDS` | int | `8` |  |
| `IP_CONST_IMMUNITYSPELL_CALL_LIGHTNING` | int | `9` |  |
| `IP_CONST_IMMUNITYSPELL_CHAIN_LIGHTNING` | int | `12` |  |
| `IP_CONST_IMMUNITYSPELL_CHARM_MONSTER` | int | `13` |  |
| `IP_CONST_IMMUNITYSPELL_CHARM_PERSON` | int | `14` |  |
| `IP_CONST_IMMUNITYSPELL_CHARM_PERSON_OR_ANIMAL` | int | `15` |  |
| `IP_CONST_IMMUNITYSPELL_CIRCLE_OF_DEATH` | int | `16` |  |
| `IP_CONST_IMMUNITYSPELL_CIRCLE_OF_DOOM` | int | `17` |  |
| `IP_CONST_IMMUNITYSPELL_CLOUDKILL` | int | `21` |  |
| `IP_CONST_IMMUNITYSPELL_COLOR_SPRAY` | int | `22` |  |
| `IP_CONST_IMMUNITYSPELL_CONE_OF_COLD` | int | `23` |  |
| `IP_CONST_IMMUNITYSPELL_CONFUSION` | int | `24` |  |
| `IP_CONST_IMMUNITYSPELL_CONTAGION` | int | `25` |  |
| `IP_CONST_IMMUNITYSPELL_CONTROL_UNDEAD` | int | `26` |  |
| `IP_CONST_IMMUNITYSPELL_CURE_CRITICAL_WOUNDS` | int | `27` |  |
| `IP_CONST_IMMUNITYSPELL_CURE_LIGHT_WOUNDS` | int | `28` |  |
| `IP_CONST_IMMUNITYSPELL_CURE_MINOR_WOUNDS` | int | `29` |  |
| `IP_CONST_IMMUNITYSPELL_CURE_MODERATE_WOUNDS` | int | `30` |  |
| `IP_CONST_IMMUNITYSPELL_CURE_SERIOUS_WOUNDS` | int | `31` |  |
| `IP_CONST_IMMUNITYSPELL_DARKNESS` | int | `32` |  |
| `IP_CONST_IMMUNITYSPELL_DAZE` | int | `33` |  |
| `IP_CONST_IMMUNITYSPELL_DEATH_WARD` | int | `34` |  |
| `IP_CONST_IMMUNITYSPELL_DELAYED_BLAST_FIREBALL` | int | `35` |  |
| `IP_CONST_IMMUNITYSPELL_DISMISSAL` | int | `36` |  |
| `IP_CONST_IMMUNITYSPELL_DISPEL_MAGIC` | int | `37` |  |
| `IP_CONST_IMMUNITYSPELL_DOMINATE_ANIMAL` | int | `39` |  |
| `IP_CONST_IMMUNITYSPELL_DOMINATE_MONSTER` | int | `40` |  |
| `IP_CONST_IMMUNITYSPELL_DOMINATE_PERSON` | int | `41` |  |
| `IP_CONST_IMMUNITYSPELL_DOOM` | int | `42` |  |
| `IP_CONST_IMMUNITYSPELL_ENERGY_DRAIN` | int | `46` |  |
| `IP_CONST_IMMUNITYSPELL_ENERVATION` | int | `47` |  |
| `IP_CONST_IMMUNITYSPELL_ENTANGLE` | int | `48` |  |
| `IP_CONST_IMMUNITYSPELL_FEAR` | int | `49` |  |
| `IP_CONST_IMMUNITYSPELL_FEEBLEMIND` | int | `50` |  |
| `IP_CONST_IMMUNITYSPELL_FINGER_OF_DEATH` | int | `51` |  |
| `IP_CONST_IMMUNITYSPELL_FIRE_STORM` | int | `52` |  |
| `IP_CONST_IMMUNITYSPELL_FIREBALL` | int | `53` |  |
| `IP_CONST_IMMUNITYSPELL_FLAME_ARROW` | int | `54` |  |
| `IP_CONST_IMMUNITYSPELL_FLAME_LASH` | int | `55` |  |
| `IP_CONST_IMMUNITYSPELL_FLAME_STRIKE` | int | `56` |  |
| `IP_CONST_IMMUNITYSPELL_FREEDOM_OF_MOVEMENT` | int | `57` |  |
| `IP_CONST_IMMUNITYSPELL_GREASE` | int | `59` |  |
| `IP_CONST_IMMUNITYSPELL_GREATER_DISPELLING` | int | `60` |  |
| `IP_CONST_IMMUNITYSPELL_GREATER_PLANAR_BINDING` | int | `62` |  |
| `IP_CONST_IMMUNITYSPELL_GREATER_SHADOW_CONJURATION` | int | `64` |  |
| `IP_CONST_IMMUNITYSPELL_GREATER_SPELL_BREACH` | int | `65` |  |
| `IP_CONST_IMMUNITYSPELL_HAMMER_OF_THE_GODS` | int | `68` |  |
| `IP_CONST_IMMUNITYSPELL_HARM` | int | `69` |  |
| `IP_CONST_IMMUNITYSPELL_HEAL` | int | `71` |  |
| `IP_CONST_IMMUNITYSPELL_HEALING_CIRCLE` | int | `72` |  |
| `IP_CONST_IMMUNITYSPELL_HOLD_ANIMAL` | int | `73` |  |
| `IP_CONST_IMMUNITYSPELL_HOLD_MONSTER` | int | `74` |  |
| `IP_CONST_IMMUNITYSPELL_HOLD_PERSON` | int | `75` |  |
| `IP_CONST_IMMUNITYSPELL_IMPLOSION` | int | `78` |  |
| `IP_CONST_IMMUNITYSPELL_IMPROVED_INVISIBILITY` | int | `79` |  |
| `IP_CONST_IMMUNITYSPELL_INCENDIARY_CLOUD` | int | `80` |  |
| `IP_CONST_IMMUNITYSPELL_INVISIBILITY_PURGE` | int | `82` |  |
| `IP_CONST_IMMUNITYSPELL_LESSER_DISPEL` | int | `84` |  |
| `IP_CONST_IMMUNITYSPELL_LESSER_PLANAR_BINDING` | int | `86` |  |
| `IP_CONST_IMMUNITYSPELL_LESSER_SPELL_BREACH` | int | `88` |  |
| `IP_CONST_IMMUNITYSPELL_LIGHTNING_BOLT` | int | `91` |  |
| `IP_CONST_IMMUNITYSPELL_MAGIC_MISSILE` | int | `97` |  |
| `IP_CONST_IMMUNITYSPELL_MASS_BLINDNESS_AND_DEAFNESS` | int | `100` |  |
| `IP_CONST_IMMUNITYSPELL_MASS_CHARM` | int | `101` |  |
| `IP_CONST_IMMUNITYSPELL_MASS_HEAL` | int | `104` |  |
| `IP_CONST_IMMUNITYSPELL_MELFS_ACID_ARROW` | int | `105` |  |
| `IP_CONST_IMMUNITYSPELL_METEOR_SWARM` | int | `106` |  |
| `IP_CONST_IMMUNITYSPELL_MIND_FOG` | int | `108` |  |
| `IP_CONST_IMMUNITYSPELL_MORDENKAINENS_DISJUNCTION` | int | `112` |  |
| `IP_CONST_IMMUNITYSPELL_PHANTASMAL_KILLER` | int | `116` |  |
| `IP_CONST_IMMUNITYSPELL_PLANAR_BINDING` | int | `117` |  |
| `IP_CONST_IMMUNITYSPELL_POISON` | int | `118` |  |
| `IP_CONST_IMMUNITYSPELL_POWER_WORD_KILL` | int | `120` |  |
| `IP_CONST_IMMUNITYSPELL_POWER_WORD_STUN` | int | `121` |  |
| `IP_CONST_IMMUNITYSPELL_PRISMATIC_SPRAY` | int | `124` |  |
| `IP_CONST_IMMUNITYSPELL_RAY_OF_ENFEEBLEMENT` | int | `131` |  |
| `IP_CONST_IMMUNITYSPELL_RAY_OF_FROST` | int | `132` |  |
| `IP_CONST_IMMUNITYSPELL_SCARE` | int | `142` |  |
| `IP_CONST_IMMUNITYSPELL_SEARING_LIGHT` | int | `143` |  |
| `IP_CONST_IMMUNITYSPELL_SHADES` | int | `145` |  |
| `IP_CONST_IMMUNITYSPELL_SHADOW_CONJURATION` | int | `146` |  |
| `IP_CONST_IMMUNITYSPELL_SILENCE` | int | `150` |  |
| `IP_CONST_IMMUNITYSPELL_SLAY_LIVING` | int | `151` |  |
| `IP_CONST_IMMUNITYSPELL_SLEEP` | int | `152` |  |
| `IP_CONST_IMMUNITYSPELL_SLOW` | int | `153` |  |
| `IP_CONST_IMMUNITYSPELL_SOUND_BURST` | int | `154` |  |
| `IP_CONST_IMMUNITYSPELL_STINKING_CLOUD` | int | `158` |  |
| `IP_CONST_IMMUNITYSPELL_STONESKIN` | int | `159` |  |
| `IP_CONST_IMMUNITYSPELL_STORM_OF_VENGEANCE` | int | `160` |  |
| `IP_CONST_IMMUNITYSPELL_SUNBEAM` | int | `161` |  |
| `IP_CONST_IMMUNITYSPELL_VIRTUE` | int | `165` |  |
| `IP_CONST_IMMUNITYSPELL_WAIL_OF_THE_BANSHEE` | int | `166` |  |
| `IP_CONST_IMMUNITYSPELL_WEB` | int | `167` |  |
| `IP_CONST_IMMUNITYSPELL_WEIRD` | int | `168` |  |
| `IP_CONST_IMMUNITYSPELL_WORD_OF_FAITH` | int | `169` |  |
| `IP_CONST_IMMUNITYSPELL_MAGIC_CIRCLE_AGAINST_ALIGNMENT` | int | `171` |  |
| `IP_CONST_IMMUNITYSPELL_EAGLE_SPLEDOR` | int | `173` |  |
| `IP_CONST_IMMUNITYSPELL_OWLS_WISDOM` | int | `174` |  |
| `IP_CONST_IMMUNITYSPELL_FOXS_CUNNING` | int | `175` |  |
| `IP_CONST_IMMUNITYSPELL_GREATER_EAGLES_SPLENDOR` | int | `176` |  |
| `IP_CONST_IMMUNITYSPELL_GREATER_OWLS_WISDOM` | int | `177` |  |
| `IP_CONST_IMMUNITYSPELL_GREATER_FOXS_CUNNING` | int | `178` |  |
| `IP_CONST_IMMUNITYSPELL_GREATER_BULLS_STRENGTH` | int | `179` |  |
| `IP_CONST_IMMUNITYSPELL_GREATER_CATS_GRACE` | int | `180` |  |
| `IP_CONST_IMMUNITYSPELL_GREATER_ENDURANCE` | int | `181` |  |
| `IP_CONST_IMMUNITYSPELL_AURA_OF_VITALITY` | int | `182` |  |
| `IP_CONST_IMMUNITYSPELL_WAR_CRY` | int | `183` |  |
| `IP_CONST_IMMUNITYSPELL_REGENERATE` | int | `184` |  |
| `IP_CONST_IMMUNITYSPELL_EVARDS_BLACK_TENTACLES` | int | `185` |  |
| `IP_CONST_IMMUNITYSPELL_LEGEND_LORE` | int | `186` |  |
| `IP_CONST_IMMUNITYSPELL_FIND_TRAPS` | int | `187` |  |
| `IP_CONST_SPELLLEVEL_0` | int | `0` | hmm are these necessary? |
| `IP_CONST_SPELLLEVEL_1` | int | `1` |  |
| `IP_CONST_SPELLLEVEL_2` | int | `2` |  |
| `IP_CONST_SPELLLEVEL_3` | int | `3` |  |
| `IP_CONST_SPELLLEVEL_4` | int | `4` |  |
| `IP_CONST_SPELLLEVEL_5` | int | `5` |  |
| `IP_CONST_SPELLLEVEL_6` | int | `6` |  |
| `IP_CONST_SPELLLEVEL_7` | int | `7` |  |
| `IP_CONST_SPELLLEVEL_8` | int | `8` |  |
| `IP_CONST_SPELLLEVEL_9` | int | `9` |  |
| `IP_CONST_CASTSPELL_ACID_FOG_11` | int | `0` |  |
| `IP_CONST_CASTSPELL_ACID_SPLASH_1` | int | `355` |  |
| `IP_CONST_CASTSPELL_ACTIVATE_ITEM` | int | `359` |  |
| `IP_CONST_CASTSPELL_AID_3` | int | `1` |  |
| `IP_CONST_CASTSPELL_AMPLIFY_5` | int | `373` |  |
| `IP_CONST_CASTSPELL_ANIMATE_DEAD_10` | int | `3` |  |
| `IP_CONST_CASTSPELL_ANIMATE_DEAD_15` | int | `4` |  |
| `IP_CONST_CASTSPELL_ANIMATE_DEAD_5` | int | `2` |  |
| `IP_CONST_CASTSPELL_AURA_OF_VITALITY_13` | int | `321` |  |
| `IP_CONST_CASTSPELL_AURA_VERSUS_ALIGNMENT_15` | int | `287` |  |
| `IP_CONST_CASTSPELL_AURAOFGLORY_7` | int | `360` |  |
| `IP_CONST_CASTSPELL_AWAKEN_9` | int | `303` |  |
| `IP_CONST_CASTSPELL_BALAGARNSIRONHORN_7` | int | `367` |  |
| `IP_CONST_CASTSPELL_BANE_5` | int | `380` |  |
| `IP_CONST_CASTSPELL_BANISHMENT_15` | int | `361` |  |
| `IP_CONST_CASTSPELL_BARKSKIN_12` | int | `7` |  |
| `IP_CONST_CASTSPELL_BARKSKIN_3` | int | `5` |  |
| `IP_CONST_CASTSPELL_BARKSKIN_6` | int | `6` |  |
| `IP_CONST_CASTSPELL_BESTOW_CURSE_5` | int | `8` |  |
| `IP_CONST_CASTSPELL_BIGBYS_CLENCHED_FIST_20` | int | `393` |  |
| `IP_CONST_CASTSPELL_BIGBYS_CRUSHING_HAND_20` | int | `394` |  |
| `IP_CONST_CASTSPELL_BIGBYS_FORCEFUL_HAND_15` | int | `391` |  |
| `IP_CONST_CASTSPELL_BIGBYS_GRASPING_HAND_17` | int | `392` |  |
| `IP_CONST_CASTSPELL_BIGBYS_INTERPOSING_HAND_15` | int | `390` |  |
| `IP_CONST_CASTSPELL_BLADE_BARRIER_11` | int | `9` |  |
| `IP_CONST_CASTSPELL_BLADE_BARRIER_15` | int | `10` |  |
| `IP_CONST_CASTSPELL_BLESS_2` | int | `11` |  |
| `IP_CONST_CASTSPELL_BLINDNESS_DEAFNESS_3` | int | `14` |  |
| `IP_CONST_CASTSPELL_BLOOD_FRENZY_7` | int | `353` |  |
| `IP_CONST_CASTSPELL_BOMBARDMENT_20` | int | `354` |  |
| `IP_CONST_CASTSPELL_BULLS_STRENGTH_10` | int | `16` |  |
| `IP_CONST_CASTSPELL_BULLS_STRENGTH_15` | int | `17` |  |
| `IP_CONST_CASTSPELL_BULLS_STRENGTH_3` | int | `15` |  |
| `IP_CONST_CASTSPELL_BURNING_HANDS_2` | int | `18` |  |
| `IP_CONST_CASTSPELL_BURNING_HANDS_5` | int | `19` |  |
| `IP_CONST_CASTSPELL_CALL_LIGHTNING_10` | int | `21` |  |
| `IP_CONST_CASTSPELL_CALL_LIGHTNING_5` | int | `20` |  |
| `IP_CONST_CASTSPELL_CAMOFLAGE_5` | int | `352` |  |
| `IP_CONST_CASTSPELL_CATS_GRACE_10` | int | `26` |  |
| `IP_CONST_CASTSPELL_CATS_GRACE_15` | int | `27` |  |
| `IP_CONST_CASTSPELL_CATS_GRACE_3` | int | `25` |  |
| `IP_CONST_CASTSPELL_CHAIN_LIGHTNING_11` | int | `28` |  |
| `IP_CONST_CASTSPELL_CHAIN_LIGHTNING_15` | int | `29` |  |
| `IP_CONST_CASTSPELL_CHAIN_LIGHTNING_20` | int | `30` |  |
| `IP_CONST_CASTSPELL_CHARM_MONSTER_10` | int | `32` |  |
| `IP_CONST_CASTSPELL_CHARM_MONSTER_5` | int | `31` |  |
| `IP_CONST_CASTSPELL_CHARM_PERSON_10` | int | `34` |  |
| `IP_CONST_CASTSPELL_CHARM_PERSON_2` | int | `33` |  |
| `IP_CONST_CASTSPELL_CHARM_PERSON_OR_ANIMAL_10` | int | `36` |  |
| `IP_CONST_CASTSPELL_CHARM_PERSON_OR_ANIMAL_3` | int | `35` |  |
| `IP_CONST_CASTSPELL_CIRCLE_OF_DEATH_11` | int | `37` |  |
| `IP_CONST_CASTSPELL_CIRCLE_OF_DEATH_15` | int | `38` |  |
| `IP_CONST_CASTSPELL_CIRCLE_OF_DEATH_20` | int | `39` |  |
| `IP_CONST_CASTSPELL_CIRCLE_OF_DOOM_15` | int | `41` |  |
| `IP_CONST_CASTSPELL_CIRCLE_OF_DOOM_20` | int | `42` |  |
| `IP_CONST_CASTSPELL_CIRCLE_OF_DOOM_9` | int | `40` |  |
| `IP_CONST_CASTSPELL_CLAIRAUDIENCE_CLAIRVOYANCE_10` | int | `44` |  |
| `IP_CONST_CASTSPELL_CLAIRAUDIENCE_CLAIRVOYANCE_15` | int | `45` |  |
| `IP_CONST_CASTSPELL_CLAIRAUDIENCE_CLAIRVOYANCE_5` | int | `43` |  |
| `IP_CONST_CASTSPELL_CLARITY_3` | int | `46` |  |
| `IP_CONST_CASTSPELL_CLOUDKILL_9` | int | `48` |  |
| `IP_CONST_CASTSPELL_COLOR_SPRAY_2` | int | `49` |  |
| `IP_CONST_CASTSPELL_CONE_OF_COLD_15` | int | `51` |  |
| `IP_CONST_CASTSPELL_CONE_OF_COLD_9` | int | `50` |  |
| `IP_CONST_CASTSPELL_CONFUSION_10` | int | `53` |  |
| `IP_CONST_CASTSPELL_CONFUSION_5` | int | `52` |  |
| `IP_CONST_CASTSPELL_CONTAGION_5` | int | `54` |  |
| `IP_CONST_CASTSPELL_CONTINUAL_FLAME_7` | int | `350` |  |
| `IP_CONST_CASTSPELL_CONTROL_UNDEAD_13` | int | `55` |  |
| `IP_CONST_CASTSPELL_CONTROL_UNDEAD_20` | int | `56` |  |
| `IP_CONST_CASTSPELL_CREATE_GREATER_UNDEAD_15` | int | `57` |  |
| `IP_CONST_CASTSPELL_CREATE_GREATER_UNDEAD_16` | int | `58` |  |
| `IP_CONST_CASTSPELL_CREATE_GREATER_UNDEAD_18` | int | `59` |  |
| `IP_CONST_CASTSPELL_CREATE_UNDEAD_11` | int | `60` |  |
| `IP_CONST_CASTSPELL_CREATE_UNDEAD_14` | int | `61` |  |
| `IP_CONST_CASTSPELL_CREATE_UNDEAD_16` | int | `62` |  |
| `IP_CONST_CASTSPELL_CREEPING_DOOM_13` | int | `304` |  |
| `IP_CONST_CASTSPELL_CURE_CRITICAL_WOUNDS_12` | int | `64` |  |
| `IP_CONST_CASTSPELL_CURE_CRITICAL_WOUNDS_15` | int | `65` |  |
| `IP_CONST_CASTSPELL_CURE_CRITICAL_WOUNDS_7` | int | `63` |  |
| `IP_CONST_CASTSPELL_CURE_LIGHT_WOUNDS_2` | int | `66` |  |
| `IP_CONST_CASTSPELL_CURE_LIGHT_WOUNDS_5` | int | `67` |  |
| `IP_CONST_CASTSPELL_CURE_MINOR_WOUNDS_1` | int | `68` |  |
| `IP_CONST_CASTSPELL_CURE_MODERATE_WOUNDS_10` | int | `71` |  |
| `IP_CONST_CASTSPELL_CURE_MODERATE_WOUNDS_3` | int | `69` |  |
| `IP_CONST_CASTSPELL_CURE_MODERATE_WOUNDS_6` | int | `70` |  |
| `IP_CONST_CASTSPELL_CURE_SERIOUS_WOUNDS_10` | int | `73` |  |
| `IP_CONST_CASTSPELL_CURE_SERIOUS_WOUNDS_5` | int | `72` |  |
| `IP_CONST_CASTSPELL_DARKNESS_3` | int | `75` |  |
| `IP_CONST_CASTSPELL_DARKVISION_3` | int | `305` |  |
| `IP_CONST_CASTSPELL_DARKVISION_6` | int | `306` |  |
| `IP_CONST_CASTSPELL_DAZE_1` | int | `76` |  |
| `IP_CONST_CASTSPELL_DEATH_WARD_7` | int | `77` |  |
| `IP_CONST_CASTSPELL_DELAYED_BLAST_FIREBALL_13` | int | `78` |  |
| `IP_CONST_CASTSPELL_DELAYED_BLAST_FIREBALL_15` | int | `79` |  |
| `IP_CONST_CASTSPELL_DELAYED_BLAST_FIREBALL_20` | int | `80` |  |
| `IP_CONST_CASTSPELL_DESTRUCTION_13` | int | `307` |  |
| `IP_CONST_CASTSPELL_DIRGE_15` | int | `376` |  |
| `IP_CONST_CASTSPELL_DISMISSAL_12` | int | `82` |  |
| `IP_CONST_CASTSPELL_DISMISSAL_18` | int | `83` |  |
| `IP_CONST_CASTSPELL_DISMISSAL_7` | int | `81` |  |
| `IP_CONST_CASTSPELL_DISPEL_MAGIC_10` | int | `85` |  |
| `IP_CONST_CASTSPELL_DISPEL_MAGIC_5` | int | `84` |  |
| `IP_CONST_CASTSPELL_DISPLACEMENT_9` | int | `389` |  |
| `IP_CONST_CASTSPELL_DIVINE_FAVOR_5` | int | `345` |  |
| `IP_CONST_CASTSPELL_DIVINE_MIGHT_5` | int | `395` |  |
| `IP_CONST_CASTSPELL_DIVINE_POWER_7` | int | `86` |  |
| `IP_CONST_CASTSPELL_DIVINE_SHIELD_5` | int | `396` |  |
| `IP_CONST_CASTSPELL_DOMINATE_ANIMAL_5` | int | `87` |  |
| `IP_CONST_CASTSPELL_DOMINATE_MONSTER_17` | int | `88` |  |
| `IP_CONST_CASTSPELL_DOMINATE_PERSON_7` | int | `89` |  |
| `IP_CONST_CASTSPELL_DOOM_2` | int | `90` |  |
| `IP_CONST_CASTSPELL_DOOM_5` | int | `91` |  |
| `IP_CONST_CASTSPELL_DRAGON_BREATH_ACID_10` | int | `400` |  |
| `IP_CONST_CASTSPELL_DRAGON_BREATH_COLD_10` | int | `401` |  |
| `IP_CONST_CASTSPELL_DRAGON_BREATH_FEAR_10` | int | `402` |  |
| `IP_CONST_CASTSPELL_DRAGON_BREATH_FIRE_10` | int | `403` |  |
| `IP_CONST_CASTSPELL_DRAGON_BREATH_GAS_10` | int | `404` |  |
| `IP_CONST_CASTSPELL_DRAGON_BREATH_LIGHTNING_10` | int | `405` |  |
| `IP_CONST_CASTSPELL_DRAGON_BREATH_PARALYZE_10` | int | `406` |  |
| `IP_CONST_CASTSPELL_DRAGON_BREATH_SLEEP_10` | int | `407` |  |
| `IP_CONST_CASTSPELL_DRAGON_BREATH_SLOW_10` | int | `408` |  |
| `IP_CONST_CASTSPELL_DRAGON_BREATH_WEAKEN_10` | int | `409` |  |
| `IP_CONST_CASTSPELL_DROWN_15` | int | `368` |  |
| `IP_CONST_CASTSPELL_EAGLE_SPLEDOR_10` | int | `289` |  |
| `IP_CONST_CASTSPELL_EAGLE_SPLEDOR_15` | int | `290` |  |
| `IP_CONST_CASTSPELL_EAGLE_SPLEDOR_3` | int | `288` |  |
| `IP_CONST_CASTSPELL_EARTHQUAKE_20` | int | `357` |  |
| `IP_CONST_CASTSPELL_ELECTRIC_JOLT_1` | int | `370` |  |
| `IP_CONST_CASTSPELL_ELEMENTAL_SHIELD_12` | int | `93` |  |
| `IP_CONST_CASTSPELL_ELEMENTAL_SHIELD_7` | int | `92` |  |
| `IP_CONST_CASTSPELL_ELEMENTAL_SWARM_17` | int | `94` |  |
| `IP_CONST_CASTSPELL_ENDURANCE_10` | int | `96` |  |
| `IP_CONST_CASTSPELL_ENDURANCE_15` | int | `97` |  |
| `IP_CONST_CASTSPELL_ENDURANCE_3` | int | `95` |  |
| `IP_CONST_CASTSPELL_ENDURE_ELEMENTS_2` | int | `98` |  |
| `IP_CONST_CASTSPELL_ENERGY_BUFFER_11` | int | `311` |  |
| `IP_CONST_CASTSPELL_ENERGY_BUFFER_15` | int | `312` |  |
| `IP_CONST_CASTSPELL_ENERGY_BUFFER_20` | int | `313` |  |
| `IP_CONST_CASTSPELL_ENERGY_DRAIN_17` | int | `99` |  |
| `IP_CONST_CASTSPELL_ENERVATION_7` | int | `100` |  |
| `IP_CONST_CASTSPELL_ENTANGLE_2` | int | `101` |  |
| `IP_CONST_CASTSPELL_ENTANGLE_5` | int | `102` |  |
| `IP_CONST_CASTSPELL_ENTROPIC_SHIELD_5` | int | `349` |  |
| `IP_CONST_CASTSPELL_ETHEREAL_VISAGE_15` | int | `196` |  |
| `IP_CONST_CASTSPELL_ETHEREAL_VISAGE_9` | int | `195` |  |
| `IP_CONST_CASTSPELL_ETHEREALNESS_18` | int | `374` |  |
| `IP_CONST_CASTSPELL_EVARDS_BLACK_TENTACLES_15` | int | `325` |  |
| `IP_CONST_CASTSPELL_EVARDS_BLACK_TENTACLES_7` | int | `324` |  |
| `IP_CONST_CASTSPELL_EXPEDITIOUS_RETREAT_5` | int | `387` |  |
| `IP_CONST_CASTSPELL_FEAR_5` | int | `103` |  |
| `IP_CONST_CASTSPELL_FEEBLEMIND_9` | int | `104` |  |
| `IP_CONST_CASTSPELL_FIND_TRAPS_3` | int | `327` |  |
| `IP_CONST_CASTSPELL_FINGER_OF_DEATH_13` | int | `105` |  |
| `IP_CONST_CASTSPELL_FIRE_STORM_13` | int | `106` |  |
| `IP_CONST_CASTSPELL_FIRE_STORM_18` | int | `107` |  |
| `IP_CONST_CASTSPELL_FIREBALL_10` | int | `109` |  |
| `IP_CONST_CASTSPELL_FIREBALL_5` | int | `108` |  |
| `IP_CONST_CASTSPELL_FIREBRAND_15` | int | `371` |  |
| `IP_CONST_CASTSPELL_FLAME_ARROW_12` | int | `111` |  |
| `IP_CONST_CASTSPELL_FLAME_ARROW_18` | int | `112` |  |
| `IP_CONST_CASTSPELL_FLAME_ARROW_5` | int | `110` |  |
| `IP_CONST_CASTSPELL_FLAME_LASH_10` | int | `114` |  |
| `IP_CONST_CASTSPELL_FLAME_LASH_3` | int | `113` |  |
| `IP_CONST_CASTSPELL_FLAME_STRIKE_12` | int | `116` |  |
| `IP_CONST_CASTSPELL_FLAME_STRIKE_18` | int | `117` |  |
| `IP_CONST_CASTSPELL_FLAME_STRIKE_7` | int | `115` |  |
| `IP_CONST_CASTSPELL_FLARE_1` | int | `347` |  |
| `IP_CONST_CASTSPELL_FLESH_TO_STONE_5` | int | `398` |  |
| `IP_CONST_CASTSPELL_FOXS_CUNNING_10` | int | `295` |  |
| `IP_CONST_CASTSPELL_FOXS_CUNNING_15` | int | `296` |  |
| `IP_CONST_CASTSPELL_FOXS_CUNNING_3` | int | `294` |  |
| `IP_CONST_CASTSPELL_FREEDOM_OF_MOVEMENT_7` | int | `118` |  |
| `IP_CONST_CASTSPELL_GATE_17` | int | `119` |  |
| `IP_CONST_CASTSPELL_GHOSTLY_VISAGE_15` | int | `194` |  |
| `IP_CONST_CASTSPELL_GHOSTLY_VISAGE_3` | int | `192` |  |
| `IP_CONST_CASTSPELL_GHOSTLY_VISAGE_9` | int | `193` |  |
| `IP_CONST_CASTSPELL_GHOUL_TOUCH_3` | int | `120` |  |
| `IP_CONST_CASTSPELL_GLOBE_OF_INVULNERABILITY_11` | int | `121` |  |
| `IP_CONST_CASTSPELL_GREASE_2` | int | `122` |  |
| `IP_CONST_CASTSPELL_GREATER_BULLS_STRENGTH_11` | int | `300` |  |
| `IP_CONST_CASTSPELL_GREATER_CATS_GRACE_11` | int | `301` |  |
| `IP_CONST_CASTSPELL_GREATER_DISPELLING_15` | int | `124` |  |
| `IP_CONST_CASTSPELL_GREATER_DISPELLING_7` | int | `123` |  |
| `IP_CONST_CASTSPELL_GREATER_EAGLES_SPLENDOR_11` | int | `297` |  |
| `IP_CONST_CASTSPELL_GREATER_ENDURANCE_11` | int | `302` |  |
| `IP_CONST_CASTSPELL_GREATER_FOXS_CUNNING_11` | int | `299` |  |
| `IP_CONST_CASTSPELL_GREATER_MAGIC_FANG_9` | int | `384` |  |
| `IP_CONST_CASTSPELL_GREATER_OWLS_WISDOM_11` | int | `298` |  |
| `IP_CONST_CASTSPELL_GREATER_PLANAR_BINDING_15` | int | `126` |  |
| `IP_CONST_CASTSPELL_GREATER_RESTORATION_13` | int | `127` |  |
| `IP_CONST_CASTSPELL_GREATER_SHADOW_CONJURATION_9` | int | `128` |  |
| `IP_CONST_CASTSPELL_GREATER_SPELL_BREACH_11` | int | `129` |  |
| `IP_CONST_CASTSPELL_GREATER_SPELL_MANTLE_17` | int | `130` |  |
| `IP_CONST_CASTSPELL_GREATER_STONESKIN_11` | int | `131` |  |
| `IP_CONST_CASTSPELL_GRENADE_ACID_1` | int | `341` |  |
| `IP_CONST_CASTSPELL_GRENADE_CALTROPS_1` | int | `343` |  |
| `IP_CONST_CASTSPELL_GRENADE_CHICKEN_1` | int | `342` |  |
| `IP_CONST_CASTSPELL_GRENADE_CHOKING_1` | int | `339` |  |
| `IP_CONST_CASTSPELL_GRENADE_FIRE_1` | int | `336` |  |
| `IP_CONST_CASTSPELL_GRENADE_HOLY_1` | int | `338` |  |
| `IP_CONST_CASTSPELL_GRENADE_TANGLE_1` | int | `337` |  |
| `IP_CONST_CASTSPELL_GRENADE_THUNDERSTONE_1` | int | `340` |  |
| `IP_CONST_CASTSPELL_GUST_OF_WIND_10` | int | `410` |  |
| `IP_CONST_CASTSPELL_HAMMER_OF_THE_GODS_12` | int | `134` |  |
| `IP_CONST_CASTSPELL_HAMMER_OF_THE_GODS_7` | int | `133` |  |
| `IP_CONST_CASTSPELL_HARM_11` | int | `136` |  |
| `IP_CONST_CASTSPELL_HASTE_10` | int | `138` |  |
| `IP_CONST_CASTSPELL_HASTE_5` | int | `137` |  |
| `IP_CONST_CASTSPELL_HEAL_11` | int | `139` |  |
| `IP_CONST_CASTSPELL_HEALING_CIRCLE_16` | int | `141` |  |
| `IP_CONST_CASTSPELL_HEALING_CIRCLE_9` | int | `140` |  |
| `IP_CONST_CASTSPELL_HOLD_ANIMAL_3` | int | `142` |  |
| `IP_CONST_CASTSPELL_HOLD_MONSTER_7` | int | `143` |  |
| `IP_CONST_CASTSPELL_HOLD_PERSON_3` | int | `144` |  |
| `IP_CONST_CASTSPELL_HORRID_WILTING_15` | int | `308` |  |
| `IP_CONST_CASTSPELL_HORRID_WILTING_20` | int | `309` |  |
| `IP_CONST_CASTSPELL_ICE_STORM_9` | int | `310` |  |
| `IP_CONST_CASTSPELL_IDENTIFY_3` | int | `147` |  |
| `IP_CONST_CASTSPELL_IMPLOSION_17` | int | `148` |  |
| `IP_CONST_CASTSPELL_IMPROVED_INVISIBILITY_7` | int | `149` |  |
| `IP_CONST_CASTSPELL_INCENDIARY_CLOUD_15` | int | `150` |  |
| `IP_CONST_CASTSPELL_INFERNO_15` | int | `377` |  |
| `IP_CONST_CASTSPELL_INFLICT_CRITICAL_WOUNDS_12` | int | `366` |  |
| `IP_CONST_CASTSPELL_INFLICT_LIGHT_WOUNDS_5` | int | `363` |  |
| `IP_CONST_CASTSPELL_INFLICT_MINOR_WOUNDS_1` | int | `362` |  |
| `IP_CONST_CASTSPELL_INFLICT_MODERATE_WOUNDS_7` | int | `364` |  |
| `IP_CONST_CASTSPELL_INFLICT_SERIOUS_WOUNDS_9` | int | `365` |  |
| `IP_CONST_CASTSPELL_INVISIBILITY_3` | int | `151` |  |
| `IP_CONST_CASTSPELL_INVISIBILITY_PURGE_5` | int | `152` |  |
| `IP_CONST_CASTSPELL_INVISIBILITY_SPHERE_5` | int | `153` |  |
| `IP_CONST_CASTSPELL_ISAACS_GREATER_MISSILE_STORM_15` | int | `379` |  |
| `IP_CONST_CASTSPELL_ISAACS_LESSER_MISSILE_STORM_13` | int | `378` |  |
| `IP_CONST_CASTSPELL_KNOCK_3` | int | `154` |  |
| `IP_CONST_CASTSPELL_LEGEND_LORE_5` | int | `326` |  |
| `IP_CONST_CASTSPELL_LESSER_DISPEL_3` | int | `155` |  |
| `IP_CONST_CASTSPELL_LESSER_DISPEL_5` | int | `156` |  |
| `IP_CONST_CASTSPELL_LESSER_MIND_BLANK_9` | int | `157` |  |
| `IP_CONST_CASTSPELL_LESSER_PLANAR_BINDING_9` | int | `158` |  |
| `IP_CONST_CASTSPELL_LESSER_RESTORATION_3` | int | `159` |  |
| `IP_CONST_CASTSPELL_LESSER_SPELL_BREACH_7` | int | `160` |  |
| `IP_CONST_CASTSPELL_LESSER_SPELL_MANTLE_9` | int | `161` |  |
| `IP_CONST_CASTSPELL_LIGHT_1` | int | `162` |  |
| `IP_CONST_CASTSPELL_LIGHT_5` | int | `163` |  |
| `IP_CONST_CASTSPELL_LIGHTNING_BOLT_10` | int | `165` |  |
| `IP_CONST_CASTSPELL_LIGHTNING_BOLT_5` | int | `164` |  |
| `IP_CONST_CASTSPELL_MAGE_ARMOR_2` | int | `167` |  |
| `IP_CONST_CASTSPELL_MAGIC_CIRCLE_AGAINST_ALIGNMENT_5` | int | `286` |  |
| `IP_CONST_CASTSPELL_MAGIC_FANG_5` | int | `383` |  |
| `IP_CONST_CASTSPELL_MAGIC_MISSILE_3` | int | `172` |  |
| `IP_CONST_CASTSPELL_MAGIC_MISSILE_5` | int | `173` |  |
| `IP_CONST_CASTSPELL_MAGIC_MISSILE_9` | int | `174` |  |
| `IP_CONST_CASTSPELL_MANIPULATE_PORTAL_STONE` | int | `344` |  |
| `IP_CONST_CASTSPELL_MASS_BLINDNESS_DEAFNESS_15` | int | `179` |  |
| `IP_CONST_CASTSPELL_MASS_CAMOFLAGE_13` | int | `386` |  |
| `IP_CONST_CASTSPELL_MASS_CHARM_15` | int | `180` |  |
| `IP_CONST_CASTSPELL_MASS_HASTE_11` | int | `182` |  |
| `IP_CONST_CASTSPELL_MASS_HEAL_15` | int | `183` |  |
| `IP_CONST_CASTSPELL_MELFS_ACID_ARROW_3` | int | `184` |  |
| `IP_CONST_CASTSPELL_MELFS_ACID_ARROW_6` | int | `185` |  |
| `IP_CONST_CASTSPELL_MELFS_ACID_ARROW_9` | int | `186` |  |
| `IP_CONST_CASTSPELL_METEOR_SWARM_17` | int | `187` |  |
| `IP_CONST_CASTSPELL_MIND_BLANK_15` | int | `188` |  |
| `IP_CONST_CASTSPELL_MIND_FOG_9` | int | `189` |  |
| `IP_CONST_CASTSPELL_MINOR_GLOBE_OF_INVULNERABILITY_15` | int | `191` |  |
| `IP_CONST_CASTSPELL_MINOR_GLOBE_OF_INVULNERABILITY_7` | int | `190` |  |
| `IP_CONST_CASTSPELL_MORDENKAINENS_DISJUNCTION_17` | int | `197` |  |
| `IP_CONST_CASTSPELL_MORDENKAINENS_SWORD_13` | int | `198` |  |
| `IP_CONST_CASTSPELL_MORDENKAINENS_SWORD_18` | int | `199` |  |
| `IP_CONST_CASTSPELL_NATURES_BALANCE_15` | int | `200` |  |
| `IP_CONST_CASTSPELL_NEGATIVE_ENERGY_BURST_10` | int | `315` |  |
| `IP_CONST_CASTSPELL_NEGATIVE_ENERGY_BURST_5` | int | `314` |  |
| `IP_CONST_CASTSPELL_NEGATIVE_ENERGY_PROTECTION_10` | int | `202` |  |
| `IP_CONST_CASTSPELL_NEGATIVE_ENERGY_PROTECTION_15` | int | `203` |  |
| `IP_CONST_CASTSPELL_NEGATIVE_ENERGY_PROTECTION_5` | int | `201` |  |
| `IP_CONST_CASTSPELL_NEGATIVE_ENERGY_RAY_1` | int | `316` |  |
| `IP_CONST_CASTSPELL_NEGATIVE_ENERGY_RAY_3` | int | `317` |  |
| `IP_CONST_CASTSPELL_NEGATIVE_ENERGY_RAY_5` | int | `318` |  |
| `IP_CONST_CASTSPELL_NEGATIVE_ENERGY_RAY_7` | int | `319` |  |
| `IP_CONST_CASTSPELL_NEGATIVE_ENERGY_RAY_9` | int | `320` |  |
| `IP_CONST_CASTSPELL_NEUTRALIZE_POISON_5` | int | `204` |  |
| `IP_CONST_CASTSPELL_ONE_WITH_THE_LAND_7` | int | `351` |  |
| `IP_CONST_CASTSPELL_OWLS_INSIGHT_15` | int | `369` |  |
| `IP_CONST_CASTSPELL_OWLS_WISDOM_10` | int | `292` |  |
| `IP_CONST_CASTSPELL_OWLS_WISDOM_15` | int | `293` |  |
| `IP_CONST_CASTSPELL_OWLS_WISDOM_3` | int | `291` |  |
| `IP_CONST_CASTSPELL_PHANTASMAL_KILLER_7` | int | `205` |  |
| `IP_CONST_CASTSPELL_PLANAR_ALLY_15` | int | `382` |  |
| `IP_CONST_CASTSPELL_PLANAR_BINDING_11` | int | `206` |  |
| `IP_CONST_CASTSPELL_POISON_5` | int | `207` |  |
| `IP_CONST_CASTSPELL_POLYMORPH_SELF_7` | int | `208` |  |
| `IP_CONST_CASTSPELL_POWER_WORD_KILL_17` | int | `209` |  |
| `IP_CONST_CASTSPELL_POWER_WORD_STUN_13` | int | `210` |  |
| `IP_CONST_CASTSPELL_PRAYER_5` | int | `211` |  |
| `IP_CONST_CASTSPELL_PREMONITION_15` | int | `212` |  |
| `IP_CONST_CASTSPELL_PRISMATIC_SPRAY_13` | int | `213` |  |
| `IP_CONST_CASTSPELL_PROTECTION_FROM_ALIGNMENT_2` | int | `284` |  |
| `IP_CONST_CASTSPELL_PROTECTION_FROM_ALIGNMENT_5` | int | `285` |  |
| `IP_CONST_CASTSPELL_PROTECTION_FROM_ELEMENTS_10` | int | `217` |  |
| `IP_CONST_CASTSPELL_PROTECTION_FROM_ELEMENTS_3` | int | `216` |  |
| `IP_CONST_CASTSPELL_PROTECTION_FROM_SPELLS_13` | int | `224` |  |
| `IP_CONST_CASTSPELL_PROTECTION_FROM_SPELLS_20` | int | `225` |  |
| `IP_CONST_CASTSPELL_QUILLFIRE_8` | int | `356` |  |
| `IP_CONST_CASTSPELL_RAISE_DEAD_9` | int | `226` |  |
| `IP_CONST_CASTSPELL_RAY_OF_ENFEEBLEMENT_2` | int | `227` |  |
| `IP_CONST_CASTSPELL_RAY_OF_FROST_1` | int | `228` |  |
| `IP_CONST_CASTSPELL_REGENERATE_13` | int | `323` |  |
| `IP_CONST_CASTSPELL_REMOVE_BLINDNESS_DEAFNESS_5` | int | `229` |  |
| `IP_CONST_CASTSPELL_REMOVE_CURSE_5` | int | `230` |  |
| `IP_CONST_CASTSPELL_REMOVE_DISEASE_5` | int | `231` |  |
| `IP_CONST_CASTSPELL_REMOVE_FEAR_2` | int | `232` |  |
| `IP_CONST_CASTSPELL_REMOVE_PARALYSIS_3` | int | `233` |  |
| `IP_CONST_CASTSPELL_RESIST_ELEMENTS_10` | int | `235` |  |
| `IP_CONST_CASTSPELL_RESIST_ELEMENTS_3` | int | `234` |  |
| `IP_CONST_CASTSPELL_RESISTANCE_2` | int | `236` |  |
| `IP_CONST_CASTSPELL_RESISTANCE_5` | int | `237` |  |
| `IP_CONST_CASTSPELL_RESTORATION_7` | int | `238` |  |
| `IP_CONST_CASTSPELL_RESURRECTION_13` | int | `239` |  |
| `IP_CONST_CASTSPELL_ROGUES_CUNNING_3` | int | `328` |  |
| `IP_CONST_CASTSPELL_SANCTUARY_2` | int | `240` |  |
| `IP_CONST_CASTSPELL_SCARE_2` | int | `241` |  |
| `IP_CONST_CASTSPELL_SEARING_LIGHT_5` | int | `242` |  |
| `IP_CONST_CASTSPELL_SEE_INVISIBILITY_3` | int | `243` |  |
| `IP_CONST_CASTSPELL_SHADES_11` | int | `244` |  |
| `IP_CONST_CASTSPELL_SHADOW_CONJURATION_7` | int | `245` |  |
| `IP_CONST_CASTSPELL_SHADOW_SHIELD_13` | int | `246` |  |
| `IP_CONST_CASTSPELL_SHAPECHANGE_17` | int | `247` |  |
| `IP_CONST_CASTSPELL_SHIELD_5` | int | `348` |  |
| `IP_CONST_CASTSPELL_SHIELD_OF_FAITH_5` | int | `381` |  |
| `IP_CONST_CASTSPELL_SILENCE_3` | int | `249` |  |
| `IP_CONST_CASTSPELL_SLAY_LIVING_9` | int | `250` |  |
| `IP_CONST_CASTSPELL_SLEEP_2` | int | `251` |  |
| `IP_CONST_CASTSPELL_SLEEP_5` | int | `252` |  |
| `IP_CONST_CASTSPELL_SLOW_5` | int | `253` |  |
| `IP_CONST_CASTSPELL_SOUND_BURST_3` | int | `254` |  |
| `IP_CONST_CASTSPELL_SPECIAL_ALCOHOL_BEER` | int | `330` |  |
| `IP_CONST_CASTSPELL_SPECIAL_ALCOHOL_SPIRITS` | int | `332` |  |
| `IP_CONST_CASTSPELL_SPECIAL_ALCOHOL_WINE` | int | `331` |  |
| `IP_CONST_CASTSPELL_SPECIAL_HERB_BELLADONNA` | int | `333` |  |
| `IP_CONST_CASTSPELL_SPECIAL_HERB_GARLIC` | int | `334` |  |
| `IP_CONST_CASTSPELL_SPELL_MANTLE_13` | int | `257` |  |
| `IP_CONST_CASTSPELL_SPELL_RESISTANCE_15` | int | `256` |  |
| `IP_CONST_CASTSPELL_SPELL_RESISTANCE_9` | int | `255` |  |
| `IP_CONST_CASTSPELL_SPIKE_GROWTH_9` | int | `385` |  |
| `IP_CONST_CASTSPELL_STINKING_CLOUD_5` | int | `259` |  |
| `IP_CONST_CASTSPELL_STONE_TO_FLESH_5` | int | `399` |  |
| `IP_CONST_CASTSPELL_STONESKIN_7` | int | `260` |  |
| `IP_CONST_CASTSPELL_STORM_OF_VENGEANCE_17` | int | `261` |  |
| `IP_CONST_CASTSPELL_SUMMON_CREATURE_I_2` | int | `262` |  |
| `IP_CONST_CASTSPELL_SUMMON_CREATURE_I_5` | int | `263` |  |
| `IP_CONST_CASTSPELL_SUMMON_CREATURE_II_3` | int | `264` |  |
| `IP_CONST_CASTSPELL_SUMMON_CREATURE_III_5` | int | `265` |  |
| `IP_CONST_CASTSPELL_SUMMON_CREATURE_IV_7` | int | `266` |  |
| `IP_CONST_CASTSPELL_SUMMON_CREATURE_IX_17` | int | `267` |  |
| `IP_CONST_CASTSPELL_SUMMON_CREATURE_V_9` | int | `268` |  |
| `IP_CONST_CASTSPELL_SUMMON_CREATURE_VI_11` | int | `269` |  |
| `IP_CONST_CASTSPELL_SUMMON_CREATURE_VII_13` | int | `270` |  |
| `IP_CONST_CASTSPELL_SUMMON_CREATURE_VIII_15` | int | `271` |  |
| `IP_CONST_CASTSPELL_SUNBEAM_13` | int | `272` |  |
| `IP_CONST_CASTSPELL_SUNBURST_20` | int | `358` |  |
| `IP_CONST_CASTSPELL_TASHAS_HIDEOUS_LAUGHTER_7` | int | `388` |  |
| `IP_CONST_CASTSPELL_TENSERS_TRANSFORMATION_11` | int | `273` |  |
| `IP_CONST_CASTSPELL_TIME_STOP_17` | int | `274` |  |
| `IP_CONST_CASTSPELL_TRUE_SEEING_9` | int | `275` |  |
| `IP_CONST_CASTSPELL_TRUE_STRIKE_5` | int | `346` |  |
| `IP_CONST_CASTSPELL_UNDEATHS_ETERNAL_FOE_20` | int | `375` |  |
| `IP_CONST_CASTSPELL_UNIQUE_POWER` | int | `329` |  |
| `IP_CONST_CASTSPELL_UNIQUE_POWER_SELF_ONLY` | int | `335` |  |
| `IP_CONST_CASTSPELL_VAMPIRIC_TOUCH_5` | int | `277` |  |
| `IP_CONST_CASTSPELL_VIRTUE_1` | int | `278` |  |
| `IP_CONST_CASTSPELL_WAIL_OF_THE_BANSHEE_17` | int | `279` |  |
| `IP_CONST_CASTSPELL_WALL_OF_FIRE_9` | int | `280` |  |
| `IP_CONST_CASTSPELL_WAR_CRY_7` | int | `322` |  |
| `IP_CONST_CASTSPELL_WEB_3` | int | `281` |  |
| `IP_CONST_CASTSPELL_WEIRD_17` | int | `282` |  |
| `IP_CONST_CASTSPELL_WORD_OF_FAITH_13` | int | `283` |  |
| `IP_CONST_CASTSPELL_WOUNDING_WHISPERS_9` | int | `372` |  |
| `IP_CONST_SPELLSCHOOL_ABJURATION` | int | `0` |  |
| `IP_CONST_SPELLSCHOOL_CONJURATION` | int | `1` |  |
| `IP_CONST_SPELLSCHOOL_DIVINATION` | int | `2` |  |
| `IP_CONST_SPELLSCHOOL_ENCHANTMENT` | int | `3` |  |
| `IP_CONST_SPELLSCHOOL_EVOCATION` | int | `4` |  |
| `IP_CONST_SPELLSCHOOL_ILLUSION` | int | `5` |  |
| `IP_CONST_SPELLSCHOOL_NECROMANCY` | int | `6` |  |
| `IP_CONST_SPELLSCHOOL_TRANSMUTATION` | int | `7` |  |
| `IP_CONST_SPELLRESISTANCEBONUS_10` | int | `0` |  |
| `IP_CONST_SPELLRESISTANCEBONUS_12` | int | `1` |  |
| `IP_CONST_SPELLRESISTANCEBONUS_14` | int | `2` |  |
| `IP_CONST_SPELLRESISTANCEBONUS_16` | int | `3` |  |
| `IP_CONST_SPELLRESISTANCEBONUS_18` | int | `4` |  |
| `IP_CONST_SPELLRESISTANCEBONUS_20` | int | `5` |  |
| `IP_CONST_SPELLRESISTANCEBONUS_22` | int | `6` |  |
| `IP_CONST_SPELLRESISTANCEBONUS_24` | int | `7` |  |
| `IP_CONST_SPELLRESISTANCEBONUS_26` | int | `8` |  |
| `IP_CONST_SPELLRESISTANCEBONUS_28` | int | `9` |  |
| `IP_CONST_SPELLRESISTANCEBONUS_30` | int | `10` |  |
| `IP_CONST_SPELLRESISTANCEBONUS_32` | int | `11` |  |
| `IP_CONST_TRAPTYPE_SPIKE` | int | `1` |  |
| `IP_CONST_TRAPTYPE_HOLY` | int | `2` |  |
| `IP_CONST_TRAPTYPE_TANGLE` | int | `3` |  |
| `IP_CONST_TRAPTYPE_BLOBOFACID` | int | `4` |  |
| `IP_CONST_TRAPTYPE_FIRE` | int | `5` |  |
| `IP_CONST_TRAPTYPE_ELECTRICAL` | int | `6` |  |
| `IP_CONST_TRAPTYPE_GAS` | int | `7` |  |
| `IP_CONST_TRAPTYPE_FROST` | int | `8` |  |
| `IP_CONST_TRAPTYPE_ACID_SPLASH` | int | `9` |  |
| `IP_CONST_TRAPTYPE_SONIC` | int | `10` |  |
| `IP_CONST_TRAPTYPE_NEGATIVE` | int | `11` |  |
| `IP_CONST_TRAPSTRENGTH_MINOR` | int | `0` |  |
| `IP_CONST_TRAPSTRENGTH_AVERAGE` | int | `1` |  |
| `IP_CONST_TRAPSTRENGTH_STRONG` | int | `2` |  |
| `IP_CONST_TRAPSTRENGTH_DEADLY` | int | `3` |  |
| `IP_CONST_REDUCEDWEIGHT_80_PERCENT` | int | `1` |  |
| `IP_CONST_REDUCEDWEIGHT_60_PERCENT` | int | `2` |  |
| `IP_CONST_REDUCEDWEIGHT_40_PERCENT` | int | `3` |  |
| `IP_CONST_REDUCEDWEIGHT_20_PERCENT` | int | `4` |  |
| `IP_CONST_REDUCEDWEIGHT_10_PERCENT` | int | `5` |  |
| `IP_CONST_WEIGHTINCREASE_5_LBS` | int | `0` |  |
| `IP_CONST_WEIGHTINCREASE_10_LBS` | int | `1` |  |
| `IP_CONST_WEIGHTINCREASE_15_LBS` | int | `2` |  |
| `IP_CONST_WEIGHTINCREASE_30_LBS` | int | `3` |  |
| `IP_CONST_WEIGHTINCREASE_50_LBS` | int | `4` |  |
| `IP_CONST_WEIGHTINCREASE_100_LBS` | int | `5` |  |
| `IP_CONST_CLASS_BARBARIAN` | int | `0` |  |
| `IP_CONST_CLASS_BARD` | int | `1` |  |
| `IP_CONST_CLASS_CLERIC` | int | `2` |  |
| `IP_CONST_CLASS_DRUID` | int | `3` |  |
| `IP_CONST_CLASS_FIGHTER` | int | `4` |  |
| `IP_CONST_CLASS_MONK` | int | `5` |  |
| `IP_CONST_CLASS_PALADIN` | int | `6` |  |
| `IP_CONST_CLASS_RANGER` | int | `7` |  |
| `IP_CONST_CLASS_ROGUE` | int | `8` |  |
| `IP_CONST_CLASS_SORCERER` | int | `9` |  |
| `IP_CONST_CLASS_WIZARD` | int | `10` |  |
| `IP_CONST_ARCANE_SPELL_FAILURE_MINUS_50_PERCENT` | int | `0` |  |
| `IP_CONST_ARCANE_SPELL_FAILURE_MINUS_45_PERCENT` | int | `1` |  |
| `IP_CONST_ARCANE_SPELL_FAILURE_MINUS_40_PERCENT` | int | `2` |  |
| `IP_CONST_ARCANE_SPELL_FAILURE_MINUS_35_PERCENT` | int | `3` |  |
| `IP_CONST_ARCANE_SPELL_FAILURE_MINUS_30_PERCENT` | int | `4` |  |
| `IP_CONST_ARCANE_SPELL_FAILURE_MINUS_25_PERCENT` | int | `5` |  |
| `IP_CONST_ARCANE_SPELL_FAILURE_MINUS_20_PERCENT` | int | `6` |  |
| `IP_CONST_ARCANE_SPELL_FAILURE_MINUS_15_PERCENT` | int | `7` |  |
| `IP_CONST_ARCANE_SPELL_FAILURE_MINUS_10_PERCENT` | int | `8` |  |
| `IP_CONST_ARCANE_SPELL_FAILURE_MINUS_5_PERCENT` | int | `9` |  |
| `IP_CONST_ARCANE_SPELL_FAILURE_PLUS_5_PERCENT` | int | `10` |  |
| `IP_CONST_ARCANE_SPELL_FAILURE_PLUS_10_PERCENT` | int | `11` |  |
| `IP_CONST_ARCANE_SPELL_FAILURE_PLUS_15_PERCENT` | int | `12` |  |
| `IP_CONST_ARCANE_SPELL_FAILURE_PLUS_20_PERCENT` | int | `13` |  |
| `IP_CONST_ARCANE_SPELL_FAILURE_PLUS_25_PERCENT` | int | `14` |  |
| `IP_CONST_ARCANE_SPELL_FAILURE_PLUS_30_PERCENT` | int | `15` |  |
| `IP_CONST_ARCANE_SPELL_FAILURE_PLUS_35_PERCENT` | int | `16` |  |
| `IP_CONST_ARCANE_SPELL_FAILURE_PLUS_40_PERCENT` | int | `17` |  |
| `IP_CONST_ARCANE_SPELL_FAILURE_PLUS_45_PERCENT` | int | `18` |  |
| `IP_CONST_ARCANE_SPELL_FAILURE_PLUS_50_PERCENT` | int | `19` |  |
| `ACTION_MODE_DETECT` | int | `0` |  |
| `ACTION_MODE_STEALTH` | int | `1` |  |
| `ACTION_MODE_PARRY` | int | `2` |  |
| `ACTION_MODE_POWER_ATTACK` | int | `3` |  |
| `ACTION_MODE_IMPROVED_POWER_ATTACK` | int | `4` |  |
| `ACTION_MODE_COUNTERSPELL` | int | `5` |  |
| `ACTION_MODE_FLURRY_OF_BLOWS` | int | `6` |  |
| `ACTION_MODE_RAPID_SHOT` | int | `7` |  |
| `ACTION_MODE_EXPERTISE` | int | `8` |  |
| `ACTION_MODE_IMPROVED_EXPERTISE` | int | `9` |  |
| `ACTION_MODE_DEFENSIVE_CAST` | int | `10` |  |
| `ACTION_MODE_DIRTY_FIGHTING` | int | `11` |  |
| `ITEM_VISUAL_ACID` | int | `0` |  |
| `ITEM_VISUAL_COLD` | int | `1` |  |
| `ITEM_VISUAL_ELECTRICAL` | int | `2` |  |
| `ITEM_VISUAL_FIRE` | int | `3` |  |
| `ITEM_VISUAL_SONIC` | int | `4` |  |
| `ITEM_VISUAL_HOLY` | int | `5` |  |
| `ITEM_VISUAL_EVIL` | int | `6` |  |
| `SKYBOX_NONE` | int | `0` |  |
| `SKYBOX_GRASS_CLEAR` | int | `1` |  |
| `SKYBOX_GRASS_STORM` | int | `2` |  |
| `SKYBOX_DESERT_CLEAR` | int | `3` |  |
| `SKYBOX_WINTER_CLEAR` | int | `4` |  |
| `SKYBOX_ICY` | int | `5` |  |
| `FOG_TYPE_ALL` | int | `0` |  |
| `FOG_TYPE_SUN` | int | `1` |  |
| `FOG_TYPE_MOON` | int | `2` |  |
| `FOG_COLOR_RED` | int | `16711680` |  |
| `FOG_COLOR_RED_DARK` | int | `6684672` |  |
| `FOG_COLOR_GREEN` | int | `65280` |  |
| `FOG_COLOR_GREEN_DARK` | int | `23112` |  |
| `FOG_COLOR_BLUE` | int | `255` |  |
| `FOG_COLOR_BLUE_DARK` | int | `102` |  |
| `FOG_COLOR_BLACK` | int | `0` |  |
| `FOG_COLOR_WHITE` | int | `16777215` |  |
| `FOG_COLOR_GREY` | int | `10066329` |  |
| `FOG_COLOR_YELLOW` | int | `16776960` |  |
| `FOG_COLOR_YELLOW_DARK` | int | `11184640` |  |
| `FOG_COLOR_CYAN` | int | `65535` |  |
| `FOG_COLOR_MAGENTA` | int | `16711935` |  |
| `FOG_COLOR_ORANGE` | int | `16750848` |  |
| `FOG_COLOR_ORANGE_DARK` | int | `13395456` |  |
| `FOG_COLOR_BROWN` | int | `10053120` |  |
| `FOG_COLOR_BROWN_DARK` | int | `6697728` |  |
| `AREA_LIGHT_COLOR_MOON_AMBIENT` | int | `0` |  |
| `AREA_LIGHT_COLOR_MOON_DIFFUSE` | int | `1` |  |
| `AREA_LIGHT_COLOR_SUN_AMBIENT` | int | `2` |  |
| `AREA_LIGHT_COLOR_SUN_DIFFUSE` | int | `3` |  |
| `AREA_LIGHT_DIRECTION_MOON` | int | `0` |  |
| `AREA_LIGHT_DIRECTION_SUN` | int | `1` |  |
| `AMBIENT_SOUND_NONE` | int | `0` |  |
| `AMBIENT_SOUND_MEN_WHISPER_INSIDE` | int | `1` |  |
| `AMBIENT_SOUND_WOMEN_WHISPER_INSIDE` | int | `2` |  |
| `AMBIENT_SOUND_PEOPLE_WHISPER_INSIDE` | int | `3` |  |
| `AMBIENT_SOUND_SMALL_GROUP_TALKS_INSIDE` | int | `4` |  |
| `AMBIENT_SOUND_MEDIUM_GROUP_TALKS_INSIDE` | int | `5` |  |
| `AMBIENT_SOUND_LARGE_GROUP_TALKS_INSIDE` | int | `6` |  |
| `AMBIENT_SOUND_COMMONER_TAVERN_TALK` | int | `7` |  |
| `AMBIENT_SOUND_NOBLE_TAVERN_TALK` | int | `8` |  |
| `AMBIENT_SOUND_CITY_SLUMS_DAY_CROWDED` | int | `9` |  |
| `AMBIENT_SOUND_CITY_SLUMS_DAY_SPARSE` | int | `10` |  |
| `AMBIENT_SOUND_CITY_SLUMS_NIGHT` | int | `11` |  |
| `AMBIENT_SOUND_CITY_DAY_CROWDED` | int | `12` |  |
| `AMBIENT_SOUND_CITY_DAY_SPARSE` | int | `13` |  |
| `AMBIENT_SOUND_CITY_NIGHT` | int | `14` |  |
| `AMBIENT_SOUND_CITY_MARKET` | int | `15` |  |
| `AMBIENT_SOUND_CITY_TEMPLE_DISTRICT` | int | `16` |  |
| `AMBIENT_SOUND_TOWN_DAY_CROWDED` | int | `17` |  |
| `AMBIENT_SOUND_TOWN_DAY_SPARSE` | int | `18` |  |
| `AMBIENT_SOUND_TOWN_NIGHT` | int | `19` |  |
| `AMBIENT_SOUND_BORDELLO_WOMEN` | int | `20` |  |
| `AMBIENT_SOUND_BORDELLO_MEN_AND_WOMEN` | int | `21` |  |
| `AMBIENT_SOUND_RIOT_OUTSIDE` | int | `22` |  |
| `AMBIENT_SOUND_RIOT_MUFFLED` | int | `23` |  |
| `AMBIENT_SOUND_COMBAT_OUTSIDE_1` | int | `24` |  |
| `AMBIENT_SOUND_COMBAT_OUTSIDE_2` | int | `25` |  |
| `AMBIENT_SOUND_COMBAT_MUFFLED_1` | int | `26` |  |
| `AMBIENT_SOUND_COMBAT_MUFFLED_2` | int | `27` |  |
| `AMBIENT_SOUND_DUNGEON_LAKE_LAVA` | int | `28` |  |
| `AMBIENT_SOUND_SEWER_SLUDGE_LAKE` | int | `29` |  |
| `AMBIENT_SOUND_WIND_SOFT` | int | `30` |  |
| `AMBIENT_SOUND_WIND_MEDIUM` | int | `31` |  |
| `AMBIENT_SOUND_WIND_STRONG` | int | `32` |  |
| `AMBIENT_SOUND_WIND_FOREST` | int | `33` |  |
| `AMBIENT_SOUND_GUST_CHASM` | int | `34` |  |
| `AMBIENT_SOUND_GUST_CAVERN` | int | `35` |  |
| `AMBIENT_SOUND_GUST_GRASS` | int | `36` |  |
| `AMBIENT_SOUND_GUST_DRAFT` | int | `37` |  |
| `AMBIENT_SOUND_RAIN_LIGHT` | int | `38` |  |
| `AMBIENT_SOUND_RAIN_HARD` | int | `39` |  |
| `AMBIENT_SOUND_RAIN_STORM_SMALL` | int | `40` |  |
| `AMBIENT_SOUND_RAIN_STORM_BIG` | int | `41` |  |
| `AMBIENT_SOUND_CAVE_INSECTS_1` | int | `42` |  |
| `AMBIENT_SOUND_CAVE_INSECTS_2` | int | `43` |  |
| `AMBIENT_SOUND_INTERIOR_INSECTS_1` | int | `44` |  |
| `AMBIENT_SOUND_INTERIOR_INSECTS_2` | int | `45` |  |
| `AMBIENT_SOUND_LIZARD_FOLK_CAVE_CRYSTALS` | int | `46` |  |
| `AMBIENT_SOUND_SEWERS_1` | int | `47` |  |
| `AMBIENT_SOUND_SEWERS_2` | int | `48` |  |
| `AMBIENT_SOUND_FOREST_DAY_1` | int | `49` |  |
| `AMBIENT_SOUND_FOREST_DAY_2` | int | `50` |  |
| `AMBIENT_SOUND_FOREST_DAY_3` | int | `51` |  |
| `AMBIENT_SOUND_FOREST_DAY_SCARY` | int | `52` |  |
| `AMBIENT_SOUND_FOREST_NIGHT_1` | int | `53` |  |
| `AMBIENT_SOUND_FOREST_NIGHT_2` | int | `54` |  |
| `AMBIENT_SOUND_FOREST_NIGHT_SCARY` | int | `55` |  |
| `AMBIENT_SOUND_FOREST_MAGICAL` | int | `56` |  |
| `AMBIENT_SOUND_EVIL_DUNGEON_SMALL` | int | `57` |  |
| `AMBIENT_SOUND_EVIL_DUNGEON_MEDIUM` | int | `58` |  |
| `AMBIENT_SOUND_EVIL_DUNGEON_LARGE` | int | `59` |  |
| `AMBIENT_SOUND_CAVE_SMALL` | int | `60` |  |
| `AMBIENT_SOUND_CAVE_MEDIUM` | int | `61` |  |
| `AMBIENT_SOUND_CAVE_LARGE` | int | `62` |  |
| `AMBIENT_SOUND_MINE_SMALL` | int | `63` |  |
| `AMBIENT_SOUND_MINE_MEDIUM` | int | `64` |  |
| `AMBIENT_SOUND_MINE_LARGE` | int | `65` |  |
| `AMBIENT_SOUND_CASTLE_INTERIOR_SMALL` | int | `66` |  |
| `AMBIENT_SOUND_CASTLE_INTERIOR_MEDIUM` | int | `67` |  |
| `AMBIENT_SOUND_CASTLE_INTERIOR_LARGE` | int | `68` |  |
| `AMBIENT_SOUND_CRYPT_SMALL` | int | `69` |  |
| `AMBIENT_SOUND_CRYPT_MEDIUM_1` | int | `70` |  |
| `AMBIENT_SOUND_CRYPT_MEDIUM_2` | int | `71` |  |
| `AMBIENT_SOUND_HOUSE_INTERIOR_1` | int | `72` |  |
| `AMBIENT_SOUND_HOUSE_INTERIOR_2` | int | `73` |  |
| `AMBIENT_SOUND_HOUSE_INTERIOR_3` | int | `74` |  |
| `AMBIENT_SOUND_KITCHEN_INTERIOR_SMALL` | int | `75` |  |
| `AMBIENT_SOUND_KITCHEN_INTERIOR_LARGE` | int | `76` |  |
| `AMBIENT_SOUND_HAUNTED_INTERIOR_1` | int | `77` |  |
| `AMBIENT_SOUND_HAUNTED_INTERIOR_2` | int | `78` |  |
| `AMBIENT_SOUND_HAUNTED_INTERIOR_3` | int | `79` |  |
| `AMBIENT_SOUND_BLACK_SMITH` | int | `80` |  |
| `AMBIENT_SOUND_PIT_CRIES` | int | `81` |  |
| `AMBIENT_SOUND_MAGIC_INTERIOR_SMALL` | int | `82` |  |
| `AMBIENT_SOUND_MAGIC_INTERIOR_MEDIUM` | int | `83` |  |
| `AMBIENT_SOUND_MAGIC_INTERIOR_LARGE` | int | `84` |  |
| `AMBIENT_SOUND_MAGIC_INTERIOR_EVIL` | int | `85` |  |
| `AMBIENT_SOUND_MAGICAL_INTERIOR_FIRELAB` | int | `86` |  |
| `AMBIENT_SOUND_MAGICAL_INTERIOR_EARTHLAB` | int | `87` |  |
| `AMBIENT_SOUND_MAGICAL_INTERIOR_AIRLAB` | int | `88` |  |
| `AMBIENT_SOUND_MAGICAL_INTERIOR_WATERLAB` | int | `89` |  |
| `AMBIENT_SOUND_WINTER_DAY_WET_XP1` | int | `90` |  |
| `AMBIENT_SOUND_WINTER_DAY_WINDY_XP1` | int | `91` |  |
| `AMBIENT_SOUND_DESERT_DAY_XP1` | int | `92` |  |
| `AMBIENT_SOUND_DESERT_NIGHT_XP1` | int | `93` |  |
| `AMBIENT_SOUND_MONASTERY_INTERIOR_XP1` | int | `94` |  |
| `AMBIENT_SOUND_RUIN_WET_XP1` | int | `96` |  |
| `AMBIENT_SOUND_RUIN_RUMBLING_XP1` | int | `97` |  |
| `AMBIENT_SOUND_RUIN_HAUNTED_XP1` | int | `98` |  |
| `AMBIENT_SOUND_SAND_STORM_LIGHT_XP1` | int | `99` |  |
| `AMBIENT_SOUND_SAND_STORM_EXTREME_XP1` | int | `100` |  |
| `AMBIENT_SOUND_EVIL_DRONE_XP2` | int | `101` |  |
| `AMBIENT_SOUND_PLAIN_OF_FIRE_XP2` | int | `102` |  |
| `AMBIENT_SOUND_FROZEN_HELL_XP2` | int | `103` |  |
| `AMBIENT_SOUND_CAVE_EVIL_1_XP2` | int | `104` |  |
| `AMBIENT_SOUND_CAVE_EVIL_2_XP2` | int | `105` |  |
| `AMBIENT_SOUND_CAVE_EVIL_3_XP2` | int | `106` |  |
| `AMBIENT_SOUND_TAVERN_ROWDY` | int | `107` |  |
| `FOOTSTEP_TYPE_INVALID` | int | `-1` |  |
| `FOOTSTEP_TYPE_NORMAL` | int | `0` |  |
| `FOOTSTEP_TYPE_LARGE` | int | `1` |  |
| `FOOTSTEP_TYPE_DRAGON` | int | `2` |  |
| `FOOTSTEP_TYPE_SOFT` | int | `3` |  |
| `FOOTSTEP_TYPE_HOOF` | int | `4` |  |
| `FOOTSTEP_TYPE_HOOF_LARGE` | int | `5` |  |
| `FOOTSTEP_TYPE_BEETLE` | int | `6` |  |
| `FOOTSTEP_TYPE_SPIDER` | int | `7` |  |
| `FOOTSTEP_TYPE_SKELETON` | int | `8` |  |
| `FOOTSTEP_TYPE_LEATHER_WING` | int | `9` |  |
| `FOOTSTEP_TYPE_FEATHER_WING` | int | `10` |  |
| `FOOTSTEP_TYPE_NONE` | int | `12` |  |
| `FOOTSTEP_TYPE_SEAGULL` | int | `13` |  |
| `FOOTSTEP_TYPE_SHARK` | int | `14` |  |
| `FOOTSTEP_TYPE_WATER_NORMAL` | int | `15` |  |
| `FOOTSTEP_TYPE_WATER_LARGE` | int | `16` |  |
| `FOOTSTEP_TYPE_HORSE` | int | `17` |  |
| `FOOTSTEP_TYPE_DEFAULT` | int | `65535` |  |
| `CREATURE_WING_TYPE_NONE` | int | `0` |  |
| `CREATURE_WING_TYPE_DEMON` | int | `1` |  |
| `CREATURE_WING_TYPE_ANGEL` | int | `2` |  |
| `CREATURE_WING_TYPE_BAT` | int | `3` |  |
| `CREATURE_WING_TYPE_DRAGON` | int | `4` |  |
| `CREATURE_WING_TYPE_BUTTERFLY` | int | `5` |  |
| `CREATURE_WING_TYPE_BIRD` | int | `6` |  |
| `CREATURE_TAIL_TYPE_NONE` | int | `0` |  |
| `CREATURE_TAIL_TYPE_LIZARD` | int | `1` |  |
| `CREATURE_TAIL_TYPE_BONE` | int | `2` |  |
| `CREATURE_TAIL_TYPE_DEVIL` | int | `3` |  |
| `CREATURE_PART_RIGHT_FOOT` | int | `0` |  |
| `CREATURE_PART_LEFT_FOOT` | int | `1` |  |
| `CREATURE_PART_RIGHT_SHIN` | int | `2` |  |
| `CREATURE_PART_LEFT_SHIN` | int | `3` |  |
| `CREATURE_PART_LEFT_THIGH` | int | `4` |  |
| `CREATURE_PART_RIGHT_THIGH` | int | `5` |  |
| `CREATURE_PART_PELVIS` | int | `6` |  |
| `CREATURE_PART_TORSO` | int | `7` |  |
| `CREATURE_PART_BELT` | int | `8` |  |
| `CREATURE_PART_NECK` | int | `9` |  |
| `CREATURE_PART_RIGHT_FOREARM` | int | `10` |  |
| `CREATURE_PART_LEFT_FOREARM` | int | `11` |  |
| `CREATURE_PART_RIGHT_BICEP` | int | `12` |  |
| `CREATURE_PART_LEFT_BICEP` | int | `13` |  |
| `CREATURE_PART_RIGHT_SHOULDER` | int | `14` |  |
| `CREATURE_PART_LEFT_SHOULDER` | int | `15` |  |
| `CREATURE_PART_RIGHT_HAND` | int | `16` |  |
| `CREATURE_PART_LEFT_HAND` | int | `17` |  |
| `CREATURE_PART_HEAD` | int | `20` |  |
| `CREATURE_MODEL_TYPE_NONE` | int | `0` |  |
| `CREATURE_MODEL_TYPE_SKIN` | int | `1` |  |
| `CREATURE_MODEL_TYPE_TATTOO` | int | `2` |  |
| `CREATURE_MODEL_TYPE_UNDEAD` | int | `255` |  |
| `COLOR_CHANNEL_SKIN` | int | `0` |  |
| `COLOR_CHANNEL_HAIR` | int | `1` |  |
| `COLOR_CHANNEL_TATTOO_1` | int | `2` |  |
| `COLOR_CHANNEL_TATTOO_2` | int | `3` |  |
| `TILESET_RESREF_BEHOLDER_CAVES` | string | `"tib01"` |  |
| `TILESET_RESREF_CASTLE_INTERIOR` | string | `"tic01"` |  |
| `TILESET_RESREF_CITY_EXTERIOR` | string | `"tcn01"` |  |
| `TILESET_RESREF_CITY_INTERIOR` | string | `"tin01"` |  |
| `TILESET_RESREF_CRYPT` | string | `"tdc01"` |  |
| `TILESET_RESREF_DESERT` | string | `"ttd01"` |  |
| `TILESET_RESREF_DROW_INTERIOR` | string | `"tid01"` |  |
| `TILESET_RESREF_DUNGEON` | string | `"tde01"` |  |
| `TILESET_RESREF_FOREST` | string | `"ttf01"` |  |
| `TILESET_RESREF_FROZEN_WASTES` | string | `"tti01"` |  |
| `TILESET_RESREF_ILLITHID_INTERIOR` | string | `"tii01"` |  |
| `TILESET_RESREF_MICROSET` | string | `"tms01"` |  |
| `TILESET_RESREF_MINES_AND_CAVERNS` | string | `"tdm01"` |  |
| `TILESET_RESREF_RUINS` | string | `"tdr01"` |  |
| `TILESET_RESREF_RURAL` | string | `"ttr01"` |  |
| `TILESET_RESREF_RURAL_WINTER` | string | `"tts01"` |  |
| `TILESET_RESREF_SEWERS` | string | `"tds01"` |  |
| `TILESET_RESREF_UNDERDARK` | string | `"ttu01"` |  |
| `TILESET_RESREF_LIZARDFOLK_INTERIOR` | string | `"dag01"` |  |
| `TILESET_RESREF_MEDIEVAL_CITY_2` | string | `"tcm02"` |  |
| `TILESET_RESREF_MEDIEVAL_RURAL_2` | string | `"trm02"` |  |
| `TILESET_RESREF_EARLY_WINTER_2` | string | `"trs02"` |  |
| `TILESET_RESREF_SEASHIPS` | string | `"tss13"` |  |
| `TILESET_RESREF_FOREST_FACELIFT` | string | `"ttf02"` |  |
| `TILESET_RESREF_RURAL_WINTER_FACELIFT` | string | `"tts02"` |  |
| `TILESET_RESREF_STEAMWORKS` | string | `"tsw01"` |  |
| `TILESET_RESREF_BARROWS_INTERIOR` | string | `"tbw01"` |  |
| `TILESET_RESREF_SEA_CAVES` | string | `"tdt01"` |  |
| `TILESET_RESREF_CITY_INTERIOR_2` | string | `"tni01"` |  |
| `TILESET_RESREF_CASTLE_INTERIOR_2` | string | `"tni02"` |  |
| `TILESET_RESREF_CASTLE_EXTERIOR_RURAL` | string | `"tno01"` |  |
| `TILESET_RESREF_TROPICAL` | string | `"ttz01"` |  |
| `TILESET_RESREF_FORT_INTERIOR` | string | `"twc03"` |  |
| `NAME_FIRST_GENERIC_MALE` | int | `-1` |  |
| `NAME_ANIMAL` | int | `0` |  |
| `NAME_FAMILIAR` | int | `1` |  |
| `NAME_FIRST_DWARF_MALE` | int | `2` |  |
| `NAME_FIRST_DWARF_FEMALE` | int | `3` |  |
| `NAME_LAST_DWARF` | int | `4` |  |
| `NAME_FIRST_ELF_MALE` | int | `5` |  |
| `NAME_FIRST_ELF_FEMALE` | int | `6` |  |
| `NAME_LAST_ELF` | int | `7` |  |
| `NAME_FIRST_GNOME_MALE` | int | `8` |  |
| `NAME_FIRST_GNOME_FEMALE` | int | `9` |  |
| `NAME_LAST_GNOME` | int | `10` |  |
| `NAME_FIRST_HALFELF_MALE` | int | `11` |  |
| `NAME_FIRST_HALFELF_FEMALE` | int | `12` |  |
| `NAME_LAST_HALFELF` | int | `13` |  |
| `NAME_FIRST_HALFLING_MALE` | int | `14` |  |
| `NAME_FIRST_HALFLING_FEMALE` | int | `15` |  |
| `NAME_LAST_HALFLING` | int | `16` |  |
| `NAME_FIRST_HALFORC_MALE` | int | `17` |  |
| `NAME_FIRST_HALFORC_FEMALE` | int | `18` |  |
| `NAME_LAST_HALFORC` | int | `19` |  |
| `NAME_FIRST_HUMAN_MALE` | int | `20` |  |
| `NAME_FIRST_HUMAN_FEMALE` | int | `21` |  |
| `NAME_LAST_HUMAN` | int | `22` |  |
| `EVENT_SCRIPT_MODULE_ON_HEARTBEAT` | int | `3000` |  |
| `EVENT_SCRIPT_MODULE_ON_USER_DEFINED_EVENT` | int | `3001` |  |
| `EVENT_SCRIPT_MODULE_ON_MODULE_LOAD` | int | `3002` |  |
| `EVENT_SCRIPT_MODULE_ON_MODULE_START` | int | `3003` |  |
| `EVENT_SCRIPT_MODULE_ON_CLIENT_ENTER` | int | `3004` |  |
| `EVENT_SCRIPT_MODULE_ON_CLIENT_EXIT` | int | `3005` |  |
| `EVENT_SCRIPT_MODULE_ON_ACTIVATE_ITEM` | int | `3006` |  |
| `EVENT_SCRIPT_MODULE_ON_ACQUIRE_ITEM` | int | `3007` |  |
| `EVENT_SCRIPT_MODULE_ON_LOSE_ITEM` | int | `3008` |  |
| `EVENT_SCRIPT_MODULE_ON_PLAYER_DEATH` | int | `3009` |  |
| `EVENT_SCRIPT_MODULE_ON_PLAYER_DYING` | int | `3010` |  |
| `EVENT_SCRIPT_MODULE_ON_RESPAWN_BUTTON_PRESSED` | int | `3011` |  |
| `EVENT_SCRIPT_MODULE_ON_PLAYER_REST` | int | `3012` |  |
| `EVENT_SCRIPT_MODULE_ON_PLAYER_LEVEL_UP` | int | `3013` |  |
| `EVENT_SCRIPT_MODULE_ON_PLAYER_CANCEL_CUTSCENE` | int | `3014` |  |
| `EVENT_SCRIPT_MODULE_ON_EQUIP_ITEM` | int | `3015` |  |
| `EVENT_SCRIPT_MODULE_ON_UNEQUIP_ITEM` | int | `3016` |  |
| `EVENT_SCRIPT_MODULE_ON_PLAYER_CHAT` | int | `3017` |  |
| `EVENT_SCRIPT_MODULE_ON_PLAYER_TARGET` | int | `3018` |  |
| `EVENT_SCRIPT_MODULE_ON_PLAYER_GUIEVENT` | int | `3019` |  |
| `EVENT_SCRIPT_MODULE_ON_PLAYER_TILE_ACTION` | int | `3020` |  |
| `EVENT_SCRIPT_MODULE_ON_NUI_EVENT` | int | `3021` |  |
| `EVENT_SCRIPT_AREA_ON_HEARTBEAT` | int | `4000` |  |
| `EVENT_SCRIPT_AREA_ON_USER_DEFINED_EVENT` | int | `4001` |  |
| `EVENT_SCRIPT_AREA_ON_ENTER` | int | `4002` |  |
| `EVENT_SCRIPT_AREA_ON_EXIT` | int | `4003` |  |
| `EVENT_SCRIPT_AREAOFEFFECT_ON_HEARTBEAT` | int | `11000` |  |
| `EVENT_SCRIPT_AREAOFEFFECT_ON_USER_DEFINED_EVENT` | int | `11001` |  |
| `EVENT_SCRIPT_AREAOFEFFECT_ON_OBJECT_ENTER` | int | `11002` |  |
| `EVENT_SCRIPT_AREAOFEFFECT_ON_OBJECT_EXIT` | int | `11003` |  |
| `EVENT_SCRIPT_CREATURE_ON_HEARTBEAT` | int | `5000` |  |
| `EVENT_SCRIPT_CREATURE_ON_NOTICE` | int | `5001` |  |
| `EVENT_SCRIPT_CREATURE_ON_SPELLCASTAT` | int | `5002` |  |
| `EVENT_SCRIPT_CREATURE_ON_MELEE_ATTACKED` | int | `5003` |  |
| `EVENT_SCRIPT_CREATURE_ON_DAMAGED` | int | `5004` |  |
| `EVENT_SCRIPT_CREATURE_ON_DISTURBED` | int | `5005` |  |
| `EVENT_SCRIPT_CREATURE_ON_END_COMBATROUND` | int | `5006` |  |
| `EVENT_SCRIPT_CREATURE_ON_DIALOGUE` | int | `5007` |  |
| `EVENT_SCRIPT_CREATURE_ON_SPAWN_IN` | int | `5008` |  |
| `EVENT_SCRIPT_CREATURE_ON_RESTED` | int | `5009` |  |
| `EVENT_SCRIPT_CREATURE_ON_DEATH` | int | `5010` |  |
| `EVENT_SCRIPT_CREATURE_ON_USER_DEFINED_EVENT` | int | `5011` |  |
| `EVENT_SCRIPT_CREATURE_ON_BLOCKED_BY_DOOR` | int | `5012` |  |
| `EVENT_SCRIPT_TRIGGER_ON_HEARTBEAT` | int | `7000` |  |
| `EVENT_SCRIPT_TRIGGER_ON_OBJECT_ENTER` | int | `7001` |  |
| `EVENT_SCRIPT_TRIGGER_ON_OBJECT_EXIT` | int | `7002` |  |
| `EVENT_SCRIPT_TRIGGER_ON_USER_DEFINED_EVENT` | int | `7003` |  |
| `EVENT_SCRIPT_TRIGGER_ON_TRAPTRIGGERED` | int | `7004` |  |
| `EVENT_SCRIPT_TRIGGER_ON_DISARMED` | int | `7005` |  |
| `EVENT_SCRIPT_TRIGGER_ON_CLICKED` | int | `7006` |  |
| `EVENT_SCRIPT_PLACEABLE_ON_CLOSED` | int | `9000` |  |
| `EVENT_SCRIPT_PLACEABLE_ON_DAMAGED` | int | `9001` |  |
| `EVENT_SCRIPT_PLACEABLE_ON_DEATH` | int | `9002` |  |
| `EVENT_SCRIPT_PLACEABLE_ON_DISARM` | int | `9003` |  |
| `EVENT_SCRIPT_PLACEABLE_ON_HEARTBEAT` | int | `9004` |  |
| `EVENT_SCRIPT_PLACEABLE_ON_INVENTORYDISTURBED` | int | `9005` |  |
| `EVENT_SCRIPT_PLACEABLE_ON_LOCK` | int | `9006` |  |
| `EVENT_SCRIPT_PLACEABLE_ON_MELEEATTACKED` | int | `9007` |  |
| `EVENT_SCRIPT_PLACEABLE_ON_OPEN` | int | `9008` |  |
| `EVENT_SCRIPT_PLACEABLE_ON_SPELLCASTAT` | int | `9009` |  |
| `EVENT_SCRIPT_PLACEABLE_ON_TRAPTRIGGERED` | int | `9010` |  |
| `EVENT_SCRIPT_PLACEABLE_ON_UNLOCK` | int | `9011` |  |
| `EVENT_SCRIPT_PLACEABLE_ON_USED` | int | `9012` |  |
| `EVENT_SCRIPT_PLACEABLE_ON_USER_DEFINED_EVENT` | int | `9013` |  |
| `EVENT_SCRIPT_PLACEABLE_ON_DIALOGUE` | int | `9014` |  |
| `EVENT_SCRIPT_PLACEABLE_ON_LEFT_CLICK` | int | `9015` |  |
| `EVENT_SCRIPT_DOOR_ON_OPEN` | int | `10000` |  |
| `EVENT_SCRIPT_DOOR_ON_CLOSE` | int | `10001` |  |
| `EVENT_SCRIPT_DOOR_ON_DAMAGE` | int | `10002` |  |
| `EVENT_SCRIPT_DOOR_ON_DEATH` | int | `10003` |  |
| `EVENT_SCRIPT_DOOR_ON_DISARM` | int | `10004` |  |
| `EVENT_SCRIPT_DOOR_ON_HEARTBEAT` | int | `10005` |  |
| `EVENT_SCRIPT_DOOR_ON_LOCK` | int | `10006` |  |
| `EVENT_SCRIPT_DOOR_ON_MELEE_ATTACKED` | int | `10007` |  |
| `EVENT_SCRIPT_DOOR_ON_SPELLCASTAT` | int | `10008` |  |
| `EVENT_SCRIPT_DOOR_ON_TRAPTRIGGERED` | int | `10009` |  |
| `EVENT_SCRIPT_DOOR_ON_UNLOCK` | int | `10010` |  |
| `EVENT_SCRIPT_DOOR_ON_USERDEFINED` | int | `10011` |  |
| `EVENT_SCRIPT_DOOR_ON_CLICKED` | int | `10012` |  |
| `EVENT_SCRIPT_DOOR_ON_DIALOGUE` | int | `10013` |  |
| `EVENT_SCRIPT_DOOR_ON_FAIL_TO_OPEN` | int | `10014` |  |
| `EVENT_SCRIPT_ENCOUNTER_ON_OBJECT_ENTER` | int | `13000` |  |
| `EVENT_SCRIPT_ENCOUNTER_ON_OBJECT_EXIT` | int | `13001` |  |
| `EVENT_SCRIPT_ENCOUNTER_ON_HEARTBEAT` | int | `13002` |  |
| `EVENT_SCRIPT_ENCOUNTER_ON_ENCOUNTER_EXHAUSTED` | int | `13003` |  |
| `EVENT_SCRIPT_ENCOUNTER_ON_USER_DEFINED_EVENT` | int | `13004` |  |
| `EVENT_SCRIPT_STORE_ON_OPEN` | int | `14000` |  |
| `EVENT_SCRIPT_STORE_ON_CLOSE` | int | `14001` |  |
| `OBJECT_VISUAL_TRANSFORM_SCALE` | int | `10` |  |
| `OBJECT_VISUAL_TRANSFORM_ROTATE_X` | int | `21` |  |
| `OBJECT_VISUAL_TRANSFORM_ROTATE_Y` | int | `22` |  |
| `OBJECT_VISUAL_TRANSFORM_ROTATE_Z` | int | `23` |  |
| `OBJECT_VISUAL_TRANSFORM_TRANSLATE_X` | int | `31` |  |
| `OBJECT_VISUAL_TRANSFORM_TRANSLATE_Y` | int | `32` |  |
| `OBJECT_VISUAL_TRANSFORM_TRANSLATE_Z` | int | `33` |  |
| `OBJECT_VISUAL_TRANSFORM_ANIMATION_SPEED` | int | `40` |  |
| `OBJECT_VISUAL_TRANSFORM_LERP_NONE` | int | `0` | 1 |
| `OBJECT_VISUAL_TRANSFORM_LERP_LINEAR` | int | `1` | x |
| `OBJECT_VISUAL_TRANSFORM_LERP_SMOOTHSTEP` | int | `2` | x * x * (3 - 2 * x) |
| `OBJECT_VISUAL_TRANSFORM_LERP_INVERSE_SMOOTHSTEP` | int | `3` | 0.5 - sin(asin(1.0 - 2.0 * x) / 3.0) |
| `OBJECT_VISUAL_TRANSFORM_LERP_EASE_IN` | int | `4` | (1 - cosf(x * M_PI * 0.5)) |
| `OBJECT_VISUAL_TRANSFORM_LERP_EASE_OUT` | int | `5` | sinf(x * M_PI * 0.5) |
| `OBJECT_VISUAL_TRANSFORM_LERP_QUADRATIC` | int | `6` | x * x |
| `OBJECT_VISUAL_TRANSFORM_LERP_SMOOTHERSTEP` | int | `7` | (x * x * x * (x * (6.0 * x - 15.0) + 10.0)) |
| `OBJECT_VISUAL_TRANSFORM_DATA_SCOPE_BASE` | int | `0` |  |
| `OBJECT_VISUAL_TRANSFORM_DATA_SCOPE_CREATURE_HEAD` | int | `254` |  |
| `OBJECT_VISUAL_TRANSFORM_DATA_SCOPE_CREATURE_TAIL` | int | `253` |  |
| `OBJECT_VISUAL_TRANSFORM_DATA_SCOPE_CREATURE_WINGS` | int | `252` |  |
| `OBJECT_VISUAL_TRANSFORM_DATA_SCOPE_CREATURE_CLOAK` | int | `243` |  |
| `OBJECT_VISUAL_TRANSFORM_DATA_SCOPE_ITEM_PART1` | int | `255` |  |
| `OBJECT_VISUAL_TRANSFORM_DATA_SCOPE_ITEM_PART2` | int | `254` |  |
| `OBJECT_VISUAL_TRANSFORM_DATA_SCOPE_ITEM_PART3` | int | `253` |  |
| `OBJECT_VISUAL_TRANSFORM_DATA_SCOPE_ITEM_PART4` | int | `252` |  |
| `OBJECT_VISUAL_TRANSFORM_DATA_SCOPE_ITEM_PART5` | int | `251` |  |
| `OBJECT_VISUAL_TRANSFORM_BEHAVIOR_DEFAULT` | int | `0` | no special behavior |
| `OBJECT_VISUAL_TRANSFORM_BEHAVIOR_BOUNCE` | int | `1` | when repeating a lerp, swap to and from states |
| `VIBRATOR_MOTOR_ANY` | int | `0` |  |
| `VIBRATOR_MOTOR_LEFT` | int | `1` |  |
| `VIBRATOR_MOTOR_RIGHT` | int | `2` |  |
| `SCREEN_ANCHOR_TOP_LEFT` | int | `0` |  |
| `SCREEN_ANCHOR_TOP_RIGHT` | int | `1` |  |
| `SCREEN_ANCHOR_BOTTOM_LEFT` | int | `2` |  |
| `SCREEN_ANCHOR_BOTTOM_RIGHT` | int | `3` |  |
| `SCREEN_ANCHOR_CENTER` | int | `4` |  |
| `DOMAIN_AIR` | int | `0` |  |
| `DOMAIN_ANIMAL` | int | `1` |  |
| `DOMAIN_DEATH` | int | `3` |  |
| `DOMAIN_DESTRUCTION` | int | `4` |  |
| `DOMAIN_EARTH` | int | `5` |  |
| `DOMAIN_EVIL` | int | `6` |  |
| `DOMAIN_FIRE` | int | `7` |  |
| `DOMAIN_GOOD` | int | `8` |  |
| `DOMAIN_HEALING` | int | `9` |  |
| `DOMAIN_KNOWLEDGE` | int | `10` |  |
| `DOMAIN_MAGIC` | int | `13` |  |
| `DOMAIN_PLANT` | int | `14` |  |
| `DOMAIN_PROTECTION` | int | `15` |  |
| `DOMAIN_STRENGTH` | int | `16` |  |
| `DOMAIN_SUN` | int | `17` |  |
| `DOMAIN_TRAVEL` | int | `18` |  |
| `DOMAIN_TRICKERY` | int | `19` |  |
| `DOMAIN_WAR` | int | `20` |  |
| `DOMAIN_WATER` | int | `21` |  |
| `MOUSECURSOR_DEFAULT` | int | `1` |  |
| `MOUSECURSOR_DEFAULT_DOWN` | int | `2` |  |
| `MOUSECURSOR_WALK` | int | `3` |  |
| `MOUSECURSOR_WALK_DOWN` | int | `4` |  |
| `MOUSECURSOR_NOWALK` | int | `5` |  |
| `MOUSECURSOR_NOWALK_DOWN` | int | `6` |  |
| `MOUSECURSOR_ATTACK` | int | `7` |  |
| `MOUSECURSOR_ATTACK_DOWN` | int | `8` |  |
| `MOUSECURSOR_NOATTACK` | int | `9` |  |
| `MOUSECURSOR_NOATTACK_DOWN` | int | `10` |  |
| `MOUSECURSOR_TALK` | int | `11` |  |
| `MOUSECURSOR_TALK_DOWN` | int | `12` |  |
| `MOUSECURSOR_NOTALK` | int | `13` |  |
| `MOUSECURSOR_NOTALK_DOWN` | int | `14` |  |
| `MOUSECURSOR_FOLLOW` | int | `15` |  |
| `MOUSECURSOR_FOLLOW_DOWN` | int | `16` |  |
| `MOUSECURSOR_EXAMINE` | int | `17` |  |
| `MOUSECURSOR_EXAMINE_DOWN` | int | `18` |  |
| `MOUSECURSOR_NOEXAMINE` | int | `19` |  |
| `MOUSECURSOR_NOEXAMINE_DOWN` | int | `20` |  |
| `MOUSECURSOR_TRANSITION` | int | `21` |  |
| `MOUSECURSOR_TRANSITION_DOWN` | int | `22` |  |
| `MOUSECURSOR_DOOR` | int | `23` |  |
| `MOUSECURSOR_DOOR_DOWN` | int | `24` |  |
| `MOUSECURSOR_USE` | int | `25` |  |
| `MOUSECURSOR_USE_DOWN` | int | `26` |  |
| `MOUSECURSOR_NOUSE` | int | `27` |  |
| `MOUSECURSOR_NOUSE_DOWN` | int | `28` |  |
| `MOUSECURSOR_MAGIC` | int | `29` |  |
| `MOUSECURSOR_MAGIC_DOWN` | int | `30` |  |
| `MOUSECURSOR_NOMAGIC` | int | `31` |  |
| `MOUSECURSOR_NOMAGIC_DOWN` | int | `32` |  |
| `MOUSECURSOR_DISARM` | int | `33` |  |
| `MOUSECURSOR_DISARM_DOWN` | int | `34` |  |
| `MOUSECURSOR_NODISARM` | int | `35` |  |
| `MOUSECURSOR_NODISARM_DOWN` | int | `36` |  |
| `MOUSECURSOR_ACTION` | int | `37` |  |
| `MOUSECURSOR_ACTION_DOWN` | int | `38` |  |
| `MOUSECURSOR_NOACTION` | int | `39` |  |
| `MOUSECURSOR_NOACTION_DOWN` | int | `40` |  |
| `MOUSECURSOR_LOCK` | int | `41` |  |
| `MOUSECURSOR_LOCK_DOWN` | int | `42` |  |
| `MOUSECURSOR_NOLOCK` | int | `43` |  |
| `MOUSECURSOR_NOLOCK_DOWN` | int | `44` |  |
| `MOUSECURSOR_PUSHPIN` | int | `45` |  |
| `MOUSECURSOR_PUSHPIN_DOWN` | int | `46` |  |
| `MOUSECURSOR_CREATE` | int | `47` |  |
| `MOUSECURSOR_CREATE_DOWN` | int | `48` |  |
| `MOUSECURSOR_NOCREATE` | int | `49` |  |
| `MOUSECURSOR_NOCREATE_DOWN` | int | `50` |  |
| `MOUSECURSOR_KILL` | int | `51` |  |
| `MOUSECURSOR_KILL_DOWN` | int | `52` |  |
| `MOUSECURSOR_NOKILL` | int | `53` |  |
| `MOUSECURSOR_NOKILL_DOWN` | int | `54` |  |
| `MOUSECURSOR_HEAL` | int | `55` |  |
| `MOUSECURSOR_HEAL_DOWN` | int | `56` |  |
| `MOUSECURSOR_NOHEAL` | int | `57` |  |
| `MOUSECURSOR_NOHEAL_DOWN` | int | `58` |  |
| `MOUSECURSOR_RUNARROW` | int | `59` |  |
| `MOUSECURSOR_WALKARROW` | int | `75` |  |
| `MOUSECURSOR_PICKUP` | int | `91` |  |
| `MOUSECURSOR_PICKUP_DOWN` | int | `92` |  |
| `MOUSECURSOR_CUSTOM_00` | int | `93` | gui_mp_custom00u |
| `MOUSECURSOR_CUSTOM_00_DOWN` | int | `94` | gui_mp_custom00d |
| `MOUSECURSOR_CUSTOM_99` | int | `291` | gui_mp_custom99u |
| `MOUSECURSOR_CUSTOM_99_DOWN` | int | `292` | gui_mp_custom99d |
| `CASSOWARY_STRENGTH_WEAK` | float | `1.0` |  |
| `CASSOWARY_STRENGTH_MEDIUM` | float | `1000.0` |  |
| `CASSOWARY_STRENGTH_STRONG` | float | `1000000.0` |  |
| `CASSOWARY_STRENGTH_REQUIRED` | float | `1001001000.0` |  |
| `RUNSCRIPT_EFFECT_SCRIPT_TYPE_ON_APPLIED` | int | `1` |  |
| `RUNSCRIPT_EFFECT_SCRIPT_TYPE_ON_REMOVED` | int | `2` |  |
| `RUNSCRIPT_EFFECT_SCRIPT_TYPE_ON_INTERVAL` | int | `3` |  |
| `EFFECT_ICON_INVALID` | int | `0` |  |
| `EFFECT_ICON_DAMAGE_RESISTANCE` | int | `1` |  |
| `EFFECT_ICON_REGENERATE` | int | `2` |  |
| `EFFECT_ICON_DAMAGE_REDUCTION` | int | `3` |  |
| `EFFECT_ICON_TEMPORARY_HITPOINTS` | int | `4` |  |
| `EFFECT_ICON_ENTANGLE` | int | `5` |  |
| `EFFECT_ICON_INVULNERABLE` | int | `6` |  |
| `EFFECT_ICON_DEAF` | int | `7` |  |
| `EFFECT_ICON_FATIGUE` | int | `8` |  |
| `EFFECT_ICON_IMMUNITY` | int | `9` |  |
| `EFFECT_ICON_BLIND` | int | `10` |  |
| `EFFECT_ICON_ENEMY_ATTACK_BONUS` | int | `11` |  |
| `EFFECT_ICON_CHARMED` | int | `12` |  |
| `EFFECT_ICON_CONFUSED` | int | `13` |  |
| `EFFECT_ICON_FRIGHTENED` | int | `14` |  |
| `EFFECT_ICON_DOMINATED` | int | `15` |  |
| `EFFECT_ICON_PARALYZE` | int | `16` |  |
| `EFFECT_ICON_DAZED` | int | `17` |  |
| `EFFECT_ICON_STUNNED` | int | `18` |  |
| `EFFECT_ICON_SLEEP` | int | `19` |  |
| `EFFECT_ICON_POISON` | int | `20` |  |
| `EFFECT_ICON_DISEASE` | int | `21` |  |
| `EFFECT_ICON_CURSE` | int | `22` |  |
| `EFFECT_ICON_SILENCE` | int | `23` |  |
| `EFFECT_ICON_TURNED` | int | `24` |  |
| `EFFECT_ICON_HASTE` | int | `25` |  |
| `EFFECT_ICON_SLOW` | int | `26` |  |
| `EFFECT_ICON_ABILITY_INCREASE_STR` | int | `27` |  |
| `EFFECT_ICON_ABILITY_DECREASE_STR` | int | `28` |  |
| `EFFECT_ICON_ATTACK_INCREASE` | int | `29` |  |
| `EFFECT_ICON_ATTACK_DECREASE` | int | `30` |  |
| `EFFECT_ICON_DAMAGE_INCREASE` | int | `31` |  |
| `EFFECT_ICON_DAMAGE_DECREASE` | int | `32` |  |
| `EFFECT_ICON_DAMAGE_IMMUNITY_INCREASE` | int | `33` |  |
| `EFFECT_ICON_DAMAGE_IMMUNITY_DECREASE` | int | `34` |  |
| `EFFECT_ICON_AC_INCREASE` | int | `35` |  |
| `EFFECT_ICON_AC_DECREASE` | int | `36` |  |
| `EFFECT_ICON_MOVEMENT_SPEED_INCREASE` | int | `37` |  |
| `EFFECT_ICON_MOVEMENT_SPEED_DECREASE` | int | `38` |  |
| `EFFECT_ICON_SAVING_THROW_INCREASE` | int | `39` |  |
| `EFFECT_ICON_SAVING_THROW_DECREASE` | int | `40` |  |
| `EFFECT_ICON_SPELL_RESISTANCE_INCREASE` | int | `41` |  |
| `EFFECT_ICON_SPELL_RESISTANCE_DECREASE` | int | `42` |  |
| `EFFECT_ICON_SKILL_INCREASE` | int | `43` |  |
| `EFFECT_ICON_SKILL_DECREASE` | int | `44` |  |
| `EFFECT_ICON_INVISIBILITY` | int | `45` |  |
| `EFFECT_ICON_IMPROVEDINVISIBILITY` | int | `46` |  |
| `EFFECT_ICON_DARKNESS` | int | `47` |  |
| `EFFECT_ICON_DISPELMAGICALL` | int | `48` |  |
| `EFFECT_ICON_ELEMENTALSHIELD` | int | `49` |  |
| `EFFECT_ICON_LEVELDRAIN` | int | `50` |  |
| `EFFECT_ICON_POLYMORPH` | int | `51` |  |
| `EFFECT_ICON_SANCTUARY` | int | `52` |  |
| `EFFECT_ICON_TRUESEEING` | int | `53` |  |
| `EFFECT_ICON_SEEINVISIBILITY` | int | `54` |  |
| `EFFECT_ICON_TIMESTOP` | int | `55` |  |
| `EFFECT_ICON_BLINDNESS` | int | `56` |  |
| `EFFECT_ICON_SPELLLEVELABSORPTION` | int | `57` |  |
| `EFFECT_ICON_DISPELMAGICBEST` | int | `58` |  |
| `EFFECT_ICON_ABILITY_INCREASE_DEX` | int | `59` |  |
| `EFFECT_ICON_ABILITY_DECREASE_DEX` | int | `60` |  |
| `EFFECT_ICON_ABILITY_INCREASE_CON` | int | `61` |  |
| `EFFECT_ICON_ABILITY_DECREASE_CON` | int | `62` |  |
| `EFFECT_ICON_ABILITY_INCREASE_INT` | int | `63` |  |
| `EFFECT_ICON_ABILITY_DECREASE_INT` | int | `64` |  |
| `EFFECT_ICON_ABILITY_INCREASE_WIS` | int | `65` |  |
| `EFFECT_ICON_ABILITY_DECREASE_WIS` | int | `66` |  |
| `EFFECT_ICON_ABILITY_INCREASE_CHA` | int | `67` |  |
| `EFFECT_ICON_ABILITY_DECREASE_CHA` | int | `68` |  |
| `EFFECT_ICON_IMMUNITY_ALL` | int | `69` |  |
| `EFFECT_ICON_IMMUNITY_MIND` | int | `70` |  |
| `EFFECT_ICON_IMMUNITY_POISON` | int | `71` |  |
| `EFFECT_ICON_IMMUNITY_DISEASE` | int | `72` |  |
| `EFFECT_ICON_IMMUNITY_FEAR` | int | `73` |  |
| `EFFECT_ICON_IMMUNITY_TRAP` | int | `74` |  |
| `EFFECT_ICON_IMMUNITY_PARALYSIS` | int | `75` |  |
| `EFFECT_ICON_IMMUNITY_BLINDNESS` | int | `76` |  |
| `EFFECT_ICON_IMMUNITY_DEAFNESS` | int | `77` |  |
| `EFFECT_ICON_IMMUNITY_SLOW` | int | `78` |  |
| `EFFECT_ICON_IMMUNITY_ENTANGLE` | int | `79` |  |
| `EFFECT_ICON_IMMUNITY_SILENCE` | int | `80` |  |
| `EFFECT_ICON_IMMUNITY_STUN` | int | `81` |  |
| `EFFECT_ICON_IMMUNITY_SLEEP` | int | `82` |  |
| `EFFECT_ICON_IMMUNITY_CHARM` | int | `83` |  |
| `EFFECT_ICON_IMMUNITY_DOMINATE` | int | `84` |  |
| `EFFECT_ICON_IMMUNITY_CONFUSE` | int | `85` |  |
| `EFFECT_ICON_IMMUNITY_CURSE` | int | `86` |  |
| `EFFECT_ICON_IMMUNITY_DAZED` | int | `87` |  |
| `EFFECT_ICON_IMMUNITY_ABILITY_DECREASE` | int | `88` |  |
| `EFFECT_ICON_IMMUNITY_ATTACK_DECREASE` | int | `89` |  |
| `EFFECT_ICON_IMMUNITY_DAMAGE_DECREASE` | int | `90` |  |
| `EFFECT_ICON_IMMUNITY_DAMAGE_IMMUNITY_DECREASE` | int | `91` |  |
| `EFFECT_ICON_IMMUNITY_AC_DECREASE` | int | `92` |  |
| `EFFECT_ICON_IMMUNITY_MOVEMENT_SPEED_DECREASE` | int | `93` |  |
| `EFFECT_ICON_IMMUNITY_SAVING_THROW_DECREASE` | int | `94` |  |
| `EFFECT_ICON_IMMUNITY_SPELL_RESISTANCE_DECREASE` | int | `95` |  |
| `EFFECT_ICON_IMMUNITY_SKILL_DECREASE` | int | `96` |  |
| `EFFECT_ICON_IMMUNITY_KNOCKDOWN` | int | `97` |  |
| `EFFECT_ICON_IMMUNITY_NEGATIVE_LEVEL` | int | `98` |  |
| `EFFECT_ICON_IMMUNITY_SNEAK_ATTACK` | int | `99` |  |
| `EFFECT_ICON_IMMUNITY_CRITICAL_HIT` | int | `100` |  |
| `EFFECT_ICON_IMMUNITY_DEATH_MAGIC` | int | `101` |  |
| `EFFECT_ICON_REFLEX_SAVE_INCREASED` | int | `102` |  |
| `EFFECT_ICON_FORT_SAVE_INCREASED` | int | `103` |  |
| `EFFECT_ICON_WILL_SAVE_INCREASED` | int | `104` |  |
| `EFFECT_ICON_TAUNTED` | int | `105` |  |
| `EFFECT_ICON_SPELLIMMUNITY` | int | `106` |  |
| `EFFECT_ICON_ETHEREALNESS` | int | `107` |  |
| `EFFECT_ICON_CONCEALMENT` | int | `108` |  |
| `EFFECT_ICON_PETRIFIED` | int | `109` |  |
| `EFFECT_ICON_EFFECT_SPELL_FAILURE` | int | `110` |  |
| `EFFECT_ICON_DAMAGE_IMMUNITY_MAGIC` | int | `111` |  |
| `EFFECT_ICON_DAMAGE_IMMUNITY_ACID` | int | `112` |  |
| `EFFECT_ICON_DAMAGE_IMMUNITY_COLD` | int | `113` |  |
| `EFFECT_ICON_DAMAGE_IMMUNITY_DIVINE` | int | `114` |  |
| `EFFECT_ICON_DAMAGE_IMMUNITY_ELECTRICAL` | int | `115` |  |
| `EFFECT_ICON_DAMAGE_IMMUNITY_FIRE` | int | `116` |  |
| `EFFECT_ICON_DAMAGE_IMMUNITY_NEGATIVE` | int | `117` |  |
| `EFFECT_ICON_DAMAGE_IMMUNITY_POSITIVE` | int | `118` |  |
| `EFFECT_ICON_DAMAGE_IMMUNITY_SONIC` | int | `119` |  |
| `EFFECT_ICON_DAMAGE_IMMUNITY_MAGIC_DECREASE` | int | `120` |  |
| `EFFECT_ICON_DAMAGE_IMMUNITY_ACID_DECREASE` | int | `121` |  |
| `EFFECT_ICON_DAMAGE_IMMUNITY_COLD_DECREASE` | int | `122` |  |
| `EFFECT_ICON_DAMAGE_IMMUNITY_DIVINE_DECREASE` | int | `123` |  |
| `EFFECT_ICON_DAMAGE_IMMUNITY_ELECTRICAL_DECREASE` | int | `124` |  |
| `EFFECT_ICON_DAMAGE_IMMUNITY_FIRE_DECREASE` | int | `125` |  |
| `EFFECT_ICON_DAMAGE_IMMUNITY_NEGATIVE_DECREASE` | int | `126` |  |
| `EFFECT_ICON_DAMAGE_IMMUNITY_POSITIVE_DECREASE` | int | `127` |  |
| `EFFECT_ICON_DAMAGE_IMMUNITY_SONIC_DECREASE` | int | `128` |  |
| `EFFECT_ICON_WOUNDING` | int | `129` |  |
| `GUIEVENT_CHATBAR_FOCUS` | int | `1` |  |
| `GUIEVENT_CHATBAR_UNFOCUS` | int | `2` |  |
| `GUIEVENT_CHARACTERSHEET_SKILL_CLICK` | int | `3` |  |
| `GUIEVENT_CHARACTERSHEET_FEAT_CLICK` | int | `4` |  |
| `GUIEVENT_EFFECTICON_CLICK` | int | `5` |  |
| `GUIEVENT_DEATHPANEL_WAITFORHELP_CLICK` | int | `6` |  |
| `GUIEVENT_MINIMAP_MAPPIN_CLICK` | int | `7` |  |
| `GUIEVENT_MINIMAP_OPEN` | int | `8` |  |
| `GUIEVENT_MINIMAP_CLOSE` | int | `9` |  |
| `GUIEVENT_JOURNAL_OPEN` | int | `10` |  |
| `GUIEVENT_JOURNAL_CLOSE` | int | `11` |  |
| `GUIEVENT_PLAYERLIST_PLAYER_CLICK` | int | `12` |  |
| `GUIEVENT_PARTYBAR_PORTRAIT_CLICK` | int | `13` |  |
| `GUIEVENT_DISABLED_PANEL_ATTEMPT_OPEN` | int | `14` |  |
| `GUIEVENT_COMPASS_CLICK` | int | `15` |  |
| `GUIEVENT_LEVELUP_CANCELLED` | int | `16` |  |
| `GUIEVENT_AREA_LOADSCREEN_FINISHED` | int | `17` |  |
| `GUIEVENT_QUICKCHAT_ACTIVATE` | int | `18` |  |
| `GUIEVENT_QUICKCHAT_SELECT` | int | `19` |  |
| `GUIEVENT_QUICKCHAT_CLOSE` | int | `20` |  |
| `GUIEVENT_SELECT_CREATURE` | int | `21` |  |
| `GUIEVENT_UNSELECT_CREATURE` | int | `22` |  |
| `GUIEVENT_EXAMINE_OBJECT` | int | `23` |  |
| `GUIEVENT_OPTIONS_OPEN` | int | `24` |  |
| `GUIEVENT_OPTIONS_CLOSE` | int | `25` |  |
| `GUIEVENT_RADIAL_OPEN` | int | `26` |  |
| `GUIEVENT_CHATLOG_PORTRAIT_CLICK` | int | `27` |  |
| `GUIEVENT_PLAYERLIST_PLAYER_TELL` | int | `28` |  |
| `JSON_TYPE_NULL` | int | `0` | Also invalid |
| `JSON_TYPE_OBJECT` | int | `1` |  |
| `JSON_TYPE_ARRAY` | int | `2` |  |
| `JSON_TYPE_STRING` | int | `3` |  |
| `JSON_TYPE_INTEGER` | int | `4` |  |
| `JSON_TYPE_FLOAT` | int | `5` |  |
| `JSON_TYPE_BOOL` | int | `6` |  |
| `PLAYER_DEVICE_PROPERTY_GUI_WIDTH` | string | `"gui_width"` |  |
| `PLAYER_DEVICE_PROPERTY_GUI_HEIGHT` | string | `"gui_height"` |  |
| `PLAYER_DEVICE_PROPERTY_GUI_SCALE` | string | `"gui_scale"` |  |
| `PLAYER_DEVICE_PROPERTY_GRAPHICS_ANTIALIASING_MODE` | string | `"graphics.video.anti-aliasing.mode"` |  |
| `PLAYER_DEVICE_PROPERTY_GRAPHICS_ANISOTROPIC_FILTERING` | string | `"graphics.video.anisotropic-filtering.mode"` |  |
| `PLAYER_DEVICE_PROPERTY_GRAPHICS_GAMMA` | string | `"graphics.gamma"` |  |
| `PLAYER_DEVICE_PROPERTY_GRAPHICS_TEXTURE_ANIMATIONS` | string | `"graphics.texture-animations.enabled"` |  |
| `PLAYER_DEVICE_PROPERTY_GRAPHICS_SKYBOXES` | string | `"graphics.skyboxes.enabled"` |  |
| `PLAYER_DEVICE_PROPERTY_GRAPHICS_CREATURE_WIND` | string | `"graphics.creature-wind.mode"` |  |
| `PLAYER_DEVICE_PROPERTY_GRAPHICS_SECOND_STORY_TILES` | string | `"graphics.second-story-tiles.mode"` |  |
| `PLAYER_DEVICE_PROPERTY_GRAPHICS_TILE_BORDERS` | string | `"graphics.tile-borders.enabled"` |  |
| `PLAYER_DEVICE_PROPERTY_GRAPHICS_SPELL_TARGETING_EFFECT` | string | `"graphics.spell-targeting-effect.enabled"` |  |
| `PLAYER_DEVICE_PROPERTY_GRAPHICS_TEXTURES_PACK` | string | `"graphics.textures.pack"` |  |
| `PLAYER_DEVICE_PROPERTY_GRAPHICS_GRASS` | string | `"graphics.grass.mode"` |  |
| `PLAYER_DEVICE_PROPERTY_GRAPHICS_GRASS_RENDER_DISTANCE` | string | `"graphics.grass.render-distance"` |  |
| `PLAYER_DEVICE_PROPERTY_GRAPHICS_SHINY_WATER` | string | `"graphics.water.shiny"` |  |
| `PLAYER_DEVICE_PROPERTY_GRAPHICS_LIGHTING_MAX_LIGHTS` | string | `"graphics.lighting.max-lights"` |  |
| `PLAYER_DEVICE_PROPERTY_GRAPHICS_LIGHTING_ENHANCED` | string | `"graphics.lighting.enhanced"` |  |
| `PLAYER_DEVICE_PROPERTY_GRAPHICS_SHADOWS_ENVIRONMENT` | string | `"graphics.shadows.environment.enabled"` |  |
| `PLAYER_DEVICE_PROPERTY_GRAPHICS_SHADOWS_CREATURES` | string | `"graphics.shadows.creatures.mode"` |  |
| `PLAYER_DEVICE_PROPERTY_GRAPHICS_SHADOWS_MAX_CASTING_LIGHTS` | string | `"graphics.shadows.max-casting-lights"` |  |
| `PLAYER_DEVICE_PROPERTY_GRAPHICS_EFFECTS_HIGH_QUALITY` | string | `"graphics.effects.high-quality"` |  |
| `PLAYER_DEVICE_PROPERTY_GRAPHICS_EFFECTS_CREATURE_ENVIRONMENT_MAPPING` | string | `"graphics.effects.creature-environment-mapping"` |  |
| `PLAYER_DEVICE_PROPERTY_GRAPHICS_KEYHOLING` | string | `"graphics.keyholing.enabled"` |  |
| `PLAYER_DEVICE_PROPERTY_GRAPHICS_KEYHOLING_WITH_TOOLTIP` | string | `"graphics.keyholing.with-tooltip"` |  |
| `PLAYER_DEVICE_PROPERTY_GRAPHICS_KEYHOLING_DISABLES_CAMERA_COLLISIONS` | string | `"graphics.keyholing.disables-camera-collisions"` |  |
| `PLAYER_DEVICE_PROPERTY_GRAPHICS_FBO_SSAO` | string | `"graphics.fbo.ssao.enabled"` |  |
| `PLAYER_DEVICE_PROPERTY_GRAPHICS_FBO_HIGH_CONTRAST` | string | `"graphics.fbo.high-contrast.enabled"` |  |
| `PLAYER_DEVICE_PROPERTY_GRAPHICS_FBO_VIBRANCE` | string | `"graphics.fbo.vibrance.enabled"` |  |
| `PLAYER_DEVICE_PROPERTY_GRAPHICS_FBO_TOON` | string | `"graphics.fbo.toon.enabled"` |  |
| `PLAYER_DEVICE_PROPERTY_GRAPHICS_FBO_DOF` | string | `"graphics.fbo.dof.enabled"` |  |
| `PLAYER_DEVICE_PROPERTY_GRAPHICS_LOD` | string | `"graphics.lod.enabled"` |  |
| `PLAYER_DEVICE_PROPERTY_GRAPHICS_RENDER_CLOAKS` | string | `"graphics.experimental.render-cloaks"` |  |
| `PLAYER_DEVICE_PROPERTY_GRAPHICS_GENERATE_PLT_WITH_SHADERS` | string | `"graphics.experimental.generate-plt-with-shaders"` |  |
| `PLAYER_DEVICE_PROPERTY_GRAPHICS_HILITE` | string | `"graphics.hilite.enabled"` |  |
| `PLAYER_DEVICE_PROPERTY_GRAPHICS_HILITE_GLOW` | string | `"graphics.hilite.glow"` |  |
| `PLAYER_DEVICE_PROPERTY_INPUT_KEYBOARD_SHIFT_WALK_INVERTED` | string | `"input.keyboard.shift-walk-mode-inverted"` |  |
| `PLAYER_DEVICE_PROPERTY_INPUT_MOUSE_HARDWARE_POINTER` | string | `"input.mouse.hardware-pointer"` |  |
| `PLAYER_DEVICE_PROPERTY_UI_SCALE` | string | `"ui.scale"` |  |
| `PLAYER_DEVICE_PROPERTY_UI_LARGE_FONT` | string | `"ui.large-font"` |  |
| `PLAYER_DEVICE_PROPERTY_UI_TOOLTIP_DELAY` | string | `"ui.tooltip-delay"` |  |
| `PLAYER_DEVICE_PROPERTY_UI_MOUSEOVER_FEEDBACK` | string | `"ui.mouseover-feedback"` |  |
| `PLAYER_DEVICE_PROPERTY_UI_TEXT_BUBBLE` | string | `"ui.text-bubble-mode"` |  |
| `PLAYER_DEVICE_PROPERTY_UI_TARGETING_FEEDBACK` | string | `"ui.targeting-feedback-mode"` |  |
| `PLAYER_DEVICE_PROPERTY_UI_CAN_CLICK_SELF_WHILE_WALKING` | string | `"ui.can-click-self-while-walking"` |  |
| `PLAYER_DEVICE_PROPERTY_UI_FLOATING_TEXT_FEEDBACK` | string | `"ui.floating-text-feedback"` |  |
| `PLAYER_DEVICE_PROPERTY_UI_FLOATING_TEXT_FEEDBACK_DAMAGE_TOTALS_ONLY` | string | `"ui.floating-text-feedback-damage-totals-only"` |  |
| `PLAYER_DEVICE_PROPERTY_UI_HIDE_QUICKCHAT_TEXT_IN_CHAT_WINDOW` | string | `"ui.hide-quick-chat-text-in-chat-window"` |  |
| `PLAYER_DEVICE_PROPERTY_UI_CONFIRM_SELFCAST_SPELLS` | string | `"ui.confirm-self-cast-spells"` |  |
| `PLAYER_DEVICE_PROPERTY_UI_CONFIRM_SELFCAST_FEATS` | string | `"ui.confirm-self-cast-feats"` |  |
| `PLAYER_DEVICE_PROPERTY_UI_CONFIRM_SELFCAST_ITEMS` | string | `"ui.confirm-self-cast-items"` |  |
| `PLAYER_DEVICE_PROPERTY_UI_CHARGEN_SORT_CLASSES` | string | `"ui.chargen.sort-classes"` |  |
| `PLAYER_DEVICE_PROPERTY_UI_CHAT_PANE_PRIMARY_HEIGHT` | string | `"ui.chat.pane.primary.height"` |  |
| `PLAYER_DEVICE_PROPERTY_UI_CHAT_PANE_SECONDARY_HEIGHT` | string | `"ui.chat.pane.secondary.height"` |  |
| `PLAYER_DEVICE_PROPERTY_UI_CHAT_SWEAR_FILTER` | string | `"ui.chat.swear-filter.enabled"` |  |
| `PLAYER_DEVICE_PROPERTY_UI_PARTY_INVITE_POPUP` | string | `"ui.party.invite-popup.enabled"` |  |
| `PLAYER_DEVICE_PROPERTY_UI_SPELLBOOK_SORT_SPELLS` | string | `"ui.spellbook.sort-spells"` |  |
| `PLAYER_DEVICE_PROPERTY_UI_RADIAL_SPELLCASTING_ALWAYS_SUBRADIAL` | string | `"ui.radial.spellcasting.always-show-as-subradial"` |  |
| `PLAYER_DEVICE_PROPERTY_UI_RADIAL_CLASS_ABILITIES_ALWAYS_SUBRADIAL` | string | `"ui.radial.class-abilities.always-show-as-subradial"` |  |
| `PLAYER_DEVICE_PROPERTY_UI_DISPLAY_LOADSCREEN_HINTS_IN_CHATLOG` | string | `"ui.display-loadscreen-hints-in-chatlog"` |  |
| `PLAYER_DEVICE_PROPERTY_UI_MOUSE_SCALE` | string | `"ui.mouse.scale.enabled"` |  |
| `PLAYER_DEVICE_PROPERTY_UI_MOUSE_SCALE_VALUE` | string | `"ui.mouse.scale.value"` |  |
| `PLAYER_DEVICE_PROPERTY_CAMERA_MODE` | string | `"camera.mode"` |  |
| `PLAYER_DEVICE_PROPERTY_CAMERA_EDGE_TURNING` | string | `"camera.edge-turning"` |  |
| `PLAYER_DEVICE_PROPERTY_CAMERA_DIALOG_ZOOM` | string | `"camera.dialog-zoom"` |  |
| `PLAYER_DEVICE_PROPERTY_GAME_GORE` | string | `"game.gore"` |  |
| `PLAYER_LANGUAGE_INVALID` | int | `-1` |  |
| `PLAYER_LANGUAGE_ENGLISH` | int | `0` |  |
| `PLAYER_LANGUAGE_FRENCH` | int | `1` |  |
| `PLAYER_LANGUAGE_GERMAN` | int | `2` |  |
| `PLAYER_LANGUAGE_ITALIAN` | int | `3` |  |
| `PLAYER_LANGUAGE_SPANISH` | int | `4` |  |
| `PLAYER_LANGUAGE_POLISH` | int | `5` |  |
| `PLAYER_DEVICE_PLATFORM_INVALID` | int | `0` |  |
| `PLAYER_DEVICE_PLATFORM_WINDOWS_X86` | int | `1` |  |
| `PLAYER_DEVICE_PLATFORM_WINDOWS_X64` | int | `2` |  |
| `PLAYER_DEVICE_PLATFORM_LINUX_X86` | int | `10` |  |
| `PLAYER_DEVICE_PLATFORM_LINUX_X64` | int | `11` |  |
| `PLAYER_DEVICE_PLATFORM_LINUX_ARM32` | int | `12` |  |
| `PLAYER_DEVICE_PLATFORM_LINUX_ARM64` | int | `13` |  |
| `PLAYER_DEVICE_PLATFORM_MAC_X86` | int | `20` |  |
| `PLAYER_DEVICE_PLATFORM_MAC_X64` | int | `21` |  |
| `PLAYER_DEVICE_PLATFORM_MAC_ARM64` | int | `22` |  |
| `PLAYER_DEVICE_PLATFORM_IOS` | int | `30` |  |
| `PLAYER_DEVICE_PLATFORM_ANDROID_ARM32` | int | `40` |  |
| `PLAYER_DEVICE_PLATFORM_ANDROID_ARM64` | int | `41` |  |
| `PLAYER_DEVICE_PLATFORM_ANDROID_X64` | int | `42` |  |
| `PLAYER_DEVICE_PLATFORM_NINTENDO_SWITCH` | int | `50` |  |
| `PLAYER_DEVICE_PLATFORM_MICROSOFT_XBOXONE` | int | `60` |  |
| `PLAYER_DEVICE_PLATFORM_SONY_PS4` | int | `70` |  |
| `RESTYPE_RES` | int | `0` |  |
| `RESTYPE_BMP` | int | `1` |  |
| `RESTYPE_MVE` | int | `2` |  |
| `RESTYPE_TGA` | int | `3` |  |
| `RESTYPE_WAV` | int | `4` |  |
| `RESTYPE_WFX` | int | `5` |  |
| `RESTYPE_PLT` | int | `6` |  |
| `RESTYPE_INI` | int | `7` |  |
| `RESTYPE_MP3` | int | `8` |  |
| `RESTYPE_MPG` | int | `9` |  |
| `RESTYPE_TXT` | int | `10` |  |
| `RESTYPE_KEY` | int | `9999` |  |
| `RESTYPE_BIF` | int | `9998` |  |
| `RESTYPE_ERF` | int | `9997` |  |
| `RESTYPE_IDS` | int | `9996` |  |
| `RESTYPE_PLH` | int | `2000` |  |
| `RESTYPE_TEX` | int | `2001` |  |
| `RESTYPE_MDL` | int | `2002` |  |
| `RESTYPE_THG` | int | `2003` |  |
| `RESTYPE_FNT` | int | `2005` |  |
| `RESTYPE_LUA` | int | `2007` |  |
| `RESTYPE_SLT` | int | `2008` |  |
| `RESTYPE_NSS` | int | `2009` |  |
| `RESTYPE_NCS` | int | `2010` |  |
| `RESTYPE_MOD` | int | `2011` |  |
| `RESTYPE_ARE` | int | `2012` |  |
| `RESTYPE_SET` | int | `2013` |  |
| `RESTYPE_IFO` | int | `2014` |  |
| `RESTYPE_BIC` | int | `2015` |  |
| `RESTYPE_WOK` | int | `2016` |  |
| `RESTYPE_2DA` | int | `2017` |  |
| `RESTYPE_TLK` | int | `2018` |  |
| `RESTYPE_TXI` | int | `2022` |  |
| `RESTYPE_GIT` | int | `2023` |  |
| `RESTYPE_BTI` | int | `2024` |  |
| `RESTYPE_UTI` | int | `2025` |  |
| `RESTYPE_BTC` | int | `2026` |  |
| `RESTYPE_UTC` | int | `2027` |  |
| `RESTYPE_DLG` | int | `2029` |  |
| `RESTYPE_ITP` | int | `2030` |  |
| `RESTYPE_BTT` | int | `2031` |  |
| `RESTYPE_UTT` | int | `2032` |  |
| `RESTYPE_DDS` | int | `2033` |  |
| `RESTYPE_BTS` | int | `2034` |  |
| `RESTYPE_UTS` | int | `2035` |  |
| `RESTYPE_LTR` | int | `2036` |  |
| `RESTYPE_GFF` | int | `2037` |  |
| `RESTYPE_FAC` | int | `2038` |  |
| `RESTYPE_BTE` | int | `2039` |  |
| `RESTYPE_UTE` | int | `2040` |  |
| `RESTYPE_BTD` | int | `2041` |  |
| `RESTYPE_UTD` | int | `2042` |  |
| `RESTYPE_BTP` | int | `2043` |  |
| `RESTYPE_UTP` | int | `2044` |  |
| `RESTYPE_DFT` | int | `2045` |  |
| `RESTYPE_GIC` | int | `2046` |  |
| `RESTYPE_GUI` | int | `2047` |  |
| `RESTYPE_CSS` | int | `2048` |  |
| `RESTYPE_CCS` | int | `2049` |  |
| `RESTYPE_BTM` | int | `2050` |  |
| `RESTYPE_UTM` | int | `2051` |  |
| `RESTYPE_DWK` | int | `2052` |  |
| `RESTYPE_PWK` | int | `2053` |  |
| `RESTYPE_BTG` | int | `2054` |  |
| `RESTYPE_UTG` | int | `2055` |  |
| `RESTYPE_JRL` | int | `2056` |  |
| `RESTYPE_SAV` | int | `2057` |  |
| `RESTYPE_UTW` | int | `2058` |  |
| `RESTYPE_4PC` | int | `2059` |  |
| `RESTYPE_SSF` | int | `2060` |  |
| `RESTYPE_HAK` | int | `2061` |  |
| `RESTYPE_NWM` | int | `2062` |  |
| `RESTYPE_BIK` | int | `2063` |  |
| `RESTYPE_NDB` | int | `2064` |  |
| `RESTYPE_PTM` | int | `2065` |  |
| `RESTYPE_PTT` | int | `2066` |  |
| `RESTYPE_BAK` | int | `2067` |  |
| `RESTYPE_DAT` | int | `2068` |  |
| `RESTYPE_SHD` | int | `2069` |  |
| `RESTYPE_XBC` | int | `2070` |  |
| `RESTYPE_WBM` | int | `2071` |  |
| `RESTYPE_MTR` | int | `2072` |  |
| `RESTYPE_KTX` | int | `2073` |  |
| `RESTYPE_TTF` | int | `2074` |  |
| `RESTYPE_SQL` | int | `2075` |  |
| `RESTYPE_TML` | int | `2076` |  |
| `RESTYPE_SQ3` | int | `2077` |  |
| `RESTYPE_LOD` | int | `2078` |  |
| `RESTYPE_GIF` | int | `2079` |  |
| `RESTYPE_PNG` | int | `2080` |  |
| `RESTYPE_JPG` | int | `2081` |  |
| `RESTYPE_CAF` | int | `2082` |  |
| `RESTYPE_JUI` | int | `2083` |  |
| `RESTYPE_CDB` | int | `2084` |  |
| `RESMAN_FILE_CONTENTS_FORMAT_RAW` | int | `0` |  |
| `RESMAN_FILE_CONTENTS_FORMAT_BASE64` | int | `1` |  |
| `RESMAN_FILE_CONTENTS_FORMAT_HEX` | int | `2` |  |
| `JSON_ARRAY_SORT_ASCENDING` | int | `1` |  |
| `JSON_ARRAY_SORT_DESCENDING` | int | `2` |  |
| `JSON_ARRAY_SHUFFLE` | int | `3` |  |
| `JSON_ARRAY_REVERSE` | int | `4` |  |
| `JSON_ARRAY_UNIQUE` | int | `5` |  |
| `JSON_ARRAY_COALESCE` | int | `6` |  |
| `JSON_FIND_EQUAL` | int | `0` |  |
| `JSON_FIND_LT` | int | `1` |  |
| `JSON_FIND_LTE` | int | `2` |  |
| `JSON_FIND_GT` | int | `3` |  |
| `JSON_FIND_GTE` | int | `4` |  |
| `JSON_SET_SUBSET` | int | `1` |  |
| `JSON_SET_UNION` | int | `2` |  |
| `JSON_SET_INTERSECT` | int | `3` |  |
| `JSON_SET_DIFFERENCE` | int | `4` |  |
| `JSON_SET_SYMMETRIC_DIFFERENCE` | int | `5` |  |
| `SHADER_UNIFORM_1` | int | `0` |  |
| `SHADER_UNIFORM_2` | int | `1` |  |
| `SHADER_UNIFORM_3` | int | `2` |  |
| `SHADER_UNIFORM_4` | int | `3` |  |
| `SHADER_UNIFORM_5` | int | `4` |  |
| `SHADER_UNIFORM_6` | int | `5` |  |
| `SHADER_UNIFORM_7` | int | `6` |  |
| `SHADER_UNIFORM_8` | int | `7` |  |
| `SHADER_UNIFORM_9` | int | `8` |  |
| `SHADER_UNIFORM_10` | int | `9` |  |
| `SHADER_UNIFORM_11` | int | `10` |  |
| `SHADER_UNIFORM_12` | int | `11` |  |
| `SHADER_UNIFORM_13` | int | `12` |  |
| `SHADER_UNIFORM_14` | int | `13` |  |
| `SHADER_UNIFORM_15` | int | `14` |  |
| `SHADER_UNIFORM_16` | int | `15` |  |
| `SPELL_TARGETING_SHAPE_NONE` | int | `0` |  |
| `SPELL_TARGETING_SHAPE_SPHERE` | int | `1` |  |
| `SPELL_TARGETING_SHAPE_RECT` | int | `2` |  |
| `SPELL_TARGETING_SHAPE_CONE` | int | `3` |  |
| `SPELL_TARGETING_SHAPE_HSPHERE` | int | `4` |  |
| `SPELL_TARGETING_FLAGS_NONE` | int | `0` |  |
| `SPELL_TARGETING_FLAGS_HARMS_ENEMIES` | int | `1` |  |
| `SPELL_TARGETING_FLAGS_HARMS_ALLIES` | int | `2` |  |
| `SPELL_TARGETING_FLAGS_HELPS_ALLIES` | int | `4` |  |
| `SPELL_TARGETING_FLAGS_IGNORES_SELF` | int | `8` |  |
| `SPELL_TARGETING_FLAGS_ORIGIN_ON_SELF` | int | `16` |  |
| `SPELL_TARGETING_FLAGS_SUPPRESS_WITH_TARGET` | int | `32` |  |
| `REGEXP_ECMASCRIPT` | int | `0` |  |
| `REGEXP_BASIC` | int | `1` |  |
| `REGEXP_EXTENDED` | int | `2` |  |
| `REGEXP_AWK` | int | `4` |  |
| `REGEXP_GREP` | int | `8` |  |
| `REGEXP_EGREP` | int | `16` |  |
| `REGEXP_ICASE` | int | `32` |  |
| `REGEXP_NOSUBS` | int | `64` |  |
| `REGEXP_MATCH_NOT_BOL` | int | `1` |  |
| `REGEXP_MATCH_NOT_EOL` | int | `2` |  |
| `REGEXP_MATCH_NOT_BOW` | int | `4` |  |
| `REGEXP_MATCH_NOT_EOW` | int | `8` |  |
| `REGEXP_MATCH_ANY` | int | `16` |  |
| `REGEXP_MATCH_NOT_NULL` | int | `32` |  |
| `REGEXP_MATCH_CONTINUOUS` | int | `64` |  |
| `REGEXP_MATCH_PREV_AVAIL` | int | `128` |  |
| `REGEXP_FORMAT_DEFAULT` | int | `0` |  |
| `REGEXP_FORMAT_SED` | int | `256` |  |
| `REGEXP_FORMAT_NO_COPY` | int | `512` |  |
| `REGEXP_FORMAT_FIRST_ONLY` | int | `1024` |  |
| `OBJECT_UI_DISCOVERY_DEFAULT` | int | `-1` |  |
| `OBJECT_UI_DISCOVERY_NONE` | int | `0` |  |
| `OBJECT_UI_DISCOVERY_HILITE_MOUSEOVER` | int | `1` |  |
| `OBJECT_UI_DISCOVERY_HILITE_TAB` | int | `2` |  |
| `OBJECT_UI_DISCOVERY_TEXTBUBBLE_MOUSEOVER` | int | `4` |  |
| `OBJECT_UI_DISCOVERY_TEXTBUBBLE_TAB` | int | `8` |  |
| `OBJECT_UI_TEXT_BUBBLE_OVERRIDE_NONE` | int | `0` |  |
| `OBJECT_UI_TEXT_BUBBLE_OVERRIDE_REPLACE` | int | `1` |  |
| `OBJECT_UI_TEXT_BUBBLE_OVERRIDE_PREPEND` | int | `2` |  |
| `OBJECT_UI_TEXT_BUBBLE_OVERRIDE_APPEND` | int | `3` |  |
| `CAMERA_FLAG_ENABLE_COLLISION` | int | `1` |  |
| `CAMERA_FLAG_DISABLE_COLLISION` | int | `2` |  |
| `CAMERA_FLAG_DISABLE_SHAKE` | int | `4` |  |
| `CAMERA_FLAG_DISABLE_SCROLL` | int | `8` |  |
| `CAMERA_FLAG_DISABLE_TURN` | int | `16` |  |
| `CAMERA_FLAG_DISABLE_TILT` | int | `32` |  |
| `CAMERA_FLAG_DISABLE_ZOOM` | int | `64` |  |
| `SETTILE_FLAG_RELOAD_GRASS` | int | `1` |  |
| `SETTILE_FLAG_RELOAD_BORDER` | int | `2` |  |
| `SETTILE_FLAG_RECOMPUTE_LIGHTING` | int | `4` |  |
| `AUDIOSTREAM_IDENTIFIER_0` | int | `0` |  |
| `AUDIOSTREAM_IDENTIFIER_1` | int | `1` |  |
| `AUDIOSTREAM_IDENTIFIER_2` | int | `2` |  |
| `AUDIOSTREAM_IDENTIFIER_3` | int | `3` |  |
| `AUDIOSTREAM_IDENTIFIER_4` | int | `4` |  |
| `AUDIOSTREAM_IDENTIFIER_5` | int | `5` |  |
| `AUDIOSTREAM_IDENTIFIER_6` | int | `6` |  |
| `AUDIOSTREAM_IDENTIFIER_7` | int | `7` |  |
| `AUDIOSTREAM_IDENTIFIER_8` | int | `8` |  |
| `AUDIOSTREAM_IDENTIFIER_9` | int | `9` |  |
| `SPELL_FAILURE_TYPE_ALL` | int | `0` |  |
| `SPELL_FAILURE_TYPE_ARCANE` | int | `1` |  |
| `sLanguage` | string | `"nwscript"` |  |

## Functions

#### `int Random(int nMaxInteger)`
> Get an integer between 0 and nMaxInteger-1.
> Return value on error: 0

#### `void PrintString(string sString)`
> Output sString to the log file.

#### `void PrintFloat(float fFloat, int nWidth = 18, int nDecimals = 9)`
> Output a formatted float to the log file.
> - nWidth should be a value from 0 to 18 inclusive.
> - nDecimals should be a value from 0 to 9 inclusive.

#### `string FloatToString(float fFloat, int nWidth = 18, int nDecimals = 9)`
> Convert fFloat into a string.
> - nWidth should be a value from 0 to 18 inclusive.
> - nDecimals should be a value from 0 to 9 inclusive.

#### `void PrintInteger(int nInteger)`
> Output nInteger to the log file.

#### `void PrintObject(object oObject)`
> Output oObject's ID to the log file.

#### `void AssignCommand(object oActionSubject, action aActionToAssign)`
> Assign aActionToAssign to oActionSubject.
> No return value, but if an error occurs, the log file will contain
> "AssignCommand failed."
> (If the object doesn't exist, nothing happens.)

#### `void DelayCommand(float fSeconds, action aActionToDelay)`
> Delay aActionToDelay by fSeconds.
> No return value, but if an error occurs, the log file will contain
> "DelayCommand failed.".
> It is suggested that functions which create effects should not be used
> as parameters to delayed actions.  Instead, the effect should be created in the
> script and then passed into the action.  For example:
> effect eDamage = EffectDamage(nDamage, DAMAGE_TYPE_MAGICAL);
> DelayCommand(fDelay, ApplyEffectToObject(DURATION_TYPE_INSTANT, eDamage, oTarget);

#### `void ExecuteScript(string sScript, object oTarget = OBJECT_SELF)`
> Make oTarget run sScript and then return execution to the calling script.
> If sScript does not specify a compiled script, nothing happens.

#### `void ClearAllActions(int nClearCombatState = FALSE, object oObject = OBJECT_SELF)`
> Clear all the actions of oObject.
> No return value, but if an error occurs, the log file will contain
> "ClearAllActions failed.".
> - nClearCombatState: if true, this will immediately clear the combat state
> on a creature, which will stop the combat music and allow them to rest,
> engage in dialog, or other actions that they would normally have to wait for.

#### `void SetFacing(float fDirection, object oObject = OBJECT_SELF)`
> Cause oObject to face fDirection.
> - fDirection is expressed as anticlockwise degrees from Due East.
> DIRECTION_EAST, DIRECTION_NORTH, DIRECTION_WEST and DIRECTION_SOUTH are
> predefined. (0.0f=East, 90.0f=North, 180.0f=West, 270.0f=South)

#### `void SetCalendar(int nYear, int nMonth, int nDay)`
> Set the calendar to the specified date.
> - nYear should be from 0 to 32000 inclusive
> - nMonth should be from 1 to 12 inclusive
> - nDay should be from 1 to 28 inclusive
> 1) Time can only be advanced forwards; attempting to set the time backwards
> will result in no change to the calendar.
> 2) If values larger than the month or day are specified, they will be wrapped
> around and the overflow will be used to advance the next field.
> e.g. Specifying a year of 1350, month of 33 and day of 10 will result in
> the calender being set to a year of 1352, a month of 9 and a day of 10.

#### `void SetTime(int nHour, int nMinute, int nSecond, int nMillisecond)`
> Set the time to the time specified.
> - nHour should be from 0 to 23 inclusive
> - nMinute should be from 0 to 59 inclusive
> - nSecond should be from 0 to 59 inclusive
> - nMillisecond should be from 0 to 999 inclusive
> 1) Time can only be advanced forwards; attempting to set the time backwards
> will result in the day advancing and then the time being set to that
> specified, e.g. if the current hour is 15 and then the hour is set to 3,
> the day will be advanced by 1 and the hour will be set to 3.
> 2) If values larger than the max hour, minute, second or millisecond are
> specified, they will be wrapped around and the overflow will be used to
> advance the next field, e.g. specifying 62 hours, 250 minutes, 10 seconds
> and 10 milliseconds will result in the calendar day being advanced by 2
> and the time being set to 18 hours, 10 minutes, 10 milliseconds.

#### `int GetCalendarYear()`
> Get the current calendar year.

#### `int GetCalendarMonth()`
> Get the current calendar month.

#### `int GetCalendarDay()`
> Get the current calendar day.

#### `int GetTimeHour()`
> Get the current hour.

#### `int GetTimeMinute()`
> Get the current minute

#### `int GetTimeSecond()`
> Get the current second

#### `int GetTimeMillisecond()`
> Get the current millisecond

#### `void ActionRandomWalk()`
> The action subject will generate a random location near its current location
> and pathfind to it.  ActionRandomwalk never ends, which means it is neccessary
> to call ClearAllActions in order to allow a creature to perform any other action
> once ActionRandomWalk has been called.
> No return value, but if an error occurs the log file will contain
> "ActionRandomWalk failed."

#### `void ActionMoveToLocation(location lDestination, int bRun = FALSE)`
> The action subject will move to lDestination.
> - lDestination: The object will move to this location.  If the location is
> invalid or a path cannot be found to it, the command does nothing.
> - bRun: If this is TRUE, the action subject will run rather than walk
> No return value, but if an error occurs the log file will contain
> "MoveToPoint failed."

#### `void ActionMoveToObject(object oMoveTo, int bRun = FALSE, float fRange = 1.0f)`
> Cause the action subject to move to a certain distance from oMoveTo.
> If there is no path to oMoveTo, this command will do nothing.
> - oMoveTo: This is the object we wish the action subject to move to
> - bRun: If this is TRUE, the action subject will run rather than walk
> - fRange: This is the desired distance between the action subject and oMoveTo
> No return value, but if an error occurs the log file will contain
> "ActionMoveToObject failed."

#### `void ActionMoveAwayFromObject(object oFleeFrom, int bRun = FALSE, float fMoveAwayRange = 40.0f)`
> Cause the action subject to move to a certain distance away from oFleeFrom.
> - oFleeFrom: This is the object we wish the action subject to move away from.
> If oFleeFrom is not in the same area as the action subject, nothing will
> happen.
> - bRun: If this is TRUE, the action subject will run rather than walk
> - fMoveAwayRange: This is the distance we wish the action subject to put
> between themselves and oFleeFrom
> No return value, but if an error occurs the log file will contain
> "ActionMoveAwayFromObject failed."

#### `object GetArea(object oTarget)`
> Get the area that oTarget is currently in
> Return value on error: OBJECT_INVALID

#### `object GetEnteringObject()`
> The value returned by this function depends on the object type of the caller:
> 1) If the caller is a door it returns the object that last
> triggered it.
> 2) If the caller is a trigger, area of effect, module, area or encounter it
> returns the object that last entered it.
> Return value on error: OBJECT_INVALID
> When used for doors, this should only be called from the OnAreaTransitionClick
> event.  Otherwise, it should only be called in OnEnter scripts.

#### `object GetExitingObject()`
> Get the object that last left the caller.  This function works on triggers,
> areas of effect, modules, areas and encounters.
> Return value on error: OBJECT_INVALID
> Should only be called in OnExit scripts.

#### `vector GetPosition(object oTarget)`
> Get the position of oTarget
> Return value on error: vector (0.0f, 0.0f, 0.0f)

#### `float GetFacing(object oTarget)`
> Get the direction in which oTarget is facing, expressed as a float between
> 0.0f and 360.0f
> Return value on error: -1.0f

#### `object GetItemPossessor(object oItem, int bReturnBags = FALSE)`
> Get the possessor of oItem
> - bReturnBags: If TRUE will potentially return a bag container item the item is in, instead of
> the object holding the bag. Make sure to check the returning item object type with this flag.
> Return value on error: OBJECT_INVALID

#### `object GetItemPossessedBy(object oCreature, string sItemTag)`
> Get the object possessed by oCreature with the tag sItemTag
> Return value on error: OBJECT_INVALID

#### `object CreateItemOnObject(string sItemTemplate, object oTarget = OBJECT_SELF, int nStackSize = 1, string sNewTag = "")`
> Create an item with the template sItemTemplate in oTarget's inventory.
> - nStackSize: This is the stack size of the item to be created
> - sNewTag: If this string is not empty, it will replace the default tag from the template
> Return value: The object that has been created.  On error, this returns
> OBJECT_INVALID.
> If the item created was merged into an existing stack of similar items,
> the function will return the merged stack object. If the merged stack
> overflowed, the function will return the overflowed stack that was created.

#### `void ActionEquipItem(object oItem, int nInventorySlot)`
> Equip oItem into nInventorySlot.
> - nInventorySlot: INVENTORY_SLOT_*
> No return value, but if an error occurs the log file will contain
> "ActionEquipItem failed."
> Note:
> If the creature already has an item equipped in the slot specified, it will be
> unequipped automatically by the call to ActionEquipItem.
> In order for ActionEquipItem to succeed the creature must be able to equip the
> item oItem normally. This means that:
> 1) The item is in the creature's inventory.
> 2) The item must already be identified (if magical).
> 3) The creature has the level required to equip the item (if magical and ILR is on).
> 4) The creature possesses the required feats to equip the item (such as weapon proficiencies).

#### `void ActionUnequipItem(object oItem)`
> Unequip oItem from whatever slot it is currently in.

#### `void ActionPickUpItem(object oItem)`
> Pick up oItem from the ground.
> No return value, but if an error occurs the log file will contain
> "ActionPickUpItem failed."

#### `void ActionPutDownItem(object oItem)`
> Put down oItem on the ground.
> No return value, but if an error occurs the log file will contain
> "ActionPutDownItem failed."

#### `object GetLastAttacker(object oAttackee = OBJECT_SELF)`
> Get the last attacker of oAttackee.  This should only be used ONLY in the
> OnAttacked events for creatures, placeables and doors.
> Return value on error: OBJECT_INVALID

#### `void ActionAttack(object oAttackee, int bPassive = FALSE)`
> Attack oAttackee.
> - bPassive: If this is TRUE, attack is in passive mode.

#### `object GetNearestCreature(int nFirstCriteriaType, int nFirstCriteriaValue, object oTarget = OBJECT_SELF, int nNth = 1, int nSecondCriteriaType = -1, int nSecondCriteriaValue = -1, int nThirdCriteriaType = -1, int nThirdCriteriaValue = -1)`
> Get the creature nearest to oTarget, subject to all the criteria specified.
> - nFirstCriteriaType: CREATURE_TYPE_*
> - nFirstCriteriaValue:
> -> CLASS_TYPE_* if nFirstCriteriaType was CREATURE_TYPE_CLASS
> -> SPELL_* if nFirstCriteriaType was CREATURE_TYPE_DOES_NOT_HAVE_SPELL_EFFECT
> or CREATURE_TYPE_HAS_SPELL_EFFECT
> -> TRUE or FALSE if nFirstCriteriaType was CREATURE_TYPE_IS_ALIVE
> -> PERCEPTION_* if nFirstCriteriaType was CREATURE_TYPE_PERCEPTION
> -> PLAYER_CHAR_IS_PC or PLAYER_CHAR_NOT_PC if nFirstCriteriaType was
> CREATURE_TYPE_PLAYER_CHAR
> -> RACIAL_TYPE_* if nFirstCriteriaType was CREATURE_TYPE_RACIAL_TYPE
> -> REPUTATION_TYPE_* if nFirstCriteriaType was CREATURE_TYPE_REPUTATION
> For example, to get the nearest PC, use:
> (CREATURE_TYPE_PLAYER_CHAR, PLAYER_CHAR_IS_PC)
> - oTarget: We're trying to find the creature of the specified type that is
> nearest to oTarget
> - nNth: We don't have to find the first nearest: we can find the Nth nearest...
> - nSecondCriteriaType: This is used in the same way as nFirstCriteriaType to
> further specify the type of creature that we are looking for.
> - nSecondCriteriaValue: This is used in the same way as nFirstCriteriaValue
> to further specify the type of creature that we are looking for.
> - nThirdCriteriaType: This is used in the same way as nFirstCriteriaType to
> further specify the type of creature that we are looking for.
> - nThirdCriteriaValue: This is used in the same way as nFirstCriteriaValue to
> further specify the type of creature that we are looking for.
> Return value on error: OBJECT_INVALID

#### `void ActionSpeakString(string sStringToSpeak, int nTalkVolume = TALKVOLUME_TALK)`
> Add a speak action to the action subject.
> - sStringToSpeak: String to be spoken
> - nTalkVolume: TALKVOLUME_*

#### `void ActionPlayAnimation(int nAnimation, float fSpeed = 1.0, float fDurationSeconds = 0.0)`
> Cause the action subject to play an animation
> - nAnimation: ANIMATION_*
> - fSpeed: Speed of the animation
> - fDurationSeconds: Duration of the animation (this is not used for Fire and
> Forget animations)

#### `float GetDistanceToObject(object oObject, object oFrom = OBJECT_SELF)`
> Get the distance from oFrom to oObject in metres.
> Return value on error: -1.0f

#### `int GetIsObjectValid(object oObject)`
> Returns TRUE if oObject is a valid object.

#### `void ActionOpenDoor(object oDoor, int bRun = FALSE)`
> Cause the action subject to open oDoor
> - bRun: If TRUE, subject will run to the door instead of walking

#### `void ActionCloseDoor(object oDoor, int bRun = FALSE)`
> Cause the action subject to close oDoor
> - bRun: If TRUE, subject will run to the door instead of walking

#### `void SetCameraFacing(float fDirection, float fDistance = -1.0f, float fPitch = -1.0, int nTransitionType = CAMERA_TRANSITION_TYPE_SNAP)`
> Change the direction in which the camera is facing
> - fDirection is expressed as anticlockwise degrees from Due East.
> (0.0f=East, 90.0f=North, 180.0f=West, 270.0f=South)
> A value of -1.0f for any parameter will be ignored and instead it will
> use the current camera value.
> This can be used to change the way the camera is facing after the player
> emerges from an area transition.
> - nTransitionType: CAMERA_TRANSITION_TYPE_*  SNAP will immediately move the
> camera to the new position, while the other types will result in the camera moving gradually into position
> Pitch and distance are limited to valid values for the current camera mode:
> Top Down: Distance = 5-20, Pitch = 1-50
> Driving camera: Distance = 6 (can't be changed), Pitch = 1-62
> Chase: Distance = 5-20, Pitch = 1-50
> NOTE *** In NWN:Hordes of the Underdark the camera limits have been relaxed to the following:
> Distance 1-25
> Pitch 1-89

#### `void PlaySound(string sSoundName)`
> Play sSoundName
> - sSoundName: TBD - SS
> This will play a mono sound from the location of the object running the command.

#### `object GetSpellTargetObject()`
> Get the object at which the caller last cast a spell
> Return value on error: OBJECT_INVALID

#### `void ActionCastSpellAtObject(int nSpell, object oTarget, int nMetaMagic = METAMAGIC_ANY, int bCheat = FALSE, int nDomainLevel = 0, int nProjectilePathType = PROJECTILE_PATH_TYPE_DEFAULT, int bInstantSpell = FALSE, int nClass = -1, int bSpontaneousCast = FALSE)`
> This action casts a spell at oTarget.
> - nSpell: SPELL_*
> - oTarget: Target for the spell
> - nMetaMagic: METAMAGIC_*. If nClass is specified, cannot be METAMAGIC_ANY.
> - bCheat: If this is TRUE, then the executor of the action doesn't have to be
> able to cast the spell. Ignored if nClass is specified.
> - bCheat: If this is TRUE, then the executor of the action doesn't have to be
> able to cast the spell.
> - nDomainLevel: The level of the spell if cast from a domain slot.
> eg SPELL_HEAL can be spell level 5 on a cleric. Use 0 for no domain slot.
> - nProjectilePathType: PROJECTILE_PATH_TYPE_*
> - bInstantSpell: If this is TRUE, the spell is cast immediately. This allows
> the end-user to simulate a high-level magic-user having lots of advance
> warning of impending trouble
> - nClass: If set to a CLASS_TYPE_* it will cast using that class specifically.
> CLASS_TYPE_INVALID will use spell abilities.
> - bSpontaneousCast: If set to TRUE will attempt to cast the given spell spontaneously,
> ie a Cleric casting Cure Light Wounds using any level 1 slot. Needs a valid nClass set.

#### `int GetCurrentHitPoints(object oObject = OBJECT_SELF)`
> Get the current hitpoints of oObject
> Return value on error: 0

#### `int GetMaxHitPoints(object oObject = OBJECT_SELF)`
> Get the maximum hitpoints of oObject
> Return value on error: 0

#### `int GetLocalInt(object oObject, string sVarName)`
> Get oObject's local integer variable sVarName
> Return value on error: 0

#### `float GetLocalFloat(object oObject, string sVarName)`
> Get oObject's local float variable sVarName
> Return value on error: 0.0f

#### `string GetLocalString(object oObject, string sVarName)`
> Get oObject's local string variable sVarName
> Return value on error: ""

#### `object GetLocalObject(object oObject, string sVarName)`
> Get oObject's local object variable sVarName
> Return value on error: OBJECT_INVALID

#### `void SetLocalInt(object oObject, string sVarName, int nValue)`
> Set oObject's local integer variable sVarName to nValue

#### `void SetLocalFloat(object oObject, string sVarName, float fValue)`
> Set oObject's local float variable sVarName to nValue

#### `void SetLocalString(object oObject, string sVarName, string sValue)`
> Set oObject's local string variable sVarName to nValue

#### `void SetLocalObject(object oObject, string sVarName, object oValue)`
> Set oObject's local object variable sVarName to nValue

#### `int GetStringLength(string sString)`
> Get the length of sString
> Return value on error: -1

#### `string GetStringUpperCase(string sString)`
> Convert sString into upper case
> Return value on error: ""

#### `string GetStringLowerCase(string sString)`
> Convert sString into lower case
> Return value on error: ""

#### `string GetStringRight(string sString, int nCount)`
> Get nCount characters from the right end of sString
> Return value on error: ""

#### `string GetStringLeft(string sString, int nCount)`
> Get nCounter characters from the left end of sString
> Return value on error: ""

#### `string InsertString(string sDestination, string sString, int nPosition)`
> Insert sString into sDestination at nPosition
> Return value on error: ""

#### `string GetSubString(string sString, int nStart, int nCount)`
> Get nCount characters from sString, starting at nStart
> Return value on error: ""

#### `int FindSubString(string sString, string sSubString, int nStart = 0)`
> Find the position of sSubstring inside sString
> - nStart: The character position to start searching at (from the left end of the string).
> Return value on error: -1

#### `float fabs(float fValue)`
> Maths operation: absolute value of fValue

#### `float cos(float fValue)`
> Maths operation: cosine of fValue

#### `float sin(float fValue)`
> Maths operation: sine of fValue

#### `float tan(float fValue)`
> Maths operation: tan of fValue

#### `float acos(float fValue)`
> Maths operation: arccosine of fValue
> Returns zero if fValue > 1 or fValue < -1

#### `float asin(float fValue)`
> Maths operation: arcsine of fValue
> Returns zero if fValue >1 or fValue < -1

#### `float atan(float fValue)`
> Maths operation: arctan of fValue

#### `float log(float fValue)`
> Maths operation: log of fValue
> Returns zero if fValue <= zero

#### `float pow(float fValue, float fExponent)`
> Maths operation: fValue is raised to the power of fExponent
> Returns zero if fValue ==0 and fExponent <0

#### `float sqrt(float fValue)`
> Maths operation: square root of fValue
> Returns zero if fValue <0

#### `int abs(int nValue)`
> Maths operation: integer absolute value of nValue
> Return value on error: 0

#### `effect EffectHeal(int nDamageToHeal)`
> Create a Heal effect. This should be applied as an instantaneous effect.
> Returns an effect of type EFFECT_TYPE_INVALIDEFFECT if nDamageToHeal < 0.

#### `effect EffectDamage(int nDamageAmount, int nDamageType = DAMAGE_TYPE_MAGICAL, int nDamagePower = DAMAGE_POWER_NORMAL)`
> Create a Damage effect
> - nDamageAmount: amount of damage to be dealt. This should be applied as an
> instantaneous effect.
> - nDamageType: DAMAGE_TYPE_*
> - nDamagePower: DAMAGE_POWER_*

#### `effect EffectAbilityIncrease(int nAbilityToIncrease, int nModifyBy)`
> Create an Ability Increase effect
> - bAbilityToIncrease: ABILITY_*

#### `effect EffectDamageResistance(int nDamageType, int nAmount, int nLimit = 0, int bRangedOnly = FALSE)`
> Create a Damage Resistance effect that removes the first nAmount points of
> damage of type nDamageType, up to nLimit (or infinite if nLimit is 0)
> - nDamageType: DAMAGE_TYPE_*
> - nAmount: The amount of damage to soak each time the target is damaged.
> - nLimit: How much damage the effect can absorb before disappearing.
> Set to zero for infinite.
> - bRangedOnly: Set to TRUE to have this resistance only apply to ranged attacks.

#### `effect EffectResurrection()`
> Create a Resurrection effect. This should be applied as an instantaneous effect.

#### `effect EffectSummonCreature(string sCreatureResref, int nVisualEffectId = VFX_NONE, float fDelaySeconds = 0.0f, int nUseAppearAnimation = 0, int nUnsummonVisualEffectId = VFX_IMP_UNSUMMON, object oSummonToAdd = OBJECT_INVALID)`
> Create a Summon Creature effect.  The creature is created and placed into the
> caller's party/faction.
> - sCreatureResref: Identifies the creature to be summoned
> - nVisualEffectId: VFX_*
> - fDelaySeconds: There can be delay between the visual effect being played, and the
> creature being added to the area
> - nUseAppearAnimation: should this creature play it's "appear" animation when it is
> summoned. If zero, it will just fade in somewhere near the target.  If the value is 1
> it will use the appear animation, and if it's 2 it will use appear2 (which doesn't exist for most creatures)
> - nUnsummonVisualEffectId: VFX_* to apply when the creature is unsummoned
> - oSummonToAdd: If sCreatureResref is blank, this object (if they have no master) is instead added as the summon, applying nVisualEffectId at their location
> fDelaySeconds and nUseAppearAnimation are unused, and no "Summoned a creature" feedback is sent, allowing you to do your own.
> The creature otherwise acts like a summon from then on, including not giving out XP for being killed, and able to be
> unsummoned by the master or when the effect expires.

#### `int GetCasterLevel(object oObject)`
> Get the caster level of an object. This is consistent with the caster level used when applying effects if OBJECT_SELF is used.
> - oObject: A creature will return the caster level of their currently cast spell or ability, or the item's caster level if an item was used
> A placeable will return an automatic caster level: floor(10, (spell innate level * 2) - 1)
> An Area of Effect object will return the caster level that was used to create the Area of Effect.
> Return value on error, or if oObject has not yet cast a spell: 0;

#### `effect GetFirstEffect(object oCreature)`
> Get the first in-game effect on oCreature.

#### `effect GetNextEffect(object oCreature)`
> Get the next in-game effect on oCreature.

#### `void RemoveEffect(object oCreature, effect eEffect)`
> Remove eEffect from oCreature.
> No return value

#### `int GetIsEffectValid(effect eEffect)`
> Returns TRUE if eEffect is a valid effect. The effect must have been applied to
> an object or else it will return FALSE

#### `int GetEffectDurationType(effect eEffect)`
> Get the duration type (DURATION_TYPE_*) of eEffect.
> Return value if eEffect is not valid: -1

#### `int GetEffectSubType(effect eEffect)`
> Get the subtype (SUBTYPE_*) of eEffect.
> Return value on error: 0

#### `object GetEffectCreator(effect eEffect)`
> Get the object that created eEffect.
> Returns OBJECT_INVALID if eEffect is not a valid effect.

#### `string IntToString(int nInteger)`
> Convert nInteger into a string.
> Return value on error: ""

#### `object GetFirstObjectInArea(object oArea = OBJECT_INVALID, int nObjectFilter = OBJECT_TYPE_ALL)`
> Get the first object in oArea.
> If no valid area is specified, it will use the caller's area.
> - nObjectFilter: This allows you to filter out undesired object types, using bitwise "or".
> For example, to return only creatures and doors, the value for this parameter would be OBJECT_TYPE_CREATURE | OBJECT_TYPE_DOOR
> Return value on error: OBJECT_INVALID

#### `object GetNextObjectInArea(object oArea = OBJECT_INVALID, int nObjectFilter = OBJECT_TYPE_ALL)`
> Get the next object in oArea.
> If no valid area is specified, it will use the caller's area.
> - nObjectFilter: This allows you to filter out undesired object types, using bitwise "or".
> For example, to return only creatures and doors, the value for this parameter would be OBJECT_TYPE_CREATURE | OBJECT_TYPE_DOOR
> Return value on error: OBJECT_INVALID

#### `int d2(int nNumDice = 1)`
> Get the total from rolling (nNumDice x d2 dice).
> - nNumDice: If this is less than 1, the value 1 will be used.

#### `int d3(int nNumDice = 1)`
> Get the total from rolling (nNumDice x d3 dice).
> - nNumDice: If this is less than 1, the value 1 will be used.

#### `int d4(int nNumDice = 1)`
> Get the total from rolling (nNumDice x d4 dice).
> - nNumDice: If this is less than 1, the value 1 will be used.

#### `int d6(int nNumDice = 1)`
> Get the total from rolling (nNumDice x d6 dice).
> - nNumDice: If this is less than 1, the value 1 will be used.

#### `int d8(int nNumDice = 1)`
> Get the total from rolling (nNumDice x d8 dice).
> - nNumDice: If this is less than 1, the value 1 will be used.

#### `int d10(int nNumDice = 1)`
> Get the total from rolling (nNumDice x d10 dice).
> - nNumDice: If this is less than 1, the value 1 will be used.

#### `int d12(int nNumDice = 1)`
> Get the total from rolling (nNumDice x d12 dice).
> - nNumDice: If this is less than 1, the value 1 will be used.

#### `int d20(int nNumDice = 1)`
> Get the total from rolling (nNumDice x d20 dice).
> - nNumDice: If this is less than 1, the value 1 will be used.

#### `int d100(int nNumDice = 1)`
> Get the total from rolling (nNumDice x d100 dice).
> - nNumDice: If this is less than 1, the value 1 will be used.

#### `float VectorMagnitude(vector vVector)`
> Get the magnitude of vVector; this can be used to determine the
> distance between two points.
> Return value on error: 0.0f

#### `int GetMetaMagicFeat()`
> Get the metamagic type (METAMAGIC_*) of the last spell cast by the caller
> Return value if the caster is not a valid object: -1

#### `int GetObjectType(object oTarget)`
> Get the object type (OBJECT_TYPE_*) of oTarget
> Return value if oTarget is not a valid object: -1

#### `int GetRacialType(object oCreature)`
> Get the racial type (RACIAL_TYPE_*) of oCreature
> Return value if oCreature is not a valid creature: RACIAL_TYPE_INVALID

#### `int FortitudeSave(object oCreature, int nDC, int nSaveType = SAVING_THROW_TYPE_NONE, object oSaveVersus = OBJECT_SELF)`
> Do a Fortitude Save check for the given DC
> - oCreature
> - nDC: Difficulty check
> - nSaveType: SAVING_THROW_TYPE_*
> - oSaveVersus
> Returns: 0 if the saving throw roll failed
> Returns: 1 if the saving throw roll succeeded
> Returns: 2 if the target was immune to the save type specified
> Note: If used within an Area of Effect Object Script (On Enter, OnExit, OnHeartbeat), you MUST pass
> GetAreaOfEffectCreator() into oSaveVersus!!

#### `int ReflexSave(object oCreature, int nDC, int nSaveType = SAVING_THROW_TYPE_NONE, object oSaveVersus = OBJECT_SELF)`
> Does a Reflex Save check for the given DC
> - oCreature
> - nDC: Difficulty check
> - nSaveType: SAVING_THROW_TYPE_*
> - oSaveVersus
> Returns: 0 if the saving throw roll failed
> Returns: 1 if the saving throw roll succeeded
> Returns: 2 if the target was immune to the save type specified
> Note: If used within an Area of Effect Object Script (On Enter, OnExit, OnHeartbeat), you MUST pass
> GetAreaOfEffectCreator() into oSaveVersus!!

#### `int WillSave(object oCreature, int nDC, int nSaveType = SAVING_THROW_TYPE_NONE, object oSaveVersus = OBJECT_SELF)`
> Does a Will Save check for the given DC
> - oCreature
> - nDC: Difficulty check
> - nSaveType: SAVING_THROW_TYPE_*
> - oSaveVersus
> Returns: 0 if the saving throw roll failed
> Returns: 1 if the saving throw roll succeeded
> Returns: 2 if the target was immune to the save type specified
> Note: If used within an Area of Effect Object Script (On Enter, OnExit, OnHeartbeat), you MUST pass
> GetAreaOfEffectCreator() into oSaveVersus!!

#### `int GetSpellSaveDC()`
> Get the DC to save against for a spell (10 + spell level + relevant ability
> bonus).  This can be called by a creature or by an Area of Effect object.

#### `effect MagicalEffect(effect eEffect)`
> Set the subtype of eEffect to Magical and return eEffect.
> (Effects default to magical if the subtype is not set)
> Magical effects are removed by resting, and by dispel magic

#### `effect SupernaturalEffect(effect eEffect)`
> Set the subtype of eEffect to Supernatural and return eEffect.
> (Effects default to magical if the subtype is not set)
> Permanent supernatural effects are not removed by resting

#### `effect ExtraordinaryEffect(effect eEffect)`
> Set the subtype of eEffect to Extraordinary and return eEffect.
> (Effects default to magical if the subtype is not set)
> Extraordinary effects are removed by resting, but not by dispel magic

#### `effect EffectACIncrease(int nValue, int nModifyType = AC_DODGE_BONUS, int nDamageType = AC_VS_DAMAGE_TYPE_ALL)`
> Create an AC Increase effect
> - nValue: size of AC increase
> - nModifyType: AC_*_BONUS
> - nDamageType: DAMAGE_TYPE_*
> Default value for nDamageType should only ever be used in this function prototype.

#### `int GetAC(object oObject, int nForFutureUse = 0)`
> If oObject is a creature, this will return that creature's armour class
> If oObject is an item, door or placeable, this will return zero.
> - nForFutureUse: this parameter is not currently used
> Return value if oObject is not a creature, item, door or placeable: -1

#### `effect EffectSavingThrowIncrease(int nSave, int nValue, int nSaveType = SAVING_THROW_TYPE_ALL)`
> Create a Saving Throw Increase effect
> - nSave: SAVING_THROW_* (not SAVING_THROW_TYPE_*)
> SAVING_THROW_ALL
> SAVING_THROW_FORT
> SAVING_THROW_REFLEX
> SAVING_THROW_WILL
> - nValue: size of the Saving Throw increase
> - nSaveType: SAVING_THROW_TYPE_* (e.g. SAVING_THROW_TYPE_ACID )

#### `effect EffectAttackIncrease(int nBonus, int nModifierType = ATTACK_BONUS_MISC)`
> Create an Attack Increase effect
> - nBonus: size of attack bonus
> - nModifierType: ATTACK_BONUS_*

#### `effect EffectDamageReduction(int nAmount, int nDamagePower, int nLimit = 0, int bRangedOnly = FALSE)`
> Create a Damage Reduction effect
> - nAmount: amount of damage reduction
> - nDamagePower: DAMAGE_POWER_*
> - nLimit: How much damage the effect can absorb before disappearing.
> Set to zero for infinite
> - bRangedOnly: Set to TRUE to have this reduction only apply to ranged attacks

#### `effect EffectDamageIncrease(int nBonus, int nDamageType = DAMAGE_TYPE_MAGICAL)`
> Create a Damage Increase effect
> - nBonus: DAMAGE_BONUS_*
> - nDamageType: DAMAGE_TYPE_*
> NOTE! You *must* use the DAMAGE_BONUS_* constants! Using other values may
> result in odd behaviour.

#### `float RoundsToSeconds(int nRounds)`
> Convert nRounds into a number of seconds
> A round is always 6.0 seconds

#### `float HoursToSeconds(int nHours)`
> Convert nHours into a number of seconds
> The result will depend on how many minutes there are per hour (game-time)

#### `float TurnsToSeconds(int nTurns)`
> Convert nTurns into a number of seconds
> A turn is always 60.0 seconds

#### `int GetLawChaosValue(object oCreature)`
> Get an integer between 0 and 100 (inclusive) to represent oCreature's
> Law/Chaos alignment
> (100=law, 0=chaos)
> Return value if oCreature is not a valid creature: -1

#### `int GetGoodEvilValue(object oCreature)`
> Get an integer between 0 and 100 (inclusive) to represent oCreature's
> Good/Evil alignment
> (100=good, 0=evil)
> Return value if oCreature is not a valid creature: -1

#### `int GetAlignmentLawChaos(object oCreature)`
> Return an ALIGNMENT_* constant to represent oCreature's law/chaos alignment
> Return value if oCreature is not a valid creature: -1

#### `int GetAlignmentGoodEvil(object oCreature)`
> Return an ALIGNMENT_* constant to represent oCreature's good/evil alignment
> Return value if oCreature is not a valid creature: -1

#### `object GetFirstObjectInShape(int nShape, float fSize, location lTarget, int bLineOfSight = FALSE, int nObjectFilter = OBJECT_TYPE_CREATURE, vector vOrigin = [0.0, 0.0, 0.0])`
> Get the first object in nShape
> - nShape: SHAPE_*
> - fSize:
> -> If nShape == SHAPE_SPHERE, this is the radius of the sphere
> -> If nShape == SHAPE_SPELLCYLINDER, this is the length of the cylinder
> Spell Cylinder's always have a radius of 1.5m.
> -> If nShape == SHAPE_CONE, this is the widest radius of the cone
> -> If nShape == SHAPE_SPELLCONE, this is the length of the cone in the
> direction of lTarget. Spell cones are always 60 degrees with the origin
> at OBJECT_SELF.
> -> If nShape == SHAPE_CUBE, this is half the length of one of the sides of
> the cube
> - lTarget: This is the centre of the effect, usually GetSpellTargetLocation(),
> or the end of a cylinder or cone.
> - bLineOfSight: This controls whether to do a line-of-sight check on the
> object returned. Line of sight check is done from origin to target object
> at a height 1m above the ground
> (This can be used to ensure that spell effects do not go through walls.)
> - nObjectFilter: This allows you to filter out undesired object types, using
> bitwise "or".
> For example, to return only creatures and doors, the value for this
> parameter would be OBJECT_TYPE_CREATURE | OBJECT_TYPE_DOOR
> - vOrigin: This is only used for cylinders and cones, and specifies the
> origin of the effect(normally the spell-caster's position).
> Return value on error: OBJECT_INVALID

#### `object GetNextObjectInShape(int nShape, float fSize, location lTarget, int bLineOfSight = FALSE, int nObjectFilter = OBJECT_TYPE_CREATURE, vector vOrigin = [0.0, 0.0, 0.0])`
> Get the next object in nShape
> - nShape: SHAPE_*
> - fSize:
> -> If nShape == SHAPE_SPHERE, this is the radius of the sphere
> -> If nShape == SHAPE_SPELLCYLINDER, this is the length of the cylinder.
> Spell Cylinder's always have a radius of 1.5m.
> -> If nShape == SHAPE_CONE, this is the widest radius of the cone
> -> If nShape == SHAPE_SPELLCONE, this is the length of the cone in the
> direction of lTarget. Spell cones are always 60 degrees with the origin
> at OBJECT_SELF.
> -> If nShape == SHAPE_CUBE, this is half the length of one of the sides of
> the cube
> - lTarget: This is the centre of the effect, usually GetSpellTargetLocation(),
> or the end of a cylinder or cone.
> - bLineOfSight: This controls whether to do a line-of-sight check on the
> object returned. (This can be used to ensure that spell effects do not go
> through walls.) Line of sight check is done from origin to target object
> at a height 1m above the ground
> - nObjectFilter: This allows you to filter out undesired object types, using
> bitwise "or". For example, to return only creatures and doors, the value for
> this parameter would be OBJECT_TYPE_CREATURE | OBJECT_TYPE_DOOR
> - vOrigin: This is only used for cylinders and cones, and specifies the origin
> of the effect (normally the spell-caster's position).
> Return value on error: OBJECT_INVALID

#### `effect EffectEntangle()`
> Create an Entangle effect
> When applied, this effect will restrict the creature's movement and apply a
> (-2) to all attacks and a -4 to AC.

#### `void SignalEvent(object oObject, event evToRun)`
> Causes object oObject to run the event evToRun. The script on the object that is
> associated with the event specified will run.
> Events can be created using the following event functions:
> EventActivateItem() - This creates an OnActivateItem module event. The script for handling
> this event can be set in Module Properties on the Event Tab.
> EventConversation() - This creates on OnConversation creature event. The script for handling
> this event can be set by viewing the Creature Properties on a
> creature and then clicking on the Scripts Tab.
> EventSpellCastAt()  - This creates an OnSpellCastAt event. The script for handling this
> event can be set in the Scripts Tab of the Properties menu
> for the object.
> EventUserDefined()  - This creates on OnUserDefined event. The script for handling this event
> can be set in the Scripts Tab of the Properties menu for the object/area/module.

#### `event EventUserDefined(int nUserDefinedEventNumber)`
> Create an event of the type nUserDefinedEventNumber
> Note: This only creates the event. The event wont actually trigger until SignalEvent()
> is called using this created UserDefined event as an argument.
> For example:
> SignalEvent(oObject, EventUserDefined(9999));
> Once the event has been signaled. The script associated with the OnUserDefined event will
> run on the object oObject.
> To specify the OnUserDefined script that should run, view the object's Properties
> and click on the Scripts Tab. Then specify a script for the OnUserDefined event.
> From inside the OnUserDefined script call:
> GetUserDefinedEventNumber() to retrieve the value of nUserDefinedEventNumber
> that was used when the event was signaled.

#### `effect EffectDeath(int nSpectacularDeath = FALSE, int nDisplayFeedback = TRUE)`
> Create a Death effect
> - nSpectacularDeath: if this is TRUE, the creature to which this effect is
> applied will die in an extraordinary fashion
> - nDisplayFeedback

#### `effect EffectKnockdown()`
> Create a Knockdown effect
> This effect knocks creatures off their feet, they will sit until the effect
> is removed. This should be applied as a temporary effect with a 3 second
> duration minimum (1 second to fall, 1 second sitting, 1 second to get up).

#### `void ActionGiveItem(object oItem, object oGiveTo)`
> Give oItem to oGiveTo
> If oItem is not a valid item, or oGiveTo is not a valid object, nothing will
> happen.

#### `void ActionTakeItem(object oItem, object oTakeFrom)`
> Take oItem from oTakeFrom
> If oItem is not a valid item, or oTakeFrom is not a valid object, nothing
> will happen.

#### `vector VectorNormalize(vector vVector)`
> Normalize vVector

#### `effect EffectCurse(int nStrMod = 1, int nDexMod = 1, int nConMod = 1, int nIntMod = 1, int nWisMod = 1, int nChaMod = 1)`
> Create a Curse effect.
> - nStrMod: strength modifier
> - nDexMod: dexterity modifier
> - nConMod: constitution modifier
> - nIntMod: intelligence modifier
> - nWisMod: wisdom modifier
> - nChaMod: charisma modifier

#### `int GetAbilityScore(object oCreature, int nAbilityType, int nBaseAbilityScore = FALSE)`
> Get the ability score of type nAbility for a creature (otherwise 0)
> - oCreature: the creature whose ability score we wish to find out
> - nAbilityType: ABILITY_*
> - nBaseAbilityScore: if set to true will return the base ability score without
> bonuses (e.g. ability bonuses granted from equipped items).
> Return value on error: 0

#### `int GetIsDead(object oCreature)`
> Returns TRUE if oCreature is a dead NPC, dead PC or a dying PC.

#### `void PrintVector(vector vVector, int bPrepend)`
> Output vVector to the logfile.
> - vVector
> - bPrepend: if this is TRUE, the message will be prefixed with "PRINTVECTOR:"

#### `vector Vector(float x = 0.0f, float y = 0.0f, float z = 0.0f)`
> Create a vector with the specified values for x, y and z

#### `void SetFacingPoint(vector vTarget, object oObject = OBJECT_SELF)`
> Cause oObject to face vTarget.

#### `vector AngleToVector(float fAngle)`
> Convert fAngle to a vector

#### `float VectorToAngle(vector vVector)`
> Convert vVector to an angle

#### `int TouchAttackMelee(object oTarget, int bDisplayFeedback = TRUE, object oAttacker = OBJECT_SELF)`
> The oAttacker will perform a Melee Touch Attack on oTarget.
> This is not an action, and it assumes the caller is already within range of
> oTarget
> Returns 0 on a miss, 1 on a hit and 2 on a critical hit

#### `int TouchAttackRanged(object oTarget, int bDisplayFeedback = TRUE, object oAttacker = OBJECT_SELF)`
> The oAttacker will perform a Ranged Touch Attack on oTarget.
> Returns 0 on a miss, 1 on a hit and 2 on a critical hit

#### `effect EffectParalyze()`
> Create a Paralyze effect

#### `effect EffectSpellImmunity(int nImmunityToSpell = SPELL_ALL_SPELLS)`
> Create a Spell Immunity effect.
> There is a known bug with this function. There *must* be a parameter specified
> when this is called (even if the desired parameter is SPELL_ALL_SPELLS),
> otherwise an effect of type EFFECT_TYPE_INVALIDEFFECT will be returned.
> - nImmunityToSpell: SPELL_*
> Returns an effect of type EFFECT_TYPE_INVALIDEFFECT if nImmunityToSpell is
> invalid.

#### `effect EffectDeaf()`
> Create a Deaf effect

#### `float GetDistanceBetween(object oObjectA, object oObjectB)`
> Get the distance in metres between oObjectA and oObjectB.
> Return value if either object is invalid: 0.0f

#### `void SetLocalLocation(object oObject, string sVarName, location lValue)`
> Set oObject's local location variable sVarname to lValue

#### `location GetLocalLocation(object oObject, string sVarName)`
> Get oObject's local location variable sVarname

#### `effect EffectSleep()`
> Create a Sleep effect

#### `object GetItemInSlot(int nInventorySlot, object oCreature = OBJECT_SELF)`
> Get the object which is in oCreature's specified inventory slot
> - nInventorySlot: INVENTORY_SLOT_*
> - oCreature
> Returns OBJECT_INVALID if oCreature is not a valid creature or there is no
> item in nInventorySlot.

#### `effect EffectCharmed()`
> Create a Charm effect

#### `effect EffectConfused()`
> Create a Confuse effect

#### `effect EffectFrightened()`
> Create a Frighten effect

#### `effect EffectDominated()`
> Create a Dominate effect

#### `effect EffectDazed()`
> Create a Daze effect

#### `effect EffectStunned()`
> Create a Stun effect

#### `void SetCommandable(int bCommandable, object oTarget = OBJECT_SELF)`
> Set whether oTarget's action stack can be modified

#### `int GetCommandable(object oTarget = OBJECT_SELF)`
> Determine whether oTarget's action stack can be modified.

#### `effect EffectRegenerate(int nAmount, float fIntervalSeconds)`
> Create a Regenerate effect.
> - nAmount: amount of damage to be regenerated per time interval
> - fIntervalSeconds: length of interval in seconds

#### `effect EffectMovementSpeedIncrease(int nPercentChange)`
> Create a Movement Speed Increase effect.
> - nPercentChange - range 0 through 99
> eg.
> 0 = no change in speed
> 50 = 50% faster
> 99 = almost twice as fast

#### `int GetHitDice(object oCreature)`
> Get the number of hitdice for oCreature.
> Return value if oCreature is not a valid creature: 0

#### `void ActionForceFollowObject(object oFollow, float fFollowDistance = 0.0f)`
> The action subject will follow oFollow until a ClearAllActions() is called.
> - oFollow: this is the object to be followed
> - fFollowDistance: follow distance in metres
> No return value

#### `string GetTag(object oObject)`
> Get the Tag of oObject
> Return value if oObject is not a valid object: ""

#### `int ResistSpell(object oCaster, object oTarget)`
> Do a Spell Resistance check between oCaster and oTarget, returning TRUE if
> the spell was resisted.
> Return value if oCaster or oTarget is an invalid object: FALSE
> Return value if spell cast is not a player spell: - 1
> Return value if spell resisted: 1
> Return value if spell resisted via magic immunity: 2
> Return value if spell resisted via spell absorption: 3

#### `int GetEffectType(effect eEffect, int bAllTypes = FALSE)`
> Get the effect type (EFFECT_TYPE_*) of eEffect.
> - bAllTypes: Set to TRUE to return additional values the game used to return EFFECT_INVALIDEFFECT for, specifically:
> EFFECT_TYPE: APPEAR, CUTSCENE_DOMINATED, DAMAGE, DEATH, DISAPPEAR, HEAL, HITPOINTCHANGEWHENDYING, KNOCKDOWN, MODIFYNUMATTACKS, SUMMON_CREATURE, TAUNT, WOUNDING
> Return value if eEffect is invalid: EFFECT_INVALIDEFFECT

#### `effect EffectAreaOfEffect(int nAreaEffectId, string sOnEnterScript = "", string sHeartbeatScript = "", string sOnExitScript = "")`
> Create an Area Of Effect effect in the area of the creature it is applied to.
> If the scripts are not specified, default ones will be used.

#### `int GetFactionEqual(object oFirstObject, object oSecondObject = OBJECT_SELF)`
> Returns TRUE if the Faction Ids of the two objects are the same

#### `void ChangeFaction(object oObjectToChangeFaction, object oMemberOfFactionToJoin)`
> Make oObjectToChangeFaction join the faction of oMemberOfFactionToJoin.
> NB. ** This will only work for two NPCs **

#### `int GetIsListening(object oObject)`
> Returns TRUE if oObject is listening for something

#### `void SetListening(object oObject, int bValue)`
> Set whether oObject is listening.

#### `void SetListenPattern(object oObject, string sPattern, int nNumber = 0)`
> Set the string for oObject to listen for.
> Note: this does not set oObject to be listening.

#### `int TestStringAgainstPattern(string sPattern, string sStringToTest)`
> Returns TRUE if sStringToTest matches sPattern.

#### `string GetMatchedSubstring(int nString)`
> Get the appropriate matched string (this should only be used in
> OnConversation scripts).
> Returns the appropriate matched string, otherwise returns ""

#### `int GetMatchedSubstringsCount()`
> Get the number of string parameters available.
> Returns -1 if no string matched (this could be because of a dialogue event)

#### `effect EffectVisualEffect(int nVisualEffectId, int nMissEffect = FALSE, float fScale = 1.0f, vector vTranslate = [0.0, 0.0, 0.0], vector vRotate = [0.0, 0.0, 0.0])`
> Create a Visual Effect that can be applied to an object.
> - nVisualEffectId
> - nMissEffect: if this is TRUE, a random vector near or past the target will
> be generated, on which to play the effect

#### `object GetFactionWeakestMember(object oFactionMember = OBJECT_SELF, int bMustBeVisible = TRUE)`
> Get the weakest member of oFactionMember's faction.
> Returns OBJECT_INVALID if oFactionMember's faction is invalid.

#### `object GetFactionStrongestMember(object oFactionMember = OBJECT_SELF, int bMustBeVisible = TRUE)`
> Get the strongest member of oFactionMember's faction.
> Returns OBJECT_INVALID if oFactionMember's faction is invalid.

#### `object GetFactionMostDamagedMember(object oFactionMember = OBJECT_SELF, int bMustBeVisible = TRUE)`
> Get the member of oFactionMember's faction that has taken the most hit points
> of damage.
> Returns OBJECT_INVALID if oFactionMember's faction is invalid.

#### `object GetFactionLeastDamagedMember(object oFactionMember = OBJECT_SELF, int bMustBeVisible = TRUE)`
> Get the member of oFactionMember's faction that has taken the fewest hit
> points of damage.
> Returns OBJECT_INVALID if oFactionMember's faction is invalid.

#### `int GetFactionGold(object oFactionMember)`
> Get the amount of gold held by oFactionMember's faction.
> Returns -1 if oFactionMember's faction is invalid.

#### `int GetFactionAverageReputation(object oSourceFactionMember, object oTarget)`
> Get an integer between 0 and 100 (inclusive) that represents how
> oSourceFactionMember's faction feels about oTarget.
> Return value on error: -1

#### `int GetFactionAverageGoodEvilAlignment(object oFactionMember)`
> Get an integer between 0 and 100 (inclusive) that represents the average
> good/evil alignment of oFactionMember's faction.
> Return value on error: -1

#### `int GetFactionAverageLawChaosAlignment(object oFactionMember)`
> Get an integer between 0 and 100 (inclusive) that represents the average
> law/chaos alignment of oFactionMember's faction.
> Return value on error: -1

#### `int GetFactionAverageLevel(object oFactionMember)`
> Get the average level of the members of the faction.
> Return value on error: -1

#### `int GetFactionAverageXP(object oFactionMember)`
> Get the average XP of the members of the faction.
> Return value on error: -1

#### `int GetFactionMostFrequentClass(object oFactionMember)`
> Get the most frequent class in the faction - this can be compared with the
> constants CLASS_TYPE_*.
> Return value on error: -1

#### `object GetFactionWorstAC(object oFactionMember = OBJECT_SELF, int bMustBeVisible = TRUE)`
> Get the object faction member with the lowest armour class.
> Returns OBJECT_INVALID if oFactionMember's faction is invalid.

#### `object GetFactionBestAC(object oFactionMember = OBJECT_SELF, int bMustBeVisible = TRUE)`
> Get the object faction member with the highest armour class.
> Returns OBJECT_INVALID if oFactionMember's faction is invalid.

#### `void ActionSit(object oChair)`
> Sit in oChair.
> Note: Not all creatures will be able to sit and not all
> objects can be sat on.
> The object oChair must also be marked as usable in the toolset.
> For Example: To get a player to sit in oChair when they click on it,
> place the following script in the OnUsed event for the object oChair.
> void main()
> object oChair = OBJECT_SELF;
> AssignCommand(GetLastUsedBy(),ActionSit(oChair));

#### `int GetListenPatternNumber()`
> In an onConversation script this gets the number of the string pattern
> matched (the one that triggered the script).
> Returns -1 if no string matched

#### `void ActionJumpToObject(object oToJumpTo, int bWalkStraightLineToPoint = TRUE)`
> Jump to an object ID, or as near to it as possible.

#### `object GetWaypointByTag(string sWaypointTag)`
> Get the first waypoint with the specified tag.
> Returns OBJECT_INVALID if the waypoint cannot be found.

#### `object GetTransitionTarget(object oTransition)`
> Get the destination object for the given object.
> All objects can hold a transition target, but only Doors and Triggers
> will be made clickable by the game engine (This may change in the
> future). You can set and query transition targets on other objects for
> your own scripted purposes.
> Returns OBJECT_INVALID if oTransition does not hold a target.

#### `effect EffectLinkEffects(effect eChildEffect, effect eParentEffect)`
> Link the two supplied effects, returning eChildEffect as a child of
> eParentEffect.
> Note: When applying linked effects if the target is immune to all valid
> effects all other effects will be removed as well. This means that if you
> apply a visual effect and a silence effect (in a link) and the target is
> immune to the silence effect that the visual effect will get removed as well.
> Visual Effects are not considered "valid" effects for the purposes of
> determining if an effect will be removed or not and as such should never be
> packaged *only* with other visual effects in a link.

#### `object GetObjectByTag(string sTag, int nNth = 0)`
> Get the nNth object with the specified tag.
> - sTag
> - nNth: the nth object with this tag may be requested
> Returns OBJECT_INVALID if the object cannot be found.
> Note: The module cannot be retrieved by GetObjectByTag(), use GetModule() instead.

#### `void AdjustAlignment(object oSubject, int nAlignment, int nShift, int bAllPartyMembers = TRUE)`
> Adjust the alignment of oSubject.
> - oSubject
> - nAlignment:
> -> ALIGNMENT_LAWFUL/ALIGNMENT_CHAOTIC/ALIGNMENT_GOOD/ALIGNMENT_EVIL: oSubject's
> alignment will be shifted in the direction specified
> -> ALIGNMENT_ALL: nShift will be added to oSubject's law/chaos and
> good/evil alignment values
> -> ALIGNMENT_NEUTRAL: nShift is applied to oSubject's law/chaos and
> good/evil alignment values in the direction which is towards neutrality.
> e.g. If oSubject has a law/chaos value of 10 (i.e. chaotic) and a
> good/evil value of 80 (i.e. good) then if nShift is 15, the
> law/chaos value will become (10+15)=25 and the good/evil value will
> become (80-25)=55
> Furthermore, the shift will at most take the alignment value to 50 and
> not beyond.
> e.g. If oSubject has a law/chaos value of 40 and a good/evil value of 70,
> then if nShift is 15, the law/chaos value will become 50 and the
> good/evil value will become 55
> - nShift: this is the desired shift in alignment
> - bAllPartyMembers: when TRUE the alignment shift of oSubject also has a
> diminished affect all members of oSubject's party (if oSubject is a Player).
> When FALSE the shift only affects oSubject.
> No return value

#### `void ActionWait(float fSeconds)`
> Do nothing for fSeconds seconds.

#### `void SetAreaTransitionBMP(int nPredefinedAreaTransition, string sCustomAreaTransitionBMP = "")`
> Set the transition bitmap of a player; this should only be called in area
> transition scripts. This action should be run by the person "clicking" the
> area transition via AssignCommand.
> - nPredefinedAreaTransition:
> -> To use a predefined area transition bitmap, use one of AREA_TRANSITION_*
> -> To use a custom, user-defined area transition bitmap, use
> AREA_TRANSITION_USER_DEFINED and specify the filename in the second
> parameter
> - sCustomAreaTransitionBMP: this is the filename of a custom, user-defined
> area transition bitmap

#### `void ActionStartConversation(object oObjectToConverseWith, string sDialogResRef = "", int bPrivateConversation = FALSE, int bPlayHello = TRUE)`
> Starts a conversation with oObjectToConverseWith - this will cause their
> OnDialog event to fire.
> - oObjectToConverseWith
> - sDialogResRef: If this is blank, the creature's own dialogue file will be used
> - bPrivateConversation
> Turn off bPlayHello if you don't want the initial greeting to play

#### `void ActionPauseConversation()`
> Pause the current conversation.

#### `void ActionResumeConversation()`
> Resume a conversation after it has been paused.

#### `effect EffectBeam(int nBeamVisualEffect, object oEffector, int nBodyPart, int bMissEffect = FALSE, float fScale = 1.0f, vector vTranslate = [0.0, 0.0, 0.0], vector vRotate = [0.0, 0.0, 0.0])`
> Create a Beam effect.
> - nBeamVisualEffect: VFX_BEAM_*
> - oEffector: the beam is emitted from this creature
> - nBodyPart: BODY_NODE_*
> - bMissEffect: If this is TRUE, the beam will fire to a random vector near or
> past the target
> Returns an effect of type EFFECT_TYPE_INVALIDEFFECT if nBeamVisualEffect is
> not valid.

#### `int GetReputation(object oSource, object oTarget)`
> Get an integer between 0 and 100 (inclusive) that represents how oSource
> feels about oTarget.
> -> 0-10 means oSource is hostile to oTarget
> -> 11-89 means oSource is neutral to oTarget
> -> 90-100 means oSource is friendly to oTarget
> Returns -1 if oSource or oTarget does not identify a valid object

#### `void AdjustReputation(object oTarget, object oSourceFactionMember, int nAdjustment)`
> Adjust how oSourceFactionMember's faction feels about oTarget by the
> specified amount.
> Note: This adjusts Faction Reputation, how the entire faction that
> oSourceFactionMember is in, feels about oTarget.
> No return value
> Note: You can't adjust a player character's (PC) faction towards
> NPCs, so attempting to make an NPC hostile by passing in a PC object
> as oSourceFactionMember in the following call will fail:
> AdjustReputation(oNPC,oPC,-100);
> Instead you should pass in the PC object as the first
> parameter as in the following call which should succeed:
> AdjustReputation(oPC,oNPC,-100);
> Note: Will fail if oSourceFactionMember is a plot object.

#### `object GetSittingCreature(object oChair)`
> Get the creature that is currently sitting on the specified object.
> - oChair
> Returns OBJECT_INVALID if oChair is not a valid placeable.

#### `object GetGoingToBeAttackedBy(object oTarget)`
> Get the creature that is going to attack oTarget.
> Note: This value is cleared out at the end of every combat round and should
> not be used in any case except when getting a "going to be attacked" shout
> from the master creature (and this creature is a henchman)
> Returns OBJECT_INVALID if oTarget is not a valid creature.

#### `effect EffectSpellResistanceIncrease(int nValue)`
> Create a Spell Resistance Increase effect.
> - nValue: size of spell resistance increase

#### `location GetLocation(object oObject)`
> Get the location of oObject.

#### `void ActionJumpToLocation(location lLocation)`
> The subject will jump to lLocation instantly (even between areas).
> If lLocation is invalid, nothing will happen.

#### `location Location(object oArea, vector vPosition, float fOrientation)`
> Create a location.
> The special constant LOCATION_INVALID describes a location with area equalling OBJECT_INVALID
> and all other values 0.0f. Declared but not initialised location variables default to this value.

#### `void ApplyEffectAtLocation(int nDurationType, effect eEffect, location lLocation, float fDuration = 0.0f)`
> Apply eEffect at lLocation.

#### `int GetIsPC(object oCreature)`
> Returns TRUE if oCreature is a Player Controlled character.

#### `float FeetToMeters(float fFeet)`
> Convert fFeet into a number of meters.

#### `float YardsToMeters(float fYards)`
> Convert fYards into a number of meters.

#### `void ApplyEffectToObject(int nDurationType, effect eEffect, object oTarget, float fDuration = 0.0f)`
> Apply eEffect to oTarget.

#### `void SpeakString(string sStringToSpeak, int nTalkVolume = TALKVOLUME_TALK)`
> The caller will immediately speak sStringToSpeak (this is different from
> ActionSpeakString)
> - sStringToSpeak
> - nTalkVolume: TALKVOLUME_*

#### `location GetSpellTargetLocation()`
> Get the location of the caller's last spell target.

#### `vector GetPositionFromLocation(location lLocation)`
> Get the position vector from lLocation.

#### `object GetAreaFromLocation(location lLocation)`
> Get the area's object ID from lLocation.

#### `float GetFacingFromLocation(location lLocation)`
> Get the orientation value from lLocation.

#### `object GetNearestCreatureToLocation(int nFirstCriteriaType, int nFirstCriteriaValue, location lLocation, int nNth = 1, int nSecondCriteriaType = -1, int nSecondCriteriaValue = -1, int nThirdCriteriaType = -1, int nThirdCriteriaValue = -1)`
> Get the creature nearest to lLocation, subject to all the criteria specified.
> - nFirstCriteriaType: CREATURE_TYPE_*
> - nFirstCriteriaValue:
> -> CLASS_TYPE_* if nFirstCriteriaType was CREATURE_TYPE_CLASS
> -> SPELL_* if nFirstCriteriaType was CREATURE_TYPE_DOES_NOT_HAVE_SPELL_EFFECT
> or CREATURE_TYPE_HAS_SPELL_EFFECT
> -> TRUE or FALSE if nFirstCriteriaType was CREATURE_TYPE_IS_ALIVE
> -> PERCEPTION_* if nFirstCriteriaType was CREATURE_TYPE_PERCEPTION
> -> PLAYER_CHAR_IS_PC or PLAYER_CHAR_NOT_PC if nFirstCriteriaType was
> CREATURE_TYPE_PLAYER_CHAR
> -> RACIAL_TYPE_* if nFirstCriteriaType was CREATURE_TYPE_RACIAL_TYPE
> -> REPUTATION_TYPE_* if nFirstCriteriaType was CREATURE_TYPE_REPUTATION
> For example, to get the nearest PC, use
> (CREATURE_TYPE_PLAYER_CHAR, PLAYER_CHAR_IS_PC)
> - lLocation: We're trying to find the creature of the specified type that is
> nearest to lLocation
> - nNth: We don't have to find the first nearest: we can find the Nth nearest....
> - nSecondCriteriaType: This is used in the same way as nFirstCriteriaType to
> further specify the type of creature that we are looking for.
> - nSecondCriteriaValue: This is used in the same way as nFirstCriteriaValue
> to further specify the type of creature that we are looking for.
> - nThirdCriteriaType: This is used in the same way as nFirstCriteriaType to
> further specify the type of creature that we are looking for.
> - nThirdCriteriaValue: This is used in the same way as nFirstCriteriaValue to
> further specify the type of creature that we are looking for.
> Return value on error: OBJECT_INVALID

#### `object GetNearestObject(int nObjectType = OBJECT_TYPE_ALL, object oTarget = OBJECT_SELF, int nNth = 1)`
> Get the Nth object nearest to oTarget that is of the specified type.
> - nObjectType: OBJECT_TYPE_*
> - oTarget
> - nNth
> Return value on error: OBJECT_INVALID

#### `object GetNearestObjectToLocation(int nObjectType, location lLocation, int nNth = 1)`
> Get the nNth object nearest to lLocation that is of the specified type.
> - nObjectType: OBJECT_TYPE_*
> - lLocation
> - nNth
> Return value on error: OBJECT_INVALID

#### `object GetNearestObjectByTag(string sTag, object oTarget = OBJECT_SELF, int nNth = 1)`
> Get the nth Object nearest to oTarget that has sTag as its tag.
> Return value on error: OBJECT_INVALID

#### `float IntToFloat(int nInteger)`
> Convert nInteger into a floating point number.

#### `int FloatToInt(float fFloat)`
> Convert fFloat into the nearest integer.

#### `int StringToInt(string sNumber)`
> Convert sNumber into an integer.

#### `float StringToFloat(string sNumber)`
> Convert sNumber into a floating point number.

#### `void ActionCastSpellAtLocation(int nSpell, location lTargetLocation, int nMetaMagic = METAMAGIC_ANY, int bCheat = FALSE, int nProjectilePathType = PROJECTILE_PATH_TYPE_DEFAULT, int bInstantSpell = FALSE, int nClass = -1, int bSpontaneousCast = FALSE, int nDomainlevel = 0)`
> Cast spell nSpell at lTargetLocation.
> - nSpell: SPELL_*
> - lTargetLocation
> - nMetaMagic: METAMAGIC_*. If nClass is specified, cannot be METAMAGIC_ANY.
> - bCheat: If this is TRUE, then the executor of the action doesn't have to be
> able to cast the spell. Ignored if nClass is specified.
> - bCheat: If this is TRUE, then the executor of the action doesn't have to be
> able to cast the spell.
> - nProjectilePathType: PROJECTILE_PATH_TYPE_*
> - bInstantSpell: If this is TRUE, the spell is cast immediately; this allows
> the end-user to simulate
> a high-level magic user having lots of advance warning of impending trouble.
> - nClass: If set to a CLASS_TYPE_* it will cast using that class specifically.
> CLASS_TYPE_INVALID will use spell abilities.
> - bSpontaneousCast: If set to TRUE will attempt to cast the given spell spontaneously,
> ie a Cleric casting Cure Light Wounds using any level 1 slot. Needs a valid nClass set.
> - nDomainLevel: The level of the spell if cast from a domain slot.
> eg SPELL_HEAL can be spell level 5 on a cleric. Use 0 for no domain slot.

#### `int GetIsEnemy(object oTarget, object oSource = OBJECT_SELF)`
> Returns TRUE if oSource considers oTarget as an enemy.

#### `int GetIsFriend(object oTarget, object oSource = OBJECT_SELF)`
> Returns TRUE if oSource considers oTarget as a friend.

#### `int GetIsNeutral(object oTarget, object oSource = OBJECT_SELF)`
> Returns TRUE if oSource considers oTarget as neutral.

#### `object GetPCSpeaker()`
> Get the PC that is involved in the conversation.
> Returns OBJECT_INVALID on error.

#### `string GetStringByStrRef(int nStrRef, int nGender = GENDER_MALE)`
> Get a string from the talk table using nStrRef.

#### `void ActionSpeakStringByStrRef(int nStrRef, int nTalkVolume = TALKVOLUME_TALK)`
> Causes the creature to speak a translated string.
> - nStrRef: Reference of the string in the talk table
> - nTalkVolume: TALKVOLUME_*

#### `void DestroyObject(object oDestroy, float fDelay = 0.0f)`
> Destroy oObject (irrevocably).
> This will not work on modules and areas.

#### `object GetModule()`
> Get the module.
> Return value on error: OBJECT_INVALID

#### `object CreateObject(int nObjectType, string sTemplate, location lLocation, int bUseAppearAnimation = FALSE, string sNewTag = "")`
> Create an object of the specified type at lLocation.
> - nObjectType: OBJECT_TYPE_ITEM, OBJECT_TYPE_CREATURE, OBJECT_TYPE_PLACEABLE,
> OBJECT_TYPE_STORE, OBJECT_TYPE_WAYPOINT
> - sTemplate
> - lLocation
> - bUseAppearAnimation
> - sNewTag - if this string is not empty, it will replace the default tag from the template

#### `event EventSpellCastAt(object oCaster, int nSpell, int bHarmful = TRUE)`
> Create an event which triggers the "SpellCastAt" script
> Note: This only creates the event. The event wont actually trigger until SignalEvent()
> is called using this created SpellCastAt event as an argument.
> For example:
> SignalEvent(oCreature, EventSpellCastAt(oCaster, SPELL_MAGIC_MISSILE, TRUE));
> This function doesn't cast the spell specified, it only creates an event so that
> when the event is signaled on an object, the object will use its OnSpellCastAt script
> to react to the spell being cast.
> To specify the OnSpellCastAt script that should run, view the Object's Properties
> and click on the Scripts Tab. Then specify a script for the OnSpellCastAt event.
> From inside the OnSpellCastAt script call:
> GetLastSpellCaster() to get the object that cast the spell (oCaster).
> GetLastSpell() to get the type of spell cast (nSpell)
> GetLastSpellHarmful() to determine if the spell cast at the object was harmful.

#### `object GetLastSpellCaster()`
> This is for use in a "Spell Cast" script, it gets who cast the spell.
> The spell could have been cast by a creature, placeable or door.
> Returns OBJECT_INVALID if the caller is not a creature, placeable or door.

#### `int GetLastSpell()`
> This is for use in a "Spell Cast" script, it gets the ID of the spell that
> was cast.

#### `int GetUserDefinedEventNumber()`
> This is for use in a user-defined script, it gets the event number.

#### `int GetSpellId()`
> This is for use in a Spell script, it gets the ID of the spell that is being cast.
> If used in an Area of Effect script it will return the ID of the spell that generated the AOE effect.
> Returns the spell ID (SPELL_*) or -1 if no spell was cast or on error

#### `string RandomName(int nNameType = NAME_FIRST_GENERIC_MALE)`
> Generate a random name.
> nNameType: The type of random name to be generated (NAME_*)

#### `effect EffectPoison(int nPoisonType)`
> Create a Poison effect.
> - nPoisonType: POISON_*

#### `effect EffectDisease(int nDiseaseType)`
> Create a Disease effect.
> - nDiseaseType: DISEASE_*

#### `effect EffectSilence()`
> Create a Silence effect.

#### `string GetName(object oObject, int bOriginalName = FALSE)`
> Get the name of oObject.
> - bOriginalName:  if set to true any new name specified via a SetName scripting command
> is ignored and the original object's name is returned instead.

#### `object GetLastSpeaker()`
> Use this in a conversation script to get the person with whom you are conversing.
> Returns OBJECT_INVALID if the caller is not a valid creature.

#### `int BeginConversation(string sResRef = "", object oObjectToDialog = OBJECT_INVALID)`
> Use this in an OnDialog script to start up the dialog tree.
> - sResRef: if this is not specified, the default dialog file will be used
> - oObjectToDialog: if this is not specified the person that triggered the
> event will be used

#### `object GetLastPerceived()`
> Use this in an OnPerception script to get the object that was perceived.
> Returns OBJECT_INVALID if the caller is not a valid creature.

#### `int GetLastPerceptionHeard()`
> Use this in an OnPerception script to determine whether the object that was
> perceived was heard.

#### `int GetLastPerceptionInaudible()`
> Use this in an OnPerception script to determine whether the object that was
> perceived has become inaudible.

#### `int GetLastPerceptionSeen()`
> Use this in an OnPerception script to determine whether the object that was
> perceived was seen.

#### `object GetLastClosedBy(object oObject = OBJECT_SELF)`
> Use this in an OnClosed script to get the object that closed oObject.
> Returns OBJECT_INVALID if oObject is not a valid door, placeable or store.

#### `int GetLastPerceptionVanished()`
> Use this in an OnPerception script to determine whether the object that was
> perceived has vanished.

#### `object GetFirstInPersistentObject(object oPersistentObject = OBJECT_SELF, int nResidentObjectType = OBJECT_TYPE_CREATURE, int nPersistentZone = PERSISTENT_ZONE_ACTIVE)`
> Get the first object within oPersistentObject.
> - oPersistentObject
> - nResidentObjectType: OBJECT_TYPE_*
> - nPersistentZone: PERSISTENT_ZONE_ACTIVE. [This could also take the value
> PERSISTENT_ZONE_FOLLOW, but this is no longer used.]
> Returns OBJECT_INVALID if no object is found.

#### `object GetNextInPersistentObject(object oPersistentObject = OBJECT_SELF, int nResidentObjectType = OBJECT_TYPE_CREATURE, int nPersistentZone = PERSISTENT_ZONE_ACTIVE)`
> Get the next object within oPersistentObject.
> - oPersistentObject
> - nResidentObjectType: OBJECT_TYPE_*
> - nPersistentZone: PERSISTENT_ZONE_ACTIVE. [This could also take the value
> PERSISTENT_ZONE_FOLLOW, but this is no longer used.]
> Returns OBJECT_INVALID if no object is found.

#### `object GetAreaOfEffectCreator(object oAreaOfEffectObject = OBJECT_SELF)`
> This returns the creator of oAreaOfEffectObject.
> Returns OBJECT_INVALID if oAreaOfEffectObject is not a valid Area of Effect object.

#### `void DeleteLocalInt(object oObject, string sVarName)`
> Delete oObject's local integer variable sVarName

#### `void DeleteLocalFloat(object oObject, string sVarName)`
> Delete oObject's local float variable sVarName

#### `void DeleteLocalString(object oObject, string sVarName)`
> Delete oObject's local string variable sVarName

#### `void DeleteLocalObject(object oObject, string sVarName)`
> Delete oObject's local object variable sVarName

#### `void DeleteLocalLocation(object oObject, string sVarName)`
> Delete oObject's local location variable sVarName

#### `effect EffectHaste()`
> Create a Haste effect.

#### `effect EffectSlow()`
> Create a Slow effect.

#### `string ObjectToString(object oObject)`
> Convert oObject into a hexadecimal string.

#### `effect EffectImmunity(int nImmunityType)`
> Create an Immunity effect.
> - nImmunityType: IMMUNITY_TYPE_*

#### `int GetIsImmune(object oCreature, int nImmunityType, object oVersus = OBJECT_INVALID)`
> - oCreature
> - nImmunityType: IMMUNITY_TYPE_*
> - oVersus: if this is specified, then we also check for the race and
> alignment of oVersus
> Returns TRUE if oCreature has immunity of type nImmunity versus oVersus.

#### `effect EffectDamageImmunityIncrease(int nDamageType, int nPercentImmunity)`
> Creates a Damage Immunity Increase effect.
> - nDamageType: DAMAGE_TYPE_*
> - nPercentImmunity

#### `int GetEncounterActive(object oEncounter = OBJECT_SELF)`
> Determine whether oEncounter is active.

#### `void SetEncounterActive(int nNewValue, object oEncounter = OBJECT_SELF)`
> Set oEncounter's active state to nNewValue.
> - nNewValue: TRUE/FALSE
> - oEncounter

#### `int GetEncounterSpawnsMax(object oEncounter = OBJECT_SELF)`
> Get the maximum number of times that oEncounter will spawn.

#### `void SetEncounterSpawnsMax(int nNewValue, object oEncounter = OBJECT_SELF)`
> Set the maximum number of times that oEncounter can spawn

#### `int GetEncounterSpawnsCurrent(object oEncounter = OBJECT_SELF)`
> Get the number of times that oEncounter has spawned so far

#### `void SetEncounterSpawnsCurrent(int nNewValue, object oEncounter = OBJECT_SELF)`
> Set the number of times that oEncounter has spawned so far

#### `object GetModuleItemAcquired()`
> Use this in an OnItemAcquired script to get the item that was acquired.
> Returns OBJECT_INVALID if the module is not valid.

#### `object GetModuleItemAcquiredFrom()`
> Use this in an OnItemAcquired script to get the creatre that previously
> possessed the item.
> Returns OBJECT_INVALID if the item was picked up from the ground.

#### `void SetCustomToken(int nCustomTokenNumber, string sTokenValue)`
> Set the value for a custom token.

#### `int GetHasFeat(int nFeat, object oCreature = OBJECT_SELF, int bIgnoreUses = FALSE)`
> Determine whether oCreature has nFeat, optionally if nFeat is useable.
> - nFeat: FEAT_*
> - oCreature
> - bIgnoreUses: Will check if the creature has the given feat even if it has no uses remaining

#### `int GetHasSkill(int nSkill, object oCreature = OBJECT_SELF)`
> Determine whether oCreature has nSkill, and nSkill is useable.
> - nSkill: SKILL_*
> - oCreature

#### `void ActionUseFeat(int nFeat, object oTarget = OBJECT_SELF, int nSubFeat = 0, location lTarget = LOCATION_INVALID)`
> Use nFeat on oTarget.
> - nFeat: FEAT_*
> - oTarget: Target of the feat. Must be OBJECT_INVALID if lTarget is used.
> - nSubFeat: - For feats with subdial options, use either:
> - SUBFEAT_* for some specific feats like called shot
> - spells.2da line of the subdial spell, eg 708 for Dragon Shape: Blue Dragon when using FEAT_EPIC_WILD_SHAPE_DRAGON
> - lTarget: The location to use the feat at. oTarget must be OBJECT_INVALID for this to be used.

#### `void ActionUseSkill(int nSkill, object oTarget, int nSubSkill = 0, object oItemUsed = OBJECT_INVALID)`
> Runs the action "UseSkill" on the current creature
> Use nSkill on oTarget.
> - nSkill: SKILL_*
> - oTarget
> - nSubSkill: SUBSKILL_*
> - oItemUsed: Item to use in conjunction with the skill

#### `int GetObjectSeen(object oTarget, object oSource = OBJECT_SELF)`
> Determine whether oSource sees oTarget.
> NOTE: This *only* works on creatures, as visibility lists are not
> maintained for non-creature objects.

#### `int GetObjectHeard(object oTarget, object oSource = OBJECT_SELF)`
> Determine whether oSource hears oTarget.
> NOTE: This *only* works on creatures, as visibility lists are not
> maintained for non-creature objects.

#### `object GetLastPlayerDied()`
> Use this in an OnPlayerDeath module script to get the last player that died.

#### `object GetModuleItemLost()`
> Use this in an OnItemLost script to get the item that was lost/dropped.
> Returns OBJECT_INVALID if the module is not valid.

#### `object GetModuleItemLostBy()`
> Use this in an OnItemLost script to get the creature that lost the item.
> Returns OBJECT_INVALID if the module is not valid.

#### `void ActionDoCommand(action aActionToDo)`
> Do aActionToDo.

#### `event EventConversation()`
> Creates a conversation event.
> Note: This only creates the event. The event wont actually trigger until SignalEvent()
> is called using this created conversation event as an argument.
> For example:
> SignalEvent(oCreature, EventConversation());
> Once the event has been signaled. The script associated with the OnConversation event will
> run on the creature oCreature.
> To specify the OnConversation script that should run, view the Creature Properties on
> the creature and click on the Scripts Tab. Then specify a script for the OnConversation event.

#### `void SetEncounterDifficulty(int nEncounterDifficulty, object oEncounter = OBJECT_SELF)`
> Set the difficulty level of oEncounter.
> - nEncounterDifficulty: ENCOUNTER_DIFFICULTY_*
> - oEncounter

#### `int GetEncounterDifficulty(object oEncounter = OBJECT_SELF)`
> Get the difficulty level of oEncounter.

#### `float GetDistanceBetweenLocations(location lLocationA, location lLocationB)`
> Get the distance between lLocationA and lLocationB.

#### `int GetReflexAdjustedDamage(int nDamage, object oTarget, int nDC, int nSaveType = SAVING_THROW_TYPE_NONE, object oSaveVersus = OBJECT_SELF)`
> Use this in spell scripts to get nDamage adjusted by oTarget's reflex and
> evasion saves.
> - nDamage
> - oTarget
> - nDC: Difficulty check
> - nSaveType: SAVING_THROW_TYPE_*
> - oSaveVersus

#### `void PlayAnimation(int nAnimation, float fSpeed = 1.0, float fSeconds = 0.0)`
> Play nAnimation immediately.
> - nAnimation: ANIMATION_*
> - fSpeed
> - fSeconds

#### `talent TalentSpell(int nSpell)`
> Create a Spell Talent.
> - nSpell: SPELL_*

#### `talent TalentFeat(int nFeat)`
> Create a Feat Talent.
> - nFeat: FEAT_*

#### `talent TalentSkill(int nSkill)`
> Create a Skill Talent.
> - nSkill: SKILL_*

#### `int GetHasSpellEffect(int nSpell, object oObject = OBJECT_SELF)`
> Determines whether oObject has any effects applied by nSpell
> - nSpell: SPELL_*
> - oObject
> The spell id on effects is only valid if the effect is created
> when the spell script runs. If it is created in a delayed command
> then the spell id on the effect will be invalid.

#### `int GetEffectSpellId(effect eSpellEffect)`
> Get the spell (SPELL_*) that applied eSpellEffect.
> Returns -1 if eSpellEffect was applied outside a spell script.

#### `int GetCreatureHasTalent(talent tTalent, object oCreature = OBJECT_SELF)`
> Determine whether oCreature has tTalent.

#### `talent GetCreatureTalentRandom(int nCategory, object oCreature = OBJECT_SELF)`
> Get a random talent of oCreature, within nCategory.
> - nCategory: TALENT_CATEGORY_*
> - oCreature

#### `talent GetCreatureTalentBest(int nCategory, int nCRMax, object oCreature = OBJECT_SELF)`
> Get the best talent (i.e. closest to nCRMax without going over) of oCreature,
> within nCategory.
> - nCategory: TALENT_CATEGORY_*
> - nCRMax: Challenge Rating of the talent
> - oCreature

#### `void ActionUseTalentOnObject(talent tChosenTalent, object oTarget)`
> Use tChosenTalent on oTarget.

#### `void ActionUseTalentAtLocation(talent tChosenTalent, location lTargetLocation)`
> Use tChosenTalent at lTargetLocation.

#### `int GetGoldPieceValue(object oItem)`
> Get the gold piece value of oItem.
> Returns 0 if oItem is not a valid item.

#### `int GetIsPlayableRacialType(object oCreature)`
> Returns TRUE if oCreature is of a playable racial type.

#### `void JumpToLocation(location lDestination)`
> Jump to lDestination.  The action is added to the TOP of the action queue.

#### `effect EffectTemporaryHitpoints(int nHitPoints)`
> Create a Temporary Hitpoints effect.
> - nHitPoints: a positive integer
> Returns an effect of type EFFECT_TYPE_INVALIDEFFECT if nHitPoints < 0.

#### `int GetSkillRank(int nSkill, object oTarget = OBJECT_SELF, int nBaseSkillRank = FALSE)`
> Get the number of ranks that oTarget has in nSkill.
> - nSkill: SKILL_*
> - oTarget
> - nBaseSkillRank: if set to true returns the number of base skill ranks the target
> has (i.e. not including any bonuses from ability scores, feats, etc).
> Returns -1 if oTarget doesn't have nSkill.
> Returns 0 if nSkill is untrained.

#### `object GetAttackTarget(object oCreature = OBJECT_SELF)`
> Get the attack target of oCreature.
> This only works when oCreature is in combat.

#### `int GetLastAttackType(object oCreature = OBJECT_SELF)`
> Get the attack type (SPECIAL_ATTACK_*) of oCreature's last attack.
> This only works when oCreature is in combat.

#### `int GetLastAttackMode(object oCreature = OBJECT_SELF)`
> Get the attack mode (COMBAT_MODE_*) of oCreature's last attack.
> This only works when oCreature is in combat.

#### `object GetMaster(object oAssociate = OBJECT_SELF)`
> Get the master of oAssociate.

#### `int GetIsInCombat(object oCreature = OBJECT_SELF)`
> Returns TRUE if oCreature is in combat.

#### `int GetLastAssociateCommand(object oAssociate = OBJECT_SELF)`
> Get the last command (ASSOCIATE_COMMAND_*) issued to oAssociate.

#### `void GiveGoldToCreature(object oCreature, int nGP)`
> Give nGP gold to oCreature.

#### `void SetIsDestroyable(int bDestroyable, int bRaiseable = TRUE, int bSelectableWhenDead = FALSE, object oObject = OBJECT_SELF)`
> Set the destroyable status of oObject
> - bDestroyable: If this is FALSE, the caller does not fade out on death, but
> sticks around as a corpse.
> - bRaiseable: If this is TRUE, the caller can be raised via resurrection.
> - bSelectableWhenDead: If this is TRUE, the caller is selectable after death.
> - oObject: Object to affect.

#### `void SetLocked(object oTarget, int bLocked)`
> Set the locked state of oTarget, which can be a door or a placeable object.

#### `int GetLocked(object oTarget)`
> Get the locked state of oTarget, which can be a door or a placeable object.

#### `object GetClickingObject()`
> Use this in a trigger's OnClick event script to get the object that last
> clicked on it.
> This is identical to GetEnteringObject.
> GetClickingObject() should not be called from a placeable's OnClick event,
> instead use GetPlaceableLastClickedBy();

#### `void SetAssociateListenPatterns(object oTarget = OBJECT_SELF)`
> Initialise oTarget to listen for the standard Associates commands.

#### `object GetLastWeaponUsed(object oCreature)`
> Get the last weapon that oCreature used in an attack.
> Returns OBJECT_INVALID if oCreature did not attack, or has no weapon equipped.

#### `void ActionInteractObject(object oPlaceable)`
> Use oPlaceable.

#### `object GetLastUsedBy()`
> Get the last object that used the placeable object that is calling this function.
> Returns OBJECT_INVALID if it is called by something other than a placeable or
> a door.

#### `int GetAbilityModifier(int nAbility, object oCreature = OBJECT_SELF)`
> Returns the ability modifier for the specified ability
> Get oCreature's ability modifier for nAbility.
> - nAbility: ABILITY_*
> - oCreature

#### `int GetIdentified(object oItem)`
> Determined whether oItem has been identified.

#### `void SetIdentified(object oItem, int bIdentified)`
> Set whether oItem has been identified.

#### `void SummonAnimalCompanion(object oMaster = OBJECT_SELF)`
> Summon an Animal Companion

#### `void SummonFamiliar(object oMaster = OBJECT_SELF)`
> Summon a Familiar

#### `object GetBlockingDoor()`
> Get the last blocking door encountered by the caller of this function.
> Returns OBJECT_INVALID if the caller is not a valid creature.

#### `int GetIsDoorActionPossible(object oTargetDoor, int nDoorAction)`
> - oTargetDoor
> - nDoorAction: DOOR_ACTION_*
> Returns TRUE if nDoorAction can be performed on oTargetDoor.

#### `void DoDoorAction(object oTargetDoor, int nDoorAction)`
> Perform nDoorAction on oTargetDoor.

#### `object GetFirstItemInInventory(object oTarget = OBJECT_SELF)`
> Get the first item in oTarget's inventory (start to cycle through oTarget's
> inventory).
> Returns OBJECT_INVALID if oTarget is not a creature, item, placeable or store,
> or if no item is found.

#### `object GetNextItemInInventory(object oTarget = OBJECT_SELF)`
> Get the next item in oTarget's inventory (continue to cycle through oTarget's
> inventory).
> Returns OBJECT_INVALID if oTarget is not a creature, item, placeable or store,
> or if no item is found.

#### `int GetClassByPosition(int nClassPosition, object oCreature = OBJECT_SELF)`
> A creature can have up to three classes.  This function determines the
> creature's class (CLASS_TYPE_*) based on nClassPosition.
> - nClassPosition: 1, 2 or 3
> - oCreature
> Returns CLASS_TYPE_INVALID if the oCreature does not have a class in
> nClassPosition (i.e. a single-class creature will only have a value in
> nClassLocation=1) or if oCreature is not a valid creature.

#### `int GetLevelByPosition(int nClassPosition, object oCreature = OBJECT_SELF)`
> A creature can have up to three classes.  This function determines the
> creature's class level based on nClass Position.
> - nClassPosition: 1, 2 or 3
> - oCreature
> Returns 0 if oCreature does not have a class in nClassPosition
> (i.e. a single-class creature will only have a value in nClassLocation=1)
> or if oCreature is not a valid creature.

#### `int GetLevelByClass(int nClassType, object oCreature = OBJECT_SELF)`
> Determine the levels that oCreature holds in nClassType.
> - nClassType: CLASS_TYPE_*
> - oCreature

#### `int GetDamageDealtByType(int nDamageType)`
> Get the amount of damage of type nDamageType that has been dealt to the caller.
> - nDamageType: DAMAGE_TYPE_*

#### `int GetTotalDamageDealt()`
> Get the total amount of damage that has been dealt to the caller.

#### `object GetLastDamager(object oObject = OBJECT_SELF)`
> Get the last object that damaged oObject
> Returns OBJECT_INVALID if oObject is not a valid object.

#### `object GetLastDisarmed()`
> Get the last object that disarmed the trap on the caller.
> Returns OBJECT_INVALID if the caller is not a valid placeable, trigger or
> door.

#### `object GetLastDisturbed(object oObject = OBJECT_SELF)`
> Get the last object that disturbed the inventory of oObject.
> Returns OBJECT_INVALID if oObject is not a valid creature or placeable.

#### `object GetLastLocked(object oObject = OBJECT_SELF)`
> Get the last object that locked oObject.
> Returns OBJECT_INVALID if oObject is not a valid door or placeable.

#### `object GetLastUnlocked(object oObject = OBJECT_SELF)`
> Get the last object that unlocked oObject.
> Returns OBJECT_INVALID if oObject is not a valid door or placeable.

#### `effect EffectSkillIncrease(int nSkill, int nValue)`
> Create a Skill Increase effect.
> - nSkill: SKILL_*
> - nValue
> Returns an effect of type EFFECT_TYPE_INVALIDEFFECT if nSkill is invalid.

#### `int GetInventoryDisturbType(object oObject = OBJECT_SELF)`
> Get the type of disturbance (INVENTORY_DISTURB_*) that caused the oObject's
> OnInventoryDisturbed script to fire.  This will only work for creatures and
> placeables.

#### `object GetInventoryDisturbItem(object oObject = OBJECT_SELF)`
> get the item that caused oObject's OnInventoryDisturbed script to fire.
> Returns OBJECT_INVALID if the oObject is not a valid object.

#### `object GetHenchman(object oMaster = OBJECT_SELF, int nNth = 1)`
> Get the henchman belonging to oMaster.
> Return OBJECT_INVALID if oMaster does not have a henchman.
> -nNth: Which henchman to return.

#### `effect VersusAlignmentEffect(effect eEffect, int nLawChaos = ALIGNMENT_ALL, int nGoodEvil = ALIGNMENT_ALL)`
> Set eEffect to be versus a specific alignment.
> - eEffect
> - nLawChaos: ALIGNMENT_LAWFUL/ALIGNMENT_CHAOTIC/ALIGNMENT_ALL
> - nGoodEvil: ALIGNMENT_GOOD/ALIGNMENT_EVIL/ALIGNMENT_ALL

#### `effect VersusRacialTypeEffect(effect eEffect, int nRacialType)`
> Set eEffect to be versus nRacialType.
> - eEffect
> - nRacialType: RACIAL_TYPE_*

#### `effect VersusTrapEffect(effect eEffect)`
> Set eEffect to be versus traps.

#### `int GetGender(object oCreature)`
> Get the gender of oCreature.

#### `int GetIsTalentValid(talent tTalent)`
> Returns TRUE if tTalent is valid.

#### `void ActionMoveAwayFromLocation(location lMoveAwayFrom, int bRun = FALSE, float fMoveAwayRange = 40.0f)`
> Causes the action subject to move away from lMoveAwayFrom.

#### `object GetAttemptedAttackTarget()`
> Get the target that the caller attempted to attack - this should be used in
> conjunction with GetAttackTarget(). This value is set every time an attack is
> made, and is reset at the end of combat.
> Returns OBJECT_INVALID if the caller is not a valid creature.

#### `int GetTypeFromTalent(talent tTalent)`
> Get the type (TALENT_TYPE_*) of tTalent.

#### `int GetIdFromTalent(talent tTalent)`
> Get the ID of tTalent.  This could be a SPELL_*, FEAT_* or SKILL_*.

#### `object GetAssociate(int nAssociateType, object oMaster = OBJECT_SELF, int nTh = 1)`
> Get the associate of type nAssociateType belonging to oMaster.
> - nAssociateType: ASSOCIATE_TYPE_*
> - nMaster
> - nTh: Which associate of the specified type to return
> Returns OBJECT_INVALID if no such associate exists.

#### `void AddHenchman(object oMaster, object oHenchman = OBJECT_SELF)`
> Add oHenchman as a henchman to oMaster
> If oHenchman is either a DM or a player character, this will have no effect.

#### `void RemoveHenchman(object oMaster, object oHenchman = OBJECT_SELF)`
> Remove oHenchman from the service of oMaster, returning them to their original faction.

#### `void AddJournalQuestEntry(string szPlotID, int nState, object oCreature, int bAllPartyMembers = TRUE, int bAllPlayers = FALSE, int bAllowOverrideHigher = FALSE)`
> Add a journal quest entry to oCreature.
> - szPlotID: the plot identifier used in the toolset's Journal Editor
> - nState: the state of the plot as seen in the toolset's Journal Editor
> - oCreature
> - bAllPartyMembers: If this is TRUE, the entry will show up in the journal of
> everyone in the party
> - bAllPlayers: If this is TRUE, the entry will show up in the journal of
> everyone in the world
> - bAllowOverrideHigher: If this is TRUE, you can set the state to a lower
> number than the one it is currently on

#### `void RemoveJournalQuestEntry(string szPlotID, object oCreature, int bAllPartyMembers = TRUE, int bAllPlayers = FALSE)`
> Remove a journal quest entry from oCreature.
> - szPlotID: the plot identifier used in the toolset's Journal Editor
> - oCreature
> - bAllPartyMembers: If this is TRUE, the entry will be removed from the
> journal of everyone in the party
> - bAllPlayers: If this is TRUE, the entry will be removed from the journal of
> everyone in the world

#### `string GetPCPublicCDKey(object oPlayer, int nSinglePlayerCDKey = FALSE)`
> Get the public part of the CD Key that oPlayer used when logging in.
> - nSinglePlayerCDKey: If set to TRUE, the player's public CD Key will
> be returned when the player is playing in single player mode
> (otherwise returns an empty string in single player mode).

#### `string GetPCIPAddress(object oPlayer)`
> Get the IP address from which oPlayer has connected.

#### `string GetPCPlayerName(object oPlayer)`
> Get the name of oPlayer.

#### `void SetPCLike(object oPlayer, object oTarget)`
> Sets oPlayer and oTarget to like each other.

#### `void SetPCDislike(object oPlayer, object oTarget)`
> Sets oPlayer and oTarget to dislike each other.

#### `void SendMessageToPC(object oPlayer, string szMessage)`
> Send a server message (szMessage) to the oPlayer.

#### `object GetAttemptedSpellTarget()`
> Get the target at which the caller attempted to cast a spell.
> This value is set every time a spell is cast and is reset at the end of
> combat.
> Returns OBJECT_INVALID if the caller is not a valid creature.

#### `object GetLastOpenedBy(object oObject = OBJECT_SELF)`
> Get the last creature that opened oObject.
> Returns OBJECT_INVALID if oObject is not a valid door, placeable or store.

#### `int GetHasSpell(int nSpell, object oCreature = OBJECT_SELF)`
> Determines the number of times that oCreature has nSpell memorised.
> - nSpell: SPELL_*
> - oCreature

#### `void OpenStore(object oStore, object oPC, int nBonusMarkUp = 0, int nBonusMarkDown = 0)`
> Open oStore for oPC.
> - nBonusMarkUp is added to the stores default mark up percentage on items sold (-100 to 100)
> - nBonusMarkDown is added to the stores default mark down percentage on items bought (-100 to 100)

#### `effect EffectTurned()`
> Create a Turned effect.
> Turned effects are supernatural by default.

#### `object GetFirstFactionMember(object oMemberOfFaction, int bPCOnly = TRUE)`
> Get the first member of oMemberOfFaction's faction (start to cycle through
> oMemberOfFaction's faction).
> Returns OBJECT_INVALID if oMemberOfFaction's faction is invalid.

#### `object GetNextFactionMember(object oMemberOfFaction, int bPCOnly = TRUE)`
> Get the next member of oMemberOfFaction's faction (continue to cycle through
> oMemberOfFaction's faction).
> Returns OBJECT_INVALID if oMemberOfFaction's faction is invalid.

#### `void ActionForceMoveToLocation(location lDestination, int bRun = FALSE, float fTimeout = 30.0f)`
> Force the action subject to move to lDestination.

#### `void ActionForceMoveToObject(object oMoveTo, int bRun = FALSE, float fRange = 1.0f, float fTimeout = 30.0f)`
> Force the action subject to move to oMoveTo.

#### `int GetJournalQuestExperience(string szPlotID)`
> Get the experience assigned in the journal editor for szPlotID.

#### `void JumpToObject(object oToJumpTo, int nWalkStraightLineToPoint = 1)`
> Jump to oToJumpTo (the action is added to the top of the action queue).

#### `void SetMapPinEnabled(object oMapPin, int nEnabled)`
> Set whether oMapPin is enabled.
> - oMapPin
> - nEnabled: 0=Off, 1=On

#### `effect EffectHitPointChangeWhenDying(float fHitPointChangePerRound)`
> Create a Hit Point Change When Dying effect.
> - fHitPointChangePerRound: this can be positive or negative, but not zero.
> Returns an effect of type EFFECT_TYPE_INVALIDEFFECT if fHitPointChangePerRound is 0.

#### `void PopUpGUIPanel(object oPC, int nGUIPanel)`
> Spawn a GUI panel for the client that controls oPC.
> Will force show panels disabled with SetGuiPanelDisabled()
> - oPC
> - nGUIPanel: GUI_PANEL_*, except GUI_PANEL_COMPASS / GUI_PANEL_LEVELUP / GUI_PANEL_GOLD_* / GUI_PANEL_EXAMINE_*
> Nothing happens if oPC is not a player character or if an invalid value is used for nGUIPanel.

#### `void ClearPersonalReputation(object oTarget, object oSource = OBJECT_SELF)`
> Clear all personal feelings that oSource has about oTarget.

#### `void SetIsTemporaryFriend(object oTarget, object oSource = OBJECT_SELF, int bDecays = FALSE, float fDurationInSeconds = 180.0f)`
> oSource will temporarily be friends towards oTarget.
> bDecays determines whether the personal reputation value decays over time
> fDurationInSeconds is the length of time that the temporary friendship lasts
> Make oSource into a temporary friend of oTarget using personal reputation.
> - oTarget
> - oSource
> - bDecays: If this is TRUE, the friendship decays over fDurationInSeconds;
> otherwise it is indefinite.
> - fDurationInSeconds: This is only used if bDecays is TRUE, it is how long
> the friendship lasts.
> Note: If bDecays is TRUE, the personal reputation amount decreases in size
> over fDurationInSeconds. Friendship will only be in effect as long as
> (faction reputation + total personal reputation) >= REPUTATION_TYPE_FRIEND.

#### `void SetIsTemporaryEnemy(object oTarget, object oSource = OBJECT_SELF, int bDecays = FALSE, float fDurationInSeconds = 180.0f)`
> Make oSource into a temporary enemy of oTarget using personal reputation.
> - oTarget
> - oSource
> - bDecays: If this is TRUE, the enmity decays over fDurationInSeconds;
> otherwise it is indefinite.
> - fDurationInSeconds: This is only used if bDecays is TRUE, it is how long
> the enmity lasts.
> Note: If bDecays is TRUE, the personal reputation amount decreases in size
> over fDurationInSeconds. Enmity will only be in effect as long as
> (faction reputation + total personal reputation) <= REPUTATION_TYPE_ENEMY.

#### `void SetIsTemporaryNeutral(object oTarget, object oSource = OBJECT_SELF, int bDecays = FALSE, float fDurationInSeconds = 180.0f)`
> Make oSource temporarily neutral to oTarget using personal reputation.
> - oTarget
> - oSource
> - bDecays: If this is TRUE, the neutrality decays over fDurationInSeconds;
> otherwise it is indefinite.
> - fDurationInSeconds: This is only used if bDecays is TRUE, it is how long
> the neutrality lasts.
> Note: If bDecays is TRUE, the personal reputation amount decreases in size
> over fDurationInSeconds. Neutrality will only be in effect as long as
> (faction reputation + total personal reputation) > REPUTATION_TYPE_ENEMY and
> (faction reputation + total personal reputation) < REPUTATION_TYPE_FRIEND.

#### `void GiveXPToCreature(object oCreature, int nXpAmount)`
> Gives nXpAmount to oCreature.

#### `void SetXP(object oCreature, int nXpAmount)`
> Sets oCreature's experience to nXpAmount.

#### `int GetXP(object oCreature)`
> Get oCreature's experience.

#### `string IntToHexString(int nInteger)`
> Convert nInteger to hex, returning the hex value as a string.
> Return value has the format "0x????????" where each ? will be a hex digit
> (8 digits in total).

#### `int GetBaseItemType(object oItem)`
> Get the base item type (BASE_ITEM_*) of oItem.
> Returns BASE_ITEM_INVALID if oItem is an invalid item.

#### `int GetItemHasItemProperty(object oItem, int nProperty)`
> Determines whether oItem has nProperty.
> - oItem
> - nProperty: ITEM_PROPERTY_*
> Returns FALSE if oItem is not a valid item, or if oItem does not have
> nProperty.

#### `void ActionEquipMostDamagingMelee(object oVersus = OBJECT_INVALID, int bOffHand = FALSE)`
> The creature will equip the melee weapon in its possession that can do the
> most damage. If no valid melee weapon is found, it will equip the most
> damaging range weapon. This function should only ever be called in the
> EndOfCombatRound scripts, because otherwise it would have to stop the combat
> round to run simulation.
> - oVersus: You can try to get the most damaging weapon against oVersus
> - bOffHand

#### `void ActionEquipMostDamagingRanged(object oVersus = OBJECT_INVALID)`
> The creature will equip the range weapon in its possession that can do the
> most damage.
> If no valid range weapon can be found, it will equip the most damaging melee
> weapon.
> - oVersus: You can try to get the most damaging weapon against oVersus

#### `int GetItemACValue(object oItem)`
> Get the Armour Class of oItem.
> Return 0 if the oItem is not a valid item, or if oItem has no armour value.

#### `void ActionRest(int bCreatureToEnemyLineOfSightCheck = FALSE)`
> The creature will rest if not in combat and no enemies are nearby.
> - bCreatureToEnemyLineOfSightCheck: TRUE to allow the creature to rest if enemies
> are nearby, but the creature can't see the enemy.
> FALSE the creature will not rest if enemies are
> nearby regardless of whether or not the creature
> can see them, such as if an enemy is close by,
> but is in a different room behind a closed door.

#### `void ExploreAreaForPlayer(object oArea, object oPlayer, int bExplored = TRUE)`
> Expose/Hide the entire map of oArea for oPlayer.
> - oArea: The area that the map will be exposed/hidden for.
> - oPlayer: The player the map will be exposed/hidden for.
> - bExplored: TRUE/FALSE. Whether the map should be completely explored or hidden.

#### `void ActionEquipMostEffectiveArmor()`
> The creature will equip the armour in its possession that has the highest
> armour class.

#### `int GetIsDay()`
> Returns TRUE if it is currently day.

#### `int GetIsNight()`
> Returns TRUE if it is currently night.

#### `int GetIsDawn()`
> Returns TRUE if it is currently dawn.

#### `int GetIsDusk()`
> Returns TRUE if it is currently dusk.

#### `int GetIsEncounterCreature(object oCreature = OBJECT_SELF)`
> Returns TRUE if oCreature was spawned from an encounter.

#### `object GetLastPlayerDying()`
> Use this in an OnPlayerDying module script to get the last player who is dying.

#### `location GetStartingLocation()`
> Get the starting location of the module.

#### `void ChangeToStandardFaction(object oCreatureToChange, int nStandardFaction)`
> Make oCreatureToChange join one of the standard factions.
> This will only work on an NPC **
> - nStandardFaction: STANDARD_FACTION_*

#### `void SoundObjectPlay(object oSound)`
> Play oSound.

#### `void SoundObjectStop(object oSound)`
> Stop playing oSound.

#### `void SoundObjectSetVolume(object oSound, int nVolume)`
> Set the volume of oSound.
> - oSound
> - nVolume: 0-127

#### `void SoundObjectSetPosition(object oSound, vector vPosition)`
> Set the position of oSound.

#### `void SpeakOneLinerConversation(string sDialogResRef = "", object oTokenTarget = OBJECT_TYPE_INVALID)`
> Immediately speak a conversation one-liner.
> - sDialogResRef
> - oTokenTarget: This must be specified if there are creature-specific tokens
> in the string.

#### `int GetGold(object oTarget = OBJECT_SELF)`
> Get the amount of gold possessed by oTarget.

#### `object GetLastRespawnButtonPresser()`
> Use this in an OnRespawnButtonPressed module script to get the object id of
> the player who last pressed the respawn button.

#### `int GetIsDM(object oCreature)`
> Returns TRUE if oCreature is the Dungeon Master.
> Note: This will return FALSE if oCreature is a DM Possessed creature.
> To determine if oCreature is a DM Possessed creature, use GetIsDMPossessed()

#### `void PlayVoiceChat(int nVoiceChatID, object oTarget = OBJECT_SELF)`
> Play a voice chat.
> - nVoiceChatID: VOICE_CHAT_*
> - oTarget

#### `int GetIsWeaponEffective(object oVersus = OBJECT_INVALID, int bOffHand = FALSE)`
> Returns TRUE if the weapon equipped is capable of damaging oVersus.

#### `int GetLastSpellHarmful()`
> Use this in a SpellCast script to determine whether the spell was considered
> harmful.
> Returns TRUE if the last spell cast was harmful.

#### `event EventActivateItem(object oItem, location lTarget, object oTarget = OBJECT_INVALID)`
> Activate oItem.

#### `void MusicBackgroundPlay(object oArea)`
> Play the background music for oArea.

#### `void MusicBackgroundStop(object oArea)`
> Stop the background music for oArea.

#### `void MusicBackgroundSetDelay(object oArea, int nDelay)`
> Set the delay for the background music for oArea.
> - oArea
> - nDelay: delay in milliseconds

#### `void MusicBackgroundChangeDay(object oArea, int nTrack)`
> Change the background day track for oArea to nTrack.
> - oArea
> - nTrack

#### `void MusicBackgroundChangeNight(object oArea, int nTrack)`
> Change the background night track for oArea to nTrack.
> - oArea
> - nTrack

#### `void MusicBattlePlay(object oArea)`
> Play the battle music for oArea.

#### `void MusicBattleStop(object oArea)`
> Stop the battle music for oArea.

#### `void MusicBattleChange(object oArea, int nTrack)`
> Change the battle track for oArea.
> - oArea
> - nTrack

#### `void AmbientSoundPlay(object oArea)`
> Play the ambient sound for oArea.

#### `void AmbientSoundStop(object oArea)`
> Stop the ambient sound for oArea.

#### `void AmbientSoundChangeDay(object oArea, int nTrack)`
> Change the ambient day track for oArea to nTrack.
> - oArea
> - nTrack

#### `void AmbientSoundChangeNight(object oArea, int nTrack)`
> Change the ambient night track for oArea to nTrack.
> - oArea
> - nTrack

#### `object GetLastKiller()`
> Get the object that killed the caller.

#### `object GetSpellCastItem()`
> Use this in a spell script to get the item used to cast the spell.

#### `object GetItemActivated()`
> Use this in an OnItemActivated module script to get the item that was activated.

#### `object GetItemActivator()`
> Use this in an OnItemActivated module script to get the creature that
> activated the item.

#### `location GetItemActivatedTargetLocation()`
> Use this in an OnItemActivated module script to get the location of the item's
> target.

#### `object GetItemActivatedTarget()`
> Use this in an OnItemActivated module script to get the item's target.

#### `int GetIsOpen(object oObject)`
> Returns TRUE if oObject (which is a placeable or a door) is currently open.

#### `void TakeGoldFromCreature(int nAmount, object oCreatureToTakeFrom, int bDestroy = FALSE)`
> Take nAmount of gold from oCreatureToTakeFrom.
> - nAmount
> - oCreatureToTakeFrom: If this is not a valid creature, nothing will happen.
> - bDestroy: If this is TRUE, the caller will not get the gold.  Instead, the
> gold will be destroyed and will vanish from the game.

#### `int IsInConversation(object oObject)`
> Determine whether oObject is in conversation.

#### `effect EffectAbilityDecrease(int nAbility, int nModifyBy)`
> Create an Ability Decrease effect.
> - nAbility: ABILITY_*
> - nModifyBy: This is the amount by which to decrement the ability

#### `effect EffectAttackDecrease(int nPenalty, int nModifierType = ATTACK_BONUS_MISC)`
> Create an Attack Decrease effect.
> - nPenalty
> - nModifierType: ATTACK_BONUS_*

#### `effect EffectDamageDecrease(int nPenalty, int nDamageType = DAMAGE_TYPE_MAGICAL)`
> Create a Damage Decrease effect.
> - nPenalty
> - nDamageType: DAMAGE_TYPE_*

#### `effect EffectDamageImmunityDecrease(int nDamageType, int nPercentImmunity)`
> Create a Damage Immunity Decrease effect.
> - nDamageType: DAMAGE_TYPE_*
> - nPercentImmunity

#### `effect EffectACDecrease(int nValue, int nModifyType = AC_DODGE_BONUS, int nDamageType = AC_VS_DAMAGE_TYPE_ALL)`
> Create an AC Decrease effect.
> - nValue
> - nModifyType: AC_*
> - nDamageType: DAMAGE_TYPE_*
> Default value for nDamageType should only ever be used in this function prototype.

#### `effect EffectMovementSpeedDecrease(int nPercentChange)`
> Create a Movement Speed Decrease effect.
> - nPercentChange - range 0 through 99
> eg.
> 0 = no change in speed
> 50 = 50% slower
> 99 = almost immobile

#### `effect EffectSavingThrowDecrease(int nSave, int nValue, int nSaveType = SAVING_THROW_TYPE_ALL)`
> Create a Saving Throw Decrease effect.
> - nSave: SAVING_THROW_* (not SAVING_THROW_TYPE_*)
> SAVING_THROW_ALL
> SAVING_THROW_FORT
> SAVING_THROW_REFLEX
> SAVING_THROW_WILL
> - nValue: size of the Saving Throw decrease
> - nSaveType: SAVING_THROW_TYPE_* (e.g. SAVING_THROW_TYPE_ACID )

#### `effect EffectSkillDecrease(int nSkill, int nValue)`
> Create a Skill Decrease effect.
> Returns an effect of type EFFECT_TYPE_INVALIDEFFECT if nSkill is invalid.

#### `effect EffectSpellResistanceDecrease(int nValue)`
> Create a Spell Resistance Decrease effect.

#### `int GetPlotFlag(object oTarget = OBJECT_SELF)`
> Determine whether oTarget is a plot object.

#### `void SetPlotFlag(object oTarget, int nPlotFlag)`
> Set oTarget's plot object status.

#### `effect EffectInvisibility(int nInvisibilityType)`
> Create an Invisibility effect.
> - nInvisibilityType: INVISIBILITY_TYPE_*
> Returns an effect of type EFFECT_TYPE_INVALIDEFFECT if nInvisibilityType
> is invalid.

#### `effect EffectConcealment(int nPercentage, int nMissType = MISS_CHANCE_TYPE_NORMAL)`
> Create a Concealment effect.
> - nPercentage: 1-100 inclusive
> - nMissChanceType: MISS_CHANCE_TYPE_*
> Returns an effect of type EFFECT_TYPE_INVALIDEFFECT if nPercentage < 1 or
> nPercentage > 100.

#### `effect EffectDarkness()`
> Create a Darkness effect.

#### `effect EffectDispelMagicAll(int nCasterLevel = USE_CREATURE_LEVEL)`
> Create a Dispel Magic All effect.
> If no parameter is specified, USE_CREATURE_LEVEL will be used. This will
> cause the dispel effect to use the level of the creature that created the
> effect.

#### `effect EffectUltravision()`
> Create an Ultravision effect.

#### `effect EffectNegativeLevel(int nNumLevels, int bHPBonus = FALSE)`
> Create a Negative Level effect.
> - nNumLevels: the number of negative levels to apply.
> Returns an effect of type EFFECT_TYPE_INVALIDEFFECT if nNumLevels > 100.

#### `effect EffectPolymorph(int nPolymorphSelection, int nLocked = FALSE, int nUnpolymorphVFX = VFX_IMP_POLYMORPH, int nSpellAbilityModifier = -1, int nSpellAbilityCasterLevel = 0)`
> Create a Polymorph effect.
> - nLocked: If TRUE the creature cannot cancel the polymorph.
> - nUnpolymorphVFX: If -1 no VFX will play when this polymorph is removed. Else will play the relevant VFX.
> - nSpellAbilityModifier: Set a custom spell ability modifier for the 3 polymorph spells.
> Save DC is 10 + Innate spell level + this ability modifier.
> -1 uses the creators spellcasting/feat using class spellcasting ability modifier.
> - nSpellAbilityCasterLevel: Set a custom caster level for the 3 polymorph spells.
> Default (0) is to use the first class slot class level as previously.

#### `effect EffectSanctuary(int nDifficultyClass)`
> Create a Sanctuary effect.
> - nDifficultyClass: must be a non-zero, positive number
> Returns an effect of type EFFECT_TYPE_INVALIDEFFECT if nDifficultyClass <= 0.

#### `effect EffectTrueSeeing()`
> Create a True Seeing effect.

#### `effect EffectSeeInvisible()`
> Create a See Invisible effect.

#### `effect EffectTimeStop()`
> Create a Time Stop effect.

#### `effect EffectBlindness()`
> Create a Blindness effect.

#### `int GetIsReactionTypeFriendly(object oTarget, object oSource = OBJECT_SELF)`
> Determine whether oSource has a friendly reaction towards oTarget, depending
> on the reputation, PVP setting and (if both oSource and oTarget are PCs),
> oSource's Like/Dislike setting for oTarget.
> Note: If you just want to know how two objects feel about each other in terms
> of faction and personal reputation, use GetIsFriend() instead.
> Returns TRUE if oSource has a friendly reaction towards oTarget

#### `int GetIsReactionTypeNeutral(object oTarget, object oSource = OBJECT_SELF)`
> Determine whether oSource has a neutral reaction towards oTarget, depending
> on the reputation, PVP setting and (if both oSource and oTarget are PCs),
> oSource's Like/Dislike setting for oTarget.
> Note: If you just want to know how two objects feel about each other in terms
> of faction and personal reputation, use GetIsNeutral() instead.
> Returns TRUE if oSource has a neutral reaction towards oTarget

#### `int GetIsReactionTypeHostile(object oTarget, object oSource = OBJECT_SELF)`
> Determine whether oSource has a Hostile reaction towards oTarget, depending
> on the reputation, PVP setting and (if both oSource and oTarget are PCs),
> oSource's Like/Dislike setting for oTarget.
> Note: If you just want to know how two objects feel about each other in terms
> of faction and personal reputation, use GetIsEnemy() instead.
> Returns TRUE if oSource has a hostile reaction towards oTarget

#### `effect EffectSpellLevelAbsorption(int nMaxSpellLevelAbsorbed, int nTotalSpellLevelsAbsorbed = 0, int nSpellSchool = SPELL_SCHOOL_GENERAL)`
> Create a Spell Level Absorption effect.
> - nMaxSpellLevelAbsorbed: maximum spell level that will be absorbed by the
> effect
> - nTotalSpellLevelsAbsorbed: maximum number of spell levels that will be
> absorbed by the effect
> - nSpellSchool: SPELL_SCHOOL_*
> Returns an effect of type EFFECT_TYPE_INVALIDEFFECT if:
> nMaxSpellLevelAbsorbed is not between -1 and 9 inclusive, or nSpellSchool
> is invalid.

#### `effect EffectDispelMagicBest(int nCasterLevel = USE_CREATURE_LEVEL)`
> Create a Dispel Magic Best effect.
> If no parameter is specified, USE_CREATURE_LEVEL will be used. This will
> cause the dispel effect to use the level of the creature that created the
> effect.

#### `void ActivatePortal(object oTarget, string sIPaddress = "", string sPassword = "", string sWaypointTag = "", int bSeemless = FALSE)`
> Try to send oTarget to a new server defined by sIPaddress.
> - oTarget
> - sIPaddress: this can be numerical "192.168.0.84" or alphanumeric
> "www.bioware.com". It can also contain a port "192.168.0.84:5121" or
> "www.bioware.com:5121"; if the port is not specified, it will default to
> 5121.
> - sPassword: login password for the destination server
> - sWaypointTag: if this is set, after portalling the character will be moved
> to this waypoint if it exists
> - bSeamless: if this is set, the client wil not be prompted with the
> information window telling them about the server, and they will not be
> allowed to save a copy of their character if they are using a local vault
> character.

#### `int GetNumStackedItems(object oItem)`
> Get the number of stacked items that oItem comprises.

#### `void SurrenderToEnemies()`
> Use this on an NPC to cause all creatures within a 10-metre radius to stop
> what they are doing and sets the NPC's enemies within this range to be
> neutral towards the NPC for roughly 3 minutes. If this command is run on a PC
> or an object that is not a creature, nothing will happen.

#### `effect EffectMissChance(int nPercentage, int nMissChanceType = MISS_CHANCE_TYPE_NORMAL)`
> Create a Miss Chance effect.
> - nPercentage: 1-100 inclusive
> - nMissChanceType: MISS_CHANCE_TYPE_*
> Returns an effect of type EFFECT_TYPE_INVALIDEFFECT if nPercentage < 1 or
> nPercentage > 100.

#### `int GetTurnResistanceHD(object oUndead = OBJECT_SELF)`
> Get the number of Hitdice worth of Turn Resistance that oUndead may have.
> This will only work on undead creatures.

#### `int GetCreatureSize(object oCreature)`
> Get the size (CREATURE_SIZE_*) of oCreature.

#### `effect EffectDisappearAppear(location lLocation, int nAnimation = 1)`
> Create a Disappear/Appear effect.
> The object will "fly away" for the duration of the effect and will reappear
> at lLocation.
> - nAnimation determines which appear and disappear animations to use. Most creatures
> only have animation 1, although a few have 2 (like beholders)

#### `effect EffectDisappear(int nAnimation = 1)`
> Create a Disappear effect to make the object "fly away" and then destroy
> itself.
> - nAnimation determines which appear and disappear animations to use. Most creatures
> only have animation 1, although a few have 2 (like beholders)

#### `effect EffectAppear(int nAnimation = 1)`
> Create an Appear effect to make the object "fly in".
> - nAnimation determines which appear and disappear animations to use. Most creatures
> only have animation 1, although a few have 2 (like beholders)

#### `void ActionUnlockObject(object oTarget)`
> The action subject will unlock oTarget, which can be a door or a placeable
> object.

#### `void ActionLockObject(object oTarget)`
> The action subject will lock oTarget, which can be a door or a placeable
> object.

#### `effect EffectModifyAttacks(int nAttacks)`
> Create a Modify Attacks effect to add attacks.
> - nAttacks: maximum is 5, even with the effect stacked
> Returns an effect of type EFFECT_TYPE_INVALIDEFFECT if nAttacks > 5.

#### `object GetLastTrapDetected(object oTarget = OBJECT_SELF)`
> Get the last trap detected by oTarget.
> Return value on error: OBJECT_INVALID

#### `effect EffectDamageShield(int nDamageAmount, int nRandomAmount, int nDamageType)`
> Create a Damage Shield effect which does (nDamageAmount + nRandomAmount)
> damage to any melee attacker on a successful attack of damage type nDamageType.
> - nDamageAmount: an integer value
> - nRandomAmount: DAMAGE_BONUS_*
> - nDamageType: DAMAGE_TYPE_*
> NOTE! You *must* use the DAMAGE_BONUS_* constants! Using other values may
> result in odd behaviour.

#### `object GetNearestTrapToObject(object oTarget = OBJECT_SELF, int nTrapDetected = TRUE)`
> Get the trap nearest to oTarget.
> Note : "trap objects" are actually any trigger, placeable or door that is
> trapped in oTarget's area.
> - oTarget
> - nTrapDetected: if this is TRUE, the trap returned has to have been detected
> by oTarget.

#### `string GetDeity(object oCreature)`
> Get the name of oCreature's deity.
> Returns "" if oCreature is invalid (or if the deity name is blank for
> oCreature).

#### `string GetSubRace(object oTarget)`
> Get the name of oCreature's sub race.
> Returns "" if oCreature is invalid (or if sub race is blank for oCreature).

#### `int GetFortitudeSavingThrow(object oTarget)`
> Get oTarget's base fortitude saving throw value (this will only work for
> creatures, doors, and placeables).
> Returns 0 if oTarget is invalid.

#### `int GetWillSavingThrow(object oTarget)`
> Get oTarget's base will saving throw value (this will only work for creatures,
> doors, and placeables).
> Returns 0 if oTarget is invalid.

#### `int GetReflexSavingThrow(object oTarget)`
> Get oTarget's base reflex saving throw value (this will only work for
> creatures, doors, and placeables).
> Returns 0 if oTarget is invalid.

#### `float GetChallengeRating(object oCreature)`
> Get oCreature's challenge rating.
> Returns 0.0 if oCreature is invalid.

#### `int GetAge(object oCreature)`
> Get oCreature's age.
> Returns 0 if oCreature is invalid.

#### `int GetMovementRate(object oCreature)`
> Get oCreature's movement rate.
> Returns 0 if oCreature is invalid.

#### `int GetFamiliarCreatureType(object oCreature)`
> Get oCreature's familiar creature type (FAMILIAR_CREATURE_TYPE_*).
> Returns FAMILIAR_CREATURE_TYPE_NONE if oCreature is invalid or does not
> currently have a familiar.

#### `int GetAnimalCompanionCreatureType(object oCreature)`
> Get oCreature's animal companion creature type
> (ANIMAL_COMPANION_CREATURE_TYPE_*).
> Returns ANIMAL_COMPANION_CREATURE_TYPE_NONE if oCreature is invalid or does
> not currently have an animal companion.

#### `string GetFamiliarName(object oCreature)`
> Get oCreature's familiar's name.
> Returns "" if oCreature is invalid, does not currently
> have a familiar or if the familiar's name is blank.

#### `string GetAnimalCompanionName(object oTarget)`
> Get oCreature's animal companion's name.
> Returns "" if oCreature is invalid, does not currently
> have an animal companion or if the animal companion's name is blank.

#### `void ActionCastFakeSpellAtObject(int nSpell, object oTarget, int nProjectilePathType = PROJECTILE_PATH_TYPE_DEFAULT)`
> The action subject will fake casting a spell at oTarget; the conjure and cast
> animations and visuals will occur, nothing else.
> - nSpell
> - oTarget
> - nProjectilePathType: PROJECTILE_PATH_TYPE_*

#### `void ActionCastFakeSpellAtLocation(int nSpell, location lTarget, int nProjectilePathType = PROJECTILE_PATH_TYPE_DEFAULT)`
> The action subject will fake casting a spell at lLocation; the conjure and
> cast animations and visuals will occur, nothing else.
> - nSpell
> - lTarget
> - nProjectilePathType: PROJECTILE_PATH_TYPE_*

#### `void RemoveSummonedAssociate(object oMaster, object oAssociate = OBJECT_SELF)`
> Removes oAssociate from the service of oMaster, returning them to their
> original faction.

#### `void SetCameraMode(object oPlayer, int nCameraMode)`
> Set the camera mode for oPlayer.
> - oPlayer
> - nCameraMode: CAMERA_MODE_*
> If oPlayer is not player-controlled or nCameraMode is invalid, nothing
> happens.

#### `int GetIsResting(object oCreature = OBJECT_SELF)`
> Returns TRUE if oCreature is resting.

#### `object GetLastPCRested()`
> Get the last PC that has rested in the module.

#### `void SetWeather(object oTarget, int nWeather)`
> Set the weather for oTarget.
> - oTarget: if this is GetModule(), all outdoor areas will be modified by the
> weather constant. If it is an area, oTarget will play the weather only if
> it is an outdoor area.
> - nWeather: WEATHER_*
> -> WEATHER_USER_AREA_SETTINGS will set the area back to random weather.
> -> WEATHER_CLEAR, WEATHER_RAIN, WEATHER_SNOW will make the weather go to
> the appropriate precipitation *without stopping*.

#### `int GetLastRestEventType()`
> Determine the type (REST_EVENTTYPE_REST_*) of the last rest event (as
> returned from the OnPCRested module event).

#### `void StartNewModule(string sModuleName)`
> Shut down the currently loaded module and start a new one (moving all
> currently-connected players to the starting point.

#### `effect EffectSwarm(int nLooping, string sCreatureTemplate1, string sCreatureTemplate2 = "", string sCreatureTemplate3 = "", string sCreatureTemplate4 = "")`
> Create a Swarm effect.
> - nLooping: If this is TRUE, for the duration of the effect when one creature
> created by this effect dies, the next one in the list will be created.  If
> the last creature in the list dies, we loop back to the beginning and
> sCreatureTemplate1 will be created, and so on...
> - sCreatureTemplate1
> - sCreatureTemplate2
> - sCreatureTemplate3
> - sCreatureTemplate4

#### `int GetWeaponRanged(object oItem)`
> Returns TRUE if oItem is a ranged weapon.

#### `void DoSinglePlayerAutoSave()`
> Only if we are in a single player game, AutoSave the game.

#### `int GetGameDifficulty()`
> Get the game difficulty (GAME_DIFFICULTY_*).

#### `void SetTileMainLightColor(location lTileLocation, int nMainLight1Color, int nMainLight2Color)`
> Set the main light color on the tile at lTileLocation.
> - lTileLocation: the vector part of this is the tile grid (x,y) coordinate of
> the tile.
> - nMainLight1Color: TILE_MAIN_LIGHT_COLOR_*
> - nMainLight2Color: TILE_MAIN_LIGHT_COLOR_*

#### `void SetTileSourceLightColor(location lTileLocation, int nSourceLight1Color, int nSourceLight2Color)`
> Set the source light color on the tile at lTileLocation.
> - lTileLocation: the vector part of this is the tile grid (x,y) coordinate of
> the tile.
> - nSourceLight1Color: TILE_SOURCE_LIGHT_COLOR_*
> - nSourceLight2Color: TILE_SOURCE_LIGHT_COLOR_*

#### `void RecomputeStaticLighting(object oArea)`
> All clients in oArea will recompute the static lighting.
> This can be used to update the lighting after changing any tile lights or if
> placeables with lights have been added/deleted.

#### `int GetTileMainLight1Color(location lTile)`
> Get the color (TILE_MAIN_LIGHT_COLOR_*) for the main light 1 of the tile at
> lTile.
> - lTile: the vector part of this is the tile grid (x,y) coordinate of the tile.

#### `int GetTileMainLight2Color(location lTile)`
> Get the color (TILE_MAIN_LIGHT_COLOR_*) for the main light 2 of the tile at
> lTile.
> - lTile: the vector part of this is the tile grid (x,y) coordinate of the
> tile.

#### `int GetTileSourceLight1Color(location lTile)`
> Get the color (TILE_SOURCE_LIGHT_COLOR_*) for the source light 1 of the tile
> at lTile.
> - lTile: the vector part of this is the tile grid (x,y) coordinate of the
> tile.

#### `int GetTileSourceLight2Color(location lTile)`
> Get the color (TILE_SOURCE_LIGHT_COLOR_*) for the source light 2 of the tile
> at lTile.
> - lTile: the vector part of this is the tile grid (x,y) coordinate of the
> tile.

#### `void SetPanelButtonFlash(object oPlayer, int nButton, int nEnableFlash)`
> Make the corresponding panel button on the player's client start or stop
> flashing.
> - oPlayer
> - nButton: PANEL_BUTTON_*
> - nEnableFlash: if this is TRUE nButton will start flashing.  It if is FALSE,
> nButton will stop flashing.

#### `int GetCurrentAction(object oObject = OBJECT_SELF)`
> Get the current action (ACTION_*) that oObject is executing.

#### `void SetStandardFactionReputation(int nStandardFaction, int nNewReputation, object oCreature = OBJECT_SELF)`
> Set how nStandardFaction feels about oCreature.
> - nStandardFaction: STANDARD_FACTION_*
> - nNewReputation: 0-100 (inclusive)
> - oCreature

#### `int GetStandardFactionReputation(int nStandardFaction, object oCreature = OBJECT_SELF)`
> Find out how nStandardFaction feels about oCreature.
> - nStandardFaction: STANDARD_FACTION_*
> - oCreature
> Returns -1 on an error.
> Returns 0-100 based on the standing of oCreature within the faction nStandardFaction.
> 0-10   :  Hostile.
> 11-89  :  Neutral.
> 90-100 :  Friendly.

#### `void FloatingTextStrRefOnCreature(int nStrRefToDisplay, object oCreatureToFloatAbove, int bBroadcastToFaction = TRUE, int bChatWindow = TRUE)`
> Display floaty text above the specified creature.
> The text will also appear in the chat buffer of each player that receives the
> floaty text.
> - nStrRefToDisplay: String ref (therefore text is translated)
> - oCreatureToFloatAbove
> - bBroadcastToFaction: If this is TRUE then only creatures in the same faction
> as oCreatureToFloatAbove
> will see the floaty text, and only if they are within range (30 metres).
> - bChatWindow:  If TRUE, the string reference will be displayed in oCreatureToFloatAbove's chat window

#### `void FloatingTextStringOnCreature(string sStringToDisplay, object oCreatureToFloatAbove, int bBroadcastToFaction = TRUE, int bChatWindow = TRUE)`
> Display floaty text above the specified creature.
> The text will also appear in the chat buffer of each player that receives the
> floaty text.
> - sStringToDisplay: String
> - oCreatureToFloatAbove
> - bBroadcastToFaction: If this is TRUE then only creatures in the same faction
> as oCreatureToFloatAbove
> will see the floaty text, and only if they are within range (30 metres).
> - bChatWindow:  If TRUE, sStringToDisplay will be displayed in oCreatureToFloatAbove's chat window.

#### `int GetTrapDisarmable(object oTrapObject)`
> - oTrapObject: a placeable, door or trigger
> Returns TRUE if oTrapObject is disarmable.

#### `int GetTrapDetectable(object oTrapObject)`
> - oTrapObject: a placeable, door or trigger
> Returns TRUE if oTrapObject is detectable.

#### `int GetTrapDetectedBy(object oTrapObject, object oCreature)`
> - oTrapObject: a placeable, door or trigger
> - oCreature
> Returns TRUE if oCreature has detected oTrapObject

#### `int GetTrapFlagged(object oTrapObject)`
> - oTrapObject: a placeable, door or trigger
> Returns TRUE if oTrapObject has been flagged as visible to all creatures.

#### `int GetTrapBaseType(object oTrapObject)`
> Get the trap base type (TRAP_BASE_TYPE_*) of oTrapObject.
> - oTrapObject: a placeable, door or trigger

#### `int GetTrapOneShot(object oTrapObject)`
> - oTrapObject: a placeable, door or trigger
> Returns TRUE if oTrapObject is one-shot (i.e. it does not reset itself
> after firing.

#### `object GetTrapCreator(object oTrapObject)`
> Get the creator of oTrapObject, the creature that set the trap.
> - oTrapObject: a placeable, door or trigger
> Returns OBJECT_INVALID if oTrapObject was created in the toolset.

#### `string GetTrapKeyTag(object oTrapObject)`
> Get the tag of the key that will disarm oTrapObject.
> - oTrapObject: a placeable, door or trigger

#### `int GetTrapDisarmDC(object oTrapObject)`
> Get the DC for disarming oTrapObject.
> - oTrapObject: a placeable, door or trigger

#### `int GetTrapDetectDC(object oTrapObject)`
> Get the DC for detecting oTrapObject.
> - oTrapObject: a placeable, door or trigger

#### `int GetLockKeyRequired(object oObject)`
> Returns TRUE if a specific key is required to open the lock on oObject.

#### `string GetLockKeyTag(object oObject)`
> Get the tag of the key that will open the lock on oObject.

#### `int GetLockLockable(object oObject)`
> Returns TRUE if the lock on oObject is lockable.

#### `int GetLockUnlockDC(object oObject)`
> Get the DC for unlocking oObject.

#### `int GetLockLockDC(object oObject)`
> Get the DC for locking oObject.

#### `object GetPCLevellingUp()`
> Get the last PC that levelled up.

#### `int GetHasFeatEffect(int nFeat, object oObject = OBJECT_SELF)`
> - nFeat: FEAT_*
> - oObject
> Returns TRUE if oObject has effects on it originating from nFeat.

#### `void SetPlaceableIllumination(object oPlaceable = OBJECT_SELF, int bIlluminate = TRUE)`
> Set the status of the illumination for oPlaceable.
> - oPlaceable
> - bIlluminate: if this is TRUE, oPlaceable's illumination will be turned on.
> If this is FALSE, oPlaceable's illumination will be turned off.
> Note: You must call RecomputeStaticLighting() after calling this function in
> order for the changes to occur visually for the players.
> SetPlaceableIllumination() buffers the illumination changes, which are then
> sent out to the players once RecomputeStaticLighting() is called.  As such,
> it is best to call SetPlaceableIllumination() for all the placeables you wish
> to set the illumination on, and then call RecomputeStaticLighting() once after
> all the placeable illumination has been set.
> If oPlaceable is not a placeable object, or oPlaceable is a placeable that
> doesn't have a light, nothing will happen.

#### `int GetPlaceableIllumination(object oPlaceable = OBJECT_SELF)`
> Returns TRUE if the illumination for oPlaceable is on

#### `int GetIsPlaceableObjectActionPossible(object oPlaceable, int nPlaceableAction)`
> - oPlaceable
> - nPlaceableAction: PLACEABLE_ACTION_*
> Returns TRUE if nPlacebleAction is valid for oPlaceable.

#### `void DoPlaceableObjectAction(object oPlaceable, int nPlaceableAction)`
> The caller performs nPlaceableAction on oPlaceable.
> - oPlaceable
> - nPlaceableAction: PLACEABLE_ACTION_*

#### `object GetFirstPC()`
> Get the first PC in the player list.
> This resets the position in the player list for GetNextPC().

#### `object GetNextPC()`
> Get the next PC in the player list.
> This picks up where the last GetFirstPC() or GetNextPC() left off.

#### `int SetTrapDetectedBy(object oTrap, object oDetector, int bDetected = TRUE)`
> Set whether or not the creature oDetector has detected the trapped object oTrap.
> - oTrap: A trapped trigger, placeable or door object.
> - oDetector: This is the creature that the detected status of the trap is being adjusted for.
> - bDetected: A Boolean that sets whether the trapped object has been detected or not.

#### `int GetIsTrapped(object oObject)`
> Note: Only placeables, doors and triggers can be trapped.
> Returns TRUE if oObject is trapped.

#### `effect EffectTurnResistanceDecrease(int nHitDice)`
> Create a Turn Resistance Decrease effect.
> - nHitDice: a positive number representing the number of hit dice for the
> decrease

#### `effect EffectTurnResistanceIncrease(int nHitDice)`
> Create a Turn Resistance Increase effect.
> - nHitDice: a positive number representing the number of hit dice for the
> increase

#### `void PopUpDeathGUIPanel(object oPC, int bRespawnButtonEnabled = TRUE, int bWaitForHelpButtonEnabled = TRUE, int nHelpStringReference = 0, string sHelpString = "")`
> Spawn in the Death GUI.
> The default (as defined by BioWare) can be spawned in by PopUpGUIPanel, but
> if you want to turn off the "Respawn" or "Wait for Help" buttons, this is the
> function to use.
> - oPC
> - bRespawnButtonEnabled: if this is TRUE, the "Respawn" button will be enabled
> on the Death GUI.
> - bWaitForHelpButtonEnabled: if this is TRUE, the "Wait For Help" button will
> be enabled on the Death GUI (Note: This button will not appear in single player games).
> - nHelpStringReference
> - sHelpString

#### `void SetTrapDisabled(object oTrap)`
> Disable oTrap.
> - oTrap: a placeable, door or trigger.

#### `object GetLastHostileActor(object oVictim = OBJECT_SELF)`
> Get the last object that was sent as a GetLastAttacker(), GetLastDamager(),
> GetLastSpellCaster() (for a hostile spell), or GetLastDisturbed() (when a
> creature is pickpocketed).
> Note: Return values may only ever be:
> 1) A Creature
> 2) Plot Characters will never have this value set
> 3) Area of Effect Objects will return the AOE creator if they are registered
> as this value, otherwise they will return INVALID_OBJECT_ID
> 4) Traps will not return the creature that set the trap.
> 5) This value will never be overwritten by another non-creature object.
> 6) This value will never be a dead/destroyed creature

#### `void ExportAllCharacters()`
> Force all the characters of the players who are currently in the game to
> be exported to their respective directories i.e. LocalVault/ServerVault/ etc.

#### `int MusicBackgroundGetDayTrack(object oArea)`
> Get the Day Track for oArea.

#### `int MusicBackgroundGetNightTrack(object oArea)`
> Get the Night Track for oArea.

#### `void WriteTimestampedLogEntry(string sLogEntry)`
> Write sLogEntry as a timestamped entry into the log file

#### `string GetModuleName()`
> Get the module's name in the language of the server that's running it.
> If there is no entry for the language of the server, it will return an
> empty string

#### `object GetFactionLeader(object oMemberOfFaction)`
> Get the player leader of the faction of which oMemberOfFaction is a member.
> Returns OBJECT_INVALID if oMemberOfFaction is not a valid creature,
> or oMemberOfFaction is a member of a NPC faction.

#### `void SendMessageToAllDMs(string szMessage)`
> Sends szMessage to all the Dungeon Masters currently on the server.

#### `void EndGame(string sEndMovie)`
> End the currently running game, play sEndMovie then return all players to the
> game's main menu.

#### `void BootPC(object oPlayer, string sReason = "")`
> Remove oPlayer from the server.
> You can optionally specify a reason to override the text shown to the player.

#### `void ActionCounterSpell(object oCounterSpellTarget)`
> Counterspell oCounterSpellTarget.

#### `void AmbientSoundSetDayVolume(object oArea, int nVolume)`
> Set the ambient day volume for oArea to nVolume.
> - oArea
> - nVolume: 0 - 100

#### `void AmbientSoundSetNightVolume(object oArea, int nVolume)`
> Set the ambient night volume for oArea to nVolume.
> - oArea
> - nVolume: 0 - 100

#### `int MusicBackgroundGetBattleTrack(object oArea)`
> Get the Battle Track for oArea.

#### `int GetHasInventory(object oObject)`
> Determine whether oObject has an inventory.
> Returns TRUE for creatures and stores, and checks to see if an item or placeable object is a container.
> Returns FALSE for all other object types.

#### `float GetStrRefSoundDuration(int nStrRef)`
> Get the duration (in seconds) of the sound attached to nStrRef
> Returns 0.0f if no duration is stored or if no sound is attached

#### `void AddToParty(object oPC, object oPartyLeader)`
> Add oPC to oPartyLeader's party.  This will only work on two PCs.
> - oPC: player to add to a party
> - oPartyLeader: player already in the party

#### `void RemoveFromParty(object oPC)`
> Remove oPC from their current party. This will only work on a PC.
> - oPC: removes this player from whatever party they're currently in.

#### `int GetStealthMode(object oCreature)`
> Returns the stealth mode of the specified creature.
> - oCreature
> Returns a constant STEALTH_MODE_*

#### `int GetDetectMode(object oCreature)`
> Returns the detection mode of the specified creature.
> - oCreature
> Returns a constant DETECT_MODE_*

#### `int GetDefensiveCastingMode(object oCreature)`
> Returns the defensive casting mode of the specified creature.
> - oCreature
> Returns a constant DEFENSIVE_CASTING_MODE_*

#### `int GetAppearanceType(object oCreature)`
> returns the appearance type of the specified creature.
> returns a constant APPEARANCE_TYPE_* for valid creatures
> returns APPEARANCE_TYPE_INVALID for non creatures/invalid creatures

#### `void SpawnScriptDebugger()`
> SpawnScriptDebugger() will attempt to communicate with the a running script debugger
> instance. You need to run it yourself, and enable it in Options/Config beforehand.
> A sample debug server is included with the game installation in utils/.
> Will only work in singleplayer, NOT on dedicated servers.
> In order to compile the script for debugging go to Tools->Options->Script Editor
> and check the box labeled "Generate Debug Information When Compiling Scripts"
> After you have checked the above box, recompile the script that you want to debug.
> If the script file isn't compiled for debugging, this command will do nothing.
> Remove any SpawnScriptDebugger() calls once you have finished
> debugging the script.

#### `int GetModuleItemAcquiredStackSize()`
> in an onItemAcquired script, returns the size of the stack of the item
> that was just acquired.
> returns the stack size of the item acquired

#### `void DecrementRemainingFeatUses(object oCreature, int nFeat)`
> Decrement the remaining uses per day for this creature by one.
> - oCreature: creature to modify
> - nFeat: constant FEAT_*

#### `void DecrementRemainingSpellUses(object oCreature, int nSpell)`
> Decrement the remaining uses per day for this creature by one.
> - oCreature: creature to modify
> - nSpell: constant SPELL_*

#### `string GetResRef(object oObject)`
> returns the template used to create this object (if appropriate)
> returns an empty string when no template found

#### `effect EffectPetrify()`
> returns an effect that will petrify the target
> currently applies EffectParalyze and the stoneskin visual effect.

#### `object CopyItem(object oItem, object oTargetInventory = OBJECT_INVALID, int bCopyVars = FALSE)`
> duplicates the item and returns a new object
> oItem - item to copy
> oTargetInventory - create item in this object's inventory. If this parameter
> is not valid, the item will be created in oItem's location
> bCopyVars - copy the local variables from the old item to the new one
> returns the new item
> returns OBJECT_INVALID for non-items.
> can only copy empty item containers. will return OBJECT_INVALID if oItem contains
> other items.
> if it is possible to merge this item with any others in the target location,
> then it will do so and return the merged object.

#### `effect EffectCutsceneParalyze()`
> returns an effect that is guaranteed to paralyze a creature.
> this effect is identical to EffectParalyze except that it cannot be resisted.

#### `int GetDroppableFlag(object oItem)`
> returns TRUE if the item CAN be dropped
> Droppable items will appear on a creature's remains when the creature is killed.

#### `int GetUseableFlag(object oObject = OBJECT_SELF)`
> returns TRUE if the object is usable

#### `int GetStolenFlag(object oStolen)`
> returns TRUE if the item is stolen

#### `void SetCampaignFloat(string sCampaignName, string sVarName, float flFloat, object oPlayer = OBJECT_INVALID)`
> This stores a float out to the specified campaign database
> The database name:
> - is case insensitive and it must be the same for both set and get functions.
> - can only contain alphanumeric characters, no spaces.
> The var name must be unique across the entire database, regardless of the variable type.
> If you want a variable to pertain to a specific player in the game, provide a player object.

#### `void SetCampaignInt(string sCampaignName, string sVarName, int nInt, object oPlayer = OBJECT_INVALID)`
> This stores an int out to the specified campaign database
> The database name:
> - is case insensitive and it must be the same for both set and get functions.
> - can only contain alphanumeric characters, no spaces.
> The var name must be unique across the entire database, regardless of the variable type.
> If you want a variable to pertain to a specific player in the game, provide a player object.

#### `void SetCampaignVector(string sCampaignName, string sVarName, vector vVector, object oPlayer = OBJECT_INVALID)`
> This stores a vector out to the specified campaign database
> The database name:
> - is case insensitive and it must be the same for both set and get functions.
> - can only contain alphanumeric characters, no spaces.
> The var name must be unique across the entire database, regardless of the variable type.
> If you want a variable to pertain to a specific player in the game, provide a player object.

#### `void SetCampaignLocation(string sCampaignName, string sVarName, location locLocation, object oPlayer = OBJECT_INVALID)`
> This stores a location out to the specified campaign database
> The database name:
> - is case insensitive and it must be the same for both set and get functions.
> - can only contain alphanumeric characters, no spaces.
> The var name must be unique across the entire database, regardless of the variable type.
> If you want a variable to pertain to a specific player in the game, provide a player object.

#### `void SetCampaignString(string sCampaignName, string sVarName, string sString, object oPlayer = OBJECT_INVALID)`
> This stores a string out to the specified campaign database
> The database name:
> - is case insensitive and it must be the same for both set and get functions.
> - can only contain alphanumeric characters, no spaces.
> The var name must be unique across the entire database, regardless of the variable type.
> If you want a variable to pertain to a specific player in the game, provide a player object.

#### `void DestroyCampaignDatabase(string sCampaignName)`
> This will delete the entire campaign database if it exists.

#### `float GetCampaignFloat(string sCampaignName, string sVarName, object oPlayer = OBJECT_INVALID)`
> This will read a float from the  specified campaign database
> The database name:
> - is case insensitive and it must be the same for both set and get functions.
> - can only contain alphanumeric characters, no spaces.
> The var name must be unique across the entire database, regardless of the variable type.
> If you want a variable to pertain to a specific player in the game, provide a player object.

#### `int GetCampaignInt(string sCampaignName, string sVarName, object oPlayer = OBJECT_INVALID)`
> This will read an int from the  specified campaign database
> The database name:
> - is case insensitive and it must be the same for both set and get functions.
> - can only contain alphanumeric characters, no spaces.
> The var name must be unique across the entire database, regardless of the variable type.
> If you want a variable to pertain to a specific player in the game, provide a player object.

#### `vector GetCampaignVector(string sCampaignName, string sVarName, object oPlayer = OBJECT_INVALID)`
> This will read a vector from the  specified campaign database
> The database name:
> - is case insensitive and it must be the same for both set and get functions.
> - can only contain alphanumeric characters, no spaces.
> The var name must be unique across the entire database, regardless of the variable type.
> If you want a variable to pertain to a specific player in the game, provide a player object.

#### `location GetCampaignLocation(string sCampaignName, string sVarName, object oPlayer = OBJECT_INVALID)`
> This will read a location from the  specified campaign database
> The database name:
> - is case insensitive and it must be the same for both set and get functions.
> - can only contain alphanumeric characters, no spaces.
> The var name must be unique across the entire database, regardless of the variable type.
> If you want a variable to pertain to a specific player in the game, provide a player object.

#### `string GetCampaignString(string sCampaignName, string sVarName, object oPlayer = OBJECT_INVALID)`
> This will read a string from the  specified campaign database
> The database name:
> - is case insensitive and it must be the same for both set and get functions.
> - can only contain alphanumeric characters, no spaces.
> The var name must be unique across the entire database, regardless of the variable type.
> If you want a variable to pertain to a specific player in the game, provide a player object.

#### `object CopyObject(object oSource, location locLocation, object oOwner = OBJECT_INVALID, string sNewTag = "", int bCopyLocalState = FALSE)`
> Duplicates the object specified by oSource.
> NOTE: this command can be used for copying Creatures, Items, Placeables, Waypoints, Stores, Doors, Triggers, Encounters.
> If an owner is specified and the object is an item, it will be put into their inventory
> Otherwise, it will be created at the location.
> If a new tag is specified, it will be assigned to the new object.
> If bCopyLocalState is TRUE, local vars, effects, action queue, and transition info (triggers, doors) are copied over.

#### `void DeleteCampaignVariable(string sCampaignName, string sVarName, object oPlayer = OBJECT_INVALID)`
> This will remove ANY campaign variable. Regardless of type.

#### `int StoreCampaignObject(string sCampaignName, string sVarName, object oObject, object oPlayer = OBJECT_INVALID, int bSaveObjectState = FALSE)`
> Stores an object with the given id.
> NOTE: this command can be used for storing Creatures, Items, Placeables, Waypoints, Stores, Doors, Triggers, Encounters.
> Returns 0 if it failled, 1 if it worked.
> If bSaveObjectState is TRUE, local vars, effects, action queue, and transition info (triggers, doors) are saved out
> (except for Combined Area Format, which always has object state saved out).

#### `object RetrieveCampaignObject(string sCampaignName, string sVarName, location locLocation, object oOwner = OBJECT_INVALID, object oPlayer = OBJECT_INVALID, int bLoadObjectState = FALSE)`
> Use RetrieveCampaign with the given id to restore it.
> If you specify an owner, the object will try to be created in their repository
> If the owner can't handle the item (or if it's a non-item) it will be created at the given location.
> If bLoadObjectState is TRUE, local vars, effects, action queue, and transition info (triggers, doors) are read in.

#### `effect EffectCutsceneDominated()`
> Returns an effect that is guaranteed to dominate a creature
> Like EffectDominated but cannot be resisted

#### `int GetItemStackSize(object oItem)`
> Returns stack size of an item
> - oItem: item to query

#### `void SetItemStackSize(object oItem, int nSize)`
> Sets stack size of an item.
> - oItem: item to change
> - nSize: new size of stack.  Will be restricted to be between 1 and the
> maximum stack size for the item type.  If a value less than 1 is passed it
> will set the stack to 1.  If a value greater than the max is passed
> then it will set the stack to the maximum size

#### `int GetItemCharges(object oItem)`
> Returns charges left on an item
> - oItem: item to query

#### `void SetItemCharges(object oItem, int nCharges)`
> Sets charges left on an item.
> - oItem: item to change
> - nCharges: number of charges.  If value below 0 is passed, # charges will
> be set to 0.  If value greater than maximum is passed, # charges will
> be set to maximum.  If the # charges drops to 0 the item
> will be destroyed.

#### `void AddItemProperty(int nDurationType, itemproperty ipProperty, object oItem, float fDuration = 0.0f)`
> adds an item property to the specified item
> Only temporary and permanent duration types are allowed.

#### `void RemoveItemProperty(object oItem, itemproperty ipProperty)`
> removes an item property from the specified item

#### `int GetIsItemPropertyValid(itemproperty ipProperty)`
> if the item property is valid this will return true

#### `itemproperty GetFirstItemProperty(object oItem)`
> Gets the first item property on an item

#### `itemproperty GetNextItemProperty(object oItem)`
> Will keep retrieving the next and the next item property on an Item,
> will return an invalid item property when the list is empty.

#### `int GetItemPropertyType(itemproperty ip)`
> will return the item property type (ie. holy avenger)

#### `int GetItemPropertyDurationType(itemproperty ip)`
> will return the duration type of the item property

#### `itemproperty ItemPropertyAbilityBonus(int nAbility, int nBonus)`
> Returns Item property ability bonus.  You need to specify an
> ability constant(IP_CONST_ABILITY_*) and the bonus.  The bonus should
> be a positive integer between 1 and 12.

#### `itemproperty ItemPropertyACBonus(int nBonus)`
> Returns Item property AC bonus.  You need to specify the bonus.
> The bonus should be a positive integer between 1 and 20. The modifier
> type depends on the item it is being applied to.

#### `itemproperty ItemPropertyACBonusVsAlign(int nAlignGroup, int nACBonus)`
> Returns Item property AC bonus vs. alignment group.  An example of
> an alignment group is Chaotic, or Good.  You need to specify the
> alignment group constant(IP_CONST_ALIGNMENTGROUP_*) and the AC bonus.
> The AC bonus should be an integer between 1 and 20.  The modifier
> type depends on the item it is being applied to.

#### `itemproperty ItemPropertyACBonusVsDmgType(int nDamageType, int nACBonus)`
> Returns Item property AC bonus vs. Damage type (ie. piercing).  You
> need to specify the damage type constant(IP_CONST_DAMAGETYPE_*) and the
> AC bonus.  The AC bonus should be an integer between 1 and 20.  The
> modifier type depends on the item it is being applied to.
> NOTE: Only the first 3 damage types may be used here, the 3 basic
> physical types.

#### `itemproperty ItemPropertyACBonusVsRace(int nRace, int nACBonus)`
> Returns Item property AC bonus vs. Racial group.  You need to specify
> the racial group constant(IP_CONST_RACIALTYPE_*) and the AC bonus.  The AC
> bonus should be an integer between 1 and 20.  The modifier type depends
> on the item it is being applied to.

#### `itemproperty ItemPropertyACBonusVsSAlign(int nAlign, int nACBonus)`
> Returns Item property AC bonus vs. Specific alignment.  You need to
> specify the specific alignment constant(IP_CONST_ALIGNMENT_*) and the AC
> bonus.  The AC bonus should be an integer between 1 and 20.  The
> modifier type depends on the item it is being applied to.

#### `itemproperty ItemPropertyEnhancementBonus(int nEnhancementBonus)`
> Returns Item property Enhancement bonus.  You need to specify the
> enhancement bonus.  The Enhancement bonus should be an integer between
> 1 and 20.

#### `itemproperty ItemPropertyEnhancementBonusVsAlign(int nAlignGroup, int nBonus)`
> Returns Item property Enhancement bonus vs. an Alignment group.  You
> need to specify the alignment group constant(IP_CONST_ALIGNMENTGROUP_*)
> and the enhancement bonus.  The Enhancement bonus should be an integer
> between 1 and 20.

#### `itemproperty ItemPropertyEnhancementBonusVsRace(int nRace, int nBonus)`
> Returns Item property Enhancement bonus vs. Racial group.  You need
> to specify the racial group constant(IP_CONST_RACIALTYPE_*) and the
> enhancement bonus.  The enhancement bonus should be an integer between
> 1 and 20.

#### `itemproperty ItemPropertyEnhancementBonusVsSAlign(int nAlign, int nBonus)`
> Returns Item property Enhancement bonus vs. a specific alignment.  You
> need to specify the alignment constant(IP_CONST_ALIGNMENT_*) and the
> enhancement bonus.  The enhancement bonus should be an integer between
> 1 and 20.

#### `itemproperty ItemPropertyEnhancementPenalty(int nPenalty)`
> Returns Item property Enhancment penalty.  You need to specify the
> enhancement penalty.  The enhancement penalty should be a POSITIVE
> integer between 1 and 5 (ie. 1 = -1).

#### `itemproperty ItemPropertyWeightReduction(int nReduction)`
> Returns Item property weight reduction.  You need to specify the weight
> reduction constant(IP_CONST_REDUCEDWEIGHT_*).

#### `itemproperty ItemPropertyBonusFeat(int nFeat)`
> Returns Item property Bonus Feat.  You need to specify the the feat
> constant(IP_CONST_FEAT_*).

#### `itemproperty ItemPropertyBonusLevelSpell(int nClass, int nSpellLevel)`
> Returns Item property Bonus level spell (Bonus spell of level).  You must
> specify the class constant(IP_CONST_CLASS_*) of the bonus spell(MUST BE a
> spell casting class) and the level of the bonus spell.  The level of the
> bonus spell should be an integer between 0 and 9.

#### `itemproperty ItemPropertyCastSpell(int nSpell, int nNumUses)`
> Returns Item property Cast spell.  You must specify the spell constant
> (IP_CONST_CASTSPELL_*) and the number of uses constant(IP_CONST_CASTSPELL_NUMUSES_*).
> NOTE: The number after the name of the spell in the constant is the level
> at which the spell will be cast.  Sometimes there are multiple copies
> of the same spell but they each are cast at a different level.  The higher
> the level, the more cost will be added to the item.
> NOTE: The list of spells that can be applied to an item will depend on the
> item type.  For instance there are spells that can be applied to a wand
> that cannot be applied to a potion.  Below is a list of the types and the
> spells that are allowed to be placed on them.  If you try to put a cast
> spell effect on an item that is not allowed to have that effect it will
> not work.
> NOTE: Even if spells have multiple versions of different levels they are only
> listed below once.
> WANDS:
> Acid_Splash
> Activate_Item
> Aid
> Amplify
> Animate_Dead
> AuraOfGlory
> BalagarnsIronHorn
> Bane
> Banishment
> Barkskin
> Bestow_Curse
> Bigbys_Clenched_Fist
> Bigbys_Crushing_Hand
> Bigbys_Forceful_Hand
> Bigbys_Grasping_Hand
> Bigbys_Interposing_Hand
> Bless
> Bless_Weapon
> Blindness/Deafness
> Blood_Frenzy
> Bombardment
> Bulls_Strength
> Burning_Hands
> Call_Lightning
> Camoflage
> Cats_Grace
> Charm_Monster
> Charm_Person
> Charm_Person_or_Animal
> Clairaudience/Clairvoyance
> Clarity
> Color_Spray
> Confusion
> Continual_Flame
> Cure_Critical_Wounds
> Cure_Light_Wounds
> Cure_Minor_Wounds
> Cure_Moderate_Wounds
> Cure_Serious_Wounds
> Darkness
> Darkvision
> Daze
> Death_Ward
> Dirge
> Dismissal
> Dispel_Magic
> Displacement
> Divine_Favor
> Divine_Might
> Divine_Power
> Divine_Shield
> Dominate_Animal
> Dominate_Person
> Doom
> Dragon_Breath_Acid
> Dragon_Breath_Cold
> Dragon_Breath_Fear
> Dragon_Breath_Fire
> Dragon_Breath_Gas
> Dragon_Breath_Lightning
> Dragon_Breath_Paralyze
> Dragon_Breath_Sleep
> Dragon_Breath_Slow
> Dragon_Breath_Weaken
> Drown
> Eagle_Spledor
> Earthquake
> Electric_Jolt
> Elemental_Shield
> Endurance
> Endure_Elements
> Enervation
> Entangle
> Entropic_Shield
> Etherealness
> Expeditious_Retreat
> Fear
> Find_Traps
> Fireball
> Firebrand
> Flame_Arrow
> Flame_Lash
> Flame_Strike
> Flare
> Foxs_Cunning
> Freedom_of_Movement
> Ghostly_Visage
> Ghoul_Touch
> Grease
> Greater_Magic_Fang
> Greater_Magic_Weapon
> Grenade_Acid
> Grenade_Caltrops
> Grenade_Chicken
> Grenade_Choking
> Grenade_Fire
> Grenade_Holy
> Grenade_Tangle
> Grenade_Thunderstone
> Gust_of_wind
> Hammer_of_the_Gods
> Haste
> Hold_Animal
> Hold_Monster
> Hold_Person
> Ice_Storm
> Identify
> Improved_Invisibility
> Inferno
> Inflict_Critical_Wounds
> Inflict_Light_Wounds
> Inflict_Minor_Wounds
> Inflict_Moderate_Wounds
> Inflict_Serious_Wounds
> Invisibility
> Invisibility_Purge
> Invisibility_Sphere
> Isaacs_Greater_Missile_Storm
> Isaacs_Lesser_Missile_Storm
> Knock
> Lesser_Dispel
> Lesser_Restoration
> Lesser_Spell_Breach
> Light
> Lightning_Bolt
> Mage_Armor
> Magic_Circle_against_Alignment
> Magic_Fang
> Magic_Missile
> Manipulate_Portal_Stone
> Mass_Camoflage
> Melfs_Acid_Arrow
> Meteor_Swarm
> Mind_Blank
> Mind_Fog
> Negative_Energy_Burst
> Negative_Energy_Protection
> Negative_Energy_Ray
> Neutralize_Poison
> One_With_The_Land
> Owls_Insight
> Owls_Wisdom
> Phantasmal_Killer
> Planar_Ally
> Poison
> Polymorph_Self
> Prayer
> Protection_from_Alignment
> Protection_From_Elements
> Quillfire
> Ray_of_Enfeeblement
> Ray_of_Frost
> Remove_Blindness/Deafness
> Remove_Curse
> Remove_Disease
> Remove_Fear
> Remove_Paralysis
> Resist_Elements
> Resistance
> Restoration
> Sanctuary
> Scare
> Searing_Light
> See_Invisibility
> Shadow_Conjuration
> Shield
> Shield_of_Faith
> Silence
> Sleep
> Slow
> Sound_Burst
> Spike_Growth
> Stinking_Cloud
> Stoneskin
> Summon_Creature_I
> Summon_Creature_I
> Summon_Creature_II
> Summon_Creature_III
> Summon_Creature_IV
> Sunburst
> Tashas_Hideous_Laughter
> True_Strike
> Undeaths_Eternal_Foe
> Unique_Power
> Unique_Power_Self_Only
> Vampiric_Touch
> Virtue
> Wall_of_Fire
> Web
> Wounding_Whispers
> POTIONS:
> Activate_Item
> Aid
> Amplify
> AuraOfGlory
> Bane
> Barkskin
> Barkskin
> Barkskin
> Bless
> Bless_Weapon
> Bless_Weapon
> Blood_Frenzy
> Bulls_Strength
> Bulls_Strength
> Bulls_Strength
> Camoflage
> Cats_Grace
> Cats_Grace
> Cats_Grace
> Clairaudience/Clairvoyance
> Clairaudience/Clairvoyance
> Clairaudience/Clairvoyance
> Clarity
> Continual_Flame
> Cure_Critical_Wounds
> Cure_Critical_Wounds
> Cure_Critical_Wounds
> Cure_Light_Wounds
> Cure_Light_Wounds
> Cure_Minor_Wounds
> Cure_Moderate_Wounds
> Cure_Moderate_Wounds
> Cure_Moderate_Wounds
> Cure_Serious_Wounds
> Cure_Serious_Wounds
> Cure_Serious_Wounds
> Darkness
> Darkvision
> Darkvision
> Death_Ward
> Dispel_Magic
> Dispel_Magic
> Displacement
> Divine_Favor
> Divine_Might
> Divine_Power
> Divine_Shield
> Dragon_Breath_Acid
> Dragon_Breath_Cold
> Dragon_Breath_Fear
> Dragon_Breath_Fire
> Dragon_Breath_Gas
> Dragon_Breath_Lightning
> Dragon_Breath_Paralyze
> Dragon_Breath_Sleep
> Dragon_Breath_Slow
> Dragon_Breath_Weaken
> Eagle_Spledor
> Eagle_Spledor
> Eagle_Spledor
> Elemental_Shield
> Elemental_Shield
> Endurance
> Endurance
> Endurance
> Endure_Elements
> Entropic_Shield
> Ethereal_Visage
> Ethereal_Visage
> Etherealness
> Expeditious_Retreat
> Find_Traps
> Foxs_Cunning
> Foxs_Cunning
> Foxs_Cunning
> Freedom_of_Movement
> Ghostly_Visage
> Ghostly_Visage
> Ghostly_Visage
> Globe_of_Invulnerability
> Greater_Bulls_Strength
> Greater_Cats_Grace
> Greater_Dispelling
> Greater_Dispelling
> Greater_Eagles_Splendor
> Greater_Endurance
> Greater_Foxs_Cunning
> Greater_Magic_Weapon
> Greater_Owls_Wisdom
> Greater_Restoration
> Greater_Spell_Mantle
> Greater_Stoneskin
> Grenade_Acid
> Grenade_Caltrops
> Grenade_Chicken
> Grenade_Choking
> Grenade_Fire
> Grenade_Holy
> Grenade_Tangle
> Grenade_Thunderstone
> Haste
> Haste
> Heal
> Hold_Animal
> Hold_Monster
> Hold_Person
> Identify
> Invisibility
> Lesser_Dispel
> Lesser_Dispel
> Lesser_Mind_Blank
> Lesser_Restoration
> Lesser_Spell_Mantle
> Light
> Light
> Mage_Armor
> Manipulate_Portal_Stone
> Mass_Camoflage
> Mind_Blank
> Minor_Globe_of_Invulnerability
> Minor_Globe_of_Invulnerability
> Mordenkainens_Disjunction
> Negative_Energy_Protection
> Negative_Energy_Protection
> Negative_Energy_Protection
> Neutralize_Poison
> One_With_The_Land
> Owls_Insight
> Owls_Wisdom
> Owls_Wisdom
> Owls_Wisdom
> Polymorph_Self
> Prayer
> Premonition
> Protection_From_Elements
> Protection_From_Elements
> Protection_from_Spells
> Protection_from_Spells
> Raise_Dead
> Remove_Blindness/Deafness
> Remove_Curse
> Remove_Disease
> Remove_Fear
> Remove_Paralysis
> Resist_Elements
> Resist_Elements
> Resistance
> Resistance
> Restoration
> Resurrection
> Rogues_Cunning
> See_Invisibility
> Shadow_Shield
> Shapechange
> Shield
> Shield_of_Faith
> Special_Alcohol_Beer
> Special_Alcohol_Spirits
> Special_Alcohol_Wine
> Special_Herb_Belladonna
> Special_Herb_Garlic
> Spell_Mantle
> Spell_Resistance
> Spell_Resistance
> Stoneskin
> Tensers_Transformation
> True_Seeing
> True_Strike
> Unique_Power
> Unique_Power_Self_Only
> Virtue
> GENERAL USE (ie. everything else):
> Just about every spell is useable by all the general use items so instead we
> will only list the ones that are not allowed:
> Special_Alcohol_Beer
> Special_Alcohol_Spirits
> Special_Alcohol_Wine

#### `itemproperty ItemPropertyDamageBonus(int nDamageType, int nDamage)`
> Returns Item property damage bonus.  You must specify the damage type constant
> (IP_CONST_DAMAGETYPE_*) and the amount of damage constant(IP_CONST_DAMAGEBONUS_*).
> NOTE: not all the damage types will work, use only the following: Acid, Bludgeoning,
> Cold, Electrical, Fire, Piercing, Slashing, Sonic.

#### `itemproperty ItemPropertyDamageBonusVsAlign(int nAlignGroup, int nDamageType, int nDamage)`
> Returns Item property damage bonus vs. Alignment groups.  You must specify the
> alignment group constant(IP_CONST_ALIGNMENTGROUP_*) and the damage type constant
> (IP_CONST_DAMAGETYPE_*) and the amount of damage constant(IP_CONST_DAMAGEBONUS_*).
> NOTE: not all the damage types will work, use only the following: Acid, Bludgeoning,
> Cold, Electrical, Fire, Piercing, Slashing, Sonic.

#### `itemproperty ItemPropertyDamageBonusVsRace(int nRace, int nDamageType, int nDamage)`
> Returns Item property damage bonus vs. specific race.  You must specify the
> racial group constant(IP_CONST_RACIALTYPE_*) and the damage type constant
> (IP_CONST_DAMAGETYPE_*) and the amount of damage constant(IP_CONST_DAMAGEBONUS_*).
> NOTE: not all the damage types will work, use only the following: Acid, Bludgeoning,
> Cold, Electrical, Fire, Piercing, Slashing, Sonic.

#### `itemproperty ItemPropertyDamageBonusVsSAlign(int nAlign, int nDamageType, int nDamage)`
> Returns Item property damage bonus vs. specific alignment.  You must specify the
> specific alignment constant(IP_CONST_ALIGNMENT_*) and the damage type constant
> (IP_CONST_DAMAGETYPE_*) and the amount of damage constant(IP_CONST_DAMAGEBONUS_*).
> NOTE: not all the damage types will work, use only the following: Acid, Bludgeoning,
> Cold, Electrical, Fire, Piercing, Slashing, Sonic.

#### `itemproperty ItemPropertyDamageImmunity(int nDamageType, int nImmuneBonus)`
> Returns Item property damage immunity.  You must specify the damage type constant
> (IP_CONST_DAMAGETYPE_*) that you want to be immune to and the immune bonus percentage
> constant(IP_CONST_DAMAGEIMMUNITY_*).
> NOTE: not all the damage types will work, use only the following: Acid, Bludgeoning,
> Cold, Electrical, Fire, Piercing, Slashing, Sonic.

#### `itemproperty ItemPropertyDamagePenalty(int nPenalty)`
> Returns Item property damage penalty.  You must specify the damage penalty.
> The damage penalty should be a POSITIVE integer between 1 and 5 (ie. 1 = -1).

#### `itemproperty ItemPropertyDamageReduction(int nEnhancement, int nHPSoak)`
> Returns Item property damage reduction.  You must specify the enhancment level
> (IP_CONST_DAMAGEREDUCTION_*) that is required to get past the damage reduction
> and the amount of HP of damage constant(IP_CONST_DAMAGESOAK_*) will be soaked
> up if your weapon is not of high enough enhancement.

#### `itemproperty ItemPropertyDamageResistance(int nDamageType, int nHPResist)`
> Returns Item property damage resistance.  You must specify the damage type
> constant(IP_CONST_DAMAGETYPE_*) and the amount of HP of damage constant
> (IP_CONST_DAMAGERESIST_*) that will be resisted against each round.

#### `itemproperty ItemPropertyDamageVulnerability(int nDamageType, int nVulnerability)`
> Returns Item property damage vulnerability.  You must specify the damage type
> constant(IP_CONST_DAMAGETYPE_*) that you want the user to be extra vulnerable to
> and the percentage vulnerability constant(IP_CONST_DAMAGEVULNERABILITY_*).

#### `itemproperty ItemPropertyDarkvision()`
> Return Item property Darkvision.

#### `itemproperty ItemPropertyDecreaseAbility(int nAbility, int nModifier)`
> Return Item property decrease ability score.  You must specify the ability
> constant(IP_CONST_ABILITY_*) and the modifier constant.  The modifier must be
> a POSITIVE integer between 1 and 10 (ie. 1 = -1).

#### `itemproperty ItemPropertyDecreaseAC(int nModifierType, int nPenalty)`
> Returns Item property decrease Armor Class.  You must specify the armor
> modifier type constant(IP_CONST_ACMODIFIERTYPE_*) and the armor class penalty.
> The penalty must be a POSITIVE integer between 1 and 5 (ie. 1 = -1).

#### `itemproperty ItemPropertyDecreaseSkill(int nSkill, int nPenalty)`
> Returns Item property decrease skill.  You must specify the constant for the
> skill to be decreased(SKILL_*) and the amount of the penalty.  The penalty
> must be a POSITIVE integer between 1 and 10 (ie. 1 = -1).

#### `itemproperty ItemPropertyContainerReducedWeight(int nContainerType)`
> Returns Item property container reduced weight.  This is used for special
> containers that reduce the weight of the objects inside them.  You must
> specify the container weight reduction type constant(IP_CONST_CONTAINERWEIGHTRED_*).

#### `itemproperty ItemPropertyExtraMeleeDamageType(int nDamageType)`
> Returns Item property extra melee damage type.  You must specify the extra
> melee base damage type that you want applied.  It is a constant(IP_CONST_DAMAGETYPE_*).
> NOTE: only the first 3 base types (piercing, slashing, & bludgeoning are applicable
> here.
> NOTE: It is also only applicable to melee weapons.

#### `itemproperty ItemPropertyExtraRangeDamageType(int nDamageType)`
> Returns Item property extra ranged damage type.  You must specify the extra
> melee base damage type that you want applied.  It is a constant(IP_CONST_DAMAGETYPE_*).
> NOTE: only the first 3 base types (piercing, slashing, & bludgeoning are applicable
> here.
> NOTE: It is also only applicable to ranged weapons.

#### `itemproperty ItemPropertyHaste()`
> Returns Item property haste.

#### `itemproperty ItemPropertyHolyAvenger()`
> Returns Item property Holy Avenger.

#### `itemproperty ItemPropertyImmunityMisc(int nImmunityType)`
> Returns Item property immunity to miscellaneous effects.  You must specify the
> effect to which the user is immune, it is a constant(IP_CONST_IMMUNITYMISC_*).

#### `itemproperty ItemPropertyImprovedEvasion()`
> Returns Item property improved evasion.

#### `itemproperty ItemPropertyBonusSpellResistance(int nBonus)`
> Returns Item property bonus spell resistance.  You must specify the bonus spell
> resistance constant(IP_CONST_SPELLRESISTANCEBONUS_*).

#### `itemproperty ItemPropertyBonusSavingThrowVsX(int nBonusType, int nBonus)`
> Returns Item property saving throw bonus vs. a specific effect or damage type.
> You must specify the save type constant(IP_CONST_SAVEVS_*) that the bonus is
> applied to and the bonus that is be applied.  The bonus must be an integer
> between 1 and 20.

#### `itemproperty ItemPropertyBonusSavingThrow(int nBaseSaveType, int nBonus)`
> Returns Item property saving throw bonus to the base type (ie. will, reflex,
> fortitude).  You must specify the base type constant(IP_CONST_SAVEBASETYPE_*)
> to which the user gets the bonus and the bonus that he/she will get.  The
> bonus must be an integer between 1 and 20.

#### `itemproperty ItemPropertyKeen()`
> Returns Item property keen.  This means a critical threat range of 19-20 on a
> weapon will be increased to 17-20 etc.

#### `itemproperty ItemPropertyLight(int nBrightness, int nColor)`
> Returns Item property light.  You must specify the intesity constant of the
> light(IP_CONST_LIGHTBRIGHTNESS_*) and the color constant of the light
> (IP_CONST_LIGHTCOLOR_*).

#### `itemproperty ItemPropertyMaxRangeStrengthMod(int nModifier)`
> Returns Item property Max range strength modification (ie. mighty).  You must
> specify the maximum modifier for strength that is allowed on a ranged weapon.
> The modifier must be a positive integer between 1 and 20.

#### `itemproperty ItemPropertyNoDamage()`
> Returns Item property no damage.  This means the weapon will do no damage in
> combat.

#### `itemproperty ItemPropertyOnHitProps(int nProperty, int nSaveDC, int nSpecial = 0)`
> Returns Item property on hit -> do effect property.  You must specify the on
> hit property constant(IP_CONST_ONHIT_*) and the save DC constant(IP_CONST_ONHIT_SAVEDC_*).
> Some of the item properties require a special parameter as well.  If the
> property does not require one you may leave out the last one.  The list of
> the ones with 3 parameters and what they are are as follows:
> ABILITYDRAIN      :nSpecial is the ability it is to drain.
> constant(IP_CONST_ABILITY_*)
> BLINDNESS         :nSpecial is the duration/percentage of effecting victim.
> constant(IP_CONST_ONHIT_DURATION_*)
> CONFUSION         :nSpecial is the duration/percentage of effecting victim.
> constant(IP_CONST_ONHIT_DURATION_*)
> DAZE              :nSpecial is the duration/percentage of effecting victim.
> constant(IP_CONST_ONHIT_DURATION_*)
> DEAFNESS          :nSpecial is the duration/percentage of effecting victim.
> constant(IP_CONST_ONHIT_DURATION_*)
> DISEASE           :nSpecial is the type of desease that will effect the victim.
> constant(DISEASE_*)
> DOOM              :nSpecial is the duration/percentage of effecting victim.
> constant(IP_CONST_ONHIT_DURATION_*)
> FEAR              :nSpecial is the duration/percentage of effecting victim.
> constant(IP_CONST_ONHIT_DURATION_*)
> HOLD              :nSpecial is the duration/percentage of effecting victim.
> constant(IP_CONST_ONHIT_DURATION_*)
> ITEMPOISON        :nSpecial is the type of poison that will effect the victim.
> constant(IP_CONST_POISON_*)
> SILENCE           :nSpecial is the duration/percentage of effecting victim.
> constant(IP_CONST_ONHIT_DURATION_*)
> SLAYRACE          :nSpecial is the race that will be slain.
> constant(IP_CONST_RACIALTYPE_*)
> SLAYALIGNMENTGROUP:nSpecial is the alignment group that will be slain(ie. chaotic).
> constant(IP_CONST_ALIGNMENTGROUP_*)
> SLAYALIGNMENT     :nSpecial is the specific alignment that will be slain.
> constant(IP_CONST_ALIGNMENT_*)
> SLEEP             :nSpecial is the duration/percentage of effecting victim.
> constant(IP_CONST_ONHIT_DURATION_*)
> SLOW              :nSpecial is the duration/percentage of effecting victim.
> constant(IP_CONST_ONHIT_DURATION_*)
> STUN              :nSpecial is the duration/percentage of effecting victim.
> constant(IP_CONST_ONHIT_DURATION_*)

#### `itemproperty ItemPropertyReducedSavingThrowVsX(int nBaseSaveType, int nPenalty)`
> Returns Item property reduced saving throw vs. an effect or damage type.  You must
> specify the constant to which the penalty applies(IP_CONST_SAVEVS_*) and the
> penalty to be applied.  The penalty must be a POSITIVE integer between 1 and 20
> (ie. 1 = -1).

#### `itemproperty ItemPropertyReducedSavingThrow(int nBonusType, int nPenalty)`
> Returns Item property reduced saving to base type.  You must specify the base
> type to which the penalty applies (ie. will, reflex, or fortitude) and the penalty
> to be applied.  The constant for the base type starts with (IP_CONST_SAVEBASETYPE_*).
> The penalty must be a POSITIVE integer between 1 and 20 (ie. 1 = -1).

#### `itemproperty ItemPropertyRegeneration(int nRegenAmount)`
> Returns Item property regeneration.  You must specify the regeneration amount.
> The amount must be an integer between 1 and 20.

#### `itemproperty ItemPropertySkillBonus(int nSkill, int nBonus)`
> Returns Item property skill bonus.  You must specify the skill to which the user
> will get a bonus(SKILL_*) and the amount of the bonus.  The bonus amount must
> be an integer between 1 and 50.

#### `itemproperty ItemPropertySpellImmunitySpecific(int nSpell)`
> Returns Item property spell immunity vs. specific spell.  You must specify the
> spell to which the user will be immune(IP_CONST_IMMUNITYSPELL_*).

#### `itemproperty ItemPropertySpellImmunitySchool(int nSchool)`
> Returns Item property spell immunity vs. spell school.  You must specify the
> school to which the user will be immune(IP_CONST_SPELLSCHOOL_*).

#### `itemproperty ItemPropertyThievesTools(int nModifier)`
> Returns Item property Thieves tools.  You must specify the modifier you wish
> the tools to have.  The modifier must be an integer between 1 and 12.

#### `itemproperty ItemPropertyAttackBonus(int nBonus)`
> Returns Item property Attack bonus.  You must specify an attack bonus.  The bonus
> must be an integer between 1 and 20.

#### `itemproperty ItemPropertyAttackBonusVsAlign(int nAlignGroup, int nBonus)`
> Returns Item property Attack bonus vs. alignment group.  You must specify the
> alignment group constant(IP_CONST_ALIGNMENTGROUP_*) and the attack bonus.  The
> bonus must be an integer between 1 and 20.

#### `itemproperty ItemPropertyAttackBonusVsRace(int nRace, int nBonus)`
> Returns Item property attack bonus vs. racial group.  You must specify the
> racial group constant(IP_CONST_RACIALTYPE_*) and the attack bonus.  The bonus
> must be an integer between 1 and 20.

#### `itemproperty ItemPropertyAttackBonusVsSAlign(int nAlignment, int nBonus)`
> Returns Item property attack bonus vs. a specific alignment.  You must specify
> the alignment you want the bonus to work against(IP_CONST_ALIGNMENT_*) and the
> attack bonus.  The bonus must be an integer between 1 and 20.

#### `itemproperty ItemPropertyAttackPenalty(int nPenalty)`
> Returns Item property attack penalty.  You must specify the attack penalty.
> The penalty must be a POSITIVE integer between 1 and 5 (ie. 1 = -1).

#### `itemproperty ItemPropertyUnlimitedAmmo(int nAmmoDamage = IP_CONST_UNLIMITEDAMMO_BASIC)`
> Returns Item property unlimited ammo.  If you leave the parameter field blank
> it will be just a normal bolt, arrow, or bullet.  However you may specify that
> you want the ammunition to do special damage (ie. +1d6 Fire, or +1 enhancement
> bonus).  For this parmeter you use the constants beginning with:
> (IP_CONST_UNLIMITEDAMMO_*).

#### `itemproperty ItemPropertyLimitUseByAlign(int nAlignGroup)`
> Returns Item property limit use by alignment group.  You must specify the
> alignment group(s) that you want to be able to use this item(IP_CONST_ALIGNMENTGROUP_*).

#### `itemproperty ItemPropertyLimitUseByClass(int nClass)`
> Returns Item property limit use by class.  You must specify the class(es) who
> are able to use this item(IP_CONST_CLASS_*).

#### `itemproperty ItemPropertyLimitUseByRace(int nRace)`
> Returns Item property limit use by race.  You must specify the race(s) who are
> allowed to use this item(IP_CONST_RACIALTYPE_*).

#### `itemproperty ItemPropertyLimitUseBySAlign(int nAlignment)`
> Returns Item property limit use by specific alignment.  You must specify the
> alignment(s) of those allowed to use the item(IP_CONST_ALIGNMENT_*).

#### `itemproperty BadBadReplaceMeThisDoesNothing()`
> replace this function it does nothing.

#### `itemproperty ItemPropertyVampiricRegeneration(int nRegenAmount)`
> Returns Item property vampiric regeneration.  You must specify the amount of
> regeneration.  The regen amount must be an integer between 1 and 20.

#### `itemproperty ItemPropertyTrap(int nTrapLevel, int nTrapType)`
> Returns Item property Trap.  You must specify the trap level constant
> (IP_CONST_TRAPSTRENGTH_*) and the trap type constant(IP_CONST_TRAPTYPE_*).

#### `itemproperty ItemPropertyTrueSeeing()`
> Returns Item property true seeing.

#### `itemproperty ItemPropertyOnMonsterHitProperties(int nProperty, int nSpecial = 0)`
> Returns Item property Monster on hit apply effect property.  You must specify
> the property that you want applied on hit.  There are some properties that
> require an additional special parameter to be specified.  The others that
> don't require any additional parameter you may just put in the one.  The
> special cases are as follows:
> ABILITYDRAIN:nSpecial is the ability to drain.
> constant(IP_CONST_ABILITY_*)
> DISEASE     :nSpecial is the disease that you want applied.
> constant(DISEASE_*)
> LEVELDRAIN  :nSpecial is the number of levels that you want drained.
> integer between 1 and 5.
> POISON      :nSpecial is the type of poison that will effect the victim.
> constant(IP_CONST_POISON_*)
> WOUNDING    :nSpecial is the amount of wounding.
> integer between 1 and 5.
> NOTE: Any that do not appear in the above list do not require the second
> parameter.
> NOTE: These can only be applied to monster NATURAL weapons (ie. bite, claw,
> gore, and slam).  IT WILL NOT WORK ON NORMAL WEAPONS.

#### `itemproperty ItemPropertyTurnResistance(int nModifier)`
> Returns Item property turn resistance.  You must specify the resistance bonus.
> The bonus must be an integer between 1 and 50.

#### `itemproperty ItemPropertyMassiveCritical(int nDamage)`
> Returns Item property Massive Critical.  You must specify the extra damage
> constant(IP_CONST_DAMAGEBONUS_*) of the criticals.

#### `itemproperty ItemPropertyFreeAction()`
> Returns Item property free action.

#### `itemproperty ItemPropertyMonsterDamage(int nDamage)`
> Returns Item property monster damage.  You must specify the amount of damage
> the monster's attack will do(IP_CONST_MONSTERDAMAGE_*).
> NOTE: These can only be applied to monster NATURAL weapons (ie. bite, claw,
> gore, and slam).  IT WILL NOT WORK ON NORMAL WEAPONS.

#### `itemproperty ItemPropertyImmunityToSpellLevel(int nLevel)`
> Returns Item property immunity to spell level.  You must specify the level of
> which that and below the user will be immune.  The level must be an integer
> between 1 and 9.  By putting in a 3 it will mean the user is immune to all
> 3rd level and lower spells.

#### `itemproperty ItemPropertySpecialWalk(int nWalkType = 0)`
> Returns Item property special walk.  If no parameters are specified it will
> automatically use the zombie walk.  This will apply the special walk animation
> to the user.

#### `itemproperty ItemPropertyHealersKit(int nModifier)`
> Returns Item property healers kit.  You must specify the level of the kit.
> The modifier must be an integer between 1 and 12.

#### `itemproperty ItemPropertyWeightIncrease(int nWeight)`
> Returns Item property weight increase.  You must specify the weight increase
> constant(IP_CONST_WEIGHTINCREASE_*).

#### `int GetIsSkillSuccessful(object oTarget, int nSkill, int nDifficulty)`
> Returns true if 1d20 roll + skill rank is greater than or equal to difficulty
> - oTarget: the creature using the skill
> - nSkill: the skill being used
> - nDifficulty: Difficulty class of skill

#### `effect EffectSpellFailure(int nPercent = 100, int nSpellSchool = SPELL_SCHOOL_GENERAL, int nSpellFailureType = SPELL_FAILURE_TYPE_ALL)`
> Creates an effect that inhibits spells
> - nPercent - percentage of failure
> - nSpellSchool - the school of spells affected. Only applies to SPELL_FAILURE_TYPE_ALL.
> - nSpellFailureType - Use SPELL_FAILURE_TYPE_* constants for different spell failure types

#### `void SpeakStringByStrRef(int nStrRef, int nTalkVolume = TALKVOLUME_TALK)`
> Causes the object to instantly speak a translated string.
> (not an action, not blocked when uncommandable)
> - nStrRef: Reference of the string in the talk table
> - nTalkVolume: TALKVOLUME_*

#### `void SetCutsceneMode(object oCreature, int nInCutscene = TRUE, int nLeftClickingEnabled = FALSE)`
> Sets the given creature into cutscene mode.  This prevents the player from
> using the GUI and camera controls.
> - oCreature: creature in a cutscene
> - nInCutscene: TRUE to move them into cutscene, FALSE to remove cutscene mode
> - nLeftClickingEnabled: TRUE to allow the user to interact with the game world using the left mouse button only.
> FALSE to stop the user from interacting with the game world.
> Note: SetCutsceneMode(oPlayer, TRUE) will also make the player 'plot' (unkillable).
> SetCutsceneMode(oPlayer, FALSE) will restore the player's plot flag to what it
> was when SetCutsceneMode(oPlayer, TRUE) was called.

#### `object GetLastPCToCancelCutscene()`
> Gets the last player character to cancel from a cutscene.

#### `float GetDialogSoundLength(int nStrRef)`
> Gets the length of the specified wavefile, in seconds
> Only works for sounds used for dialog.

#### `void FadeFromBlack(object oCreature, float fSpeed = FADE_SPEED_MEDIUM)`
> Fades the screen for the given creature/player from black to regular screen
> - oCreature: creature controlled by player that should fade from black

#### `void FadeToBlack(object oCreature, float fSpeed = FADE_SPEED_MEDIUM)`
> Fades the screen for the given creature/player from regular screen to black
> - oCreature: creature controlled by player that should fade to black

#### `void StopFade(object oCreature)`
> Removes any fading or black screen.
> - oCreature: creature controlled by player that should be cleared

#### `void BlackScreen(object oCreature)`
> Sets the screen to black.  Can be used in preparation for a fade-in (FadeFromBlack)
> Can be cleared by either doing a FadeFromBlack, or by calling StopFade.
> - oCreature: creature controlled by player that should see black screen

#### `int GetBaseAttackBonus(object oCreature)`
> Returns the base attach bonus for the given creature.

#### `void SetImmortal(object oCreature, int bImmortal)`
> Set a creature's immortality flag.
> -oCreature: creature affected
> -bImmortal: TRUE = creature is immortal and cannot be killed (but still takes damage)
> FALSE = creature is not immortal and is damaged normally.
> This scripting command only works on Creature objects.

#### `void OpenInventory(object oCreature, object oPlayer)`
> Open's this creature's inventory panel for this player
> - oCreature: creature to view
> - oPlayer: the owner of this creature will see the panel pop up
> DM's can view any creature's inventory
> Players can view their own inventory, or that of their henchman, familiar or animal companion

#### `void StoreCameraFacing()`
> Stores the current camera mode and position so that it can be restored (using
> RestoreCameraFacing())

#### `void RestoreCameraFacing()`
> Restores the camera mode and position to what they were last time StoreCameraFacing
> was called.  RestoreCameraFacing can only be called once, and must correspond to a
> previous call to StoreCameraFacing.

#### `int LevelUpHenchman(object oCreature, int nClass = CLASS_TYPE_INVALID, int bReadyAllSpells = FALSE, int nPackage = PACKAGE_INVALID)`
> Levels up a creature using default settings.
> If successfull it returns the level the creature now is, or 0 if it fails.
> If you want to give them a different level (ie: Give a Fighter a level of Wizard)
> you can specify that in the nClass.
> However, if you specify a class to which the creature no package specified,
> they will use the default package for that class for their levelup choices.
> (ie: no Barbarian Savage/Wizard Divination combinations)
> If you turn on bReadyAllSpells, all memorized spells will be ready to cast without resting.
> if nPackage is PACKAGE_INVALID then it will use the starting package assigned to that class or just the class package

#### `void SetDroppableFlag(object oItem, int bDroppable)`
> Sets the droppable flag on an item
> - oItem: the item to change
> - bDroppable: TRUE or FALSE, whether the item should be droppable
> Droppable items will appear on a creature's remains when the creature is killed.

#### `int GetWeight(object oTarget = OBJECT_SELF)`
> Gets the weight of an item, or the total carried weight of a creature in tenths
> of pounds (as per the baseitems.2da).
> - oTarget: the item or creature for which the weight is needed

#### `object GetModuleItemAcquiredBy()`
> Gets the object that acquired the module item.  May be a creature, item, or placeable

#### `int GetImmortal(object oTarget = OBJECT_SELF)`
> Get the immortal flag on a creature

#### `void DoWhirlwindAttack(int bDisplayFeedback = TRUE, int bImproved = FALSE)`
> Does a single attack on every hostile creature within 10ft. of the attacker
> and determines damage accordingly.  If the attacker has a ranged weapon
> equipped, this will have no effect.
> NOTE ** This is meant to be called inside the spell script for whirlwind
> attack, it is not meant to be used to queue up a new whirlwind attack.  To do
> that you need to call ActionUseFeat(FEAT_WHIRLWIND_ATTACK, oEnemy)
> - int bDisplayFeedback: TRUE or FALSE, whether or not feedback should be
> displayed
> - int bImproved: If TRUE, the improved version of whirlwind is used

#### `string Get2DAString(string s2DA, string sColumn, int nRow)`
> Gets a value from a 2DA file on the server and returns it as a string
> avoid using this function in loops
> - s2DA: the name of the 2da file, 16 chars max
> - sColumn: the name of the column in the 2da
> - nRow: the row in the 2da
> returns an empty string if file, row, or column not found

#### `effect EffectEthereal()`
> Returns an effect of type EFFECT_TYPE_ETHEREAL which works just like EffectSanctuary
> except that the observers get no saving throw

#### `int GetAILevel(object oTarget = OBJECT_SELF)`
> Gets the current AI Level that the creature is running at.
> Returns one of the following:
> AI_LEVEL_INVALID, AI_LEVEL_VERY_LOW, AI_LEVEL_LOW, AI_LEVEL_NORMAL, AI_LEVEL_HIGH, AI_LEVEL_VERY_HIGH

#### `void SetAILevel(object oTarget, int nAILevel)`
> Sets the current AI Level of the creature to the value specified. Does not work on Players.
> The game by default will choose an appropriate AI level for
> creatures based on the circumstances that the creature is in.
> Explicitly setting an AI level will over ride the game AI settings.
> The new setting will last until SetAILevel is called again with the argument AI_LEVEL_DEFAULT.
> AI_LEVEL_DEFAULT  - Default setting. The game will take over seting the appropriate AI level when required.
> AI_LEVEL_VERY_LOW - Very Low priority, very stupid, but low CPU usage for AI. Typically used when no players are in the area.
> AI_LEVEL_LOW      - Low priority, mildly stupid, but slightly more CPU usage for AI. Typically used when not in combat, but a player is in the area.
> AI_LEVEL_NORMAL   - Normal priority, average AI, but more CPU usage required for AI. Typically used when creature is in combat.
> AI_LEVEL_HIGH     - High priority, smartest AI, but extremely high CPU usage required for AI. Avoid using this. It is most likely only ever needed for cutscenes.

#### `int GetIsPossessedFamiliar(object oCreature)`
> This will return TRUE if the creature running the script is a familiar currently
> possessed by his master.
> returns FALSE if not or if the creature object is invalid

#### `void UnpossessFamiliar(object oCreature)`
> This will cause a Player Creature to unpossess his/her familiar.  It will work if run
> on the player creature or the possessed familiar.  It does not work in conjunction with
> any DM possession.

#### `int GetIsAreaInterior(object oArea = OBJECT_INVALID)`
> This will return TRUE if the area is flagged as either interior or underground.

#### `void SendMessageToPCByStrRef(object oPlayer, int nStrRef)`
> Send a server message (szMessage) to the oPlayer.

#### `void IncrementRemainingFeatUses(object oCreature, int nFeat)`
> Increment the remaining uses per day for this creature by one.
> Total number of feats per day can not exceed the maximum.
> - oCreature: creature to modify
> - nFeat: constant FEAT_*

#### `void ExportSingleCharacter(object oPlayer)`
> Force the character of the player specified to be exported to its respective directory
> i.e. LocalVault/ServerVault/ etc.

#### `void PlaySoundByStrRef(int nStrRef, int nRunAsAction = TRUE)`
> This will play a sound that is associated with a stringRef, it will be a mono sound from the location of the object running the command.
> if nRunAsAction is off then the sound is forced to play intantly.

#### `void SetSubRace(object oCreature, string sSubRace)`
> Set the name of oCreature's sub race to sSubRace.

#### `void SetDeity(object oCreature, string sDeity)`
> Set the name of oCreature's Deity to sDeity.

#### `int GetIsDMPossessed(object oCreature)`
> Returns TRUE if the creature oCreature is currently possessed by a DM character.
> Returns FALSE otherwise.
> Note: GetIsDMPossessed() will return FALSE if oCreature is the DM character.
> To determine if oCreature is a DM character use GetIsDM()

#### `int GetWeather(object oArea)`
> Gets the current weather conditions for the area oArea.
> Returns: WEATHER_CLEAR, WEATHER_RAIN, WEATHER_SNOW, WEATHER_INVALID
> Note: If called on an Interior area, this will always return WEATHER_CLEAR.

#### `int GetIsAreaNatural(object oArea)`
> Returns AREA_NATURAL if the area oArea is natural, AREA_ARTIFICIAL otherwise.
> Returns AREA_INVALID, on an error.

#### `int GetIsAreaAboveGround(object oArea)`
> Returns AREA_ABOVEGROUND if the area oArea is above ground, AREA_UNDERGROUND otherwise.
> Returns AREA_INVALID, on an error.

#### `object GetPCItemLastEquipped()`
> Use this to get the item last equipped by a player character in OnPlayerEquipItem..

#### `object GetPCItemLastEquippedBy()`
> Use this to get the player character who last equipped an item in OnPlayerEquipItem..

#### `object GetPCItemLastUnequipped()`
> Use this to get the item last unequipped by a player character in OnPlayerEquipItem..

#### `object GetPCItemLastUnequippedBy()`
> Use this to get the player character who last unequipped an item in OnPlayerUnEquipItem..

#### `object CopyItemAndModify(object oItem, int nType, int nIndex, int nNewValue, int bCopyVars = FALSE)`
> Creates a new copy of an item, while making a single change to the appearance of the item.
> Helmet models and simple items ignore iIndex.
> iType                            iIndex                              iNewValue
> ITEM_APPR_TYPE_SIMPLE_MODEL      [Ignored]                           Model #
> ITEM_APPR_TYPE_WEAPON_COLOR      ITEM_APPR_WEAPON_COLOR_*            1-4
> ITEM_APPR_TYPE_WEAPON_MODEL      ITEM_APPR_WEAPON_MODEL_*            Model #
> ITEM_APPR_TYPE_ARMOR_MODEL       ITEM_APPR_ARMOR_MODEL_*             Model #
> ITEM_APPR_TYPE_ARMOR_COLOR       ITEM_APPR_ARMOR_COLOR_* [0]         0-175 [1]
> [0] Alternatively, where ITEM_APPR_TYPE_ARMOR_COLOR is specified, if per-part coloring is
> desired, the following equation can be used for nIndex to achieve that:
> ITEM_APPR_ARMOR_NUM_COLORS + (ITEM_APPR_ARMOR_MODEL_ * ITEM_APPR_ARMOR_NUM_COLORS) + ITEM_APPR_ARMOR_COLOR_
> For example, to change the CLOTH1 channel of the torso, nIndex would be:
> 6 + (7 * 6) + 2 = 50
> [1] When specifying per-part coloring, the value 255 is allowed and corresponds with the logical
> function 'clear colour override', which clears the per-part override for that part.

#### `int GetItemAppearance(object oItem, int nType, int nIndex)`
> Queries the current value of the appearance settings on an item. The parameters are
> identical to those of CopyItemAndModify().

#### `itemproperty ItemPropertyOnHitCastSpell(int nSpell, int nLevel)`
> Creates an item property that (when applied to a weapon item) causes a spell to be cast
> when a successful strike is made, or (when applied to armor) is struck by an opponent.
> - nSpell uses the IP_CONST_ONHIT_CASTSPELL_* constants

#### `int GetItemPropertySubType(itemproperty iProperty)`
> Returns the SubType number of the item property. See the 2DA files for value definitions.

#### `int GetActionMode(object oCreature, int nMode)`
> Gets the status of ACTION_MODE_* modes on a creature.

#### `void SetActionMode(object oCreature, int nMode, int nStatus)`
> Sets the status of modes ACTION_MODE_* on a creature.

#### `int GetArcaneSpellFailure(object oCreature)`
> Returns the current arcane spell failure factor of a creature

#### `void ActionExamine(object oExamine)`
> Makes a player examine the object oExamine. This causes the examination
> pop-up box to appear for the object specified.

#### `itemproperty ItemPropertyVisualEffect(int nEffect)`
> Creates a visual effect (ITEM_VISUAL_*) that may be applied to
> melee weapons only.

#### `void SetLootable(object oCreature, int bLootable)`
> Sets the lootable state of a *living* NPC creature.
> This function will *not* work on players or dead creatures.

#### `int GetLootable(object oCreature)`
> Returns the lootable state of a creature.

#### `float GetCutsceneCameraMoveRate(object oCreature)`
> Returns the current movement rate factor
> of the cutscene 'camera man'.
> NOTE: This will be a value between 0.1, 2.0 (10%-200%)

#### `void SetCutsceneCameraMoveRate(object oCreature, float fRate)`
> Sets the current movement rate factor for the cutscene
> camera man.
> NOTE: You can only set values between 0.1, 2.0 (10%-200%)

#### `int GetItemCursedFlag(object oItem)`
> Returns TRUE if the item is cursed and cannot be dropped

#### `void SetItemCursedFlag(object oItem, int nCursed)`
> When cursed, items cannot be dropped

#### `void SetMaxHenchmen(int nNumHenchmen)`
> Sets the maximum number of henchmen

#### `int GetMaxHenchmen()`
> Gets the maximum number of henchmen

#### `int GetAssociateType(object oAssociate)`
> Returns the associate type of the specified creature.
> - Returns ASSOCIATE_TYPE_NONE if the creature is not the associate of anyone.

#### `int GetSpellResistance(object oCreature)`
> Returns the spell resistance of the specified creature.
> - Returns 0 if the creature has no spell resistance or an invalid
> creature is passed in.

#### `void DayToNight(object oPlayer, float fTransitionTime = 0.0f)`
> Changes the current Day/Night cycle for this player to night
> - oPlayer: which player to change the lighting for
> - fTransitionTime: how long the transition should take

#### `void NightToDay(object oPlayer, float fTransitionTime = 0.0f)`
> Changes the current Day/Night cycle for this player to daylight
> - oPlayer: which player to change the lighting for
> - fTransitionTime: how long the transition should take

#### `int LineOfSightObject(object oSource, object oTarget)`
> Returns whether or not there is a direct line of sight
> between the two objects. (Not blocked by any geometry).
> PLEASE NOTE: This is an expensive function and may
> degrade performance if used frequently.

#### `int LineOfSightVector(vector vSource, vector vTarget)`
> Returns whether or not there is a direct line of sight
> between the two vectors. (Not blocked by any geometry).
> This function must be run on a valid object in the area
> it will not work on the module or area.
> PLEASE NOTE: This is an expensive function and may
> degrade performance if used frequently.

#### `int GetLastSpellCastClass()`
> Returns the class that the spellcaster cast the
> spell as.
> - Returns CLASS_TYPE_INVALID if the caster has
> no valid class (placeables, etc...)
> If used in an Area of Effect script it will return the creators spellcasting class.

#### `void SetBaseAttackBonus(int nBaseAttackBonus, object oCreature = OBJECT_SELF)`
> Sets the number of base attacks each round for the specified creature (PC or NPC).
> If set on a PC it will not be shown on their character sheet, but will save to BIC/savegame.
> - nBaseAttackBonus - Number of base attacks per round, 1 to 6

#### `void RestoreBaseAttackBonus(object oCreature = OBJECT_SELF)`
> Restores the number of base attacks back to it's
> original state.

#### `effect EffectCutsceneGhost()`
> Creates a cutscene ghost effect, this will allow creatures
> to pathfind through other creatures without bumping into them
> for the duration of the effect.

#### `itemproperty ItemPropertyArcaneSpellFailure(int nModLevel)`
> Creates an item property that offsets the effect on arcane spell failure
> that a particular item has. Parameters come from the ITEM_PROP_ASF_* group.

#### `int GetStoreGold(object oidStore)`
> Returns the amount of gold a store currently has. -1 indicates it is not using gold.
> -2 indicates the store could not be located.

#### `void SetStoreGold(object oidStore, int nGold)`
> Sets the amount of gold a store has. -1 means the store does not use gold.

#### `int GetStoreMaxBuyPrice(object oidStore)`
> Gets the maximum amount a store will pay for any item. -1 means price unlimited.
> -2 indicates the store could not be located.

#### `void SetStoreMaxBuyPrice(object oidStore, int nMaxBuy)`
> Sets the maximum amount a store will pay for any item. -1 means price unlimited.

#### `int GetStoreIdentifyCost(object oidStore)`
> Gets the amount a store charges for identifying an item. Default is 100. -1 means
> the store will not identify items.
> -2 indicates the store could not be located.

#### `void SetStoreIdentifyCost(object oidStore, int nCost)`
> Sets the amount a store charges for identifying an item. Default is 100. -1 means
> the store will not identify items.

#### `void SetCreatureAppearanceType(object oCreature, int nAppearanceType)`
> Sets the creature's appearance type to the value specified (uses the APPEARANCE_TYPE_XXX constants)

#### `int GetCreatureStartingPackage(object oCreature)`
> Returns the default package selected for this creature to level up with
> - returns PACKAGE_INVALID if error occurs

#### `effect EffectCutsceneImmobilize()`
> Returns an effect that when applied will paralyze the target's legs, rendering
> them unable to walk but otherwise unpenalized. This effect cannot be resisted.

#### `int GetIsInSubArea(object oCreature, object oSubArea = OBJECT_SELF)`
> Is this creature in the given subarea? (trigger, area of effect object, etc..)
> This function will tell you if the creature has triggered an onEnter event,
> not if it is physically within the space of the subarea

#### `int GetItemPropertyCostTable(itemproperty iProp)`
> Returns the Cost Table number of the item property. See the 2DA files for value definitions.

#### `int GetItemPropertyCostTableValue(itemproperty iProp)`
> Returns the Cost Table value (index of the cost table) of the item property.
> See the 2DA files for value definitions.

#### `int GetItemPropertyParam1(itemproperty iProp)`
> Returns the Param1 number of the item property. See the 2DA files for value definitions.

#### `int GetItemPropertyParam1Value(itemproperty iProp)`
> Returns the Param1 value of the item property. See the 2DA files for value definitions.

#### `int GetIsCreatureDisarmable(object oCreature)`
> Is this creature able to be disarmed? (checks disarm flag on creature, and if
> the creature actually has a weapon equipped in their right hand that is droppable)

#### `void SetStolenFlag(object oItem, int nStolenFlag)`
> Sets whether this item is 'stolen' or not

#### `void ForceRest(object oCreature)`
> Instantly gives this creature the benefits of a rest (restored hitpoints, spells, feats, etc..)

#### `void SetCameraHeight(object oPlayer, float fHeight = 0.0f)`
> Forces this player's camera to be set to this height. Setting this value to zero will
> restore the camera to the racial default height.

#### `void SetSkyBox(int nSkyBox, object oArea = OBJECT_INVALID)`
> Changes the sky that is displayed in the specified area.
> nSkyBox = SKYBOX_* constants (associated with skyboxes.2da)
> If no valid area (or object) is specified, it uses the area of caller.
> If an object other than an area is specified, will use the area that the object is currently in.

#### `int GetPhenoType(object oCreature)`
> Returns the creature's currently set PhenoType (body type).

#### `void SetPhenoType(int nPhenoType, object oCreature = OBJECT_SELF)`
> Sets the creature's PhenoType (body type) to the type specified.
> nPhenoType = PHENOTYPE_NORMAL
> nPhenoType = PHENOTYPE_BIG
> nPhenoType = PHENOTYPE_CUSTOM* - The custom PhenoTypes should only ever
> be used if you have specifically created your own custom content that
> requires the use of a new PhenoType and you have specified the appropriate
> custom PhenoType in your custom content.
> SetPhenoType will only work on part based creature (i.e. the starting
> default playable races).

#### `void SetFogColor(int nFogType, int nFogColor, object oArea = OBJECT_INVALID, float fFadeTime = 0.0)`
> Sets the fog color in the area specified.
> nFogType = FOG_TYPE_* specifies wether the Sun, Moon, or both fog types are set.
> nFogColor = FOG_COLOR_* specifies the color the fog is being set to.
> The fog color can also be represented as a hex RGB number if specific color shades
> are desired.
> The format of a hex specified color would be 0xFFEEDD where
> FF would represent the amount of red in the color
> EE would represent the amount of green in the color
> DD would represent the amount of blue in the color.
> If no valid area (or object) is specified, it uses the area of caller.
> If an object other than an area is specified, will use the area that the object is currently in.
> If fFadeTime is above 0.0, it will fade to the new color in the amount of seconds specified.

#### `int GetCutsceneMode(object oCreature = OBJECT_SELF)`
> Gets the current cutscene state of the player specified by oCreature.
> Returns TRUE if the player is in cutscene mode.
> Returns FALSE if the player is not in cutscene mode, or on an error
> (such as specifying a non creature object).

#### `int GetSkyBox(object oArea = OBJECT_INVALID)`
> Gets the skybox that is currently displayed in the specified area.
> Returns:
> SKYBOX_* constant
> If no valid area (or object) is specified, it uses the area of caller.
> If an object other than an area is specified, will use the area that the object is currently in.

#### `int GetFogColor(int nFogType, object oArea = OBJECT_INVALID)`
> Gets the fog color in the area specified.
> nFogType specifies wether the Sun, or Moon fog type is returned.
> Valid values for nFogType are FOG_TYPE_SUN or FOG_TYPE_MOON.
> If no valid area (or object) is specified, it uses the area of caller.
> If an object other than an area is specified, will use the area that the object is currently in.

#### `void SetFogAmount(int nFogType, int nFogAmount, object oArea = OBJECT_INVALID)`
> Sets the fog amount in the area specified.
> nFogType = FOG_TYPE_* specifies wether the Sun, Moon, or both fog types are set.
> nFogAmount = specifies the density that the fog is being set to.
> If no valid area (or object) is specified, it uses the area of caller.
> If an object other than an area is specified, will use the area that the object is currently in.

#### `int GetFogAmount(int nFogType, object oArea = OBJECT_INVALID)`
> Gets the fog amount in the area specified.
> nFogType = nFogType specifies wether the Sun, or Moon fog type is returned.
> Valid values for nFogType are FOG_TYPE_SUN or FOG_TYPE_MOON.
> If no valid area (or object) is specified, it uses the area of caller.
> If an object other than an area is specified, will use the area that the object is currently in.

#### `int GetPickpocketableFlag(object oItem)`
> returns TRUE if the item CAN be pickpocketed

#### `void SetPickpocketableFlag(object oItem, int bPickpocketable)`
> Sets the Pickpocketable flag on an item
> - oItem: the item to change
> - bPickpocketable: TRUE or FALSE, whether the item can be pickpocketed.

#### `int GetFootstepType(object oCreature = OBJECT_SELF)`
> returns the footstep type of the creature specified.
> The footstep type determines what the creature's footsteps sound
> like when ever they take a step.
> returns FOOTSTEP_TYPE_INVALID if used on a non-creature object, or if
> used on creature that has no footstep sounds by default (e.g. Will-O'-Wisp).

#### `void SetFootstepType(int nFootstepType, object oCreature = OBJECT_SELF)`
> Sets the footstep type of the creature specified.
> Changing a creature's footstep type will change the sound that
> its feet make when ever the creature makes takes a step.
> By default a creature's footsteps are detemined by the appearance
> type of the creature. SetFootstepType() allows you to make a
> creature use a difference footstep type than it would use by default
> for its given appearance.
> - nFootstepType (FOOTSTEP_TYPE_*):
> FOOTSTEP_TYPE_NORMAL
> FOOTSTEP_TYPE_LARGE
> FOOTSTEP_TYPE_DRAGON
> FOOTSTEP_TYPE_SoFT
> FOOTSTEP_TYPE_HOOF
> FOOTSTEP_TYPE_HOOF_LARGE
> FOOTSTEP_TYPE_BEETLE
> FOOTSTEP_TYPE_SPIDER
> FOOTSTEP_TYPE_SKELETON
> FOOTSTEP_TYPE_LEATHER_WING
> FOOTSTEP_TYPE_FEATHER_WING
> FOOTSTEP_TYPE_DEFAULT - Makes the creature use its original default footstep sounds.
> FOOTSTEP_TYPE_NONE
> - oCreature: the creature to change the footstep sound for.

#### `int GetCreatureWingType(object oCreature = OBJECT_SELF)`
> returns the Wing type of the creature specified.
> CREATURE_WING_TYPE_NONE
> CREATURE_WING_TYPE_DEMON
> CREATURE_WING_TYPE_ANGEL
> CREATURE_WING_TYPE_BAT
> CREATURE_WING_TYPE_DRAGON
> CREATURE_WING_TYPE_BUTTERFLY
> CREATURE_WING_TYPE_BIRD
> returns CREATURE_WING_TYPE_NONE if used on a non-creature object,
> if the creature has no wings, or if the creature can not have its
> wing type changed in the toolset.

#### `void SetCreatureWingType(int nWingType, object oCreature = OBJECT_SELF)`
> Sets the Wing type of the creature specified.
> - nWingType (CREATURE_WING_TYPE_*)
> CREATURE_WING_TYPE_NONE
> CREATURE_WING_TYPE_DEMON
> CREATURE_WING_TYPE_ANGEL
> CREATURE_WING_TYPE_BAT
> CREATURE_WING_TYPE_DRAGON
> CREATURE_WING_TYPE_BUTTERFLY
> CREATURE_WING_TYPE_BIRD
> - oCreature: the creature to change the wing type for.
> Note: Only two creature model types will support wings.
> The MODELTYPE for the part based (playable races) 'P'
> and MODELTYPE 'W'in the appearance.2da

#### `int GetCreatureBodyPart(int nPart, object oCreature = OBJECT_SELF)`
> returns the model number being used for the body part and creature specified
> The model number returned is for the body part when the creature is not wearing
> armor (i.e. whether or not the creature is wearing armor does not affect
> the return value).
> Note: Only works on part based creatures, which is typically restricted to
> the playable races (unless some new part based custom content has been
> added to the module).
> returns CREATURE_PART_INVALID if used on a non-creature object,
> or if the creature does not use a part based model.
> - nPart (CREATURE_PART_*)
> CREATURE_PART_RIGHT_FOOT
> CREATURE_PART_LEFT_FOOT
> CREATURE_PART_RIGHT_SHIN
> CREATURE_PART_LEFT_SHIN
> CREATURE_PART_RIGHT_THIGH
> CREATURE_PART_LEFT_THIGH
> CREATURE_PART_PELVIS
> CREATURE_PART_TORSO
> CREATURE_PART_BELT
> CREATURE_PART_NECK
> CREATURE_PART_RIGHT_FOREARM
> CREATURE_PART_LEFT_FOREARM
> CREATURE_PART_RIGHT_BICEP
> CREATURE_PART_LEFT_BICEP
> CREATURE_PART_RIGHT_SHOULDER
> CREATURE_PART_LEFT_SHOULDER
> CREATURE_PART_RIGHT_HAND
> CREATURE_PART_LEFT_HAND
> CREATURE_PART_HEAD

#### `void SetCreatureBodyPart(int nPart, int nModelNumber, object oCreature = OBJECT_SELF)`
> Sets the body part model to be used on the creature specified.
> The model names for parts need to be in the following format:
> p<m/f><race letter><phenotype>_<body part><model number>.mdl
> - nPart (CREATURE_PART_*)
> CREATURE_PART_RIGHT_FOOT
> CREATURE_PART_LEFT_FOOT
> CREATURE_PART_RIGHT_SHIN
> CREATURE_PART_LEFT_SHIN
> CREATURE_PART_RIGHT_THIGH
> CREATURE_PART_LEFT_THIGH
> CREATURE_PART_PELVIS
> CREATURE_PART_TORSO
> CREATURE_PART_BELT
> CREATURE_PART_NECK
> CREATURE_PART_RIGHT_FOREARM
> CREATURE_PART_LEFT_FOREARM
> CREATURE_PART_RIGHT_BICEP
> CREATURE_PART_LEFT_BICEP
> CREATURE_PART_RIGHT_SHOULDER
> CREATURE_PART_LEFT_SHOULDER
> CREATURE_PART_RIGHT_HAND
> CREATURE_PART_LEFT_HAND
> CREATURE_PART_HEAD
> - nModelNumber: CREATURE_MODEL_TYPE_*
> CREATURE_MODEL_TYPE_NONE
> CREATURE_MODEL_TYPE_SKIN (not for use on shoulders, pelvis or head).
> CREATURE_MODEL_TYPE_TATTOO (for body parts that support tattoos, i.e. not heads/feet/hands).
> CREATURE_MODEL_TYPE_UNDEAD (undead model only exists for the right arm parts).
> - oCreature: the creature to change the body part for.
> Note: Only part based creature appearance types are supported.
> i.e. The model types for the playable races ('P') in the appearance.2da

#### `int GetCreatureTailType(object oCreature = OBJECT_SELF)`
> returns the Tail type of the creature specified.
> CREATURE_TAIL_TYPE_NONE
> CREATURE_TAIL_TYPE_LIZARD
> CREATURE_TAIL_TYPE_BONE
> CREATURE_TAIL_TYPE_DEVIL
> returns CREATURE_TAIL_TYPE_NONE if used on a non-creature object,
> if the creature has no Tail, or if the creature can not have its
> Tail type changed in the toolset.

#### `void SetCreatureTailType(int nTailType, object oCreature = OBJECT_SELF)`
> Sets the Tail type of the creature specified.
> - nTailType (CREATURE_TAIL_TYPE_*)
> CREATURE_TAIL_TYPE_NONE
> CREATURE_TAIL_TYPE_LIZARD
> CREATURE_TAIL_TYPE_BONE
> CREATURE_TAIL_TYPE_DEVIL
> - oCreature: the creature to change the Tail type for.
> Note: Only two creature model types will support Tails.
> The MODELTYPE for the part based (playable) races 'P'
> and MODELTYPE 'T'in the appearance.2da

#### `int GetHardness(object oObject = OBJECT_SELF)`
> returns the Hardness of a Door or Placeable object.
> - oObject: a door or placeable object.
> returns -1 on an error or if used on an object that is
> neither a door nor a placeable object.

#### `void SetHardness(int nHardness, object oObject = OBJECT_SELF)`
> Sets the Hardness of a Door or Placeable object.
> - nHardness: must be between 0 and 250.
> - oObject: a door or placeable object.
> Does nothing if used on an object that is neither
> a door nor a placeable.

#### `void SetLockKeyRequired(object oObject, int nKeyRequired = TRUE)`
> When set the object can not be opened unless the
> opener possesses the required key. The key tag required
> can be specified either in the toolset, or by using
> the SetLockKeyTag() scripting command.
> - oObject: a door, or placeable.
> - nKeyRequired: TRUE/FALSE

#### `void SetLockKeyTag(object oObject, string sNewKeyTag)`
> Set the key tag required to open object oObject.
> This will only have an effect if the object is set to
> "Key required to unlock or lock" either in the toolset
> or by using the scripting command SetLockKeyRequired().
> - oObject: a door, placeable or trigger.
> - sNewKeyTag: the key tag required to open the locked object.

#### `void SetLockLockable(object oObject, int nLockable = TRUE)`
> Sets whether or not the object can be locked.
> - oObject: a door or placeable.
> - nLockable: TRUE/FALSE

#### `void SetLockUnlockDC(object oObject, int nNewUnlockDC)`
> Sets the DC for unlocking the object.
> - oObject: a door or placeable object.
> - nNewUnlockDC: must be between 0 and 250.

#### `void SetLockLockDC(object oObject, int nNewLockDC)`
> Sets the DC for locking the object.
> - oObject: a door or placeable object.
> - nNewLockDC: must be between 0 and 250.

#### `void SetTrapDisarmable(object oTrapObject, int nDisarmable = TRUE)`
> Sets whether or not the trapped object can be disarmed.
> - oTrapObject: a placeable, door or trigger
> - nDisarmable: TRUE/FALSE

#### `void SetTrapDetectable(object oTrapObject, int nDetectable = TRUE)`
> Sets whether or not the trapped object can be detected.
> - oTrapObject: a placeable, door or trigger
> - nDetectable: TRUE/FALSE
> Note: Setting a trapped object to not be detectable will
> not make the trap disappear if it has already been detected.

#### `void SetTrapOneShot(object oTrapObject, int nOneShot = TRUE)`
> Sets whether or not the trap is a one-shot trap
> (i.e. whether or not the trap resets itself after firing).
> - oTrapObject: a placeable, door or trigger
> - nOneShot: TRUE/FALSE

#### `void SetTrapKeyTag(object oTrapObject, string sKeyTag)`
> Set the tag of the key that will disarm oTrapObject.
> - oTrapObject: a placeable, door or trigger

#### `void SetTrapDisarmDC(object oTrapObject, int nDisarmDC)`
> Set the DC for disarming oTrapObject.
> - oTrapObject: a placeable, door or trigger
> - nDisarmDC: must be between 0 and 250.

#### `void SetTrapDetectDC(object oTrapObject, int nDetectDC)`
> Set the DC for detecting oTrapObject.
> - oTrapObject: a placeable, door or trigger
> - nDetectDC: must be between 0 and 250.

#### `object CreateTrapAtLocation(int nTrapType, location lLocation, float fSize = 2.0f, string sTag = "", int nFaction = STANDARD_FACTION_HOSTILE, string sOnDisarmScript = "", string sOnTrapTriggeredScript = "")`
> Creates a square Trap object.
> - nTrapType: The base type of trap (TRAP_BASE_TYPE_*)
> - lLocation: The location and orientation that the trap will be created at.
> - fSize: The size of the trap. Minimum size allowed is 1.0f.
> - sTag: The tag of the trap being created.
> - nFaction: The faction of the trap (STANDARD_FACTION_*).
> - sOnDisarmScript: The OnDisarm script that will fire when the trap is disarmed.
> If "" no script will fire.
> - sOnTrapTriggeredScript: The OnTrapTriggered script that will fire when the
> trap is triggered.
> If "" the default OnTrapTriggered script for the trap
> type specified will fire instead (as specified in the
> traps.2da).

#### `void CreateTrapOnObject(int nTrapType, object oObject, int nFaction = STANDARD_FACTION_HOSTILE, string sOnDisarmScript = "", string sOnTrapTriggeredScript = "")`
> Creates a Trap on the object specified.
> - nTrapType: The base type of trap (TRAP_BASE_TYPE_*)
> - oObject: The object that the trap will be created on. Works only on Doors and Placeables.
> - nFaction: The faction of the trap (STANDARD_FACTION_*).
> - sOnDisarmScript: The OnDisarm script that will fire when the trap is disarmed.
> If "" no script will fire.
> - sOnTrapTriggeredScript: The OnTrapTriggered script that will fire when the
> trap is triggered.
> If "" the default OnTrapTriggered script for the trap
> type specified will fire instead (as specified in the
> traps.2da).
> Note: After creating a trap on an object, you can change the trap's properties
> using the various SetTrap* scripting commands by passing in the object
> that the trap was created on (i.e. oObject) to any subsequent SetTrap* commands.

#### `void SetWillSavingThrow(object oObject, int nWillSave)`
> Set the Will saving throw value of the Door or Placeable object oObject.
> - oObject: a door or placeable object.
> - nWillSave: must be between 0 and 250.

#### `void SetReflexSavingThrow(object oObject, int nReflexSave)`
> Set the Reflex saving throw value of the Door or Placeable object oObject.
> - oObject: a door or placeable object.
> - nReflexSave: must be between 0 and 250.

#### `void SetFortitudeSavingThrow(object oObject, int nFortitudeSave)`
> Set the Fortitude saving throw value of the Door or Placeable object oObject.
> - oObject: a door or placeable object.
> - nFortitudeSave: must be between 0 and 250.

#### `string GetTilesetResRef(object oArea)`
> returns the resref (TILESET_RESREF_*) of the tileset used to create area oArea.
> TILESET_RESREF_BEHOLDER_CAVES
> TILESET_RESREF_CASTLE_INTERIOR
> TILESET_RESREF_CITY_EXTERIOR
> TILESET_RESREF_CITY_INTERIOR
> TILESET_RESREF_CRYPT
> TILESET_RESREF_DESERT
> TILESET_RESREF_DROW_INTERIOR
> TILESET_RESREF_DUNGEON
> TILESET_RESREF_FOREST
> TILESET_RESREF_FROZEN_WASTES
> TILESET_RESREF_ILLITHID_INTERIOR
> TILESET_RESREF_MICROSET
> TILESET_RESREF_MINES_AND_CAVERNS
> TILESET_RESREF_RUINS
> TILESET_RESREF_RURAL
> TILESET_RESREF_RURAL_WINTER
> TILESET_RESREF_SEWERS
> TILESET_RESREF_UNDERDARK
> returns an empty string on an error.

#### `int GetTrapRecoverable(object oTrapObject)`
> - oTrapObject: a placeable, door or trigger
> Returns TRUE if oTrapObject can be recovered.

#### `void SetTrapRecoverable(object oTrapObject, int nRecoverable = TRUE)`
> Sets whether or not the trapped object can be recovered.
> - oTrapObject: a placeable, door or trigger

#### `int GetModuleXPScale()`
> Get the XP scale being used for the module.

#### `void SetModuleXPScale(int nXPScale)`
> Set the XP scale used by the module.
> - nXPScale: The XP scale to be used. Must be between 0 and 200.

#### `string GetKeyRequiredFeedback(object oObject)`
> Get the feedback message that will be displayed when trying to unlock the object oObject.
> - oObject: a door or placeable.
> Returns an empty string "" on an error or if the game's default feedback message is being used

#### `void SetKeyRequiredFeedback(object oObject, string sFeedbackMessage)`
> Set the feedback message that is displayed when trying to unlock the object oObject.
> This will only have an effect if the object is set to
> "Key required to unlock or lock" either in the toolset
> or by using the scripting command SetLockKeyRequired().
> - oObject: a door or placeable.
> - sFeedbackMessage: the string to be displayed in the player's text window.
> to use the game's default message, set sFeedbackMessage to ""

#### `int GetTrapActive(object oTrapObject)`
> - oTrapObject: a placeable, door or trigger
> Returns TRUE if oTrapObject is active

#### `void SetTrapActive(object oTrapObject, int nActive = TRUE)`
> Sets whether or not the trap is an active trap
> - oTrapObject: a placeable, door or trigger
> - nActive: TRUE/FALSE
> Notes:
> Setting a trap as inactive will not make the
> trap disappear if it has already been detected.
> Call SetTrapDetectedBy() to make a detected trap disappear.
> To make an inactive trap not detectable call SetTrapDetectable()

#### `void LockCameraPitch(object oPlayer, int bLocked = TRUE)`
> Locks the player's camera pitch to its current pitch setting,
> or unlocks the player's camera pitch.
> Stops the player from tilting their camera angle.
> - oPlayer: A player object.
> - bLocked: TRUE/FALSE.

#### `void LockCameraDistance(object oPlayer, int bLocked = TRUE)`
> Locks the player's camera distance to its current distance setting,
> or unlocks the player's camera distance.
> Stops the player from being able to zoom in/out the camera.
> - oPlayer: A player object.
> - bLocked: TRUE/FALSE.

#### `void LockCameraDirection(object oPlayer, int bLocked = TRUE)`
> Locks the player's camera direction to its current direction,
> or unlocks the player's camera direction to enable it to move
> freely again.
> Stops the player from being able to rotate the camera direction.
> - oPlayer: A player object.
> - bLocked: TRUE/FALSE.

#### `object GetPlaceableLastClickedBy()`
> Get the last object that default clicked (left clicked) on the placeable object
> that is calling this function.
> Should only be called from a placeables OnClick event.
> Returns OBJECT_INVALID if it is called by something other than a placeable.

#### `int GetInfiniteFlag(object oItem)`
> returns TRUE if the item is flagged as infinite.
> - oItem: an item.
> The infinite property affects the buying/selling behavior of the item in a store.
> An infinite item will still be available to purchase from a store after a player
> buys the item (non-infinite items will disappear from the store when purchased).

#### `void SetInfiniteFlag(object oItem, int bInfinite = TRUE)`
> Sets the Infinite flag on an item
> - oItem: the item to change
> - bInfinite: TRUE or FALSE, whether the item should be Infinite
> The infinite property affects the buying/selling behavior of the item in a store.
> An infinite item will still be available to purchase from a store after a player
> buys the item (non-infinite items will disappear from the store when purchased).

#### `int GetAreaSize(int nAreaDimension, object oArea = OBJECT_INVALID)`
> Gets the size of the area.
> - nAreaDimension: The area dimension that you wish to determine.
> AREA_HEIGHT
> AREA_WIDTH
> - oArea: The area that you wish to get the size of.
> Returns: The number of tiles that the area is wide/high, or zero on an error.
> If no valid area (or object) is specified, it uses the area of the caller.
> If an object other than an area is specified, will use the area that the object is currently in.

#### `void SetName(object oObject, string sNewName = "")`
> Set the name of oObject.
> - oObject: the object for which you are changing the name (a creature, placeable, item, or door).
> - sNewName: the new name that the object will use.
> Note: Setting an object's name to "" will make the object
> revert to using the name it had originally before any
> SetName() calls were made on the object.

#### `int GetPortraitId(object oTarget = OBJECT_SELF)`
> Get the PortraitId of oTarget.
> - oTarget: the object for which you are getting the portrait Id.
> Returns: The Portrait Id number being used for the object oTarget.
> The Portrait Id refers to the row number of the Portraits.2da
> that this portrait is from.
> If a custom portrait is being used, oTarget is a player object,
> or on an error returns PORTRAIT_INVALID. In these instances
> try using GetPortraitResRef() instead.

#### `void SetPortraitId(object oTarget, int nPortraitId)`
> Change the portrait of oTarget to use the Portrait Id specified.
> - oTarget: the object for which you are changing the portrait.
> - nPortraitId: The Id of the new portrait to use.
> nPortraitId refers to a row in the Portraits.2da
> Note: Not all portrait Ids are suitable for use with all object types.
> Setting the portrait Id will also cause the portrait ResRef
> to be set to the appropriate portrait ResRef for the Id specified.

#### `string GetPortraitResRef(object oTarget = OBJECT_SELF)`
> Get the Portrait ResRef of oTarget.
> - oTarget: the object for which you are getting the portrait ResRef.
> Returns: The Portrait ResRef being used for the object oTarget.
> The Portrait ResRef will not include a trailing size letter.

#### `void SetPortraitResRef(object oTarget, string sPortraitResRef)`
> Change the portrait of oTarget to use the Portrait ResRef specified.
> - oTarget: the object for which you are changing the portrait.
> - sPortraitResRef: The ResRef of the new portrait to use.
> The ResRef should not include any trailing size letter ( e.g. po_el_f_09_ ).
> Note: Not all portrait ResRefs are suitable for use with all object types.
> Setting the portrait ResRef will also cause the portrait Id
> to be set to PORTRAIT_INVALID.

#### `void SetUseableFlag(object oTarget, int nUseableFlag)`
> Set oTarget's useable object status.
> Note: Only works on non-static placeables, creatures, doors and items.
> On items, it affects interactivity when they're on the ground, and not useability in inventory.

#### `string GetDescription(object oObject, int bOriginalDescription = FALSE, int bIdentifiedDescription = TRUE)`
> Get the description of oObject.
> - oObject: the object from which you are obtaining the description.
> Can be a creature, item, placeable, door, trigger or module object.
> - bOriginalDescription:  if set to true any new description specified via a SetDescription scripting command
> is ignored and the original object's description is returned instead.
> - bIdentified: If oObject is an item, setting this to TRUE will return the identified description,
> setting this to FALSE will return the unidentified description. This flag has no
> effect on objects other than items.

#### `void SetDescription(object oObject, string sNewDescription = "", int bIdentifiedDescription = TRUE)`
> Set the description of oObject.
> - oObject: the object for which you are changing the description
> Can be a creature, placeable, item, door, or trigger.
> - sNewDescription: the new description that the object will use.
> - bIdentified: If oObject is an item, setting this to TRUE will set the identified description,
> setting this to FALSE will set the unidentified description. This flag has no
> effect on objects other than items.
> Note: Setting an object's description to "" will make the object
> revert to using the description it originally had before any
> SetDescription() calls were made on the object.

#### `object GetPCChatSpeaker()`
> Get the PC that sent the last player chat(text) message.
> Should only be called from a module's OnPlayerChat event script.
> Returns OBJECT_INVALID on error.
> Note: Private tells do not trigger a OnPlayerChat event.

#### `string GetPCChatMessage()`
> Get the last player chat(text) message that was sent.
> Should only be called from a module's OnPlayerChat event script.
> Returns empty string "" on error.
> Note: Private tells do not trigger a OnPlayerChat event.

#### `int GetPCChatVolume()`
> Get the volume of the last player chat(text) message that was sent.
> Returns one of the following TALKVOLUME_* constants based on the volume setting
> that the player used to send the chat message.
> TALKVOLUME_TALK
> TALKVOLUME_WHISPER
> TALKVOLUME_SHOUT
> TALKVOLUME_SILENT_SHOUT (used for DM chat channel)
> TALKVOLUME_PARTY
> Should only be called from a module's OnPlayerChat event script.
> Returns -1 on error.
> Note: Private tells do not trigger a OnPlayerChat event.

#### `void SetPCChatMessage(string sNewChatMessage = "")`
> Set the last player chat(text) message before it gets sent to other players.
> - sNewChatMessage: The new chat text to be sent onto other players.
> Setting the player chat message to an empty string "",
> will cause the chat message to be discarded
> (i.e. it will not be sent to other players).
> Note: The new chat message gets sent after the OnPlayerChat script exits.

#### `void SetPCChatVolume(int nTalkVolume = TALKVOLUME_TALK)`
> Set the last player chat(text) volume before it gets sent to other players.
> - nTalkVolume: The new volume of the chat text to be sent onto other players.
> TALKVOLUME_TALK
> TALKVOLUME_WHISPER
> TALKVOLUME_SHOUT
> TALKVOLUME_SILENT_SHOUT (used for DM chat channel)
> TALKVOLUME_PARTY
> TALKVOLUME_TELL (sends the chat message privately back to the original speaker)
> Note: The new chat message gets sent after the OnPlayerChat script exits.

#### `int GetColor(object oObject, int nColorChannel)`
> Get the Color of oObject from the color channel specified.
> - oObject: the object from which you are obtaining the color.
> Can be a creature that has color information (i.e. the playable races).
> - nColorChannel: The color channel that you want to get the color value of.
> COLOR_CHANNEL_SKIN
> COLOR_CHANNEL_HAIR
> COLOR_CHANNEL_TATTOO_1
> COLOR_CHANNEL_TATTOO_2
> Returns -1 on error.

#### `void SetColor(object oObject, int nColorChannel, int nColorValue)`
> Set the color channel of oObject to the color specified.
> - oObject: the object for which you are changing the color.
> Can be a creature that has color information (i.e. the playable races).
> - nColorChannel: The color channel that you want to set the color value of.
> COLOR_CHANNEL_SKIN
> COLOR_CHANNEL_HAIR
> COLOR_CHANNEL_TATTOO_1
> COLOR_CHANNEL_TATTOO_2
> - nColorValue: The color you want to set (0-175).

#### `itemproperty ItemPropertyMaterial(int nMaterialType)`
> Returns Item property Material.  You need to specify the Material Type.
> - nMasterialType: The Material Type should be a positive integer between 0 and 77 (see iprp_matcost.2da).
> Note: The Material Type property will only affect the cost of the item if you modify the cost in the iprp_matcost.2da.

#### `itemproperty ItemPropertyQuality(int nQuality)`
> Returns Item property Quality. You need to specify the Quality.
> - nQuality:  The Quality of the item property to create (see iprp_qualcost.2da).
> IP_CONST_QUALITY_*
> Note: The quality property will only affect the cost of the item if you modify the cost in the iprp_qualcost.2da.

#### `itemproperty ItemPropertyAdditional(int nAdditionalProperty)`
> Returns a generic Additional Item property. You need to specify the Additional property.
> - nProperty: The item property to create (see iprp_addcost.2da).
> IP_CONST_ADDITIONAL_*
> Note: The additional property only affects the cost of the item if you modify the cost in the iprp_addcost.2da.

#### `void SetTag(object oObject, string sNewTag)`
> Sets a new tag for oObject.
> Will do nothing for invalid objects or the module object.
> Note: Care needs to be taken with this function.
> Changing the tag for creature with waypoints will make them stop walking them.
> Changing waypoint, door or trigger tags will break their area transitions.

#### `string GetEffectTag(effect eEffect)`
> Returns the string tag set for the provided effect.
> - If no tag has been set, returns an empty string.

#### `effect TagEffect(effect eEffect, string sNewTag)`
> Tags the effect with the provided string.
> - Any other tags in the link will be overwritten.

#### `int GetEffectCasterLevel(effect eEffect)`
> Returns the caster level of the creature who created the effect.
> - If not created by a creature, returns 0.
> - If created by a spell-like ability, returns 0.

#### `int GetEffectDuration(effect eEffect)`
> Returns the total duration of the effect in seconds.
> - Returns 0 if the duration type of the effect is not DURATION_TYPE_TEMPORARY.

#### `int GetEffectDurationRemaining(effect eEffect)`
> Returns the remaining duration of the effect in seconds.
> - Returns 0 if the duration type of the effect is not DURATION_TYPE_TEMPORARY.

#### `string GetItemPropertyTag(itemproperty nProperty)`
> Returns the string tag set for the provided item property.
> - If no tag has been set, returns an empty string.

#### `itemproperty TagItemProperty(itemproperty nProperty, string sNewTag)`
> Tags the item property with the provided string.
> - Any tags currently set on the item property will be overwritten.

#### `int GetItemPropertyDuration(itemproperty nProperty)`
> Returns the total duration of the item property in seconds.
> - Returns 0 if the duration type of the item property is not DURATION_TYPE_TEMPORARY.

#### `int GetItemPropertyDurationRemaining(itemproperty nProperty)`
> Returns the remaining duration of the item property in seconds.
> - Returns 0 if the duration type of the item property is not DURATION_TYPE_TEMPORARY.

#### `object CreateArea(string sSourceResRef, string sNewTag = "", string sNewName = "")`
> Instances a new area from the given sSourceResRef, which needs to be a existing module area.
> Will optionally set a new area tag and displayed name. The new area is accessible
> immediately, but initialisation scripts for the area and all contained creatures will only
> run after the current script finishes (so you can clean up objects before returning).
> Returns the new area, or OBJECT_INVALID on failure.
> Note: When spawning a second instance of a existing area, you will have to manually
> adjust all transitions (doors, triggers) with the relevant script commands,
> or players might end up in the wrong area.
> Note: Areas cannot have duplicate ResRefs, so your new area will have a autogenerated,
> sequential resref starting with "nw_"; for example: nw_5. You cannot influence this resref.
> If you destroy an area, that resref will be come free for reuse for the next area created.
> If you need to know the resref of your new area, you can call GetResRef on it.
> Note: When instancing an area from a loaded savegame, it will spawn the area as it was at time of save, NOT
> at module creation. This is because the savegame replaces the module data. Due to technical limitations,
> polymorphed creatures, personal reputation, and associates will currently fail to restore correctly.

#### `int DestroyArea(object oArea)`
> Destroys the given area object and everything in it.
> If the area is in a module, the .are and .git data is left behind and you can spawn from
> it again. If the area is a temporary copy, the data will be deleted and you cannot spawn it again
> via the resref.
> Return values:
> 0: Object not an area or invalid.
> -1: Area contains spawn location and removal would leave module without entrypoint.
> -2: Players in area.
> 1: Area destroyed successfully.

#### `object CopyArea(object oArea, string sNewTag = "", string sNewName = "")`
> Creates a copy of a existing area, including everything inside of it (except players).
> Will optionally set a new area tag and displayed name. The new area is accessible
> immediately, but initialisation scripts for the area and all contained creatures will only
> run after the current script finishes (so you can clean up objects before returning).
> This is similar to CreateArea, except this variant will copy all changes made to the source
> area since it has spawned. CreateArea() will instance the area from the .are and .git data
> as it was at creation.
> Returns the new area, or OBJECT_INVALID on error.
> Note: You will have to manually adjust all transitions (doors, triggers) with the
> relevant script commands, or players might end up in the wrong area.
> Note: Areas cannot have duplicate ResRefs, so your new area will have a autogenerated,
> sequential resref starting with "nw_"; for example: nw_5. You cannot influence this resref.
> If you destroy an area, that resref will be come free for reuse for the next area created.
> If you need to know the resref of your new area, you can call GetResRef on it.

#### `object GetFirstArea()`
> Returns the first area in the module.

#### `object GetNextArea()`
> Returns the next area in the module (after GetFirstArea), or OBJECT_INVALID if no more
> areas are loaded.

#### `void SetTransitionTarget(object oTransition, object oTarget)`
> Sets the transition target for oTransition.
> Notes:
> - oTransition can be any valid game object, except areas.
> - oTarget can be any valid game object with a location, or OBJECT_INVALID (to unlink).
> - Rebinding a transition will NOT change the other end of the transition; for example,
> with normal doors you will have to do either end separately.
> - Any valid game object can hold a transition target, but only some are used by the game engine
> (doors and triggers). This might change in the future. You can still set and query them for
> other game objects from nwscript.
> - Transition target objects are cached: The toolset-configured destination tag is
> used for a lookup only once, at first use. Thus, attempting to use SetTag() to change the
> destination for a transition will not work in a predictable fashion.

#### `void SetHiddenWhenEquipped(object oItem, int nValue)`
> Sets whether the provided item should be hidden when equipped.
> - The intended usage of this function is to provide an easy way to hide helmets, but it
> can be used equally for any slot which has creature mesh visibility when equipped,
> e.g.: armour, helm, cloak, left hand, and right hand.
> - nValue should be TRUE or FALSE.

#### `int GetHiddenWhenEquipped(object oItem)`
> Returns whether the provided item is hidden when equipped.

#### `int SetTileExplored(object creature, object area, int x, int y, int newState)`
> Sets if the given creature has explored tile at x, y of the given area.
> Note that creature needs to be a player- or player-possessed creature.
> Keep in mind that tile exploration also controls object visibility in areas
> and the fog of war for interior and underground areas.
> Return values:
> -1: Area or creature invalid.
> 0: Tile was not explored before setting newState.
> 1: Tile was explored before setting newState.

#### `int GetTileExplored(object creature, object area, int x, int y)`
> Returns whether the given tile at x, y, for the given creature in the stated
> area is visible on the map.
> Note that creature needs to be a player- or player-possessed creature.
> Keep in mind that tile exploration also controls object visibility in areas
> and the fog of war for interior and underground areas.
> Return values:
> -1: Area or creature invalid.
> 0: Tile is not explored yet.
> 1: Tile is explored.

#### `int SetCreatureExploresMinimap(object creature, int newState)`
> Sets the creature to auto-explore the map as it walks around.
> Keep in mind that tile exploration also controls object visibility in areas
> and the fog of war for interior and underground areas.
> This means that if you turn off auto exploration, it falls to you to manage this
> through SetTileExplored(); otherwise, the player will not be able to see anything.
> Valid arguments: TRUE and FALSE.
> Does nothing for non-creatures.
> Returns the previous state (or -1 if non-creature).

#### `int GetCreatureExploresMinimap(object creature)`
> Returns TRUE if the creature is set to auto-explore the map as it walks around (on by default).
> Returns FALSE if creature is not actually a creature.

#### `int GetSurfaceMaterial(location at)`
> Get the surface material at the given location. (This is
> equivalent to the walkmesh type).
> Returns 0 if the location is invalid or has no surface type.

#### `float GetGroundHeight(location at)`
> Returns the z-offset at which the walkmesh is at the given location.
> Returns -6.0 for invalid locations.

#### `int GetAttackBonusLimit()`
> Gets the attack bonus limit.
> - The default value is 20.

#### `int GetDamageBonusLimit()`
> Gets the damage bonus limit.
> - The default value is 100.

#### `int GetSavingThrowBonusLimit()`
> Gets the saving throw bonus limit.
> - The default value is 20.

#### `int GetAbilityBonusLimit()`
> Gets the ability bonus limit.
> - The default value is 12.

#### `int GetAbilityPenaltyLimit()`
> Gets the ability penalty limit.
> - The default value is 30.

#### `int GetSkillBonusLimit()`
> Gets the skill bonus limit.
> - The default value is 50.

#### `void SetAttackBonusLimit(int nNewLimit)`
> Sets the attack bonus limit.
> - The minimum value is 0.
> - The maximum value is 255.
> - This script call will temporarily override user/server configuration for the running module only.

#### `void SetDamageBonusLimit(int nNewLimit)`
> Sets the damage bonus limit.
> - The minimum value is 0.
> - The maximum value is 255.
> - This script call will temporarily override user/server configuration for the running module only.

#### `void SetSavingThrowBonusLimit(int nNewLimit)`
> Sets the saving throw bonus limit.
> - The minimum value is 0.
> - The maximum value is 255.
> - This script call will temporarily override user/server configuration for the running module only.

#### `void SetAbilityBonusLimit(int nNewLimit)`
> Sets the ability bonus limit.
> - The minimum value is 0.
> - The maximum value is 255.
> - This script call will temporarily override user/server configuration for the running module only.

#### `void SetAbilityPenaltyLimit(int nNewLimit)`
> Sets the ability penalty limit.
> - The minimum value is 0.
> - The maximum value is 255.
> - This script call will temporarily override user/server configuration for the running module only.

#### `void SetSkillBonusLimit(int nNewLimit)`
> Sets the skill bonus limit.
> - The minimum value is 0.
> - The maximum value is 255.
> - This script call will temporarily override user/server configuration for the running module only.

#### `int GetIsPlayerConnectionRelayed(object oPlayer)`
> Get if oPlayer is currently connected over a relay (instead of directly).
> Returns FALSE for any other object, including OBJECT_INVALID.

#### `string GetEventScript(object oObject, int nHandler)`
> Returns the event script for the given object and handler.
> Will return "" if unset, the object is invalid, or the object cannot
> have the requested handler.

#### `int SetEventScript(object oObject, int nHandler, string sScript)`
> Sets the given event script for the given object and handler.
> Returns 1 on success, 0 on failure.
> Will fail if oObject is invalid or does not have the requested handler.

#### `float GetObjectVisualTransform(object oObject, int nTransform, int bCurrentLerp = FALSE, int nScope = OBJECT_VISUAL_TRANSFORM_DATA_SCOPE_BASE)`
> Gets a visual transform on the given object.
> - oObject can be any valid Creature, Placeable, Item or Door.
> - nTransform is one of OBJECT_VISUAL_TRANSFORM_*
> - nScope is one of OBJECT_VISUAL_TRANSFORM_DATA_SCOPE_* and specific to the object type being VT'ed.
> Returns the current (or default) value.

#### `float SetObjectVisualTransform(object oObject, int nTransform, float fValue, int nLerpType = OBJECT_VISUAL_TRANSFORM_LERP_NONE, float fLerpDuration = 0.0, int bPauseWithGame = TRUE, int nScope = OBJECT_VISUAL_TRANSFORM_DATA_SCOPE_BASE, int nBehaviorFlags = OBJECT_VISUAL_TRANSFORM_BEHAVIOR_DEFAULT, int nRepeats = 0)`
> Sets a visual transform on the given object.
> - oObject can be any valid Creature, Placeable, Item or Door.
> - nTransform is one of OBJECT_VISUAL_TRANSFORM_*
> - fValue depends on the transformation to apply.
> - nScope is one of OBJECT_VISUAL_TRANSFORM_DATA_SCOPE_* and specific to the object type being VT'ed.
> - nBehaviorFlags: bitmask of OBJECT_VISUAL_TRANSFORM_BEHAVIOR_*.
> - nRepeats: If > 0: N times, jump back to initial/from state after completing the transform. If -1: Do forever.
> Returns the old/previous value.

#### `void SetMaterialShaderUniformInt(object oObject, string sMaterial, string sParam, int nValue)`
> Sets an integer material shader uniform override.
> - sMaterial needs to be a material on that object.
> - sParam needs to be a valid shader parameter already defined on the material.

#### `void SetMaterialShaderUniformVec4(object oObject, string sMaterial, string sParam, float fValue1, float fValue2 = 0.0, float fValue3 = 0.0, float fValue4 = 0.0)`
> Sets a vec4 material shader uniform override.
> - sMaterial needs to be a material on that object.
> - sParam needs to be a valid shader parameter already defined on the material.
> - You can specify a single float value to set just a float, instead of a vec4.

#### `void ResetMaterialShaderUniforms(object oObject, string sMaterial = "", string sParam = "")`
> Resets material shader parameters on the given object:
> - Supply a material to only reset shader uniforms for meshes with that material.
> - Supply a parameter to only reset shader uniforms of that name.
> - Supply both to only reset shader uniforms of that name on meshes with that material.

#### `void Vibrate(object oPlayer, int nMotor, float fStrength, float fSeconds)`
> Vibrate the player's device or controller. Does nothing if vibration is not supported.
> - nMotor is one of VIBRATOR_MOTOR_*
> - fStrength is between 0.0 and 1.0
> - fSeconds is the number of seconds to vibrate

#### `void UnlockAchievement(object oPlayer, string sId, int nLastValue = 0, int nCurValue = 0, int nMaxValue = 0)`
> Unlock an achievement for the given player who must be logged in.
> - sId is the achievement ID on the remote server
> - nLastValue is the previous value of the associated achievement stat
> - nCurValue is the current value of the associated achievement stat
> - nMaxValue is the maximum value of the associate achievement stat

#### `string ExecuteScriptChunk(string sScriptChunk, object oObject = OBJECT_SELF, int bWrapIntoMain = TRUE)`
> Execute a script chunk.
> The script chunk runs immediately, same as ExecuteScript().
> The script is jitted in place and currently not cached: Each invocation will recompile the script chunk.
> Note that the script chunk will run as if a separate script. This is not eval().
> By default, the script chunk is wrapped into void main() {}. Pass in bWrapIntoMain = FALSE to override.
> Returns "" on success, or the compilation error.

#### `string GetRandomUUID()`
> Returns a UUID. This UUID will not be associated with any object.
> The generated UUID is currently a v4.

#### `string GetObjectUUID(object oObject)`
> Returns the given objects' UUID. This UUID is persisted across save boundaries,
> like Save/RestoreCampaignObject and save games.
> Thus, reidentification is only guaranteed in scenarios where players cannot introduce
> new objects (i.e. servervault servers).
> UUIDs are guaranteed to be unique in any single running game.
> If a loaded object would collide with a UUID already present in the game, the
> object receives no UUID and a warning is emitted to the log. Requesting a UUID
> for the new object will generate a random one.
> This UUID is useful to, for example:
> - Safely identify servervault characters
> - Track serialisable objects (like items or creatures) as they are saved to the
> campaign DB - i.e. persistent storage chests or dropped items.
> - Track objects across multiple game instances (in trusted scenarios).
> Currently, the following objects can carry UUIDs:
> Items, Creatures, Placeables, Triggers, Doors, Waypoints, Stores,
> Encounters, Areas.
> Will return "" (empty string) when the given object cannot carry a UUID.

#### `void ForceRefreshObjectUUID(object oObject)`
> Forces the given object to receive a new UUID, discarding the current value.

#### `object GetObjectByUUID(string sUUID)`
> Looks up a object on the server by it's UUID.
> Returns OBJECT_INVALID if the UUID is not on the server.

#### `void Reserved899()`
> Do not call. This does nothing on this platform except to return an error.

#### `void SetTextureOverride(string sOldName, string sNewName = "", object oPC = OBJECT_INVALID)`
> Makes oPC load texture sNewName instead of sOldName.
> If oPC is OBJECT_INVALID, it will apply the override to all active players
> Setting sNewName to "" will clear the override and revert to original.

#### `void PostString(object oPC, string sMsg, int nX = 0, int nY = 0, int nAnchor = SCREEN_ANCHOR_TOP_LEFT, float fLife = 10.0f, int nRGBA = 2147418367, int nRGBA2 = 2147418367, int nID = 0, string sFont = "")`
> Displays sMsg on oPC's screen.
> The message is displayed on top of whatever is on the screen, including UI elements
> nX, nY - coordinates of the first character to be displayed. The value is in terms
> of character 'slot' relative to the nAnchor anchor point.
> If the number is negative, it is applied from the bottom/right.
> nAnchor - SCREEN_ANCHOR_* constant
> fLife - Duration in seconds until the string disappears.
> nRGBA, nRGBA2 - Colors of the string in 0xRRGGBBAA format. String starts at nRGBA,
> but as it nears end of life, it will slowly blend into nRGBA2.
> nID - Optional ID of a string. If not 0, subsequent calls to PostString will
> remove the old string with the same ID, even if it's lifetime has not elapsed.
> Only positive values are allowed.
> sFont - If specified, use this custom font instead of default console font.

#### `int GetSpecialization(object oCreature, int nClass = CLASS_TYPE_WIZARD)`
> Returns oCreature's spell school specialization in nClass (SPELL_SCHOOL_* constants)
> Unless custom content is used, only Wizards have spell schools
> Returns -1 on error

#### `int GetDomain(object oCreature, int nDomainIndex = 1, int nClass = CLASS_TYPE_CLERIC)`
> Returns oCreature's domain in nClass (DOMAIN_* constants)
> nDomainIndex - 1 or 2
> Unless custom content is used, only Clerics have domains
> Returns -1 on error

#### `int GetPlayerBuildVersionMajor(object oPlayer)`
> Returns the patch build number of oPlayer (i.e. the 8193 out of "87.8193.35-29 abcdef01").
> Returns 0 if the given object isn't a player or did not advertise their build info, or the
> player version is old enough not to send this bit of build info to the server.

#### `int GetPlayerBuildVersionMinor(object oPlayer)`
> Returns the patch revision number of oPlayer (i.e. the 35 out of "87.8193.35-29 abcdef01").
> Returns 0 if the given object isn't a player or did not advertise their build info, or the
> player version is old enough not to send this bit of build info to the server.

#### `string GetScriptParam(string sParamName)`
> Returns the script parameter value for a given parameter name.
> Script parameters can be set for conversation scripts in the toolset's
> Conversation Editor, or for any script with SetScriptParam().
> Will return "" if a parameter with the given name does not exist.

#### `void SetScriptParam(string sParamName, string sParamValue)`
> Set a script parameter value for the next script to be run.
> Call this function to set parameters right before calling ExecuteScript().

#### `int GetItemPropertyUsesPerDayRemaining(object oItem, itemproperty ip)`
> Returns the number of uses per day remaining of the given item and item property.
> Will return 0 if the given item does not have the requested item property,
> or the item property is not uses/day.

#### `void SetItemPropertyUsesPerDayRemaining(object oItem, itemproperty ip, int nUsesPerDay)`
> Sets the number of uses per day remaining of the given item and item property.
> Will do nothing if the given item and item property is not uses/day.
> Will constrain nUsesPerDay to the maximum allowed as the cost table defines.

#### `void ActionUseItemOnObject(object oItem, itemproperty ip, object oTarget, int nSubPropertyIndex = 0, int bDecrementCharges = TRUE)`
> Queue an action to use an active item property.
> oItem - item that has the item property to use
> ip - item property to use
> object oTarget - target
> nSubPropertyIndex - specify if your itemproperty has subproperties (such as subradial spells)
> bDecrementCharges - decrement charges if item property is limited

#### `void ActionUseItemAtLocation(object oItem, itemproperty ip, location lTarget, int nSubPropertyIndex = 0, int bDecrementCharges = TRUE)`
> Queue an action to use an active item property.
> oItem - item that has the item property to use
> ip - item property to use
> location lTarget - target location (must be in the same area as item possessor)
> nSubPropertyIndex - specify if your itemproperty has subproperties (such as subradial spells)
> bDecrementCharges - decrement charges if item property is limited

#### `void EnterTargetingMode(object oPC, int nValidObjectTypes = OBJECT_TYPE_ALL, int nMouseCursorId = MOUSECURSOR_MAGIC, int nBadTargetCursor = MOUSECURSOR_NOMAGIC)`
> Makes oPC enter a targeting mode, letting them select an object as a target
> If a PC selects a target or cancels out, it will trigger the module OnPlayerTarget event.
> nValidObjectTypes - If you use 0 will cancel any current targeting mode the client is in.

#### `object GetTargetingModeSelectedObject()`
> Gets the target object in the module OnPlayerTarget event.
> Returns the area object when the target is the ground.
> Note: returns OBJECT_INVALID if the player cancelled out of targeting mode.

#### `vector GetTargetingModeSelectedPosition()`
> Gets the target position in the module OnPlayerTarget event.

#### `object GetLastPlayerToSelectTarget()`
> Gets the player object that triggered the OnPlayerTarget event.

#### `void SetObjectHiliteColor(object oObject, int nColor = -1)`
> Sets oObject's hilite color to nColor
> The nColor format is 0xRRGGBB; -1 clears the color override.

#### `void SetObjectMouseCursor(object oObject, int nCursor = -1)`
> Sets the cursor (MOUSECURSOR_*) to use when hovering over oObject

#### `int GetIsPlayerDM(object oCreature)`
> Returns TRUE if the given player-controlled creature has DM privileges
> gained through a player login (as opposed to the DM client).
> Note: GetIsDM() also returns TRUE for player creature DMs.

#### `void SetAreaWind(object oArea, vector vDirection, float fMagnitude, float fYaw, float fPitch)`
> Sets the detailed wind data for oArea
> The predefined values in the toolset are:
> NONE:  vDirection=(1.0, 1.0, 0.0), fMagnitude=0.0, fYaw=0.0,   fPitch=0.0
> LIGHT: vDirection=(1.0, 1.0, 0.0), fMagnitude=1.0, fYaw=100.0, fPitch=3.0
> HEAVY: vDirection=(1.0, 1.0, 0.0), fMagnitude=2.0, fYaw=150.0, fPitch=5.0

#### `void ReplaceObjectTexture(object oObject, string sOld, string sNew = "")`
> Replace's oObject's texture sOld with sNew.
> Specifying sNew = "" will restore the original texture.
> If sNew cannot be found, the original texture will be restored.
> sNew must refer to a simple texture, not PLT

#### `void SqlDestroyDatabase(object oObject)`
> Destroys the given sqlite database, clearing out all data and schema.
> This operation is _immediate_ and _irreversible_, even when
> inside a transaction or running query.
> Existing active/prepared sqlqueries will remain functional, but any references
> to stored data or schema members will be invalidated.
> oObject: Same as SqlPrepareQueryObject().
> To reset a campaign database, please use DestroyCampaignDatabase().

#### `string SqlGetError(sqlquery sqlQuery)`
> Returns "" if the last Sql command succeeded; or a human-readable error otherwise.
> Additionally, all SQL errors are logged to the server log.
> Additionally, all SQL errors are sent to all connected players.

#### `sqlquery SqlPrepareQueryCampaign(string sDatabase, string sQuery)`
> Sets up a query.
> This will NOT run the query; only make it available for parameter binding.
> To run the query, you need to call SqlStep(); even if you do not
> expect result data.
> sDatabase: The name of a campaign database.
> Note that when accessing campaign databases, you do not write access
> to the builtin tables needed for CampaignDB functionality.
> N.B.: You can pass sqlqueries into DelayCommand; HOWEVER
> they will NOT survive a game save/load ***
> Any commands on a restored sqlquery will fail.
> N.B.: All uncommitted transactions left over at script termination are automatically rolled back.
> This ensures that no database handle will be left in an unusable state.
> Please check the SQLite_README.txt file in lang/en/docs/ for the list of builtin functions.

#### `sqlquery SqlPrepareQueryObject(object oObject, string sQuery)`
> Sets up a query.
> This will NOT run the query; only make it available for parameter binding.
> To run the query, you need to call SqlStep(); even if you do not
> expect result data.
> oObject: Can be either the module (GetModule()), or a player character.
> The database is persisted to savegames in case of the module,
> and to character files in case of a player characters.
> Other objects cannot carry databases, and this function call
> will error for them.
> N.B: Databases on objects (especially player characters!) should be kept
> to a reasonable size. Delete old data you no longer need.
> If you attempt to store more than a few megabytes of data on a
> player creature, you may have a bad time.
> N.B.: You can pass sqlqueries into DelayCommand; HOWEVER
> they will NOT survive a game save/load ***
> Any commands on a restored sqlquery will fail.
> N.B.: All uncommitted transactions left over at script termination are automatically rolled back.
> This ensures that no database handle will be left in an unusable state.
> Please check the SQLite_README.txt file in lang/en/docs/ for the list of builtin functions.

#### `void SqlBindInt(sqlquery sqlQuery, string sParam, int nValue)`
> Bind an integer to a named parameter of the given prepared query.
> Example:
> sqlquery v = SqlPrepareQueryObject(GetModule(), "insert into test (col) values (@myint);");
> SqlBindInt(v, "@myint", 5);
> SqlStep(v);

#### `void SqlBindFloat(sqlquery sqlQuery, string sParam, float fFloat)`
> Bind a float to a named parameter of the given prepared query.

#### `void SqlBindString(sqlquery sqlQuery, string sParam, string sString)`
> Bind a string to a named parameter of the given prepared query.

#### `void SqlBindVector(sqlquery sqlQuery, string sParam, vector vVector)`
> Bind a vector to a named parameter of the given prepared query.

#### `void SqlBindObject(sqlquery sqlQuery, string sParam, object oObject, int bSaveObjectState = FALSE)`
> Bind a object to a named parameter of the given prepared query.
> Objects are serialized, NOT stored as a reference!
> Currently supported object types: Creatures, Items, Placeables, Waypoints, Stores, Doors, Triggers, Encounters, Areas (CAF format)
> If bSaveObjectState is TRUE, local vars, effects, action queue, and transition info (triggers, doors) are saved out
> (except for Combined Area Format, which always has object state saved out).

#### `int SqlStep(sqlquery sqlQuery)`
> Executes the given query and fetches a row; returning true if row data was
> made available; false otherwise. Note that this will return false even if
> the query ran successfully but did not return data.
> You need to call SqlPrepareQuery() and potentially SqlBind* before calling this.
> Example:
> sqlquery n = SqlPrepareQueryObject(GetFirstPC(), "select widget from widgets;");
> while (SqlStep(n))
> SendMessageToPC(GetFirstPC(), "Found widget: " + SqlGetString(n, 0));

#### `int SqlGetInt(sqlquery sqlQuery, int nIndex)`
> Retrieve a column cast as an integer of the currently stepped row.
> You can call this after SqlStep() returned TRUE.
> In case of error, 0 will be returned.
> In traditional fashion, nIndex starts at 0.

#### `float SqlGetFloat(sqlquery sqlQuery, int nIndex)`
> Retrieve a column cast as a float of the currently stepped row.
> You can call this after SqlStep() returned TRUE.
> In case of error, 0.0f will be returned.
> In traditional fashion, nIndex starts at 0.

#### `string SqlGetString(sqlquery sqlQuery, int nIndex)`
> Retrieve a column cast as a string of the currently stepped row.
> You can call this after SqlStep() returned TRUE.
> In case of error, a empty string will be returned.
> In traditional fashion, nIndex starts at 0.

#### `vector SqlGetVector(sqlquery sqlQuery, int nIndex)`
> Retrieve a vector of the currently stepped query.
> You can call this after SqlStep() returned TRUE.
> In case of error, a zero vector will be returned.
> In traditional fashion, nIndex starts at 0.

#### `object SqlGetObject(sqlquery sqlQuery, int nIndex, location lSpawnAt, object oInventory = OBJECT_INVALID, int bLoadObjectState = FALSE)`
> Retrieve a object of the currently stepped query.
> You can call this after SqlStep() returned TRUE.
> The object will be spawned into a inventory if it is a item and the receiver
> has the capability to receive it, otherwise at lSpawnAt.
> Objects are serialized, NOT stored as a reference!
> In case of error, INVALID_OBJECT will be returned.
> In traditional fashion, nIndex starts at 0.
> If bLoadObjectState is TRUE, local vars, effects, action queue, and transition info (triggers, doors) are read in.

#### `object StringToObject(string sHex)`
> Convert sHex, a string containing a hexadecimal object id,
> into a object reference. Counterpart to ObjectToString().

#### `void SetCurrentHitPoints(object oObject, int nHitPoints)`
> Sets the current hitpoints of oObject.
> You cannot destroy or revive objects or creatures with this function.
> For currently dying PCs, you can only set hitpoints in the range of -9 to 0.
> All other objects need to be alive and the range is clamped to 1 and max hitpoints.
> This is not considered damage (or healing). It circumvents all combat logic, including damage resistance and reduction.
> This is not considered a friendly or hostile combat action. It will not affect factions, nor will it trigger script events.
> This will not advise player parties in the combat log.

#### `int GetCurrentlyRunningEvent(int bInheritParent = TRUE)`
> Returns the currently executing event (EVENT_SCRIPT_*) or 0 if not determinable.
> Note: Will return 0 in DelayCommand/AssignCommand.
> bInheritParent: If TRUE, ExecuteScript(Chunk) will inherit their event ID from their parent event.
> If FALSE, it will return the event ID of the current script, which may be 0.
> Some events can run in the same script context as a previous event (for example: CreatureOnDeath, CreatureOnDamaged)
> In cases like these calling the function with bInheritParent = TRUE will return the wrong event ID.

#### `int GetEffectInteger(effect eEffect, int nIndex)`
> Get the integer parameter of eEffect at nIndex.
> nIndex bounds: 0 >= nIndex < 8.
> Some experimentation will be needed to find the right index for the value you wish to determine.
> Returns: the value or 0 on error/when not set.

#### `float GetEffectFloat(effect eEffect, int nIndex)`
> Get the float parameter of eEffect at nIndex.
> nIndex bounds: 0 >= nIndex < 4.
> Some experimentation will be needed to find the right index for the value you wish to determine.
> Returns: the value or 0.0f on error/when not set.

#### `string GetEffectString(effect eEffect, int nIndex)`
> Get the string parameter of eEffect at nIndex.
> nIndex bounds: 0 >= nIndex < 6.
> Some experimentation will be needed to find the right index for the value you wish to determine.
> Returns: the value or "" on error/when not set.

#### `object GetEffectObject(effect eEffect, int nIndex)`
> Get the object parameter of eEffect at nIndex.
> nIndex bounds: 0 >= nIndex < 4.
> Some experimentation will be needed to find the right index for the value you wish to determine.
> Returns: the value or OBJECT_INVALID on error/when not set.

#### `vector GetEffectVector(effect eEffect, int nIndex)`
> Get the vector parameter of eEffect at nIndex.
> nIndex bounds: 0 >= nIndex < 2.
> Some experimentation will be needed to find the right index for the value you wish to determine.
> Returns: the value or {0.0f, 0.0f, 0.0f} on error/when not set.

#### `int GetBaseItemFitsInInventory(int nBaseItemType, object oTarget)`
> Check if nBaseItemType fits in oTarget's inventory.
> Note: Does not check inside any container items possessed by oTarget.
> nBaseItemType: a BASE_ITEM_* constant.
> oTarget: a valid creature, placeable or item.
> Returns: TRUE if the baseitem type fits, FALSE if not or on error.

#### `cassowary GetLocalCassowary(object oObject, string sVarName)`
> Get oObject's local cassowary variable reference sVarName
> Return value on error: empty solver
> NB: cassowary types are references, same as objects.
> Unlike scalars such as int and string, solver references share the same data.
> Modifications made to one reference are reflected on others.

#### `void SetLocalCassowary(object oObject, string sVarName, cassowary cSolver)`
> Set a reference to the given solver on oObject.
> NB: cassowary types are references, same as objects.
> Unlike scalars such as int and string, solver references share the same data.
> Modifications made to one reference are reflected on others.

#### `void DeleteLocalCassowary(object oObject, string sVarName)`
> Delete local solver reference.
> NB: cassowary types are references, same as objects.
> Unlike scalars such as int and string, solver references share the same data.
> Modifications made to one reference are reflected on others.

#### `void CassowaryReset(cassowary cSolver)`
> Clear out this solver, removing all state, constraints and suggestions.
> This is provided as a convenience if you wish to reuse a cassowary variable.
> It is not necessary to call this for solvers you simply want to let go out of scope.

#### `string CassowaryConstrain(cassowary cSolver, string sConstraint, float fStrength = CASSOWARY_STRENGTH_REQUIRED)`
> Add a constraint to the system.
> The constraint needs to be a valid comparison equation, one of: >=, ==, <=.
> This implementation is a linear constraint solver.
> You cannot multiply or divide variables and expressions with each other.
> Doing so will result in a error when attempting to add the constraint.
> (You can, of course, multiply or divide by constants).
> fStrength must be >= CASSOWARY_STRENGTH_WEAK && <= CASSOWARY_STRENGTH_REQUIRED.
> Any referenced variables can be retrieved with CassowaryGetValue().
> Returns "" on success, or the parser/constraint system error message.

#### `void CassowarySuggestValue(cassowary cSolver, string sVarName, float fValue, float fStrength = CASSOWARY_STRENGTH_STRONG)`
> Suggest a value to the solver.
> Edit variables are soft constraints and exist as an optimisation for complex systems.
> You can do the same with Constrain("v == 5", CASSOWARY_STRENGTH_xxx); but edit variables
> allow you to suggest values without having to rebuild the solver.
> fStrength must be >= CASSOWARY_STRENGTH_WEAK && < CASSOWARY_STRENGTH_REQUIRED
> Suggested values cannot be required, as suggesting a value must not invalidate the solver.

#### `float CassowaryGetValue(cassowary cSolver, string sVarName)`
> Get the value for the given variable, or 0.0 on error.

#### `string CassowaryDebug(cassowary cSolver)`
> Gets a printable debug state of the given solver, which may help you debug
> complex systems.

#### `void SetTlkOverride(int nStrRef, string sValue = "")`
> Overrides a given strref to always return sValue instead of what is in the TLK file.
> Setting sValue to "" will delete the override

#### `itemproperty ItemPropertyCustom(int nType, int nSubType = -1, int nCostTableValue = -1, int nParam1Value = -1)`
> Constructs a custom itemproperty given all the parameters explicitly.
> This function can be used in place of all the other ItemPropertyXxx constructors
> Use GetItemProperty{Type,SubType,CostTableValue,Param1Value} to see the values for a given itemproperty.

#### `effect EffectRunScript(string sOnAppliedScript = "", string sOnRemovedScript = "", string sOnIntervalScript = "", float fInterval = 0.0f, string sData = "")`
> Create a RunScript effect.
> Notes: When applied as instant effect, only sOnAppliedScript will fire.
> In the scripts, OBJECT_SELF will be the object the effect is applied to.
> sOnAppliedScript: An optional script to execute when the effect is applied.
> sOnRemovedScript: An optional script to execute when the effect is removed.
> sOnIntervalScript: An optional script to execute every fInterval seconds.
> fInterval: The interval in seconds, must be >0.0f if an interval script is set.
> Very low values may have an adverse effect on performance.
> sData: An optional string of data saved in the effect, retrievable with GetEffectString() at index 0.

#### `effect GetLastRunScriptEffect()`
> Get the effect that last triggered an EffectRunScript() script.
> Note: This can be used to get the creator or tag, among others, of the EffectRunScript() in one of its scripts.
> Returns an effect of type EFFECT_TYPE_INVALIDEFFECT when called outside of an EffectRunScript() script.

#### `int GetLastRunScriptEffectScriptType()`
> Get the script type (RUNSCRIPT_EFFECT_SCRIPT_TYPE_*) of the last triggered EffectRunScript() script.
> Returns 0 when called outside of an EffectRunScript() script.

#### `effect HideEffectIcon(effect eEffect)`
> Hides the effect icon of eEffect and of all effects currently linked to it.

#### `effect EffectIcon(int nIconID)`
> Create an Icon effect.
> nIconID: The effect icon (EFFECT_ICON_*) to display.
> Using the icon for Poison/Disease will also color the health bar green/brown, useful to simulate custom poisons/diseases.
> Returns an effect of type EFFECT_TYPE_INVALIDEFFECT when nIconID is < 1 or > 255.

#### `object GetLastGuiEventPlayer()`
> Gets the player that last triggered the module OnPlayerGuiEvent event.

#### `int GetLastGuiEventType()`
> Gets the last triggered GUIEVENT_* in the module OnPlayerGuiEvent event.

#### `int GetLastGuiEventInteger()`
> Gets an optional integer of specific gui events in the module OnPlayerGuiEvent event.
> GUIEVENT_CHATBAR_*: The selected chat channel. Does not indicate the actual used channel.
> 0 = Shout, 1 = Whisper, 2 = Talk, 3 = Party, 4 = DM
> GUIEVENT_CHARACTERSHEET_SKILL_SELECT: The skill ID.
> GUIEVENT_CHARACTERSHEET_FEAT_SELECT: The feat ID.
> GUIEVENT_EFFECTICON_CLICK: The effect icon ID (EFFECT_ICON_*)
> GUIEVENT_DISABLED_PANEL_ATTEMPT_OPEN: The GUI_PANEL_* the player attempted to open.
> GUIEVENT_QUICKCHAT_SELECT: The hotkey character representing the option
> GUIEVENT_EXAMINE_OBJECT: A GUI_PANEL_EXAMINE_* constant

#### `object GetLastGuiEventObject()`
> Gets an optional object of specific gui events in the module OnPlayerGuiEvent event.
> GUIEVENT_MINIMAP_MAPPIN_CLICK: The waypoint the map note is attached to.
> GUIEVENT_CHARACTERSHEET_*_SELECT: The owner of the character sheet.
> GUIEVENT_PLAYERLIST_PLAYER_CLICK: The player clicked on.
> GUIEVENT_PARTYBAR_PORTRAIT_CLICK: The creature clicked on.
> GUIEVENT_DISABLED_PANEL_ATTEMPT_OPEN: For GUI_PANEL_CHARACTERSHEET, the owner of the character sheet.
> For GUI_PANEL_EXAMINE_*, the object being examined.
> GUIEVENT_*SELECT_CREATURE: The creature that was (un)selected
> GUIEVENT_EXAMINE_OBJECT: The object being examined.
> GUIEVENT_CHATLOG_PORTRAIT_CLICK: The owner of the portrait.
> GUIEVENT_PLAYERLIST_PLAYER_TELL: The selected player.

#### `void SetGuiPanelDisabled(object oPlayer, int nGuiPanel, int bDisabled, object oTarget = OBJECT_INVALID)`
> Disable a gui panel for the client that controls oPlayer.
> Notes: Will close the gui panel if currently open, except GUI_PANEL_LEVELUP / GUI_PANEL_GOLD_*
> Does not persist through relogging or in savegames.
> Will fire a GUIEVENT_DISABLED_PANEL_ATTEMPT_OPEN OnPlayerGuiEvent for some gui panels if a player attempts to open them.
> You can still force show a panel with PopUpGUIPanel().
> You can still force examine an object with ActionExamine().
> nGuiPanel: A GUI_PANEL_* constant, except GUI_PANEL_PLAYER_DEATH.

#### `int GetLastTileActionId()`
> Gets the ID (1..8) of the last tile action performed in OnPlayerTileAction

#### `vector GetLastTileActionPosition()`
> Gets the target position in the module OnPlayerTileAction event.

#### `object GetLastPlayerToDoTileAction()`
> Gets the player object that triggered the OnPlayerTileAction event.

#### `json JsonParse(string sJson)`
> Parse the given string as a valid json value, and returns the corresponding type.
> Returns a JSON_TYPE_NULL on error.
> Check JsonGetError() to see the parse error, if any.
> NB: The parsed string needs to be in game-local encoding, but the generated json structure
> will contain UTF-8 data.

#### `string JsonDump(json jValue, int nIndent = -1)`
> Dump the given json value into a string that can be read back in via JsonParse.
> nIndent describes the indentation level for pretty-printing; a value of -1 means no indentation and no linebreaks.
> Returns a string describing JSON_TYPE_NULL on error.
> NB: The dumped string is in game-local encoding, with all non-ascii characters escaped.

#### `int JsonGetType(json jValue)`
> Describes the type of the given json value.
> Returns JSON_TYPE_NULL if the value is empty.

#### `int JsonGetLength(json jValue)`
> Returns the length of the given json type.
> For objects, returns the number of top-level keys present.
> For arrays, returns the number of elements.
> Null types are of size 0.
> All other types return 1.

#### `string JsonGetError(json jValue)`
> Returns the error message if the value has errored out.
> Currently only describes parse errors.

#### `json JsonNull(string sError = "")`
> Create a NULL json value, seeded with a optional error message for JsonGetError().
> You can say JSON_NULL for default parameters on functions to initialise with a null value.

#### `json JsonObject()`
> Create a empty json object.
> You can say JSON_OBJECT for default parameters on functions to initialise with an empty object.

#### `json JsonArray()`
> Create a empty json array.
> You can say JSON_ARRAY for default parameters on functions to initialise with an empty array.

#### `json JsonString(string sValue)`
> Create a json string value.
> You can say JSON_STRING for default parameters on functions to initialise with a empty string.
> NB: Strings are encoded to UTF-8 from the game-local charset.

#### `json JsonInt(int nValue)`
> Create a json integer value.

#### `json JsonFloat(float fValue)`
> Create a json floating point value.

#### `json JsonBool(int bValue)`
> Create a json bool value.
> You can say JSON_TRUE or JSON_FALSE for default parameters on functions to initialise with a bool.

#### `string JsonGetString(json jValue)`
> Returns a string representation of the json value.
> Returns "" if the value cannot be represented as a string, or is empty.
> NB: Strings are decoded from UTF-8 to the game-local charset.

#### `int JsonGetInt(json jValue)`
> Returns a int representation of the json value, casting where possible.
> Returns 0 if the value cannot be represented as a int.
> Use this to parse json bool types.
> NB: This will narrow down to signed 32 bit, as that is what NWScript int is.
> If you are trying to read a 64 bit or unsigned integer that doesn't fit into int32, you will lose data.
> You will not lose data if you keep the value as a json element (via Object/ArrayGet).

#### `float JsonGetFloat(json jValue)`
> Returns a float representation of the json value, casting where possible.
> Returns 0.0 if the value cannot be represented as a float.
> NB: This will narrow doubles down to float.
> If you are trying to read a double, you will potentially lose precision.
> You will not lose data if you keep the value as a json element (via Object/ArrayGet).

#### `json JsonObjectKeys(json jObject)`
> Returns a json array containing all keys of jObject.
> Returns a empty array if the object is empty or not a json object, with JsonGetError() filled in.

#### `json JsonObjectGet(json jObject, string sKey)`
> Returns the key value of sKey on the object jObect.
> Returns a null json value if jObject is not a object or sKey does not exist on the object, with JsonGetError() filled in.

#### `json JsonObjectSet(json jObject, string sKey, json jValue)`
> Returns a modified copy of jObject with the key at sKey set to jValue.
> Returns a json null value if jObject is not a object, with JsonGetError() filled in.

#### `json JsonObjectDel(json jObject, string sKey)`
> Returns a modified copy of jObject with the key at sKey deleted.
> Returns a json null value if jObject is not a object, with JsonGetError() filled in.

#### `json JsonArrayGet(json jArray, int nIndex)`
> Gets the json object at jArray index position nIndex.
> Returns a json null value if the index is out of bounds, with JsonGetError() filled in.

#### `json JsonArraySet(json jArray, int nIndex, json jValue)`
> Returns a modified copy of jArray with position nIndex set to jValue.
> Returns a json null value if jArray is not actually an array, with JsonGetError() filled in.
> Returns a json null value if nIndex is out of bounds, with JsonGetError() filled in.

#### `json JsonArrayInsert(json jArray, json jValue, int nIndex = -1)`
> Returns a modified copy of jArray with jValue inserted at position nIndex.
> All succeeding objects in the array will move by one.
> By default (-1), inserts objects at the end of the array ("push").
> nIndex = 0 inserts at the beginning of the array.
> Returns a json null value if jArray is not actually an array, with JsonGetError() filled in.
> Returns a json null value if nIndex is not 0 or -1 and out of bounds, with JsonGetError() filled in.

#### `json JsonArrayDel(json jArray, int nIndex)`
> Returns a modified copy of jArray with the element at position nIndex removed,
> and the array resized by one.
> Returns a json null value if jArray is not actually an array, with JsonGetError() filled in.
> Returns a json null value if nIndex is out of bounds, with JsonGetError() filled in.

#### `json ObjectToJson(object oObject, int bSaveObjectState = FALSE)`
> Transforms the given object into a json structure.
> The json format is compatible with what https://github.com/niv/neverwinter.nim@1.4.3+ emits.
> Returns the null json type on errors, or if oObject is not serializable, with JsonGetError() filled in.
> Supported object types: creature, item, trigger, placeable, door, waypoint, encounter, store, area (combined format), soundobject
> If bSaveObjectState is TRUE, local vars, effects, action queue, and transition info (triggers, doors) are saved out
> (except for Combined Area Format, which always has object state saved out).
> N.B.:
> This function is for advanced usecases that require understanding of the game's internals
> and how the engine loads and migrates data as the game is changed to support new features.
> The only guarantee given is that older data files can be loaded on newer game versions.
> As such, fields can become deprecated or change meaning. You need to handle this by
> either constructing a clean-room GFF file, or by writing migration code using the
> game/build version getters.

#### `object JsonToObject(json jObject, location locLocation, object oOwner = OBJECT_INVALID, int bLoadObjectState = FALSE)`
> Deserializes the game object described in jObject.
> Returns OBJECT_INVALID on errors.
> Supported object types: creature, item, trigger, placeable, door, waypoint, encounter, store, area (combined format), soundobject
> For areas, locLocation is ignored.
> If bLoadObjectState is TRUE, local vars, effects, action queue, and transition info (triggers, doors) are read in.
> N.B.:
> This function is for advanced usecases that require understanding of the game's internals
> and how the engine loads and migrates data as the game is changed to support new features.
> The only guarantee given is that older data files can be loaded on newer game versions.
> As such, fields can become deprecated or change meaning. You need to handle this by
> either constructing a clean-room GFF file, or by writing migration code using the
> game/build version getters.

#### `json JsonPointer(json jData, string sPointer)`
> Returns the element at the given JSON pointer value.
> For example, given the JSON document:
> "foo": ["bar", "baz"],
> "a/b": 1,
> "c%d": 2,
> "e^f": 3,
> "g|h": 4,
> "m~n": 8
> The following JSON strings evaluate to the accompanying values:
> ""           // the whole document
> "/foo"       ["bar", "baz"]
> "/foo/0"     "bar"
> "/a~1b"      1
> "/c%d"       2
> "/e^f"       3
> "/g|h"       4
> "/i\\j"      5
> "/k\"l"      6
> "/m~0n"      8
> See https://datatracker.ietf.org/doc/html/rfc6901 for more details.
> Returns a json null value on error, with JsonGetError() filled in.

#### `json JsonPatch(json jData, json jPatch)`
> Return a modified copy of jData with jPatch applied, according to the rules described below.
> See JsonPointer() for documentation on the pointer syntax.
> Returns a json null value on error, with JsonGetError() filled in.
> jPatch is an array of patch elements, each containing a op, a path, and a value field. Example:
> { "op": "replace", "path": "/baz", "value": "boo" },
> { "op": "add", "path": "/hello", "value": ["world"] },
> { "op": "remove", "path": "/foo"}
> Valid operations are: add, remove, replace, move, copy, test
> See https://datatracker.ietf.org/doc/html/rfc7386 for more details on the patch rules.

#### `json JsonDiff(json jLHS, json jRHS)`
> Returns the diff (described as a json structure you can pass into JsonPatch) between the two objects.
> Returns a json null value on error, with JsonGetError() filled in.

#### `json JsonMerge(json jData, json jMerge)`
> Returns a modified copy of jData with jMerge merged into it. This is an alternative to
> JsonPatch/JsonDiff, with a syntax more closely resembling the final object.
> See https://datatracker.ietf.org/doc/html/rfc7386 for details.
> Returns a json null value on error, with JsonGetError() filled in.

#### `json GetLocalJson(object oObject, string sVarName)`
> Get oObject's local json variable sVarName
> Return value on error: json null type

#### `void SetLocalJson(object oObject, string sVarName, json jValue)`
> Set oObject's local json variable sVarName to jValue

#### `void DeleteLocalJson(object oObject, string sVarName)`
> Delete oObject's local json variable sVarName

#### `void SqlBindJson(sqlquery sqlQuery, string sParam, json jValue)`
> Bind an json to a named parameter of the given prepared query.
> Json values are serialised into a string.
> Example:
> sqlquery v = SqlPrepareQueryObject(GetModule(), "insert into test (col) values (@myjson);");
> SqlBindJson(v, "@myjson", myJsonObject);
> SqlStep(v);

#### `json SqlGetJson(sqlquery sqlQuery, int nIndex)`
> Retrieve a column cast as a json value of the currently stepped row.
> You can call this after SqlStep() returned TRUE.
> In case of error, a json null value will be returned.
> In traditional fashion, nIndex starts at 0.

#### `void SetCampaignJson(string sCampaignName, string sVarName, json jValue, object oPlayer = OBJECT_INVALID)`
> This stores a json out to the specified campaign database
> The database name:
> - is case insensitive and it must be the same for both set and get functions.
> - can only contain alphanumeric characters, no spaces.
> The var name must be unique across the entire database, regardless of the variable type.
> If you want a variable to pertain to a specific player in the game, provide a player object.

#### `json GetCampaignJson(string sCampaignName, string sVarName, object oPlayer = OBJECT_INVALID)`
> This will read a json from the  specified campaign database
> The database name:
> - is case insensitive and it must be the same for both set and get functions.
> - can only contain alphanumeric characters, no spaces.
> The var name must be unique across the entire database, regardless of the variable type.
> If you want a variable to pertain to a specific player in the game, provide a player object.

#### `int GetPlayerDeviceProperty(object oPlayer, string sProperty)`
> Gets a device property/capability as advertised by the client.
> sProperty is one of PLAYER_DEVICE_PROPERTY_xxx.
> Returns -1 if
> - the property was never set by the client,
> - the the actual value is -1,
> - the player is running a older build that does not advertise device properties,
> - the player has disabled sending device properties (Options->Game->Privacy).

#### `int GetPlayerLanguage(object oPlayer)`
> Returns the LANGUAGE_xx code of the given player, or -1 if unavailable.

#### `int GetPlayerDevicePlatform(object oPlayer)`
> Returns one of PLAYER_DEVICE_PLATFORM_xxx, or 0 if unavailable.

#### `json TemplateToJson(string sResRef, int nResType)`
> Deserializes the given resref/template into a JSON structure.
> Supported GFF resource types:
> RESTYPE_CAF (and RESTYPE_ARE, RESTYPE_GIT, RESTYPE_GIC)
> RESTYPE_UTC
> RESTYPE_UTI
> RESTYPE_UTT
> RESTYPE_UTP
> RESTYPE_UTD
> RESTYPE_UTW
> RESTYPE_UTE
> RESTYPE_UTM
> RESTYPE_DLG
> RESTYPE_UTS
> RESTYPE_IFO
> RESTYPE_FAC
> RESTYPE_ITP
> RESTYPE_GUI
> RESTYPE_GFF
> Returns a valid gff-type json structure, or a null value with JsonGetError() set.

#### `string ResManGetAliasFor(string sResRef, int nResType)`
> Returns the resource location of sResRef.nResType, as seen by the running module.
> Note for dedicated servers: Checks on the module/server side, not the client.
> Returns "" if the resource does not exist in the search space.

#### `string ResManFindPrefix(string sPrefix, int nResType, int nNth = 1, int bSearchBaseData = FALSE, string sOnlyKeyTable = "")`
> Finds the nNth available resref starting with sPrefix.
> Set bSearchBaseData to TRUE to also search base game content stored in your game installation directory.
> WARNING: This can be very slow.
> Set sOnlyKeyTable to a specific keytable to only search the given named keytable (e.g. "OVERRIDE:").
> Returns "" if no such resref exists.

#### `int NuiCreateFromResRef(object oPlayer, string sResRef, string sWindowId = "", string sEventScript = "")`
> Create a NUI window from the given resref(.jui) for the given player.
> The resref needs to be available on the client, not the server.
> The token is a integer for ease of handling only. You are not supposed to do anything with it, except store/pass it.
> The window ID needs to be alphanumeric and short. Only one window (per client) with the same ID can exist at a time.
> Re-creating a window with the same id of one already open will immediately close the old one.
> sEventScript is optional and overrides the NUI module event for this window only.
> See nw_inc_nui.nss for full documentation.
> Returns the window token on success (>0), or 0 on error.

#### `int NuiCreate(object oPlayer, json jNui, string sWindowId = "", string sEventScript = "")`
> Create a NUI window inline for the given player.
> The token is a integer for ease of handling only. You are not supposed to do anything with it, except store/pass it.
> The window ID needs to be alphanumeric and short. Only one window (per client) with the same ID can exist at a time.
> Re-creating a window with the same id of one already open will immediately close the old one.
> sEventScript is optional and overrides the NUI module event for this window only.
> See nw_inc_nui.nss for full documentation.
> Returns the window token on success (>0), or 0 on error.

#### `int NuiFindWindow(object oPlayer, string sId)`
> You can look up windows by ID, if you gave them one.
> Windows with a ID present are singletons - attempting to open a second one with the same ID
> will fail, even if the json definition is different.
> Returns the token if found, or 0.

#### `void NuiDestroy(object oPlayer, int nUiToken)`
> Destroys the given window, by token, immediately closing it on the client.
> Does nothing if nUiToken does not exist on the client.
> Does not send a close event - this immediately destroys all serverside state.
> The client will close the window asynchronously.

#### `object NuiGetEventPlayer()`
> Returns the originating player of the current event.

#### `int NuiGetEventWindow()`
> Gets the window token of the current event (or 0 if not in a event).

#### `string NuiGetEventType()`
> Returns the event type of the current event.
> See nw_inc_nui.nss for full documentation of all events.

#### `string NuiGetEventElement()`
> Returns the ID of the widget that triggered the event.

#### `int NuiGetEventArrayIndex()`
> Get the array index of the current event.
> This can be used to get the index into an array, for example when rendering lists of buttons.
> Returns -1 if the event is not originating from within an array.

#### `string NuiGetWindowId(object oPlayer, int nUiToken)`
> Returns the window ID of the window described by nUiToken.
> Returns "" on error, or if the window has no ID.

#### `json NuiGetBind(object oPlayer, int nUiToken, string sBindName)`
> Gets the json value for the given player, token and bind.
> json values can hold all kinds of values; but NUI widgets require specific bind types.
> It is up to you to either handle this in NWScript, or just set compatible bind types.
> No auto-conversion happens.
> Returns a json null value if the bind does not exist.

#### `void NuiSetBind(object oPlayer, int nUiToken, string sBindName, json jValue)`
> Sets a json value for the given player, token and bind.
> The value is synced down to the client and can be used in UI binding.
> When the UI changes the value, it is returned to the server and can be retrieved via NuiGetBind().
> json values can hold all kinds of values; but NUI widgets require specific bind types.
> It is up to you to either handle this in NWScript, or just set compatible bind types.
> No auto-conversion happens.
> If the bind is on the watch list, this will immediately invoke the event handler with the "watch"
> even type; even before this function returns. Do not update watched binds from within the watch handler
> unless you enjoy stack overflows.
> Does nothing if the given player+token is invalid.

#### `void NuiSetGroupLayout(object oPlayer, int nUiToken, string sElement, json jNui)`
> Swaps out the given element (by id) with the given nui layout (partial).
> This currently only works with the "group" element type, and the special "_window_" root group.

#### `int NuiSetBindWatch(object oPlayer, int nUiToken, string sBind, int bWatch)`
> Mark the given bind name as watched.
> A watched bind will invoke the NUI script event every time it's value changes.
> Be careful with binding nui data inside a watch event handler: It's easy to accidentally recurse yourself into a stack overflow.

#### `int NuiGetNthWindow(object oPlayer, int nNth = 0)`
> Returns the nNth window token of the player, or 0.
> nNth starts at 0.
> Iterator is not write-safe: Calling DestroyWindow() will invalidate move following offsets by one.

#### `string NuiGetNthBind(object oPlayer, int nToken, int bWatched, int nNth = 0)`
> Return the nNth bind name of the given window, or "".
> If bWatched is TRUE, iterates only watched binds.
> If FALSE, iterates all known binds on the window (either set locally or in UI).

#### `json NuiGetEventPayload()`
> Returns the event payload, specific to the event.
> Returns JsonNull if event has no payload.

#### `json NuiGetUserData(object oPlayer, int nToken)`
> Get the userdata of the given window token.
> Returns JsonNull if the window does not exist on the given player, or has no userdata set.

#### `void NuiSetUserData(object oPlayer, int nToken, json jUserData)`
> Sets an arbitrary json value as userdata on the given window token.
> This userdata is not read or handled by the game engine and not sent to clients.
> This mechanism only exists as a convenience for the programmer to store data bound to a windows' lifecycle.
> Will do nothing if the window does not exist.

#### `int GetScriptInstructionsRemaining()`
> Returns the number of script instructions remaining for the currently-running script.
> Once this value hits zero, the script will abort with TOO MANY INSTRUCTIONS.
> The instruction limit is configurable by the user, so if you have a really long-running
> process, this value can guide you with splitting it up into smaller, discretely schedulable parts.
> Note: Running this command and checking/handling the value also takes up some instructions.

#### `json JsonArrayTransform(json jArray, int nTransform)`
> Returns a modified copy of jArray with the value order changed according to nTransform:
> JSON_ARRAY_SORT_ASCENDING, JSON_ARRAY_SORT_DESCENDING
> Sorting is dependent on the type and follows json standards (.e.g. 99 < "100").
> JSON_ARRAY_SHUFFLE
> Randomises the order of elements.
> JSON_ARRAY_REVERSE
> Reverses the array.
> JSON_ARRAY_UNIQUE
> Returns a modified copy of jArray with duplicate values removed.
> Coercable but different types are not considered equal (e.g. 99 != "99"); int/float equivalence however applies: 4.0 == 4.
> Order is preserved.
> JSON_ARRAY_COALESCE
> Returns the first non-null entry. Empty-ish values (e.g. "", 0) are not considered null, only the json scalar type.

#### `json JsonFind(json jHaystack, json jNeedle, int nNth = 0, int nConditional = JSON_FIND_EQUAL)`
> Returns the nth-matching index or key of jNeedle in jHaystack.
> Supported haystacks: object, array
> Ordering behaviour for objects is unspecified.
> Return null when not found or on any error.

#### `json JsonArrayGetRange(json jArray, int nBeginIndex, int nEndIndex)`
> Returns a copy of the range (nBeginIndex, nEndIndex) inclusive of jArray.
> Negative nEndIndex values count from the other end.
> Out-of-bound values are clamped to the array range.
> Examples:
> json a = JsonParse("[0, 1, 2, 3, 4]");
> JsonArrayGetRange(a, 0, 1)    // => [0, 1]
> JsonArrayGetRange(a, 1, -1)   // => [1, 2, 3, 4]
> JsonArrayGetRange(a, 0, 4)    // => [0, 1, 2, 3, 4]
> JsonArrayGetRange(a, 0, 999)  // => [0, 1, 2, 3, 4]
> JsonArrayGetRange(a, 1, 0)    // => []
> JsonArrayGetRange(a, 1, 1)    // => [1]
> Returns a null type on error, including type mismatches.

#### `json JsonSetOp(json jValue, int nOp, json jOther)`
> Returns the result of a set operation on two arrays.
> Operations:
> JSON_SET_SUBSET (v <= o):
> Returns true if every element in jValue is also in jOther.
> JSON_SET_UNION (v | o):
> Returns a new array containing values from both sides.
> JSON_SET_INTERSECT (v & o):
> Returns a new array containing only values common to both sides.
> JSON_SET_DIFFERENCE (v - o):
> Returns a new array containing only values not in jOther.
> JSON_SET_SYMMETRIC_DIFFERENCE (v ^ o):
> Returns a new array containing all elements present in either array, but not both.

#### `string Get2DAColumn(string s2DA, int nColumnIdx)`
> Returns the column name of s2DA at nColumn index (starting at 0).
> Returns "" if column nColumn doesn't exist (at end).

#### `int Get2DARowCount(string s2DA)`
> Returns the number of defined rows in the 2da s2DA.

#### `effect UnyieldingEffect(effect eEffect)`
> Set the subtype of eEffect to Unyielding and return eEffect.
> (Effects default to magical if the subtype is not set)
> Unyielding effects are not removed by resting, death or dispel magic, only by RemoveEffect().
> Note: effects that modify state, Stunned/Knockdown/Deaf etc, WILL be removed on death.

#### `effect IgnoreEffectImmunity(effect eEffect)`
> Set eEffect to ignore immunities and return eEffect.

#### `void SetShaderUniformFloat(object oPlayer, int nShader, float fValue)`
> Sets the global shader uniform for the player to the specified float.
> These uniforms are not used by the base game and are reserved for module-specific scripting.
> You need to add custom shaders that will make use of them.
> In multiplayer, these need to be reapplied when a player rejoins.
> - nShader: SHADER_UNIFORM_*

#### `void SetShaderUniformInt(object oPlayer, int nShader, int nValue)`
> Sets the global shader uniform for the player to the specified integer.
> These uniforms are not used by the base game and are reserved for module-specific scripting.
> You need to add custom shaders that will make use of them.
> In multiplayer, these need to be reapplied when a player rejoins.
> - nShader: SHADER_UNIFORM_*

#### `void SetShaderUniformVec(object oPlayer, int nShader, float fX, float fY, float fZ, float fW)`
> Sets the global shader uniform for the player to the specified vec4.
> These uniforms are not used by the base game and are reserved for module-specific scripting.
> You need to add custom shaders that will make use of them.
> In multiplayer, these need to be reapplied when a player rejoins.
> - nShader: SHADER_UNIFORM_*

#### `void SetSpellTargetingData(object oPlayer, int nSpell, int nShape, float fSizeX, float fSizeY, int nFlags)`
> Sets the spell targeting data manually for the player. This data is usually specified in spells.2da.
> This data persists through spell casts; you're overwriting the entry in spells.2da for this session.
> In multiplayer, these need to be reapplied when a player rejoins.
> - nSpell: SPELL_*
> - nShape: SPELL_TARGETING_SHAPE_*
> - nFlags: SPELL_TARGETING_FLAGS_*

#### `void SetEnterTargetingModeData(object oPlayer, int nShape, float fSizeX, float fSizeY, int nFlags, float fRange = 0.0f, int nSpell = -1, int nFeat = -1)`
> Sets the spell targeting data which is used for the next call to EnterTargetingMode() for this player.
> If the shape is set to SPELL_TARGETING_SHAPE_NONE and the range is provided, the dotted line range indicator will still appear.
> - nShape: SPELL_TARGETING_SHAPE_*
> - nFlags: SPELL_TARGETING_FLAGS_*
> - nSpell: SPELL_* (optional, passed to the shader but does nothing by default, you need to edit the shader to use it)
> - nFeat: FEAT_* (optional, passed to the shader but does nothing by default, you need to edit the shader to use it)

#### `int GetMemorizedSpellCountByLevel(object oCreature, int nClassType, int nSpellLevel)`
> Gets the number of memorized spell slots for a given spell level.
> - nClassType: a CLASS_TYPE_* constant. Must be a MemorizesSpells class.
> - nSpellLevel: the spell level, 0-9.
> Returns: the number of spell slots.

#### `int GetMemorizedSpellId(object oCreature, int nClassType, int nSpellLevel, int nIndex)`
> Gets the spell id of a memorized spell slot.
> - nClassType: a CLASS_TYPE_* constant. Must be a MemorizesSpells class.
> - nSpellLevel: the spell level, 0-9.
> - nIndex: the index of the spell slot. Bounds: 0 <= nIndex < GetMemorizedSpellCountByLevel()
> Returns: a SPELL_* constant or -1 if the slot is not set.

#### `int GetMemorizedSpellReady(object oCreature, int nClassType, int nSpellLevel, int nIndex)`
> Gets the ready state of a memorized spell slot.
> - nClassType: a CLASS_TYPE_* constant. Must be a MemorizesSpells class.
> - nSpellLevel: the spell level, 0-9.
> - nIndex: the index of the spell slot. Bounds: 0 <= nIndex < GetMemorizedSpellCountByLevel()
> Returns: TRUE/FALSE or -1 if the slot is not set.

#### `int GetMemorizedSpellMetaMagic(object oCreature, int nClassType, int nSpellLevel, int nIndex)`
> Gets the metamagic of a memorized spell slot.
> - nClassType: a CLASS_TYPE_* constant. Must be a MemorizesSpells class.
> - nSpellLevel: the spell level, 0-9.
> - nIndex: the index of the spell slot. Bounds: 0 <= nIndex < GetMemorizedSpellCountByLevel()
> Returns: a METAMAGIC_* constant or -1 if the slot is not set.

#### `int GetMemorizedSpellIsDomainSpell(object oCreature, int nClassType, int nSpellLevel, int nIndex)`
> Gets if the memorized spell slot has a domain spell.
> - nClassType: a CLASS_TYPE_* constant. Must be a MemorizesSpells class.
> - nSpellLevel: the spell level, 0-9.
> - nIndex: the index of the spell slot. Bounds: 0 <= nIndex < GetMemorizedSpellCountByLevel()
> Returns: TRUE/FALSE or -1 if the slot is not set.

#### `void SetMemorizedSpell(object oCreature, int nClassType, int nSpellLevel, int nIndex, int nSpellId, int bReady = TRUE, int nMetaMagic = METAMAGIC_NONE, int bIsDomainSpell = FALSE)`
> Set a memorized spell slot.
> - nClassType: a CLASS_TYPE_* constant. Must be a MemorizesSpells class.
> - nSpellLevel: the spell level, 0-9.
> - nIndex: the index of the spell slot. Bounds: 0 <= nIndex < GetMemorizedSpellCountByLevel()
> - nSpellId: a SPELL_* constant.
> - bReady: TRUE to mark the slot ready.
> - nMetaMagic: a METAMAGIC_* constant.
> - bIsDomainSpell: TRUE for a domain spell.

#### `void SetMemorizedSpellReady(object oCreature, int nClassType, int nSpellLevel, int nIndex, int bReady)`
> Set the ready state of a memorized spell slot.
> - nClassType: a CLASS_TYPE_* constant. Must be a MemorizesSpells class.
> - nSpellLevel: the spell level, 0-9.
> - nIndex: the index of the spell slot. Bounds: 0 <= nIndex < GetMemorizedSpellCountByLevel()
> - bReady: TRUE to mark the slot ready.

#### `void ClearMemorizedSpell(object oCreature, int nClassType, int nSpellLevel, int nIndex)`
> Clear a specific memorized spell slot.
> - nClassType: a CLASS_TYPE_* constant. Must be a MemorizesSpells class.
> - nSpellLevel: the spell level, 0-9.
> - nIndex: the index of the spell slot. Bounds: 0 <= nIndex < GetMemorizedSpellCountByLevel()

#### `void ClearMemorizedSpellBySpellId(object oCreature, int nClassType, int nSpellId)`
> Clear all memorized spell slots of a specific spell id, including metamagic'd ones.
> - nClassType: a CLASS_TYPE_* constant. Must be a MemorizesSpells class.
> - nSpellId: a SPELL_* constant.

#### `int GetKnownSpellCount(object oCreature, int nClassType, int nSpellLevel)`
> Gets the number of known spells for a given spell level.
> - nClassType: a CLASS_TYPE_* constant. Must be a SpellBookRestricted class.
> - nSpellLevel: the spell level, 0-9.
> Returns: the number of known spells.

#### `int GetKnownSpellId(object oCreature, int nClassType, int nSpellLevel, int nIndex)`
> Gets the spell id of a known spell.
> - nClassType: a CLASS_TYPE_* constant. Must be a SpellBookRestricted class.
> - nSpellLevel: the spell level, 0-9.
> - nIndex: the index of the known spell. Bounds: 0 <= nIndex < GetKnownSpellCount()
> Returns: a SPELL_* constant or -1 on error.

#### `int GetIsInKnownSpellList(object oCreature, int nClassType, int nSpellId)`
> Gets if a spell is in the known spell list.
> - nClassType: a CLASS_TYPE_* constant. Must be a SpellBookRestricted class.
> - nSpellId: a SPELL_* constant.
> Returns: TRUE if the spell is in the known spell list.

#### `int GetSpellUsesLeft(object oCreature, int nClassType, int nSpellId, int nMetaMagic = METAMAGIC_NONE, int nDomainLevel = 0)`
> Gets the amount of uses a spell has left.
> - nClassType: a CLASS_TYPE_* constant.
> - nSpellid: a SPELL_* constant.
> - nMetaMagic: a METAMAGIC_* constant.
> - nDomainLevel: the domain level, if a domain spell.
> Returns: the amount of spell uses left.

#### `int GetSpellLevelByClass(int nClassType, int nSpellId)`
> Gets the spell level at which a class gets a spell.
> - nClassType: a CLASS_TYPE_* constant.
> - nSpellId: a SPELL_* constant.
> Returns: the spell level or -1 if the class does not get the spell.

#### `void ReplaceObjectAnimation(object oObject, string sOld, string sNew = "")`
> Replaces oObject's animation sOld with sNew.
> Specifying sNew = "" will restore the original animation.

#### `void SetObjectVisibleDistance(object oObject, float fDistance = 45.0f)`
> Sets the distance (in meters) at which oObject info will be sent to clients (default 45.0)
> This is still subject to other limitations, such as perception ranges for creatures
> Note: Increasing visibility ranges of many objects can have a severe negative effect on
> network latency and server performance, and rendering additional objects will
> impact graphics performance of clients. Use cautiously.

#### `float GetObjectVisibleDistance(object oObject)`
> Gets oObject's visible distance, as set by SetObjectVisibleDistance()
> Returns -1.0f on error

#### `void SetGameActivePause(int bState)`
> Sets the active game pause state - same as if the player requested pause.

#### `int GetGamePauseState()`
> Returns >0 if the game is currently paused:
> - 0: Game is not paused.
> - 1: Timestop
> - 2: Active Player Pause (optionally on top of timestop)

#### `void SetGender(object oCreature, int nGender)`
> Set the gender of oCreature.
> - nGender: a GENDER_* constant.

#### `int GetSoundset(object oCreature)`
> Get the soundset of oCreature.
> Returns -1 on error.

#### `void SetSoundset(object oCreature, int nSoundset)`
> Set the soundset of oCreature, see soundset.2da for possible values.

#### `void ReadySpellLevel(object oCreature, int nSpellLevel, int nClassType = CLASS_TYPE_INVALID, int nSlotsToReady = 255)`
> Ready a spell level for oCreature.
> - nSpellLevel: 0-9
> - nClassType: a CLASS_TYPE_* constant or CLASS_TYPE_INVALID to ready the spell level for all classes.
> - nSlotsToReady: The amount of spells to set to ready at the given spell level. 0 will clear all uses, negative numbers will
> reduce the amount, positive increase the amount.

#### `void SetCommandingPlayer(object oCreature, object oPlayer)`
> Makes oCreature controllable by oPlayer, if player party control is enabled
> Setting oPlayer=OBJECT_INVALID removes the override and reverts to regular party control behavior
> NB: A creature is only controllable by one player, so if you set oPlayer to a non-Player object
> (e.g. the module) it will disable regular party control for this creature

#### `void SetCameraLimits(object oPlayer, float fMinPitch = -1.0, float fMaxPitch = -1.0, float fMinDist = -1.0, float fMaxDist = -1.0)`
> Sets oPlayer's camera limits that override any client configuration limits
> Value of -1.0 means use the client config instead
> NB: Like all other camera settings, this is not saved when saving the game

#### `json RegExpMatch(string sRegExp, string sValue, int nSyntaxFlags = REGEXP_ECMASCRIPT, int nMatchFlags = REGEXP_FORMAT_DEFAULT)`
> Applies sRegExp on sValue, returning an array containing all matching groups.
> The regexp is not bounded by default (so /t/ will match "test").
> A matching result with always return a JSON_ARRAY with the full match as the first element.
> All matching groups will be returned as additional elements, depth-first.
> A non-matching result will return a empty JSON_ARRAY.
> If there was an error, the function will return JSON_NULL, with a error string filled in.
> nSyntaxFlags is a mask of REGEXP_*
> nMatchFlags is a mask of REGEXP_MATCH_* and REGEXP_FORMAT_*.
> Examples:
> RegExpMatch("[", "test value")             -> null (error: "The expression contained mismatched [ and ].")
> RegExpMatch("nothing", "test value")       -> []
> RegExpMatch("^test", "test value")         -> ["test"]
> RegExpMatch("^(test) (.+)$", "test value") -> ["test value", "test", "value"]

#### `json RegExpIterate(string sRegExp, string sValue, int nSyntaxFlags = REGEXP_ECMASCRIPT, int nMatchFlags = REGEXP_FORMAT_DEFAULT)`
> Iterates sValue with sRegExp.
> Returns an array of arrays; where each sub-array contains first the full match and then all matched groups.
> Returns empty JSON_ARRAY if no matches are found.
> If there was an error, the function will return JSON_NULL, with a error string filled in.
> nSyntaxFlags is a mask of REGEXP_*
> nMatchFlags is a mask of REGEXP_MATCH_* and REGEXP_FORMAT_*.
> Example: RegExpIterate("(\\d)(\\S+)", "1i 2am 3 4asentence"); -> [["1i", "1", "i"], ["2am", "2", "am"], ["4sentence", "4", "sentence"]]

#### `string RegExpReplace(string sRegExp, string sValue, string sReplacement, int nSyntaxFlags = REGEXP_ECMASCRIPT, int nMatchFlags = REGEXP_FORMAT_DEFAULT)`
> Replaces all matching sRegExp in sValue with sReplacement.
> Returns a empty string on error.
> Please see the format documentation for replacement patterns.
> nSyntaxFlags is a mask of REGEXP_*
> nMatchFlags is a mask of REGEXP_MATCH_* and REGEXP_FORMAT_*.
> FORMAT_DEFAULT replacement patterns:
> $&    The matched substring.
> $`    The portion of string that precedes the matched substring.
> $'    The portion of string that follows the matched substring.
> $n    The nth capture, where n is a single digit in the range 1 to 9 and $n is not followed by a decimal digit.
> $nn   The nnth capture, where nn is a two-digit decimal number in the range 01 to 99.
> Example: RegExpReplace("a+", "vaaalue", "[$&]")    => "v[aaa]lue"

#### `string ResManGetFileContents(string sResRef, int nResType, int nFormat = RESMAN_FILE_CONTENTS_FORMAT_RAW)`
> Get the contents of a file as string, as seen by the server's resman.
> Note: If the output contains binary data it will only return data up to the first null byte.
> - nResType: a RESTYPE_* constant.
> - nFormat: one of RESMAN_FILE_CONTENTS_FORMAT_*
> Returns "" if the file does not exist.

#### `string CompileScript(string sScriptName, string sScriptData, int bWrapIntoMain = FALSE, int bGenerateNDB = FALSE)`
> Compile a script and place it in the server's CURRENTGAME: folder.
> Note: Scripts will persist for as long as the module is running.
> SinglePlayer / Saves: Scripts that overwrite existing module scripts will persist to the save file.
> New scripts, unknown to the module, will have to be re-compiled on module load when loading a save.
> Returns "" on success or the error on failure.

#### `void AttachCamera(object oPlayer, object oTarget, int bFindClearView = FALSE)`
> Sets the object oPlayer's camera will be attached to.
> - oTarget: A valid creature or placeable. If oTarget is OBJECT_INVALID, it will revert the camera back to oPlayer's character.
> The target must be known to oPlayer's client, this means it must be in the same area and within visible distance.
> - SetObjectVisibleDistance() can be used to increase this range.
> - If the target is a creature, it also must be within the perception range of oPlayer and perceived.
> - bFindClearView: if TRUE, the client will attempt to find a camera position where oTarget is in view.
> Notes:
> - If oTarget gets destroyed while oPlayer's camera is attached to it, the camera will revert back to oPlayer's character.
> - If oPlayer goes through a transition with its camera attached to a different object, it will revert back to oPlayer's character.
> - The object the player's camera is attached to is not saved when saving the game.

#### `int GetObjectUiDiscoveryMask(object oObject)`
> Get the current discoverability mask of oObject.
> Returns -1 if oObject cannot have a discovery mask.

#### `void SetObjectUiDiscoveryMask(object oObject, int nMask = OBJECT_UI_DISCOVERY_DEFAULT)`
> Sets the discoverability mask on oObject.
> This allows toggling areahilite (TAB key by default) and mouseover discovery in the area view.
> nMask is a bitmask of OBJECT_UI_DISCOVERY_*
> Will currently only work on Creatures, Doors (Hilite only), Items and Useable Placeables.
> Does not affect inventory items.

#### `void SetObjectTextBubbleOverride(object oObject, int nMode, string sText)`
> Sets a text override for the mouseover/tab-highlight text bubble of oObject.
> Will currently only work on Creatures, Items and Useable Placeables.
> nMode is one of OBJECT_UI_TEXT_BUBBLE_OVERRIDE_*.

#### `int ClearObjectVisualTransform(object oObject, int nScope = -1)`
> Immediately unsets a VTs for the given object, with no lerp.
> nScope: one of OBJECT_VISUAL_TRANSFORM_DATA_SCOPE_, or -1 for all scopes
> Returns TRUE only if transforms were successfully removed (valid object, transforms existed).

#### `vector GetLastGuiEventVector()`
> Gets an optional vecror of specific gui events in the module OnPlayerGuiEvent event.
> GUIEVENT_RADIAL_OPEN - World vector position of radial if on tile.

#### `void SetCameraFlags(object oPlayer, int nFlags = 0)`
> Sets oPlayer's camera settings that override any client configuration settings
> nFlags is a bitmask of CAMERA_FLAG_* constants;
> NB: Like all other camera settings, this is not saved when saving the game

#### `int GetAreaLightColor(int nColorType, object oArea = OBJECT_INVALID)`
> Gets the light color in the area specified.
> nColorType specifies the color type returned.
> Valid values for nColorType are the AREA_LIGHT_COLOR_* values.
> If no valid area (or object) is specified, it uses the area of caller.
> If an object other than an area is specified, will use the area that the object is currently in.

#### `void SetAreaLightColor(int nColorType, int nColor, object oArea = OBJECT_INVALID, float fFadeTime = 0.0)`
> Sets the light color in the area specified.
> nColorType = AREA_LIGHT_COLOR_* specifies the color type.
> nColor = FOG_COLOR_* specifies the color the fog is being set to.
> The color can also be represented as a hex RGB number if specific color shades
> are desired.
> The format of a hex specified color would be 0xFFEEDD where
> FF would represent the amount of red in the color
> EE would represent the amount of green in the color
> DD would represent the amount of blue in the color.
> If no valid area (or object) is specified, it uses the area of caller.
> If an object other than an area is specified, will use the area that the object is currently in.
> If fFadeTime is above 0.0, it will fade to the new color in the amount of seconds specified.

#### `vector GetAreaLightDirection(int nLightType, object oArea = OBJECT_INVALID)`
> Gets the light direction of origin in the area specified.
> nLightType specifies whether the Moon or Sun light direction is returned.
> Valid values for nColorType are the AREA_LIGHT_DIRECTION_* values.
> If no valid area (or object) is specified, it uses the area of caller.
> If an object other than an area is specified, will use the area that the object is currently in.

#### `void SetAreaLightDirection(int nLightType, vector vDirection, object oArea = OBJECT_INVALID, float fFadeTime = 0.0)`
> Sets the light direction of origin in the area specified.
> nLightType = AREA_LIGHT_DIRECTION_* specifies the light type.
> vDirection = specifies the direction of origin of the light type, i.e. the direction the sun/moon is in from the area.
> If no valid area (or object) is specified, it uses the area of caller.
> If an object other than an area is specified, will use the area that the object is currently in.
> If fFadeTime is above 0.0, it will fade to the new color in the amount of seconds specified.

#### `void AbortRunningScript(string sError = "")`
> This immediately aborts the running script.
> - Will not emit an error to the server log by default.
> - You can specify the optional sError to emit as a script error, which will be printed
> to the log and sent to all players, just like any other script error.
> - Will not terminate other script recursion (e.g. nested ExecuteScript()) will resume as if the
> called script exited cleanly.
> - This call will never return.

#### `json GetScriptBacktrace(int bIncludeStack = TRUE)`
> Generate a VM debug view into the current execution location.
> - Names and symbols can only be resolved if debug information is available (NDB file).
> - This call can be a slow call for large scripts.
> - Setting bIncludeStack = TRUE will include stack info in the output, which could be a
> lot of data for large scripts. You can turn it off if you do not need the info.
> Returned data format (JSON object):
> "frames": array of stack frames:
> "ip": instruction pointer into code
> "bp", "sp": current base/stack pointer
> "file", "line", "function": available only if NDB loaded correctly
> "stack": abbreviated stack data (only if bIncludeStack is TRUE)
> "type": one of the nwscript object types, OR:
> "type_unknown": hex code of AUX
> "data": type-specific payload. Not all type info is rendered in the interest of brevity.
> Only enough for you to re-identify which variable this might belong to.

#### `int SetJmp(string sLabel)`
> Mark the current location in code as a jump target, identified by sLabel.
> - Returns 0 on initial invocation, but will return nRetVal if jumped-to by LongJmp.
> - sLabel can be any valid string (including empty); though it is recommended to pick
> something distinct. The responsibility of namespacing lies with you.
> - Calling repeatedly with the same label will overwrite the previous jump location.
> If you want to nest them, you need to manage nesting state externally.

#### `void LongJmp(string sLabel, int nRetVal = 1)`
> Jump execution back in time to the point where you called SetJmp with the same label.
> - This function is a GREAT way to get really hard-to-debug stack under/overflows.
> - Will not work across script runs or script recursion; only within the same script.
> (However, it WILL work across includes - those go into the same script data in compilation)
> - Will throw a script error if sLabel does not exist.
> - Will throw a script error if no valid jump destination exists.
> - You CAN jump to locations with compatible stack layout, including sibling functions.
> For the script to successfully finish, the entire stack needs to be correct (either in code or
> by jumping elsewhere again). Making sure this is the case is YOUR responsibility.
> - The parameter nRetVal is passed to SetJmp, resuming script execution as if SetJmp returned
> that value (instead of 0).
> If you accidentally pass 0 as nRetVal, it will be silently rewritten to 1.
> Any other integer value is valid, including negative ones.
> - This call will never return.

#### `int GetIsValidJmp(string sLabel)`
> Returns TRUE if the given sLabel is a valid jump target at the current code location.

#### `effect EffectPacified()`
> Create a Pacified effect, making the creature unable to attack anyone

#### `int GetScriptRecursionLevel()`
> Get the current script recursion level.

#### `string GetScriptName(int nRecursionLevel = -1)`
> Get the name of the script at a script recursion level.
> - nRecursionLevel: Between 0 and <= GetScriptRecursionLevel() or -1 for the current recursion level.
> Returns the script name or "" on error.

#### `string GetScriptChunk(int nRecursionLevel = -1)`
> Get the script chunk attached to a script recursion level.
> - nRecursionLevel: Between 0 and <= GetScriptRecursionLevel() or -1 for the current recursion level.
> Returns the script chunk or "" on error / no script chunk attached.

#### `int GetPlayerBuildVersionPostfix(object oPlayer)`
> Returns the patch postfix of oPlayer (i.e. the 29 out of "87.8193.35-29 abcdef01").
> Returns 0 if the given object isn't a player or did not advertise their build info, or the
> player version is old enough not to send this bit of build info to the server.

#### `string GetPlayerBuildVersionCommitSha1(object oPlayer)`
> Returns the patch commit sha1 of oPlayer (i.e. the "abcdef01" out of "87.8193.35-29 abcdef01").
> Returns "" if the given object isn't a player or did not advertise their build info, or the
> player version is old enough not to send this bit of build info to the server.

#### `int GetSpellFeatId()`
> In the spell script returns the feat used, or -1 if no feat was used
> In an Area of Effect script returns the feat used to generate it (or -1 otherwise)

#### `string GetEffectLinkId(effect eEffect)`
> Returns the given effects Link ID. There is no guarantees about this identifier other than
> it is unique and the same for all effects linked to it.

#### `int GetFeatRemainingUses(int nFeat, object oCreature = OBJECT_SELF)`
> If oCreature has nFeat, and nFeat is useable, returns the number of remaining uses left
> or the maximum int value if the feat has unlimited uses (eg FEAT_KNOCKDOWN)
> - nFeat: FEAT_*
> - oCreature: Creature to check the feat of

#### `void SetTile(location locTile, int nTileID, int nOrientation, int nHeight = 0, int nFlags = SETTILE_FLAG_RECOMPUTE_LIGHTING)`
> Change a tile in an area, it will also update the tile for all players in the area.
> Notes:
> - For optimal use you should be familiar with how tilesets / .set files work.
> - Will not update the height of non-creature objects.
> - Creatures may get stuck on non-walkable terrain.
> - locTile: The location of the tile.
> - nTileID: the ID of the tile, for values see the .set file of the tileset.
> - nOrientation: the orientation of the tile, 0-3.
> 0 = Normal orientation
> 1 = 90 degrees counterclockwise
> 2 = 180 degrees counterclockwise
> 3 = 270 degrees counterclockwise
> - nHeight: the height of the tile.
> - nFlags: a bitmask of SETTILE_FLAG_* constants.
> - SETTILE_FLAG_RELOAD_GRASS: reloads the area's grass, use if your tile used to have grass or should have grass now.
> - SETTILE_FLAG_RELOAD_BORDER: reloads the edge tile border, use if you changed a tile on the edge of the area.
> - SETTILE_FLAG_RECOMPUTE_LIGHTING: recomputes the area's lighting and static shadows, use most of time.

#### `int GetTileID(location locTile)`
> Get the ID of the tile at location locTile.
> Returns -1 on error.

#### `int GetTileOrientation(location locTile)`
> Get the orientation of the tile at location locTile.
> Returns -1 on error.

#### `int GetTileHeight(location locTile)`
> Get the height of the tile at location locTile.
> Returns -1 on error.

#### `void ReloadAreaGrass(object oArea)`
> All clients in oArea will reload the area's grass.
> This can be used to update the grass of an area after changing a tile with SetTile() that will have or used to have grass.

#### `void SetTileAnimationLoops(location locTile, int bAnimLoop1, int bAnimLoop2, int bAnimLoop3)`
> Set the state of the tile animation loops of the tile at location locTile.

#### `void SetTileJson(object oArea, json jTileData, int nFlags = SETTILE_FLAG_RECOMPUTE_LIGHTING, string sTileset = "")`
> Change multiple tiles in an area, it will also update the tiles for all players in the area.
> Note: See SetTile() for additional information.
> - oArea: the area to change one or more tiles of.
> - jTileData: a JsonArray() with one or more JsonObject()s with the following keys:
> - index: the index of the tile as a JsonInt()
> For example, a 3x3 area has the following tile indexes:
> 6 7 8
> 3 4 5
> 0 1 2
> - tileid: the ID of the tile as a JsonInt(), defaults to 0 if not set
> - orientation: the orientation of the tile as JsonInt(), defaults to 0 if not set
> - height: the height of the tile as JsonInt(), defaults to 0 if not set
> - animloop1: the state of a tile animation, 1/0 as JsonInt(), defaults to the current value if not set
> - animloop2: the state of a tile animation, 1/0 as JsonInt(), defaults to the current value if not set
> - animloop3: the state of a tile animation, 1/0 as JsonInt(), defaults to the current value if not set
> - nFlags: a bitmask of SETTILE_FLAG_* constants.
> - sTileset: if not empty, it will also change the area's tileset
> Warning: only use this if you really know what you're doing, it's very easy to break things badly.
> Make sure jTileData changes *all* tiles in the area and to a tile id that's supported by sTileset.

#### `void ReloadAreaBorder(object oArea)`
> All clients in oArea will reload the inaccesible border tiles.
> This can be used to update the edge tiles after changing a tile with SetTile().

#### `void SetEffectIconFlashing(object oCreature, int nIconId, int bFlashing = TRUE)`
> Sets whether or not oCreatures's nIconId is flashing in their GUI icon bar.  If oCreature does not
> have an icon associated with nIconId, nothing happens. This function does not add icons to
> oCreatures's GUI icon bar. The icon will flash until the underlying effect is removed or this
> function is called again with bFlashing = FALSE.
> - oCreature: Player object to affect
> - nIconId: Referenced to effecticons.2da or EFFECT_ICON_*
> - bFlashing: TRUE to force an existing icon to flash, FALSE to to stop.

#### `effect EffectBonusFeat(int nFeat)`
> Creates a bonus feat effect. These act like the Bonus Feat item property,
> and do not work as feat prerequisites for levelup purposes.
> - nFeat: FEAT_*

#### `int GetPCItemLastEquippedSlot()`
> Returns the INVENTORY_SLOT_* constant of the last item equipped.  Can only be used in the
> module's OnPlayerEquip event.  Returns -1 on error.

#### `int GetPCItemLastUnequippedSlot()`
> Returns the INVENTORY_SLOT_* constant of the last item unequipped.  Can only be used in the
> module's OnPlayerUnequip event.  Returns -1 on error.

#### `int GetSpellCastSpontaneously()`
> Returns TRUE if the last spell was cast spontaneously
> eg; a Cleric casting SPELL_CURE_LIGHT_WOUNDS when it is not prepared, using another level 1 slot
> Area of Effect objects can also retrieve if the spell used to generate it was casted spontaneously.

#### `void SqlResetQuery(sqlquery sqlQuery, int bClearBinds = FALSE)`
> Reset the given sqlquery, readying it for re-execution after it has been stepped.
> All existing binds are kept untouched, unless bClearBinds is TRUE.
> This command only works on successfully-prepared queries that have not errored out.

#### `effect EffectTimeStopImmunity()`
> Provides immunity to the effects of EffectTimeStop which allows actions during other creatures time stop effects

#### `int GetTickRate()`
> Return the current game tick rate (mainloop iterations per second).
> This is equivalent to graphics frames per second when the module is running inside a client.

#### `int GetLastSpellLevel()`
> Returns the level of the last spell cast. This value is only valid in a Spell script.

#### `int HashString(string sString)`
> Returns the 32bit integer hash of sString
> This hash is stable and will always have the same value for same input string, regardless of platform.
> The hash algorithm is the same as the one used internally for strings in case statements, so you can do:
> switch (HashString(sString))
> case "AAA":    HandleAAA(); break;
> case "BBB":    HandleBBB(); break;
> NOTE: The exact algorithm used is XXH32(sString) ^ XXH32(""). This means that HashString("") is 0.

#### `int GetMicrosecondCounter()`
> Returns the current microsecond counter value. This value is meaningless on its own, but can be subtracted
> from other values returned by this function in the same script to get high resolution elapsed time:
> int nMicrosecondsStart = GetMicrosecondCounter();
> DoSomething();
> int nElapsedMicroseconds = GetMicrosecondCounter() - nMicrosecondsStart;

#### `effect EffectForceWalk()`
> Forces the creature to always walk

#### `void StartAudioStream(object oPlayer, int nStreamIdentifier, string sResRef, int bLooping = FALSE, float fFadeTime = 0.0f, float fSeekOffset = -1.0f, float fVolume = 1.0f)`
> Assign one of the available audio streams to play a specific file. This mechanism can be used
> to replace regular music playback, and synchronize it between clients.
> There is currently no way to get playback state from clients.
> Audio streams play in the streams channel which has its own volume setting in the client.
> nStreamIdentifier is one of AUDIOSTREAM_IDENTIFIER_*.
> Currently, only MP3 CBR files are supported and properly seekable.
> Unlike regular music, audio streams do not pause on load screens.
> If fSeekOffset is at or beyond the end of the stream, the seek offset will wrap around, even if the file is configured not to loop.
> fFadeTime is in seconds to gradually fade in the audio instead of starting directly.
> Only one type of fading can be active at once, for example:
> If you call StartAudioStream() with fFadeTime = 10.0f, any other audio stream functions with a fade time >0.0f will have no effect
> until StartAudioStream() is done fading.

#### `void StopAudioStream(object oPlayer, int nStreamIdentifier, float fFadeTime = 0.0)`
> Stops the given audio stream.
> fFadeTime is in seconds to gradually fade out the audio instead of stopping directly.
> Only one type of fading can be active at once, for example:
> If you call StartAudioStream() with fFadeInTime = 10.0f, any other audio stream functions with a fade time >0.0f will have no effect
> until StartAudioStream() is done fading.
> Will do nothing if the stream is currently not in use.

#### `void SetAudioStreamPaused(object oPlayer, int nStreamIdentifier, int bPaused, float fFadeTime = 0.0f)`
> Un/pauses the given audio stream.
> fFadeTime is in seconds to gradually fade the audio out/in instead of pausing/resuming directly.
> Only one type of fading can be active at once, for example:
> If you call StartAudioStream() with fFadeInTime = 10.0f, any other audio stream functions with a fade time >0.0f will have no effect
> until StartAudioStream() is done fading.
> Will do nothing if the stream is currently not in use.

#### `void SetAudioStreamVolume(object oPlayer, int nStreamIdentifier, float fVolume = 1.0, float fFadeTime = 0.0f)`
> Change volume of audio stream.
> Volume is from 0.0 to 1.0.
> fFadeTime is in seconds to gradually change the volume.
> Only one type of fading can be active at once, for example:
> If you call StartAudioStream() with fFadeInTime = 10.0f, any other audio stream functions with a fade time >0.0f will have no effect
> until StartAudioStream() is done fading.
> Subsequent calls to this function with fFadeTime >0.0f while already fading the volume
> will start the new fade with the previous' fade's progress as starting point.
> Will do nothing if the stream is currently not in use.

#### `void SeekAudioStream(object oPlayer, int nStreamIdentifier, float fSeconds)`
> Seek the audio stream to the given offset.
> When seeking at or beyond the end of a stream, the seek offset will wrap around, even if the file is configured not to loop.
> Will do nothing if the stream is currently not in use.
> Will do nothing if the stream is in ended state (reached end of file and looping is off). In this
> case, you need to restart the stream.

#### `effect SetEffectCreator(effect eEffect, object oCreator)`
> Sets the effect creator
> - oCreator: The creator of the effect. Can be OBJECT_INVALID.

#### `effect SetEffectCasterLevel(effect eEffect, int nCasterLevel)`
> Sets the effect caster level
> - nCasterLevel: The caster level of the effect for the purposes of dispel magic and GetEffectCasterlevel. Must be >= 0.

#### `effect SetEffectSpellId(effect eEffect, int nSpellId)`
> Sets the effect spell id
> - nSpellId: The spell id for the purposes of effect stacking, dispel magic and GetEffectSpellId. Must be >= -1 (-1 being invalid/no spell)

#### `int SqlGetColumnCount(sqlquery sqlQuery)`
> Retrieve the column count of a prepared query.
> sqlQuery must be prepared before this function is called, but can be called before or after parameters are bound.
> If the prepared query contains no columns (such as with an UPDATE or INSERT query), 0 is returned.
> If a non-SELECT query contains a RETURNING clause, the number of columns in the RETURNING clause will be returned.
> A returned value greater than 0 does not guarantee the query will return rows.

#### `string SqlGetColumnName(sqlquery sqlQuery, int nNth)`
> Retrieve the column name of the Nth column of a prepared query.
> sqlQuery must be prepared before this function is called, but can be called before or after parameters are bound.
> If the prepared query contains no columns (such as with an UPDATE or INSERT query), an empty string is returned.
> If a non-SELECT query contains a RETURNING clause, the name of the nNth column in the RETURNING clause is returned.
> If nNth is out of range, an sqlite error is broadcast and an empty string is returned.
> The value of the AS clause will be returned, if the clause exists for the nNth column.
> A returned non-empty string does not guarantee the query will return rows.

#### `int GetSpellAbilityCount(object oCreature)`
> Gets the total number of spell abilities a creature has.

#### `int GetSpellAbilitySpell(object oCreature, int nIndex)`
> Gets the spell Id of the spell ability at the given index.
> - nIndex: the index of the spell ability. Bounds: 0 <= nIndex < GetSpellAbilityCount()
> Returns: a SPELL_* constant or -1 if the slot is not set.

#### `int GetSpellAbilityCasterLevel(object oCreature, int nIndex)`
> Gets the caster level of the spell ability in the given slot. Returns 0 by default.
> - nIndex: the index of the spell ability. Bounds: 0 <= nIndex < GetSpellAbilityCount()
> Returns: the caster level or -1 if the slot is not set.

#### `int GetSpellAbilityReady(object oCreature, int nIndex)`
> Gets the ready state of a spell ability.
> - nIndex: the index of the spell ability. Bounds: 0 <= nIndex < GetSpellAbilityCount()
> Returns: TRUE/FALSE or -1 if the slot is not set.

#### `void SetSpellAbilityReady(object oCreature, int nIndex, int bReady = TRUE)`
> Set the ready state of a spell ability slot.
> - nIndex: the index of the spell ability. Bounds: 0 <= nIndex < GetSpellAbilityCount()
> - bReady: TRUE to mark the slot ready.

#### `int JsonToTemplate(json jTemplateSpec, string sResRef, int nResType)`
> Serializes the given JSON structure (which must be a valid template spec) into a template.
> The template will be stored in the TEMP: alias and currently NOT stored in savegames.
> The stored template will override anything currently available in the module.
> Supported GFF resource types are the same as TemplateToJson().
> However, some types will not be read by the game (e.g. module.IFO is only read at module load).
> Returns TRUE if the serialization was successful.
> Any target file in TEMP: will be overwritten, even if the serialisation is not successful.
> JsonToTemplate(JSON_NULL, ..) can be used to delete a previously-generated file.

#### `void JsonObjectSetInplace(json jObject, string sKey, json jValue)`
> Modifies jObject in-place (with no memory copies of the full object).
> jObject will have the key at sKey set to jValue.

#### `void JsonObjectDelInplace(json jObject, string sKey)`
> Modifies jObject in-place (with no memory copies needed).
> jObject will have the element at the key sKey removed.
> Will do nothing if jObject is not a object, or sKey does not exist on the object.

#### `void JsonArrayInsertInplace(json jArray, json jValue, int nIndex = -1)`
> Modifies jArray in-place (with no memory copies needed).
> jArray will have jValue inserted at position nIndex.
> All succeeding elements in the array will move by one.
> By default (-1), inserts elements at the end of the array ("push").
> nIndex = 0 inserts at the beginning of the array.

#### `void JsonArraySetInplace(json jArray, int nIndex, json jValue)`
> Modifies jArray in-place (with no memory copies needed).
> jArray will have jValue set at position nIndex.
> Will do nothing if jArray is not an array or nIndex is out of range.

#### `void JsonArrayDelInplace(json jArray, int nIndex)`
> Modifies jArray in-place (with no memory copies needed).
> jArray will have the element at nIndex removed, and the array will be resized accordingly.
> Will do nothing if jArray is not an array or nIndex is out of range.

#### `void SetAreaGrassOverride(object oArea, int nMaterialId, string sTexture, float fDensity, float fHeight, vector vAmbientColor, vector vDiffuseColor)`
> Sets a grass override for nMaterialId in oArea.
> You can have multiple grass types per area by using different materials.
> You can add grass to areas that normally do not have grass, for example by calling this on the
> wood surface material(5) for an inn area.
> - nMaterialId: a surface material, see surfacemat.2da. 3 is the default grass material.
> - sTexture: the grass texture, cannot be empty.
> - fDensity: the density of the grass.
> - fHeight: the height of the grass.
> - vAmbientColor: the ambient color of the grass, xyz as RGB clamped to 0.0-1.0f per value.
> - vDiffuseColor: the diffuse color of the grass, xyz as RGB clamped to 0.0-1.0f per value.

#### `void RemoveAreaGrassOverride(object oArea, int nMaterialId)`
> Remove a grass override from oArea for nMaterialId.

#### `void SetAreaDefaultGrassDisabled(object oArea, int bDisabled)`
> Set to TRUE to disable the default grass of oArea.

#### `int GetAreaNoRestFlag(object oArea = OBJECT_INVALID)`
> Gets the NoRest area flag.
> Returns TRUE if resting is not allowed in the area.
> Passing in OBJECT_INVALID to parameter oArea will result in operating on the area of the caller.

#### `void SetAreaNoRestFlag(int bNoRestFlag, object oArea = OBJECT_INVALID)`
> Sets the NoRest flag on an area.
> Passing in OBJECT_INVALID to parameter oArea will result in operating on the area of the caller.

#### `void SetAge(object oCreature, int nAge)`
> Sets the age of oCreature.

#### `int GetAttacksPerRound(object oCreature, int bCheckOverridenValue = TRUE)`
> Gets the base number of attacks oCreature can make every round
> Excludes additional effects such as haste, slow, spells, circle kick, attack modes, etc.
> bCheckOverridenValue - Checks for SetBaseAttackBonus() on the creature, if FALSE will return the non-overriden version

#### `effect EffectEnemyAttackBonus(int nBonus)`
> Create an Enemy Attack Bonus effect. Creatures attacking the given creature with melee/ranged attacks or touch attacks get a bonus to hit.

#### `void SetAreaTileBorderDisabled(object oArea, int bDisabled)`
> Set to TRUE to disable the inaccessible tile border of oArea. Requires a client area reload to take effect.

#### `int GetIsDestroyable(object oObject)`
> Checks if a object is destroyable (toggle this state with SetIsDestroyable)
> Returns TRUE if they can be destroyed, FALSE otherwise or in error

#### `int GetIsRaiseable(object oCreature)`
> Checks if a creature is able to be raised with EffectResurrection (toggle this state with SetIsDestroyable)
> Returns TRUE if they can be raised, FALSE otherwise or in error

#### `int GetIsSelectableWhenDead(object oCreature)`
> Checks if a creature is able to be selected when dead (toggle this state with SetIsDestroyable)
> Returns TRUE if they can be selected, FALSE otherwise or in error

#### `int NWNXGetIsAvailable()`
> Check if NWNX is currently running.
> Returns TRUE if NWNX is available, FALSE if not.

#### `void NWNXCall(string sArg1, string sArg2)`
> This is an internal function for NWNX, it will abort the script if called without NWNX running.

#### `void NWNXPushInt(int nValue)`
> This is an internal function for NWNX, it will abort the script if called without NWNX running.

#### `void NWNXPushFloat(float fValue)`
> This is an internal function for NWNX, it will abort the script if called without NWNX running.

#### `void NWNXPushObject(object oValue)`
> This is an internal function for NWNX, it will abort the script if called without NWNX running.

#### `void NWNXPushString(string sValue)`
> This is an internal function for NWNX, it will abort the script if called without NWNX running.

#### `void NWNXPushVector(vector vValue)`
> This is an internal function for NWNX, it will abort the script if called without NWNX running.

#### `void NWNXPushLocation(location locValue)`
> This is an internal function for NWNX, it will abort the script if called without NWNX running.

#### `void NWNXPushEffect(effect eValue)`
> This is an internal function for NWNX, it will abort the script if called without NWNX running.

#### `void NWNXPushItemProperty(itemproperty ipValue)`
> This is an internal function for NWNX, it will abort the script if called without NWNX running.

#### `void NWNXPushJson(json jValue)`
> This is an internal function for NWNX, it will abort the script if called without NWNX running.

#### `void NWNXPushAction(action aValue)`
> This is an internal function for NWNX, it will abort the script if called without NWNX running.

#### `void NWNXPushEvent(event eValue)`
> This is an internal function for NWNX, it will abort the script if called without NWNX running.

#### `void NWNXPushTalent(talent tValue)`
> This is an internal function for NWNX, it will abort the script if called without NWNX running.

#### `void NWNXPushSqlquery(sqlquery sqlValue)`
> This is an internal function for NWNX, it will abort the script if called without NWNX running.

#### `void NWNXPushCassowary(cassowary cValue)`
> This is an internal function for NWNX, it will abort the script if called without NWNX running.

#### `int NWNXPopInt()`
> This is an internal function for NWNX, it will abort the script if called without NWNX running.

#### `float NWNXPopFloat()`
> This is an internal function for NWNX, it will abort the script if called without NWNX running.

#### `object NWNXPopObject()`
> This is an internal function for NWNX, it will abort the script if called without NWNX running.

#### `string NWNXPopString()`
> This is an internal function for NWNX, it will abort the script if called without NWNX running.

#### `vector NWNXPopVector()`
> This is an internal function for NWNX, it will abort the script if called without NWNX running.

#### `location NWNXPopLocation()`
> This is an internal function for NWNX, it will abort the script if called without NWNX running.

#### `effect NWNXPopEffect()`
> This is an internal function for NWNX, it will abort the script if called without NWNX running.

#### `itemproperty NWNXPopItemProperty()`
> This is an internal function for NWNX, it will abort the script if called without NWNX running.

#### `json NWNXPopJson()`
> This is an internal function for NWNX, it will abort the script if called without NWNX running.

#### `event NWNXPopEvent()`
> This is an internal function for NWNX, it will abort the script if called without NWNX running.

#### `talent NWNXPopTalent()`
> This is an internal function for NWNX, it will abort the script if called without NWNX running.

#### `sqlquery NWNXPopSqlquery()`
> This is an internal function for NWNX, it will abort the script if called without NWNX running.

#### `cassowary NWNXPopCassowary()`
> This is an internal function for NWNX, it will abort the script if called without NWNX running.

#### `int SpellResistanceCheck(object oTarget, object oCaster, int nSpellId = -1, int nCasterLevel = -1, int nSpellResistance = -1, int bFeedback = TRUE)`
> Does a spell resistance check. The roll is 1d20 + nCasterLevel + nCasterBonus vs. nSpellResistance
> - nSpellId         - The spell ID to use if other variables are not set. If -1 it will attempt to be auto-detected.
> - nCasterLevel     - The caster level. If -1 it attempts to find it automatically from oCaster.
> - nSpellResistance - The spell resistance to penetrate. If -1 it will use the spell resistance of oTarget.
> - bFeedback        - If TRUE displays feedback automatically, FALSE it suppresses it.
> Returns: TRUE if the target resists oCasters spell resistance roll, FALSE if failed or an error occured

#### `int SpellImmunityCheck(object oTarget, object oCaster, int nSpellId = -1, int bFeedback = TRUE)`
> Does a spell immunity check. This checks for EFfectSpellImmunity and related item properties.
> - nSpellId  - The spell ID to check immunity of. If -1 it will attempt to be auto-detected.
> - bFeedback - If TRUE displays feedback automatically, FALSE it suppresses it.
> Returns: TRUE if the target is immune to nSpellId, FALSE if failed or an error occured

#### `int SpellAbsorptionLimitedCheck(object oTarget, object oCaster, int nSpellId = -1, int nSpellSchool = -1, int nSpellLevel = -1, int bRemoveLevels = TRUE, int bFeedback = TRUE)`
> Does a spell absorption check that checks limited (eg Spell Mantle)
> - nSpellId      - The Spell Id. If -1 it will attempt to be auto-detected.
> - nSpellSchool  - The spell school to check for. If -1 uses nSpellId's spell school.
> - nSpellLevel   - The spell level. If -1 uses nSpellId's spell level (given the casters last spell cast class)
> - bRemoveLevels - If TRUE this removes spell levels from the effect that would stop it (and remove it if 0 or less remain), but if FALSE they will not be removed.
> - bFeedback     - If TRUE displays feedback automatically, FALSE it suppresses it.
> Returns: TRUE if the target absorbs oCasters spell, FALSE if failed or an error occured

#### `int SpellAbsorptionUnlimitedCheck(object oTarget, object oCaster, int nSpellId = -1, int nSpellSchool = -1, int nSpellLevel = -1, int bFeedback = FALSE)`
> Does a spell absorption check that checks unlimited spell absorption effects (eg; Globes)
> - nSpellId     - The Spell Id. If -1 it will attempt to be auto-detected.
> - nSpellSchool - The spell school to check for. If -1 uses nSpellId's spell school.
> - nSpellLevel  - The spell level. If -1 uses nSpellId's spell level (given the casters last spell cast class)
> - bFeedback    - If TRUE displays feedback automatically, FALSE it suppresses it. As per existing ResistSpell convention it defaults to FALSE.
> Returns: TRUE if the target absorbs oCasters spell, FALSE if failed or an error occured

#### `int GetPlayerNetworkLatency(object oPlayer, int bSmoothed = TRUE)`
> Returns the network latency of this player device.
> The value is a round trip time (server->player->server) in milliseconds.
> Players are pinged every 6000 milliseconds.
> When bSmoothed is TRUE, returns a moving average over a longer timeframe.
> This average calculation is not strictly specified and subject to change,
> but intended to provide a reasonable average to rely on.
> When bSmoothed is FALSE, returns the current/last received value.
> Returns 0 if the client failed to respond to latency requests or no data is available.
> This is currently the case for clients that do not support this functionality (build <37).

#### `int GetBodyBag(object oObject)`
> Gets the creature or placeable body bag type (bodybag.2da entry)
> Returns -1 on error.

#### `void SetBodyBag(object oObject, int nBodyBag)`
> Sets the creature or placeable body bag type (bodybag.2da entry)
