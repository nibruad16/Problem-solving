class Solution:
    def commonChars(self, words: List[str]) -> List[str]:
        from collections import Counter
        
        c = Counter(words[0])
        
        for i in range(1, len(words)):
            c &= Counter(words[i])

        re = []
        
        for char, count in c.items():
            re.extend([char] * count)
            
        return re
        
