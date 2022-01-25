# 問題8.
# for 文のネストと条件分岐の組み合わせ_4
# white = '□'
# black = '■'
# 上記二つの変数を用いて、チェック模様を出力してください。
#
# 実行例
#
# 表示したいチェック模様の一辺の大きさを入力してください。
# >>8
# □■□■□■□■
# ■□■□■□■□
# □■□■□■□■
# ■□■□■□■□
# □■□■□■□■
# ■□■□■□■□
# □■□■□■□■
# ■□■□■□■□
size = int(input('表示したいヨコ縞模様の一辺の大きさを入力してください'))
for i in range(size):
    print('')
    if i % 2 != 0:
        for j in range(size):
            if j % 2 != 0:
                print('■', end='')
            elif j % 2 == 0:
                print('□', end='')
    else:
        for j in range(size):
            if j % 2 != 0:
                print('□', end='')
            elif j % 2 == 0:
                print('■', end='')