# (1) Positional Arguments::
# def linear_search(l,key):
#     for value in l:
#         if key==value:
#             return True
#     else:
#         return False

# l=[100,200,300,400,500]
# key=400
# result=linear_search(l,key)
# print(result)


#(2) Default Argument::
# password generator
# task is you should generate a password-
# contains::
# 8char
# 1Upper
# 1Lower
# 1Special Char
# 5 digits

# ord() gives acii values
# chr()

# print(ord("a"),ord("z"))
# print(ord("A"),ord("Z"))

'''
import random

# def gen_password():
def gen_password(Length=8):
    # if you want a particuler password like 5 character the you can put::
    # gen_password(Length=8)

    l=["@","#","$","&"]
    upper=chr(random.randint(65,90))
    lower=chr(random.randint(97,122))
    special=random.choice(l)
    digit=random.randint(10000,99999)
    password= upper+lower+special+str(digit)
    l= random.sample(password,Length)
    password=("").join(l)
    return password



result=gen_password()
print(result)

'''

# (3rd) Keyword Argument::
'''
def validate (username,password):
    if username == "ABC" and password == "Abc@123":
        print("Valid Password")
    else:
        print("Invalid password")


validate("ABC","Abs@123")
validate("Abc@123","ABC")
validate(password="Abc@123",username="ABC")
'''


# help(print)
# Ex:-
'''
print(100,200,sep=" , ",end=" ")
print("me")
'''








