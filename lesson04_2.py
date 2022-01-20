'''
生徒の人数を入力
人数分の繰り返し
    点数入力
平均点を表示
人数分繰り返し
「一人目：70点：合格」
「二人目：50点：不合格」
・・・
'''

count = 0
student_num = int(input('学生の数を入力 >>'))
score_list = list()
while count < student_num:
    count += 1
    score = int(input('{}人目の試験の得点を入力 >>'.format(count)))
    score_list.append(score)
    # score_list.append(int(input('{}人目の点数を入力>>'.format(count))))
print(score_list)
# avg = sum(score_list) / len(score_list); print(avg)　でも可能
total = sum(score_list)
print('平均点は{:.1f}点です。'.format(total / student_num))

count = 1
while count < len(score_list):
    if score_list[count] >= 60:
        print('{}人目：{}点：合格'.format(count, score_list[count-1]))
    else:
        print('{}人目：{}点：不合格'.format(count, score_list[count-1]))
    count += 1