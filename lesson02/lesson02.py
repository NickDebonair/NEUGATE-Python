# p.81
members = ['工藤', '松田', '浅木'] #リストは[]で囲んで、中に要素をカンマ区切りで列挙する。
print(members)
print(members[0])
print(members[1])
print(members[2])
# print(members[3])

# p.85
scores = [88, 90, 95, 70, 40, 100]
total = sum(scores) # 戻り値を格納する
avg = total / len(scores)
print('合計{}点'.format(total))
print('平均{}点'.format(avg))

# p.87　リストに追加するときは、「append()」、（末尾に追加）
members.append('菅原')
members.append('湊')
members.append('朝香')
members.append('松田')
members.append('松田')
members.append('松田')
print(members)

# p.88 リストからの削除は「remove()」。先頭から検索して、最初の該当要素だけを削除。
members.remove('松田')
print(members)

# p.89
members[5] = '高橋'
print(members)

# p.93
score_dic = {
    'network': 60,
    'database': 80,
    'security': 50,
    'network': 99,
}
print(score_dic)

# p.94
print(score_dic['database'])
score_dic['programming'] = 65
score_dic['security'] = 55
print(score_dic)

# p.97
del score_dic['security']
print(score_dic)

# ディクショナリの使用例
it_words = {'python': 'プログラミング言語です。様々な場面で使われています。',
            'html': 'webページを作成する時に使う言語です。',
            'sql': 'データベース操作の言語です。'}
# word = input('調べたい用語を入力してください')

# print(it_words[word])

word_list = list(it_words)
print(word_list)

