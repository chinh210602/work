from random import randint
def hash_function(number):
    max_len = 10
    m = 1000
    p = 10**max_len + 1
    a = randint(1, p - 1)
    b = randint(0, p - 1)
    
    return ((a*number + b) // p) // m

number = 948045269
print(hash_function(number))