'''
Loops:-

Q1:- Calculate the sum of all numbers from 1 to a given number

Q2:- Display numbers from a list using loop
Write a program to display only those numbers from a list that satisfy the following conditions

The number must be divisible by five
If the number is greater than 150, then skip it and move to the next number
If the number is greater than 500, then stop the loop

Q3:-  Count the total number of digits in a number
Write a program to count the total number of digits in a number using a while loop/ for loop.

For example, the number is 75869, so the output should be 5.

Q4:- Print list in reverse order using a loop
Given:

list1 = [10, 20, 30, 40, 50]

Q5:- Use a loop to display elements from a given list present at odd index positions
Given:

my_list = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100]
Note: list index always starts at 0

Expected output:
20 40 60 80 100
'''
# Functional programming

'''
def FuncName(num1,num2):
    logic
    return/print
FuncName(15,10)

'''

# def add(a,b):
#     print( a+b)
# add(10,15)
# print(add(10,15))
# result = add(10,25)
# print(result)
# start:end:step:
my_list = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100]
for i in my_list[1::2]:
    print(i, end=" ")

def no_of_digits(num):
    count = 0
    while(num != 0):
        num = num//10
        count += 1
    return count

nums = no_of_digits(24568)
print(nums)

# take input list of length 5 from user
def show(lst):
    for i in lst:
        print(i)
show([1,5,7,9,10])


'''
Github:- 
'''



