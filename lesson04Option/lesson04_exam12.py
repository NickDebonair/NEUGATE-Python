# 問題12.（オプション問題）
# for文のネスト応用_2
#  for文の入れ子を用いて以下のような出力をしてください。
# 　実行例
# 0 = 0　
# 0+1 = 1
# 0+1+2 = 3 三行目は行数3-1の2までの足し算 3行目で3列の数値を出力⇒0,1,2
# 0+1+2+3 = 6
# 0+1+2+3+4 = 10
# 0+1+2+3+4+5 = 15
# 0+1+2+3+4+5+6 = 21 7行目は行数7-1の6までの足し算 7行目で7列の数字を出力⇒0,1,2,3,4,5,6
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
    for j in range(i):
        print( '+' + str(sum_list[count-i]), end='')
        # print(sum_list)
        # print(sum_list[count], end='')
        count += 1
    print(' = ' + str(total), end='')
    print()