#goal here is to return the time, not mark every cell 
from collections import deque
class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        fresh = 0 
        time = 0
        queue = deque()
        for r in range(len(grid)):
            for c in range(len(grid[0])):
                if grid[r][c] == 1:
                    fresh += 1
                if grid[r][c] == 2:
                    queue.append((r,c))
        while queue and fresh > 0:
            for q in range(len(queue)):
                r,c = queue.popleft()
                if r+1 < len(grid) and grid[r+1][c] == 1:
                    grid[r+1][c] = grid[r][c]
                    fresh -= 1
                    queue.append((r+1,c))
                if r-1 >= 0 and grid[r-1][c] == 1:
                    grid[r-1][c] = grid[r][c]
                    fresh -= 1
                    queue.append((r-1,c))
                if c+1 < len(grid[0]) and grid[r][c+1] == 1:
                    grid[r][c+1] = grid[r][c]
                    fresh -= 1
                    queue.append((r,c+1))
                if c-1 >= 0 and grid[r][c-1] == 1:
                    grid[r][c-1] = grid[r][c]
                    fresh -= 1
                    queue.append((r,c-1))
            time += 1
        if fresh == 0:
            return time
        else:
            return -1
