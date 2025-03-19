# Problem: Decode String - https://leetcode.com/problems/decode-string/

class Solution:
    def decodeString(self, s: str) -> str:

        def helper(s,index):
            result = ""
            num = 0
            while index < len(s):
                char = s[index]
                if char.isdigit():
                    num = num * 10 + int(char)
                    index += 1
                elif char == "[":
                    decode , index = helper(s,index+1)
                    result += decode * num
                    num = 0
                elif char == "]":
                    return result , index+1
                else:
                    result += char
                    index += 1
            return result , index
        new, _  = helper(s,0)  
        return new                 


