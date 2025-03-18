# Problem: Pascal's Triangle II - LeetCode - https://leetcode.com/problems/pascals-triangle-ii/

class Solution:
    def getRow(self, rowIndex: int) -> List[int]:

       
        def rec(n):
            if n == 0:
               return [1]
            
            prev = rec(n-1)
            new = [1]

            for i in range(len(prev)-1):
                new.append(prev[i]+prev[i+1])
            new.append(1)


            return new
        return rec(rowIndex)
        
        
     