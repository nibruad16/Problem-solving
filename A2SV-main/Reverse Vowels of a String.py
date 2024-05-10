class Solution:
    def reverseVowels(self, s: str) -> str:
        list_vouls = ["a","A","e","E","i","I","o","O","u","U"]
        first = 0
        last = len(s) - 1
        s1 = list(s)
        while first < last:
            if s1[first] in list_vouls and s1[last] in list_vouls: 
                s1[first] , s1[last] = s1[last] , s1[first]
                first += 1
                last -= 1 
            elif s1[first] not in list_vouls and s1[last] in list_vouls:
                first += 1
            elif s1[first] in list_vouls and s1[last] not in  list_vouls: 
                last -= 1
            else:
                first += 1
                last -= 1   
        return ("".join(str(i) for i in s1))
