"""Main class for bot."""

import os
import sys
import time

import botskeleton

import gen

# Delay between tweets in seconds.
DELAY = 3600

if __name__ == "__main__":
    SECRETS_DIR = os.path.join(os.path.abspath(os.path.dirname(__file__)), "SECRETS")
    api = botskeleton.BotSkeleton(SECRETS_DIR, bot_name="dirtyunix_bot")

    LOG = botskeleton.set_up_logging()

    while True:
        garbage = gen.gen()
        LOG.info(f"Tweeting: {garbage}.")

        api.send(garbage)

        LOG.info(f"Sleeping for {DELAY} seconds.")
        time.sleep(DELAY)
