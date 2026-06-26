class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        for i,x in enumerate(nums):
            nums[i] = (x,i)
        nums = sorted(nums,key = lambda x: x[0])
        print(nums)
        i = 0; j=len(nums)-1
        while i<j:
            if nums[i][0]+nums[j][0] == target:
                return sorted([nums[i][1],nums[j][1]])
            elif nums[i][0]+nums[j][0] > target:
                j = j-1
            else:
                i = i+1
        return [-1,-1]
        