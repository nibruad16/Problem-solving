# Problem: Find Largest Value in Each Tree Row - https://leetcode.com/problems/find-largest-value-in-each-tree-row/

class Solution:
    def largestValues(self, root: Optional[TreeNode]) -> List[int]:
        if not root:
            return []
        que = deque()

        ans = []
        que.append(root)

        while que:
            node = que[0].val
            rowMax = que[0].val

            for _ in range(len(que)):
                node = que.popleft()
                rowMax = max(rowMax,node.val)

                if node.left:
                    que.append(node.left)
                if node.right:
                    que.append(node.right)
            ans.append(rowMax)
    
        return ans