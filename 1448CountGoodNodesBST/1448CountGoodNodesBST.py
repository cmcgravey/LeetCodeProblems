class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution(object):
    def goodNodes(self, root):
        
        def checkPath(root, path):
            if not root:
                return 0
            if root:
                path.append(root.val)
                val = 0
                if max(path) == root.val:
                    val =  1 + checkPath(root.left, path) + checkPath(root.right, path)
                else:
                    val =  checkPath(root.left, path) + checkPath(root.right, path)
                path.pop(-1)
                return val

        
        return checkPath(root, [])
    
def main():
    s = Solution()

    leaf1 = TreeNode(3)
    leaf2 = TreeNode(1)
    leaf3 = TreeNode(5)

    branch1 = TreeNode(1, leaf1)
    branch2 = TreeNode(4, leaf2, leaf3)

    root = TreeNode(3, branch1, branch2)

    output = s.goodNodes(root)
    assert(output == 4)

if __name__ == "__main__":
    main()