# 問題16.（オプション問題）
# 多次元コレクション
#
# マインスイーパのマップ準備プログラムを作成してください。
# ユーザーの指定した数値を元にランダムに地雷（ * ）を配置してください。
# 地雷の数の上限は（マスの総数 - 1）としてください。
#
# 実行例
# 一辺のマス数を、2
# 以上かつ26
# 以下の整数で入力してください
# >> 10
# 地雷の数を、99
# 以下の整数で入力してください
# >> 30
#
#  	   a   b   c   d   e   f   g   h   i   j
#    +---+---+---+---+---+---+---+---+---+---+
#  1 |   |   |   |   | * | * | * |   |   |   | # その行の列数以内で＊をランダムに入れる random.randint(0, cr_num)
#    +---+---+---+---+---+---+---+---+---+---+ # ランダムに入れた＊の総数 sum(list) ＝地雷の数 mine_num
#  2 |   | * |   |   | * |   |   |   |   | * |
#    +---+---+---+---+---+---+---+---+---+---+
#  3 | * |   |   |   |   |   |   |   | * | * |
#    +---+---+---+---+---+---+---+---+---+---+
#  4 |   | * |   |   | * |   |   |   |   |   |
#    +---+---+---+---+---+---+---+---+---+---+
#  5 | * | * |   |   |   |   |   |   |   |   |
#    +---+---+---+---+---+---+---+---+---+---+
#  6 | * |   |   |   |   | * | * | * | * | * |
#    +---+---+---+---+---+---+---+---+---+---+
#  7 |   |   | * |   |   |   |   |   |   |   |
#    +---+---+---+---+---+---+---+---+---+---+
#  8 |   |   |   | * |   |   |   |   |   | * |
#    +---+---+---+---+---+---+---+---+---+---+
#  9 | * | * |   | * | * | * | * |   |   | * |
#    +---+---+---+---+---+---+---+---+---+---+
# 10 |   |   |   |   |   | * |   |   |   |   |
#    +---+---+---+---+---+---+---+---+---+---+

'''
cr_num = 10
mine_num = 30
とした場合、例えば
mine_list = [5, 2, 3, 5, 3, 7, 1, 2, 1, 1]
と入ればよい、
random.randint(0, 10)で、cr_numの数で制御
sum(mine_list) == mine_numとなるように制御
最後の行は、mine_list[cr_num] = mine_num - sum(mine_num_temp)　という個数で良い？
でも12個とかになった場合、上手くいかなくなってしまう。
sum(mine_list) == mine_num かつ、mine_list[i] <= cr_num とならなくてはならない。
len(mine_list) == cr_numであれば良い。
while文で無限ループにして、条件がそろえばbreak?
最後の行の*の個数がcr_numより大きくならないように再帰しなくてはならない。
ランダムでint整数を発生させるのはrandom.randint(x, y)しかない
ループさせるごとに、mine_perrowの数を削っていく、mine_numの範囲で
'''

'''
random.randint(0, 1)にして、＊があるなしでリストを作る方法も考えた。
mine_list[cr_num - 1]で区切る、これが1行目
mine_list[2 * cr_num - 1]で区切る、これが2行目
mine_list[3 * cr_num - 1]で区切る。これが3行目

mine_sumを1ずつ要素がcr_num*cr_num個分あるmine_listに対して配るようなプログラムが書ければ解決する
if文で、mine_listの余りの要素個数mine_num - len(mine_list)が、
残りの地雷数、mine_sum - sum(mine_list)と等しくなれば、
全部1を入力するという方法を考えた。足りすぎる場合を除去、足りない場合を除去
⇒間違いだった。これだと全部1が入力される
足りない場合の考察が必要。cr_num = 4, 4*4のマス、mine_sum = 4とした場合、
[0, 0, 0, 0, 1, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0]
こういう時。残りのmine_listの要素個数が、mine_sumの残りより少ない場合なので
cr_num*cr_num - len(mine_list) < mine_sum - sum(mine_list)
でもこれだといつだってそうなので、この条件を満たすまで全部1になってしまう。

足りすぎる場合、
sum(mine_list) == mine_sum　の時、
[1, 1, 1, 0, 1, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0]
それ以降は全部0じゃないといけない
mine_sum = 10
としたら、
'*' * 10を先ずやって、
そこからランダムに取り出すという方法があるかな？ 
'''


import random
cr_num = 4
column_list = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

mine_sum = 10
mine_num_temp = 0
mine_list = []
mine_list.append(random.randint(0, 1))
for i in range(1, cr_num*cr_num):
    # if mine_sum - len(mine_list) == mine_sum - sum(mine_list):
    #     mine_list.append(1)
    if sum(mine_list) >= mine_sum:
        mine_list.append(0)
    if cr_num*cr_num - len(mine_list) > mine_sum - sum(mine_list):
        mine_list.append(1)
    else:
        mine_list.append(random.randint(0, 1))


print(mine_list)








#
# for i in range(cr_num):
#     mine_perrow = random.randint(1, cr_num)
#
#     # for j in range(mine_num):
#
#     if mine_perrow > 1:
#         mine_list.append(random.randint(1, cr_num))
#     else:
#         mine_list.append(random.randint(0, 1))
#     mine_num -= mine_perrow
#
# print(mine_list)

mine_random = random.randint(1, mine_sum)
mine_random2 = random.randint(1, (mine_sum) - (mine_random))
mine_random_last = mine_random
num = 10
for i in range(1, num):
    print('+---' * (num - 1) + '+')
    for j in range(1, num):
        if (i * j) < 10:
            print('| ' + ('*' * 1) + ' ', end='')
            if j == 9:
                print('|', end='')
        elif ( i * j ) >= 10:
            print('| ' + ('*' * 1)  + ' ', end='')
            if j == 9:
                print('|', end='')
    print()
print('+---' * 9 + '+')
