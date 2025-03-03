# Problem: Partition Array According to Given Pivot - https://leetcode.com/problems/partition-array-according-to-given-pivot/description/

class Solution:
    def pivotArray(self, nums: List[int], pivot: int) -> List[int]:
        befor = []
        midd = []
        after = []

        for i in nums:
            if i < pivot:
                befor.append(i)
            elif i == pivot:
                midd.append(i)
            else:
                after.append(i)
        
        befor += midd
        befor += after
        return befor


        