# if Statement:::
# if with boolean::
'''
print("Hello World")
if True:
    print("Hello Sandesh")
    print("Hey Man")
print("Hey EveryOne")



print("Hello World")
if False:
    print("Hello Sandesh")
    print("Hey Man")
print("Hey EveryOne")

print("outside")
if 0>1:
    print("Sir")
    print("Mam")
print("Student")
print("Class")


print("outside")
if 0<1:
    print("Sir")
    print("Mam")
print("Student")
print("Class")



print("Code Start")
if True:
    print("Inside Code")
print("Code End")
'''

# if with expression
'''
if (5>3):
  print("Inside Code")
'''

#if with Varialbles
'''
name1="Rahul"
name2="Rahul"
check=(name1==name2)

if(check):
    print("Both Names are same")



a= 1
b=1
check=(a==b)

if(check):
    print(("both names are same "))
'''


# if....else Statements::

'''
a= 1
b=1
 check(a==b)
 check=(a!=b)
if(check):
    print("both names are same ")
else:
    print("both names are not  same ")
'''


#List of False Values::
'''
* Empty sequences
* Zero 
* None
* False
'''
# a= 1
# b=1
# if False:  #Also all for used Empty,Zero,None
#     print("both names are same ")
# else:
#     print("both names are not  same ")
#     print("both names are not  same ")


'''
a=5
b=1

if a>b:
    print("a is greater than b ")
else:
    print("a is not greater than b")



str="Ramesh"
str1="Mahesh"

if str==str1:
    print("str is same")
else:
    print("str is not same")

Given_total_bill=10999        
discount_start_price=5000
if Given_total_bill>discount_start_price:
    print("Discount Available")
else:
    print("No Discount")
    
'''

#if..elif...else Statement::

'''

a=2
b=1
if a>b:
    print("a is greater than b")
elif a==b:
    print("a is equal to b")
else:
    print("b is greater than a")


a=1
b=1
if a>b:
    print("a is greater than b")
elif a==b:
    print("a is equal to b")
else:
    print("b is greater than a")


a=0
b=1
if a>b:
    print("a is greater than b")
elif a==b:
    print("a is equal to b")
else:
    print("b is greater than a")
    
    
    total_bill=10000
if total_bill>500:
    print("10 percent Discount")
elif total_bill<1000:
    print("20 percent Discount")
else:
    print("No Discount")





rice_available= True
wheat_available=True
apple_available=True

if rice_available:
    print("buy rice ")
elif wheat_available:
    print(" but weat")
elif apple_available:
    print("buy apple")
else:
    print("don't buy ")



rice_available= False
wheat_available=True
apple_available=True

if rice_available:
    print("buy rice ")
elif wheat_available:
    print(" but weat")
elif apple_available:
    print("buy apple")
else:
    print("don't buy ")

rice_available= True
wheat_available=True
apple_available=False

if rice_available:
    print("buy rice ")
elif wheat_available:
    print(" but weat")
elif apple_available:
    print("buy apple")
else:
    print("don't buy ")


'''

#Nested if ::

'''
gender="Female"
age=25

if gender=="Male":
    if age>=21:
        print("He can marry")
    else:
        print("he can't marry")
else:
    if age>=18:
        print("she can marry ")
    else:
        print("she can't marry")



char="a"

if char=="a":
    print("vowel")
elif char=="e":
    print("vowel")
elif char=="i":
    print("vowel")
elif char=="o":
    print("vowel")
elif char=="u":
    print("vowel")
else:
    print("not vowel")

check=27

if check%3==0:
    print("Divided")
else:
    print("Not Divided")



yob=1990
age=2023-yob

if yob>=18:
    print("Apply for Licence")
else:
    print("NA")

stored_username="Sandesh"
stored_password="1234@"

input_username="Sandesh"
input_password="123"

if stored_password==input_username:
    if stored_password==input_password:
        print("login")
    else:
        print("Not Valid")
else:
  print("not valid")

'''
