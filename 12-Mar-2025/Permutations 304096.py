# Problem: Permutations - https://leetcode.com/problems/permutations/

class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        ans = []
        used = [False] * len(nums)

        def backtrack(temp):
            if len(temp) == len(nums):
                ans.append(temp.copy())
                return 
            
            for i in range(len(nums)):
                if not used[i]:
                    used[i] = True
                    temp.append(nums[i])
                    backtrack(temp)
                    temp.pop()
                    used[i] = False
        backtrack([])
        return (ans)

        