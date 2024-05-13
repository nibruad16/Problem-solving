class Solution:
    def addSpaces(self, s: str, spaces: List[int]) -> str:

        ans = ""
        point = 0
        lens = len(spaces)
        for i in range(len(s)):
            if i == spaces[point]:
                ans+=" "
                if point != lens -1 :
                    point += 1
            ans+=s[i]
        return ans
