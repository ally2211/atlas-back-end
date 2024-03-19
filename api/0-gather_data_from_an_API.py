#!/usr/bin/python3
"""
Import the Flask class from the flask module
"""
import requests
""" Create an instance of the Flask class. __name__ is the name of module."""
app = flask.Flask(__name__)

"""set strict slashes to false"""
app.url_map.strict_slashes = False


# Use the route() decorator to trigger the function that follows.
@app.route('/<int:user_id>')
def users(user_id):
    # Use requests.get() to fetch data from the external URL.
    response = requests.get('https://jsonplaceholder.typicode.com/users')
    users = response.json()
    response = requests.get('https://jsonplaceholder.typicode.com/todos')
    tasks = response.json()

    # Extract the 'name' from each user and create a list of names
    employeetasks = ""
    EMPLOYEE_ID = user_id
    # Filter the users list for the user with the matching username
    user = next((user for user in users if user['id'] == EMPLOYEE_ID), None)

    if user:
        EMPLOYEE_NAME = user['name']
        TOTAL_NUMBER_OF_TASKS = 0
        NUMBER_OF_DONE_TASKS = 0
        TASKS_LIST = []
        for task in tasks:
            if task['userId'] == EMPLOYEE_ID:
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

        return employeetasks.strip(), 200, {'Content-Type': 'text/plain'}

    else:
        return {'message': 'User not found'}, 404


# Check if not imported as a module
if __name__ == '__main__':
    # host='0.0.0.0' makes the server accessible externally.
    app.run(host='0.0.0.0', port=5000)
