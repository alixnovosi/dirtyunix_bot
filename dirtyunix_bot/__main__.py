"""Main class for bot."""

import sys
import time
from os import path

import botskeleton

import gen


# Delay between tweets in seconds.
DELAY = 3600


if __name__ == "__main__":
    SECRETS_DIR = path.join(path.abspath(path.dirname(__file__)), "SECRETS")
    BOT_SKELETON = botskeleton.BotSkeleton(SECRETS_DIR, bot_name="dirtyunix_bot", delay=DELAY)

    LOG = botskeleton.set_up_logging()

    while True:
        garbage = gen.gen()

        LOG.info(f"Tweeting: {garbage}.")
        BOT_SKELETON.send(garbage)

        BOT_SKELETON.nap()
