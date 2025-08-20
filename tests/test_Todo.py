from lib.Todo import *

"""
Instance of Todo() class initialises a task_name property
"""
def test_Todo_initialises_task_name():
    task1 = Todo("Walk the dog")
    task1.task_name = "Walk the dog"