# Problem: Next Greater Element - https://leetcode.com/problems/next-greater-element-i/

class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        ans = []
        hashmap = {}
        stack = []

        for num in nums2[::-1]:
            while stack and num > stack[-1]:
                stack.pop()
            if stack:
                hashmap[num] = stack[-1]
            else:
                hashmap[num] = -1

            stack.append(num)
     

        for num in nums1:
            if num not in hashmap:
                ans.append(-1)
            else:
                ans.append(hashmap[num])





            
        return ans