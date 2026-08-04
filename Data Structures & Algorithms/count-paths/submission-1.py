class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        dp_pre_row = [0]*m
        dp_cur = 0
        for i in range(n):
            for j in range(m):
                if i ==0 and j==0:
                    dp_cur = 1
                    dp_pre_row[j] = 1
                elif j==0:
                    dp_cur = dp_pre_row[j]
                else:
                    dp_cur = dp_cur + dp_pre_row[j]
                    dp_pre_row[j] = dp_cur
        return dp_cur
        