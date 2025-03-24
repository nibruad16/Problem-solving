# Problem: Find First and Last Position of Element in Sorted Array - https://leetcode.com/problems/find-first-and-last-position-of-element-in-sorted-array/


class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        def lowerBound(num,t):
            left = 0
            right = len(num) - 1
            mid = (right + left) // 2

            while left <= right:
                mid = (right + left) // 2
                if num[mid] < t:
                    left = mid+1
                else:
                    right = mid -1
            return left 
        def upperBound(num,t):
            left = 0
            right = len(num) - 1
            mid = (right + left) // 2

            while left <= right:
                mid = (right + left) // 2
                if num[mid] > t:
                    right = mid -1
                else:
                    left = mid+1
            return right

        first = lowerBound(nums,target) 
        last = upperBound(nums,target)

        print(first,last)
        if first <= last and first < len(nums) and nums[first] == target:
            return [first, last]
        else:
            return [-1, -1]




        
        
        

     

