x=[1,2,3,4,5,1,2,3]
print(x)
y=[6,7,8,9,5]
for i in range(len(y)):
    print(x[i]+y[i])

sum=0
for value in range(1,6):
    sum=sum+value
print(sum)




a=set({1,2,3,4,5})
b=list(a)
b[0] = 0
a=set(b)
print(a)

#n= int(input("Enter any number"))
#d=dict()
#for i in range(1,n):
 #   d[i]=i*i
#print(d)

#n=input("Enter any sentence")
#d={'digits':0,'letters':0}
#for i in n:
    #if i.isdigit():
        #d['digits']+=1
    #elif i.isalpha():
        #d['letters']+=1
    #else:
        #pass

#print(d['digits'])
#print(d['letters'])

n=input("Enter your name")
str1=dict()
for i in n:
    if i in str1:
        str1[i]+=1
    else:
        str1[i]=1
    
print(str1)



