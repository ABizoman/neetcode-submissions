class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        maxL = 0
        chars = set()
        i = 0
        for char in s:
            while char in chars:
                chars.remove(s[i])
                i += 1
            chars.add(char)
            maxL = max(len(chars), maxL)

        return maxL
