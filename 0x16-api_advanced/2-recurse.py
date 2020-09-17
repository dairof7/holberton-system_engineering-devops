#!/usr/bin/python3

"""[task 2, all the hot post]
"""
import requests


def recurse(subreddit, hot_list=[], after=None):
    """[print 100 hot post]

    Args:
        subreddit ([string]): [type of subreddit to consult]
        hot_list (list): [list of the titles]. Defaults to [].
    """

    url = 'https://www.reddit.com/r/{}/hot.json'.format(subreddit)
    info = requests.get(url, headers={"User-Agent": "dairof7"},
                        allow_redirects=False,
                        params={'after': after})

    if info.status_code == 200:
        after = info.json()['data']['after']
        if after is None:
            return hot_list

        for post in info.json()['data']['children']:
            hot_list.append(post['data']['title'])
        return recurse(subreddit, hot_list, after)

    else:
        return None


if __name__ == "__main__":
    pass
