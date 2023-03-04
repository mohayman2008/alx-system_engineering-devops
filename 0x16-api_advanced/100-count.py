#!/usr/bin/python3
'''This script queries the Reddit API, parses the title of all hot articles
and prints a sorted count of given keywords (case-insensitive)'''
from functools import cmp_to_key
import re
import requests


def cmp_counts(item_A, item_B):
    '''Compares two two-elements tuples, returns (-1) if the 1st tuple has
    larger 2nd element, in case of equality, it returns (-1) if the 1st
    tuple's first element precedes the other alphabetically'''
    if item_A[1] > item_B[1]:
        return -1
    elif item_A[1] < item_B[1]:
        return 1
    elif item_A[0] < item_B[0]:
        return -1
    return 1


def count_words(subreddit, word_list, after=None, count=0, titles=None):
    '''Parses the title of all hot articles and prints a sorted count of
    given keywords, by querying the Reddit API'''

    if titles is None:
        titles = []
    url = 'https://www.reddit.com/r/{}/hot.json'.format(subreddit)
    limit = 100  # Maximum number of posts to be retreived
    headers = {'user-agent': 'MyApp v.2023'}
    params = {'raw_json': '1', 'limit': str(limit), 'count': str(count)}
    if after is not None:
        params['after'] = after

    response = requests.get(url, headers=headers, params=params,
                            allow_redirects=False)
    if response.status_code != 200:
        return None
    try:
        results = response.json()
        data = results.get('data')
        if data is None:
            return None
        count += data.get('dist', 0)
        after = data.get('after')

        posts = data.get('children')
        if posts is None:
            return None

        for post in posts:
            post_data = post.get('data')
            if post_data:
                titles.append(post_data.get('title'))

        if not after:
            counts = {}
            words = []
            for title in titles:
                words.extend(title.split())
            pile = '  '.join(words)
            for word_raw in word_list:
                word = word_raw.lower()
                w_count = len(re.findall('[\\s\\n]{}[\\s\\n]'.format(word),
                                         pile, re.IGNORECASE))
                if w_count:
                    counts[word] = counts.get(word, 0) + w_count
            sorted_counts = sorted(counts.items(), key=cmp_to_key(cmp_counts))
            for key, val in sorted_counts:
                print('{}: {}'.format(key, val))
            return
        return count_words(subreddit, word_list, after, count, titles)

    except ValueError:
        return None
