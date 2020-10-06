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
    st = Storage({
        'a': 1, 
        'b': 2, 
        9999: 3.0, 
        42.42: 4,
    })
    # test removing of existent keys
    def test_existent_key(key, expected_val):
        assert st.get(key) is not None, f"!! Test is misconfigured: key={key} doesn't exist, but was expected to exist"
        previous_len = len(st.data)
        removed_val = st.remove(key)
        assert removed_val == expected_val, f"Returned value of removed key={key} is={removed_val}, but was expected to be={expected_val}" 
        assert st.get(key) is None, f"Removed key={key} is still present, but was expected otherwise"
        # FIXME(alexey larionov) this test should also check that other key-value pairs are not 
        # changed, but comparison of lengths is just easier, yet not totally reliable
        removed_pairs = previous_len - len(st.data)
        assert removed_pairs == 1, f"After removing one of the keys, {removed_pairs} key-value pairs were removed, but only 1 was expected"
    test_existent_key('b', 2)
    test_existent_key(9999, 3.0)
    test_existent_key(42.42, 4)
    
    # test removing of non-existent keys
    def test_non_existent_key(key):
        assert st.get(key) is None, f"!! Test is misconfigured: key={key} already exists, but should've not"
        removed_val = st.remove(key)
        assert removed_val is None, f"Removing of non-existent key={key} returned={removed_val}, but was expected to return None"
        assert st.get(key) is None, f"Removing of non-existent key={key} created this key, but should've not"
        
    test_non_existent_key('c')
    test_non_existent_key(5)
    test_non_existent_key(11.11)

    # test removing of values that cannot be keys (mutable objects)
    def test_invalid_key(key):
        assert st.remove(key) is None, f"Removing of a mutable object key={key} was expected to return None"
        # FIXME(alexey larionov): this test should assert that st.get(key) with an 
        # invalid (mutable) key returns None before and after removal,
        # but it can't be done because st.get(key) throws an expection in such case
    test_invalid_key([1, 2, 3])
    test_invalid_key({ 'z': st })

def test_set():
    key, cur_value = 'key', 1
    storage = Storage({key: cur_value})
    set_value = 5
    storage.set(key, set_value)
    get_value = storage.get(key)
    assert get_value == set_value,  f"Wrong value {get_value} was set for key '{key}' instead of {set_value}"

    wrong_key = 'wrong_key'
    try:
        storage.set(wrong_key, set_value)
    except KeyError as ke:
        pass
    except:
        assert False, f"Unexpected behaviour while setting the value by the wrong key"

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
