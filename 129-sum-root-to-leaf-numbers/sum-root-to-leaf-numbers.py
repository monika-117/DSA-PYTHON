class Solution:
    def sumNumbers(self, root):
        def dfs(node, path):
            if node is None:
                return 0

            path = path * 10 + node.val

            if node.left is None and node.right is None:
                return path

            return dfs(node.left, path) + dfs(node.right, path)

        return dfs(root, 0)