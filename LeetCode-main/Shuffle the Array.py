class Solution:
    def shuffle(self, nums: List[int], n: int) -> List[int]:
        nums1 = []
        nums2 = []
        nums1.extend(nums[:n])
        nums2.extend(nums[n:])
        ans = []
        for i in range(n):
            ans.append(nums1[i])
            ans.append(nums2[i])
        return ans
