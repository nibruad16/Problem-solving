# Problem: Palindrome Linked List - https://leetcode.com/problems/palindrome-linked-list/

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
       
        if not head or not head.next:
            return True
        slow = head
        fast  = head

        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
    
        prev = None
        curr = slow

        while curr:
            temp = curr.next
            curr.next = prev
            prev = curr
            curr = temp
        
        firsthead = head
        sechead = prev

        while sechead:
            if firsthead.val != sechead.val:
                return False
            firsthead = firsthead.next
            sechead = sechead.next

        return True
        









        