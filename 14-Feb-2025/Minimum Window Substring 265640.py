# Problem: Minimum Window Substring - https://leetcode.com/problems/minimum-window-substring/submissions/

class Solution:
    def minWindow(self, s: str, t: str) -> str:
        def check(w_c,t_c):
            for ch , count in t_c.items():
                if w_c[ch] < count:
                    return False
            return True

        count_target = Counter(t)
        window_count = Counter()
        ans = ""
        left = right = 0
        while right < len(s):
            window_count[s[right]] += 1

            while check(window_count , count_target):
                c = right - left + 1
                

                if c < len(ans) or ans == "":
                    ans = s[left:right + 1]
                
                window_count[s[left]] -= 1
                left += 1

            right += 1

        return ans

                

        
        
       









































        # def check(window_counter, target_counter):
        #     for char, count in target_counter.items():
        #         if window_counter[char] < count:
        #             return False
        #     return True

        # t_c = Counter(t)  
        # window = Counter()  

        # l = r = 0
        # ans = ""

        # while r < len(s):
        #     window[s[r]] += 1
            
           
        #     while check(window, t_c):
        #         c = r - l + 1
               
        #         if c < len(ans) or ans == "":
        #             ans = s[l:r+1]
                   

        #         window[s[l]] -= 1
        #         l += 1

        #     print(window)
        #     r += 1  
        
        # return ans
