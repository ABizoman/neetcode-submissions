import itertools

class Solution:
    def reverseWords(self, s: str) -> str:
        
        words = [[""]]
        for char in s: 
            if char != " ":
                words[len(words)-1] += char
            else: 
                words.append([" "])
                words.append([""])
        
        print(words)

        for word in words:
            word = word.reverse()



        return "".join(itertools.chain.from_iterable(words))
            
