class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        my_map = dict()
        for x in s:
            if x in my_map.keys():
                my_map[x] += 1
            else:
                my_map[x] = 1
        for y in t:
            if y in my_map.keys():
                my_map[y] -= 1
            else:
                return False
        for v in my_map.values():
            if v != 0:
                return False
        return True
        