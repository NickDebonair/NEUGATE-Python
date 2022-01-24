count = 1
print('カレーを召し上がれ')

ans = 'y'

while ans == 'y':
    print(str(count) + '皿のカレーを食べました')
    ans = input('おかわりいかがですか？(y/n)>>')
    if nas == 'y':
        count += 1
