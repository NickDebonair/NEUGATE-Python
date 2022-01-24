import copy
temp = [7.8, 9.1, 10.2, 11.0, 12.5, 12.4, 14.3, 13.8, 12.9, 12.4]
for i in temp:
    print(i)
print('*' * 10)
temp_old = temp
print(temp_old)
temp_new = copy.copy(temp)

temp_new[5] = 'N/A'
print(temp_old)

for (i, j) in zip(temp_old, temp_new):
    print(i)
    print(j)
print('*' * 10)
print(temp_old)
print(temp_new)

sum_temp = 0
for i in temp_new:
    if not isinstance(i, float):
        continue
    sum_temp += i
    print('*' * 10)
    print(i)
    print(sum_temp)
print(sum_temp)
avg_temp = sum_temp / (len(temp_new) - 1)
print(avg_temp)