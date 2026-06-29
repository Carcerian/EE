# `x2_inc_switches.nss`

Source: `NSS/x2_/x2_inc_switches.nss`  
23 functions · 48 constants

## Constants

| Constant | Type | Value | Note |
|---|---|---|---|
| `MODULE_SWITCH_ENABLE_UMD_SCROLLS` | string | `"X2_SWITCH_ENABLE_UMD_SCROLLS"` |  |
| `MODULE_SWITCH_DISABLE_ITEM_CREATION_FEATS` | string | `"X2_SWITCH_DISABLE_ITEMCREATION_FEATS"` |  |
| `MODULE_SWITCH_AOE_HURT_NEUTRAL_NPCS` | string | `"X0_G_ALLOWSPELLSTOHURT"` |  |
| `MODULE_SWITCH_ENABLE_CRAFT_WAND_50_CHARGES` | string | `"X2_SWITCH_ENABLE_50_WAND_CHARGES"` |  |
| `MODULE_SWITCH_EPIC_SPELLS_HURT_CASTER` | string | `"X2_SWITCH_EPIC_SPELLS_HURT_CASTER"` |  |
| `MODULE_SWITCH_SPELL_CORERULES_DMASTERTOUCH` | string | `"X2_SWITCH_SPELL_CORERULE_DMTOUCH"` |  |
| `MODULE_SWITCH_RESTRICT_USE_POISON_TO_FEAT` | string | `"X2_SWITCH_RESTRICT_USE_POISON_FEAT"` |  |
| `MODULE_SWITCH_ENABLE_MULTI_HENCH_AOE_DAMAGE` | string | `"X2_SWITCH_MULTI_HENCH_AOE_MADNESS"` |  |
| `MODULE_SWITCH_ENABLE_NPC_AOE_HURT_ALLIES` | string | `"X2_SWITCH_ENABLE_NPC_AOE_HURT_ALLIES"` |  |
| `MODULE_SWITCH_ENABLE_BEBILITH_RUIN_ARMOR` | string | `"X2_SWITCH_BEBILITH_HARDCORE_RUIN_ARMOR"` |  |
| `MODULE_SWITCH_ENABLE_INVISIBLE_GLYPH_OF_WARDING` | string | `"X2_SWITCH_GLYPH_OF_WARDING_INVISIBLE"` |  |
| `MODULE_SWITCH_ENABLE_CROSSAREA_WALKWAYPOINTS` | string | `"X2_SWITCH_CROSSAREA_WALKWAYPOINTS"` |  |
| `MODULE_SWITCH_DISABLE_SECRET_DOOR_FLASH` | string | `"X2_SWITCH_DISABLE_SECRET_DOOR_FLASH"` |  |
| `MODULE_SWITCH_ENABLE_TAGBASED_SCRIPTS` | string | `"X2_SWITCH_ENABLE_TAGBASED_SCRIPTS"` |  |
| `MODULE_SWITCH_USE_XP2_RESTSYSTEM` | string | `"X2_SWITCH_ENABLE_XP2_RESTSYSTEM"` |  |
| `MODULE_SWITCH_DISABLE_AI_DISPEL_AOE` | string | `"X2_L_AI_NO_AOE_DISPEL"` |  |
| `MODULE_SWITCH_NO_RANDOM_MONSTER_LOOT` | string | `"X2_L_NOTREASURE"` |  |
| `MODULE_VAR_OVERRIDE_SPELLSCRIPT` | string | `"X2_S_UD_SPELLSCRIPT"` |  |
| `MODULE_VAR_TAGBASED_SCRIPT_PREFIX` | string | `"X2_S_UD_SPELLSCRIPT"` |  |
| `MODULE_VAR_WANDERING_MONSTER_2DA` | string | `"X2_WM_2DA_NAME"` |  |
| `MODULE_VAR_AI_NO_DISPEL_AOE_CHANCE` | string | `"X2_L_AI_AOE_DISPEL_CHANCE"` |  |
| `MODULE_VAR_AI_STOP_EXPERTISE_ABUSE` | string | `"X2_L_STOP_EXPERTISE_ABUSE"` |  |
| `CREATURE_VAR_CUSTOM_AISCRIPT` | string | `"X2_SPECIAL_COMBAT_AI_SCRIPT"` |  |
| `CREATURE_VAR_RANDOMIZE_NAME` | string | `"X2_NAME_RANDOM"` |  |
| `CREATURE_VAR_RANDOMIZE_SPELLUSE` | string | `"X2_SPELL_RANDOM"` |  |
| `CREATURE_VAR_USE_SPAWN_STEALTH` | string | `"X2_L_SPAWN_USE_STEALTH"` |  |
| `CREATURE_VAR_USE_SPAWN_SEARCH` | string | `"X2_L_SPAWN_USE_SEARCH"` |  |
| `CREATURE_VAR_USE_SPAWN_AMBIENT` | string | `"X2_L_SPAWN_USE_AMBIENT"` |  |
| `CREATURE_VAR_USE_SPAWN_AMBIENT_IMMOBILE` | string | `"X2_L_SPAWN_USE_AMBIENT_IMMOBILE"` |  |
| `CREATURE_VAR_IMMUNE_TO_DISPEL` | string | `"X1_L_IMMUNE_TO_DISPEL"` |  |
| `CREATURE_VAR_IS_INCORPOREAL` | string | `"X2_L_IS_INCORPOREAL"` |  |
| `CREATURE_VAR_NUMBER_OF_ATTACKS` | string | `"X2_L_NUMBER_OF_ATTACKS"` |  |
| `CREATURE_AI_MODIFIED_MAGIC_RATE` | string | `"X2_L_BEH_MAGIC"` |  |
| `CREATURE_AI_MODIFIED_OFFENSE_RATE` | string | `"X2_L_BEH_OFFENSE"` |  |
| `CREATURE_AI_MODIFIED_COMPASSION_RATE` | string | `"X2_L_BEH_COMPASSION"` |  |
| `CREATURE_VAR_PALE_MASTER_SPECIAL_ITEM` | string | `"X2_S_PM_SPECIAL_ITEM"` |  |
| `X2_ITEM_EVENT_ACTIVATE` | int | `0` |  |
| `X2_ITEM_EVENT_EQUIP` | int | `1` |  |
| `X2_ITEM_EVENT_UNEQUIP` | int | `2` |  |
| `X2_ITEM_EVENT_ONHITCAST` | int | `3` |  |
| `X2_ITEM_EVENT_ACQUIRE` | int | `4` |  |
| `X2_ITEM_EVENT_UNACQUIRE` | int | `5` |  |
| `X2_ITEM_EVENT_SPELLCAST_AT` | int | `6` |  |
| `X2_EXECUTE_SCRIPT_CONTINUE` | int | `0` |  |
| `X2_EXECUTE_SCRIPT_END` | int | `1` |  |
| `DOOR_FLAG_RESIST_KNOCK` | string | `"X2_FLAG_DOOR_RESIST_KNOCK"` |  |
| `WAYPOINT_VAR_FORCE_SETFACING` | string | `"X2_L_WAYPOINT_SETFACING"` |  |
| `ITEM_FLAG_NO_CRAFT_MODIFICATION` | string | `"X2_FLAG_ITEM_CRAFT_DO_NOT_MODIFY"` |  |

