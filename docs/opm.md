# OVOS plugin

`lingua_podre` ships an OVOS Plugin Manager language detector so the same
word-list engine plugs into an OVOS voice stack without any glue code.

## The class

`lingua_podre.opm.LinguaPodrePlugin` subclasses
`ovos_plugin_manager.templates.language.LanguageDetector` and forwards to the
two top-level functions:

```python
from lingua_podre.opm import LinguaPodrePlugin

detector = LinguaPodrePlugin()
detector.detect("olá o meu nome é João")        # ['pt']   -> predict_lang
detector.detect_probs("olá o meu nome é João")  # {...}    -> get_lang_scores
```

- `detect(text)` returns the top language code(s), the same list `predict_lang`
  produces.
- `detect_probs(text)` returns the normalised score distribution from
  `get_lang_scores`.

Both inherit `predict_lang`/`get_lang_scores` behaviour exactly, including the
exceptions on unmatched text — see
[advanced.md](advanced.md#empty-and-undetectable-input). Guard the input the same
way before handing it to the plugin.

## Entry point

The plugin registers under the OPM language-detector group:

```
ovos-lang-detector-plugin-lingua-podre = lingua_podre.opm:LinguaPodrePlugin
```

Once installed, OVOS discovers it by that name; you select it through your OVOS
language configuration rather than importing it directly.

## Where next

- [api.md](api.md) — the functions the plugin wraps
- [advanced.md](advanced.md) — guarding undetectable input
- [quickstart.md](quickstart.md) — the engine on its own
