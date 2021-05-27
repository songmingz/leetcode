# Runtime: 156 ms, faster than 30.06% of Python3 online submissions for First Unique Character in a String.
# Memory Usage: 14.6 MB, less than 7.87% of Python3 online submissions for First Unique Character in a String.

def firstUniqChar(s: str) -> int:
    repeat = dict()
    for i in range(len(s)):
        if s[i] in repeat.keys() and repeat[s[i]] == False:
            continue

        if i == len(s) - 1 and not(s[i] in repeat.keys()):
            return i

        for j in range(i + 1, len(s)):
            if s[j] == s[i]:
                repeat[s[i]] = False
                break
            if j == len(s) - 1:
                return i
    return -1

s = 'bba'

print(firstUniqChar(s))