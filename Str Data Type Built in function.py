# help(str)
# print(dir(str))

# format()
# Different way to use format method

'''
num1=100
num2=200
print("value of num1 is ",num1,"value of num2 is ",num2)
print('value of num1 is{} value of num2 is, {}'.format(num1,num2))
print('value of num1 is{1} value of num2 is, {0}'.format(num1,num2))
print('value of num1 is{val1} value of num2 is, {val2}'.format(val1=num1,val2=num2))
'''

# s="python sample string"
# print(id(s))
# s=s.capitalize()
# print(s)
# print(id(s))


# Functions

# upper
# lower
# title
'''
print(s.upper())
print(s.lower())
print(s.title())
'''

# split
# join

# s='HTML,CSS,JAVA,PYTHON,Django'
# l=s.split(",")
# l=s.split(" ")
# print(l)
#
#
# s1=(" ").join(l)
# print(s1)


# maketrans
# translate

'''
s1 = 'abcd'
s2 = '1234'
s3 = 'Python sample string abcd'

table = str.maketrans(s1,s2)
result = s3.translate(table)
print(result)
'''


# index
# find
# rfind

'''
s="HTML,CSS,PYTHON,jAVA"
print("PYTHON" in s)
print(s.index("PYTHON"))
print(s.find("PYTHON"))
print(s.rfind(" "))
'''


# Strip

'''
s="********Python*****"
s1=s.strip("*")
s1=s.lstrip("*")
s1=s.rstrip("*")
print(s1)
'''

# center
# ljust
# rjust

'''
s= "Python"
s1=s.center(20,"*")
s2=s.ljust(20,"*")
s3=s.rjust(20,"*")
print(s1)
print(s2)
print(s3)
'''

# replace

'''
s="html,CSS,JAVA, html"
s1=s.replace("html","HTML7")
print(s1)

'''









