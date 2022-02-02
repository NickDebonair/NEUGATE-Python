'''
num = [int(x) for x in input().split()]
print(max(num))

num1 = int(input("1番目の数値"))
num2 = int(input("2番目の数値"))
num3 = int(input("3番目の数値"))
num_list = [num1, num2, num3]
print(max(num_list))
'''
max_list = []
for i in range(3):
    num = int(input('{}番目の数を入力してください'.format(i+1)))
    max_list.append(num)
print(max(max_list))