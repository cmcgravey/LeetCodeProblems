class Solution(object):
    def pivotIndex(self, nums):
        pivotIndex = -1
        leftSum = 0
        rightSum = sum(nums)

        for idx, num in enumerate(nums):
            rightSum -= num
            if leftSum == rightSum:
                pivotIndex = idx
                break
            leftSum += nums[idx]

        return pivotIndex

def main():
    s = Solution()

    nums = [1, 7, 3, 6, 5, 6]
    output = s.pivotIndex(nums)
    assert(output == 3)

    nums = [1, 2, 3]
    output = s.pivotIndex(nums)
    assert(output == -1)

if __name__ == "__main__":
    main()