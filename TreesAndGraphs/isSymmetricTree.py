# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def isSymmetric(self, root: TreeNode) -> bool:
        stack = []
        if not root or (not root.left and not root.right):
            return True
        stack.append((root.left, root.right))
        while(len(stack)):
            left, right = stack.pop()
            if not left or not right or (left.val != right.val):
                return False
            # only append if the corresponding pair exists.
            if left.left or right.right:
                stack.append((left.left, right.right))
            if left.right or right.left:
                stack.append((left.right, right.left))
        return True

if __name__ == '__main__':
    solution = Solution()
    # root = TreeNode(1)  
    # root.left = TreeNode(2)  
    # root.right = TreeNode(2)  
    # root.left.left = TreeNode(3)
    # root.left.right = TreeNode(4)
    # root.right.left = TreeNode(4)  
    # root.right.right = TreeNode(3) 

    root = TreeNode(1)  
    root.left = TreeNode(2)  
    root.right = TreeNode(2)  
    root.left.right = TreeNode(4)
    root.right.right = TreeNode(4)


    if (solution.isSymmetric(root) == True): 
        print("Is symmetric binary tree") 
    else: 
        print("Not a symmetric binary tree")

