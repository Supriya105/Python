
#taskthree

#1st
list1 = [10,10.36,'i+3',"supriya"]
print(list1)

#2nd
list2 = [1,2,3,4]
print(list2[:])
print(list2[1:3])

#3rd
list3 = [1,2,3,4]
sum=0
mul=1
for i in list3:
    sum=sum+i
    mul=mul*i
print(sum)
print(mul)

#4th 
list3 = [2,1,4,3]
list3.sort()
max=list3[-1]
min=list3[0]
print(max)
print(min)

#5th
list4 = [2,3,4,5,6,8]
list3=list()
for i in list4:
    if i%2!=0:
        list3.append(i)
        print(list3)


#6th
l = list()
for i in range(1,31):
	l.append(i**2)
print(l[:5])
print(l[-5:])

#7th
list=[[1,3,5,7,9,10],[2,4,6,8]]
num1 = list[0]
num2=list[1]
num1[-1:]=num2
print(num1)


#8th
a={1:10,2:20}
b={3:30,4:40}
a.update(b)
print(a)

#9th
list=[1,2,3,4]
d={}
for i in list:
    d[i]=i*i
print(d)

#or
d={}
for i in range(0,6):
    d[i]=i*i
print(d)

#10th
values = input("Input some comma separated numbers : ")
list = values.split(",")
tuple = tuple(list)
print('List : ',list)
print('Tuple : ',tuple)
