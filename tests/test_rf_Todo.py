from lib.rf_Todo import *

"""
When initialised, Todo()
Sets the task_name and sets the complete status to incomplete
"""
def test_Todo_initialises_task_name_and_incomplete_status():
    task1 = Todo("Walk the dog")
    assert task1.task_name == "Walk the dog"
    assert task1.complete == False

"""
Given a task, mark_complete()
Sets the complete status to complete
"""
def test_mark_complete_changes_status_to_complete():
    task1 = Todo("Walk the dog")
    task1.mark_complete()
    assert task1.complete == True

