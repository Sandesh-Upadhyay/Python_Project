# dict:
# it's mutable
# ordered
# key should be unique
# key should immutable int,float,str,tuple

# d={"emp_id":101,"name":"ABC","email":"abc@gmail.com","name":"PQR"}
# print(d)

# print(d["emp_id"])
# you can also use with the help of[.get method]::

# get

'''
print(d.get("emp_id"))
print(d.get("name"))
print(d.get("email"))

"if we want print which keyword is not exits in the Dict
then it throws none"
Ex:-
print(d.get("number"))

another note::

print(d.get("number","number is not given"))
'''


# set default
'''
set default is setting default in dict like:
when key exits or not :
if key exit then it print the value and if key is not exits then it print none 
Ex:
print(d.setdefault("Age"))
'''
# Some iterating


# for x in d:
#     print(x)
#
# for key in d:
#     print(key,d[key])

# for value in range(1,11):
#     d[value]=value*value
#
# print(d)

# key
# value
# items
'''
print(d.values())
print(d.items())
print(d.keys())
'''

# for t in d.items():
#     print(t)


# convert a list into dict ::
'''
L1=[1,2,3,4,5,6,7,8,9]
L2=[1,4,6,8,10,12,14,16,18]

d = dict(zip(L1,L2))
print(d)
'''


# Update Method::
'''
l=[1,2,3,4,5]
d=dict.fromkeys(l,0)
d=dict.fromkeys(l,(5*2*4))
print(d)
'''

'''
d1={1:1,2:4,3:9,4:16}
d2={5:25,6:36,7:49}

d1.update(d2)
print(d1)
'''

# pop
# popitem
# clear
# del



#same as previous