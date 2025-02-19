# Problem: Middle of the Linked List - https://leetcode.com/problems/middle-of-the-linked-list/

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class ListNode:
    def __init__(self,val=0,next=None):
        self.val = val
        self.next = next

class Solution:
    def middleNode(self, head: Optional[ListNode]) -> Optional[ListNode]:

        if not head:
            return 
            
        curr = head
        size = 0

        while curr:
            curr = curr.next
            size += 1

        mid = size // 2
        curr = head
        
        for _ in range(mid):
            curr = curr.next
        return curr
    



        


        
        