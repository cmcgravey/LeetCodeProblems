class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution(object):
    def maxLevelSum(self, root):
        lvlSums = []

        deque = []
        deque.append(root)

        while deque != []:
            lvlSum = 0
            for _ in range(0, len(deque)):
                node = deque.pop(0)  
                lvlSum += node.val

                if node.left:
                    deque.append(node.left)
                if node.right:
                    deque.append(node.right)

            lvlSums.append(lvlSum)
        
        return lvlSums.index(max(lvlSums)) + 1



def main():
    s = Solution()

    leaf1 = TreeNode(7)
    leaf2 = TreeNode(-8)
    leaf3 = TreeNode()

    branch1 = TreeNode(7, leaf1, leaf2)
    root = TreeNode(1, branch1, leaf3)

    output = s.maxLevelSum(root)
    assert(output == 2)

if __name__ == "__main__":
    main()
