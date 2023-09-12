# use reduce fn to add two numbers
from functools import reduce
l1=[2,3,4,5,6,7,8,9,10]
l2=(reduce(lambda x,y:x+y,l1))
print(l2)

#multiplying numbers using reduce fn
from functools import*
def product(x,y):
    return x*y
result=reduce(product,[2,5,3,7])
print(result)

#mul numbers using lambda fn
from functools import*
lst=[1,2,3,4,5]
result=reduce(lambda x,y:x*y,lst)
print(result)

#reduce fn with 3 parameters:
from functools import reduce
l1=(1,2,3,6,7)
print(reduce(lambda a,b:a+b,l1,4))

