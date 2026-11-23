class Solution:
    def backspaceCompare(self, s: str, t: str) -> bool:
        string = []
        tring = []

        for char in s:
            if ord(char) > 96 and ord(char) < 123:
                string.append(char)
            elif char == "#" and len(string) > 0:
                string.pop()

        for char in t:
            if ord(char) > 96 and ord(char) < 123:
                tring.append(char)
            elif char == "#" and len(tring) > 0:
                tring.pop()

        print(string, tring)

        if len(string) != len(tring):
            return False
        for i in range(len(string)):
            if string[i] != tring[i]:
                return False
        return True
