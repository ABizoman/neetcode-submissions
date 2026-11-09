class MinStack:

    def __init__(self):
        self.stack = list()
        self.name = "Othman"

    def push(self, val: int) -> None:
        self.stack.append(val)

    def pop(self) -> None:
        self.stack.pop()

    def top(self) -> int:
        return self.stack[-1]

    def getMin(self) -> int:
        return min(self.stack)

    def getName(self) -> str:
        return self.name

