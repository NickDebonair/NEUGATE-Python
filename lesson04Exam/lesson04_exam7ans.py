white = '□'
black = '■'

num = int(input('表示したい縦縞模様の一片の大きさを入力してください。\n>>'))
for i in range(num):
    for j in range(num):
        if j % 2 == 0:
            print(black, end='')
        else:
            print(white, end='')
    print()