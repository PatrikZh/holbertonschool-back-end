#!/usr/bin/python3
""" Importing and doing api"""
import json
import requests
import sys


if __name__ == "__main__":
    ''' In order for it to work'''
    todos_api = requests.get(
        'https://jsonplaceholder.typicode.com/todos/')
    user_api = requests.get(
        'https://jsonplaceholder.typicode.com/users/{}'.format(sys.argv[1]))
    todo_data = todos_api.text
    user_data = user_api.text
    user = json.loads(user_data)
    todos = json.loads(todo_data)
    stored= []
    all_todos = 0
    for todo in todos:
        if todo['userId'] == user['id']:
            if todo['completed']:
                stored.append(todo)
            all_todos += 1
    print(
        'Employee {} is done with tasks({}/{}):'
        .format(user['name'], len(stored), all_todos), file=sys.stdout)
    for finished_todo in stored:
        print('\t {}'.format(finished_todo['title']), file=sys.stdout)
