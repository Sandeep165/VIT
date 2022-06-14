# Lambda functions
'''
lamda :-1
oops 1-2 lec
dsa stack queue linked list :- 3 lec
dbms :- 1lec
60hr :- 23rd May  :  16hrs left

'''
def show():
    print("Good morning")

# OOPs
class Employee:        #class declaration

    def __init__(self,name,age,salary):
        self.my_name = name
        self.age = age
        self.salary = salary

    # def __init__(self):
    #     print("Welcome to Employee class")
        
    def show(self):
        print(f"Name of the employee is {self.my_name} Age is {self.age}yrs old and having salary {self.salary}Rs")   #methods declaration

obj1 = Employee("harry",24,35000)   #employee.__init__()
obj1.show() 
print(obj1.age)
print(obj1.my_name)
print(obj1.salary)


'''
class XYZ:                class creation

    # def __init__(self,parameter1,parameter2...):    constructor
        pass

    # def show(self):       methods declaration
        pass
obj1 = XYZ(value1,value2....)
obj1.name
obj1.show()


'''


'''
class multiplication.........const:- num1,num2  .......add(+)......subs(-)....mul(*).....div(/)int value
3 obj
'''

class Multiplication:
    def __init__(number,num1,num2):
        number.num1=num1
        number.num2=num2

    def add(number):
        return number.num1+number.num2

    def subs(number):
        return number.num1-number.num2

    def mul(number):
        return number.num1*number.num2

    def div(number):
        return int(number.num1/number.num2)

obj=Multiplication(5,6)

print(obj.add())
print(obj.subs())
print(obj.mul())
print(obj.div())

class multiplication:
    def __init__(self,num1,num2):
        self.num1=num1
        self.num2=num2
    def add(self):
        print(self.num1+self.num2)
    def sub(self):
        print(self.num1-self.num2)
    def mul(self):
        print(self.num1*self.num2)
    def div(self):
        print(self.num1//self.num2)    
        
        
obj1=multiplication(5,2)
obj1.add()
obj1.sub()
obj1.mul()
obj1.div()



class multiplication:
    def __init__(self,num1,num2):
        self.num1=num1
        self.num2=num2

    def add(self):
        print("addition is ",self.num1 + self.num2)
    def sub(self):
        s=self.num1-self.num2
        print("subtraction is ",s)
    def mul(self):
        m=self.num1*self.num2
        print("multiplication is ",m)
    def div(self):
        d=self.num1//self.num2
        print("division is ",d)
# numb1 = multiplication(5,6)
# numb1.add()
# numb1.sub()
# numb1.mul()
# numb1.div()


'''
employee.....const--name,age,sal my_sal(salary)     increment() age>30 2500+sal incremented sal is xyzRs

increment()
age>30:
result = sal+2500
 else:
    original sal

'''

# class Employee:
#     def __init__(self,name,age,salary):
#         self.name=name
#         self.age=age
#         self.salary=salary
#     def my_salary(self):
#         print(f" My Original salary is {self.salary}")
#     def increment(self):
#         if self.age>30:
#             new_salary=self.salary+2500
#             print("My new salary is",new_salary)
#         else:
#             print("My salary is",self.salary)
# obj1=Employee("rahul",35,4500)
# obj1.increment()


class employee():
    def __init__(self,name,age,sal):
        self.name = name
        self.age = age
        self.sal = sal

    def my_salary(self):
         print("salary is ",self.sal)
    def increment(self):
        if self.age >30:
            print("incremented salary is ",self.sal+2500," Rs")
        else:
            print("salary is ",self.sal)

emp1 = employee('tom',34,5000)
emp1.my_salary()
emp1.increment()

'''

bus   :- milege, seating_cap, distance
154rs per person
fare():

profit or loss():
    distance <20 km   passenger >50
    bus route is in the profit state

'''
class Bus:
    def __init__(self,milage,seating_cap,distance):
        self.milage=milage
        self.seating_cap=seating_cap
        self.distance=distance
    
    def fare(self):
        print(f"Total fare recieved is {154*(self.seating_cap)}")

    def profit_or_loss(self):
        if(self.distance<20 & self.seating_cap>50):
            print("Bus route is in the profit state")
        else:
            print("Bus route is in loss state" )
obj1=Bus(45,50,70)
obj1.fare()
obj1.profit_or_loss()

'''

Create a class that takes the following four arguments for a particular football player:

name
age
height
weight
Also, create three functions for the class that returns the following strings:

get_age() returns "name is age age"
get_height() returns "name is heightcm"
get_weight() returns "name weighs weightkg"
Examples
 p1 = player("David Jones", 25, 175, 75)

 p1.get_age() ➞ "David Jones is age 25"
 p1.get_height() ➞ "David Jones is 175cm"
 p1.get_weight() ➞ "David Jones weighs 75kg"
Notes
name will be passed in as a string and age, height, weight will be integers.
'''
class player:
    country = "India"

    def __init__(self,name,age,height,weight):
        self.name=name
        self.age=age
        self.height=height
        self.weight=weight
    def get_age(self):
        print(self.name,f"is age",self.age)
        print(f"{self.name},is age,{self.age}")
        
    def get_height(self):
        print(self.name,f"is",self.height,"cm")
    
    def get_weight(self):
        print(self.name,f"is age",self.weight,"kg")
        
        
obj1=player("David",27,167,65)
obj1.get_age()
obj1.get_height()
obj1.get_weight()
'''
inheritance

print(f"anything i can print {name} my sal is {salary}")
'''