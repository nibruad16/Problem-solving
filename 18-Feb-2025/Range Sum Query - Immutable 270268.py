# Problem: Range Sum Query - Immutable - https://leetcode.com/problems/range-sum-query-immutable/

class NumArray:
    def __init__(self, nums: List[int]):
        self.presum = []
        if len(nums) > 0:
            self.presum.append(nums[0])

            for i in range(1,len(nums)):
                self.presum.append(self.presum[i-1] + nums[i])

    
    def sumRange(self, left: int, right: int) -> int:
        return self.presum[right] -  (self.presum[left-1] if left > 0 else 0 )
        


# Your NumArray object will be instantiated and called as such:
# obj = NumArray(nums)
# param_1 = obj.sumRange(left,right)