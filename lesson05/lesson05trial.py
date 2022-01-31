def plus_and_minus(a, b):
    return a + b, a - b
next, prev = plus_and_minus(1990, 1)
print(next, prev)

def eat(**kwargs):
    for k, v in kwargs.items():
        print('{}に{}を食べました'.format(k, v))
eat(朝食='納豆', 遅めの昼食='パスタ', 夕方のおやつ='カレーパン')

def eat2(**kwargs):
    for k in kwargs:
        print('{}に{}を食べました'.format(k, kwargs[k]))
eat2(朝食='納豆', 遅めの昼食='パスタ', 夕方のおやつ='カレーパン')


def eat3(breakfast, lunch, dinner, *args):
    print('朝は{}を食べました'.format(breakfast))
    print('昼は{}を食べました'.format(lunch))
    print('晩は{}を食べました'.format(dinner))
    for d in args:
        print('おやつに{}を食べました'.format(d))
eat3('トースト', 'パスタ', 'カレー', 'アイス', 'チョコ', 'カレー')

def input_scores(name):
    print('{}さんの試験結果を入力してください'.format(name))
    network = int(input('ネットワークの得点？ >>'))
    database = int(input('データベースの得点？ >>'))
    security = int(input('セキュリティの得点？ >>'))
    scores = [network, database, security]
    return scores

def calc_average(scores):
    average = sum(scores) / len(scores)
    return average

def output_result(name, average):
    print('{}さんの平均点は{}です。'.format(name, average))



asagi_scores = input_scores('浅木')
matsuda_scores = input_scores('松田')

asagi_avg = calc_average(asagi_scores)
matsuda_avg = calc_average(matsuda_scores)

output_result('浅木', asagi_avg)
output_result('松田', matsuda_avg)