class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        my_anagrams = dict()
        for string in strs:
            sorted_string = "".join(sorted(string))
            cur_anagram_list = my_anagrams.get(sorted_string,[])
            my_anagrams[sorted_string] = cur_anagram_list + [string]
        print(my_anagrams.values())
        return list(my_anagrams.values())
        