## Functions

#### `void SetUserDefinedItemEventNumber(int nEvent)`
> Set the active User Defined Item Event
> X2_ITEM_EVENT_ACTIVATE
> X2_ITEM_EVENT_EQUIP
> X2_ITEM_EVENT_UNEQUIP
> X2_ITEM_EVENT_ONHITCAST
> X2_ITEM_EVENT_ACQUIRE
> X2_ITEM_EVENT_UNACQUIRE
> X2_ITEM_EVENT_SPELLCAST_AT

#### `int GetUserDefinedItemEventNumber()`
> Get the active User Defined Item Event
> X2_ITEM_EVENT_ACTIVATE
> X2_ITEM_EVENT_EQUIP
> X2_ITEM_EVENT_UNEQUIP
> X2_ITEM_EVENT_ONHITCAST
> X2_ITEM_EVENT_ACQUIRE
> X2_ITEM_EVENT_UNACQUIRE
> X2_ITEM_EVENT_SPELLCAST_AT

#### `void SetModuleSwitch(string sModuleSwitchConstant, int bValue)`
> Used to switch between different rule implementations or to subsystems for the game
> see x2_inc_switches for more detailed information on these constants

#### `int GetModuleSwitchValue(string sModuleSwitchConstant)`
> Returns the value of a module switch

