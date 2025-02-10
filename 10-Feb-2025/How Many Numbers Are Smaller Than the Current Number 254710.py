# Problem: How Many Numbers Are Smaller Than the Current Number - https://leetcode.com/problems/how-many-numbers-are-smaller-than-the-current-number/

class Solution:
    def smallerNumbersThanCurrent(self, nums: List[int]) -> List[int]:
        new = sorted(nums)
        hashmap = {}

        for index,value in enumerate(new):
            if value not in hashmap:
                hashmap[value] = index
        ans = []
        for num in nums:
            ans.append(hashmap[num])

        return ans



        # ans = []
       
        # print(nums)
        # for i in range(len(nums)):
        #     count = 0
        #     for j in range(len(nums)):
        #         if nums[i] > nums[j]:
        #             count += 1
        #     print(count)
        #     ans.append(count)

        # return ans
        