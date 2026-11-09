class Solution:

    def encode(self, strs: List[str]) -> str:

        encoded_string = ""
        for string in strs:
            encoded_string += string + "End"

        return encoded_string

    def decode(self, s: str) -> List[str]:
        
        strs = s.split("End")[:-1]

        return strs
