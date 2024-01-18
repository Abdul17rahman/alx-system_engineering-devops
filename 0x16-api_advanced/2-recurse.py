#!/usr/bin/python3
"""
    This module provides a function that sends a get request to the Reddit API
    with the specified subreddit then process the response and prints all the
    titles of the hot posts listed for a given subreddit
"""


def recurse(subreddit, hot_list=[], after=None):
    """
    recurse: This function queries the Reddit API recursively
    Args:
        subreddit (str): The api subreddit to send a get request to.
    Return: List of all the posts
    """

    import requests

    if (after is None and len(hot_list) != 0):
        return hot_list

    url = 'https://www.reddit.com/r/{}/hot.json'.format(subreddit)
    headers = {'User-Agent': 'MyServer/1.0'}
    params = {'after': after}

    response = requests.get(url, headers=headers, params=params)
    if response.status_code != 200:
        return None
    try:
        hot_posts = response.json()['data']['children']
        after = response.json()['data']['after']
        hot_list.extend(hot_posts)
        recurse(subreddit, hot_list, after)
        return hot_list
    except IndexError:
        return None
