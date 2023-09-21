# Sets::

# Sets are mutable
# All the elements should be unique
# immutable elements in the set- int float tuple str
# unordered


# s={10,20,30,40,50,60,70,80,90}
# print(s,type(s))

# s={10,20,30,40,50,10,20,30,40}
# print(s)

# s={100,200,300,400}
# s.add(500)
# print(s)


# s1 = {10,20,30,40,50}
# s2 = {60,70,80,90}

# s3=s1.union(s2)
# print(s3)

# s3=s1.intersection(s2)
# print(s3)

# (help(set))

# s3=s1.difference(s2)
# print(s3)

# s3=s2.difference(s1)
# print(s3)

# s3=s1.symmetric_difference(s2)
# print(s3)

# print(s1)
# s1.update(s2)
# print(s1)

# s1.intersection_update(s2)
# print(s1)

# s1.difference_update(s2)
# print(s1)

# s1.symmetric_difference_update(s2)
# print(s1)


# issubset

# s1={100,200,300,400}
# s2={100,200,300}

# print(s2.issubset(s1))

# issuperset

# s1={100,200,300,400}
# s2={100,200,300}
# print(s1.issuperset(s2))

# convert a list into set::
'''
l=[100,200,300,400,500]

s=set(l)
print(s)
'''

'''




'''

'''
l1=[10,20,30,40,50,60,70,80,90]
l2=[15,25,35,45,65,75,85,95]

s1=set(l1)
s2=set(l2)
s3=s1.union(s2)
print(s3)
'''

# convert a set into list::
'''
l3=list(s3)
print(l3)

l3.sort()
print(l3)
'''

# instead of doing this use this builtins function
'''
l3=sorted(s3)
print(l3)
'''

# pop
# remove
# discard
# clear
# del

'''
s = {100,200,300,400,500}
r = s.pop()
print(s,r)

s.remove(100)
print(s)

s.discard(100)
print(s)
'''


# if we put element which is not present in list DISCARD ignored it ::
# Ex:-
'''
s.discard(10000)
print(s)
'''
# s.clear()
# print(s)
