count = 0

while count < 30:
    count += 1
    print('ひつじが{}匹'.format(count))

print('おやすみなさい')

i = 1
for i in range(1, 30):
    print('ひつじが{}匹'.format(i))

is_awake = True

while is_awake == True:
    count += 1
    print('ひつじが{}匹・・・'.format(count))
    key = input('もう眠りそうですか？(y/n) >>')
    if key == 'y':
        is_awake = False
print('おやすみなさい・・・')