#!/usr/bin/python3

"""[task 0, get rest api]
"""
import requests


def top_ten(subreddit):
    """print the top 10 hot post

    Args:
        subreddit ([string]): [type of subreddit to consult]

    """
    url = 'https://www.reddit.com/r/{}/hot.json?limit=10'.format(subreddit)
    about_info = requests.get(url, headers={"User-Agent": "dairof7"},
                              allow_redirects=False)

    if about_info.status_code == 200:
        for post in about_info.json()['data']['children']:
            print(post['data']['title'])
    else:
        print(None)


if __name__ == "__main__":
    pass
