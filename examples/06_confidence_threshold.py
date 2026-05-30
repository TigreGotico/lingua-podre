"""Example — turn the score distribution into a confident label or "unsure".

Accept the top language only when it clears a probability floor and beats the
runner-up by a margin; otherwise report the text as ambiguous.

Run::

    python examples/06_confidence_threshold.py
"""
from lingua_podre import get_lang_scores, get_word_counts


def confident_label(text: str, floor: float = 0.25, margin: float = 0.05):
    if not get_word_counts(text):
        return None, "no known words"
    ranked = sorted(get_lang_scores(text).items(),
                    key=lambda kv: kv[1], reverse=True)
    top_code, top_p = ranked[0]
    runner_p = ranked[1][1] if len(ranked) > 1 else 0.0
    if top_p >= floor and (top_p - runner_p) >= margin:
        return top_code, f"{top_p:.0%}"
    return None, f"ambiguous (top {top_code} at {top_p:.0%})"


def main() -> None:
    samples = [
        "olá o meu nome é João e gosto muito de música portuguesa",
        "the quick brown fox jumps over the lazy dog",
        "a o e",                         # function words, no real signal
    ]
    for text in samples:
        label, why = confident_label(text)
        print(f"{label!s:6} [{why}] <- {text}")


if __name__ == "__main__":
    main()
