class Solution:
    def rob(self, nums: List[int]) -> int:
        n = len(nums)
        if n==0:
            return 0
        elif n==1:
            return nums[0]
        elif n==2:
            return max(nums[0],nums[1])
        max_2_loots = [nums[0],max(nums[0],nums[1])]
        for i in range(2,n):
            cur_max = max_2_loots[1]
            max_2_loots[1] = max(cur_max,max_2_loots[0]+nums[i])
            max_2_loots[0] = cur_max

        return max_2_loots[1]
        