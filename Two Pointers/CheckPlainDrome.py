def isPlainDrome(s):
    new_str = ""
    s = s.lower()
    for ele in s:
        if ord(ele) >= 97 and ord(ele) <= 122:
            new_str += ele
    if len(new_str) == 1:
        return False
    return new_str == new_str[::-1]

s = "0P"
print(isPlainDrome(s))
# print(ord('0'))