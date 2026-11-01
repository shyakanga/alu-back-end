#!/usr/bin/python3
"""
Fetches information about an employee's TODO list progress from an API
and exports the data in JSON format.
"""
import json
import requests
import sys


if __name__ == "__main__":
    if len(sys.argv) > 1:
        emp_id = sys.argv[1]
        base_url = "https://jsonplaceholder.typicode.com"

        user_url = f"{base_url}/users/{emp_id}"
        user_response = requests.get(user_url).json()
        username = user_response.get("username")

        todos_url = f"{base_url}/todos"
        todos_response = requests.get(
            todos_url, params={"userId": emp_id}
        ).json()

        tasks_list = []
        for task in todos_response:
            tasks_list.append({
                "task": task.get("title"),
                "completed": task.get("completed"),
                "username": username
            })

        json_data = {emp_id: tasks_list}
        filename = f"{emp_id}.json"

        with open(filename, mode='w') as json_file:
            json.dump(json_data, json_file)
