class Solution:
    def findMin(self, nums: List[int]) -> int:
        i,j=0,len(nums)-1
        mid = 0
        while i<j:
            if nums[i]<nums[j]:
                return nums[i]
            if i==j-1:
                return nums[j]
            else:
                mid = (i+j)//2
                if nums[mid] > nums[i]:
                    i = mid+1
                else:
                    j = mid

        return nums[i]