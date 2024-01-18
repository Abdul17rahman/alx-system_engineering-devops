#!/usr/bin/python3
""" module to get subscribers for a given subreddit"""

import requests


def number_of_subscribers(subreddit):
    """functions to get subscribers for a given subreddit"""
    if subreddit is None or not isinstance(subreddit, str):
        return 0

    headers = {
            'User-Agent': 'Your-User-Agent-Name'
            }
    url = "https://www.reddit.com/r/{}/about.json".format(subreddit)

    response = requests.get(url, headers=headers, allow_redirects=False)
    data = response.json()
    try:
        return data['data']['subscribers']
    except Exception:
        return 0
