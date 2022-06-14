# inheritace,stack,queu,dbms

# single 



class Parent:
    def show(self):
        print("I am from class Parent")

    def display(self):
        print("i am using nokia")

class Child(Parent):
    def show(self):
        print("I am from class Child")

    def display(self):
        print("i am using nokia")


obj_p = Parent()
obj_c = Child()


#multilevel,Hybrid
class GrandParent:

    def show(self):
        print("I am from class GrandParent")

    def display(self):
        print("i am using nokia")
    
    def gp(self):
        print("I am from GP method")

class Parent(GrandParent):
    def show(self):
        print("I am from class Parent")

    def display(self):
        print("i am using onePlus")

class Child(Parent):

    def show(self):
        print("I am from class Child")

    def display(self):
        print("i am using Iphone")


p = Parent()
c = Child()

# Multiple
class A:
    def show(self):
        print(" I am from class A")

    def display(self):
        print("i am using Oneplus")

class B:
    def show(self):
        print(" I am from class B")

    def display(self):
        print("i am using Iphone")

class C(B,A):
    def show(self):
        print(" I am from class C")

c = C()


#Hierarchical 

class Parent:
    def info(self):
        print("I am from class Parent")
    def display(self):
        print("i am using Iphone")

class Child1(Parent):
    def info(self):
        print("I am from class Child1")

class Child2(Parent):
    def info(self):
        print("I am from class Child2")


ch1 = Child1()
ch2 = Child2()
ch1.display()
ch2.display()


#Hybrid -Mixture of all inheritance

#single and multilevel

'''
Create a child class Bus that will inherit all of the variables and methods of the Vehicle class
Create a Bus object that will inherit all of the variables and methods of the parent Vehicle class and display it.

Expected Output:

Vehicle Name: School Volvo Speed: 180 Mileage: 12
'''

class Vehicle:
    def __init__(self, name, max_speed, mileage):
        self.name = name
        self.max_speed = max_speed
        self.mileage = mileage

class Bus(Vehicle):
    def display(self):
        print(f"Vehicle Name: {self.name} speed: {self.max_speed} Mileage: {self.mileage}")

bus = Bus('School Volvo',180,12)
bus.display()

# class player:
#     def info(self):
#         print("this player belongs to india ")
#     def sports(self):
#         print("he plays table tennis")
            
# class player1(player):
#     def info(self):
#         print("this player belongs to south africa")
    
# P2= player1()
# P1= player()

# P1.sports()
# P2.info()


# class player1:
#     def info(self):
#         print("this player belongs to india ")
#     def sports(self):
#         print("he plays table tennis")
#     def room(self):
#         print("player1 is in room:-306")    
            
# class player2(player1):
#     def info(self):
#         print("this player belongs to south africa")
#     def room(self):
#         print (" player2 is in room no:-304 ")    

# class stay(player2):
#     def info(self):
#         print("they are staying in taj hotel")
      
    
# P2= player2()
# P1= player1()
# P3=stay()

# P1.sports()
# P2.info()
# P3.info()
# P3.room()

'''

Create a Bus class that inherits from the Vehicle class. 
Give the capacity argument of Bus.seating_capacity() a default value of 50.

Use the following code for your parent Vehicle class.



The seating capacity of a bus is 50 passengers
'''
# class Vehicle:
#     def __init__(self, name, max_speed, mileage):
#         self.name = name
#         self.max_speed = max_speed
#         self.mileage = mileage

#     def seating_capacity(self, capacity):
#         return f"The seating capacity of a {self.name} is {capacity} passengers"

class Mamal:
    def __init__(self,name):
        print(f"{name} :- is a warm blooded animal")

class Dog(Mamal):
    def __init__(self):
        print("I am from Dog category")
        super().__init__("Cat")


dog1 = Dog()    #dog1.__init__()


class Node:
     def __init__(self,data)-> None:
        self.data= data 
        self.next= None 

class Linkedlist:
    def __init__(self) -> None:
        self.head= None
        self.tail= None 

    def insert(self,data) :
        new_node= Node(data)
        if self.head == None:
            self.head=self.tail=new_node
            return "The node is inserted in the empty linkedlist:-",new_node.data

        else:
            self.tail.next= new_node
            self.tail=self.tail.next 
            return "New node inserted in linked list is :",new_node.data  

l1 = Linkedlist()
print(l1.insert(6))
print(l1.insert(20))

#oops linkedlist
