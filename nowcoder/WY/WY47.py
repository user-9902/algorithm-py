"""
@title:      WY47 安置路灯
@difficulty: 简单
@importance: 4/5
@tags:       greedy
"""
n = int(input())

for i in range(n):
    m = int(input())
    s = input()
    s_n = len(s)
    cnt = {}
    ans = 0
    for i, v in enumerate(s):
        if v == ".":
            if i in cnt or (i - 1) in cnt:
                # 有路灯照着
                continue
            elif i < s_n - 1:
                # i没路灯照，把路灯放下 i+1 贪心的体现
                cnt[i + 1] = True
            else:
                cnt[i] = True
            ans += 1
    print(ans)
