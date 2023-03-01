#!/usr/bin/python3
'''This script queries the Reddit API prints the titles
of the first 10 hot posts listed for a given subreddit'''
import requests


def top_ten(subreddit):
    '''prints the titles of the first 10 hot posts listed
    for a given "subreddit", by querying the Reddit API'''

    url = 'https://www.reddit.com/r/{}/hot.json'.format(subreddit)
    limit = 10  # number of posts to be retreived
    headers = {'user-agent': 'MyApp v.2023'}
    params = {'raw_json': '1', 'limit': str(limit)}
    response = requests.get(url, headers=headers, params=params,
                            allow_redirects=False)
    try:
        about = response.json()
        data = about.get('data')
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
        return 0
