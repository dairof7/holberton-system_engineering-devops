#!/usr/bin/python3

"""[task 2, all the hot post]
"""
from collections import defaultdict
import requests


def count_words(subreddit, word_list, after=None, count=defaultdict(int)):
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
            first_sort = sorted(count.items(), key=lambda x: x[0])
            for k, v in sorted(first_sort, key=lambda x: x[1], reverse=True):
                if v != 0:
                    print('{}: {}'.format(k, v))
            return

        for post in info.json()['data']['children']:
            for word in word_list:
                string = post['data']['title']
                string_split = string.lower().split(' ')
                count[word] += string_split.count(word.lower())
        return count_words(subreddit, word_list, after, count)
    else:
        return


if __name__ == "__main__":
    pass
