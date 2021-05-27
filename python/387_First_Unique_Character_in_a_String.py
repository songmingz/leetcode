# Runtime: 156 ms, faster than 30.06% of Python3 online submissions for First Unique Character in a String.
# Memory Usage: 14.6 MB, less than 7.87% of Python3 online submissions for First Unique Character in a String.

def firstUniqChar(s: str) -> int:
    repeat = dict() # 记录已经重复的字符
    for i in range(len(s)):
        #若该字符已经重复,则跳到下一个字符
        if s[i] in repeat.keys() and repeat[s[i]] == False:
            continue
        #处理最后一个字符为非重复字符的特殊情况
        if i == len(s) - 1 and not(s[i] in repeat.keys()):
            return i

        for j in range(i + 1, len(s)):
            #若扫描到重复字符,记录并退出循环
            if s[j] == s[i]:
                repeat[s[i]] = False
                break
            #直到最后一个字符都没有重复,返回位置
            if j == len(s) - 1:
                return i
    return -1

s = 'bba'

print(firstUniqChar(s))