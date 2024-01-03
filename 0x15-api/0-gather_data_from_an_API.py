#!/usr/bin/python3

"""
    Get data from an APi using requests
"""


from requests_html import HTMLSession
import sys
import json


session = HTMLSession()
user_id = int(sys.argv[1])

# get user data
url = 'https://jsonplaceholder.typicode.com'
user = session.get(f'{url}/users/{user_id}').json()

# get todos
todos = session.get(f'{url}/todos?userId={user_id}').json()

completed = [todo for todo in todos if todo['completed']]
emp_name = user['name']
print(f'Employee {emp_name} is done with tasks({len(completed)}/{len(todos)})')

# Print completed todos
for todo in completed:
    title = todo['title']
    print(f'\t{title}')
