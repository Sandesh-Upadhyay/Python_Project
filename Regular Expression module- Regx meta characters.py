import re
'''
. - any char
[a-zA-Z] - chr class a or b or c ... or z A or B or .....Z
[0-9] - digit class 0 or 1 or 2....... or 9



+ - atleast one [a-z]+
* - zero or more

^ - start of the string
& - end of the string

? - optional

[a-z]{2,4}
'''

# Ex::
'''
s= "ABCDE1234A"
r=re.compile("^[A-Z]{5}[0-9]{4}[A-Z]&")
l=re.findall(r,s)
print(l)
'''
'''
s="88888888123456789"
r= re.compile("^[6-9][0-9]{9}&")
l= re.findall(r,s)
print(l)
'''

# dd-mm-yyyy
'''
s = "20-05-2018"
r = re.compile("^[0-9]{2}-[0-9]{2}-[0-9]{4}&")
l = re.findall(r,s)
print(l)
'''

# Re Modules Groups::
'''
s = "20-05-2018"
r = re.compile("^(?P<Date>[0-9]{2})-(?P<Month>[0-9]{2})-(?P<Year>[0-9]{4})$")
m = re.search(r,s)
if m:
    print(m.group(3))
    print(m.group(0))
    print(m.group(1))
    print(m.group(2))
    print(m.groups("date"))
    print(m.groups("Month"))
    print(m.groups("Year"))
else:
    print("pattern not found")
'''


'''
s = "+91 8123456789"
r = re.compile("(?:\+91)?\s[6-9][0-9]{9}")
m = re.search(r,s)
if m:
    print(m.groups(1))
else:
    print("Number Not Found")
'''









# help(re)