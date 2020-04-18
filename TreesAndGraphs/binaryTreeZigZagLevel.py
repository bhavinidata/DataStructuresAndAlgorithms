# Given a binary tree, return the zigzag level order traversal of its nodes' values. (ie, from left to right, then right to left for the next level and alternate between).

# For example:
# Given binary tree [3,9,20,null,null,15,7],
#     3
#    / \
#   9  20
#     /  \
#    15   7
# return its zigzag level order traversal as:
# [
#   [3],
#   [20,9],
#   [15,7]
# ]

# ==============================================================

from typing import List
from collections import deque
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def zigzagLevelOrder(self, root: TreeNode) -> List[List[int]]:
        result = []
        level_list = deque()
        if root is None:
            return result
        # start with the level 0 with a delimiter
        node_queue = deque([root, None])
        is_order_left = True

        while len(node_queue) > 0:
            print(f"length of node_queue: {len(node_queue)}")
            curr_node = node_queue.popleft()
            print(f"CUUR NODE: {curr_node}")
            if curr_node:
                if is_order_left:
                    level_list.append(curr_node.val)
                else:
                    level_list.appendleft(curr_node.val)
                print(f"level_list: {level_list}")
                if curr_node.left:
                    node_queue.append(curr_node.left)
                if curr_node.right:
                    node_queue.append(curr_node.right)
                print(f"node_queue: {node_queue}")
            else:
                # we finish one level
                # Before we start another level, change the value of is_order_left,
                # append None to node_queue to seperate the elements from different level means 
                # when one level finishes there will be None and then we will append another level elements, 
                # empty level_list so that it will start from scratch for new level.
                result.append(level_list)
                # add a delimiter to mark the level
                print(f"NODE Q BEFORE: {node_queue}")
                if len(node_queue) > 0:
                    node_queue.append(None)
                print(f"NODE Q after: {node_queue}")
                # prepare for the next level
                level_list = deque()
                is_order_left = not is_order_left

        return result

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
    resLevels = solution.zigzagLevelOrder(root)
    print(resLevels)

# =====================================================================
# through Recursive call
# from collections import deque

# class Solution:
#     def zigzagLevelOrder(self, root):
#         """
#         :type root: TreeNode
#         :rtype: List[List[int]]
#         """
#         if root is None:
#             return []

#         results = []
#         def dfs(node, level):
#             print(f"level in dfs: {level}")
#             print(f"result: {results}")
#             if level >= len(results):
#                 print(f"level greater than results")
#                 results.append(deque([node.val]))
#                 print(results)
#             else:
#                 if level % 2 == 0:
#                     print("append right")
#                     results[level].append(node.val)
#                 else:
#                     print("appende left")
#                     results[level].appendleft(node.val)

#             for next_node in [node.left, node.right]:
#                 print("go for next node")
#                 if next_node is not None:
#                     dfs(next_node, level+1)

#         # normal level order traversal with DFS
#         dfs(root, 0)

#         return results

# if __name__ == '__main__':
#     solution = Solution()
#     root = TreeNode(5)  
#     root.left = TreeNode(3)  
#     root.right = TreeNode(7)  
#     root.left.left = TreeNode(1)
#     root.left.right = TreeNode(4)
#     root.right.left = TreeNode(6)  
#     root.right.right = TreeNode(9) 

#     resresLevels = [[]]
#     resLevels = solution.zigzagLevelOrder(root)
#     print(resLevels)