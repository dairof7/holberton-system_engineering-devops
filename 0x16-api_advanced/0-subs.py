#!/usr/bin/python3

"""[task 0, get rest api]
"""
import requests


def number_of_subscribers(subreddit):
    """returns the number of subscribers

    Args:
        subreddit ([string]): [type of subreddit to consult]

    Returns:
        [int]: [# of subscribers]
    """
    url = 'https://www.reddit.com/r/{}/about.json'.format(subreddit)
    about_info = requests.get(url, headers={"User-Agent": "dairof7"},
                              allow_redirects=False)
    if about_info.status_code == 200:
        return about_info.json()['data']['subscribers']
    else:
        return 0


if __name__ == "__main__":
    pass
