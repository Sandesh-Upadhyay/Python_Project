# r => read
# r+
# w=> write
# w+
# a =>append
# a+
# fp = open('input.text','r')
# content = fp.read()
# print(content)


# print("--------------")
# content = fp.read()
# print(content)


# content = fp.readline()
# print(content)

# for x in fp:
#     print(x)




# FILE OPERATIONS - READ ,WRITE- APPEND:::


'''
fp = open("input2.txt","w+")
print(fp.tell())
fp.write("sample text line1")
print(fp.tell())
fp.seek(0,0)
print(fp.tell())
content = fp.read()
print(fp.tell())
print(content)
'''



# tell => current fp position
# seek(offset,position) => to change the fp position
# offset => number of char
# position => 0 => Start of the file
#             1=> current position
#             2=> end of the file

# Ex:-
# seek(15,0) => change the fp by 15 char from start of the file
# seek(0,2) => change the fp by 0 char from end of the file


# fp = open("input2.txt","w+")
# print(fp.tell())
# fp.write("sample text line1")
# print(fp.tell())
# content = fp.read()
# print(fp.tell())
# print(content)



# r+ => read + write



#
# fp.write("\n\nSample line using python script")

# a
# a+

# r,r+.w,w+ => fp is at start
# a and a+ => at the end


# fp = open("input2.txt","r")
# print(fp.tell())
# content = fp.read()
# print(content)


# Summary
'''
r => fp => start , file should already exist , read
r+ => fp => start , file should already exist , read + write

w => fp => start , create a new file ,write
w+ => fp => start , create a new file , write + read

a => fp => and, create a new file , write at the end
a+ => fp => end,create a new file , write + read
'''



