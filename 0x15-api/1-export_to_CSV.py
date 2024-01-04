#!/usr/bin/python3
"""
    Get data from an API - csv

    a Python script that, using this REST API,
    for a given employee ID, and exports it to a csv.
"""


if __name__ == "__main__":
    import csv
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
    filename = f'{user_id}.csv'

    with open(filename, 'w') as user_csv_file:
        csv_writer = csv.writer(user_csv_file, delimiter=',',
                                quotechar='"', quoting=csv.QUOTE_ALL)
        for todo in todos:
            csv_writer.writerow([todo.get('userId'), emp_name,
                                todo.get('completed'), todo.get('title')])
