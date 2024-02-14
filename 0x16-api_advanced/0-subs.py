#!/usr/bin/python3
'''This script queries the Reddit API and returns the number of total
subscribers for a given subreddit'''
import requests


def number_of_subscribers(subreddit):
    '''Gets the total number of subscribers for a given "subreddit",
    by querying the Reddit API'''

    url = 'https://www.reddit.com/r/{}/about.json'.format(subreddit)
    headers = {'user-agent': 'MyApp v.2024'}
    params = {'raw_json': 1}
    response = requests.get(url, headers=headers, params=params,
                            allow_redirects=False)

    if response.status_code != 200:
        return 0
    try:
        about = response.json()
        data = about.get('data')
        if data is None:
            return 0
        return data.get('subscribers', 0)

    except ValueError:
        return 0
