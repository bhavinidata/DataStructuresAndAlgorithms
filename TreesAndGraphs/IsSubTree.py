# Given two non-empty binary trees s and t, check whether tree t has exactly the same structure and node values with a subtree of s. A subtree of s is a tree consists of a node in s and all of this node's descendants. The tree s could also be considered as a subtree of itself.

# Example 1:
# Given tree s:

#      3
#     / \
#    4   5
#   / \
#  1   2
# Given tree t:
#    4 
#   / \
#  1   2
# Return true, because t has the same structure and node values with a subtree of s.
# Example 2:
# Given tree s:

#      3
#     / \
#    4   5
#   / \
#  1   2
#     /
#    0
# Given tree t:
#    4
#   / \
#  1   2
# Return false.

# ==============================================================

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def isSubtree(self, s: TreeNode, t:TreeNode) -> bool:
        # corner cases
        if (s == None and t == None): return True
        if (s == None or t == None): return False

        # Case:1 subtree begins at root level
        if (s.val == t.val):
            if (self.isSameTree(s.left, t.left) and self.isSameTree(s.right, t.right)): return True
        # Case:2 subtree begins at other than root level
        return (self.isSubtree(s.left, t) or self.isSubtree(s.right, t))


    def isSameTree(self, s1:TreeNode, t1:TreeNode):
        # corner cases
        if (s1 == None and t1 == None): return True
        if (s1 == None or t1 == None): return False
        if (s1.val != t1.val): return False
        # recursive calls
        return (self.isSameTree(s1.left, t1.left) and self.isSameTree(s1.right, t1.right))

if __name__ == '__main__':
    solution = Solution()
    sroot = TreeNode(5)  
    sroot.left = TreeNode(3)  
    sroot.right = TreeNode(7)  
    sroot.left.left = TreeNode(1)
    sroot.left.right = TreeNode(4)
    sroot.right.left = TreeNode(6)  
    sroot.right.right = TreeNode(9) 

 
    troot = TreeNode(3)  
    troot.left = TreeNode(1)
    troot.right = TreeNode(5)

    result = solution.isSubtree(sroot, troot)
    if result == True:
        print("it is subtree")
    else:
        print("Not a sub tree")


