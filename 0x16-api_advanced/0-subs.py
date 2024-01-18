#!/usr/bin/python3
""" module to get subscribers for a given subreddit"""

import requests


def number_of_subscribers(subreddit):
    """functions to get subscribers for a given subreddit"""
    headers = {
            'User-Agent': 'Your-User-Agent-Name'
            }
    url = "https://www.reddit.com/r/{}/about.json".format(subreddit)

    response = requests.get(url, headers=headers)
    try:
        data = response.json()
        return data['data']['subscribers']
    except KeyError:
        return 0
