# Problem: Minimum Recolors to Get K Consecutive Black Blocks - https://leetcode.com/problems/minimum-recolors-to-get-k-consecutive-black-blocks/

class Solution:
    def minimumRecolors(self, blocks: str, k: int) -> int:
        ans = float('inf')
        temp = blocks[:k]
        dummy = temp.count("W")
        ans = min(dummy,ans)
        print(temp)
        for i in range(k,len(blocks)):
            temp = blocks[i-k+1:i+1]
            print(temp)
            dummy = temp.count("W")
            ans = min(dummy,ans)
        return ans




        
        