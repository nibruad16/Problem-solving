class Solution:
    def smallerNumbersThanCurrent(self, nums: List[int]) -> List[int]:
        ans = []
        for i in range(len(nums)):
            temp = nums[i]
            co = 0
            for j in range(len(nums)):
                if nums[j] < temp:
                    co+=1
            ans.append(co)
        
        return ans
        
