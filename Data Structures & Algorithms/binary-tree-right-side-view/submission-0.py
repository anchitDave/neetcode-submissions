# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        ans = []
        q = collections.deque()
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
                ans.append(level[-1])
        
        return ans

                    
        