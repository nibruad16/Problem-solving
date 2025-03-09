# Problem: Add Two Numbers - https://leetcode.com/problems/add-two-numbers/

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        curr=l1
        num1=""
        dummy=ListNode()
        while curr:
            num1+=str(curr.val)
            curr=curr.next
        num2=""
        curr=l2
        while curr:
            num2+=str(curr.val)
            curr=curr.next
        a=num1[::-1]
        b=num2[::-1]
        ans= int(a)+int(b)
        res=dummy
        print(num1,num2,ans)
        for i in reversed(str(ans)):
            res.next=ListNode(int(i))
            res=res.next
        
        return dummy.next