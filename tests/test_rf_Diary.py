from lib.rf_Diary import *
"""
Initially, Diary()
Has no entries in entry_list 
"""
def test_Diary_initialises_list():
    diary = Diary()
    assert diary.all() == []