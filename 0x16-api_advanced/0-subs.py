#!/usr/bin/python3
""" module for a function that queries reddit subscriber"""


import requests


def number_of_subscribers(subreddit):
    """ Function to return the No of Subs"""
    url = "https://www.reddit.com/r/{}/about.json".format(subreddit)

    response = requests.get(url, headers={"User-Agent": "Mozilla/5.0"})

    if response.status_code == 200:
        subreddit_data = response.json()

        return subreddit_data["data"]["subscribers"]
    else:
        return 0
