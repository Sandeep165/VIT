################ LinkedList ######


'''
A linked list is a sequence of data elements, which are connected together via links.
Each data element contains a connection to another data element in form of a pointer. 


######## Understanding Linked Lists ########

Linked lists are an ordered collection of objects. So what makes them different from normal lists? 

Linked lists differ from lists in the way that they store elements in memory. 

While lists use a contiguous memory block to store references to their data,

linked lists store references as part of their own elements.


###########  Linkedlist structure :-

Each element of a linked list is called a node, and every node has two different fields:


Data contains the value to be stored in the node.
Next contains a reference to the next node on the list.


The first node is called the head, and its used as the starting point for any iteration through the list.

The last node must have its next reference pointing to None to determine the end of the list. also called as tail.

'''

### Basic Operations ######

'''
Insertion − Adds an element at the beginning of the list.

Deletion − Deletes an element at the beginning of the list.

Display − Displays the complete list.

Search − Searches an element using the given key.

'''

from hashlib import new
'''
head   _________
|     |         |
4 ->  6   7     9  
                  |
                tail

'''


'''
new_node = 6,tail=node  (mem loc :- 2)


self.head = new_node
'''
class Node:
    def __init__(self,data) -> None:
        self.data = data
        self.next = None 


class LinkedList:
    def __init__(self) -> None:
        self.head = None
        self.tail = None

    
    def insert(self,data):
        new_node = Node(data)
        if self.head == None:
            self.head = self.tail = new_node
            return "New node inserted in empty linked list is:",new_node.data
        else:
            self.tail.next = new_node
            self.tail = self.tail.next
            return "New node inserted in linked list is:",new_node.data

    def display(self):
        lt = []
        temp = self.head
        while temp:
            lt.append(str(temp.data))
            temp = temp.next
        return '->'.join(lt)

    def search(self,key):
        temp = self.head
        index = 0
        while temp:
            if temp.data == key:
                return temp.data,index
            index = index+1
            temp = temp.next
        return 'Value not found..'

    def find(self,key):
        temp = self.head
        while temp:
            if temp.data == key:
                return temp
            temp = temp.next
        return None

    def delete(self,val):
        node = self.find(val)
        if node is not None:
            if node == self.head:
                if self.head == self.tail:
                    self.tail = None
                self.head = node.next
            else:
                temp = self.head
                while temp:
                    if temp.next == node:
                        temp.next = node.next
                        if node == self.tail:
                            self.tail = temp
                        node.next = None
                        break
                    temp = temp.next
            return f'Element {val} has been deleted successfully...'
        else:
            return 'value to be deleted is not present in LL..'
        

                    






        


ll = LinkedList()

print(ll.insert(6))

print(ll.insert(9))

ll.insert(19)

print('head:-',ll.head.data,'tail:-',ll.tail.data)

print('Linkedlist:-', ll.display())

# print(ll.search(90))

print(ll.delete(19))

print(ll.delete(6))

print('Linkedlist:-', ll.display())
print('head:-',ll.head.data,'tail:-',ll.tail.data)