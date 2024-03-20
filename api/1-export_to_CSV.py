#!/usr/bin/python3
"""
Import the Flask class from the flask module
"""
import csv
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

        USER_ID = user['id']
        USERNAME = user['name']
        employeetasks = []

        for task in tasks:
            TASK_COMPLETED_STATUS = task['completed']
            TASK_TITLE = task['title']
            employeetasks.append([str(USER_ID) + "," + USERNAME + "," +
                                  str(TASK_COMPLETED_STATUS) +
                                  "," + TASK_TITLE])
        csvfilename = str(USER_ID) + '.csv'
        with open(csvfilename, 'w', newline='') as file:
            writer = csv.writer(file)
            writer.writerows(employeetasks)
    else:
        print('Employee not found')
