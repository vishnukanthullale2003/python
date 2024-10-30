"""import keyword
print(len(keyword.kwlist))
print(keyword.kwlist )"""

"""x="123"
print(type(x))
y=int(x)
print(type(y))
print(y)"""

"""import math
x=math.factorial(4)
print(x)

import turtle
y=turtle.Screen()
y.setup(200,200)"""

"""print("enter the age")
x=int(input())
if x <= 17:
    print("you are elgible for vote")
else:
    print("you are not elgible")"""

"""r=float(input("enter the area of a circle"))
a=3.14*r*r
print("thearea of a circle is :",a)"""




# day 2

"""x=435
print(bin(x))

print(oct(x))

print(hex(x))

a=[5,8,12,5,7,8,3,54,21,6,4,85,84,789,52,0]
print(max(a))
print(min(a))

print(len(a))

b=4
print(id(b))

c=4
print(id(c))

d=5
c=5.0

print(c==d)

print(c is d)

x=int(input("enter a number"))
if x>0:
    print(x,"is positive")
elif x<0:
    print(x, "is negative")
else:
    print(x,"neither negative  nor positive")"""

""""z=int(input("enter the first number"))
y=int(input("enter the second number"))
if (z>y):
    print(z,"is greater")
elif (y>z):
    print(q,"is grater")
else:
    print("both are equal")"""


#loops

'''for i in range(0,100,2):
    print(i)'''

  
#write a program to check whether the given number is even or odd

'''a=int(input("enter the number"))
if a%2==0:
    print("the number is even")
else:
    print("the given number is odd")'''

#LISTS

a=[11,12,13,14,15,16]
'''a.append(17)
print(a)
del a[0]
print(a)'''

'''a.sort()
print(a)
a.reverse()
print(a)

#help(list)

a.remove(13)
print(a)

a.pop(0)
print(a)'''

'''a.insert(0,11)
print(a)


print(a.index(12))

b=4
print(id(b))'''

'''b=a[1:4:1]
print(b)

b=a[1::]
print(b)


c=(2,3,4,5,6,7,8,9,10,11)
d=list(c)
print(d)

d.reverse()
d.remove(3)
print(d)
print(d)'''

a={1,2,3,4,5,5,6,7,8,9,9,1,2,10}
print(a)
a.remove(1)
print(a)

a1={2,3,4,5,6}

b=a.issubset(a1)
print(b)

c=a1.issubset(a)
print(c)

k1=set()
print(type(k1))


p=1234
c=0
while c!=3:
    c=c+1
    pin=int(input("enter the pin"))
    if (pin == p):
        print("the pin is correct")
    else:
        print("please try again")
else:
    print("your card i sblocked")



