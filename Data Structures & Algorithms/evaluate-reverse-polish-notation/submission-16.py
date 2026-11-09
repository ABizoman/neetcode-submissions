from abc import abstractproperty
class Solution:
    def __init__(self):
        self.total = 0
        self.operands = ('+','-','*','/')

    def evalRPN(self, tokens: List[str]) -> int:
        
        # just use a stack
        stack = list()
        for char in tokens:
            if char in self.operands:
                scndNum = stack.pop()
                if char == "+":
                    val = stack.pop() + scndNum
                elif char == "-":
                    val = stack.pop() - scndNum
                elif char == "*":
                    val = stack.pop() * scndNum
                elif char == "/":
                    val = int(stack.pop() / scndNum)
                stack.append(val)
            else:
                stack.append(int(char))

        return stack.pop()



        
