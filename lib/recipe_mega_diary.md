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

class Todo():
    # User facing property:
        # task: string

    def __init__(self, task):
            # Parameters:
            #   task: string
            # Side effects:
            #   Sets the task_name property of the self object
            pass # No code here yet

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

    def format(self):
        # Parameters:
            # None
        # Side Effects:
            # None
        # Returns:
            # Diary_Entry() instance formatted like: "Title: contents"
    
    def count_words(self):
        # Parameters:
            # None
        # Side Effects:
            # None
        # Returns:
            # Length of Diary_Entry() instance (words)

    def reading_time(self, wpm):
        def format(self):
        # Parameters:
            # wpm - words per minute, integer
        # Side Effects:
            # None
        # Returns:
            # Integer representing time (in mins) it will take to read Diary_Entry() instance at given wpm speed


class Mega_Diary():

    def __init__(self):
        # Parameters:
        #   None
        # Side effects:
        #   Initialises:
                 # diary_entries = []
                 # contact_list = []
                 # todo_list = []
        pass

    def add_diary_entry(self, entry):
        # Parameters:
            # entry: instance of Diary_Entry()
        # Side Effects:
            # Adds entry to diary_entries list
        # Returns:
            # Nothing

    def get_all_diary_entries(self):
        # Parameters:
            # None
        # Side Effects:
            # None
        # Returns:
            # diary_entries list 

    def best_entry_to_read(self, wpm, mins):
        # Parameters:
            # wpm - words per minute, integer
            # mins - integer
        # Side Effects:
            # None
        # Returns:
            # Entry from diary_entries list that is the longest entry readable within the parameters given 

    def add_to_do_task(self, task):
        # Parameters:
            # task: Todo() instance
        # Side Effects:
            # Adds task to todo_list 
        # Returns:
            # Nothing

    def get_all_phone_numbers(self):
        # Parameters:
            # None
        # Side Effects:
            # None
        # Returns:
            # contact_list -> List of all phone numbers mentioned in all diary entries, if phone number is repeated, only returns it once in the list 


```

## 3. Create Examples as Tests

_Make a list of examples of how the class will behave in different situations._

``` python
# _____UNIT TESTS____-> Todo()

# """
# Instance of Todo() class initialises a task_name property
# """
# task1 = Todo("Walk the dog")
# task1.task_name = "Walk the dog"

# _____UNIT TESTS____-> DiaryEntry()
# """
# Instance of Diary_Entry() class initialises title and contents properties
# """
# entry1 = Diary_Entry("Title1", "Contents1")
# entry1.title = "Title1"
# entry1.contents = "Contents1"

# """
# Given a blank string as title, 
# Raises error: "Diary Entries must have a title and contents"
# """
# entry1 = Diary_Entry("", "Contents1")
# => error

# """
# Given a blank string as contents, 
# Raises error: "Diary Entries must have a title and contents"
# """
# entry1 = Diary_Entry("Title1", "")
# => error

# """
# Given blank strings as title and contents, 
# Raises error: "Diary Entries must have a title and contents"
# """
# entry1 = Diary_Entry("", "")
# => error

# """
# Given non-string as title,
# Raises error: "Title and contents must be strings"
# """
# entry1 = Diary_Entry(1234, "Contents1")
# => error

# """
# Given non-string as contents,
# Raises error: "Title and contents must be strings"
# """
# entry1 = Diary_Entry("Title1", 1234)
# => error

# """
# Given an instance has been created, format()
# Returns formatted diary entry
# """
# entry1 = Diary_Entry("Title1", "Contents1")
# entry1.format() => "Title1: Contents1"

# """
# Given an instance has been created, count_words()
# Returns length of contents of instance in words 
# """
# entry1 = Diary_Entry("Title1", "Contents1")
# entry1.count_words() => 1

# """
# Given an instance has been created,
# given a wpm, reading_time()
# Returns time in mins needed to read contents of instance at given wpm speed
# """
# entry1 = Diary_Entry("Title1", "Contents1")
# entry1.reading_time(1) => 1

# """
# Given an instance has been created,
# given a wpm of 0, reading_time()
# Raises error: "wpm can't be 0!"
# """
# entry1 = Diary_Entry("Title1", "Contents1")
# entry1.reading_time(0) => error!


# _____UNIT TESTS____-> Mega_Diary()
# """
# Instance of Mega_Diary() class initialises diary_entries, contact_list and todo_list properties as lists
# """
# Sarahs_diary = Mega_Diary()
# Sarahs_diary.diary_entries = []
# Sarahs_diary.contact_list = []
# Sarahsdiary.todo_list = []

# """
# Given a non-instance, add_diary_entry()
# Does not add to diary_entries list
# Raises error: can only add diary_entry instances to mega diary!
# """
# Sarahs_diary = mega_diary()
# Sarahs_diary.add_diary_entry("This is not an instance")
# => error

# """
# If diary_entries list is empty (none have been added), get_all_diary_entries()
# Raises error: "No diary entries found!"
# """
# Sarahs_diary = mega_diary()
# Sarahs_diary.get_all_diary_entries()
# => error!

