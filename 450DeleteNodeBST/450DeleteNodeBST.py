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

    def deleteNode(self, root, key):
        def leftmostOfRight(root):
            if (not root.left):
                return root.val
            else:
                val = leftmostOfRight(root.left)
                return val
        
        def rightmostOfLeft(root):
            if (not root.right):
                return root.val
            else: 
                val = rightmostOfLeft(root.right)
                return val

        if root is None: 
            return root
        if key < root.val:
            root.left  = self.deleteNode(root.left, key)
            return root
        if key > root.val:
            root.right = self.deleteNode(root.right, key)
            return root
        else:
            if (not root.left and not root.right):
                return None
            if (root.left and not root.right):
                root.val = rightmostOfLeft(root.left)
                root.left = self.deleteNode(root.left, root.val)
            if (root.right):
                root.val = leftmostOfRight(root.right)
                root.right = self.deleteNode(root.right, root.val)
            
        return root

def main():
    s = Solution()

    key = 3
    leaf1 = TreeNode(2)
    leaf2 = TreeNode(4)
    leaf3 = TreeNode(7)
    branch1 = TreeNode(3, leaf1, leaf2)
    branch2 = TreeNode(6, None, leaf3)
    root = TreeNode(5, branch1, branch2)
    output = s.deleteNode(root, key)
    s.printTree(output)

if __name__ == "__main__":
    main()