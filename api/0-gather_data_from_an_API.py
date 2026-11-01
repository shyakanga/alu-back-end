#!/usr/bin/python3
"""
For a given employee ID,
this module returns information about his/her TODO list progress.
"""
import requests
import sys


def TodoProgress(empId):
    base_url = "https://jsonplaceholder.typicode.com"

    user_endpoint = f"{base_url}/users"
    todos_endpoint = f"{base_url}/todos"

    users_response = requests.get(user_endpoint).json()

    our_user = [
        user.get("name") for user in users_response
        if user.get("id") == empId
        ]

    todos_response = requests.get(todos_endpoint).json()
    our_user_todos = [
        todo for todo in todos_response
        if todo.get("userId") == empId]
    completed_todos = [
        c_todo for c_todo in our_user_todos if c_todo.get("completed") is True
    ]

    user_name = our_user[0]
    num_c_tasks = len(completed_todos)
    num_total_tasks = len(our_user_todos)
    completed_todos_titles = [todo.get("title") for todo in completed_todos]
    task_titles = '\n\t '.join(completed_todos_titles)

    print(
        f"Employee {user_name} is done with tasks"
        f"({num_c_tasks}/{num_total_tasks}):\n"
        f"\t {task_titles}"
        )


if __name__ == "__main__":
    TodoProgress(int(sys.argv[1]))
