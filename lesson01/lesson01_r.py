height = int(input("身長(cm)を入力してください"))
weight = float(input("体重(kg)を入力してください？"))
height /= 100
bmi = weight / height / height
print("あなたのBMIは" + str(bmi) + "です。")
# 小数点以下の桁数の指定、および、.を含めた全桁数の指定
# formatを用いた場合
print("あなたのBMIは{:.1f}です。".format(bmi))
print("あなたのBMIは{:.2f}です。".format(bmi))
print("あなたのBMIは{:3.1f}です。".format(bmi))
print("あなたのBMIは{:10.1f}です。".format(bmi))
print("あなたのBMIは{:010.1f}です。".format(bmi))
print("あなたのBMIは{:20.1f}です。".format(bmi))
# f stringを用いた場合
print(f"あなたのBMIは{bmi:.1f}です。") # 以下formatと同様
# round関数を用いた場合
print("あなたのBMIは" + str(round(bmi, 1)) + "です。")
print("あなたのBMIは" + str(round(bmi, 3)) + "です。")
print("あなたのBMIは" + str(round(bmi, 4)) + "です。")
