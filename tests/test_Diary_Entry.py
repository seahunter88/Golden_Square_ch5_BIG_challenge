from lib.Diary_Entry import *
import pytest

"""
1. Instance of Diary_Entry() class initialises title and contents properties
"""
def test_Diary_Entry_initialises_title_and_contents():
    entry1 = Diary_Entry("Title1", "Contents1")
    assert entry1.title == "Title1"
    assert entry1.contents == "Contents1"

"""
2. Given a blank string as title, 
Raises error: "Diary Entries must have a title and contents"
"""
def test_Diary_Entry_no_title_raises_error():
    with pytest.raises(Exception) as e:
        Diary_Entry("", "Contents1")
    error_message = str(e.value)
    assert error_message == "Diary Entries must have a title and contents"

"""
3. Given a blank string as contents, 
Raises error: "Diary Entries must have a title and contents"
"""
def test_Diary_Entry_no_contents_raises_error():
    with pytest.raises(Exception) as e:
        Diary_Entry("Title1", "")
    assert str(e.value) == "Diary Entries must have a title and contents"

"""
4. Given blank strings as title and contents, 
Raises error: "Diary Entries must have a title and contents"
"""
def test_Diary_Entry_no_title_or_contents_raises_error():
    with pytest.raises(Exception) as e:
        Diary_Entry("", "")
    assert str(e.value) == "Diary Entries must have a title and contents"

"""
5. Given non-string as title,
Raises error: "Title and contents must be strings"
"""
def test_Diary_Entry_non_string_title_raises_error():
    with pytest.raises(Exception) as e:
        Diary_Entry(1234, "Contents1")
    assert str(e.value) == "Title and contents must be strings"

"""
6. Given non-string as contents,
Raises error: "Title and contents must be strings"
"""
def test_Diary_Entry_non_string_contents_raises_error():
    with pytest.raises(Exception) as e:
        Diary_Entry(1234, "Contents1")
    assert str(e.value) == "Title and contents must be strings"

"""
7. Given an instance has been created, format()
Returns formatted diary entry
"""
def test_format_returns_formated_entry():
    entry1 = Diary_Entry("Title1", "Contents1")
    assert entry1.format() == "Title1: Contents1"

"""
8. Given an instance has been created, count_words()
Returns length of contents of instance in words 
"""
def test_count_words_returns_length_of_contents():
    entry1 = Diary_Entry("Title1", "Contents1 here is a contents")
    assert entry1.count_words() == 5

"""
9. Given an instance has been created,
given a wpm, reading_time()
Returns time in mins needed to read contents of instance at given wpm speed
"""
def test_reading_time_returns_time_takes_to_read():
    entry1 = Diary_Entry("Title1", "Contents1")
    assert entry1.reading_time(1) == 1

"""
10. Given an instance has been created,
given a wpm of 0, reading_time()
Raises error: "wpm can't be 0!"
"""
def test_count_words_0_wpm_raises_error():
    entry1 = Diary_Entry("Title1", "Contents1")
    with pytest.raises(Exception) as e:
        entry1.reading_time(0) 
    assert str(e.value) == "WPM must be an integer greater than 0!"

"""
10. Given an instance has been created,
given a non-integer wpm, reading_time()
Raises error: "WPM must be an integer greater than 0!"
"""
def test_count_words_non_int_wpm_raises_error():
    entry1 = Diary_Entry("Title1", "Contents1")
    with pytest.raises(Exception) as e:
        entry1.reading_time(1.5) 
    assert str(e.value) == "WPM must be an integer greater than 0!"