import datetime
import sys
import random

# define a dictionary to store tasks with their IDs as keys
tasks = {}

# function to add a task to the to-do list

def add_task(task_description):
    task_id = generate_task_id()
    tasks[task_id] = {"description": task_description, "created_at": get_current_time(), "completed": False}
    print(f"Task '{task_description}' added with ID '{task_id}'.")

# function to mark a task as completed

def complete_task(task_id):
    if task_id in tasks:
        tasks[task_id]["completed"] = True
        print(f"Task '{tasks[task_id]['description']}' marked as completed.")
    else:
        print("Task not found.")

# function to display the list of tasks

def display_tasks():
    print("To-Do List:")
    for task_id, task_details in tasks.items():
        status = "Completed" if task_details["completed"] else "Pending"
        print(f"ID: {task_id} | Description: {task_details['description']} | Status: {status}")

# function to generate a unique task ID

def generate_task_id():
    return random.randint(1000, 9999)

# function to get the current time

def get_current_time():
    return datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")

# example: usage of the functions
add_task("Buy groceries")
add_task("Complete assignment")
complete_task(1234)
display_tasks()
