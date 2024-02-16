import os

from .lexicon_methods import get_text

LEXICON_DIR = os.path.dirname(os.path.abspath(__file__))

LEXICON_RU = {
    'answers': {
        '/start': get_text(
            LEXICON_DIR, 'ru/answer_texts/start.txt'
        ),
        'if_dog': get_text(
            LEXICON_DIR, 'ru/answer_texts/if_dog.txt'
        ),
        'if_cucumber': get_text(
            LEXICON_DIR, 'ru/answer_texts/if_cucumber.txt'
        ),
    },
    'buttons': {
        'cucumber': get_text(
            LEXICON_DIR, 'ru/button_texts/cucumber.txt'
        ),
        'dog': get_text(
            LEXICON_DIR, 'ru/button_texts/dog.txt'
        )
    }
}
