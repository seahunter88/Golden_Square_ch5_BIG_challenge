from lib.Diary_Entry import *
from lib.Todo import *
import re

class mega_diary():
    
    def __init__(self):
        self.diary_entries = []
        self.contact_list = []
        self.todo_list = []

    def add_diary_entry(self, entry):
        if isinstance(entry, Diary_Entry):
            self.diary_entries.append(entry)
        else:
            raise Exception("Can only add diary_entry instances to mega diary!")
        
    def get_all_diary_entries(self):
        if self.diary_entries == []:
            raise Exception("No diary entries found!")
        formatted_entries = [entry.format() for entry in self.diary_entries]
        return formatted_entries
    
    def add_to_do_task(self, task):
        if isinstance(task, Todo):
            self.todo_list.append(task)
        else: 
            raise Exception("Can only add Todo instances to Mega Diary!")
        
    def best_entry_to_read(self, wpm, mins):
        if self.diary_entries == []:
            raise Exception("No diary entries found!")
        if wpm == 0 or not isinstance(wpm, int):
            raise Exception("wpm must be an integer greater than 0!")
        if mins == 0:
            raise Exception("You have no time to read!")
        if not isinstance(mins, int):
            raise Exception("Mins must be an integer greater than 0!")
        else:
            words_readable = wpm * mins
            entry_lengths = {}
            for i in self.diary_entries:
                entry_lengths[i] = i.count_words()
            best_entry = max((entry for entry, word_length in entry_lengths.items() if word_length <= words_readable), 
                                key = lambda entry: entry_lengths[entry],
                                default = "No readable entries!")
            return best_entry.format()
        
    def get_all_phone_numbers(self):
        if self.diary_entries == []:
            raise Exception("No diary entries found!")
        else:
            formatted_entries = [entry.format() for entry in self.diary_entries]
            phone_numbers = []
            for i in formatted_entries:
                number = re.findall(r'\b[0-9]+\b', i)
                if "".join(number) not in phone_numbers:
                    phone_numbers.append("".join(number))
            if phone_numbers == ['']:
                return "No phone numbers found!"
        return phone_numbers