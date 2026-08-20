class Solution:
    def rob(self, nums: List[int]) -> int:
        n = len(nums)
        if n == 1:
            return nums[0]
        elif n == 2:
            return max(nums[1],nums[0])
        n = len(nums)
        def robb(nums,r):
            max_rob = 0
            pre_max_rob = 0
            pre_pre_max_rob = nums[0]
            max_rob = pre_max_rob = max(nums[0],nums[1])
            for i in range(2,r):
                if pre_max_rob > pre_pre_max_rob+nums[i]:
                    pre_pre_max_rob = pre_max_rob
                else:
                    max_rob = pre_pre_max_rob+nums[i]
                    pre_pre_max_rob = pre_max_rob
                    pre_max_rob = max_rob
            return max_rob
        max_rob = robb(nums,n-1)
        for i in range(n//2):
            cur_i = nums[i]
            nums[i] = nums[n-i-1]
            nums[n-i-1] = cur_i
        max_rob = max(max_rob,robb(nums,n-1))
        return max_rob
        