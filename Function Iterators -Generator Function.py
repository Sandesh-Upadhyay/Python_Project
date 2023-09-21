'''
def printVal(l):
    for value in l:
        yield value
l=[10,20,30,40,50,60]
g = printVal(l)
print(next(g))
print(next(g))
print(next(g))
print(next(g))
print(next(g))
'''


'''def fibo():
    first_num = 0
    second_num = 1
    while(True):
        next_val = first_num+second_num
        yield next_val
        first_num,second_num = second_num,next_val

g = fibo()
print(g)
print(next(g))
print(next(g))
print(next(g))
print(next(g))
print(next(g))
print(next(g))
for value in range(10):
    print(next(g))

for value in range(20):
    print(next(g))'''


'''
l= [10,20,30,40,50,60]
l2 = (value * value for value in l)
print(l2)
print(next(l2))
print(next(l2))
print(next(l2))
print(next(l2))
print(next(l2))
print(next(l2))
'''











