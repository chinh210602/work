class PhoneObject():
    def __init__(self):
        self.number = None
        self.name = None
        
class Chain():
    def __init__(self, object):
        self.object = object
        self.next = None
        self.prev = None
        
class PhoneBook():
    def __init__(self, number_max_len):
        self.phonebook = {}
        self.number_max_len = number_max_len
    
    def hash_funciton(self, number):
        pass