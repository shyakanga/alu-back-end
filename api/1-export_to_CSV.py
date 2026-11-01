#!/usr/bin/python3
#!/usr/bin/python3
"""
Fetches information about an employee's TODO list progress from an API
and exports the data in CSV format.
"""
import csv
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
        todos_response = requests.get(todos_url, params={"userId": emp_id}).json()

        filename = f"{emp_id}.csv"

        with open(filename, mode='w', newline='') as csv_file:
            writer = csv.writer(csv_file, quoting=csv.QUOTE_ALL)
            
            for task in todos_response:
                writer.writerow([
                    emp_id, 
                    username, 
                    task.get("completed"), 
                    task.get("title")
                ])
