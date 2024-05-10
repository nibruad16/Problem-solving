class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        ans = []
        left = 0
        right = len(numbers)-1
        for i in range(len(numbers)):
            if( numbers[left] + numbers[right]) > target:
                right -= 1
            elif ( numbers[left] + numbers[right]) < target:
                left += 1
            else:
                ans.append(left+1)
                ans.append(right+1)
            
        s  = set(ans)
        k = list(s)
        k.sort()
        return k
                
        
