#nested functions for multiplication
def multi(a):
    def mul(b):
        def mu(c):
            return a*b*c
        return mu
    return mul
m=multi(2)(3)(4)
print(m)

#nested fn for addition of two numbers
def num1(x):
    def num2(y):
        return x+y
    return num2
print(num1(10)(5))


#nested fn to print strings
def greeting(first,last):
    def full_name():
        return first+""+last
    print("Hi" +full_name()+"!")
greeting('Harshini','Sakhamuru')

#nested fn ex
def outer():
    print("I'm the outer function")
    def inner():
        print("I'm the inner function.")
    inner()
outer()        
