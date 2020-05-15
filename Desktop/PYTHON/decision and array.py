#a=[1,2,3,[4,5,["sup",34.67,"kam"],6,7],8,9,10]
#b=a[3][2][2]
#print(b)
x=10
if x==10:
    print("The value of x -",x)
    if x==5:
        print("yes")
    elif x==1:
        print("I am there")
    else:
        print("hello")
    
x = [1,2,3,[10,[20,30],40],6,7,8,9]
y = x[3][1][0]
print(y)

import numpy as np
x=[1,2,3,4,5,6]
res = np.array(x)
print(res)

a=range(1,10)
print(a)

x=[1,2,3,4,5]
y=[6,7,8,9,10]
for i in range(len(x)):
    for j in range(len(y)):
        res=x[i]*y[j]
        



