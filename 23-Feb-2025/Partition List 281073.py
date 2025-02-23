# Problem: Partition List - https://leetcode.com/problems/partition-list/

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def partition(self, head: ListNode, x: int) -> ListNode:
        if not head:
            return None

        less_head = ListNode(0)
        less_tail = less_head
        greater_head = ListNode(0)
        greater_tail = greater_head

        current = head

        while current:
            if current.val < x:
                less_tail.next = current
                less_tail = less_tail.next
            else:
                greater_tail.next = current
                greater_tail = greater_tail.next
            current = current.next

        greater_tail.next = None  
        less_tail.next = greater_head.next

        return less_head.next