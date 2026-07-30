# lingua podre

`lingua_podre` is a word-list language detector written in pure Python. It scores
text by counting how many tokens match each language's word list, then returns
the language with the most matches. It uses no model and needs no network
access. The word lists ship inside the package.

## Install

```bash
pip install lingua_podre
```

## Usage

```python
from lingua_podre import predict_lang, get_lang_scores
utterance = "hello my name is Bob"
utterance_pt = "olá o meu nome é João"
print(predict_lang(utterance))
# ['en']
print(get_lang_scores(utterance))
# {'en': 0.2727272727272727, 'pl': 0.09090909090909091, 'cs': 0.09090909090909091, 'sk': 0.09090909090909091, 'hu': 0.09090909090909091, 'sv': 0.09090909090909091, 'nb': 0.09090909090909091, 'da': 0.09090909090909091, 'nl': 0.09090909090909091}
print(predict_lang(utterance_pt))
# ['pt']
print(get_lang_scores(utterance_pt))
# {'pt': 0.2857142857142857, 'ca': 0.07142857142857142, 'pl': 0.07142857142857142, 'cs': 0.07142857142857142, 'ro': 0.14285714285714285, 'it': 0.14285714285714285, 'tr': 0.07142857142857142, 'sk': 0.07142857142857142, 'es': 0.07142857142857142}
```

See [docs/quickstart.md](docs/quickstart.md) for a walkthrough, and
[docs/api.md](docs/api.md) for the full function reference.

## Available languages

The active set covers 28 languages: Arabic, Bulgarian, Catalan, Czech, Danish,
Dutch, English, Finnish, French, German, Gujarati.

Also covered: Hindi, Hebrew, Hungarian, Indonesian, Malaysian, Italian,
Norwegian, Polish, Portuguese, Romanian.

Also covered: Russian, Slovak, Spanish, Swedish, Turkish, Ukrainian,
Vietnamese.

## OVOS plugin

`lingua_podre` also ships an OVOS Plugin Manager language-detector plugin. See
[docs/opm.md](docs/opm.md) for how to use it in an OVOS voice stack.

## Related projects

- [OpenVoiceOS/ovos-plugin-manager](https://github.com/OpenVoiceOS/ovos-plugin-manager): the plugin framework this package's OVOS plugin registers with.

## License

Apache License 2.0. See [LICENSE](LICENSE).