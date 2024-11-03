class Solution(object):
    def uniqueOccurences(self, arr):
        hashMap1 = {}
        hashMap2 = {}

        for i in arr:
            if i in hashMap1: hashMap1[i] += 1
            else: hashMap1[i] = 1
        
        for numOccurences in hashMap1.values():
            if numOccurences in hashMap2: hashMap2[numOccurences] += 1
            else: hashMap2[numOccurences] = 1

        return len(hashMap1.values()) == len(hashMap2.values())
    
def main():
    s = Solution()

    input = [1, 2]
    output = s.uniqueOccurences(input)
    print(output)

if __name__ == "__main__":
    main()