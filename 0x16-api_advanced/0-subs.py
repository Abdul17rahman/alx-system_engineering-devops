#!/usr/bin/python3
""" module to get subscribers for a given subreddit"""

import requests


def number_of_subscribers(subreddit):
    """functions to get subscribers for a given subreddit"""
    if not subreddit or type(subreddit) is not str:
        return 0

    headers = {
            'User-Agent': 'Your-User-Agent-Name'
            }
    url = "https://www.reddit.com/r/{}/about.json".format(subreddit)

    response = requests.get(url, headers=headers)
    if response.status_code == 200:
        response = response.json()
    else:
        return 0
    return response.get('data', {}).get('subscribers', 0)
