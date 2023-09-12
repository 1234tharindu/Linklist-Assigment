# constructor
class Node:
    def __init__(self): #pass data
        self.data=None
        self.next=None
        self.prve=None

    #set data of the Node
    def setdata(self,data):
        self.data=data

    #get data of this node
    def getdata(self):
        return self.data

    #set previous data of the Node
    def setprve(self,prve_address):
        self.prve=prve_address

    #get previous data  of this node
    def getprve(self):
        return self.prve

    #get if it has a previous
    def hasprve(self):
        return self.prve is not None

    #set next of the node
    def setnext(self,next_address):
        self.next=next_address

    #get data of this node
    def getnext(self):
        return self.next

    #get if it has a next
    def hasnext(self):
        return self.next is not None







