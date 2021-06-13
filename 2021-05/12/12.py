# https://leetcode.com/explore/challenge/card/may-leetcoding-challenge-2021/599/week-2-may-8th-may-14th/3742/

# Flatten Binary Tree to Linked List

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def flatten(self, root: TreeNode) -> None:
        """
        Do not return anything, modify root in-place instead.
        """
        # if root is null
        if root is None:
            return
        
        # if root does not have children
        if root.right is None and root.left is None:
            return root
        
        # both children are not null
        if root.right is not None and root.left is not None:
            current_node = root.left
            while current_node.right is not None:
                current_node = current_node.right
                
            current_node.right = root.right
            root.right = root.left
            root.left = None
            self.flatten(root.right)
            
        # for left child only
        if root.left is not None:
            root.right = root.left
            root.left = None
            self.flatten(root.right)  
            
        # for right child only
        if root.right is not None:
            self.flatten(root.right)          


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def __init__(self):
        self.prev = None

    
    def flatten(self, root: TreeNode) -> None:
        """
        Do not return anything, modify root in-place instead.
        """
        if not root: return
        self.flatten(root.right)
        self.flatten(root.left)
        root.right = self.prev
        root.left = None
        self.prev = root   