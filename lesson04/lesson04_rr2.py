# 問題2.
# while 文での繰り返しを正しく使えるようになりましょう。
# 採点結果に80 以上の数値が入力されるまで、繰り返し入力を受け続けるプログラムを作成してください。
#
# 実行例
#
# 採点結果を数値で入力してください。>>50
# 採点結果を数値で入力してください。>>60
# 採点結果を数値で入力してください。>>80
# 合格おめでとうございます！

score = 0
while score < 80:
    score = int(input('採点結果を数値で入力してください。>>'))
print('合格おめでとうございます！')