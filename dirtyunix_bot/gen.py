"""Object for generating random sentences according to some grammar rules."""
import random

import botskeleton

import tokens


def gen():
    """Create random sentence."""
    debug = False

    phrase = []

    max_len = random.choice(range(30, 141))
    sentence_len = 0

    token = tokens.START
    while True:
        if debug:
            phrase.append(f"[{token}]")

        # Invisible tokens - only show if debugging.
        # These both start a new phrase.
        if token in [tokens.START, tokens.IMPLICIT_COMMA]:
            token = random.choice(tokens.FOLLOW_RULES[tokens.START])

        # END is end.
        elif token == tokens.END:
            break

        # Explicit break - show break and start a new phrase.
        elif token == tokens.BREAK:
            phrase.append(tokens.BREAK)
            sentence_len += len(tokens.BREAK) + 1

            token = tokens.START

        # Any other tokens.
        else:
            next = botskeleton.random_line(tokens.FILES[token])

            # Stay below max length.
            if len(next) + sentence_len + 1 > max_len:
                break

            else:
                phrase.append(next)
                sentence_len += len(next) + 1
                token = random.choice(tokens.FOLLOW_RULES[token])

    result = " ".join(phrase).strip()

    if result[-1] == tokens.BREAK:
        result = result[:-1].strip()

    return result
