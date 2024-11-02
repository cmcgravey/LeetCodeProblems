class Solution(object):
    def asteroidCollision(self, asteroids):
        stack = []

        for asteroid in asteroids: 
            while stack and asteroid < 0 < stack[-1]:
                if stack[-1] < -asteroid:
                    stack.pop()
                    continue
                elif stack[-1] == -asteroid:
                    stack.pop()
                break
            else:
                stack.append(asteroid)
        
        return stack

def main():
    input = []
    s = Solution()
    output = s.asteroidCollision(input)
    print(output)

if __name__ == "__main__":
    main()