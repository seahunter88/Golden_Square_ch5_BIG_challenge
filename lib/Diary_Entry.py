class Diary_Entry():
    
    def __init__(self, title, contents):
        if not title or not contents:
            raise Exception("Diary Entries must have a title and contents")
        if not isinstance(title, str) or not isinstance(contents, str):
            raise Exception("Title and contents must be strings")
        self.title = title
        self.contents = contents
    
    def format(self):
        return f"{self.title}: {self.contents}"
    
    def count_words(self):
        words = self.contents.split()
        return len(words)
    
    def reading_time(self, wpm):
        if wpm > 0 and isinstance(wpm, int):
            return self.count_words() / wpm
        else:
            raise Exception("WPM must be an integer greater than 0!")