#!/usr/bin/python3
'''This script uses {JSON} Placeholder API to return information about
the tasks of an employee with an identifier <ID>, exported as '<ID>.json' file
'''
import json
import requests
from sys import argv


def main():
    '''Main function'''
    if len(argv) < 2:
        return None

    id = argv[1]
    url = 'https://jsonplaceholder.typicode.com/users/{}'.format(id)
    response = requests.get(url)
    try:
        user = response.json()
        if user and not isinstance(user, dict):
            return None
        username = user.get('username', None)
        if username is None:
            return None
    except ValueError:
        print("Not a valid JSON")
        return None

    url += '/todos'
    response = requests.get(url)
    try:
        todos = response.json()
        if todos and not isinstance(todos, list):
            return None
    except ValueError:
        print("Not a valid JSON")
        return None

    tasks = [{"task": todo.get('title'), "completed": todo.get('completed'),
              "username": username}
             for todo in todos]
    out_dict = {id: tasks}

    with open(id + '.json', 'w') as f:
        json.dump(out_dict, f)


if __name__ == "__main__":
    main()
