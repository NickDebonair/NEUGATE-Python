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
num_min = 500000000

while True:
    is_prime = True
    for i in range(2, num_min - 1):
        if num_min % i == 0:
            result = '素数ではありません'
            is_prime = False
            break
    if is_prime:
        print(num_min)
        break
    else:
        num_min += 1

print('もっとも小さな素数は、{} です。'.format(num_min))
