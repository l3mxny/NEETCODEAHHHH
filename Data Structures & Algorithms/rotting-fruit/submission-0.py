from collections import deque
class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        queue = deque()

        for r in range(len(grid)):
            for c in range(len(grid[0])):
                if grid[r][c] == 2:
                    queue.append((r,c))
        while queue: 
            r,c = queue.popleft()
            if r+1 < len(grid) and grid[r+1][c] == 1:
                grid[r+1][c] = grid[r][c]+1
                queue.append((r+1,c))
            if r-1 >= 0 and grid[r-1][c] == 1:
                grid[r-1][c] = grid[r][c]+1
                queue.append((r-1,c))
            if c+1 < len(grid[0]) and grid[r][c+1] == 1:
                grid[r][c+1] = grid[r][c]+1
                queue.append((r,c+1))
            if c-1 >= 0 and grid[r][c-1] == 1:
                grid[r][c-1] = grid[r][c]+1
                queue.append((r,c-1))
        #special case starts here
        maxFruit = 0 
        for r in range(len(grid)):
            for c in range(len(grid[0])):
                if grid[r][c] == 1:
                    return -1
                maxFruit = max(maxFruit, grid[r][c])
        
        return maxFruit - 2