# Problem: Reverse Odd Levels of Binary Tree - https://leetcode.com/problems/reverse-odd-levels-of-binary-tree/description/

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def reverseOddLevels(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        if not root:
            return root
    
        queue = deque([root])
        level = 0
        
        while queue:
            level_size = len(queue)
            
            # If current level is odd, reverse the node values
            if level % 2 == 1:
                # Collect all nodes at current level
                nodes = list(queue)
                # Collect all values
                values = [node.val for node in nodes]
                # Reverse the values
                values.reverse()
                # Assign reversed values back to nodes
                for i in range(len(nodes)):
                    nodes[i].val = values[i]
            
            # Process current level
            for _ in range(level_size):
                node = queue.popleft()
                
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
            
            level += 1
        
        return root






        