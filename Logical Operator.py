# Logical Operator::
#  and
'''
 *True and True=True
 *True and False=False
 *False and True=False
 *False and False =False
 '''

'''
a=True
b=True
print(a and b)

a=True
b=False
print(a and b)

a=False
b=True
print(a and b)

a=False
b=False
print(a and b)



a=5>3
b=6>3
c= a and b
print(c)

a=5>3
b=6<3
c= a and b
print(c)



if 5>3:
    if 6>4:
     print("both conditions are true")
     
        
if 5>3 and 6>4:
    print("both conditions are true")
'''
#
# if 10>15 and 6>4:
#     print("both conditions are true")

# print(5>3)and (6>4) and (10<15)

# subject = "english"
# passing_marks=70
# rahul_marks=75
# rahul_subject="english"
#
# if rahul_subject==subject and rahul_marks>=passing_marks:
#    print("Rahul Has Passed")
# else:
#     print("Rahul Failed")
#

# Gender="Female"
# age = 25
#
# if Gender=="Male" and age >=21:
#     print("He can marry")
# elif Gender=="Female" and age >=18:
#     print("She can marry")
# else:
#     print(Gender ,"can not  marry")

# a= "Sandesh"
# b= 21
# print(a,b)

# a= "Sandesh"
# b= 21
# print(a + b)
#
# a= "Sandesh"
# b= "Upadhyay"
# print(a + b) [+ add without space]
#
# a= "Sandesh"
# b= "Upadhyay"
# print(a,b)    [comma seprate ]

# a= "Sandesh"
# b= 21
# print(a,b)
# print(a,"\n" ,b)  [backslash N define in new line ]


# palak_available=True
# paneer_available=True
#
# if paneer_available and paneer_available:
#     print("can make the dish")
# else:
#     print("cannot make dish")


# Logical Operator::
# or
'''
 *True or True=True
 *True or False=True
 *False or True=True
 *False or False =False
'''

'''

a=5>3
b=6>3
c=a or b
print(c)

a=5>3
b=6<3
c=a or b
print(c)

a=5<3
b=6>3
c=a or b
print(c)

a=5<3
b=6<3
c=a or b
print(c)


potato_available=True
paneer_available=True
if potato_available and paneer_available:
    print("dinner possible")
else:
    print("dinner not possible")


'''


# gender ="female"
# age=25
#
# if ((gender=="male" and age>=21) or (gender=="female" and age>=18)):
#     print(gender,"can  marry")
# else:
#     print(gender,"can not marry")


# Logical Operator::

# not
# True= False
# False=True

'''
if not True:
    print("not a true")
else:
    print("a true")


if not False:
    print("not a true")
else:
    print("a true")


    
age=13 , 19
age= 20,29
if (age==13 and 19 ) or (age==20 and 29):
    print("Teenage")
else:
    print("Twenties")


    
yob=1990
age= 2023-yob

if age>=13 and age<=19:
    print("Teenage")
elif age>=20 and age<=29:
    print("Twenties")
    
    
char="z"
if char=="a" or char=="e" or char=="i" or char=="o" or char=="u":
    print(char,"Is Vowel")
else:
    print(char,"is consonant")
# a,e,i,o,u



a=2
b=3
c=1

if a>b and a>c:
    print(a,"is largest")
elif b>a and b>c:
    print(b,"is largest")
else:
    print(c,"is largest")
  
a=1
b=1
c=1

if a>b and a>c:
    print(a,"is largest")
elif b>a and b>c:
    print(b,"is largest")
elif c>a and c>b:
    print(c, "is largest")
else:
    print("none of these ")
  
'''