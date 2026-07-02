class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        nums_length = len(nums)
        left_product = [1]*nums_length
        right_product = [1]*nums_length
        result = []
        for i in range(nums_length):
            left_product[i] = left_product[i-1]*nums[i-1] if i > 0 else 1
            j = nums_length - i - 1
            right_product[j] = right_product[j+1]*nums[j+1] if j < nums_length-1 else 1

        for i in range(nums_length):
            product = left_product[i]*right_product[i]
            result.append(product)
        return result
        