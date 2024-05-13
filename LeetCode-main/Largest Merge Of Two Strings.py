class Solution:
    def largestMerge(self, word1: str, word2: str) -> str:
        ans = []
        len1=len(word1)
        lword1 = list(word1)
        len2=len(word2)
        lword2 = list(word2)
        for i in range(len1+len2):
            if lword1 > lword2:
                ans.append(lword1[0])
                lword1.remove(lword1[0])
            else:
                ans.append(lword2[0])
                lword2.remove(lword2[0])
        return "".join([str(i) for i in ans])

        
        
