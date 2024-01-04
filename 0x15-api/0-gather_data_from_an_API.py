#!/usr/bin/python3
"""
    Get data from an API

    a Python script that, using this REST API,
    for a given employee ID, returns information
    about his/her TODO list progress.
"""


import requests
from sys import arg


if __name__ == "__main__":
    user_id = int(argv[1])
    url = 'https://jsonplaceholder.typicode.com'

    def get_user(_id, _url):
        """ Function that gets user data """
        return requests.get(f'{_url}/users/{_id}').json()

    def get_todos(_id, _url):
        """ Fuction that todo data"""
        return requests.get(f'{_url}/todos?userId={_id}').json()

    user = get_user(user_id, url)
    todos = get_todos(user_id, url)

    completed = [todo for todo in todos if todo.get('completed')]
    emp_name = user.get('name')
    print('Employee {} is done with tasks({}/{})'
          .format(emp_name, len(completed), len(todos)))

    for todo in completed:
        title = todo.get('title')
        print(f'\t{title}')
