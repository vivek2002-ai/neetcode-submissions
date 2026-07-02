class Solution:

    def encode(self, strs: List[str]) -> str:
        encoded_string = ''
        for string in strs:
            encoded_string += '#$ '+string+' $#'
        return encoded_string

    def decode(self, s: str) -> List[str]:
        n = len(s)
        i = 0
        strs = []
        end = " $#"
        print(s)
        while(i+5 < n):
            j = i + 3
            while (j+2 < n) and (s[j:j+3]!=end):
                j += 1
            strs.append(s[i+3:j])
            i = j + 3
        return strs
