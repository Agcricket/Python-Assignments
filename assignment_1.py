# -*- coding: utf-8 -*-
"""Assignment 1

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1a3u4Il6SXme2Uc7QYbogMpR2-F6wuWGn
"""

#Q1
print('"Twinkle, twinkle, little star,\n\t How I wonder what you are!\n\t\t Up above the world so high,\n\t\t\t Like a diamond in the sky.\n\t\t\t\t Twinkle, twinkle, little star,\n\t\t\t\t\t How I wonder what you are"')

#Q2
first_name = input("Enter your first name: ")
last_name = input("Enter your last name: ")
print(last_name + " " + first_name)

#Q3
radius=float(input("Enter the value of radius of circle : "))
area=(3.14)*(radius**2)
print("Area of circle is : ",area)

#Q4
color_list=["Red","Green","White" ,"Black"]
first_c=color_list[0]
last_c=color_list[3]
print("First color is : ",first_c)
print("Last color is : ",last_c)

#Q5
n=int(input("Enter the value of n : "))
a=n+n*n+n*n*n
print("Value of n+nn+nnn is : ",a)

#Q6
x = str(input("Enter the number: ")).split(",")
print(x)
x = tuple(x)
print(x)

#Q7
C=float(input('Enter the temprature : '))
F=(1.8)*C+32
print("Temprature in Fahrenheit is :  ",F)

#Q8
a=int(input("Enter the value of a : "))
b=int(input("Enter the value of b : "))
print('Values of a and b before swapping is : ',a,b)
k=a
a=b
b=k
print('Value of a and b after swapping is : ',a,b)
a+=1
print('Value of a after increment is : ',a)

#Q9
a=int(input("Enter the value of a : "))
if (a%2==0):
    print("number is even")
else:
    print("number is odd")

#Q10
year=int(input("Enter the year : "))
if (year%4==0 and year%100!=0) or (year%400==0):
    print("the year is a leap year")
else:
    print("the year is not a leap year")

#Q11
x1,y1 = int(input("x1:")), int(input("y1:"))
x2,y2 = int(input("x2:")), int(input("y2:"))
dist = ((x2 - x1)**2 + (y2 - y1)**2)**0.5
print(dist)

#12
a=float(input("Enter the value of fisrt angle: "))
b=float(input("Enter the value of second angle: "))
c=float(input("Enter the value of third angle: "))
if (a+b+c==180):
    print("can make a triangle")
else:
    print("cannot make a triangle")

#13
principal_amount = float(input("Enter the principal amount: "))
rateof = float(input("Enter the annual interest rate (as a percentage): ")) / 100
timeof = float(input("Enter the time (in years): "))
n = int(input("Enter the number of times interest is compounded per year: "))

amount = principal_amount * (1 + rateof / n) ** (n * timeof)
interest = amount - principal_amount
print("Compound Interest: ",interest)
print("Total Amount : ",amount)

#14
n= int(input("Enter a positive integer: "))
if n<= 1:
    print(f"{n} is not a prime number.")
else:

    prime = True


    for i in range(2, int(n**0.5) + 1):
        if n% i == 0:
            prime = False
            break

    if prime:
        print(" the entered number is a prime number.")
    else:
        print("the entered number is not a prime number.")

#15
n=int(input("Enter a positive integer : "))
answer= n * (n + 1) * (2 * n+ 1) // 6
print("The sum of squares from (1^2) to (n^2) is: ",answer)