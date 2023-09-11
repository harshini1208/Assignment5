#recursive fn for towers of hanoi
def towerofhanoi(numrings,from_pole,to_pole,aux_pole):
    if numrings==1:
        print("move ring 1 from",from_pole,'pole to',to_pole,'pole')
        return
    towerofhanoi(numrings-1,from_pole,aux_pole,to_pole)
    print("move ring",numrings, "from",from_pole,'pole to',to_pole,'pole')
    towerofhanoi(numrings-1,aux_pole,to_pole,from_pole)
    numrings=2
    towerofhanoi(numrings,'left','right','middle')

#set a number to a power using recursive function
def power(num,topwr):
        if topwr==0:
            return 1
        else:
            return num*power(num,topwr-1)
        print('{} to the power of {}'.format(4,7,power(4,7)))

 #fibonacci series using recursive functions
def fibonacci(n):
     if n<=1:
          return n
     else:
          return fibonacci(n-1)+fibonacci(n-2)
number=14
print("fibonacci series")
for i in range(number):
     print(fibonacci(i))

        

    

