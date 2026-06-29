# `x0_i0_campaign.nss`

Source: `NSS/x0_/x0_i0_campaign.nss`  
28 functions · 0 constants

## Functions

#### `string GetCampaignDBName()`
> Return the name of the campaign database that should be used for
> this module (or a default value if none).

#### `void SetCampaignDBString(object oPC, string sVarname, string value)`
> Set a campaign string on a PC in the default DB for this module

#### `string GetCampaignDBString(object oPC, string sVarname)`
> Set a campaign string on a PC in the default DB for this module

#### `void SetCampaignDBInt(object oPC, string sVarname, int value)`
> Set a campaign int on a PC in the default DB for this module

#### `int GetCampaignDBInt(object oPC, string sVarname)`
> Get a campaign int on a PC in the default DB for this module

#### `void SetCampaignDBFloat(object oPC, string sVarname, float value)`
> Set a campaign float on a PC in the default DB for this module

#### `float GetCampaignDBFloat(object oPC, string sVarname)`
> Get a campaign float on a PC in the default DB for this module

#### `void SetCampaignDBVector(object oPC, string sVarname, vector value)`
> Set a campaign vector on a PC in the default DB for this module

#### `vector GetCampaignDBVector(object oPC, string sVarname)`
> Get a campaign vector on a PC in the default DB for this module

#### `void SetCampaignDBLocation(object oPC, string sVarname, location value)`
> Set a campaign location on a PC in the default DB for this module

#### `location GetCampaignDBLocation(object oPC, string sVarname)`
> Get a campaign location on a PC in the default DB for this module

#### `int StoreCampaignDBObject(object oPC, string sVarname, object value)`
> Store a campaign object on a PC in the default DB for this module
> NOTE: this does not store a reference, it stores the entire actual object,
> including all of its inventory. Storing many objects can be highly resource-
> intensive! It should NOT be used like Set/GetLocalObject.

#### `object RetrieveCampaignDBObject(object oPC, string sVarname, location lLoc, object oInventory = OBJECT_INVALID)`
> Get a campaign object stored on a PC in the default DB for this module
> NOTE: this does not get a reference, it creates the actual object,
> either in the PC's inventory if possible or in the specified location
> if not. It should NOT be used like Set/GetLocalObject.
> If you pass in a valid object for oInventory, the object will be
> retrieved in that object's inventory instead of the PC's.
> You should use DeleteCampaignDBVariable to remove the object once you
> are done retrieving it, or else the DB will bloat.

#### `void DeleteCampaignDBVariable(object oPC, string sVarname)`
> Delete a campaign variable

#### `string GetCampaignDBName()`
> Return the name of the campaign database that should be used for
> this module (or a default value if none).

#### `void SetCampaignDBString(object oPC, string sVarname, string value)`
> Set a campaign string on a PC in the default DB for this module

#### `string GetCampaignDBString(object oPC, string sVarname)`
> Get a campaign string on a PC in the default DB for this module

#### `void SetCampaignDBInt(object oPC, string sVarname, int value)`
> Set a campaign int on a PC in the default DB for this module

#### `int GetCampaignDBInt(object oPC, string sVarname)`
> Get a campaign int on a PC in the default DB for this module

#### `void SetCampaignDBFloat(object oPC, string sVarname, float value)`
> Set a campaign float on a PC in the default DB for this module

#### `float GetCampaignDBFloat(object oPC, string sVarname)`
> Get a campaign float on a PC in the default DB for this module

#### `void SetCampaignDBVector(object oPC, string sVarname, vector value)`
> Set a campaign vector on a PC in the default DB for this module

#### `vector GetCampaignDBVector(object oPC, string sVarname)`
> Get a campaign vector on a PC in the default DB for this module

#### `void SetCampaignDBLocation(object oPC, string sVarname, location value)`
> Set a campaign location on a PC in the default DB for this module

#### `location GetCampaignDBLocation(object oPC, string sVarname)`
> Get a campaign location on a PC in the default DB for this module

#### `int StoreCampaignDBObject(object oPC, string sVarname, object value)`
> Set a campaign object on a PC in the default DB for this module

#### `object RetrieveCampaignDBObject(object oPC, string sVarname, location lLoc, object oInventory = OBJECT_INVALID)`
> Get a campaign object stored on a PC in the default DB for this module
> NOTE: this does not get a reference, it creates the actual object,
> either in the PC's inventory if possible or in the specified location
> if not. It should NOT be used like Set/GetLocalObject.
> If you pass in a valid object for oInventory, the object will be
> retrieved in that object's inventory instead of the PC's.
> You should use DeleteCampaignDBVariable to remove the object once you
> are done retrieving it, or else the DB will bloat.

#### `void DeleteCampaignDBVariable(object oPC, string sVarname)`
> Delete a campaign variable
