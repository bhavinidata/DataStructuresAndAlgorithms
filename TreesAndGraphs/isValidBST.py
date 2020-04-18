# Given a binary tree, determine if it is a valid binary search tree (BST).

# Assume a BST is defined as follows:

# The left subtree of a node contains only nodes with keys less than the node's key.
# The right subtree of a node contains only nodes with keys greater than the node's key.
# Both the left and right subtrees must also be binary search trees.
 

# Example 1:

#     2
#    / \
#   1   3

# Input: [2,1,3]
# Output: true
# Example 2:

#     5
#    / \
#   1   4
#      / \
#     3   6

# Input: [5,1,4,null,null,3,6]
# Output: false
# Explanation: The root node's value is 5 but its right child's value is 4.

# ============================================================================

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def isValidBST(self, root: TreeNode) -> bool:
        """
        :type root: TreeNode
        :rtype: bool
        """
        stack, prev = [], float('-inf')
        while stack or root:
            while root:
                stack.append(root)
                root = root.left
            root = stack.pop()
            # If next element in inorder traversal
            # is smaller than the previous one
            # that's not BST.
            if root.val <= prev:
                return False
            prev = root.val
            root = root.right

        return True

if __name__ == '__main__':
    solution = Solution()
    root = TreeNode(2)  
    root.left = TreeNode(1)  
    root.right = TreeNode(3)  
    # root = TreeNode(5)  
    # root.left = TreeNode(3)  
    # root.right = TreeNode(7)  
    # root.left.left = TreeNode(1)
    # root.left.right = TreeNode(4)
    # root.right.left = TreeNode(6)  
    # root.right.right = TreeNode(9)  


    if (solution.isValidBST(root) == True): 
        print("Is valid BST") 
    else: 
        print("Not a BST")

# ==============================================================
# NEED TO REVISIT THIS PORTION AND UNDERSTAND THE RECURSIVE FUNCTION.
# class Solution:
#     # sortArray = []
#     def isValidBST(self, root: TreeNode) -> bool:
#         print(f"first root value: {root.val}")
#         global sortArray
#         sortArray = []
#         if root.left:
#             print(f"left going: {root.val}")
#             self.isValidBST(root.left)
#         print(f"ROOT: {root.val}")
#         sortArray.append(root.val)
#         # print(f"sorted after left: {sortArray}")
#         if root.right:
#             print(f"right going: {root.val}")
#             self.isValidBST(root.right)
#         # if root.left == None and root.right == None:
#         #     print(f"sorted at last: {sortArray}")
#         return sortArray
    

# if __name__ == '__main__':
#     solution = Solution()
#     # root = TreeNode(2)  
#     # root.left = TreeNode(1)  
#     # root.right = TreeNode(3)  
#     root = TreeNode(5)  
#     root.left = TreeNode(3)  
#     root.right = TreeNode(7)  
#     root.left.left = TreeNode(1)
#     root.left.right = TreeNode(4)
#     root.right.left = TreeNode(6)  
#     root.right.right = TreeNode(9)  

#     resArray = solution.isValidBST(root)
#     print(f"REsult Array: {resArray}")
#     sArray = resArray.sort()
#     if sArray == resArray:
#         print("Is valid BST") 
#     else: 
#         print("Not a BST")




