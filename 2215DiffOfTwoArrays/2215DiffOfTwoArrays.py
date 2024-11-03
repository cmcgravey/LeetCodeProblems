class Solution(object):
    def findDifference(self, nums1, nums2):
        list1 = []
        list2 = []

        for i in nums1:
            if i not in nums2 and i not in list1:
                list1.append(i)
        
        for j in nums2: 
            if j not in nums1 and j not in list2:
                list2.append(j)
        
        return [list1, list2]

def main():
    s = Solution()
    nums1 = [1, 2, 3]
    nums2 = [2, 4, 6]

    output = s.findDifference(nums1, nums2)
    print(output)

if __name__ == "__main__":
    main()
