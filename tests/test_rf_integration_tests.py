from lib.rf_Diary import *
from lib.rf_Diary_Entry import *
from lib.rf_todo_list import *
from lib.rf_Todo import *
from lib.rf_phone_number_extractor import *
from lib.rf_readable_entry_finder import *

# INTEGRATION TEST FOR DIARY() AND DIARY_ENTRY()

"""
When I add multiple diary entries to Diary(), all()
Returns list of all diary_entry instances, in order they were added
"""
def test_Diary_adds_and_lists_entries():
    diary = Diary()
    entry1 = Diary_Entry("Title 1", "Contents 1")
    entry2 = Diary_Entry("Title 2", "Contents 2")
    entry3 = Diary_Entry("Title 3", "Contents 3")
    diary.add(entry1)
    diary.add(entry2)
    diary.add(entry3)
    assert diary.all() == [entry1, entry2, entry3]


# INTEGRATION TESTS FOR TODO() AND TODO_LIST()

"""
When I add multiple tasks 
And I don't mark any complete
all_incomplete() lists them out in the order they were added 
"""
def test_todo_list_adds_incomplete_tasks():
    task_list = todo_list()
    task1 = Todo("Walk the dog")
    task2 = Todo("Walk the cat")
    task3 = Todo("Walk the frog")
    task_list.add_task(task1)
    task_list.add_task(task2)
    task_list.add_task(task3)
    assert task_list.all_incomplete() == [task1, task2, task3]


"""
When I add multiple tasks 
And I mark one as complete
all_incomplete() lists only incomplete tasks in the order they were added 
"""
def test_marking_task_completed_removes_task_from_incomplete_list():
    task1 = Todo("Walk the dog")
    task2 = Todo("Walk the cat")
    task2.mark_complete()
    task_list = todo_list()
    task3 = Todo("Walk the frog")
    task_list.add_task(task1)
    task_list.add_task(task2)
    task_list.add_task(task3)
    assert task_list.all_incomplete() == [task1, task3]

"""
When I add multiple tasks 
And I mark one as complete
all_complete() lists only complete tasks in the order they were added 
"""
def test_marking_task_completed_shows_task_in_complete_list():
    task1 = Todo("Walk the dog")
    task2 = Todo("Walk the cat")
    task2.mark_complete()
    task_list = todo_list()
    task3 = Todo("Walk the frog")
    task_list.add_task(task1)
    task_list.add_task(task2)
    task_list.add_task(task3)
    assert task_list.all_incomplete() == [task1, task3]


# INTEGRATION TESTS FOR DIARY() AND PHONE_NUMBER_EXTRACTOR()

"""
When I add multiple diary entries to Diary(), phone_number_extractor()
Returns list of all phone numbers found in the Diary() instance
"""
def test_phone_number_extractor_returns_list_of_phone_numbers():
    diary = Diary()
    entry1 = Diary_Entry("Title 1", "Phone number 07833383747")
    entry2 = Diary_Entry("Title 2", "Phone number 07666252736")
    entry3 = Diary_Entry("Title 3", "Phone number")
    diary.add(entry1)
    diary.add(entry2)
    diary.add(entry3)
    extractor = phone_number_extractor(diary)
    assert extractor.get_numbers() == {"07833383747", "07666252736"} # Return the phone numbers as a set rather than a list


"""
When I add a diary entry to Diary(), phone_number_extractor()
Ignores invalid phone numbers
"""
def test_ignores_invalid_phone_numbers():
    diary = Diary()
    entry1 = Diary_Entry("Title 1", "Phone number 07833383747, 070000000000, 070000000, 07862 000000")
    diary.add(entry1)
    extractor = phone_number_extractor(diary)
    assert extractor.get_numbers() == {"07833383747"}

"""
When I add a diary entry to Diary(), phone_number_extractor()
Ignores duplicate phone numbers
"""
def test_ignores_duplicate_numbers():
    diary = Diary()
    entry1 = Diary_Entry("Title 1", "Phone number 07833383747, 07833383747, 07833383747")
    diary.add(entry1)
    extractor = phone_number_extractor(diary)
    assert extractor.get_numbers() == {"07833383747"}

"""
When I add a diary entry to Diary() that doesn't contain a phone number, phone_number_extractor()
Returns an empty set
"""
def test_returns_empty_set_if_no_numbers_found():
    diary = Diary()
    entry1 = Diary_Entry("Title 1", "Phone number")
    diary.add(entry1)
    extractor = phone_number_extractor(diary)
    assert extractor.get_numbers() == set()


"""
When I add one Diary_Entry() instance that is readable, 
With an wpm of 2 and a mins of 2,
readable_entry_finder(),
Returns that diary entry
"""
def test_readable_entry_finder_returns_readable_entry():
    diary = Diary()
    entry1 = Diary_Entry("Title", "one two three four")
    diary.add(entry1)
    extractor = readable_entry_finder(diary)
    assert extractor.extract_best_entry(wpm=2, mins=2) == entry1


"""
When I add one Diary_Entry() instance that is not readable, 
With an wpm of 2 and a mins of 2,
readable_entry_finder(),
Returns None
"""
def test_readable_entry_finder_only_returns_readable_entry():
    diary = Diary()
    entry1 = Diary_Entry("Title", "one two three four five")
    diary.add(entry1)
    extractor = readable_entry_finder(diary)
    extractor.extract_best_entry(wpm=2, mins=2) == None


"""
When I add multiple Diary_Entry() instances, one that is not readable and one that is readable, 
With an wpm of 2 and a mins of 2,
readable_entry_finder(),
Returns the readable entry
"""
def test_readable_entry_finder_returns_readable_entry_from_multiple_entries():
    diary = Diary()
    entry1 = Diary_Entry("Title", "one two three four five")
    diary.add(entry1)
    entry2 = Diary_Entry("Title", "one two three four")
    diary.add(entry2)
    extractor = readable_entry_finder(diary)
    assert extractor.extract_best_entry(wpm=2, mins=2) == entry2


"""
When I add multiple Diary_Entry() instances, both that are readable, 
With an wpm of 2 and a mins of 2,
readable_entry_finder(),
Returns the longer diary entry
"""
def test_readable_entry_finder_returns_longest_entry():
    diary = Diary()
    entry1 = Diary_Entry("Title", "one two three")
    diary.add(entry1)
    entry2 = Diary_Entry("Title", "one two three four")
    diary.add(entry2)
    extractor = readable_entry_finder(diary)
    assert extractor.extract_best_entry(wpm=2, mins=2) == entry2


"""
When I add no Diary_Entry() instances,
With an wpm of 2 and a mins of 2,
readable_entry_finder(),
Returns None
"""
def test_no_readable_entries_returns_none():
    diary = Diary()
    entry1 = Diary_Entry("Title", "one two three")
    diary.add(entry1)
    entry2 = Diary_Entry("Title", "one two three four")
    diary.add(entry2)
    extractor = readable_entry_finder(diary)
    assert extractor.extract_best_entry(wpm=1, mins=1) == None