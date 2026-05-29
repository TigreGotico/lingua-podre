# API reference

Everything public lives at the top level of `lingua_podre`. The detector is four
small functions plus the data they read.

```python
from lingua_podre import (
    tokenize, get_word_counts, get_lang_scores, predict_lang,
    langs, lang_codes, stopwords,
)
```

## Functions

### `tokenize(text) -> list[str]`

Lowercases the text and splits on a single space.

```python
from lingua_podre import tokenize
tokenize("Olá Mundo")           # ['olá', 'mundo']
```

It splits on `" "` only — it does not strip punctuation, so `"João,"` stays
`"joão,"`. Tokens are matched against the word lists verbatim, so trailing
punctuation simply fails to match.

### `get_word_counts(text) -> dict[str, int]`

Counts, per language code, how many tokens of `text` appear in that language's
word list. Accepts either a raw string (it tokenises for you) or an
already-tokenised `list[str]`.

```python
from lingua_podre import get_word_counts
get_word_counts("olá o meu nome é João")
# {'ca': 1, 'pt': 4, 'es': 1, 'pl': 1, 'tr': 1, 'ro': 2, 'it': 2, 'cs': 1, 'sk': 1}
```

A token that appears in several languages' lists is counted once per language —
that is the whole signal. Only language codes with at least one hit are keys.

### `get_lang_scores(text) -> dict[str, float]`

`get_word_counts` divided by the total count, so the values sum to 1. Same key
set as `get_word_counts`.

```python
from lingua_podre import get_lang_scores
get_lang_scores("olá o meu nome é João")
# {'pt': 0.285..., 'ro': 0.142..., 'it': 0.142..., 'ca': 0.071..., ...}
```

Raises `ZeroDivisionError` when no token matches anything (total is 0). See
[advanced.md](advanced.md#empty-and-undetectable-input).

### `predict_lang(text) -> list[str]`

The top-scoring language code(s). Returns a **list** because ties are possible.

```python
from lingua_podre import predict_lang
predict_lang("olá o meu nome é João")   # ['pt']
```

Raises `ValueError` on text where nothing matched (it calls `max()` on the empty
score set). Wrap it if input can be arbitrary.

## Module data

### `langs -> dict[str, str]`

Code to English name, for the 28 active languages. Loaded from
`res/languages.json`, with an in-code fallback.

```python
from lingua_podre import langs
langs["pt"]                 # 'portuguese'
len(langs)                  # 28
```

### `lang_codes -> dict[str, str]`

The inverse of `langs` — English name to code.

```python
from lingua_podre import lang_codes
lang_codes["portuguese"]    # 'pt'
```

### `stopwords -> dict[str, list[str]]`

Code to its loaded word list. Built once at import time from `res/stopwords/`
and `res/1000/`. Only languages present in `langs` are loaded.

```python
from lingua_podre import stopwords
sorted(stopwords)           # ['ar', 'bg', 'ca', 'cs', ...]  (28 codes)
"meu" in stopwords["pt"]    # True
```

## Return-shape summary

| Call | Returns | Empty / no-match behaviour |
| --- | --- | --- |
| `tokenize(text)` | `list[str]` | `['']` for empty string |
| `get_word_counts(text)` | `dict[str, int]` | `{}` |
| `get_lang_scores(text)` | `dict[str, float]` (sums to 1) | raises `ZeroDivisionError` |
| `predict_lang(text)` | `list[str]` (codes) | raises `ValueError` |

## Where next

- [quickstart.md](quickstart.md) — install and first call
- [advanced.md](advanced.md) — ties, guards, supported languages
- [opm.md](opm.md) — the OVOS plugin wrapper
