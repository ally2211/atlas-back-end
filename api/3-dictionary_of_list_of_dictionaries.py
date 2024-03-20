#!/usr/bin/python3
"""
Import the Flask class from the flask module
"""
import json
import requests
import sys

if __name__ == '__main__':

    base_url = "https://jsonplaceholder.typicode.com"
    user_ext = "/users"
    todo_ext = "/todos"

    user_response = requests.get(base_url + user_ext)
    users = user_response.json()
    tasks_response = requests.get(base_url + todo_ext)
    tasks = tasks_response.json()
    USER_DICT = {}

    for user in users:
        TASKS = []
        USER_ID = user['id']
        USERNAME = user['username']
        for task in tasks:
            TASK_USERID = task['userId']
            if TASK_USERID == USER_ID:
                TASK_COMPLETED_STATUS = task['completed']
                TASK_TITLE = task['title']
                TASKS.append({
                    'username': USERNAME,
                    'task': TASK_TITLE,
                    'completed': TASK_COMPLETED_STATUS
                })
            # After populating TASKS for the user, assign it to USER_DICT
            USER_DICT[USER_ID] = TASKS
    with open("todo_all_employees.json", "w") as outfile:
        json.dump(USER_DICT, outfile)
