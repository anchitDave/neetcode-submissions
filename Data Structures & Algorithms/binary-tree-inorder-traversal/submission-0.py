# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        return self.inorder(root, [])

    def inorder(self, head, ans):
        if not head:
            return ans
        
        self.inorder(head.left, ans)
        ans.append(head.val)
        self.inorder(head.right, ans)

        return ans
        