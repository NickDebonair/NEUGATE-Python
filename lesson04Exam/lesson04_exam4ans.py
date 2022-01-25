num = 1
row = 9
for i in range(row):
    for j in range(num):
        print('*', end='')
    if i < row/2-1:
        num += 1
    else:
        num -= 1
    print()