# 問題7.
# for 文のネストと条件分岐の組み合わせ_3
# white = '□'
# black = '■'
# 上記二つの変数を用いて、タテ縞模様を出力してください。
#
# 実行例
#
# 表示したいタテ縞模様の一辺の大きさを入力してください。
# >>8
# ■□■□■□■□
# ■□■□■□■□
# ■□■□■□■□
# ■□■□■□■□
# ■□■□■□■□
# ■□■□■□■□
# ■□■□■□■□
# ■□■□■□■□
size = int(input('表示したいタテ縞模様の一辺の大きさを入力してください'))
for i in range(size):
    print('')
    # if size == 1:
    #     for j in range(size):
    #         print('■', end='')
    #         print('□', end='')
    # elif size % 2 != 0 and size >= 3:
    #     for j in range(size):
    #         print('■□', end='')
    # else:
    for j in range(size):
        if j % 2 != 0:
            print('■', end='')
        elif j % 2 == 0:
            print('□', end='')

