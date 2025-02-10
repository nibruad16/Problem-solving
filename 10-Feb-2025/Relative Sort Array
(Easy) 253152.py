# Problem: Relative Sort Array
(Easy) - https://leetcode.com/problems/relative-sort-array/

class Solution:
    def relativeSortArray(self, arr1: List[int], arr2: List[int]) -> List[int]:
        
        max_num = max(arr1)
        count = [0] * (max_num + 1)

        for i in arr1:
            count[i] += 1
        # print(count)
        
        target = 0
        ans = []
        for i in arr2:
            temp = count[i]
            for j in range(temp):
                ans.append(i)
        a = []
        for i in arr1:
            if i not in arr2:
                a.append(i)
        a.sort()
        ans+=a
        return ans
            
        