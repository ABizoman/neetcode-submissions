class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        maxL = 0
        chars = set()
        i = 0
        for j, char in enumerate(s):
            if char not in chars:
                chars.add(char)
            else:
                while char in chars:
                    chars.remove(s[i])
                    i += 1
                chars.add(char)
            maxL = max(len(chars), maxL)

        return maxL
