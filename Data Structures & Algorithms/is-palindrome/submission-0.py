class Solution:

    def isPalindrome(self, s: str) -> bool:
        s_lower = s.lower()
        s_clean = ''.join(c for c in s_lower if (ord(c)-ord('a') in range(0,26)) or (ord(c)-ord('0')in range(0,10)))
        return s_clean == s_clean[::-1]
        