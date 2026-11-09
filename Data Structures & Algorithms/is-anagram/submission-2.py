# an anagram is a string that containes the exact same characters

class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        s, t = sorted(s), sorted(t)
        if s != t:
            return False
        return True
        