#!/usr/bin/python3
"""
For a given employee ID,
this module returns information about his/her TODO list progress.
"""

import requests
import sys


def TodoProgress(empId):
    base_url = "https://jsonplaceholder.typicode.com"

    user_url = f"{base_url}/users/{empId}"
    user_response = requests.get(user_url).json()
    user_name = user_response.get("name")

    todos_url = f"{base_url}/todos?userId={empId}"
    todos_response = requests.get(todos_url).json()

    completed_todos = [
        todo for todo in todos_response
        if todo.get("completed") is True
        ]

    num_c_tasks = len(completed_todos)
    num_total_tasks = len(todos_response)

    print(
        f"Employee {user_name} is done with tasks("
        f"{num_c_tasks}/{num_total_tasks}):"
        )

    for task in completed_todos:
        print(f"\t {task.get('title')}")


if __name__ == "__main__":
    TodoProgress(int(sys.argv[1]))
