num = int(input('素数判定したい整数を入力してください。\n >>'))
result = '素数です'
for i in range(2, num-1):
    if num % i == 0:
        result = '素数ではありません'
        break
print('{}は、{}'.format(num, result))
