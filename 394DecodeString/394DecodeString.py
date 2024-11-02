def solution(s):
    stack = []

    for char in s: 
        if char == ']':
            tmp = ''
            while stack[-1] != '[':
                tmp = stack[-1] + tmp
                stack.pop()
            stack.pop()
            num = ''
            while stack and stack[-1].isdigit():
                num = stack[-1] + num
                stack.pop()
            stack.append(int(num) * tmp)

        else:
            stack.append(char)
    
    return ''.join(stack)

def main():
    input = "3[z]2[2[y]pq4[2[jk]e1[f]]]ef"
    output = solution(input)
    print(output)

if __name__ == "__main__":
    main()