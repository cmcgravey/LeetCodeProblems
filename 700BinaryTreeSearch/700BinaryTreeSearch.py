class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution(object):
    def printTree(self, root):
        if root:
            self.printTree(root.left)
            print(root.val)
            self.printTree(root.right)

    def searchBST(self, root, val):
        if not root:
            return None
        if val < root.val:
            root = self.searchBST(root.left, val)
            return root
        if val > root.val:
            root = self.searchBST(root.right, val)
            return root
        else:
            return root

def main():
    val = 2

    leaf1 = TreeNode(1)
    leaf2 = TreeNode(3)
    leaf3 = TreeNode(7)
    branch1 = TreeNode(2, leaf1, leaf2)
    root = TreeNode(4, branch1, leaf3)

    s = Solution()
    output = s.searchBST(root, val)
    s.printTree(output)

if __name__ == "__main__":
    main()