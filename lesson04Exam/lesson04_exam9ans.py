import random

result_tpl = ("あいこ", "PCの勝ち", "あなたの勝ち")
hands = ('ぐー', 'ちょき', 'ぱー')
cnt = 1
result_list = [0, 0, 0]
while result_list[1] < 2 and result_list[2] < 2:
    print('第{}回戦：あなたの手を数字で選んでください'.format(cnt))
    user_hand = int(input('>>'))
    pc_hand = random.randint(0, 2)
    print('あなたの手は「' + hands[user_hand] + '」、')
    print('PCの手は「' + hands[pc_hand] + '」。')
    result_num = (user_hand - pc_hand + 3) % 3
    print(result_tpl[result_num])
    result_list[result_num] += 1
    cnt += 1
    # 現状を表示
    print('あなた:{} 勝、PC:{} 勝、あいこ:{} 回'.format(result_list[2], result_list[1], result_list[0]))
    winner = 'PC'
    if result_list[2] == 2:
        winner = 'あなた'
print('ゲーム終了！ 優勝者は{} です。'.format(winner))