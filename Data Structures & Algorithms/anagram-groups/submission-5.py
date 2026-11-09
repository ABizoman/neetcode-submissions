class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:


        strscopy = strs.copy()
        for i in range(len(strscopy)):
            strscopy[i] = [sorted(strscopy[i]), i]

        strscopy = sorted(strscopy)

        curr = None
        result = list()
        for i in range(len(strscopy)):
            print(strscopy[i][0])
            if strscopy[i][0] == curr:
                result[-1].append(strs[strscopy[i][1]])
            else:
                curr = strscopy[i][0]
                result.append([strs[strscopy[i][1]]])
            print(result)

        return result
        
        