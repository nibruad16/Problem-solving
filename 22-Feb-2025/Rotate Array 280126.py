# Problem: Rotate Array - https://leetcode.com/problems/rotate-array/

class Solution:
    def rotate(self, nums: list[int], k: int) -> None:
        """
        Rotates the array to the right by k steps in-place.
        """
        n = len(nums)
        k %= n 

      
        def reverse(nums, start, end):
            while start < end:
                nums[start], nums[end] = nums[end], nums[start]
                start += 1
                end -= 1

        reverse(nums, 0, n - 1)

  
        reverse(nums, 0, k - 1)

       
        reverse(nums, k, n - 1)