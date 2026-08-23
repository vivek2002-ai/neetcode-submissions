class Solution:
    def longestPalindrome(self, s: str) -> str:
        n = len(s)
        if n==1:
            return s
        longest_pal = 1
        pal_str = s[0]
        for i in range(1,n-1):
            window_center = min(i,n-i-1)
            j = 0
            while j<window_center and s[i+j+1]==s[i-j-1]:
                j+=1
            if 2*j+1>longest_pal:
                longest_pal = 2*j+1
                pal_str = s[i-j:i+j+1]
            window_right = min(i,n-i)
            k=0
            while k<window_right and s[i+k]==s[i-k-1]:
                k+=1
            if 2*k>longest_pal:
                longest_pal = 2*k
                pal_str = s[i-k:i+k]
        if s[n-2]==s[n-1] and longest_pal==1:
            return s[n-2:]
        return pal_str

        