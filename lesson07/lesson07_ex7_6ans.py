# （1） 画面に「数当てゲームを始めます。3 桁の数を当ててください！」と表示する。
from random import randint

print('数当てゲームを始めます。3 桁の数を当ててください！')

# （2） リストanswer を準備して、
answer = [1, 1, 0]
# 0 ～ 9 のランダムな整数を3 つ格納する。
# for i in range(3):
#     answer.append(randint(0, 9))
# 確認用出力
print(answer)

while True:
    # （3） 画面に「○桁目の予想を入力（0 ～ 9） >>」と3 回表示し、
    #       それぞれ入力された数をリストprediction に格納する。
    prediction = list()
    for i in range(3):
        prediction.append(int(input('{}桁目の予想を入力（0 ～ 9） >>'.format(i + 1))))
    # 確認用出力
    print(prediction)

    # （4） リストanswer とprediction を比較し、位置と数値が一致する要素と、
    #       位置は異なるが数値が一致する要素を数え、それぞれの結果を「○ヒット！○ボール！」と画面に表示する。
    hit = 0 # ヒットの数
    ball = 0 # ボールの数
    for i in range(3):
        if prediction[i] == answer[i]:
            hit += 1
        else:
            for j in range(3):
                if prediction[i] == answer[j]:
                    ball += 1
        # elif prediction[i] in answer:

    # 確認用出力
    print('hit:{}_ball:{}'.format(hit, ball))

    # （5） 3 ヒットなら続けて画面に「正解です！」と表示してゲームを終了する。
    if hit == 3:
        print('正解です！')
        break

    # （6） それ以外の場合は、「続けますか？ 1：続ける 2：終了 >>」を表示する。
    else:
        input_num = int(input('続けますか？ 1：続ける 2：終了 >>'))

    # （7） 1 を入力されたら（3）に戻る。2 が入力されたら正解を表示してゲームを終了する。
    if input_num == 2:
        break


