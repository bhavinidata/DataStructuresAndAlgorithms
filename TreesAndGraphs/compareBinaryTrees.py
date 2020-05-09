# Write an efficient algorithm thats able to compare 
# two binary search trees. The method returns 
# true if the trees are identical (same topology 
# with same values in the nodes) otherwise it returns false.

# =========================================================

class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def compareBinaryTree(self, treeRoot1: TreeNode, treeRoot2: TreeNode) -> bool:
        # if both node are same (even null) then return true 
        if not treeRoot1 or not treeRoot2:
            return treeRoot1 == treeRoot2
        # check the values within the trees
        if treeRoot1.val != treeRoot2.val:
            return False
        return (self.compareBinaryTree(treeRoot1.left, treeRoot2.left) and \
            self.compareBinaryTree(treeRoot1.right, treeRoot2.right))

if __name__ == '__main__':
    solution = Solution()
    root1 = TreeNode(5)  
    root1.left = TreeNode(3)  
    root1.right = TreeNode(7)  
    root1.left.left = TreeNode(1)
    root1.left.right = TreeNode(4)
    root1.right.left = TreeNode(6)  
    root1.right.right = TreeNode(9) 

    root2 = TreeNode(5)  
    root2.left = TreeNode(3)  
    root2.right = TreeNode(7)  
    root2.left.left = TreeNode(1)
    root2.left.right = TreeNode(4)
    root2.right.left = TreeNode(6)  
    root2.right.right = TreeNode(7) 

    result = solution.compareBinaryTree(root1, root2)
    if result == True:
        print("Both trees are same")
    else:
        print("Trees are not same")