# {{PROBLEM}} Multi Class Design Recipe

Copy this into a `recipe.md` in your project and fill it out.

## 1. Describe the Problem

_Put or write the user story here. Add any clarifying notes you might have._

As a user
So that I can record my experiences
I want to keep a regular diary

As a user
So that I can reflect on my experiences
I want to read my past diary entries

As a user
So that I can reflect on my experiences in my busy day
I want to select diary entries to read based on how much time I have and my reading speed

As a user
So that I can keep track of my tasks
I want to keep a todo list along with my diary

As a user
So that I can keep track of my contacts
I want to see a list of all of the mobile phone numbers in all my diary entries



## 2. Design the Classes Interfaces

_Include the initializer, public properties, and public methods with all parameters, return values, and side-effects._

Nouns:
Mega-diary - class
Diary entry - class
Task - class
To do list - property within mega-diary
Contacts list - property within mega-diary

Verbs:
Record experiences
Read past experiences
Read best diary entry based on params (time and reading speed)
Store list of tasks -> from task instance (task class) that feeds into method in diary 
    (CLARIFY: doesn't ask for ability to mark tasks as complete etc -> I'm not going to add this capability)
Store list of phone numbers -> from diary entries 
    (CLARIFY: do we want the capacity to add phone numbers too or just scrape them from diary entries? -> I'm going to just scrape them)

```python

class Diary():

    def __init__(self):
        # Parameters:
        #   None
        # Side effects:
        #   Initialises:
                 # diary_entries = []
                 # contact_list = []
                 # todo_list = []
        pass

    def add(self, entry):
        # Parameters:
            # entry: instance of Diary_Entry()
        # Side Effects:
            # Adds entry to diary_entries list
        # Returns:
            # Nothing

    def all(self):
        # Parameters:
            # None
        # Side Effects:
            # None
        # Returns:
            # diary_entries list 


class Diary_Entry():
    # User facing property:
        # title: string
        # contents: string

    def __init__(self, title, contents):
        # Parameters:
            # title: string
            # contents: string
        # Side Effects:
            # Initialises title and contents properties of Diary_Entry() instance
        # Returns:
            # Nothing


class readable_entry_finder():
    def best_entry_to_read(self, wpm, mins):
        # Parameters:
            # wpm - words per minute, integer
            # mins - integer
        # Side Effects:
            # None
        # Returns:
            # Entry from diary_entries list that is the longest entry readable within the parameters given 


class Todo():
    # User facing property:
        # task: string

    def __init__(self, task):
            # Parameters:
            #   task: string representing a job to do
            # Side effects:
            #   Sets the task_name property of the self object
            pass # No code here yet

    def mark_complete(self, task):
            # Parameters:
            #   task: string representing a job to do
            # Side effects:
            #   Sets the task as complete
            # Returns:
                # Nothing
            pass # No code here yet


class todo_list():
    def add_task(self, entry):
        # Parameters:
            # entry: instance of Todo()
        # Side Effects:
            # Adds entry to task_list list
        # Returns:
            # Nothing

    def all_incomplete(self):
        # Parameters:
            # None
        # Side Effects:
            # None
        # Returns:
            # List of all instances of incomplete tasks

    def all_complete(self):
        # Parameters:
            # None
        # Side Effects:
            # None
        # Returns:
            # List of all instances of complete tasks


class phone_number_extractor():
    def __init__(self, diary)
    # Parameters:
            # Instance of Diary()
        # Side Effects:
            # Sets the diary property to the Diary instance 
        # Returns:
            # Nothing

    def get_numbers(self):
        # Parameters:
            # None
        # Side Effects:
            # None
        # Returns:
            # contact_list -> List of all phone numbers mentioned in Diary() instance (all diary entries), if phone number is repeated, only returns it once in the list 


```

## 3. Create Examples as  Integration Tests

_Make a list of examples of how the class will behave in different situations._

``` python

"""
When I add multiple diary entries to Diary(), all()
Returns list of all diary_entry instances, in order they were added
"""
diary = Diary()
entry1 = Diary_Entry("Title 1", "Contents 1")
entry2 = Diary_Entry("Title 2", "Contents 2")
entry3 = Diary_Entry("Title 3", "Contents 3")
diary.add(entry1)
diary.add(entry2)
diary.add(entry3)
diary.all() => [entry1, entry2, entry3]


"""
When I add multiple tasks 
And I don't mark any complete
all_incomplete() lists them out in the order they were added 
"""
task_list = todo_list()
task1 = Todo("Walk the dog")
task2 = Todo("Walk the cat")
task3 = Todo("Walk the frog")
task_list.add(task1)
task_list.add(task2)
task_list.add(task3)
task_list.all_incomplete() => [task1, task2, task3]


"""
When I add multiple tasks 
And I mark one as complete
all_incomplete() lists only incomplete tasks in the order they were added 
"""
task_list = todo_list()
task1 = Todo("Walk the dog")
task2 = Todo("Walk the cat")
task_list.mark_complete(task2)
task3 = Todo("Walk the frog")
task_list.add(task1)
task_list.add(task2)
task_list.add(task3)
task_list.all_incomplete() => [task1, task3]


"""
When I add multiple tasks 
And I mark one as complete
all_complete() lists only complete tasks in the order they were added 
"""
task_list = todo_list()
task1 = Todo("Walk the dog")
task2 = Todo("Walk the cat")
task_list.mark_complete(task2)
task3 = Todo("Walk the frog")
task_list.add(task1)
task_list.add(task2)
task_list.add(task3)
task_list.all_incomplete() => [task2]


"""
When I add multiple diary entries to Diary(), phone_number_extractor()
Returns list of all phone numbers found in the Diary() instance
"""
diary = Diary()
entry1 = Diary_Entry("Title 1", "Phone number 07833383747")
entry2 = Diary_Entry("Title 2", "Phone number 07666252736")
entry3 = Diary_Entry("Title 3", "Phone number")
diary.add(entry1)
diary.add(entry2)
diary.add(entry3)
extractor = phone_number_extractor(diary)
extractor.get_numbers() => ["07833383747", "07666252736"]


"""
When I add a diary entry to Diary(), phone_number_extractor()
Ignores non-valid phone numbers
"""
diary = Diary()
entry1 = Diary_Entry("Title 1", "Phone number 07833383747, 070000000000, 070000000, 07862 000000")
diary.add(entry1)
extractor = phone_number_extractor(diary)
extractor.get_numbers() => ["07833383747"]

"""
When I add a diary entry to Diary(), phone_number_extractor()
Ignores duplicate phone numbers
"""
diary = Diary()
entry1 = Diary_Entry("Title 1", "Phone number 07833383747, 07833383747, 07833383747")
diary.add(entry1)
extractor = phone_number_extractor(diary)
extractor.get_numbers() => ["07833383747"]


"""
When I add one Diary_Entry() instance that is readable, 
With an wpm of 2 and a mins of 2,
readable_entry_finder(),
Returns that diary entry
"""
diary = Diary()
entry1 = Diary_Entry("Title", "one two three four")
diary.add(entry1)
extractor = readable_entry_finder()
extractor.best_entry_to_read(wpm=2, mins=2) => entry1


"""
When I add one Diary_Entry() instance that is not readable, 
With an wpm of 2 and a mins of 2,
readable_entry_finder(),
Returns None
"""
diary = Diary()
entry1 = Diary_Entry("Title", "one two three four five")
diary.add(entry1)
extractor = readable_entry_finder()
extractor.best_entry_to_read(wpm=2, mins=2) => None


"""
When I add multiple Diary_Entry() instances, one that is not readable and one that is readable, 
With an wpm of 2 and a mins of 2,
readable_entry_finder(),
Returns the readable entry
"""
diary = Diary()
entry1 = Diary_Entry("Title", "one two three four five")
diary.add(entry1)
entry2 = Diary_Entry("Title", "one two three four")
diary.add(entry2)
extractor = readable_entry_finder()
extractor.best_entry_to_read(wpm=2, mins=2) => entry2


"""
When I add multiple Diary_Entry() instances, both that are readable, 
With an wpm of 2 and a mins of 2,
readable_entry_finder(),
Returns that diary entry
"""
diary = Diary()
entry1 = Diary_Entry("Title", "one two three")
diary.add(entry1)
entry2 = Diary_Entry("Title", "one two three four")
diary.add(entry2)
extractor = readable_entry_finder()
extractor.best_entry_to_read(wpm=2, mins=2) => entry2


"""
When I add no Diary_Entry() instances,
With an wpm of 2 and a mins of 2,
readable_entry_finder(),
Returns None
"""
diary = Diary()
entry1 = Diary_Entry("Title", "one two three")
diary.add(entry1)
entry2 = Diary_Entry("Title", "one two three four")
diary.add(entry2)
extractor = readable_entry_finder()
extractor.best_entry_to_read(wpm=2, mins=2) => entry2

```
_Encode each example as a test. You can add to the above list as you go._

## 3. Create Examples as  Unit Tests

_Make a list of examples of how the class will behave in different situations._
``` python

# Diary()

"""
Initially, Diary()
Has no entries in entry_list 
"""
diary = Diary()
diary.all() => []


# Diary_Entry()
"""
Instance of Diary_Entry() class initialises title and contents properties
"""
entry1 = Diary_Entry("Title1", "Contents1")
entry1.title = "Title1"
entry1.contents = "Contents1"


# todo_list():
"""
Initially, todo_list() has no incomplete tasks
"""
task_list = todo_list()
task_list.all_incomplete() => []

# todo_list():
"""
Initially, todo_list() has no complete tasks
"""
task_list = todo_list()
task_list.all_complete() => []


# Todo():
"""
When initialised, Todo()
Sets the task_name
"""
task = Todo("Walk the dog")
task_list.task_name() => "Walk the dog"

```

## 4. Implement the Behaviour

_After each test you write, follow the test-driving process of red, green, refactor to implement the behaviour._
