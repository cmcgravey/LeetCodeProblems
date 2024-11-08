class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution(object):
    def leafSimilar(self, root1, root2):
        
        def leafSequence(root, sequence):
            if not root:
                return None
            if not root.left and not root.right:
                sequence.append(root.val)
            if root:
                leafSequence(root.left, sequence)
                leafSequence(root.right, sequence)
            return sequence

        sequence1 = leafSequence(root1, [])
        sequence2 = leafSequence(root2, [])

        return sequence1 == sequence2
                
    
def main():
    s = Solution()

    leaf1 = TreeNode(2)
    leaf2 = TreeNode(3)

    root1 = TreeNode(1, leaf1, leaf2)

    leaf1 = TreeNode(3)
    leaf2 = TreeNode(2)

    root2 = TreeNode(1, leaf1, leaf2)

    output = s.leafSimilar(root1, root2)
    assert(output == False)

if __name__ == "__main__":
    main()