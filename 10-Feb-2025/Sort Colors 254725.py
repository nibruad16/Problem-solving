# Problem: Sort Colors - https://leetcode.com/problems/sort-colors/

class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        return nums.sort()

        # bubbel Sort 
        # for i in range(len(nums)):
        #     for j in range(i+1 ,len(nums)):
        #         if nums[i] > nums[j]:
        #             print(nums)
        #             nums[i] , nums[j] = nums[j] , nums[i]
        #             print(nums)



        # selection Sort 
        # for i in range(len(nums)):
        #     mini = i
        #     for j in range(i+1,len(nums)):
        #         if nums[mini] > nums[j]:
        #             mini = j
        #     nums[i] , nums[mini] = nums[mini] , nums[i]



        # insertion Sort 
        # for i in range(1,len(nums)):
        #     key = nums[i]
        #     j = i - 1

        #     while j>= 0 and key < nums[j]:
        #         nums[j + 1] = nums[j]
        #         j -= 1
        #     nums[j + 1] = key 
        # return nums
        