# list are mutable and update and delete
# ordered data structure indexing and slicing
# heterogeneous datatype
# l=[10,20,30,40,"python","Java",[100,200,300]]
# print(l,type(l))

# Indexing and slicing:
# print(l[0])
# print(l[-1][1])
# print(l[])


# Slicing
# print(l[1:3])
# print(l[::-1])


l=[100,200,300,400,500]

# for value in l:
#     print(value)

# for value in l[::2]:
#     print(value)



# append
# print(id(l))
# l.append(600)
# print(id(l))
# print(l)


# extend

# l.extend("python")
# print(l)


# insert
'''
(1,1000)
print(l)
'''

# copy

'''
l=[10,20,30]
l2=l
l.copy()
l.append(40) [if we put this datatype then it will print only in first list ]
print(id(l),id(l2))
print(l,l2) [because of same memory location]

'''

# for update
l=[10,20,30,40,50]
# l[2]=500
# print(l)

# for delete there are many types of datatype:

# pop
# remove
# clear
# del

# r=l.pop()  [it will delete last item]
# print(l)


# remove

# l.remove(20)
# print(l)

# clear
# print(l)
# l.clear()

# del

# del l
# print(l)

# l=[50,40,30,20,10]     it gives nothing just gives us original form::
# l.sort()
# print(l)


# if you want to know that which element have what index ::
# then use this

# print(l.index(30))

# count variable is :::also do same work as index::

# print(l.count(30))
