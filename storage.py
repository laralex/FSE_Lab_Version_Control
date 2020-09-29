class Storage:
    def __init__(self, data={}):
        super().__init__()
        if isinstance(data, dict):
            self.data = data
        else:
            raise Exception

    def get(self, key):
        if key in self.data:
            return self.data[key]
        else:
            return None

    def remove(self, key):
        from collections import Hashable
        if not isinstance(key, Hashable):
            return None # given key is a mutable object (thus cannot be a dict's key by Python rules)
        return self.data.pop(key, None) # if key isn't found, returns default=None
        
    def set(self):
        pass
    
    def add(self):
        pass
