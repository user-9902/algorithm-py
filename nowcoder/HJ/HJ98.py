goods_price = [2, 3, 4, 5, 8, 6]
goods_num = [0, 0, 0, 0, 0, 0]

coins_val = [10, 5, 2, 1]
coins_num = [0, 0, 0, 0]

rest = 0

def q(s):
    arr = s.split()
    if len(arr) != 2 and (arr[1] != '0' or arr[1] != 1):
        print('E010:Parameter error')
    if arr[1] == '0':
        n = len(goods_price)
        for i in range(n):
            print('A{} {} {}'.format(i+1, goods_price[i],  goods_num[i]))
    elif arr[1] == '1':
        n = len(coins_val)
        for i in range(n):
            print('{} yuan coin number={}'.format(coins_val[i],  coins_num[i]))

def p(s):
    
    nonlocal rest
    rest += v

def b(s):

def c(s):
    # 找零钱 多重背包


# s = input().split(';')
# cmd = s[0]
# cmd.split()
# for i,v in enumerate(cmd[1].split('-')):
#     goods_num[i] = int(v)
# for i,v in enumerate(cmd[2].split('-')):
#     coins_num[i] = int(v)

# for i in range(1,len(s)):
#     if s[i][0] == 'p':
#         p(s[i])
#     elif s[i][1] == 'q':
#         q(s[i])
#     elif s[i][1] == 'c':
#         c(s[i])
#     elif s[i][1] == 'b':
#         b(s[i])

    
