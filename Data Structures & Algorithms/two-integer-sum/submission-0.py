class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        my_map = dict({})
        for i,num in enumerate(nums):
            j = my_map.get(target-num,-1)
            if j != -1:
                return [j,i]
            else:
                my_map[num] = i
        return [-1,-1]
        