class Solution:
    def isValid(self, s: str) -> bool:
        opens = ('[','(','{')
        # openDict = dict()
        # closes = (']',')','}')
        closesDict = {']':'[',')':'(','}':'{'}

        # for parenthese in s:
        #     if parenthese in opens:
        #         current = openDict.get(parenthese, 0)
        #         current += 1
        #         openDict[parenthese] = current
        #     elif parenthese in closes:
        #         opposite = closesDict[parenthese]
        #         current = openDict.get(opposite, 0)
        #         current = current - 1
        #         openDict[opposite] = current 
        
        # remaining = openDict.values()
        # print(openDict)
        # print(remaining)
        
        # for x in remaining:
        #     if x != 0:
        #         return False

        # return True

        opened = []

        for parenthese in s:
            if len(opened) > 0:
                if closesDict.get(parenthese, 0) == opened[-1]:
                    opened.pop()
                    continue
            if parenthese in opens:
                opened.append(parenthese)
            else:
                return False

        if len(opened) == 0:
            return True
        return False
        