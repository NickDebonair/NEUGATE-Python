# 問題2.
# for 文のネスト
# プログラミングでは、for 文を二重にして使うことがよくあります。しっかり理解しましょう。
#
# 二重for ループを用いて以下の出力を行ってください。（5 行10 列の*を出力）
# ヒント：改行なし出力の例「 print('*',end='') 」
#
# 実行例
# **********
# **********
# **********
# **********
# **********
for i in range(5):
    print('')
    for j in range(10):
        print('*', end='')