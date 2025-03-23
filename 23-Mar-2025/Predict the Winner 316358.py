# Problem: Predict the Winner - https://leetcode.com/problems/predict-the-winner/

class Solution:
    memo = {}
    def totalScore(self,nums, left, right):

        if left > right:
            return 0

        if (left, right) in self.memo:
            return self.memo[(left, right)]

        score_left = nums[left] - self.totalScore(nums, left+1, right)
        score_right = nums[right] - self.totalScore(nums, left, right-1)

        self.memo[(left, right)] = max(score_left, score_right)
        return max(score_left, score_right)

    def predictTheWinner(self, nums: List[int]) -> bool:
        self.memo = {}
        return self.totalScore(nums, 0, len(nums)-1) >= 0