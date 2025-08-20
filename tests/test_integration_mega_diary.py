from lib.Diary_Entry import *
from lib.Todo import *
from lib.mega_diary import *
import pytest

"""
1. Given an instance of Diary_Entry(), add_diary_entry()
Adds the instance to diary_entries list
"""
def test_add_diary_entry_uding_diary_entry_instance_adds_successfully():
    Sarahs_diary = mega_diary()
    entry1 = Diary_Entry("Title1", "Contents1")
    Sarahs_diary.add_diary_entry(entry1)
    assert Sarahs_diary.diary_entries == [entry1]

"""
2. Given that diary_entries is not empty, get_all_diary_entries()
Returns diary_entries list, with each entry formatted into "Title: contents" format
"""
def test_get_all_diary_entries_returns_diary_entries_list():
    Sarahs_diary = mega_diary()
    entry1 = Diary_Entry("Title1", "Contents1")
    Sarahs_diary.add_diary_entry(entry1)
    assert Sarahs_diary.get_all_diary_entries() == ["Title1: Contents1"]

"""
3. Given that diary_entries is not empty, get_all_diary_entries()
Returns diary_entries list, with each entry formatted into "Title: contents" format
"""
def test_get_all_diary_entries_returns_diary_entries_list_multiple_entries():
    Sarahs_diary = mega_diary()
    entry1 = Diary_Entry("Title1", "Contents1")
    Sarahs_diary.add_diary_entry(entry1)
    entry2 = Diary_Entry("Title2", "Contents2")
    Sarahs_diary.add_diary_entry(entry2)
    assert Sarahs_diary.get_all_diary_entries() == ["Title1: Contents1", "Title2: Contents2"]

"""
4. Given an instance of Todo(), add_to_do_task()
Adds the instance to todo_list
"""
def test_add_to_do_task_adds_to_to_do_list():
    Sarahs_diary = mega_diary()
    task1 = Todo("Walk the dog")
    Sarahs_diary.add_to_do_task(task1)
    assert Sarahs_diary.todo_list == [task1]

"""
5. Given diary_entries list is not empty, and given a wpm and mins, best_entry_to_read()
Returns the longest entry readable within the parameters given, formatted
"""
def test_best_entry_to_read_returns_longest_readable_entry():
    Sarahs_diary = mega_diary()
    entry1 = Diary_Entry("Title1", "Contents1")
    entry2 = Diary_Entry("Title2", "Contents2 is longer")
    Sarahs_diary.add_diary_entry(entry1)
    Sarahs_diary.add_diary_entry(entry2)
    assert Sarahs_diary.best_entry_to_read(2, 2) == "Title2: Contents2 is longer"

"""
6. Given diary_entries list is not empty, and given a wpm and mins, best_entry_to_read()
Returns the default message if no entries are possible to read within params
"""
def test_best_entry_to_read_returns_default_message():
    Sarahs_diary = mega_diary()
    entry1 = Diary_Entry("Title1", "Contents1 is short")
    entry2 = Diary_Entry("Title2", "Contents2 is a bit longer")
    Sarahs_diary.add_diary_entry(entry1)
    Sarahs_diary.add_diary_entry(entry2)
    assert Sarahs_diary.best_entry_to_read(1, 2) == "No readable entries!"

"""
7. Given a wpm of 0, best_entry_to_read()
Raises error "wpm must be an integer greater than 0!"
"""
def test_wpm_0_best_entry_raises_error():
    Sarahs_diary = mega_diary()
    entry1 = Diary_Entry("Title1", "Contents1")
    entry2 = Diary_Entry("Title2", "Contents2 is longer")
    Sarahs_diary.add_diary_entry(entry1)
    Sarahs_diary.add_diary_entry(entry2)
    with pytest.raises(Exception) as e:
        Sarahs_diary.best_entry_to_read(0, 2)
    assert str(e.value) == "wpm must be an integer greater than 0!"

"""
8. Given wpm not as an integer, best_entry_to_read()
Raises error "You have no time to read!"
"""
def test_non_integer_best_entry_raises_exception():
    Sarahs_diary = mega_diary()
    entry1 = Diary_Entry("Title1", "Contents1")
    entry2 = Diary_Entry("Title2", "Contents2 is longer")
    Sarahs_diary.add_diary_entry(entry1)
    Sarahs_diary.add_diary_entry(entry2)
    with pytest.raises(Exception) as e:
        Sarahs_diary.best_entry_to_read(1.5, 2)
    assert str(e.value) == "wpm must be an integer greater than 0!"

"""
9. Given a mins of 0, best_entry_to_read()
Raises error "You have no time to read!"
"""
def test_no_mins_best_entry_raises_exception():
    Sarahs_diary = mega_diary()
    entry1 = Diary_Entry("Title1", "Contents1")
    entry2 = Diary_Entry("Title2", "Contents2 is longer")
    Sarahs_diary.add_diary_entry(entry1)
    Sarahs_diary.add_diary_entry(entry2)
    with pytest.raises(Exception) as e:
        Sarahs_diary.best_entry_to_read(2, 0)
    assert str(e.value) == "You have no time to read!"

"""
10. Given a mins that is not an integer, best_entry_to_read()
Raises error "Mins must be an integer greater than 0!"
"""
def test_mins_not_integer_best_entry_raises_exception():
    Sarahs_diary = mega_diary()
    entry1 = Diary_Entry("Title1", "Contents1")
    entry2 = Diary_Entry("Title2", "Contents2 is longer")
    Sarahs_diary.add_diary_entry(entry1)
    Sarahs_diary.add_diary_entry(entry2)
    with pytest.raises(Exception) as e:
        Sarahs_diary.best_entry_to_read(2, 2.5)
    assert str(e.value) == "Mins must be an integer greater than 0!"

"""
11. Given that diary_entries is not empty, get_all_phone_numbers()
Returns list of all phone numbers mentioned in all diary entries (no duplicate numbers)
"""
def test_get_all_phone_numbers_returns_list_of_phone_numbers():
    Sarahs_diary = mega_diary()
    entry1 = Diary_Entry("Title1", "Contents1 07383474565")
    entry2 = Diary_Entry("Title2", "Contents2 07191222390")
    Sarahs_diary.add_diary_entry(entry1)
    Sarahs_diary.add_diary_entry(entry2)
    assert Sarahs_diary.get_all_phone_numbers() == ["07383474565", "07191222390"]

"""
12. Given that diary_entries is not empty, get_all_phone_numbers()
Returns list of all phone numbers mentioned in all diary entries (no duplicate numbers)
"""
def test_get_all_phone_numbers_returns_no_duplicates():
    Sarahs_diary = mega_diary()
    entry1 = Diary_Entry("Title1", "Contents1 07383474565")
    entry2 = Diary_Entry("Title2", "Contents2 07383474565")
    Sarahs_diary.add_diary_entry(entry1)
    Sarahs_diary.add_diary_entry(entry2)
    assert Sarahs_diary.get_all_phone_numbers() == ["07383474565"]

"""
13. Given that diary_entries is not empty, but there are no phone numbers in diary_entries, get_all_phone_numbers()
Returns default "No phone numbers found!"
"""
def test_get_all_phone_numbers_returns_message_if_no_numbers_found():
    Sarahs_diary = mega_diary()
    entry1 = Diary_Entry("Title1", "Contents1")
    entry2 = Diary_Entry("Title2", "Contents2")
    Sarahs_diary.add_diary_entry(entry1)
    Sarahs_diary.add_diary_entry(entry2)
    assert Sarahs_diary.get_all_phone_numbers() == "No phone numbers found!"