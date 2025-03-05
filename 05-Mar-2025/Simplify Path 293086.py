# Problem: Simplify Path - https://leetcode.com/problems/simplify-path/

class Solution:
    def simplifyPath(self, path: str) -> str:
        stack = []
        new = path.split("/")
        for i in new:
            if i == "" or i == ".":
                continue
            elif i == "..":
                if stack:
                    stack.pop()
            else:
                stack.append(i)
        return "/" + "/".join(stack)

            

        