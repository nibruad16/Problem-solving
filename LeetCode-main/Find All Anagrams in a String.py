class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        from collections import Counter 
        dataP = Counter(p)
        answer = []
        for i in range(len(s)-len(p)+1):
            newData = Counter(s[i:len(p)+i])
            if dataP == newData:
                answer.append(i)

        return answer
    
