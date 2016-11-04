"""Main class for bot."""

import time

import tweepy

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

            try:
                send.send_tweet(api, garbage)

            except tweepy.error.TweepError as e:

                f.write("Tweepy error!\n")
                f.write("code: {}\n".format(e.code()))
                f.write("message: {}\n".format(e.message()))
                f.flush()

                f.write("Unhandled error, breaking.\n")
                f.flsuh()
                break

                if e.message == "Status is a duplicate.":
                    continue

            f.write("Sleeping for {} seconds.\n".format(DELAY))
            f.flush()
            time.sleep(DELAY)
