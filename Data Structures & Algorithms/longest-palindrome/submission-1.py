class Solution:
    def longestPalindrome(self, s: str) -> int:
        char_dict = defaultdict(int)
        for char in s:
            char_dict[char] += 1

        total = 0
        for count in char_dict:
            if char_dict[count] % 2 == 0:
                total += char_dict[count]

        for count in char_dict:
            if char_dict[count] % 2 == 1:
                while char_dict[count] > 1:
                    char_dict[count] -= 2
                    total += 2

        
        for count in char_dict:
            if char_dict[count] == 1:
                total += 1
                break

        return total
