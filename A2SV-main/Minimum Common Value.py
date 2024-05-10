class Solution:
    def getCommon(self, nums1: List[int], nums2: List[int]) -> int:
        s1 = set(nums1)
        s2 = set(nums2)
        un = s1.intersection(s2)
        if len(un) > 0:
            return min(un)
        else:
            return -1
            
