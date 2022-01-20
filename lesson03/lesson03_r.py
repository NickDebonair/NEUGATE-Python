isError = False
n = 100
text = input('数値を入力してください>>')
if not(text.isdecimal()):
    isError = True # isErrorがTrueということはErrorということ
else:
    text = int(text)
    isError = False
#テキストの条件で分岐を行い、条件合致の場合には、
#「システム正常稼働中です。正常範囲数値の入力を確認しました。」を出力
if isError is False and n < 100:
    print('ほにゃらら/システム正常稼働中です。正常範囲数値の入力を確認しました。')
elif isError and n < 100:
    print('エラーが起こりました。nはあっています。')
elif (not isError) and n >= 100:
    print('エラーは起きていません。nが間違っています。')
elif isError and n >= 100:
    print('エラーが起こっており、nも間違っています。')

# value = int(input('数値を入力>>'))
# if value % 2 == 0:
#     print('偶数を入力しました')
# else:
#     print('奇数を入力しました')

# greeting = input('挨拶をどうぞ')
# if greeting == 'こんにちは':
#     print('ようこそ！')
# elif greeting == '景気は？':
#     print('ぼちぼちです')
# elif greeting == 'さようなら':
#     print('お元気で')

greeting2 = ''
# while greeting2 != 'こんにちは' and greeting2 != '景気は？' and greeting2 !='さようなら':　#←うまくいく！！
while not(greeting2 in ['こんにちは', '景気は？', 'さようなら']): #inで指定したリストで候補を与えると、'または'を否定して'かつ'が与えられるみたい
    # while greeting2 != ['こんにちは', '景気は？', 'さようなら']だと永遠にループする
    # while greeting2 != 'こんにちは' and '景気は？' and 'さようなら'　だと、'さようなら'などがうまく終わらない
    greeting2 = input('こんにちは、景気は？、さようなら、から挨拶を入力してください')
    if greeting2 == 'こんにちは':
        print('ようこそ！')
    elif greeting2 == '景気は？':
        print('ぼちぼちです')
    elif greeting2 == 'さようなら':
        print('お元気で')
