# Problem: Design Linked List - https://leetcode.com/problems/design-linked-list/

class Linkednode():
    def __init__(self, value=0 , next = None):
        self.val = value
        self.next = next

class MyLinkedList:
    def __init__(self):
        self.head = Linkednode()
        self.size = 0 # to keep track of the element in our linked list

    def get(self, index: int) -> int:

        if index < 0 or index >= self.size:
            return -1
        
        currunt = self.head.next # used to accses the starting point of our linked list also help us to handel edege case like empty list    
        for _ in range(index):
            currunt = currunt.next
        return currunt.val


    def addAtHead(self, val: int) -> None:
        self.addAtIndex(0,val)
        

    def addAtTail(self, val: int) -> None:
        self.addAtIndex(self.size,val)
        

    def addAtIndex(self, index: int, val: int) -> None:
        if index > self.size:
            return 
        prenode = self.head # it intialize an empty node
        for _ in range(index):
            prenode = prenode.next  # this code try to find the pointer of the next element or that index
        newnode = Linkednode(val,prenode.next) # creating new likned list node to be insertrd
        prenode.next = newnode # assing the value pointer of the new node to the perveose node
        self.size += 1

    def deleteAtIndex(self, index: int) -> None:

        if index < 0 or index >= self.size:
            return 

        prenode = self.head

        for _ in range(index):
            prenode = prenode.next

        todel = prenode.next
        prenode.next = todel.next
        todel.next =  None
        self.size -= 1

        

        


# Your MyLinkedList object will be instantiated and called as such:
# obj = MyLinkedList()
# param_1 = obj.get(index)
# obj.addAtHead(val)
# obj.addAtTail(val)
# obj.addAtIndex(index,val)
# obj.deleteAtIndex(index)