"""Example — list the active languages and resolve names to codes.

Run::

    python examples/05_languages.py
"""
from lingua_podre import langs, lang_codes, stopwords


def main() -> None:
    print(f"active languages: {len(langs)}")
    for code, name in sorted(langs.items()):
        loaded = len(stopwords.get(code, []))
        print(f"  {code}  {name:<12} ({loaded} words loaded)")

    print()
    print("portuguese ->", lang_codes["portuguese"])
    print("pt ->", langs["pt"])


if __name__ == "__main__":
    main()
