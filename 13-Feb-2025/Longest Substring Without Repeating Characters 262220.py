# Problem: Longest Substring Without Repeating Characters - https://leetcode.com/problems/longest-substring-without-repeating-characters/

class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        left = 0
        maxs = 0
        track = set()
        
        for r in range(len(s)):
            while s[r] in track:
                track.remove(s[left])
                left += 1
            track.add(s[r])
            maxs = max(maxs, r - left + 1) 

        return maxs


        