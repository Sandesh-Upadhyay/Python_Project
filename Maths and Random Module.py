# some builtin function in maths
'''
l=[100,200,300,400,500,600]
print(sum(l))
print(max(l))
print(min(l))
'''


# if you want to know exact value of a floating number::

# num= 62.5678
# print(round(num,2))


# print(dir('__builtins__'))

# help(__builtins__)

import math
'''
l = [0.1] * 10
print(l)
print(sum(l))

print(math.fsum(l))

num1= 15.5556
print(math.floor(15.5556),math.ceil(15.5556))

print(math.sqrt(45))
print(math.factorial(10))
'''


# {
'num2=45.5559'
'print(math.modf(num2))'
# } print separate out  non decimal and decimal part also::

'''
d,i=math.modf(num2)
print(d)
# print(i) [it gives separate part of it decimal and non-decimal]
'''


# Random function
'''
print(math.pow(10,2))

print(math.log(10,3))
print(math.log2(10))
print(math.log10(2))

print(math.sin(math.radians(30)))
print(math.cos(math.radians(45)))
print(math.tan(math.radians(60)))
'''

# help(math)
# print(dir(math))


# for generating random number for given below::
import random
'''
print(random.random())
l=[1,2,3,4,5,6,7,8,9]
print(random.choice(l))

print(random.randint(1,5))   [it also gives random number given in this list]
print(random.randrange(1,10))  [it also gives random number given in this list]
'''


