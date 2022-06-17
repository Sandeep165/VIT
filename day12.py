'''
Javascript:-  

Queue:

Initialization in stack :- Top = -1
 
Initialization in Queue :- Front = 0, Rear = -1



Front  = 0  Bcz it is responsible to remove the first value
first value will always there on index = 0
Front = 0

!(Front = -1)
Bcz first value will be at 0th index
From that onl;y we are taking the data out
so -1 will not satisfy the condition


Rear = -1
Bcz data will always be added in a queue from rear end only
so first index need to be zero so after first incrementaion my rear has to be pointing to index 0
i.e Rear = -1

!(Rear = 0)
becasuse after pushing the 1st data the pointer will be at1 but it should be at 0th position



is_full():
Rear = max-1
print(Queue is full)

is_empty():
rear = -1 front = 0
rear<front
print(Queue is empty)


enqueue (data):
1. Check whether queue is full. If full, display appropriate message
2. If not,
   a. increment rear by one
   b. Add the element at rear position in the elements array

if is_full():False


dequeue()
1. Check whether the queue is empty. If it is empty, display appropriate message
2. If not,
   a. Retrieve data at the front of the queue
   b. Increment front by 1
   c. Return the retrieved data

if is_empty():  false

if condition:
    priny()
else:
    exe
'''



class Queue:
    def __init__(self,max_size):
        self.__max_size=max_size
        self.__elements=[None]*self.__max_size
        self.__rear=-1
        self.__front=0
        
    def get_max_size(self):
        return self.__max_size
    
    def is_full(self):
        if(self.__rear == self.__max_size-1):
            return True
        return False
        #Remove pass and write the logic to check whether Queue is full. If the queue is full, return true else return false.
    
    def enqueue(self,data):
            if(self.is_full()):
                print("Queue is full!!!")
            else:
                self.__rear+=1
                self.__elements[self.__rear]=data

    def dequeue(self):
            if(self.is_empty()):
                print("Queue is empty!!!")
            else:
                data=self.__elements[self.__front]
                self.__front+=1
                return data


    def is_empty(self):
        if(self.__rear<self.__front):
            return True
        return False
        

    def display(self):
        for i in range(self.__front,self.__rear+1):
            print(self.__elements[i])


        #Remove pass and write the logic to display all the queue element(s).



