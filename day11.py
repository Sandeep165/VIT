'''
3 lecs :-

stack
queue
dbms
list comp, func, oops :- 


10  2lec
9-11    for
3-5     while

9-1    while 

10 days

9-11



2-4


trees



drive :- dp + trees + regular exp
'''

class Stack:
    def __init__(self,max_size):
        self.__max_size=max_size
        self.__elements=[None]*self.__max_size
        self.__top=-1

    def get_max_size(self):
        return self.__max_size

    def is_full(self):
        if self.__top == self.__max_size-1:
            return True
        return False
        
        #Remove pass and write the logic to check whether stack is full. If the stack is full, return true else return false.

    def push(self,data):
        if (self.is_full()):
            print("Stack is full !")
        else:
            self.__top += 1
            self.__elements[self.__top] = data

        #Remove pass and write the logic to push element into the stack. Element should be pushed only if the stack is not full. Otherwise, display appropriate message

    def is_empty(self):
        if self.__top == -1:
            return True
        return False
         
    def pop(self):
        if (self.is_empty()):
            print("Stack is empty")
        else:
            data = self.__elements[self.__top]
            self.__top -= 1
            return data




'''
is_full():
    if self._top == max_size-1:
        print("Stack is full)
    else:
        print("You can push the data")

push():
 if is_full() == False 
    top += 1   # top = top+1
 else: "stack is full"
'''


'''
if (condition):
    print()
else:

'''