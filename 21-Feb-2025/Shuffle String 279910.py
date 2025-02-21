# Problem: Shuffle String - https://leetcode.com/problems/shuffle-string/description/

class Solution:
    def restoreString(self, s: str, indices: List[int]) -> str:
        res,res_1=[],[]
        ans=""
        for i in range(len(s)):
            res.append(s[i])
        for i in range(len(res)):
            res_1.append((res[i],indices[i]))
        for i in range(len(res)):
            for j in res_1:
                if j[1]==i:
                    ans +=j[0]
        return ans
        