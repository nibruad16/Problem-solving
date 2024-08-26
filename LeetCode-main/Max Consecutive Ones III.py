class Solution:
    def longestOnes(self, nums: List[int], k: int) -> int:
        left = 0
        maxNum = 0 
        maxZeroCount = 0
        for right in range(len(nums)):
            if nums[right] == 0:
                maxZeroCount += 1

            while maxZeroCount > k:
                if nums[left] == 0:
                    maxZeroCount -= 1
                left += 1

            newNum = right - left +1

            maxNum = max(maxNum , newNum)

        return maxNum
