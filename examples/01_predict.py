"""Example — predict the language of a few short texts.

Run::

    python examples/01_predict.py
"""
from lingua_podre import predict_lang


SAMPLES = [
    "olá o meu nome é João",          # Portuguese
    "hello my name is Bob",            # English
    "hola me llamo Juan",              # Spanish
    "bonjour je suis ravi de vous",    # French
]


def main() -> None:
    for text in SAMPLES:
        # predict_lang returns a list of codes (ties are possible).
        print(f"{predict_lang(text)!s:10} <- {text}")


if __name__ == "__main__":
    main()
