"""Example — inspect the raw signal: tokens and per-language word counts.

Run::

    python examples/04_tokenize_counts.py
"""
from lingua_podre import tokenize, get_word_counts


def main() -> None:
    text = "o meu nome é João e o teu nome é Maria"

    tokens = tokenize(text)             # lowercase, split on spaces
    print("tokens:", tokens)

    counts = get_word_counts(tokens)    # accepts a pre-tokenised list
    ranked = sorted(counts.items(), key=lambda kv: kv[1], reverse=True)
    print("word hits per language:")
    for code, n in ranked:
        print(f"  {code}: {n}")


if __name__ == "__main__":
    main()
