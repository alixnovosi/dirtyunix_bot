"""Tokens used by grammar generator."""

import os

HERE = os.path.abspath(os.path.dirname(__file__))

# Special tokens for start and end of sentences.
END = "END"
START = "START"

# Tokens that can appear in sentences.
# Parts-of-speech things.
VERB = "verbs"
NOUN = "nouns"
ADJEC = "adjectives"
ADV = "adverbs"
INTERJ = "interjections"
QUEST = "questions"

# Special.
# IMPLICIT_COMMA divides phrases, but the comma isn't shown in the output.
# example: yes hello [,] hi [,] hello yes
# Not currently used in dirtyunixbot because (as it turns out) that's really unclear and doesn't
# make for good output.
IMPLICIT_COMMA = ","

# BREAK is an explicit break between phrases, shown as ; in output.
BREAK = ";"

# Files with random lines corresponding to those tokens.
FILES = {
    VERB: os.path.join(HERE, "verbs"),
    NOUN: os.path.join(HERE, "nouns"),
    ADJEC: os.path.join(HERE, "adjectives"),
    ADV: os.path.join(HERE, "adverbs"),
    INTERJ: os.path.join(HERE, "interjections"),
    QUEST: os.path.join(HERE, "questions")
}

# Rules for moving from one token to another.
# Every token reachable from another token should have a corresponding file, or have a way to move
# to one that does in the actual generating logic.
FOLLOW_RULES = {
    VERB: [ADJEC, NOUN],
    NOUN: [ADV, BREAK, END],
    ADJEC: [ADJEC, NOUN],
    ADV: [NOUN],
    INTERJ: [INTERJ, BREAK, END],
    START: [VERB, INTERJ, QUEST],
    QUEST: [ADJEC, NOUN]
}
