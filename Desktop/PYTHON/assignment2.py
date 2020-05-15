#Task2
i=9
if i%3==0:
    print("Consultadd")
if i%5==0:
    print("c")
if i%3 == 0 and i%5==0:
    print("Consultadd Training")

##2nd question

x=int(input("Enter any number between 1 to 5"))
if x==1:
    first = int(input("Enter any number"))
    second = int(input("Enter an another number"))
    res = first+second
    print(res)
if x==2:
    first = int(input("Enter any number"))
    second = int(input("Enter an another number"))
    res = first-second
    print(res)
if x==3:
    first = int(input("Enter any number"))
    second = int(input("Enter an another number"))
    res = first/second
    print(res)
if x==4:
    first = int(input("Enter any number"))
    second = int(input("Enter an another number"))
    res = first*second
    print(res)
if x==5:
    first1=int(input("Enter number"))
    second2=int(input("enter an another number"))
    res=(first1+second2)/2
    print(res)
if res<0:
    print("zsa")

#3rd question

a=10
b=20
c=30
avg = (a+b+c)/30
if avg>a and avg>b and avg>c:
    print("avg is higher than a,b and c")
elif avg>a and avg>b:
    print("avg is greater than a and b")
elif avg>a and avg>c:
    print("avg is greater than a and c")
elif avg>b and avg>c:
    print("avg is greater than b and c")
elif avg>a:
    print("greater than a")
elif avg>b:
    print("greater than b")
elif avg>c:
     print("greater than c")

#4th question
n=[1,2,3,1,-2,3]
for i in n:
    if i>0:
        print("good going",i)
        continue
    elif i<0:
        break
print("its over")

#5th question
for i in range(2000,3201):
    if i%7==0 and i%3!=0:
        print(i)

#6th - Object is not iterable
#0,1,2
#break is not defined

#7th
for i in range(0,6):
    if i==3:
        continue
    print(i)

#8th
n = input("enter a string")
d={'letters':0,'digits':0}
for i in n:
    if i.isdigit():
        d['digits']+=1
    if i.isalpha():
        d['letters']+=1
print("letters",d['letters'])
print("digits",d['digits'])

#9th
lucky_number = 5
number=int(input("guess a number"))
while number!=lucky_number:
    answer=input("hard luck!,wann guess again?Enter yes or no")
    if answer=='yes':
        number=int(input("guess a number"))
    elif answer=='no' or number==lucky_number:
        print("okay,try next time")
        break

#10th

counter=1
n=5
while counter<5:
    n=int(input("enter a number"))
    if n!=5:
        print("try again")
        counter+=1
    elif n==5:
        print("good guess")
print("game over")

    
#11th
counter=0
n=5
while counter<5:
    n=int(input("enter a number"))
    if n!=5:
        print("try again")
        counter+=1
    if n==5:
        print("good guess")
        break
    elif counter==5:
        print("game over")