#### `void SetDoorFlag(object oDoor, string sDoorFlagConstant, int nValue)`
> Used to toggle custom flags on a door
> oDoor - Door to set the switch on
> Valid values for sDoorFlagConstant:
> X2_FLAG_DOOR_RESIST_KNOCK -
> Set to 1 to prevent knock from working with feedback.
> Set to 2 to prevent knock from working without feedback

#### `int GetDoorFlag(object oDoor, string sDoorFlagConstant)`

#### `void SetItemFlag(object oItem, string sItemFlagConstant, int nValue)`

#### `int GetItemFlag(object oItem, string sItemFlagConstant)`

#### `int ExecuteScriptAndReturnInt(string sScript, object oTarget)`
> Execute sScript on oTarget returning an integer.
> Do not nest this function

#### `void SetExecutedScriptReturnValue(int nValue = X2_EXECUTE_SCRIPT_END)`
> Sets the return value for scripts called via ExecuteScriptAndReturnInt
> valid values are
> X2_EXECUTE_SCRIPT_CONTINUE - continue calling script after executed scriptis done
> X2_EXECUTE_SCRIPT_END - end calling script after executed script is done

#### `void SetUserDefinedItemEventPrefix(string sPrefix = "")`
> This is a security feature. If you are running a *local vault* server and you
> have tag based script execution enabled, people could bring items into your
> game that execute existing scripts. You can set a script prefix here to
> prevent that. Note that you have to add this prefix to your item scripts in
> the module to make them work.

#### `void SetModuleOverrideSpellscript(string sScriptName)`
> Allows the module creator to specify a script that will be run before any spellscript is run
> You can call SetModuleOverrideSpellscript() at the end of the script specified by
> sScriptName. If you call this function this will prevent the original spellscript
> (and all craft item code) from being executed.
> If you do not add this line, the original spellscript and/or crafting code will
> run in addition to your script

#### `void SetCreatureFlag(object oCreature, string sFlag, int nValue)`

#### `int GetCreatureFlag(object oCreature, string sFlag)`

#### `void SetCreatureOverrideAIScript(object oCreature, string sScriptName)`
> Define a replacement script for DetermineCombatRound
> See x2_ai_demo for details

#### `void SetCreatureOverrideAIScriptFinished(object oCreature = OBJECT_SELF)`
> Call this at end of your custom override AI script set via CREATURE_VAR_CUSTOM_AISCRIPT
> See x2_ai_demo for details.

#### `void ClearCreatureOverrideAIScriptTarget(object oCreature = OBJECT_SELF)`

#### `object GetCreatureOverrideAIScriptTarget(object oCreature = OBJECT_SELF)`

#### `void SetWanderingMonster2DAFile(string s2DAName = "des_restsystem")`
> Define the name of the 2da file which is used for the wandering monster
> system

#### `string GetModuleOverrideSpellscript()`

#### `void SetModuleOverrideSpellScriptFinished()`
> You can call this in our overridden spellscript. If you call this
> this will prevent the original spellscript (and all craft item code)
> from being executed. If you do not add this line, the original spellscript
> and/or crafting code will run in addition to your script

#### `int GetModuleOverrideSpellScriptFinished()`

#### `string GetUserDefinedItemEventScriptName(object oItem)`
> Returns the name for the User Defined Item Event script for oItem,
> including possible prefixes configured by SetUserDefinedItemEventPrefix
