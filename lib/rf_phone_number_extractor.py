import re

class phone_number_extractor():
    def __init__(self, diary):
        self._diary = diary

    def get_numbers(self): # Use a set to make this more computationally efficient (sets can't have duplicate entries)
        phone_numbers = set()
        for entry in self._diary.all():
            phone_numbers.update(re.findall(r'\b0[0-9]{10}\b', entry.contents)) # USe regex to find all phone numbers
        return phone_numbers