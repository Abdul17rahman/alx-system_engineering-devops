#!/usr/bin/python3
""" module for a function that queries reddit subscriber"""


import requests


def top_ten(subreddit):
    """ Function to return the No of Subs"""
    url = "https://www.reddit.com/r/{}/about.json".format(subreddit)

    params = {'limit': 10}
    headers = {'User-Agent': 'Myserver/1.0'}

    response = requests.get(url, headers=headers, params=params)

    if response.status_code == 200:
        try:
            subreddit_data = response.json()

            top = subreddit_data["data"]["post"]
            for data in top:
                print(data)
        except Exception:
            print(None)
            return
    else:
        print(None)
        return
