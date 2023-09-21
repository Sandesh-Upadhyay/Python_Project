# define normal step
# in this code i intialize in 0
# [NOte:- In this code intialization is by
# default option so that i start with 0 ]

'''
for i in range(10):
    print(i)

for i in range(10):
    print("*")


'''

# With th help of While Loop adding 1 to 10 numbers
'''
sum=0
i=1
while(i<11):
 sum+=i
 print(sum)
 i+=1
 
 
'''

#for reverse
'''
for i in range(5,0,-1):
 print(i)
'''

# For reverse in one line
'''
for i in range(5,0,-1):
 print(i, end=" ")
'''

# define step by step
# in this code i intialize in 1 because
# there is given
# [Note:- Start and Stop is optional]
'''
for i in range(1,11,1):
    print("*:",i)


for i in range(1,16,2):
    print(i)

(
i=1+2+3+4+5+6+7+8+9+10
print(i)


sum=0
for i in range(1,11,1):
    sum+=i
print(sum)
'''


# For using Factorial::
'''
factorial=1
for i in range(5,0,-1):
    factorial*=i
print(factorial)
'''

#  Another way write this code
'''
factorial=1
for i in range(1,6,1):
    factorial*=i
print(factorial)
'''


# Continue Func.
'''
for guest in range(1,6,1):
    if guest==3:
        continue
    print("guest",guest)
'''

# First Method::
'''
for i in range(1,51,1):
 if i%2==0:
  print(i)
'''

# Another Method
'''
for i in range(2,51,2):
 print(i)
'''

# i=1
# while(i%7):
#  i+=1
#  print(i)

# total=1,2,3,4,6
# for total in range(total):
#  print(total)

# i=0
# sum=0
# for i in range(1,8,2):
#  sum=sum+i
# print(sum)
# i+=1


# for i in range(1,):
#  print(i*12)

# sum=0
# for i in range(1,7+1,2):
#     sum=sum+i
# print(sum)
# i+=1

#
# i=0
# sum=0
# while (i<=4):
#     if (i%2==1):
#         sum=sum+i
#     print(sum)
#     i+=1

# age =2
# age =15
# age = 60
# age=5
# age=30
# if age>=13<18:
#     print("5Kms")
# elif age>=18<30:
#     print("10 Kms")
# else:
#     print("You can make friends anywhere ")
#     # print("10 Kms")





# Nested Loop


# for printing (1,2,3,4,5) in next line
# for i in range(1,6):
#     for j in range(1,6):
#         print(j,end=" ")
#     print()
# for printing (*) in next line:
# for i in range(5):
#     for j in range(1,6,1):
#         print('*',end=" ")
#
#     print()
#
# for printing same number in different line:
# for row in range(1,6):
#     for star in range(1,6):
#         print(row,end=" ")
#     print()


# for printing (*) in pyramid format:*
# * *
# * * *
# * * * *
# * * * * *
# for row in range(1,6):
#     for star in range(1,row+1,1):
#         print("*",end=" ")
#     print()

# for printing numbers(1-5)1
# 1 2
# 1 2 3
# 1 2 3 4
# 1 2 3 4 5 :
# for i in range(6):
#     for j in range(1,i+1,1):
#         print(j,end=" ")
#     print()

# for printing revers pyramid:
# * * * * *
# * * * *
# * * *
# * *
# *
#
# for rows in range(5,0,-1):
#     for stars in range(rows):
#         print('*',end=" ")
#     print()

# for printing numbers(1-5):1 2 3 4 5
# 1 2 3 4
# 1 2 3
# 1 2
# # 1
# for rows in range(5,0,-1):
#     for stars in range(1,rows+1):
#         print(stars,end=" ")
#     print()


#print this type method:
# 1
# 1 2
# 1 2 3
# 1 2 3 4
# 1 2 3 4 5
# 1 2 3 4 5
# 1 2 3 4
# 1 2 3
# 1 2
# 1


# for i in range(6):
#     for j in range(1,i+1,1):
#         print(j,end=" ")
#     print()


# for rows in range(5,0,-1):
#     for stars in range(1,rows+1):
#         print(stars,end=" ")
#     print()
