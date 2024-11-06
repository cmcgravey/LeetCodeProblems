class Solution(object):
    def equalPairs(self, grid):
        hashMapRows = {}
        hashMapCols = {}
        numPairs = 0

        for index, list in enumerate(grid):
            hashMapRows[index] = list
            for index, i in enumerate(list):
                if index in hashMapCols:
                    hashMapCols[index].append(i)
                else:
                    hashMapCols[index] = [i]
        
        for index, row in enumerate(hashMapRows.values()):
            for index, col in enumerate(hashMapCols.values()):
                if row == col:
                    numPairs += 1

        return numPairs


                

def main():
    s = Solution()

    input = [[3, 2, 1], [1, 7, 6], [2, 7, 7]]
    output = s.equalPairs(input)
    assert(output == 1)

    input = ([3, 1, 2, 2], [1, 4, 4, 5], [2, 4, 2, 2], [2, 4, 2, 2])
    output = s.equalPairs(input)
    assert(output == 3)

if __name__ == "__main__":
    main()