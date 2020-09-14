#!/usr/bin/python3

"""[task 3, get and save on json]
"""
import json
import requests


def get_user():
    """get the user
    Args:
        id (integer: user id]
    """
    url = 'https://jsonplaceholder.typicode.com/'
    users = requests.get(url + 'users').json()
    todos = requests.get(url + 'todos').json()
    return([users, todos])


def store_csv(data):
    """data to csv

    Args:
        data (list): users and todos
    """

    users = data[0]
    todos = data[1]
    info = {}
    list_items = []
    idx = todos[0]['userId']
    for task in todos:
        username = users[task['userId'] - 1]['username']
        if task['userId'] != idx:
            list_items = []
            idx = task['userId']
        list_items.append({
                                'username': username,
                                'task': task['title'],
                                'completed': task['completed']})
        info[task['userId']] = list_items
    with open('todo_all_employees' + '.json', 'w') as f:
        json.dump(info, f)


if __name__ == '__main__':
    data = get_user()
    store_csv(data)
