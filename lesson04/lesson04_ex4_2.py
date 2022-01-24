count = 0
print('カレーを召し上がれ')
print('{}皿のカレーを食べました'.format(count))
okawari = 'y'
while okawari == 'y':
    count += 1
    okawari = input('おかわりはいかがですか？(y/n) ??')
    print('{}皿のカレーを食べました'.format(count))
print('ごちそうさまでした。')