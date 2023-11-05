def valid_brackets(string):
    brackets_map = {"]": "[",
                    "}": "{",
                    ")": "("}
    open_brackets = ["[", "{", "("]
    stack = []
    result = "Success"
    for i, c in enumerate(string):
        #c is a character
            #continue
        if c not in brackets_map and c not in open_brackets:
            continue
        #c is an open bracket
            #append to the stack
        elif c in open_brackets:
            stack.append(c)

        else:
            if stack != []:
                if stack[-1] == brackets_map[c]:
                    stack.pop()
                else:
                    result = i + 1
                    break
            else:
                result = i + 1
                break
    if stack != []: result = i + 1

    return result

if __name__ == "__main__":
    input_string = input()
    print(valid_brackets(input_string))