# Problem: Remove Linked List Elements - https://leetcode.com/problems/remove-linked-list-elements/

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def removeElements(self, head: Optional[ListNode], val: int) -> Optional[ListNode]:
        dummy = ListNode(0, head)
        prev = dummy

        while prev.next:
            if prev.next.val == val:
                prev.next = prev.next.next
            else:
                prev = prev.next
        return dummy.next
        