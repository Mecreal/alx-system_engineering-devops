#!/usr/bin/python3
"""Module to query the Reddit API and print top 10 hot posts titles."""
import requests


def top_ten(subreddit):
    """
    queries the Reddit API and prints the titles of the first 10 hot posts
    """
    headers = {"User-Agent": "Frocuts"}
    endpoint = "http://reddit.com/r/{}/hot.json?limit=10"
    subs = r.get(endpoint.format(subreddit), headers=headers)
    if subs.status_code != 200:
        print(None)
        return 0
    subs = subs.json()
    if subs["kind"] == "Listing":
        for data in subs["data"]["children"]:
            print(data["data"]["title"])
    else:
        print(None)


if __name__ == '__main__':
    import sys
    if len(sys.argv) < 2:
        print("Please pass an argument for the subreddit to search.")
    else:
        top_ten(sys.argv[1])
