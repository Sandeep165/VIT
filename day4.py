'''
Create a function that takes a list containing only numbers and return the first element.

Examples
get_first_value([1, 2, 3]) ➞ 1

get_first_value([80, 5, 100]) ➞ 80

get_first_value([-500, 0, 50]) ➞ -500
Notes
The first element in a list always has an index of 0.


Create a function that takes two arguments. Both arguments are integers, a and b. Return True if one of them is 10 or if their sum is 10.

Examples
makes10(9, 10) ➞ True

makes10(9, 9) ➞ False

makes10(1, 9) ➞ True
Notes
Don't forget to return the result.

Create a function that takes three arguments prob, prize, pay and returns True if prob * prize > pay; otherwise return False.

To illustrate:

profitable_gamble(0.2, 50, 9)
... should yield True, since the net profit is 1 (0.2 * 50 - 9), and 1 > 0.

Examples
profitable_gamble(0.2, 50, 9) ➞ True

profitable_gamble(0.9, 1, 2) ➞ False

profitable_gamble(0.9, 3, 2) ➞ True
Notes
A profitable gamble is a game that yields a positive net profit, where net profit is calculated in the following manner: 
net_outcome = probability_of_winning * prize - cost_of_playing.

'''
# lst1 = ["mumbai","pune","goa"]
# print(lst1[0])
# print(lst1[1])
# print(lst1[2])
def get_first_value(lst):
    return lst[0]

def makes10(a, b):
    if ((a == 10 or b == 10) or (a + b == 10)) :
        return True
    else:
        return False
print(makes10(9,10))

def profitable_gamble(prob,prize,pay):
    if (prob*prize)>pay:
        print("True")
    else:
        print("False")
profitable_gamble(0.9,3,2)

# Recursion
# 5! = 5*4! = 5*4*3! = 5*4*3*2! = 5*4*3*2*1! = 5*4*3*2*1
# n*n-1!

def fact(numb):
    if numb == 1:
        return 1
    else:
        return(numb*fact(numb-1))    #5 * fact(4) == 5*4*fact(3) = 5*4*3*fact(2) = 5*4*3*2*1 = 120

def func1(n):
    if n==1:
        return 1
    else:
        return 1 +func1(n//2)   # 1 + fun1(2)  = 1 + 1 + fun1(1) = 1+1+1 = 3

'''
 create a function that finds all even numbers from 1 to the given number.

Examples
find_even_nums(8) ➞ [2, 4, 6, 8]

find_even_nums(4) ➞ [2, 4]

find_even_nums(2) ➞ [2]

vals = []
for value in collection:
  if condition:
    vals.append(expression)


Write a function that takes a list and a number as arguments. Add the number to the end of the list, then remove the first element of the list. The function should then return the updated list.

Examples
next_in_line([5, 6, 7, 8, 9], 1) ➞ [6, 7, 8, 9, 1]

next_in_line([7, 6, 3, 23, 17], 10) ➞ [6, 3, 23, 17, 10]

next_in_line([1, 10, 20, 42 ], 6) ➞ [10, 20, 42, 6]

next_in_line([], 6) ➞ "No list has been selected"
Notes
For an empty list input, return: "No list has been selected"


Create a function that takes three integer arguments (a, b, c) and returns the amount of integers which are of equal value.

Examples
equal(3, 4, 3) ➞ 2

equal(1, 1, 1) ➞ 3

equal(3, 4, 1) ➞ 0 
Notes
Your function must return 0, 2 or 3.
'''