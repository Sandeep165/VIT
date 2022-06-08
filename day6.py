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

'''
list1=range(1,50)
result=[i for i in list1 if i%2==0]
print(result)

list2=range(1,50)
result2=[i for i in list2 if i%2!=0]
print(result2)





















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
