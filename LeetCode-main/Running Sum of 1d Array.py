class Solution:
    def runningSum(self, nums: List[int]) -> List[int]:
        newArray = []
        newArray.append(nums[0])
        for i in range(1,len(nums)):
            newArray.append(nums[i] + newArray[i-1])
        return newArray
