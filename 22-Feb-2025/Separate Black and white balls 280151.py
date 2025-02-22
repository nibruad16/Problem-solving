# Problem: Separate Black and white balls - https://leetcode.com/problems/separate-black-and-white-balls/

class Solution:
    def minimumSteps(self, s: str) -> int:
        nums = [int(i) for i in s]
        left = 0
        right =  1
        count = 0

        while right < len(nums):
            if nums[left] == 1 and nums[right] == 0:
                nums[left] , nums[right] = nums[right] , nums[left]
                count += right - left
                left += 1
            if nums[left] == 0:
                left += 1
            right += 1

        print(nums)
        return count


     
