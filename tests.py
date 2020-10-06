from storage import Storage

def test_add ():
     key, val = 'key', 'val'
     wrong_key = 'key1'
     storage = Storage({'key1':'val1'})
     storage.add(key, val)
     get_value = storage.get(key)
     get_value == val
     assert get_value == val, 'Wtong value for key was added'
     try:
         storage.add(wrong_key, val)
         get_value = storage.get(key)
     except KeyError:
         print('Such key already exists, try another one')

def test_remove():
    pass

def test_set():
    pass

def test_get():
    st = Storage({'a': 1, 'b': 2})
    key = 'b'
    val = st.get(key)
    assert val == 2, "Value for the key {} is not equal to expected".format(key)
    key = 'c'
    val = st.get(key)
    assert val is None, "Value for an unexisting key is not None"

def run_tests():
    test_add()
    test_remove()
    test_set()
    test_get()

if __name__ == "__main__":
    run_tests()