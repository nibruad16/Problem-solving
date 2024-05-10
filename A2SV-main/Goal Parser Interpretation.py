class Solution:
    def interpret(self, command: str) -> str:
        a = command.replace("G", "G")
        b = a.replace("()", "o")
        c = b.replace("(al)", "al")
        return c
        
