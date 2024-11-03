class Solution(object):
    def removeStars(self, s):
        string = ''

        for i in range(0, len(s)):
            if (s[i] != '*'):
                string += s[i]
            else:
                string.pop()
        
        return string

def main():
    input = ""
    s = Solution()
    output = s.removeStars(input)
    print(output)

if __name__ == "__main__":
    main()