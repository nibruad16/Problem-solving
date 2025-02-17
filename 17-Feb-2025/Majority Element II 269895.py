# Problem: Majority Element II - https://leetcode.com/problems/majority-element-ii/?envType=daily-question&envId=2023-10-05

class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        new = len(nums) // 3
        count = Counter(nums)
        return [key for key , val in count.items() if val > new]
        