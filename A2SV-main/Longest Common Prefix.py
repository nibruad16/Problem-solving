class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        if len(strs) == 0:
            return ""
        if len(strs) == 1:
            return strs[0]
        p = strs[0] 
        pl = len(p)

        for s in strs[1:]:
            while p != s[0:pl]:
                p = p[0:(pl-1)]
                pl -= 1
            if p == 0:
                return ("")
        return p
