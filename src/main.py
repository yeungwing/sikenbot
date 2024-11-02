"""
Tweets a random quote from `quotes.txt` using the Twitter API.
"""

import os
import random
import requests
import tweepy


def main():
    """Fetches a random quote to tweet."""
    quote = get_quote()
    tweet(quote)


def get_quote():
    """Picks a random quote from `quotes.txt`."""
    with open('../assets/quotes.txt', 'r', encoding='utf-8') as f:
        quotes = f.read()
    return random.choice(quotes.split('---')).strip().lower()


def tweet(quote):
    """Tweets the given quote."""
    consumer_key = os.environ['CONSUMER_KEY']
    consumer_secret = os.environ['CONSUMER_SECRET']
    access_token = os.environ['ACCESS_TOKEN']
    access_token_secret = os.environ['ACCESS_TOKEN_SECRET']

    client_v2 = auth_v2(consumer_key, consumer_secret, access_token,
                        access_token_secret)
    return client_v2.create_tweet(text=quote)


def auth_v2(consumer_key, consumer_secret, access_token, access_token_secret):
    """Authorizes Twitter using the v2 API."""
    return tweepy.Client(consumer_key=consumer_key,
                         consumer_secret=consumer_secret,
                         access_token=access_token,
                         access_token_secret=access_token_secret,
                         return_type=requests.Response)


if __name__ == '__main__':
    main()
