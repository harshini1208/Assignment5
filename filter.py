#filter fn to print only vowels
def vowels_list(variable):
    vowels=['a','e','i','o','u']
    if variable in vowels:
        return True
    else:
        return False
l =['j','k','l','m','n','e','q','p','i']
filtered=filter(vowels_list,l)
print('the filtered letters are:')
for s in filtered:
    print(s)

#filter fn to list where each element is greater than or equal to 70
scores=[70,80,60,90,50]
filtered=[]
for score in scores:
    if score>=70:
        filtered.append(score)
print(filtered)

#using lamda
scores=[70,80,60,90,50]
filtered=list(filter(lambda score:score>=70,scores))
print(filtered)

#to check if number is multiple of 3
def multiple_of(num):
    return num%3==0
numbers=[1,2,3,4,5,6,7,8,9,10,]
result=list(filter(lambda x:multiple_of(x),numbers))
print(result)