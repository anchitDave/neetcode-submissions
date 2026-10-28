# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        q = collections.deque()
        ans = []
        q.append(root)

        while q:
            level = []
            for i in range(len(q)):
                head = q.popleft()
                if head:
                    q.append(head.left)
                    q.append(head.right)
                    level.append(head.val)
            
            if level:
                ans.append(level)
        
        return ans






            

        