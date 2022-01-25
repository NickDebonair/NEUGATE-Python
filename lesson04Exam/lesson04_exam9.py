# 問題9.
# 繰り返しと条件分岐の複合問題_1
#
# 「先に2 勝した方を優勝とする、じゃんけんゲームプログラム」を作成してください。
#
# 実行例
#
# じゃんけんゲーム始めるよー
# PC と勝負です！
# 先に2 勝した方が優勝です！！
# 第1 回戦：あなたの手を数字で選んでください
# 0:ぐー 1:ちょき 2:ぱー
# >>0
# あなたの手は「ぐー」、PC の手は「ちょき」。
# あなたの勝ちです。
# あなた:1 勝、PC:0 勝、あいこ:0 回
# 第2 回戦：あなたの手を数字で選んでください
# 0:ぐー 1:ちょき 2:ぱー
# >>1
# あなたの手は「ちょき」、PC の手は「ぐー」。
# PC の勝ちです。
# あなた:1 勝、PC:1 勝、あいこ:0 回
# 第3 回戦：あなたの手を数字で選んでください
# 0:ぐー 1:ちょき 2:ぱー
# >>2
# あなたの手は「ぱー」、PC の手は「ちょき」。
# PC の勝ちです。
# あなた:1 勝、PC:2 勝、あいこ:0 回
# ゲーム終了！ 優勝者はPC です。
import random


print('じゃんけんゲーム始めるよー')
print('PC と勝負です！')
print('先に2 勝した方が優勝です！！')
user_victory = 0
pc_victory = 0
no_victory = 0
count = 1
hands = ('ぐー', 'ちょき', 'ぱー')
pc_hand = random.randint(0, 2)
while user_victory < 2 and pc_victory < 2:
    print('第{} 回戦：あなたの手を数字で選んでください'.format(count))
    print('0:ぐー 1:ちょき 2:ぱー')
    user_hand = int(input('>>'))

    print('あなたの手は「' + hands[user_hand] + '」、')
    print('PCの手は「' + hands[pc_hand] + '」。')
    result_tpl = ("あいこ", "PCの勝ち", "あなたの勝ち")
    result_num = (user_hand - pc_hand + 3) % 3
    print(result_tpl[result_num])
    if result_num == 1:
        pc_victory += 1
    elif result_num == 2:
        user_victory += 1
    else:
        no_victory += 1
    print('あなた:{} 勝、PC:{} 勝、あいこ:{} 回'.format(user_victory, pc_victory, no_victory))
    count += 1
    press_enter = input('Press Enter')
msg = ''
if user_victory == 2:
    msg = 'あなた'
elif pc_victory == 2:
    msg = 'PC'
print('ゲーム終了！ 優勝者は{} です。'.format(msg))