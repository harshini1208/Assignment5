#lambda function examples
#sqaure of given no using  lambda function
s=lambda n:n*n
n=int(input("enter a number"))
print(s(n))

#write a lambda to find biggest of 2 numbers
s=lambda x,y:x if x>y else y
x=int(input("enter a number"))
y=int(input("enter a number"))
print("the biggest no is ",s(x,y))

#write lambda to find sum of two numbers
s=lambda x,y:x+y
x=int(input("enter a number"))
y=int(input("enter a number"))
print(s(x,y))

