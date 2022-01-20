print(1)
print(10)
print(1+1)
print(10-2)
print('1')
print('1' + '1')
print('Hello, \nWorld')
print('Hello, \\World') #エスケープシーケンス
print('Hello, \'World') #エスケープシーケンス
print('Hello, \"World') #エスケープシーケンス

name = '松田' # nameという箱に文字列「松田」を格納
age = 22 # ageという箱に数値2「22」を格納
print(name) # nameという箱の中身を出力
print(age) # ageという箱の中身を出力

# プログラミング用語では「箱に格納」することを「変数に代入」という。
# 代入には代入演算子である「=」を使う。

# japan = 100000000
# global = 7000000000
# print(japan)
# print(global)

age = 24
print(age)
age += 1
print(age)
age += 1
print(age)
age += 1
print(age)

# name = input('あなたの名前を入力してください >>')
# print('おお' + name + 'よ、待ってたぞい！！')

print(type(age))
print(type(name))

x = 3.14
y = int(x) # float型の値をint型に変換
print(y) #小数点以下が切り捨てられて3と出力される

z = str(x) #str型への変換
print(z)
print(type(z))

weight = int(input("あなたの体重は？"))
height = int(input("あなたの身長は？"))
height_m = height / 100
BMI = weight / height_m / height_m
print("あなたのBMIは" + str(BMI) + "です。")

