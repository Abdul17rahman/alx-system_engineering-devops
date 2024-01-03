#!/usr/bin/python3
"""
Get data from an APi using requests
"""


from requests_html import HTMLSession
from sys import argv
import json


session = HTMLSession()
user_id = int(argv[1])
url = 'https://jsonplaceholder.typicode.com'


if __name__ == "__main__":
    def get_user(user_id, url):
        """ Function that gets user data """
        return session.get(f'{url}/users/{user_id}').json()


    def get_todos(user_id, url):
        """ Fuction that todo data"""
        return session.get(f'{url}/todos?userId={user_id}').json()


    user = get_user(user_id, url)
    todos = get_todos(user_id, url)

    completed = [todo for todo in todos if todo.get('completed')]
    emp_name = user.get('name')
    print(f'Employee {emp_name} is done with tasks({len(completed)}/{len(todos)})')

    for todo in completed:
        title = todo.get('title')
        print(f'\t{title}')
