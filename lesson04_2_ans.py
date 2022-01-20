# 人数入力
student_num = int(input('人数を入力>>'))
#空のリストを準備
score_list = list()
#カウンタ変数 （繰り返し回数を管理）
count = 0
#繰り返し（カウンタと生徒人数を比較して条件とする）
while count < student_num:
    #カウンタを増分
    count += 1
    #点数入力
    score_list.append(int(input('{}人目の点数を入力>>'.format(count))))

#平均点算出
avg = sum(score_list) / len(score_list)
print(avg)

#合否判定を人数分繰り返し
count = 0
while count < len(score_list):
    result = '不合格'
    if score_list[count] >= 60:
        result = '合格'
    print('{}人目:{}点:{}'.format(count+1,score_list[count],result))
    count += 1