# """
# If diary_entries list is empty (none have been added), best_entry_to_read()
# Raises error: "No diary entries found!"
# """
# Sarahs_diary = mega_diary()
# Sarahs_diary.gbest_entry_to_read()
# => error!

# """
# Given a non-instance of Todo(), add_to_do_task()
# Does not add the instance to todo_list and raises error: "Can only add Todo instances to Mega Diary!"
# """
# Sarahs_diary = mega_diary()
# Sarahs_diary.add_to_do_task("This is not an instance")
# Sarahs_dairy.todo_list => error!

# """
# If diary_entries list is empty, get_all_phone_numbers()
# Returns nothing, raises error: "No diary entries found!"
# """
# Sarahs_diary = mega_diary()
# Sarahs_dairy.get_all_phone_numbers() => error!

# _____INTEGRATION TESTS_____

# EXAMPLE

# """
# Given an instance of Diary_Entry(), add_diary_entry()
# Adds the instance to diary_entries list
# """
# Sarahs_diary = mega_diary()
# entry1 = Diary_Entry("Title1", "Contents1")
# Sarahs_diary.add_diary_entry(entry1)
# => Sarahs_diary.diary_entries = [entry1]

# """
# Given that diary_entries is not empty, get_all_diary_entries()
# Returns diary_entries list, with each entry formatted into "Title: contents" format
# """
# Sarahs_diary = mega_diary()
# entry1 = Diary_Entry("Title1", "Contents1")
# Sarahs_diary.get_all_diary_entries()
# => ["Title1: Contents1"]

# """
# Given diary_entries list is not empty, and given a wpm and mins, best_entry_to_read()
# Returns the longest entry readable within the parameters given, formatted
# """
# Sarahs_diary = mega_diary()
# entry1 = Diary_Entry("Title1", "Contents1")
# entry2 = Diary_Entry("Title2", "Contents2 is longer")
# Sarahs_diary.add_diary_entry(entry1)
# Sarahs_diary.add_diary_entry(entry2)
# Sarahs_diary.best_entry_to_read(2, 2)
# => "Title 2: Contents2 is longer"

# """
# Given a wpm of 0, best_entry_to_read()
# Raises error "wpm must be an integer greater than 0!"
# """
# Sarahs_diary = mega_diary()
# entry1 = Diary_Entry("Title1", "Contents1")
# entry2 = Diary_Entry("Title2", "Contents2 is longer")
# Sarahs_diary.add_diary_entry(entry1)
# Sarahs_diary.add_diary_entry(entry2)
# Sarahs_diary.best_entry_to_read(0, 2)
# => error!

# """
# Given wpm not as an integer, best_entry_to_read()
# Raises error "You have no time to read!"
# """
# Sarahs_diary = mega_diary()
# entry1 = Diary_Entry("Title1", "Contents1")
# entry2 = Diary_Entry("Title2", "Contents2 is longer")
# Sarahs_diary.add_diary_entry(entry1)
# Sarahs_diary.add_diary_entry(entry2)
# Sarahs_diary.best_entry_to_read(1.5, 2)
# => error!

# """
# Given a mins of 0, best_entry_to_read()
# Raises error "You have no time to read!"
# """
# Sarahs_diary = mega_diary()
# entry1 = Diary_Entry("Title1", "Contents1")
# entry2 = Diary_Entry("Title2", "Contents2 is longer")
# Sarahs_diary.add_diary_entry(entry1)
# Sarahs_diary.add_diary_entry(entry2)
# Sarahs_diary.best_entry_to_read(2, 0)
# => error!

# """
# Given an instance of Todo(), add_to_do_task()
# Adds the instance to todo_list
# """
# Sarahs_diary = mega_diary()
# task1 = Todo("Walk the dog")
# Sarahs_diary.add_to_do_task(task1)
# Sarahs_dairy.todo_list => [task1]

# """
# Given that diary_entries is not empty, get_all_phone_numbers()
# Returns list of all phone numbers mentioned in all diary entries (no duplicate numbers)
# """
# Sarahs_diary = mega_diary()
# entry1 = Diary_Entry("Title1", "Contents1 07383474565")
# entry2 = Diary_Entry("Title2", "Contents2 07191222390")
# Sarahs_diary.add_diary_entry(entry1)
# Sarahs_diary.add_diary_entry(entry2)
# Sarahs_diary.get_all_phone_numbers() => ["07383474565", "07191222390"]

# """
# Given that diary_entries is not empty, but there are no phone numbers in diary_entries, get_all_phone_numbers()
# Returns default "No phone numbers found!"
# """
# Sarahs_diary = mega_diary()
# entry1 = Diary_Entry("Title1", "Contents1")
# entry2 = Diary_Entry("Title2", "Contents2")
# Sarahs_diary.add_diary_entry(entry1)
# Sarahs_diary.add_diary_entry(entry2)
# Sarahs_diary.get_all_phone_numbers() => "No phone numbers found!"


_Encode each example as a test. You can add to the above list as you go._

## 4. Implement the Behaviour

_After each test you write, follow the test-driving process of red, green, refactor to implement the behaviour._
