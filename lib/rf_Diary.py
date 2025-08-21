class Diary():

    def __init__(self):
        self._entries = []
        pass

    def add(self, entry):
        self._entries.append(entry)

    def all(self):
        return self._entries