# Problem: Two Sum II - Input Array Is Sorted - https://leetcode.com/problems/two-sum-ii-input-array-is-sorted/

class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:


        # # hashmap Optimal Approch 
        # hashmap = {}
        # ans = []
        # for i in range(len(numbers)):
        #     temp = target - numbers[i]
        #     if numbers[i] in hashmap:
        #         ans.append(hashmap[numbers[i]] + 1)
        #         ans.append(i+1)
    
        #     hashmap[temp] = i
        # return ans 

        # two Pointer Approch 
        
        left = 0
        right = len(numbers) - 1
        ans = []
        while left < right:
            if numbers[left] + numbers[right] > target:
                right -= 1
            elif numbers[left] + numbers[right] < target:
                left += 1
            else:
                ans.append(left+1)
                ans.append(right+1)
                break

        return ans


        