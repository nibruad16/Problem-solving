# Problem: Maximum Twin Sum of a Linked List - https://leetcode.com/problems/maximum-twin-sum-of-a-linked-list/

class Solution:
    def pairSum(self, head: Optional[ListNode]) -> int:
        slow = fast = head
        prev = None

        while fast and fast.next:
            fast = fast.next.next
            temp = slow.next
            slow.next = prev
            prev = slow
            slow= temp
        max_sum = -1
        while slow:
            max_sum = max(max_sum , slow.val + prev.val)
            slow = slow.next
            prev = prev.next
        return max_sum