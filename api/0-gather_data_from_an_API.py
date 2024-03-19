#!/usr/bin/python3
"""
Import the Flask class from the flask module
"""
import requests
import sys

if __name__== '__main__':

    base_url = "https://jsonplaceholder.typicode.com"
    user_ext = "/users/{}".format(sys.argv[1])
    todo_ext = "/todos"

    user_response = requests.get(base_url + user_ext)
    user = user_response.json()
    
    if user:
        tasks_response = requests.get(base_url + user_ext + todo_ext)
        tasks = tasks_response.json()
        
        EMPLOYEE_NAME = user['name']
        TOTAL_NUMBER_OF_TASKS = 0
        NUMBER_OF_DONE_TASKS = 0
        TASKS_LIST = []
        for task in tasks:
            TOTAL_NUMBER_OF_TASKS += 1
            if task['completed'] is True:
                NUMBER_OF_DONE_TASKS += 1
                TASK_TITLE = task['title']
                TASKS_LIST.append('\t ' + TASK_TITLE + '\n')
        employeetasks = ("Employee " + EMPLOYEE_NAME +
                         " is done with tasks(" + str(NUMBER_OF_DONE_TASKS) +
                         "/" + str(TOTAL_NUMBER_OF_TASKS) + "):\n")
        for task in TASKS_LIST:
            employeetasks += task
        print (employeetasks)
    else:
        print('Employee not found')
