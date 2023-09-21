# a=10
# c=a+1
# b=10
# d=b+1
# print(a)
# print(b)
# print(c)
# print(d)


# x=1
# print(x)
# x+=5
# print(x)
# x+=10
# print(x)
# x=x+4
# print(x)

# x=1
# print(x)
# x+=3
# print(x)
# x-=10
# print(x)
# x=x+4
# print(x)

# jump=1
# while(jump<=5):
#   print("jump")
#   jump=jump+1

# jump=2
# while(jump<=3):
#     print("jump")
#     jump=jump+1

# jump=2
# while(jump<=10):
#     print("jump")
#     jump=jump+1

# jump=2
# while(jump<=6):
#     print("jump")
#     jump=jump+1


# jump=2
# while(jump<=3):
#   print("jump")
#   jump=jump+1

# jump=2
# while(jump<=6):
#     print("jump")
#     jump=jump+1

# jump=1
# while(jump<=5):
#     print("jump")
#     jump=jump+1

# jump=1
# while(jump<=5):
#     print("jump")
#     jump=jump+2



# jump=1
# while(jump<=10):
#     print("jump")
#     jump=jump+2



# jump=1
# while(jump<=10):
#     print("jump")
#     jump=jump+3




# jump=1
# while(jump<=15):
#     print("jump")
#     jump=jump+5


# jump=0
# while(jump<=20):
#     print("jump")
#     jump=jump+10

# jump=1
# while(jump<=10):
#     print("jump")
#     jump+=1


# find=1
# while(find<=5):
#     print("jump")
#     find+=1


# when we want to print only 9 numbers
'''
jump=1
while(jump<10):
    print("jump")
    jump+=1


'''


# reverse
'''
position=100
while(position>=0):
    print("Current position",position)
    position-=1
    
    
position=7
while(position>=1):
    print("Current position",position)
    position-=3  
    
    
employeeCode=1000;
while(employeeCode>=0):
    print("Send the above notice",employeeCode)
    employeeCode-=1      
'''



# Break::
'''
guest=1
while(guest<=10):
    if(guest==4):
        break
    print("guest",guest)
    guest+=1

guest=1
while(guest<=10):
    if(guest==4):
        break
    print("guest",guest)
    guest+=1
print("outside while",guest)

guest=1
while(guest<=10):
    if(guest==3):
        break
    print("guest",guest)
    guest+=1
print("outside while",guest)

guest=1
while(guest<=10):
    if(guest==5):
        break
    print("guest",guest)
    guest+=1
'''



# Continue::

'''
guest=1
while(guest<=10):
    guest+=1
    if(guest==5):
        continue
    print("guest",guest)


guest=0
while(guest<=5):
    guest+=1
    if(guest==3):
        continue
    print("guest",guest)


guest=1
while(guest<=10):
    guest+=1
    if(guest==5):
        continue
    print("guest",guest)

i=0
sum=0
while(i<=10):
    sum=sum+i
    i+=1
print(sum)



i=5
while(i<=20):
    print(i)
    i+=1


# for odd number

i=0
while(i<=15):
    if(i%2==1):
     print(i)
    i+=1

i=1
while(i<=15):
 print(i)
 i+=2  //output also come in odd numbers




i=0
while(i<=15):
    if(i%2==1):
     print(i)
    i+=1  // output come in even number


i=0
sum=0
while(i<=15):
    if (i%3==0):
     sum=sum+i
    i+=1
print(sum)

'''



# Average of these numbers from 0 to 100::
# Average formula=total number of sum/ total digit
'''
i=1
sum=0
count=0
while(i<=100):
    if(i%2==0):
        sum=sum+i
        count=count+1
    i+=1
print(sum/count)
'''
# i=1
# while(i>n<):
#     if(i%2==0):
#         print(i)
#     i+=1

# i=1
# while(i<=12>0):
#     if(i%2==0):
#         print(i)
#     i+=1

#
# i=1
# sum=0
# while(i<=6):
#     if(i%2==0):
#       sum=sum+i
#       print(sum)
#     i+=1


# i=0
# sum=0
# while(i<=6):
#     if (i%2==0):
#         sum=sum+i
#         print(sum)
#     i+=1


# i=1
# sum=0
# while(i<=6):
#     if (i%2==0):
#         sum=sum+i
#         print(sum)
#     i+=1

# i=1
# sum=0
# while(i<=6):
#     if (i%2==0):
#         sum+=i
#     i+=1
# print(sum)


# one=7
# two=3
# three=4
# four=5
#
# sum1=one+two
# sum2=three+four
#
# if sum1>=sum2:
#     print("Yes")
# else:
#     print("No")

# age =12
# if age<13:
#     print("1km")
# elif age>=13<18:
#     print("5km")
# elif age>=18<30:
#     print("10 km")
# # elif age>=30:
# #     print("")
# else:
#     print("anywhere")

# num=1
# num1=2
#
# if num%2==0 and num1%2==0:
#     print("even")
# elif num%2!=0 and num1%2!=0:
#     print("Odd")
# else:
#     print("Even-Odd")


# x=11
# x+=1
# x=x+4
# x=x+8
# print(x)
# x-=10
# x=x-5
# print(x)


# num=1
# while(num>=-31):
#     print(num)
#     num-=4

# guest=1
# while(guest<20):
#     if(guest==19):
#         break
#     print("guest: ",guest)
#     guest+=1

# guest=0
# while(guest<7):
#     if(guest==6):
#         break
#     print("guest: ",guest)
#     guest+=1

# guest=1
# while(guest<7):
#     if(guest==6):
#         break
#     print("guest: ",guest)
#     guest+=1

# Method (I)

'''
i=3
while(i<=20):
    print(i)
    i+=3
'''

# Method (II)

'''
i=1
while(i<=20):
    if (i%3==0):
        print(i)
    i+=1
'''

# Continue[in while loop when we using continue func.
# then we should put print statement and after continue func.

'''guest=0
while(guest<6):
 guest+=1
 if (guest==3):
  continue
 print("guest",guest)
'''