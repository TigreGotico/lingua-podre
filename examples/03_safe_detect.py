"""Example — guard undetectable input so predict_lang never raises.

Text with no words in any bundled list makes get_lang_scores divide by zero and
predict_lang raise ValueError. A cheap pre-check on get_word_counts avoids it.

Run::

    python examples/03_safe_detect.py
"""
from lingua_podre import predict_lang, get_word_counts


def safe_predict(text: str) -> list:
    if not get_word_counts(text):       # no token matched anything
        return []
    return predict_lang(text)


def main() -> None:
    samples = [
        "olá mundo",        # detectable Portuguese
        "xyzzy",             # nonsense, nothing matches
        "qwerty zzz",        # nonsense, nothing matches
        "hello there",       # detectable English
    ]
    for text in samples:
        print(f"{safe_predict(text)!s:10} <- {text!r}")


if __name__ == "__main__":
    main()
