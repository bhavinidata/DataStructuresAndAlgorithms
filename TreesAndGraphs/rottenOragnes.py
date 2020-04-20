# In a given grid, each cell can have one of three values:

# the value 0 representing an empty cell;
# the value 1 representing a fresh orange;
# the value 2 representing a rotten orange.
# Every minute, any fresh orange that is adjacent (4-directionally) to a rotten orange becomes rotten.

# Return the minimum number of minutes that must elapse until no cell has a fresh orange.  If this is impossible, return -1 instead.

 

# Example 1:



# Input: [[2,1,1],[1,1,0],[0,1,1]]
# Output: 4
# Example 2:

# Input: [[2,1,1],[0,1,1],[1,0,1]]
# Output: -1
# Explanation:  The orange in the bottom left corner (row 2, column 0) is never rotten, because rotting only happens 4-directionally.
# Example 3:

# Input: [[0,2]]
# Output: 0
# Explanation:  Since there are already no fresh oranges at minute 0, the answer is just 0.
 

# Note:

# 1 <= grid.length <= 10
# 1 <= grid[0].length <= 10
# grid[i][j] is only 0, 1, or 2.

# =======================================================
# Solution with BFS

from collections import deque
from typing import List
class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        rows, cols = len(grid), len(grid[0])
        fresh = 0
        # store location of rotten oranges in queue
        q = deque()
        for i in range(rows):
            for j in range(cols):
                if grid[i][j] == 1:
                    fresh += 1
                elif grid[i][j] == 2:
                    q.append((i, j))
        # if there is no fresh oranges then return 0 
        if fresh == 0:
            return 0
        # take adjacent locations of rotten oranges in the list
        dirs = [(0, 1), (0, -1), (-1, 0), (1, 0)]
        step = 0
        while q:
            size = len(q)
            # iterate through the each element in the level
            for i in range(size):
                x, y = q.popleft()
                for d in dirs:
                    nx, ny = x + d[0], y + d[1]
                    if nx < 0 or nx >= rows or ny < 0 or ny >= cols or grid[nx][ny] != 1:
                        continue
                    grid[nx][ny] = 2
                    q.append((nx, ny))
                    fresh -= 1
            step += 1
        if fresh != 0:
            return -1
        # need to reduce step by 1 as we have started with 1 with first rotten orange.
        return step - 1

if __name__ == '__main__':
    myGrid = [[2,1,1],[1,1,0],[0,1,1], [1,1,0]]
    solution = Solution()
    result = solution.orangesRotting(myGrid)
    print(f"Minutes: {result}")