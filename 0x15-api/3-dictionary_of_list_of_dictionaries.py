#!/usr/bin/python3
"""
    Get data from an API - json of all tasks

    a Python script that, using this REST API,
    for all users, and exports it to a json.
"""


if __name__ == "__main__":
    import json
    import requests
    import sys

    url = 'https://jsonplaceholder.typicode.com'

    def get_user(_url):
        """ Function that gets user data """
        return requests.get(f'{_url}/users').json()

    def get_todos(_url):
        """ Fuction that todo data"""
        return requests.get(f'{_url}/todos').json()

    all_users = get_user(url)
    all_todos = get_todos(url)
    filename = 'todo_all_employees.json'

    with open(filename, 'w') as user_json_file:
        all_emp_data = {}
        for user in all_users:
            userId = user.get('id')
            user_name = user.get('username')
            todos = requests.get(f'{url}/todos?userId={userId}')

            all_emp_data[userId] = all_emp_data.get(userId, [])

            for todo in todos.json():
                all_emp_data[userId].append({
                    'username': user_name,
                    'task': todo.get('title'),
                    'completed': todo.get('completed'),
                })

        user_json_file.write(json.dumps(all_emp_data, indent=3))
