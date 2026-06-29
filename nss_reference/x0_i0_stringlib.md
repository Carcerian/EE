# `x0_i0_stringlib.nss`

Source: `NSS/x0_/x0_i0_stringlib.nss`  
12 functions · 1 constants

## Constants

| Constant | Type | Value | Note |
|---|---|---|---|
| `DELIM_NOT_FOUND` | int | `-1` |  |

## Functions

#### `struct sStringTokenizer GetStringTokenizer(string sString, string sDelim)`
> Get a string tokenizer for sString. sDelim may be multiple
> characters in length.

#### `int HasMoreTokens(struct sStringTokenizer stTok)`
> Check to see if any more tokens remain. Returns 0 if not, 1 if so.

#### `struct sStringTokenizer AdvanceToNextToken(struct sStringTokenizer stTok)`
> Get next token

#### `string GetNextToken(struct sStringTokenizer stTok)`
> Get the last token retrieved

#### `int GetNumberTokens(string sString, string sDelim)`
> Get the number of tokens in the string, by delimeter.

#### `string GetTokenByPosition(string sString, string sDelim, int nPos)`
> Get the specified token in the string, by delimiter.
> The first string is position 0, the second is position 1, etc.

#### `struct sStringTokenizer GetStringTokenizer(string sString, string sDelim)`
> Get a string tokenizer for sString. sDelim may be multiple
> characters in length.

#### `int HasMoreTokens(struct sStringTokenizer stTok)`
> Check to see if any more tokens remain. Returns 0 if not, 1 if so.

#### `struct sStringTokenizer AdvanceToNextToken(struct sStringTokenizer stTok)`
> Move tokenizer to next token

#### `string GetNextToken(struct sStringTokenizer stTok)`
> Get the next token

#### `int GetNumberTokens(string sString, string sDelim)`
> Get the number of tokens in the string, by delimeter.

#### `string GetTokenByPosition(string sString, string sDelim, int nPos)`
> Get the specified token in the string, by delimiter.
> The first string is position 0, the second is position 1, etc.
