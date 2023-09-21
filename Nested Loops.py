# Nested Loop using for loop::
'''
for you in range(1,6,1):
    for me in range(1,5):
     # print("you ",you)
      print("me ",me)


for row in range(4):
    for applepic in range(4):
        print("Mango")
        applepic+=1
        row+=1
'''
# Nested Loop in While Loop ::
'''
you=1
while(you<6):
    me=1
    while(me<5):
        # print("Sandesh ",Name)
        print("me ")
        me+=1
        you+=1
'''
# Doubts
'''
row=1
while(row<4):
    applepic=1
    while(applepic<4):
        print("Mango")
        applepic+=1
        row+=1

for row in range(4):
    for applepic in range(4):
        print("Mango")
        applepic+=1
        row+=1
'''


# Nested Loop Some Examples::
'''
for day in range(1,31,1):
    for set in range(1,11,1):
        print("Day ",day,"set ",set)
        set+=1
        day+=1

for day in range(1,6,1):
    for set in range(1,5,1):
        print("Day ",day,"set ",set)
'''

# Nested Patterns Question using For Loop::

'''
for i in range(1,5):
    for j in range(1,5):
        print("*",end=" ")
    print()



for row in range(6):
    for i in range(6):
        print("*",end=" ")
    print()
 '''
# for printing this::
# 1 2 3 4 5
# 1 2 3 4 5
# 1 2 3 4 5
# 1 2 3 4 5
# 1 2 3 4 5
'''
for i in range(1,6):
 for j in range(1,6):
        print(j,end=" ")
 print( ) 
'''


# for printing this::
# 1 1 1 1 1 1
# 2 2 2 2 2 2
# 3 3 3 3 3 3
# 4 4 4 4 4 4
# 5 5 5 5 5 5
'''
for i in range(1,6):
    for j in range(6):
        print(i,end=" ")
    print( )
'''
# For printing this::
# *
# * *
# * * *
# * * * *
# * * * * *

'''
for i in range(1,6,1):
    for j in range(1,i+1,1):
        print("*",end=" ")
    print()
'''

# For printing this::
# 1
# 1 2
# 1 2 3
# 1 2 3 4
# 1 2 3 4 5

'''
for i in range(6):
    for j in range(1,i+1,1):
        print(j,end=" ")
    print()
'''
# For printing this::
# * * * * * *
# * * * * *
# * * * *
# * * *
# * *
# *
'''
for i in range(6,0,-1):
    for j in range(i):
        print("*",end=" ")
    print()
'''


# For printing this::
# 1 2 3 4 5
# 1 2 3 4
# 1 2 3
# 1 2
# 1

'''
for i in range(6,0,-1):
    for j in range(1,i):
        print(j,end=" ")
    print()
'''
# for i in range(5,0,-1):
#     for j in range(5,i,-1):
#         print(j,end=" ")
#     print()



# For printing this::
# 1
# 1 2
# 1 2 3
# 1 2 3 4
# 1 2 3 4 5
# 1 2 3 4
# 1 2 3
# 1 2
# 1 2