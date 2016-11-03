import os
import random

import util

HERE = os.path.abspath(os.path.dirname(__file__))


def gen_grammar():
    """Generate using some grammar rules."""
    phrase = []

    VERB = "verbs"
    NOUN = "nouns"
    ADJEC = "adjectives"
    ADV = "adverbs"
    INTERJ = "interjections"
    QUEST = "questions"
    IMPLICIT_COMMA = ","
    BREAK = ";"
    END = "END"
    START = "START"

    DEBUG = False

    files = {VERB: os.path.join(HERE, "verbs"),
             NOUN: os.path.join(HERE, "nouns"),
             ADJEC: os.path.join(HERE, "adjectives"),
             ADV: os.path.join(HERE, "adverbs"),
             INTERJ: os.path.join(HERE, "interjections"),
             QUEST: os.path.join(HERE, "questions")
             }

    follow_rules = {VERB: [ADJEC, NOUN],
                    NOUN: [ADV, BREAK, END],
                    ADJEC: [ADJEC, NOUN],
                    ADV: [NOUN],
                    INTERJ: [INTERJ, BREAK, END],
                    START: [VERB, INTERJ, QUEST],
                    QUEST: [ADJEC, NOUN]
                    }

    PHRASE_LEN = random.choice(range(30, 141))

    type = START
    done = False
    while not done:
        if DEBUG:
            phrase.append("[{}]".format(type))

        # Invisible tokens - only show if debugging.
        # These both start a new sentence or phrase.
        if type in [START, IMPLICIT_COMMA]:
            type = random.choice(follow_rules[START])

        elif type == END:
            break

        elif type == BREAK:
            phrase.append(BREAK)
            type = START

        else:
            phrase.append(util.random_line(files[type]))
            last = phrase[-1]
            type = random.choice(list(filter(lambda x: x != last, follow_rules[type])))

        # Try to keep under PHRASE_LEN.
        total_len = len(" ".join(phrase))
        if total_len > PHRASE_LEN:
            break

    result = " ".join(phrase)

    if result[-1] == BREAK:
        result = result[:-1]

    # TODO need to handle breaking too late and having > PHRASE_LEN.

    return result

if __name__ == "__main__":
    for i in range(8):
        print(gen_grammar())
