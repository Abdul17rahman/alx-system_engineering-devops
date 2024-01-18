#!/usr/bin/python3
""" module to get subscribers for a given subreddit"""

import requests


def number_of_subscribers(subreddit):
    """functions to get subscribers for a given subreddit"""
    if not subreddit:
        return 0

    headers = {
            'User-Agent': 'Your-User-Agent-Name'
            }
    url = "https://www.reddit.com/r/{}/about.json".format(subreddit)

    response = requests.get(url, headers=headers, allow_redirects=False)
    
    if response.status_code == 200:
        try:
            data = response.json()
            return data['data']['subscribers']
        except KeyError:
            return 0
    else:
        return 0
