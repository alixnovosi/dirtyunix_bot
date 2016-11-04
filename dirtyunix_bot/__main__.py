"""Main class for bot."""

import time

import gen
import send

# Delay between tweets in seconds.
DELAY = 3600

if __name__ == "__main__":
    api = send.auth_and_get_api()

    while True:
        garbage = gen.gen()
        print("Tweeting: {}".format(garbage))

        send.send_tweet(api, garbage)

        time.sleep(DELAY)
