from  Node import Node

class LinkedList:
    def __init__(self):
        self.head = None
        self.Length = 1

#list length

    def Length(self):
        current = self.head #star head
        count = 0
        while current is not None: # while is not None
            count = count + 1 #count add data one by one
            print(current.getdata())
            current = current.getnext() # get next node adress
        return count #if current is None return count

#Insert an item/add begin

    def Begin(self, data):
        new_node = Node() #allocate the new node
        new_node.setdata(data) #pass the data new_node
        if self.head is None:
            self.head = new_node
        else:

            new_node.setnext(self.head)  #pass the head to  new_node
            self.head.setprve(new_node)
            self.head = new_node

        self.Length  += 1

#nsert an item / add end

    def end(self,data):
        new_node=Node()
        new_node.setdata(data)
        if self .head is None: # check the head
            self.head=new_node
        else:
            present=self.head
            prve=None
            while present is not None:
                prve=present
                present=present.getnext()
            prve.setnext(new_node)  #check last node
            new_node.setprve(prve) # last node next add  to new _node
            new_node.setnext(None)  #new _node add to null

        self.Length+=1

#nsert an item/add position

    def position(self,pos,data):
        if pos >self.Length -1 or pos<0:
            return None
        elif pos==0:
            self.Begin(data)
        elif pos==self.Length -1:
            self.end(data)
        else:
            new_node=Node()
            new_node.setdata(data)
            count=0
            present=self.head
            while count !=pos - 1:
                count +=1
                present =present.getnext()
            x=present.getnext()

            new_node.setnext(present.getnext())
            present.setnext(new_node)
            new_node.setnext(x)
            new_node.setprve(present)
            x.setprve(new_node)

        self.Length +=1

#print fuction

    def List(self):
        if self.head is None:
            print("Empty Linked List")
        else:
            current = self.head
            while current is not None:
                print(current.getdata(),end="  ")
                current = current.getnext()
            print()

#Delete an item/begin

    def delfristnode(self):

        if self.head is None:#check the list empty
            print("empty list")
        else:
            self.head =self.head.getnext() #get next node
            self.head .setprve(None)
        self.Length -=1

#Delete an item/last

    def dellastnode(self):
        if self.head is None:  # check the head Node
            print("empty list")
        else:
            present = self.head
            prve = None
            while present.getnext() is not None:# check the getnext is not none
                prve = present
                present = present.getnext()
            prve.setnext(None)
            self.Length -= 1

#Delete an item/position

    def delPosition(self, Pos):
        if self.head is None:
            print("Empty Linked List")
            return None
        if self.Length > Pos or Pos >= 0:
            if Pos == 0:
                self.delfristnode()
            if Pos == self.Length - 1:
                self.dellastnode()
            else:
                count = 0
                current = self.head
                while count != Pos - 1:
                    count += 1
                    current = current.getnext()
                deletingNode = current.getnext()
                nextNode = deletingNode.getnext()
                current.setnext(nextNode)
                nextNode.setprve(current)

        self.Length -= 1

#Traversing/forward

    def forward(self):

        if self.head is None:
            print("list is empty")
        else:
            current = self.head
            #print()
            while current.getnext ():
                current = current.getnext()
            while current is not None:

                current = current.getprve()
                print()

#Traversing/backword

    def backward(self):

        if self.head is None:
            print("list is empty")
        else:
            current = self.head
            print()
            while current.getnext ():
                current = current.getnext()
            while current is not None:
                print(current.getdata(),end=" ")
                current = current.getprve()

#search position

    def searching_position(self, Pos):
        if self.head is None:
            print(" List is empty")
            return None

        elif self.Length > Pos or Pos >= 0:
            if Pos == 0:
                print(self.head.getdata())

            else:
                count = 0
                current = self.head
                while count != Pos - 1:
                    count += 1
                    current = current.getnext()
                current = current.getnext()
                print( current.getdata())


Doublylinklist=LinkedList()
Doublylinklist.Begin(100)
Doublylinklist.Begin(500)
Doublylinklist.List()

Doublylinklist.end(600)
Doublylinklist.List()

Doublylinklist.position(1,120)
Doublylinklist.position(0,220)
Doublylinklist.position(2,520)
Doublylinklist.List()

Doublylinklist.delfristnode()
Doublylinklist.List()

Doublylinklist.dellastnode()
Doublylinklist.List()

Doublylinklist.delPosition(2)
Doublylinklist.List()

Doublylinklist.forward()
Doublylinklist.List()

Doublylinklist.backward()
Doublylinklist.List()

Doublylinklist.searching_position(1)
Doublylinklist.List()
Doublylinklist.searching_position(0)
Doublylinklist.List()

























