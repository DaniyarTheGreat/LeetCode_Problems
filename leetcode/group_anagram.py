def groupAnagrams(strs: list[str]) -> list[list[str]]:
    res = []
    i=0
    while i < len(strs):
        j = i+1
        local = []
        if strs[i] == None:
            i+= 1
            continue
        while j < len(strs):
            if strs[j] == None:
                j+=1
                continue
            if isAnagram(strs[i], strs[j]):
                if strs[i] not in local:
                    local.append(strs[i])
                local.append(strs[j])
                strs[j] = None
            j += 1
        if local:
            res.append(local)
        else:
            res.append([strs[i]])
        i+=1
    return res

def isAnagram(s: str, t: str) -> bool:
    dic = {}
    for char in s:
        if char in dic:
            dic[char] += 1
        else:
            dic[char] = 1

    for char in t:
        if char in dic:
            dic[char] -= 1
        else:
            dic[char] = 1
    
    for key, val in dic.items():
        if val != 0:
            return False
    return True

strs = ["act","pots","tops","cat","stop","hat"]
print(groupAnagrams(strs))


# Optimized O(nlgn)

def group(strs):
    anagrams = {}
    for s in strs:
        key = ''.join(sorted(s))
        if key not in anagrams:
            anagrams[key] = []
        anagrams[key].append(s)
    return list(anagrams.values())