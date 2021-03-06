#########################################################
#                                                       #
#     Assignment 3: Ordered Collection Data Types       #
#     CS 301      Due March 6th, 2020                   #
#     Contributors:                                     #
#        Yusuf Kortobi                                  #
#        David Thompson                                 #
#        Asepha Shaffer                                 #
#                                                       #
#########################################################

###########################################
#                                         #
#     Singly Linked List                  #
#                                         #
###########################################
class Node:
    def __init__(self, data=None):
        self.data = data
        self.next = None

    def __str__(self):
        return self.data
class SLinkedList:
    def __init__(self):
        self.head = None

    def add(self, data_in):
        NewNode = Node(data_in)
        NewNode.next = self.head
        self.head = NewNode


    def RemoveNode(self, Removekey):
        HeadVal = self.head
        if (HeadVal is not None):
            if (HeadVal.data == Removekey):
                self.head = HeadVal.next
                HeadVal = None
                return
        while (HeadVal is not None):
            if HeadVal.data == Removekey:
                break
            prev = HeadVal
            HeadVal = HeadVal.next
        if (HeadVal == None):
            return
        prev.next = HeadVal.next
        HeadVal = None

    def search(self, searchKey): 

        current = self.head 
        # loop till current not equal to None 
        while current != None: 
            if current.data == searchKey: 
                return True # data found
            current = current.next
        return False

    def isEmpty(self):
        if(self.head is None):
            return(True)
        return(False)

    def size(self):
        counter = 0
        current=self.head
        while(current !=None):
            counter+=1
            current=current.next
        return(counter)

    def append(self, newdata):
        NewNode = Node(newdata)
        if self.head is None:
            self.head=NewNode
            return
        last = self.head
        while(last.next):
            last = last.next
        last.next=NewNode

    def index(self, searchKey):
        current = self.head
        counter = 0
        # loop till current not equal to None 
        while current != None:
            if current.data == searchKey: 
                return counter # data found
            counter += 1
            current = current.next
        return -1

    def insert(self, pos, newdata):
        if pos is None:
            print("no node with position: ", pos)
            return
        NewNode = Node(newdata)
        NewNode.next = pos.next
        pos.next = NewNode

    def Listprint(self):
        printval = self.head
        while (printval):
            print(printval.data),
            printval = printval.next

    def pop(self, pos = -1):
        if pos == -1:
            last = self.head
            while(last.next):
                last = last.next
            temp = last.data
            self.RemoveNode(last.data)
            return temp
        else:
            last = self.head
            for i in range(pos):
                last = last.next
            temp = last.data
            self.RemoveNode(last.data)
            return temp

    #Tests the above functions
llist = SLinkedList()

e1 = Node("Mon")
e2 = Node("Tue")
e3 = Node("Wed") 
e4 = Node("Thur")
e5 = Node("Fri")

llist.add(e1)
llist.append(e2)
llist.append(e3)
llist.append(e4)
llist.append(e5)
llist.Listprint()

print(llist.pop(1))
#llist.insert(llist.head.next.next, e4)

llist.Listprint()


###########################################
#                                         #
#     Doubly Linked List                  #
#                                         #
###########################################
class Node:
    def __init__(self, data=None):
        self.data = data
        self.next = None
        self.last = None

    def __str__(self):
        return self.data

class DLinkedList:
    def __init__(self):
        self.head = None

    def add(self, newdata):
        new_node = Node(newdata) 
        new_node.next = self.head 
        if self.head is not None: 
            self.head.prev = new_node 
        self.head = new_node

    def deleteNode(self, dele):  
        if self.head is None or dele is None: 
           return  
        if self.head == dele: 
            self.head = dele.next
        if dele.next is not None: 
            dele.next.last = dele.last
        if dele.last is not None: 
            dele.last.next = dele.next

    def search(self, searchKey): 
        current = self.head 
        # loop till current not equal to None 
        while current != None: 
            if current.data == searchKey: 
                return True # data found
            current = current.next
        return False

    def isEmpty(self):
        if(self.head is None):
            return(True)
        return(False)

    def size(self):
        counter = 0
        current=self.head
        while(current !=None):
            counter+=1
            current=current.next
        return(counter)

    def append(self, new_data): 
        new_node = Node(data = new_data) 
        last = self.head 
        new_node.next = None
        if self.head is None: 
            new_node.prev = None
            self.head = new_node 
            return 
        while (last.next is not None): 
            last = last.next 
        last.next = new_node 
        new_node.prev = last

    def index(self, searchKey):
        current = self.head
        counter = 0
        # loop till current not equal to None 
        while current != None:
            if current.data == searchKey: 
                return counter # data found
            counter += 1
            current = current.next
        return -1

    def insert(self, prev_node, new_data): 
        if prev_node is None: 
            print("This node doesn't exist in DLL") 
            return
        new_node = Node(new_data)
        new_node.next = prev_node.next
        prev_node.next = new_node 
        new_node.prev = prev_node 
        if new_node.next is not None: 
            new_node.next.prev = new_node


    def Listprint(self):
        printval = self.head
        while (printval):
            print(printval.data),
            printval = printval.next
            if(printval==self.head.data):  #because in doubly linked lists
                break                           #this would usually loop forever

    def pop(self, pos =-1):
        if pos == -1:
            last = self.head
            while(last.next):
                last = last.next
            temp = last.data
            self.deleteNode(last)
            return temp
        else:
            last = self.head
            for i in range(pos):
                last = last.next
            temp = last.data
            self.deleteNode(last)
            return temp

