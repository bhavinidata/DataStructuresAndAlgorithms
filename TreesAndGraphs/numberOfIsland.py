# Given a 2d grid map of '1's (land) and '0's (water), count the number of islands. An island is surrounded by water and is formed by connecting adjacent lands horizontally or vertically. You may assume all four edges of the grid are all surrounded by water.

# Example 1:

# Input:
# 11110
# 11010
# 11000
# 00000

# Output: 1
# Example 2:

# Input:
# 11000
# 11000
# 00100
# 00011

# Output: 3

# ===============================================================
# solution using BFS
from typing import List
from collections import deque
class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        if not grid or not grid[0]:
            return 0
        numberOfIsland = 0
        rows, cols = len(grid), len(grid[0])
        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == "1":
                    self.chkAdjacent(grid, r, c)
                    numberOfIsland +=1
                    print(grid)
                    print(f"nu of island: {numberOfIsland}")
        return numberOfIsland

    def chkAdjacent(self, grid, x, y):
        q = deque()
        q.append((x,y))
        grid[x][y] = "99"
        while q:
            dirs = [(0, 1), (0, -1), (-1, 0), (1, 0)]
            x, y = q.popleft()
            for d in dirs:
                print("check direction")
                nx, ny = x+d[0], y+d[1]
                rows, cols = len(grid), len(grid[0])
                if nx>=0 and ny >=0 and nx<rows and ny<cols and grid[nx][ny]=="1":
                    grid[nx][ny] = "99"
                    print(grid)
                    q.append((nx,ny))
                


if __name__ == '__main__':
    # myGrid = [["1", "1", "0", "0", "0"], 
    #     ["0", "1", "0", "0", "1"], 
    #     ["1", "0", "0", "1", "1"], 
    #     ["0", "0", "0", "0", "0"], 
    #     ["1", "0", "1", "0", "1"]] 

    myGrid = [["1", "1", "0", "0", "1"], 
        ["1", "1", "0", "0", "0"], 
        ["0", "1", "1", "0", "0"], 
        ["1", "0", "0", "1", "1"]] 

    # myGrid = [["1", "1", "0"], 
    #     ["1", "1", "0"], 
    #     ["0", "0", "1"],
    #     ["0", "1", "0"]] 
    solution = Solution()
    result = solution.numIslands(myGrid)
    print(f"Number of Island: {result}")


# # ===========================================================
# from typing import List
# class Solution:
#     def numIslands(self, grid: List[List[str]]) -> int:
#         print(grid)
#         # check if it is empty grid then simply return number of island as 0
#         if not grid:
#             print("not grid")
#             return 0
#         # take counter to count number of island
#         noOfIsland = 0
#         # get the number of rows
#         rows = len(grid)
#         # get the number of columns
#         cols = len(grid[0])
        
#         # iterate through each rows of matrix
#         for r in range(rows):
#             # in particular row of matrix, iterate through the each column
#             for c in range(cols):
#                 # check if the particular element is "1"(here matrix elements are 1 
#                 # but it is represented in string as seen from function parameter List[List[str]])
#                 if grid[r][c] == "1":
#                     # if "1" is found then increament the number of island
#                     noOfIsland += 1
#                     # call the helper function
#                     self.chkAdjacent(grid, r, c)
#         print(grid)
#         return noOfIsland
    
#     # helper function, which is called when "1" is encountered.
#     # this function will change "1" to "99", so when we encounter "99" we don't go ahead with the process.
    
#     def chkAdjacent(self,grid, r, c):
#         if r>=0 and c>=0 and r<len(grid) and c<len(grid[0]):
#             if grid[r][c] == "1":
#                 grid[r][c] = "99"
#                 # check the element in above row but the same column.
#                 # keep on checking until it is "1" or matrix limit is reached
#                 self.chkAdjacent(grid, r+1, c)
#                 # check the element in below row but the same column.
#                 # keep on checking until it is "1" or matrix limit is reached
#                 self.chkAdjacent(grid, r-1, c)
#                 # check the element in same row but the right column.
#                 # keep on checking until it is "1" or matrix limit is reached
#                 self.chkAdjacent(grid, r, c+1)
#                 # check the element in same row but the left column.
#                 # keep on checking until it is "1" or matrix limit is reached
#                 self.chkAdjacent(grid, r, c-1)
#             else:
#                 return
#         else:
#             return

# if __name__ == '__main__':
#     # myGrid = [["1", "1", "0", "0", "0"], 
#     #     ["0", "1", "0", "0", "1"], 
#     #     ["1", "0", "0", "1", "1"], 
#     #     ["0", "0", "0", "0", "0"], 
#     #     ["1", "0", "1", "0", "1"]] 

#     myGrid = [["1", "1", "0", "0", "1"], 
#         ["1", "1", "0", "0", "0"], 
#         ["0", "1", "1", "0", "0"], 
#         ["1", "0", "0", "1", "1"]] 
#     solution = Solution()
#     result = solution.numIslands(myGrid)
#     print(f"Number of Island: {result}")

