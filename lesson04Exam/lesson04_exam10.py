# 問題10.
# 繰り返し文を使用したアルゴリズムを考える_1
# 素数判定プログラムを作成してください。
#
# 実行例
#
# 素数判定したい整数を入力してください
# >>9999991
# 9999991 は素数です
import math

print('素数判定したい整数を入力してください')
num = int(input('>>'))
msg = '素数です'
if num <= 1:
    msg = '素数ではない'
elif num == 2:
    msg = '素数です'
elif num % 2 == 0:
    msg = '素数ではない'
for i in range(3, math.ceil(math.sqrt(num)) + 1 , 2):
    if num % i == 0:
        msg = '素数ではない'
print('{}は'.format(num) + msg)

print('素数判定したい整数を入力してください')
num = int(input('>>'))
msg = '素数です'
if num <= 1:
    msg = '素数ではない'
elif num == 2:
    msg = '素数です'
elif num % 2 == 0:
    msg = '素数ではない'
for i in range(num-1):
    if i != 0 and i !=1:
        if num % i == 0:
            msg = '素数ではない'
            print(i)
print('{}は'.format(num) + msg)
