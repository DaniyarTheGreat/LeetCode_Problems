def check_plaindrome(s):
    new_s = ''
    for char in s:
        char = char.lower()
        if ord(char) in range(97, 122) or ord(char) in range(48, 57):
            new_s = new_s + char
    
    i, j = 0, len(new_s) - 1
    while i < j:
        if new_s[i] != new_s[j]:
            return False
        i += 1
        j -= 1
    return True

s="0P"
print(check_plaindrome(s))