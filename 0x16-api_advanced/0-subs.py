#!/usr/bin/python3
"""
Queries the Reddit API and returns the number of subscribers for a given subreddit.
If the subreddit is invalid, it returns 0.
"""


import requests


def number_of_subscribers(subreddit):
    """
    Returns the number of subscribers for a given subreddit.
    If the subreddit is invalid, return 0.
    """
    url = f"https://www.reddit.com/r/{subreddit}/about.json"
    headers = {'User-Agent': 'by u/mecreal'}

    response = requests.get(url, headers=headers)

    if response.status_code == 200:
        data = response.json()
        return data['data']['subscribers']
    else:
        return 0
