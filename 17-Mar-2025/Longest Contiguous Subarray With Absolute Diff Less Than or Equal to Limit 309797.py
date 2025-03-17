# Problem: Longest Contiguous Subarray With Absolute Diff Less Than or Equal to Limit - https://leetcode.com/problems/longest-continuous-subarray-with-absolute-diff-less-than-or-equal-to-limit/

class Solution:
    def longestSubarray(self, nums: List[int], limit: int) -> int:
        n = len(nums)
        min_queue = deque()
        max_queue = deque()
        length = 0
        left_index = 0
        
        # we will be going through the numbers:
        for i in range(n):
            # maintain the queue
            # mono-increasing
            while min_queue and nums[i] < nums[min_queue[-1]]:
                min_queue.pop()
            min_queue.append(i)

            # mono-decreasing
            while max_queue and nums[i] > nums[max_queue[-1]]:
                max_queue.pop()
            max_queue.append(i)

            while nums[max_queue[0]] - nums[min_queue[0]] > limit:
                left_index += 1 
                if min_queue[0] < left_index:
                    min_queue.popleft()
                if max_queue[0] < left_index:
                    max_queue.popleft()
                
            length = max(length, i - left_index + 1)


        return length