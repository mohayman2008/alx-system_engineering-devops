#!/usr/bin/python3
'''This script uses {JSON} Placeholder API to return information about
the TODO list progress of an employee with an identifier <ID>
'''
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
        name = user.get('name', None)
        if name is None:
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
        completed = [todo for todo in todos if todo.get('completed')]
    except ValueError:
        print("Not a valid JSON")
        return None

    line = 'Employee {} is done with tasks({}/{}):'
    print(line.format(name, len(completed), len(todos)))
    for todo in completed:
        print('\t {}'.format(todo.get('title')))


if __name__ == "__main__":
    main()
