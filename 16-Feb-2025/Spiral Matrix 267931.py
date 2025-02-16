# Problem: Spiral Matrix - https://leetcode.com/problems/spiral-matrix/

class Solution:
    def frequencySort(self, s: str) -> str:

        count = Counter(s)
        result = ""
        sorted_key = sorted(count.items(), key = lambda count : (count[1], count[0]))
        print(sorted_key)
        for key, value in sorted_key[::-1]:
            result+= key*value
        return result