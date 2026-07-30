# Quickstart

`lingua_podre` is a word-list language detector in pure Python. It scores a piece
of text by counting how many of its tokens appear in per-language stopword and
top-word lists, normalises those counts to probabilities, and returns the most
likely language code. It uses no model, needs no download, and needs no
network. The word lists ship inside the package.

## 1. Install

```bash
pip install lingua_podre        # from PyPI
pip install -e .                # from a checkout
```

There are zero runtime dependencies. The OVOS plugin entry point
([opm.md](opm.md)) also needs `ovos-plugin-manager`, but the detector
functions themselves do not.

## 2. The one idea

Every supported language has a bundled list of common words. Tokenise the input,
count how many tokens land in each language's list, and the language with the
most hits wins. Counts are normalised so the scores for a single text sum to 1.

```python
from lingua_podre import predict_lang, get_lang_scores

print(predict_lang("olá o meu nome é João"))
# ['pt']
print(predict_lang("hello my name is Bob"))
# ['en']
```

`predict_lang` returns a **list** of [ISO 639-1] codes, not a single string,
because two languages can tie for the top score.

## 3. First real call

```python
from lingua_podre import predict_lang, get_lang_scores

text = "olá o meu nome é João"
print(predict_lang(text))       # ['pt']
print(get_lang_scores(text))    # {'pt': 0.28..., 'ro': 0.14..., 'it': 0.14..., ...}
```

`get_lang_scores` gives you the full normalised distribution over the languages
that matched at least one token. Languages with no matches do not appear in the
dict. The values sum to 1.

## 4. The gotcha you will hit first

If **none** of the tokens match any list (short text, a name, an emoji, or a
language that is not bundled), there is nothing to score. `get_lang_scores`
returns an empty dict and `predict_lang` raises `ValueError` (it calls `max()`
on an empty sequence). Guard it:

```python
from lingua_podre import predict_lang

def safe_predict(text):
    try:
        return predict_lang(text)
    except ValueError:
        return []          # undetectable: no known words matched

print(safe_predict("xyzzy"))    # []
```

See [advanced.md](advanced.md) for the rest of the edge cases.

---
[Home](../readme.md) · [API →](api.md)
