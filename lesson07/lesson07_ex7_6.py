import random

print('数当てゲームを始めます。３桁の数を当ててください！')
answer = list()
for i in range(3):
    answer.append(random.randint(0, 9))

while True:
    prediction = list()
    for i in range(3):
        prediction.append(int(input('{}桁の予想を入力(0~9) >>'.format(i+1))))
    hit_num = 0
    ball_num = 0

    for i in range(3):
        if answer[i] == prediction[i]:
            hit_num += 1
    '''
    if answer[0] == prediction[1]:
        ball_num += 1
    if answer[0] == prediction[2]:
        ball_num += 1
    if answer[1] == prediction[0]:
        ball_num += 1
    if answer[1] == prediction[2]:
        ball_num += 1
    if answer[2] == prediction[0]:
        ball_num += 1
    if answer[2] == prediction[1]:
        ball_num += 1
    '''
    if answer[0] in prediction and answer[0] != prediction[0]:
        ball_num += 1
    elif answer[1] in prediction and answer[1] != prediction[1]:
        ball_num += 1
    elif answer[2] in prediction and answer[2] != prediction[2]:
        ball_num += 1

    print('{}ヒット！{}ボール！'.format(hit_num, ball_num))

    if hit_num == 3:
        print('正解です！')
        break
    else:
        will = int(input('続けますか？1:続ける 2:終了 >>'))
        if will == 1:
            continue
        elif will == 2:
            break

print('{}{}{}'.format(answer[0], answer[1], answer[2]))