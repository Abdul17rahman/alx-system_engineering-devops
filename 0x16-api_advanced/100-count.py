#!/usr/bin/python3
"""
This module provides a recursive function that queries the Reddit API,
parses the title of all hot articles, and prints a sorted count
of given keywords (case-insensitive, delimited by spaces.
Javascript should count as javascript, but java should not).
"""


def print_all(words):
    """
    print_all: This function prints all the element in the word dict
            in descending order of value.
    Args:
        words (dict): A dictionary of words and counts
    Return:
        None
    """
    key_list = sorted(words, key=words.get, reverse=True)
    for i in range(len(key_list) + 1):
        word = key_list[i]
        if words[word] != 0:
            print('{}: {}'.format(word, words[word]))


def count_words(subreddit, word_list, title_list=[], after=None):
    """
    count_words: This function queries the Reddit API recursively
            then prints a sorted count of given keywords in the
            title.
    Args:
        subreddit (str): The api subreddit to send a get request to.
    Return:
        word counts in all the posts
    """

    import requests

    if (after is None and len(title_list) != 0):
        # Create a dictionary for word counts
        word_count = {}
        for word in word_list:
            count = 0
            for title in title_list:
                count += title.count(word)
            # if similar word(case-insensitive) is searched
            if word.lower() in word_count:
                word_count[word.lower()] += count
            else:
                word_count[word.lower()] = count
        print_all(word_count)
        return

    url = 'https://www.reddit.com/r/{}/hot.json'.format(subreddit)
    headers = {'User-Agent': 'MyServer/1.0'}
    params = {'after': after}

    response = requests.get(url, headers=headers, params=params)
    if response.status_code != 200:
        return None
    try:
        hot_posts = response.json()['data']['children']
        after = response.json()['data']['after']
        titles = [x['data']['title'] for x in hot_posts]
        title_list.extend(titles)
        count_words(subreddit, word_list, title_list, after)
        return
    except IndexError:
        return None
