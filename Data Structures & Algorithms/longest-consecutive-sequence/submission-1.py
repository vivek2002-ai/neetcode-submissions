class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        sorted_set = set(nums)
        res = 0
        
        for num in nums:
            curr,streak = num, 0
            while curr in sorted_set:
                streak += 1
                curr += 1
            res = max(res, streak)
        return res

        