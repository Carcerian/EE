# `x2_inc_banter.nss`

Source: `NSS/x2_/x2_inc_banter.nss`  
13 functions · 4 constants

## Constants

| Constant | Type | Value | Note |
|---|---|---|---|
| `TRIGGER_ONELINERNONRANDOM` | int | `1` |  |
| `TRIGGER_ONELINERRANDOM` | int | `2` |  |
| `TRIGGER_INTERJECTION_NONRANDOM` | int | `3` |  |
| `TRIGGER_INTERJECTION_RANDOM` | int | `4` |  |

## Functions

#### `void AttemptInterjectionOrPopup(object oSelf, string sTag, object oTrigger, int nOverrideModNum = 0, object oOverrideBanter = OBJECT_INVALID)`
> This is the main interjection function called from x2_evt_trigger
> and any plot means of making banter happen\
> oSelf - is used only when triggers are running the script
> sTag is the tag of the trigger. Pass in an appropriate henchman tag
> when using this function for plot purposes (i.e., x2_oneliner_nr gives you
> non-random popups
> oTrigger - should be the player involved. The object who triggered things
> nOverrideModNum - Change the popup to display. Should only be used when calling it
> from non-triggers
> oOverrideBanter - this hench should try to initiate banter

#### `int AttemptToShowInfo(int nTriggerType, int nId, int bDestroyAnyways = FALSE, object oHench = OBJECT_INVALID)`
> Have the proper plot variables been set?

#### `int GetRandomTextNumber(object oHench, string sVariableName, int nDeleteMe = -1)`
> Looks for the valid random Number # to return; updates sVariableName stringlist (i.e., 1|2|3|)

#### `void FireInterjection(int nType, int nModNumber, object oMaster, object oHench, int nDestroyTriggerAnyways = FALSE, string sConvFile = "")`
> actually speaks the interjection

#### `object GetRandomHench(object oPC, string sTag = "")`
> Returns either the 1st or second henchman, randomly
> for purposes of interjections and such

#### `void WrapInterjection(int nType, int nId, object oMaster, object oHench, string sTag, int nDestroyTriggerAnyways = FALSE, string sConvFile = "")`
> Making code reusable. Call this at the highest level to fire the appropriate interjection

#### `int TryBanterWith(string sTag, int nBanter)`
> Wrapper function to streamline that party banter system

#### `void AttemptRomanceDialog(object oPC, int nLimit)`
> Nathyrra or Valen romance dialog

#### `int HenchmanMoveable(object oHench)`

#### `void DoInterjection(object oHench, object oPC, int MOD_EVENT_NUMBER, string sConvFile = "")`

#### `int ValidForInterjection(object oPC, object oHench)`
> am I valid for doing an interjection

#### `int BanterReady(string sTag, string sTag2 = "", string sTag3 = "")`
> Checks to see if henchmen is available for banter interjection
> and then moves them to the position of the Master, as well
> as OBJECT_SELF

#### `int GetPlotProgress()`
> returns true if its time to say another romance line
