"""
@title:      HJ19 简单错误记录
@difficulty: 简单
@importance: 3/5
@tags:       业务分析题
"""

maps = {}
while True:
    try:
        s = input()
        path, line = s.split(" ")
        path = path.split("\\")[-1][-16:]
        k = path + " " + line
        if k in maps:
            maps[k] += 1
        else:
            maps[k] = 1
    except:
        break

# 💲打印dic指定位置元素的技巧
for k in list(maps.keys())[-8:]:
    print("{} {}".format(k, maps[k]))
