# score_la = int(input('国語の点数は？'))
# score_ma = int(input('算数の点数は？'))
# score_sc = int(input('理科の点数は？'))
# score_so = int(input('社会の点数は？'))
# score_en = int(input('英語の点数は？'))
# タプルを使う場合、またはリストが良い
# score = (score_la, score_ma, score_sc, score_so, score_en)
# total_score = sum(score)
# avg = total_score / len(score)
# print('合計点：' + str(total_score) + '\n平均点：' + str(avg))

# dictionaryを使う場合
# d = dict(国語=score_la, 算数=score_ma, 理科=score_sc, 社会=score_so, 英語=score_en)
# print(d)
# score_dict = sum(d.values())
# avg_dict = score_dict / len(d)
# print("合計点：" + str(score_dict) + "\n平均点：" + str(avg_dict))

print('国語、算数、理科、社会、英語の点数を順に入力してください')
japanese, math, science, social, english = map(int, input().split()) #数値の入力はスペースで区切る
dic = dict(国語=japanese, 算数=math, 理科=science, 社会=social, 英語=english)
print(dic)