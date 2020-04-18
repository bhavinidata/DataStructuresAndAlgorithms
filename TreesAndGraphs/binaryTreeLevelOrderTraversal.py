# Given a binary tree, return the level order traversal of its nodes' values. (ie, from left to right, level by level).

# For example:
# Given binary tree [3,9,20,null,null,15,7],
#     3
#    / \
#   9  20
#     /  \
#    15   7
# return its level order traversal as:
# [
#   [3],
#   [9,20],
#   [15,7]
# ]

# =============================================================

from collections import deque
from typing import List
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def levelOrder(self, root: TreeNode) -> List[List[int]]:
        levels = []
        if not root:
            return levels
        
        level = 0
        queue = deque([root,])
        # print(queue)
        # print(len(queue))
        while queue:
            print("in QUEUE")
            # start the current level
            levels.append([])
            # number of elements in the current level 
            level_length = len(queue)
            print(f"levelLength: {level_length}")
            for i in range(level_length):
                node = queue.popleft()
                print(f"node: {node}")
                # fulfill the current level
                levels[level].append(node.val)
                print(f"LEVELS: {levels}")
                # add child nodes of the current level
                # in the queue for the next level
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
            print(f"queue last: {queue}")
            
            # go to next level
            level += 1
        
        return levels


if __name__ == '__main__':
    solution = Solution()
    root = TreeNode(5)  
    root.left = TreeNode(3)  
    root.right = TreeNode(7)  
    root.left.left = TreeNode(1)
    root.left.right = TreeNode(4)
    root.right.left = TreeNode(6)  
    root.right.right = TreeNode(9) 

    resresLevels = [[]]
    resLevels = solution.levelOrder(root)
    print(resLevels) 
