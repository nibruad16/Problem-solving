# Problem: H-Index - https://leetcode.com/problems/h-index/

class Solution:
    def hIndex(self, citations: List[int]) -> int:
        ans  = 0
        citations.sort(reverse=True)
    
    # Iterate through the sorted array
        for i, citation in enumerate(citations):
            # Check if the citation count is >= h (i + 1)
            if citation < i + 1:
                return i  # Return the previous h-index
        # If all citations are >= h, return the length of the array
        return len(citations)

 