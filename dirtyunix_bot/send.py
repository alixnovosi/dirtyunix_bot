import os

import tweepy


def auth_and_get_api():
    """Authenticate with twitter and get access to API."""
    # auth auth auth auth
    SECRETS_DIR = os.path.join(os.path.abspath(os.path.dirname(__file__)), "SECRETS")

    with open(os.path.join(SECRETS_DIR, "CONSUMER_KEY")) as f:
        CONSUMER_KEY = f.read().strip()

    with open(os.path.join(SECRETS_DIR, "CONSUMER_SECRET")) as f:
        CONSUMER_SECRET = f.read().strip()

    with open(os.path.join(SECRETS_DIR, "ACCESS_TOKEN")) as f:
        ACCESS_TOKEN = f.read().strip()

    with open(os.path.join(SECRETS_DIR, "ACCESS_SECRET")) as f:
        ACCESS_SECRET = f.read().strip()

    auth = tweepy.OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
    auth.set_access_token(ACCESS_TOKEN, ACCESS_SECRET)

    api = tweepy.API(auth)

    return api


def send_tweet(api, text):
    """Send tweet using api."""
    api.update_status(text)
