class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        n = len(nums)
        result = set()

        max_num_index_map = dict({})
        for i,num in enumerate(nums):
            max_num_index_map[num] = i

        for i in range(n):
            for j in range(i+1,n):
                two_sum = nums[i]+nums[j]
                index = max_num_index_map.get(-two_sum,-1)
                if index > j:
                    sorted_nums = sorted([nums[i],nums[j],nums[index]])
                    result.add((sorted_nums[0],sorted_nums[1],sorted_nums[2]))
        
        final_result = [[x for x in item] for item in result]
        return final_result

        