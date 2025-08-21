from lib.rf_todo_list import *

"""
Initially, todo_list() has no incomplete tasks
"""
def test_todo_list_initialises_empty_incomplete_task_list():
    task_list = todo_list()
    assert task_list.all_incomplete() == []

"""
Initially, todo_list() has no complete tasks
"""
def test_todo_list_initialises_empty_complete_task_list():
    task_list = todo_list()
    assert task_list.all_complete() == []