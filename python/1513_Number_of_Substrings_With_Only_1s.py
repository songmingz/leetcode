#暴力比较,超时
def numSub__(s):
    sum = 0
    substr = ''
    for i in range(1, len(s) + 1):
        substr = substr + '1'
        count = 0
        for j in range(0, len(s) - i + 1):
            temp = s[j:j + i]
            if s[j:j + i] == substr:
                count+=1
        sum = sum + count
        if count == 0:
            break
    return sum

#164ms faster than 5.53% of Python3
#Memory Usage: 14.6 MB, less than 83.89% of Python3

#计算全1字符串有多少全1子串
def count1(s):
    count = 0
    for i in range(1, s + 1):
        count += i
    return count

def numSub(s: str) -> int:
    sum = 0
    len1 = 0
    i = 0
    while i < len(s):
        if s[i] == '1':
            for j in range(0, len(s) - i):
                if s[i + j] == '1' :
                    len1 += 1
                    #当下一个字符为0或到字符串边界时,计算子串长度,退出循环
                    if i + j == len(s) - 1 or s[i + j + 1] == '0':
                        i = i + j + 1
                        sum += count1(len1)
                        len1 = 0
                        break
        i += 1
    return sum % (10**9+7)

s = '111111'
#print(count1(6))
print(numSub(s))
print(numSub('0110111'))