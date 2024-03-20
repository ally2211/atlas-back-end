#!/usr/bin/python3
"""
Import the Flask class from the flask module
"""
import json
import requests
import sys

if __name__ == '__main__':

    base_url = "https://jsonplaceholder.typicode.com"
    user_ext = "/users/{}".format(sys.argv[1])
    todo_ext = "/todos"

    user_response = requests.get(base_url + user_ext)
    user = user_response.json()

    if user:
        tasks_response = requests.get(base_url + user_ext + todo_ext)
        tasks = tasks_response.json()

        USER_DICT = {}
        TASKS = []
        USER_ID = user['id']
        USERNAME = user['username']
        employeetasks = []
        TOTAL_NUMBER_OF_TASKS = 0
        USER_DICT = {}
        for task in tasks:
            TASK_COMPLETED_STATUS = task['completed']
            TASK_TITLE = task['title']
            TOTAL_NUMBER_OF_TASKS += 1

            TASKS.append({
                'task': TASK_TITLE,
                'completed': TASK_COMPLETED_STATUS,
                'username': USERNAME
            })

        # use USER_ID as key, mapping to the TASKS_LIST
        USER_DICT = {
            USER_ID: TASKS
        }
        jsonfilename = str(USER_ID) + '.json'
        with open(jsonfilename, "w") as outfile:
            json.dump(USER_DICT, outfile)
    else:
        print('Employee not found')
