from lib.mega_diary import *
import pytest

"""
1. Instance of Mega_Diary() class initialises diary_entries, contact_list and todo_list properties as lists
"""
def test_mega_diary_initialises_3_lists():
    Sarahs_diary = mega_diary()
    assert Sarahs_diary.diary_entries == []
    assert Sarahs_diary.contact_list == []
    assert Sarahs_diary.todo_list == []

"""
2. Given a non-instance, add_diary_entry()
Does not add to diary_entries list
Raises error: can only add diary_entry instances to mega diary!
"""
def test_add_diary_entry_only_accepts_diary_entry_instances():
    Sarahs_diary = mega_diary()
    with pytest.raises(Exception) as e:
        Sarahs_diary.add_diary_entry("This is not an instance")
    assert str(e.value) == "Can only add diary_entry instances to mega diary!"
    assert Sarahs_diary.diary_entries == []

"""
3. If diary_entries list is empty (none have been added), get_all_diary_entries()
Raises error: "No diary entries found!"
"""
def test_get_all_diary_entries_with_empty_entries_list_raises_error():
    Sarahs_diary = mega_diary()
    with pytest.raises(Exception) as e:
        Sarahs_diary.get_all_diary_entries()
    assert str(e.value) == "No diary entries found!"

"""
4. Given a non-instance of Todo(), add_to_do_task()
Does not add the instance to todo_list and raises error: "Can only add Todo instances to Mega Diary!"
"""
def test_add_to_do_task_only_accepts_todo_instances():
    Sarahs_diary = mega_diary()
    with pytest.raises(Exception) as e:
        Sarahs_diary.add_to_do_task("This is not an instance")
    assert str(e.value) == "Can only add Todo instances to Mega Diary!"
    assert Sarahs_diary.todo_list == []

"""
5. If diary_entries list is empty (none have been added), best_entry_to_read()
Raises error: "No diary entries found!"
"""
def test_no_diary_entries_best_entry_raises_error():
    Sarahs_diary = mega_diary()
    with pytest.raises(Exception) as e:
        Sarahs_diary.best_entry_to_read(2, 1)
    assert str(e.value) == "No diary entries found!"

"""
6. If diary_entries list is empty, get_all_phone_numbers()
Returns nothing, raises error: "No diary entries found!"
"""
def test_empty_diary_entries_raises_error_with_get_all_phone_numbers():
    Sarahs_diary = mega_diary()
    with pytest.raises(Exception) as e:
        Sarahs_diary.get_all_phone_numbers()
    assert str(e.value) == "No diary entries found!"