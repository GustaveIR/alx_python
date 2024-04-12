#!/usr/bin/python3
"""
Checks student output for returning info from REST API
"""

import requests
import sys
import os

users_url = "https://jsonplaceholder.typicode.com/users"
todos_url = "https://jsonplaceholder.typicode.com/todos"


def check_tasks(id):
    """ Fetch user name, number of tasks """

    resp = requests.get(todos_url).json()

    filename = 'student_output'
    count = 0
    if os.path.exists(filename):
        with open(filename, 'r') as f:
            next(f)
            for line in f:
                count += 1
                if line.startswith('\t ') and line.endswith('\n'):
                    print("Task {} Formatting: OK".format(count))
                else:
                    print("Task {} Formatting: Incorrect".format(count))
    else:
        print(f"File {filename} not found!")


if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python3 script_name.py <employee_id>")
        sys.exit(1)

    check_tasks(int(sys.argv[1]))
