qq = []
j = 1
for i in range(1, 10):
    qq.append(i * j)
    print('***' * 10)
    print(qq)
    qq1 = []
    for j in range(2, 10):
        qq1.append(i*j)
        print('*'*10)
        print(qq1)
        print(i * j)
