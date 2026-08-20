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

        return max(robb(nums,n-1),robb(nums[::-1],n-1))




        
        dp = [0]*n
        is_start = [False]*n
        dp[0:2] = nums[0],max(nums[0],nums[1])
        is_start[0] = True
        if nums[0]>nums[1]:
            is_start[1] = True
        print(f"index: {0}, dp: {dp[0]}, is_start: {is_start[0]}")
        print(f"index: {1}, dp: {dp[1]}, is_start: {is_start[1]}")
        for i in range(2,n-1):
            if dp[i-2]+nums[i] > dp[i-1]:
                is_start[i] = is_start[i-2]
                dp[i] = dp[i-2]+nums[i]
            else:
                is_start[i] = is_start[i-1]
                dp[i] = dp[i-1]   
            print(f"index: {i}, dp: {dp[i]}, is_start: {is_start[i]}")

        if dp[n-2]>=dp[n-3]+nums[n-1]:
            print(f"index: {n-2}, dp: {dp[n-2]}, is_start: {is_start[n-2]}")
            return dp[n-2]
        else:
            if is_start[n-3]:
                print(f"is_start: {is_start[n-3]}")
                return max(dp[n-3],dp[n-2],dp[n-3]-nums[0]+nums[n-1])
            else:
                print(f"is_start: {is_start[n-3]}")
                return dp[n-3]+nums[n-1]
        