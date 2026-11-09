class Solution:
    def isPalindrome(self, s: str) -> bool:
        s = s.casefold()
        s = s.replace(' ', '')
        for char in s:
            if not char.isalnum():
                s = s.replace(char, '')
        return s == s[::-1]
        
