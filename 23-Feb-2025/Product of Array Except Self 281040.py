# Problem: Product of Array Except Self - https://leetcode.com/problems/product-of-array-except-self/

class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        pro = 1
        ans = []
        flag = True
        count = 0
        for i in nums:
            if i == 0:
                flag = False
                count += 1
                continue 
            else:
                pro *= i
        
        for i in nums:
            if flag:
                ans.append(pro//i)
            else:
                if i == 0 and count >= 2:
                    ans.append(0)
                else:
                    if i != 0:
                        ans.append(0)
                    else:
                        ans.append(pro)
        return ans
    

        
