class Solution:
    def hammingWeight(self, n: int) -> int:
        num_1_bit = 0
        while n>0:
            num_1_bit += n%2
            n = n//2
        return num_1_bit
        