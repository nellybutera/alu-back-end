#!/usr/bin/python3
"""
This is a script that returns information about an employee's todo list progress
"""

import requests
import sys

if __name__ == "__main__":
    # Ensure the user provides an employee ID as an argument
    if len(sys.argv) < 2:
        print("Usage: ./0-gather_data_from_an_API.py <employee_id>")
        sys.exit(1)

    employee_id = int(sys.argv[1])  # Convert argument to integer

    # Define API URLs
    user_url = f"https://jsonplaceholder.typicode.com/users/{employee_id}"
    todos_url = f"https://jsonplaceholder.typicode.com/todos?userId={employee_id}"

    # Make GET requests to the API
    user_response = requests.get(user_url)
    todos_response = requests.get(todos_url)

    # Convert responses to Python dictionaries/lists
    user_data = user_response.json()
    todos_data = todos_response.json()

    # Get employee name
    employee_name = user_data.get("name")

    # Filter completed tasks
    completed_tasks = [task for task in todos_data if task.get("completed")]

    # Calculate stats
    total_tasks = len(todos_data)
    done_tasks = len(completed_tasks)

    # Display progress
    print("Employee {} is done with tasks({}/{}):".format(
        employee_name, done_tasks, total_tasks))

    # Print each completed task title
    for task in completed_tasks:
        print("\t {}".format(task.get("title")))
