# Problem: Pancake Sorting - https://leetcode.com/problems/pancake-sorting/

class Solution:
    def pancakeSort(self, arr: List[int]) -> List[int]:
        x = len(arr)
        k = []
        for i in range(x):
            max_ = max(arr[:x-i])
            max_in = arr.index(max_) + 1
            arr[:max_in] = reversed(arr[:max_in])
            k.append(max_in)
            arr[:x-i] = reversed( arr[:x-i])
            k.append(x-i)
        return k
        