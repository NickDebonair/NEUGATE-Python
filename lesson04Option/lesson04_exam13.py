# 問題13.（オプション問題）
# for文の応用（番外編）
#  for文を入れ子にせずに以下のような出力をしてください。
# 　実行例
# 0 = 0
# 0+1 = 1
# 0+1+2 = 3
# 0+1+2+3 = 6
# 0+1+2+3+4 = 10
# 0+1+2+3+4+5 = 15
# 0+1+2+3+4+5+6 = 21
# 0+1+2+3+4+5+6+7 = 28
# 0+1+2+3+4+5+6+7+8 = 36
# 0+1+2+3+4+5+6+7+8+9 = 45
# 0+1+2+3+4+5+6+7+8+9+10 = 55
sum_list = list()
for i in range(11):
    sum_list.append(i)
    total = sum(sum_list)
    count = 0
    print(str(sum_list[0]), end='')
    print('+' + str(sum_list), end='')

        # print(str(j), end='')
        # print('+', end='')
        # print('=', end='')
    print(' = ' + str(total), end='')
    print()