#!/usr/bin/python3
"""
    Get data from an API - json

    a Python script that, using this REST API,
    for a given employee ID, and exports it to a json.
"""


if __name__ == "__main__":
    import json
    import requests
    import sys

    user_id = int(sys.argv[1])
    url = 'https://jsonplaceholder.typicode.com'

    def get_user(_id, _url):
        """ Function that gets user data """
        return requests.get(f'{_url}/users/{_id}').json()

    def get_todos(_id, _url):
        """ Fuction that todo data"""
        return requests.get(f'{_url}/todos?userId={_id}').json()

    user = get_user(user_id, url)
    todos = get_todos(user_id, url)
    emp_name = user.get('username')
    filename = f'{user_id}.json'

    with open(filename, 'w') as user_json_file:
        task_by_user = {}
        for todo in todos:
            userId = todo.get('userId')
            task_by_user[userId] = task_by_user.get(userId, [])

            task_by_user[userId].append({
                'task': todo.get('title'),
                'completed': todo.get('completed'),
                'username': emp_name
            })

        user_json_file.write(json.dumps(task_by_user, indent=2))
