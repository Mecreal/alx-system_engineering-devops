#!/usr/bin/python3
"""Module to query Reddit API, parse titles, and count keywords."""
import requests
import re
from collections import Counter


def count_words(subreddit, word_list, after='', word_dict=None):
    """
    Recursively query the Reddit API, parse the titles of hot articles,
    and print a sorted count of given keywords.
    """
    if word_dict is None:
        word_dict = Counter()

    url = f"https://www.reddit.com/r/{subreddit}/hot.json"
    headers = {'User-Agent': 'MyBot/0.0.1'}
    params = {'limit': 100, 'after': after}

    response = requests.get(url, headers=headers, params=params,
                            allow_redirects=False)

    if response.status_code != 200:
        return

    data = response.json()
    posts = data['data']['children']

    for post in posts:
        title = post['data']['title'].lower()
        for word in word_list:
            word = word.lower()
            # Use word boundary to ensure we're counting whole words
            count = len(re.findall(r'\b{}\b'.format(re.escape(word)), title))
            word_dict[word] += count

    after = data['data']['after']
    if after is not None:
        return count_words(subreddit, word_list, after, word_dict)
    else:
        # Sort and print results
        sorted_counts = sorted(word_dict.items(), key=lambda x: (-x[1], x[0]))
        for word, count in sorted_counts:
            if count > 0:
                print(f"{word}: {count}")


if __name__ == '__main__':
    import sys
    if len(sys.argv) < 3:
        print("Usage: {} <subreddit> <list of keywords>".format(sys.argv[0]))
        print("Ex: {} programming 'python java javascript'"
              .format(sys.argv[0]))
    else:
        count_words(sys.argv[1], [x for x in sys.argv[2].split()])
