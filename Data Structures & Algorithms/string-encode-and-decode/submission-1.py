class Solution:

    def encode(self, strs: List[str]) -> str:

        encoded_string = ""
        for string in strs:
            encoded_string += string + "EndSalt"

        return encoded_string

    def decode(self, s: str) -> List[str]:
        
        strs = s.split("EndSalt")[:-1]

        return strs
