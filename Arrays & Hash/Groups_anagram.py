import collections

def groupAnagrams(strs):
    result = collections.defaultdict(list)
    for s in strs:
        count = [0]*26
        for c in s:
            count[ord(c) - ord('a')] += 1
        result[tuple(count)].append(s)
    return result.values()

strs = ["eat","tea","tan","ate","nat","bat"]
print(groupAnagrams(strs))