"""
@title:      HJ23 删除字符串中出现次数最少的字符
@difficulty: 简单
@importance: 3/5
@tags:       业务分析
"""


from collections import Counter

s = input()
cnt = Counter(s)
min_n = min([cnt[i] for i in cnt])

min_key = []
for i in cnt:
    if cnt[i] == min_n:
        min_key.append(i)

ans = ""
for i in s:
    if i in min_key:
        continue
    ans += i
print(ans)
