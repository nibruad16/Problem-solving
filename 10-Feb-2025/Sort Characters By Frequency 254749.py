# Problem: Sort Characters By Frequency - https://leetcode.com/problems/sort-characters-by-frequency/description/

class Solution:
    def frequencySort(self, s: str) -> str:

        ans =  []
        for char in set(s):
            cnt = s.count(char)
            ans.append(char * cnt)
        ans = sorted(ans, key=len , reverse = True)
        return "".join(ans)


        # new = Counter(s)
        # new = dict(sorted(new.items(), key=lambda x : x[1], reverse = True))
        # ans = ""
        # for key , val in new.items():
        #     for i in range(val):
        #         ans += key
        # return (ans)

        
        