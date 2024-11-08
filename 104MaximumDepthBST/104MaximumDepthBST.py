class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution(object):
    def maxDepth(self, root):
        
        def solve(root, lvl):
            if not root:
                return lvl - 1
            if root:
                leftLvl = solve(root.left, lvl + 1)
                rightLvl = solve(root.right, lvl + 1)
            return max(leftLvl, rightLvl)
            
        return solve(root, 1)

    
def main():
    s = Solution()

    leaf1 = TreeNode(15)
    leaf2 = TreeNode(7)
    leaf3 = TreeNode(9)

    branch1 = TreeNode(20, leaf1, leaf2)
    root = TreeNode(3, leaf3, branch1)

    output = s.maxDepth(root)
    assert(output == 3)

if __name__ == "__main__":
    main()