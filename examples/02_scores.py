"""Example — read the full normalised score distribution, not just the winner.

Run::

    python examples/02_scores.py
"""
from lingua_podre import get_lang_scores


def main() -> None:
    text = "olá o meu nome é João e gosto de música"
    scores = get_lang_scores(text)          # values sum to 1

    print(f"text: {text}")
    print(f"languages that matched: {len(scores)}")
    ranked = sorted(scores.items(), key=lambda kv: kv[1], reverse=True)
    for code, prob in ranked[:5]:
        bar = "#" * round(prob * 40)
        print(f"  {code}  {prob:6.1%}  {bar}")


if __name__ == "__main__":
    main()
