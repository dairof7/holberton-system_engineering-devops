#!usr/bin/python3

"""[task 0, get rest api]
"""
import requests
from sys import argv


def get_user(id):
    """get the user
    Args:
        id (integer: user id]
    """
    data = {'Id': id}
    url = 'https://jsonplaceholder.typicode.com/'
    users = requests.get(url + 'users', params={'id': id}).json()
    name = users[0]['name']
    data = {'Id': id}
    url = 'https://jsonplaceholder.typicode.com/'
    todos = requests.get(url + 'todos', params={'userId': id}).json()
    n = 0
    str_to_print = ''
    for task in todos:
        if task['completed'] is True:
            num_complete += 1
            str_to_print += '\t' + task['title'] + '\n'
    print('Employee {} is done with tasks({}/{}):'.format(name, n, len(todos)))
    print(str_to_print, end='')


if __name__ == '__main__':
    data = get_user(argv[1])
