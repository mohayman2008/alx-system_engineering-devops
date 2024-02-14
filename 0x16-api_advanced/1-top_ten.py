#!/usr/bin/python3
'''This script queries the Reddit API and prints the titles
of the first 10 hot posts listed for a given subreddit'''
import requests


def top_ten(subreddit):
    '''Prints the titles of the first 10 hot posts listed
    for a given "subreddit", by querying the Reddit API'''

    url = 'https://www.reddit.com/r/{}/hot.json'.format(subreddit)
    limit = 10  # number of posts to be retreived
    headers = {'user-agent': 'MyApp v.2024'}
    params = {'raw_json': '1', 'limit': str(limit)}
    response = requests.get(url, headers=headers, params=params,
                            allow_redirects=False)
    if response.status_code != 200:
        print(None)
        return
    try:
        result = response.json()
        data = result.get('data')
        if data is None:
            print(None)
            return
        posts = data.get('children')
        if posts is None:
            print(None)
            return
        for post in posts:
            post_data = post.get('data')
            if post_data:
                print(post_data.get('title'))
            else:
                print(None)
    except ValueError:
        print(None)
        return
