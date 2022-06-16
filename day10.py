'''

Name
List of foods they like
List of foods they hate
In this class, create the method taste(slef,food):

It will take in a food name as a string.
Return {person_name} eats the {food_name}.
If the food is in the person's like list, add 'and loves it!' to the end.
If it is in the person's hate list, add 'and hates it!' to the end.
If it is in neither list, simply add an exclamation mark to the end.
Examples
p1 = Person("Sam", ["ice cream"], ["carrots"])
p1.taste("ice cream") ➞ "Sam eats the ice cream and loves it!"

p1.taste("cheese") ➞ "Sam eats the cheese!"

p1.taste("carrots") ➞ "Sam eats the carrots and hates it!"

'''
class Person:
    def __init__(self,name,like_lst,hate_lst):
        self.name = name
        self.like_lst = like_lst
        self.hate_lst = hate_lst

    def taste(self,food):
        if food in self.like_lst:
            print(f"{self.name} eats the {food} and loves it!")
        elif food in self.hate_lst:
            print(f"{self.name} eats the {food} and hates it!")
        else:
            print(f"{self.name} eats the {food}!")
        
p1 = Person("Sam", ["ice cream"], ["carrots"])
p1.taste("ice cream")
p1.taste("cheese")
p1.taste("carrots")


'''
stack :- LIFO  last in first out
queue :-  FIFO first in first out


stack max_size = 4   0 1 2 3 

top == -1    stack empty ?Yes    pop underflow
top == max_size   stack full? Yes   push  overflow


lst = 10
len -1 
0 1 


Algorithm :- 

Push:-
step1 :- is_full() ---> stack is full or not     
         is_full()  -> True/False    = False push operation    :True -> error - overflow
step2 :-  increment your top pointer by 1    top += 1


Pop:-
Step1 :- is_empty() ---> stack is empty or not  
         is_empty()  -->True/False    =  False pop operation    :True -> error - underflow
step2 :-   decrement your top pointer by 1      top -= 1


top
max_size

is_full():
    if self._top == max_size-1:
        print("Stack is full)
    else:
        print("You can push the data")

push():
 if is_full() == False 
    top += 1   # top = top+1
 else: "stack is full"

is_empty():
  if self.top == -1:
    print("stack is empty")
  else:
    print("you can pop the data")

pop():
    if is_empty() == False
       top -= 1 # top = top -1 
    else: 
        print("stack is empty")


Application(where we are excecuting those ds) and examples (real life)

1) stack basic imp :-  infix  (A+B)     (6+(3*5))   = 21
2) queue           :- Deadlock 



Create a Book class that has two attributes:

.title =
.author
and two methods:

A method named .get_title() that returns: "Title:  " + the instance title.
A method named .get_author() that returns: "Author: " + the instance author.
and instantiate this class by creating 3 new books:

Pride and Prejudice - Jane Austen (PP)
Hamlet - William Shakespeare (H)
War and Peace - Leo Tolstoy (WP)
The name of the new instances should be PP, H, and WP, respectively.

For instance, if I instantiated the following book using this Book class:

Harry Potter - J.K. Rowling (HP)
I would get the following attributes and methods:

Examples
HP.title ➞ "Harry Potter"
HP.author ➞ "J.K. Rowling"
HP.get_title() ➞ "Title: Harry Potter"
HP.get_author() ➞ "Author: J.K. Rowling"

'''
class Book:
    def __init__(self,title,author):
        self.title =title
        self.author = author
    def get_title(self):
        print(f"Title : {self.title}")
    def get_author(self):
        print(f"Author : {self.author}")  
          
pp = Book('Pride and Prejudice','Jane Austen')
H=Book("Hamlet","William Shakespeare")
wp = Book("War and Peace","Leo Tolstoy")
pp.get_title()
pp.get_author()
H.get_title()
H.get_author()
wp.get_title()
wp.get_author()

