#!/usr/bin/python3
'''This script queries the Reddit API and returns a list containing
the titles of all hot articles for a given subreddit'''
import requests


def recurse(subreddit, hot_list=None):
    '''Returns a list containing the titles of all hot articles
    for a given "subreddit", by querying the Reddit API'''

    if hot_list is None:
        hot_list = []

    url = 'https://www.reddit.com/r/{}/hot.json'.format(subreddit)
    limit = 100  # Maximum number of posts to be retreived
    headers = {'user-agent': 'MyApp v.2023'}
    params = {'raw_json': '1', 'limit': str(limit)}
    if len(hot_list):
        params['after'] = hot_list[-1]['name']
    response = requests.get(url, headers=headers, params=params,
                            allow_redirects=False)
    if response.status_code != 200:
        return None
    try:
        results = response.json()
        data = results.get('data')
        if data is None:
            return None
        posts = data.get('children')
        if posts is None:
            return None

        for post in posts:
            post_data = post.get('data')
            if post_data:
                hot_list.append(post_data)

        if not len(posts):
            if not len(hot_list):
                return None
            else:
                return [post.get('title') for post in hot_list]
        return recurse(subreddit, hot_list)

    except ValueError:
        return None
