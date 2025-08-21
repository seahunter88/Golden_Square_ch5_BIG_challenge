from lib.rf_Diary_Entry import *

"""
Instance of Diary_Entry() class initialises title and contents properties
"""
def test_Diary_Entry_initialises_title_and_contents():
    entry1 = Diary_Entry("Title1", "Contents1")
    assert entry1.title == "Title1"
    assert entry1.contents == "Contents1"