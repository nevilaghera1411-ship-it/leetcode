class Solution(object):
    def maxPathSum(self, root):
      return self.helper(root)[0]

    def helper(self, node):   
        if not node:
            return float('-inf'), 0     

        left_via, left_down = self.helper(node.left)
        right_via, right_down = self.helper(node.right)

        via = max(node.val + max(0, left_down) + max(0, right_down), left_via, right_via)
        down = node.val + max(0, left_down, right_down)

        return via, down