a_list = list(range(1, 11))
a_dictionary = {
1 : 'one',
2 : 'two',
3 : 'three',
4 : 'four',
5 : 'five',
6 : 'six',
7 : 'seven',
8 : 'eight',
9 : 'nine',
10 : 'ten'}
a_dictionary[2] 
result = [a_dictionary[i] for i in a_list if i%2==0]
result = [i*10 for i in a_list ]
print(result)

#result = [expression for i in iterable if condition == True]
'''
Q1:- use a list comprehension that iterates over a_list, prints a list composed of each value in a_list multiplied by 10.
The desired list must be like this:

[ 10, 20, 30, 40, 50, 60, 70, 80, 90, 100 ]

Q2:-  Use a list comprehension that iterates over a_list, prints a list composed of odd numbers from 1 to 9.

The desired list must be like this: [ 1, 3, 5, 7, 9 ]

Q3:- Using a list comprehension which iterates over a_list and whose output expression accesses a value from a dictionary,
 print a list composed of the text form of each even number from 2 to 10, e.g.,
[ 'two', 'four', 'six', 'eight', 'ten' ]

Q4:
original_list = [2,3.75,0.04,59.354,6,7.7777,8,9]
remove the float

Q5:
Find the common numbers in two lists (without using a tuple or set) list_a = [1, 2, 3, 4], list_b = [2, 3, 4, 5]

Q6:- Produce a list of tuples consisting of only the matching numbers in these lists list_a = [1, 2, 3,4,5,6,7,8,9],
 list_b = [2, 7, 1, 12].  Result would look like [(4,4), (12,12)]
'''
# list_a = [1, 2, 3, 4]
# list_b = [2, 3, 4, 5]
list_a = [1, 2, 3,4,5,6,7,8,9]
list_b = [2, 7, 1, 12]
op_lst = [(i,i) for i in list_a if i in list_b]
op_lst = [i for i in list_a if i in list_b]

# list_a = [1, 2, 3,4,5,6,7,8,9]

# list_b = [2, 7, 1, 12]


# list1=range(1,50)
# result=[i for i in list1 if i%2==0]
# print(result)

# list2=range(1,50)
# result2=[i for i in list2 if i%2!=0]
# print(result2)

# original_list = [2,6,8,9]
# int_list=[int(i) for i in original_list ]
# print(int_list)


# res_lst=[d for d in original_list if type(d) == int]
# print(res_lst)

# result = [expression for i in iterable if condition == True]

# even no lst   odd no lst
range(1,50)

lst = [1,5,7,9,2,36,5,4,12,51]
#op_lst of square of this list and print the no which is divisible by 5 only

list1=range(1,50)
result=[i for i in list1 if i%2==0]
print(result)

list2=range(1,50)
result2=[i for i in list2 if i%2!=0]
print(result2)


# Q1: Even no lst odd no lst range(1,50)

def evenodd(a,b):
    even = [ i for i in range(a,b) if i%2==0]
    odd = [i for i in range(a,b) if i%2 != 0]
    return even, odd

even, odd = evenodd(1,50)
print(f"Even {even}")
print(f"Odd {odd}")

# Q2: 

def op_lst(lst):
    op = [i**2 for i in lst if i%5==0]
    return op


'''
Write a function named odd_or_zero which takes one parameter, a number,
 and returns that number if it is odd or returns 0 if the number is even.
  Then using a list comprehension which iterates over a_list and calls your odd or zero function for each value, 
  print a list like the following:

[ 1, 0, 3, 0, 5, 0, 7, 0, 9, 0 ]
'''
a_list = list(range(1, 11))

result = [a_dictionary[i] for i in a_list if i%2==0]
print(result)


a_list = list(range(1, 11))

def odd_even(num):
        if num%2==0:
            return("0")
        else:
            return(num)

result = [odd_even(i) for i in a_list]
print(result)