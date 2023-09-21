# List allowes many strings in one single line::
# name1= "Ankush"
# name2="Nrupul"
# name3="Albert"
# name4="Aman"

# List allowes many strings in one single line::
# Note :: it always [] in brackets;;

'''
names= ["Nrupul","Aman","Albert","Ankush"];
print(names)


name =["Ram","Ali","Mohan","Rahul"]
print(name)

vegetable_name=["Chilli","Tomato","Potato","Pea"]
print(vegetable_name)
print(len(vegetable_name))
print(vegetable_name[2])
vegetable_name[2]="Sandesh"
print(vegetable_name)
vegetable_name.append("Brinjal")
print(vegetable_name)
vegetable_name.pop()
print(vegetable_name)

'''

'''
states = ["Jammu_and_Kashmir","Punjab","Karnataka","Tamil_Nadu"]
print(states[0])
print(states[1])
print(states[2])
print(states[3])

print(len(states))
'''
# for indexing in numbers for getting-
# -value and understanding with an Ex::
'''
price=[12,23,22,29]
length=len(price)
index=length-1
print(price[index])
'''

# Using Loop Function::
'''
states = ["Jammu_and_Kashmir","Punjab","Karnataka","Tamil_Nadu"]
for i in range(len(states)):
    print(states[i])
    
    
    
name=["Maa","Papa","Friend","Family"]
for i in range(len(name)):
    print(name[i])    
'''

#want to total number of Item and want a special
# number output::
'''
marks=[34,46,67,98]
print(marks)
print(len(marks))
print(marks[3])
'''
# List keywords is allow to
# add different datatypes in one line::
'''
total_marks=["Nrupul",35,True]
print(total_marks)
'''

#want to total number of Item and want a special
# number output::
'''
names= ["Nrupul","Aman","Albert","Ankush"];
print(names)
print(len(names))
print(names[2])
'''

#want to total number of Item and want a special
# number output::
'''
marks=[34,46,67,98]
print(marks)
print(len(marks))
print(marks[3])
'''

# Replace Name:: by this trick
'''
names= ["Nrupul","Aman","Albert","Ankush"];
names[1]="Sandesh"
print(names)
'''

# Add an element::[it will add in the last of element]
# using append keyword::
'''
names= ["Nrupul","Aman","Albert","Ankush"];
print(names)
print(len(names))

names.append("Ayush")
print(names)
print(len(names))


name=[]
name.append("Maa")
name.append("Papa")
name.append("Family")
name.append("me")
print(name)
'''
# If we want print one or more elements
# without using Append keyword::
'''
name=[]
name.extend("Maa","Papa","Family","Me")
print(name)
'''
#Insert Keyword::[It will insert a particular which element
# we give command::
# [Note:: if we give index out of range in given-
# -elements and its prints on last of the element]
'''
numbers=[1,2,3,4,5]
numbers.insert(3,56)
print(numbers)

numbers=[1,2,3,4,5]
numbers.insert(10,56)
print(numbers)
'''

# Remove the element::
# using pop keyword
# [it will remove last element from the list]
'''
names= ["Nrupul","Aman","Albert","Ankush"];
print(names)
print(len(names))

names.pop()
print(names)

# 2nd example::
name=["Maa","Papa","Friend","Family"]
name.pop()
print(name)

# it print index which we put in [pop()] 

name=["Maa","Papa","Friend","Family"]
name.pop(2)
print(name)
'''

# if any particular element want to access::
'''
names = ["Nrupul","Aman","Albert","Ankush"];
print(names[3])

total_items = len(names)
print(names[total_items-1])


total_items = len(names)
print(names[total_items-2])
'''
# Example::
'''
list=[12,12,23,23,34,45]
print(list)
print(len(list))
list.pop()
print(list)
list.pop()
print(list)
list.pop()
print(list)

# using for loop::
for i in range(3):
    list.pop()
print(list)
'''

