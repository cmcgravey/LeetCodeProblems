class Solution(object):
    def closeStrings(self, word1, word2):
        return word1 + word2

def main():
    s = Solution()

    word1 = ""
    word2 = ""
    output = s.closeStrings(word1, word2)
    print(output)

if __name__ == "__main__":
    main()