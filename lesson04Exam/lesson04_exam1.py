# 問題1.
# 条件分岐の応用_1
# 学習してきた条件分岐を使って、じゃんけんゲームを作成してみましょう。（PCの手を、「0,1,2」の中からランダムに決定する方法は検索で調べてみましょう。）
#
# じゃんけんゲームを作成してください。
# ユーザーの手はキーボード入力、PC の手はランダムで決めてください。
#
# 実行例
#
# じゃんけんゲーム始めるよー
# PC と勝負です！
# あなたの手を数字で選んでください
# 0:ぐー 1:ちょき 2:ぱー
# >>1
# あなたの手は「ちょき」、PC の手は「ぐー」。
# PC の勝ちです。
import random
print('じゃんけんゲーム始めるよー')
print('PC と勝負です')
print('あなたの手を数字で選んでください')
print('0:ぐー 1:ちょき 2:ぱー')
your_hand = int(input('>>'))
pc_hand = random.randint(0, 2)
hand_pattern = {0: 'ぐー', 1: 'ちょき', 2: 'ぱー'}
msg = ''
if your_hand == 0 and pc_hand == 1:
    msg = 'あなたの勝ちです。'
elif your_hand == 1 and pc_hand == 2:
    msg = 'あなたの勝ちです。'
elif your_hand == 2 and pc_hand == 0:
    msg = 'あなたの勝ちです。'
elif your_hand == 0 and pc_hand == 2:
    msg = 'PCの勝ちです。'
elif your_hand == 1 and pc_hand == 0:
    msg = 'PCの勝ちです。'
elif your_hand == 2 and pc_hand == 1:
    msg = 'PCの勝ちです。'
elif your_hand == 0 and pc_hand == 0:
    msg = 'おあいこです。。'
elif your_hand == 1 and pc_hand == 1:
    msg = 'おあいこです。。'
elif your_hand == 2 and pc_hand == 2:
    msg = 'おあいこです。。'
print('あなたの手は「' + hand_pattern[your_hand] + '」、PCの手は「' + hand_pattern[pc_hand] + '」。')
print(msg)