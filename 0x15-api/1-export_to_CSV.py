#!/usr/bin/python3
'''This script uses {JSON} Placeholder API to return information about
the task of an employee with an identifier <ID>, exported as '<ID>.csv' file
'''
import csv
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

    with open(id + '.csv', 'w', newline='') as f:
        fields = ["id", "username", "task_status", "task_title"]
        # writer = csv.DictWriter(f, fieldnames=fields, quoting=csv.QUOTE_NONNUMERIC)
        writer = csv.DictWriter(f, fieldnames=fields)

        row_dict = {'id': id, 'username': username}
        for todo in todos:
            row_dict['task_status'] = todo.get('completed')
            row_dict['task_title'] = todo.get('title')
            writer.writerow(row_dict)


if __name__ == "__main__":
    main()
