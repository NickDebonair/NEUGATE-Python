#コレクション点数を格納（sum()関数を使いたい!)
scores = []
#国語の点数を整数で入力させる
japanese = int(input('国語>>'))
#算数の点数を整数で入力させる
math = int(input('算数>>'))
#理科の点数を整数で入力させる
sci = int(input('理科>>'))
#社会の点数を整数で入力させる
social = int(input('社会>>'))
#英語の点数を整数で入力させる
eng = int(input('英語>>'))

#コレクション点数を格納（sum()関数を使いたい！）


#sum()関数を用いて合計点を算出
sum = sum(scores)

#平均点の算出のため、合計点を科目数(コレクションの要素数）で割る
ave = sum/len(scores)

#結果表示
print('合計:{}点、平均:{}点'.format(sum,ave))
