# 問題3.
# for 文のネスト_2
# ループカウンタを効果的に活用することによって、多彩な処理を行うことができます。しっかり理解しましょう。
#
# 二重for ループを用いて以下の出力を行ってください。
#
# 実行例
#
# *
# **
# ***
# ****
# *****

for i in range(5):
    for j in range(1):
        print('*'*(i+1))

for i in range(5):
    print('*' * (i+1))