class Solution:
    def numEnclaves(self, grid: List[List[int]]) -> int:
        rows,cols=len(grid),len(grid[0])
        visit=set()
        def dfs(i,j):
            if i<0 or j<0 or i>=rows or j>=cols or grid[i][j]==0 or (i,j) in visit:
                return 
            visit.add((i,j))
            grid[i][j]-=1
            dfs(i+1,j)
            dfs(i-1,j)
            dfs(i,j+1)
            dfs(i,j-1)

        for r in range(rows):
            for c in range(cols):
                if r==0 or r==rows-1 or c==0 or c==cols-1:
                    dfs(r,c)
        moves=0
        for m in range(rows):
            for n in range(cols):
                if grid[m][n]==1:
                    moves+=1
        return moves

        
       