""" Testing the functions above
llist = DLinkedList()

e1 = Node("mon")
e2 = Node("tues")
e3 = Node("wed") 
e4 = Node("thur")
e5 = Node("fri")
e6 = Node("bad day")

llist.add(e2)
llist.add(e1)
llist.append(e4)
llist.insert(llist.head.next,e3)
llist.add(e5)

llist.insert(llist.head.next.next,e6)
llist.Listprint() 
#print(llist.pop(e6), " should be deleted")

llist.add(e1)
llist.add(e2)
llist.add(e3)
llist.add(e4)
llist.add(e5)
llist.add(e6)

llist.Listprint()
print("__________")
print(llist.pop(3))
llist.pop()
llist.Listprint() 
"""
###########################################
#                                         #
#     Question #3                         #
#                                         #
###########################################
"""
I don’t think that python’s internal list systems are a linked list of any sort.
If the implemented list methods were made for linked lists sort functions or
index function would take longer than they actually do in python, as we see by
the methods in the code above.  There are advantages to using linked lists, like
wanting to go through each element of a linked list or wanting to loop back
through them. However there are also negatives that come with database work,
or when the list gets too long.  

"""


###########################################
#                                         #
#     Stack                               #
#                                         #
###########################################
class Stack:

    def __init__(self):
        self.top=None
        self.stack= []


    def push(self, data):              #O(1)
            self.stack.append(data)
            self.top = data

    def pop(self):                     #O(n)
        temp1 = self.stack.pop()
        temp = ""
        for i in self.stack:
            if(i == temp1):
                break
            temp = i
        self.top = temp
        return(temp1)

    def peek(self):                    #O(1)
        return(self.top)

    def isEmpty(self):                 #O(1)
        if(self.top is None):
            return True
        else:
            return False

    def size(self):                    #O(n)
        counter = 0
        for i in self.stack:
            counter = counter + 1
        return(counter)

""" Tests the above functions
newStack = Stack()
print(newStack.isEmpty())
newStack.push('a')
newStack.push('b')
newStack.push('c')
newStack.push('d')
print(newStack.peek())
newStack.pop()
print(newStack.stack)
print(newStack.isEmpty())
print(newStack.size())"""


###########################################
#                                         #
#     Queue                               #
#                                         #
###########################################
class Queue:
    def __init__(self):
        self.back = None
        self.queue = []


    def enqueue(self,data):                 #O(1)
        self.queue.append(data)
        if self.back is None:
            self.back = data

    def dequeue(self):                      #O(n)
        pop = self.queue[0]
        temp = []
        var = 1
        while (var<=len(self.queue)-1):
            temp.append(self.queue[var])
            var = var +1
        self.queue = temp
        self.back = self.queue[0]
        return pop

    def isEmpty(self):                      #O(1)
        if self.back is None:
            return True
        else:
            return False

    def size(self):                         #O(n)
        counter = 0
        for i in self.queue:
            counter = counter + 1
        return counter

""" Tests the above functions
myQueue = Queue()
print(myQueue.isEmpty())
myQueue.enqueue('a')
myQueue.enqueue('b')
myQueue.enqueue('c')
myQueue.enqueue('d')
print(myQueue.isEmpty())
print(myQueue.dequeue())
print(myQueue.queue)
print(myQueue.size())"""


###########################################
#                                         #
#     Deque                               #
#                                         #
###########################################
class Deque:
    def __init__(self):
        self.top = None
        self.front = None
        self.stack = []

    def addFront(self,data):                 #O(n)
        temp = []
        temp.append(data)
        for i in self.stack:
            temp.append(i)
        self.stack = temp
        self.front = data


    def addRear(self, data):                 #O(1)
            self.stack.append(data)
            self.top = data

    def removeFront(self):                   #O(n)
        pop = self.stack[0]
        temp = []
        var = 1
        while (var<=len(self.stack)-1):
            temp.append(self.stack[var])
            var = var +1
        self.stack = temp
        self.back = self.stack[0]
        return pop

    def removeRear(self):                    #O(n)
        temp1 = self.stack.pop()
        temp = ""
        for i in self.stack:
            if(i == temp1):
                break
            temp = i
        self.top = temp
        return(temp1)

    def isEmpty(self):                       #O(1)
        if self.front is None and self.top is None:
            return True
        else:
            return False

    def size(self):                         #O(n)
        counter = 0
        for i in self.stack:
            counter = counter + 1
        return counter

"""  Tests the above functions
deque = Deque()
print(deque.isEmpty())
deque.addFront('c')
deque.addRear('d')
deque.addFront('b')
deque.addFront('a')
print(deque.size())
print(deque.removeFront())
print(deque.removeRear())
print(deque.isEmpty())
print(deque.stack)"""