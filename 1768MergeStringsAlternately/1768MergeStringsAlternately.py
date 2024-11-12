class Solution(object):
    def mergeAlternately(self, word1, word2):
        res =  ''

        for i in range(0, max(len(word1), len(word2))):
            if i < len(word1):
                res += word1[i]
            if i < len(word2):
                res += word2[i]
        
        return res
    
def main():
    s = Solution()

    word1 = "abc"
    word2 = "pqr"

    output = s.mergeAlternately(word1, word2)
    assert(output == "apbqcr")

if __name__ == "__main__":
    main()
