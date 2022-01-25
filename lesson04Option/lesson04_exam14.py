# 問題14.（オプション問題）
# 繰り返し文を使用したアルゴリズムを考える_2
# ① 5 億以下の数で、もっとも大きな素数を出力して下さい。
# ② 5 億以上の数で、もっとも小さな素数を出力して下さい。
#
# 実行例
#
# 5 億以下の数で、もっとも大きな素数は、499999993 です。
# 5 億以上の数で、もっとも小さな素数は、500000003 です。
num_max = 0
num_min = 14
prime = False
while prime == False:
    if num_min % 2 == 0:
        prime = False
        num_min += 1
        break
    for i in range(num_min-1):
        if i != 0 and i != 1:
            if num_min % i == 0:
                prime = False
                num_min += 1
                break
                # print(i)
            else:
                prime = True


print('5 億以下の数で、もっとも大きな素数は、{} です。'.format(num_min))
