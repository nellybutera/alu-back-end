#!/usr/bin/python3
"""
This is a script that returns information about 
an employee's todo list progress
"""


import requests
import sys


if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage: ./0-gather_data_from_an_API.py <employee_id>")
        sys.exit(1)

    employee_id = int(sys.argv[1])

    user_url = "https://jsonplaceholder.typicode.com/users/{}".format(employee_id)
    todos_url = "https://jsonplaceholder.typicode.com/todos?userId={}".format(
        employee_id)

    user_response = requests.get(user_url)
    todos_response = requests.get(todos_url)

    user_data = user_response.json()
    todos_data = todos_response.json()

    employee_name = user_data.get("name")

    completed_tasks = [t for t in todos_data if t.get("completed") is True]
    total_tasks = len(todos_data)
    done_tasks = len(completed_tasks)

    print("Employee {} is done with tasks({}/{}):"
          .format(employee_name, done_tasks, total_tasks))

    for task in completed_tasks:
        print("\t {}".format(task.get("title")))
