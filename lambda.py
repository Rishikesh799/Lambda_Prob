"""-----------------------------LAMBDA PROBLEM---------------------------------------------------------
#1. Write a Python program to create a lambda function that adds 15 to a given number passed in as an argument, also create a lambda function that multiplies argument x with argument y and print the result

x= lambda i:(i+15)
print(x(10))==25
y=lambda j,k:j*k
print(y(12,4))==48
------------------------------------------------------------------------------------------------------------
#2. Write a Python program to create a function that takes one argument,
#and that argument will be multiplied with an unknown given number.

def num(n):
    return lambda x:x*n
y=num(15)
print(y(2))==30
print(y(3))==45
print(y(4))==60
----------------------------------------------------------------------------------------------------------
#3. Write a Python program to sort a list of tuples using Lambda.
#Original list of tuples:

x=[('English', 88), ('Science', 90), ('Maths', 97), ('Social sciences', 82)]
y=sorted(x,key=lambda i:i[1],reverse=False)
print(y)
[('Social sciences', 82), ('English', 88), ('Science', 90), ('Maths', 97)]
--------------------------------------------------------------------------------------------
#4. Write a Python program to sort a list of dictionaries using Lambda.
x=[{'make': 'Nokia', 'model': 216, 'color': 'Black'}, {'make': 'Mi Max', 'model': '2', 'color': 'Gold'}, {'make': 'Samsung', 'model': 7, 'color': 'Blue'}]

y=sorted(x,key=lambda i:int(i["model"]),reverse=True)
print(y)
[{'make': 'Nokia', 'model': 216, 'color': 'Black'}, {'make': 'Samsung', 'model': 7, 'color': 'Blue'}, {'make': 'Mi Max', 'model': '2', 'color': 'Gold'}]
--------------------------------------------------------------------------------------------------------
#5. Write a Python program to filter a list of integers using Lambda.

x=[1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
print(list(filter(lambda x:x%2==0,x)))
#[2, 4, 6, 8, 10]
print(list(filter(lambda x:x%2!=0,x)))
#[1, 3, 5, 7, 9]
---------------------------------------------------------------------------------------------------------
#6. Write a Python program to square and cube every number in a given list of integers using Lambda.

x=[1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
print(list(map(lambda x:x**2,x)))
print(list(map(lambda x:x**3,x)))
[1, 4, 9, 16, 25, 36, 49, 64, 81, 100]
[1, 8, 27, 64, 125, 216, 343, 512, 729, 1000]
-----------------------------------------------------------------------------------------
#7. Write a Python program to find if a given string starts with a given character using Lambda.

x=["rishi","pranay","pratik"]
print(list(map(lambda x:x[0]=="r",x)))
[True, False, False]
--------------------------------------------------------------------
#8. Write a Python program to extract year, month, date and time using Lambda.

import datetime
z=datetime.datetime.now()
print(z)
year = lambda x:x.year
print(year(z))
month= lambda x:x.month
print(month(z))
day= lambda x:x.day
print(day(z))
##2022-01-13 16:03:04.952774
2022
1
13
-----------------------------------------------------------------------------------------
#9. Write a Python program to check whether a given string is number or not using Lambda.

x=["rishi","vicky",1,2,"dev",89]
print(list(map(lambda x:type(x)==int,x)))
[False, False, True, True, False, True]
-----------------------------------------------------------------------------------------
#11. Write a Python program to find intersection of two given arrays using Lambda.

x=[1, 2, 3, 5, 7, 8, 9, 10]
y=[1, 2, 4, 8, 9]
print(list(filter(lambda i:i in x,y)))
[1, 2, 8, 9]
------------------------------------------------------------------------------------------------------
#12. Write a Python program to rearrange positive and negative numbers in a given array using Lambda.

x=[-1, 2, -3, 5, 7, 8, 9, -10]
y= sorted(x, key = lambda i: 0 if i == 0 else -1 / i)
print(y)
[2, 5, 7, 8, 9, -10, -3, -1]
----------------------------------------------------------------------------------------------------
#13. Write a Python program to count the even, odd numbers in a given array of integers using Lambda.

a=[1, 2, 3, 5, 7, 8, 9, 10]
print(len(list(filter(lambda x:x%2==0,a))))
print(len(list(filter(lambda x:x%2!=0,a))))
3
5
--------------------------------------------------------------------------------------------------------
#14.Write a Python program to find the values of length six in a given list using Lambda.

a=['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday']
print(list(filter(lambda x:len(x)==6,a)))
['Monday', 'Friday', 'Sunday']
--------------------------------------------------------------------------------------------------
#15. Write a Python program to add two given lists using map and lambda

a=[1, 2, 3]
b=[4, 5, 6]
print(list(map(lambda i,j:i+j,a,b)))
[5, 7, 9]
---------------------------------------------------------------------------------------------------------------
#16. Write a Python program to find numbers divisible by nineteen or thirteen from a list of numbers using Lambda

a=[19, 65, 57, 39, 152, 639, 121, 44, 90, 190]
print(list(filter(lambda x:x%19==0 or x%13==0,a)))
[19, 65, 57, 39, 152, 190]
-----------------------------------------------------------------------------------------------------------------
#17. Write a Python program to find palindromes in a given list of strings using Lambda

a=['php', 'w3r', 'Python', 'abcd', 'Java', 'aaa']
print(list(filter(lambda x:x[::-1]==x,a)))
['php', 'aaa']
--------------------------------------------------------------------------------------------------
#18.Write a Python program to find the numbers of a given string and store them in a list,
#display the numbers which are bigger than the length of the list in sorted form. Use lambda function to solve the problem.

a="sdf 23 safs8 5 sdfsd8 sdfs 56 21sfs 20 5"
q=a.split()
z=len(q)
k=[]
for i in q:
    if i.isdigit():
        k.append(i)
s=list(filter(lambda x:int(x)>len(q),k))
print(sorted(s))
['20', '23', '56']
---------------------------------------------------------------------------------------------------------
#19.Write a Python program that multiply each number of given list
#with a given number using lambda function.Print the result.

a=[2, 4, 6, 9, 11]
b=2
print(list(map(lambda x:x*b,a)))
[4, 8, 12, 18, 22]
-----------------------------------------------------------------------------------------------------------
#20. Write a Python program that sum the length of the names of a
# given list of names after removing the names that starts with an lowercase letter. Use lambda function.

a=['sally', 'Dylan', 'rebecca', 'Diana', 'Joanne', 'keith']
x=list(filter(lambda x:x[0].isupper(),a))
print(len("".join(x)))
16
----------------------------------------------------------------------------------------------------------
#21.Write a Python program to calculate the sum of the positive and negative numbers of a given list of numbers using lambda function.

a=[2, 4, -6, -9, 11, -12, 14, -5, 17]
print(sum(list(filter(lambda x:x>0,a))))
print(sum(list(filter(lambda x:x<0,a))))
48
-32
"""
#22.Write a Python program to find the list with maximum and minimum length using lambda.

a=[[0], [1, 3], [5, 7], [9, 11], [13, 15, 17]]
x=list(map(lambda x:(x,len(x)),a))
print(max(x))
([13, 15, 17], 3)
-------------------------------------------------------------------------------------------------------
#23.Write a Python program to sort a given list of lists by length and value using lambda.

a=[[2], [0], [1, 3], [0, 7], [9, 11], [13, 15, 17]]
x=sorted(a,key=lambda x:(len(x),x))
print(x)
[[0], [2], [0, 7], [1, 3], [9, 11], [13, 15, 17]]
------------------------------------------------------------------------------------------------------------------------
#24.Write a Python program to find the maximum value in a given heterogeneous list using lambda.

a=['Python', 3, 2, 4, 5, 'version']
x=list(filter(lambda x: type(x) == int,a))
print(max(x))==5
"""

