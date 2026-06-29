# `x3_inc_string.nss`

Source: `NSS/x3_/x3_inc_string.nss`  
4 functions · 7 constants

## Constants

| Constant | Type | Value | Note |
|---|---|---|---|
| `STRING_COLOR_BLACK` | string | `"000"` |  |
| `STRING_COLOR_BLUE` | string | `"007"` |  |
| `STRING_COLOR_GREEN` | string | `"070"` |  |
| `STRING_COLOR_PINK` | string | `"755"` |  |
| `STRING_COLOR_RED` | string | `"700"` |  |
| `STRING_COLOR_ROSE` | string | `"744"` |  |
| `STRING_COLOR_WHITE` | string | `"777"` |  |

## Functions

#### `string StringToRGBString(string sString, string sRGB)`
> FILE: x3_inc_string      FUNCTION: StringToRGBString()
> This function will make sString be the specified color
> as specified in sRGB.  RGB is the Red, Green, and Blue
> components of the color.  Each color can have a value from
> 0 to 7.
> Ex: red   == "700"
> green == "070"
> blue  == "007"
> white == "777"
> black == "000"
> The STRING_COLOR_* constants may be used for sRGB.

#### `string StringParse(string sSource, string sDelimiter = " ", int bRightToLeft = FALSE)`
> FILE: x3_inc_string       FUNCTION: StringParse()
> This function will parse sSource from left to right until it encounters
> sDelimiter and will return all the characters it encountered before
> the delimiter occurred.
> If bRightToLeft is set to TRUE then it will parse from right to left instead.

#### `string StringRemoveParsed(string sSource, string sParsed, string sDelimiter = " ", int bRightToLeft = FALSE)`
> FILE: x3_inc_string        FUNCTION: StringRemoveParsed()
> This function will take sParsed and remove it from the left side of sSource.
> It will also remove any excess sDelimiter occurrences after sParsed.
> If bRightToLeft is set to TRUE then it will perform this from the right side
> rather than the left.
> No check is made that sParsed actually matches sSource; all that matters
> about sParsed is its length.

#### `string StringReplace(string sSource, string sFind, string sReplace)`
> FILE: x3_inc_string         FUNCTION: StringReplace()
> This function will replace any occurrence of sFind in sSource with sReplace.
