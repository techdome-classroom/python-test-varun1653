class Solution:
   

    def explore_island(self, grid, row, col):
        if row < 0 or row >= len(grid) or col < 0 or col >= len(grid[0]) or grid[row][col] != "L":
            return
        grid[row][col] = "W"  

        
        self.explore_island(grid, row + 1, col)
        self.explore_island(grid, row - 1, col)
        self.explore_island(grid, row, col + 1)
        self.explore_island(grid, row, col - 1)

    def getTotalIsles(self, grid: list[list[str]]) -> int:
        if not grid:
            return 0

        num_islands = 0
        rows, cols = len(grid), len(grid[0])

        for i in range(rows):
            for j in range(cols):
                if grid[i][j] == "L":
                    self.explore_island(grid, i, j)
                    num_islands += 1

        return num_islands




         
        return 0
        