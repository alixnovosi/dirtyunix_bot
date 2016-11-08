"""Main class for bot."""

import logging
import sys
import time
from logging.handlers import RotatingFileHandler

import tweepy

import gen
import send

# Delay between tweets in seconds.
DELAY = 3600


def set_up_logging():
    """Set up proper logging."""
    logger = logging.getLogger("root")
    logger.setLevel(logging.DEBUG)

    # Log everything verbosely to a file.
    file_handler = RotatingFileHandler(filename="log", maxBytes=1024000000, backupCount=10)
    verbose_form = logging.Formatter(fmt="%(asctime)s - %(levelname)s - %(module)s - %(message)s")
    file_handler.setFormatter(verbose_form)
    file_handler.setLevel(logging.DEBUG)
    logger.addHandler(file_handler)

    # Provide a stdout handler logging at INFO.
    stream_handler = logging.StreamHandler(sys.stdout)
    simple_form = logging.Formatter(fmt="%(message)s")
    stream_handler.setFormatter(simple_form)
    stream_handler.setLevel(logging.INFO)

    logger.addHandler(stream_handler)

    return logger

if __name__ == "__main__":
    api = send.auth_and_get_api()

    LOG = set_up_logging()

    while True:
        garbage = gen.gen()
        LOG.info("Tweeting: {}.".format(garbage))

        try:
            send.send_tweet(api, garbage)

        except tweepy.error.TweepError as e:

            if e.message == "Status is a duplicate.":
                LOG.info("Tweepy duplicate tweet error. Trying to tweet again.")
                LOG.debug("code: {}".format(e.code()))
                LOG.debug("message: {}".format(e.message()))
                continue

            LOG.error("Unhandled Tweepy error!")
            LOG.error("code: {}".format(e.code()))
            LOG.error("message: {}".format(e.message()))
            LOG.critical("Unhandled error, breaking.")
            break

        LOG.info("Sleeping for {} seconds.".format(DELAY))
        time.sleep(DELAY)
