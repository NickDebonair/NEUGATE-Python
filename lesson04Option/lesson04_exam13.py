# 問題13.（オプション問題）
# for文の応用（番外編）
#  for文を入れ子にせずに以下のような出力をしてください。
# 　実行例
# 0 = 0
# 0+1 = 1
# 0+1+2 = 3 # 3行目は2行目に2を足している
# 0+1+2+3 = 6 # 4行目は3行目に3を足している
# 0+1+2+3+4 = 10
# 0+1+2+3+4+5 = 15
# 0+1+2+3+4+5+6 = 21
# 0+1+2+3+4+5+6+7 = 28
# 0+1+2+3+4+5+6+7+8 = 36
# 0+1+2+3+4+5+6+7+8+9 = 45
# 0+1+2+3+4+5+6+7+8+9+10 = 55
sum_list = list()
msg = ''
msg3 = ''
total = 0
# for i in range(11):
#
#     count = 0
    # if i == 0:
    #     msg = str(sum_list[i])
    # else:
    # msg = str(sum_list[0])
    # msg2 = str(sum_list[i])
    # msg3 = str(sum_list[i+1])
    # print(msg2)
for i in range(11):
    sum_list.append(i)
    total = sum(sum_list)
    if i == 0:
        msg = str(sum_list[i])
        print(msg + '=' + str(total))
    else:
        msg += '+' + str(sum_list[i])
        print(msg + '=' + str(total))
        # print(str(sum_list[0]), end='')
        # print('+' + str(sum_list), end='')

# for j in range(11)
#         # print(str(j), end='')
#         # print('+', end='')
#         # print('=', end='')
#     print(' = ' + str(total), end='')
#     print()