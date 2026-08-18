class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        char_dict = {}
        i,j,n = 0,0,len(s)
        max_length = 0
        while i<n and j<n:
            while j<n:
                max_char_count = 0
                for count in char_dict.values():
                    max_char_count = max(count, max_char_count)
                # print(f"max_char_count:{max_char_count}; start:{i}; end:{j}")
                if max_char_count+k>j-i:
                    char_count = char_dict.get(ord(s[j])-ord('A'),0)
                    char_dict[ord(s[j])-ord('A')] = char_count+1
                    j+=1
                elif max_char_count+k==j-i and char_dict.get(ord(s[j])-ord('A'),0)==max_char_count:
                    char_count = char_dict.get(ord(s[j])-ord('A'),0)
                    char_dict[ord(s[j])-ord('A')] = char_count+1
                    j+=1
                else:
                    break
            max_length = max(max_length,j-i)
            # print("max_length:",max_length)
            # print("------------------------------------")
            char_count = char_dict.get(ord(s[i])-ord('A'),0)
            char_dict[ord(s[i])-ord('A')] = char_count-1
            i+=1
        return max_length
                    


            


        