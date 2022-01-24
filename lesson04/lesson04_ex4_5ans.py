temp = [7.8, 9.1, 10.2, 11.0, 12.5, 12.4, 14.3, 13.8, 12.9, 12.4]
temp_new = list()
for i in temp:
    temp_new.append(i)
temp_new[5]='N/A'
for i in temp:
    print(str(i)+'\t', end='')
print('')
for i in temp_new:
    print(str(i)+'\t', end='')
print('')

sum = 0
count = 0
for i in temp_new:
    if isinstance(i, float):
        sum += i
        count += 1
print('平均気温:' + str(sum/count))


print('')

temp = list()
for i in range(10):
    temp.append(float(input(str(i+8)+'時の気温を入力>>')))

count = 0
for j in temp:
    print(str(count+8) + '時、' + str(j) + '度')
    count += 1