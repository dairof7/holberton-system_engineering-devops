#!/usr/bin/python3

"""[task 1, get and save on csv]
"""
import csv
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
    with open(argv[1] + '.csv', 'w', newline='') as f:
        towrite = csv.writer(f, quoting=csv.QUOTE_ALL)
        for task in todos:
            towrite.writerow([task['userId'], username,
                             task['completed'], task['title']])


if __name__ == '__main__':
    data = get_user(argv[1])
    store_csv(data)
