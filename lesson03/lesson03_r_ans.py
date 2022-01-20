isError = False
n = 99

if (not isError) and n < 100:
    print('システム正常稼働中です。正常範囲数値の入力を確認しました。')

num = int(input('整数を入力>>'))
if num % 2 == 0:
    print('偶数')
else:
    print('奇数')

msg = '奇数'
if num % 2 == 0:
    msg = '奇数'
print(msg)

message = input('入力してください')

response = 'どうしました？'
if message == 'こんにちは':
    response = 'ようこそ'
elif message == '景気は？':
    response = 'ぼちぼちです'
elif message == 'さようなら':
    response = 'お元気で'

print(response)