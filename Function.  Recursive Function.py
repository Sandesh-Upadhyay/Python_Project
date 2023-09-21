'''
def factorial(num):
    if num == 1:
        return 1
    else:
        return num * factorial(num - 1)

num1 = 5
result = factorial(num1)
print(result)
'''

# factorial(5)
# 5 * factorial(4)
# 4 * factorial(3)
# 3 * factorial(2)
# 2 * factorial(1)
# 1



'''

def factorial(num):
    if num == 1:
        return 1
    else:
        return num * factorial(num - 1)


num1=5
result = factorial(num1)
print(result)
'''

# Example of recursive function

'''
def factorial(n):
    if n==1:
        return 1
    else:
        return n * factorial(n-1)

n=10
print (factorial(n))
'''

'''
def factorial (n):
    if n == 1:
        return 1
    else:
        return n*factorial(n-1)

n=3
print(factorial(n))
'''

# Binary Search in Recursive Function::

'''
def binary_search(l,key):
    mid = len(l) // 2

    if l[mid] == key:
        return True
    elif key < l[mid]:
        return binary_search(l[:mid],key)
    else:
        return binary_search(l[mid + 1:],key)



l=[100,200,300,400,500,600,700,800,900]
key=500
result = binary_search(l,key)
print(result)
'''



'''
def binary_search(arr, low, high, x):
    if high >= low:
        mid = (high + low) // 2
        if arr[mid] == x:
            return mid
        elif arr[mid] > x:
            return binary_search(arr, low, mid - 1, x)
        else:
            return binary_search(arr, mid + 1, high, x)
    else:
        return -1
'''

'''
The code you provided is a recursive binary search function in Python. It does not have any output by itself. It is a function that can be called with arguments to search for a value in an array.

If you call the function with an array, starting index, ending index, and value to search for, it will return the index of the value if it is found in the array. If the value is not found in the array, it will return -1.

I hope this helps. Let me know if you have any more questions.
'''


# Creating Modules and Packages::

# next Mod1 and Mod2

