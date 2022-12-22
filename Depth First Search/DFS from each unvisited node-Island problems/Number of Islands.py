class Solution:
    #number of islands 
    def numIslands(self, grid: List[List[str]]) -> int:
        islands = 0
        #make a hashset to prevent visit of nodes more one time
        visit = set()
        rows, cols = len(grid), len(grid[0])

        def dfs(r, c):
            #check if index out of range or value of matrix equals "0" or indicies i visited it before 
            if (
                r not in range(rows)
                or c not in range(cols)
                or grid[r][c] == "0"
                or (r, c) in visit
            ):
                return

            visit.add((r, c))
            #directions to go all the directions from my position 
            directions = [[0, 1], [0, -1], [1, 0], [-1, 0]]
            for dr, dc in directions:
                dfs(r + dr, c + dc)

        for r in range(rows):
            for c in range(cols):
                #if cell equal "1" and the indicies not visited before thats means this new island 
                if grid[r][c] == "1" and (r, c) not in visit:
                    islands += 1
                    dfs(r, c)
        return islands

