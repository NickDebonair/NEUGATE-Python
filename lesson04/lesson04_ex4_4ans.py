for i in range(9):
    print(str(i+1) + 'の段')
    if ( i + 1 ) % 2 != 0:
        for j in range(9):
            print('{} * {} = {}'.format(i+1, j+1, (i+1)*(j+1)))

for i in range(9):
    print(str(i+1) + 'の段')
    if ( i + 1 ) % 2 == 0:
        continue
    for j in range(9):
        ans = (i+1)*(j+1)
        if ans > 50:
            break
        print('{} * {} = {}'.format(i+1, j+1, ans))