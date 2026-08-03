class Solution:
    def climbStairs(self, n: int) -> int:
        if n<1:
            return 0
        elif n==1:
            return 1
        elif n==2:
            return 2
        dist_ways = [0]*n
        dist_ways[0:2]=[1,2]
        for i in range(2,n,1):
            dist_ways[i] = dist_ways[i-1]+dist_ways[i-2]
        return dist_ways[n-1]
        