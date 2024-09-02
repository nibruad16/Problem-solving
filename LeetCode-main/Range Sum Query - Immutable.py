class NumArray:

    def __init__(self, nums: List[int]):
        self.prefixSum = []
        current = 0
        for i in nums:
            current += i
            self.prefixSum.append(current)
        

    def sumRange(self, left: int, right: int) -> int:
        rightSum = self.prefixSum[right]
        leftSum = self.prefixSum[left - 1] if left > 0 else 0
        return rightSum - leftSum
