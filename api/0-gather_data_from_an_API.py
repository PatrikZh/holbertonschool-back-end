#!/usr/bin/python3
import requests
import sys

if __name__ == '__main__':
    user_id = sys.argv[1]
    url_users = 'https://jsonplaceholder.typicode.com/users/{}'.format(user_id)
    url_todos = 'https://jsonplaceholder.typicode.com/todos?userId={}'.format(user_id)
    
    response_users = requests.get(url_users)
    response_todos = requests.get(url_todos)
    
    user_name = response_users.json().get('name')
    total_number_of_tasks = len(response_todos.json())
    number_of_done_tasks = len([task for task in response_todos.json() if task.get('completed')])
    tasks_titles = '\n\t'.join([task.get('title') for task in response_todos.json() if task.get('completed')])
    
    print('Employee {} is done with tasks({}/{}):'.format(user_name, number_of_done_tasks, total_number_of_tasks))
    print('\t{}'.format(tasks_titles))
