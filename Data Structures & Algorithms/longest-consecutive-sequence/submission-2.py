class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        sorted_nums = sorted(nums)
        max_count = 0
        cur_count = 1
        pre = None
        for num in sorted_nums:
            if pre != None and pre == num-1:
                cur_count += 1
            elif pre != None and pre != num:
                cur_count = 1
            max_count = max(max_count,cur_count)
            pre = num
        return max_count


        