class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        n,m = len(grid),len(grid[0])
        num_island = 0
        is_visited = [[False for j in range(m)] for _ in range(n)]
        
        for i in range(n):
            for j in range(m):
                if grid[i][j] == "1" and is_visited[i][j] == 0:
                    num_island += 1
                    is_visited[i][j] = True
                    stack = []
                    stack.append((i,j))
                    while stack:
                        # right
                        cur_x,cur_y = stack.pop()
                        if cur_y+1<m and grid[cur_x][cur_y+1]=="1" and is_visited[cur_x][cur_y+1]==False:
                            stack.append((cur_x,cur_y+1))
                            is_visited[cur_x][cur_y+1]=True
                        # left
                        if cur_y-1>=0 and grid[cur_x][cur_y-1]=="1" and is_visited[cur_x][cur_y-1]==False:
                            stack.append((cur_x,cur_y-1))
                            is_visited[cur_x][cur_y-1]=True
                        # up
                        if cur_x-1>=0 and grid[cur_x-1][cur_y]=="1" and is_visited[cur_x-1][cur_y]==False:
                            stack.append((cur_x-1,cur_y))
                            is_visited[cur_x-1][cur_y]=True
                        # down
                        if cur_x+1<n and grid[cur_x+1][cur_y]=="1" and is_visited[cur_x+1][cur_y]==False:
                            stack.append((cur_x+1,cur_y))
                            is_visited[cur_x+1][cur_y]=True
        return num_island

        