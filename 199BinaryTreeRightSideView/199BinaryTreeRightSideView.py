class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution(object):
    def rightSideView(self, root):
        if not root: 
            return []
        deque = []
        ans = []
        deque.append(root)

        while (deque != []):
            ans.append(deque[-1].val)
            for _ in range (0, len(deque)):
                node = deque.pop(0)
                if node.left:
                    deque.append(node.left)
                if node.right: 
                    deque.append(node.right)
        
        return ans

def main():
    s = Solution()

    leaf1 = TreeNode(5)
    leaf2 = TreeNode(4)

    branch1 = TreeNode(2, None, leaf1)
    branch2 = TreeNode(3, None, leaf2)

    root = TreeNode(1, branch1, branch2)

    output = s.rightSideView(root)
    assert(output == [1, 3, 4])

if __name__ == "__main__":
    main()