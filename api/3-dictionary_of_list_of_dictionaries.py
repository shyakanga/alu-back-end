#!/usr/bin/python3
"""
Fetches TODO list progress for all employees from an API
and exports the data in JSON format.
"""
import json
import requests


if __name__ == "__main__":
    base_url = "https://jsonplaceholder.typicode.com"

    users = requests.get(f"{base_url}/users").json()
    todos = requests.get(f"{base_url}/todos").json()

    user_dict = {user.get("id"): user.get("username") for user in users}
    all_todos = {str(u_id): [] for u_id in user_dict.keys()}

    for todo in todos:
        user_id = todo.get("userId")
        if user_id in user_dict:
            all_todos[str(user_id)].append({
                "username": user_dict.get(user_id),
                "task": todo.get("title"),
                "completed": todo.get("completed")
            })

    with open("todo_all_employees.json", mode="w") as json_file:
        json.dump(all_todos, json_file)
