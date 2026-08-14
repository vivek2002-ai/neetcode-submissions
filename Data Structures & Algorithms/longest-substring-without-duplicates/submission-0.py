class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        longest_len = 0
        i,j=0,0
        letter_map = {}
        while j<len(s):
            is_present = letter_map.get(s[j],False)
            if is_present:
                letter_map[s[i]] = False
                i += 1
            else:
                longest_len = max(longest_len, j-i+1)
                letter_map[s[j]] = True
                j += 1
        return longest_len
            
        