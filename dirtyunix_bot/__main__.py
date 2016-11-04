"""Main class for bot."""

import time

import gen
import send

# Delay between tweets in seconds.
DELAY = 3600

if __name__ == "__main__":
    api = send.auth_and_get_api()

    with open("log", "w") as f:
        while True:
            garbage = gen.gen()
            f.write("Tweeting: {}.\n".format(garbage))
            f.flush()

            send.send_tweet(api, garbage)

            f.write("Sleeping for {} seconds.\n".format(DELAY))
            f.flush()
            time.sleep(DELAY)
