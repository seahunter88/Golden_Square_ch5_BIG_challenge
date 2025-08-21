class readable_entry_finder():
    def __init__(self, diary):
        self._diary = diary

    def count_words(self, string):
        return len(string.split())

    def is_entry_readable(self, wpm, mins, entry):
        words_readable = wpm * mins
        return self.count_words(entry.contents) <= words_readable

    def extract_best_entry(self, wpm, mins):
        readable_entries = []
        for entry in self._diary.all():
            if self.is_entry_readable(wpm, mins, entry):
                readable_entries.append(entry)
            else:
                continue
        if not readable_entries:
            return None
        else:
            return max(readable_entries, key = lambda entry: entry.contents)
