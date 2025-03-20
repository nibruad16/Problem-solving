# Problem: Subsets - https://leetcode.com/problems/subsets/

class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        res=[]
        cur=[]
        def backtrack(n):
            if n==len(nums):
                res.append(cur[:])
                return
            cur.append(nums[n])
            backtrack(n+1)
            cur.pop()
            backtrack(n+1)
        backtrack(0)
        return res

            




        