# (4th) Variable Length Positional Argument::
from typing import List, Any


# if I want to append in a list::

# l=[100,200,300,400]
# l.append(500)
# print(l)
# then we do append method but incase if we have lots of numbers to add...??

# l=[100,200,300,400]
# l.append(500,600,700)
# print(l)



'''
def add_value(*args):
    l = []
    for value in args:
        l.append(value)

    return l


result = add_value = (100, 200, 300, 400, 500)
print(result)
result = add_value = (100, 200)
# print(result)
result = add_value = (100, 200, 300, 400, 500, 600, 700, 800, 900)
print(result)
'''

# (5)Variable Length Keyword Argument::

# name, email,contact,DOB

'''
def get_details(**kwargs):
    print(kwargs)


get_details(name="Sandesh",email="abc123@gmail.com",contact="726152663",DOB="20-02-2002")
'''


