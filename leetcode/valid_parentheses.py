def isVald(s):
    stack = []
    opr = {'}':'{',')':'(',']':'['}
    for char in s:
        if char in opr:
            if stack and stack[-1] == opr[char]:
                stack.pop()
            else:
                return False
        else:
            stack.append(char)
    
    return True if not stack else False