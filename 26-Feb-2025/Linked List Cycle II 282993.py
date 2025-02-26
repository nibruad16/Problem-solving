# Problem: Linked List Cycle II - https://leetcode.com/problems/linked-list-cycle-ii/

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def detectCycle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        slow, fast = head, head
        while fast and fast.next:
            slow = slow.next  
            fast = fast.next.next 

            if slow == fast:  
                entry = head

                
                while entry != slow:
                    entry = entry.next
                    slow = slow.next

                return entry 
        return None  

