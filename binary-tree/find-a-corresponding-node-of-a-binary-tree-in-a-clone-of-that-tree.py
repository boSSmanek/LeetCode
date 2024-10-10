# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def getTargetCopy(self, original, cloned, target):
        """
        :type original: TreeNode
        :type cloned: TreeNode
        :type target: TreeNode
        :rtype: TreeNode
        """
        if not original:
            ## base case or stop condition:
            # empty node or empty tree
            return None
        
        ## general cases:
        if original is target:
            
            # current original node is target, so is cloned
            return cloned
        
        # either left subtree has target or right subtree has target
        return self.getTargetCopy(original.left, cloned.left, target) or self.getTargetCopy(original.right, cloned.right, target)