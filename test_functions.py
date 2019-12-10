from functions import *

def test_end_chat():
    assert callable(end_chat)
    assert isinstance(end_chat(['a', 'b']), bool)
    assert end_chat(['quit']) == True

def test_big_chat():
    assert callable(big_chat)
    