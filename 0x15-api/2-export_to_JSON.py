#!/usr/bin/python3

"""[task 1, get and save on csv]
"""
import requests
from sys import argv
import json


def get_user(id):
    """get the user
    Args:
        id (integer: user id]
    """
    data = {'Id': id}
    url = 'https://jsonplaceholder.typicode.com/'
    users = requests.get(url + 'users', params={'id': id}).json()
    data = {'Id': id}
    todos = requests.get(url + 'todos', params={'userId': id}).json()
    return([users, todos])


def store_csv(data):
    """data to csv

    Args:
        data (list): users and todos
    """

    users = data[0]
    todos = data[1]
    username = users[0]['username']
    info = {}
    list_items = []
    for task in todos:
        list_items.append({
                                'task': task['title'],
                                'completed': task['completed'],
                                'username': username})
    info[task['userId']] = list_items
    with open(str(argv[1]) + '.json', 'w') as f:
        json.dump(info, f)


if __name__ == '__main__':
    data = get_user(argv[1])
    store_csv(data)
