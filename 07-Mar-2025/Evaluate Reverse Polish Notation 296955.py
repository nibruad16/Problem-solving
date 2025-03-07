# Problem: Evaluate Reverse Polish Notation - https://leetcode.com/problems/evaluate-reverse-polish-notation/

class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []

        oprators = ["+","-","/","*"]

        for i in tokens:
            if i in oprators:
                temp1 = stack.pop()
                temp2 = stack.pop()
                if i == "+":
                    stack.append(temp2+temp1)
                elif i == "-":
                    stack.append(temp2-temp1)
                elif i == "*":
                    stack.append(temp2*temp1)
                elif i == "/":
                    stack.append(int(temp2/temp1))
            else:
                stack.append(int(i))
        return(stack[0])



        