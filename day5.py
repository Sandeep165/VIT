# lamda map filter
'''
Write a function that takes an integer minutes and converts it to seconds.

Examples
convert(5) ➞ 300

convert(3) ➞ 180

convert(2) ➞ 120
Notes
Don't forget to return the result.

There is a single operator in Python, capable of providing the remainder of a division operation. 
Two numbers are passed as parameters. The first parameter divided by the second parameter will have a remainder, possibly zero. Return that value.

Examples
remainder(1, 3) ➞ 1

remainder(3, 4) ➞ 3

remainder(5, 5) ➞ 0

remainder(7, 2) ➞ 1
Notes
The tests only use positive integers.
Don't forget to return the result.

Given a list of numbers, return True if the sum of the values in the list is less than 100; otherwise return False.

Examples
list_less_than_100([5, 57]) ➞ True

list_less_than_100([77, 30]) ➞ False

list_less_than_100([0]) ➞ True


Create a function that takes two strings as arguments and return either True or
 False depending on whether the total number of characters in the first string is equal to the total number of characters in the second string.

Examples
comp("AB", "CD") ➞ True

comp("ABC", "DE") ➞ False

comp("hello", "edabit") ➞ False

Notes
Don't forget to return the result.


Write a Python function that accepts a string and calculate the number of upper case letters and lower case letters. 
Sample String : 'The quick Brow Fox'
Expected Output :
No. of Upper case characters : 3
No. of Lower case Characters : 12

'''
string ="hello"
string.isupper()

def check(string):
    count = 0
    count1 = 0
    for i in string:
        if i.isupper():
            count += 1
        elif i.islower():
            count1 += 1
    print("Number of uppercase characters:", count)
    print("Number of lowercase characters:", count1)

# check('The quick Brow Fox')

'''
Write a Python function that takes a list and returns a new list with unique elements of the first list. Go to the editor
Sample List : [1,2,3,3,3,3,4,5]
Unique List : [1, 2, 3, 4, 5]

Write a Python program to print the even numbers from a given list. Go to the editor
Sample List : [1, 2, 3, 4, 5, 6, 7, 8, 9]
even : [2, 4, 6, 8]
odd = []


Write a Python function to create and print a 
list where the values are square of numbers between 1 and 30 (both included)

fruits = ["apple", "banana", "cherry", "kiwi", "mango"]
new_lst = []
'''
# def sq_list(num):
#     square_list = []
#     for i in range(1,num+1):
#         square_list.append(i**2)
#     return square_list

# print(sq_list(30))

fruits = ["apple","banana","cherry","kiwi","mango"]
# new_list = []
# for i in fruits :
#     if 'a' in i :
#         new_list.append(i)
# print(new_list)

new_lst = [i for i in fruits if "a" in i]
# print(new_lst)


#result = [expression for i in iterable if condition == True]

result = [i for i in range(10) ]
print(result)


def unique(list_elements):
    unique_set = set(list_elements)
    unique_elements = (list(unique_set))
    return("Unique List: ", unique_elements) 

print(unique([1,1,1,2,3,4,4,5,6,6]))
