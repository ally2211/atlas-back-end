#!/usr/bin/python3
"""
Import the Flask class from the flask module
"""
import json
import requests
import sys

if __name__ == '__main__':

    # Check if the user ID argument is provided
    if len(sys.argv) < 2:
        sys.exit(1)  # Exit the script with an error code

    base_url = "https://jsonplaceholder.typicode.com"
    user_ext = "/users/{}".format(sys.argv[1])
    todo_ext = "/todos"

    user_response = requests.get(base_url + user_ext)
    user = user_response.json()

    tasks_response = requests.get(base_url + user_ext + todo_ext)
    tasks = tasks_response.json()

    USER_ID = user['id']
    USERNAME = user['name']
    employeetasks = []

    if user:
        for task in tasks:
            TASK_COMPLETED_STATUS = task['completed']
            TASK_TITLE = task['title']
            employeetask = [str(USER_ID), USERNAME,
                            str(TASK_COMPLETED_STATUS), TASK_TITLE]
            employeetasks.append(employeetask)
            # Check if stdout is being redirected
            if not sys.stdout.isatty():
                # Print each task to stdout
                print(','.join(employeetask))
        jsonfilename = str(USER_ID) + '.json'
        with open(csvfilename, 'w+', newline='') as file:
            writer = csv.writer(file)
            writer.writerows(employeetasks)
