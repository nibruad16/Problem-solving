class Solution:
    def applyOperations(self, nums: List[int]) -> List[int]:
        for i in range(len(nums) - 1):
                if nums[i] == nums[i + 1]:
                    c = nums[i] * 2
                    nums[i] = c
                    nums[i+1] = 0
        for i in range(len(nums)-1):
            b = nums[i]
            if b == 0:
                nums.remove(b)
                nums.append(0)
        return nums
