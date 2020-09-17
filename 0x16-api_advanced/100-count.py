#!/usr/bin/python3

"""[task 2, all the hot post]
"""
import requests


def count_words(subreddit, word_list, after=None, count={}):
    """[print 100 hot post]

    Args:
        subreddit ([string]): [type of subreddit to consult]
        hot_list (list): [list of the titles]. Defaults to [].
    """
    url = 'https://www.reddit.com/r/{}/hot.json'.format(subreddit)
    info = requests.get(url, headers={"User-Agent": "dairof7"},
                        allow_redirects=False,
                        params={'after': after})
    if after is None:
        for word in word_list:
            count[word] = 0

    if info.status_code == 200:
        after = info.json()['data']['after']
        if after is None:
            for word, value in count.items():
                if value != 0:
                    print('{}: {}'.format(word, value))
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
