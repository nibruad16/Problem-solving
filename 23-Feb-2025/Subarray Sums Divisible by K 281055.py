# Problem: Subarray Sums Divisible by K - https://leetcode.com/problems/subarray-sums-divisible-by-k/

class Solution:
    def subarraysDivByK(self, nums: List[int], k: int) -> int:

        count = 0
        prsum = 0
        reminder = 0
        dic = {0:1}
        for num in nums:
            prsum += num
            reminder = prsum % k
            if reminder in dic:
                count += dic[reminder]
                dic[reminder] += 1
            else:
                dic[reminder] = 1
        return count 


        