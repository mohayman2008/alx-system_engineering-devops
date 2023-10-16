#!/usr/bin/python3
'''This script uses {JSON} Placeholder API to return information about
the tasks of all employees, exported as 'todo_all_employees.json' file
'''
import json
import requests
from sys import argv


def main():
    '''Main function'''

    url = 'https://jsonplaceholder.typicode.com/users'
    response = requests.get(url)
    try:
        users = response.json()
        if users and not isinstance(users, list):
            return None
    except ValueError:
        print("Not a valid JSON")
        return None

    out_dict = {}
    for user in users:
        id = user.get('id')
        username = user.get('username')

        url_todos = '{}/{}/todos'.format(url, id)
        response = requests.get(url_todos)
        try:
            todos = response.json()
            if todos and not isinstance(todos, list):
                return None
        except ValueError:
            print("Not a valid JSON")
            return None

        tasks = [{"username": username, "task": todo.get('title'),
                  "completed": todo.get('completed')}
                 for todo in todos]
        out_dict[id] = tasks

    with open('todo_all_employees.json', 'w') as f:
        json.dump(out_dict, f)


if __name__ == "__main__":
    main()
