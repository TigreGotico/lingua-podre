# Advanced usage

Recipes and edge cases for `lingua_podre`. The detector is intentionally tiny.
Most of the work is knowing where it goes flat.

## Empty and undetectable input

The scoring path divides by the total number of matched tokens. When nothing
matches (a single rare word, a proper name, or a non-bundled language), that
total is 0:

- `get_word_counts` returns `{}`
- `get_lang_scores` raises `ZeroDivisionError`
- `predict_lang` raises `ValueError` (`max()` on an empty set)

Always guard arbitrary input:

```python
from lingua_podre import predict_lang, get_word_counts

def detect(text):
    if not get_word_counts(text):       # cheap pre-check, never raises
        return []
    return predict_lang(text)

detect("xyzzy")     # []
detect("olá mundo") # ['pt']
```

## Ties

`predict_lang` returns every code that holds the top score, so a list of length
> 1 means the text was ambiguous. This is common for short input, and especially
for the Romance and Slavic clusters that share many function words.

```python
from lingua_podre import predict_lang

result = predict_lang("a")          # 'a' appears in many lists
if len(result) > 1:
    print("ambiguous:", result)     # break the tie with more context
```

Tie-breaking strategy: feed more text. The signal is per-token, so longer input
sharpens the distribution.

## Reading the distribution instead of the top pick

When you want a confidence-style answer rather than a hard label, use the scores
directly:

```python
from lingua_podre import get_lang_scores

scores = get_lang_scores("olá o meu nome é João")
ranked = sorted(scores.items(), key=lambda kv: kv[1], reverse=True)
for code, p in ranked[:3]:
    print(f"{code}: {p:.0%}")
```

A simple confidence threshold filters out the flat distributions you get from
short or mixed text: accept the top score only when it clears, say, 0.25 and
beats the runner-up by a margin.

## Supported languages

The active set is whatever is in `langs` (28 codes). Inspect it at runtime
rather than hardcoding:

```python
from lingua_podre import langs
for code, name in sorted(langs.items()):
    print(code, name)
```

The package ships more word-list files than it loads. Only languages listed in
`res/languages.json` (mirrored by `langs`) are active. A token from an
unsupported language will not match and contributes nothing.

## Pre-tokenising

`get_word_counts` accepts an already-tokenised `list[str]`, which lets you swap
in your own tokeniser (the built-in `tokenize` only lowercases and splits on
spaces, keeping punctuation attached):

```python
import re
from lingua_podre import get_word_counts, get_lang_scores

def words(text):
    return re.findall(r"\w+", text.lower())

toks = words("Olá, o meu nome é João!")   # punctuation stripped
get_word_counts(toks)                      # cleaner matches than the default split
```

`get_lang_scores` and `predict_lang` always tokenise internally with the built-in
splitter, so to use a custom tokeniser end-to-end, call `get_word_counts`
yourself and normalise the counts.

---
[← API](api.md) · [Home](../readme.md) · [OVOS plugin →](opm.md)
