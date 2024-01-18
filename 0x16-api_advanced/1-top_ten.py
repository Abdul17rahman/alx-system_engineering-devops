#!/usr/bin/python3
""" module for a function that queries reddit subscriber"""


import requests


def top_ten(subreddit):
    """ Function to return the No of Subs"""
    url = "https://www.reddit.com/r/{}/hot.json".format(subreddit)

    params = {'limit': 10}
    headers = {'User-Agent': 'Myserver/1.0'}

    response = requests.get(url, headers=headers, params=params)

    if response.status_code == 200:
        try:
            subreddit_data = response.json()

            for post in subreddit_data["data"]["children"]:
                print(post['data']['title'])
        except KeyError:
            print(None)
            return
    else:
        print(None)
        return
