# Problem: Find All Duplicates in an Array - https://leetcode.com/problems/find-all-duplicates-in-an-array/description/

class Solution:
    def findDuplicates(self, nums: List[int]) -> List[int]:

        # # hashmap = defaultdict(int)
        # ans = []

        # for i in range(len(nums)):
        #     if nums[i] in hashmap:
        #         ans.append(nums[i])
        #     else:
        #         hashmap[nums[i]] += 1
        # return [] if len(ans) < 1 else ans
        


        new = Counter(nums)
        ans = []

        for key , val in new.items():
            if val == 2:
                ans.append(key)
            
        return [] if len(ans) < 1 else ans 
        